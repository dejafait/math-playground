# Ordinary scalar constraints on the simultaneous shell — source scope approved

TARGET: Test whether the unchanged L056 shell and all L060 minimizing columns admit a simultaneous five/six-shell PSD completion satisfying every ordinary scalar inequality on represented unordered triples.
CHECKED: 2026-10-14
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the ready scalar assessment of 2026-10-05 and step 201 mixed-layer/completion comparison; fresh queries were `Schrijver constant weight codes scalar inequalities triple distance fixed moments feasibility` and `"constant-weight" "semidefinite" "1024" "68"`. Read foundations/04,09,10,12 relevant ranges, L021's pair specification, L053's normalization, L056/L059/L061 entry scope, ATTEMPTS/015 and histories/049,201,205. No inspected result decides this changed fixed assignment.
SOURCE_EVIDENCE: Freshly inspected Schrijver DOI 10.1109/TIT.2005.851748 author manuscript III.B (60), (62)–(67) and explanation after (65), printed p. 7; Kim–Toan arXiv:1212.3467v1 III.A Remark 11 and III.B (31)–(35), conditions (i)–(iv), pp. 8–9; Polak arXiv:1703.05171v1 Section 1.1 (1)–(3), Proposition 1.1 and complete indicator proof, p. 2. Canonical source statements remain foundations/04 and 12; reuse foundations/09 and 10 for the already reviewed mixed-layer and singular-Schur inputs.
COMPARISON: The known scalar rows apply to the changed represented triples, including every anchor and the third-distance pair. L061 omits these upper and lower rows; L023/ATTEMPTS/015 certifies another prescription only. Known completion theorems do not impose these affine scalar rows. Stronger four-word and enhanced Kim–Toan inequalities remain outside this target, not evidence against its feasibility.
GAP: Perform the exact finite scalar-plus-PSD application at all unchanged pairs and columns; verify source normalization, all presentations and the full singular-Schur remainder. No scalar evaluation, constrained completion, obstruction or new mathematical result is supplied here.
REASON: Essential theorem coverage and exact changed-slice comparison are now complete. Approve one bounded finite reproduction, preserving the saved target and every prior stop.
LITERATURE_REASON: The added ordinary scalar upper and lower inequalities were explicitly excluded from the ready PSD-only assessment; their complete permutation closure and third-distance pair inputs required separate coverage.
SCOPE: Exactly TARGET; n=1024,w=68,v=956,d=10, L053's unchanged positive rho and full pair prescription, audited L056 shell and every audited L060 minimizing column; the same 28 six/six coordinates may vary. All ordinary scalar rows on represented triples and Boolean repetitions are included. No retuning, label nonfaces, other conditioned/complement matrices, degree-four constraints or global feasibility claim.

## Primary inputs and applicability

