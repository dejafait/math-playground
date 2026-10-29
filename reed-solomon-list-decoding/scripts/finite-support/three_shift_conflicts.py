"""Complete three-shift diagnostic and full independent integer-bitset replay.

Run from notebook: python3 scripts/finite-support/three_shift_conflicts.py
No ranks, additional shifts, random tests, solver or external service.
"""
import hashlib
import json
from pathlib import Path
import struct
import subprocess
from collections import Counter
from itertools import combinations

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
OUT = HERE / 'three-shift-conflicts'
Q, N = 137, 137**3
T = [16, 64, 70, 102, 112, 118, 121]
SHIFTS = [0, 1, -1]
THRESHOLD, BUDGET = 1532496, 1038857
checks = []


def check(name, actual, required):
    checks.append(dict(name=name, actual=actual, required=required,
                       passed=actual == required))


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    OUT.mkdir(exist_ok=True)
    source = HERE / 'mixed-core-l031-embedding.json'
    saved = json.loads(source.read_text())
    check('saved source failures', saved['failures'], [])
    check('parameters', saved['parameters'], dict(P=65537, generator=19139, q=Q, T=T))
    h = [1]
    for _ in range(1023):
        h.append(h[-1] * 19139 % 65537)
    check('full subgroup recurrence', saved['domain'], h)
    check('subgroup closes', h[-1]*19139 % 65537, 1)
    check('subgroup distinct', len(set(h)), 1024)
    exponent = {x: e for e, x in enumerate(h)}
    labels = [('g', t, y) for t in T for y in range(Q)] + [('d', d) for d in range(4)]
    bp = {('g', t, 0) for t in T}
    br = {('g', t, (t-16) % Q) for t in T}
    edge_order = list(combinations(range(4), 2))
    residual_pairs = [set(range(2*j, 2*j+2)) for j in range(6)]
    supports = [set(range(12, 72)) | set(range(72+2*i, 74+2*i)) |
                set().union(*(pair for edge, pair in zip(edge_order, residual_pairs) if i in edge))
                for i in range(4)]
    cores = [set(range(12, 72)) | {0}, set(range(12, 72)) | {10}]
    check('all four pinned source supports',
          saved['supports'], [[h[e] for e in sorted(s)] for s in supports])
    check('complete source cores', saved['cores'], [[h[e] for e in sorted(s)] for s in cores])
    maps = []
    for side, (indices, fixed, image) in enumerate([
        ((0, 1), ('g', 16, 1), 10), ((2, 3), ('d', 0), 0)
    ]):
        residuals = [supports[i] - cores[side] for i in indices]
        mapping = {fixed: image}
        for sig in [(0,0), (0,1), (1,0), (1,1)]:
            src = [x for x in labels if x != fixed and (int(x in bp), int(x in br)) == sig]
            dst = [e for e in range(1024) if e not in cores[side] and e != image and
                   (int(e in residuals[0]), int(e in residuals[1])) == sig]
            check(f'side {side} signature {sig} equal lengths', len(src), len(dst))
            mapping.update(zip(src, dst))
        check(f'side {side} full domain', set(mapping) == set(labels), True)
        check(f'side {side} bijection', set(mapping.values()) == set(range(1024))-cores[side], True)
        check(f'side {side} saved full map', saved['sides'][side]['map'],
              [dict(label=list(x), image=h[mapping[x]], exponent=mapping[x]) for x in labels])
        maps.append([[mapping[('g', t, y)] for y in range(Q)] for t in T])
    check('right graph labels all avoid a', all(e != 0 for col in maps[1] for e in col), True)
    check('index count and budget', [N, N-THRESHOLD], [2571353, BUDGET])
    if any(not x['passed'] for x in checks):
        (OUT/'input-failure.json').write_text(json.dumps(checks, indent=2)+'\n')
        raise SystemExit('input failure; no scan')
    input_path = OUT / 'map-exponents.txt'
    input_path.write_text('\n'.join(' '.join(map(str, col)) for side in maps for col in side)+'\n')
    binary = OUT / 'scan-bin'
    compile_cmd = ['cc', '-std=c11', '-O2', '-Wall', '-Wextra',
                   str(HERE/'three_shift_conflicts.c'), '-o', str(binary)]
    subprocess.run(compile_cmd, check=True)
    result = subprocess.run([str(binary), str(input_path), str(OUT)],
                            check=True, text=True, capture_output=True)
    scan = json.loads(result.stdout)
    check('C complete support cardinalities', scan['bad_support_sizes'], 0)
    check('C exact shift scope', [s['c'] for s in scan['shifts']], SHIFTS)

    # Complete independent replay uses arbitrary-precision integer bitsets,
    # Horner evaluation and whole lines of constant coefficients. It does
    # not read C's individual pairs to choose which comparisons to perform.
    all_counts = [(OUT/f'shift-{c}-intersections.u8').read_bytes() for c in SHIFTS]
    for c, counts in zip(SHIFTS, all_counts):
        check(f'c={c} complete intersection file length', len(counts), N)
    masks = [[[1 << e for e in col] for col in side] for side in maps]
    core_masks = [sum(1 << e for e in s) for s in cores]
    replay_hist = [Counter() for _ in SHIFTS]
    replay_bad_sizes = 0
    mismatches = []
    total_mismatches = 0
    for w in range(Q):
        for v in range(Q):
            bases = [((w*t+v)*t) % Q for t in T]
            lines = [[], []]
            for side in range(2):
                for u in range(Q):
                    support = core_masks[side]
                    for j, base in enumerate(bases):
                        support |= masks[side][j][(base+u) % Q]
                    replay_bad_sizes += support.bit_count() != 68
                    lines[side].append(support)
            offset = (w*Q+v)*Q
            for k, c in enumerate(SHIFTS):
                for u, left in enumerate(lines[0]):
                    actual = (left & lines[1][(u+c) % Q]).bit_count()
                    replay_hist[k][actual] += 1
                    if actual != all_counts[k][offset+u]:
                        total_mismatches += 1
                        if len(mismatches) < 20:
                            mismatches.append(dict(c=c, index=offset+u, actual=actual,
                                                   stored=all_counts[k][offset+u]))
    check('independent replay support sizes', replay_bad_sizes, 0)
    check('independent replay all intersection entries', total_mismatches, 0)
    manifest = []
    for k, c in enumerate(SHIFTS):
        info = scan['shifts'][k]
        counts = all_counts[k]
        hist = [counts.count(i) for i in range(69)]
        check(f'c={c} full histogram from bytes', hist, info['histogram'])
        check(f'c={c} full replay histogram', [replay_hist[k][i] for i in range(69)], hist)
        check(f'c={c} total candidates', sum(hist), N)
        check(f'c={c} no equal supports', hist[68], 0)
        check(f'c={c} C repeated endpoints', info['repeated_tagged_endpoints'], 0)
        edge_path = OUT / f'shift-{c}-conflicts.u32'
        raw = edge_path.read_bytes()
        check(f'c={c} full edge byte length', len(raw), 12*info['matching_size'])
        records = struct.iter_unpack('<III', raw)
        left_seen, right_seen = bytearray(N), bytearray(N)
        bad_record, repeats, edge_count = 0, 0, 0
        for f, intersection in enumerate(counts):
            if 63 < intersection < 68:
                triple = next(records, None)
                g = f-f % Q+(f % Q+c) % Q
                bad_record += triple != (f, g, intersection)
                repeats += bool(left_seen[f] or right_seen[g])
                left_seen[f] = right_seen[g] = 1
                edge_count += 1
        check(f'c={c} all edge records exact and complete', bad_record, 0)
        check(f'c={c} no extra records', next(records, None), None)
        check(f'c={c} disjoint tagged endpoints', repeats, 0)
        check(f'c={c} unique endpoint counts', [sum(left_seen), sum(right_seen)], [edge_count]*2)
        check(f'c={c} qualifying counts', edge_count, sum(hist[64:68]))
        check(f'c={c} C matching size', info['matching_size'], edge_count)
        manifest.append(dict(c=c, candidates=N, matching_size=edge_count,
            nonqualifying=dict(intersection_at_most_63=sum(hist[:64]), equal_supports=hist[68]),
            histogram={str(i): n for i, n in enumerate(hist) if n},
            required_matching_size=2*BUDGET+1, succeeds=edge_count>2*BUDGET,
            retained_size_sum_bound=2*N-edge_count,
            maximum_smaller_side=(2*N-edge_count)//2,
            files=[dict(path=str(p.relative_to(ROOT)), bytes=p.stat().st_size, sha256=digest(p))
                   for p in [OUT/f'shift-{c}-intersections.u8', edge_path]]))
    failures = [x['name'] for x in checks if not x['passed']]
    cert = dict(parameters=dict(q=Q,T=T,shifts=SHIFTS,index='((w*q)+v)*q+u',
                retention_threshold=THRESHOLD,deletion_budget=BUDGET,
                required_matching_size=2*BUDGET+1,packing_maximum=63),
        inputs=[dict(path=str(p.relative_to(ROOT)),sha256=digest(p)) for p in
                [source,HERE/'three_shift_conflicts.c',Path(__file__).resolve(),input_path]],
        map_exponents=maps, C_scan=scan, independent_replay=dict(candidates_per_shift=N,
            total_comparisons=3*N, mismatches=total_mismatches,first_mismatches=mismatches),
        shifts=manifest,checks=checks,failures=failures,
        limitations=dict(rank_tested=False,other_shifts_tested=False,
                         arbitrary_maps_excluded=False,RS_list_bound_proved=False))
    output = OUT/'certificate.json'
    output.write_text(json.dumps(cert,indent=2)+'\n')
    print(json.dumps(dict(outcome='PASS' if not failures else 'FAIL',
        checks=len(checks),complete_replay_comparisons=3*N,
        required_matching_size=2*BUDGET+1,
        matching_sizes={str(s['c']):s['matching_size'] for s in manifest},
        failures=failures,certificate=str(output.relative_to(ROOT)))))
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
