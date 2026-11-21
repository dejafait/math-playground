# Asymmetric third-marginal phase test — nomination939, approval940

TARGET: Test whether separating two nearby frequencies from the third yields a rigorously negative open patch of Re M(a,b) along (a,b)=(r+1,r-1), using the full actual law at S=3B'(1).
CHECKED: 2026-11-14
DECISION: EXPLORE
SEARCH_EVIDENCE: Approval940 completed bounded exact reciprocal-Xi/asymmetric-marginal and complex oscillatory convolution searches, compared the named C466 inputs and stops927/932, and inspected primary nonnegative convolution results. No adequate matching phase/sign theorem was found; queries and limits below, without a novelty inference.
SOURCE_EVIDENCE: Reuse reviews930/933/935 and approval938 only for unchanged Fourier, bilinear and full-completion tools. Newly inspected Asmussen-Foss-Korshunov arXiv:1303.4709v1 Section3 definitions and Propositions6-7 with complete proofs pp9-11 https://arxiv.org/pdf/1303.4709v1; Matsui-Watanabe arXiv:2308.16727v1 Definitions1.1-1.2 and Lemma2.4 statement pp1-4 https://arxiv.org/pdf/2308.16727v1. Hypotheses and exclusions below.
COMPARISON: Known nonnegative convolution asymptotics do not import this complex product's sign. Ready inversion and full-h estimates permit one analytic attempt; opposed-slice domination and phase cancellation require new justification on this ray. No asymmetric limit, leading coefficient or negative value is established.
GAP: Mathematical obligations are all competing moving-frequency regions, uniform normalized integral control, a nonzero leading coefficient with controlled phase, and an actual negative value with nonzero Vandermonde. Full integral signs, higher orders/all x and Xi transfer remain independent gaps. No essential source-access gap blocks the qualified attempt.
REASON: Separate literature approval940 completes nomination939 for the identical TARGET and SCOPE. Ready tools and the new bounded comparison support EXPLORE, not IMPORT or a sign theorem. The next turn should perform this one creative test; no further literature gate is nominated here.
SCOPE: C466l's actual M at p=theta_1, x=B'(1), S=3x, on the original Re(z)=1 line, with fixed offsets (r+1,r-1,-2r) and r tending to positive infinity. Retain C466a's external qualifications and all phase factors; no RH, PF-infinity, new source version, finite-core replacement or conditional independence.
LITERATURE_REASON: Nomination939 changed the opposed-slice geometry to an asymmetric cluster and explicitly lacked exact-target comparison. This separate approval completes that source gate, reusing ready representation and completion coverage.

## Relevance and bounded test

The following nomination paragraphs preserve their step939 gate status
as provenance. Approval940 below supersedes that status for the unchanged
target only.

The main gap remains L030-L032/C032a actual-Xi all-degree algebraic-square
positivity. This target tests a proposed sufficient pointwise sign in
C466l's real two-frequency determinant representation. A rigorously
negative open patch would rule out that sufficient sign mechanism,
while leaving the sign of the full weighted integral, global density
minors and Xi transfer unresolved. It would not disprove RH.

The candidate is to isolate the part of the original integral where
the two nearby frequencies are small, retain the distant factor's
complex phase, and determine whether that phase can produce a negative
real marginal. The bounded discriminator is one rigorously justified
negative value on the specified ray, together with the continuity and
nonzero Vandermonde conditions needed for an open patch. An asymptotic
route must pay every competing moving-frequency region and prove a
nonvanishing leading coefficient and controlled phase error. Stop the
attempt at the first unpaid domination, phase, or sign condition if
that discriminator cannot be justified. No such calculation, limiting
identity or negative value has been derived in nomination939.

## Comparison and source gate

Stop927 excludes simultaneous scalar and pairwise pointwise phases on
a regular common product contour; this proposal uses cancellation on
the original line. Stop932 excludes conditional iid factorization;
the proposed test keeps the full dependent law. C466j's chamber-generator
minimum-principle stop concerns a different object. The local searches
found no theorem resolving this exact ray, but they are not a complete
literature assessment. C466m/n do not authorize a new asymmetric proof.

