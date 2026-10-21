# Reanchored seven-distance principal diagnostic — source scope approved

TARGET: Test all four-index conditioned principal matrices on support quadruples with half-distances (DE,DF,DG,EF,EG,FG)=(5,5,7,6,5,5) at L062's unchanged represented moments.
CHECKED: 2026-10-14
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 214 compared L053,L056,L057,L058,L061,L062,L063, foundations/04,09,12, ATTEMPTS/015,038–040,043–045 and scoped histories/assessments; exact distance-pattern and reanchored-moment searches found no inspected fixed-coefficient verdict. No incidence enumeration was performed.
SOURCE_EVIDENCE: Freshly read Polak arXiv:1703.05171v1 Section 1.1 (1)–(3), Proposition 1.1's complete indicator proof and following principal/nonnegative cases, p. 2; Brouwer–Polak arXiv:1709.02195v1 Section 2 (1) and orbit discussion, p. 2; Brouwer–Haemers author preprint Theorem 2.7.1(i), p. 36 and Section 2.9/Lemma 2.9.1's full proof, p. 37. Reuse foundations/04,09,12 and the ready small-principal/four-index assessments.
COMPARISON: All four triples have two incident distance-five pairs and hence use L056 values retained by L062. L061 covers E/F anchors by principal restriction; D/G each have a distance-seven neighbor outside its layers. L057 supplies only smaller principals, L058 a different distance pattern, and L063 a complemented five/six matrix. None of these inspected results supplies the remaining coupled verdict.
GAP: Exhaustively enumerate feasible full sixteen-atom incidences and check all four anchored matrices at the unchanged dictionary, especially D/G. No feasible-case count, matrix sign or PSD verdict has been calculated in this review.
REASON: Exact coordinate and primary theorem coverage are complete for this finite specialization; citation alone does not determine the remaining matrix signs. Approve only the saved target for a later REPRODUCTION calculation, without retuning or reproving the hierarchy.
LITERATURE_REASON: The changed distance-seven and all-anchor scope was REVIEW_REQUIRED after the parked complemented test; essential coordinate and duplicate comparison was missing. Existing theorem assessments are reused rather than refreshed wholesale.
SCOPE: Exactly TARGET with all sixteen membership atoms, all four anchors, Boolean family-union pairs, unchanged rho and p_i, and L062's represented unordered moments; no new moments, optimization, labeled zeros or global feasibility claim.

Main gap: arbitrary-center safety at 67/68 agreements, bracket 955–957.
Proposed intermediate target: for every feasible full sixteen-atom
incidence of the specified quadruple, test the four-index included-anchor
matrix at each anchor A. Its indices are {A} and {A,B} for the other
three supports, with entries x(I union J)/rho. Retain Boolean pair
entries, every original p_i and exactly L062's represented triple values.
There is no fourth-order moment or free optimization variable in this
proposal. Do not extend a formula to an unrepresented triple silently.

Essential inputs: L021,L053,L056,L059,L060,audited L061,
audited L062 and audited L063; L057,L058 for duplicate comparison;
foundations/04,09,12. The original proposal required confirmation of
fixed coordinates and a nonduplicated coupled test. Step 214 supplies
that source-scope comparison below, without a mathematical verdict.

Plausible downstream use: a negative exact principal minor would expose
a cross-anchor incompatibility of this one assignment outside the retained
layers; an exhaustive exact pass would park only this specified pattern.
Continuation test: step 214 approves coverage and the finite dictionary;
the D/G coupled verdict is not supplied by the inspected results.
Later mathematical test: exhaustive feasible region
enumeration and all principal minors at all anchors, with exact failure
evidence or a complete finite pass. No enumeration or verdict is supplied
by this proposal. Keep ATTEMPTS/015,038,043,044,045 and all earlier stops.
Other assignments, larger conditioned matrices, unrepresented rows,
global PSD/moments, labels, measures, packings and RS realization remain
unresolved. Mathlib matching coverage has not been checked.

## Primary theorem comparison — step 214

