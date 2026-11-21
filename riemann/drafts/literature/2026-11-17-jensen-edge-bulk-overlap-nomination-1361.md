# Jensen edge-to-bulk count interface: source-review nomination1361

TARGET: Assess an Airy-to-bulk overlap mechanism for reducing the actual Jensen exceptional-root deficit by extracting Ono v1's exact bulk cutoff and sign-grid index range, comparing them with C019g's fixed edge intervals, and identifying one independently testable missing-root estimate.
CHECKED: 2026-11-17
DECISION: IMPORT
SEARCH_EVIDENCE: Review1362 searched the exact identifier with edge/saddle remainder, unshifted Jensen Airy/bulk and nonstationary terminology; inspected Ono v1 directly and narrowly compared assessments1344/1354/1358/1359, C019d-f/g and stops1345/1355/559. Search hits did not supply another matching theorem; no novelty inference.
SOURCE_EVIDENCE: Ken Ono, An Asymptotic Jensen–Pólya Criterion for GRH, arXiv:2610.38870v1, 28 October2026, https://arxiv.org/html/2610.38870v1 : Theorem1, Lemma7/(3.3)-(3.11), Corollary10/(3.17)-(3.20) with endpoint proof, Lemma11/(3.21)-(3.24) and proof, Lemmas12-14 with relevant amplitude/IBP proof cases, Proposition15/(5.2)-(5.5) and full assembly, (5.6), Corollary16 and full conjugation proof, Lemma17/(6.1)-(6.2), complete Section6 count and Remark18 inspected. Section2 identities reused from review1358.
COMPARISON: Source bulk starts at q_e+M*sqrt(log(d)/d), equivalently x_bulk=M*d^(1/6)*sqrt(log(d)) in C019g's coordinate. Its counted intervals are separated from the fixed x in [1,4] eventually, but those two locations supply only a bounded addition and no growing-window control. Source (6.3) separately retains near-edge and far-end losses; the latter has the larger recorded order.
GAP: No inspected result gives a vanishing relative full-contour remainder on the proposed omitted band d^(-1/2)<=q-q_e<=2*d^(-1/2). Compact Airy convergence cannot be used there. Its oscillatory complement estimate, phase-barrier growth, any added root count, dominant far-end loss and every-degree closure remain unproved.
REASON: Essential cutoff/index extraction is complete. Import the source statements without reproof; reject compact-window Airy overlap as a solution to the growing deficit and nominate a different, independently testable complement estimate. No new estimate or root-count addition is proved or approved in this literature turn.
SCOPE: Literature-only source extraction and coordinate/scope comparison for K=Q, unchanged actual polynomial, degree-dependent q_e, B=T^2 and reciprocal map. The new estimate is only nominated in assessment1362 and needs separate approval. No lemma or mathematical script was written.
LITERATURE_REASON: The target changes from the approved compact-window application to the quantitative bulk/edge count interface; the exact cutoff and index-loss evidence is essential unread coverage for this comparison. Reuse fixed-window assessments rather than repeat their analytic audits.

## Preserved nomination1361: purpose and bounded decision

The main gap remains actual-Xi all-degree positivity and, on this route,
every-degree Jensen hyperbolicity. Audit1361 retains C019g but does not
change the source's unbounded exceptional-root deficit. The proposed
intermediate target is to locate the missing count precisely enough to
specify one test of a mechanism that could supply additional roots.
This is a source-review target, not a newly derived root estimate.

Start with the primary bulk theorem's hypotheses and the exact sign-grid
and endpoint cases in its proof. Extract the q cutoff, grid phase/index
range, strict endpoint conventions and where count losses enter. Compare
their definitions with C019g's exact q_e(d)+x*d^(-2/3) window and reciprocal
map. Do not replace q_e(d) by its limit when comparing a shrinking window.
Separate what the source actually counts from locations it does not
exclude. Read only further primary passages needed to resolve those
specific interfaces. Reuse the already inspected source identities and
fixed-window Airy assessment; no source-wide audit is requested.

Continue only if this comparison identifies a growing missed family with
independently specified barriers and a concrete uniform error/margin test
that would certify distinct roots outside the already counted intervals.
Nominate that exact test with its essential input IDs and fresh coverage;
do not perform it in the literature turn. If the fixed intervals are
already counted, or a compact-window limit cannot control the relevant
count loss, record that precise limitation and choose a materially
different central mechanism. Merely adding two roots to the bulk lower
bound or renaming the automatic-Airy import fails the test. An informative
overlap obstruction is useful even if no new estimate is ready.

