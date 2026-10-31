"""Write which sampled formulas spot groups together, per item, to a text file per input.

Run:  python test_groups.py "raw_samples/raw_samples*.json" [out_dir]
  or: pytest test_groups.py   (env GROUPS_GLOB, GROUPS_OUT)
Output: <out_dir>/groups_<input stem>.txt  (default out_dir: groups)
"""
import glob
import json
import os
import sys
from collections import Counter
from pathlib import Path

from analyze_correlation import cluster, equivalent, formula_of, NOT_EXPRESSIBLE

DEFAULT_GLOB = "raw_samples/raw_samples*.json"
DEFAULT_OUT = "groups"


def render(path):
    """Text report of the equivalence classes for one samples file."""
    data = json.load(open(path, encoding="utf-8"))
    lines = [f"{path}"]
    for k, item in data.items():
        fs = [formula_of(s) for s in item["samples"]]
        labels = cluster(fs)
        assert len(labels) == len(fs)
        gold = item.get("ltl")
        lines += ["", f"[{k}] {item['nl']}", f"    gold: {gold}"]
        groups = {}
        for f, lab in zip(fs, labels):
            groups.setdefault(lab, []).append(f)
        for lab, members in sorted(groups.items(), key=lambda kv: -len(kv[1])):
            if lab == NOT_EXPRESSIBLE:
                title = "UNPARSEABLE"
            else:
                title = "matches gold" if gold and equivalent(members[0], gold) else "differs from gold"
            lines.append(f"  class {lab} x{len(members)} ({title})")
            lines += [f"      {c:2d}x  {f}" for f, c in Counter(members).most_common()]
    return "\n".join(lines) + "\n"


def write_all(pattern, out_dir):
    paths = sorted(glob.glob(pattern))
    assert paths, f"no files match {pattern!r}"
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    outs = []
    for p in paths:
        out = out_dir / f"groups_{Path(p).stem}.txt"
        out.write_text(render(p), encoding="utf-8")
        outs.append(out)
        print("wrote", out)
    return outs


def test_groups():
    outs = write_all(os.environ.get("GROUPS_GLOB", DEFAULT_GLOB), os.environ.get("GROUPS_OUT", DEFAULT_OUT))
    assert all(o.stat().st_size > 0 for o in outs)


if __name__ == "__main__":
    write_all(sys.argv[1] if len(sys.argv) > 1 else DEFAULT_GLOB,
              sys.argv[2] if len(sys.argv) > 2 else DEFAULT_OUT)