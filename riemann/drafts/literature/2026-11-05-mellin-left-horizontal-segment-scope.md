# Finite left horizontal theta-Mellin segment: completed source comparison

TARGET: Assess the standalone left horizontal theta-Mellin segment from u/2+i Im(x-da) to x-da against (9u/sqrt(Q))exp(-(77/50)Qd^2) on all D, without assuming global contour or continued-endpoint identities.
CHECKED: 2026-11-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step526 searched the nominated u/2, left horizontal, left-tail and T_L claims in L797–L801, Mellin-named local assessments and the global-import stop; exact theta/Mellin/left-horizontal/9 and Mellin/77/50/u/2 queries found no inspected matching theorem. Standard log-concave left-tangent terminology led back to the primary Devroye envelope; no novelty inference.
SOURCE_EVIDENCE: bramble_trace, paper23 v1 (18 October 2026), Section3 Lemma2 (10)–(14), https://rstation.ai/problems/riemann_hypothesis/papers/23; Luc Devroye, Non-Uniform Random Variate Generation (1986), ChapterVII Section2.6, pp299–300, explicit left envelope preceding Theorem2.6 and the reflected-case reduction/first integral in its proof, https://luc.devroye.org/chapter_seven.pdf; inspected 2026-11-05. Reuse step522's DLMF2.3(iii)/2.4(iii) comparison, without claiming their effective coverage.
COMPARISON: Devroye explicitly supplies the left tangent exponential under differentiable log-concavity, rather than only a right-tail asymptotic. It supplies no theta concavity, amplitude bound or 9,77/50 constants; paper23 prints a combined horizontal allowance without this finite split. These parameter-specific obligations require a separately approved specialization attempt.
GAP: Verify finite-segment admissibility and branches, a full theta-amplitude majorant, the real-phase concavity and quantitative positive slope at its right endpoint, and the normalized allowance on all D; none is established by this source review.
REASON: The inspected left envelope removes the essential method-coverage gap for an independent known-method test, with no global contour, continued endpoint or unread supplement as a premise. Citation alone does not settle the actual-theta hypotheses or bound.
LITERATURE_REASON: The changed target replaces the infinite right ray by a finite left segment down to Re z=u/2, with outward height displacement, smaller theta parameter and a distinct one-sided phase condition; the saved right-ray assessment does not cover these hypotheses.
SCOPE: Literature-only step526 completes the changed-target review; no new estimate, lemma or mathematical script. The new ready research nomination receives separate supervisor approval next turn. The original nomination below is retained as historical target specification, not an outstanding instruction or result.

Use L797's D and saddle x=u+ih, L798's Q,d,S_s,A,a and principal
C=sqrt(2pi/A), and L799's normally convergent theta series P on U.
Define z_L=x-da=v_L+i y_L. The proposed observable is

    T_L(s)=|integral_{u/2}^{v_L}
                  exp(2s Log(v+i y_L))P(v+i y_L) dv|
             / |4pi^2 exp(S_s(x)) C|.

The exact target for assessment is

    T_L(s)<=(9u/sqrt(Q))exp(-(77/50)Qd^2), for every s in D.

This defines a chosen standalone finite interval, not the source's
unprinted division between its horizontal and far-left terms. Check
its admissibility, branches and normalization in the scope review.
No deformation of M(s), zero information or endpoint continuation is
assumed. L801 is relevant for the downstream budget, not an automatic
bound on this opposite segment; no cross-notebook input is proposed.

The main gap remains actual-Xi all-degree mixed positivity. A paid
left segment could join the audited finite saddle and right-ray
components in a separately assessed approximation. The choice of 9
seeks room in the printed coefficient 14 after L801's recorded right
coefficient; this is only a target allocation. The portion before
Re z=u/2, the continued endpoint, contour equality, full error
assembly, quotient/inversion, certificates and sufficient signs remain
independent open obligations. This is not an RH candidate or a new
creative sufficient-sign mechanism.

Reuse the existing primary-source excerpts and narrow duplicate/failure
searches where they actually match. Compare the standard endpoint
envelope with this left-interval direction and the actual complex
amplitude before assigning IMPORT, SPECIALIZE or EXPLORE. Distinguish
the imported elementary method from unproved theta-specific hypotheses.
Read exact primary cases if essential coverage is missing, not a new
global asymptotic survey. The historical global-import stop remains
valid; unread Derivations42/43/65/87 are not premises.

Continue only if a precise known effective method or an adequately
searched independent test covers this target without the parked
global assumptions. If essential access remains blocked, park the
dependent claim and nominate a materially different independent target.
A later mathematical attempt should pass only with a uniform proof of
the displayed allowance on both closed boundaries, both signs of h,
h=0 and unbounded u, or provide a rigorous obstruction to the chosen
sufficient method. Method failure alone would not refute T_L or RH.
Full matching Mathlib coverage is unchecked.

## Completed review, step526

### Exact source comparison

