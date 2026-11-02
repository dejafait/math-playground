# Exact-theta cumulative upper-defect source comparison

TARGET: Assess primary coverage for a theta-specific half-wave pairing bound on G(t)=integral_t^infinity A(u)du implying integral_0^infinity G(t)sin(xt)dt<=G(0)/x for every x>0, checking the recorded parity and signed-remainder failures.
CHECKED: 2026-10-31
DECISION: EXPLORE
SEARCH_EVIDENCE: Completed upper-bound, cumulative/associated-kernel and reflection searches recorded below; reused the three named assessments and inspected all three named failure records. No matching theta-specific sufficient bound was found; this bounded search establishes no novelty or nonexistence.
SOURCE_EVIDENCE: Read Csordas arXiv:1309.0055v2, 21 February 2014, Proposition 3.10 (3.15), Remark 3.11 and entire following proof, printed pp.8-9, in versioned HTML and PDF https://arxiv.org/pdf/1309.0055v2 ; compared Theorem 3.4 and its admissibility warning. Reused Tuck, Bull. Austral. Math. Soc. 74 (2006), 133-138, (3)-(10), https://doi.org/10.1017/S0004972700047511 , from the inspected exact-theta review and rechecked the publisher text.
COMPARISON: The source gives an equivalent upper bound at positive frequencies and a positive sine transform, not an independent theta upper estimate; its last proof line omits x and (3.15) needs a positive-frequency restriction. The full/half associated-kernel factor cancels homogeneously. L597 gives only a finite Cauchy sign.
GAP: No inspected theorem controls the signed upper defect. The separately nominated reflected complete-kernel majorant is untested: its sufficiency, full-tail certification and theta validity are not established here. Higher degrees remain open.
REASON: Park citation-only Proposition 3.10 and generic monotonicity; nominate one bounded obstruction test for a stronger pointwise condition retaining complete A, rather than repeating separate-parity or unsigned-remainder domination.
SCOPE: Completed literature-only comparison; no new mathematical result or calculation. The separate new continuation requires supervisor approval before execution.
LITERATURE_REASON: Essential primary proof cases and conventions for the changed cumulative upper-bound target were missing at turn start; the finite Cauchy audit and earlier three-mechanism comparison did not cover them.

## Relevance and exact object

Use the same real-axis A as L233 and L597, defined from L019's actual k
and its L239 even extension. G here is a newly proposed cumulative
kernel, not the Cauchy transform C_A or the holomorphic value A(iy).
This is a proposed review target, with no positivity conclusion.
L233 supplies integrability/moments; L597 imports decreasing shape but
ends after the second-y-derivative test. The quoted source criterion
is a lead to check, not an established new notebook result.

The main gap remains all-degree actual-Xi signs at unbounded heights.
A valid all-frequency first-sign bound would address a relevant part
of that gap, while higher degrees remain independent. Merely changing
the equivalent expression of the missing sign is not an advance.
Seek a theta-specific inequality on paired half-waves whose hypotheses
can be checked without assuming that sign. An explicit failing pair
can instead stop that proposed sufficient mechanism, without refuting RH.

## Required narrow comparison

Reuse `2026-10-31-complete-first-sign-mechanism-discovery.md` for the
unadopted Proposition 3.10 lead and the completed reciprocal/translate/
Hermite comparisons. Reuse
`2026-10-31-xi-specific-theta-sign-discovery.md` and
`2026-09-27-first-associated-theta-lattice.md` for known shape scope and
the theta parity comparison. Their existing search record does not
approve this changed upper-bound target.

Search the exact upper-bound/pairing claim locally before detailed
reads. Consult the relevant passages in
`ATTEMPTS/2026-10-03-complete-parity-positive-definiteness-test.md`,
`ATTEMPTS/2026-10-31-nonlocal-paired-tail-signed-remainder-stop.md`, and
`ATTEMPTS/2026-09-23-first-associated-autocorrelation-test.md` to exclude
duplicates. These are stop evidence, not mathematical premises.
Retrieve primary hypotheses and essential proof cases for any stronger
sine-transform or variation-diminishing theorem actually proposed.
Do not repeat the stopped separate-block certificate under a new name.
No cross-notebook input is proposed.

