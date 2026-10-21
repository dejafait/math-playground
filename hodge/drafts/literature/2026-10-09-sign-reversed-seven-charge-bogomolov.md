# Changed-sign seven-charge slice — completed source comparison

TARGET: Test the changed-sign a=-11 survivor slice using its actual first higher direct image and the real-metric Bogomolov inequality.
CHECKED: 2026-10-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Scoped comparison of L071, L060, saved six-charge preservation/character assessments and ATTEMPTS/051 found no completed changed-sign a=-11 slice filter; two bounded external queries found no inspected matching coefficient theorem. General theorem coverage is reused.
SOURCE_EVIDENCE: Reused Bartocci--Bruzzo--Hernandez Ruiperez (1998), Definition 2, Lemmas 1--2 and Theorem 3, pp. 243--246, and Fulton (1998), Theorem 15.2 and Example 15.2.8; freshly inspected Perego arXiv:1910.01867v1, Definition 4.7, Definition 4.20 and Corollary 6.42, pp. 59, 65, 118; Stacks 0A1H, Lemma 36.31.3 (0BDK, within 0BDH) and 02UO.
COMPARISON: Known preservation, perfect base change, relative GRR and real-metric Bogomolov permit arbitrary image rank and impose no positive-mixed-tensor hypothesis. Their conditional applicability framework covers the changed slice; no source evaluates its full character or the admitted integer domain.
GAP: Separately justify every-fibre concentration and compatible image preservation using L071, compute the actual image character with the alternating sign, then compare its discriminant with the complete L071 survivor slice. No slice character, bound or exclusion is established here.
REASON: Essential theorem-level comparison for the changed charge and image rank is now complete; only a bounded application of known tools remains. Import the general theorems without reproof; classify the subsequent test as REPRODUCTION.
SCOPE: L071's identical marked K3 factors and metric, full integral -tau_D, integral c_1=0, actual locally free rank-two product-polystable F, a=-11, integer b in L071's non-exclusion set, unrestricted initial higher characters and K-class; only the actual p_2 first-image Bogomolov necessary test, allowing a reducible image.
LITERATURE_REASON: The saved target was REVIEW_REQUIRED because its charge/image rank and discriminant test were outside the earlier slice-specific approval; reuse general coverage and compare these changed hypotheses before calculation.

## Gap, use and stopping test

Universal primitive rational Hodge-class algebraicity remains the main
gap. The intermediate target is a necessary discriminant constraint on
this larger-charge slice. It could remove candidate compatible product
bundles before construction or transport; it supplies neither a cycle
nor a route resolving arbitrary fourfolds. Kernel existence, inverse or
reconstruction, transverse transport and other larger charges remain open.

Continue only after the actual every-fibre concentration, locally free
image and compatible connection hypotheses have been verified. Compare
the resulting inequality with every integer admitted by L071, including
the boundary, rather than a sampled range. If applicability fails, stop
this bridge; if the inequality removes nothing, abandon this filter
without declaring existence. Do not add opposite-fibre stability,
transform stability or an equivalence to make the argument work.

## Primary inputs and scope comparison

