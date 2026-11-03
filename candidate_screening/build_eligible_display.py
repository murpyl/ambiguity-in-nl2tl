#!/usr/bin/env python3
"""Build the standalone eligible-candidate reading view (Python standard library only)."""

import html
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "eligible_combined.html"


def escape(value):
    return html.escape(str(value), quote=True)


def render(value):
    """Render arbitrary JSON recursively, preserving keys, order, and scalar types."""
    if isinstance(value, dict):
        if not value:
            return '<span class="literal">{}</span>'
        return '<dl class="fields">' + "".join(
            f'<div><dt>{escape(key)}</dt><dd>{render(item)}</dd></div>'
            for key, item in value.items()
        ) + '</dl>'
    if isinstance(value, list):
        if not value:
            return '<span class="literal">[]</span>'
        return '<ol class="values">' + "".join(
            f'<li>{render(item)}</li>' for item in value
        ) + '</ol>'
    if value is None or isinstance(value, (bool, int, float)):
        return f'<code class="literal">{escape(json.dumps(value))}</code>'
    if value == "":
        return '<span class="literal">"" (empty string)</span>'
    return f'<span class="text">{escape(value)}</span>'


def readings_table(readings):
    if not isinstance(readings, list) or not readings or not all(
        isinstance(reading, dict) for reading in readings
    ):
        return render(readings)
    columns = list(dict.fromkeys(key for reading in readings for key in reading))
    if not columns:
        return render(readings)
    return (
        '<div class="table-scroll"><table><thead><tr>'
        + ''.join(f'<th scope="col">{escape(key)}</th>' for key in columns)
        + '</tr></thead><tbody>'
        + ''.join(
            '<tr>' + ''.join(
                f'<td class="{ "formula" if key == "ltl" else "" }">'
                + (render(reading[key]) if key in reading else '<span class="missing">— (absent)</span>')
                + '</td>' for key in columns
            ) + '</tr>' for reading in readings
        )
        + '</tbody></table></div>'
    )


def card(record, source, line, number):
    sections = []
    for key, value in record.items():
        if key == 'ambiguous_text':
            continue
        if key in ('item_id', 'family_id', 'contrast_id'):
            continue
        body = readings_table(value) if key == 'readings' else render(value)
        sections.append(f'<section class="field-section"><h3>{escape(key)}</h3>{body}</section>')
    metadata = {key: record[key] for key in ('item_id', 'family_id', 'contrast_id') if key in record}
    searchable = json.dumps(record, ensure_ascii=False) + ' ' + source
    ambiguous = render(record['ambiguous_text']) if 'ambiguous_text' in record else '<span class="missing">No ambiguous_text field</span>'
    return f'''<article class="candidate" id="candidate-{number}" data-source="{escape(source)}" data-search="{escape(searchable.lower())}">
      <div class="card-top"><a class="number" href="#candidate-{number}">#{number:03d}</a><span class="provenance">{escape(source)} · line {line}</span></div>
      <h2><span class="eyebrow">ambiguous_text</span>{ambiguous}</h2>
      <div class="metadata">{render(metadata)}</div>
      {''.join(sections)}
    </article>'''


STYLE = """
:root{color-scheme:light;--ink:#1e303b;--muted:#576d78;--line:#d9e2e5;--accent:#18655c;--paper:#fff;--wash:#f2f6f5}
*{box-sizing:border-box}body{margin:0;background:var(--wash);color:var(--ink);font:16px/1.6 system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}
main,header>div{max-width:1180px;margin:auto;padding:0 32px}header{background:#173b39;color:#fff;padding:45px 0 36px}header p{max-width:780px;color:#d7e7e2;margin:12px 0 0}h1{font-size:clamp(30px,4vw,46px);letter-spacing:-1.3px;margin:0;line-height:1.15}.eyebrow{display:block;font:600 11px/1.6 system-ui,sans-serif;text-transform:uppercase;letter-spacing:1.6px;color:var(--muted);margin-bottom:8px}header .eyebrow{color:#a8d5c7}
.controls{display:grid;grid-template-columns:minmax(220px,1fr) minmax(220px,1fr) auto;gap:16px;align-items:end;padding:26px 0 16px}label{display:block;font-weight:650;font-size:13px}input,select,button{font:inherit;border:1px solid #aebfbe;border-radius:7px;background:#fff;color:var(--ink);padding:10px 12px;width:100%;margin-top:6px}button{cursor:pointer}input:focus-visible,select:focus-visible,button:focus-visible,a:focus-visible{outline:3px solid #218b78;outline-offset:3px}.results{color:var(--muted);font-size:14px;margin:0 0 22px}.candidate{background:var(--paper);border:1px solid var(--line);border-radius:12px;margin:0 0 28px;padding:26px 30px;box-shadow:0 3px 10px #153c3610;scroll-margin-top:20px}.card-top{display:flex;gap:15px;align-items:baseline}.number{font:650 13px ui-monospace,monospace;color:var(--accent);text-decoration:none}.provenance{font:12px/1.6 ui-monospace,monospace;color:var(--muted);overflow-wrap:anywhere}h2{font-size:25px;line-height:1.4;letter-spacing:-.4px;margin:23px 0 20px;font-weight:600}h3{font-size:12px;color:var(--accent);letter-spacing:.7px;margin:0 0 9px;font-weight:700}.metadata{background:#f3f7f6;border-radius:7px;padding:12px 16px}.metadata>.fields{display:flex;flex-wrap:wrap;gap:12px 30px}.metadata>.fields>div{display:block}.field-section{margin-top:22px}.fields{margin:0}.fields>div{display:grid;grid-template-columns:minmax(100px,170px) minmax(0,1fr);gap:6px 18px;padding:7px 0;border-bottom:1px solid #edf1f1}.fields>div:last-child{border:0}dt{font:600 12px/1.8 ui-monospace,monospace;color:var(--muted);overflow-wrap:anywhere}dd{margin:0;min-width:0}.text{white-space:pre-wrap;overflow-wrap:anywhere}.literal,.missing{font:13px ui-monospace,monospace;color:#68767d}.values{margin:0;padding-left:25px}.values>li{padding:5px 0 5px 5px}.table-scroll{overflow-x:auto}table{border-collapse:collapse;width:100%;font-size:14px;table-layout:auto}th{background:#edf4f2;font:600 12px ui-monospace,monospace;text-align:left;padding:10px 12px;color:#395b53}td{padding:13px 12px;vertical-align:top;border-bottom:1px solid var(--line);min-width:90px;overflow-wrap:anywhere}td.formula{font:13px/1.6 ui-monospace,monospace;min-width:150px;color:#19594c}td:first-child{min-width:70px}footer{font-size:13px;color:var(--muted);padding:0 0 30px}.empty{padding:30px;border:1px dashed #aebfbe;border-radius:10px;text-align:center}[hidden]{display:none!important}
@media(max-width:700px){main,header>div{padding:0 16px}header{padding:30px 0}.controls{grid-template-columns:1fr}.candidate{padding:20px 17px}h2{font-size:22px}.card-top{flex-wrap:wrap;gap:4px 12px}.fields>div{grid-template-columns:1fr;gap:2px}.metadata>.fields{gap:10px 20px}td{min-width:180px}td:first-child{min-width:65px}}
@media print{body{background:#fff;font-size:10pt}header{background:#fff;color:#173b39;padding:0 0 20px}header p,header .eyebrow{color:#576d78}main,header>div{max-width:none;padding:0}.controls,.results,footer{display:none}.candidate{box-shadow:none;border-radius:0;margin-bottom:20px;padding:16px;break-inside:auto}h2{font-size:16pt;break-after:avoid}.field-section{break-inside:avoid}table{font-size:9pt}thead{display:table-header-group}tr{break-inside:avoid}.table-scroll{overflow:visible}.provenance{font-size:8pt}a{color:inherit;text-decoration:none}}
"""

