# Proposed four-index conditioned test with an off-shell neighbor

TARGET: Test L056's fixed moments on every four-index union matrix anchored at D with half-distances (DE,DF,DG,EF,EG,FG)=(5,5,6,5,5,5).
CHECKED: 2026-10-12
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 189 compared the exact L053/L054/L056/L057 coordinate scope, ATTEMPTS/035,038,039 and history/188; targeted searches for constant-weight triple moments, four principal indices, cross-shell PSD and A(1024,10,68) found the primary Polak hierarchy but no inspected fixed-coefficient verdict.
SOURCE_EVIDENCE: Freshly read Polak arXiv:1703.05171v1 Section 1.1 (1)–(3), Proposition 1.1, complete indicator proof and following principal/nonnegative cases, printed p. 2; reused foundations/09,12 and the step-185 assessment; freshly read Brouwer–Haemers author preprint Theorem 2.7.1(i), p. 36 and Section 2.9 through Lemma 2.9.1's complete proof, p. 37.
COMPARISON: The known order-three union condition covers the four indices, and every entry uses an already represented triple or fixed lower-order moment; L056 and L057 do not certify the coupled matrix anchored at D with DG=6. Known higher-order programs are stronger frameworks, not a verdict for these coefficients.
GAP: Exhaustively construct feasible full 16-region incidences for the specified six distances and test their unchanged rational matrices; no sign, incidence count, feasible example or PSD verdict was calculated in this literature turn.
REASON: Source applicability and essential coordinate coverage are now complete; a separate bounded calculation is needed because citation alone does not decide the prescribed matrix signs. No theorem needs reproof.
SCOPE: Exactly the saved target, with indices {D},{D,E},{D,F},{D,G}, unchanged L053 rho,p_i and L056 represented unordered triple moments; exhaustive incidence coverage or a complete negative witness, with singular cases retained. No optimization, added zeros or moment completion.

## Gap, target and discriminating test

The main gap is arbitrary-center safety at 68 agreements, independently
at 67. The intermediate target is the TARGET above. Its plausible use
is to reject one fixed released-zero shell prescription through a
coupled necessary PSD condition after its small principals passed.
A negative exact matrix certificate would exclude that prescription;
a complete pass would park this specified diagnostic only. Neither
outcome is a uniform bound or an improvement of the 955–957 bracket.

## Primary source applicability

