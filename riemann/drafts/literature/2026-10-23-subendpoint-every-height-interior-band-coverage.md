# Coverage review: every-height interior subendpoint band

TARGET: Attempt to transfer C455a to every sufficiently large real a and every integer n with (249/1024)log(a/(2π))≤n≤(251/1024)log(a/(2π)), using the exact implicit saddle parameter and retaining the pinned external premise.
CHECKED: 2026-10-23
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Scoped local searches compared C455a, L269, L296 and L453, the ready rounded-endpoint assessment, and recorded L323/L327/fixed-r phase failures; no already stated exact band was located. Web queries were "Riemann Xi" "Laguerre" "logarithmic" inequalities and "generalized Laguerre" "249/1024"; no inspected matching theorem was found. This is bounded coverage, not a novelty claim.
SOURCE_EVIDENCE: Read C455a's complete statement, proof and separate audit; L454/L455 hypotheses and conclusions; L269's saddle existence argument and parameterwise contour justification; L296's exact monotone parameter-map proof; L453 Section 1. Reused the rounded-endpoint primary-source comparison and refreshed Csordas 1309.0055v2 Theorems 3.5/3.7, Lemma 3.6 and their proofs. Precise citations, qualifications and an unread new lead appear below.
COMPARISON: C455a already gives one uniform onset for positive real r and every admissible even m, with full error and normalization. The stated real-height/index rectangle is not its explicit conclusion. Existing exact saddle and monotone-map arguments supply the tools for testing inclusion without extending any analytic estimate; L453's different one-index result and L296's h>5 sign cannot simply be imported.
GAP: Prove exact saddle existence, uniqueness and uniform inclusion in C455a for every requested a,n; transfer its real-r onset to one real-height onset and retain its full P, B and error. These parameter claims and the new every-height sign remain unproved by this review.
REASON: Essential theorem/scope comparison is complete for one bounded known-method specialization attempt. A matching sign statement cannot replace the parameter argument, but no new Mellin, sector, zero-free or phase-return mechanism is needed within the approved scope.
SCOPE: One conditional transfer attempt for the exact stated interior logarithmic-index band using C455a and the existing exact saddle conversion only; no changed arithmetic/sector band, fixed-r arbitrary-height assertion, external-proof audit or initial-segment completion.
LITERATURE_REASON: The saved continuation changes the coupled-domain quantifiers to an every-height rectangle; its exact implicit-parameter inclusion was outside the prior assembly audit. This review reuses the adequate analytic-source assessments rather than repeating their research.

## Proposed continuation and decision test

The main gap remains global mixed positivity and the initial low-index
segment. An every-height interior band could clarify how the audited
coupled result compares with the height-dependent witness range, without
asserting that the initial segment is covered. This is a proposed target,
not a derived theorem or a claim of novelty.

Essential input C455a retains L454/L455 and the precise September 30,
2026 Theorem 1.1 at commit
`1581d4cbdd69a0faf34b2089614fe2a814316a6a`, with the same
unaudited external manuscript and formal import closure. L269 supplies
the parameterwise saddle-equation precedent; its proportional-index
asymptotic must not be applied outside its hypotheses. L453 is a
comparison, not an asserted theorem for the proposed band.

The eventual test is whether every specified a,n has an exact admissible
r, with m=2n, in C455a's closed band beyond one common height. Retain
the full sum, non-Euler B lower bound and exact P; an approximate
equality of heights does not suffice. Continue only if that uniform
parameter transfer is justified by the assessed tools; otherwise record
the exact failed inclusion or quantifier. Do not extend source mechanisms
within this target. L323/L327 and fixed-r/arbitrary-phase negative
examples retain their scopes. Smaller indices, bounded exterior heights,
mixed positivity and selected-law/regulator gaps remain unresolved.

No calculation or proof of this continuation was performed in the C455a
audit turn or in this literature turn. This completed review authorizes
one later mathematical attempt, not a theorem or a successful inclusion.
Full matching Mathlib coverage for the proposed transfer is unchecked.

## Inspected local theorem interfaces

C455a's Hypotheses and Conclusion, and its separate critical audit dated
2026-10-23, explicitly allow positive real r, positive even integer m,
and the closed ratio band 31/32≤m/r≤63/64. Its constants and threshold
are independent of both parameters. The height is the exact positive
square root, not a sampled or rounded height. The full finite S, cutoff
equality, non-Euler square B and positive P are already matched in the
audited assembly. L454/L455 state the same real-r domain. Thus source
coverage does not require a new stationary-phase or Mellin estimate.

The proposed a,n prescription is not one of those explicit hypotheses.
L269's first proof paragraph supplies a monotone-crossing existence and
uniqueness argument for the exact implicit equation; its following
asymptotic estimate assumes proportional indices and is not applicable
here. Its contour identity is parameterwise, separately justified before
uniform estimates. L453 Section 1 uses the same exact equation and the
identity r=R+log(1+h²/a²)/4, R=log(a/(2π))/2, but its ceiling bounds
are only for its own n. They are a method precedent, not bounds for
this new band.

