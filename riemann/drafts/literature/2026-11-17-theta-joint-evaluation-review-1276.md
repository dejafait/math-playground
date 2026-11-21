# Joint complex evaluations — continuation nomination1276

TARGET: Attempt a simultaneous complex-evaluation nonmembership test for C032f(20), specializing the inspected RKHS criterion to both unweighted L2 half-line components and seeking an incompatible finite system or rigorously diverging minimum preimage norms.
CHECKED: 2026-11-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Review1275/completed1276 searched exact/unbounded Hardy ideal membership, Leech/corona and RKHS range/membership formulations; compared review1270/completed1271 and the specific pointwise stops1272/1273. No inspected result decides the fixed theta membership problem; no novelty claim.
SOURCE_EVIDENCE: Direct primary URLs verified in recovery1277: Hamilton2012 Proposition2.1.7/Remark2.1.8 pp15-16 https://dspacemainprd01.lib.uwaterloo.ca/server/api/core/bitstreams/5cb1b66f-d860-4f95-963e-898cda124537/content ; Manton--Amblard1408.0952v2 Sections2.5,5.1,6.1-6.2/Theorem6.2.1 https://arxiv.org/html/1408.0952v2 ; Seifert--Trostorff--Waurick2022 Theorem8.1.2/Corollary8.1.3 pp121-124 https://link.springer.com/content/pdf/10.1007/978-3-030-89397-2_8.pdf ; Gale et al2401.16091v1 Section1(1.1) and kernel display https://arxiv.org/html/2401.16091v1 . Prior full proof-case coverage is reused from review1275/completed1276; recovery reread the membership statement/converse/remark, range theorem/proof and finite interpolation discussion, and transform definition/isometry statement.
COMPARISON: Known RKHS results cover arbitrary families of individually bounded evaluations and one uniform finite-interpolation norm criterion, including complex conjugations and singular cases after explicit specialization. This differs from the exhausted scalar positive-real norm bound and does not require globally bounded theta coefficient multipliers. The actual theta obstruction is unpaid.
GAP: Construct the exact evaluation representers/Gram kernel in the original L2 pair, justify the RKHS range and common-zero cases, and test for finite incompatibility or divergent required norms. No incompatible system, divergence or actual Hardy pair is presently known; neither delta nor Xi positivity is decided.
REASON: A concrete known range criterion supplies a materially different analytic test of joint realizability. Permit one bounded mathematical attempt after separate continuation approval; do not resume the scalar test or assume a bounded normalization. The required source coverage is now present, although the specialization has not been performed.
SCOPE: Fixed C032f(19)-(20), omega=1/4,z=i,c=Xi(3i/4)/Xi(5i/4), F(z)=2Xi(2iz), a=1/8, alpha=1-c,beta=1+c; both complex unweighted half-line L2 profiles, no preimage-norm cap. Only the RKHS specialization and a controlled analytic obstruction test are covered; no zeta zero-free estimate, analytic coefficient normalization, source metric, universal range claim or signing theorem.
COVERED_TARGET: Attempt a simultaneous complex-evaluation nonmembership test for C032f(20), specializing the inspected RKHS criterion to both unweighted L2 half-line components and seeking an incompatible finite system or rigorously diverging minimum preimage norms.

## Direct-source repair1277

17 November2026. This is a source-link recovery, not new theorem coverage
or mathematical progress. All four direct endpoints above opened successfully;
the theorem-level comparison from completed1276 remains adequate for the
unchanged target. No new search for novelty or theta calculation was needed.

