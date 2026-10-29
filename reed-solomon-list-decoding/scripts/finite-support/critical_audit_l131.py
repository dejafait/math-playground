"""Independent complete-map verification of L131; no rank recomputation.

Inputs are read-only. Reconstruct subgroup points by recurrence and verify
the saved maps by their full inverse partitions and ordered-class ranks.
"""
import hashlib
import json
from itertools import combinations
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
OUTPUT = HERE / 'l131-critical-audit.json'
checks = []


def equal(name, actual, required):
    # Normalize finite tuples to the JSON representation before comparison.
    actual = json.loads(json.dumps(actual))
    required = json.loads(json.dumps(required))
    checks.append(dict(name=name, actual=actual, required=required,
                       passed=actual == required))


def main():
    filenames = ['mixed-core-l031-embedding.json',
                 'four-support-rank-results.json',
                 'four-support-audit-results.json']
    raw = {n: (HERE / n).read_bytes() for n in filenames}
    saved, original, old_audit = [json.loads(raw[n]) for n in filenames]
    hashes = {n: hashlib.sha256(raw[n]).hexdigest() for n in filenames}
    prime, generator, q = 65537, 19139, 137
    ts = [16, 64, 70, 102, 112, 118, 121]
    h = [1]
    for _ in range(1023):
        h.append(h[-1] * generator % prime)
    exponent = {point: e for e, point in enumerate(h)}
    equal('subgroup recurrence closes', h[-1] * generator % prime, 1)
    equal('distinct subgroup points', len(set(h)), 1024)
    equal('generator half power', h[512], prime - 1)
    equal('all saved parameters', saved['parameters'],
          dict(P=prime, generator=generator, q=q, T=ts))
    equal('original field parameters', [original['modulus'], original['generator']],
          [prime, generator])
    equal('full domain in embedding certificate', saved['domain'], h)
    equal('full domain in rank input', original['domain'], h)
    equal('full domain in prior rank audit', old_audit['domain'], h)
    equal('prior audited source is current rank input',
          old_audit['source_sha256'], hashes[filenames[1]])
    equal('embedding source hash is current rank input',
          saved['source']['sha256'], hashes[filenames[1]])
    equal('embedding source path', saved['source']['path'],
          'scripts/finite-support/four-support-rank-results.json')
    equal('embedding does not claim a new rank computation',
          saved['source']['rank_recomputed'], False)
    equal('original failures', original['failures'], [])
    equal('prior rank-audit failures', old_audit['failures'], [])

    edges = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
    pair_sets = [h[2*i:2*i+2] for i in range(6)]
    core = h[12:72]
    private = [h[72+2*i:74+2*i] for i in range(4)]
    supports = [set(core + private[i] + [x for e, pair in
                zip(edges, pair_sets) if i in e for x in pair]) for i in range(4)]
    equal('all 80 configuration labels are distinct',
          len(set(core + sum(pair_sets, []) + sum(private, []))), 80)
    for source_name, case in [('rank source', original['cases']['consecutive']),
                              ('prior rank audit', old_audit['cases']['consecutive'])]:
        equal(source_name+' full ordered pair sets', case['pairs'], pair_sets)
        equal(source_name+' full ordered core', case['core'], core)
        equal(source_name+' full ordered private sets', case['private'], private)
        equal(source_name+' all complete supports', case['supports'],
              [sorted(s) for s in supports])
    equal('saved ordered pair sets', saved['pair_sets'], pair_sets)
    equal('saved ordered core', saved['core'], core)
    equal('saved ordered private sets', saved['private'], private)
    equal('saved exponent-ordered supports', saved['supports'],
          [sorted(s, key=exponent.get) for s in supports])
    imported = dict(rank=12, nullity=0, augmented_ranks=[12]*6,
                    six_noncontainments=[False]*6, realizable=False,
                    agreement_counts=None)
    for name, actual in [('original', original['summary']['consecutive']),
                         ('prior audit', old_audit['summary']['consecutive']),
                         ('embedding import', saved['source']['imported_summary'])]:
        equal(name+' imported theorem summary (not a rank reproof)', actual, imported)
    a, b = h[0], h[10]
    cores = [set(core + [a]), set(core + [b])]
    equal('distinguished points', [saved['a'], saved['b']], [a, b])
    equal('saved full cores', saved['cores'],
          [sorted(c, key=exponent.get) for c in cores])
    labels = [('g', t, y) for t in ts for y in range(q)] + [('d', d) for d in range(4)]
    blocks = [{('g', t, 0) for t in ts},
              {('g', t, (t-16) % q) for t in ts}]
    equal('saved graph blocks in domain order', saved['blocks'],
          [[x for x in labels if x in block] for block in blocks])
    signature = lambda x, pair: (int(x in pair[0]), int(x in pair[1]))
    required_counts = [950, 6, 6, 1]
    sigs = [(0, 0), (0, 1), (1, 0), (1, 1)]
    all_maps = []
    for side_number, (name, vertices, fixed, fixed_image) in enumerate([
        ('left', [0, 1], ('g', 16, 1), b),
        ('right', [2, 3], ('d', 0), a),
    ]):
        side = saved['sides'][side_number]
        target = set(h) - cores[side_number]
        residuals = [supports[v] - cores[side_number] for v in vertices]
        entries = side['map']
        keys = [tuple(row['label']) for row in entries]
        images = [row['image'] for row in entries]
        equal(name+' saved side', side['side'], name)
        equal(name+' all domain labels in exact order', keys, labels)
        equal(name+' exact map length', len(entries), 963)
        equal(name+' image set is whole target', sorted(set(images)), sorted(target))
        equal(name+' image injectivity', len(set(images)), 963)
        mapping = dict(zip(keys, images))
        equal(name+' fixed-label record', side['fixed_label'], fixed)
        equal(name+' fixed-image record', side['fixed_image'], fixed_image)
        equal(name+' distinguished assignment', mapping[fixed], fixed_image)
        counts, ordered_evidence = [], []
        for sig, count in zip(sigs, required_counts):
            domain_class = [x for x in labels if signature(x, blocks) == sig]
            image_class = [x for x in h if x in target and signature(x, residuals) == sig]
            equal(name+f' domain class {sig}', len(domain_class), count)
            equal(name+f' target class {sig}', len(image_class), count)
            remaining_domain = [x for x in domain_class if x != fixed]
            remaining_target = [x for x in image_class if x != fixed_image]
            required_remaining = count - int(sig == (0, 0))
            equal(name+f' remaining class sizes {sig}',
                  [len(remaining_domain), len(remaining_target)],
                  [required_remaining]*2)
            # Verify every image by its rank in this ordered signature class.
            expected_images = {x: remaining_target[i] for i, x in enumerate(remaining_domain)}
            if sig == (0, 0):
                expected_images[fixed] = fixed_image
            for x in domain_class:
                equal(name+' complete map entry '+str(x), mapping[x], expected_images[x])
            ordered_evidence.append(dict(signature=sig,
                domain=remaining_domain, targets=remaining_target))
            counts.append(dict(signature=sig, domain=count, target=count,
                remaining_domain=required_remaining, remaining_target=required_remaining))
        equal(name+' complete signature table', side['signature_counts'], counts)
        equal(name+' every saved exponent', [row['exponent'] for row in entries],
              [exponent[y] for y in images])
        graph_images = [{mapping[x] for x in block} for block in blocks]
        equal(name+' both residual identities',
              [sorted(s) for s in graph_images], [sorted(s) for s in residuals])
        equal(name+' both full support identities',
              [sorted(cores[side_number] | s) for s in graph_images],
              [sorted(supports[v]) for v in vertices])
        equal(name+' saved full block images', side['block_images'],
              [sorted(s, key=exponent.get) for s in graph_images])
        equal(name+' common graph image', mapping[('g', 16, 0)], h[1 if side_number == 0 else 11])
        all_maps.append(dict(side=name, entries=entries, ordered_classes=ordered_evidence,
                             residuals=[sorted(s, key=exponent.get) for s in residuals]))
    equal('all left selected supports omit b', [b in supports[i] for i in [0, 1]], [False]*2)
    right_map = {tuple(e['label']): e['image'] for e in saved['sides'][1]['map']}
    equal('entire inverse image of a on right', [x for x in labels if right_map[x] == a], [('d', 0)])
    equal('all 959 right graph labels avoid a',
          sum(right_map[x] == a for x in labels if x[0] == 'g'), 0)
    equal('right core omits a', a in cores[1], False)
    intersections = []
    for size in range(2, 5):
        for vertices in combinations(range(4), size):
            intersection = set.intersection(*(supports[v] for v in vertices))
            required = set(core)
            if size == 2:
                required |= set(pair_sets[edges.index(vertices)])
            equal('complete intersection '+str(vertices), sorted(intersection), sorted(required))
            equal('intersection cardinality '+str(vertices), len(intersection), 62 if size == 2 else 60)
            intersections.append(dict(indices=[v+1 for v in vertices], size=len(intersection),
                points=sorted(intersection, key=exponent.get)))
    equal('all saved intersections', saved['intersections'], intersections)
    equal('all support cardinalities', [len(s) for s in supports], [68]*4)
    equal('all core cardinalities', [len(c) for c in cores], [61]*2)
    equal('actual pair maximum versus packing threshold',
          max(len(supports[i] & supports[j]) for i, j in edges) <= 63, True)
    equal('all recorded scope limits', saved['limitations'],
          dict(retention_survival_proved=False, large_retention_for_this_labeling_proved=False,
               universal_occurrence_proved=False, RS_list_bound_claimed=False))
    equal('embedding failures', saved['failures'], [])
    equal('all 84 original checks present', len(saved['checks']), 84)
    for record in saved['checks']:
        equal('original record arithmetic: '+record['name'], record['actual'], record['required'])
        equal('original record success flag: '+record['name'], record['passed'], True)
    for n in filenames:
        equal('input remains byte-identical: '+n, (HERE / n).read_bytes() == raw[n], True)
    failures = [c['name'] for c in checks if not c['passed']]
    cert = dict(input_hashes=hashes, domain=h, pairs=pair_sets, core=core, private=private,
        supports=[sorted(s, key=exponent.get) for s in supports], maps=all_maps,
        intersections=intersections, imported_rank_recomputed=False,
        checks=checks, failures=failures)
    OUTPUT.write_text(json.dumps(cert, indent=2)+'\n')
    print(json.dumps(dict(outcome='PASS' if not failures else 'FAIL', checks=len(checks),
        map_entries_checked=sum(len(m['entries']) for m in all_maps), required_map_entries=1926,
        support_sizes=[len(s) for s in supports], required_support_size=68,
        pair_intersection_maximum=max(len(supports[i] & supports[j]) for i, j in edges),
        required_pair_maximum=63,
        higher_intersection_sizes=[x['size'] for x in intersections if len(x['indices']) > 2],
        required_higher_intersection_size=60, rank_recomputed=False,
        failures=failures, certificate=str(OUTPUT.relative_to(ROOT)))))
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
