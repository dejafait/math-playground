# Full-degree d=2 row-resolved density dual — proposed finite test

TARGET: Test the fixed degree-13 row-resolved density-dual residual for full-degree d=2 actual-theta contacts on 0<lambda<=1/20, seeking one uniform coefficient tuple in [-16,16]^60 that makes the complete half-line residual nonpositive, or a rigorously scoped obstruction to this fixed class.
CHECKED: 2026-11-09
DECISION: EXPLORE
SEARCH_EVIDENCE: Step198 selected this class after comparing three mechanisms; reuse 2026-11-09-d2-contact-flux-discovery.md for exact/stronger searches, duplicates/failures and inspected versus unread leads. No matching residual theorem was inspected; novelty and feasibility remain unestablished.
SOURCE_EVIDENCE: Ley-Swan ECP18(2013), paper7, Definition2.1/Theorem2.2 pp2-3, https://www.maths.tcd.ie/EMIS/journals/EJP-ECP/article/download/2578/2199.pdf ; Fantuzzi et al. arXiv:1512.05599v2 Section4(4.2)-(4.10), Proposition3 pp8-9, https://arxiv.org/pdf/1512.05599v2 . Step198 inspected operator endpoint hypotheses/proof directions and auxiliary-bound boundary/reversed-sign cases, reusing step176. No theta-sign or polynomial-SOS theorem is imported.
COMPARISON: Zero-mean density correction is known. This class seeks signed actual-theta control with separate corrections from all null rows before absolute estimation. The old d=1 pilot was empty; global-convex/two-cell and moment-box stops concern different sufficient tests. No specialization or source-exceeding result is established here.
GAP: Verify rowwise zero means and the density-operator interface, including boundaries/integrability, then certify the complete residual sign or a genuine scoped obstruction. No coefficients, contact, inequality or implementation exists for this target.
REASON: Three separate null rows offer signed information lost in step193's absolute bound. A full residual certificate could control L874's unpaid S7 without another determinant enclosure. Failure assesses this fixed sufficient class, not the flux in general. Separate next-turn approval is required.
SCOPE: Exactly the class and first-attempt stop below; actual L019/L058/L874 family, c2!=0, normalized c, H2 PSD and all H2*c=0 rows, full theta score and whole half-line. No class/box enlargement, parameter sweep or moment-box rerun is covered.

## Purpose and premises

The main gap is L030-L032/C032a actual-Xi all-degree mixed positivity.
This conditional d=2 boundary input could help decreasing heat-time
continuation. Essential inputs are L019/L058/L874. L915/L916/L917 and
step178/193 are method comparisons; unfinished step193 identities must
be checked rather than imported as canonical results. No cross-notebook
input. Contact existence, initialization, tangency, lambda=0, other
degrees and global continuation remain open. Existing real-zero/no-contact
coverage addresses lambda=1/20 as recorded in the completed comparison;
the lower-time interior remains unresolved, with no known contact.

Use L874's exact normalized density rho_lambda, T_n(u), R(u), S_n and
H2, and retain at every stipulated contact

    c real, c0^2+c1^2+c2^2=1, c2!=0,
    H2 positive semidefinite, all three equations H2*c=0,
    0<lambda<=1/20.

c0/c1 may vanish. Do not divide by a coordinate or minor. Nonzero c2
is an explicit full-degree restriction, not a lower-degree exclusion
proved here. R has degree twelve by L874. Verify the intended flux
orientation Phi=E[u^2 R]<=0 from its canonical statement.

## Proposed residual — no inequality derived here

Define finite row polynomials

    V_i(u)=sum_(j=0)^2 c_j*T_(i+j+2)(u),  i=0,1,2.

First verify their means and dilation means using L874's individual
T_n identities and every null row. No such specialization is derived
or approved as proved in this literature turn.

Choose once seven real symmetric 3x3 matrices A_0,...,A_6 and arbitrary
real 3x3 matrices B,C. Each independent entry lies in [-16,16]. These
7*6+9+9=60 constants are independent of u, lambda, c, moments and Phi.
Use the ordinary quadratic form convention, including twice each
off-diagonal term in c^T A_k c. Propose

    P_c(u)=sum_(k=0)^6 (c^T A_k c)*u^(2k+1),
    W(u)=u^2*R(u)+P_c'(u)
         +(2lambda*u+K'(u)/K(u))*P_c(u)
         +sum_(i,j=0)^2 c_i*(B_ij*V_j(u)+C_ij*u*V_j'(u)).

The test asks for one tuple making W<=0 for all u>=0 at every stated
actual contact. The degree, coefficient box and constant dependence
are pilot restrictions, not optimal or theoretically sufficient ranges.
All actual lower coefficients remain in T_n; no surrogate moment law.
Do not choose constants from unknown Phi or assume an unrestricted
Stein-equation solution belongs to this finite class.

The proposed correction is Ley-Swan's T_rho P=(P*rho)'/rho. Check its
zero-mean applicability with L874's full polynomial-weighted K/K'
boundary and integrability estimates, citing the general rule rather
than reproving it. The new obligation is the residual sign, not that
known identity. Fantuzzi et al. is a template only; no theta diffusion
or polynomial drift is assumed. Exact K'/K is transcendental: an SDP
or sampled sign cannot certify the full residual. Full/supporting
Mathlib coverage is unchecked, not asserted absent.

## Discriminating test and stop

One attempt may check analytic endpoint/tail compatibility and exploit
all null rows to seek a full signed certificate in this fixed class.
Certify u=0, the complete compact head and the entire full-series tail;
report actual versus required bounds and failures. Higher-degree PSD
or the desired flux may not be premises. Verify the expectation
interface as well as W's pointwise sign.

If only the zero means or an unpaid decisive residual estimate emerge,
save the reasoning and stop this class after the first attempt. Do
not enlarge degree/box, move the band, split new cells or launch a sweep.
A rigorous obstruction must state its scope: a failed noncontact or
relaxed certificate does not refute the actual contact-only statement.
A negative flux needs a certified actual contact. An empty contact
domain is emptiness evidence, not a successful dual mechanism.

Creative purpose is the separate-row signed correction at the external-S7
bottleneck. Interface reproduction alone is REPRODUCTION; a new estimate
or informative obstruction may be POTENTIALLY_NEW within this assessed
scope, without a certified-originality claim. No calculation or lemma
occurred in step198. Separate supervisor approval precedes research.
