# Independent compensated prime-cutoff Cauchy-tail source assessment

TARGET: Assess whether an unconditional PNT remainder yields an explicit n-dependent cutoff X_n with |P_n(Y)-P_n(X_n)|<=1 for every Y>=X_n and n>=2, with full prime-power jumps.
CHECKED: 2026-11-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step225 searched Johnston-Yang theorem/correction/version terms, DLMF Laguerre formulas, Abel summation endpoints, compensated Laguerre Cauchy estimates and Li prime truncation bounds; reused review223's fixed-moment/retraction comparison and the October baseline. Narrow local searches found no ready matching cutoff theorem; related unread leads are explicitly distinguished below. No novelty inference.
SOURCE_EVIDENCE: Read Johnston-Yang arXiv2204.01980v2 (20 April2022), Theorem1.1/(1.3), Table1 first row, Sections1.4,3.1-3.2 pp3-4,7-9; DLMF18.5.12 and18.9.23 with source notes; Tristan Shin, Math104B Discussion3 (23 January2025), pp1-2, Abel formula and real-endpoint proof (Apostol Theorem4.2). Reused review223/L977/L980 conventions and October register; links and access limits below.
COMPARISON: The inspected unconditional all-real-x psi bound, global finite Laguerre identities and finite Abel formula cover the tools for a nonoptimal uniform Cauchy-tail specialization. No inspected statement directly supplies this n-dependent cutoff. Stronger zero-free baseline statements are not explicit psi-error inputs here. Absolute tail control would still leave the retained signed sum and S_f identification unresolved.
GAP: Prove a fully explicit cutoff and all-Y bound, including both boundary terms and complete prime-power jumps. The candidate scale below is an untested target, not an estimate established by this review. Finite signed payment, identification with S_f and L030-L032/C032a remain open.
REASON: Essential source coverage is now adequate for one routine mathematical specialization without the blocked1999 proof or retracted cutoff paper. Only source readiness advances locally; no new theorem, target bound, cancellation mechanism or RH claim is made.
SCOPE: Actual zeta prime powers; integers n>=2; real Y>=X_n>1; full terms m<=X at every cutoff. No RH, simplicity, S_f identity, signed finite-head bound or exchange of n and X limits is assumed.
LITERATURE_REASON: At invocation this standalone quantitative tail target lay outside the completed fixed-moment/source-exclusion comparison; its essential PNT, polynomial and endpoint source coverage was unassessed.
COVERED_TARGET: Test X_n=exp(10000*(n+1)^4) for |P_n(Y)-P_n(X_n)|<=1 for every integer n>=2 and real Y>=X_n, using Johnston-Yang Theorem1.1 and full prime-power jumps.

The nomination below is preserved as historical scope. Its pending-source
instructions were discharged by the completed step225 comparison below;
they do not request another search of the same sources.

Use the finite observable from review223:

    P_n(X)=sum_(2<=m<=X) Lambda(m)/m * L_(n-1)^(1)(log m)
           -integral_1^X L_(n-1)^(1)(log x) dx/x.

This definition is finite and proposes no identity with S_f. Essential
local context is L977's eta convention and L980's residual; L968 is
downstream only. The initial continuation must keep those signs and
normalizations, but no zero theorem is needed merely to define P_n.
The mathematical target is a uniform Cauchy bound on this explicit
finite statistic. No target bound or integration-by-parts formula
has been derived in step224.

First retrieve the primary PNT theorem, including its x range and
whether the bound concerns psi, theta or pi, and the proof cases
needed for any specialization. Johnston-Yang's paper is a concrete
lead, not a requirement to prefer its bound over adequate ready
coverage. Reuse the October register without redoing its source
assessment; nonvanishing alone is not a quantitative psi bound.
Then inspect primary polynomial and endpoint tools and check narrowly
for a matching existing local tail estimate before any research.

Continue only with a specified cutoff scale and a uniform all-Y
remainder whose constants can be verified independently of the
desired one-sided S_f estimate. Fixed-index convergence, omission of
prime powers or reliance on the retracted cutoff argument fails the
test. An absolute tail result would leave the retained signed sum,
its relation to S_f and the main positivity gap unresolved. Do not
claim it establishes a new cancellation mechanism or classify its
routine specialization as creative. Full Mathlib coverage is unknown.

## Completed comparison — step225, 10 November2026

The main gap remains actual-Xi positivity and the signed Li forcing
in L030-L032/C032a and L966/L968. This intermediate target isolates
the tail uniformity needed to replace a regularized arithmetic limit
by a finite observable. A successful absolute estimate would not
bound that observable's signed value. Continue only on a rigorous
all-n, all-Y bound at error1; fixed-n convergence, omitted jumps or
an unproved uniformity claim fails the test. A failed candidate
scale is evidence about that scale/envelope, not RH.

### Primary PNT input and qualifications

