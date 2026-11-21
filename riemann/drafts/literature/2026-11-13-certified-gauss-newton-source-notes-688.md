# Certified Gauss-node Newton setup source review688

LITERATURE_REASON: Nomination687 is REVIEW_REQUIRED; the changed Newton mechanism needs inclusion, convergence and fully charged all-root setup coverage beyond the already reviewed recurrence and bisection implementation.

## Working checkpoint

The supplied startup snapshot was used directly. Narrow reads covered
source-notes683/686, C998k and its ATTEMPTS entry. Their prescriptions and
stops are preserved. No witness, mathematical script or other notebook
was loaded. Existing notebook changes are preserved.

The exact target is retained in assessment687. Main gap: actual-Xi
positivity and signed remote-plus-induced coupling. Intermediate target:
all nodes and weights for degrees63,81,117, radii<=2^-512, within5000000
scalar setup operations. Its possible use is the unchanged shared-bank
square service; no signed or global conclusion follows from readiness.
Continue only if inspected primary hypotheses support one complete finite
construction with paid isolation, refinement, weights and arithmetic;
stop that construction at an unpaid case or excess budget.

Initial primary retrieval: Johansson--Mezzarobba arXiv:1802.03948v1;
its Section2 interval-Newton details and Section3 evaluation proof are
being retrieved after the statement-level check. A2007 author-hosted
interval-Newton lecture note was inspected as orientation only; it does
not replace the precise primary citation. No finite root certificate,
local convergence constant, complexity bound or mathematical result is
asserted at this checkpoint. Completed source evidence follows below.

## Bounded search and reuse

Queries included `Johansson Mezzarobba 1802.03948 rigorous Gauss Legendre
Newton interval`, `interval Newton theorem inclusion convergence scalar
root interval derivative Moore Krawczyk theorem`, `Petras On the
computation 1999 pdf Gauss Legendre`, `Laurent Fousse accurate multiple
precision Gauss Legendre quadrature interval Newton`, `Interval newton
iteration in multiple precision pdf`, `Revol interval Newton 2003 pdf
ens lyon`, and `Alefeld Inclusion methods for systems pdf 1994`.
Followed the two node papers' references for seed and scalar inclusion
methods. No source for the exact degrees/radii/scalar cap was identified;
a failed search is not evidence of novelty or impossibility.

Source-notes683/686 already cover recurrence, simple roots, weight
formula and interval arithmetic. Their recurrence opening did not cover
the fixed-point error proof or the changed Newton stopping obligations.
C998k's full proof was read only to distinguish its fixed-loop stop.
It does not constrain the iteration count of Newton. Earlier stops
652/657/660/662/672/685 retain their exact scopes; no such service is
reopened by approving this separate setup test.

## Inspected primary evidence and applicability

