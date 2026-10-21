"""Bind L051's complete JSON, compact export and independent audit replays."""
from collections import Counter
from pathlib import Path
import hashlib
import json
import sys

ROOT = Path(__file__).parent
BASE = ROOT / 'forced-v-audit-before.json'
OUT = ROOT / 'forced-v-critical-audit.json'
FILES = [
    'disjoint-d-pair-result.json', 'forced-v-mixed-result.json',
    'forced-v-mixed-verifier-input.txt', 'forced-v-mixed-coverage.json',
    'forced-v-mixed-recurrence-verification.json', 'forced_v_mixed.py',
    'finite_count.py', 'export_forced_v_mixed.py',
    'check_forced_v_coverage.py', 'verify_forced_v_mixed.cpp',
]


def sha(path):
    digest = hashlib.sha256()
    with path.open('rb') as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b''):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    hashes = {name: sha(ROOT / name) for name in FILES}
    if sys.argv[1:] == ['--snapshot']:
        with BASE.open('x') as stream:
            json.dump(hashes, stream, indent=2)
            stream.write('\n')
        print(f'preserved {len(hashes)} artifact/source hashes; path {BASE}')
        return
    assert not sys.argv[1:]
    assert hashes == json.loads(BASE.read_text()), 'audit changed saved evidence'
    prior = json.loads((ROOT / 'disjoint-d-critical-audit.json').read_text())
    source_key = 'scripts/simultaneous-recovery/disjoint-d-pair-result.json'
    assert hashes['disjoint-d-pair-result.json'] == prior['certificate_sha256'][source_key]
    assert prior['replay_matches_initial_bytes'] and not prior['summary']['failures']
    data = json.loads((ROOT / 'forced-v-mixed-result.json').read_text())
    coverage = json.loads((ROOT / 'forced-v-mixed-coverage.json').read_text())
    replay = json.loads((ROOT / 'forced-v-mixed-audit-recurrence.json').read_text())
    old_replay = json.loads((ROOT / 'forced-v-mixed-recurrence-verification.json').read_text())
    assert replay == old_replay
    h = [x for x in range(1, 97) if pow(x, 16, 97) == 1]
    assert len(h) == 16 and data['complete']
    assert data['scope'] == {'h': 1, 'prime': 97, 'H': h, 'all_labelings': True,
        'two_d_and_forced_V_branch_only': True, 'E_exclusion_relaxed': True,
        'required_mixed_count': 9}
    hist = Counter()
    records = 0
    with (ROOT / 'forced-v-mixed-verifier-input.txt').open() as stream:
        assert stream.readline() == str(len(data['cases'])) + '\n'
        for case in data['cases']:
            rr = case['mixed_records']
            row = [*case['Y'], *case['Z'], case['d'], *case['W'], *case['p_q_r'],
                *case['V'], *case['S'], *case['SS'], *case['Bprime_minus_d'],
                *case['T0'], case['V_recovery']['mu'],
                *(r['mu'] for r in case['selected_recoveries']), len(rr)]
            memberships = set()
            c = {int(x): a for x, a in case['c'].items()}
            p, q, r = case['p_q_r']
            for rec in rr:
                k, m = rec['K'], rec['mu']
                assert k == sorted(set(k)) and len(k) == 4 and m not in (0, 96)
                mask = sum(1 << h.index(x) for x in k)
                assert (mask, m) not in memberships
                memberships.add((mask, m))
                row.extend([mask, m])
                n = {x: -m*c[x] % 97 for x in case['Y']}
                n.update({x: c[x] for x in case['Z']})
                n[1] = c[1]*(q-m*p) % 97
                n[case['d']] = c[case['d']]*(1-(1+m)*r) % 97
                moments = [sum(a*pow(x, j, 97) for x, a in n.items()) % 97
                           for j in range(1, 9)]
                assert rec['N_moments'] == moments
            assert stream.readline() == ' '.join(map(str, row)) + '\n'
            mus = sorted({m for _, m in memberships})
            assert case['mixed_mus'] == mus and case['mixed_supports_tested'] == 250
            assert not set(mus) & {case['V_recovery']['mu'],
                                   *(r['mu'] for r in case['selected_recoveries'])}
            hist[len(mus)] += 1
            records += len(rr)
        assert stream.read() == ''
    count = len(data['cases'])
    assert count == 289488 and records == 1700
    assert hist == {0: 287788, 1: 1700}
    assert data['counters'] == coverage['complete_filter_counts'] == {
        'd_pair_presentations': 302400, 'feasible': count,
        'r_gate': 7952, 'V_selected_scalar': 4960}
    assert data['summary'] == {
        'Y_Z_choices': 8190, 'W_pair_presentations': 75600,
        'unique_pair_configurations': 302400, 'full_forced_V_configurations': count,
        'mixed_support_tests': 250*count,
        'mixed_count_histogram': {str(k): v for k, v in hist.items()},
        'maximum_distinct_mixed_scalars': max(hist), 'required_for_twelve': 9,
        'all_admitted_eight_moments_verified': True,
        'independent_completeness_check_pending': True,
        'proves_uniform_eleven': False, 'failures': []}
    assert coverage['summary'] == {
        'normalized_choices_checked': 8190, 'W_pair_presentations_checked': 75600,
        'unique_configurations_checked': 302400, 'accepted_configurations_checked': count,
        'all_weight_records_eight_moments_checked': 3*count+records,
        'original_triples_checked': count, 'all_retained_and_rejected_filters_match': True,
        'failures': []}
    assert replay == {
        'complete_cases_checked': count, 'required_cases': count,
        'mixed_supports_checked': 250*count, 'required_supports': 250*count,
        'admitted_memberships_checked': records, 'maximum_distinct_mixed_scalars': max(hist),
        'required_for_twelve': 9, 'all_membership_sets_match': True, 'failures': [],
        'mixed_count_histogram': {str(k): v for k, v in hist.items()}}
    result = {'artifact_sha256': hashes, 'audit_script_sha256': sha(Path(__file__)),
        'recurrence_replay_sha256': sha(ROOT / 'forced-v-mixed-audit-recurrence.json'),
        'summary': {'all_prior_bytes_preserved': True, 'audited_L049_source_unchanged': True,
            'complete_export_rows_checked': count, 'required_export_rows': count,
            'mixed_memberships_checked': records, 'full_mixed_support_tests': 250*count,
            'all_eight_moment_weight_records_checked_by_coverage_replay': 3*count+records,
            'coverage_and_recurrence_replays_match_saved_results': True,
            'actual_maximum': max(hist), 'required_for_twelve': 9, 'failures': []}}
    OUT.write_text(json.dumps(result, indent=2) + '\n')
    print(f'export rows {count}/{count}; mixed tests {250*count}/{250*count}; '
          f'actual maximum {max(hist)}; required 9; failures 0; certificate {OUT}')


if __name__ == '__main__':
    main()
