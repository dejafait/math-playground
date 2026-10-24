# Complete co-closed cubic-probe response — proposed rate review

TARGET: Prove that L193's complete co-closed cubic-probe response |E[F_i rho_F]| is at most C_i N^(5/2)log(eN)^2 for both actual probes.
CHECKED: 2026-10-23
DECISION: EXPLORE
SEARCH_EVIDENCE: Reused the 2026-10-14 joint-probe assessment and 2026-10-20 complete-rate inventory; compared L189--L193's stated estimates and load-bearing heat-transfer/endpoint cases, history/231 and ATTEMPTS/043. Four bounded exact/stronger-result web queries below found no adequate match; search failure is not novelty evidence.
SOURCE_EVIDENCE: Reused the inspected primary passages in the joint-probe assessment and rechecked Luescher--Weisz 1101.0963v2 sections 7.1--7.2, 8.2, 8.4; Del Debbio--Patella--Rago 1306.1173v1 section 6, (6.11)--(6.16); Ramos--Sint 1508.05552v1 section 3.4, (3.43)--(3.45) and its boundary qualifications. Reused the precise Isserlis coverage in the 2026-10-23 prefix-sextic assessment. None supplies the selected mesh rate.
COMPARISON: L193 gives a zero cubic-scaled limit, an O(N^2) final-observable response, uniform W derivative envelopes, and only an O_delta(N^2) positive-time rho_H pairing. L189/L190 give uniform initial-time removal at cubic scale. Neither their qualitative assembly nor the primary full-correlation results establishes the requested quantitative bound; L264 estimates an independent block.
GAP: Obtain uniform quantitative control of the complete rho_H Duhamel pairing near zero, assemble it with all W placements and the final observable, and retain both endpoints and full heat sums within the exact target budget. Fixed-delta constants must be quantified before any varying time split.
REASON: Essential source comparison is complete enough for one bounded research attempt on the unchanged target. EXPLORE approves the attempt, not the proposed estimate or a new theorem; the needed selected-group rate is not imported and no mathematical result is derived here.
LITERATURE_REASON: The sharper complete co-closed response rate was REVIEW_REQUIRED and lies outside the prior qualitative joint-probe assessment; its changed quantitative requirement needs this separate comparison.
SCOPE: Relative SU(2) cube, sufficiently fine admitted even N, a=8/N, tau=1/16, lower-rooted direction-1 forest, stored full-link coordinates, bare-first expansion, actual probes 3 and 6, all physical/source/end rows, constant modes and heat sums; only the complete co-closed response in L193(1)--(2).

Essential input IDs: L181 L182 L183 L189 L190 L191 L192 L193.
L193 fixes F_i=F_(i,3)(z), including the complete final observable
cubic and the quadratic-flow integral on [0,tau]. L183 fixes
rho_F=rho_H-<Lz,W>, with rho_H=script R_3-d script S_3[2SAz]
and W=P db(z)[2SAz]. Both residual Q forms, all three differentiated
action placements, both derivatives of the moving prefixes and the
signed tilt's original order must remain. Do not replace F_i(z) by
F_i(Rz), or rho_F by rho_H. All upstream analytic and audit premises
remain imports. L264 is contextual evidence that a different rate
block is now audited; it is not an estimate for this object.

Plausible use: together with the separately controlled prefix sextic
and quartic placements, a successful rate could close the joint cubic
probe-jet component of the quantitative L011 budget. The transverse-H
rate, full assembly and its upstream qualifications, interacting
reflected comparison, continuum axioms and finite positive infrared
mass remain independent gaps. No complete solution is proposed.

The discriminating test after source approval is a uniform estimate
for the full response at the stated N^(5/2)log(eN)^2 threshold,
including both flow endpoints before summing all heat modes. A useful
partial estimate must identify its remaining term explicitly. If the
known bounds leave a larger allowance, record that allowance and the
responsible placement; it is not signed growth. No fixed-delta limit
may receive a varying delta without a uniform finite-mesh bound.

## Exact local comparison and recorded failures

The startup overview and local DAG were supplied in full. Scoped searches
of TARGET/COVERED_TARGET lines and L193 occurrences in the recent local
assessments found the registered target, the qualitative joint review,
the complete-rate inventory and the separate sextic target. No ready
assessment or theorem for this exact rate was found. This is a duplicate
check within the searched scope, not an exhaustive originality claim.

