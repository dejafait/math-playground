# Real subdiagonal scale comparison: nomination1232/review1233

TARGET: Establish or refute beta_(i,0)(t)>=beta_(i,0)(x)/2 for every 3*x/4<=t<=x in C030r's fixed real-reference family, uniformly for x>0, m>=1, n>=max(4,2m), 1<=i<d<=floor(n/2), positive a_l,r and all real-rate contrasts.
CHECKED: 2026-11-17
DECISION: EXPLORE
SEARCH_EVIDENCE: Review1233 completed the bounded exact/stronger-result and obstruction searches listed below, including finite exponential convolutions, Hirschman-Widder/hypoexponential densities, derivative-Hankel ratios, signed Toda and exponential B-splines; no matching theorem or admissible counterexample was located in the inspected coverage.
SOURCE_EVIDENCE: Reused1228/1229 and C030r; refreshed Sra author-v3 C.5/(C.9), pp22-23, C.6/(C.10) and coalescence case, pp23-24, C.9/(C.18)/(C.22), pp27-28, via arXiv2611.02944v1; inspected Belton-Guillot-Khare-Putinar arXiv2101.02129v2 Propositions2.1 and2.14 with proofs, pp6-7,15-16; source scope and access details below.
COMPARISON: Sra's pointwise beta upper bound and moving-frame theorem do not state the required two-time lower comparison; the latter also has an additional degree condition. Hirschman-Widder existence/PF and probability identifications cover the real density, not monotonicity of its derivative-Hankel coefficient. Positive-measure recurrence theorems still require an absent functional identification.
GAP: The uniform half-value comparison on [3*x/4,x] remains unproved and unrefuted; no source import closes it, and C030t's conditional implication remains pending audit.
REASON: Essential source comparison is complete for one bounded attempt on the unchanged target after the supervisor's separate approval of this newly ready assessment; EXPLORE permits investigation, not an assertion of novelty, monotonicity or the target's truth.
SCOPE: All rates are fixed as t varies; the reference replaces every b_l by zero and has rates (a_1,a_1,...,a_m,a_m,r,...,r), with repeated rates, n=2m, every real contrast and both interval endpoints included; the coefficient is the positive square root of C030r's signed derivative-Hankel ratio.
LITERATURE_REASON: The target changes from the assessed complex phase perturbation to an essential, previously unassessed real-coefficient scale-comparison premise; exact theorem hypotheses and known obstructions must be checked before attempting it.

## Relevance and the bounded test

The main RH gap remains L030-L032/C032a actual-Xi positivity in every
degree. C030q and C030r provide the finite response and actual moving
basis. The conditional reduction
[C030t](../../lemmas/C030t-conditional-subdiagonal-bound-from-real-scale-comparison.md)
would turn TARGET into the full absolute phase comparison with constant
28. That reduction awaits independent audit; it is motivation for this
source review, not authority to assume TARGET. Finite evolution norms,
real-reference evolution hypotheses, actual-Xi supply, degree/time,
complement payment, signing and graph realization remain unresolved.

The source review should seek an exact match or a stronger real-coefficient
monotonicity theorem, including any finite-exponential-convolution,
derivative-Hankel, signed Toda or variation-diminishing terminology that
actually applies. These are proposed search directions, not sources
already read. Positive-measure orthogonal-polynomial theorems cannot be
transferred to the alternating signed derivative functional without a
proved identification. Arbitrary real-rate contrasts and the actual
coefficient normalization must be retained.

The existing assessed variance upper bound has the wrong direction for
TARGET. A theorem giving beta_(i,0) nonincreasing in t would suffice, but
neither that statement nor any stronger logarithmic derivative estimate
has been proved here. No new mathematical script or attempt on TARGET
is authorized by this nomination.

Continue after a precise imported theorem, a justified specialization,
or a bounded search establishing readiness for an independent test.
A rigorous admissible fixed-rate example with t in [3*x/4,x] and
beta_(i,0)(t)<beta_(i,0)(x)/2 refutes TARGET. It would not refute every
constant c>0 in C030t or the original complex phase comparison. Finite
samples cannot certify the universal lower bound. No generic real
coefficient lower bound, complex variance positivity or shared rank
normalizer may be assumed.

## Existing evidence to retain

Reused source assessment1228 and the full scope of stops1117/1181/1193/
1200/1107 remain unchanged. C030s's large-multiplicity partial comparison
remains pending audit. The joint compression-moment sufficient route is
parked, not disproved, as recorded in
[attempt1232](../../ATTEMPTS/2026-11-17-paired-compression-joint-route-unpaid-1232.md).
This real-scale comparison is a different independently testable premise.
Mathlib matching is unchecked, not absent. No cross-notebook input is used.

At nomination1232 this file was REVIEW_REQUIRED and approved no new
mathematics or source import. The separate review1233 below changes only
source readiness; the target and scope remain unchanged.

## Completed literature-only review1233

17 November 2026. No new mathematical statement, specialization,
counterexample, lemma or mathematical script was derived. This is an
EXPLORATION outcome: a bounded source screen, not a mathematical advance.

### Local duplication and failure checks

Read C030r in full and the conditional C030t, including its exact
derivative-Hankel identity and the role of the additional hypothesis (H).
Reused assessment1228/review1229 for unchanged finite-basis, positive-
measure sensitivity and complex-Toda coverage. Targeted searches in
C030q-r, the paired working notes, paired assessments and C030 lemmas
located the unproved premise and explicit exclusions, not a completed
real-scale theorem. This is a scoped duplicate check, not an originality
claim for the notebook or literature.

