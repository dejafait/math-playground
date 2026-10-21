# L047 — Nonoptimal conductor-eleven quadratic enclosure at five

## Hypotheses

Let E/Q be the global minimal curve
\(y^2+y=x^3-x^2-7820x-263580\), with coefficients
[0,-1,1,-7820,-263580]. Use L046's separately audited degree-five
isogeny from L039's geometric non-CM source and its exact full-relative
normalization. In L039's entire integral relative module at level 11,
the quotient has dimension three, \(\phi=(5/2,5,1)\), and
\(F_E=I/\Omega(E)=\phi\), with total minimal real Neron period.
Retain L046's inherited published source-optimality/complete-isogeny-class
qualification. Its twelve normalized values, including both zeros, are
\((-1,1,0,5,5/2,-5/2,-5,-5,-5/2,5/2,5,0)\).

Apply L027 on the primitive untwisted trivial Teichmuller branch at
p=5, in coordinate \(\kappa(\gamma)=6\). Write
\(L_5(E,T)=\sum_i a_iT^i\). Neither lower coefficient is assumed zero.
The prior SPECIALIZE assessment is
`drafts/literature/2026-10-11-nonoptimal-quadratic-five-enclosure.md`.
It approves exactly n=2,3,4, M=n+1, stopping at the first strict bound.

