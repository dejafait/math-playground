"""Separate step-317 audit of the existing L114 partition; no new filter."""
from hashlib import sha256
from itertools import combinations, product
from pathlib import Path
import json
import subprocess
import sys

import zero_anchor_support_filter as direct
import fixed_three_row_extensions as kernels
import verify_fixed_three_row_extensions as independent

HERE = Path(__file__).resolve().parent

def digest(path):
    return sha256(path.read_bytes()).hexdigest()

def run():
    checks, failures = [], []
    def check(name, valid):
        checks.append({'check': name, 'passed': bool(valid)})
        if not valid:
            failures.append(name)
    source_path = HERE/'remaining-third-factor-filter.json'
    source = json.loads(source_path.read_bytes())
    paths = [source_path, HERE/'remaining-third-factor-filter-replay.json']
    paths += [HERE/s['certificate'] for s in source['thirds']]
    before = {str(p.relative_to(HERE)): digest(p) for p in paths}
    code_names = ['remaining_third_factor_filter.py', 'verify_remaining_third_factor_filter.py',
                  'zero_anchor_support_filter.py', 'fixed_three_row_extensions.py',
                  'verify_fixed_three_row_extensions.py', 'audit_remaining_third_partition.py']
    code_hashes = {n: digest(HERE/n) for n in code_names}
    universe = list(product(combinations(direct.S, 2), combinations(direct.J, 2)))
    block_checks = 0
    for i, k in universe:
        a = direct.block(i, k)['matrix']
        b = independent.block(i, k)
        c = kernels.ratio_block(i, k)
        observed = [x for x in direct.S if x not in i]
        z = observed[0]
        for row, (x, y) in enumerate(combinations(observed[1:], 2)):
            scale = direct.g(k, z)**2*direct.g(k, x)*direct.g(k, y) % 97
            check(f'block {i}/{k} row {row} direct/derivative/ratio identity',
                  scale != 0 and a[row] == b[row] == [scale*t % 97 for t in c[row]])
            block_checks += 1
    check('all 756 blocks, six original exterior rows each', block_checks == 4536)
    disjoint = [[list(i), list(k)] for i, k in product(
        combinations([22,27,33], 2), combinations([75,79,85,89,96], 2))]
    check('exact removed disjoint list', source['removed_disjoint_thirds'] == disjoint)
    intervals = [(20,34),(36,37),(39,50),(52,59),(61,64),(66,68),(70,78),
                 (279,293),(296,299),(301,313),(315,350)]
    excluded = [i for a,b in intervals for i in range(a,b+1)]
    check('written 121 excluded indices', len(excluded) == len(set(excluded)) == 121
          and source['excluded_triple_indices'] == excluded)
    check('written complementary 230 residual indices', source['residual_triple_indices']
          == [i for i in range(351) if i not in excluded])
    expected = {'actual_thirds':351, 'required_thirds':351,
        'actual_fourth_cases':265356, 'required_fourth_cases':265356,
        'all_ranks':{'16':1520,'17':4047,'18':62864,'19':13385,'20':88461,'21':95079},
        'eligible_ranks':{'18':9096,'19':593,'20':34119,'21':50042},
        'statuses':{'excluded_label_1_factor':18942,'excluded_rank':50042,
                    'ineligible':171506,'unresolved':24866},
        'excluded_triples':121,'residual_triples':230,'nonzero_minor_witnesses':95079,
        'complete_deficient_kernels':170277,'complete_kernel_vectors':327611,
        'eligible_deficient_kernels':43808,'eligible_label_1_factor_kernels':18942,
        'required_exclusion_rank':21}
    check('all written partition counts', source['summary'] == expected)
    # The verifier reads every original case and proves rank/nullity, complete bases,
    # all original residuals, factor status, coverage, eligibility and summary equality.
    process = subprocess.run([sys.executable, str(HERE/'verify_remaining_third_factor_filter.py')],
                             capture_output=True, text=True)
    log = HERE/'remaining-third-partition-critical-audit.log'
    log.write_text(process.stdout + process.stderr)
    check('complete independent replay exits successfully', process.returncode == 0)
    replay = json.loads((HERE/'remaining-third-factor-filter-replay.json').read_bytes())
    check('replay counts and original residual count', replay['summary'] == expected
          and replay['kernel_residual_entries_checked'] == 7862664 and replay['failures'] == [])
    after = {str(p.relative_to(HERE)): digest(p) for p in paths}
    check('manifest, every shard and replay byte-identical after audit', before == after)
    check('replay binds exact original manifest', replay['source_sha256'] == before[source_path.name])
    check('all indexed shard hashes match', all(before[s['certificate']] == s['sha256']
                                               for s in source['thirds']))
    result = {'scope':'Separate step-317 complete L114 partition certificate audit; analytic review in L114',
              'summary':expected, 'block_rows_compared':block_checks,
              'kernel_residual_entries_checked':replay['kernel_residual_entries_checked'],
              'artifact_hashes_before':before, 'artifact_hashes_after':after,
              'code_hashes':code_hashes, 'checks':checks,
              'replay_returncode':process.returncode, 'replay_log':log.name, 'failures':failures}
    output = HERE/'remaining-third-partition-critical-audit.json'
    output.write_text(json.dumps(result, indent=2)+'\n')
    print(f'Cases 265356/265356; thirds 351/351; exclusions 121; residual thirds 230; '
          f'residual occurrences 24866; minors 95079; deficient kernels 170277; '
          f'vectors 327611; original residuals 7862664; block rows {block_checks}/4536; '
          f'failures {len(failures)}; certificate {output}; log {log}', flush=True)
    if failures:
        print(failures)
        raise SystemExit(1)

if __name__ == '__main__':
    run()
