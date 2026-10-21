# Five-adic norm-slice strictness — critical-review coverage

TARGET: Critically audit L060's five-adic norm-slice strictness, including its complete scalar coverage and the bounds 600 < 5^10.
CHECKED: 2026-10-12
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the ready norm-slice-image and L040 critical-audit assessments; searched the specific L035/L038/L040/L060 source claims, foundations/15, ATTEMPTS/010,012 and history/176–177. Compared the complete L060 text with primary lifting and descent statements; no duplicate independent L060 audit appears in these targeted records. No novelty inference or renewed broad discovery search.
SOURCE_EVIDENCE: Retrieved Clark ANT II 161-page notes Theorem 1.79 p.58; Milne ANT v3.08 (2020) Theorem 7.33, Lemmas 7.34–7.35, complete factor-lifting proof and Remark 7.36 pp.121–122; Schaefer–Stoll June 13, 2001 Section 5 pp.8–9 hypotheses and good-divisor identification; FNS June 10, 2019 Section 7.2 pp.24–26 map and equation (7.4). Reused earlier inspected Section 9 cyclic-isogeny and local-field coverage.
COMPARISON: These sources cover the general connecting-map and lifting inputs with the actual complete-field and divisor qualifications. They do not assert L060's 600 upper bound, translated lower bound or strictness; those remain explicit specialization-audit obligations. Cohen's decision theorem and an isogeny image-size formula are unnecessary for this proof.
GAP: No essential external coverage is missing for the exact audit; independent verification of all scalar cases, residue certificates, unit precision, norm injection and translated family remains pending, without accepting L060's arithmetic output as proof.
REASON: Separate source approval is now complete for the saved audit; reuse the named theorems and audit their specialization next turn, preserving the completed result and all independent global gaps.
SCOPE: Exactly the saved TARGET, using L033–L035, L038–L040, L060 and its complete selected certificate values; retain all scalars, entire-fiber isomorphisms, class collisions and exceptional evaluations. REPRODUCTION audit only, with no new image search or global arithmetic claim.
LITERATURE_REASON: The supervisor explicitly requires separate approval for the newly proposed L060 audit; its unbounded scaled-root exclusion, modulo-125 precision and subgroup translation were not independently covered by the prior L040 audit target.

## Relevance and reuse

Main gap: global positive primitive integer emptiness for the surviving
signatures, in particular the surviving 54a1 branch of ordered (3,4,11).
The intermediate target is the exact audit above. Its plausible downstream
use is a reliable necessary local restriction in a future certified global
class intersection. A cardinality separation need not exclude any class
in that global image. Other twists, global classes, compatibility at other
places and integer lifting remain independent unresolved steps.

The ready comparison in
[the norm-slice assessment](2026-10-12-five-adic-norm-slice-image.md)
already records the exact-statement/stronger-result search and the limits
of FNS's local comparison. The target and algebra are unchanged; repeat
browsing for an exact image theorem is unnecessary. Reuse
[L040 audit coverage](2026-10-08-full-fiber-image-equality-critical-audit.md)
for degree, value-group and complete-field inputs. This turn examines the
additional source scope of L060's audit, not its mathematical correctness.

ATTEMPTS/010 excludes the unrestricted identity by the inherited norm;
that does not settle strictness inside the norm slice. ATTEMPTS/012 and
audited L040 settle I_pow=I_fiber, a different comparison. History/177
records L060's completed bound and pending audit, not an independent
review. Preserve those stops and the parked global searches. A historical
stop of scalar filtering does not prohibit this entire-fiber restriction.

## Primary theorem coverage and applicability