Import Alexander Schrijver, *New code upper bounds from the Terwilliger
algebra and semidefinite programming*, IEEE Trans. Inform. Theory 51
(2005), 2859–2866, DOI 10.1109/TIT.2005.851748,
[author manuscript](https://homepages.cwi.nl/~lex/files/codes.pdf),
III.B (62)–(65), printed p. 7. It concerns nonempty binary constant-weight
codes, without linearity or RS hypotheses. The explanation after (65)
uses the included/excluded-anchor indicator averages of (60) for scalar
inequalities and the ordered triple counts for symmetry and distance
zeros. Source equalities preserve t-s as well as the distance multiset.
Use only actual nonzero multinomial orbits and retain repeated words.
The suspect complement prefactor in (61) is unused. Full canonical
statement and qualifications remain in foundations/04; no reproof.

Cross-check and import Hyun Kwang Kim and Phan Thanh Toan,
*Improved Semidefinite Programming Bound on Sizes of Codes*,
[arXiv:1212.3467v1](https://arxiv.org/pdf/1212.3467v1), 14 December 2012,
III.A Remark 11, III.B (31)–(35), printed pp. 8–9. Their hypotheses
are even d>=4 and d<2w<=n, satisfied by 10<136<=1024.
With p_i=y_(i,0)^(0,0), the ordinary rows are

    p_0=1; y>=0; p_i-y>=0; 1+y-p_i-p_j>=0.

Conditions (iii)–(iv) require all source permutation equalities and
zeros when any nonzero pair distance is less than d. Formula (31)
sets impossible multinomial coefficients to zero; these are not extra
scalar variables. Their later strengthened rows are not imported.

Reuse Sven C. Polak, *Semidefinite Programming Bounds for Constant-Weight
Codes*, IEEE Trans. Inform. Theory 65 (2019), 28–38,
DOI 10.1109/TIT.2018.2854800,
[arXiv:1703.05171v1](https://arxiv.org/pdf/1703.05171v1),
Section 1.1 (1)–(3), Proposition 1.1 and its complete indicator proof,
printed p. 2. This supplies the union-index interpretation; its proof
bounds A(n,d,w), qualifying the printed A(n,d) endpoint. Nonnegativity
also follows there from the diagonal cases. Section 1.2's averaging
requires preservation of every constraint. The stronger A_4/B_4 results
are not a verdict for this fixed slice. Foundations/12 retains this
canonical input; no hierarchy theorem is reproved.

Primary PDFs were accessible through the web reader; their text supplied
the formulas and proof cases. No local PDF snapshot/checksum is claimed.
Search results were discovery leads only. The cited small-instance tables,
asymptotic constructions and stronger hierarchies do not establish this
prescribed shell's verdict; no novelty or source absence is inferred.
Full matching Mathlib coverage remains not checked, as in foundations/04,12.

## Exact finite application obligations

L053 fixes rho=M/binomial(1024,68)>0 and the pairs x({A,B})=rho*p_i,
with p_0=1, p_1=...=p_4=0 and
p_i=a_i/[2*binomial(68,i)*binomial(956,i)] for i>=5.
L021's exact Ax=1 specification fixes every a_i; the ready complete
rational evidence is scripts/finite-support/delsarte-lp-results.json.
Use those same pairs, not the values of L053's superseded distinct-triple
trial. L053's critical audit also checks all 0<=p_i<=1. These inputs
are canonical, not new values computed in this review.

For a represented unordered triple, the conditional source coefficient
is its moment divided by the unchanged positive rho. Reconstruct the
source normalization from (62)–(63) and L053 before evaluating rows;
rho, rho*p_5 and rho*p_6 are different normalizations. Do not compare
L056's d5 or L061's d6 directly with p_i. Their actual conditional entries
are p_5*d5 and p_6*d6, respectively; the mixed entries are p_5*t at
L060's unchanged minimizing parameter. Boolean repetition uses its pair
coordinate rather than a distinct-triple prescription.

Use L061's existing eight-atom dictionary, in mask order 0,...,7:

    (956-l-m+j, m-j, l-j, j, i, l-i, m-i, 68-l-m+i).

Here (l,m)=(5,5),(5,6),(6,6), and the old relation indices are
0<=i,j<=min(l,m). It already represents the 36,36,49 respective types.
Their half-distances are l,m,l+m-i-j. Thus the required third-distance
pair inputs extend through 10,11,12 in the three blocks: retain the
unchanged p_0,...,p_12, including Boolean zero and forbidden 1,...,4.
No p_13,...,p_68 enters these represented scalar rows; their global
prescription remains unchanged. Verify these ranges directly from complete
atom representatives during the attempt rather than trusting a cached map.

At each of all six ordered presentations, regenerate source indices
(a,b,t,s), the third half-distance h=a+b-t-s, and original t-s.
Apply the imported slacks y, p_a-y and 1+y-p_a-p_b, with the same
unordered y and actual fixed pairs. This includes anchors whose two
incident distances are outside {5,6}; being absent from the retained PSD
matrix does not remove their scalar rows. In particular the third-pair
upper bound and the two other-anchor lower rows must not be omitted.
Check all source equalities (including closure outside the retained
matrix), original t-s, nonnegative atoms, zeros and Boolean cases.
Distances alone are not an authorized orbit identification. Source closure
can represent the same coordinate outside the matrix without requiring
another PSD matrix. Do not introduce a new free triple there.

Retain exactly the L061 free-coordinate partition: six/six r+q=5
entries are fixed by transported minimizing columns; r+q>=6 supplies
28 free entries, with the old diagonal and forbidden entries fixed.
First check all fixed rows; an exact violation there excludes every
completion of this prescription. Otherwise the added affine rows must
be imposed on those free coordinates together with the full existing
PSD criterion. Reuse audited L061's mixed-layer and generalized-Schur
coverage (foundations/09,10), checking all singular-mode equations and
all remainder coordinates for any changed witness. L061's particular
assignment is only a proposed starting witness.

Point permutations preserving the anchor and its complement preserve
ordinary distances and the represented full-region data. The existing
unlabeled stabilizer reduction is relevant, but the attempt must verify
that its added scalar/permutation rows are preserved before averaging.
No actual-label restriction is averaged or assumed satisfied. Do not
invoke unconstrained chordal/free-cross-block completion as a substitute
for the affine rows; the existing comparison already rules out that use.

## Duplicates, downstream use and bounded decision

L023's full scalar supplement and ATTEMPTS/015 retain the old all-orbit
pass. Its prescription differs from L056's released shell and the
minimizing columns. It is neither a witness nor an obstruction here.
ATTEMPTS/038–043 retain the necessary-PSD stops at these newer inputs;
adding precisely the omitted ordinary scalar rows is a separately
covered constraint test, not a repetition of their PSD-only verdicts.

Main gap: arbitrary-center safety at 67/68 agreements in the 955–957
bracket. Intermediate target: the exact saved scalar-plus-PSD completion
question. A verified obstruction could identify a necessary ordinary
constraint missing from this fixed prescription; a verified feasible
completion would park this stronger diagnostic. Neither resolves the
main gap or establishes progress beyond the assessed known methods.

Continue only to this finite test. A complete rational witness must check
every represented type, all six presentations and Boolean cases, every
scalar row and all retained PSD modes independently. Excluding all
completions requires a fixed-entry contradiction or an exact separating
certificate for the whole constrained slice. Failure of L061's particular
witness, a numerical solver report, samples or a preview cannot exclude
all 28-coordinate choices. An inconclusive computation stays unfinished.
Save full exact certificates with all failures and report actual/required
bounds; no calculation was run in this literature turn.

Essential inputs: L021,L053,L054,audited L056,L059,audited L060,audited
L061 and their complete certificates; foundations/04,09,10,12.
Off-shell/global PSD and moment consistency, actual-label constraints,
representing measures, RS realization and both boundary indices remain
unresolved. No complete candidate resolution is proposed.
