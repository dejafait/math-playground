"""Exact bounded auxiliary-point search for the prescribed moment extension."""
import itertools
import json
import math
from pathlib import Path
import random

Q = 137
SEED = 137007
LIMIT = 1000


def matchings(xs):
    if not xs:
        yield ()
        return
    a = xs[0]
    for i in range(1, len(xs)):
        b = xs[i]
        for rest in matchings(xs[1:i] + xs[i + 1:]):
            yield ((a, b),) + rest


def determinant(pairs):
    cols = [(a * b, -a - b, 1) for a, b in pairs]
    a, b, c = cols
    direct = (a[0] * (b[1] * c[2] - b[2] * c[1])
              - b[0] * (a[1] * c[2] - a[2] * c[1])
              + c[0] * (a[1] * b[2] - a[2] * b[1]))
    # Independent six-term permutation formula, using rows rather than columns.
    matrix = list(zip(*cols))
    expanded = 0
    for perm in itertools.permutations(range(3)):
        inversions = sum(perm[i] > perm[j] for i in range(3) for j in range(i + 1, 3))
        expanded += (-1)**inversions * math.prod(matrix[i][perm[i]] for i in range(3))
    assert direct == expanded
    return direct % Q


def rows_for(points):
    return [{"omitted": omitted, "pairs": pairs, "det_mod_137": determinant(pairs)}
            for omitted in points
            for pairs in matchings(tuple(x for x in points if x != omitted))]


def main():
    rng = random.Random(SEED)
    trials = []
    winner = None
    for attempt in range(LIMIT):
        points = tuple(range(7)) if attempt == 0 else tuple(sorted(rng.sample(range(Q), 7)))
        rows = rows_for(points)
        assert len(rows) == 105
        assert len({tuple(tuple(pair) for pair in row['pairs']) for row in rows}) == 105
        zeros = sum(row['det_mod_137'] == 0 for row in rows)
        trials.append({"points": points, "zero_count": zeros})
        if zeros == 0:
            winner = points
            break
    result = {"q": Q, "seed": SEED, "limit": LIMIT, "trials": trials,
              "points": winner, "matching_rows": rows if winner else [],
              "scope": "Finite auxiliary certificate; symbolic proof required for all-core moments."}
    if winner:
        result['determinants_by_omitted'] = {
            str(x): [r['det_mod_137'] for r in rows if r['omitted'] == x] for x in winner}
        histogram = [0] * 8
        polynomials = [(1, 0, 0)] + [(b, 1, 0) for b in range(Q)]
        polynomials += [(b, a, 1) for a in range(Q) for b in range(Q)]
        for b, a, c in polynomials:
            roots = sum((b + a*x + c*x*x) % Q == 0 for x in winner)
            histogram[roots] += 1
        d = [(Q-1)*histogram[i] for i in range(3)]
        result['monic_root_histogram'] = histogram
        result['neighbor_counts'] = d
        result['checks'] = {
            "prime": all(Q % d for d in range(2, math.isqrt(Q)+1)),
            "seven_distinct": len(set(winner)) == 7,
            "all_105_nonzero": len(rows) == 105 and all(r['det_mod_137'] for r in rows),
            "no_more_than_two_roots": not any(histogram[3:]),
            "unchanged_counts": d == [2442832, 125664, 2856],
            "total_neighbors": sum(d) == Q**3-1,
            "root_incidence": d[1] + 2*d[2] == 7*(Q**2-1),
            "above_required_cap": Q**3 > 1532495,
            "ambient_size": 7*Q+4 == 963,
        }
    path = Path(__file__).with_name('shared-degree-four-results.json')
    path.write_text(json.dumps(result, indent=2) + '\n')
    print(f"Candidate: {winner}; trials: {len(trials)}/{LIMIT}")
    print(f"Nonzero determinants: {105-sum(r['det_mod_137']==0 for r in rows)}/105")
    print(f"Independent-family size: {Q**3}; required cap: <=1532495")
    failures = [k for k, v in result.get('checks', {}).items() if not v]
    print(f"Failures: {failures if winner else ['no candidate']}; certificate: {path}")
    assert winner and not failures


if __name__ == '__main__':
    main()
