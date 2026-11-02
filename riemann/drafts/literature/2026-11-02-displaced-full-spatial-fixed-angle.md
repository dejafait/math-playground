# Full spatial logarithmic mean after the scalar sampling reassessment

TARGET: Test whether the full spatial logarithmic mean m(-1) for L666's independently displaced family satisfies m(-1) >= -n/100-C*log n uniformly, with an absolute C and onset and all M moments and roots retained.
CHECKED: 2026-11-02
DECISION: EXPLORE
SEARCH_EVIDENCE: Completed a bounded search on 2026-11-02 for complex-coefficient and fewnomial Mahler lower bounds, structured moment/power-sum polynomials, positive residues, and inverse Vandermonde recovery; inspected the primary statements/proof cases below. Reused the ready root-formula, norm, continuity and pure-power comparisons and checked L649/L660/L663/L665 stops. No exact-family theorem was identified; no novelty follows.
SOURCE_EVIDENCE: New readings: Akhtari--Vaaler arXiv:1810.12413v1 (29 October 2018), (1.3) p.1, Theorem 1.1/Corollary 1.1 p.2, complete Section 2 proof pp.4--5 (https://arxiv.org/pdf/1810.12413v1); Gautschi, Numer. Math. 4 (1962), 117--123, (1.1)/(1.4), Section 2 lemma/proof pp.118--119, Theorem 1/proof p.119 (https://www.cs.purdue.edu/homes/wxg/selected_works/section_01/016.pdf). Existing primary readings are reused below; no new lower bound is imported into the argument.
COMPARISON: Known coefficient-to-Mahler bounds apply to complex slices but retain binomial degree/term-count losses; finite inverse moment recovery retains full products of node gaps. Neither directly proves the rate 1/100. Existing continuity needs unproved relative coefficient control; unweighted power-sum theorems do not remove the actual complex weights. The different full-circle, ambient inverse, monomial and inherited-anchor stops do not decide this target.
GAP: For the exact independent-displacement family, obtain family-restricted signed moment control sufficient for the full spatial logarithmic mean, paying all binomial and inverse-recovery costs. No source inspected supplies m(-1)>=-n/100-C*log n, a uniform favorable cost, or a countersequence. Finite moment recovery is now an assessed mechanism to test, not a proved transfer.
REASON: The theorem-level comparison is adequate for one bounded mathematical test of the unchanged target using complete finite moment recovery and cited Mahler bounds. EXPLORE records source readiness only; no favorable specialization, quantitative obstruction or new lemma was derived in this literature-only turn. The newly changed assessment receives separate next-turn approval.
LITERATURE_REASON: The invocation began with REVIEW_REQUIRED coverage for a changed full-polynomial target. This turn resolves its coefficient-to-Mahler and finite moment-recovery source scope; it does not repeat a ready assessment to fill a quota.

## Exact proposed target and relevance

Retain L666's family: q>=1, n=12q+3, H_0=27/(10n), fixed
x=-5/4, and nonanchor poles
x+i*H_0*(m+1/2+e_m), -2q<=m<2q, with independent real
|e_m|<=1/8. All M=4q+1=n/3 original residues are one. Keep
L649's R=11/8, U=R^2, complete t_j=j/n product, conjugated
angular denominator, and all coefficients 0<=k<M in G.

The proposed quantity is exactly

    m(-1)=mean_(|zeta|=1) log|G(-1,zeta)|.

No symmetry of the displaced set is assumed. Use L658's inherited
L657 nonzero-slice and integrability results, actual degree and leading
factor, every spatial root including multiplicities and boundary roots,
and the actual squared-residue D. The target permits a uniform onset
and an absolute C independent of n and the displacement vector.

The main gap remains actual-Xi mixed positivity and unbounded-height
signs. A positive result at this one angle would supply a lower bound
for H and could feed L658's paid arc with L661's diagonal envelope.
The nominated loss 1/100 is below the available rate
1/32-91/5000=261/20000; it is a benchmark to test, not a proved
loss. Arbitrary support, Xi realization and all-degree signs remain
independent. A failure at this angle would not refute H or RH.

## Invocation-start nomination and source-review task

L666's two scalar attempts gave exact rational observation and a
bounded diagonal deformation, but neither controls the signed energy
relative to D. Repeating quadrature, finite optimization, or an absolute
derivative bound is not the next mechanism. The new target retains
the spatial information discarded by c_0. It is stronger than needed
for H at one fixed angle, but has a concrete falsification test.

First reuse the existing Mahler and perturbation assessments. Compare
precise primary statements for lower bounds from structured polynomial
coefficients or finite moment sequences, with their degree costs.
The general coefficient-to-Mahler inequalities and finite Vandermonde
recovery are search leads only; no quantitative application is assumed.
Check the previously recorded L649 ambient deweighting limitation and
L660 monomial obstruction before selecting a specific transfer. Do not
reuse the stopped absolute contour error or assume a degree-independent
Mahler continuity constant. An uninspected theorem remains a lead.

Continue to a later mathematical turn only after a precise theorem
comparison approves an exact full-polynomial test at the target rate,
or identifies a concrete unproved cost with a discriminating threshold.
Abandon this fixed-angle benchmark if an admissible countersequence
has (m(-1)+n/100)/log n tending to minus infinity, or a proposed
transfer has a verified loss above its available budget. A transfer
failure alone is not a counterexample to the benchmark, and a
fixed-angle counterexample alone is not a counterexample to H.

Essential later inputs: L649 definitions; L658 and its inherited L657
nonzero/integrability scope; L661's audited general diagonal envelope;
L664's audited exact-grid benchmark. L665 and L666 are qualified
comparisons, not proofs of the new lower bound. Their unaudited parts
remain unaudited. No lemma, mathematical script or new bound is
created by this nomination. Matching Mathlib coverage is not checked;
reuse the previously recorded supporting MahlerMeasure coverage.

## Completed bounded comparison — 2 November 2026

This section supersedes the nomination's incomplete-source status, not
its mathematical target. The exact family and loss benchmark above stay
unchanged. The full bound remains unproved.

### New primary statements and their scope

**Coefficient bounds.** S. Akhtari and J. D. Vaaler, *Lower bounds for
Mahler measure that depend on the number of monomials*,
[arXiv:1810.12413v1](https://arxiv.org/pdf/1810.12413v1),
Theorem 1.1, p.2: if a nonzero complex polynomial has a representation

    P(z)=sum_(j=0)^s b_j z^(h_j),  0<=h_0<...<h_s,

then, with normalized-circle multiplicative Mahler measure,

    |b_j|<=binomial(s,j)*M(P),  0<=j<=s.

No integrality, realness or sign condition is imposed. Equation (1.3),
p.1, is the classical degree-indexed inequality, sharp for (z+/-1)^s.
Read the entire univariate proof, Section 2 pp.4--5: monomial removal,
constant and binomial cases, reversal, derivative inequalities,
induction and endpoint indices. No reproof is needed. This covers
our nonzero complex spatial slice. Its coefficient noncancellation
and growing binomial cost remain obligations; no bounded term count
is known. This theorem does not turn coefficient energy into a
logarithmic mean without that cost. Its multivariate extension is
not imported.

**Finite moment recovery.** W. Gautschi, *On inverses of Vandermonde
and confluent Vandermonde matrices*, Numerische Mathematik 4 (1962),
117--123, [Theorem 1, p.119](https://www.cs.purdue.edu/homes/wxg/selected_works/section_01/016.pdf).
For distinct complex nodes z_1,...,z_N and columns
(1,z_j,...,z_j^(N-1))^T, the maximum row-sum norm satisfies

    ||V^(-1)||_infinity
       <=max_i product_(j!=i) (1+|z_j|)/|z_i-z_j|.

Read the matrix/norm conventions (1.1)/(1.4), Section 2's
symmetric-coefficient lemma and its three argument cases,
pp.118--119, and the complete Theorem 1 proof from explicit inverse
entries. The theorem needs distinctness, not real nodes, symmetry,
or a fixed lower separation. Applying it to the actual a/R nodes
requires retaining every node gap, normalization and all M moments;
a dimension-free recovery constant is not supplied. Same-ray equality
is a source qualification, not a hypothesis satisfied by our vertical
family. No local recovery identity or cost has been derived here.

### Reused assessments, duplicates and limitations

Reuse the following inspected-source records, without claiming a new
manuscript audit or rederiving any of their conclusions:

- `2026-11-02-two-offset-anchor-audit.md`: Brunault--Zudilin,
  *Many Variations of Mahler Measures*, Propositions 1.4--1.5,
  pp.6--7, including boundary roots, leading factors and multiplicity.
  This supplies the complete-root interpretation, not a numerical
  lower bound for its actual roots.
- `2026-11-02-independent-grid-displacement-paid-arc.md`:
  Dimitrov--Habegger, arXiv:1909.06051v2, Lemmas A.3--A.5,
  pp.45--48. Relative coefficient proximity, term-count constants,
  the exponent 1/(8(k-1)), and the direction of comparison remain
  essential. No such relative control is available here.
- `2026-11-02-localized-logarithmic-joint-moment.md`:
  Defant--Mastylo, arXiv:1508.05556v1, Theorem 3.1/proof,
  pp.7--8 and Theorem 4.2 p.11. The sharp univariate L2-to-Mahler
  factor is sqrt(binomial(2d,d)); the source comparison already
  retains its growing-degree loss. No new small loss is assumed.
- `2026-11-02-positive-mass-angular-propagation.md`: Biro's
  unweighted power-sum theorem, p.344. Original unit residues do
  not make W_a(-1) positive or unweighted. L649 already records
  the failed ambient deweighting mechanism.

The local comparison read L649's full definitions, conclusions and
source scope; L658's definitions, localization threshold and inherited
nonzero/integrability scope; L660's statement and source comparison;
L661's general envelope; L664 Section 7's full-polynomial logarithm
bridge; L665's hypotheses, conclusions and source scope; and L666's
hypotheses and conclusions. Existing nomination/ready assessments
supply the recorded Section 6 comparison and two unproductive scalar
attempts. No omitted proof or unaudited specialization is silently
accepted. The exact-grid baseline is audited; L665/L666 retain their
existing qualifications.

L649 concerns an ambient infinite-sequence coisometry and loses the
permitted preimage information. A finite inverse at the actual M
nodes retains that information, but may incur excessive costs. L660
stops one phase-neutral monomial, not a full finite polynomial
functional. L663 and its canonical attempt record stop full angular
averaging on another lattice. L665 stops an o(1) inherited-anchor
approximation and one absolute contour cost. Neither those stops nor
the unresolved scalar attempts establish failure of this fixed-angle
full-polynomial bound. No duplicate resolution was identified in this
bounded check.

### Search record and inaccessible or unread leads

Queries included `Mahler measure polynomial coefficient bound binomial
coefficients complex polynomial theorem`, `Mahler measure power sums
complex moments polynomial lower bound Turan`, `Gautschi inverse
Vandermonde matrix norm product node differences theorem pdf`,
`"Mahler measure" "moment polynomials"`, `"Mahler measure"
"positive residues"`, `"Mahler measure" "power sums"
"complex coefficients"`, and searches for Cauchy-transform and
weighted-power-sum formulations. The searches found the primary
coefficient result and inverse theorem above, not an inspected result
for these exact structured weights. Unrelated counting/average-Mahler
results and arithmetic-coefficient bounds are not imports. Absence
from this bounded search establishes no novelty.

Gautschi's primary web PDF text and proof were accessible; a local
curl download failed DNS and screenshot calls returned only reference
text through this tool interface. No visual reading is claimed.
Chern--Vaaler Theorem 4 remains the earlier assessment's unread
continuity lead; it is not essential for the direct finite recovery
experiment and is not cited as a proved estimate here. No persistent
source blocker prevents the stated test.

### Approved later bounded test and decision rule

SCOPE: One mathematical attempt at the exact TARGET using finite moment recovery at the actual displaced nodes and the inspected coefficient/Mahler bounds or complete-root formula; retain the complete spatial polynomial and actual weights, do not repeat L649's stopped ambient inverse, and review any new theorem-dependent mechanism outside this scope.

Use essential inputs L649, L658 with inherited L657 nonzero-slice,
integrability and full-root scope, L661's audited general diagonal
envelope, and L664's audited exact-grid baseline; L666 specifies the
family and L665 supplies only qualified comparisons. Assess the finite
inverse's anchor row or another explicitly bounded full-moment
functional without discarding signed terms. Keep binomial costs,
all node gaps, degree drops, normalization, and the actual D. This is
a proposed mathematical test, not an assertion of a favorable bound.

Continue this mechanism only if its certified total cost can meet
m(-1)>=-n/100-C*log n with absolute C and uniform onset, or a
quantitatively controlled remaining term gives a discriminating next
test. A verified recovery/transfer loss above that budget stops that
transfer, not the benchmark. An admissible countersequence with
(m(-1)+n/100)/log n tending to minus infinity stops the fixed-angle
benchmark, not H, Xi signs or RH. Inconclusive numerical screens do
not justify another repetition. Prior exploration usage is preserved;
this literature turn does not reset it.

Mathlib's [official MahlerMeasure module](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Polynomial/MahlerMeasure.html)
was checked on 2026-11-02. The exact classical theorem
`Polynomial.norm_coeff_le_choose_mul_mahlerMeasure` bounds the norm of
coefficient k by natDegree.choose(k) times multiplicative measure.
The module also contains the root formula, polynomial logarithm
integrability and Landau upper bound already recorded. These are
supporting results; no matching family-specific lower bound or
fewnomial/finite-recovery formalization was checked. Nonzero analytic
slice hypotheses are still required despite Lean's totalized logarithm.

DECISION EXPLORE completes source coverage for this bounded test only.
It establishes neither the target nor an informative mathematical
negative. No lemmas or mathematical scripts were changed or run.
PROOF and DAG stay unchanged because the argument has not changed.