SCRIPT = """
const search = document.querySelector('#search');
const source = document.querySelector('#source');
const cards = [...document.querySelectorAll('.candidate')];
function filter() {
  const terms = search.value.toLowerCase().trim().split(/\\s+/).filter(Boolean);
  let visible = 0;
  for (const card of cards) {
    const matches = (!source.value || card.dataset.source === source.value)
      && terms.every(term => card.dataset.search.includes(term));
    card.hidden = !matches;
    if (matches) visible++;
  }
  document.querySelector('#count').textContent = `${visible} of ${cards.length} records shown`;
  document.querySelector('#empty').hidden = visible !== 0;
}
search.addEventListener('input', filter);
source.addEventListener('change', filter);
document.querySelector('#reset').addEventListener('click', () => {
  search.value = ''; source.value = ''; filter(); search.focus();
});
"""


def main():
    sources = []
    cards = []
    # Match the complete stem suffix, so the output and generator never match.
    for path in sorted(ROOT.rglob('*')):
        if not path.is_file() or not path.stem.endswith('_eligible'):
            continue
        source = path.relative_to(ROOT).as_posix()
        count = 0
        for line_number, line in enumerate(path.read_text(encoding='utf-8').splitlines(), 1):
            if not line.strip():
                continue
            try:
                record = json.loads(line)
            except json.JSONDecodeError as error:
                raise ValueError(f'{source}:{line_number}: {error}') from error
            if not isinstance(record, dict):
                raise ValueError(f'{source}:{line_number}: expected a JSON object')
            cards.append(card(record, source, line_number, len(cards) + 1))
            count += 1
        sources.append((source, count))
    if not sources:
        raise ValueError('No files with stems ending in _eligible found')
    options = ''.join(f'<option value="{escape(source)}">{escape(source)} ({count})</option>' for source, count in sources)
    document = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Eligible candidates · Combined reading view</title><style>{STYLE}</style></head>
<body><header><div><span class="eyebrow">Candidate screening · Reading view</span><h1>Eligible candidates</h1><p>{len(cards)} records across {len(sources)} source files. Compare interpretations, formulas, and screening evidence. Every original field is included; source paths distinguish the original and final trigger-scope sets.</p></div></header>
<main><div class="controls"><label for="search">Search every field<input id="search" type="search" placeholder="Text, formula, ID, or solver witness…"></label><label for="source">Source file<select id="source"><option value="">All {len(sources)} source files</option>{options}</select></label><button id="reset" type="button">Reset filters</button></div>
<p class="results" id="count" role="status" aria-live="polite">{len(cards)} of {len(cards)} records shown</p><noscript><p>All records are visible. Enable JavaScript to search and filter.</p></noscript><p class="empty" id="empty" hidden>No records match these filters.</p>
{''.join(cards)}
<footer>Generated by build_eligible_display.py · Sources are relative to candidate_screening/ · Print uses the current filtered selection. Screening results are reproduced from the source files.</footer></main><script>{SCRIPT}</script></body></html>
'''
    OUTPUT.write_text(document, encoding='utf-8')
    for source, count in sources:
        print(f'{count:3}  {source}')
    print(f'Wrote {OUTPUT}: {len(cards)} records from {len(sources)} files')


if __name__ == '__main__':
    main()