Read L189's hypotheses, (1)--(4), full relative spectral bounds and
initial-integrability argument; L190's hypotheses and (1)--(3);
L191's external-placement statement and its quadratic-output estimates;
L192's hypotheses, (1)--(4), short-time spectral proof and complete
polarized-action estimate; and L193's hypotheses and proof sections
1--4, including the actual compact-stencil regularity at s=tau.
These are imported premises, not critically reaudited results here.
The precise useful statements are:

- L189(2)--(3): the probe norm has an integrable uniform envelope and
  initial integral norm at most C_i eta(delta).
- L190(1)--(3): ||rho_H||_2<=C N^3, with exact forest pairing given by
  the rho_H pairing minus the W derivative. This does not bound rho_F
  by the same norm.
- L193(11)--(13): heat transfer is exact for the color-alternating pure
  cubic cross contractions because S commutes with heat. Its resulting
  positive-time rho_H estimate is C_delta N^2; its constant is not
  quantified uniformly as delta decreases.
- L193(15): the external W derivative is bounded by C_i N^2 m_a(s)
  for the entire interval 0<=s<=tau.
- L193(16): the two short-output placements satisfy
  a^3 |B_(i,a)(s)|<=C_i sqrt(a)[(s+a^2)^(-1/2)+(s+a^2)^(-1)]
  for that same entire interval. L192 proves the corresponding explicit
  integrated bound on [0,delta] in (3). These are quantitative inputs,
  not estimates transferred from a fixed-delta limit.
- L193(19)--(21): the complete final observable response is O(N^2).

No new integration, optimization of delta, or sharper estimate is
claimed in this comparison. The remaining rho_H time dependence is
not supplied by the W bounds. L193(18) and its ordered limsup argument
establish only the already recorded qualitative conclusion.

ATTEMPTS/043 preserves the failed complete-effective-residual absolute
norm count O(N^4); it is not an obstruction to a signed response test.
History/231 records the fixed-delta heat-transfer proof and explicitly
separates the unsmoothed final-time prefix group. The inherited
joint-probe assessment preserves L022's failed termwise curvature
transfer, the growing raw forest covariance, and the need for complete
nonlinear compensation. None is reopened by assuming a smooth rough
tilt, assigning independent laws to correlated prefixes, commuting A
with heat, or extending the forest through its upper pin.

## Primary comparison and bounded search

Reused [the joint-probe assessment](2026-10-14-joint-cubic-probe-jet-scale.md)
and [the prefix-sextic assessment](2026-10-23-prefix-sextic-quantitative-remainder.md)
for their already inspected sources. The following targeted primary
passages were reopened to compare the sharper quantitative requirement:

