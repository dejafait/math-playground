# Exact auxiliary Legendre field — independent reduction target proposed

TARGET: Determine whether L078's unchanged Legendre curve E_L has semistable reduction at every finite place of its exact field G, using its full rational 15-torsion.
CHECKED: 2026-10-18
DECISION: IMPORT
SEARCH_EVIDENCE: Step318 reused L049 and the 2026-10-11 assessment; checked L078 hypotheses/conclusion and its full-coordinate rationality, history/317 and ATTEMPTS/033–034; searched Raynaud semistable reduction n>=3 torsion Silverberg Zarhin and full 3 torsion Raynaud criterion. Read the published criterion, publisher endpoint confirmation and SGA7 transcription cases. No exact-G duplicate was identified in the scoped records; no novelty claim.
SOURCE_EVIDENCE: Silverberg–Zarhin, Ann. Inst. Fourier 45(2) (1995), 403–420, Definition 3.1 p.405 and Theorem 3.5 p.406, https://www.numdam.org/article/AIF_1995__45_2_403_0.pdf ; publisher abstract https://aif.centre-mersenne.org/item/AIF_1995__45_2_403_0/ explicitly confirms n>=3; cited original SGA7 I, LNM288 (1972), Expose IX Proposition 4.7, with supplemental transcription 4.7–4.7.4 inspected at https://grothendiecksga.com/read/sga7/fr/9-4.html . Reuse Milne, Elliptic Curves, second edition (2021), II Proposition 6.3 pp.70–71, as assessed in L049 for complete geometric torsion under completion.
COMPARISON: The full-torsion Raynaud criterion covers the proposed application using level 5 away from residue characteristic 5 and level 3 at 5; both divide 15. The equality endpoint n=3 is explicitly covered. Normality, full 2-primary torsion and enlargement of G are unnecessary. Only citation and local applicability remain; no new reduction theorem or reproof is justified.
GAP: Essential source coverage is ready for the exact TARGET; the canonical mathematical application remains deferred. It must verify all geometric sublevel torsion after every completion and use the identity unramified extension. This review supplies no canonical semistability lemma or normality, sufficient-initial-data or finite B>=A verdict.
REASON: The changed-field/level-15 comparison now has an inspected criterion covering every residue characteristic, including its essential n=3 endpoint. Return to the same mathematical target by known-result import; no additional classification retrieval or repeated literature search is needed.
SCOPE: Same L073 auxiliary witness, L077 choices D,s,t and embedding, and exactly L078's E_L/G and H,N completions. No enlargement, reselection, equality G=F', G/Q normality, splitness at every place or sufficient initial theta-data is assumed.

## Step317 proposal retained as historical context

Main gap remains original finite B>=A. The proposed intermediate input
would address the reduction part of initial-data admissibility for the
exact field prescription. Its downstream use would be a later check of
stable pointed reduction on this same field; semistability alone must
not be reported as all initial data or the original comparison.

Three mechanisms were compared, without attempting additional mathematics:

1. Reuse powers of the recorded 89-Frobenius as a normality separator:
   reject under the audited ATTEMPTS/034 stop; there is no new element.
2. Determine the full mixed radical/15-torsion kernel: potentially relevant,
   but no additional joint-image data or explicit witness coefficients
   are available. Park pending concrete new input; the overall normality
   question is not declared exhausted.
3. Apply the torsion reduction criterion to the unchanged E_L/G: select
   for separate source comparison. L078 supplies the rational torsion
   directly, so this test need not depend on normality or those ratios.

Pass the source gate only if the exact cited criterion covers this
number-field curve and a prime-to-residue torsion sublevel at every
finite place, without the extra 2-primary torsion used in L049's p=5
case. Identify the correct replacement sublevel and its hypotheses in
that review. If any place case requires unavailable hypotheses, record
it and do not authorize a universal conclusion. Do not repeat the
parked classification retrieval or the completed L080 audit.

