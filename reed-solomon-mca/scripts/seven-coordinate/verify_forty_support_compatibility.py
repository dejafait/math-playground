"""Independent incidence/obstruction checker; imports no producer code."""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[2]
SOURCE = Path(__file__).with_name('forty-support-compatibility.json')
OUT = SOURCE.with_name('forty-support-compatibility-verification.json')


def main():
    c = json.loads(SOURCE.read_text())
    failures = []
    checks = 0

    def check(name, actual, expected):
        nonlocal checks
        checks += 1
        if actual != expected:
            failures.append(dict(check=name, actual=actual, expected=expected))

    s = (1,8,12,18,22,27,33)
    j = (47,50,64,70,75,79,85,89,96)
    fixed = [35,522,477,566]
    text = (ROOT/'lemmas/L163-l162-complete-additional-row-parameter-loci.md').read_text()
    b = [int(x) for x in re.findall(r'\d+', re.search(r'B=\{([^}]+)\}', text).group(1))]
    check('S', c['S'], list(s))
    check('J', c['J'], list(j))
    check('fixed labels', c['fixed_labels'], fixed)
    check('complete canonical B', c['candidate_labels'], b)
    check('distinct canonical B', len(set(b)), 40)
    for p, digest in c['source_sha256'].items():
        check('source hash '+p, digest, hashlib.sha256((ROOT/p).read_bytes()).hexdigest())

    # Reconstruct the label table by explicit ordered index loops, independently
    # of the producer's itertools Cartesian enumeration or certificate supports.
    table = []
    for u in range(7):
        for v in range(u+1,7):
            for w in range(9):
                for z in range(w+1,9):
                    table.append(dict(label=len(table), I=[s[u],s[v]], K=[j[w],j[z]],
                                      support=sorted([s[u],s[v],j[w],j[z]])))
    check('full original label count', len(table), 756)
    check('stored label count', c['original_label_count'], 756)
    check('all reconstructed records', c['records'], [table[a] for a in fixed+b])
    labels = fixed+b
    supports = {a: set(table[a]['support']) for a in labels}
    pairs = []
    for n,a in enumerate(labels):
        for d in labels[n+1:]:
            overlap = sorted(supports[a].intersection(supports[d]))
            pairs.append(dict(labels=[a,d], intersection=overlap))
            if a in fixed or d in fixed:
                check(f'fixed-row compatibility {a},{d}', len(overlap) <= 1, True)
    check('all 946 pair intersections', c['pair_intersections'], pairs)
    fd = {str(x): sum(x in supports[a] for a in fixed) for x in s+j}
    bd = {str(x): sum(x in supports[a] for a in b) for x in s+j}
    check('all fixed integer degrees', c['fixed_degrees'], fd)
    check('all candidate-universe integer degrees', c['candidate_universe_degrees'], bd)
    common = [x for x in s+j if all(x in supports[a] for a in b)]
    check('common coordinate exactly 27', common, [27])
    check('stored common coordinates', c['common_candidate_coordinates'], common)
    for a in b:
        check(f'candidate {a} contains 27', 27 in supports[a], True)
    check('fixed coordinate-27 degree', fd['27'], 1)
    expected = dict(coordinate=27, fixed_degree=1, candidate_count=40,
                    requested_additions=8, degree_for_requested_additions=9,
                    required_degree_at_most=4, additions_at_most=3, total_rows_at_most=7)
    check('complete obstruction', c['obstruction'], expected)
    check('strict violated capacity', fd['27']+8 > 4, True)
    check('producer failures', c['failures'], [])
    check('negative decision', c['feasible'], False)
    out = dict(checks=checks, failures=failures, passed=not failures,
               certificate_sha256=hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
               coordinate_27_fixed_degree=fd['27'],
               degree_with_eight_additions=fd['27']+8, required_at_most=4,
               maximum_additions_upper_bound=3, maximum_total_rows_upper_bound=7)
    OUT.write_text(json.dumps(out, indent=2)+'\n')
    print(f'Checks: {checks}; failures: {len(failures)}; all 40 candidates and 4 fixed rows checked')
    print('Eight additions: degree 9 at coordinate 27, required <=4; infeasible')
    print(f'Full verification evidence: {OUT.relative_to(ROOT)}')
    if failures:
        print(failures)
        raise SystemExit(1)


if __name__ == '__main__':
    main()
