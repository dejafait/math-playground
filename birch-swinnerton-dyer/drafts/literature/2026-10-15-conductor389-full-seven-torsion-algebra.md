# Fixed full seven-torsion algebra: construction coverage

TARGET: Construct and independently verify the full nonzero 7-torsion algebra for y^2+y=x^3+x^2-2x as an arithmetic input to L066.
CHECKED: 2026-10-15
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched division-polynomial/full-torsion construction, Sutherland isogeny-kernel notes, exact finite-field irreducibility tests, and the exact 389a1 seven-division query; inspected primary sources below and scoped L030/L065/L066 plus ATTEMPTS/032/033/034. No matching completed local arithmetic certificate was found; this is no novelty claim.
SOURCE_EVIDENCE: Sutherland, MIT 18.783 Fall 2023 Lecture 5, Sections 5.5--5.6, Lemmas 5.20/5.22/5.24 and Theorems 5.21/5.25, pp. 9--14; Schaefer--Stoll, author long version 2001-06-13, Section 5 step 2, printed p. 9; A. K. Lenstra, Factorization of Polynomials, MC Tracts 154/155 reprint, Theorems 2.1 and 4.2, pp. 171,176--177, and Section 5 Tests 1--3, p. 181; inspected statements and relevant proof cases online 2026-10-15.
COMPARISON: The full torsion construction and exact irreducibility criteria are known; remaining work is fixed-model equation transport, exact polynomial/basis computations and a separately replayed finite certificate identifying all field factors. The target is known-algorithm reproduction, not new descent theory.
GAP: No model-specific polynomial, faithful primitive element, complete field factorization, inverse coordinate map or replay certificate is produced in this literature turn; units/classes, local factors and every other L066 obligation remain separate.
REASON: Essential construction and finite-verification coverage was missing at invocation start; this source review supplies it before any fixed-instance calculation.
SCOPE: The exact TARGET permits a bounded fixed-model construction/replay using rational coordinate transport, division polynomials, faithful power-basis evidence and exact rational factor identities with certified modular irreducibility; it excludes descent functions, units/classes, local Selmer calculations and general software-correctness claims.

## Sources actually inspected

