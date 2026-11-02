# Proposed signed spatial-root deformation test

TARGET: Test whether signed spatial-root deformation along e_r(s)=s*e_r proves m_e(-1)>=m_0(-1)-C*log n uniformly for L666's independent displacements, with absolute C and onset, retaining every spatial root, multiplicity, circle crossing and leading factor.
CHECKED: 2026-11-02
DECISION: EXPLORE
SEARCH_EVIDENCE: On 2026-11-02 searched polynomial Mahler continuity, analytic root motion, signed variation and the exact independent-displacement terminology; inspected the primary statements and relevant collision/degree-drop proof cases below. Scoped local comparison checked L649/L660/L664/L665/L666/L668 and the two prior displaced-family assessments. No exact-family signed bound was found; this is not evidence of novelty.
SOURCE_EVIDENCE: New primary readings: Parusinski--Rainer, Ann. Sci. ENS 51 (2018), Theorem 1/(1.2), pp.1344--1345, and Section 8 final collision/gluing cases pp.1370--1373 (https://www.numdam.org/item/10.24033/asens.2376.pdf); Sinclair, arXiv:math/0509591v2 (13 July 2007), Theorem 1.1 pp.1--2 and complete Section 2 pp.12--14 (https://arxiv.org/pdf/math/0509591v2). Reuse the inspected Brunault--Zudilin root formula and Dimitrov--Habegger Lemmas A.3--A.5. Chern--Vaaler's original Theorem 4 was inaccessible and is not an input.
COMPARISON: The sources supply monic root regularity through collisions and fixed-ambient-degree Mahler continuity through leading-factor loss, not a signed bound uniform in growing n. Monic normalization, its coefficient norms and degree-dependent constants must be paid. Existing absolute coefficient estimates still require relative control; L665/L668 stop different costs, not the actual full mean.
GAP: Control the signed net root-plus-leading-factor loss by C*log n uniformly over the exact displacement cube, or construct the specified admissible countersequence. Local normalization, all crossing/degree-drop junctions, and any integration of root motion must be justified; no uniform relative coefficient, root separation, noncancellation or small-loss estimate is supplied.
REASON: Primary source scope is now adequate for one bounded attempt at the unchanged target. EXPLORE approves investigation of the structured quantitative gap, not a new deformation theorem or a favorable specialization. No essential source is blocked: the inaccessible Chern--Vaaler lead is optional because fixed-degree continuity and the earlier complex quantitative comparison are available. Separate next-turn approval is still required for this newly completed assessment.
LITERATURE_REASON: The invocation began with REVIEW_REQUIRED for a new signed full-root mechanism; collision regularity and leading-factor/degree-drop source cases were essential unread coverage. This review does not repeat a ready target merely for balance.
SCOPE: Exactly TARGET and its stated L666 straight paths, using the complete-root identity, fixed-degree continuity and local monic root regularity with their actual hypotheses; permit a family-specific signed estimate or rigorous countersequence, but do not replace it by the stopped inverse-data, scalar-energy or absolute-contour tests. No degree-uniform regularity constant, globally monic normalization, or differentiability of the logarithmic mean is preapproved as a fact.

## Exact scope to assess

Use L649's full product and L666's exact family with q>=1,
n=12q+3, M=4q+1, H_0=27/(10n), x=-5/4, R=11/8 and independent
real |e_r|<=1/8 for -2q<=r<2q. The anchor x stays fixed and all
original residues remain one. For 0<=s<=1 replace each e_r by s*e_r
and retain all M spatial coefficients in G_s(-1,zeta). The denominator
angle and every grid factor are unchanged. Here m_s(-1) is the
normalized spatial circle mean of log|G_s(-1,zeta)|; m_0 refers to
the undisplaced family, not to its constant coefficient. In TARGET,
m_e denotes s=1.

The specific mechanism to assess is signed variation of the complete
root formula along this path, including the actual leading factor.
It would need to account for roots crossing the spatial unit circle,
coalescing, or escaping when degree drops. No differentiability,
uniform integrability, root labeling, cancellation formula or bound
along the path is asserted. Do not replace this by an absolute
coefficient perturbation estimate already missing relative control.
The full moment identity in L668 ensures nonzero slices, but does
not control their logarithmic variation.

L664 supplies the audited baseline at delta=1/4. If the stated
logarithmic loss held, it would support the rate-1/100 fixed-angle
benchmark and the later L661/L658 paid-arc use. This leaves arbitrary
support, realization and actual-Xi mixed positivity independent.
The desired stability is stronger than that benchmark: a failure
of this stability would not alone disprove the weaker rate benchmark.

## Invocation-start nomination (historical; completed review below)

The next invocation is literature-only. Retrieve primary theorem
hypotheses and relevant cases for parameter-dependent polynomial
Mahler measure/root variation; reuse known interpolation and root
formula coverage. Check duplicates and the precise scope of earlier
continuity failures. Distinguish inspected theorems from unread leads,
including Chern--Vaaler. No source theorem is an input until its exact
hypotheses, quantitative degree dependence and applicability are read.

If review approves a later mathematical attempt, seek a bound for the
actual signed net loss uniform over the cube of displacements, or an
explicit admissible sequence with (m_0(-1)-m_e(-1))/log n unbounded.
An absolute root-speed or coefficient norm bound too large for the
threshold is inconclusive about this signed test. A numerical screen
alone is not the required evidence. Preserve all prior stops.

This is a prospective creative mechanism at the fixed-angle gap:
it would use the movement of the full spatial zero divisor rather
than prescribed inverse data or scalar angular energy. After essential
coverage, nominate proof_attempt/creative with the precise escalation
that negative root/leading-factor variation must be bounded despite
circle crossings and dense support. The bounded decision above is
the test; do not perform it during this nomination or the source review.
For now the blocker is missing theorem-level coverage, so next-turn
routing is literature_comparison, not a mathematical approval.

Mathlib coverage for this full structured root-deformation statement
has not been checked. The previously inspected Mahler root formula
is supporting coverage only; unknown availability is not absence.

## Completed source comparison — 2 November 2026

The target and its exact family above are unchanged. This literature-only
step supplies source coverage; it derives no new family-specific result.

### Primary theorem scope

**Root motion.** A. Parusinski and A. Rainer, *Optimal Sobolev
regularity of roots of polynomials*, Ann. Sci. ENS (4) 51 (2018),
1343--1387, [Theorem 1, (1.2), pp.1344--1345](https://www.numdam.org/item/10.24033/asens.2376.pdf).
Write degree as d>=2. For a bounded
interval I=(alpha,beta), a monic polynomial
P_s(Z)=Z^d+sum_(j=1)^d a_j(s) Z^(d-j), with complex
a_j in C^(d-1,1)(closure I), every continuous root lambda is absolutely
continuous, belongs to W^(1,p)(I), 1<=p<d/(d-1), and satisfies

    ||lambda'||_Lp(I)
       <=C(d,p)*max{1,|I|^(1/p)}
          *max_(1<=j<=d)||a_j||_{C^(d-1,1)(closure I)}^(1/j).

No separation is required. Read Z^d=s, the proof strategy
pp.1346--1347, and pp.1370--1373: short-interval extension,
collision gluing and reversal of the Tschirnhausen transformation.
These selected cases are not a full audit. Monicity, fixed degree and
degree-dependent constants remain restrictions; no signed loss or
vanishing-leading-factor estimate follows from the stated theorem.

**Degree loss and continuity.** C. D. Sinclair, *The range of
multiplicative functions on C[x], R[x] and Z[x]*,
[arXiv:math/0509591v2](https://arxiv.org/pdf/math/0509591v2),
13 July 2007, Theorem 1.1, pp.1--2; Section 2, pp.12--14.
A continuous positive root function psi with psi(z)/|z| tending to one
at infinity defines a continuous multiplicative distance function
|a| product psi(alpha) on each finite-dimensional coefficient space.
The choice psi(z)=max(1,|z|) is Mahler measure. Read the entire
Section 2 proof, including escaping roots and leading factors in (2.1).
Only bounded ambient degree is used; no arbitrary unbounded-degree
limit is imported. Actual degree may drop in that space. There is no
growing-dimension rate, derivative or signed identity. The particular
nonzero coefficient path still needs verification.

**Already assessed supporting inputs.** Reuse Brunault--Zudilin,
*Many Variations of Mahler Measures*,
[Propositions 1.4--1.5, pp.6--7](https://assets.cambridge.org/97811087/94459/excerpt/9781108794459_excerpt.pdf),
with the interior, exterior and boundary-root cases recorded in
`2026-11-02-two-offset-anchor-audit.md`. For each nonzero slice this
is the actual leading factor plus the sum of log max(1,|alpha|),
including all multiplicities, constants and circle roots. It is not a
root-speed estimate. Unit-circle crossings must be treated with this
complete formula, rather than differentiating an integral with an
uncontrolled reciprocal of G.

Reuse Dimitrov--Habegger,
[arXiv:1909.06051v2](https://arxiv.org/pdf/1909.06051v2),
Lemma A.5 p.48 and the A.3--A.4 proof cases already inspected in
`2026-11-02-independent-grid-displacement-paid-arc.md`.
For nonzero complex polynomials P,Q in d variables, at most k terms
each, k>=2, with maximum coefficient norm and
rho=|P-Q|/|Q|<=1/2, it gives
m(P)<=m(Q)+C(d,k)*rho^(1/(8(k-1))).
Its comparison direction, relative norm hypothesis and growing
term-count dependence remain essential. Reversing the order requires
that order's hypotheses. No such family-uniform control is established.

### Duplicates, failed transfers and accessibility

The scoped reads covered L649's complete definitions and stop; L660's
monomial statement; L664's full-root bridge and audited baseline;
L665's hypotheses, two perturbations and qualified conclusions;
L666's exact family and observation statement; and L668's identity,
cost stop and source conventions. Its unaudited results remain
unaudited. Relevant history was searched only in the fixed-angle
source review and signed-cost stop records. The two displaced-family
assessments were read for source reuse and earlier scalar failures.
No existing resolution of the signed root-loss target was located.

L668's excessive prescribed interpolation cost occurs even for the
successful undeformed family; it therefore is not evidence that the
actual signed deformation loss is large. L665 refutes an inherited
anchor o(1) approximation and bounds one absolute contour cost from
below, not the signed change of the full logarithmic mean. L649 loses
admissible-preimage information; L660 addresses one monomial. The two
earlier scalar tests do not resolve this full-polynomial observable.
These distinctions preserve every recorded stop without reopening them.

Searches included `Chern Vaaler distribution values Mahler measure
Theorem 4 continuity polynomials`, `Mahler measure variation polynomial
roots unit circle differentiability parameter leading coefficient
continuity quantitative`, `Rainer roots polynomials analytic coefficients
locally absolutely continuous Puiseux theorem pdf`, `Mahler measure
variation roots parameter signed`, and the exact independent-displacement
terminology. Searches for stronger regularity led to the primary
monic theorem above. No inspected source matches this structured
signed bound; the bounded search establishes no novelty.

Chern--Vaaler, *The distribution of values of Mahler's measure*,
J. reine angew. Math. 540 (2001), 1--47,
[DOI](https://doi.org/10.1515/crll.2001.084), Theorem 4, remains
unread in the original. Both DOI and publisher PDF retrieval failed.
Grizzard--Gunther's published quotation was found, but is only a lead;
its real-vector version is not imported for nonsymmetric complex G.
This is an optional quantitative-continuity lead, not a persistent
essential blocker for the direct signed test. The primary continuity
proof and the previously inspected complex estimate suffice to identify
their limitations. No assertion of the original theorem's full complex
scope is made. Other search hits on arithmetic counting, random
polynomials and special bivariate measures are not applicable imports.

### Bounded continuation and limits of approval

One later mathematical attempt may test the stated signed net loss
using the actual full root divisor and leading factor. First justify
the path's coefficient regularity and nonzero slices (L668 supplies
a finite identity, not logarithmic variation), then account for local
monic normalization, coalescences, circle contacts/crossings and every
degree-change junction. Global labeling or differentiability is not
assumed. Fixed-degree continuity is available for limits, but any
integrated variation identity and its endpoint terms require proof.
This records proof obligations, not a new chart or variation lemma.
No reproof of general root regularity is justified; a family-specific
argument is needed because the source estimates do not give the
required growing-degree signed cancellation.

Continue on a rigorous C*log n loss, or a controlled remaining signed
term with a discriminating bound. An admissible sequence with
(m_0(-1)-m_e(-1))/log n unbounded stops only this stronger stability
target. Excessive absolute speed, coefficient cost or a numerical
screen alone is inconclusive; it cannot justify repeating an exhausted
transfer. Essential inputs remain L649, L666, the audited L664
baseline and L668's nonzero identity; L658/L661 are prospective
downstream uses. Support, realization and actual-Xi signs remain open.

**Mathlib.** Rechecked the official
[MahlerMeasure module](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Polynomial/MahlerMeasure.html).
`Polynomial.logMahlerMeasure_eq_log_leadingCoeff_add_sum_log_roots`,
`Polynomial.intervalIntegrable_mahlerMeasure` and
`Polynomial.mahlerMeasure_pos_of_ne_zero` support the full-root and
nonzero-polynomial scope. No full structured deformation estimate or
matching root-regularity formalization was checked. Unknown coverage
is not absence. No lemma or mathematical script was changed or run;
PROOF and DAG remain unchanged because the argument has not changed.
