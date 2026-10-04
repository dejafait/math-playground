# Rank-two fourth-Chern consistency — literature assessment

TARGET: Test the rank-two identity c_4(F)=0 against L044's surviving integral ample-chamber virtual class, retaining all three normalization double-point corrections.
CHECKED: 2026-10-03
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Bounded searches on 2026-10-03 screened rank-two fourth-Chern constraints on K3 products, normalization and singular-point character corrections, stronger bundle constructions and real multiplication; exact queries and the local redundancy check are below. Reused adequate degree-six coverage for unchanged rank, chamber, generation and stability inputs.
SOURCE_EVIDENCE: Read the fourth-character expansion and Lemmas 42.45.2--42.45.3 in Stacks Tag 02UM, https://stacks.math.columbia.edu/tag/02UM; Todd expansion in Tag 02UN, https://stacks.math.columbia.edu/tag/02UN; Tags 0FET, 02UD and 02UO. Read Fulton, Intersection Theory, second edition (1998), Theorem 15.2, pp. 286--287, Corollaries 15.2.1--15.2.2, p. 288, Example 15.2.2, p. 289, and Theorem 18.3(1),(3),(5), pp. 353--354, https://djvu.online/file/87GFN2nbfbdF7. Read Maciocia, Rank Two Fourier-Mukai Transforms for K3 Surfaces (2017), accepted manuscript, Theorem 0.1, p. 2, Proposition 1.1, pp. 3--4, and Theorem 2.5, p. 5, https://www.pure.ed.ac.uk/ws/portalfiles/portal/30370169/Rank_Two_Fourier_Mukai_Transforms_for_K3_Surfaces.pdf.
COMPARISON: Known formulas cover rank truncation, the full fourth-character polynomial, Todd terms, perfect-class products and proper pushforward. Maciocia treats Fourier--Mukai kernels under additional hypotheses and does not evaluate this doubled singular-support class. L044 passes c_3=0 but supplies no degree-eight calculation. No inspected theorem decides c_4 for its fixed V'.
GAP: Apply the imported formulas to the fixed V' in L044 (15), compute the normalization's degree-eight contribution with the ambient Todd factor and all three point corrections, and compare its full second-character square with the rank-two c_4=0 threshold. This exact arithmetic specialization remains undone.
REASON: The previous assessment explicitly stopped at degree six. The missing degree-eight source comparison is now complete, so retain the proposed calculation for one separate research step. It can reject the fixed survivor before maps or stability; it does not reopen residue sampling or the exhausted presentation recipe.
SCOPE: The same very general cubic RM surface S, X=S x S, support C, and the exact integral ample chamber and signed virtual class V' in L044 (15). Covers finite-normalization and degree-eight bookkeeping, an equivalent Hirzebruch--Riemann--Roch cross-check and exact arithmetic; excludes changing V', arbitrary residue searches, bundle existence, stability and transverse transport.
COVERED_TARGET: Compute the degree-eight Chern character of O_C from L019's finite normalization sequence using proper Grothendieck--Riemann--Roch, retaining the normalization's second Todd term, the ambient Todd factor and all three point corrections.
COVERED_TARGET: Evaluate ch_4 and c_4 of the fixed V' in L044 (15), retaining both third finite-difference corrections and the full second-character square, and decide whether c_4=0 excludes that class.

## Hypotheses

Preserve the exact saved target. Fix the final integral chamber and
V' in L044 (15), including its two third finite-difference corrections.
The saved class has virtual rank two, c_1=0, invariant c_2 and c_3=0.
It is not an existing bundle or an actual terminal presentation.
The trivial integral twist used there remains fixed. Retain the full
cohomology class, including its transcendental tensor and point terms.

L008 gives a smooth finite normalization Y of C and the two finite
flat double-cover projections. L019 (10) supplies the exact sequence
with one residue-field quotient at each of three points. These are
existing notebook inputs; their geometry is not recalculated here.

The main gap is an actual representative permitting transport into
the fourth NS-fixed RM direction. The intermediate target is a
necessary rank identity for this fixed survivor, with a clear test
before attempting maps or stability. It does not address every
representative or every primitive fourfold Hodge class.

## Conclusion

SPECIALIZE. Import the standard formulas below by citation; only
their application to C and the fixed V' needs a separate calculation.
No essential unread source blocks this consistency test. No fourth
character of C or V', Chern number, exclusion or existence result is
derived in this literature turn.

