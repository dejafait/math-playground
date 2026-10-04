# Corrected pure coefficients — rank-two arithmetic assessment

TARGET: Test rank-two Chern truncation and untwisted Hirzebruch--Riemann--Roch integrality for all integer pure point corrections admitted by L047, with c_1=0 and L044's mixed action fixed.
CHECKED: 2026-10-04
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Bounded searches on 2026-10-04 checked rank-two Chern and Euler integrality on K3 products, real-multiplication bundles and Schwarzenberger conditions; exact queries and the local redundancy check are recorded below. Adequate earlier rank-truncation, K3 Todd and Fourier--Mukai coverage is reused.
SOURCE_EVIDENCE: Read Stacks Definition 42.37.1, Tag 02TZ, https://stacks.math.columbia.edu/tag/02TZ; Sections 42.45, 42.65 and 42.66, Tags 02UM, 02UN and 02UO, including the character expansion through ch_4 and Lemmas 42.45.2--42.45.4. Read Munoz--Occhetta--Sola Conde, arXiv:0911.2606v4 (20 October 2010), Lemma 5.4, p. 14, https://arxiv.org/pdf/0911.2606v4#page=14; Ellia--Franco--Gruson, Comment. Math. Helv. 83 (2008), Remark 3.10, p. 383, https://content.ems.press/assets/public/full-texts/serials/cmh/83/2/1654/online/10.4171-cmh-128.pdf#page=13. Reused the previously inspected Fulton and Maciocia statements specified below.
COMPARISON: Universal rank truncation and HRR apply with the changed pure coefficients and unrestricted initial higher characters. The inspected Schwarzenberger statements concern projective space; Maciocia requires Fourier--Mukai hypotheses. Neither gives the correction region for this fixed mixed tensor. L045 excludes one K-class and L046 fixes the uncorrected lower data; neither answers this changed-data test.
GAP: Apply the imported rank identities and character polynomials to the full corrected second character, then evaluate the untwisted Euler expression and its exact integrality condition throughout L047's integer region. No corrected square, forced higher-character value, Euler value or congruence is calculated here.
REASON: The changed lower data required a new target comparison, now completed. Import the standard formulas without reproof and reserve their arithmetic specialization for a separate research turn; it can reject corrected rank-two data before existence work without reopening the fixed-class or presentation stops.
SCOPE: The same S, X=S x S, chamber and full mixed tensor as L044 and L047; integer corrections a e_1+b e_2 with a+b<=-13, c_1=0 and putative locally free rank two. Higher characters and K-class are not fixed in advance. The TARGET is untwisted HRR necessity; the explicit continuation below also covers ordinary HRR for integral product-line twists of surviving data. Bundle existence, full K-theory realization, stability and transverse transport are outside this assessment.
COVERED_TARGET: Test Hirzebruch--Riemann--Roch integrality after arbitrary integral product-line twists for corrected rank-two data with c_1=0 and L044's mixed action fixed that pass the untwisted test.

## Hypotheses

Preserve L047's corrected-data region and every previous stop. For
e_1=eta tensor 1 and e_2=1 tensor eta, the proposed second character
is beta_(a,b)=2[C]+B_c+a e_1+b e_2. The coefficients a,b are integers
with a+b<=-13. The prospective bundle has rank two and c_1=0 in
cohomology; its full mixed tensor, including its divisor and
transcendental components, stays fixed. These data differ both from
the unchanged lower data excluded by L046 and from the exact K-class
V' excluded by L045. No higher character of V' is imposed on them.

## Conclusion

SPECIALIZE. The assessment created as REVIEW_REQUIRED at step 087
is completed without changing its TARGET. Essential primary-source
coverage is ready for a separate arithmetic step. No inspected
theorem evaluates this corrected-data family or supplies a bundle.

This completed step is LITERATURE / NOVELTY_UNCHECKED / EXPLORATION.
It establishes source coverage and an actionable test, not a
mathematical result beyond the sources checked. The planned arithmetic
application is a REPRODUCTION of known character and index tools;
their general proofs should be imported by citation.

## Proof — source comparison and applicability