Pete L. Clark, [Algebraic Number Theory II](https://plclark.github.io/PeteLClark/Expositions/8410FULLL.pdf),
161-page author-hosted version retrieved 2026-10-12, revision date
unidentified, Theorem 1.79, printed p.58: for a complete valued field,
an integral polynomial and integral approximate root a, the hypothesis
|G(a)|<|G'(a)|^2 gives a unique root in |z-a|<|G'(a)|, with an exact
error formula. The full statement was read; these notes print no proof
of this theorem. Import the named result, without a new Hensel reproof.
Q5 and the finite unramified extension U are in scope. The audit must
check polynomial integrality, the strict inequality, and membership in
the same uniqueness ball when comparing the base-field and U roots.
For the fifth-power use the derivative is not a unit; for the scaled
eleventh-root and coordinate uses it must be a unit. This distinction
is covered by the theorem, not by simple-root lifting alone.

J. S. Milne, [Algebraic Number Theory](https://www.jmilne.org/math/CourseNotes/ANT.pdf),
v3.08, July 19, 2020, Theorem 7.33, printed pp.121–122, and Remark 7.36,
p.122: a monic integral polynomial over a complete DVR with coprime
monic residue factors has unique corresponding monic lifted factors.
Read Lemmas 7.34–7.35 and the successive-correction existence proof.
The corrections preserve factor degrees; squarefreeness inside a block
is not required. This covers the residue-one argument provided its full
factorization and coprimality are checked. Previous coverage gives
Theorem 7.38, Corollary 7.42 and Remark 7.43 for completeness and the
unramified value group. No new local-field theorem is needed. The PDF
page indices are one larger than these printed page numbers.

Edward F. Schaefer and Michael Stoll, *How to do a p-descent on an
elliptic curve*, Trans. AMS **356** (2004), 1209–1231,
[DOI](https://doi.org/10.1090/S0002-9947-03-03366-X),
[June 13, 2001 long manuscript](https://mathe2.uni-bayreuth.de/stoll/papers/p-descent-long.pdf),
Section 5, printed pp.8–9: re-read the Galois-invariant spanning set,
cohomological injectivity/image requirements and evaluation on good
degree-zero divisors. The source identifies this evaluation with the
connecting map, citing its reference [25], Theorem 2.3. That cited proof
was not independently read this turn; the stated identification is
imported. L033 supplies the dual cyclic-isogeny/Kummer specialization;
foundation 15 retains the prior Section 9 inspection. The audit can use
the resulting homomorphism and exceptional evaluations. It must not
transfer subgroup closure to I_fiber or presume an uncomputed quotient
size. No global point-surjectivity or Sha assumption is supplied.

Nuno Freitas, Bartosz Naskręcki and Michael Stoll, *The generalized
Fermat equation with exponents 2, 3, n*, Compositio Math. **156** (2020),
77–113, [June 10, 2019 final manuscript](https://www.mathe2.uni-bayreuth.de/stoll/papers/genfermat-final.pdf),
Section 7.2, printed pp.24–26: retrieved the curve, rational modular
map and eliminated relation (7.4). L034 is the canonical local input
for its chart extension and complete norm, and L035 retains the
exceptional norm specialization. The source's Q2 disk/square-class
analysis is not a Q5 fifth-power precision theorem. Its displayed
global 2-Selmer dimensions require GRH and are not inputs here. General
decidability also supplies neither the claimed bound nor its precision.

These imported results are the strongest needed general coverage;
none of the inspected statements decides the explicit norm-slice
strictness. The local specialization warrants an audit rather than a
citation-only acceptance. Full or supporting Mathlib coverage remains
not checked; that is not evidence of absence.

## Exact audit obligations and stop test

The exact continuation is the TARGET above. Essential inputs are L033's
homomorphism and good-divisor values, L034's complete map, L035's norm
identity including exceptional fibers and Hensel openness, L038's entire
Q5 x U_11 algebra and complete residue-one factors, L039's nonempty
realization, and audited L040's degree-eleven and negative-scalar
necessity. L060 and scripts/five-adic-norm-slice/bounds-certificate.json
contain the proposed result and full arithmetic evidence. No
cross-notebook input is used.

The principal obligations are substantive: uniqueness of the scaled
eleventh root in the entire U_11 residue field; uniformity for every
negative scalar valuation; simple residue roots and invertible b at
both allowed residues without assuming d invertible; f a unit on the
degree-eleven component; congruence modulo 125 sufficient for fifth
classes; inclusion of every isomorphism and the exceptional rational
component via the norm; and 5^11 distinct unrestricted unit classes
giving at least 5^10 classes in the correct norm slice by translation.

Continue if all hypotheses and complete cases pass independent review;
otherwise record and repair the first substantive gap, retaining the
original evidence. No explicit excluded class, exact image cardinality,
global unit/class value, global intersection, other-place compatibility,
rational point or integer lifting is assumed. The bound does not itself
provide a practical class-membership algorithm. Mathlib coverage is not
checked. No mathematical audit or calculation was performed in this
literature turn. Coverage is ready for one bounded REPRODUCTION audit
next turn. Read the complete load-bearing residue-two/residue-four
Bezout values, unit-quotient values and bounds from the certificate with
the shared JSON inspector; bounded previews are not verification.
Independently check the uniform proofs rather than merely rerunning the
existing script. Preserve and report the first substantive defect if
one is found. No changed target or new lemma is approved here.
