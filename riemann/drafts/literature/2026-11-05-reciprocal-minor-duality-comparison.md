# Reciprocal coefficient sign — completed duality source comparison

TARGET: Compare L785's determinant u_2 u_4-u_3^2 with dual Jacobi-Trudi and complementary Toeplitz-minor identities, including its normalization and relation to L776's D_(3,2).
CHECKED: 2026-11-05
DECISION: IMPORT
SEARCH_EVIDENCE: Step461 reused October31 ordinary Jacobi-Trudi and step456/457 rational-interface coverage; searched Jacobi complementary minor theorem inverse matrix singular minors dual Jacobi Trudi Macdonald, then targeted Macdonald formula/generating-series queries; read the primary passages recorded below. The narrow November5 assessment/history/attempt search found no completed exact normalization for this block.
SOURCE_EVIDENCE: Macdonald, Symmetric Functions and Hall Polynomials, second edition (1995), I.2 (2.6)-(2.9') pp.21-23 and I.3 (3.4)-(3.7') pp.41-42, inspected via https://djvu.online/file/evBrSjuw4lsEJ after repeated Berkeley fetch timeouts; Böttcher-Widom, Szegő via Jacobi, math/0604009v1 (1 April2006), Theorem2.1 p.3 and Corollary2.3 with proof p.4, https://arxiv.org/pdf/math/0604009v1 .
COMPARISON: The source's dual determinant and complementary-cofactor identities cover the normalized rectangular coefficient comparison without real-zero or positive-alphabet assumptions and retain singular minors; they give no sign inequality. The two-root analytic hypotheses belong to L785's congruence, not to these algebraic identities. Exact local Hankel orientation and c_0/R factors are reserved for the separate cited specialization.
GAP: Essential theorem coverage is complete; the local normalization, orientation and resulting relation to D_(3,2) still require a separate mathematical application. No independent actual-theta sign input is supplied.
REASON: Newly inspected primary duality/proof and singular-minor hypotheses close the essential source gap; this is local source progress, not a new determinant identity or inequality.
LITERATURE_REASON: The exact reciprocal block is now known and audited; its comparison with the original coefficient minor introduces dual Jacobi-Trudi/complementary-minor normalization outside the previously assessed rational congruence. Reuse ordinary Jacobi-Trudi coverage; inspect only the essential missing duality and applicability cases.
SCOPE: Completed source comparison only; the original nomination below is historical. The separately nominated specialization is limited to this reciprocal two-by-two block and the three-by-three D_(3,2), with no new sign theorem, all-order extension, numerical model or reproof of Jacobi's theorem.

## Completed source review — step461

The main gap is actual-Xi all-degree mixed positivity. The intermediate
target was source-level comparison of L785's remaining determinant with
the coefficient minor of L776. Its downstream use is to reject a possible
algebraic renaming before seeking an independent theta estimate.

