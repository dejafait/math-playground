# Collision-flow discriminator — source assessment948

TARGET: Assess whether a collision-divided holomorphic gradient flow supplies a finite, nonautomatic Jacobian-phase obstruction test near a single pair collision for the arbitrary-order Bromwich Vandermonde form.
CHECKED: 2026-11-14
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step948 searched holomorphic gradient flow/logarithmic zeros/blow-up, Vandermonde collisions, residual Jacobian phase and double-zero integrability; inspected TNV2017 Sections2.1–3.2 and AppendixB through its flat-metric case, plus LY2021 SectionsIV.A–IV.B through(21). Compared local reviews925/946 and C466k/l with stop947; no exact actual-h uniform collision theorem was located, with no novelty inference.
SOURCE_EVIDENCE: Tanizaki–Nishimura–Verbaarschot, JHEP10(2017)100, arXiv1706.03822v2, (2.2),(2.4),(2.12), Section2.2 (2.13)–(2.21) and footnotes1–2 pp5–6, Sections3.1–3.2 pp7–9, AppendixB (B.1)–(B.5) p22; Lawrence–Yamauchi, PRD103(2021)114509, SectionsIV.A–IV.B (10)–(21), pp4–6. Direct primary links and inspected qualifications are below; reuse review925's deformation coverage rather than reapproving noncompact homology.
COMPARISON: Known action-phase conservation is automatic; residual phase still contains the signed Jacobian. Sources allow nonsmooth contours at zeros and qualify negligible collision contributions by weight-times-Jacobian control. Smooth collision-divided extension is therefore not a justified necessary screen. Modified-flow completeness under polynomial hypotheses does not cover the nominated raw actual-h flow.
GAP: No nonautomatic necessary phase-regularity condition or actual-h collision-uniform Jacobian theorem is supplied. The finite-time full weighted mass, stopped-branch interpretation, analytic remainder, global homology and all-order/Xi transfer remain unpaid. Only a separately assessed frozen-model source audit is nominated; no actual-h calculation is approved here.
REASON: Park the smooth phase-extension screen and action-phase-only screen; retain the precise target as reviewed rather than claim a general impossibility theorem. Specialize only the source's local logarithmic model and Jacobian law in a later approved audit of weighted integrability; this is reproduction, not creative sign discovery.
LITERATURE_REASON: The target changes from a free local holomorphic coordinate germ to prescribed holomorphic gradient dynamics near a logarithmic Vandermonde singularity; essential existence, residual-phase and collision-asymptotic source coverage was missing at invocation start.

## Source checkpoint — step948, completed below

Primary sources retrieved: Tanizaki–Nishimura–Verbaarschot,
arXiv:1706.03822v2, Section 2.2 including both footnotes, Sections
3.1–3.2 and Appendix B; Lawrence–Yamauchi, PRD103 (2021) 114509,
Section IV.A and the beginning of IV.B. The former explicitly warns
that vanishing weight must be compared with the Jacobian and treats
finite-time logarithmic collisions; the latter allows nonsmooth
collision contours. These are source statements, not an actual-h
collision theorem. No mathematical calculation has been performed.
The completed assessment distinguishes raw from modified flow, action
phase from effective phase, and fixed physical time from
separation-dependent time. No smooth collision-extension necessity
has been established.

## Original proposed scope and discriminator — preserved nomination

The main gap remains actual-Xi all-degree algebraic-square positivity,
L030-L032/C032a. The possible downstream use is an order-dependent
global signed-contour construction, whose phase must include the full
Jacobian. Local phase rectification by an arbitrary map cannot screen
that mechanism, as C466k scope947 now shows.

For source comparison consider the n-variable signed Bromwich form
with algebraic Vandermonde squared and factors A_x(z)=exp(xz)/h(z),
at x=B'(1), under C466a/k's actual-function qualifications. On a
collision-free zero-free local branch its prospective action is
S_n(z)=sum_j(log h(z_j)-xz_j)-2 log Delta(z). The proposed dynamics
to assess is dot z_j=conjugate(partial_j S_n); the sign is specified
to remove ambiguities in the term gradient flow. This is a definition
for literature comparison, not a claimed existence theorem or estimate.

Seek primary statements about this flow, logarithmic singularities,
residual Jacobian phase and failure of completeness. The bounded
prospective discriminator is a single generic pair collision, with
the remaining coordinates in a fixed compact set separated from each
other, the colliding center and zeros of h. Determine from inspected
results whether there is a meaningful finite-time or infinitesimal
phase-regularity test after accounting for the full collision factor.
Specify the time/separation scaling before approving a calculation.
No assumption of uniformity in n is licensed by this fixed-n screen.

Continue only if the assessment identifies a nonautomatic necessary
condition and an exact bounded computation or theorem application.
Park this flow if the proposed condition merely restates a known
phase identity or integral positivity, or if no relevant global use
can be justified. An essential source block requires a different,
independently testable target. Do not fit more arbitrary contour jets.
No extra discovery budget is claimed by changing mechanisms.

