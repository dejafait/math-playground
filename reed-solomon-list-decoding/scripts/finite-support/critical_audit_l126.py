#!/usr/bin/env python3
"""L126 arithmetic audit and full linkage/coverage check of L125 rigidity.

The polynomial bijection and arbitrary-label specialization are symbolic
proof obligations in L126, not claims certified by this program.
"""
import hashlib
import itertools
import json
from pathlib import Path

BASE = Path(__file__).resolve().parent
Q = 137
T = [16, 64, 70, 102, 112, 118, 121]
FAILURES = []


def check(name, value):
    if not value:
        FAILURES.append(name)
    return bool(value)


def main():
    paths = [BASE / name for name in (
        'full-star-thinning-count.json', 'two-core-star-rigidity.json',
        'two_core_star_rigidity.py', 'l125-critical-audit.json')]
    counts, rigidity, _, prior = [json.loads(p.read_text()) if p.suffix == '.json'
                                 else None for p in paths]
    hashes = {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
    linkage = {name: check('prior hash:' + name, hashes[name] == digest)
               for name, digest in prior['inputs'].items()}
    check('exact prior hashed inputs', set(linkage) ==
          {'two-core-star-rigidity.json', 'two_core_star_rigidity.py'})
    expected = dict(q=Q, full_family_size_each=Q**3,
                    full_star_size_each=Q**2, nonstar_matching_edges=Q**3-Q**2,
                    retained_nonstar_sum_upper_bound=Q**3-Q**2,
                    retained_family_sum_upper_bound=Q**3+Q**2,
                    balanced_retention_upper_bound=(Q**3+Q**2)//2,
                    required_retention_each=1532496,
                    required_retention_sum=2*1532496,
                    sum_shortfall=2*1532496-(Q**3+Q**2),
                    balanced_shortfall=1532496-(Q**3+Q**2)//2)
    c = expected
    arithmetic = dict(
        nonstar_size=c['nonstar_matching_edges'] == c['full_family_size_each']-c['full_star_size_each'],
        star_size=c['full_star_size_each'] == Q**2,
        sum_bound_identity=c['retained_family_sum_upper_bound'] == 2*Q**2+c['nonstar_matching_edges'],
        bound_even=c['retained_family_sum_upper_bound'] % 2 == 0,
        balanced_bound=2*c['balanced_retention_upper_bound'] == c['retained_family_sum_upper_bound'],
        required_sum=c['required_retention_sum'] == 2*c['required_retention_each'],
        sum_threshold_excluded=c['retained_family_sum_upper_bound'] < c['required_retention_sum'],
        sum_shortfall=c['sum_shortfall'] == c['required_retention_sum']-c['retained_family_sum_upper_bound'],
        balanced_shortfall=c['balanced_shortfall'] == c['required_retention_each']-c['balanced_retention_upper_bound'])
    expected.update(checks=arithmetic, failures=[], qualification=
        'Exact integer arithmetic only; the complete nonstar bijection and forbidden-support proof are in L126. No sharpness, feasibility or independent critical audit is certified.')
    field_checks = {k: check('count field:' + k, counts.get(k) == v) for k, v in expected.items()}
    check('exact count keys', set(counts) == set(expected))
    check('all arithmetic checks', all(arithmetic.values()))
    records = rigidity['records']
    check('complete prior record equality', records == prior['records'])
    check('prior no failures', prior['failures'] == [])
    check('prior full field and record checks', all(prior['field_checks'].values())
          and len(prior['record_checks']) == 840 and all(prior['record_checks']))
    required = [(t, list(ys)) for t in T for ys in itertools.permutations(T[1:], 3)]
    check('840 complete ordered cases', [(r['removed'], r['anchor_images']) for r in records] == required)
    details, accepted = [], []
    for i, r in enumerate(records):
        source = [t for t in T if t != r['removed']]
        a, b, c0, d = r['matrix']
        det = (a*d-b*c0) % Q
        images = [None if (c0*x+d) % Q == 0 else
                  (a*x+b)*pow((c0*x+d) % Q, -1, Q) % Q for x in source]
        accept = None not in images and sorted(images) == T[1:]
        tests = dict(source=r['source'] == source,
                     invertible=det != 0 and r['determinant'] == det,
                     anchors=images[:3] == r['anchor_images'],
                     all_six_images=images == r['all_six_images'],
                     acceptance=r['accepted'] == accept)
        for key, val in tests.items():
            check(f'rigidity record {i}:{key}', val)
        details.append(dict(index=i, checks=tests))
        if accept:
            accepted.append(dict(removed=r['removed'], matrix=r['matrix']))
    check('only identity survivor', accepted == [dict(removed=16, matrix=[1, 0, 0, 1])])
    check('original summary linkage', rigidity['accepted'] == [r for r in records if r['accepted']]
          and rigidity['actual_candidates'] == rigidity['required_candidates'] == len(records) == 840)
    check('conflict threshold', 60+6 > 63)
    result = dict(audit='L126 arithmetic and established rigidity input audit',
                  inputs=hashes, prior_input_linkage=linkage,
                  complete_arithmetic=expected, arithmetic_field_checks=field_checks,
                  actual_rigidity_records=len(records), required_rigidity_records=840,
                  rigidity_record_checks=details, accepted_maps=accepted,
                  support_bounds=dict(actual_intersection_lower_bound=66,
                                      permitted_intersection_upper_bound=63),
                  failures=FAILURES,
                  qualification='Symbolic applicability, polynomial inverse, distinct supports and disjoint-edge counting are reviewed in L126. No enumeration of thinnings or sharpness claim.')
    output = BASE / 'l126-critical-audit.json'
    output.write_text(json.dumps(result, indent=2) + '\n')
    print(f'Complete arithmetic fields: {sum(field_checks.values())}/{len(expected)}')
    print(f'Rigidity records checked: {len(records)}; required 840; accepted {accepted}')
    print('Retained sum <=2590122; required 3064992. Balanced <=1295061; required 1532496.')
    print(f'Failures: {FAILURES}; certificate: {output.relative_to(Path.cwd())}')
    if FAILURES:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
