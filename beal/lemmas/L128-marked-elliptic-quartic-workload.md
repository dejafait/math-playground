# L128 — Minimal elliptic model and over-cap raw quartic workload

## Hypotheses

Use L112's nonsingular Q-elliptic model

    E': y²=x³−2874960x+1739350800.

Apply J.E. Cremona, *Algorithms for Modular Elliptic Curves*, second
edition, CUP 1997, corrected online edition, Chapter III Section 3.6,
Steps 1–2, pp.91–94. A raw row is an integer (a,b) in its coefficient
loops before syzygy, integrality, local or equivalence tests. A raw
triple also includes an integer c in that row's closed interval.
The saved caps are 200000 rows for workload counting and 2000000
triples for enumeration. No upper rank or generator claim is assumed.

## Conclusion

A reduced global minimal model is

    E_m: Y²+Y=X³−179685X+27177356,
    x=4X, y=8Y+4.

Its invariants are c4=8624880, c6=−23481235800 and
Delta=52212919952197125. Its rational two-torsion dimension is zero.
Cremona's Step 1 requires only (I,J)=(8624880,−46962471600).

The Step 2 maximal |a| values are 1043 (type 1, positive), 898
(type 2, positive) and 144 (type 2, negative). The complete raw row
count is 3834148; the type-one subregion 1<=a<=16 already has at least
2199936 raw triples. Both saved caps are exceeded. This stops the
unsieved loops, not descent itself. These are not counts of distinct
coverings or locally soluble classes; no Selmer or upper rank follows.

## Proof

### Normalization and two-torsion

