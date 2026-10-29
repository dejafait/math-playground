"""Complete L123 artifact audit and fresh replay; originals remain read-only.

Independent small checks use six-subsets and perfect matchings, and generate
histograms by ordered endpoints followed by diagonal exclusion and halving.
The actual-field replay is the reviewed C algorithm, not a new algorithm.
"""
from hashlib import sha256
from itertools import combinations
from math import comb, isqrt
from pathlib import Path
import json
import struct
import subprocess

BASE = Path(__file__).resolve().parent
REPORT = BASE / 'l123-critical-audit.json'


def digest(p):
    return sha256(p.read_bytes()).hexdigest()


def canonical(x):
    return json.loads(json.dumps(x))


def main():
    out = {'checks': [], 'failures': [], 'complete': False}

    def check(name, actual, required):
        actual, required = canonical(actual), canonical(required)
        ok = actual == required
        out['checks'].append({'name': name, 'actual': actual, 'required': required, 'ok': ok})
        if not ok:
            out['failures'].append(name)

    def parse_input(p):
        lines = p.read_text().splitlines()
        check(p.name + '_input_lines', len(lines), 3)
        return [list(map(int, line.split())) for line in lines]

    def parse_counts(p, H):
        rows = [list(map(int, line.split())) for line in p.read_text().splitlines()]
        check(p.name + '_row_widths', all(len(r) == 3 for r in rows), True)
        check(p.name + '_ordered_ratios', [r[0] for r in rows], [a for a in H if a != 1])
        check(p.name + '_nonnegative_multiple_six', all(s >= 0 and d >= 0 and s % 6 == 0 and d % 6 == 0 for _, s, d in rows), True)
        return {b: {'same': s, 'different': d, 'total': s+d} for b, s, d in rows}

    def cosets(q, H):
        remaining = set(range(1, q))
        reps = []
        while remaining:
            u = min(remaining)
            part = {u*a % q for a in H}
            check(f'coset_{q}_{len(H)}_{u}', len(part) == len(H) and part <= remaining, True)
            reps.append(u)
            remaining -= part
        return reps

    def matchings(points):
        if not points:
            yield ()
            return
        a = points[0]
        for i in range(1, len(points)):
            b = points[i]
            for rest in matchings(points[1:i] + points[i+1:]):
                yield ((a, b),) + rest

    try:
        small_specs = [(17, 8), (17, 16), (41, 8), (97, 16)]
        originals = [BASE / name for name in (
            'endpoint_pair_count.c', 'endpoint_pair_count.py', 'endpoint-pair-count.json',
            'endpoint-pair-counts.txt', 'endpoint-pair-input.txt', 'l122-full-count.json',
            'l122-full-count-histograms.u32', 'c122a-critical-audit.json')]
        for q, n in small_specs:
            originals += [BASE / f'endpoint-small-{q}-{n}{suffix}' for suffix in ('-counts.txt', '-input.txt', '.u32')]
        before = {p.name: digest(p) for p in originals}
        out['original_sha256'] = before
        saved = json.loads((BASE / 'endpoint-pair-count.json').read_text())
        upstream = json.loads((BASE / 'c122a-critical-audit.json').read_text())
        manifest = json.loads((BASE / 'l122-full-count.json').read_text())
        check('upstream_audit_complete', upstream['complete'], True)
        check('upstream_audit_failures', upstream['failures'], [])
        check('upstream_audit_all_checks', [len(upstream['checks']), all(c['ok'] for c in upstream['checks'])], [420, True])
        for name in ('l122-full-count.json', 'l122-full-count-histograms.u32'):
            check('upstream_link_' + name, before[name], upstream['original_sha256'][name])
        check('upstream_complete_manifest_link', manifest, upstream['expected_production_manifest'])
        hist = BASE / 'l122-full-count-histograms.u32'
        check('histogram_bytes', hist.stat().st_size, 66 * 65537 * 4)
        check('histogram_sha256', digest(hist), '4f8161677371fe052b12ead70436b92c0ceb508883a5bd658a593086043aa681')
        expected_checks = []

        def production_check(name, actual, required):
            expected_checks.append(canonical({'name': name, 'actual': actual, 'required': required}))
            check('production_' + name, actual, required)

        compiler = ['cc', '-O2', '-std=c11', '-Wall', '-Wextra', '-fsanitize=undefined', '-fno-sanitize-recover=all', str(BASE / 'endpoint_pair_count.c'), '-o', str(BASE / 'l123-audit-replay-bin')]
        out['compile_command'] = compiler
        process = subprocess.run(compiler, capture_output=True, text=True)
        out['compiler'] = {'returncode': process.returncode, 'stdout': process.stdout, 'stderr': process.stderr}
        check('compile_success', process.returncode, 0)
        process.check_returncode()
        out['replays'] = []

        def replay(tag, input_path, hist_path, H, expected):
            destination = BASE / (tag + '-audit-replay-counts.txt')
            process = subprocess.run([str(BASE / 'l123-audit-replay-bin'), str(input_path), str(hist_path), str(destination)], capture_output=True, text=True)
            out['replays'].append({'tag': tag, 'returncode': process.returncode, 'stdout': process.stdout, 'stderr': process.stderr, 'path': destination.name})
            check(tag + '_replay_exit', process.returncode, 0)
            check(tag + '_sanitizer_diagnostics', process.stderr, '')
            process.check_returncode()
            check(tag + '_replay_every_count', parse_counts(destination, H), expected)

        small_instances = []
        for q, n in small_specs:
            check(f'prime_{q}', [a for a in range(2, isqrt(q)+1) if q % a == 0], [])
            H = [a for a in range(1, q) if pow(a, n, q) == 1]
            production_check(f'{q}_{n}_order', len(H), n)
            reps = cosets(q, H)
            tag = f'endpoint-small-{q}-{n}'
            check(tag + '_input', parse_input(BASE / (tag + '-input.txt')), [[q, n, len(reps)], H, reps])
            # Generate independently by ordered endpoint loops, excluding diagonals.
            rows = []
            for slope in [None, 0] + reps:
                row = [0] * q
                for a in H:
                    for b in H:
                        if a == b:
                            continue
                        bin_index = (a+b) % q if slope is None else ((a-slope)*(b-slope)-slope*slope) % q
                        row[bin_index] += 1
                check(tag + f'_even_{slope}', all(r % 2 == 0 for r in row), True)
                rows.append([r//2 for r in row])
            data = b''.join(struct.pack(f'<{q}I', *row) for row in rows)
            check(tag + '_every_histogram_byte', (BASE / (tag + '.u32')).read_bytes() == data, True)
            fresh_hist = BASE / (tag + '-audit-replay.u32')
            fresh_hist.write_bytes(data)
            computed = parse_counts(BASE / (tag + '-counts.txt'), H)
            brute = {a: {'same': 0, 'different': 0, 'total': 0} for a in H if a != 1}
            total = 0
            tested = 0
            for six in combinations(H, 6):
                for edges in matchings(six):
                    tested += 1
                    (a, b), (c, d), (e, f) = edges
                    # Expanded 3-by-3 determinant, no line lookup or occupancy formula.
                    det = (a+b)*(c*d-e*f) - a*b*((c+d)-(e+f)) + (c+d)*e*f-c*d*(e+f)
                    if det % q:
                        continue
                    total += 6
                    if 1 in six:
                        partner = next(y if x == 1 else x for x, y in edges if 1 in (x, y))
                        for endpoint in six:
                            if endpoint == 1:
                                continue
                            brute[endpoint]['same' if endpoint == partner else 'different'] += 6
                            brute[endpoint]['total'] += 6
            check(tag + '_all_six_matchings', tested, 15 * comb(n, 6))
            production_check(f'{q}_{n}_all_counts', computed, brute)
            small_instances.append({'q': q, 'n': n, 'ordered_count': total, 'counts': computed, 'brute_counts': brute})
            replay(tag, BASE / (tag + '-input.txt'), fresh_hist, H, brute)
        q, n = 65537, 1024
        check('actual_prime', [a for a in range(2, isqrt(q)+1) if q % a == 0], [])
        H = [pow(pow(3, 64, q), j, q) for j in range(n)]
        roots = [a for a in range(1, q) if pow(a, n, q) == 1]
        check('actual_roots', sorted(H), roots)
        check('actual_distinct_roots', len(set(H)), n)
        reps = cosets(q, H)
        check('actual_manifest_subgroup', manifest['H'], H)
        check('actual_histogram_row_order', [r['slope'] for r in manifest['rows']], [None, 0] + reps)
        check('actual_input', parse_input(BASE / 'endpoint-pair-input.txt'), [[q, n, 64], H, reps])
        # Check every inverse used by C, not only inverses exercised by a sample.
        inv = [0] * q
        inv[1] = 1
        for a in range(2, q):
            inv[a] = q - (q//a)*inv[q % a] % q
        check('all_inverse_recurrence_entries', all(a*inv[a] % q == 1 and 1 <= inv[a] < q for a in range(1, q)), True)
        vertical = struct.unpack(f'<{q}I', hist.read_bytes()[:q*4])
        check('same_pair_all_vertical_bounds', all(1 <= vertical[(1+x) % q] <= n//2 for x in H if x != 1), True)
        counts = parse_counts(BASE / 'endpoint-pair-counts.txt', H)
        replay('endpoint-pair', BASE / 'endpoint-pair-input.txt', hist, H, counts)
        T = manifest['ordered_count']
        s = 6*T//n
        production_check('audited_histogram_digest', digest(hist), '4f8161677371fe052b12ead70436b92c0ceb508883a5bd658a593086043aa681')
        production_check('H_all_roots', sorted(H), roots)
        production_check('coset_partition', sorted(u*a % q for u in reps for a in H), list(range(1, q)))
        production_check('all_nonidentity_ratios', sorted(counts), sorted(set(H)-{1}))
        production_check('singleton_integrality', 6*T % n, 0)
        production_check('sum_same', sum(c['same'] for c in counts.values()), s)
        production_check('sum_different', sum(c['different'] for c in counts.values()), 4*s)
        production_check('all_endpoint_pairs', n//2*sum(c['total'] for c in counts.values()), 15*T)
        production_check('inverse_ratio_symmetry', all(c == counts[pow(b, -1, q)] for b, c in counts.items()), True)
        M = max(c['total'] for c in counts.values())
        attainers = sorted(b for b, c in counts.items() if c['total'] == M)
        lower = T-61*s
        upper = lower + comb(61, 2)*M
        incidence = T-(61*s+5)//6
        production_check('nontrivial_upper_improvement', upper < incidence, True)
        deletion = {'core_size': 61, 'bonferroni_upper': upper, 'singleton_only_upper': T-s, 'union_bound_lower': lower, 'incidence_only_upper': incidence, 'upper_improvement': incidence-upper}
        expected = {'failures': [], 'checks': expected_checks, 'small_instances': small_instances, 'q': q, 'n': n, 'ordered_count': T, 'counts': counts, 'maximum': M, 'attainers': attainers, 'antipodal': counts[q-1], 'singleton': s, 'deletion': deletion, 'histogram_sha256': digest(hist), 'c_sha256': before['endpoint_pair_count.c'], 'python_sha256': before['endpoint_pair_count.py'], 'complete': True}
        out['expected_complete_manifest'] = canonical(expected)
        check('every_manifest_field', saved, expected)
        check('canonical_maximum_and_attainers', [M, attainers, counts[q-1]], [67798380, [65536], {'same': 15270744, 'different': 52527636, 'total': 67798380}])
        check('canonical_diagnostics', [s, lower, upper, incidence, incidence-upper, T-s], [13466310768, 1476805414224, 1600876449624, 2161342878264, 560466428640, 2284784060304])
        trials = (n-1)*comb(n, 2)
        disjoint = (n-1)*comb(n-2, 2)
        lines = (n-1)*(q+1)
        same_bound = (q+1)*3*511*510
        diff_bound = 2*disjoint*6*510
        check('canonical_operation_bounds', [trials, disjoint, lines], [535822848, 533730813, 67045374])
        check('accumulator_bounds', [same_bound < 2**36, diff_bound < 2**42], [True, True])
        out['arithmetic'] = {'maximum': M, 'attainers': attainers, 'singleton': s, 'sum_same': sum(c['same'] for c in counts.values()), 'sum_different': sum(c['different'] for c in counts.values()), 'sum_total': sum(c['total'] for c in counts.values()), 'unordered_pair_total': 15*T, 'deletion': deletion, 'same_accumulator_bound': same_bound, 'same_required_limit': 2**36, 'all_different_updates_bound': diff_bound, 'different_required_limit': 2**42, 'signed_product_bound': (q-1)**2, 'signed_required_limit': 2**63, 'pair_trials': trials, 'disjoint_trials': disjoint, 'same_line_queries_upper': lines}
        check('originals_unchanged', {p.name: digest(p) for p in originals}, before)
    except Exception as exc:
        out['failures'].append({'exception': type(exc).__name__, 'message': str(exc)})
    out['script_sha256'] = digest(Path(__file__))
    out['complete'] = not out['failures']
    REPORT.write_text(json.dumps(out, indent=2) + '\n')
    print(json.dumps({'complete': out['complete'], 'checks': len(out['checks']), 'arithmetic': out.get('arithmetic'), 'failures': out['failures'], 'certificate': str(REPORT.relative_to(Path.cwd()))}))
    return 0 if out['complete'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
