# Local-L2 coefficient remainder: source-review working record

Literature-only step, 31 October 2026. Target is the exact TARGET in
`literature/2026-10-31-actual-xi-local-l2-signed-remainder.md`.
No new coefficient expansion or Xi estimate is being derived.

The main gap is all-degree actual-Xi positivity, especially low indices
at unbounded heights. The intermediate target is a source-supported
local-L2 remainder smaller than an explicit nonzero signed coefficient
term for fixed 0<d<=3/8, fixed full multiplicity m>=1, unbounded gamma.
Such a result could address signs below L463's tail. Other indices,
heights and effective overlap would remain independent gaps.

Continuation test: primary sources must control the actual signed
remainder, its contour pairing, height uniformity and complementary
arcs, without assuming simplicity, separation or a zero-free deflated
quotient. A positive aggregate norm alone fails this test.

Local comparison completed: read L018, L463's coefficient definition
and hypotheses, L474 Sections 1--6, L570's exact-model setup and
cancellation, and the relevant passages of the prior amplitude review.
L474 uses finite Blaschke factors, then a continuous shifted second
moment and area submean bound. Its displacement scope is d_j log T<=
epsilon<=1 and its output is a nonnegative dyadic aggregate, not an
individual fixed-displacement contour remainder. Section 6 already
records its application audit; do not schedule that audit again merely
because PROOF.md still calls it unaudited. L570's failure is a known
erratum and is not new evidence this turn.

Initial searches: `"saddle point" "L2" "remainder" error bound`,
`"zeta" "zeros" "quotient" "mean square"`,
`"steepest descent" "L^2" "amplitude" error bounds`,
`"saddle-point" "remainder" "Lp"`,
`"stationary phase" "remainder" "Sobolev" asymptotic`,
`"Bettin" "second moment" "unbounded shifts" theorem`,
`"zeta" "mean square" "divided" "zero" quotient`.
Most hits were unrelated variational saddle-point problems or
uninspected leads. No absence/novelty conclusion follows. Next primary
inspection was Bettin Theorem 1 and its small-shift proof case, together
with a norm-dependent saddle remainder result. The existing O'Sullivan
primary reading was reused for fixed-data scope.

## Primary results inspected

Sandro Bettin, *The second moment of the Riemann zeta function with
unbounded shifts*, IJNT 6 (2010), 1933--1944,
[arXiv:1111.0925v1, 3 November 2011](https://arxiv.org/pdf/1111.0925v1),
Theorem 1, p.2: T>=2, complex a(T),b(T), real parts O(1/log T),
c=a-b. It estimates the integral over [0,T] of
zeta(1/2+a+it) zeta(1/2-b-it) by the integral of
zeta(1+c)+zeta(1-c)chi(1/2+a+it)chi(1/2-b-it), with error
O((sqrt(T)+sqrt(|Im a|)+sqrt(|Im b|))log^2 T). At c=0 the
combined integrand has its pointwise limiting meaning. Read p.2's
bounded-real-shift remark, the opening contour proof p.7 and the
small-imaginary-c completion pp.9--10, including W1/W2 and the
integration by parts. The real microscopic shifts of L474 lie in this
theorem; fixed nonzero real shifts do not. Its suggestion about extending
the method supplies no such theorem. No arithmetic proof audit or
microscopic-interval subtraction estimate is claimed here. The arXiv
metadata uses the alternate title *The second shifted moment of the
Riemann zeta function*; the PDF title and theorem identify the input.

Thomas Bennett, Christopher J. Howls, Gergo Nemes and Adri B. Olde
Daalhuis, *Globally exact asymptotics for integrals with arbitrary order
saddles*, SIAM J. Math. Anal. 50 (2018), 2144--2177,
[arXiv:1710.10073v2, 8 February 2018](https://arxiv.org/html/1710.10073v2).
Read Section 2 hypotheses, Section 3 (9)--(22), Section 5 (51)--(53).
Required: analytic f,g on the closed descent domain; |f| tending to
infinity; paths ending at infinity; a nonempty finite adjacent-saddle
set; prescribed branches/orientations; initially one saddle per adjacent
contour, with the stated limiting qualification; sector (7), convergence
of (1), decay g/f^((N+1)/omega_n)=o(1/|t|), and integrability (22).
The proof deforms the enclosing contour, excludes denominator zeros in
the swept region, and uses absolute convergence before interchanging.
Bound (53) retains weighted amplitude integrals on adjacent contours
and angular factors. It is not a local contour-L2 theorem, does not
require nonvanishing g, and provides no Xi-specific signed term.
No L2 conversion or Xi contour deformation is derived here.

O'Sullivan v2 Assumptions 1.1/(1.7)/Corollary 5.1 and Section 4:
reuse the complete primary inspection in the parent amplitude assessment.
Fixed phase/domain/contour, absolute supremum-dependent errors, possible
amplitude zeros and opposite-sector cancellations remain exactly as
recorded there and in L570. No repeated source audit is claimed.

## Search limits, overlap and decision

Additional queries: `"saddle-point" "remainder" "Lp"`,
`"steepest descents" "error bounds" Nemes 2017 remainder contour`,
`"Laplace" "remainder" "L2" asymptotic integral`,
`"stationary phase" "L2 norm" remainder amplitude`,
`"zeta" "local second moment" "short intervals" fixed sigma`,
`"Globally Exact Asymptotics" arxiv`,
`"stationary phase" "L2" "remainder" -saddle -optimization -schrodinger`,
`"zeta" "divided differences" "mean square"`, and
`"xi" "deflated" "L2"`. The global exact-remainder result was
followed to its primary hypotheses and relevant proof cases. An attempted
Zworski book URL returned 404; that lead is unread and not essential.
Search hits on stationary phase in PDEs, special-function remainders and
general zeta ratios are leads only, not inspected matching theorems.

The new comparison supplies no actual-Xi signed term, local remainder
estimate or relative error. L474's positive aggregate cannot replace
that missing signed quantity. The current application is parked on
mathematical input gaps, not an inaccessible essential source.

For choosing an independent continuation, checked only the named
L486 statement, its all-mesoscopic stop and its ready assessment;
L475's existing audit headings; and the relevant ready audit records.
These prevent nominating already completed application audits, or
repeating the count-only band sum/global Blaschke envelope as a new
mechanism. Their proofs were not re-audited. Narrow searches for Hardy
space, model space, inner/outer, reproducing-kernel and extremal-Blaschke
terminology in drafts/literature and ATTEMPTS did not identify an exact
disk-norm/negative-D1 interpolation criterion. Most named matches concern
Hardy's real Z function, moment duals, operator model spaces or theta
kernels; this is only a preliminary overlap screen. The next nomination
still requires a full exact-target literature comparison, not a novelty
claim or mathematical approval.