Import Sven C. Polak, *Semidefinite Programming Bounds for Constant-Weight
Codes*, IEEE Trans. Inform. Theory 65 (2019), 28–38,
DOI 10.1109/TIT.2018.2854800;
[arXiv:1703.05171v1](https://arxiv.org/pdf/1703.05171v1),
15 March 2017, Section 1.1 (1)–(3), Proposition 1.1 and its complete
indicator proof, printed p. 2. For binary fixed-weight words, the
order-three singleton-conditioned indices include the anchor and its
unions with one other support. Their entry families contain at most
three supports. Apply at n=1024,d=10,w=68; four matrix indices do not
require fourth-order moments. Retain the printed A(n,d) endpoint
qualification: the proof establishes A(n,d,w).

The ensuing principal-inclusion and nonnegative-diagonal cases were
also read. They do not identify distinct singleton anchors' matrices.
The stronger A4/B4 programs introduce additional coordinates and
constraints and provide no verdict for this fixed partial assignment.
No hierarchy or source theorem is reproved.

Cross-check Andries E. Brouwer and Sven C. Polak, *Uniqueness of codes
using semidefinite programming*,
[arXiv:1709.02195v1](https://arxiv.org/pdf/1709.02195v1),
7 September 2017, Section 2 (1), printed p. 2. This explicitly uses
nonnegative moments and the same union indices. The orbit discussion
requires a constraint-preserving action. Here atom bijections may
transport this ordinary invariant dictionary; no labeled RS averaging
or uniqueness conclusion is imported.

Reuse A.E. Brouwer and W.H. Haemers, *Spectra of Graphs*, Springer,
2012, ISBN 978-1-4614-1938-9,
[author preprint](https://homepages.cwi.nl/~aeb/math/ipm/ipm.pdf),
Theorem 2.7.1(i), printed p. 36, and Section 2.9 through Lemma 2.9.1
and its complete proof, p. 37; both freshly inspected. The Schur
congruence requires a nonsingular leading block; after division by
positive rho the leading scalar is one. The real symmetric PSD and
congruence criteria allow singular residuals. A later certificate must
check an invertible congruence and all zero residual rows, or provide
a rational negative quadratic form. Retain every principal minor;
leading minors alone are not the proposed verification.

## Represented values and duplicates

L053 supplies rho and the unchanged L021 pair prescription, not its
superseded distinct-triple trial. L056 supplies the following four
unordered moments, retained in L061/L062:

| Triple | Sorted half-distances | Two-five shell anchor | Input value |
| --- | --- | --- | --- |
| DEF | (5,5,6) | D | L056 five/five dictionary |
| DEG | (5,5,7) | E | L056 five/five dictionary |
| DFG | (5,5,7) | F | L056 five/five dictionary |
| EFG | (5,5,6) | G | L056 five/five dictionary |

This is conditional scope coverage for any quadruple with the specified
distances, not an existence or enumeration result. Use L057's existing
full-region recipe at the indicated anchor: r=63 minus the common
triple intersection size, q=the other pair's half-distance minus r,
and y=p5*d5_(r,q). Each two-five shell triple belongs to its represented
dictionary. Full regions, rather than distances alone, select r,q.
Check each presentation against L062's canonical unordered-orbit key.
The singleton and Boolean pair entries remain rho and rho*p_i;
p7 is the original fixed pair, not p5 or p6. At an anchor A the only
three-support entries are the three triples containing A. Across all
four anchors exactly the four triples above occur. A four-support
moment never occurs.

For duplicate comparison, L061's full included-anchor matrix retains
all neighbors at distances five and six. E and F have incident
distance multisets (5,5,6), so their proposed matrices are principal
restrictions of that audited result, using its retained unordered
values. Keep them as consistency controls in the exact saved target.
D and G have incident multiset (5,5,7), so each requested index family
includes a pair outside L061's retained layers. They cannot be read
off as principal restrictions of that matrix. This comparison does
not prove abstract logical independence from all available constraints;
no inspected theorem or recorded certificate establishes those coupled
matrices. Their finite signs remain the test.

L057 already covers the three-index anchor-containing principals for
every L056 represented triple, including distance-seven presentations,
but does not establish the new four-index coupling. L058 covers only
(5,5,6,5,5,5), whose multiset of six pair distances differs from this
target; relabeling four supports does not identify them. Its atom
enumeration method is reusable, not its finite pass. L063 certifies
excluded-anchor coefficients p_h-y on layers five/six, rather than the
included-anchor union matrix with a distance-seven index. L062's scalar
pass assigns the required values but proves no additional anchored PSD.
ATTEMPTS/015,038–040,043–045 remain parked with their original evidence.
No test on an already parked matrix is reopened.

## Bounded search and approved continuation

Queries on 2026-10-14 were `"constant-weight" "four" "principal"
"semidefinite" Polak`, `"constant-weight" "5,5,7" semidefinite`, and
`"constant-weight" "reanchored" moments semidefinite`. They surfaced
the known Polak framework and Brouwer–Polak comparison, not an inspected
exact-assignment verdict. Third-party search descriptions were not
theorem evidence. Related higher-order programs are comparisons only;
no essential unread lead remains. A failed search establishes no novelty.
The ready 2026-10-12 reanchored and four-index assessments and
2026-10-14 simultaneous/complemented coverage were reused where applicable.

The next calculation keeps the exact TARGET. Enumerate all nonnegative
integer membership atoms for four 68-subsets of 1024 points satisfying
all six distances; include outside, common-four, triple, private and
pair regions. Establish completeness before using representatives.
Reconstruct every triple by set operations and use only the fixed
dictionary above. Test all anchors and every nonempty principal subset,
retaining singular cases, and independently verify the complete finite
evidence. A negative minor with a valid full-incidence witness rejects
this assignment; an exhaustive exact pass parks only this pattern.
No feasibility count or sign is predicted here. If reconstruction needs
an unrepresented value or changes a moment, stop and seek separate
coverage instead of extending the formula.

The main gap and 955–957 bracket remain unchanged. Other assignments,
larger matrices, global consistency/PSD, labels, measures, packings and
RS realization are independent unresolved steps. Full matching Mathlib
coverage for this diagnostic and supporting hierarchy/PSD machinery is
not checked; unknown coverage is not absence. This literature-only
approval creates no lemma, mathematical script or new finite result.
