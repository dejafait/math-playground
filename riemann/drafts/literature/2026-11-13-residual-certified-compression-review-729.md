# Proposed residual certification after the constructor728 cost stop

TARGET: Assess primary coverage for a residual-certified positive exponential construction of C998u's G on [0,ell], using bounded-precision candidates and moment checks instead of certified root bisection, under B^2 uniform error<=1e-7 and total work<=10^8.
CHECKED: 2026-11-13
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Review730 searched positive/inexact quadrature, approximate moments, moment-residual bounds, Chebyshev approximation and Caratheodory--Tchakaloff subsampling; compared assessment726/comparison727 and stop729 with the primary results below. No complete affordable certificate for this G was located; no novelty inference follows.
SOURCE_EVIDENCE: Piazzon--Sommariva--Vianello DRNA10(2017),5-14,Theorem1.1,Proposition1.2(7)-(15)/full proof and algorithm pp5-8; Trefethen ATAP,Chapter8,Theorems8.1-8.2/proofs,ETH-hosted text PDF pp56-57; Lawson--Hanson SIAM1995 companion NNLS.FOR,contract/main/secondary/termination loops; Sommariva--Vianello DRNA14(2021),Sections3/4.1 for scope comparison only. Reuse726/727's Gaussian,moment and conditioning coverage.
COMPARISON: A published residual certificate covers positive discrete measures and inexact nonnegative quadrature on their original support, in a measure-orthonormal basis. It does not directly certify arbitrary floating Gaussian nodes or raw monomial residuals. The source algorithm enumerates the support; that implementation cannot be treated as affordable. A support-constrained finite-candidate NNLS test with certified original moments is covered as a specialization, with feasibility and cost explicitly unproved.
GAP: Specialize the cited residual and analytic-approximation bounds to C998v's blocks; certify the original-measure basis/residual, positivity,zero-inclusive uniform constants,finite candidate generation,all preparation/validation work and memory. No success at1e-7 or10^8 is claimed; no new general residual theorem is required for the support-constrained test.
REASON: New primary coverage changes the source gate for a bounded known-method specialization after729's implementation stop. No residual estimate,coefficients,rank,affordable ledger or new lemma is derived730. The newly ready continuation requires separate approval next turn.
LITERATURE_REASON: Changed construction/validation hypothesis: replace certified root-by-root refinement by a positive approximate rule with an explicit residual certificate. Exact Gaussian existence and the inspected ill-conditioning warning do not by themselves justify this change.
SCOPE: Same G(r)=sum_(j>=0)exp[-(2j+1/2)r]/(2j+1/2)^2, B=2^23, ell=log(3)/2; finite positive spectral blocks and a paid infinite tail. No density replacement, scalar evaluation, inverse, witness change or sign inference.
COVERED_TARGET: Test one support-constrained NNLS moment-residual compression of C998u's G on C998v's spectral blocks, including r=0, with B^2 uniform error<=1e-7 and complete preparation/validation work<=10^8.

The original nomination below is retained. Its pending-coverage language
describes729 and is superseded only within the completed730 scope below.

The main gap remains L030-L032/C032a actual-Xi positivity and signed S3.
The intermediate question is whether a directly validated inexact rule
can pay kernel preparation for a later full signed-measure scalar.
It is independently testable against a uniform error and complete work
threshold, rather than a request to repeat the728 bisection audit.

Use C998v's canonical block normalization and audited error/tail evidence,
C998u Section2's signed-measure transfer, and the unchanged C998t/C998s
contracts, C744z(1), C999l(1), C998r witness. Retain all334 shifts,
identity2187,512 modes, full K14 and exact P0 in any downstream scalar.
The witness SHA256 is
99ebc79ed3d82771ad0b5567356ba953e0d123d86aecdfe07d8e57f6fb9c634a;
it was not replayed729. The analytic-response, neutral-core,
IEEE754/Decimal and unreplayed c_* qualifications persist.

For the source review, first check the exact statements and proof cases
for approximate moment matching of a positive quadrature rule, including
bounded-support Laplace tests at zero. Possible terminology includes
positive quadrature residual bounds, inexact Gaussian quadrature and
modified Chebyshev moments. These are search leads, not imported results.
Compare against the already inspected exact Gaussian theorem before
larger source reads. Do not infer that a numerical residual is already
a rigorous uniform exponential error bound.

