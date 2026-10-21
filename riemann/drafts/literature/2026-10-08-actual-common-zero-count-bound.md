# Completed bounded source comparison for actual common-zero counts

TARGET: Assess whether known arithmetic results give N_common([H,T])=o(sqrt(log log T)) for the exact actual F_0,G pair of L366 at fixed sufficiently large H.
CHECKED: 2026-10-08
DECISION: EXPLORE
SEARCH_EVIDENCE: Bounded exact-pair/coincidence, Gram-point nonvanishing and shifted-projection pair-correlation searches on 2026-10-08; scoped local duplicate/failure checks found no matching count theorem in inspected sources; queries below.
SOURCE_EVIDENCE: Reused saved Lagarias/Li coverage; inspected Kalpokas–Steuding arXiv:0907.1910v1 pp. 2–5, Theorems 1–2 and Corollary 5 with its complete proof p. 12; Korolev arXiv:1106.0516v2 definitions pp. 1–3, parameter conventions p. 7 and Theorem 1/proof opening p. 11; Das–Ismoilov–Ramos arXiv:2502.05106v1 §1.6.3 Corollary 10/application; NIST DLMF 25.10.1–3 and stated remainder, version 1.2.8.
COMPARISON: Fixed-angle Gram-grid moments and nonvanishing lower bounds do not control the variable arithmetic response grid; the inspected pair-correlation corollary assumes RH and treats another sequence. None supplies the requested distinct-coincidence scale by an identified specialization.
GAP: Actual N_common=o(sqrt(log log T)) and its falsity remain unproved; the exact-grid critical-line sampling margin is missing. No literature-wide absence claim is made.
REASON: One bounded primary-source comparison is complete; park direct theorem import and select an arithmetic remainder-margin test retaining the exact response grid, with separate next-turn approval.
SCOPE: Fixed real-frequency functions in L366 (1), with distinct common zeros on closed [H,T]; no RH, simplicity of F_0 zeros, common ODE, or discriminant premise assumed for the proposed arithmetic bound.

This literature-only review completes bounded coverage, not the count
bound. Outcome: EXPLORATION; no new mathematics, lemma or script.

LITERATURE_REASON: The requested quantitative coincidence scale was outside the earlier eventual-disjointness assessment; the newly inspected Gram-grid and pair-correlation comparisons address that changed conclusion.

The exact pair, quoted from L366 as recorded in the earlier assessment,
is F_0(t)=2 xi_c(1/2+it) and
G(t)=−(t²+1/4) Re[xi_c(5/2+it)/(5/2+it)].
The count is of distinct simultaneous real zeros; complex nonvanishing
on Re s=5/2 does not imply nonvanishing of this real projection.

Essential local inputs for the proposed review are L366's exact pair,
L372's response phase/count statement, L377's signed deficit statement
and audited L378's conditional count loss. Read only their relevant
definitions/statements initially. No cross-notebook input is proposed.
L371/L373 rule out constant loss without common-zero accounting;
L375/L376 exclude an inference from the tested generic exact-shift
geometry. Reuse these failures without repeating their constructions.
The prior actual-disjointness assessment inspected Lagarias and Li for
different projection pairs; their hypotheses must not be conflated
with the present pair. Do not repeat those reads unless a precise
new application requires an essential unread proof case.

Main gap remains actual-theta mixed positivity and the total L367 signed
margin. The possible downstream use of this bound is a comparison with
L377's sqrt(log log T) negative count excursions through L378, conditional
on eventual actual D≤0. The latter is independently unproved. No such
application or new mathematical implication is derived here.

Continuation test: find an unconditional primary statement controlling
this exact coincidence count at the stated scale, or identify a concrete
arithmetic subtarget with separately assessed coverage. Compare exact
hypotheses and growth rates, not just terminology. If available results
only compare components of one shifted function, assume RH/noncoincidence,
or allow much larger exceptional counts, record that mismatch and park
the direct import. A persistent source blocker requires a different
independently testable target. Do not replace the target by another
generic geometric counterexample. No historical novelty is asserted;
matching Mathlib coverage has not been checked.

## Primary statements and applicability

