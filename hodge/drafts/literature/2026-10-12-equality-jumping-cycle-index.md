# Equality kernel — proposed global jumping-cycle comparison

TARGET: Assess whether the global index class of Rp_2*(F tensor p_1^*L^{-1}) forces an effective jumping-cycle constraint incompatible with a split fibre at (m,n)=(14,21), without assuming expected codimension.
CHECKED: 2026-10-12
DECISION: EXPLORE
SEARCH_EVIDENCE: Searched localized Chern character, Thom-Porteous excess codimension and positivity terminology; checked ATTEMPTS/059/060 and the preceding line-twist assessment; inspected Fulton 14.4 and Stacks 42.50/42.52. No matching unconditional effective jumping-cycle constraint was identified.
SOURCE_EVIDENCE: Fulton, Intersection Theory, 2nd ed. (1998), Theorem 14.4(a)-(d), pp. 254-255 and Example 14.4.13, pp. 260-261; Stacks Situation 42.50.1, Lemma 42.50.2, Definition 42.50.3 (0FB0), Lemma 42.52.5 (0FB9), hypotheses and relevant proof cases inspected on 2026-10-12.
COMPARISON: Porteous supplies a localized degeneracy class in excess dimension but identifies an effective fundamental cycle at expected codimension; a separate positivity result requires global generation. Localized Chern character requires exactness off its support and gives no effectivity conclusion.
GAP: No global determinantal presentation with the required positivity, expected codimension, or supported comparison complex is established for the twisted pushforward. No incompatible effective class is available from the inspected results.
REASON: The source comparison changes the route: park automatic index-to-effective-jump exclusion rather than calculate a virtual sign without an applicable effectivity theorem.
SCOPE: L071 and audited L093 at identical marked K3 factors and fixed real h; rank-two locally free Omega-polystable F with c_1=0 and full ch_2=-14e_1-21e_2-tau_D; c_1(L)=k. Neither F nor split fibre nor generic concentration is known to exist.

Essential inputs are L071, L093 and the qualified perfect-base-change
coverage in the preceding line-twist assessment. Higher characters
remain only those forced by actual rank two. Do not assume finite,
reduced, transverse or expected-codimension jumping support; constant
fibre type; an inverse; ordinary scalar self-duality; or effectivity of
an alternating virtual class. No cross-notebook result is used.

A useful test would either identify a canonical effective cycle whose
required class is impossible, or show that no such class comparison is
available without additional unproved hypotheses. In the latter case
park this mechanism. It would leave all-stable equality kernels,
common-kernel existence, prescribed mixed action, transport and
universal primitive rational Hodge realization unresolved. This completed review supplies no new mathematical derivation or split-fibre exclusion.


## Completed source comparison

The main gap is universal primitive rational Hodge realization. The
intermediate threshold was an effective jumping-cycle constraint that
would exclude a split fibre of this equality kernel. Such a constraint
could narrow later common-kernel construction; all-stable equality,
positive Euler, prescribed mixed action and transport remain independent.
The abandonment test is failure to supply effectivity under the stated
hypotheses. It is met for the inspected index/Porteous mechanism, not
for every possible split-fibre argument.

**Primary degeneracy theorem.** [Fulton, *Intersection Theory*, second
edition, Chapter 14](https://link.springer.com/chapter/10.1007/978-1-4612-1700-8_15),
Theorem 14.4(a)-(d), pp. 254-255: for a bundle map A to B on a pure
dimensional scheme, the rank-at-most-r locus carries a class in the
expected dimension. Its pushforward is the Porteous determinant.
Expected codimension gives positivity; with Cohen--Macaulay base it is
the scheme's fundamental cycle. The proof reduces to a flag case and
the localized top Chern construction. Example 14.4.13(a), pp. 260-261,
gives an excess-dimensional alternative: global generation of
Hom(A,B) gives a nonnegative representative, when the expected dimension
is nonnegative. Its proof invokes positivity of intersections with the
universal degeneracy locus. These additional hypotheses are essential
qualifications, not an unconditional effectivity assertion.
The publisher's primary abstract and theorem text in the
[accessible book transcription](https://djvu.online/file/8KbyCnh9POwWS)
were inspected. OCR drops displayed formulas; the publisher abstract
was used for the determinant, correcting its displayed F-K typo to B-A
in the book's notation. No missing OCR formula supports a new calculation.

**Primary localized-character theorem.** [Stacks 42.50, 0FB0](https://stacks.math.columbia.edu/tag/0FB0),
Situation 42.50.1, Lemma 42.50.2 and Definition 42.50.3 require a
perfect object, a closed support, and a listed finiteness condition.
For localized character the object must vanish off the support; for
localized p-th Chern class it may instead be a degree-zero locally
free object of rank less than p there. Quasi-compactness supplies the
finiteness condition in our projective setting. The graph-construction
proof produces a bivariant class with the stated pushforward identity,
not a positive representative. [Stacks 42.52.5, 0FB9](https://stacks.math.columbia.edu/tag/0FB9)
gives additivity for distinguished triangles of perfect objects whose
outer terms vanish off the same support, under its finiteness conditions.
The proof uses a cone family and specialization to the split triangle.
This is additivity of virtual classes, not positivity of cohomology jumps.
These statements and their relevant proof cases were read; no reproof
is necessary. Stacks is a live source, accessed 2026-10-12.

**Applicability boundary.** Reuse the preceding assessment's qualified
0A1H coverage for perfect pushforward and derived base change of
K=Rp_2*(F tensor p_1^*L^{-1}). Neither generic odd IT nor exactness of K
off the endpoint-jumping locus is an established input. Even a
conditional one-degree restriction leaves its middle bundle; a supported
comparison would require a specified extension and comparison map.
Local finite-free differentials and their minors do not by themselves
supply a global map whose two-bundle difference is K. No such map's
Hom bundle is known globally generated, and expected codimension is
explicitly unavailable. Thus the inspected theorems cannot presently
turn GRR for K into the sought effective class. This is a hypothesis
comparison, not a proof of compatibility of K or a universal theorem
that no effectivity approach can work. No twisted index was calculated.

**Duplicates and preserved failures.** ATTEMPTS/059/060 record only the
untwisted strict-Euler exclusion; the preceding line-twist review parks
IT preservation. This is a distinct source-based stop at effectivity.
Searches included “Fulton Intersection Theory localized Chern character
complex exact off closed subset effective Porteous excess codimension”,
“Thom Porteous formula degeneracy locus expected codimension Fulton
theorem 14.4”, and targeted Stacks/publisher queries. Returned quiver
and generalized degeneracy papers are unread leads, not imported
coverage. No absence or novelty claim follows from this bounded search.
Full matching Mathlib coverage: not checked. No lemma, proof, DAG or
mathematical script is modified.

The next proposed mechanism is the local deformation slice of the
actual split rank-two fibre, rather than global index effectivity.
Its real-metric and quaternionic scope needs separate source approval;
existing L080-L082 orthogonal rank-five coverage cannot silently cover
this changed object. No local slice or obstruction is derived here.