Read the short stop records1117/1181/1193/1200/1107 and the parked joint
compression attempt1232. None supplies this two-time estimate or an
admissible counterexample to it. Those stops concern automatic transfers
or different unpaid premises and retain their original scope. C030s's
multiplicity estimate and working1231's joint-moment diagnostic remain
distinct from this test. Unfinished work1218 is untouched.

### Primary theorem comparison

**Exact finite reference.** S. Sra, *On some positivity properties of the
Riemann Xi function*, author-v3, 2 November 2026, also
[arXiv2611.02944v1](https://arxiv.org/pdf/2611.02944v1).
Refreshed C.5/(C.9), pp22-23; C.6/(C.10), pp23-24, including its
repeated-rate continuity case; and C.9/(C.18)/(C.22), pp27-28.
Positive real rates, including repeats, are covered. Equation (C.22)
identifies the positive squared subdiagonal with minus the second
logarithmic derivative and bounds it above by i(n-i)/t^2.
C.9's moving-frame conclusion additionally requires
n>=2d and (n-2d+1)/2>=sqrt((d-1)(n-d+1)), with source m renamed d;
n>=8d suffices. TARGET does not impose the second restriction.
These statements give no lower comparison between two times.
The upper bound alone is not a lower relative bound.
Reused1229's comparison of C.8 and the moving-basis proof; no new
rank-derivative or coefficient-monotonicity inference is made.

**Classical density identification.** A. Belton, D. Guillot, A. Khare
and M. Putinar, *Hirschman-Widder densities*,
[arXiv2101.02129v2](https://arxiv.org/pdf/2101.02129v2), 9 April 2022;
Applied and Computational Harmonic Analysis60 (2022), 396-425,
DOI10.1016/j.acha.2022.04.002. Read Propositions2.1 and2.14 and their
proofs, pp6-7 and15-16. The first covers nonzero real scales, including
repeats; the second positive scales. Their construction is the
convolution of scaled one-sided exponential densities. Matching the
scale list to reciprocals of C030r's real rates identifies the density
family directly, with no distinct-rate limit or new theorem needed.
Their conclusions are existence, PF, support and probability
identifications, not the proposed time comparison. The inspected
Hankel discussion after (2.16), pp19-20, concerns integrated moments;
it is not C030r's derivative functional. No matching coefficient
monotonicity statement was located. Source identification is reused as
context, not recorded as a new canonical import.

The positive-measure sensitivity framework and oscillatory Toda
identities assessed in review1229 remain mismatched in functional or
conclusion; their exact citations and read qualifications remain there.
Neither positivity of the density nor a formal Toda identity supplies
the missing uniform comparison without another argument. No generic
monotonicity counterexample has been transferred into this family.

### Search and access record

Target-specific queries issued during this turn:

- `"exponential convolution" "Toda" monotonicity`
- `"Hankel" "recurrence coefficients" "monotonicity" convolution`
- `"Sra" "Xi" "beta" "variance"`
- `"hypoexponential" "Hankel" monotonicity`
- `"Hirschman" "Widder" "log" "concavity"`
- `"exponential convolutions" "monotone"`
- `"Hankel" "Toda" "monotonicity" "coefficients"`
- `"hypoexponential" "logarithmic" "derivative"`
- `"Hankel" "negative Toda" exponential`
- `"Hirschman-Widder" "monotonicity"`
- `"exponential convolution" "log-concavity" curvature`
- `"signed Toda" "monotonicity"`
- `"hypoexponential" "log-concavity" derivative monotonicity`
- `"Hirschman Widder" "curvature"`
- `"hypoexponential" "third derivative"`
- `"finite exponential" "Hankel" monotonicity`
- `"derivative Hankel" "monotonicity"`
- `"exponential B-splines" "Wronskian" monotonicity`
- `"Hankel determinant ratios" "monotonicity" exponential`
- `"finite convolution" "recurrence coefficients"`
- `"hypoexponential" "logarithmic curvature"`

Access queries also located the Sra author version page and the
Hirschman-Widder arXiv record. Within-source searches for `monoton`
found no match in these two PDFs; `Hankel` in the latter located the
integrated-moment discussion just distinguished. These searches are
not a proof that no stronger result exists.

The direct Sra PDF failed through web access; its author page identifies
author-v3 with arXiv2611.02944v1, whose relevant text was accessible.
The Elsevier DOI redirect failed; arXiv2101.02129v2 supplied the
Hirschman-Widder statements and proofs. Screenshot calls exposed no
inspectable page images and supplied no evidence. A shell PDF download
failed DNS resolution and produced no retained source file. None of
these failures blocks the inspected theorem comparison.

Searches surfaced spline existence, rational-transform classification,
hazard-rate preservation, structured reconstruction and asymptotic
orthogonal-polynomial leads. Their full theorems were not read, imported,
or claimed to be excluded; search snippets are not theorem evidence.
No essential matching source was identified but left inaccessible.
Mathlib matching remains unchecked, not absent. No cross-notebook input.

### Bounded continuation after separate approval

Preserve TARGET exactly. A later attempt may use C030r's actual real
determinants and C030q's existing response/floor; C030t motivates the
threshold but is still conditional and unaudited. Do not assume its
premise or reprove the known determinant construction as an advance.
Keep rates fixed while comparing times. Retain repeated rates, n=2m,
every real contrast, all allowed ranks and both endpoints.

The discriminating test is a proof of the uniform half-value comparison
or a rigorous admissible violation; numerical samples alone prove
neither. An estimate restricted by rate spread, degree, rank or a fixed
family does not establish TARGET. A violation rejects the half-value
premise only, leaving other positive constants and the full complex
phase bound open. Existing exploration usage is not reset by this
literature turn. Newly ready coverage requires separate supervisor
approval before research. No justified central creative target has
been prepared: the independent actual-Xi signed input and its essential
coverage remain missing. The proposed work is established-route
development, not a creative RH mechanism.
