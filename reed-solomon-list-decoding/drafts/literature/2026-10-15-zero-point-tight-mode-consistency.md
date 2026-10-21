# Fixed zero-point tight-mode consistency — source scope approved

TARGET: Test consistency of the 24 positive-weight mode equalities in L067's seven/seven completion variables at L069's fixed u=v=0,w=w_star point, retaining all forced entries.
CHECKED: 2026-10-15
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 239 searched constant-weight SDP complementary slackness, prescribed zero moments and zero-dual linear consistency; compared the ready L067/L068 assessments, canonical L061,L062,L065,L067,L068,L069 and ATTEMPTS/049,050,051. Queries and inspected passages are below; no checked result gives this fixed system's verdict.
SOURCE_EVIDENCE: Reuse Schrijver DOI 10.1109/TIT.2005.851748 Proposition 5 (44)–(47), Theorem 1 (51), III.A (52)–(59), III.B (64); Sano DOI 10.1007/s44146-026-00231-y Section 2 Corollary 2.2, Theorem 2.6 and Lemma 2.7; Polak arXiv:1703.05171v1 Sections 1.1–1.2. Freshly read Brouwer–Polak arXiv:1709.02195v1 Section 2.1 (2)–(3) and scalar-block argument, pp. 2–3; Ye, Conic Linear Programming, October 2017 revision, Section 2.3 opening p. 42, Theorem 1.11 p. 13 and Section 1.5.1 pp. 23–24. Canonical sources: foundations/04,09,10,12.
COMPARISON: Known scalar complementary slackness covers necessary tightness when nonnegative slacks have an exactly zero weighted sum; exact linear-system alternatives cover a solution or left-null certificate. The mixed-layer and singular-Schur inputs are unchanged. None supplies this fixed-point consistency verdict. L067 rejects different fixed columns; L068/L069 do not solve new/new entries.
GAP: Reconstruct and test the exact 24-by-36 equality system from original normalized data at the audited fixed point, independently checking all forced entries, cancellations, right sides and the final certificate. No rank, solution, inconsistency or PSD completion has been calculated in this review.
REASON: Essential source coverage now suffices for one bounded REPRODUCTION attempt at exactly TARGET; import standard complementarity and elimination without reproof. No source blocker requires another literature turn.
LITERATURE_REASON: This newly proposed necessary-equality target was outside the completed scalar audit and required checking the zero-weighted-slack implication and original normalization; reuse adequate mixed-layer coverage rather than repeat discovery of that algebra.
SCOPE: Only L069's fixed u=v=0,w=w_star, original positive rho,p7, unchanged L061/L062 base and pairs, L067's 36 seven/seven variables, all forced entries and its unchanged 24 positive weights. Test equality consistency over the rationals/reals with signed free variables; a solution need not satisfy nonnegativity or remaining inequalities. No parameter, pair, base or dual retuning.

Main gap: arbitrary-center safety at 67/68 agreements. The intermediate
target tests a necessary linear consistency condition at the audited
zero point, using the original spectral modes rather than adding more
column scalar rows. Essential inputs: L061,L062,L065,L067,L068,L069,
foundations/04,09,10,12 and their precise assessed source statements.
Step 239 approves this scope for one later mathematical attempt, using
adequate existing coverage and the source comparison below. No completion
calculation or repeat L069 audit was performed in this literature turn.

Proposed downstream use: a certified inconsistency would reject this fixed
completion point; consistency would justify only a later separately
assessed test of the remaining inequalities. The discriminating test is
an exact rational solution or a rational left-null contradiction for the
specified affine system. Its scope must be checked before implementation.
Neither outcome decides the entire u,v plane, simultaneous PSD, all scalar
rows, global moments, labeled restrictions or RS realization. Preserve
ATTEMPTS/049,050,051 and L067's immutable obstruction.

## Reused coverage and precise source comparison