L296's last proof paragraphs give the exact maps
r_a(t)=log(a/(2π))/2+log(1+t²/a²)/4 and
N_a(t)=r_a(t)(t−9/2), with their explicit positive derivatives for
large a and t≥9/2. These displayed identities and the elementary
monotonicity calculation specify a second existing way to test the
parameter inclusion. Its sign theorem requires a compact h-band above
5, so that sign conclusion is not an input here. A later proof must
justify whichever parameter conversion it uses on the requested
domain; this review has not established the resulting inequalities.

The precise difference to prove is therefore a uniform inclusion and
quantifier transfer. Keep m=2n, solve the exact equation, check both
closed ratio inequalities, and obtain r beyond C455a's common threshold
for every sufficiently large real a. Once those obligations pass, use
the already stated C455a conclusion with unchanged P and B. Do not
approximate the requested height by a coupled height, freeze m or r,
or invent a new sector bound. Any error-rate rewrite in log a needs
its own uniform comparison within that same attempt. A known-method
proof should be classified REPRODUCTION, without an originality claim.

## Reused primary literature and fresh bounded search

The [ready rounded-endpoint assessment](2026-10-23-rounded-endpoint-height-coverage.md)
is reused for its primary comparisons: Ian Wagner, arXiv:2108.01827v2
(27 June 2022), Theorems 1.2/1.4 and the proof of 1.2 concern fixed
inequality orders after a sufficiently high derivative shift; Wang and
Yang's institutional manuscript, pp. 1–4, equations (1.1)–(1.4) and
Theorem 1.3 concern Taylor-coefficient indices. Neither gives the
unshifted real-height/index rectangle here. Those sources were not
newly retrieved in this step; the earlier inspected comparison is
adequate for these unchanged distinctions.

Freshly read George Csordas, [Fourier transforms of positive definite
kernels and the Riemann ξ-Function, arXiv:1309.0055v2, 21 February
2014](https://arxiv.org/html/1309.0055v2), Theorems 3.5/3.7, Lemma 3.6
and proofs. For a strictly logarithmically concave admissible kernel,
these construct associated kernels and identify their Fourier
transforms with generalized Laguerre expressions. Real-rootedness still
requires positive definiteness of every associated kernel. The proof
uses the coefficient identity and Fourier positivity equivalence; it
contains no every-height logarithmic-index estimate or saddle-inclusion
theorem. This refresh confirms the reused comparison, without importing
that missing positivity premise or reproving the source result.

The new queries listed in SEARCH_EVIDENCE returned no inspected exact
match. They also surfaced the author listing for Suvrit Sra, On some
positivity properties of the Riemann Xi function, v1, 20 October 2026,
at https://suvrit.github.io/ and a linked GitHub riem-xi/v1 directory.
The listing advertises a bounded-height Laguerre consequence under
zero verification through a prescribed height. Attempts to open the
author page and GitHub directory failed in the web tool. Its actual
theorem and proof remain UNREAD; the listing is not theorem evidence,
is not imported, and is not treated as an adequate match. The present
attempt has complete essential inputs in C455a and the inspected exact
parameter methods, so this optional inaccessible lead is parked and
does not block that independently testable specialization. No claim
about the unread manuscript's strongest conclusion is made.

The October overlap review and external-input register were read for
their unchanged scope and trust qualifications. The analytic premise
continues to be the pinned September 30 Theorem 1.1 cited above, not
an independently audited proof, a boundary nonvanishing statement or
an extension of absolute Euler convergence below one. Reproving that
premise or L452/L454/L455 would be duplicate work for this target.

## Recorded failures and stopping threshold

Read L323's hypotheses/conclusion: its obstruction concerns summed
moduli in boundary strips with cutoff r/4 at h=39/8. C455a already
uses L455's different audited reduction; this transfer must not change
that reduction. Read L327's hypotheses/conclusion: its operator-norm
obstruction is to a positive-semidefinite replacement at a different
paired band, not to the actual signed C455a comparison. The canonical
proofs remain the evidence for both stops; they are not invalidated.
The endpoint Liouville-phase attempt of 2026-09-24 explicitly holds r
fixed when producing arbitrarily late negative arithmetic values.
It does not transfer the theta normalization to those heights. This
is a quantifier distinction, not a new sign calculation.

Continue only if one proof gives the exact admissible r for every
requested a,n, with one common real-height onset and the unaltered
complete C455a error smaller than its positive margin. Abandon this
transfer if either endpoint inclusion or the uniform onset fails;
record the precise failed inequality or quantifier rather than
altering the target band or claiming a negative actual coefficient.
No new mathematical lemma or script, DAG edge or overview argument
was written in this literature-only review. The initial low-index,
bounded-height and global mixed-positivity gaps remain independent.
