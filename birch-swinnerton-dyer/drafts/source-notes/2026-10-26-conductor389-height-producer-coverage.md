# Conductor-389 absolute height producer — primary source coverage

2026-10-26, step 504. Literature comparison only. No height computation,
new mathematical deduction, canonical lemma or mathematical script changed.
The associated assessment is
[the producer review](../literature/2026-10-26-conductor389-five-adic-height-production.md).

## Question, scope and decision

The general unresolved claim remains equality of rational rank and complex
analytic order for arbitrary curves of order at least two. The intermediate
target is three absolute Harvey quadratic-height certificates modulo 5^6
for P=(0,0), Q=(1,0), and their exact sum on the minimal equation
[0,1,1,-2,0]. They could complete the missing finite height input of L119
with L120's full Selmer bound b=2 and torsion correction t=0. Independent
implementation correctness, determinant success and the general complex
order comparison remain unresolved. No result concerning those is inferred
from this review.

Decision: SPECIALIZE for a bounded reproduction of the known standard
Frobenius/sigma algorithm. No new height theorem is needed. A printed
regulator is already known for this curve; reproduction is justified solely
to produce pointwise, fully checkable certificates at the retained absolute
bound. The new continuation needs separate next-turn approval.

## Prior inputs, duplicates and failures

Read L119's finite-input statement, equations (1)--(6), source precision
paragraph and audited MST replacement. Reused the finite-certificate,
canonical-height-replacement and replacement-critical-audit assessments.
Read L120's model, point-count and Kummer applicability; L030's arithmetic
proof fixes the minimal equation, c-invariants, discriminant and conductor.
L034's group provenance is retained through L120 and the ready assessments,
without repeating its proof. No original arithmetic execution is replayed.

L082 imports a distinct p=7 Sha result; it does not supply these p=5
heights. ATTEMPTS/032 concerns the failed bounded p=7 scalar, ATTEMPTS/034
rejects repeating an unfilled conditional descent interface, and ATTEMPTS/057
preserves the literal SW sigma discrepancy. None forbids actual height
production via the audited Harvey/MST convention. No cross-notebook read
or input was used.

Exact searches included `"Harvey" "p-adic heights" "389" precision`,
`"389a1" "padic_height" sigma`, `Kedlaya Counting points Monsky Washnitzer
errata Lemma 3 2004`, and `Harvey Efficient computation p-adic heights errata
Theorem 2`. The first searches located official Sage examples; the last
search located the published Harvey paper. Search absence is not an
absence-of-errata claim. The inspected sources below, rather than snippets,
supply the method. General discovery and the already audited canonical
height comparison were not restarted.

## Harvey: complete effective interface and relevant cases