[Hamilton, pp15-16](https://dspacemainprd01.lib.uwaterloo.ca/server/api/core/bitstreams/5cb1b66f-d860-4f95-963e-898cda124537/content#page=23)
requires one constant for every finite subset. Its converse uses finite
Douglas factorization and weak compactness; Remark2.1.8 identifies the
infimum as the norm. Preserve the earlier warning about proof typography.
[Manton--Amblard, Theorem6.2.1 and Proof6.2.2](https://arxiv.org/html/1408.0952v2)
uses the closed span of the representing vectors; Section6.1 explicitly
allows infeasible interpolation systems. Its real formulation still needs
explicit complex conventions in the specialization.
[Seifert--Trostorff--Waurick, (8.1) and Corollary8.1.3](https://link.springer.com/content/pdf/10.1007/978-3-030-89397-2_8.pdf)
uses the normalized Laplace transform and an unscaled vertical integral.
The previously recorded factor1/(2pi) convention remains necessary for
C032f's unnormalized transform. No new specialization is asserted here.

The ready SPECIALIZE decision and exact TARGET are retained. The repair
removes the reported missing-URL defect; the supervisor decides next-turn
admission. All common-zero, singular-system and uniform-bound obligations
below remain unpaid. Mathlib coverage remains unchecked. Stops1272/1273
and bounded-corona stop1276 remain in force at their stated scopes.

## Essential sources and proof obligations

Use the complete citations, inspected hypotheses and qualifications in
`2026-11-17-theta-hardy-ideal-membership-review-1275.md`, completed1276.
In particular use the Hardy norm with factor1/(2pi) when identifying
it isometrically with C032f's unnormalized Laplace transform. The
constant cannot be lost when comparing Gram bounds with input norms.

The prospective construction is an evaluation range of the original
Hilbert input space L2((0,infinity),C^2). At every selected complex
point with positive real part, verify the evaluation functional and
its representing vector, including conjugations. Derive its Gram
kernel explicitly in a canonical proof. This is future specialization,
not a formula proved by the literature turn. The coefficients may
be unbounded over the half-plane; individual evaluations and their
representers must be bounded at each point. No assertion that the
coefficient-weighted sum maps into the original H2 space is needed
or authorized without proof.

Hamilton assumes nonzero evaluations. Do not discard a common zero
with a nonzero RHS, which would already be incompatible. If restricting
the index set to avoid zero evaluations, justify why the resulting
condition still tests the whole analytic equation. Handle singular
finite Gram matrices by compatibility on their nullspaces; ordinary
matrix inverses or strict positivity must not be assumed. His
membership converse requires a single uniform norm bound over all
finite sets, not individually finite fits. Read the statement and
Remark2.1.8 with norm bound C; the extracted PDF norm typography
must not be used to infer a different normalization.

The Manton--Amblard theorem's displayed real-space version requires
the complex conventions explicitly discussed in its Section2.5.
Use the inspected isometry/closed-span construction and the scalar
complex form of Hamilton, rather than asserting complex applicability
without specifying the convention. Standard Hilbert projection and
weak compactness may be cited. No reproof of Paley--Wiener, Douglas
or a general RKHS theorem is necessary; the theta-specific range,
analytic identity and finite-matrix realization justify the work.

## Discriminator and limits

The sought evidence is either exact incompatibility of a finite
simultaneous system or a rigorously controlled family whose minimum
preimage norms tend to infinity. No finite norm threshold is imposed
by C032f. A finite large norm, a small singular value, a numerical
complex zero, ill-conditioning or passing finitely many systems is
not a nonmembership certificate. If numerical screening is later
used, retain its full certificate and distinguish it from analytic
proof. An analytic family or exact obstruction is preferable to an
unbounded numerical search.

One bounded attempt is justified by the new joint-evaluation criterion.
If it yields only a reformulation and finite norm lower bounds with
no controlled divergence mechanism, record that limitation and park
this test; another run needs materially new input. The two earlier
branch explorations remain recorded and are not reset by this review.

Nonmembership could feed C032f(5)'s Douglas diagnostic, after that
reduction and the witness equivalence receive the necessary audit.
Membership for this single RHS would not establish universal range
inclusion or positive delta. Actual source metric, signing,
H_(d-1)>0, singular Schur blocks, initialization and all degrees
remain independent gaps. Inputs are C032f(12)-(25), C032e and
L016/L018/L019/L020 only at their stated scopes; no cross-notebook
input is used. Full Mathlib coverage is unchecked.

This is known-route development, not a new central positivity
mechanism. Recommend proof_attempt/development, deep_research/xhigh
for the analytic obstruction attempt. The missing independent signed
Xi bridge remains the blocker to a justified creative nomination.
This newly written continuation must receive the supervisor's separate
approval next turn before mathematical invocation; that approval does
not reject the completed source review.
