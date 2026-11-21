# Complete localized Stokes identity — bounded cutoff nomination960

TARGET: Attempt the localized distributional identity d beta_chi=gamma_chi for the complete zero-extended space-time pullback under C466s, by controlling mixed minors and survivor-cutoff flux.
CHECKED: 2026-11-14
DECISION: EXPLORE
SEARCH_EVIDENCE: Source review960 completed exact/stronger searches for singular-flow pullback currents, zero extension, removability, rough transport and worldvolume boundary identities; no matching theorem was identified. Scoped local duplicates and stops927/932/941/947/948/959 were compared. This is bounded coverage, not certified novelty.
SOURCE_EVIDENCE: Full comparison in assessment959/review960; Harvey–Polking Acta Math.125(1970) Theorem2.1/Lemma2.2 and proofs pp40–41, Theorems4.1–4.2 pp45–46, Theorem5.2 pp48–49 https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/6102-11511_2008_Article_BF02838327.pdf; TNV1706.03822v2 Section2.2 https://arxiv.org/html/1706.03822v2#S2.SS2; reuse TNV AppendixB and WKM2008.10321v2 Proposition5 with proofs via954/955/957, https://arxiv.org/pdf/2008.10321v2.
COMPARISON: Smooth-survivor variational/compound machinery and primary weak cutoff proofs are available. General removability/transport theorems have unpaid mass, geometry or trace premises. Only the complete singular-flow specialization and its limit passage are proposed for investigation.
GAP: Establish complete-form L1_loc control and vanishing survivor-cutoff flux with all stopped events included, or detect failure with an admissible example; no complete-form envelope, regular survivor boundary, trace, or defect-free identity is assumed.
REASON: Source review960 supplies adequate coverage for one established-tool attempt after separate approval; it derives no mathematical specialization. The signed transport premise is independently testable and could pay a local boundary step without signing an actual-Xi determinant.
SCOPE: Exact C466s bidisk/common derivative data and unit flat raw flow; finite physical time, arbitrary compact ambient smooth cutoff, compact tests in Q, all complete pullback coefficients, zero extension at finite stopping and r=0; no changed metric, regular hitting surface or worldvolume immersion assumption.

## Exact mathematical question, unproved

Retain all C466s hypotheses: real 0<a<R and0<b<L, fixed complex
H_0, finite nonnegative M_1,M_2, H holomorphic on
B={|q|<R,|z|<L}, H(0,0)=H_0, and Hermitian bounds
||grad H||_2<=M_1, ||D^2H||_op<=M_2 throughout B. Use the unit
flat raw flow dot X=conjugate(grad S), S=-2 log q+H(q,z),
X(0,r,s)=(ir,s). A local logarithm suffices. I=(-a,a) times(-b,b).
Let tau(r,s) be maximal lifetime in U=B minus{q=0}.

Fix any finite T_0>0, Q=(0,T_0) times I, and let D_H be its
survivors with r!=0. Psi=X on D_H only. For any smooth scalar
chi compactly supported in B, put Omega=q^2 exp(-H) dq wedge dz,
beta_chi=Psi^*(chi Omega), and
gamma_chi=Psi^*(dchi wedge Omega). Bars denote coefficientwise
zero extensions from D_H to Q. The target is that both bars are
L1_loc and d bar(beta_chi)=bar(gamma_chi) distributionally on Q.
There is no flow map defined through q=0 or after outer exit.
Tests have compact support in Q, not necessarily away from r=0
or from any stopping locus. Simultaneous events are included.
No uniform assertion over unbounded time is sought.

The explicit gamma_chi must be retained; no signed integral
invariance, sign, global homology or endpoint-free identity is
part of the conclusion. Physical boundary localization does not
authorize omitting a prior outer escape or assuming a continuous
lifetime function.

## One bounded test and stopping rule

For each fixed H,chi and compact test support, seek smooth
survivor-domain cutoffs eta_j, 0<=eta_j<=1, approaching1 at every
surviving point, with support away from its stopping and excluded
initial-coordinate loci. The quantitative goals are:

- complete coefficientwise L1_loc convergence of the zero-extended
  eta_j beta_chi and eta_j gamma_chi to their bars;
- for every smooth compactly supported scalar test phi on Q,
  integral_{D_H} phi d eta_j wedge beta_chi ->0.

Construct the cutoffs and justify the smooth interior exterior-
derivative identity and the distributional passage, including all
orientation/sign conventions. These are requested proof tasks, not
an asserted new criterion proved by this nomination. A single
uniform norm bound is not mandatory if another rigorously justified
method pays the same complete-form limits. In particular HP's
homogeneous removability theorem requires an explicitly justified
operator/unknown formulation before any use for this equation.

Begin with the assessed real variational/compound tools on compact
surviving intervals; ask whether they can control the mixed minors
as well as the spatial determinant, and then the cutoff error.
No estimate for those new quantities has been calculated today.
Do not replace the actual raw physical-time flow by a complete
modified flow, or assume survivor-boundary geometry from the
ambient analytic divisor. Account for r=0 and earlier escapes;
do not presume that chi alone makes the exhaustion smooth there.

Continue if all required limits can be justified. A negative result
requires an admissible H and compact chi/test with rigorously
nonintegrable complete coefficient or nonzero distributional defect.
If only the chosen estimate or exhaustion fails, preserve the
precise unpaid quantity and stop that method without refuting the
identity. Preserve partial reasoning before extended work; do not
replace this bounded test by another absolute-density replay.

The full source comparisons, inspected proof cases, versions,
queries and access qualifications are in
[review960](2026-11-14-collision-current-stokes-source-959.md).
C466s is the essential local theorem; the scalar C466q/C466r are
comparisons only. Stops927/932/941/947/948/959 keep their scopes.
There is no cross-notebook input. Matching Mathlib coverage is
unchecked. A future canonical result must include all hypotheses,
full limit justification and the same qualifications.

This is development using established volume/cutoff machinery,
not a creative central sign mechanism. Signed global integration,
actual-Xi realization, all-order positivity, metric normalization,
intersecting divisors and other endpoint costs remain independent
gaps. There is no RH candidate. This new EXPLORE nomination needs
separate approval next turn before its mathematical invocation;
no part of the requested proof has been attempted in review960.
