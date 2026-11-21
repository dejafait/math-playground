# Fixed gamma/geometric model: proposed bounded diagnostic

TARGET: Test the fixed density p=g_(3/2,1)*g_1, where Lg_1(s)=product_(n>=1)(1+s/2^n)^(-1), for the stated smooth scalar-Volterra first-D3-crossing conditions.
CHECKED: 2026-11-14
DECISION: EXPLORE
SEARCH_EVIDENCE: Assessment891 completion892 records the exact self-decomposable/Wronskian/gamma-finite-PF searches, scoped duplicate/failure screen and primary proof cases. No inspected theorem settles the joint first-contact conditions. Separate approval completed in recovery893; no new search or originality claim.
SOURCE_EVIDENCE: Direct primary URLs https://arxiv.org/pdf/2008.05121v2 (Khare Theorems1.2/1.7/A, Corollary3.2, pp3-4/11-12) and https://arxiv.org/pdf/1710.11023v3 (Kwasnicki Sections6.1-6.2, pp20-21) accessed 2026-11-14 in recovery893; reuse Steutel--van Harn V.2.11/V.2.16 equation(2.23) via assessment883. Version/access qualifications and direct book URL below.
COMPARISON: The gamma base has a cited finite-PF-order distinction but fails flat smoothness; the one-sided infinite-exponential component supplies a sourced smoothing construction. Neither source states the convolved model's strict D2, boundary D3 sign or simple first D3 crossing. The scalar theorem must be applied with this model's verified canonical kernel.
GAP: Verify admissibility and all joint determinant/contact conditions for this fixed candidate. Arbitrary translation minors, weak log-concavity, local numerical signs and approximate-identity convergence do not establish the required strict confluent signs or first/simple contact.
REASON: One law-level test can distinguish the full scalar premises from C466c's free jet. It is a generic diagnostic, not an actual-Xi construction or a reproof of Sra v3 low-order positivity. No novelty claim follows from this search.
SCOPE: Exactly the fixed shape3/2, rate1 gamma convolved with g_1; no parameter/order sweep, replacement family or actual-H inference. Standard source inputs may be applied after verifying hypotheses; no source theorem needs wholesale reproof.

## Proposed test, not an established example

Write g_(3/2,1)(x)=x^(1/2)exp(-x)/Gamma(3/2) for x>0,
zero otherwise. Use the source's g_1 with the transform in TARGET.
The proposed canonical kernel for verification is

    H(t)=(3/2)exp(-t)+sum_(n>=1)exp(-2^n t).

The required conclusion is: p is a probability density in C^infinity(R),
zero on (-infinity,0], positive on (0,infinity), and the verified H
belongs to C1(0,infinity), is strictly positive and decreasing,
is integrable, and satisfies xp=H*p. For

    D_j(p;x)=(-1)^(j(j-1)/2)det[p^(r+s)(x)]_(0<=r,s<j),

seek x_*>0 and eta>0 with D1,D2>0 on (0,x_*+eta),
D3>0 on (0,x_*), D3(x_*)=0 and D3'(x_*)<0.
None of the model-specific assertions is proved by this assessment.

The source toolkit covers why this is a meaningful family to test;
it does not guarantee that the family meets the requested signs.
Proving strict D2 needs more than citing weak PF2 or strict Jensen
concavity: the pointwise curvature must be strictly negative.
Non-PF3 need not give a negative confluent D3. Any use of smoothing
limits must justify the needed derivative convergence for this base,
whose derivatives are singular at zero. Fixed m=1 does not follow
from a source's unspecified sufficiently large smoothing parameter.

An analytic or certified calculation must cover the full prefix,
including the endpoint neighborhood, exclude earlier D3 zeros and
prove the derivative at the first contact is negative. A plot or a
single negative sample is only a diagnostic. If the attempt cannot
complete these obligations, preserve the partial reasoning and name
the missing bound; do not announce a countermodel. A proved lower-sign
failure before the proposed crossing or a proved incompatible contact
geometry stops this fixed candidate. Repetition requires a materially
new input, informative obstruction or refined test, not a parameter sweep.

C466a distinguishes boundary from global signs, C466b supplies the
motivation for testing the full scalar premises, and C466c only
excludes a finite-jet real-root inference. L018/L024 normalize actual
Xi but supply no premise to this generic example. Even success leaves
actual-V signs/locations/masses, strict forcing, simultaneous contacts,
barriers, compact propagation and L030-L032/C032a transfer open.

Reuse the source notes in
[assessment891 completion892](2026-11-14-scalar-volterra-third-contact-model-891.md)
and the named preservation/bell-shape/finite-root stops there. No
essential source remains unread for this bounded exploratory test;
this does not assert exhaustive literature coverage or originality.
Mathlib matching for the joint model/contact statement is unchecked.
Any later canonical result must state its actual proof or precise
imports and all qualifications. This literature turn writes no lemma.

This is established-route model development, not a creative central-gap
mechanism. The desired actual-H creative route remains blocked by the
absence of an independently justified signed-weight control; this
generic candidate does not pretend to supply it. Suggested mathematical
routing after separate approval is proof_attempt/development,
deep_research/xhigh, because endpoint estimates and exclusion of earlier
contacts are analytic proof obligations, rather than free-jet arithmetic.


## Separate source approval: recovery893 (2026-11-14)

LITERATURE_REASON: Supervisor recovery requires a direct source URL in the ready assessment; verify access and precise scope without changing the saved target.

The [Khare author URL](https://math.iisc.ac.in/~khare/papers/TN-crit.pdf)
failed retrieval today. The accessible [arXiv v2](https://arxiv.org/pdf/2008.05121v2)
is dated April 2021 and has 31 pages. Inspected Theorems1.2/1.7/A,
Corollary3.2 and the relevant proof on pp11-12: positive diagonal
factors transfer negative translation minors; the homotopy argument
uses nonsingularity. These are finite-order translation statements,
not the fixed convolved density's confluent first-contact theorem.
The original author-version locators remain historical evidence;
this approval uses the explicitly versioned alternative.

Reopened [Kwasnicki v3](https://arxiv.org/pdf/1710.11023v3),
dated 27 November 2018, Sections6.1-6.2 pp20-21. Read the complete
one-sided smoothing paragraph and the decreasing-kernel example.
The geometric exponential convolution is smooth and scales with m;
preservation of that source example's excess second-derivative sign
changes requires sufficiently large m. This supplies no fixed-m=1
D3 crossing guarantee for the fractional gamma base. The source's
self-decomposable counterexample concerns bell shape, a different
conclusion from the joint determinant/contact target.

Reuse the previously inspected Steutel--van Harn (2004) Chapter V
Theorems2.11/2.16, equation(2.23), including assessment883's
singular-kernel qualification; [direct book text](https://www.nzdr.ru/data/media/biblio/kolxoz/M/MV/Steutel%20F.%2C%20van%20Harn%20K.%20Infinite%20divisibility%20of%20probability%20distributions%20on%20real%20line%20%28Dekker%2C%202004%29%28ISBN%200824707249%29%28546s%29_MV_.pdf).
This book was not retrieved again in recovery893. Its scope remains
the scalar equation for a nondegenerate positive self-decomposable
law with left endpoint zero and its verified canonical kernel, not
any determinant sign.

Approval: retain EXPLORE for exactly TARGET and the existing SCOPE.
Coverage is adequate for attempting the bounded diagnostic, not for
asserting a witness. No new model property was derived or checked.
Reuse assessment891's duplicate/failure screen; no evidence here
undermines it. Mathlib coverage of the joint statement remains unchecked.
