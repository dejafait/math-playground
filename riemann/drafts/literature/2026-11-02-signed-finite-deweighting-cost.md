# Signed finite interpolation of the actual inverse weights

TARGET: Test whether the degree-at-most-M-1 interpolant F_n(a/R)=1/W_a(-1) at every L666 pole has sum_(k=0)^(M-1) binomial(M-1,k)*|coefficient_k(F_n)| <= (M/R)*exp(n/100)*n^C uniformly over the independent displacements, for an absolute C and onset.
CHECKED: 2026-11-02
DECISION: EXPLORE
SEARCH_EVIDENCE: Completed the changed-scope bounded search on 2026-11-02 for polynomial interpolation of rational/Blaschke products, signed inverse data, binomial coefficient norms and Wiener-norm estimates; reused the prior finite inverse/Mahler comparison and checked L649/L667's exact limitations. No inspected theorem supplies the prescribed uniform cost; this is not a novelty claim.
SOURCE_EVIDENCE: Reused Gautschi (1962), Section 2/Theorem 1 pp.118--119, and Akhtari--Vaaler arXiv:1810.12413v1 (1.3)/Theorem 1.1. New readings: de Boor, Surveys in Approximation Theory 1 (2005), Propositions 7/32 and Section 9 (49)--(51), pp.48,56--57,62--63; Wang--Weiss, JCAM 236 (2011), Theorem 2 and proof (6)--(16), author PDF pp.2--4; Baranov--Zarouf, MJPAA 9(2) (2023), Theorem 2 p.160 and complete proof pp.162--163. Exact hypotheses, access qualifications and comparisons are below.
COMPARISON: Finite interpolation existence/formulas are known; analytic contour formulas retain nodal products. Rational small-norm interpolation changes the allowed pole structure/data, while the inspected rational Wiener bound is unweighted and still requires a norm of the function. None estimates this specific polynomial's full binomial coefficient cost. L667's row stop and L649's ambient stop do not decide signed finite interpolation.
GAP: Establish or refute the exact displayed uniform cost for the prescribed inverse-weight interpolant; any successful cost-to-Mahler use also needs its exact finite-moment identity and normalization verified in the later mathematical attempt. No signed cancellation or favorable norm is assumed.
REASON: Essential comparison for the changed signed functional is now complete enough for one bounded mathematical test. No source import settles its family-dependent estimate. This literature-only review approves the saved target without deriving any new estimate or transfer identity.
LITERATURE_REASON: The saved target changed from individual inverse rows to their prescribed signed combination; finite rational interpolation and its coefficient-norm scope had not been assessed.

## Exact family and proposed test

Keep q>=1, n=12q+3, M=4q+1, H_0=27/(10n), x=-5/4, R=11/8,
U=R^2 and the full conjugated-angle product from L649. The poles are
x and x+i*H_0*(j+1/2+e_j), -2q<=j<2q, with independent real
|e_j|<=1/8 and original residues one. L666 specifies this family;
its other unaudited assertions are not assumed. The finite distinct
nodes and nonzero W_a(-1) are the exact data for the proposed interpolant.

The proposed functional uses the simultaneous inverse-weight data
1/W_a(-1) at all M nodes and combines the finite inverse rows before
any absolute value. It does not change the original residues. Retain
every coefficient of F_n, every coefficient of G, the actual complete
product and degree drops. No symmetry, coefficient integrality,
positivity of complex weights, bounded inverse norm or favorable
cancellation is assumed. No estimate for F_n is asserted here.

The target cost is nominated to test whether the exact finite-moment
identity and the already-inspected coefficient/Mahler bound can give
the original fixed-angle loss 1/100. That application still requires
verification at the next mathematical step after source approval.
If successful, L661's audited general envelope and L658's audited
localization could supply the paid arc. The actual D, all spatial
roots and their leading factor remain required in that downstream use.
General support, Xi realization and all-degree signs remain independent.

## Invocation-start review requirements and decision rule

First compare this precise signed cost with known finite polynomial
interpolation of rational/Blaschke products, using the prior primary
sources wherever adequate. Check whether it is already ruled out by
L649's exact ambient result or L667's qualified row-cost argument;
neither is to be extended by analogy. Inspect any essential new theorem
hypotheses and proof cases before importing it. This is a new scope
comparison, not permission to repeat a generic Mahler search.

