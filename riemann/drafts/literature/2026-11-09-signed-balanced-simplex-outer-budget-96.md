# Signed balanced-simplex outer budget — source comparison, step97

TARGET: Assess a cancellation-preserving effective balanced-simplex bound for L938's outer negative mass on E>=8 against exact L949 m-B, explicitly covering the finite-energy region outside L939's r>=2 estimates.
CHECKED: 2026-11-09
DECISION: EXPLORE
SEARCH_EVIDENCE: Step97 reused assessments50/51/52/85/94 and the L939/L940/L950 stops; searched signed-amplitude finite Laplace bounds, explicit-constant alternatives and exp-square-root supporting inequalities. No inspected source supplies the actual outer allowance or the proposed finite-phase inequality; queries and inspected/unread leads are distinguished below.
SOURCE_EVIDENCE: Read full L939 and relevant L938/L947/L949/L950 statements/proofs; reinspected Katsevich arXiv:2406.12706v3 Assumptions2.1-2.3, Remark2.5, Theorem2.12 and LemmaE.1; read Majerski arXiv:1511.00302v2 Theorems2.1/2.4, equations(3)-(7),(17), local/outer proof cases and the amplitude proof; read Boyd-Vandenberghe Sections3.1.3-3.1.4 and DLMF1.4.11,1.4.35-37. Precise citations and limitations below.
COMPARISON: Signed Laplace methods cover the proposed decomposition, not its finite numerical success. Katsevich retains separate local/Gaussian/actual-complement errors but uses unspecified L-dependent constants in the local bound; Majerski gives explicit constants and onset conditions but requires a verified finite phase gap, local convexity and amplitude control. None supplies these actual-theta data from E=8. A finite supporting-parabola discriminator is nominated before effectivizing the full budget.
GAP: Finite-energy localization for sqrt(2/3)<=r<2 is unproved; signed-amplitude derivative/error constants, a local ball inside the simplex, every boundary/full-theta complement and an effective infinite-energy join remain unpaid. No allowance below exact L949 m-B is established. The next proposed test isolates only the finite-phase obligation.
REASON: Completed one literature-only comparison yielding a concrete independently testable prerequisite for signed localization. New continuation97 has EXPLORE coverage and receives separate approval next turn; no finite bound, lemma, script, effective onset or RH result was derived.
LITERATURE_REASON: Changed essential hypotheses: retain the signed joint amplitude instead of positive row measures, and require effective finite-join bounds rather than L939's eventual asymptotic. Existing assessment94 covers neither requirement.

## Original nomination, before the completed step97 comparison

Main gap: L030-L032/C032a actual-Xi all-degree mixed positivity.
This intermediate target could pay only the outer part of the fixed
B_4 budget. It leaves head/global variation, parameter signs, contacts,
other degrees, initialization and realization open.

Essential local inputs for the next review are L019,L058,L938,L939,
L947,L949,L950 and the existing signed-saddle source comparisons50/51.
Review the exact L939 statement and relevant canonical proof ranges
before retrieving primary quantitative cases. L939 uses
r=sqrt(E/12); r>=2 starts at E=48, not8, and even48 is not an
asserted positivity onset. Do not fill this gap with an asymptotic
o(1), a sampled sign, an unsigned envelope or a persistent BKR blocker.
The full theta kernel, all34 rows, twelve factors, factorials and
M_0^12 normalization remain fixed. Cross-notebook input is unnecessary.

A useful review must identify an independently testable quantitative
localization/complement statement or document a specific obstruction;
repeating eventual positivity is STALLED. A later mathematical test
would need a complete upper outer-negative-mass allowance below exact
m-B (or pointwise positivity yielding zero outer allowance). An
oversized upper bound stops its selected method only. No exponent
optimization, split enlargement or repeated fixed Chernoff calculation
is nominated. Choosing a specific localization neighborhood or numerical
budget requires the separate coverage decision; none is silently fixed
or approved here.

