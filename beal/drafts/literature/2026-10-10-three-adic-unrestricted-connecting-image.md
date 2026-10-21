# Three-adic unrestricted connecting image — source comparison

TARGET: Determine the unrestricted three-adic connecting image of L033's dual five-isogeny over the entire algebra K tensor Q3.
CHECKED: 2026-10-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Exact 54a1/five-isogeny/local-three, X0(11)/local-descent/Kummer and distinctive field-coefficient queries found FNS and general descent sources, but no inspected explicit image classification; scoped comparison of L033, L046, L047, foundations 15/17, ready two-adic/local-algebra assessments, ATTEMPTS/014–015 and history/123 found no duplicate completed three-adic image calculation.
SOURCE_EVIDENCE: Rechecked Schaefer–Stoll June 13, 2001 long manuscript Lemmas 4.2–4.5 statements and complete relevant proofs, printed pp.6–7; rechecked FNS June 10, 2019 final manuscript Section 7.2 canonical-fiber paragraph and Table 5, printed pp.24–27; reused the inspected Clark/Milne certificate inputs specified below.
COMPARISON: The general prime-to-residue-characteristic theorem determines the unrestricted image after local hypotheses are verified. L033 supplies the dual kernel and good-reduction interface, but neither that theorem nor L047 certifies every three-adic residue field. L046's F2 factors and singleton conclusion do not transfer.
GAP: Certify every factor's actual residue field and total degree twelve, verify local good reduction/Tamagawa hypotheses, and specialize the cited image theorem through L033's Kummer identification. This review establishes no three-adic factorization or image size.
REASON: General theorem coverage is ready for one bounded REPRODUCTION attempt; the new work is an explicit local certificate and applicability argument, not a descent reproof or another witness search.
SCOPE: Exactly the unrestricted image for L033's theta:E1 -> E0 over every factor of K tensor Q3, using certified local algebra and the cited image theorem; no global class evaluation, restricted-image enumeration, other twist or changed isogeny.
LITERATURE_REASON: The unrestricted class-image target changed scope after L047's witness audit; complete its required separate approval using ready general source coverage.

## Gap, use and bounded test

The main gap is unconditional global emptiness of the 54a1 branch,
including L045's unevaluated quotient classes; other twists and infinitely
many signatures also remain open. The intermediate target is the entire
unrestricted local connecting image at three. It could provide another
necessary global class condition. If trivial, L047's audited nonemptiness
would be available for a later restricted-image comparison. If nontrivial,
a separately assessed restricted comparison may be useful. Neither
possibility by itself proves global emptiness.

The test is a complete image certificate, or a precise unresolved local
block with actual and required lifting/separation bounds. Retire extra
class filtering at three only after a proved trivial unrestricted image
and established restricted nonemptiness are assembled mathematically.
Nontriviality does not imply that primitive powers shrink the image.
Do not enumerate witnesses or audit L047 again. Preserve ATTEMPTS/008–015
and unfinished global arithmetic. Changing the target does not renew the
mathematical exploration budget.

## Primary theorem comparison

