# Vertical Pick block — completed zero-count/concentration source review

TARGET: Test whether rational Hardy-kernel concentration and local counts of all xi zeros produce full-Gram Rayleigh quotients tending to zero for K/ell_X along T tending to infinity, with off-line zeros and the entire tail controlled.
CHECKED: 2026-11-01
DECISION: EXPLORE
SEARCH_EVIDENCE: Reused the finite-Pick assessment and exact arithmetic failure records; newly searched rational Hardy concentration, prescribed-pole inequalities, model-space sampling and truncated-Toeplitz spectral limits. Inspected primary statements and relevant proof cases below. No matching actual-Xi witness theorem was identified; no novelty or exhaustive-absence claim.
SOURCE_EVIDENCE: Reused L467 and its Bellotti--Wong 2412.15470v2 Theorem 1.1/Sections 3,5 coverage, reconfirming the versioned theorem and final height cases; inspected Suzuki 2206.03682v4 Section 2.2/(2.6); Baranov--Zarouf 1310.1182v1 Section 1.1; Baranov--Jaming--Kellay--Speckbacher 2304.02385v2 Section 3.1 and Theorems 5.1--5.2/Lemma 5.3 with proofs; Hartmann--Jaming--Kellay 1707.07880v1 Theorem 2.3; Miheisi--O'Loughlin 2404.03087v1 Theorem 2.1, Sections 4.1--4.2 and Lemma 4.3 with proofs.
COMPARISON: Known zero expansions, all-zero counts, rational model spaces and spectral concentration tools cover the standard inputs, but not their actual-Xi combination. The spectral theorem is stated for one nested zero sequence; L640's moving grid is a triangular array. Boundary sampling estimates do not control off-line evaluations or yield a vanishing Rayleigh quotient. These are identified research differences, not source-access blockers.
GAP: Quantify concentration dimension versus all local zero constraints for the exact distinct-node family, justify any triangular-array specialization, and bound every off-line/exterior contribution in the full Gram norm. Neither a dimension surplus nor a full-tail witness is established by this review.
REASON: The separate source review is complete and supports one bounded attempt on the unchanged target. EXPLORE licenses testing the documented differences using inspected standard inputs; it does not assert a concentration theorem for this family, an obstruction, positivity or RH. Repeated arithmetic reduction remains parked.
SCOPE: Same s_j=2+i(X+j/N), N=floor(log T), full C and K as L640; standard finite spectral/min-max linear algebra and rational-function estimates may be applied with written applicability proofs. No confluent-node replacement, nested-grid assumption, RH, simplicity, critical-line nonvanishing or positive zero measure is assumed.
LITERATURE_REASON: Invocation-start REVIEW_REQUIRED lacked zero-product, all-zero-count and finite rational concentration comparisons; this separate literature-only step supplies them. Further unchanged-target browsing is unnecessary unless a specific essential new input emerges.

## Completed review — 1 November 2026

This is a literature-only EXPLORATION, NOVELTY_UNCHECKED. No lemma,
mathematical script, numerical probe or new inequality was produced.
The original nomination is retained below as historical scope. Sources
support the proposed *test*, not its success. The exact TARGET and its
asymptotic threshold are unchanged.

### Actual zeros, normalization and counts

