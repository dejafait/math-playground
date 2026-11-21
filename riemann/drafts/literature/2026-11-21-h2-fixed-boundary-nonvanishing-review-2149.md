# Fixed boundary control before a low-time finite-head certificate

TARGET: Review source coverage for a fixed proof that F(lambda,100+iy) is nonzero throughout 0<=lambda<=1/20 and |y|<=1/2, as a boundary-control prerequisite for using C919a.
CHECKED: 2026-11-21
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step2150 completed exact-boundary/method searches and compared primary Polymath effective approximation/nonvanishing, Johansson integration and enclosing-arithmetic contracts; reused the 9November finite-head assessment and preserved step206/2146 stops. Queries and inspected cases follow; no novelty or absence claim.
SOURCE_EVIDENCE: Polymath1904.12438v2 (5)-(25), Theorem1.3/Corollary1.4, Section6.3 (69)-(74), Proposition6.6(iv)-(vi) and relevant proof; Johansson1802.07942v1 Sections2/2.1; Arb2.23 acb_calc/using contracts; DLMF4.2.5/4.6.1/4.14.3/4.19.1-2; Python3.15.2 Decimal contracts. Reuse L019/L058/L919/C919a; exact links and limits below.
COMPARISON: Published normalized finite sums and explicit errors offer a whole-box boundary test without integrating the oscillatory improper integral. L036/L037 do not certify complex boxes. The source states t>0; zero-time continuity, constant cutoff, branch checks and a strict box margin remain required specializations.
GAP: No inspected source supplies this surface certificate or its lower bound. Fixed finite-sum implementation and endpoint applicability remain work; initial census, head reality/continuation and eigenvalue margin are independent gaps.
REASON: A specific existing theorem replaces the unassessed complex-integration prerequisite with a bounded normalized finite-sum test. Import it and specialize its explicit criterion; stop on a failed fixed budget without reproving heat asymptotics or inferring head positivity.
LITERATURE_REASON: Essential coverage was missing for this changed complex two-parameter target; Theorem1.3/Corollary1.4 had not been compared for it. This is not further browsing for a ready calculation.
SCOPE: Completed literature-only review of exact TARGET. No boundary estimate, new lemma or mathematical script. The newly nominated fixed calculation requires the supervisor's separate next-turn approval.

## Original nomination (preserved; step2150 completion follows)

The main gap remains L030-L032/C032a actual-Xi all-degree algebraic
mixed positivity. A later fixed-boundary certificate could support
control of a finite region under the heat deformation. Even then,
initial real-zero census, all relevant continuation hypotheses and a
uniform head minimum eigenvalue above1/2000000000 would remain unpaid.
No implication from boundary nonvanishing alone to H2 positivity is
being proposed. C919a's accepted tail cost is a prerequisite, not
evidence that these further conditions hold.

The future observable is exactly the vertical segment z=100+iy,
|y|<=1/2, with lambda in the unchanged closed band. Review methods
for obtaining a strict certified lower bound on |F| there, with a
complete theta/integration remainder and rigorous coverage between
sample points. Sampled nonzero values alone cannot certify it. This
nomination makes no claim about that lower bound or numerical scale.
The next review should specify one fixed feasible certificate budget
and its pass/fail test before authorizing implementation. If essential
coverage or a justified fixed test is unavailable, park this target;
do not launch a precision/mesh/radius sweep or retry a blocked source.

Essential local inputs are L019,L058,L919,C919a. L036/L037 are only
prospective enclosing-arithmetic support and must be checked for the
changed complex two-parameter scope before use. Read only relevant
ranges. No RH, all-real-zero, simplicity, boundary separation,
continuous zero enumeration, cross-notebook theorem or uncertified
arithmetic premise may be silently imported. Full matching Mathlib
coverage is unchecked.

The prior comparison is in
`2026-11-09-low-time-h2-finite-zero-domination-review.md`; the old
endpoint stop is `../../ATTEMPTS/2026-11-09-h2-endpoint-rayleigh-inconclusive-206.md`.
Those stops remain intact. A smaller accepted tail cost does not
repair their lost correlations or authorize their rerun. This review
targets boundary control instead. No specific new theta-signed
mechanism was identified by the bounded C919a audit; this established-
method prerequisite is not labeled creative to fill a routing quota.

