#!/usr/bin/env python3
"""Exact arithmetic and inherited rigidity checks for L129's symbolic audit."""
import hashlib
import itertools
import json
from fractions import Fraction
from pathlib import Path

BASE = Path(__file__).resolve().parent
Q = 137
T = [16, 64, 70, 102, 112, 118, 121]


def main():
    failures = []
    checks = {}

    def check(name, condition):
        checks[name] = bool(condition)
        if not condition:
            failures.append(name)

    names = ['l126-critical-audit.json', 'l125-critical-audit.json',
             'two-core-star-rigidity.json', 'two_core_star_rigidity.py',
             'full-star-thinning-count.json']
    hashes = {n: hashlib.sha256((BASE / n).read_bytes()).hexdigest() for n in names}
    prior = json.loads((BASE / names[0]).read_text())
    rigidity_audit = json.loads((BASE / names[1]).read_text())
    rigidity = json.loads((BASE / names[2]).read_text())
    for name, digest in prior['inputs'].items():
        check('L126 input hash: ' + name, hashes[name] == digest)
    for name, digest in rigidity_audit['inputs'].items():
        check('L125 input hash: ' + name, hashes[name] == digest)
    check('L126 empty failures', prior['failures'] == [])
    check('L125 empty failures', rigidity_audit['failures'] == [])
    check('L126 arithmetic accepted', all(prior['arithmetic_field_checks'].values()))
    check('L126 every rigidity check accepted',
          len(prior['rigidity_record_checks']) == 840 and
          all(all(r['checks'].values()) for r in prior['rigidity_record_checks']))
    records = rigidity['records']
    check('complete equality with L125 records', records == rigidity_audit['records'])
    check('all ordered anchor cases', [(r['removed'], r['anchor_images']) for r in records]
          == [(t, list(ys)) for t in T for ys in itertools.permutations(T[1:], 3)])
    record_checks, accepted = [], []
    for index, r in enumerate(records):
        source = [t for t in T if t != r['removed']]
        a, b, c, d = r['matrix']
        det = (a*d-b*c) % Q
        images = [None if (c*x+d) % Q == 0 else
                  (a*x+b)*pow((c*x+d) % Q, -1, Q) % Q for x in source]
        accept = None not in images and sorted(images) == T[1:]
        valid = (r['source'] == source and det != 0 and det == r['determinant']
                 and images[:3] == r['anchor_images'] and images == r['all_six_images']
                 and accept == r['accepted'])
        record_checks.append(valid)
        if not valid:
            failures.append('rigidity record ' + str(index))
        if accept:
            accepted.append({'removed': r['removed'], 'matrix': r['matrix']})
    check('only identity map', accepted == [{'removed': 16, 'matrix': [1, 0, 0, 1]}])
    check('every rigidity record', len(record_checks) == 840 and all(record_checks))

    recovery = dict(min_observed_column=Q-1, min_dominant=(Q-1+5)//6,
                    pair_budget=5*Q, smallest_excluded_product=
                    min(n*(Q-1-n) for n in range(23, 131)),
                    two_outsiders_rows=2*131-1, two_global_outsiders_rows=2*135-1,
                    good_lines=Q-Q//2, good_intersections=(Q-Q//2)**2)
    check('dominant lower bound', recovery['min_dominant'] == 23)
    check('entire excluded dominant range', recovery['smallest_excluded_product'] == 780 > 685)
    check('two outsiders impossible', recovery['two_outsiders_rows'] > Q)
    check('two global outsiders impossible', recovery['two_global_outsiders_rows'] > Q)
    check('unique dominant columns', 2*135 > Q)
    check('good base point exists', recovery['good_intersections'] == 4761 > Q)
    delta = Fraction(3, Q)
    check('stability threshold', delta < Fraction(2, 9))
    check('rationalization denominator exceeds four', 9-24*delta > 1)
    check('at most one disagreement', Q*delta/2 == Fraction(3, 2) < 2)
    check('zero homomorphism impossible', Q-1 > 1)
    counts = dict(q=Q, s=Q**2-Q, nonstar_pairs=Q**3-Q**2,
                  sum_bound=Q**3-Q**2+2*(Q**2-Q),
                  smaller_size_bound=(Q**3-Q**2+2*(Q**2-Q))//2,
                  required_each=1532496, required_sum=2*1532496,
                  original_intersection_lower_bound=60+5, permitted_intersection=63)
    counts['sum_shortfall'] = counts['required_sum']-counts['sum_bound']
    counts['smaller_size_shortfall'] = counts['required_each']-counts['smaller_size_bound']
    for key, expected in dict(s=18632, nonstar_pairs=2552584, sum_bound=2589848,
                              smaller_size_bound=1294924, sum_shortfall=475144,
                              smaller_size_shortfall=237572).items():
        check('exact count: ' + key, counts[key] == expected)
    check('original transferred edge forbidden', 60+5 > 63)
    check('both size thresholds excluded', counts['sum_bound'] < counts['required_sum'])
    result = dict(inputs=hashes, checks=checks, recovery_arithmetic=recovery,
                  stability=dict(delta_upper=str(delta), disagreement_upper='3/2',
                                 required_delta_upper='2/9', required_disagreement_upper='2'),
                  counts=counts, actual_rigidity_records=len(records), required_rigidity_records=840,
                  rigidity_record_checks=record_checks, accepted_maps=accepted,
                  failures=failures, qualification=
                  'Exact arithmetic and full inherited finite-map checks only. Universal incidence, '
                  'completion and transfer arguments are critically reviewed in canonical L129; '
                  'no enumeration of thinnings, sharpness or RS realization is asserted.')
    output = BASE / 'l129-critical-audit.json'
    output.write_text(json.dumps(result, indent=2) + '\n')
    print(f'Rigidity records: {len(records)}/840; all checks: {all(checks.values())}.')
    print('Sum <=2589848 against required 3064992; smaller size <=1294924 against 1532496.')
    print('Transferred intersection >=65 against permitted <=63; disagreement <=3/2, required <2.')
    print(f'Failures: {failures}; certificate: {output.relative_to(Path.cwd())}')
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