Justas Kalpokas and Jörn Steuding, *On the value-distribution of the
Riemann zeta-function on the critical line*,
[arXiv:0907.1910v1](https://arxiv.org/pdf/0907.1910v1), 10 July 2009,
printed pp. 2–5: their grid has fixed φ∈[0,π) and
Δ(1/2+it)=exp(2iφ). Theorems 1–2 count this grid and evaluate
discrete moments. Corollary 5, p. 5, gives at least
2 cos²(φ)T/π nonzero samples for φ≠π/2, and no nontrivial bound
in the remaining case. Read its complete §4.3 proof, p. 12:
Cauchy–Schwarz uses the first and second moments; zero samples
contribute nothing. It does not count them. The discussion on p. 2
leaves fixed-angle coincidences unresolved in that source. A lower
bound of order T for nonzero samples among order T log T samples
does not furnish the requested tiny coincidence upper bound. L372's
phase includes Im log ζ(5/2+it) and the variable carrier b, whereas
φ here is constant. No grid replacement is justified. This historical
discussion does not assert the state of all literature in 2026.

M. A. Korolev, *Gram's Law and the Argument of the Riemann Zeta
Function*, [arXiv:1106.0516v2](https://arxiv.org/pdf/1106.0516v2),
26 June 2011: read the ordinary-Gram definitions and coincidence
qualification, printed pp. 1–3; followed the nonvanishing reference
to the preceding primary paper. Inspected Theorem 1, p. 11, and
global conventions, p. 7: 0<ε<10⁻³, N sufficiently large,
N^(27/82+0.9ε)≤M≤N^(27/82+ε), integers k≥1 and
k ε⁻¹ exp(λk²)≤m≤c log N, λ=(2Beπ²)², B as in Lemma 5,
c sufficiently small. It evaluates moments of S differences at
ordinary Gram points. The proof opening uses their spacing and a
prime-polynomial approximation. Neither the statement nor this
opening controls exact coincidences on the response grid. The full
moment proof was not read and is not imported. Interval occupancy
is not exact coincidence counting.

M. K. Das, T. Ismoilov and A. P. Ramos, *Fourier optimization and
pair correlation problems*,
[arXiv:2502.05106v1, §1.6.3](https://arxiv.org/html/2502.05106v1#S1.SS6.SSS3):
identifier dated 7 February 2025; retrieved HTML internally dated
24 August 2026 (version discrepancy recorded). Read the full
application through Corollary 10 and its conjecture comparison.
Corollary 10 assumes RH, fixed θ∈[0,2π), a=1/2−c/log T,
c≥0, and zeros of f_a(w,θ)=ζ(a+w)+exp(iθ)ζ(a−w) on Re w=0.
It bounds long averages of that sequence's form factor, with stated
interval restrictions. Its application argument uses a cited
single-sequence form-factor asymptotic, not a mixed-sequence zero
count. Thus it is neither unconditional nor a theorem about our
right-line divided projection. The original Gonek–Ki manuscript
endpoint again returned HTTP 403; its full theorem and proof remain
unread. This branch is comparison evidence, not an essential premise
or a substitute for primary coverage of Gonek–Ki.

[NIST DLMF §25.10](https://dlmf.nist.gov/25.10#E3), version 1.2.8,
15 September 2026, equations 25.10.1–3, cites Titchmarsh,
*The Theory of the Riemann Zeta-function*, second edition (1986),
§4.17, (4.17.2)/(4.17.4), p. 89. Read the Hardy transform and
gamma phase, the cosine sum with exact
m=floor(sqrt(t/(2π))), and R(t)=O(t^(−1/4)) as t→+∞.
This unconditional formula supplies a sampling representation,
not a nonvanishing margin. Its unevaluated remainder constant
suffices for an asymptotic comparison only. The displayed leading
correction with a potentially vanishing denominator is unnecessary
and is not used. Phase branches must be reconciled with L372 in a
later specialization. No such specialization is derived here.

## Search, reuse and decision

Queries included `Riemann zeta xi common zeros shifted real part Gram
points coincidence zeros count`, `Gonek Ki Pair correlation zeros
real imaginary Riemann xi function theorem common zeros`, `zeta zeros
Gram points count exact coincidences zero at Gram point`, `zeta shifted
common zeros count`, `Korolev Gram's law and the argument arxiv`,
`Kalpokas Steuding value distribution critical line arxiv`, and
`Riemann common zeros 5/2 1/2`. Search hits are not theorem evidence.
Other discrete-value-distribution hits remain unread leads. No novelty
is inferred from this bounded search. The published Korolev endpoint
failed HTTP 502; the accessible author arXiv version supplied the
specific inspected statements instead. No essential source blocker
remains for the bounded continuation below.

Read L366 (1), L372's phase/count definitions through (9), L377's
conclusion and cited deficit scale, and L378's hypotheses/conclusion.
Reuse the saved Lagarias/Li comparison without repeating its proof
reads. Scoped failure reads preserve L371/L373 and L376; L375 is
retained from the overview and earlier assessment. Scoped searches
in L366–L378, the response/count assessments and actual-disjointness
history found no recorded exact-grid Riemann–Siegel margin test.
L370 and the earlier discriminant-mean assessment were read narrowly
to avoid reopening their parked source-dependent mean route.
No cross-notebook input was read.

Park direct import of the requested count bound. The separately
assessed continuation tests a full Riemann–Siegel remainder margin
at the exact G phase levels:
`drafts/literature/2026-10-08-response-grid-remainder-margin.md`.
This is an arithmetic certificate test, not another geometry example.
It must retain every finite-sum term and the actual Euler-log phase.
A certificate failure would not refute the count bound. No margin,
sampling inequality, count consequence or sign was proved in this turn.
Actual D≤0, total margin, remaining low-index signs, heights above
forty and endpoint margin remain unresolved. Newly written coverage
receives separate supervisor approval next turn.