Import Cremona, same edition, Chapter III Proposition 3.1.1 and
Sections 3.1–3.2, pp.63–65, with coordinate change (3.1.2), pp.62–63:
[corrected Chapter III](https://johncremona.github.io/book/fulltext/chapter3.pdf).
This determines the maximal integer scaling u for which c4/u⁴,c6/u⁶
are invariants of an integral model, including its 2/3 conditions.
It is applied here, not reproved.

The original integral invariants factor as

    c4'=137998080=2⁸·3⁴·5·11³,
    c6'=−1502799091200=−2⁹·3⁶·5²·11⁵.

Every possible integer scaling therefore divides 6. For u=3 and u=6,
the scaled discriminants are 1207269217792000/3 and 294743461375/3,
respectively. Neither is integral. For u=2 the invariants are c4,c6
in the conclusion, with nonzero integral Delta. Kraus's conditions
hold: c6 is 0 modulo 27, c4 is 0 modulo 16, and c6 is 8 modulo 32.
Thus u=2 is maximal. Substitution and its rational inverse
X=x/4,Y=(y−4)/8 give the full identity

    y²−x³+2874960x−1739350800
      =64(Y²+Y−X³+179685X−27177356).

The coefficients [0,0,1,−179685,27177356] are integral and reduced,
and their directly computed invariants are exactly c4,c6,Delta.
The imported criterion proves minimality. Divisibility of the two
invariants alone at 3 would not suffice.

A nonidentity rational two-torsion point on E' would have y=0, hence
a rational root of its monic integral cubic. By the rational-root
theorem that root is an integer. Modulo 7 the cubic is x³+3x+5;
its values at all residues 0,...,6 are 5,2,5,6,4,5,1. There is no
root. Thus E'(Q)[2]=0, also on E_m by the origin-preserving model
change. This elementary instance check supplies no Selmer bound.

### Invariant selection and real types

Import Cremona III.3.6 Step 1, p.92. For a minimal model it starts
with I=c4,J=2c6, performs the stated dyadic reduction if possible,
and prescribes whether the larger pair must also be retained. Here

    I mod 16=0, J mod 64=16,
    I mod 4=0, J mod 8=0, (2I+J) mod 16=0.

There is no division by (16,64), and the last three tests meet exactly
the sufficient criterion for omitting (16I,64J). The non-dyadic
normalization is covered by minimality and Step 1; no further prime
pair is being omitted. Agreement with L112's quartic invariants is
only a cross-check, not the coverage argument. We have
4I³−J²=360895702709586528000>0. Step 2, pp.93–94, therefore requires
types 1 and 2, with both signs for type 2; type 3 does not occur.
Negative definite type-one quartics have no real points and are
excluded by that algorithm.

### Exact regions and workload

Let phi1>phi2>phi3 be the roots of

    f(phi)=phi³−25874640phi−46962471600.

Exact rational isolating intervals are

    phi1 in [5825.478876337878, 5825.478876337879],
    phi2 in [−2262.749518242581, −2262.749518242580],
    phi3 in [−3562.729358095299, −3562.729358095298].

All decimals here mean exact rationals. Endpoint signs are respectively
(−,+), (+,−), (−,+), with complete rational evaluations in the
certificate below. These disjoint intervals have sign changes, hence
each contains a root; a cubic has no other roots.

Set K=(4I−phi1²)/3. The p.94 coefficient bounds give

    A1=(K+sqrt(K)phi1)/(3sqrt(K)+phi1+2phi2),
    A2+=(I−phi2²)/(3(phi2−phi3)),
    A2−=(I−phi2²)/(3(phi1−phi2)).

The last expression includes the source's reversed root ordering
for negative a. All denominators are positive. Rational interval
arithmetic gives

    1043.1342482703 < A1 < 1043.1342482704,
     898.6920438422 < A2+ < 898.6920438423,
     144.4422044280 < A2− < 144.4422044281.

The square-root enclosure is certified by exact squaring. Hence the
integer maxima are 1043,898,144 without a boundary ambiguity. For
each a the b range −2|a|<b<=2|a| contains exactly 4|a| integers.
Summing 4m over 1<=m<=N gives 2N(N+1), so the complete raw rows are

    2177784 + 1614604 + 41760 = 3834148 > 200000.

Even type one alone exceeds the row cap, and all its rows have c
integers. For type one the p.94 c interval is

    [(4a phi2+3b²)/(8a), (4a phi1+3b²)/(8a)].

Its length (phi1−phi2)/2, independent of a,b, lies in the exact interval
[4044.114197290229,4044.114197290230]. Every closed interval of length
greater than 4044 contains at least 4044 integers: start at the ceiling
of its lower endpoint and take the next 4043 integers. The type-one
subregion 1<=a<=16 has 2·16·17=544 rows and therefore at least
544·4044=2199936 raw triples, exceeding 2000000. These triples need
not reconstruct integral d,e or survive any sieve or type test. None
of those unperformed tests is used in the workload claim.

### Verification and limits

Run `python3 scripts/pair-genus-two/quartic_workload.py`; the full
certificate is `scripts/pair-genus-two/elliptic-quartic-workload-certificate.json`.
All 19 checks pass, with no failures. Every normalization candidate,
model residual, mod-7 value, dyadic test, root endpoint evaluation,
coefficient bound and count was inspected in full. Analytic counting
visited zero coefficient rows and enumerated zero triples. The full
triple count was not computed; its lower bound already fails the cap.

The script uses rational interval arithmetic, with integer-square-root
enclosures at denominator 2¹⁰⁰ checked by squaring. Saved bounds are
rounded outward to denominator 10¹². Root bisection retains opposite
signs before and after outward rounding. Thus no floating-point
approximation is used as proof. Elementary interval operations and
the explicit endpoint evidence suffice to reproduce each inequality.

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-25-marked-elliptic-explicit-two-descent.md`.
This is reproduction/specialization of known algorithms, supplying
new local route evidence, not a new descent theorem. No use was made
of the unsafe older equivalence criterion. No syzygy sieve, local
test, class merge, Selmer calculation or upper rank was run. A different
certified traversal could succeed; increasing these raw caps is not
the recorded continuation. L112's lower rank one and all independent
Beal obligations remain unchanged.

## Mathlib

Full matching minimal-model normalization, quartic descent, coefficient
regions and this exact-instance certificate were not checked in Mathlib.
No absence or Lean verification is claimed. The cited algorithms and
elementary exact arithmetic above are the informal inputs.