The [changed-sign preservation assessment](2026-10-08-sign-reversed-six-charge-preservation.md)
records inspection of Bartocci, Bruzzo and Hernandez Ruiperez,
*A hyperkahler Fourier transform*, Differential Geometry and its
Applications **8** (1998), 239--249,
[Definition 2, Lemmas 1--2 and Theorem 3, pp. 243--246](https://mat.usal.es/ruiperez/Site/Papers_files/Hyperkahler-Fourier-Mukai.pdf#page=5).
Reuse that extraction: compact hyperkahler source, simultaneous product
rotations, an actual hermitian quaternionic-instanton kernel, a source
instanton and IT are required. Odd IT means every even fibre cohomology
group vanishes. The twistor restriction/identification and descent cases
produce the compatible connection on the actual holomorphic higher
images, not merely their index. Neither a prescribed kernel charge,
positive mixed operator, target rank nor irreducibility is required.

The same assessment's Bartocci--Jardim,
[arXiv:math/0312045v1, Theorem 2 and Theorem-Definition 3, pp. 4--5](https://arxiv.org/pdf/math/0312045v1#page=4),
corroborates hermitian compatibility and explicitly permits reducibility.
Retain its printed target-name typo qualification; use the published
1998 theorem as the principal input. No fresh transform-source read or
twistor reproof is claimed or needed in this turn.

L071's full proof was inspected for the changed-sign product connection,
every-fibre polystability, stable/split alternatives and exact line
lattice. These established statements are conditional on F. The new
charge-specific stability and fibre cohomology must still be written
using its cited surface RR, dual stability and Serre duality inputs.
The [nonflat opposite-projection assessment](2026-10-06-nonflat-opposite-projection-review.md)
already checks their arbitrary-rank scope and the exact real metric.
L060 is a completed positive-sign charge-seven comparison, not a theorem
about the new F or the whole integer slice. L073 covers a different
charge and likewise cannot be invoked as the new preservation result.

Freshly read [Stacks Lemma 36.30.1, 0A1H](https://stacks.math.columbia.edu/tag/0A1H):
a finite-presentation morphism, perfect object and bounded finitely
presented flat complex with proper support give perfect pushforward and
arbitrary base change. Its proof treats the Noetherian case before
approximation; this projective complex surface setting is Noetherian.
Freshly read [Lemma 36.31.3, 0BDK](https://stacks.math.columbia.edu/tag/0BDK),
including its proof of the open fixed-rank single-degree locus. The
earlier 0BDH link is the containing section, not the lemma's own tag.
Apply these only after every derived fibre and its dimension are proved;
also justify that the open locus contains all points, not just a generic
fibre. GAGA and the locally free input permit the algebraic comparison.

Reuse the [six-charge character assessment](2026-10-05-six-charge-surface-character-filter.md)
for Fulton, *Intersection Theory*, second edition (1998), Theorem 15.2,
pp. 286--287, and Example 15.2.8, pp. 291--292, retaining its scan-host
qualification. Freshly read [Stacks 02UO](https://stacks.math.columbia.edu/tag/02UO):
its displayed relative GRR case assumes proper smooth projection, finite
locally free input and locally free higher images, and uses their
alternating sum. Fulton remains the proof citation. The new application
must retain L071's forced full character, its full mixed square and the
relative Todd class, and distinguish the positive holomorphic image from
the negative alternating class. Its first Chern class must be checked
before any simplified discriminant test is used.

Freshly read Perego, *Kobayashi-Hitchin correspondence for twisted vector
bundles*, [arXiv:1910.01867v1, 4 October 2019](https://arxiv.org/pdf/1910.01867v1#page=118),
Corollary 6.42 (p. 118) and its proof/citation paragraph. For a
g-semistable twisted holomorphic bundle of rank r on the compact Kähler
n-fold of the paper's setup, it states

\[
\int_X ((r-1)c_1(E)^2-2r c_2(E))\wedge\sigma_g^{n-2}\leq0.
\]

Definition 4.7 (p. 59) tests subsheaves using the real Kähler form;
Definition 4.20 (p. 65) includes semistability in polystability.
Neither rational polarization nor rank two is required. Use trivial
twisting and zero auxiliary B-field for ordinary Chern classes.
The [earlier inequality assessment](2026-10-04-fixed-lower-chern-stability-test.md)
supplies unchanged Chern-class conventions and source qualifications.
The corollary cites Kobayashi, Chapter IV, Theorems 4.7 and 5.7,
and Lübke--Teleman, Theorem 2.2.3 and Corollary 2.2.4; those original
passages remain unread leads here. No equality-case or projective-flatness
conclusion is approved.

## Duplicates, searches and continuation

ATTEMPTS/051 exhausts the a=-10 rank-two image character/surface filter.
Changing the integrated-factor charge and testing the resulting image's
discriminant is a different, independently testable target. L072's line
identity and L076's factor exchange do not decide this slice; L060's
fixed positive-sign pair does not give its integer-domain verdict.
The positive-tensor curvature exclusion is not imported, and the
persistent flat-index source blocker stays parked. No cross-notebook
input is used and no historical stop is erased.

Bounded external queries on CHECKED were:

- K3 hyperkahler Nahm transform higher direct image Bogomolov inequality Chern character arbitrary rank
- "K3" "real multiplication" "rank three" "bundle"

Results gave no inspected theorem evaluating these coefficients.
The lead [The nef cone of the moduli space of sheaves and strong Bogomolov inequalities, arXiv:1512.02661](https://arxiv.org/abs/1512.02661)
and unrelated Hilbert-scheme/Bridgeland results were not read and are not
inputs. Reuse the prior primary transform/GRR searches and Maciocia
comparison: an equivalence-kernel classification cannot be imposed on an
arbitrary conditional F. Failed searches are not evidence of novelty.

Essential continuation input is L071, with its full integral tensor,
common metric and entire admitted integer domain. L060 and L073 are
method/source comparisons only. All-fibre concentration and the actual
image's preservation remain proof obligations under the now-covered
general theorems; no F or image existence is asserted independently.
The separate research step should import those theorems and perform
only this applicability/character/inequality test. This assessment
approves scope, not the slice's mathematics or its eventual verdict.

Mathlib coverage of the full target and supporting preservation,
base-change, GRR and Bogomolov results: **not checked**. No absence or
full matching declaration is asserted. No lemma or mathematical script
was created or modified in this LITERATURE turn.
