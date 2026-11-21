# Joint fixed-bump projection after the coefficient audit

TARGET: Test whether the joint two-shift arithmetic span in L933 has uniformly vanishing projection of L637's fixed unit bump, using the full coefficient supremum at N=floor(T^(1/5)).
CHECKED: 2026-11-09
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step27 reuses the exact joint-dictionary searches and Pratt–Robles/BCR comparison in drafts/literature/2026-11-09-joint-two-shift-arithmetic-dictionary-scope.md and the fixed-order versus growing-order projection comparison in drafts/literature/2026-11-09-longer-arithmetic-dictionary-scope.md; read L927 Section3 and its separate audit, L637 fixed hypotheses, L933 hypotheses and conclusions, and the four relevant stop records. No new broad search or novelty claim.
SOURCE_EVIDENCE: Reopened Hughes July2017 Theorem2.2 printed p18 and the complete two-branch passage and heuristic qualification p19 https://personal.maths.manchester.ac.uk/jm/wiki/uploads/LMS/Hughes-lectures.pdf#page=20 ; named underlying import is Titchmarsh–Heath-Brown second edition (1986) Section4.17 (4.17.4) p89. Reuse L927 Section3's finite-dimensional projection identity and audited numerator framework, and step26-audited L933(4)'s actual joint norm. No new moment theorem is needed.
COMPARISON: The real-axis source covers both translated heights without differentiating the remainder; the weight, unit bump and coefficient class coincide with L927/L933. L927's variational identity applies to the entire finite joint span, whereas adding separate projection estimates is invalid. Prior related growing-order projection coverage does not include this fixed-Z space; no inspected source directly supplies this exact joint projection conclusion.
GAP: In one later application write the joint local correlation estimate with both coefficient channels, divide by L933(4), and test the complete coefficient supremum uniformly in X with one common onset. This review establishes coverage only; the combined bound and its limiting ratio are not derived here. Signed transfer and actual-Xi positivity remain open.
REASON: Step27 separately approves the saved changed observable after inspecting source hypotheses and local specialization obligations; SPECIALIZE authorizes exactly one fixed-parameter application, not a new arithmetic theorem or another norm audit. No essential coverage is missing or persistently blocked.
LITERATURE_REASON: Changed conclusion from joint coefficient coercivity to projection of the specified bump; compare the translated numerator and full Hilbert-space supremum with ready source coverage before application. Reuse adequate sources rather than repeat unchanged searches.
SCOPE: Fixed L637 w,u0,psi,g and actual Hardy Z; T<=X<=2T, L=log T, N=floor(T^(1/5)), s=-1,+1; all moving complex coefficient pairs in the exact weighted L2 space. No changed length, shift set, bump, weight, numerical grid or signed-Xi assertion.

## Step26 nomination, preserved

The following nomination records the state before step27. Its pending
approval language is superseded only by the completed comparison below.

This record was written at the end of the step26 RESEARCH audit. It
does not approve or perform a second mathematical attempt. The next
turn is a source-scope comparison, using the ready assessments above
where they apply. There is no known persistent source-access blocker;
the pending gate concerns this changed conclusion, not a request to
retrieve the same documents again.

The main gap remains L030–L032/C032a actual-Xi all-degree mixed
positivity. Let V_(T,X) be the complex span of
Z(t+s/L)n^(-it), s in {-1,+1}, n<=N, in L2(w_XT dt), and let
Pi_(T,X) be its orthogonal projection. The proposed test asks whether

    sup_(T<=X<=2T) ||Pi_(T,X) g_(T,X)||_T^2 -> 0.

This is a target, not a proved limit. Its plausible downstream use
is to decide whether this precise enlarged dictionary can realize
the fixed microscopic bump to any fixed error below one. Even a
successful exclusion would leave other dictionaries, signed weighted
realization/transfer, and actual-Xi positivity unresolved.

Essential local mathematical inputs for the future application are
L933's actual norm (4), L637's fixed bump and undifferentiated Hardy
normalization, and L927 Section 3's numerator/projection argument for
comparison. L737 is provenance only. L928's arithmetic main form,
L925/L929/L930/L932 conclusions and cross-notebook results are not
needed inputs. Verify every change from the unshifted numerator,
including support after both shifts and uniformity in X. Preserve the
whole two-channel coefficient class throughout the supremum; do not
infer the joint statement from separate spans or assume a Gram inverse
before a valid norm estimate supplies it.

Continue only if the combined correlation estimate and the retained
joint denominator control that full supremum uniformly and tend to
zero, or supply a different informative decision on the stated test.
Otherwise record the exact unpaid estimate; an inadequate upper bound
is not a realization counterexample. End after this one fixed-parameter
test; no automatic length or shift enlargement is nominated. Full
matching Mathlib coverage remains unchecked. No novelty certification
or RH candidate is claimed.

## Completed source-scope comparison — step27, 9 November 2026

This is one LITERATURE / literature_comparison step, classification
NOVELTY_UNCHECKED, outcome EXPLORATION. It completes the separate gate
for the unchanged TARGET. It does not prove a projection theorem or
repeat L933's mathematical audit. Next invocation defaults to the
bounded mathematical application; another unchanged approval is not
needed. Full matching Mathlib coverage remains unchecked.

