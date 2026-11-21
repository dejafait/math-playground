# Fixed-degree Jensen homotopy collision census — completed source review2048

TARGET: Assess a certified real-collision census for the fixed-degree Jensen homotopy P_{6,theta}, 0<=theta<=1/6, testing a one-pair ceiling without a full-support metric.
CHECKED: 2026-11-21
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Review2048 searched exact Jensen/Pollaczek homotopies, parametric real-root counting, ordered-domain subresultants/CAD and degeneracy handling; inspected BPR primary statements and relevant proof cases below, and scoped November20-21 Jensen/tilted/Pollaczek duplicates. No exact-path ceiling theorem was found; no novelty or nonexistence inference.
SOURCE_EVIDENCE: Reuse Kuznetsov and reviews2001/2012 for C029m/n/p's coefficients and endpoint; newly read Basu-Pollack-Roy, Algorithms in Real Algebraic Geometry, 2nd ed. (2006), Theorem5.16/proof and Notation5.15 pp165-166, Algorithms11.1-11.2 pp403-406 and11.13 p414, and Algorithms10.13/10.15/10.17-10.19 pp395-400; primary-text mirror and qualifications below. Rump (2010), Sections5/5.1/5.5, (5.1)/(5.4)/(5.16)-(5.17), including division's nonzero-denominator premise, inspected for the bounded witness method.
COMPARISON: General exact projection/lifting covers multiplicities and degenerate fibers, but presupposes effective coefficient sign tests; integer-only root isolation does not directly apply to Q(sqrt(2))[pi]. The fixed degree-six path is distinct from C029q/r/v and review2041. C029p already certifies theta=1/6; theta=0 is a different polynomial and a possible single-point falsifier, not an index already recounted.
GAP: No whole-path degree certificate, projection polynomial, collision parameter, exceptional-fiber count or ceiling has been calculated. Full CAD practicality with fixed enclosures is unverified. A bounded theta=0 Hermite certificate is source-ready; a pass there leaves the entire collision census and C029m's eventual index premise open.
REASON: Import known parameter-census coverage, but do not authorize a general CAD implementation or unbounded sign/precision campaign. First nominate the smallest falsifier within this same path: one theta=0 index certificate, using existing exact interval methods. Its separate ready assessment2048 requires next-turn approval; no calculation is performed now.
LITERATURE_REASON: Invocation-start REVIEW_REQUIRED lacked essential parameter-isolation and degeneracy coverage. This review fills that gap and reuses ready coefficient/Hermite/enclosure assessments; it is not additional browsing of a ready target.
SCOPE: Completed literature-only assessment. General census theory is covered with an effective-sign qualification; only the separate bounded endpoint-witness continuation is nominated for implementation. No new mathematical result, lemma or script; no full-census execution approval.

## Completed comparison2048

The original path and main-gap relevance are preserved below. The
continuation gate asked for exhaustive degeneracy coverage and a feasible
certificate, rather than a simple-root ODE or numerical scan. Theoretical
coverage is available; a practical complete census is not established.