## Step2150 completed comparison

Main gap: actual-Xi all-degree algebraic mixed positivity in
L030-L032/C032a. The intermediate observable remains exactly the
specified vertical segment throughout the closed time band. Its
plausible use is finite-region boundary control, followed by a
separately justified census/continuation and head margin above C919a's
1/2000000000 tolerance. Success here would not complete those tasks.
In particular, a vertical segment is not the radial boundary of
L919's head: transferring a rectangular census to |zeta|<=100 would
need separate accounting. No such transfer is authorized or asserted.

### Primary theorem and relevant cases inspected

D. H. J. Polymath, *Effective approximation of heat flow evolution of
the Riemann xi function, and a new upper bound for the de Bruijn-Newman
constant*, Research in the Mathematical Sciences 6 (2019), article31,
[arXiv:1904.12438v2, 4 August2019](https://arxiv.org/html/1904.12438v2#S1).
Read (5)-(25), Theorem1.3/Corollary1.4; Section6.3's (69)-(74),
Proposition6.6(iv)-(vi) and the error proof through its conclusion.
The source region is 0<t<=1/2, 0<=Y<=1, x>=200. Its normalized
criterion compares |f_t| with explicit complete errors; (14)-(19)
define the finite sum and cutoff, (23)-(24) bound the errors.

Reuse L919's established F(lambda,z)=8H_(4lambda)(2z).
The requested positive-Y boundary therefore falls in the source
coordinates x=200, t in [0,1/5], Y in [0,1]. L058's conjugation is
the available lower-Y input. The theorem itself requires t>0.
Research must supply the limiting argument at zero, cutoff constancy
and nonvanishing normalizer; none is newly proved here. The branches
are those of (6)-(11), not arbitrary complex logarithms. We avoid
(21): its printed correction differs from Proposition6.6(ii).
The selected calculation evaluates s_* directly and uses (23)-(24),
so neither competing lower bound is an input. No Section8 large-x
numerical constants are imported at x=200.

This source already absorbs the infinite theta/integration remainder;
it is unnecessary to produce a new theta quadrature theorem for this
test. No numerical instance of its criterion is asserted here.

### Numerical-method coverage and qualifications

F. Johansson, *Numerical integration in arbitrary-precision ball
arithmetic*, [arXiv:1802.07942v1](https://arxiv.org/html/1802.07942v1),
22 February2018, Sections2/2.1, including the direct-box fallback,
analytic ellipse check, evaluation-limit and tiny-integral cases.
Reuse the adequately assessed method in the step2065 four-coefficient
review; inspect the newly relevant tiny-integral qualification.
Finite path quadrature encloses the integrand only under a correct
callback; requested tolerances do not certify the final error.
Improper tails remain the caller's duty. These methods are available
coverage, not a paid boundary certificate or a proof of a practical
parameter mesh. The selected normalized method needs no quadrature.

The archived primary [Arb2.23 acb_calc documentation](https://arblib.org/acb_calc.html),
Types/macros/constants and Integration, and
[Using ball arithmetic](https://arblib.org/using.html), ball semantics,
Binary and decimal, Quality of enclosures and Predicates, were read.
They require setwise inclusion, input uncertainty and safe output
rounding; failure to exclude zero is inconclusive. Revised
FLINT3.7.0-dev integration documentation was consulted and identifies
an October2026 partially generated rewrite. It is not the sole basis
for these contracts. Neither python-flint nor the narrowly checked
Homebrew FLINT/Arb libraries was present, so the selected test assumes
no certified installed complex library or package installation.

Reuse L037's real directed arithmetic and rational Machin pi procedure.
The [Python3.15.2 Decimal documentation](https://docs.python.org/3.15/library/decimal.html),
exp/ln, next_minus/next_plus, contexts, signals and power qualification,
was inspected. Exp/ln are correctly rounded half-even; widening and
directed elementary arithmetic support enclosures. General noninteger
power is not assumed correctly rounded: use exp times ln. Square-root
endpoints must additionally pass exact squared-bound checks. Existing
real enclosures are not already a complex implementation.

NIST DLMF, live edition checked 21 November2026:
[4.2.5](https://dlmf.nist.gov/4.2.E5) fixes the principal logarithm,
[4.6.1](https://dlmf.nist.gov/4.6.E1) supplies its local series for
|w|<1, and [4.14.3](https://dlmf.nist.gov/4.14.E3),
[4.19.1-2](https://dlmf.nist.gov/4.19) supply complex exponentials
via real trigonometric series. Research must document branch-safe
scaling, series-tail bounds and outward operations on whole input
rectangles. This is routine implementation of cited identities,
not a new theorem about F. DLMF4.23's opening definitions were also
consulted but are not an input to the selected logarithm-series plan.

### One fixed test, awaiting separate approval

The exact nominated calculation is in
`2026-11-21-h2-fixed-boundary-polymath-certificate-2150.md`.
Its immutable budget is 32 source-time intervals
[j/160,(j+1)/160], j=0,...,31, and 64 source-height intervals
[k/64,(k+1)/64], k=0,...,63: 2048 closed rectangles, including all
edges. Use x=200, 100 significant Decimal digits, L037's 96-term
Machin enclosures, and at most128 retained nonzero terms per elementary
logarithm/sine/cosine series. Verify any scaling and argument reduction
with outward intervals; each series needs its complete tail bound.
No precision, grid, formula or cutoff sweep is covered.

The first required guard is to certify from (19) that the cutoff is
N=3 on the entire band; otherwise stop rather than alter the sum.
This guard and branch/domain checks are part of the future calculation,
not results of this review. Implement only (14)-(19), (23)-(24) and
the nonzero normalizer in (6)-(11), using the actual enclosed gamma,
kappa and s_* instead of the optional bounds (20)-(22). All printed
source decimals are exact rationals for enclosure purposes.

On each rectangle obtain a lower bound l for |f_t| and an upper bound
e for the right sides of (23)+(24). A strictly positive certified
minimum of l-e over every rectangle is the pass test. Include all
arithmetic/series errors in these bounds. To conclude at t=0, write
out the uniform-margin limiting argument using L058 and the source
expressions; merely applying the t>0 statement at zero is forbidden.
Conjugation must explicitly cover negative local y. Save every box,
its rational endpoints, cutoff/branch guards, l, e, margin and all
failures in a full on-disk certificate; print only summary and paths.
Any failed guard, undecided rectangle or nonpositive sufficient margin
parks this fixed test as inconclusive; it is not a zero of F or a
counterexample to RH. No ABC correction fallback is preapproved.

This is a feasible bounded *test budget*, not a proved successful
certificate: after the cutoff guard, each box uses two three-term
sums and elementary enclosing operations, with no improper quadrature.
No claim about runtime or the size/sign of its minimum is made.
If it passes, a later independent audit is needed before using the
new certificate as an accepted boundary input. The fixed target
leaves the initial census, complete boundary of any chosen region,
real-head continuation and eigenvalue margin unresolved.

### Searches, reuse, failures and decision

Queries actually submitted included `Johansson numerical integration
arbitrary precision ball arithmetic 2018 acb_calc_integrate holomorphic
parameters`, `Polymath effective approximation heat flow Riemann xi
function rigorous numerics interval arithmetic 200 boundary`,
`"H_t" "200" "non-vanishing" Polymath barrier`, and
`"H_t" "200" "t=0" Riemann Siegel Polymath`.
Search hits outside the primary sources above are unread leads; no
claimed new RH proof or external numerical package was imported.
The shell's direct arXiv extraction attempt failed DNS resolution;
the connected search tool supplied the complete relevant statements
and proof ranges, so this is not an essential persistent source block.
No repeated shell-access attempt was made.

Read only the active notebook's named definitions and relevant ranges,
plus the specific prior numerical-source assessments cited above.
L917/L922 moment-box and step206 Rayleigh stops remain intact; the
step2146 expansion-only source limit remains intact. Normalized
boundary nonvanishing tests a different observable, not a refinement
of those contractions. No all-notebook scan or cross-notebook theorem
was used. Full matching Mathlib coverage remains unchecked; supporting
arithmetic or holomorphy declarations would not certify this surface.

Decision: SPECIALIZE a published finite-sum criterion with the fixed
budget above. This is local source coverage progress only, not a new
bound or a verified boundary result. No specific new theta-signed
mechanism emerged within this review; a justified creative target is
not ready. Preserve that discovery need while finishing this bounded
prerequisite, and do not relabel known-method implementation creative.
