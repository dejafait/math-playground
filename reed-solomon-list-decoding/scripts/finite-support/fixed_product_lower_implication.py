"""Bind prior complete evidence and check the 64 reused minimum identities.

This does not reverify the original orbit enumeration or enclose a new root.
The mathematical implication and Boolean cases are proved in L114.
"""
import gzip
import hashlib
import json
from fractions import Fraction as F
from math import comb
from pathlib import Path

B = Path(__file__).resolve().parent
ROOT = B.parent.parent
OUT = B / 'fixed-product-lower-implication.json'


def read(name):
    path = ROOT / name
    if path.suffix == '.gz':
        with gzip.open(path, 'rt') as stream:
            return json.load(stream)
    return json.loads(path.read_text())


def sha(name):
    return hashlib.sha256((ROOT / name).read_bytes()).hexdigest()


def main():
    base = 'scripts/finite-support/'
    names = [base + s for s in (
        'fixed-pair-row-capacity-results.json',
        'fixed-pair-row-capacity-verification.json',
        'positive-factor-enclosure.json.gz',
        'enclosed-root-all-capacities-verification.json',
        'l112-l113-critical-audit.json', 'delsarte-lp-results.json')]
    row, rv, root, upper, audit, lp = map(read, names)
    report = dict(stage='in_progress', failures=[], checks=0,
                  input_sha256={p: sha(p) for p in names}, rows=[])

    def ck(name, condition):
        report['checks'] += 1
        if not condition:
            report['failures'].append(name)

    ck('prior_complete_evidence', row['stage'] == 'complete' and rv['verified']
       and audit['stage'] == upper['stage'] == 'verified'
       and all(not r['failures'] for r in (row, rv, audit, upper)))
    ck('row_verifier_binding', rv['construction_sha256'] == sha(names[0]))
    for source in (row, audit):
        for path, expected in source['input_sha256'].items():
            ck('unchanged:' + path, sha(path) == expected)
    N = 65537**28 // 2**128 + 1
    U = F(comb(1024, 64), comb(68, 64))
    a = [F(z['numerator'], z['denominator']) for z in lp['exact']['primal']]
    c = [F(1)] + [F(0)]*4 + [
        (N-1)*a[i-5]/((U-1)*comb(68, i)*comb(956, i)) for i in range(5, 69)]
    q = row['denominator']
    ck('identical_pairs_and_N', N == row['N'] == root['N']
       and c == [F(p, q) for p in row['pair_numerators']]
       == [F(*p) for p in root['c']])
    ck('complete_rows', len(row['rows']) == 69)
    ck('Boolean_pair_range', all(0 <= p <= 1 for p in c))
    for i in range(5, 69):
        r = row['rows'][i]
        ck('minimum_identity:' + str(i), r['i'] == i
           and F(r['lower_numerator'], q) == 2*c[i]
           and r['repetitions'] == [[0, 0, 0, 1], [i, i, i, 1]])
        report['rows'].append(dict(i=i, pair=[c[i].numerator, c[i].denominator],
                                  minimum_numerator=r['lower_numerator'], denominator=q,
                                  distinct_lower_sum=0, required_distinct_lower_sum=0))
    report.update(stage='verified' if not report['failures'] else 'failed',
                  scope='Binding and reused row identities only; full case proof in L114.',
                  required_minimum_identity='L_i=2*c_i for every i=5,...,68',
                  code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    OUT.write_text(json.dumps(report, indent=2) + '\n')
    print('stage:', report['stage'], 'checks:', report['checks'],
          'identities:', len(report['rows']), 'failures:', len(report['failures']))
    print('actual distinct lower sums: 0; required: 0; certificate:', OUT)
    if report['failures']:
        print('failures:', report['failures'])
        raise SystemExit(1)


if __name__ == '__main__':
    main()