**Legendre evaluation and weights.** Johansson and Mezzarobba,
*Fast and rigorous arbitrary-precision computation of Gauss-Legendre
quadrature nodes and weights*, arXiv:1802.03948v1,12February2018,
[primary PDF](https://arxiv.org/pdf/1802.03948v1): Section1(1)-(4),
Section2(5), Proposition3(6)-(7) and its complete proof, printed pp1-5;
Section3 Proposition5, Algorithm1, Corollary6(14) and complete proofs
including both delayed-division branches, pp6-8; Section6.2,p16.
These are known inputs, not claims of a new algorithm.

For a dyadic point x with |x|<=1, integer n>=1,t>=0, Algorithm1 returns
approximations to P_(n-1)(x),P_n(x), each with absolute error at most
[3(n+1)(n+2)/4+1]2^-t. Use this stated output bound(14), not a
precision heuristic. Proposition5 assumes |x|<=1 and bounded additive
recurrence perturbations. Its proof bounds their accumulation through
a generating-function majorant; Corollary6 separately checks both
Algorithm1 division branches. The input interval must be handled in
addition to the point-evaluation error. Proposition3 bounds P'_n and
P''_n throughout[-1,1]; the endpoint-valid alternatives are n(n+1)/2
and(n-1)n(n+1)(n+2)/8. Equation(5) obtains P'_n from adjacent polynomial
values; near1 its subtraction/division can lose precision. Every use
of this identity still requires a nonzero denominator and full interval
propagation. No guard-bit schedule is supplied locally.

Section6.2 uses Petras seeds followed by interval Newton at increasing
precision. That is implementation evidence, not a finite step or scalar
count theorem. Theorem1 concerns p comparable to n and asymptotic bit
operations and has only a proof sketch; it is not imported for the cap.
Nor are benchmark seconds an operation count. The fixed-point evaluator
and elementary interval arithmetic are sufficient available options;
hypergeometric algorithms and method-selection heuristics are outside
this approval. No general source theorem needs reproof.

All three saved degrees are positive integers, so these degree/domain
hypotheses fit. Actual dyadic evaluation points and intervals within
(-1,1), derivative exclusion of zero, complete error propagation and
adequate precision must be checked by the future finite construction.
The weights are those of Section1(3); their radii must be tested after
interval evaluation, independently of node radii. Simple roots ensure
the exact denominator is nonzero, not that its computed enclosure avoids
zero at an arbitrary working precision.

**Scalar inclusion, safeguards and the convergence qualification.**
Alefeld and Claudio, *The basic properties of interval arithmetic, its
software realizations and some applications*, Computers & Structures
67(1998),3-8, Section5 Theorem2 and the complete scalar discussion,
p6; Section6's finite-arithmetic qualification and Example4,p7,
[author-hosted primary PDF](https://na.math.kit.edu/alefeld/download/1998_The-basic_properties_of_interval_arithmetic_its_software_realization_and_some_applications.pdf).
For a C1 function on a domain containing the interval, a derivative
interval excluding zero permits the scalar Newton operator
N=m-f(m)/F'(X),m in X. Theorem2 gives root preservation, exclusion when
N and X are disjoint, and existence/uniqueness on inclusion N subset X,
with its interval solve defined. The scalar opening explains repeated
intersection with X. Section6 requires arithmetic inclusion to survive
machine evaluation. Polynomials satisfy the smoothness hypotheses;
the derivative interval condition remains a finite obligation.

The same inclusion, uniqueness and exclusion cases and their full
mean-value/Brouwer proof were also read in the author-hosted lecture
note *Interval Krawczyk and Newton method*,20February2007,
Theorem1,pp1-2,
[PDF](https://ww2.ii.uj.edu.pl/~zgliczyn/cap07/krawczyk.pdf).
This is a supporting proof check, not a separate convergence or work
input. The multivariate Krawczyk discussion is unnecessary here.

The primary scalar discussion asserts quadratic convergence only under
additional assumptions and refers elsewhere for proof. Do NOT import
an unconditional quadratic rate or a fixed iteration count from that
sentence. A bounded attempt instead checks each inclusion, actual
contraction and final radius, retaining prior root enclosures. It may
fail its chosen finite schedule. Zero-containing derivative intervals,
undecidable point signs and roundoff stagnation need charged safeguards
or explicit failure; they cannot be divided away. This allows the finite
test without relying on unread general convergence assumptions.

**All-root scope and alternative isolation.** Fousse, *Accurate
Multiple-Precision Gauss-Legendre Quadrature*, ARITH18(2007),150-160,
doi10.1109/ARITH.2007.8,
[conference primary PDF](https://www.lirmm.fr/arith18/papers/fousse-GLQuad.pdf):
Section2.2/Algorithm1,PDFp2; Section3.1 through the affine node-error
case and Section3.2 weight formula(2),PDFpp3-4. Read those passages,
including the separate isolation/refinement steps. Its Uspensky solver
and Revol refinement are external dependencies; their detailed
algorithms have not been inspected and are not imported. Its later
quadrature analysis assumes correctly rounded weights. Neither that
assumption nor the quoted ability to compute weights arbitrarily
accurately establishes this setup's absolute radius or work cap.

NIST DLMF[18.2(i)/(vi)](https://dlmf.nist.gov/18.2#vi),version1.2.8,
retrieved13November2026: read the nonnegative weight, finite positive
mass/all-moments hypotheses and the complete simple-zero/interlacing
paragraph. The unit weight on(-1,1) meets those hypotheses. This
provides the standard complete simple-root statement, with book
references Andrews--Askey--Roy1999,Theorems5.4.2/5.4.3. A future
construction may prove its own explicit proposed brackets by certified
endpoint signs and a complete root count, rather than importing an
unread Uspensky or asymptotic seed theorem. Its finite generation and
verification costs are then part of the target. This is an obligation,
not a new bracket construction or proof in this review.

## Access limits, nonessential leads and Mathlib

Petras1999, *On the computation of the Gauss-Legendre quadrature formula
with a given precision*, JCAM112,253-267,doi10.1016/S0377-0427(99)00225-3:
identified from the primary reference list; publisher full text returned
403 and was not read. Revol2003, *Interval Newton iteration in multiple
precision for the univariate case*, Numerical Algorithms34,417-426,
doi10.1023/B:NUMA.0000005354.92791.41: author's publication list located
the PostScript and report RR4334; PostScript is unsupported by the web
reader and the report page denied access. No invented PDF or snippet
stands in for either theorem. Moore--Kearfott--Cloud2009 Chapter8's
publisher preview stops before the full theorem; no unseen theorem
number or convergence hypothesis is attributed to it.

Those are nonessential leads for the approved finite-inclusion test.
They would become essential only if a future attempt relies on their
asymptotic seeds or general convergence schedules rather than directly
certifying brackets and steps. No persistent source blocker is asserted.
A shell download also failed DNS; the accessible primary web texts
above supplied the stated evidence. Search-connector PDF image and
link-following failures were bypassed by the direct web reader; text
extractions sufficed for the stated cases, with no image-only assertion.
Full matching Mathlib coverage is unchecked; supporting polynomial or
interval facts alone would not pay this finite setup service.

## Decision and limits

SPECIALIZE for the exact unchanged TARGET in assessment687: permit ONE
separate REPRODUCTION attempt with the five finite obligations added
there. No seeds, intervals, precision schedule, iteration count, cost,
node/weight value or mathematical script was produced here. No new
lemma or source reproof is warranted. Finite root/weight accuracy and
work are the local specialization still to establish, not source facts.
The cap is a chosen setup subbudget, not a universal lower-bound claim.

A successful setup could support the shared endpoint-bank square rule.
The bank, its remainder/cancellation/error propagation, both endpoint
brackets, fourteen moment families, C999q exact Z, contraction and
complete square error<=1e-10/work<=20000000 are still unpaid. Actual-Xi
positivity, signed S3, A-square, both mixed terms, projection, inverse
debt, higher/mixed endpoints, C744q/H2 and global/non-neutral assembly
remain independent gaps. This is a local source-readiness advance,
with no mathematical advance beyond the checked sources and no RH
claim. No new signed comparison suggests a justified creative central
target in this step; routine node setup is not relabeled creative.