The separate review should first retrieve precise primary hypotheses
and relevant proof cases for any claimed asymmetric convolution or
moving-frequency theorem, compare with the actual full-h growth and
complex phases, and check exact-statement duplicates/obstructions.
Reuse existing inversion and completion coverage where unchanged;
do not reprove those known identities. If no adequate theorem is found,
record the bounded search and exact uncovered difference honestly.
This nomination remains REVIEW_REQUIRED and authorizes no calculation.

If source coverage later permits this mechanism, its intended purpose
is proof_attempt/creative (deep_research/max), rather than another
opposed-slice specialization: the critical claim is whether asymmetric
phase survival obstructs full-marginal positivity, a sufficient route
toward the main gap. The fixed ray and negative-open-patch criterion
are the bounded test. Source coverage must precede that attempt; the
current routing is literature_comparison, standard/high. Full matching
Mathlib coverage is unchecked, not known absent.

## Separate source approval940 — 14 November 2026

This is one literature-only comparison of the prior nomination, not a
proof attempt. Its TARGET, main gap and bounded negative-open-patch test
are unchanged. No new limit, sign, lemma or mathematical script was
produced. A target-specific estimate still to be proved is a research
obligation, not an inaccessible theorem being silently assumed.

### Inspected primary comparisons

Asmussen, Foss and Korshunov, *Asymptotics for sums of random variables
with local subexponential behaviour*, J. Theoret. Probab.16 (2003),
489-518; [arXiv:1303.4709v1, 19 March 2013, Section3, pp9-11](https://arxiv.org/pdf/1303.4709v1).
Read the definitions and complete proofs of Propositions6-7. A long-tailed
density is bounded on its tail, eventually positive, with f(x+t)/f(x)
tending uniformly to 1 for t in [0,1]. Subexponentiality for a
distribution on R+ further requires f*f(x)~2f(x). Proposition6
characterizes this using a negligible middle integral and a diverging
cutoff with uniform shift control. Proposition7 assumes subexponential
f and probability densities f1,f2 on the same half-line, with fi/f
tending to ci>=0, and concludes (f1*f2)/f tends to c1+c2. Its proof
pays both endpoints and bounds the middle by Proposition6. These are
nonnegative density results. Neither complex F nor its shifted product
has those stated input types. Modulus replacement loses the phase.
No asymptotic or sign is imported from these propositions.

Matsui and Watanabe, *On convolution closure properties of
subexponentiality approaching from densities*,
[arXiv:2308.16727v1, 31 August 2023, pp1-4, Definitions1.1-1.2 and Lemma2.4](https://arxiv.org/pdf/2308.16727v1).
This two-sided extension still concerns nonnegative probability densities.
Lemma2.4 assumes long-tailed f,g and a subexponential probability mixture
pf+(1-p)g; it concludes f*g~f+g. Its additional almost-decreasing or
negative-tail bound is needed for its stated subexponential closure
conclusion. The statement and definitions already exclude direct
application to complex F; its proof and counterexamples were not read
or used. The 2025 publication is a lead, without presumed version
equivalence or additional imported claims.

These supplement review933's inspected Finkelshtein-Tkachov nonnegative
kernel and Omey-Segers compact positive-dilation results. No cited
theorem pays this ray's complex phase or moving-frequency domination.
No reproof or extension of those theorems is authorized by this review.

### Reused tools and local comparison

Review930/recovery931 in
`2026-11-14-third-marginal-full-law-test-930.md` already inspected
[Heil, Fall2009, Theorem1.23, pp16-17](https://heil.math.gatech.edu/7338/fall09/convolution.pdf),
[Jerison, Fall2013, Corollary4/Proposition2/Theorem2, pp2-4](https://math.mit.edu/~jerison/103/handouts/fourierint1.13.pdf),
and [Ruzza, 4May2022, Lemma3.1.1, pp27-28](https://webpages.ciencias.ulisboa.pt/~gruzza/introRMT.pdf).
Reuse that complex L1 convolution, inversion and bilinear coverage with
its absolute cross-product, L1/L2 and continuous-version qualifications.
It does not preserve signs. C466l(1) and its continuity proof establish
the relation of M to the third density minor. Any new asymmetric
specialization must retain constants, complex phases and pointwise
evaluation; cite the identities rather than reprove them.

Review935 in `2026-11-14-third-marginal-effective-tail-nomination-934.md`
already covers [DLMF5.11.1/5.11(ii)](https://dlmf.nist.gov/5.11), the
analytic log-Gamma branch and explicit value remainder, and
[DLMF25.2.1/6/7](https://dlmf.nist.gov/25.2), the absolutely convergent
zeta/Euler series for Re(s)>1. Reuse these tools and the canonical
C466k(4),(6),(7), C466l(9)-(22), C466m full-function expansion only
within their justified domains. Value errors cannot be differentiated
without justification. The audited C466m/n opposed-slice bound supplies
no asymmetric majorant. No new special-function source is essential
for an analytic attempt. A numerical witness would require effective
enclosure coverage before implementation.

The narrow local comparison read C466a's density hypotheses,
C466k's fixed-line estimates, C466l's representations and tail proof,
C466m's expansion, named reviews930/933/935/938 and stops927/932.
Literal asymmetric/nearby-frequency searches in the specific C466l/m/n
and assessment paths found no established matching ray statement.
This was not an exhaustive notebook search or a novelty certification.
The common-product scalar/pair phase obstruction and conditional
iid-mixture support obstruction remain unchanged. The present mechanism
uses cancellation on the original line and the full dependent law;
neither stopped premise is reopened. C466j's chamber mechanism is a
recorded contrast, not a mathematical input.

### Bounded search and evidence limits

Queries actually run included:
`"reciprocal xi" "marginal" "asymmetric"`,
`"reciprocal" "Xi" "three" marginal positivity Fourier`,
`"reciprocal xi" "Fourier" "positivity"`,
`"complex valued" convolution "subexponential" asymptotic`,
`"complex-valued" "convolution" "long-tailed"`,
`"convolution" "oscillatory" "stretched exponential" asymptotics`,
`"convolution" "oscillatory" "Weibull" asymptotic`,
`"complex" "subexponential densities"`,
`"subexponential" densities convolution Asmussen Foss Korshunov theorem pdf`,
`"Convolution closure properties of subexponential densities" arxiv`, and
`"triple product" "Fourier" "characteristic function" "negative" conditional sum`.
No inspected theorem supplies this ray's complex asymptotic or actual
negative patch. Unrelated xi notation, product convolutions and secondary
hits were not theorem evidence. DLMF2.4's fixed-phase integral setup was
briefly screened; its full hypotheses/proof were not inspected and no
saddle theorem is imported. No named essential source remains blocked.
A bounded search failure neither certifies originality nor predicts
whether the proposed test succeeds.

### Approved one-attempt boundary

The exact TARGET is now EXPLORE after this separate approval of
nomination939; no new continuation assessment is introduced. Reuse
ready coverage next turn. The analysis must pay every moving
frequency-zero neighborhood and the unbounded complement, keep the
complex phase, and justify integral limits sufficiently for a sign
inference. A fixed-t limit or modulus comparison alone cannot pass.
Prove nonvanishing and the phase of a proposed leading coefficient,
rather than assuming that it is positive or nonzero.

The discriminator is a rigorous negative value on the specified ray,
with C466l continuity and nonzero Vandermonde giving an open patch.
If domination, a competing contribution, coefficient nonvanishing or
phase control remains unpaid after one bounded attempt, preserve the
first gap and stop that attempt. An informative obstruction may change
the route; repetition requires new input or a refined discriminating
test. A negative patch rejects pointwise marginal nonnegativity, without
signing the full integral, refuting a density minor or disproving RH.
All-ray positivity would still leave the two-frequency domain, all
orders/all x and Xi transfer unresolved.

Retain C466a's version-specific density/counting/low-zero qualifications;
no external certificate was replayed. Essential continuation inputs are
C466a/C466k/C466l/C466m/C466n; L030-L032/C032a remain unresolved.
Full matching Mathlib coverage is unchecked, not known absent. Route
the next turn as proof_attempt/creative, deep_research/max: the new
bounded mechanism asks whether asymmetric phase survival obstructs a
sufficient pointwise sign route related to the main gap. This approval
is source preparation, not a mathematical advance beyond checked work.
