"""Freeze the authoritative worksheet and its mapped blank reading forms, offline."""
import argparse
import hashlib
import json
from pathlib import Path
import re

from annotation_pipeline.runner import validate_scope

ROOT = Path(__file__).resolve().parents[1]
WORKSHEET = Path('candidate_screening/human_annotation.md')


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def blocks(text):
    parts = re.split(r'^### (R\d{3})\s*$', text, flags=re.M)
    result = {}
    for index in range(1, len(parts), 2):
        key = parts[index]
        if key in result:
            raise ValueError(f'Duplicate worksheet entry {key}')
        result[key] = parts[index + 1]
    return parts[0].strip(), result


def content(block):
    requirement = re.search(r'^\*\*Requirement:\*\* (.+)$', block, re.M)
    propositions = re.search(r'\*\*Proposition definitions:\*\*\n\n(.*?)(?=\n\n)', block, re.S)
    if not requirement or not propositions:
        raise ValueError('Missing worksheet requirement/propositions')
    pairs = re.findall(r'^- ([^:]+): (.+)$', propositions[1], re.M)
    if not pairs or len(dict(pairs)) != len(pairs):
        raise ValueError('Invalid worksheet propositions')
    return requirement[1], dict(pairs)


def build_scope(root=ROOT):
    root = Path(root)
    source = root / WORKSHEET
    text = source.read_text(encoding='utf-8')
    main, mapping_text = text.split('<!--\nAdministrative mapping for reproducibility: source family / annotation ID -> review ID.\n')
    mapping_body, suffix = mapping_text.split('-->')
    if suffix.strip():
        raise ValueError('Unexpected text after administrative mapping')
    mappings = []
    for line in mapping_body.strip().splitlines():
        match = re.fullmatch(r'([A-Za-z0-9_-]+) / (item_\d{4}) -> (R\d{3})', line)
        if not match or match[1] == 'trigger_scope':
            raise ValueError('Invalid administrative mapping')
        mappings.append(match.groups())
    if len(mappings) != 88 or len({m[2] for m in mappings}) != 88 or len({m[:2] for m in mappings}) != 88:
        raise ValueError('Expected 88 unique administrative mappings')
    intro, stages = main.split('## Stage 1 — Open interpretations\n', 1)
    first, second = stages.split('## Stage 2 — Proposed reading assessment\n')
    first, stop = first.split('---\n\n## STOP — Complete all Stage 1 entries before proceeding')
    if stop.strip():
        raise ValueError('Unexpected stage separator')
    first_header, stage1 = blocks(first)
    second_header, stage2 = blocks(second)
    expected = [f'R{i:03d}' for i in range(1, 89)]
    if list(stage1) != expected or list(stage2) != expected or [m[2] for m in mappings] != expected:
        raise ValueError('Worksheet/mapping order or coverage mismatch')
    # Preserve instructions verbatim, including the reusable per-entry response prompts.
    stage1_prompt = stage1['R001'].split('**Your interpretations:**', 1)[1].strip()
    stage2_prompt = stage2['R001'].split('Additional interpretations', 1)[1].strip()
    scope = {'source_sha256': sha256(source), 'source_files_sha256': {},
             'stage1_instructions': intro.strip() + '\n\n## Stage 1 — Open interpretations\n\n' + first_header + '\n\n**Your interpretations:**\n\n' + stage1_prompt,
             'stage2_instructions': '## Stage 2 — Proposed reading assessment\n\n' + second_header + '\n\nAdditional interpretations ' + stage2_prompt,
             'entries': []}
    forms = {}
    for family, annotation_id, review_id in mappings:
        if family not in forms:
            directory = root / 'candidate_screening' / family
            paths = sorted(directory.glob('*_reading_assessment.jsonl'))
            if len(paths) != 1:
                raise ValueError(f'Expected one mapped reading form for {family}')
            path = paths[0]
            rows = [json.loads(line) for line in path.read_text(encoding='utf-8').splitlines()]
            by_id = {}
            for row in rows:
                if row['annotation_id'] in by_id:
                    raise ValueError('Duplicate blank annotation ID')
                readings = row['readings']
                ids = [r['reading_id'] for r in readings]
                if (row['annotator_id'] is not None or row['comments'] != '' or row['additional_interpretations'] != []
                        or row['supports'] != dict.fromkeys(ids) or len(ids) != len(set(ids))
                        or any(set(r) != {'reading_id', 'plain'} for r in readings)):
                    raise ValueError('Source reading assessment is not a blank form')
                by_id[row['annotation_id']] = row
            forms[family] = by_id
            scope['source_files_sha256'][path.relative_to(root).as_posix()] = sha256(path)
        row = forms[family][annotation_id]
        for stage in (stage1, stage2):
            if content(stage[review_id]) != (row['requirement'], row['propositions']):
                raise ValueError(f'Worksheet requirement/propositions mismatch: {review_id}')
        proposed = stage2[review_id].split('**Proposed readings:**\n', 1)[1].split('Additional interpretations', 1)[0]
        readings = re.findall(r'^(\d+)\. (.+)$', proposed, re.M)
        if [int(n) for n, _ in readings] != list(range(1, len(readings) + 1)) or [plain for _, plain in readings] != [r['plain'] for r in row['readings']]:
            raise ValueError(f'Worksheet proposed readings mismatch: {review_id}')
        entry = {'review_id': review_id, 'annotation_id': annotation_id, 'source_family': family,
                 'requirement': row['requirement'], 'propositions': row['propositions'], 'readings': row['readings']}
        if 'scenario' in row:
            entry['scenario'] = row['scenario']
        scope['entries'].append(entry)
    validate_scope(scope)
    return scope


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--run-dir', required=True, type=Path)
    args = parser.parse_args()
    scope = build_scope()
    output = args.run_dir / 'scope.json'
    data = json.dumps(scope, ensure_ascii=False, indent=2) + '\n'
    if output.exists() and output.read_text(encoding='utf-8') != data:
        parser.error('Refusing to replace a different frozen scope')
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(data, encoding='utf-8')
    print(f'Prepared {len(scope["entries"])} entries: {output}')


if __name__ == '__main__':
    main()
