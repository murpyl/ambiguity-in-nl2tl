"""Offline integrity checks against the actual authoritative worksheet/forms."""
import hashlib
import json
from pathlib import Path
import tempfile
import unittest

from annotation_pipeline.prepare import ROOT, WORKSHEET, build_scope
from annotation_pipeline.runner import messages, validate_scope


class PrepareTests(unittest.TestCase):
    def test_actual_source_integrity_and_isolation(self):
        before = build_scope()
        self.assertEqual(before, build_scope())
        self.assertEqual(len(validate_scope(before)), 88)
        self.assertEqual(before['source_sha256'], hashlib.sha256((ROOT / WORKSHEET).read_bytes()).hexdigest())
        self.assertEqual(len(before['source_files_sha256']), 8)
        for name, digest in before['source_files_sha256'].items():
            self.assertNotIn('/trigger_scope/', name)
            self.assertTrue(name.endswith('_reading_assessment.jsonl'))
            path = ROOT / name
            self.assertEqual(digest, hashlib.sha256(path.read_bytes()).hexdigest())
            rows = {row['annotation_id']: row for row in map(json.loads, path.read_text().splitlines())}
            for entry in before['entries']:
                if entry['source_family'] == path.parent.name:
                    row = rows[entry['annotation_id']]
                    for field in ('requirement', 'propositions', 'readings'):
                        self.assertEqual(entry[field], row[field])
                    self.assertEqual(entry.get('scenario'), row.get('scenario'))
        self.assertIn('Comments are optional.', before['stage1_instructions'])
        self.assertIn('Optional comments:', before['stage2_instructions'])
        self.assertIn('leave empty if none', before['stage2_instructions'])
        first = json.loads(messages(before, 1)[0]['content'].split('\n')[-1])
        self.assertTrue(all('readings' not in row and 'annotation_id' not in row for row in first))

    def test_reject_changed_worksheet_or_nonblank_form(self):
        scope = build_scope()
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            for name in [WORKSHEET.as_posix(), *scope['source_files_sha256']]:
                target = root / name
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes((ROOT / name).read_bytes())
            self.assertEqual(build_scope(root), scope)
            worksheet = root / WORKSHEET
            original = worksheet.read_text()
            worksheet.write_text(original.replace('At least one step has both events.', 'Changed reading.', 1))
            with self.assertRaisesRegex(ValueError, 'proposed readings mismatch'):
                build_scope(root)
            worksheet.write_text(original)
            path = root / next(iter(scope['source_files_sha256']))
            rows = list(map(json.loads, path.read_text().splitlines()))
            rows[0]['supports'][rows[0]['readings'][0]['reading_id']] = 'Supported'
            path.write_text(''.join(json.dumps(row) + '\n' for row in rows))
            with self.assertRaisesRegex(ValueError, 'not a blank form'):
                build_scope(root)


if __name__ == '__main__':
    unittest.main()