This completed step is LITERATURE / NOVELTY_UNCHECKED / EXPLORATION:
it supplies new source coverage and an actionable test, not a
mathematical advance or a certified originality claim. Mathematical
exploration usage is unchanged. The exact Next action can reuse this
assessment without another literature turn.

## Proof — source comparison and applicability

### Rank and fourth-character inputs

Reuse the [degree-six assessment](2026-10-03-rank-two-third-chern-test.md)
for Fulton, [Theorem 3.2(a), pp. 50--52](https://djvu.online/file/87GFN2nbfbdF7):
Chern classes above the rank vanish for a vector bundle. Virtual rank
does not meet the local-freeness hypothesis. This is a necessary test,
not a realization theorem.

Read the full displayed expansion in
[Stacks Section 42.45, Tag 02UM](https://stacks.math.columbia.edu/tag/02UM).
Its already published fourth component is

\[
\operatorname{ch}_4(G)
 =\frac{c_1(G)^4-4c_1(G)^2c_2(G)+4c_1(G)c_3(G)
             +2c_2(G)^2-4c_4(G)}{24}.
\]

This universal polynomial is imported, not derived for V' here.
The test concerns c_4=0; vanishing of ch_4 is a different condition.
Use the full c_2 square when making the later comparison, including
the transcendental component rather than only divisor products.
Section 42.45 also supplies the Chern-root exponential and
Lemma 42.45.2 supplies additivity. Tensor multiplicativity is
[Lemma 42.45.3, Tag 0F9D](https://stacks.math.columbia.edu/tag/0F9D).

Read [Remark 42.56.11, Tag 0FET](https://stacks.math.columbia.edu/tag/0FET):
the character on perfect K-groups is additive on triangles and
multiplicative for derived products. Its quasi-compactness conditions
hold on projective X. This covers the coherent source and all signed
products in V', without treating a virtual class as locally free.
[Lemma 42.39.1, Tag 02UD](https://stacks.math.columbia.edu/tag/02UD)
was checked for the line-twist scope; the fixed survivor requires no
new twist or rational half-determinant line bundle.

### Todd terms, normalization and points

Read [Stacks Section 42.65, Tag 02UN](https://stacks.math.columbia.edu/tag/02UN).
It gives the Todd root product, multiplicativity and the explicit
second component

\[
\operatorname{td}_2(G)=\frac{c_1(G)^2+c_2(G)}{12}.
\]

Both source and ambient Todd terms must be retained in the later
pushforward comparison. The source is the smooth Y; C itself is
non-lci, so a smooth embedded-support normal-bundle formula would
have the wrong hypotheses.

Read Fulton, [Theorem 15.2, pp. 286--287](https://djvu.online/file/87GFN2nbfbdF7):
for a proper morphism f between nonsingular varieties,

\[
\operatorname{ch}(f_!u)\operatorname{td}(T_{\rm target})
 =f_*\bigl(\operatorname{ch}(u)\operatorname{td}(T_{\rm source})\bigr).
\]

Thus L008's finite map to X has the required scope. Read the
HRR corollaries 15.2.1--15.2.2, p. 288, and surface Example 15.2.2,
p. 289, for evaluating a smooth surface's Todd integral by its
structure-sheaf Euler characteristic. The saved double-cover trace
data provide a way to evaluate that input later; no value is obtained
here. Read Theorem 18.3(1),(3),(5), pp. 353--354, for covariance,
smooth-ambient character comparison and the leading support term.
They cover the residue-field corrections in L019's sequence.

[Stacks Section 42.66, Tag 02UO](https://stacks.math.columbia.edu/tag/02UO)
assumes a proper smooth morphism and locally free higher images in
its displayed case. It is adequate for HRR to a point for smooth Y,
but not for the normalization's ambient map. Use Fulton's theorem
for that map. The three corrections previously absent from degree
six must all be included in degree eight, as already recorded in
L012, L013 and L044. No correction coefficient is calculated here.

The Fulton source is the second edition, 1998, as identified in the
earlier assessment; the scan host's title says 1997. Page references
here use the book's printed pagination. Stacks statements were read
in their online version on CHECKED, with stable tag identifiers.

### Nearby bundle results and redundancy

Read Maciocia, *Rank Two Fourier-Mukai Transforms for K3 Surfaces*,
J. Geom. Phys. 118 (2017), 192--201, accepted manuscript:
[Theorem 0.1, p. 2; Proposition 1.1, pp. 3--4; Theorem 2.5, p. 5](https://www.pure.ed.ac.uk/ws/portalfiles/portal/30370169/Rank_Two_Fourier_Mukai_Transforms_for_K3_Surfaces.pdf#page=3).
Theorem 2.5 concerns a locally free extension of a product line
bundle by a product-line twist of I_Delta. Its Fourier--Mukai
criterion requires equality of the two line-bundle products on S
and acyclicity of the indicated line-bundle ratio. Proposition 1.1
computes the transform's character in that ansatz. Theorem 0.1
retains a generically special line subsheaf and the stated determinant
range. These concern equivalence kernels, not arbitrary rank-two
bundles or L044's doubled non-lci support. They supply neither the
fixed class's fourth character nor a bundle with that K-class.

Reuse the earlier adequate generation and stability readings from
the [doubled-source assessment](2026-09-27-doubled-source-cubic-resolution.md).
They remain conditional on actual presentation maps or an existing
stable bundle. No renewed source survey of that unchanged framework
is needed for this arithmetic test.

Checked `lemmas`, `drafts`, `foundations` and `ATTEMPTS` for ch_4,
c_4, fourth-Chern, degree-eight and Todd calculations. The existing
leading-character arguments locate the point corrections but do
not evaluate this degree-eight target. L044 supplies the fixed
survivor and explicitly leaves that calculation undone. The overview's
L028 undoubled parity stop and L030 rank-divisible stop do not cover
this fixed rank-two class. Preserve those stops and Attempt 033.

### Discriminating test and remaining gap

Compute only the exact fourth-Chern condition of the saved V'.
Include both finite-difference products from L044 (15); agreement
in lower degrees does not license discarding their higher terms.
Use the normalization sequence, all three points, and the ambient
Todd factor. An HRR check and exact rational arithmetic can validate
the bookkeeping without relying on numerical sampling.

A nonzero c_4 excludes a rank-two locally free representative of
this particular K-class and warrants stopping it. Zero c_4 records
survival of another necessary test, leaving exact maps, local
freeness, stability and transverse transport unresolved. It does
not justify further residue sampling or an existence claim. Either
outcome completes this bounded consistency test; a later construction
needs its own concrete mechanism and adequate source coverage.

The span remains 21 and three RM directions are attained against
four required. No new class, bundle or transverse surface is supplied.
Rechecked Deligne's [Clay statement, section 1 and remark 2(ii),
p. 2](https://www.claymath.org/wp-content/uploads/2022/06/hodge.pdf#page=2):
the target has rational coefficients and concerns all smooth
projective complex varieties. Its finite-resolution observation
does not supply a rank-two stable representative.

### Search and access record

Queries on 2026-10-03 were:

- `"K3" "product" "rank two" "fourth Chern"`
- `"rank 2" "Chern character" "c4"`
- `"normalization" "surface" "Chern character" "double points"`
- `"rank two" "K3" "Chern" "real multiplication"`
- `"fourth Chern character" "c_4" bundle`
- `"Chern character" "c_1^4" "24" filetype:pdf`
- `"K3" "product" "rank 2" "bundles" Chern class`
- `"K3" "K3" "rank two" "bundles" Chern`
- `"normalization" "Riemann Roch" "surface" "double points" Chern`
- `"Grothendieck Riemann Roch" "skyscraper" "Chern character"`

Read the primary statements and formulas identified above. Other
results concerned a single K3, Hilbert powers, threefolds or
ind-Grassmannians. Penkov--Tikhomirov's introduction, printed
pp. 547--548, was inspected in
[the published chapter](https://math.nyu.edu/~tschinke/.manin/final/penkov/penkov.pdf#page=1)
only to screen its setting; no exclusion theorem from it is imported.
Other returned papers and their references remain uninspected leads,
not theorem evidence for this target or essential dependencies.

An optional open of Huybrechts's `K3Global.pdf` and a text lookup
returned extractor errors. That reading supplies no new evidence;
it is parked. Fulton's inspected surface HRR covers the Todd-integral
input, and the existing chamber assessment is reused. There is no
essential source blocker for this fixed consistency test. The bounded
search found no full match and does not certify novelty.

## Mathlib

Coverage of the full fourth-Chern target: **not checked**. No Mathlib
match or absence from checked Mathlib sources is asserted. The named,
directly linked Fulton and Stacks statements are supporting inputs,
not Mathlib declaration identifications or a match for the complete
fixed-class test. Maciocia's theorems have the different scope stated
above. Library lookup was not needed to finish this assessment.