Continue only after a precise source comparison approves a bounded
test of the displayed cost, or supplies a known result with verified
hypotheses. In a later approved mathematical attempt, a uniform upper
cost meeting the threshold supports this transfer; an admissible
sequence whose log cost minus n/100 grows faster than log n stops
this prescribed signed interpolant. Such a cost failure still does
not refute the full fixed-angle bound, H, Xi signs or RH. An unknown
signed cancellation is not a quantitative success or negative result.

Essential later inputs: L649 and L666 for the exact data; L667 for the
new individual-row limitation, with its separate audit still pending.
Downstream inputs are L657/L658's full-root and integrability scope,
L661's general D envelope and L664's audited exact-grid comparison.
The scalar, inherited-anchor, absolute-contour and ambient stops are
retained as contrasts, not assumed extensions to the new functional.

Reuse the prior official Mathlib MahlerMeasure supporting coverage.
Coverage of the full signed interpolant or the proposed uniform cost
was unassessed at nomination. That REVIEW_REQUIRED nomination authorized
no dependent mathematical derivation. The completed review below
supersedes its source-gate status, without asserting the target.

## Completed source comparison — 2 November 2026

This step addresses the unresolved full fixed-angle logarithmic bound,
whose possible downstream paid-arc use is described above. Actual-Xi
mixed positivity remains the main gap; this intermediate cost test can
fail or succeed while realization, support and all-degree signs remain
open. No mathematical calculation was performed in this review.

### Inspected primary results

