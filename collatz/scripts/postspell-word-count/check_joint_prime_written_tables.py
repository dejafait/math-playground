#!/usr/bin/env python3
"""Transcription check of L060's complete two tables, not a critical audit."""
from pathlib import Path
import json
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
OUT = HERE / 'joint-prime-written-table-check.json'
PROOF = ROOT / 'lemmas/L060-two-transposition-joint-prime-nonvanishing-stop.md'
CERT = HERE / 'joint-prime-two-transposition-certificate.json'


def main():
    text = PROOF.read_text()
    cert = json.loads(CERT.read_text())
    checks, failures = [], []
    for m, expected_sum in ((5, 45), (431, 6034)):
        part = text.split(f'Modulo {m}:\n', 1)[1].split('\n\nThe contribution sums', 1)[0]
        if m == 5:
            part = part.split('Modulo 431:', 1)[0]
        written = [list(map(int, row)) for row in
                   re.findall(r'^\|(\d+)\|(\d+)\|(\d+)\|(\d+)\|(\d+)\|(\d+)\|(\d+)\|$', part, re.M)]
        evidence = cert['witness_evidence'][str(m)]
        required = [[r['position'], r['index'], r['closed_triple'][1],
                     r['prefix_two'], r['suffix_three'], r['term'], r['resulting_triple'][1]]
                    for r in evidence['trace']]
        for name, actual, wanted in [
            (f'm={m}: all written entries', written, required),
            (f'm={m}: table size', len(written), 25),
            (f'm={m}: intact multiplicities', sorted(r[1] for r in written), list(range(25))),
            (f'm={m}: term sums', [sum(r[5] for r in written), evidence['term_sum']], [expected_sum]*2),
            (f'm={m}: common zeros', [sum(r[5] for r in written) % m, written[-1][6], evidence['delta']], [0, 0, 0])
        ]:
            record = dict(name=name, actual=actual, required=wanted)
            checks.append(record)
            if actual != wanted:
                failures.append(record)
    OUT.write_text(json.dumps(dict(checks=checks, failures=failures), indent=2)+'\n')
    print(f'Written-table checks: {len(checks)}; failures: {len(failures)}; actual/required rows: 25/25 at each modulus.')
    print('Certificate: scripts/postspell-word-count/'+OUT.name)
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