Continue to a separately approved mathematical attempt only if the
source supports an explicit residual-to-uniform-error certificate for
this measure class and a concrete finite candidate recipe. Count all
candidate generation, moment preparation, directed arithmetic,
validation, control and storage. The saved728 coefficients can be
reference evidence; their expensive production is not free preparation
for a purported cheaper construction. No new precision, order, rank,
iteration count or affordable work estimate is asserted here.

Abandon this nomination if the relevant theorem requires exact moments
or an unvalidated conditioning constant that defeats the intended
independent residual test, or if a justified minimum work count exceeds
the cap. A source blocker remains a source blocker, not an RH obstruction.
Preserve stops617/603/635/640/652/705/712/716/720/722/724/729 and the
100-digit failure. No repetition budget or supervisor state is changed.

Passing would pay only kernel preparation; density/mixed interactions,
h preparation, d0 C(0), the remaining9e-7 error allowance, other entries
and endpoints, C744q/H2, signed S3 and actual-Xi/global assembly remain.
There is still no justified new signed remote-plus-induced domination
mechanism to nominate as creative work. This is standard source
comparison, not a relabeled central sign argument. Mathlib coverage
for the proposed residual theorem has not been checked.

## Completed source comparison730 — 13 November2026

### Residual theorem: precise scope, including its proof cases

