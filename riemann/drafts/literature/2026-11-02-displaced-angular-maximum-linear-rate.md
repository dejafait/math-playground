# Displaced-family angular maximum: source comparison

TARGET: Test whether L666's displaced family satisfies max_(|u|=1) mean_(|zeta|=1) log|G_e(u,zeta)| >= -n/100-C*log n with absolute C and onset, using the full angular dependence and retaining every unit residue and all M spatial moments.
CHECKED: 2026-11-02
DECISION: EXPLORE
SEARCH_EVIDENCE: On 2026-11-02 searched joint angular/spatial logarithmic means, Mahler lower bounds for rational functions and sums of Blaschke products, positive residues, and degree/support-sensitive norm comparisons; inspected the primary results and local records below. No matching uniform displaced-family theorem emerged from this bounded search; novelty is not established.
SOURCE_EVIDENCE: New scope: Akhtari--Vaaler arXiv:1810.12413v1, Theorem 1.2 p.3, ordering discussion pp.3--4, Lemmas 3.1--3.2 and complete proofs pp.6--8, complete Section 4 proof pp.8--9 and its Boyd Lemma 2 reference. Rechecked Defant--Mastylo arXiv:1508.05556v1, (4)--(5) p.2 and Theorem 3.1/full proof pp.7--8; reuse the inspected Danchenko--Semin Theorem 2 and full-root/integrability sources identified below.
COMPARISON: The multivariable coefficient theorem retains support-order binomial costs; the sharp torus norm theorem retains separate-degree costs. Neither supplies a large signed coefficient or the prescribed angular maximum. L666's rational quadrature is an exact scalar energy identity, not spatial logarithmic coercivity. L669's accepted fixed-angle obstruction does not decide this weaker angular target.
GAP: Establish or refute H>=-n/100-C*log n uniformly over the exact displacement cube. Any coefficient, joint-torus or angular observation route must verify its signed family estimate, denominator charges and quantitative costs; no favorable noncancellation, sparsity, angle or uniform root-motion constant is available from the sources.
REASON: Essential source comparison is adequate for one bounded full-angular attempt at the unchanged TARGET; no selected essential source is blocked. EXPLORE records source readiness, not the inequality or a new specialization. This newly ready assessment receives separate approval next turn before mathematics; that approval can reuse these readings without fresh browsing.
LITERATURE_REASON: Invocation-start coverage was REVIEW_REQUIRED for angular selection after the fixed-angle stop. The changed joint angular/spatial scope required comparison with multivariable coefficient and torus norm theorems; prior scalar sampling and fixed-angle assessments alone did not approve it.
SCOPE: Exactly TARGET for the fixed L666 displacement family, all original unit residues, full grid including j=0, denominator angle 1/u, and every 0<=k<M moment. One later signed full-angular proof or admissible full-angular countersequence test is covered, using the inspected polynomial/root, rational-observation and finite algebra inputs. New external theorems, arbitrary support, modified residues, uniform-in-K onsets and Xi transfer require separate coverage.

## Exact proposed target and downstream use

Use L649's full B_u(v), including j=0 and the denominator angle 1/u,
and L666's definitions of c_k(u) and G_e(u,zeta). Keep q>=1,
n=12q+3, M=4q+1, x=-5/4, R=11/8, U=121/64, H_0=27/(10n),
and the fixed anchor x together with
x+i*H_0*(r+1/2+e_r), -2q<=r<2q, real |e_r|<=1/8.
All original residues remain one, and 0<=k<M includes every spatial
coefficient. No symmetry is imposed. The same displaced poles must
serve every angle; the maximizing angle may depend on that family.
Both circle means are normalized. C and the onset must be absolute
over this whole displacement cube and allowed sequence of n.

A successful bound is intended to supply the logarithmic-height input
for L658/L661's paid-arc comparison. Its precise normalization and
diagonal charges must be checked from those canonical results before
application; this nomination proves no transfer. General support,
Xi realization and actual mixed signs remain independent gaps.

The bounded mathematical decision, if a later review approves it,
is a proof of the stated uniform threshold or an admissible sequence
with (-max_u mean_zeta log|G_e|-n/100)/log n unbounded above.
Cancellation at u=-1 alone does not decide this target. An excessive
absolute contour cost, prescribed inverse-interpolation cost or scalar
energy bound alone is likewise not the required signed full-mean test.

## Nomination and reuse