Local inputs for formulation are C466a/k/l; C466o/stop941 and scope947
are failure comparisons, and C466p is only a known finite-sign contrast.
Do not load broader proofs unless an exact needed claim is named.
Global homology, endpoints, convergence, orientation, all orders,
density-to-Xi transfer and full matching Mathlib coverage remain open.
There is no ready creative proof attempt: the required collision-flow
source comparison and nonautomatic discriminator are the blocker.

## Inspected primary statements and proof cases

TNV denotes Yuya Tanizaki, Hiromichi Nishimura and Jacobus J. M.
Verbaarschot, [*Gradient flows without blow-up for Lefschetz thimbles*,
JHEP10(2017)100](https://doi.org/10.1007/JHEP10(2017)100), inspected in
[arXiv:1706.03822v2, 27 September 2017](https://arxiv.org/html/1706.03822v2),
with equation/page locators checked in the
[v2 PDF](https://arxiv.org/pdf/1706.03822v2). PDF equation numbering is
used here; the HTML renumbers equations consecutively.

TNV (2.2),(2.4) fix the upward conjugated-gradient convention and
conserve Im S on nonsingular trajectories. Appendix B derives the
real-parameter variation equation, including metric derivatives, and
then gives the flat-metric law (B.5):
\[
 \dot J=\overline{S''(z)J}.
\]
It is not \(\overline{S''}J\). Section 2.2 treats quartic escape and
a logarithmic zero separately: (2.19) uses
\(S=x^2-\log(1-x^2)\); (2.20)–(2.21) give the leading normal
collision and its finite hitting time. Footnote 1 warns that vanishing
weight alone does not control a divergent Jacobian. Footnote 2 states
a bounded-product justification for that shrinking deleted region;
this is not an arbitrary-dimensional uniform-integrability theorem.
Section 3 instead changes the vector field. Its polynomial
\(S_B,D\) assumptions and decelerating metric are essential to its
no-blow-up discussion. No completeness result for the raw flow or
for \(\log h\) at infinity is imported.

LY denotes Scott Lawrence and Yukari Yamauchi,
[*Normalizing flows and the real-time sign problem*,
Phys.Rev.D103(2021)114509](https://doi.org/10.1103/PhysRevD.103.114509),
inspected in the [published primary PDF](https://scoap3-prod-backend.s3.cern.ch/media/files/62831/10.1103/PhysRevD.103.114509.pdf).
Section IV.A (10)–(18) includes the Jacobian contribution to the
quenched integral and an initial-time improvement calculation.
The end of IV.A permits continuous nonsmooth contours at zeros;
IV.B retains residual and between-piece phases. Its (19)–(21)
iterates the effective action including log det J, rather than proving
raw-flow perfection. The first-order illustration is expressly not
the prescribed treatment of zeros. We do not import its existence
discussion as a uniform collision or global Bromwich theorem.

## Applicability, overlap and decision

The local action in the preserved nomination agrees with TNV's raw
flow convention on each zero-free, collision-free branch. The
antiholomorphic vector field is smooth there, not a holomorphic
coordinate map of the kind in C466k scope947. Its real-parameter
Jacobian is the object in Appendix B. The full signed pullback must
retain that Jacobian and the algebraic Vandermonde square. Neither
phase constancy along trajectories nor positivity of an absolute
square is a new necessary sign estimate. This is a comparison of
formulations, not a solution or an existence/parameter-uniformity
proof for the local dynamics.

The source examples prevent adopting smooth extension of a divided
coefficient as a necessary condition merely because the original
holomorphic form vanishes on collision. The total weighted pullback
is the quantity needing control. They do not prove that every
candidate phase condition is automatic or that no raw-flow contour
can work. In particular, failure of a parameterization at collision
does not itself refute deformation or determinant positivity.

Duplicate/failure checks used the targeted reviews925/946, C466k's
scalar/pair stop and scope947, C466l(5) and its signed Jacobian
convention, and stop947. Stops927/932/941 retain their original
scope; no arbitrary contour jet, marginal sign or known D3 test is
reopened. Searches also used the exact phrases `holomorphic gradient
flow double zero Jacobian`, `holomorphic gradient flow Vandermonde
collision integrability`, and `logarithmic singularities Lefschetz
Jacobian flow`. No matching actual-h theorem was found in the
inspected sources. Unread search leads include the broader
Rev.Mod.Phys.94(2022)015006 review and one-site fermionic-model
papers; none is a mathematical input. This is not a claim of novelty
or comprehensive absence.

The independently testable continuation is the full weighted mass of
one frozen double-zero normal model, with an exact time convention.
It checks whether a proposed collision objection survives the measure
factor; it does not search for another positive phase jet. Its
assessment is
[review948](2026-11-14-double-zero-weighted-flow-audit-948.md).
No actual-h perturbation estimate, global contour, determinant sign
or Xi transfer follows from a successful normal-model audit.
Full matching Mathlib coverage was not checked; these are cited
analytic source inputs, not formalized results.