Essential local inputs are L018/L021 and C019c-C019g. The source bulk
count and its exact index/cutoff evidence need precise citations in the
completed comparison. No source-wide validity, effective onset, root
simplicity, other-edge closure or Mathlib theorem is assumed. Fixed-window
C0 convergence alone supplies neither growing-window control nor an
integer root count on an unbounded collection of intervals.

Preserve stops1345 and1355: the first rejects an automatic generic-Airy
import and the second rejects opposite signs at the two outer fixed
endpoints. Neither is a global ban on a separately justified matching
mechanism. The November5 bulk-screen failure concerns a different,
provisional scaling and supplies no prohibition here; its source-scope
evidence remains preserved. No cross-notebook input is proposed.

Creative discovery remains due. No justified creative proof target is
ready: there is no signed estimate on a growing omitted region or proved
bulk disjointness. This source comparison is preparation toward that
central obstruction, not a creative attempt or a completed assessment.
Mathlib coverage remains unchecked. This newly written continuation must
receive separate review; it does not alter the completed mathematical
audit's outcome.

## Completed source comparison1362 — 17 November 2026

This section supersedes the nomination's unread-source qualifications.
It records source statements and their scope, not a new contour lemma.
The inspected primary is [Ono v1](https://arxiv.org/html/2610.38870v1),
whose HTML identifies the version as 28 October 2026. Theorem1 treats
K=Q, d>=2 with an absolute constant; the analytic proof works beyond
an enlarged fixed onset. Theorem3 permits constants depending on a
fixed field. Only K=Q is used here. Formal artifacts, source-wide
correctness and a full matching Mathlib theorem were not audited.

### Exact cutoffs and barriers from the primary proof

In (5.6), after fixing epsilon_0 and c_g from Corollary10, choose
M>0 with c_g M^2>N+4, and c_0>0 small enough for Lemma13 and
c_g N/(4 pi c_0)>N+4. The definitions are exactly

    tau=M sqrt(log(d)/d), Q=c_0 T, I_d=[q_e(d)+tau,Q].

Here N=1 locally. Neither endpoint is an effective numerical constant.
Proposition15 uses ell_q=epsilon_0 min(alpha,cos(alpha)),
theta_q=-2 alpha, D_q=u_q^2 h_q''(u_q),
n_q=d |D_q| ell_q^2 and

    Z_d(q)=(d!/d^d) a_q(theta_q) exp(d h_q(u_q))
              / sqrt(2 pi d D_q),

with principal square root and nonzero Z_d. Its range is
q_e<q<=c_0 T and n_q>=1. Its local Gaussian error is O(n_q^(-1/10));
its complementary-circle error is

    O_K(d^(N+1) exp(-c_g d min((q-q_e)^2,q^(-1)))).

The proof explicitly uses an absolute-value bound on the complementary
semicircle, after the local application of Lemma14. Near the edge its
recorded effective parameter is n_q asymp d(q-q_e)^(3/2). At Q it is
asymp d/Q asymp log d. The two exponential inequalities after (5.6)
make that complementary error O(d^(-3)) on I_d. Corollary16 then
supplies A_d(-q)=2 Re Z_d(q)+O(|Z_d(q)|(log d)^(-1/10)) uniformly
on I_d. Its proof uses exact conjugation, not a second independent
approximation on the upper semicircle.

Lemma17 provides a continuous phase vartheta_d=d S+omega_d on I_d,
with |omega_d|<=C. Equation (6.2) specifies its branches using the
Euler-product logarithm, the holomorphic logarithm of g_K and principal
Arg D_q. The correction includes -mu_K alpha and -Arg D_q/2; it must
not be suppressed when choosing grid points. Section6 first makes the
cosine-normalized error <1/2. It then considers the consecutive integer
multiples k*pi between the two endpoint phase values. The source does
not supply explicit numerical k_min,k_max or a monotonicity theorem
for vartheta_d. It supplies at least Delta_d/pi-1 such values, chooses
successive hitting points in increasing q using continuity, and counts
at least Delta_d/pi-2 intervening open intervals. Thus the endpoint
rounding/hitting losses are bounded. Roots lie strictly between
successive sign samples, even if an extremal sample is at a cutoff.

Lemma11's S(q_e)=0, S'>0 and endpoint estimates give, in Section6,

    Delta_d >= pi*d-C*d*(Q^(-1/2)+tau^(3/2))-C.

Equation (6.3) retains the same two losses in the distinct-root lower
bound. The source then records separately

    d Q^(-1/2)=O(sqrt(d log d)),
    d tau^(3/2)=O(d^(1/4)(log d)^(3/4)).

These are losses in a lower-bound argument, not exact counts of
exceptional/nonreal roots. One must not identify either loss with a
known collection of nonreal zeros. Remark18 gives the exact reciprocal
image [-T^2/(d(q_e+tau)),-T^2/(dQ)]. The source states no absence of
other real zeros outside it.

### Scope comparison and decision

C019g retains x in [1,4] in q=q_e(d)+x*d^(-2/3). Expressing the
source cutoff in that same coordinate gives
x_bulk(d)=M*d^(1/6)*sqrt(log d), tending to infinity. This is a direct
coordinate comparison, retaining q_e(d), not a new root theorem.
The two fixed windows are therefore on the omitted side of the bulk
cutoff for large d; the earlier uncertainty about possible overlap can
be replaced by this explicit cutoff comparison. A later count application
would still need its common onset, exact map and finite counting checks.
No such addition is performed here. Even adding both locations could
only change a bounded term and would not control either growing loss.
The larger recorded loss is at Q, so edge progress alone cannot improve
the overall order O(sqrt(d log d)) without independent far-end work.

The compact Airy estimate in C019f/g has no quantified growing-x error.
It cannot be extended to x_bulk or an intervening band by substituting
a degree-dependent x into its fixed-window limit. Stop1345 likewise
preserves the missing full-contour hypothesis for automatic CFU import;
stop1355's fixed-endpoint sign failure is unchanged. The November5
stop559 concerns different provisional scaling and does not prohibit
the source's exact saddle geometry. None is a global route ban.

A different bounded mechanism is worth nominating: on the band
d^(-1/2)<=q-q_e<=2*d^(-1/2), test cancellation on the complement of
the two separated Gaussian neighborhoods instead of using its absolute
modulus. The proposed lower-semicircle target and all its definitions
are in `2026-11-17-jensen-moving-saddle-complement-1362.md`.
This is outside I_d eventually. The displayed Proposition15 exterior
bound is not a vanishing relative bound there; this does not prove the
actual remainder large. Its local Gaussian proof and exact geometry
remain usable inputs after checking their hypotheses. C019d's single
annulus does not contain the inner endpoint-to-saddle gap in this regime.
No bound for that gap, no phase-growth estimate and no new root count
is derived in this review.

Prospective barriers are the exact consecutive phase levels k*pi from
the source expression (6.2), restricted to the proposed band. A future
application must establish the phase expression's validity there, an
unbounded number of attained levels, a uniform normalized error <1/2,
and separation from the old bulk intervals. These are obligations,
not consequences of compact convergence. The new target tests only the
load-bearing complementary integral. Failure of its uniform derivative,
boundary or amplitude control must be recorded, not hidden in an
unnamed o(1). Success could supply a growing omitted family later;
far-end and all-degree gaps would remain.

Searches were `"2610.38870" "edge"`, `"unshifted Jensen" "Airy"
roots bulk`, `"Jensen" "Ono" "2026" "cutoff"`, `"Jensen"
"2610.38870" saddle remainder`, and `"unshifted" "Jensen"
"nonstationary"`. Aggregator hits and unrelated results supplied no
theorem evidence; only the named primary was used. Reused earlier
CFU/Olde Daalhuis-Temme, shifted-Hermite and compact-convergence
assessments rather than repeat their source reads. Narrow searches of
the named Jensen assessments/stops found no completed complement test
on this exact band. Neither search failure nor this comparison proves
novelty. An initial scoped git-status output was excessive; its
truncated listing was not mathematical or preservation evidence.

Outcome: informative source-scope NEGATIVE for compact Airy overlap as
a growing-count mechanism; new exact cutoff/loss evidence determines
the next independent test. Completed kind LITERATURE, classification
KNOWN_IMPORTED, task literature_comparison. No canonical lemma, DAG,
PROOF or mathematical script changed. The new continuation is an
established cancellation-method development, not certified originality
or a justified creative global mechanism, and requires separate approval.
