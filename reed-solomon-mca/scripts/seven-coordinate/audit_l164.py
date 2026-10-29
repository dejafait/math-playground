"""Separate complete L164 incidence audit; no producer/verifier imports."""
from pathlib import Path
from collections import Counter
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[2]
BASE = Path(__file__).resolve().parent
OUT = BASE / 'l164-critical-audit.json'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    source = BASE / 'forty-support-compatibility.json'
    verification = BASE / 'forty-support-compatibility-verification.json'
    c = json.loads(source.read_text())
    v = json.loads(verification.read_text())
    checks, failures = [], []

    def check(name, actual, required):
        passed = actual == required
        checks.append(dict(check=name, actual=actual, required=required, passed=passed))
        if not passed:
            failures.append(name)

    s = [1, 8, 12, 18, 22, 27, 33]
    j = [47, 50, 64, 70, 75, 79, 85, 89, 96]
    fixed = [35, 522, 477, 566]
    canonical = ROOT / 'lemmas/L163-l162-complete-additional-row-parameter-loci.md'
    b = [int(x) for x in re.findall(r'\d+', re.search(r'B=\{([^}]+)\}', canonical.read_text()).group(1))]
    check('ordered S', c['S'], s)
    check('ordered J', c['J'], j)
    check('fixed labels', c['fixed_labels'], fixed)
    check('canonical B in full', c['candidate_labels'], b)
    check('forty distinct candidates', [len(b), len(set(b))], [40, 40])
    check('fixed labels excluded', sorted(set(b) & set(fixed)), [])
    check('original label universe size', c['original_label_count'], 756)
    bindings = ['lemmas/L162-explicit-four-row-infinite-family.md', str(canonical.relative_to(ROOT))]
    check('exact source bindings', sorted(c['source_sha256']), sorted(bindings))
    for name in bindings:
        check('source binding ' + name, c['source_sha256'].get(name), digest(ROOT / name))

    # Decode a pair rank by its triangular prefix count, rather than by either
    # earlier script's Cartesian enumeration. This gives every requested row.
    def pair(values, rank):
        n = len(values)
        u = max(u for u in range(n-1) if u*(2*n-u-1)//2 <= rank)
        prefix = u*(2*n-u-1)//2
        return [values[u], values[u+1+rank-prefix]]

    labels = fixed + b
    records = []
    for label in labels:
        ip, kp = pair(s, label//36), pair(j, label%36)
        records.append(dict(label=label, I=ip, K=kp, support=sorted(ip+kp)))
    check('complete 44 records', c['records'], records)
    supports = {r['label']: set(r['support']) for r in records}
    for record in records:
        check('support cardinality ' + str(record['label']), len(record['support']), 4)
    blocks = {}
    for label in b:
        blocks.setdefault(label//36, []).append(label)
    check('all five I-blocks', sorted(blocks), [4, 9, 16, 18, 20])
    check('eight labels in each block', [len(blocks[m]) for m in sorted(blocks)], [8]*5)
    check('five decoded I-pairs', [pair(s, m) for m in sorted(blocks)],
          [[1,27], [8,27], [18,27], [22,27], [27,33]])

    pairs = []
    for n, a in enumerate(labels):
        for d in labels[n+1:]:
            overlap = sorted(supports[a] & supports[d])
            pairs.append(dict(labels=[a,d], intersection=overlap))
            if a in fixed or d in fixed:
                check('fixed compatibility ' + str([a,d]), len(overlap) <= 1, True)
    check('946 complete intersections', len(pairs), 946)
    check('all retained intersections', c['pair_intersections'], pairs)
    fd = Counter(x for a in fixed for x in supports[a])
    bd = Counter(x for a in b for x in supports[a])
    check('all sixteen fixed degrees', c['fixed_degrees'], {str(x): fd[x] for x in s+j})
    check('all sixteen candidate degrees', c['candidate_universe_degrees'], {str(x): bd[x] for x in s+j})
    common = [x for x in s+j if bd[x] == len(b)]
    check('exact common coordinates', common, [27])
    check('stored common coordinates', c['common_candidate_coordinates'], common)
    check('fixed users of 27', [a for a in fixed if 27 in supports[a]], [477])
    for a in b:
        check('candidate contains 27 ' + str(a), 27 in supports[a], True)
    obstruction = dict(coordinate=27, fixed_degree=fd[27], candidate_count=len(b),
                       requested_additions=8, degree_for_requested_additions=fd[27]+8,
                       required_degree_at_most=4, additions_at_most=4-fd[27],
                       total_rows_at_most=4+4-fd[27])
    check('full integer obstruction', c['obstruction'], obstruction)
    check('actual and required degrees', [fd[27]+8, 4], [9,4])
    check('strict violation', fd[27]+8 > 4, True)
    check('producer negative decision', [c['feasible'], c['failures']], [False, []])
    expected_verification = dict(checks=226, failures=[], passed=True,
        certificate_sha256=digest(source), coordinate_27_fixed_degree=1,
        degree_with_eight_additions=9, required_at_most=4,
        maximum_additions_upper_bound=3, maximum_total_rows_upper_bound=7)
    check('complete replay verification record', v, expected_verification)
    out = dict(source_sha256={str(p.relative_to(ROOT)): digest(p)
                             for p in [source, verification, canonical]},
               checks=checks, failures=failures, passed=not failures,
               records=records, pair_intersections=pairs,
               fixed_degrees={str(x): fd[x] for x in s+j},
               candidate_degrees={str(x): bd[x] for x in s+j}, obstruction=obstruction)
    OUT.write_text(json.dumps(out, indent=2)+'\n')
    print(f'Complete audit: {len(checks)} checks; {len(failures)} failures; 44 records, 946 intersections')
    print(f'Actual degree with eight additions: {fd[27]+8}; required <=4; total rows <=7, no attainment claim')
    print(f'Certificate: {OUT.relative_to(ROOT)}')
    if failures:
        print('Failed checks: ' + ', '.join(failures))
        raise SystemExit(1)


if __name__ == '__main__':
    main()