Essential continuation input is L078 (inheriting L073 and L077's same
choices). L049 is a source-method reference, not a theorem about E_L/G.
L079 fixes the native field interpretation; audited L080 records the
independent normality gap, not a premise needed for the proposed test.
Keep all actual curves, fields, places and parameters distinct from the
retained E_0,F,K_glob,q_0. Other initial data, normality, retained radical
memberships, native input/action, marked all-image factorization, pilot
transport, essentiality and original finite B>=A remain unresolved.
Full matching and supporting Mathlib coverage for the changed application
is not checked. No lemma, proof or source approval for it is supplied here.

## Step318 completed source comparison — 2026-10-18

LITERATURE_REASON: L049's level-30 application did not assess the changed exact E_L/G or the endpoint level 3 needed with only full 15-torsion; this is the essential missing coverage requested by the startup gate.

The main gap remains original finite B>=A. The intermediate target is
exactly TARGET; its plausible downstream use is the reduction prerequisite
for stable pointed models on this same field. Independent normality and
all marked transport/essentiality gaps remain open.

### Exact criterion and endpoint evidence

Silverberg–Zarhin Theorem 3.5 requires an abelian variety over a discretely
valued field, an integer n>=3 prime to the residue characteristic, and
full geometric n-torsion defined over an unramified extension. Its
conclusion is semistability. Definition 3.1 allows a nonsplit torus.
The n=2 exceptional branch is unused.

The PDF text extraction renders the threshold ambiguously. The publisher's
own English and French abstracts explicitly include equality at 3.
The supplemental SGA7 transcription, Proposition IX.4.7, has only n=2
as its exception. Its proof reduces to a faithful finite action on the
semiabelian special fiber; Lemma 4.7.1 removes finite automorphisms
trivial on n-torsion for n!=2. Sections 4.7.3–4.7.4 explain the rigidity
and the exceptional exponent-two group. These are inspected source
arguments, not a new reproof. The transcription is not claimed to be an
authenticated original scan. The published theorem plus its publisher's
explicit endpoint statement suffice for this import.

Web screenshot requests returned references without a viewable image;
a direct local PDF download failed DNS. No visual inspection is claimed.
The accessible theorem text and publisher endpoint resolve the needed
source issue, so there is no essential source blocker.

### Approved applicability checklist for the research turn

| Finite residue characteristic p | Available level | Required check |
| --- | --- | --- |
| p!=5, including 2 and 3 | 5 | Full 5-torsion after completion |
| p=5 | 3 | Full 3-torsion after completion; equality endpoint applies |

L078 is the essential curve/field input: a number field G and the same
nonsingular E_L with full geometric 15-torsion rational over G, using
both coordinates. For each finite place independently, the subsequent
application must embed a global algebraic closure into a local algebraic
closure. Use the assessed Milne II.6.3 cardinality n^2 in characteristic
zero to check that the embedded global torsion exhausts local geometric
torsion. This check is required even at p=3; it concerns field
characteristic zero, not reduction of p-primary torsion. Choose only
the prime-to-p level in the table for Raynaud. Take the identity
extension of the completion as the unramified extension.

The scope is unchanged E_L/G, with L073/L077 choices D,s,t,H,N and
embedding inherited through L078. L049 supplies a method, not an
E_L/G theorem. L079's native interpretation and L080's independent
normality problem are not additional premises. No everywhere splitness,
everywhere good reduction, Galoisness or sufficient initial data is
covered. Full matching Mathlib coverage remains unchecked, without an
absence claim. No theorem or proof in lemmas/ and no mathematical script
is changed by this literature turn.

Continue with the cited import if every listed completion/torsion
hypothesis is matched; abandon the universal application if any finite
place needs unavailable torsion or a changed field. The source comparison
finds no such missing case. This is useful coverage of known mathematics,
not a new mathematical result. The proposed application stays separate.
ATTEMPTS/033–034 and the normality/radical-ratio gaps remain intact.