**Complex polynomial interpolation.** C. de Boor, *Divided Differences*,
Surveys in Approximation Theory 1 (2005), 46--69, version dated
21 December 2004, [Propositions 7/32 and Section 9](https://surveys-in-approximation-theory.com/papers/2/2.pdf),
pp.48,56--57,62--63. Arbitrary complex data at distinct complex nodes
have a unique polynomial interpolant of degree below their number;
Proposition 32 also allows clustered repeated-node derivative data.
Equations (49)--(51) express analytic interpolation via Newton nodal
products and contour integrals. Read Proposition 7's divisibility and
uniqueness proof and the complete telescoping/Cauchy derivation of
(49)--(51). Its disk version requires the function analytic in a larger
disk and the integration circle inside it, with the indicated exclusion
of nodes from the intervening annulus. These give representations,
not the target's coefficient estimate. Any use on our rational data
must first verify pole exclusion and keep all nodal products. No
family-specific contour or coefficient estimate is derived here.

**Small-norm rational interpolation.** T. Wang and J. M. Weiss,
*Nevanlinna-Pick interpolation by rational functions with a single pole
inside the unit disk*, J. Comput. Appl. Math. 236(6) (2011), 1497--1501,
[author manuscript, Theorem 2 and proof](https://personal.lse.ac.uk/wangt60/publication/NPinterpolation.pdf),
PDF pp.2--4, (6)--(16). For distinct nonzero disk nodes, prescribed
finite Taylor jets, and any epsilon>0, there are an integer m>0 and
a polynomial p of degree at most total-conditions-minus-one, with
sup-norm below epsilon, such that p(z)/z^m interpolates the jets.
Read the proof: multiply the data by z^m, solve a confluent Vandermonde
system, and retain its smallest-singular-value cost while increasing m.
Thus the theorem changes the polynomial data and permits an interior
pole; it does not bound the prescribed F_n. We do not apply it or use
Theorem 1's generalized Pick formula as a uniform estimate.

**Rational Wiener control.** A. Baranov and R. Zarouf,
*H-infinity interpolation constrained by Beurling--Sobolev norms*,
Moroccan J. Pure Appl. Anal. 9(2) (2023), 157--167,
[DOI 10.2478/mjpaa-2023-0012](https://doi.org/10.2478/mjpaa-2023-0012),
Theorem 2 p.160: for n>=1, 0<=r<1 and a proper rational function f
of degree at most n with poles outside (1/r)D,

    ||f||_(coefficient l1) <= C sqrt(n/(1-r)) ||f||_(coefficient l2),

with an absolute C. Read its class definition p.159 and complete proof
pp.162--163: split at floor(n/(1-r))+1, apply Cauchy--Schwarz to head
and tail, and invoke the cited rational derivative inequality. That
derivative input's source proof was not audited. The paper's
interpolation quantity, p.158, optimizes over H-infinity interpolants;
it does not fix the polynomial F_n. Its coefficient norm is unweighted,
and its right side still needs control. Therefore it supplies no
estimate of our binomial-weighted functional. No rational-class
membership, norm conversion or specialization is assumed here.

### Reuse, duplicates and failure scope

The ready `2026-11-02-displaced-full-spatial-fixed-angle.md` supplies
the inspected Gautschi inverse theorem, complex coefficient/Mahler
bound, full-root formula and prior norm/continuity/power-sum comparisons.
Those general theorems need no reproof. The later attempt must justify
the actual signed functional and its normalization; importing a formula
for a finite inverse does not import the required asymptotic cost.

Read L649's definitions, conclusions and source scope; L666's exact
family, conclusions and source scope; L667's full statement, source
scope and finite-row proof Sections 3--4. Read
`history/2026-11-02-finite-residue-mahler-cost-test-23.md` and searched
the 2026-11-02 attempt records for finite inverse/deweighting stops.
L649 leaves permitted-preimage information uncontrolled, and L667
explicitly excludes signed combinations before absolute values.
Their stopped functionals are not the proposed F_n cost. Conversely,
no cancellation estimate for F_n follows from their exclusions.
The existing scalar, ambient, monomial, inherited-anchor and absolute
contour stops are preserved; none is relabeled as a counterexample to
the new target or to the true fixed-angle logarithmic mean.

### Search and source access record

Queries included `polynomial interpolation rational function finite
Blaschke product Lagrange coefficients inverse weights`, `polynomial
interpolation rational function remainder denominator modular inverse
Vandermonde bounds`, `"Blaschke" "polynomial interpolation" "norm"`,
`"rational" "interpolation" "Wiener" "Blaschke" norm`,
`"polynomial interpolation" "binomial" "coefficient norm"`, and
`"inverse weights" "polynomial interpolation" Blaschke`.
Retrieved the primary statements and relevant proof cases above before
making the comparison. No theorem for this exact functional was found
in this bounded search; no originality is inferred.

The de Boor and Wang--Weiss author/publisher PDFs were readable as web
text. Shell download failed DNS; screenshots were unavailable. The
Baranov--Zarouf publisher PDF open returned unsupported binary content;
the published paper's [author full-text rendering](https://www.researchgate.net/publication/371388096_H_interpolation_constrained_by_Beurling-Sobolev_norms)
provided the theorem, class definition and complete short proof. No
visual PDF audit is claimed. The 2026 Auxemery--Borichev--Zarouf
asymptotic-sharpness preprint (arXiv:2603.03908) is an unread lead about
the unweighted rational inequality; it is not an input. Likewise
Chern--Vaaler continuity remains the prior assessment's unread lead.
Neither is essential to the approved exact finite-cost test.

Reuse the earlier official Mathlib MahlerMeasure coverage, including
`Polynomial.norm_coeff_le_choose_mul_mahlerMeasure`; it is supporting
coverage only. Full matching Mathlib coverage for the prescribed
interpolant cost was not checked. Unknown coverage is not absence.

### Approved bounded mathematical scope

SCOPE: One proof attempt at the exact TARGET, using finite polynomial interpolation of the actual inverse-weight data, the complete rational product and the reused complex coefficient/Mahler bound; retain signed combinations before absolute values and every coefficient and grid factor. Point-evaluation lower tests on admissible data or exact divided-difference/coefficient representations are permitted; any new external theorem outside the inspected scope requires separate review.

Use L649/L666 for the definitions and family and L667 only for its
qualified individual-row contrast. Begin by checking the exact signed
finite-moment identity and cost normalization proposed above. Test the
full cost, allowing an exactly specified admissible displacement
sequence (including the undisplaced vector) as a possible obstruction;
neither its outcome nor a noncancellation estimate is asserted here.
Keep degree drops, complex phases, original unit residues, every
conjugated-angle grid factor and all M data. The required logarithmic
cost is at most log(M/R)+n/100+C log n, with absolute C and onset.

A proof of the uniform target supports this transfer only after the
identity is checked. A rigorously admissible sequence with
(log cost-n/100)/log n tending to infinity as n grows disproves this uniform target
for every absolute C and stops the prescribed functional. An
inconclusive numerical screen or loose upper estimate is neither.
Such a stop would leave the true mean, angular maximum, actual D,
Xi realization and RH unresolved. Downstream L657/L658 integrability
and full-root scope, L661's envelope and L664's baseline retain their
existing audit qualifications; no new application is claimed.

This review spends no mathematical exploration turn and resets no
counter. It authorizes one later mathematical attempt, not another
unmotivated literature search, and establishes no new lemma.
