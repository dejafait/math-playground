#!/usr/bin/env python3
"""Replay the fixed2167 source; only the two output destinations change."""
from pathlib import Path
import hashlib
import json

root = Path(__file__).resolve().parent
source = root / 'six_endpoint_2167.py'
outdir = root / 'audit2169-replay'
outdir.mkdir(exist_ok=True)
original = source.read_text()
replacements = {
    "OUT = ROOT / 'six_endpoint_2167.json'":
        "OUT = ROOT / 'audit2169-replay' / 'six_endpoint_2167.json'",
    "PREFLIGHT = ROOT / 'six_endpoint_preflight_2167.json'":
        "PREFLIGHT = ROOT / 'audit2169-replay' / 'six_endpoint_preflight_2167.json'",
}
executed = original
for old, new in replacements.items():
    assert executed.count(old) == 1
    executed = executed.replace(old, new)
(outdir / 'provenance.json').write_text(json.dumps({
    'source_sha256': hashlib.sha256(original.encode()).hexdigest(),
    'executed_source_sha256': hashlib.sha256(executed.encode()).hexdigest(),
    'replacements': replacements,
    'purpose': 'Resolve source-to-saved-quadrature/rotation identity; no mathematical or parameter change.',
}, indent=2) + '\n')
exec(compile(executed, str(source), 'exec'), {'__file__': str(source), '__name__': '__main__'})