[Sutherland, Lecture 5](https://math.mit.edu/classes/18.783/2023/LectureNotes5.pdf)
works with a nonsingular short Weierstrass equation, with the
characteristic-two/three qualification explicit. Section 5.5 gives the
base polynomials and odd/even recurrences. Lemma 5.20 specifies their
parity. Theorem 5.21 identifies multiplication, Lemma 5.22 gives degrees,
Lemma 5.24 prevents cancellation, and Theorem 5.25 gives degree and
separability. For odd n in characteristic zero the nonzero kernel is
specified by the division polynomial together with the curve equation;
the x-coordinate alone identifies opposite points. The inspected proof
includes odd addition and even doubling, the four degree-parity cases,
the adjacent-multiple contradiction for coprimality, and the final
separability argument. Theorem 5.21 sketches the remaining numerator
identities and points to Washington, second edition, Theorem 9.33;
that book proof was not separately inspected. Import the named theorem,
not a claim that this notebook re-proved its general recurrences.

[Schaefer--Stoll, long version](https://mathe2.uni-bayreuth.de/stoll/papers/p-descent-long.pdf),
Section 5 step 2, requires a rational function defined on all of X
and separating every pair of its points. Its characteristic product
then presents the algebra, with irreducible rational factors giving
orbit fields. Thus a y-coordinate suggestion in that step is conditional
on separation; do not assume it for this instance. Reuse the previously
assessed full-set descent statements in L065/L066 without another
interface audit. No Section 10 special three-descent formula is imported
as a seven-descent formula.

[A. K. Lenstra, Factorization of Polynomials](https://infoscience.epfl.ch/server/api/core/bitstreams/3154505c-23e7-4fd4-be73-e8c8b9c85951/content),
Theorems 2.1 and 4.2, constructs the Frobenius matrix modulo a monic
squarefree finite-field polynomial; the fixed-space dimension equals
its number of irreducible factors. The proof uses CRT and that the
Frobenius-fixed elements of each finite field are the base field.
Section 5 also states the power/gcd tests, including Rabin's Test 2.
Use either criterion, with its hypotheses checked. Gauss's lemma
transfers a degree-preserving irreducible reduction of a primitive
integer polynomial to rational irreducibility. No converse or guaranteed
successful prime search is asserted. The extracted theorem and proof
were readable; optional screenshot retrieval failed at the repository's
signed redirect, which does not block the inspected text.

## Applicability and proposed finite evidence

This is a verification specification for later research, not a derived
instance or a successful calculation. Start from L030's exact equation
and nonsingularity. Characteristic zero meets the cited restrictions;
7 is nonzero. Supply and check a rational change to short form and its
inverse before applying the cited formulas; transport coordinates back
to the original model. No residual-surjectivity, analytic-order, Kato
nonvanishing or L026 hypothesis is needed to construct this algebra.

The production attempt should retain these complete obligations:

1. Record the short equation, both coordinate substitutions and exact
   substitution identities. Produce all division-polynomial recurrence
   inputs actually used, with exact divisions checked. Verify the
   seven-division polynomial's full coefficients, degree 24, squarefree
   Bezout identity and disjointness from the short cubic. Retain both
   coordinates, with basis X^i and X^i Y for 0 <= i < 24. Check the
   defining relations and full dimension 48, then apply the cited kernel
   theorem. A degree-24 algebra alone fails the target.
2. Try separating elements t=Y+kX for k=0,...,64, stopping at the first
   certified full power basis. Supply the entire 48-by-48 change matrix
   and rational inverse, the annihilating monic polynomial, and both
   coordinates as polynomials in t. Verify inverse identities and the
   original curve and division equations. A resultant, dimension label,
   floating roots or characteristic polynomial without faithful basis
   evidence is insufficient. This finite range is a budget, not a
   claimed theorem guaranteeing separation in that range.
3. Supply the complete rational factor identity of that polynomial,
   primitive integer versions of each proposed factor, pairwise Bezout
   identities and exact product-algebra coordinate maps. For every
   claimed field factor, seek a degree-preserving irreducible reduction
   at a prime <=200, checking primehood and excluded denominators/leading
   coefficients. Verify squarefreeness and either the full Frobenius
   fixed-space calculation with exact rank evidence or all required
   modular power/gcd identities. Degree-one factors need no such test.
   A factorization routine may propose factors but its labels are not
   evidence. If this bounded certificate format fails, retain the
   faithful algebra as partial evidence and mark field decomposition
   uncertified; do not assume that irreducibility has failed over Q.
4. The separate verifier must reconstruct every relevant coefficient,
   basis multiplication, substitution, inverse and factor test from the
   supplied evidence without importing the producer. Save complete
   certificates/reports to a dedicated notebook scripts subdirectory,
   printing actual/required dimensions, tested bounds, failures and
   paths. Check a bounded corrupted-coefficient and missing-map case
   using copies, preserving original evidence. Replaying only a preview
   or one factor does not complete verification.

No general recurrence reproof is proposed: cite the known theorem and
justify its specialization. Exact basis and factor witnesses are needed
because these instance inputs are absent, and must support later field
arithmetic independently of a software label. Keep any eventual full
instance argument, qualifications and citations in a canonical lemma;
this turn creates neither a lemma nor a mathematical script.

## Comparison, limits and decision test

The exact-model external query returned a Heegner/Kolyvagin computation
involving p=3 rather than the required full seven-torsion algebra; it was
not treated as inspected matching coverage. The other inspected searches
led to standard construction algorithms, not a new result or a verified
389 instance. Local searches and the relevant fixed-model overview
supply no duplicate completed certificate. ATTEMPTS/032's capped zero,
033's absent ordinary evaluation and 034's exhausted interface repetition
remain preserved; none forbids this independently checkable algebra task.

Continue only on complete 48-dimensional torsion identification and
certified field factors, with independent exact replay. Budget failure
is a partial construction or negative production test, not a theorem
that full descent is impossible; do not enlarge the ranges in the same
attempt. The plausible downstream use is the global arithmetic domain
in L066 item 1. This does not finish item 1's functions/embeddings/local
identifications, much less its complete units/classes, local upper
bounds or Selmer dimension. L021/L026/L061 enter only the eventual
handoff; L026 residual nonvanishing remains unverified for this example.
Even a finished algebra supplies no D=D_div, successful localization,
rational membership, removal of divisible Sha, or arbitrary-curve
complex-order/rank comparison. The main gap remains rank equality for
arbitrary analytic order at least two.

Mathlib: full division-polynomial/kernel and finite-factor-certificate
coverage was not checked in this source review; no absence claim is made.
The assessed continuation is REPRODUCTION under SPECIALIZE. No fixed
mathematics was derived and approved in this turn, and no mathematical
exploration budget was spent.