1. M. Luescher and P. Weisz, *Perturbative analysis of the gradient flow
   in non-abelian gauge theories*, JHEP 02 (2011) 051,
   [1101.0963v2](https://arxiv.org/pdf/1101.0963v2), 10 February 2011,
   sections 7.1--7.2, printed pp. 20--21, and 8.2, 8.4, pp. 24--25.
   Section 7 assumes ordinary four-dimensional renormalization.
   Its complete positive-time correlations require no further flow
   renormalization; section 8.4 describes the lattice extension as an
   expectation. SU(2) is included by rank two. This gives no uniform
   finite-relative-box estimate for the isolated bare cubic response,
   nor its time-integrated rate. The flow-time boundary is distinct
   from the physical faces of this notebook. The prior assessment's
   inspected BRS counterterm exclusion remains reusable; no reproof
   of that exclusion is needed for the proposed local estimate.
2. L. Del Debbio, A. Patella and A. Rago, *Space-time symmetries and the
   Yang--Mills gradient flow*, JHEP 11 (2013) 212,
   [1306.1173v1](https://arxiv.org/pdf/1306.1173v1), 5 June 2013,
   section 6, printed pp. 15--16, (6.11)--(6.16).
   The exact lattice response (6.11) and multiplicatively normalized
   continuum response (6.12)--(6.13) concern complete probes.
   Residual removal (6.15) uses restoration of translations with tuned
   stress coefficients. The generator also differs from the notebook's
   endpoint-averaged transported generator. Neither completeness nor
   matching hypotheses apply to the selected bare group separately;
   no stated N-dependent quantitative bound can be imported here.
3. A. Ramos and S. Sint, *Symanzik improvement of the gradient flow in
   lattice gauge theories*, [1508.05552v1](https://arxiv.org/pdf/1508.05552v1),
   23 August 2015, section 3.4, printed pp. 14--15, (3.43)--(3.45).
   Discarding total derivatives requires translation invariance and
   does not apply to the stated Dirichlet/Neumann boundary settings
   or higher correlations. Their full-observable improvement statement
   does not bound this relative-box selected response. No derivative,
   boundary row or insertion subtraction is removed on its authority.

The precise standard Gaussian input is Isserlis' theorem, whose
primary theorem and singular-covariance specialization were already
inspected in the prefix-sextic assessment: Munthe-Kaas, Verdier and
Vilmart, *A short proof of Isserlis' theorem*, author PDF dated
7 March 2025, Theorem 1 p. 1 and Theorem 4 p. 3,
[author PDF](https://www.unige.ch/~vilmart/paper_isserlis.pdf).
It is an algebraic pairing input, not an N-dependent estimate.
L193(11) already justifies the required heat-transfer specialization;
L183 supplies the finite Gaussian integration by parts. Reprove neither
general pairing nor flow renormalizability; only the missing actual
coefficient/kernel estimate and its applicability need research.

Queries on 2026-10-23:

- `Yang Mills gradient flow tree gauge cubic probe response finite volume quantitative lattice cutoff rate`
- `"gradient flow" "Ward identities" "boundaries" perturbative renormalization`
- `"gradient flow" "maximal tree" "bound"`
- `gradient flow cubic Gaussian heat kernel boundary perturbative finiteness lattice`

Results included numerical scale setting, fermionic chiral Ward
identities, general flow lectures and thermal correlation calculations;
none of the screened descriptions states the selected forest-response
rate. Their snippets are not theorem evidence. Newly surfaced theses
and a nonstandard preprint on torus heat-kernel oscillation bounds
were not inspected and are unread leads, not imported results or
essential sources: a torus kernel statement alone would still lack
the actual residual and forest contractions. No adequate stronger
matching theorem was established by this bounded search. This says
nothing about certified novelty. No essential source is blocked.

The [current Clay page](https://www.claymath.org/millennium/yang-mills-the-maths-gap/)
was rechecked on 2026-10-23 and still links the 14-page Jaffe--Witten
[*Quantum Yang--Mills Theory*](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf)
recorded in foundations/01 and the prior assessment. No target change
or new route selection is inferred.

## Approved continuation and outcome limits

This EXPLORE assessment approves exactly TARGET for a later research
turn. Start from L193(1), L183's exact response identity and the
already uniform W envelopes. Test a direct signed rho_H contraction
with its action circulation and actual exterior heat retained, or
quantify the heat-transfer bound uniformly down to cutoff-scale
physical times. A time split may be used only after proving a uniform
finite-mesh estimate for the constants involved. These are proposed
methods to test, not newly approved mathematical statements.

Continue if the full bound fits the stated threshold, or a partial
uniform estimate identifies a genuinely smaller remaining placement.
If the attempted estimate leaves a larger allowance, identify the
term and its achieved bound, without inferring signed growth. Stop
that particular mechanism if it requires an unquantified varying
cutoff, a false full-residual norm, deleted boundary derivatives or
termwise quotient transfer. A rigorous actual-probe obstruction would
also be informative; a coarse absolute upper bound is not one.

All essential IDs and unresolved assumptions above remain in the
continuation. The transverse-H rate, quantitative full assembly,
upstream pending audits, interacting reflected comparison and
continuum/infrared construction are independent gaps. There is no
candidate solution. Full matching Mathlib coverage and supporting
relative-cochain heat/flow theorems remain **not checked**; no absence
claim is made.

Completed step: EXPLORATION / LITERATURE / NOVELTY_UNCHECKED, actual
task literature_comparison. This is a new quantitative scope comparison
and research approval, with no new mathematical result, lemma, script,
proof audit or claim of progress beyond the checked sources. Mathematical
exploration usage stays zero of three. PROOF.md and DAG.md are unchanged
because no argument or dependency changed.