Edward F. Schaefer and Michael Stoll, *How to do a p-descent on an
elliptic curve*, Trans. AMS **356** (2004), 1209–1231,
[DOI](https://doi.org/10.1090/S0002-9947-03-03366-X),
[long author manuscript](https://mathe2.uni-bayreuth.de/stoll/papers/p-descent-long.pdf),
June 13, 2001, Lemmas 4.2–4.5, printed pp.6–7. Locators refer to that
34-page manuscript, not presumed published numbering. For a kernel of
exponent p, Lemma 4.5 identifies the local connecting image with unramified
cohomology away from p when neither Tamagawa number is divisible by p.
Lemma 4.2 gives its size as the number of rational kernel points. Its
proof uses Frobenius-minus-one on inertia invariants. Lemma 4.3 proves
containment using the formal group and smooth special fiber. Lemma 4.4's
size formula cites [24], Lemma 3.8; that reference is not separately
reverified. Import the stated theorem.

Use p=5 and L033's theta:E1 -> E0 with E1[theta]=mu_5. The canonical
pairing, normalization and exceptional good-divisor values are in L033
and foundation 15. Check its integral discriminants -11^5 and -11 at
every factor, and state the good-reduction/Tamagawa applicability there.
Do not substitute rational-field kernel counts on ramified factors.
Determine rational mu_5 from each actual residue field with the cited
simple-root lifting theorem. Retain all factors. No image size is
asserted here, and no general isogeny theorem needs reproof.

Freitas–Naskręcki–Stoll, *The generalized Fermat equation with exponents
2, 3, n*, Compositio Math. **156** (2020), 77–113,
[final author manuscript](https://www.mathe2.uni-bayreuth.de/stoll/papers/genfermat-final.pdf),
June 10, 2019, Section 7.2, printed pp.24–27. The canonical-fiber paragraph
identifies all twelve cyclic subgroups and the degree-twelve field; Table
5 gives L033's polynomial. Neither inspected passage classifies the
three-adic five-isogeny image or certifies its residue fields. The adjacent
two-Selmer computation uses GRH and is excluded. The later two-adic
argument supplies no three-adic image theorem. Canonical field and map
interfaces are already in L033 and L047; their computations are not rerun.

## Reused local certificate coverage

Pete L. Clark, *Algebraic Number Theory II: Valuations, Local Fields and
Adeles*, [author notes](https://plclark.github.io/PeteLClark/Expositions/8410FULLL.pdf),
accessible 161-page version, revision date unidentified: Theorem 1.75 and
Corollary 1.77, p.57 (coprime factor/simple-root lifting), Theorem 1.79,
p.58 (strict Hensel–Newton inequality), Theorem 2.8, p.64 and Proposition
2.9/Corollary 2.10, p.65 (Eisenstein irreducibility, integer ring and total
ramification). Reuse their primary inspection in the two-adic assessment
and foundation 17. Theorems 2.38 and 2.41, pp.80–82, cover Krasner inclusion
and stability of the entire separable quotient algebra with strict
separation obligations; an existential radius is not a precision bound.

J. S. Milne, [*Algebraic Number Theory*, v3.08, July 19, 2020](https://www.jmilne.org/math/CourseNotes/ANT.pdf):
Theorem 7.33 and Remark 7.36, pp.121–123, cover coprime monic residue factor
lifting; Remark 7.37 gives an approximate-factor/resultant condition whose
strict inequality must be checked. Corollary 7.42 and Remark 7.43, p.124,
give degree ef and valuation normalization; Proposition 7.50, pp.127–128,
classifies unramified extensions by residue extensions; Proposition 7.60,
pp.131–132, gives Krasner inclusion under strict conjugate separation.
Their statements and relevant proofs were inspected in the
[complete-fiber assessment](2026-10-08-full-fiber-at-one-local-algebra.md).
This characteristic-zero complete-local-field coverage includes Q3;
no new primary inspection or Q3 certificate is claimed here. Matching
e,f pairs alone does not identify ramified fields, although this target
needs residue fields rather than paired field isomorphisms.

A bounded attempt may refine repeated residue blocks using justified
translations/scalings, exact extension models, Hensel/Eisenstein or
Hensel–Krasner certificates. Prove every factor occurrence and total
dimension twelve. Reduction at the displayed power order does not
certify maximal-order prime decomposition. Approximate factors and
output stabilization do not prove completeness or irreducibility.
If covered methods fail, save the exact unresolved block and stop;
uninspected higher-order Newton/Montes algorithms are not approved.
Only the explicit specialization and certificate are authorized next turn.

## Search and duplication record

Queries on 2026-10-10 included `"54a1" "5-isogeny" "3"`,
`"X0(11)" "local" "descent" "3"`,
`"genfermat" "54a1" "ramification"`,
`"-774" "-380" "54a1"`,
`"isogeny" "unramified subgroup" "good reduction" Schaefer Stoll`,
and `"X0(11)" "Kummer" "3-adic"`.
Returned 54a1 database material concerns the original conductor-54 curve,
not L033's X0(11) dual five-isogeny; it is not imported. Unrelated hits
and secondary mirrors were not theorem evidence. A failed search does
not establish novelty. The stronger general image theorem is reused
from the primary manuscript rather than replaced by a new local argument.

Essential input is L033 (field, curves, dual kernel and evaluation), with
foundation 15's general theorem and the local certificate sources above.
L047's audited primitive entire-fiber nonemptiness is downstream only.
L046 is a method comparison, not a mathematical three-adic input.
Exact factor residue fields and the image remain unresolved. No global
class data, GRH, rank, Sha vanishing, Selmer/point equality or cross-notebook
input is assumed. Mathlib full matching and supporting coverage are not
checked; unknown is not absence. This literature-only turn derives no
new result and writes no lemma or mathematical script. The ready
continuation receives separate supervisor approval before research.