Primary theorem source: S. Basu, R. Pollack and M.-F. Roy,
*Algorithms in Real Algebraic Geometry*, second edition, Springer2006,
[DOI](https://doi.org/10.1007/3-540-33099-2),
[primary-text mirror](https://www.cs.umd.edu/~gasarch/COURSES/752/S25/slides/AlgorithmsInRealAlgGeom.pdf).
This is the published second edition, not the differently numbered revised
online text. The author-hosted revised PDF timed out; the mirror supplied
the needed text. Shell download failed DNS; indexed primary text was read.
Neither failure blocks the theorem comparison. No download, installation,
API key, mathematical script or computation was used.

The book permits an ordered integral domain inside a real closed field.
Read Notation5.15/Theorem5.16 and its full proof, printed pp165-166:
projection includes truncations, leading coefficients and signed
subresultants, not just one discriminant. Read Algorithms11.1-11.2,
pp403-406, and11.13, p414: they produce sign-invariant cells and sample
points, including zero-dimensional fibers. Read Algorithms10.13/10.15
and10.17-10.19, pp395-400: Thom encodings support exact signs and ordered
samples. Degree constancy and common-factor cases are essential. The
continuity/multiplicity cases were checked in Theorem5.12, Proposition5.13
and their proofs, pp163-164. These are known algorithms, not an actual
coefficient sign oracle or a measured feasibility guarantee.

Applicability obligations for any later **complete** census are now
explicit. Use the actual normalized coefficients already in C029n's
Q(sqrt(2))[pi], retaining every odd term. An exact zero must be proved
algebraically or by a valid exact-number representation; an interval
containing zero is not a zero test. Fixed rational enclosures can certify
strict signs, but need not decide every sign required by projection or
lifting. Treating pi as a rational midpoint changes the problem. A
transcendence-based total sign oracle would be additional machinery,
not something supplied by a decimal enclosure or asserted here.

The source's product notation on Kuznetsov pp568-569 is compatible
with the intended theta=1/6 endpoint. That identification and the actual
degree at every parameter must be checked in a future application;
C029n certifies T_6's degree, not a continuous parameter theorem. The
constant S can be removed as in C029n/p without changing roots. There
is no source assertion that this continuous path is a zero-preserving
flow, nor that it analytically extends the varying-degree sequence.

A discriminant root may correspond to nonreal multiple roots; solving
only the real equations P=P_t=0 does not certify the whole exceptional
fiber's Hermite index. A complete implementation must certify all
projection cells, real multiple roots, higher multiplicities, possible
degree changes, both interval endpoints, and the distinct-pair index at
every exceptional parameter as well as on intervening intervals. The
repeated-root interpretation is already covered by C029l and review2001;
do not import simplicity or use only nonsingular Jacobi tests there.
No such fiber or index is evaluated in this review.

Consequently a full CAD implementation is not approved as the next
bounded calculation. This is a scope restriction, not an infeasibility
or impossibility theorem. First test theta=0 alone. Its coefficients
are C029n's beta_k/S without the T_6 Jensen weights; its degree check
and Hermite/Jacobi certificate require no parameter isolation, sign
oracle at a collision, new package or full-support metric. The exact
continuation and stop conditions are in
[assessment2048](2026-11-21-jensen-zero-endpoint-index-test-2048.md).
Index>=2 at this single member would reject the proposed whole-path
ceiling. Index<=1 is only a pointwise pass; unresolved minors are
inconclusive. Neither authorizes a full census or an eventual-N inference.

This operational restriction uses S. M. Rump, *Verification methods:
Rigorous results using floating-point arithmetic*, Acta Numerica19
(2010),287-449, [corrected primary PDF](https://www.tuhh.de/ti3/paper/rump/Ru10.pdf),
Sections5/5.1/5.5, (5.1)/(5.4)/(5.16)-(5.17), PDF pp24-25/27-28.
The relevant source definitions and inclusion argument were read,
including the requirement that a divisor interval exclude zero.
Exact rational endpoints implement those real-interval operations;
the result may overestimate and fail to separate signs. Reuse Coste
and Plaumann as already assessed in2001; no reproof is needed.

Queries included `Basu Pollack Roy Algorithms Real Algebraic Geometry
ordered domain real closed field cylindrical algebraic decomposition
polynomial coefficients sign oracle`, `Basu Roy real root counting
parameter polynomial transcendental coefficients ordered domain Sturm
theorem pdf`, `"Jensen" "Pollaczek" "homotopy"`, and
`"Jensen" "Meixner-Pollaczek" "collision"`. These found generic tools,
not a certified ceiling for this path. A Bernstein-isolation primary
chapter was located and partially inspected as a nonessential alternative;
no Bernstein algorithm or integer-input complexity bound is imported.

Local comparison read C029l/m/n, C029p's statement and construction,
review2001's multiplicity/Jacobi/Newton contract, review2012's general
Bezoutian coverage, and the scoped review2019/2041 and stop2042/2044
passages. The November20-21 Jensen/tilted/Pollaczek literature, history
and attempt search found no executed census or theta=0 certificate.
C029o/p already solve the unrestricted-metric representation problem;
no such metric is proposed again. Stops2042/2044 remain intact, with
their different hypotheses. Generic algorithms alone pay no actual-Xi
sign. This is local source coverage progress, not mathematics beyond
the sources checked. Full matching Mathlib coverage is unchecked;
no cross-notebook input or RH candidate.

Creative priority remains blocked by the absence of an independently
paid uniform actual-coefficient law. A six-dimensional witness is a
routine known-method calculation and must not be relabeled creative.
The historical finite stops are not global bans; a later materially
different signed uniform mechanism needs its own explicit discriminator.

## Invocation-start nomination2047, preserved

At invocation start this was the sole proposed next target, not an approved calculation.
Using exactly C029m's beta_k and p_k, define the proposed finite path

    P_{6,theta}(t)=sum_(k=0)^6 beta_k p_k(t)
                    product_(j=0)^(k-1)(1-j theta),
    0<=theta<=1/6,

with empty product equal to one. Source review must check its intended
endpoint identification with T_6, every actual-degree claim on the
closed interval, and whether the coefficient arithmetic/certification
is covered. This is a new, explicitly specified finite path. It is
not asserted to extend the varying-degree sequence T_N analytically
in 1/N, to approximate Xi uniformly in theta, or to obey a known
root-preserving flow.

Main gap remains L030-L032/C032a. The intermediate target is a
certificate of whether this fixed path ever has more than one distinct
nonreal conjugate pair. A complete collision census could expose or
support a particular coefficient-dependent propagation mechanism,
providing a prerequisite for a later uniform family argument. It
would not itself establish C029m's eventual hypothesis. C029p's index
one at theta=1/6 is an existing anchor, not a new result to reproduce.

The bounded future test, only if source review approves it, would
certify all relevant real solutions of P=partial_t P=0 in this closed
theta interval, handle any higher multiplicities and degeneracies,
and certify the Hermite negative index on the complementary intervals
and at the exceptional parameters. A parameter with index>=2 rejects
this path's proposed ceiling only. A complete ceiling<=1 is a finite
positive result with no automatic degree extension. Unresolved
isolation or signs are inconclusive, not evidence of absence. No
degree sweep, precision campaign, numerical root plot or runtime
installation is proposed. The review should reject infeasible scope
before approving a calculation and reuse ready elementary enclosure
coverage rather than reopen inaccessible general collision sources.

Essential local inputs are C029m/n/p and C029l's distinct-pair/nullity
convention. Contrast review2041's sign stop and review2019/C029q's
inter-degree stop narrowly. Eventual uniformity, initialization for
varying N, multiple-zero transfer and qualified weighted compact
convergence/upstream[9] remain open. No RH, simple-root or low-index
premise may be added. No cross-notebook input; Mathlib unchecked.
No mathematical derivation or evaluation was performed in nomination2047.

Creative routing is deferred: coverage and the feasibility of a
complete discriminating certificate must be settled first. If ready,
the supervisor can assess whether finite collision development
supports a genuinely new central mechanism; a routine census must
not be relabeled creative to meet a scheduling target.
