"""Separate step-321 audit of L116's saved partition; no expanded filter."""
from collections import Counter
from hashlib import sha256
from itertools import combinations, product
from pathlib import Path
import json
import subprocess
import sys

import zero_anchor_support_filter as direct
import verify_fixed_three_row_extensions as independent

HERE = Path(__file__).resolve().parent


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def run():
    checks, failures = [], []

    def check(name, value):
        checks.append({'check': name, 'passed': bool(value)})
        if not value:
            failures.append(name)

    old_path = HERE/'remaining-third-factor-filter.json'
    new_path = HERE/'residual-coordinate-factors.json'
    old = json.loads(old_path.read_bytes())
    new = json.loads(new_path.read_bytes())
    prior_path = HERE/'remaining-third-partition-critical-audit.json'
    prior = json.loads(prior_path.read_bytes())
    paths = [old_path, new_path, HERE/'residual-coordinate-factors-replay.json']
    paths += [HERE/m['certificate'] for m in old['thirds']+new['thirds']]
    before = {str(p.relative_to(HERE)): digest(p) for p in paths}
    code_names = ['residual_coordinate_factors.py', 'verify_residual_coordinate_factors.py',
                  'zero_anchor_support_filter.py', 'verify_fixed_three_row_extensions.py',
                  'audit_residual_coordinate_partition.py']
    code_hashes = {name: digest(HERE/name) for name in code_names}
    check('prior L114 audit succeeded', prior['failures'] == [] and prior['replay_returncode'] == 0
          and all(c['passed'] for c in prior['checks']))
    check('prior L114 before and after hashes identical',
          prior['artifact_hashes_before'] == prior['artifact_hashes_after'])
    for name, value in prior['artifact_hashes_after'].items():
        check('unchanged audited L114 artifact '+name, digest(HERE/name) == value)
    for name in ['zero_anchor_support_filter.py', 'verify_fixed_three_row_extensions.py']:
        check('unchanged audited mathematical helper '+name, code_hashes[name] == prior['code_hashes'][name])

    S, J = direct.S, direct.J
    universe = list(product(combinations(S, 2), combinations(J, 2)))
    sets = {key: set(key[0]+key[1]) for key in universe}
    first = [((1,8),(47,50)), ((12,18),(64,70))]
    union = sets[first[0]] | sets[first[1]]
    eligible = [key for key in universe if all(len(sets[key]&sets[a]) <= 1 for a in first)]
    removed = [key for key in eligible if not sets[key]&union]
    named = ((1,22),(75,79))
    thirds = [key for key in eligible if key not in removed and key != named]
    check('exact 382/30/351 third domain', len(eligible) == 382 and len(removed) == 30
          and len(thirds) == 351 and named in eligible and named not in removed)
    check('exact L112 removed domain', removed == list(product(
        combinations([22,27,33], 2), combinations([75,79,85,89,96], 2))))
    check('exact L114 ordered thirds', thirds == [
        (tuple(m['third_I']), tuple(m['third_K'])) for m in old['thirds']])

    block_rows = 0
    for i, k in universe:
        a = direct.block(i, k)['matrix']
        b = independent.block(i, k)
        for r in range(6):
            check(f'original/derivative block {i}/{k} row {r}', a[r] == b[r])
            block_rows += 1
    check('complete block equality', block_rows == 4536)

    remaining = list(range(20))+[35,38,51,60,65,69]+list(range(79,99))+[
        115,145,149,178,191,218,278,295,300,314]
    check('written 56 residual thirds', len(remaining) == len(set(remaining)) == 56
          and remaining == new['remaining_third_indices'])
    excluded = [n for n in old['residual_triple_indices'] if n not in remaining]
    check('exact 174 new thirds, no older-third double count', len(excluded) == 174
          and excluded == new['newly_excluded_third_indices']
          and not set(excluded)&set(old['excluded_triple_indices']))

    # Account for every eligible fourth for each claimed third. This is not
    # a recursive closure: only frozen L114 dispositions and this shard are used.
    by_third = {m['third_index']: m for m in new['thirds']}
    assembly = []
    for n in excluded:
        src = json.loads((HERE/old['thirds'][n]['certificate']).read_bytes())
        dst = json.loads((HERE/by_third[n]['certificate']).read_bytes())
        dispositions = {c['fourth_index']: c['status'] for c in dst['cases']}
        counts = Counter()
        rowsets = [sets[key] for key in first+[thirds[n]]]
        case_checks = []
        for u, key in enumerate(universe):
            ok = all(len(sets[key]&a) <= 1 for a in rowsets)
            case = src['cases'][u]
            check(f'third {n}, fourth {u}: inherited eligibility', case['eligible'] == ok)
            if not ok:
                continue
            old_status = case['status']
            if old_status in ('excluded_rank', 'excluded_label_1_factor'):
                reason = 'L114:'+old_status
            else:
                reason = 'L116:'+str(dispositions.get(u))
                check(f'third {n}, fourth {u}: nonrecursive residual exclusion',
                      old_status == 'unresolved' and dispositions.get(u) == 'excluded_coordinate_factor')
            counts[reason] += 1
            case_checks.append({'fourth_index': u, 'reason': reason})
        check(f'third {n}: nonempty complete eligible fourth coverage', bool(case_checks)
              and sum(counts.values()) == sum(c['eligible'] for c in src['cases']))
        assembly.append({'third_index': n, 'counts': dict(counts), 'eligible_fourths': case_checks})

    process = subprocess.run([sys.executable, str(HERE/'verify_residual_coordinate_factors.py')],
                             capture_output=True, text=True)
    log = HERE/'residual-coordinate-partition-critical-audit.log'
    log.write_text(process.stdout+process.stderr)
    check('complete inspected verifier succeeds', process.returncode == 0)
    replay = json.loads((HERE/'residual-coordinate-factors-replay.json').read_bytes())
    check('complete replay binds input and matches summary', replay['failures'] == []
          and replay['source_sha256'] == before[new_path.name] and replay['summary'] == new['summary'])
    expected = {'occurrences':24866, 'excluded_coordinate_factor':24267, 'unresolved':599,
                'basis_vectors':39139, 'original_residual_entries':939336, 'factor_tests':198928,
                'passing_factor_tests':88518, 'remaining_thirds':56, 'newly_excluded_thirds':174}
    for key, value in expected.items():
        check('written summary '+key, replay['summary'][key] == value)
    check('all 88518 gate certificates checked', replay['complete_gate_certificates_checked'] == 88518)
    check('written rank histogram', replay['summary']['rank_histogram'] == {'18':6840,'19':593,'20':17433})
    check('written first-factor histogram', replay['summary']['selected_factor_histogram'] ==
          {'row1_label8':19036,'row2_label12':2620,'row2_label18':2611})
    check('written overlap histogram including retained failures',
          replay['summary']['fourth_historical_class_histogram'] == {
              'L112_disjoint:excluded_coordinate_factor':211, 'L112_disjoint:unresolved':9,
              'historical_residual:excluded_coordinate_factor':24056, 'historical_residual:unresolved':590})
    check('L115 comparison retains precisely the known occurrence', replay['L115_regression'] == {
        'third_index':0, 'fourth_index':249, 'status':'excluded_coordinate_factor',
        'passing_factors':[[2,12],[3,12],[4,12]]})
    after = {str(p.relative_to(HERE)): digest(p) for p in paths}
    check('all 584 manifest/shard/replay files unchanged', len(before) == 584 and before == after)
    result = {'scope':'Separate step-321 audit of L116; no new exclusions or solver',
              'prior_L114_audit_sha256':digest(prior_path), 'code_hashes':code_hashes,
              'artifact_hashes_before':before, 'artifact_hashes_after':after,
              'summary':replay['summary'], 'block_rows_compared':block_rows,
              'third_assemblies':assembly, 'checks':checks, 'failures':failures,
              'replay_returncode':process.returncode, 'replay_log':log.name}
    output = HERE/'residual-coordinate-partition-critical-audit.json'
    output.write_text(json.dumps(result, indent=2)+'\n')
    print(f'Occurrences {replay["summary"]["occurrences"]}/24866; gates '
          f'{replay["complete_gate_certificates_checked"]}/88518; third assemblies {len(assembly)}/174; '
          f'block rows {block_rows}/4536; failures {len(failures)}; certificate {output}; log {log}', flush=True)
    if failures:
        print(failures)
        raise SystemExit(1)


if __name__ == '__main__':
    run()