Federico Piazzon, Alvise Sommariva and Marco Vianello,
*Caratheodory-Tchakaloff Subsampling*, Dolomites Research Notes on
Approximation10(2017),5-14,
[published primary PDF](https://drna.padovauniversitypress.it/system/files/papers/PiazzonSommarivaVianello_2017_CTS.pdf),
Theorem1.1 p5, Proposition1.2/(7)-(15) pp6-7 and algorithm pp7-8.
For finite X, positive masses lambda, a finite-dimensional space S
containing1, a mu-orthonormal basis with evaluation matrix V, and
nonnegative u, set epsilon=||V^t u-b||_2, b=V^t lambda. With M=mu(X),
the proposition gives, for every f on X,

    |integral f dmu - sum_j w_j f(t_j)|
      <=2(M+epsilon sqrt(M)) E_S(f;X)
         +epsilon ||f||_(ell^2_lambda(X)).

Here T={t_j} is the nonzero support of u, hence T subset X.
The full proof uses the positive-weight triangle estimate(11),
Cauchy--Schwarz in the exact orthonormal basis(12), the function-norm
bound(13), and the constant-function mass estimate(14);(15) permits
approximation on a larger compact set. No exact moment matching is
assumed. The algorithm forms support-sized matrices and uses QR/NNLS;
it provides no applicable all-work bound here.

This is an importable general result, not a lemma established730.
Applying it requires preserving its support and basis hypotheses.
In particular, a small residual computed in monomials, in a basis
orthonormal only on the candidate grid, or from inexact input moments
without enclosing their errors does not meet the stated contract.
The new test must certify residuals against the original block measure.
Use C998v Section2's normalization, not a substituted smooth density.
Zeros outside a selected subset of X are permitted in u; no source
claim guarantees that any particular small subset achieves the tolerance.
The exact Gaussian nodes of C998v need not be original support nodes,
so its1171 saved terms do not receive this certificate automatically.

### Analytic approximation and a bounded candidate recipe

Lloyd N. Trefethen, *Approximation Theory and Approximation Practice*,
Chapter8, Theorems8.1-8.2/(8.1)-(8.3),
[primary book text hosted at ETH](https://people.math.ethz.ch/~hiptmair/Seminars/RAP_22/TRE13.pdf),
PDF pp56-57 (Chapter8 local pp3-4). This copy's exact revision date is
not independently established; the cited theorem text/proofs were read.
Analytic continuation from[-1,1] to the open Bernstein ellipse E_rho,
rho>1, with |f|<=M there, gives |a_0|<=M, |a_k|<=2M rho^(-k)
for k>=1, and degree-n Chebyshev projection error
<=2M rho^(-n)/(rho-1). The contour proof explicitly treats an open
ellipse by inner contours and a limit; the projection bound sums the
coefficient tail. These are approximation bounds, not inexact
quadrature or finite-precision construction guarantees.

Reuse Koyama's inspected ellipse/Laplace analysis and C998v's block
parametrization. The later specialization must check a uniform ellipse
bound for every r>=0, including r=0, choose its degree and constants,
then combine the cited results and the paid tail. The Gaussian
Theorem2.14 error cannot simply be assigned to an inexact NNLS rule.
No such combination or numerical threshold is derived in this review.

C.L. Lawson and R.J. Hanson, *Solving Least Squares Problems*, SIAM1995
reprint of1974, primary companion
[NNLS.FOR in the Netlib package](https://netlib.org/lawson-hanson/all).
Read the NNLS unit's contract and complete main/secondary/termination
loops (source lines764-1086), including rejection of nearly dependent
columns, feasibility corrections and triangular solves. It accepts
an m-by-n real matrix and minimizes a residual with nonnegative unknowns.
ITMAX=3*n bounds its secondary-iteration counter; MODE=3 signals
exceedance. This is not a total operation bound or a residual enclosure.
Machine output is candidate evidence only; interval validation remains
independent. Any precision adaptation needs its own paid implementation.

The proposed later recipe is the published moment-system/NNLS method
restricted to a finite, explicitly listed subset of original support
indices in each block. Fix candidate counts, polynomial degrees,
precision and iteration/operation limits before running it. Generate
indices directly, without enumerating the original large block; use
the already covered finite-moment and positive-Gram methods to prepare
the original measure's basis and right side. A deterministic grid
followed by Lawson--Hanson NNLS supplies a finite candidate attempt;
its positivity, residual accuracy and conditioning must all be checked.
The selected grid is not assumed to be a Tchakaloff set. A failure to
achieve the residual is an allowed outcome for this fixed prescription.
No grid size,degree,precision,rank or affordable count is selected730.

For small blocks, retaining exact original atoms is permitted, but their
rank,storage and generation must be charged. For compressed blocks,
ensure degree<support cardinality before using a polynomial Gram basis.
Moments needed for products may have higher degree than728's saved35;
the general cited power-sum/remainder methods cover preparation, not
an assumption that the saved moment list is sufficient or free.
If certified basis conversion defeats conditioning or work, stop that
prescription. Never call a full QR,NNLS,orthogonalization or moment
routine one operation, or use its reported residual as a rigorous bound.

### Overlap, limitations and continuation decision

Alvise Sommariva and Marco Vianello, *Computing Tchakaloff-like cubature
rules on spline curvilinear polygons*, DRNA14(2021),1-11,
[published primary PDF](https://www.maths.tcd.ie/EMIS/journals/DRNA/pdf/sommarivavianello_2021_ctc.pdf),
Sections3/4.1, Theorems3.1-3.2 and the near-exact error discussion,
pp4-7, were read as a stronger-scope comparison. Its planar algorithm
uses candidate grids and moments; the existence discussion gives an
eventual sufficiently dense set, without an explicit sufficient grid
index for our blocks. Its near-exact error discussion refers back to
the2017 estimates. No planar Lebesgue result, unstated extension to our
discrete measure, empirical residual or timing is imported. The ETH
EMIS URL first returned404; the Trinity journal mirror supplied the
primary text. This resolved access, not a mathematical hypothesis.

Searches included `positive quadrature approximate moments residual
error bound`, `Sommariva Vianello approximate moments quadrature
residual error bound`, `quadrature moment residual Chebyshev`, and
`Trefethen Theorem8.2 analytic functions Chebyshev projection`.
Glaubitz's positive/exact cubature and other search hits remain unread
leads, not inputs. No result for the full G with the required effective
error/work constants was established by this bounded search.
Narrow local comparison used assessment726/comparison727, the related
frequency-compression assessment720's unread-lead note, C998v and
stop729. This reuses ready moment/Gaussian coverage while adding the
previously missing inexact-quadrature comparison.

DECISION SPECIALIZE covers only the listed support-constrained test.
Its fixed-instance normalization,error constants,basis certification
and complete work/memory ledger remain mathematical work for a later,
separately approved turn. No general theorem is to be reproved.
Full matching Mathlib coverage has not been checked; this does not mean
absence. No lemma or mathematical script is written730.

Continue only if the fixed prescription certifies nonnegative output
weights,original-support nodes,the uniform error<=1e-7 after B^2 transfer,
and all preparation/validation work<=10^8, with explicit storage.
An iteration cap,failed interval check,unpaid essential hypothesis or
above-cap ledger stops that prescription; it is not an impossibility
result for all residual methods. Preserve729's exact approximation and
cost stop and the100-digit failure. Passing pays preparation only under
the shared total cap;the remaining9e-7 and all scalar/sign/global gaps
listed in the nomination remain. There is still no justified signed
remote-plus-induced S3 domination mechanism to label creative.