David Harvey, *Efficient computation of p-adic heights*,
[LMS J. Comput. Math. 11 (2008), 40--59](https://doi.org/10.1112/S1461157000000528),
[publisher PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/8797087F163886A19EBE876F1036204C/S1461157000000528a.pdf/efficient-computation-of-p-adic-heights.pdf),
and [arXiv:0708.3404v1, 24 August 2007](https://arxiv.org/pdf/0708.3404v1).
The arXiv record currently lists v1 only. Inspected its full Theorems 1--3,
Sections 2.1/2.2/3, Proposition 4's series construction, Proposition 5's
coefficient errors, Proposition 6's algorithm and precision hypotheses,
the conclusion of the Theorem 2 proof, and Section 5's precision proof
through Lemma 8 and Proposition 9, including the bad-prime hypothesis and
sign handling. Compared the published theorem statements, Sections 3/4
and Section 5, equations (5)--(6), Lemma 8 and Proposition 9; the relevant
theorem contracts agree. Equation numbers differ between versions.

The standing hypotheses are an integral Weierstrass equation, its usual
invariant differential, good ordinary p>=5. Theorem 1 provides E_2 modulo
p^r for any integer r>=1; the faster option needs p>6r and is not the
selected branch. Section 3 obtains E_2 from the second column (B,D) of
F^r as -12B/D modulo p^r, with D a unit. The Frobenius basis must be the
short Weierstrass basis of MST Section 3.2; a general-model x-coordinate
cannot be substituted without its basis/model transport.

Theorem 2, for d>=4, uses E_2 modulo p^(d-3) and returns sigma modulo
I_d=(p^d,p^(d-1)t,...,t^d). It gives the coefficient of t^j modulo
p^(d-j), 1<=j<d. The small d cases use the fixed first coefficients.
Propositions 4--6 control the formal-series integrations and Brent step;
Proposition 6 assumes an integral solution with constant 1, k>=1 and
1<=n<p^(k/2). These conditions must be checked at the implemented
parameters. A formal differential-equation residual alone does not
certify the unknown E_2 or every sigma digit.

For a final absolute height precision M>=2, Theorem 3 sets
n1=#E(F_p), n2=lcm of the Tamagawa numbers, n=lcm(n1,n2), and
M'=M+2v_p(n). It requires sigma modulo I_(M'+1). Section 5 first
multiplies into nonsingular reduction at all bad primes and formal
reduction at p. Its logarithm argument is the unit
(-alpha/beta)(1+sum_(k>=1) c_(k+1)t^k), with t=-d alpha/beta for the
admissible multiple, where x=alpha/d^2 and y=beta/d^3 are reduced
coordinates and d>0. Lemma 8 preserves absolute unit-logarithm precision.
The height formula is +2/n^2 times that logarithm; the M' allowance
accounts for division by n^2 before the final exponent M is asserted.

Proposition 9 requires nonsingular reduction at every bad prime, an odd
modulus and multiplication index at least two. Its coordinate signs are
correlated, not independently selectable. The formula for t and the
Iwasawa logarithm remove the permitted sign ambiguity. It is an imported
algorithm, not a claim that arbitrary modular point arithmetic avoids
cancellation. At this small fixed p, exact rational multiplication and
reduction of fractions, as in Section 2.2/MST Algorithm 3.4, is also a
covered reproduction; no large-p running-time claim is sought. Identity
or torsion cases must use L119's exact-zero branch, never sigma at O.

## Frobenius input and standalone implementation coverage

Barry Mazur, William Stein and John Tate, *Computation of p-Adic Heights
and Log Convergence*, Documenta Math., Extra Volume Coates (2006),
577--614, [publisher PDF](https://ems.press/content/book-chapter-files/27479).
Read Section 3.2 and all steps of Algorithm 3.2, pp.590--591. It constructs
the short model from c_4,c_6, computes absolute Frobenius on the ordered
basis dx/y, x dx/y acting from the left, takes the second column of F^r,
and outputs -12B/D. The ordinary unit-root argument supplies the unit
condition on D. Differential scaling must be transported to the original
model. The canonical construction and arbitrary-b_2 normalization remain
the separately audited inputs; they are not reproved here.

Kiran S. Kedlaya, *Counting Points on Hyperelliptic Curves using
Monsky--Washnitzer Cohomology*,
[arXiv:math/0105031v2, 20 November 2001](https://arxiv.org/pdf/math/0105031v2).
Read Section 3's explicit Frobenius lift and both reduction identities,
Lemma 2's full proof, Lemma 3's statement/source qualification, and Section
4 Steps 1--2 including nonunit divisions. The hypotheses include odd p,
a smooth odd-degree hyperelliptic model (squarefree reduction), and the
specified cohomology basis; genus one over F_5 is within scope once the
actual model change and squarefreeness are checked. Lemma 2 applies to
A(x) dx/y^(2m+1), m>=0, deg A<=2g, and bounds the denominator by
p^floor(log_p(2m+1)). Lemma 3 gives the analogous bound for
A(x)y^(2m+1) dx; its proof is omitted in the primary source, which points
to the infinity-local version of the preceding argument. It is imported
as a cited result, not a newly verified proof. Section 4 describes the
binomial/Newton Frobenius expansion and successive cohomology reductions.

The original algorithm, with these loss bounds, supports a standalone
finite reproduction. It does not authorize ignoring denominators, an
unbounded precision heuristic or an unproved replacement tail bound.
The actual truncation and every remaining tail must be recorded and
checked under these imported bounds. Exact rational reductions may avoid
finite-ring division ambiguity, but do not remove the infinite-tail
obligation. A trace and determinant match alone cannot determine the
unit-root direction or certify the E_2 value.

## Pinned Sage source comparison and known numerical overlap

Inspected [Sage tag 10.6 padics.py](https://raw.githubusercontent.com/sagemath/sage/10.6/src/sage/schemes/elliptic_curves/padics.py):
padic_height lines 749--796, padic_sigma input/output and lines
1032--1128, padic_E2 lines 1275--1436, and matrix_of_frobenius lines
1438--1565. Also inspected [monsky_washnitzer.py](https://raw.githubusercontent.com/sagemath/sage/10.6/src/sage/schemes/hyperelliptic_curves/monsky_washnitzer.py),
frobenius_expansion_by_series specification around lines 1144--1198 and
adjusted_prec's statement and implementation, lines 1249--1289. This is
source comparison, not a complete audit of Sage or its dependencies.

The actual padic_height code returns -2 log(total)/n^2, explicitly
changing the sign for its BSD convention. Its raw output therefore must
not be labeled Harvey q_H. This comparison uses the actual common sigma
formula, not the disputed printed SW formula. padic_sigma's parameter N
returns sigma with t^j coefficient precision p^(N-j+1), hence has the
I_(N+1) profile; it requests E_2 to absolute precision N-2. This is the
index shift from Harvey's Theorem 2. padic_E2 converts through the minimal
short model and accounts for differential scaling. The standard Frobenius
branch increases working precision before calling Monsky--Washnitzer
reduction; the sqrt-p branch has a separate large-p restriction. Its
adjusted_prec documentation cites Kedlaya's lemmas for the total loss.
Do not transplant that helper's estimate to a different expansion or
representation without verifying the corresponding assumptions.

MST Section 4.3, printed p.596, already tabulates the 5-adic regulator of
389A. The [official Sage tutorial](https://doc.sagemath.org/html/en/thematic_tutorials/explicit_methods_in_number_theory/elliptic_curves.html)
also has a 389a, p=5 regulator example; the official reference has a
rank-two pairing example on another specified basis. These establish
published overlap. Their displays are not certificates for the requested
three points or the exact absolute input contract. No table digits are
imported as a new local height computation.

No sage command was found on PATH. Attempts to download source files via
shell failed DNS; the web tool supplied the primary sources, so essential
source access is not blocked. No executable, package, API key or remote
calculation was used. The next attempt must use the covered standalone
algorithm rather than assume Sage is installed. Broader installed-runtime
availability and full matching Mathlib coverage were not checked.

## Continuation and abandonment test

Preserve output M=6 and the exact three points. Future production must
certify the exact group sum and multiples, reduction at p and bad primes,
Tamagawa factor, Frobenius model/differential, all working precisions,
sigma coefficient profile and tail, unit logarithm and its tail, and final
absolute precision after division. L120 already supplies n1=9, good
ordinary p=5, b=2 and t=0; this review does not compute n2 or any height.
Use L030's Tate-algorithm source for the remaining bad-prime calculation.

Only after those pass may L119's matrix, scaling and strict test be
applied. Preserve full finite evidence and enough exact arithmetic for an
independent replay. A failed strict test at M=6 is inconclusive; do not
raise the bound silently or interpret failure as degeneracy. A source or
implementation obstruction must be recorded as unfinished/negative work,
without invented certificates. Even success is a known-method fixed-curve
input and leaves the general rank/order gap and unresolved SW convention.

## Step 505 — direct-link recovery and separate approval

2026-10-26. The three primary PDF URLs above were reopened; Harvey's
Theorems 1--3, MST's Section 3.2 and algorithm, and Kedlaya's denominator
lemmas were rechecked within their existing scope. Detailed prior coverage
is reused. The associated assessment now exposes direct URLs in its
SOURCE_EVIDENCE and matches TARGET to the exact saved production action.
The separate continuation approval is complete. This metadata repair
supplies no new mathematical evidence; no producer ran, and all original
implementation and absolute-error obligations remain.