The full exact finite witness is
`scripts/conductor-eleven/quadratic-five/certificate.json` and its
distinct complete replay is the adjacent `verification.json`.
Reproduce from the notebook root:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 scripts/conductor-eleven/quadratic-five/build_certificate.py
PYTHONDONTWRITEBYTECODE=1 python3 scripts/conductor-eleven/quadratic-five/verify_certificate.py
```

Every earlier bound input and program is read-only. Fresh complete upstream
reports are in the adjacent `upstream-replay/`. Production replay and the
separate critical audit below pass. This is a fixed known-method
reproduction, not a BSD candidate.

## Conclusion

Five is good ordinary for E, with \(\#E(\mathbf F_5)=5\) and t=1.
At n=4, M=5, C=0 and u=2846, the complete exact L027 sum is

\[
b=\frac{120974325}{5834780198523343},\qquad v_5(b)=2,
\qquad N=\min(4-1,5)=3>2.
\]

Thus \(v_5(a_2-b)\ge3\), \(a_2\ne0\), and \(v_5(a_2)=2\).
Depths two and three fail the strict test; their full evidence is retained.
The schedule stops at depth four. This produces only a fixed quadratic
coefficient input. It supplies no lower vanishing, rational points, rational
rank, Sha statement or comparison with complex order. L026's additional
hypotheses are neither assumed nor certified; the rational degree-five
isogeny and the point count at five must not be replaced by
residual-surjectivity or non-anomalous assumptions.

## Proof

**Known method and applicability.** Import L027's existing enclosure,
whose primary inputs are Stein--Wuthrich, *Algorithms for the arithmetic
of elliptic curves using Iwasawa theory*, Math. Comp. 82 (2013),
1757–1792, [Section 3, pp.1762–1766, Propositions 3.1/3.5 and
Corollary 3.3](https://wstein.org/papers/mcom2649-iwasawa-alg.pdf#page=6),
and Conrad, *Hensel's Lemma*, [Theorem 4.1, printed
p.6](https://kconrad.math.uconn.edu/blurbs/gradnumthy/hensel.pdf#page=6).
No convergence result is reproved. The ordinary interpolation multiplier
\((1-\alpha^{-1})^2\) remains present, with no rescaling or division by it.
Optimality is retained in L046's source normalization rather than imposed
on this target for convergence. Irreducibility of E[5] and the
non-anomalous condition are not L027 hypotheses.

For non-CM applicability import Sutherland, MIT 18.783 Spring 2015,
Lecture 13 (19 March 2015), [Theorem 13.18, p.7, with its proof and
Corollary 13.20, pp.7–8](https://math.mit.edu/classes/18.783/2015/LectureNotes13.pdf#page=7):
isogenous elliptic curves have isomorphic rational endomorphism algebras.
Apply over an algebraic closure of Q to L046's audited characteristic-zero
isogeny. L039's source is geometric non-CM, with endomorphism algebra Q;
the target's algebra is also Q. This establishes geometric non-CM without
equality of integral endomorphism rings or prime-to-five degree. The
certificate records the cited application, rather than a scripted proof
of the endomorphism theorem.

**Good ordinarity and all-level denominator.** L046 proves target
minimality and \(\Delta_E=-11\), four modulo five, so reduction is good.
Modulo five the equation is \(y^2+y=x^3-x^2\). For x=0,1 the right side
is zero and y=0,4 are the two solutions. For x=2,3,4 the right sides
are 4,3,3; their quadratic discriminants are 2,3,3, all nonsquares.
These rows exhaust every affine pair. At infinity the homogeneous equation
forces X=0, leaving only [0:1:0]. The total is five, hence
\(t=5+1-5=1\), a unit. Production completes the square; distinct replay
tests all 25 ordered pairs in the target equation itself, without
transferring a point count through the degree-five map.

L046's complete integral-generator values have exact denominator two.
Integral path generation in L039's full saturated relative presentation
gives \(F_E(M)\subset(1/2)\mathbf Z\), so every rational-cusp argument
at every level is five-integral. This is L027's uniform C=0 input; finite
paths do not replace that all-level proof. Replay checks all twelve values
against phi on all three coordinates, all 24 source relations and all
nine saturated relations. L046's period direction is
\(\Omega(E_0)/\Omega(E)=5\), giving \(F_E=5F_0=\phi\); the source's
scale 1/5 is not retained on E.

**Complete Teichmuller and root checks.** In order d=1,2,3,4 the
least-positive roots of \(X^4-1\) modulo \(5^n\) are:

| n | w values | residual valuations | derivatives modulo five |
|---|---|---|---|
| 2 | 1,7,18,24 | infinity,2,2,2 | 4,2,3,1 |
| 3 | 1,57,68,124 | infinity,3,3,3 | 4,2,3,1 |
| 4 | 1,182,443,624 | infinity,4,4,4 | 4,2,3,1 |

The certificate retains every integer fourth-power residual. Each w lies
in [1,5^n-1], reduces to its specified d, and has residual divisible by
5^n. Distinct replay exhausts every candidate in each residue class,
finding exactly the displayed root. Every derivative 4w^3 is a unit;
w=1 has residual zero. Conrad's simple-root criterion as specialized
in L027 identifies these Teichmuller residues.

For \(f(X)=X^2-X+5\), the certified unit-root approximations are:

| n | M | u | exact f(u) | v_5(f(u)) | f'(u) modulo five |
|---|---|---|---|---|---|
| 2 | 3 | 96 | 9125 = 5^3*73 | 3 | 1 |
| 3 | 4 | 346 | 119375 = 5^4*191 | 4 | 1 |
| 4 | 5 | 2846 | 8096875 = 5^5*2591 | 5 | 1 |

Each u is one modulo five, hence a unit. Replay enumerates [0,5^M-1]
for the residue-one root, independently of production's successive digit
lifting. The unit derivative and exact residual valuation M give
\(v_5(\alpha-u)=M\) by L027's Hensel application. This is the ordinary
unit root; the other quadratic root has valuation one. No approximate
root determines any cusp argument.

**All paths in the entire quotient.** At every approved depth, for
every d=1,...,4 and j=0,...,5^(n-1)-1, set
\(r=w_{n,d}6^j\bmod5^n\), with 1<=r<5^n. Both exact arguments
r/5^n and r/5^(n-1), including integer parts, are saved. Replay constructs
r by repeated multiplication, checks that the complete multiset is all
units modulo 5^n, and regenerates every term label. There are respectively
20,100,500 terms and 40,200,1000 path uses; identical rational arguments
across depths are stored once.

For every path the verifier evaluates the continued fraction backwards
to its exact endpoint. Each segment has a determinant-one integer lift
h=(A,B;C,D), start B/D and end A/C in canonical projective coordinates.
Chains start at infinity, have matching consecutive endpoints and finish
at the exact argument. The verifier exhausts all twelve actual L039 lifts
g_i, finding exactly one for which gamma=h*g_i^(-1) has lower-left entry
divisible by eleven. It checks det(gamma)=1, gamma*g_i=h entrywise,
and the saved index and matrix. Thus the segment is the positively
oriented generator g_i in the relative quotient, independently of the
producer's inverse coset lookup. Path addition identifies its chain sum
with {infinity,r}.

Replay reconstructs every raw integral vector in Z^12, all three quotient
coordinates, and each value both by phi on those coordinates and by all
twelve generator values. All 1120 distinct paths and 6688 segment
occurrences pass. Complete geometric witnesses, raw vectors, quotient
coordinates and evaluations are in `certificate.json`; no sampled check
or success flag substitutes for full replay.

**Complete sums and stopping.** Every term of L027 is retained with
weight binomial(j,2), including j=0,1 and all j>2. Let
A=S(r/5^n), B=S(r/5^(n-1)). The weighted sums by residue are:

| n | d | sum binomial(j,2) A | sum binomial(j,2) B |
|---|---|---|---|
| 2 | 1 | 60 | 60 |
| 2 | 2 | -15 | -65 |
| 2 | 3 | -15 | -65 |
| 2 | 4 | 60 | 60 |
| 3 | 1 | -2875 | 3800 |
| 3 | 2 | 5550 | -3450 |
| 3 | 3 | 5550 | -3450 |
| 3 | 4 | -2875 | 3800 |
| 4 | 1 | 289775/2 | -376875 |
| 4 | 2 | 535250 | 459000 |
| 4 | 3 | 535250 | 459000 |
| 4 | 4 | 289775/2 | -376875 |

The complete sums (now using sum A and sum B to mean the weighted
totals) and actual/required bounds are:

| n | sum A | sum B | b = sum A/u^n - sum B/u^(n+1) | v_5(b) | N | strict? |
|---|---|---|---|---|---|---|
| 2 | 90 | -10 | 4325/442368 | 2 | 1 | no |
| 3 | 5350 | 700 | 115650/895745041 | 2 | 2 | no |
| 4 | 1360275 | 164250 | 120974325/5834780198523343 | 2 | 3 | yes |

Each A, B, binomial and rational term is stored and replayed. Independently
of the producer's rational accumulation, replay accumulates integer values
2F_E(g_i), yielding integer weighted totals (sum_A2,sum_B2) equal to
(180,-20),(10700,1400),(2720550,328500). It computes
\(b=(u\,\mathrm{sum\_A2}-\mathrm{sum\_B2})/(2u^{n+1})\), agreeing
with every individual rational term and their sum: 20/20,100/100,500/500
terms, without dropping any large-j contribution.

The final reduced numerator is 25*4838973, with the last factor prime
to five, and the denominator is three modulo five. Thus v_5(b)=2.
L027's all-level tail and scalar-root estimate give
\(v_5(a_2-b)\ge\min(n-1-C,M-C)=3\) at n=4. The strict inequality
gives v_5(a_2)=2 by the ultrametric inequality. At earlier depths
N<=v_5(b); their enclosures certify neither vanishing nor nonvanishing.
The first-strict-stop rule is met at depth four; no depth five was attempted.

**Replay and limitations.** Fourteen grouped new replay checks pass with
no failure. Fresh upstream execution checks the entire L039 structural/dual
evidence, including all sixty paths, 218 segments and every structural
domain count; all L043 integral-boundary, primitive-image, 64-term oriented
Fourier and twelve-value normalization evidence; and all 56 L046
isogeny/minimality/differential/transfer checks. Full reports and logs are
in `upstream-replay/`, and all bound prior bytes remain unchanged.
Hashes establish provenance, not the external theorems. Generic software's
conditional provenance remains distinct from L039's independently proved
local arithmetic and exact instance replay.

The separate audit below validates the programs and this assembly for the
fixed instance. No mathematics beyond the assessed known algorithm is claimed. A nonzero
quadratic coefficient alone does not identify the order of the series
or rational rank, and resolves none of the independent Sha,
point-realization or complex-order gaps.

**Separate critical audit (2026-10-11).** The unchanged prior SPECIALIZE
assessment `drafts/literature/2026-10-11-nonoptimal-quadratic-five-critical-audit.md`
covers this audit, classified REPRODUCTION. Reproduce from the notebook root:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 scripts/conductor-eleven/quadratic-five/audit.py
```

