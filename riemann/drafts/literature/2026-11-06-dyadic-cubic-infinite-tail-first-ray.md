# Dyadic cubic infinite tail — completed source comparison

TARGET: Test whether F(z)=product_(j>=0)P(2^(-j)z), P(w)=1+2w+2w^2+w^3, has det([z^(1+j-i)]F)_(0<=i,j<r)>=0 for every integer r>=1, with negative-index coefficients zero.
CHECKED: 2026-11-06
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Bounded exact-family, dyadic-cubic, q-product reciprocal-coefficient and Toeplitz/Jacobi–Trudi searches found no inspected exact-family sign certificate. Scoped local comparison checked L840, the 6 November all-fixed-shifts assessment, its ATTEMPTS stop and the L840 audit history. Search failure makes no novelty claim; universal coefficient identities provide the proposed method.
SOURCE_EVIDENCE: Inspected Macdonald, Symmetric Functions and Hall Polynomials, 2nd ed. (1995), I.2 (2.4)–(2.6), pp.20–21, complementary-minor argument (2.9)/(2.9'), pp.22–23, and I.3 (3.4)/(3.5)/(3.9), pp.41–42; McMullen, Advanced Complex Analysis, 2 December 2025 notes, Theorem3.1 and preceding compact-product criterion p.80, Cauchy coefficient formula (1.2)/bound pp.12–13 and Theorem1.34 pp.24–25; NIST DLMF v1.2.8 (2026-09-15), 17.1, 17.2.4, 17.4.1 and 17.5.1/.2/.4. L840 supplies the already audited finite polynomial context.
COMPARISON: First-ray determinant/reciprocal duality is universal known mathematics, whereas Alexandersson's finite-band formula is unnecessary for an infinite-band transfer. Test finite reciprocal Cauchy products and compact coefficient limits using L840's m=1 signs; do not assume closure of higher solid rays. The exact normalization, convergence and application have not been carried out here.
GAP: Supply only the family-specific applicability argument: identify the normalized reciprocal coefficients, verify the L840 factor/scaling match, justify compact product and reciprocal convergence near zero and coefficient limits, and decide the complete first ray including zeros. No determinant, residue, pole packet or sign for F has been calculated in this review. Higher shifts and Xi realization remain independent.
REASON: Essential coverage now permits one known-method specialization at exactly TARGET. Prefer coefficient transfer to a new pole-asymptotic calculation; no reproof of the universal identities or inaccessible general theorem is needed. This source review does not assert the specialization succeeds.
LITERATURE_REASON: The nominated target changed finite degree to infinite support; compact-limit and universal reciprocal-series coverage were essential and absent at invocation start. They are now supplied, so the next turn defaults to mathematics.
SCOPE: Exactly TARGET with ordinary zero-extended coefficients, q=1/2, no exponential factor and weak signs at every rank. Coverage includes finite Cauchy products and local uniform limits for the first-ray test; it does not approve higher shifts, any inherited PF order, strict signs or Xi transfer.

## Purpose and comparison with recorded stops

The main gap is L030–L032/C032a actual-Xi all-degree mixed
positivity. The intermediate target is TARGET; its downstream use is
to discriminate whether the finite weak-sign obstruction survives an
infinite tail at shift one. Even success leaves every k>=2, any useful
Xi growth constraint, realization and actual-Xi signs unproved.

L840 at m=1 is the exact finite input to check, not an infinite-product
result. Its polynomial depends on no new parameter here. L839's finite
weak-sign stop and the broader fixed-shift source blocker retain their
scope. In particular, no closure theorem for all solid-ray signs is
imported. The blocked Bultheel meromorphic-Toeplitz route stays parked;
this test uses a scalar reciprocal series instead of general determinant
asymptotics. No cross-notebook result is used.

## Primary statements actually inspected

**Algebraic correspondence.** I. G. Macdonald, *Symmetric Functions
and Hall Polynomials*, second edition, Oxford (1995),
[primary book PDF](https://math.berkeley.edu/~corteel/MATH249/macdonald.pdf),
I.2 pp.20–23, (2.4)–(2.6), (2.9)/(2.9'), and I.3 pp.41–42,
(3.4), (3.5), (3.9). The e_i are algebraically independent;
H(t)E(-t)=1, h_0=e_0=1 and negative subscripts vanish.
The source gives both Jacobi–Trudi determinants and s_(n)=h_n.
Its complementary-minor proof uses finite triangular inverse matrices
with diagonal 1, so it does not divide by a potentially zero solid
minor. These are polynomial identities, valid after numerical
specialization; positive-real elementary variables are not a hypothesis.
The finite specialization and limiting normalization are the remaining
application, not new universal identities. No unproved infinite-alphabet
positivity premise is being imported.

**Analytic passage.** C. McMullen, *Advanced Complex Analysis*,
Harvard Math213a, notes dated 2 December 2025,
[primary PDF](https://people.math.harvard.edu/~ctm/home/text/class/harvard/213a/25/html/home/course/course.pdf),
Theorem3.1 and preceding paragraph, p.80: summable reciprocal nonzero
zero parameters yield the entire product with exactly the specified
zeros, including repetitions; uniform compact summability of deviations
from 1 gives holomorphic product convergence. Formula (1.2) and its
bound, pp.12–13, give Taylor coefficients by contour integrals and
|a_k|<=ML/(2pi R^(k+1)). Theorem1.34, pp.24–25, permits a finite set
of isolated interior singularities; the next paragraph gives reciprocal
simple-zero residues. These standard results cover convergence and
coefficient control once their hypotheses are verified. No new contour
estimate is proved here. The proposed coefficient approach does not
require residues; should it fail, no infinite residue expansion is
approved as a replacement without complete relevant evidence.

**Optional q-product descriptions.** NIST DLMF version1.2.8, released
15 September 2026: [17.1](https://dlmf.nist.gov/17.1) requires |q|<1;
[17.2.4](https://dlmf.nist.gov/17.2.E4) defines (a;q)_infinity;
[17.4.1](https://dlmf.nist.gov/17.4.E1) fixes basic-series conventions;
[17.5.1](https://dlmf.nist.gov/17.5.E1),
[17.5.2](https://dlmf.nist.gov/17.5.E2) and
[17.5.4](https://dlmf.nist.gov/17.5.E4) give Euler/q-binomial expansions.
The reciprocal Euler series is asserted for |z|<1; its continuation
is not a Taylor series beyond that disk. The product Euler expansion
has no |z|<1 restriction. No q-product factorization of the cubic family
was derived. These identities alone assert no sign for the target.

## Search scope, unread leads and method limits

Queries included the exact strings “1+2x+2x^2+x^3” with “infinite
product”, “1+2z+2z^2+z^3”, “dyadic cubic Toeplitz infinite product”,
“q-products nonnegative reciprocal coefficients”, “Toeplitz reciprocal
Jacobi-Trudi determinants”, and “Expansion of meromorphic functions
Theorem IV.10”. Searches returned unrelated q-products, finite-band
formulas and general symmetric-function identities; none was treated
as an exact-family sign theorem. Secondary summaries were discovery
aids only. An author post about fixed Xi shifts was not needed or
inspected as an input; it supplies no evidence for this exact family.

Flajolet–Sedgewick's *Analytic Combinatorics*, TheoremIV.10, appeared
in indexed primary text. The INRIA PDF exceeded the web size limit;
the Princeton PDF returned403; local curl failed DNS. Neither this
indexed passage nor the image-only Bologna product notes are accepted
as inspected proof coverage. No further access attempt is needed:
Macdonald and the accessible compact-convergence/Cauchy tools cover
the independent coefficient-transfer method. The old Bultheel blocker
was not retried. There is no assertion of an absolutely convergent
infinite partial-fraction series, and tied/multiple pole contributions
must never be discarded merely for having oscillatory phases.

Mathlib: full matching coverage for TARGET and its reciprocal
Toeplitz identity was not checked. No absence claim is made.

## Approved bounded continuation and stopping test

In one mathematical step, apply the cited identities to the audited
L840 m=1 input and the finite dyadic products, then justify the
necessary limit at fixed rank. Explicitly check ordinary-coefficient
normalization and scaling before any sign transfer. This is routine
known-method specialization, not a creative central-Xi mechanism or
an original theorem merely because the family was not found by search.
Do not reprove Macdonald or add a lemma solely to record an identity.

One rigorously negative minor rejects this ansatz. Success requires
all r>=1, with coefficient convergence and any zero cases justified;
finite sampling or a product-of-solid-minors assertion is insufficient.
If the coefficient-transfer argument does not decide the question,
save the precise obstruction and stop this attempt; do not start a
second pole mechanism in the same turn. Any resulting canonical proof
must cite these standard inputs, justify their specialization and state
Mathlib qualifications. Higher shifts require separate assessment.

No justified creative actual-Xi mechanism is ready: no independent
signed Xi input has emerged. This review removes the method-coverage
gap for the selected model test only. The all-rank target remains
unresolved and no lemma, mathematical script, PROOF or DAG is changed.
The original nomination is preserved in
`drafts/2026-11-06-dyadic-cubic-source-review-working.md`.