The inspected Macdonald passages supply

    H(t) E(-t)=1,
    det[h_(lambda_i-i+j)]=det[e_(lambda'_i-i+j)].

Here h_0=e_0=1, negative subscripts mean zero, and determinant sizes
are at least the lengths of lambda and lambda', respectively. I.2 (2.8)
permits arbitrary scalar specialization of the h_j; a representation by
a positive alphabet is unnecessary. The proof of (2.9') uses finite
mutually inverse unit triangular coefficient matrices, complementary
cofactors, and cancellation of parity factors. I.3 obtains the dual
formula from that identity and proves the ordinary formula in (3.6)-(3.7').
Read the complete relevant arguments, not just the displayed formulas.
The rectangular indices (2,2,2) and (3,3) fit these stated size conditions.
The source identity is polynomial; it does not divide by a selected minor.

Böttcher-Widom Theorem2.1 independently fixes the orientation:

    det A^(-1)[I,K]
      =(-1)^(sum I+sum K) det A[K^c,I^c]/det A.

The indices are increasing, one-based, equally sized subsets of an
invertible finite square matrix. Only A must be invertible. Corollary2.3's
complete short proof identifies the displaced Toeplitz block, interchanges
the complementary row/column sets and computes its parity. Neither
selected minor is assumed nonzero. No Fredholm limit or infinite-operator
invertibility from later sections is needed here. This supplies exact
coverage for singular minors, rather than an inverse of L785's H or R.

For applicability, normalization by the nonzero constant coefficient is
essential before using the unit-constant generating series. Only a finite
coefficient specialization is needed, so no convergence at a selected
root or interchange of an infinite sum is involved. The remaining
mathematical task must write the normalized coefficient substitution,
identify its finite block and complement, track any reversal needed to
obtain L785's Hankel orientation, and account explicitly for both the
constant coefficient and g(z)=G(Rz). This review has not performed that
local determinant calculation or claimed its final sign or scaling.

Coverage is ready for that known-result application. It cannot supply
positivity merely from positive coefficients, infer full inertia from a
determinant, validate actual-Xi root grouping, or close the main gap.
Continue only through one exact cited specialization; if it identifies
the same unpaid minor, close this algebraic sign route without a new
positivity lemma or duplicate derivation. A genuine hypothesis mismatch
must instead be recorded before dependent sign work. L785's separate
analytic transfer still needs exactly two simple negative roots and its
zero-free complement through sigma>1. L773/L781/L783 and the automatic
class/linked-factor stops remain qualified prior evidence.

The Berkeley URL initially returned PDF metadata, then repeatedly timed
out for detailed reads. The same primary book was accessible as the
identified edition's OCR; the crucial duality proof was fully readable
there and the finite-minor sign convention was checked against the
independent primary PDF. Search snippets and unread search hits were not
substituted for theorem inspection. Mathlib matching coverage is unchecked;
a search hit for a separate AlgebraicCombinatorics project is not Mathlib
coverage. No lemma, mathematical script, DAG or PROOF argument was changed.

The next specialization has its own assessment at
`drafts/literature/2026-11-05-reciprocal-minor-duality-specialization.md`.
It is a routine import, not a creative mechanism. An independently
motivated theta-specific signed estimate remains missing for a justified
creative central-gap target. No mathematical exploration budget is spent
by this source turn, and earlier exhaustion is not reset.

## Original nomination (historical; source gate completed above)

The main gap remains actual-Xi all-degree mixed positivity. The
intermediate target is to determine whether the remaining sign test
provided by L785 is simply the existing coefficient-minor test in
another form. Its downstream use is honest selection of an independent
signed-theta target, rather than spending research on an algebraic
renaming of the same gap. A successful comparison need not close that gap.

For the exact comparison, write g(z)=sum c_j z^j near zero with c_0>0
and 1/g(z)=sum u_j z^j locally. L785 supplies the determinant
u_2 u_4-u_3^2. Compare it with det[c_(2+j-i)] for i,j=0,1,2,
using the ordinary coefficient convention. Neither a real-zero assumption
nor positivity of a Hankel or Toeplitz form may enter the source
specialization. Singular minors must be retained. A theorem requiring
inversion of that minor does not suffice; inversion of a triangular
coefficient matrix would require a separate explicit applicability check.
No algebraic relation between these expressions has been derived here.

For actual Xi, use only the normalization already stated in L776:
G(w)=xi(1/2+sqrt(w)/2)/8=sum a_n w^n, with the square-root expression
interpreted by its entire series, and D_(3,2)=det[a_(2+j-i)].
The prospective comparison uses g(z)=G(R z), R>0. Any powers of R
and c_0 must be checked, not suppressed as an unspecified positive
factor. This does not establish an admissible root grouping or a sign
for actual G. L785's transfer to the residual still retains its exact
two-simple-negative-root, sigma>1 and zero-free-complement hypotheses.

Essential local inputs for the comparison are L785 and L776's
normalization/definition of D, plus the cited October31 source notes
and step456/457 comparisons. L781/L783, the automatic-class,
linked-factor and root-elimination stops remain contrasts. The narrow
duplicate search found ordinary Jacobi-Trudi coverage, not a verified
identification for this particular reciprocal determinant; absence from
that search is not a novelty claim. No cross-notebook result is used.
Full matching Mathlib coverage remains unchecked.

Continue only with a precise cited identity that settles the sign,
normalization and singular-case comparison, or a precise hypothesis
mismatch. If it is merely a reformulation, close the algebraic sign
route and retain the independently unpaid theta inequality; do not
commission a duplicate derivation or another fixed-model calculation.
If access to an essential source is persistently blocked, park the
dependent comparison rather than repeat access attempts indefinitely.

This is not a creative mathematical nomination. The current blocker is
the absence of an independently motivated actual-theta signed estimate,
not the historical route stops or a quota. The comparison is intended
to make that distinction testable. Any later creative mechanism must
name an additional theta-specific input and a discriminating bounded
test, and receive its own source coverage before mathematics.