Reuse relevant inspected results from
2026-11-02-independent-grid-displacement-paid-arc.md,
2026-11-02-signed-finite-deweighting-cost.md and
2026-11-02-signed-spatial-root-countersequence-audit.md where their
hypotheses apply. Check the exact angular rational-observation sources
behind L666, including whether their actual conclusion reaches a
spatial logarithmic mean rather than only a scalar or squared norm.
Search the exact joint angular/spatial statement, stronger results
and known obstructions before approving a mechanism. Treat unread
primary statements and unaudited local claims as such.

Read only the necessary parts of L649, L658, L661 and L666 for the
proposed application, with L664 as the audited undeformed comparison
and L669 as the accepted fixed-angle obstruction. In particular do
not reopen the stopped logarithmic fixed-angle transfer or assume its
failure also settles the present linear-rate angular maximum. Preserve
the recorded scalar, inverse-data and absolute-cost stops. No uniform
root separation, degree, K-onset, relative coefficient bound, favorable
angle or Xi realization is assumed.

Mathlib coverage of the full proposed statement has not been checked.
The inherited Mahler-measure module supplies supporting polynomial
facts only; no full matching formalization or absence claim is made.
The nomination was initially uncovered. The completed comparison below
supersedes that source status without supplying a mathematical result.

## Completed source comparison — 2 November 2026

### Primary statements and essential proof cases

