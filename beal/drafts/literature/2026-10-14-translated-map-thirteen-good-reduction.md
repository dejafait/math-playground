# Translated-isogeny map at thirteen — completed source comparison

TARGET: Certify good reduction at thirteen of Q -> j(P_sigma+theta(Q)) on E1 over the entire completion K tensor Q13.
CHECKED: 2026-10-14
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched abelian-scheme/Neron extension, prime-to-residue-characteristic isogeny specialization and constant degree; inspected Robert/Milne author theorem/proof passages, Snowden's named mapping theorem and direct Stacks statements; compared L033/L062/L064/L066, the ready fixed-class assessment and ATTEMPTS/029–030.
SOURCE_EVIDENCE: Robert March 7 2023 draft Theorem 2.3.11 p.15, Propositions 2.3.15–16 pp.16–17, Example 3.1.8 p.27 and Proposition 3.1.19 with proof sketch p.31; Milne January 2 2022 corrected 1986 article Proposition 20.7 with proof p.44; Snowden 2013 Lecture 9 named Neron mapping theorem and good-model identification; Stacks 0BX5, 02KB, 02KD, 04MH, 0BFH, 02NZ and 09HB inspected.
COMPARISON: Known extension, finite-flat isogeny and degree/base-change theorems cover the structural steps; the sources do not print this fixed translated modular map. L066 supplies the original-map component; no new general extension theorem or quotient-formula reproof is needed.
GAP: Write and check the application over the whole integer ring, retaining sigma/P_sigma, both dual identities, special isogeny degree/etaleness, complete composite pole pullback and separability; no such application is certified in this literature turn.
REASON: Essential source coverage is now available for the unchanged target; a bounded theorem-application proof can test this prerequisite without reopening failed class-removal tests or assuming Mordell–Weil data.
LITERATURE_REASON: Turn-start REVIEW_REQUIRED lacked inspected integral extension and special-fiber isogeny coverage; original-map coverage did not include translation or theta.
SCOPE: Only the complete translated map at thirteen using L033/L034/L062/L064/L066; no rank/index, point enumeration, class removal, other prime/covering or global power-lifting target is approved.

## Relevance and prior evidence

The main gap remains positive primitive integer emptiness, particularly
ordered (3,4,11) in this route. This intermediate certificate could supply
one prerequisite for the general rational-j method on L062's fixed class.
It would supply neither a point bound nor an integer exclusion.

Read L033's geometric models, quotient/dual identities and discriminants;
L062's intrinsic point and fixed sigma; L064's whole-field statement;
and L066's statement and integral-chart interface. L033's geometric
construction does not assume its separate transported-integer-solution
clause. No original integer solution is assumed for this target.

Reuse `2026-10-14-fixed-class-elliptic-chabauty-scope.md` for Bruin 2003
Section 4.2 pp.42–45, FNS June 10 2019 Section 7.2 pp.25–27 and Magma's
input guarantees. These unchanged sources already record inadequate
independent generators in this field and conditional Selmer dimensions.
No fresh browsing of those sources was needed. L066 explicitly does not
certify translation or theta, so there is no local duplicate result.
ATTEMPTS/029–030 remain stopped by L064/L065's class survivors; this
point-level question neither challenges them nor resolves the index gap.
The searches establish standard coverage, not originality.

## Inspected structural statements and qualifications

