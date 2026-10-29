"""Exact prescribed ambient embedding; imports L031, never recomputes its rank.

Run from the active notebook. Complete bijections and every check go to disk.
"""
import hashlib
import json
from itertools import combinations
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / 'four-support-rank-results.json'
OUTPUT = HERE / 'mixed-core-l031-embedding.json'
P, G, Q = 65537, 19139, 137
T = [16, 64, 70, 102, 112, 118, 121]
checks = []


def check(name, actual, required):
    checks.append(dict(name=name, actual=actual, required=required,
                       passed=actual == required))


def main():
    source_bytes = SOURCE.read_bytes()
    source = json.loads(source_bytes)
    old = source['cases']['consecutive']
    domain = [pow(G, e, P) for e in range(1024)]
    exponent = {x: e for e, x in enumerate(domain)}
    edges = list(combinations(range(4), 2))
    pairs = [[domain[2*r], domain[2*r+1]] for r in range(6)]
    core = set(domain[12:72])
    private = [domain[72+2*i:74+2*i] for i in range(4)]
    supports = [core | set(private[i]) | {
        x for edge, pair in zip(edges, pairs) if i in edge for x in pair
    } for i in range(4)]
    check('source modulus', source['modulus'], P)
    check('source generator', source['generator'], G)
    check('full source domain', source['domain'], domain)
    check('full source pair sets', old['pairs'], pairs)
    check('full source core', old['core'], domain[12:72])
    check('full source private sets', old['private'], private)
    check('all four complete source supports', old['supports'],
          [sorted(s) for s in supports])
    check('source recorded failures', source['failures'], [])
    # Record the already audited input, without treating a summary as a rank proof.
    check('imported consecutive summary', source['summary']['consecutive'],
          dict(rank=12, nullity=0, augmented_ranks=[12]*6,
               six_noncontainments=[False]*6, realizable=False,
               agreement_counts=None))
    check('generator order power', pow(G, 1024, P), 1)
    check('generator half power', pow(G, 512, P), P-1)
    check('distinct subgroup points', len(exponent), 1024)
    a, b = domain[0], domain[10]
    cores = [core | {a}, core | {b}]
    labels = [('g', t, y) for t in T for y in range(Q)]
    labels += [('d', i) for i in range(4)]
    blocks = [set(('g', t, 0) for t in T),
              set(('g', t, (t-16) % Q) for t in T)]
    signatures = [(0, 0), (0, 1), (1, 0), (1, 1)]
    maps = []
    side_results = []
    for side, indices, fixed, value in [
        ('left', (0, 1), ('g', 16, 1), b),
        ('right', (2, 3), ('d', 0), a),
    ]:
        j = len(maps)
        target = set(domain) - cores[j]
        residuals = [supports[i] - cores[j] for i in indices]
        dsig = lambda x: tuple(int(x in block) for block in blocks)
        tsig = lambda x: tuple(int(x in residual) for residual in residuals)
        check(side+' core contained in both supports',
              all(cores[j] <= supports[i] for i in indices), True)
        check(side+' prescribed signature compatibility', dsig(fixed), tsig(value))
        check(side+' prescribed signature', dsig(fixed), (0, 0))
        check(side+' prescribed image in target', value in target, True)
        mapping = {fixed: value}
        counts = []
        for sig in signatures:
            src = [x for x in labels if dsig(x) == sig]
            dst = [x for x in domain if x in target and tsig(x) == sig]
            remaining_src = [x for x in src if x != fixed]
            remaining_dst = [x for x in dst if x != value]
            check(side+f' full signature {sig}', len(src), len(dst))
            check(side+f' remaining signature {sig}',
                  len(remaining_src), len(remaining_dst))
            counts.append(dict(signature=sig, domain=len(src), target=len(dst),
                               remaining_domain=len(remaining_src),
                               remaining_target=len(remaining_dst)))
            mapping.update(zip(remaining_src, remaining_dst))
        check(side+' full domain', set(mapping) == set(labels), True)
        check(side+' map size', len(mapping), 963)
        check(side+' injective image size', len(set(mapping.values())), 963)
        check(side+' surjective target', set(mapping.values()) == target, True)
        check(side+' distinguished assignment', mapping[fixed], value)
        images = [{mapping[x] for x in block} for block in blocks]
        for k, i in enumerate(indices):
            check(side+f' block {k} exact residual', images[k] == residuals[k], True)
            check(side+f' block {k} exact support', cores[j] | images[k] == supports[i], True)
        maps.append(mapping)
        side_results.append(dict(side=side, signature_counts=counts,
            fixed_label=fixed, fixed_image=value,
            map=[dict(label=x, image=mapping[x], exponent=exponent[mapping[x]])
                 for x in labels],
            block_images=[sorted(x, key=exponent.get) for x in images]))
    intersections = []
    for size in range(2, 5):
        for indices in combinations(range(4), size):
            actual = set.intersection(*(supports[i] for i in indices))
            expected = core | (set(pairs[edges.index(indices)]) if size == 2 else set())
            check('intersection '+str(indices), actual == expected, True)
            check('intersection size '+str(indices), len(actual), 62 if size == 2 else 60)
            intersections.append(dict(indices=[i+1 for i in indices],
                size=len(actual), points=sorted(actual, key=exponent.get)))
    check('support sizes', [len(s) for s in supports], [68]*4)
    check('core sizes', [len(c) for c in cores], [61, 61])
    check('core common part', cores[0] & cores[1] == core, True)
    check('all pairs meet packing bound',
          max(len(supports[i] & supports[j]) for i, j in edges) <= 63, True)
    check('left selected supports omit b', all(b not in supports[i] for i in [0, 1]), True)
    check('right selected supports omit a', all(a not in supports[i] for i in [2, 3]), True)
    check('right inverse image of a is dummy',
          [x for x, y in maps[1].items() if y == a], [('d', 0)])
    # Every graph block uses graph labels only; hence this exact inverse image
    # certifies the empty right ambient star without enumerating q^3 blocks.
    check('all graph labels avoid a on right',
          all(y != a for x, y in maps[1].items() if x[0] == 'g'), True)
    failures = [c['name'] for c in checks if not c['passed']]
    cert = dict(parameters=dict(P=P, generator=G, q=Q, T=T),
        source=dict(path=str(SOURCE.relative_to(HERE.parent.parent)),
                    sha256=hashlib.sha256(source_bytes).hexdigest(),
                    imported_summary=source['summary']['consecutive'],
                    rank_recomputed=False),
        domain=domain, pair_sets=pairs, core=domain[12:72], private=private,
        supports=[sorted(s, key=exponent.get) for s in supports],
        a=a, b=b, cores=[sorted(c, key=exponent.get) for c in cores],
        blocks=[sorted(block, key=labels.index) for block in blocks],
        sides=side_results, intersections=intersections, checks=checks,
        limitations=dict(retention_survival_proved=False,
                         large_retention_for_this_labeling_proved=False,
                         universal_occurrence_proved=False,
                         RS_list_bound_claimed=False), failures=failures)
    OUTPUT.write_text(json.dumps(cert, indent=2)+'\n')
    print(json.dumps(dict(outcome='PASS' if not failures else 'FAIL',
        checks=len(checks), map_sizes=[len(m) for m in maps], required_map_size=963,
        support_sizes=[len(s) for s in supports], required_support_size=68,
        pair_intersection_sizes=[len(supports[i] & supports[j]) for i, j in edges],
        required_pair_maximum=63, higher_intersection_size=60,
        empty_right_star=True if not failures else None,
        failures=failures, certificate=str(OUTPUT.relative_to(HERE.parent.parent)))))
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