Reuse `2026-10-14-simultaneous-five-six-seven-shell-extension.md` and
`2026-10-15-seven-shell-affine-family-fixed-dual.md` in this directory.
Their primary theorem statements and relevant proofs already cover the
unchanged unequal-layer algebra, whole-block singular range/Schur test
and union-moment interpretation. Schrijver's
[author manuscript](https://homepages.cwi.nl/~lex/files/codes.pdf),
at the locations in SOURCE_EVIDENCE, permits factor sizes 68,956 and
layers 0,5,6,7, including singular and new-only modes. Sano's
[Theorem 2.6](https://link.springer.com/article/10.1007/s44146-026-00231-y)
allows a singular retained PSD block; its range condition cannot be
dropped. Polak's [v1](https://arxiv.org/pdf/1703.05171v1), Section 1.1
Proposition 1.1/proof, p. 2, and Section 1.2, p. 3, requires equal-union
moments and constraint-preserving averaging. Retain the constant-weight
qualification in foundations/12. No actual-label averaging is licensed.
These are reused passages, not new external readings in this turn.

The canonical new source comparison is in foundations/10, section
“Complementary slackness and equality consistency”. Freshly read
[Brouwer–Polak v1](https://arxiv.org/pdf/1709.02195v1), Section 2.1,
equations (2)–(3) and the complete following scalar-block argument,
printed pp. 2–3; and [Ye's author course monograph](https://web.stanford.edu/class/msande310/sdpmain.pdf),
October 2017 revision, Section 2.3 opening, printed p. 42. The latter's
direct scalar argument is sufficient here; no optimality, Slater,
attainment or strict-complementarity converse is needed. The coding
paper's final displayed implication swaps its primal/dual program labels;
the preceding correctly identified product argument is the comparison.
Its code-uniqueness conclusions are unused.

Ye's Theorem 1.11, printed p. 13, supplies the linear-system alternative;
the theorem is stated there without proof. Section 1.5.1, pp. 23–24,
gives the complete elimination/back-substitution description. Rational
input and exact rational operations are the intended specialization;
the final solution or contradiction must be directly checked. No
elimination, rank comparison or new local mathematical result is
performed in this literature turn.

The Boyd author slides and book URLs returned browser errors today.
Their previously inspected coverage is preserved; the freshly readable
scalar source makes these failures nonessential. Reuse foundations/10's
free-entry completion comparison: unrestricted completion theorems do
not impose this moment dictionary. No repeated access recovery is needed.

## Exact application scope for the later calculation

Use L067's inequality (1) in its stated orientation, retaining its
definitions of H, F, A and R. Select precisely the modes with lambda_ab>0
from its displayed h,k, namely a=0,...,5 and b=0,...,3. Take equality
in those 24 rows only. The 36 column indices are (r,q) in {0,...,7}^2
with r+q>=7. Preserve the source scaling
Y_(7,7,7-r,7-q)=p7*z_(r,q)/v_(r,q), with L067's positive v_(r,q).
Do not substitute raw triple moments for z or reverse the row sign.

Keep the forced seven/seven Boolean entry p7, forbidden entries at
1<=r+q<=4, and the reanchored L065 column values for r+q=5,6.
At the fixed point recover c,a^42 from L065's original RREF and
w_star=beta/alpha from L068's exact M, as retained by audited L069.
Do not use L067's older w=-c4/a^42_4. All old L062 entries, original
pairs and positive rho,p7 remain fixed. In particular retain
rho=((binomial(1024,64)/binomial(68,64)+1)/2)/binomial(1024,68)
and p7=3539/248922676958508, rather than refitting a normalization.

The necessary-tightness comparison applies to the nonnegative Schur
slacks in L067 (1), using L068's exact weighted zero at this point and
the unchanged cancellation of every free coefficient. These identities
are existing inputs, not a new feasibility conclusion. Research must
reconstruct and verify them in the original data, retain all singular
ranges and the full anchor correction, and then apply the cited scalar
complementarity implication. Do not assume the full SDP optimum equals
a dual value or replace a weighted inverse action by an unweighted
quotient inverse. A coherent positive congruence is already supplied
by audited L067/L068; all row scalings used in the system must match it.

This is an equality-only test with signed free variables. A contradiction
needs an explicit rational left-null vector with nonzero pairing against
the reconstructed right side. A pass needs an exact rational solution
substituted into every original selected row, with all forced-entry
and unordered-key checks retained. A rank report alone is insufficient
as the saved proof certificate. Nonnegativity, zero-weight modes, new/new
ordinary scalar rows and all other constraints are outside this verdict;
do not expand to them in the same attempt. An exact equality solution
does not establish simultaneous PSD or full SDP feasibility.

## Search record and route comparison

Queries on 2026-10-15:

- `"constant weight" "semidefinite" "complementary slackness" prescribed moments`
- `"semidefinite" "dual" "zero" "linear equations" complementary slackness feasibility`
- `"Schrijver" "prescribed" "zero" "constant-weight" semidefinite`
- `"1709.02195" complementary slackness dual`

Discovery led to the primary passages above and general facial-reduction
material. Search snippets and secondary presentations were not imported.
Facial reduction and matrix complementarity are broader leads, not
essential unread inputs to this scalar equality test. No checked source
evaluates these prescribed numerical rows; this does not establish novelty.

Targeted local search found no duplicate consistency verdict. ATTEMPTS/049
and L067 retain the immutable-point obstruction. ATTEMPTS/050 and L068
park uniform strict exclusion by the fixed dual, with an attained zero;
ATTEMPTS/051 and L069 park column scalar exclusion there. Their stops
remain intact. This independently testable linear target changes the
necessary condition, without reopening the failed scalar repair.

Approve one later REPRODUCTION attempt at exactly TARGET under this
SPECIALIZE assessment. Full matching Mathlib coverage for this prescribed
system, complementary slackness and linear-system alternative is not
checked; unknown availability is not evidence of absence. No lemmas or
mathematical scripts were written or run; PROOF.md and DAG.md are unchanged.
