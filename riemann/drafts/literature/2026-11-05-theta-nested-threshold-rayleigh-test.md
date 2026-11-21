# Actual-theta threshold encoding: proposed necessary-premise test

TARGET: Test the strongly-Rayleigh necessary condition for the actual-theta nested-threshold law S(U)={i in {1,2}: U>=a_i}, with 0<a_1<a_2<infinity, by determining the sign of its bivariate Rayleigh difference and the scope of any resulting obstruction to literal scalar discretization of L795.
CHECKED: 2026-11-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse step567's completed three-mechanism discovery, exact nested-threshold query and bounded local duplicate check in 2026-11-05-theta-signed-mechanism-bounded-discovery.md. This is a conventional application test, with no originality claim.
SOURCE_EVIDENCE: Branden math/0605678v4 Theorem5.6 and complete proof, Corollary5.5 proof and Example5.7, https://arxiv.org/html/math/0605678v4 ; Borcea--Branden--Liggett0707.2340v2 Definitions2.3/2.9-10, Section2.1(ii), Proposition3.1(2), Theorem4.1, https://arxiv.org/html/0707.2340v2 . Exact scope/read qualifications are in step567's assessment.
COMPARISON: The source criterion gives an exact necessary stability threshold for a nonzero bivariate probability generator. Actual theta cell probabilities, determinant orientation and consequences for the encoding remain to be checked; no root or matrix realization is assumed.
GAP: Only the finite-law premise is tested. A matrix realization matching P_d, coefficient identities, degree-uniform limits and signed/mixed transfer remain unresolved. One evaluation is not a general proof of stability.
REASON: One actual-law calculation can discriminate literal common-scalar encoding before investing in a stable-law realization. It differs from interlacing of Laguerre dilations and does not repeat failed source access or all-degree criterion algebra.
SCOPE: Newly written ready scope, requiring separate next-turn approval. One symbolic two-threshold calculation and its import limitation only; no degree sweep, fitted law, tail numerics or new stability theorem. REPRODUCTION, not creative work.

Main gap: actual-Xi all-degree mixed positivity. Intermediate target:
feasibility of this finite law for dependent stable averaging. Downstream
use: decide whether retaining the original shared scalar through nested
threshold discretization can meet a known necessary premise. This is
a route test, not a sufficient sign comparison for the theta polynomials.

Use exactly L019/L021/L795's probability law dmu(u)=K(u)du/m_0 on u>=0.
For U with this law and fixed finite 0<a_1<a_2, define B_i=1_{U>=a_i}
and the proposed generator

    g(z_1,z_2)=E[z_1^(B_1) z_2^(B_2)].

This is a definition for the later test; no identity for P_d is supplied.
Recover the four cell probabilities from it, verify normalization,
real multiaffinity and nonvanishing, and cite actual support facts for
strict mass claims. Retain the full law; do not replace U by independent
copies. Threshold zero, equality and infinity are excluded. No numerical
gap uniform in degenerate threshold limits is requested.

The imported test is Delta_12(g)=(partial_1 g)(partial_2 g)-g partial_12 g
>=0 at every real point when g is real stable. Branden Example5.7 supplies
the explicit bivariate coefficient criterion without reproof. Calculate
the actual difference with its correct determinant orientation and sign,
including strictness if justified. No such calculation has been made
in this source turn.

Continuation/abandonment test: a rigorous negative difference stops this
literal law as a strongly Rayleigh realization. Projection closure can
extend that obstruction only to larger finite laws whose two-coordinate
marginal is exactly this law; justify the matching. A nonnegative value
at one point alone cannot justify a matrix model. No outcome proves or
disproves P_d hyperbolicity or RH. Do not enlarge the threshold/degree
test merely to grow the result count.

The generic criterion is known; the work is its actual-law specialization.
Its test does not require homogeneity. Anari--Oveis Gharan's Section3
construction does: do not apply that construction directly to an arbitrary
nonhomogeneous generator. Passing the necessary test would leave any
homogenization, vector representation and coefficient matching unpaid.
No spectral root bound is proposed as an import.

Essential inputs: L019/L021/L795; L806 is contrast. No L791/L778 numerical
certificate, other notebook, missing source or RH-equivalent sign is
needed. Full matching Mathlib coverage is unchecked. A short source-cited
record suffices; do not create auxiliary lemmas or scripts for quotas.
Prior mathematical exploration counters remain intact.