Daniel R. Johnston and Andrew Yang, *Some explicit estimates for the
error term in the prime number theorem*,
[arXiv2204.01980v2, 20 April2022](https://arxiv.org/pdf/2204.01980v2),
Theorem1.1/(1.3), p2, states for every real x>=2:

    |psi(x)-x|<=9.39*x*(log x)^1.515*exp(-0.8274*sqrt(log x)).

Its p1 definition sums log p over all p^m<=x. Table1's first row
has X=log2, A=9.39, B=1.515, C=0.8274. Section3.1, p7, covers
[2,59], (59,exp50], (exp50,exp2000] and (exp2000,exp2488]
using computation, Lemma2.2, Broadbent et al. Table8 and Lemma2.3.
Section3.2, pp7-9, covers x>=exp2488 for that row, using finite
verified height, zero density and a classical zero-free region.
Section1.4 incorporates a correction to an earlier zeta bound.
This is an unconditional theorem citation; its computations and
dependency proofs are not independently rerun. Other rows and
Section3.3 are unnecessary. The publisher page returned403;
the readable primary v2 PDF is the pinned input. Do not substitute
9.13 from differently indexed material. No optimality is claimed.

### Global polynomial tools and endpoint theorem

The [NIST DLMF18.5.12 finite-series identity](https://dlmf.nist.gov/18.5.E12)
reads, for nonnegative integer d,

    L_d^(alpha)(u)=sum_(j=0)^d
        (alpha+j+1)_(d-j)*(-u)^j/((d-j)!*j!).

The polynomial sum at alpha=1 has no finite-u restriction. We use
this algebraic representation, not a fixed-degree asymptotic or a
bound restricted to u<=4(d+alpha). The required degree is d=n-1.
[DLMF18.9.23](https://dlmf.nist.gov/18.9.E23) states

    (d/du)L_d^(alpha)(u)=-L_(d-1)^(alpha+1)(u), d>=1.

Here d=n-1>=1 and the derivative parameter is2. DLMF's derivative
source note cites Szego, *Orthogonal Polynomials*, 4th edition1975,
(5.1.14). The live equations and derivative source note were
inspected on10 November2026;
the book proof was not independently checked. Neither formula is
itself a quantitative n-uniform tail bound. Explicit coefficient
majorization is the identified specialization still to do.

Import finite Abel summation, Tom M. Apostol, *Introduction to
Analytic Number Theory*, Springer1976, Theorem4.2. The inspected
primary exposition is Tristan Shin, *Math104B: Discussion Section3*,
23 January2025, [pp1-2](https://cseweb.ucsd.edu/~dakane/Math104B/Discussion3.pdf).
For a:N->C, 0<y<=x and f in C^1[y,x], it states

    sum_(y<m<=x) a(m)f(m)
      =A(x)f(x)-A(y)f(y)-integral_y^x A(t)f'(t)dt,
    A(t)=sum_(m<=t) a(m).

The proof uses floors and explicitly accounts for the fractional
endpoint intervals; integers at x are included fully, and at y
excluded. We inspected that complete proof, not a Stieltjes preview.
For the intended application, the weight t^(-1)L_(n-1)^(1)(log t)
is smooth on every finite interval with t>1. The compensated Lebesgue
integral and both finite boundary terms must still be handled in
the mathematical attempt. No specialized identity is derived here;
no half-weight convention or contour theorem is needed.

### Overlap, failures, stronger inputs and unread leads

Reuse [review223](2026-11-10-compensated-prime-laguerre-head-review-223.md)
for Lagarias2007's fixed moments, normalization and retracted
Omar-Ouni-Mazhouda exclusion. L977 and L980's relevant conventions
were read; their contour obstruction and audited residual are
unchanged. The local targeted search covered foundations and the
10 November Li/Laguerre reviews, histories and attempts, with
terms Cauchy tail, Johnston-Yang, compensated Laguerre and partial
summation. Review201 concerns a different regularization eta and
does not bound prime-cutoff tails. Review200's real-frequency
limitations do not invalidate a finite polynomial tail estimate.
No matching ready local theorem was found within this stated scope;
this does not establish novelty or survey the entire notebook.

The [October source register](../../foundations/2026-10-quasi-riemann-input.md)
and its overlap assessment were read. They record a stronger fixed
zero-free half-plane and an alternate prime-counting corollary,
with explicit trust/scope limits. They do not furnish a ready
explicit psi bound for this cutoff. No quantitative consequence
is derived from them here. Using a sufficient explicit classical
psi input for a coarse tail is not a rediscovery of their zero-free
conclusions or an assertion of a current best bound.

Search also found an author-deposited preprint by Sardar Dilbag
Singh Khalsa, *1% Proof of Riemann Hypothesis: An Explicit Li-Kernel
Reduction of the Riemann Hypothesis*,
[Zenodo18726797v1, 21 February2026](https://zenodo.org/records/18726797),
advertising unconditional truncation bounds. Only its record/abstract
was inspected: the PDF requests failed with decoding error and429.
Its theorem, constants and proof are UNREAD and not imported. A
kenan.works prime-Bessel cutoff lead returned502 and is also UNREAD.
Neither is essential for the established-tool specialization, and
neither can justify a novelty claim or payment of the signed gap.
No repeated blocked extraction is proposed. The literature decision
rests on the independently readable primary tools above.

### Bounded continuation and coverage boundary

Nominate X_n=exp(10000*(n+1)^4) solely as an untested, deliberately
coarse candidate scale. The separate mathematical step must either
prove the error1 bound for all integers n>=2 and all real Y>=X_n
or record where that candidate fails. No coefficients, integrals,
constants or cutoff inequalities have been calculated in this
literature-only turn. The plausible tool chain is finite Abel
summation, the inspected psi theorem and global polynomial formulas;
the assembly and uniform inequalities remain future work.

SCOPE covers those tools and the exact COVERED_TARGET above, without
requiring any identification of the infinite limit with S_f. Such
identification, the finite signed arithmetic upper bound and the
actual-Xi positivity problem are independent unresolved assumptions
for downstream use. L013/L018 supply zero context and L968 the
downstream criterion only; none is a premise of this tail test.
No cross-notebook theorem is used. Full matching Mathlib coverage
of the proposed bound is unchecked/unknown.

This is SPECIALIZE coverage for a routine REPRODUCTION attempt,
not evidence of a new sign mechanism. The newly specified concrete
continuation requires separate supervisor approval next turn before
mathematics. Creative discovery remains prioritized at the central
signed gap; no justified independent cancellation mechanism is
ready from these sources, so this auxiliary specialization is not
relabeled creative. No lemma, mathematical script, PROOF assembly
or DAG edge is changed in step225.
