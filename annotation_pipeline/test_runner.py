import json
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
                'supported_parameters': []} for m in r.MODELS]}).encode(), {}
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


if __name__ == '__main__':
    unittest.main()