Reused step522's adequate endpoint-method and fixed-data asymptotic
assessment; refreshed only the changed finite left side. Reopened
[paper23 v1](https://rstation.ai/problems/riemann_hypothesis/papers/23),
Section3 Lemma2 (10)–(14), on 5 November 2026. Its contour has the
outward left height and its horizontal allowance combines two tails.
It does not specify this split at u/2 or the coefficient 9. The source
assigns horizontal concavity and endpoint regimes to unread
Derivations42/43/65. Neither those claims nor Derivation87 is imported.
The existing global-import stop is preserved.

Luc Devroye, [*Non-Uniform Random Variate Generation*](https://luc.devroye.org/chapter_seven.pdf),
Springer-Verlag, 1986, ChapterVII Section2.6, pp299–300
(PDF pages14–15): the envelope preceding Theorem2.6 explicitly includes

    f(m-b) exp((y-(m-b)) h'(m-b)), h=log f.

It requires differentiable real log-concavity. Its proof treats the
opposite side by reflection and integrates the exponential piece.
Positive finite left slope is the decaying case. Only this pointwise
principle is imported, not the optimization theorem or its probability
normalization. Later use for an unnormalized phase must justify that
concavity step directly; no property of complex P or |P| is supplied.

Reuse [step522's comparison](2026-11-05-mellin-right-horizontal-tail-scope.md)
with DLMF2.3(iii)/2.4(iii): those fixed-data asymptotics do not automatically
pay moving-parameter effective constants. No new theorem from DLMF,
O'Sullivan, a search snippet or an unread supplement is being imported.
There is no essential source-access blocker for the specified envelope
test; this does not certify that its sufficient hypotheses hold.

### Local inputs, applicability and bounded test

The read ranges in L797 and L798 establish the already audited saddle,
branches, finite-disc decrement and normalization. L799 establishes
normal convergence on U and the exact series factorization; its
amplitude bound is only for the saddle diameter. L801's right-ray result
is downstream budget context, not an input bounding the opposite
segment. No completed standalone left-segment proof was found in the
narrow local search. The global-import stop is a restriction on automatic
assembly, not a ban on this independently defined finite integral.

A later research attempt may use the left tangent principle only after
checking these actual-theta obligations:

1. Check the ordering and nonempty finite interval, principal Log domain,
   strip admissibility and continuity along every point of the segment,
   using z_L=x-da=v_L+i y_L. Cover both closed boundaries of D, both
   signs of h, h=0 and unbounded u. A saddle-disc check alone is not the
   whole segment check.
2. Obtain a full complex theta-amplitude majorant from L799's normally
   convergent series and factorization on this segment. Do not extend its
   diameter eta estimate by assertion, or discard the n>=2 sum when the
   real part moves down to u/2. Justify any integral/series interchange.
3. For the real horizontal phase Re(S_s(v+i y_L)-S_s(x)), check concavity
   on the entire finite interval and a quantitative positive derivative
   at v=v_L. Retain L798's decrement at z_L; it gives no horizontal slope
   or whole-segment concavity. Pay the amplitude, integrated envelope
   and exact |C| normalization against the proposed 9,77/50 allowance.

These are conditions to test, not assertions proved in this review. An
explicit failure of a sufficient condition or of the resulting sufficient
bound is an informative obstruction to this method, not a counterexample
to T_L. Preserve such evidence and retire the method unless new input
changes that obstruction. Do not extend the claim to the portion before
u/2, a combined error budget, continued M(s), its quotient/inversion,
certificates or sufficient signs. A successful component could support
only a separately assessed Mellin approximation.

### Search record and decision

Queries issued in this turn were `"theta" "Mellin" "horizontal" "left"
saddle bound`, `"bramble_trace" "u/2" Mellin`, `log concave finite interval
integral upper bound positive logarithmic derivative endpoint tangent`,
`"theta" "Mellin" "left horizontal" "9"`, `"Mellin" "77/50" "u/2"`, and
`"log concave" "tangent" "left" Devroye`. Results did not supply a matching
inspected theta theorem; no absence or novelty claim follows. General
simulation, probability and unrelated author-comment hits were leads
only, not theorem inputs; their detailed sources were not read. The
primary Devroye statement and essential proof case suffice for this
conditional method test, so a broader survey is unnecessary.

DECISION is SPECIALIZE: source reproduction of a selected component,
not creative mathematics or a new discovery. A citation cannot replace
the listed hypotheses or constants. Full matching Mathlib coverage is
unchecked; no cross-notebook input was read. The actual-Xi sign gap
remains unchanged. No central creative sufficient-sign mechanism is
justified by these approximation bounds, and that missing mechanism is
the blocker to nominating one in this focused source step.

The [research nomination](2026-11-05-mellin-left-horizontal-segment-test.md)
is ready in source scope and awaits separate supervisor approval next
turn. This is local source-readiness progress only; the displayed T_L
bound has not been proved, tested numerically or assumed.