Continue only if the source comparison identifies an independently
checkable, theta-dependent sufficient pairing inequality or a concrete
obstruction test. Abandon this nomination if the only available input
is monotonicity, positive cumulative averages, a reformulated missing
Fourier sign, or an uncontrolled signed remainder. Preserve previous
stops and choose a different mechanism after such a negative review.
No justified creative proof attempt is ready until that discriminator
and its essential source coverage exist. Full Mathlib coverage is not
checked; no absence is claimed.

## Completed source comparison — 31 October 2026

In Proposition 3.10, the s integral is over the half-line; Theorem 3.5
uses the full line. For input k the former associated kernel is A/2,
and its cumulative kernel and initial mass are G/2 and G(0)/2.
Thus the local upper inequality has the same normalization. L597
already fixes the different theta scale; G is neither C_A nor A(iy).

The first integration-by-parts line on printed p.9 reads

    integral_0^infinity K_1(t)cos(xt)dt = Gbar(0) - x I(x).

The next line drops x. Also, (3.15)'s all-nonzero-frequency inequality
needs restriction to x>0: division by negative x reverses its direction.
Remark 3.11's entire half-wave proof supplies I(x)>0, not the needed
upper bound. Theorem 3.4 expressly warns that admissible kernels fail
its convexity premise. These source qualifications supply no new sign.

The full relevant PDF text and HTML agree; screenshot retrieval failed,
so no image-dependent claim is made. L233's full Fourier proof and
L597's real-axis normalization/shape were checked to identify the object
and its convergence context. No new positivity specialization is proved.

Tuck's (3)-(4), pp.134-135, likewise signs a sine transform under
monotonicity and a cosine transform under convexity. His (5)-(10),
pp.135-136, additionally need valid contour shifts and shifted shape
conditions, with distinct integrable-singularity and simple-pole cases.
Reuse the complete comparison in the exact-theta assessment: none of
these conditions is verified for A. Passing to G supplies no inspected
independent upper estimate. The publisher PDF was rechecked, without
repeating its already recorded full audit.

Two search leads were not adopted or inspected at theorem level:
Csordas-Varga, paper_180.pdf (snippet about repeated primitives of a
different kernel), and a boundary-correlation preprint indexed under
DOI 10.5281/zenodo.22069300 (strip criteria). Neither is evidence for
this signed bound or an essential input to the bounded test nominated
below. Search snippets and secondary answers are not theorem evidence.

## Failure screen and decision

Read all three required ATTEMPTS in full. L233 stops automatic weighted
autocorrelation positivity. L356's opposite parity tails stop separate
parity certificates: cancellation must remain inside A. L559's endpoint
and remainder stop disallows endpoint deletion and an unsigned growth
bound substituting for a needed signed estimate. These are comparisons,
not mathematical premises or bans on correlated mechanisms.

NEGATIVE: the completed comparison parks citation-only positivity;
it does not refute the upper bound or RH. No stronger sign than the
sources checked is claimed. No lemma, mathematical script, PROOF or
DAG was changed. Mathlib coverage remains unchecked.

The [reflected-majorant nomination](2026-10-31-associated-theta-reflected-majorant-test.md)
specifies a finite obstruction test that retains complete A and pairs
complementary positions inside each half-wave. Its sufficiency link and
sign are unproved here. A certified failing pair would stop that stronger
majorant; a finite positive scan would not prove an all-parameter sign.
This newly written continuation needs separate supervisor approval.
No justified creative all-height proof attempt is ready: independent
signed control remains missing, regardless of scheduling preferences.

## Search record

Actual queries included:

- `"sine transform" "upper bound" "decreasing" positive definite`;
- `"Csordas" "3.10" "kernel"`;
- `"theta" "half-wave" positivity sine transform`;
- `"sine transform" "convex" "Pólya" bound`;
- `"sine transform" "upper bound" monotone positive`;
- `"associated kernel" "sine" "bound" theta`;
- `"Fourier sine transform" "upper bound" decreasing convex`;
- `"positive definite" "cumulative" "Csordas"`;
- `"sine transform" "reflection" "bound" decreasing`.

Targeted folded/reflection-pair/cumulative searches in the relevant
associated/theta/first-sign local assessments and ATTEMPTS located no
identical tested majorant. No novelty inference follows. Reuse the
recorded reciprocal/translate/Hermite and theta-lattice comparisons;
no new search of those mechanisms was needed.