Masatoshi Suzuki, *Aspects of the screw function corresponding to the
Riemann zeta-function*, JLMS 108 (2023), 1448--1487,
[2206.03682v4](https://arxiv.org/pdf/2206.03682v4), Section 2.2, printed
p.7, equation (2.6) and its full proof, uses the same completion as L018.
For zeros gamma of xi(1/2-iz), with multiplicities, it states

    F(1/2-iz)=i b+i sum_gamma (1/(z-gamma)+1/gamma), b=0.

The grouped summands converge absolutely locally uniformly away from
zeros; the proof obtains b=0 from reflection. The strip bound and
gamma -> -gamma symmetry are retained. This is a precise standard
logarithmic-derivative input; it is not a formula for L640's normalized
quadratic form. Converting it requires tracking the opposite sign of
L018's Xi variable, the pairing, conjugations and the denominator
s_j+conjugate(s_k)-1. Do not separate the compensators into divergent
series. The previously inspected Suzuki Section 3.1 distinction between
complex bilinear spectral terms and real-zero modulus squares is reused
from `2026-11-01-screw-function-signed-remainder-screen.md`; no positive
zero measure is imported. The PDF is controlling: wrapper v4 is dated
30 May 2023, internal date 31 May; the HTML date is inconsistent.

For counts, reuse the already audited L467 specialization and
`2026-10-25-l467-critical-audit-coverage.md`. The controlling primary input
is Bellotti--Wong, [2412.15470v2](https://arxiv.org/pdf/2412.15470v2),
7 July 2025, Theorem 1.1, printed p.1:

    |N(H)-H/(2pi) log(H/(2pi e))|
       <=0.10076 log H+0.24460 log log H+8.08344, H>=e.

N counts positive ordinates of **all** nontrivial zeros with multiplicity;
the argument principle in Section 3 and Section 5's large/compact height
cases are covered by the saved assessment, with the final cases
reconfirmed here. The latest abstract has a different constant; it does
not replace v2. L467 proves the closed unit-shell bound 18 log(v+2),
including lower endpoints. No source computations were rerun. These
theorems supply unconditional count bounds, not a dimension surplus,
small count at every center, or a simultaneous favorable tail. Any use
of averaging in X, narrower windows, or sharper leading constants needs
its own application proof; a coarse O(log T) count alone is insufficient.

### Rational space and boundary sampling comparisons

Baranov--Zarouf, *A model space approach to some classical inequalities
for rational functions*, [1310.1182v1](https://arxiv.org/pdf/1310.1182v1),
4 October 2013, Section 1.1, printed pp.1--2, gives the finite-Blaschke
model space as rational P/Q with numerator degree at most n-1 and
prescribed reflected poles (multiplicities retained), and its reproducing
kernel. These are standard identities, not a concentration theorem.
They justify using that language; the half-plane change of variable,
norm constant and exact distinct poles must be written out in research.

Baranov--Jaming--Kellay--Speckbacher, *Oversampling and Donoho--Logan
type theorems in model spaces*, [2304.02385v2](https://arxiv.org/pdf/2304.02385v2),
12 February 2024, Section 3.1, (3.1)--(3.3), (3.7), gives upper-half-plane
model kernels with Lebesgue boundary norm and boundary diagonal
|Theta'(x)|/(2pi). Theorem 5.1 states, for positive Borel mu on R,
1<=p<infinity, bounded boundary Theta', and delta>0,

    ||f||_(Lp(mu))^p <= (1+delta ||Theta'||_infinity)^p
                             D_mu(delta) ||f||_p^p,
    D_mu(delta)=sup_x mu([x,x+delta])/delta, f in K_Theta^p.

Theorem 5.2 gives ||f'||_p<=||Theta'||_infinity ||f||_p.
Read both proofs and Lemma 5.3: derivative-kernel Holder integration,
endpoint p cases, then interval suprema and the fundamental theorem of
calculus. The theorem is an **upper** boundary sampling bound; it does
not construct a low-energy vector. Global unweighted zero counts have
unbounded shell supremum, so this cannot be applied with a silently
finite D_mu to the entire zero set. Weights/localization and off-real
evaluation bounds would need justification. No growing-N strip bound
is asserted here. The journal download returned 503; arXiv resolved
access, so this is not SOURCE_BLOCKED.

Hartmann--Jaming--Kellay, *Quantitative estimates of sampling constants
in model spaces*, [1707.07880v1](https://arxiv.org/pdf/1707.07880v1),
25 July 2017, Definition 2.2/Theorem 2.3, printed pp.6--7, characterizes
dominating measurable boundary sets for meromorphic inner Theta and
1<p<infinity by relative density in amplified Baranov intervals. Its
quantitative constant contains C(Theta,p,epsilon). Neither that
inner-function dependence nor its boundary-set hypothesis licenses
uniform concentration or complex zero sampling in our growing family.
This theorem-level comparison suffices to exclude it as a direct import;
its full proof was not reviewed or used.

### Spectral concentration: stronger source, precise remaining difference

Miheisi--O'Loughlin, *Szego Limit Theorem for Truncated Toeplitz
Operators*, [2404.03087v1](https://arxiv.org/pdf/2404.03087v1),
3 April 2024 (internal date 5 April), Theorem 2.1, printed p.3,
uses one sequence lambda_j in D, lambda_0=0, finite products B_N of its
first N entries, and dnu_N=|B_N'|dm/N. For phi in
L_infinity intersect X_Lambda, where X_Lambda closes continuous symbols
in sup_N L2(nu_N), it gives

    Tr f(T_(B_N)(phi))/N - integral f(phi) dnu_N -> 0.

f is analytic near the closed convex essential range; for real phi it
may be continuous on that interval. For poles uniformly inside the disk,
the source identifies X_Lambda with L2. Read Sections 4.1--4.2 completely:
Lemma 4.1's contraction, pointwise and Lipschitz/approximation cases;
Lemma 4.2's Hilbert--Schmidt comparison; analytic and real-symbol cases.
Also read Lemma 4.3 and its proof: fixed trigonometric symbols have a
trace-norm product defect bounded uniformly over inner B. These are
substantive known concentration tools, not an actual-Xi witness.
L640 has a moving grid, not the theorem's nested sequence; neither that
change nor indicator-symbol approximation is approved as automatic.
Local specialization must establish uniformity and preserve the norm.
No quantitative eigenvalue count or tail rate is derived here. The PDF
controls version/date over the inconsistent HTML internal date.

The 2017 Strouse--Timotin--Zarrabi original
[1702.08147v1](https://arxiv.org/pdf/1702.08147v1), opening and Section 1,
was inspected for provenance; its full theorem/proof was not used.
The stronger 2024 source supplies the operative comparison.

### Duplicates, failures, bounded research boundary

Read L018 in full, L467 with its audit, and L640's exact hypotheses and
conclusions. Reuse the ready vertical-block assessment and the two
specific arithmetic histories/failure records; L640 remains unaudited.
The joint-Blaschke mesoscopic-mass assessment
`2026-10-30-joint-blaschke-mesoscopic-mass-coverage.md` concerns pair-quotient
weighted mass at microscopic scales; its count-versus-weight warning is
relevant, but it does not address this finite rational Gram family.
The previous TV/projection and short-coordinate stops remain unchanged.
No sibling notebook was read and no cross-notebook input is used.

Queries included `rational model spaces reproducing kernels concentration
time frequency truncated Toeplitz eigenvalues finite Blaschke products`,
`rational prolate spheroidal functions concentration finite Blaschke
product`, `model spaces time concentration eigenvalues rational functions
interval Blaschke product`, `model spaces Remez inequality`,
`Baranov Jaming Kellay Speckbacher model spaces large sieve`,
`truncated Toeplitz Szego finite Blaschke products eigenvalue distribution`,
and exact xi/logarithmic-derivative/paired-product and Bellotti--Wong
searches. Snippets and generic prolate terminology are not theorem
evidence. Prescribed-pole Bernstein search hits were not imported beyond
the inspected model-space sources. Full matching Mathlib coverage is
unchecked, not asserted absent.

The next attempt must first write the correct zero-pair quadratic identity
and identify a quantitative concentration/rank comparison using **all**
local zero constraints. It must then price complex evaluations and the
entire complement, or record the first decisive obstruction. Ordinary
finite spectral/min-max arguments and elementary rational estimates may
be used with full proofs; no unknown strip-concentration theorem may be
assumed. Qualitative boundary L2 concentration alone is insufficient.
This is development from known machinery, not a reproof of the cited
theorems. The uncovered mathematical difference is the research target,
not an unavailable essential source.

Continue only with an explicit dimension surplus and a full normalized
remainder tending to zero, or an informative obstruction to a stated
necessary inequality. A full Rayleigh countersequence would rule out
the proposed fixed norm reserve and redirect finite sign research; it
would not refute positivity or RH. If the next attempt only reproduces
the old arithmetic majorant or leaves another unquantified reduction,
reassess this diagnostic at its third mathematical EXPLORATION, without
resetting the two turns already used. The global sign, arbitrary-node
and boundary-transfer gaps remain independent.

## Original nomination (preserved; source tasks above now supersede it)

## Concrete proposed test, not a result

Retain the full-Gram normalization from L640 and put

    B_(T,X)=C^(-1/2)K C^(-1/2)/ell_X=I+R_(T,X).

Seek T_m tending to infinity, X_m in [T_m,2T_m], and unit vectors x_m
such that x_m^*B_(T_m,X_m)x_m tends to zero. If such a sequence is
proved, its R-Rayleigh quotient tends to -1, which rules out every
eventual fixed norm margin below one. This is an obstruction to the
specified budget, not a negative eigenvalue assertion or a disproof of RH.
There is no claim that this sequence exists.

The proposed mechanism is to compare the dimension of a rational Hardy
space concentrated near a bounded ordinate interval with the number of
constraints contributed by all xi zeros there. A vector satisfying those
constraints would still need a quantitative bound for all remaining
contributions. Neither the dimension comparison nor that tail estimate
has been derived. Off-line zeros may give indefinite paired kernels;
positivity, a critical-line-only count, simplicity, or discarding the
outside window would invalidate the test. No conjectural zero statistics
or unproved boundary extension is licensed.

## Essential input and review boundary

L018 supplies the actual completion and zero correspondence. L640
supplies the exact Cauchy Gram and normalization; its own separate audit
remains open. These are the only local mathematical inputs currently
used. Its signed generating formula is historical motivation, not a
zero-count theorem or a concentration bound.

The source review should locate exact statements and proofs adequate
for: (a) a convergent, correctly normalized zero-pair expression for this
finite kernel; (b) a suitable count of all nontrivial zeros, with
multiplicity and height quantifiers; and (c) finite rational Hardy-space
concentration and a quantitative tail estimate in the joint N,height
regime. Riemann--von Mangoldt and finite reproducing-kernel concentration
are search leads, not imported results. L467 was identified by filename
as a local explicit unit-shell count and remains unread for this target;
the review must determine whether its bound is useful, not assume so.
No cross-notebook input is proposed. Full matching Mathlib coverage is
unchecked.

Continue only if inspected sources leave a concrete, independently
testable concentration/rank or tail inequality. If their hypotheses
already give the witness, import and specialize rather than reprove it.
If dimension or off-line/tail requirements defeat the mechanism, record
the precise obstruction and choose another target. A qualitative
concentration claim or an RH-only statement does not close this target.
The existing diagnostic has used two mathematical EXPLORATION attempts;
this source nomination does not reset that budget or endorse a third
repetition of the arithmetic reduction.