### Rank, character and Euler inputs

Reuse Fulton, *Intersection Theory*, second edition (1998),
[Theorem 3.2(a), pp. 50--52](https://djvu.online/file/87GFN2nbfbdF7),
as inspected in the
[third-Chern assessment](2026-10-03-rank-two-third-chern-test.md):
Chern classes above the rank vanish for a locally free bundle.
For rank two this covers the required third- and fourth-Chern
truncation. It is not a truncation assertion for virtual rank or
arbitrary torsion-free sheaves. The newly read
[Stacks Definition 42.37.1, Tag 02TZ](https://stacks.math.columbia.edu/tag/02TZ)
likewise constructs the total Chern class of a rank-r vector bundle
through its r-th class.

Read the displayed character expansion through ch_4 in
[Stacks Section 42.45, Tag 02UM](https://stacks.math.columbia.edu/tag/02UM).
It applies to finite locally free sheaves without fixing any pure
coefficient, polarization or support presentation. Use its universal
second-, third- and fourth-character polynomials after passing to
cohomology. A vanishing Chern class need not mean that the character
in that degree vanishes. The section's Lemmas 42.45.2--42.45.4 also
give exact-sequence additivity, tensor multiplicativity and the dual
character convention. No new substitution or character value for
beta_(a,b) is obtained in this review.

Read the Todd expansion and multiplicativity in
[Stacks Section 42.65, Tag 02UN](https://stacks.math.columbia.edu/tag/02UN).
Reuse L045's existing K3-product Todd class and full cup-product
bookkeeping. Its normalization and three singular corrections
remain recorded evidence for the old K-class; they do not prescribe
the corrected data's higher characters.

Read [Stacks Section 42.66, Tag 02UO](https://stacks.math.columbia.edu/tag/02UO).
For a finite locally free F on smooth proper X over C, its formula is

\[
\chi(X,F)=\deg\bigl(\operatorname{td}(T_X)\operatorname{ch}(F)\bigr).
\]

Here X -> Spec(C) is proper and smooth, and its higher images are
finite-dimensional vector spaces, so the stated hypotheses hold.
The Euler characteristic is an integer. This use to a point avoids
the smooth-morphism issue for the normalization's ambient map in
the earlier assessment. Also reuse Fulton, HRR Corollaries 15.2.1--15.2.2,
p. 288, as inspected in the
[fourth-Chern assessment](2026-10-03-rank-two-fourth-chern-test.md).

The same HRR statement applies to F tensor an actual integral
product line bundle. Character multiplicativity and the line-bundle
exponential in Tag 02UM cover the explicitly preapproved continuation
if the untwisted test has survivors. The c_1=0 hypothesis belongs to
the untwisted data. No twisted Euler polynomial or additional
integrality condition is derived here. Neither test is a sufficient
criterion for a holomorphic rank-two bundle or a complete integral
K-theory realization test.

### Closest integrality and construction results

Read Munoz--Occhetta--Sola Conde, *Uniform vector bundles on Fano
manifolds and applications*,
[arXiv:0911.2606v4, Lemma 5.4, p. 14](https://arxiv.org/pdf/0911.2606v4#page=14).
Its Schwarzenberger congruences are for rank-two bundles on P^n.
Read Ellia--Franco--Gruson, *Smooth divisors of projective hypersurfaces*,
[Remark 3.10, printed p. 383](https://content.ems.press/assets/public/full-texts/serials/cmh/83/2/1654/online/10.4171-cmh-128.pdf#page=13).
Its trace/binomial integrality discussion also fixes P^n.
These readings confirm the classical index-necessity mechanism but
do not give a congruence on a K3 self-product. Importing their numerical
conditions without changing the variety's Todd and intersection data
would have the wrong hypotheses. Their cited projective-space
references are unread leads, unnecessary for the HRR test here.

Reuse Maciocia, *Rank Two Fourier-Mukai Transforms for K3 Surfaces*,
J. Geom. Phys. 118 (2017), 192--201, accepted manuscript,
[Theorem 0.1, p. 2; Proposition 1.1, pp. 3--4; Theorem 2.5, p. 5](https://www.pure.ed.ac.uk/ws/portalfiles/portal/30370169/Rank_Two_Fourier_Mukai_Transforms_for_K3_Surfaces.pdf#page=5),
as already inspected in the fourth-Chern assessment. Its equivalence
kernels and product-line-twisted diagonal extensions have additional
hypotheses. The changed pure coefficients do not establish those
hypotheses; the theorem neither supplies nor excludes an arbitrary
rank-two bundle with the present full mixed action. The adequate
earlier stable-resolution and hyperholomorphic assessments are also
reused; no new bundle-construction survey is required for this test.

### Redundancy, test and route decision

Searched the local lemmas, drafts, foundations, attempts and history
for corrected rank-two integrality, untwisted HRR, Schwarzenberger
conditions and pure point corrections. L044 supplies the fixed
integral lower tensor; L045 evaluates its exact virtual survivor;
L046 excludes unchanged lower data at every polystable rank; L047
determines only the numerical correction region. None already
evaluates the present all-integer target. The older undoubled parity,
rank-divisible presentation and resolved-support failures are retained
with their recipe hypotheses, rather than made global bans.

The gap addressed is the absence of an actual compatible representative
of the cubic action that could reach the fourth NS-fixed RM direction.
The intermediate target is rank-two arithmetic compatibility of
L047's corrected lower data. It could reject impossible data before
trying to construct such a representative; it supplies no transverse
transport by itself.

In the separate research step, use rank truncation to constrain the
higher characters instead of retaining the fixed higher terms of
L044's V or V'. Retain the full mixed tensor in the
second-character square, including its transcendental part. Then
compare the imported HRR expression with the required integer
threshold across all admitted integer a,b; finite sampling alone
cannot settle the whole region. Chern characters may be rational:
do not impose integrality of each character component in place of
integral Chern classes and an integral Euler characteristic.

If the resulting arithmetic region is empty, stop these corrected
rank-two data and choose another mechanism or rank. If it is nonempty,
record exactly which data survive these necessary conditions; the
preapproved product-line HRR test is then available without another
review. Actual local freeness, stability and transverse transport
remain later gaps in either case. No surviving pair, exclusion,
Euler value or congruence is asserted in this literature turn.

The known span stays 21 and the attained RM directions three against
four required. Arbitrary primitive fourfold classes and the universal
rational Hodge target remain unresolved. No complete candidate arose.
Mathematical exploration usage remains zero. Original Bogomolov
source-access leads stay parked: they are not needed for this
independent arithmetic test, which has no essential unread source.

### Search record and coverage limits

Queries on 2026-10-04 were:

- `"K3" "product" "rank two" "Chern" "Riemann"`
- `"K3" "K3" "rank 2" "integrality"`
- `"rank two" "Chern classes" "Riemann Roch" "integrality"`
- `"K3" "real multiplication" "vector bundles" "Chern"`
- `site:stacks.math.columbia.edu "c_i" "i > r" "Chern"`
- `"Schwarzenberger" "rank two" "fourfold"`
- `"rank two" "K3 surfaces" "Maciocia" Chern integrality`
- `"Schwarzenberger conditions" "rank two"`
- `"K3" "K3" "rank two" "Chern classes"`
- `"K3 product" "rank-two" "Riemann-Roch"`
- `"Uniform vector bundles on Fano manifolds and applications" arxiv`

Read the primary statements identified above, with Stacks in its online
version on CHECKED and printed/preprint pagination for the papers.
Other search returns concerning single K3 surfaces, Fano threefolds,
Hilbert powers or unrelated physical applications were only leads,
not inspected theorem evidence for this target. The search did not
find a full match for this fixed mixed tensor and certifies no novelty.

## Mathlib

Coverage: **not checked** for the full corrected-data arithmetic
test or its supporting HRR and Chern statements. No matching Mathlib
declaration or absence from checked Mathlib sources is asserted.
The named, directly linked Fulton and Stacks results are supporting
inputs, not a full match for the evaluated TARGET. The other papers
have the different scopes stated above. Library lookup is optional
and was unnecessary for completing this source assessment.