S. Akhtari and J. D. Vaaler, *Lower bounds for Mahler measure that
depend on the number of monomials*,
[arXiv:1810.12413v1](https://arxiv.org/pdf/1810.12413v1),
29 October 2018, Theorem 1.2 p.3: a nonzero complex trigonometric
polynomial F on a finite-dimensional torus has finite Fourier support
contained in S={k_0,...,k_s}. Order S by an injective homomorphism
from the integer exponent lattice to the reals. Then

    |F_hat(k_j)| <= binomial(s,j)*M(F),  0<=j<=s.

Here M is multiplicative Mahler measure with normalized Haar measure.
No integrality or coefficient sign is required. Different orders can
give different bounds. Read the ordering discussion pp.3--4,
Lemmas 3.1--3.2 with their proofs pp.6--8, and all of Section 4
pp.8--9. The proof preserves support order in integer specializations,
uses the univariate inequality, and invokes Boyd's limsup inequality
([2], Lemma 2, J. Number Theory 13 (1981), 116--121). Boyd's original
proof was not separately read; Lawton's stronger equality is unnecessary.
This is a citation candidate, not a reproof. Neither a large exposed
coefficient nor favorable support size/order for our cleared numerator
is supplied. Any use must also account for its rational denominator.

A. Defant and M. Mastylo, *Lp-norms and Mahler's measure of polynomials
on the n-dimensional torus*,
[arXiv:1508.05556v1](https://arxiv.org/pdf/1508.05556v1),
23 August 2015, Theorem 3.1 pp.7--8, gives, for a complex polynomial P,
normalized torus measure, p>0 and separate variable degrees d_j,

    ||P||_p <= product_j Lambda(p,d_j)*M(P),
    Lambda(p,d)=||(1+z)^d||_p.

Rechecked the full induction, Fubini/Jensen, Fatou/Minkowski, and
product extremizers; the one-variable Arestov input (4)--(5) is cited,
not independently reproved. At p=2 the source records
Lambda(2,d)=sqrt(binomial(2d,d)) on p.11. Sharpness concerns all
polynomials, not realization of an extremizer by our family. The
changing spatial degree and cleared angular degree cannot be discarded;
an energy bound does not thereby acquire the requested logarithmic rate.

Reuse the following adequate primary readings rather than repeat them:

- `2026-11-02-displaced-signed-angular-sampling.md`: Danchenko--Semin,
  arXiv:1503.06476v1, Section 1.1 Theorem 2, PDF pp.1--2 and full
  proof pp.6--7. Its r=s=1 formula requires the finite interior pole
  set with 0, reflected completion, ordinary pole orders <=1 and
  combined 0/infinity order <=1. It exactly observes the squared norm
  of one combined complex rational function. Positivity of observation
  weights does not assert positivity of its signed cross terms.
  L666's membership and formulas remain unaudited local applications.
- `2026-11-02-localized-logarithmic-joint-moment.md`: Issa--Lalin,
  arXiv:1203.5379v1, Remark 3.8 and Theorem 4.1/proof p.7, supplies
  logarithmic integrability for nonzero complex polynomials, including
  torus zeros; it supplies no family-uniform small-value estimate.
  Its Tikhonov--Yuditskii Remez comparison is a supremum comparison
  on a supplied measurable set, not the present signed log-mean bound.
- `2026-11-02-signed-spatial-root-countersequence-audit.md`:
  Brunault--Zudilin, Propositions 1.4--1.5 pp.6--7, retains all spatial
  roots, boundary roots and the actual leading factor. Sinclair v2,
  Theorem 1.1 with Section 2, provides fixed-ambient-degree continuity
  through degree loss, without a growing-degree quantitative rate.
- `2026-11-02-displaced-full-spatial-fixed-angle.md` and
  `2026-11-02-independent-grid-displacement-paid-arc.md`: reuse the
  univariate coefficient, inverse-moment and perturbation comparisons.
  Changed quadrature weights or missing relative coefficient control
  cannot be inserted into this unit-residue problem.

### Local overlap, threshold and the bounded attempt

Read L649's full family and conclusions, L658's complete statement,
L661's general envelope and scope qualifications, L664's family and
audited conclusion, L666 sections 1--4, and L669's hypotheses,
accepted conclusions and source scope. Read the fixed-angle stability,
individual inverse-row and prescribed signed inverse-data ATTEMPTS
records, plus the focused step-29 history. No sibling notebook was read.

These records do not duplicate the angular-maximum target. L649 stops
an ambient inverse transfer. L667/L668 stop particular recovery costs,
even on the undeformed baseline; they do not upper-bound H. L669's
fixed-K cancellations and K-dependent onsets cannot be promoted to a
full-angular linear-rate countersequence. L664 supplies only the
undeformed benchmark. No local unaudited claim is upgraded by this review.

The proposed downstream use is L658's paid localization combined with
L661's actual-diagonal envelope. L658 requires comparison with
(log D)/2-n/32+log n. The earlier fixed-angle assessment already
records the available linear loss budget 261/20000 and the proposed
1/100 benchmark; the exact constants and uniform onset must still be
assembled in a mathematical turn. This review establishes no paid-arc
inequality. General support, realization and Xi signs remain independent.

A later attempt may use angular dependence of the complete signed
polynomial or the cleared joint numerator, retaining every denominator
charge and spatial root. The new multivariable theorem is optional:
if used, its actual support, ordering, coefficient size and cost must be
verified, not assumed. A scalar c_0 lower bound can be sufficient via
the existing Jensen bridge, but is not necessary for H. No new
identity, coefficient estimate, countersequence or numerical test was
derived here; there is no reason to reprove any cited theorem.

Continue on a uniform proof with absolute C/onset, an admissible sequence
with (-H-n/100)/log n unbounded above, or a quantitatively isolated
signed term whose bound would decide that discriminator. A finite
screen or a large absolute/inverse cost alone is inconclusive. Stop a
specific proposed mechanism if its verified cost exceeds the benchmark;
do not infer failure of H from failure of that mechanism. Fixed-angle
failure alone is insufficient. Preserve partial reasoning before any
lengthy subsequent proof or calculation.

### Search and access record

Queries included `Mahler measure rational functions lower bound
coefficients multivariate maximum`, `rational functions lower bound
Blaschke sum residues circle norm`, `Mahler measure Remez polynomial
coefficient inequality`, `sum Blaschke products lower Mahler measure`,
`rational angular maximum logarithmic mean polynomial`, and
`Mahler measure positive residues`. Searches returned general Mahler
and rational-function literature, not the exact family theorem. Search
snippets and nonprimary pages were discovery aids only; conclusions
above rely on the identified primary papers and ready assessments.

Text retrieval succeeded for both newly inspected primary passages.
One screenshot request for Akhtari--Vaaler p.9 timed out; complete
relevant text was then retrieved and read, including (4.4)--(4.7) and
the end of the proof. Thus no selected essential source remains blocked.
Boyd's original proof and Lawton's stronger identity are unused source
leads, not silently verified inputs or reasons for another source turn.

Matching Mathlib coverage remains unchecked. Reuse the recorded
univariate `Polynomial.logMahlerMeasure_eq_log_leadingCoeff_add_sum_log_roots`
support only; no full multivariable or displaced-family formalization
or absence claim is made. Separate approval of this changed assessment
is the next gate, with no additional generic literature search needed.
