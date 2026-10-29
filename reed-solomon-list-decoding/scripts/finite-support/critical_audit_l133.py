"""Read-only replay of L133 using actual labels and small sets, not bitsets.

Run from the active notebook: python3 scripts/finite-support/critical_audit_l133.py
Only the separate audit certificate is written. All production bytes are read.
"""
import hashlib
import json
from pathlib import Path
import struct

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
DIR = HERE / 'three-shift-conflicts'
Q, N, THRESHOLD = 137, 137**3, 1532496
T = [16, 64, 70, 102, 112, 118, 121]
SHIFTS = [0, 1, -1]
checks = []


def check(name, actual, required):
    checks.append(dict(name=name, actual=actual, required=required,
                       passed=(actual == required)))


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def file_info(path):
    return dict(path=str(path.relative_to(ROOT)), bytes=path.stat().st_size,
                sha256=digest(path))


def main():
    cert_path = DIR / 'certificate.json'
    source = HERE / 'mixed-core-l031-embedding.json'
    cert = json.loads(cert_path.read_text())
    saved = json.loads(source.read_text())
    h = [pow(19139, e, 65537) for e in range(1024)]
    exponent = {x: e for e, x in enumerate(h)}
    check('all subgroup labels distinct', len(exponent), 1024)
    check('subgroup closure', pow(19139, 1024, 65537), 1)
    check('source complete subgroup domain', saved['domain'], h)
    check('source parameters', saved['parameters'],
          dict(P=65537, generator=19139, q=Q, T=T))
    check('source failures', saved['failures'], [])
    core = set(h[12:72])
    cores = [core | {h[0]}, core | {h[10]}]
    # Explicit original edge order 12,13,14,23,24,34, independent of
    # combinations() and the production signature-construction code.
    incident_pairs = [[0, 1, 2], [0, 3, 4], [1, 3, 5], [2, 4, 5]]
    supports = []
    for vertex in range(4):
        support = core | set(h[72+2*vertex:74+2*vertex])
        for edge in incident_pairs[vertex]:
            support.update(h[2*edge:2*edge+2])
        supports.append(support)
    check('source four actual supports', saved['supports'],
          [[h[e] for e in range(1024) if h[e] in s] for s in supports])
    check('source two actual cores', saved['cores'],
          [[h[e] for e in range(1024) if h[e] in s] for s in cores])
    labels = [('g', t, y) for t in T for y in range(Q)]
    labels += [('d', i) for i in range(4)]
    domain_sig = {}
    for label in labels:
        if label[0] == 'd':
            domain_sig[label] = (False, False)
        else:
            _, t, y = label
            domain_sig[label] = (y == 0, y == (t-16) % Q)
    maps, full_maps = [], []
    for side in range(2):
        fixed = ('g', 16, 1) if side == 0 else ('d', 0)
        image = h[10] if side == 0 else h[0]
        residues = [supports[2*side+i] - cores[side] for i in range(2)]
        queues = {sig: [] for sig in [(False, False), (False, True),
                                     (True, False), (True, True)]}
        for actual in h:
            if actual not in cores[side] and actual != image:
                queues[(actual in residues[0], actual in residues[1])].append(actual)
        positions = dict.fromkeys(queues, 0)
        mapping = {}
        for label in labels:
            if label == fixed:
                mapping[label] = image
            else:
                sig = domain_sig[label]
                mapping[label] = queues[sig][positions[sig]]
                positions[sig] += 1
        check(f'side {side} signature queue exhaustion',
              list(positions.values()), [len(q) for q in queues.values()])
        check(f'side {side} signature counts after removal',
              [len(q) for q in queues.values()], [949, 6, 6, 1])
        check(f'side {side} bijective complement',
              sorted(mapping.values()), sorted(set(h)-cores[side]))
        check(f'side {side} fixed assignment', mapping[fixed], image)
        entries = [dict(label=list(x), image=mapping[x], exponent=exponent[mapping[x]])
                   for x in labels]
        check(f'side {side} every saved map entry', saved['sides'][side]['map'], entries)
        full_maps.append(mapping)
        maps.append([[mapping[('g', t, y)] for y in range(Q)] for t in T])
    check('right inverse image of a',
          [list(x) for x in labels if full_maps[1][x] == h[0]], [['d', 0]])
    exponents = [[[exponent[x] for x in col] for col in side] for side in maps]
    check('manifest all graph map entries', cert['map_exponents'], exponents)
    text = '\n'.join(' '.join(str(e) for e in col)
                     for side in exponents for col in side) + '\n'
    check('complete C exponent input including ordering',
          (DIR/'map-exponents.txt').read_text(), text)
    parameters = dict(q=Q, T=T, shifts=SHIFTS, index='((w*q)+v)*q+u',
                      retention_threshold=THRESHOLD, deletion_budget=N-THRESHOLD,
                      required_matching_size=2*(N-THRESHOLD)+1, packing_maximum=63)
    check('manifest parameters', cert['parameters'], parameters)
    paths = [source, HERE/'three_shift_conflicts.c',
             HERE/'three_shift_conflicts.py', DIR/'map-exponents.txt']
    check('all input paths and hashes', cert['inputs'],
          [dict(path=str(p.relative_to(ROOT)), sha256=digest(p)) for p in paths])
    check('manifest exact top-level scope', sorted(cert), sorted([
        'parameters', 'inputs', 'map_exponents', 'C_scan', 'independent_replay',
        'shifts', 'checks', 'failures', 'limitations']))
    check('original checks count', len(cert['checks']), 66)
    check('all original check outcomes internally exact',
          [x['name'] for x in cert['checks']
           if x['actual'] != x['required'] or x['passed'] is not True], [])
    check('original failures', cert['failures'], [])
    if any(not x['passed'] for x in checks):
        raise RuntimeError('input mismatch; do not scan a different instance')

    counts = [(DIR/f'shift-{c}-intersections.u8').read_bytes() for c in SHIFTS]
    raw = [(DIR/f'shift-{c}-conflicts.u32').read_bytes() for c in SHIFTS]
    for k, c in enumerate(SHIFTS):
        check(f'c={c} complete byte count', len(counts[k]), N)
        check(f'c={c} whole edge records', len(raw[k]) % 12, 0)
    records = [iter(struct.iter_unpack('<III', data)) for data in raw]
    seen_l, seen_r = [bytearray(N) for _ in SHIFTS], [bytearray(N) for _ in SHIFTS]
    hist = [[0]*69 for _ in SHIFTS]
    mismatches = [0]*3
    bad_edges, repeats, edge_count, equal = [0]*3, [0]*3, [0]*3, [0]*3
    bad_sizes, bad_core_images = 0, 0
    # Reconstruct both sides as sets of ACTUAL field elements, not exponent
    # bitsets. K is disjoint from all these sets, so complete intersection
    # size is |K| plus the small-set intersection. Check that premise for
    # every support, including every wrapping value u=0 and u=136.
    for w in range(Q):
        for v in range(Q):
            lines = [[], []]
            for u in range(Q):
                values = [(u + v*t + w*(t*t % Q)) % Q for t in T]
                for side in range(2):
                    extra = {h[0] if side == 0 else h[10]}
                    extra.update(maps[side][j][values[j]] for j in range(7))
                    bad_sizes += len(extra) != 8
                    bad_core_images += not extra.isdisjoint(core)
                    lines[side].append(extra)
            for u in range(Q):
                f = Q*Q*w+Q*v+u
                for k, c in enumerate(SHIFTS):
                    right_u = (u+c) % Q
                    g = Q*Q*w+Q*v+right_u
                    left, right = lines[0][u], lines[1][right_u]
                    s = 60 + len(left.intersection(right))
                    hist[k][s] += 1
                    equal[k] += left == right
                    mismatches[k] += counts[k][f] != s
                    if s > 63 and left != right:
                        triple = next(records[k], None)
                        bad_edges[k] += triple != (f, g, s)
                        repeats[k] += bool(seen_l[k][f] or seen_r[k][g])
                        seen_l[k][f] = seen_r[k][g] = 1
                        edge_count[k] += 1
    check('every actual support cardinality', bad_sizes, 0)
    check('every actual graph avoids K', bad_core_images, 0)
    expected_scan, expected_shifts = [], []
    for k, c in enumerate(SHIFTS):
        check(f'c={c} every independently recomputed byte', mismatches[k], 0)
        check(f'c={c} every actual cross support distinct', equal[k], 0)
        check(f'c={c} all edge triples exact', bad_edges[k], 0)
        check(f'c={c} no extra edge triple', next(records[k], None), None)
        check(f'c={c} edge length', len(raw[k]), edge_count[k]*12)
        check(f'c={c} disjoint tagged endpoints', repeats[k], 0)
        check(f'c={c} unique tagged endpoint counts',
              [sum(seen_l[k]), sum(seen_r[k])], [edge_count[k]]*2)
        check(f'c={c} histogram exhausts Q', sum(hist[k]), N)
        check(f'c={c} qualifying histogram', edge_count[k], sum(hist[k][64:68]))
        expected_scan.append(dict(c=c, matching_size=edge_count[k],
                                  repeated_tagged_endpoints=0, histogram=hist[k]))
        expected_shifts.append(dict(c=c, candidates=N, matching_size=edge_count[k],
            nonqualifying=dict(intersection_at_most_63=sum(hist[k][:64]),
                               equal_supports=equal[k]),
            histogram={str(s): n for s, n in enumerate(hist[k]) if n},
            required_matching_size=2*(N-THRESHOLD)+1,
            succeeds=edge_count[k] > 2*(N-THRESHOLD),
            retained_size_sum_bound=2*N-edge_count[k],
            maximum_smaller_side=(2*N-edge_count[k])//2,
            files=[file_info(DIR/f'shift-{c}-intersections.u8'),
                   file_info(DIR/f'shift-{c}-conflicts.u32')]))
    check('every C scan manifest field', cert['C_scan'],
          dict(bad_support_sizes=0, shifts=expected_scan))
    check('every independent replay manifest field', cert['independent_replay'],
          dict(candidates_per_shift=N, total_comparisons=3*N,
               mismatches=0, first_mismatches=[]))
    check('every shift manifest field including six whole-file hashes',
          cert['shifts'], expected_shifts)
    check('limitations exact', cert['limitations'],
          dict(rank_tested=False, other_shifts_tested=False,
               arbitrary_maps_excluded=False, RS_list_bound_proved=False))
    check('claimed three matching counts', edge_count, [1, 0, 2571300])
    arithmetic = dict(N=N, threshold=THRESHOLD, deletion_budget=N-THRESHOLD,
        required_matching=2*(N-THRESHOLD)+1, actual_matching=edge_count[2],
        size_sum_bound=2*N-edge_count[2], smaller_side=(2*N-edge_count[2])//2,
        surplus_over_required=edge_count[2]-(2*(N-THRESHOLD)+1),
        surplus_over_total_budget=edge_count[2]-2*(N-THRESHOLD),
        max_C_intermediate=136+136*121+136*121*121)
    check('all displayed final integers', arithmetic,
          dict(N=2571353, threshold=1532496, deletion_budget=1038857,
               required_matching=2077715, actual_matching=2571300,
               size_sum_bound=2571406, smaller_side=1285703,
               surplus_over_required=493585, surplus_over_total_budget=493586,
               max_C_intermediate=2007768))
    check('threshold really excluded', arithmetic['smaller_side'] < THRESHOLD, True)
    failures = [x['name'] for x in checks if not x['passed']]
    output = HERE/'l133-critical-audit.json'
    audit = dict(method='actual-label small-set independent replay; no production imports',
        inputs=[dict(path=str(p.relative_to(ROOT)), sha256=digest(p))
                for p in [cert_path, *paths, Path(__file__).resolve()]],
        complete_replay=dict(comparisons=3*N, map_entries=2*len(labels),
            intersections_mismatched=mismatches, edge_records_verified=edge_count,
            edge_records_mismatched=bad_edges, histograms=hist),
        arithmetic=arithmetic, checks=checks, failures=failures)
    output.write_text(json.dumps(audit, indent=2)+'\n')
    print(json.dumps(dict(outcome='FAIL' if failures else 'PASS', checks=len(checks),
        complete_comparisons=3*N, matching_sizes=edge_count,
        actual_matching=arithmetic['actual_matching'],
        required_matching=arithmetic['required_matching'],
        size_sum_bound=arithmetic['size_sum_bound'], smaller_side=arithmetic['smaller_side'],
        failures=failures, certificate=str(output.relative_to(ROOT)))))
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