This source preparation is not a protected creative mathematical
attempt. No source-assessed new central all-degree mechanism is yet
identified in the scoped records. The next review must compare the
known signed method and prior stops honestly rather than label an
effective specialization creative. Mathlib coverage is unchecked.


## Completed source comparison — 9 November 2026, step97

Outcome EXPLORATION: a new explicit-constant source comparison and a
bounded finite-localization discriminator, without a proved inequality
or numerical outer allowance. This is local research preparation, not
progress beyond the checked Laplace methods. PROOF and DAG do not change.

### Exact object and prior stops

Read L938 through its full-simplex representation and domination,
L939 in full including its independent audit, L947's endpoint margin,
L949's hypotheses/conclusion and normalization, and L950's signed-to-row
inequality and fixed-cost stop. Reused assessments50/51/52 for the
asymptotic method and85/94 for the negative-part budget; these remain
adequate in their unchanged scopes. No certificate was recomputed.

The original objective remains an upper bound on the actual quantity

    integral_8^infinity exp(E/10) max(-v(E),0) dE < m-B,

or an effective pointwise sign eliminating this cost, in exactly L938's
units. L949 bounds m-B between 8.935649629627021e-35 and
8.935649629627022e-35 under its stated contracts; the exact value,
not a displayed endpoint, is the eventual comparison target. A signed
integral alone cannot bound this negative part. Any pointwise lower
bound must hold for every energy before it is used for that purpose.

L939(13) supplies a global constrained quadratic lower bound for r>=2,
with r=sqrt(E/12), and its final sign has no effective onset. Its
r>=40 local-ball argument also cannot simply be invoked at E=8.
L950 stops the fixed rowwise method even with exact moments; no change
of exponent, compact split, precision or moment refinement is proposed.
L940's recorded global Schur-concavity failure concerns the signed
polynomial amplitude. It does not answer a coercivity question about
the exponential phase. This distinction supplies an independent test,
not permission to assume an amplitude sign or a balancing order.

### Primary source cases actually inspected