Damien Robert, *Theory of abelian varieties and their moduli spaces*,
[author draft](https://www.math.u-bordeaux.fr/~damienrobert/pro/publications/books/avtheory.pdf),
March 2021, footer March 7, 2023: Theorem 2.3.11 requires a connected base,
a proper smooth scheme with section and one geometric abelian fiber.
Proposition 2.3.16 extends rational maps from regular schemes into abelian
schemes; its proof sketches line-bundle extension via biduality. Example
3.1.8 identifies an abelian scheme as its generic fiber's Neron model.
Proposition 3.1.19 over a local DVR extends an abelian isogeny to a
fiberwise isogeny when its degree is prime to the residue characteristic
(or its source is semistable). Its sketch uses torsion and the
contragredient. Proposition 2.3.15 proves finite flat kernels and locally
constant degree for fiberwise abelian isogenies, by fibral flatness and
proper quasi-finite finiteness. These are inspected author-expository
statements/proof sketches, not a fresh reading of all underlying original
proofs. The reversed divisibility wording inside the 3.1.19 sketch is not
used: the statement's prime-to-characteristic hypothesis governs.

Andrew Snowden, [*Lecture 9: Neron models*](https://websites.umich.edu/~asnowden/teaching/2013/679/L09.html),
Math 679 (2013), “Classification of minimal regular models” identifies a
good minimal Weierstrass model with the Neron model. “Definition and
basic properties” states the named Neron mapping theorem: maps from a
smooth R-scheme to the generic elliptic curve extend uniquely to its
Neron model. “Types of reduction” identifies the good-reduction model
as the unique abelian-scheme extension. The lecture states these inputs;
it does not prove general Neron existence. This named-theorem coverage
is used with Robert's scheme formulation, not as a new existence proof.

J. S. Milne, *Abelian Varieties*, Chapter V in Cornell–Silverman (eds.),
*Arithmetic Geometry*, Springer (1986), 103–150,
[corrected author text, January 2, 2022](https://www.jmilne.org/math/xnotes/AVs.pdf),
Proposition 20.7, printed p.44 (PDF index 43), numbering unchanged:
for an abelian scheme of relative dimension g and a nonzero integer n,
[n] is finite flat surjective with kernel order n^(2g), and is etale
when n is invertible in every residue field. Its complete displayed
proof uses fibral flatness, properness/finite fibers and the field-case
degree/differential statements. This covers [5] over residue
characteristic thirteen; it does not alone assign degree five to a
factor of [5]. Milne's 2008 CourseNotes Section 17 was inspected but its
existence statement alone was not substituted for good-model identification.

The following direct Stacks statements/proofs were inspected on
2026-10-14. Cite stable tags because section numbers have moved.

- [0BX5, Lemma 29.43.1](https://stacks.math.columbia.edu/tag/0BX5): proper finite-type quasi-separated morphisms have unique valuation-ring lifts. This covers point extension, not an arbitrary rational map on a surface.
- [02KB, Lemma 29.49.2](https://stacks.math.columbia.edu/tag/02KB): finite flat is finite locally free over a locally Noetherian target. [02KD, Lemma 29.49.4](https://stacks.math.columbia.edu/tag/02KD) preserves finite local freeness under base change; [04MH, Lemma 29.49.5](https://stacks.math.columbia.edu/tag/04MH) gives open-and-closed constant-rank strata. The latter proofs are omitted or reduced to local rank in the source.
- [0BFH, Lemma 39.9.9](https://stacks.math.columbia.edu/tag/0BFH): for a nonzero abelian variety over a field, [n] is etale precisely when n is invertible. The proof uses the origin differential and translation.
- [02NZ, Lemma 29.52.9](https://stacks.math.columbia.edu/tag/02NZ): degrees multiply for dominant locally finite-type maps of integral schemes with finite function-field extensions, by the field tower theorem.
- [09HB, Lemma 9.12.12](https://stacks.math.columbia.edu/tag/09HB): algebraic separability is transitive; its proof retains the field generated by coefficients before treating a separable root.

Robert cites BLR, *Neron Models* (1990), Sections 1.2 Proposition 8 and
7.3 Proposition 6. The Arizona chapter-one scan was located, but its
image-only text could not be read reliably: screenshots returned
placeholders, and shell retrieval failed DNS. These original BLR
passages remain **unread underlying references**. Essential coverage
instead comes from the inspected named theorem and author-expository
statements above. No assertion relies solely on an inaccessible scan.
The queried tags 02NX and 0BFI were not the needed degree/multiplication
statements; no guessed numbering is used. Search snippets, forums and
AI-generated theorem pages are not theorem evidence.

## Covered application and continuation test

Use F=A13 and its entire integer ring R12 from L064. Retain exactly
L062's sigma and localized P_sigma. L033 gives the projective models
with discriminants -11^5 and -11, degree-five h and theta, and
h theta=[5], theta h=[5]. L066 gives the entire original morphism and
reduced polar divisor O+11(3T). These inputs fit the inspected structural
scope; the map-specific application is still to be written next turn.

The approved proof attempt must check the abelian-model hypotheses,
extend P_sigma/h/theta over R12, and justify extension of the dual
identities and translation with its inverse everywhere. It must establish
theta's finite local freeness, rank five and etaleness after reduction,
rather than infer them merely from its generic degree. It must compose
the entire morphisms and account for pullbacks of both poles with all
multiplicities over geometric residue fields: individual preimages need
not be R12-rational. Check dominance, integrality and finite
function-field extensions before 02NZ and reduced separability before
09HB. Retain O and every quotient-kernel/translated exceptional point.
These are future proof obligations, not results derived in this review.

Continue upon a complete certificate with unchanged generic/special
degree, proposed threshold 12 times 5, and separable reduction. Park
thirteen for this prerequisite upon a genuine failed hypothesis or
reduction defect; an affine denominator alone does not meet that test.
A research step under this SPECIALIZE assessment is REPRODUCTION:
apply known structural results and check the particular composition;
no general extension/isogeny theorem needs reproof. No lemma,
mathematical script or composite-map certificate was produced here.

Unconditional rank below twelve, adequate generators/index, coset zero
bounds, other-class coverage and one common global primitive power
triple remain independent gaps. No GRH, Selmer/point equality or
rationality of individual pole preimages is assumed. Full matching and
supporting Mathlib coverage is not checked; unknown is not absence.
