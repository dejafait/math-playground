# Opposite Hom stalk length — critical-audit registration

TARGET: Critically audit L135's actual off-diagonal relative Hom stalk length-one calculation.
CHECKED: 2026-10-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the completed exact-stalk discovery and primary-source assessment; read all of L135, selected L118/L121 hypotheses and tangent passages, ATTEMPTS/046 and history/417; followed Stacks 0B91 to 0A1H and 0A1D for the concrete coefficient base-change case.
SOURCE_EVIDENCE: Reused Markman math/0009109v4 Section 2 Remark 3(2), proof through (11), Section 3; FIM 0904.1301v3 Remark 7.3, Theorem 7.6, Section 8; BW 1309.2264v2 Definitions 3.2–3.8, Proposition 3.10, Lemma 3.11 and minimal-complex/stable-Hom/Nakayama coverage. Inspected live Stacks 0B91, 0117, 0G81 and 0A1H/0A1D statements and relevant proofs on CHECKED.
COMPARISON: The completed proof stays within the assessed two-family relative-Ext mechanism; four-dimensional base and reverse Hom are already covered. Audit the actual chain maps, signs and natural tangent identifications rather than reprove the universal diagonal theorem or assume ordinary Ext-sheaf pullback.
GAP: Essential source scope is ready; the later mathematical audit must still verify L135’s coefficient/minimal-Cech comparison, both Hom variations, reverse graded Serre transpose, natural KS identification and full four-dimensional Nakayama test. No audit verdict is issued here.
REASON: Separate source-scope comparison is complete for this exact audit target. Approve one later RESEARCH / REPRODUCTION proof_audit; no new lemma, stalk calculation or correctness certification occurs in this literature turn.

SCOPE: L135 under its full conditional L071/L118/L121 hypotheses, including L120 through L121; actual four-dimensional pair base, two independent full Hom factors and a selected distinct isomorphic pair. L066/L110 are methods only.
LITERATURE_REASON: The supervisor requires separate approval of the newly selected critical audit; reuse existing coverage and inspect only the concrete coefficient/base-change proof case used in L135.

## Original registration (superseded by completed scope review below)

The main gap remains universal primitive rational Hodge realization.
The bounded audit target is the conditional ordinary stalk conclusion
in L135, not collision existence, separation or a global count.
Its plausible downstream use is a trustworthy local multiplicity for a
future global coincidence budget; no useful such budget is known.

Essential inputs are L071's equality hypotheses, L118's actual all-stable
opposite family and natural KS, and L121's disjoint collision tangent
planes. L120 is retained through L121. L066 and L110 are method
comparisons only. Retain the actual hypothetical F and a selected
distinct pair with isomorphic fibres; neither existence is established.

The later audit should read the whole canonical L135 proof and inspect
the relevant actual input ranges. Reuse primary coverage where adequate;
retrieve an essential changed hypothesis or proof case only if needed.
The present turn supplies no fresh source review and no audit verdict.

Continue if the actual coefficient comparison, reverse pairing and
rank-four transpose survive; repair any substantive error explicitly.
Abandon the length-one inference if these inputs leave an unknown or
deficient map. Do not replace that map with reduced support, a model
complex, derived dimensions or an ordinary Ext-sheaf pullback assertion.
Preserve ATTEMPTS/046 and the parked order-five and ATTEMPTS/061--063
evidence. Full matching Mathlib coverage remains not checked.


## Completed audit-scope review — step 418, 2026-10-20

This is a literature comparison, not the critical proof audit. The prior
assessment `2026-10-20-opposite-off-diagonal-relative-hom-stalk.md`
contains the exact discovery queries, inspected source versions/pages,
stronger known result and failed-route comparison. Its target assumptions
have not changed. No repeated broad discovery search is needed. Reading
L135 in full reveals no additional theorem-level hypothesis outside that
coverage; this is a source-scope decision, not verification of its equations.

### Primary hypotheses and concrete comparison coverage