The complete report is
`scripts/conductor-eleven/quadratic-five/critical-audit/audit.json`.
The audit archives all four original production files, every production
upstream report/log, and every bound upstream file before replay. It imports
the preserved producer and verifier with ROOT redirected into distinct
`critical-audit/rebuild/` and `critical-audit/replay/` directories;
BASE/CAL/ABS keep their original read-only bindings. The subordinate dual,
structural and absolute-cycle outputs follow these new destinations, and
the isogeny verifier returns evidence for the new caller to save. No
production report is overwritten. The rebuilt certificate agrees byte for
byte. Complete replay again verifies the target point count, all twelve
values and relations, every root and residual, all 1120 paths, 6688
segments and 620 terms. The fresh report agrees with the original except
for output paths. Full upstream replay includes all structural domain
counts and 218 segments, the entire dual line, absolute-cycle normalization
and all 56 isogeny checks. These executions retain, rather than prove,
the named external theorem and source-optimality qualifications.

For a distinct decomposition of every rational argument, the audit uses
the ceiling Euclidean algorithm. Starting from coprime a,b with b>0,
set k=ceil(a/b) and replace (a,b) by (b,kb-a). The new remainder lies in
[0,b), so the algorithm terminates. Backwards evaluation by k-1/x
recovers the original argument. For its digits use initial pairs
(p_0,q_0)=(0,-1), (p_1,q_1)=(1,0) and successive pairs
(p_2,q_2)=k(p_1,q_1)-(p_0,q_0). Every saved segment satisfies q_2>0
and p_2 q_1-p_1 q_2=-1. Hence
h=(-p_2,p_1;-q_2,q_1) has determinant one and oriented endpoints
p_1/q_1 -> p_2/q_2. Exhausting the twelve original lifts gives exactly
one i for which gamma=h g_i^(-1) lies in Gamma_0(11); determinant and
matrix reconstruction are checked entrywise. Each full chain starts at
infinity and ends at its specified rational argument. Since none of these
arguments is integral, its first ceiling endpoint differs from the
original floor endpoint. Thus all 1120 chains are distinct decompositions.
Integral path generation and the full relative presentation here are the
named weight-two results of Stein, online v0.1,
[Propositions 3.10--3.11 and Theorem 3.13](https://wstein.org/books/modform/modform/weight_two.html),
as instantiated and audited in L039; no equality of scalar evaluations
is substituted for equality in that presentation.

In detail, let Pi be the 3-by-12 quotient map, K the 12-by-9 saturated
relation matrix, and H the 9-by-12 head of the inverse integral basis
change in L039. For each raw path difference delta=raw_alt-raw_original,
the audit saves the integral vector c=H delta and checks Kc=delta,
Pi delta=0 and equality of all three quotient coordinates. This verifies
membership in the entire saturated relation lattice. The complete chains,
all 16258 alternate segments, raw vectors, nine relation coefficients and
three quotient coordinates are in `critical-audit/alternative-paths.json`.
There are 1114 distinct raw vectors; the other six pairs of different
chains happen to have the same raw vector, giving delta=c=0. This does
not weaken their geometric or quotient checks.

The audit then enumerates all four Teichmuller residue classes and the
unit-root residue class independently at every n,M, and reconstructs
every term label using only alternate-path values and gamma=6. It uses
sum_(h=0)^(j-1) h for the binomial weight and exact rational accumulation.
Every term, including zero weights and the last terms at each depth,
agrees with the original. All twelve residue-wise sums and the three
reduced b values in the displayed tables agree; complete independent
evidence is in `critical-audit/alternate-coefficients.json`. Exact
residual valuations are M=3,4,5. The source/target ratio remains five,
so denominator two gives C=0 at five, without a source 1/5 scale.
The non-CM import applies over Qbar to the actual characteristic-zero
isogeny; its degree need not be prime to the coefficient prime.

For the infinite-series conclusion, L027's uniform denominator argument
bounds every adjacent coefficient difference, and its closed-lattice
limit gives v_5(a_2-b)>=min(n-1,M). The finite rational root substitution
has error at least M. These are the existing proved estimates, not an
inference from matching finite polynomials. At n=2 and n=3 the respective
error balls have radii 5^(-1) and 5^(-2) and contain zero, since v_5(b)=2.
At n=4, v_5(b)=2<3, so the ball excludes zero and the ultrametric
inequality gives exactly v_5(a_2)=2. Neither lower coefficient is assumed
zero, and the primitive ordinary multiplier has not been divided out.

Seven deliberately altered copies test an upstream binding, a full
quotient coordinate, false depth-two strictness, the depth-three root
residual, the final depth-four summand, the cyclotomic coordinate and the
limiting bound. All are rejected, including the early binding failure.
Each seeded stale success report is replaced by a fresh nonempty failure
report with the altered certificate hash and empty results. The full
altered certificates, reports and logs remain in `critical-audit/rejections/`.
These are expected rejection tests, not mathematical counterexamples.

All 28 audit comparisons pass without unexpected failure or mathematical
correction; the post-replay hashes confirm that original and bound
upstream bytes remain unchanged. This supplies a critically checked fixed
coefficient input within the assessed known method. It does not establish
universal program correctness, residual surjectivity, non-anomalous
reduction, lower vanishing, rational points, Sha finiteness or complex-order
equality. Published source-optimality/complete-isogeny-class and two-period
qualifications remain exactly as in L046.

## Mathlib

Full matching ordinary convergence, target normalization and finite
coefficient certificate: not checked. Supporting Hensel, valuations,
binomial coefficients, isogeny-invariant endomorphism algebras and exact
linear algebra: not checked. Unknown coverage is not absence. The precise
named imports and their specializations are above.
