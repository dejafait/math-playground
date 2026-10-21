# Fixed zero point — remaining nonnegative mode feasibility, source scope approved

TARGET: Test whether L070's 13-dimensional equality solution space contains a nonnegative seven/seven assignment satisfying all remaining 40 mode inequalities at the fixed zero point.
CHECKED: 2026-10-15
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 243 searched the specific zero-point/seven-shell assessments, history/239–242 and ATTEMPTS/049–052; no completed duplicate remaining-mode verdict was found. Reused prior mixed-layer discovery and compared canonical L067/L070. Fresh primary-source discovery for linear-inequality alternatives and rational LP certificates is recorded below.
SOURCE_EVIDENCE: Reuse foundations/04,09,10,12: Schrijver Proposition 5 (44)–(47), Theorem 1 (51), III.A (52)–(59), III.B (64); Sano Section 2 Corollary 2.2, Theorem 2.6, Lemma 2.7; Polak v1 Sections 1.1–1.2; Ye October 2017 equality/complementarity passages. Freshly read Goemans Lecture 3 (19 September 2001), Theorems 1/proof and 3, printed pp.1–2; MIT 6.854 2020 LP notes, standard-form conversion and basic-feasible-solution/rational representation passages; precise links and qualifications in foundations/10.
COMPARISON: Known mixed-layer and singular-Schur results cover the unchanged matrix reduction, and ordinary moment nonnegativity is already assessed. Farkas and rational LP certificate coverage cover exact testing of the resulting finite affine constraints, including singular equality systems. No inspected theorem decides these fixed coefficients; L070 proves only signed equality consistency and L067 uses a different column.
GAP: Reconstruct and test all original 40 remaining mode inequalities and all 36 nonnegativity conditions on L070’s 13-dimensional equality space at the fixed point, preserving the original 24 equalities, forced entries, singular ranges and full anchor correction. No feasibility verdict or coefficient calculation is made in this review.
REASON: Essential coverage is sufficient for one bounded REPRODUCTION calculation at exactly TARGET; specialize the known finite LP certificate machinery without reproof. No essential source blocker remains.
LITERATURE_REASON: The changed target adds nonnegativity and 40 previously untested mode inequalities beyond the approved equality-only scope; this review adds the essential inequality-alternative comparison while reusing adequate matrix coverage.
SCOPE: Fixed u=v=0,w=w_star only; unchanged L061/L062 base, L065 RREF, L068 zero, L069 pairs and column, L067 original 64 rows and original 36 v-scaled variables, L070's exact 24 equalities. No new/new scalar upper rows, parameter variation, base/pair retuning, alternate labeling or global feasibility claim.

The main gap is arbitrary-center safety at 67/68 agreements; the
955–957 bracket is unchanged. The intermediate target would determine
whether the equality pass survives the remaining joint-mode necessary
conditions together with nonnegative new moments. A negative certificate
would reject only this fixed point. A passing assignment would supply
an input for a later assessed new/new scalar or other-matrix test.

Essential local inputs: L061,L062,L065,L067,L068,L069,L070 and
foundations/04,09,10,12. Retain original positive rho,p7, every old and
column lookup, all 28 forced seven/seven entries and complete unordered
equalities, all 64 singular range conditions, full anchor correction,
and the original positive v_(r,q) scaling. The signed particular solution
is not assumed nonnegative. The original 13 free coordinates may vary;
the column parameters u,v,w may not. No remaining inequality was tested
while choosing this continuation.

Continuation/abandonment test: in the later research turn, require either
an exact rational assignment checked against every original row and sign
condition, or an exact rational separating certificate checked against
the unreduced system. A numerical solver status alone is insufficient.
Any infeasibility parks only this point; it cannot exclude the whole
zero plane or other moments. A pass does not settle new/new ordinary
scalar rows, other anchored/complemented matrices, global moments,
labels, representing measures, RS realization or the main target.

Preserve ATTEMPTS/049–052: the immutable obstruction and the later
dual/scalar/equality passes are distinct findings. Step 243 approves this exact scope for the next research turn; it performs
no dependent calculation. Full matching Mathlib coverage is
unchecked, not asserted absent.

## Source comparison and applicability

