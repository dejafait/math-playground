# Small-displacement pair sum: completed source comparison

TARGET: Assess zero-conditioned Hermite interpolation and discrete derivative moments for a uniform bound B_epsilon(T)<=C epsilon^alpha T(log T)^3 with some fixed alpha>0, where B_epsilon is L471's pair sum restricted to 0<d_j log T<=epsilon<=1.
CHECKED: 2026-10-28
DECISION: EXPLORE
SEARCH_EVIDENCE: Bounded exact/stronger-result searches for complex Hermite divided differences, unconditional discrete zeta-derivative moments, conjugate-zero quotients and local Blaschke sampling; narrow local duplicate/failure searches found no matching pair-sum estimate. Primary statements and relevant interpolation/factorization proof cases were read as recorded in drafts/2026-10-28-zero-conditioned-source-notes.md; no novelty or exhaustive-search claim.
SOURCE_EVIDENCE: de Boor (2005), Section 9 (50)--(52), pp. 62--64; Broughan II (2017), Theorem 3.3 proof (1),(4), pp. 26--27; Kirila arXiv:1804.08826v1 Theorems 1--2/Corollary 3; Durkan--Hughes--Pearce-Crump arXiv:2601.06292v1 (1.1), (1.3), Theorem 1/(2.1); reuse Bettin v1 Theorem 1 and small-shift scope from the existing paired-height assessment; L471 (1)--(5)/Section 4 and the two nominated ATTEMPTS records.
COMPARISON: Complex interpolation and finite zero factorization allow coalescence and multiplicities but provide no summed B_epsilon bound. Kirila's positive discrete estimates assume RH; the 2026 unconditional mixed moment is reflected bilinear, not the required positive quotient square. Continuous microscopic-shift second moments are available without RH; zero-dependent aggregation is the research gap.
GAP: Test whether interpolation retaining all nearby zero factors can control multiplicity and clustering with constants independent of epsilon and T and no extra logarithmic loss; no alpha>0 or bound for B_epsilon is established.
REASON: Essential classical tool coverage is accessible for one bounded local factorization/interpolation test without importing an unavailable discrete moment. The newly written research continuation is proposed for separate approval next invocation; the original mathematical target and old stops are retained.
LITERATURE_REASON: The target changes from an abstract six-coordinate feasibility audit to an actual-zero-conditioned analytic quotient estimate; deterministic shifted moment theorems do not supply the required zero-sampling input.
SCOPE: Source comparison for the exact restricted L471 sum; proposed research uses fixed-size microscopic disks, complex-node interpolation, finite Blaschke factors and continuous small-shift second moments only. No new zero-free region, full N(T) saving, RH, simplicity, separation or lower displacement bound.

## Completed review

The complete primary citations, hypotheses, inspected proof cases,
source-access limitations and local duplicate comparison are in
[the source notes](../2026-10-28-zero-conditioned-source-notes.md).
This is a literature-only EXPLORE outcome: no matching theorem,
new bound, positive exponent or generic obstruction was established.
The proposed [bounded research continuation](2026-10-28-small-displacement-cluster-test.md)
requires separate approval next invocation. Full matching Mathlib
coverage has not been checked; no absence claim is made.

## Original nomination (pre-review state, preserved)

The text below records the starting questions and then-unread leads.
The completed review above supersedes that source status.

## Exact proposed target and its relevance

Use L471's actual Xi, gamma normalization A, conjugate pairs
gamma_j +/- i d_j, multiplicities m_j, intervals J_j(T), and entire
quotients F_j=Xi/((z-gamma_j)^2+d_j^2). Define B_epsilon(T) by the
same nonnegative summands as B(T), restricted to d_j log T<=epsilon.
This is only a definition of the proposed target, not a bound.

Seek some fixed alpha>0 and C,T_0 independent of epsilon such that
the displayed TARGET inequality holds for all T>=T_0 and
0<epsilon<=1, retaining truncated boundary windows and multiplicities.
Equivalently, the normalized restricted mass would have a uniform
positive power of epsilon. No particular exponent is asserted.
Even such a bound would leave the complementary displacement sector,
the full little-o estimate in L471 (3), individual-height exclusion and
global mixed positivity unresolved.

The proposed new mechanism is to use both complex zero conditions
before taking absolute values: a Hermite divided-difference or Cauchy
interpolation formula for the entire quotient, followed by an estimate
sampled at the actual zeros. This is an unread route to assess, not a
derived identity or an approved mathematical application. In particular
it must not simply substitute -Z/q and repeat L471 (5).

The two prior stops remain in force at their stated scopes: ordinary
unconditioned moments lose the displacement weight, and the fixed
paired second/fourth constraints permit positive clipped mass. This
nomination adds actual zero conditions, rather than more copies of
the same finite-law test. The required October 21 baseline and external
register were read before making it; their fixed half-planes are not
being rederived or used as a substitute for microscopic sampling.

## Bounded source test

Search exact terminology, stronger quotient/moment estimates and
obstructions. Inspect primary theorem statements and essential proof
cases before large extracts. Check the active notebook narrowly for
divided-difference and zero-sampling duplicates; no exhaustive duplicate
search for this new target has yet been made. Read only relevant L471
input ranges and source qualifications. No cross-notebook input is
proposed. No full matching Mathlib coverage has been checked.

Continue only if the review supplies a directly applicable bound or
defines a concrete source-ready interpolation/sampling test with all
uniformities and its attainable epsilon power explicit. Record any
RH, simplicity, separation or fixed-displacement restriction rather
than silently applying such a theorem. If the needed sampling source
is inaccessible or structurally loses every positive epsilon power,
park that dependent test; the original pair-sum failure is not erased.

If a new source-ready mechanism survives, nominate a bounded creative
proof attempt with the restricted mass as the decisive test and the
uncontrolled complement explicitly retained. Creative routing remains
pending essential source coverage; this nomination approves no new
mathematics and claims neither novelty nor feasibility.