Anya Katsevich, *The Laplace asymptotic expansion in high dimensions*,
[arXiv:2406.12706v3](https://arxiv.org/pdf/2406.12706v3), 12 June 2025,
printed pp8-11 and38: Assumptions2.1-2.3, Remark2.5, definitions of
local derivative norms, Theorem2.12(2.15)-(2.18), and LemmaE.1's
actual-complement proof. Reuse the signed Taylor proof comparison in
assessment51 and L939's audited specialization. The theorem permits a
signed amplitude; it does not make that amplitude positive away from
the saddle. It assumes a unique minimizer and positive Hessian, C^2
g/C^4 phase for L=1 on the closed scaled ball, with R>=40, and outer
control. Remark2.5 substitutes another proved complement bound; it does
not provide one for a singular simplex. The local and Gaussian errors
use the notation less-than-up-to-C_L (defined on printed p8), so their
statements do not specify a numerical C_1. That is adequate for L939's
asymptotic use, but not a ready numerical allowance. A future numerical
use must import numerical constants or explicitly justify their extraction;
no universal C_1 is silently set to one here.

Piotr Majerski, *Simple error bounds for the multivariate Laplace
approximation under weak local assumptions*,
[arXiv:1511.00302v2](https://arxiv.org/pdf/1511.00302v2), 11 April 2016,
Theorem2.1, printed pp3-4; local ellipsoid and outer-gap proof, pp5-7;
Theorem2.4, its constants and equation(17), pp9-10, including its short
amplitude proof. Theorem2.1 assumes an integrable phase exponential,
a positive Hessian and third derivatives at the minimum, a local
Taylor-remainder inequality (A1), and (A2): convexity on a specified
ball and a strictly positive gap outside the smaller specified ball.
Its constants and admissible-parameter conditions N1,N2 are explicit.
Theorem2.4 adds a measurable amplitude nonzero at the saddle, a local
quadratic Taylor remainder, weighted absolute integrability (needed by
its displayed K_ul), and the further onset condition(17). Its proof
uses nonnegative local Taylor brackets. For the positive saddle value
in L939 this is a condition to verify, not a free global sign claim.
The printed proof's reference to the whole fixed ball is not used here
as a new theorem about that ball; the actual shrinking ellipsoid and
its containment must be checked in a future application. The source
allows an arbitrary measurable domain with a contained local ball,
so a simplex application need not use Katsevich's zero extension.
It still needs all actual boundary mass in its weighted absolute
integral and all phase-gap/onset hypotheses. No such constants or
onset are computed in this review. This is an accessible explicit-
constant alternative, not an automatic finite-join import.

Stephen Boyd and Lieven Vandenberghe, *Convex Optimization*, Cambridge
2004, corrected seventh printing2009,
[author book](https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf),
Sections3.1.3-3.1.4, printed pp69-71, equations(3.2)-(3.4) and their
one-dimensional supporting-line proof: differentiable convex functions
on an open convex domain lie above their tangent planes, with the
usual C^2 Hessian criterion. These facts do not assert full-domain
convexity for exp of a square root. No global Jensen argument is
imported without that hypothesis. The endpoint of a scalar square-root
change requires continuity rather than unproved differentiability there.
For possible elementary local error bounds, inspected the primary
[DLMF1.4.11](https://dlmf.nist.gov/1.4#E11) mean-value theorem and
[DLMF1.4.35-37](https://dlmf.nist.gov/1.4#E35) finite Taylor formulas:
continuity on the closed interval and differentiability in its interior
for the former; C^(n+1) on the closed interval for the latter. These
standard tools can be cited, without reproof, only on intervals where
their stated hypotheses have been checked.

Kirwin's fixed-data asymptotic comparison in assessment51 is reused;
Theorem2.1 was reinspected for its minimum and asymptotic-remainder
hypotheses. It provides no replacement numerical finite join. BKR
remains parked and is not needed. Kolokoltsov's 2020 explicit-error
paper was a new lead: publisher page returned429 and its PDF request
failed. Its theorem was not inspected or imported. No repeated access
loop is queued because the sources above suffice for the isolated test.
Lapinski2019 and Inglot-Majerski2014 were indexed leads only; the latter's
constant-amplitude restriction is described by Majerski's introduction,
not independently imported from the original theorem.

### Search record, decision and next discriminator

Queries included `Laplace signed amplitude explicit error bound simplex`,
`nonasymptotic Laplace Katsevich remainder constants`, `Riemann theta
Hankel convolution density sign`, the exact Majerski title, `exponential
of square root convex tangent inequality`, `exp(sqrt convex inequality`,
and the exact coefficient371319795000 with Laplace. Scoped local
searches covered only the relevant November9 L938/L939/tail assessments
and matching ATTEMPTS records. No inspected result proves the actual
finite phase inequality or the outer mass bound; search misses do not
establish novelty. Search snippets and unrelated RH frameworks are not
inputs. Full/supporting Mathlib coverage remains unchecked.

The next discriminator is the scalar supporting-parabola question in
continuation97. It targets the missing finite range8<=E<=48 only.
A uniform explicit positive constant would be a useful localization
input; it would not verify the signed amplitude, prove a tail sign,
pay m-B or settle RH. A certified violation stops this particular
scalar sufficient condition, not the constrained phase or all signed
localization methods. An unpaid uniform bound is saved and stopped
after one attempt; no parameter campaign is authorized. The full
outer budget still requires effective local and boundary errors and
an infinite-energy join, plus its original numerical qualifications.

No justified new central all-degree mechanism emerges from this
scoped review. This continuation develops an existing saddle route
and must not be labelled creative merely to fill scheduling cadence.
The source-gated new finite-phase subtarget is separate from both
the exhausted rowwise method and the failed amplitude-majorization
mechanism. Newly saved ready continuation97 receives separate approval
next turn before any mathematics. No new result is asserted here.