Import Sven C. Polak, *Semidefinite Programming Bounds for Constant-Weight
Codes*, IEEE Trans. Inform. Theory 65 (2019), 28–38,
DOI 10.1109/TIT.2018.2854800;
[arXiv:1703.05171v1](https://arxiv.org/pdf/1703.05171v1),
15 March 2017, Section 1.1 equations (1)–(3), Proposition 1.1 and
its full indicator proof, printed p. 2. The universe consists of binary
words of fixed weight w. Take n=1024, d=10, w=68 and moment order
three. All four proposed indices belong to the singleton-conditioned
index set in (1); each matrix entry is the moment of the union of two
families of supports. These unions have at most three supports.
The displayed proposition's A(n,d) endpoint is qualified by its
constant-weight proof as A(n,d,w), as already recorded in foundations/12.

The same source's A4 and B4 programs are stronger comparisons, requiring
additional moments and matrices. Its following paragraph explains
principal-matrix inclusion and nonnegative lower-order diagonals.
These known programs supply no computed result for this fixed partial
assignment at (1024,10,68). Four matrix indices must not be confused
with moment order four. No fourth-order moment is needed here.

Import A.E. Brouwer and W.H. Haemers, *Spectra of Graphs*, Springer,
2012, ISBN 978-1-4614-1938-9;
[author preprint](https://homepages.cwi.nl/~aeb/math/ipm/ipm.pdf),
Theorem 2.7.1(i), printed p. 36, and Section 2.9 through Lemma 2.9.1
and proof, p. 37; numbering is that of this preprint. The block
congruence requires an invertible leading block. The normalized
leading scalar here is one, since L053 fixes rho>0. The real symmetric
quadratic-form criterion permits singular residual matrices and zero
eigenvalues. For the later finite test use complete exact congruence
certificates with zero residual rows checked, or explicit rational
negative quadratic-form witnesses. Do not invert a singular residual
or rely on leading minors alone. These inputs need no reproof.

## Essential coordinate coverage

Reuse L053 only for its positive rho, all fixed p_i and family-union
conventions; reuse L054's full eight-region dictionary. L056 fixes one
unordered value for every triple having two incident distance-five
pairs, through its unchanged 21 coefficients and represented-orbit
consistency. L057's audited small-principal pass is retained evidence,
not a replacement for the proposed calculation.

The three distinct-triple entries have the following covered scope:

| Entry's support family | Distance-five shell anchor | Pair half-distances | Existing input |
| --- | --- | --- | --- |
| {D,E,F} | D (also E or F) | (5,5,5) | L056 represented unordered value |
| {D,E,G} | E | (5,5,6) | L056 represented unordered value |
| {D,F,G} | F | (5,5,6) | L056 represented unordered value |

The anchor row and repeated family unions use rho, rho*p_5 and
rho*p_6 as appropriate. The family {E,F,G} and the four-support family
{D,E,F,G} do not occur as entry unions for these indices. Thus this
target requires no unrepresented triple value or fourth-order
coordinate. For each covered triple, reconstruct its eight regions
from the full sets, place the indicated shell anchor first, and use
L054/L056's existing r,q dictionary. Distances alone do not select
the coefficient. Retain every eligible alternative-anchor check for
DEF. Do not substitute L053's different distinct-triple formula or
assume p_6=p_5.

## Full incidence scope and later verification

The later calculation must enumerate nonnegative integer membership
atoms for all 16 subsets of {D,E,F,G}, including the outside atom.
Their total is 1024; each support has size 68; each pair intersection
is 63 except D intersection G, which is 62. Keep all compatible
triple and four-way intersections and private atoms. Reconstruct
complete sets from every retained atom vector, check the six distances,
and obtain the entry moments by actual unions of families of supports.
This is the existing fixed-weight source scope, not a restriction to
pair-only incidences or to one common-core pattern.

Permutations within matching atoms preserve this specified invariant
partial assignment. They may compress the test only with complete
coverage justified; they do not transport actual-label RS zeros.
There is a finite bounded integer enumeration task, but no run-time
estimate, enumeration count or mathematical certificate is asserted
here. A verified negative example suffices to reject the prescription.
A claimed pass requires exhaustive coverage and complete exact PSD
evidence, including singular cases. If enumeration cannot be completed,
save the unfinished certificate and report that limitation; do not
infer a pass or silently narrow the approved target.

## Duplicates, obstructions and search limitations

ATTEMPTS/035 concerns L053's different global triple assignment;
ATTEMPTS/038 parks L056's same-anchor full distance-five shell;
ATTEMPTS/039 and history/188 retain only the represented three-index
principals. None tests this coupled four-index matrix with a distance-six
neighbor at D. L054/L055's incidence-zero obstructions remain qualified
to their different restricted prescriptions. Preserve all these stops.

Queries used: `constant weight codes semidefinite triple moments four
principal matrix Polak 1703.05171`; `"constant weight" "1024" "68"
semidefinite`; `"constant weight" "four" "principal" "triple"
semidefinite Polak`; `"A(1024,10,68)"`; and `"constant weight"
"cross-shell" "moments" SDP`. The first search surfaced Polak and
related primary work; the exact-instance and narrow phrases produced
no inspected theorem deciding these coefficients, often only irrelevant
results. Third-party descriptions were not used as theorem evidence.
The broader matrix-algebra thesis arXiv:1007.0906 was an unread lead,
not an essential source: the needed union and congruence statements
were read directly. No novelty follows from these searches.

Unrepresented triples elsewhere, other pair prescriptions, actual-label
zeros, larger/full conditioned PSD, full SDP bounds, representing
measures and common-center RS realization remain unresolved. Matching
Mathlib coverage for this complete certificate and source program is
not checked; supporting coverage remains qualified as in foundations/09,12.
This turn approves source scope only, with no lemma or mathematical
script writes and no new mathematical result beyond the cited tools.
