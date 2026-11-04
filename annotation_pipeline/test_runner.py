import json
import copy
import io
import urllib.error
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from annotation_pipeline import runner as r


def fixture():
    return {'stage1_instructions': 'List every plausible interpretation independently.',
            'stage2_instructions': 'Assess the proposed readings.',
            'entries': [{'review_id': f'R{i:03}', 'annotation_id': f'item_{i:04}',
                         'source_family': 'trigger_scope_final', 'requirement': f'If p then q {i}',
                         'propositions': {'p': 'p occurs', 'q': 'q occurs'},
                         'readings': [{'reading_id': 'a', 'plain': 'SECRET_PROPOSED_READING'}]}
                        for i in range(88)]}


def answers(scope, stage):
    return {'entries': [{'review_id': e['review_id'], 'comments': '',
                         **({'interpretations': ['Meaning']} if stage == 1 else {
                             'supports': {'a': 'Supported'}, 'additional_interpretations': []})}
                        for e in scope['entries']]}


class RunnerTests(unittest.TestCase):
    def setUp(self):
        self.scope = fixture()
        self.config = {'expected_models': r.MODELS, 'max_output_tokens': 60000,
                       'temperature': 0, 'timeout_seconds': 1}
        self.calls = []

    def transport(self, method, endpoint, key=None, payload=None, timeout=60):
        if endpoint == '/models':
            return json.dumps({'data': [{'id': m, 'context_length': 1000000,
                'top_provider': {'max_completion_tokens': 100000},
                'supported_parameters': ['temperature']} for m in r.MODELS]}).encode(), {}
        self.calls.append(payload)
        stage = 1 if len(payload['messages']) == 1 else 2
        data = answers(self.scope, stage)
        return json.dumps({'model': payload['model'], 'id': 'test', 'usage': {'cost': 0},
                           'choices': [{'finish_reason': 'stop', 'message': {'content': json.dumps(data)}}]}).encode(), {}

    def test_full_mock_run_and_resume_never_repeats_success(self):
        with tempfile.TemporaryDirectory() as tmp, patch.dict(os.environ, {'OPENROUTER_API_KEY': 'test'}):
            run = Path(tmp)
            r.annotate(run, self.scope, self.config, self.transport)
            self.assertEqual(len(self.calls), 10)
            for payload in self.calls[::2]:
                self.assertNotIn('SECRET_PROPOSED_READING', json.dumps(payload))
            for index, payload in enumerate(self.calls[1::2]):
                content = payload['messages'][1]['content']
                self.assertEqual(json.loads(content), answers(self.scope, 1))
            before = {p: p.read_bytes() for p in run.glob('*/stage1.*')}
            r.annotate(run, self.scope, self.config, self.transport)
            self.assertEqual(len(self.calls), 10)
            self.assertTrue(all(p.read_bytes() == data for p, data in before.items()))
            self.assertEqual(len(list(run.glob('*/worksheet.md'))), 5)

    def test_failure_pauses_globally_and_preserves_response(self):
        original = self.transport
        def bad(*args, **kwargs):
            raw, headers = original(*args, **kwargs)
            if args[1] == '/chat/completions':
                data = json.loads(raw)
                data['choices'][0]['finish_reason'] = 'length'
                raw = json.dumps(data).encode()
            return raw, headers
        with tempfile.TemporaryDirectory() as tmp, patch.dict(os.environ, {'OPENROUTER_API_KEY': 'test'}):
            run = Path(tmp)
            with self.assertRaises(ValueError):
                r.annotate(run, self.scope, self.config, bad)
            self.assertEqual(len(self.calls), 1)
            self.assertEqual(r.read(run / 'state.json')['status'], 'paused')
            self.assertEqual(len(list(run.glob('*/*.response.md'))), 1)
            with self.assertRaisesRegex(ValueError, 'authorize-resume'):
                r.annotate(run, self.scope, self.config, original)
            self.assertEqual(len(self.calls), 1)

    def test_interrupted_unknown_request_is_never_repeated(self):
        def interrupted(*args, **kwargs):
            if args[1] == '/chat/completions':
                self.calls.append(kwargs)
                raise KeyboardInterrupt()
            return self.transport(*args, **kwargs)
        with tempfile.TemporaryDirectory() as tmp, patch.dict(os.environ, {'OPENROUTER_API_KEY': 'test'}):
            run = Path(tmp)
            with self.assertRaises(KeyboardInterrupt):
                r.annotate(run, self.scope, self.config, interrupted)
            self.assertEqual(r.read(run / 'state.json')['status'], 'in_flight')
            with self.assertRaisesRegex(ValueError, 'Unknown in-flight'):
                r.annotate(run, self.scope, self.config, interrupted, resume=True)
            self.assertEqual(len(self.calls), 1)

    def test_validation_and_catalog_preflight(self):
        data = answers(self.scope, 1)
        data['entries'][-1] = data['entries'][0]
        with self.assertRaises(ValueError):
            r.validate(data, self.scope['entries'], 1)
        with tempfile.TemporaryDirectory() as tmp:
            def empty(*args):
                return b'{"data": []}', {}
            with self.assertRaisesRegex(ValueError, 'Unavailable'):
                r.preflight(Path(tmp), self.scope, self.config, empty)
        self.assertEqual(self.calls, [])

    def test_unsupported_temperature_blocks_all_paid_calls(self):
        unsupported = [r.MODELS[1], r.MODELS[2]]
        def catalog_without_temperature(*args, **kwargs):
            raw, headers = self.transport(*args, **kwargs)
            catalog = json.loads(raw)
            for model in catalog['data']:
                if model['id'] in unsupported:
                    model['supported_parameters'] = []
            return json.dumps(catalog).encode(), headers
        with tempfile.TemporaryDirectory() as tmp, patch.dict(os.environ, {'OPENROUTER_API_KEY': 'test'}):
            run = Path(tmp)
            with self.assertRaisesRegex(ValueError, 'Configured temperature') as caught:
                r.annotate(run, self.scope, self.config, catalog_without_temperature)
            for model in unsupported:
                self.assertIn(model, str(caught.exception))
            self.assertEqual(self.calls, [])
            self.assertEqual(r.read(run / 'state.json')['status'], 'paused')
            self.assertEqual(r.read(run / 'state.json')['attempts'], [])


    def test_authorized_temperature_omission_full_mock_run(self):
        omitted = [r.MODELS[1], r.MODELS[2]]
        self.config['omit_temperature_models'] = omitted
        def catalog_without_temperature(*args, **kwargs):
            raw, headers = self.transport(*args, **kwargs)
            if args[1] == '/models':
                catalog = json.loads(raw)
                for model in catalog['data']:
                    if model['id'] in omitted:
                        model['supported_parameters'] = []
                raw = json.dumps(catalog).encode()
            return raw, headers
        with tempfile.TemporaryDirectory() as tmp, patch.dict(os.environ, {'OPENROUTER_API_KEY': 'test'}):
            run = Path(tmp)
            r.annotate(run, self.scope, self.config, catalog_without_temperature)
            self.assertEqual(len(self.calls), 10)
            budgets = r.read(run / 'preflight.json')['budgets']
            for payload in self.calls:
                expected = {'max_tokens': 60000}
                if payload['model'] not in omitted:
                    expected['temperature'] = 0
                self.assertEqual({k: payload[k] for k in ('max_tokens', 'temperature') if k in payload}, expected)
                self.assertEqual(budgets[payload['model']]['generation_settings'], expected)
            self.assertEqual(r.read(run / 'state.json')['status'], 'annotations_complete')
            r.annotate(run, self.scope, self.config, catalog_without_temperature)
            self.assertEqual(len(self.calls), 10)

    def test_invalid_temperature_omission_blocks_calls(self):
        for invalid in ('anthropic/claude-haiku-5.5', [r.MODELS[1], r.MODELS[1]], ['unknown/model'], [None]):
            with self.subTest(invalid=invalid), tempfile.TemporaryDirectory() as tmp:
                config = {**self.config, 'omit_temperature_models': invalid}
                with self.assertRaisesRegex(ValueError, 'omit_temperature_models'):
                    r.annotate(Path(tmp), self.scope, config, self.transport)
                self.assertEqual(self.calls, [])


    def test_compact_stage2_schema_and_exact_local_validation(self):
        scope = r.read(Path(__file__).resolve().parents[1] / 'annotation_runs/five_model_v1/scope.json')
        compact = r.schema(2, scope['entries'])
        self.assertLess(len(json.dumps(compact).encode()), 2000)
        self.assertEqual(compact, r.schema(2, scope['entries'][:1]))
        row_schema = compact['properties']['entries']['items']
        self.assertNotIn('anyOf', row_schema)
        self.assertEqual(row_schema['properties']['review_id'], {'type': 'string'})
        self.assertEqual(set(row_schema['properties']['supports']['required']), {'a', 'b'})
        valid = {'entries': [{'review_id': entry['review_id'], 'comments': '',
                             'supports': {'a': 'Supported', 'b': 'Not supported'},
                             'additional_interpretations': []} for entry in scope['entries']]}
        self.assertIs(r.validate(valid, scope['entries'], 2), valid)
        for mutation in ('missing', 'extra', 'duplicate', 'unknown', 'missing_reading', 'extra_reading', 'invalid_label'):
            with self.subTest(mutation=mutation):
                invalid = copy.deepcopy(valid)
                if mutation == 'missing':
                    invalid['entries'].pop()
                elif mutation == 'extra':
                    invalid['entries'].append(copy.deepcopy(invalid['entries'][0]))
                elif mutation == 'duplicate':
                    invalid['entries'][-1] = copy.deepcopy(invalid['entries'][0])
                elif mutation == 'unknown':
                    invalid['entries'][0]['review_id'] = 'UNKNOWN'
                elif mutation == 'missing_reading':
                    invalid['entries'][0]['supports'].pop('b')
                elif mutation == 'extra_reading':
                    invalid['entries'][0]['supports']['c'] = 'Supported'
                else:
                    invalid['entries'][0]['supports']['a'] = 'INVALID'
                with self.assertRaises(ValueError):
                    r.validate(invalid, scope['entries'], 2)
        # Shared grammar shapes do not weaken per-review reading-key validation.
        varied = copy.deepcopy(self.scope)
        varied['entries'][0]['readings'][0]['reading_id'] = 'b'
        grammar = r.schema(2, varied['entries'])
        supports = grammar['properties']['entries']['items']['properties']['supports']
        self.assertEqual(len(supports['anyOf']), 2)
        with self.assertRaisesRegex(ValueError, 'reading assessments'):
            r.validate(answers(varied, 2), varied['entries'], 2)

    def test_resume_after_stage2_grammar_failure_preserves_three_successes(self):
        def grammar_failure(*args, **kwargs):
            raw, headers = self.transport(*args, **kwargs)
            if args[0] == 'POST' and len(self.calls) == 4:
                raise urllib.error.HTTPError('https://example.invalid', 400, 'Bad Request', {},
                    io.BytesIO(b'{"error":{"message":"The compiled grammar is too large"}}'))
            return raw, headers
        with tempfile.TemporaryDirectory() as tmp, patch.dict(os.environ, {'OPENROUTER_API_KEY': 'test'}):
            run = Path(tmp)
            with self.assertRaises(urllib.error.HTTPError):
                r.annotate(run, self.scope, self.config, grammar_failure)
            state = r.read(run / 'state.json')
            self.assertEqual([a['status'] for a in state['attempts']], ['validated'] * 3 + ['failed'])
            preserved = {p: p.read_bytes() for p in run.glob('*/stage*') if p.is_file()}
            frozen = (run / r.MODELS[1].replace('/', '_') / 'stage1.content.txt').read_text()
            with self.assertRaisesRegex(ValueError, 'authorize-resume'):
                r.annotate(run, self.scope, self.config, self.transport)
            self.assertEqual(len(self.calls), 4)
            r.annotate(run, self.scope, self.config, self.transport, resume=True)
            self.assertEqual(len(self.calls), 11)
            self.assertEqual(self.calls[4]['model'], r.MODELS[1])
            self.assertEqual(self.calls[4]['messages'][1]['content'], frozen)
            self.assertTrue(all(path.read_bytes() == content for path, content in preserved.items()))
            self.assertEqual(r.read(run / 'state.json')['status'], 'annotations_complete')
            self.assertEqual(len(list(run.glob('*/stage*.success.json'))), 10)


if __name__ == '__main__':
    unittest.main()