[Stacks Lemma 36.30.4(1), 0B91](https://stacks.math.columbia.edu/tag/0B91)
requires properness, finite presentation, flatness and a perfect
coefficient. Its conclusion is perfect derived pushforward with arbitrary
base change. This matches the product projection and vector coefficient;
it does not assert arbitrary ordinary Ext-sheaf base change. Its reduction
to [Lemma 36.30.1, 0A1H](https://stacks.math.columbia.edu/tag/0A1H)
was inspected, including the Noetherian case relevant to L135.

Followed that proof to [Lemma 36.26.4, 0A1D](https://stacks.math.columbia.edu/tag/0A1D):
the morphism must be quasi-compact and quasi-separated, with a bounded-above
quasi-coherent coefficient complex flat over the base. Its proof specifies
the canonical derived base-change map and checks the ordinary coefficient
pullback against the derived pullback on stalks. These hypotheses cover
the actual locally free coefficient, including dual-number restrictions.
This is supporting coverage for the chain-level comparison in L135;
the future audit must still check its particular finite affine cover,
R-flat terms, representing chain map and compatibility with epsilon.
No claim that all cohomology sheaves commute with pullback is imported.

[Stacks Lemma 12.13.12, 0117](https://stacks.math.columbia.edu/tag/0117)
requires a short exact sequence of cochain complexes in an abelian
category. The statement and snake-lemma proof give functorial connecting
maps. This is the needed comparison tool; it supplies no identification
of the actual coefficient sequence with a chosen model by itself.

[Stacks Remark 48.12.6, 0G81](https://stacks.math.columbia.edu/tag/0G81)
requires a coefficient pairing into the relative dualizing complex whose
adjoint is an isomorphism, with its second coefficient pseudo-coherent.
Its cup/trace construction and proof retain the actual pairing after
pushforward. For the intended audit use the opposite Hom coefficients,
composition trace and surface dualizing shift; a self-duality of one Hom
complex is not a substitute. The explicit odd cyclic sign in L135 must
be audited directly, rather than imported from this general statement.

The previously inspected FIM and BW passages cover bundle deformations
and their Hom-module differential without simplicity of the direct sum
or formality. Reuse their versions, exact sections/pages and qualifications
in the prior assessment. Huybrechts–Lehn Proposition 1.2.7 and Corollary
1.2.8 apply to the common-H stable fibres with the same numerical class.
Minimal free representatives and Nakayama need no surface base; the local
pair ring is the intended four-dimensional base. Their prior coverage is
unchanged. Named surface Serre duality and projective GAGA are reused.
Full matching Mathlib coverage remains not checked.

### Overlap, limitations and the approved test

Markman's universal relative-Ext diagonal result is already a stronger
known mechanism in its own universal-family setting. L135's actual-family
comparison is the bounded specialization requiring audit; no originality
or new source theorem is claimed. The unread Mukai Proposition 4.10 lead
remains unimported and nonessential. ATTEMPTS/046 explains why an
injective first obstruction permits an isolated central Hom jump, so this
audit cannot infer separation. L110 is a method comparison over a different
base and coefficient, not an independent input supplying L135's length.
L118 supplies the natural KS map; L121 supplies the actual disjoint tangent
planes, retaining L120. No new lemma or mathematical script was written.

The exact approved next target remains: Critically audit L135's actual
off-diagonal relative Hom stalk length-one calculation. Check the full
canonical proof, especially the actual epsilon diagram, both moving Hom
factors, reverse Serre transpose, scalar-independent identification of
both KS maps in the same coarse tangent space, and generation of every
one of the four cotangent directions before applying Nakayama. Continue
with length one only if every comparison survives; repair a substantive
error explicitly or abandon that inference if a map remains unknown or
deficient. Reduced support, derived dimensions and a compatible model
cannot replace the actual comparison.

The main gap is universal primitive Hodge realization. A trustworthy local
multiplicity could support a later global coincidence budget, but no useful
budget is known. F and a selected off-diagonal collision remain assumptions;
no collision existence, global count, separation or transport follows.
Preserve all historical stops. The next turn defaults to mathematics with
this unchanged SPECIALIZE assessment, classification REPRODUCTION.