### Primary statement and precise specialization scope

Reopened Christopher Hughes, *Random matrix theory and the distribution
of the zeros of the Riemann zeta function*, LMS Summer School,
July2017, Theorem2.2, printed p18 (PDF page20), and the whole following
two-exponential-branch explanation, printed p19 (PDF page21), at the
URL in SOURCE_EVIDENCE. The statement is the undifferentiated formula
already quoted in L637(1), with the floor square-root cutoff and
O(v^(-1/4)) error for large positive real v. The following explanation
explicitly calls itself heuristic; it is not used to reprove the
error estimate. The rigorous theorem remains the named classical
Riemann–Siegel import, with Titchmarsh–Heath-Brown Section4.17,
(4.17.4), p89 as its book citation. The book was not newly retrieved.
No numerical examples, formula differentiation, contour argument or
complex-height extension is imported.

L927 Section3 and its separate audit already justify the unshifted
pointwise size input on comparable positive real intervals, including
cutoff crossings. The changed application evaluates the same function
at v=t+s/L for s=-1,+1. On the unchanged bump support
[a-1/(2L),a+1/(2L)], both heights remain in [T/2,4T] eventually,
uniformly in X: a=X+u0*T, u0 is fixed in (0,1), and the total
translation has magnitude at most 3/(2L). This is the source-domain
check, not a new correlation estimate. The cited theorem requires
no separation from zeros or cutoff heights. Its all-large-real-height
scope therefore covers these translations. The later numerator must
still be written for the full sum of the two polynomials.

The bump, its positive normalization, weight and linear-first-slot
inner product are exactly L637's and L927's. In particular shifting
Z does not shift g, w_XT or n^(-it). L927's existing weighted support
estimate and finite-polynomial Cauchy–Schwarz method are available;
their joint application must charge both coefficient channels rather
than treating one channel as fixed. All constants must depend only
on the fixed data, and every estimate must hold before taking a
supremum over T,X-dependent complex vectors.

L933(4) is an audited actual norm bound for exactly this joint U and
S=sum_(s,n)|c_(s,n)|^2 in the same weighted space. Its stronger first
bound and weaker second bound are both available; the application must
say which one it uses. No new shifted twisted-moment application,
Gram inverse, or full diagonal-metric contraction is needed. Its
existential onset and that for the numerator must be made common.
The finite-dimensional Hilbert projection theorem is standard; L927
Section3 already gives the elementary variational proof in this exact
complex weighted Hilbert convention. Reuse that argument for the
whole joint span. Independence, if needed in coefficient language,
comes from L933, not from presumed invertibility. No infinite-span
limit or nonuniform asymptotic is covered by this gate.

### Literature overlap, duplicates and failures

Reuse the searches actually recorded in the joint-dictionary scope
assessment (shifted twisted second moments, arbitrary coefficients,
and exact Hardy bump/joint projection terms). Its Pratt–Robles v3
Theorem1.2 and BCR references concern the arithmetic moment inputs,
not an imported joint projection theorem. Their arithmetic proof
cases need no further retrieval because L933's already audited
actual norm is the denominator here. This review changes the
observable; it does not reopen their moment specialization.

The longer-dictionary scope assessment's inspected paper41 v3
Theorems2/2a and Section9 (64)–(65) concern positive proportional
growing Laguerre orders and a different measure. Those hypotheses
exclude this fixed-Z dictionary. Reuse that recorded comparison;
no new retrieval or endpoint passage is claimed. The prior failure
to find an exact match is not evidence of novelty or exhaustive
literature absence. There is no reason to reprove the arithmetic
imports or the classical Riemann–Siegel theorem.

Read the short arithmetic projection stop, step11 termwise-modulus
Schur stop, step21 coherent-square inconclusive record, and step26
approval-loop closure. L927 settles only the single unshifted span;
two separate exclusions cannot control their joint span. Step11 loses
combined-term cancellation, and step21 leaves a collective surrogate
defect unpaid. Neither is a failure of this numerator/actual-norm
comparison. Step26 closes repeated norm approvals while retaining
the audited theorem. The changed observable uses that retained input
and does not require any stopped estimate to become true.

### Bounded application and decision rule

SPECIALIZE covers one application of the cited local framework and
audited norm. Keep exactly N=floor(T^(1/5)), the two shifts and fixed
bump. Seek a coefficient-uniform correlation-to-norm upper bound
tending to zero; use it on the entire projection supremum. Record
the actual powers, logarithms, normalization and common onset in a
canonical proof only during the subsequent research turn. No combined
inequality or exponent calculation is approved as already proved here.

Continue with this mechanism only if that full bound gives uniform
o(1), or yields an informative decision on the exact target. If it
does not, identify the precise unpaid estimate; an inadequate upper
bound is not an adverse vector or a realization counterexample.
End the fixed test without automatic length, shift or bump changes.
Its downstream use is deciding whether this particular dictionary
can realize the fixed bump to a fixed error below one. Signed
weighted realization/transfer, other dictionaries and L030–L032/C032a
actual-Xi mixed positivity remain independent gaps. No RH candidate
or mathematical advance beyond the inspected sources is claimed.
