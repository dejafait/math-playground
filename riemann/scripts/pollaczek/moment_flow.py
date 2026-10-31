"""Bounded degree-six test; exact arithmetic, no external packages.

Run from the notebook: python3 scripts/pollaczek/moment_flow.py
Polynomials are coefficient lists in ascending order.
"""
from fractions import Fraction as F
from pathlib import Path
import json
import random


def trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def add(p, q):
    return trim([(p[i] if i < len(p) else F(0)) +
                 (q[i] if i < len(q) else F(0))
                 for i in range(max(len(p), len(q)))])


def scale(p, a):
    return trim([a * c for c in p])


def remainder(p, q):
    p, q = trim(p), trim(q)
    assert q != [0]
    while p != [0] and len(p) >= len(q):
        k, c = len(p) - len(q), p[-1] / q[-1]
        p = add(p, [F(0)] * k + scale(q, -c))
    return p


def derivative(p):
    return trim([i * p[i] for i in range(1, len(p))] or [F(0)])


def sturm(p):
    chain = [trim(p), derivative(p)]
    while chain[-1] != [0]:
        rem = scale(remainder(chain[-2], chain[-1]), -1)
        if rem == [0]:
            break
        # Positive rescaling limits fraction size without changing signs.
        chain.append(scale(rem, 1 / abs(rem[-1])))
    return chain


def variations(values):
    signs = [1 if v > 0 else -1 for v in values if v != 0]
    return sum(a != b for a, b in zip(signs, signs[1:]))


def count_positive(p):
    assert p[0] != 0
    chain = sturm(p)
    return variations([s[0] for s in chain]) - variations([s[-1] for s in chain])


def squarefree(p):
    return len(sturm(p)[-1]) == 1


def basis():
    # g_n(t)=f_n(t/2), so (n+1)g_(n+1)=t*g_n-(n+1/2)g_(n-1).
    g = [[F(1)], [F(0), F(1)]]
    for n in range(1, 6):
        g.append(scale(add([F(0)] + g[n], scale(g[n-1], -F(2*n+1, 2))), F(1, n+1)))
    return [[g[n][k] for k in range(0, n+1, 2)] for n in (0, 2, 4, 6)]


def cubic(even, q, u, v, r):
    p = [F(0)]
    for j in range(4):
        m = (1-q)*u**j + q*v**j
        p = add(p, scale(even[j], (-1)**j * m * r**(2*j)))
    return p


def strings(p):
    return [str(c) for c in p]


def main():
    out = Path(__file__).parent
    even = basis()
    rng = random.Random(20261030)
    rows, successes, witness = [], 0, None
    # Uniform deterministic draws on denominator-32 grids, conditioned only
    # on degree six; r0 in [1/32,31/32], r1 in [(32*r0+1)/32,1].
    while len(rows) < 10000:
        q = F(rng.randrange(33), 32)
        u, v = sorted([F(rng.randrange(33), 32), F(rng.randrange(1, 33), 32)])
        a = rng.randrange(1, 32)
        r0, r1 = F(a, 32), F(rng.randrange(a+1, 33), 32)
        if (1-q)*u**3 + q*v**3 == 0:
            continue
        p0, p1 = cubic(even, q, u, v, r0), cubic(even, q, u, v, r1)
        n0, n1 = count_positive(p0), count_positive(p1)
        sf0, sf1 = squarefree(p0), squarefree(p1)
        initial = n0 == 3 and sf0
        successes += initial
        row = dict(parameters=strings([q,u,v,r0,r1]), positive_roots=[n0,n1],
                   squarefree=[sf0,sf1], initial_simple_hyperbolic=initial)
        rows.append(row)
        # Final squarefree with fewer than three positive roots gives an
        # exact deficit, with no repeated-root ambiguity.
        if initial and sf1 and n1 < 3:
            witness = dict(index=len(rows)-1, **row,
                           cubic_coefficients=[strings(p0),strings(p1)],
                           sturm_chains=[[strings(s) for s in sturm(p)] for p in [p0,p1]])
            break
    data = dict(basis_cubics=[strings(p) for p in even], seed=20261030,
                selection="Python Random; denominator-32 grids as specified in main()",
                required_maximum_tuples=10000, tested_tuples=len(rows),
                denominator_bound=32, initial_hyperbolicity_successes=successes,
                witness=witness, tuples=rows,
                result="COUNTEREXAMPLE" if witness else "INCONCLUSIVE_NO_WITNESS",
                failures=[])
    path = out / "moment-flow-certificate.json"
    path.write_text(json.dumps(data, indent=2) + "\n")
    print(json.dumps({k:data[k] for k in ["result","tested_tuples","required_maximum_tuples",
          "denominator_bound","initial_hyperbolicity_successes","failures"]}))
    print("Certificate:", path)
    print("Basis cubics:", data["basis_cubics"])


if __name__ == "__main__":
    main()