Reuse the approved assessments
`2026-10-14-simultaneous-five-six-seven-shell-extension.md`,
`2026-10-15-zero-point-tight-mode-consistency.md` and
`2026-10-15-zero-point-tight-mode-critical-audit.md`. Their mathematical
source hypotheses are unchanged. Schrijver’s factors are 68 and 956,
with layers 0,5,6,7 in range. Sano allows singular retained PSD blocks;
all range conditions and the complete anchor congruence remain essential.
Polak’s ordinary union-moment interpretation permits only
constraint-preserving averaging, with no actual subgroup-label symmetry.
These primary passages and their proof cases are reused from
foundations/04,09,10,12, not claimed freshly browsed today.

The original 64 mode rows are L067 equation (1), with positive
v_(r,q) and p7. Only the column changes to L069’s exact point, as in
L070; no L067 immutable right side may be reused without reevaluation.
L070’s 24 selected equalities and rank-23 solution space are established
inputs. All other 40 mode rows are retained. Nonnegativity concerns the
36 original z variables (equivalently their positively scaled raw Y
entries), not signs of the 13 affine parameters. The signed particular
solution alone is not a feasible witness. Keep all 28 forced entries
and all unordered presentations. No new/new scalar upper row is added.
This identifies the already formulated problem’s scope, without forming
or solving any new row in this literature turn.

Fresh inequality coverage is recorded canonically in foundations/10,
“Polyhedral feasibility certificates”.
[Goemans’s Lecture 3](https://ocw.mit.edu/courses/6-854j-advanced-algorithms-fall-2008/b23096080e3d2142c3c8337bdcd9d3c7_lect9_19.pdf),
Theorems 1 and 3, printed pp.1–2, supplies the standard finite Farkas
alternatives, without a Slater assumption. The projection proof and
strict-sign ending were read. This is a linear alternative, not a
claim that general SDP infeasibility always has a strict separator.
[MIT’s LP notes](https://courses.csail.mit.edu/6.854/20/Notes/n11-lp.html)
supply the standard-form, basic-solution and rational-representation
coverage specified in foundations/10. No reproof is needed; the local
work is the exact application to prescribed rational coefficients.

A numerical LP may guide discovery, but the research result must provide
a rational witness checked in every original equality, remaining mode
row and sign condition, or a rational separating combination checked
against the unreduced constraints with its strict contradiction.
Any reduced-coordinate certificate needs an explicit checked translation
back to those rows. Save full coefficients, reconstruction and residual
checks on disk; a solver status is not evidence. Degenerate equality
rank and zero mode slacks must remain allowed. No certificate, numerical
solution or sign test has been generated here.

## Search, duplicates, failures and route decision

Targeted local queries were `remaining 40`, `13-dimensional`,
`remaining-mode` and `Farkas` in the zero-point/seven-shell assessments
and history/239–242, followed by the relevant proofs in L067/L070 and
ATTEMPTS/049–052. The supplied current assessment was the only exact
remaining-mode target; history/242 proposed it without solving it.
The previous broader discovery and source comparisons are reusable:
no new search for the same mixed-layer theorem was necessary.

Fresh external queries on 2026-10-15 were
`site.web.stanford.edu "Ye" "Theorem 1.12" Farkas`,
`site:stanford.edu/class/msande310/sdpmain.pdf "Farkas" "Ax"`,
and `site:mit.edu Farkas lemma lecture notes Ax b nonnegative pdf`.
Stanford bounded source retrieval failed as documented in foundations/10;
search extracts did not establish coverage. The complete relevant MIT
PDF theorem/proof passages and HTML basic-solution argument were readable.
The OCW wrapper is Fall 2008, while the actual Lecture 3 is dated
19 September 2001; these versions are distinguished. Goemans’s later
strong duality statement and unrelated results are not needed or imported.
No inspected source supplies the finite system’s verdict; this is not
a claim of novelty. Full matching Mathlib coverage remains unchecked.

L067 rejects the old immutable column. L068 parks the unchanged dual’s
strict exclusion on the affine family; L069 parks the column scalar
repair; L070 parks equality-only exclusion at this point. None tests
joint feasibility of the currently proposed inequalities and signs.
Their stops remain preserved. This is a discriminating next test using
the existing equality reduction, not repetition of those parked tests.
A pass could support a separately assessed new/new scalar test; a negative
certificate parks only the fixed point and requires a changed target
before further dependent work. Global and RS gaps remain independent.
The main argument and DAG do not change in this source-only review.
