# Triangle twelve-recovery bound — completed bounded source comparison

TARGET: Determine whether L057's gated fixed-H triangle pencils have at most twelve distinct additional relaxed recovery parameters, retaining both-zero lifts and the original finite exclusions.
CHECKED: 2026-10-10
DECISION: EXPLORE
SEARCH_EVIDENCE: Eight targeted triangle/count, syndrome-pencil, secant and subfield searches; compared L010/L041/L057/L058, L056's different scope, ready counting assessments and ATTEMPTS/008–009,022–024; exact queries and limits below.
SOURCE_EVIDENCE: Chojecki live author TeX v9.2 (July 17, 2026), inspected 2026-10-10: DR0–DR8/DRC statements and proofs, lines 2785–2935; slope-incidence linearization DRC1–DRC2 and proof, lines 2936–2966; fixed-core compiler and proof, lines 3000–3055; residual-kernel and single-circuit compilers and proofs, lines 1370–1460. Reused primary MDS/shortening, BCHKS, Tamo and design coverage identified below.
COMPARISON: L058 gives conditional normalized-weight descent, not a maximum; the ray compiler and incidence identity require a separate zero-fiber estimate and deduplication. Useful fixed-block/core restrictions and structured-design/random-domain hypotheses are not supplied. L056's tau=1 theorem does not cover triangle both-zero lifts. No inspected result supplies twelve.
GAP: Establish or refute the simultaneous twelve bound uniformly over all nine-label triangles and gated weights, counting distinct original finite parameters with all both-zero lifts and zero fourth weights retained; neither a finite maximum nor its original-chart passage is established.
REASON: Essential ingredients have ready coverage and this bounded comparison found no matching import; approve one bounded attempt on the unchanged TARGET without claiming novelty or a bound.
SCOPE: Proposed F_(97^20), fixed order-sixteen H in F_97, k=8 and pinned cell; L057's nine distinct triangle labels, original finite distinct gamma_i, lambda!=0 and p(1-p)q(1-q)r(1-r)!=0; all nonbase four-supports, zero recovered weights, both-zero lifts and unrestricted original infinity. No rational original chart, existence, uniform count or arbitrary extraction is assumed.

LITERATURE_REASON: Checkpoint 135 changed the target from conditional-descent audit to simultaneous counting and saved REVIEW_REQUIRED coverage; this review supplies that missing comparison while reusing unchanged ingredient assessments.

## Original checkpoint 135 review requirements (preserved)

The main gap is arbitrary sixteen-count equality-family exclusion. A
triangle twelve bound could exclude equality in this additional local
pattern; it would leave other patterns, extraction and the challenge
definitions unresolved. Essential proposed inputs are L010, audited L041,
audited L057 and now audited L058. No cross-notebook input is proposed.

Reuse adequate primary recurrence and descent comparisons, then compare
the exact simultaneous counting statement with known stronger bounds and
recorded local failures. Do not infer a count from the recurrence, from
the isolated prime-field descent formula, or from a selected regression.
Do not assume that thirteen recoveries exist. L058's descent applies
conditionally at that threshold and leaves rho and the excluded direction
unrestricted. The handling of original E!=0 must be justified in any
future finite reduction; replacing the chart by a rational one is not
authorized by L058.

After separate approval, continue only with a complete uniform exclusion
of thirteen or an informative bounded obstruction/test toward it. A
counterexample must satisfy every original gate and all eight moments at
thirteen distinct additional finite parameters. Abstract support patterns,
duplicate witnesses and maxima over sampled labelings do not meet that
threshold. The twelve bound is not proved or disproved here, and no
mathematics on this new target had been derived or approved at checkpoint 135.

## Primary exact-count comparison completed at step 136

Przemek Chojecki, *Shortening Bounds for Reed–Solomon MCA*,
[live author TeX v9.2](https://raw.githubusercontent.com/przchojecki/rs-mca/main/RS_MCA_Paving_v9.2.tex),
dated July 17, 2026; inspected October 10. Title/date at lines 122–135
match the reused assessment. This mutable source is not certified
identical to ePrint 2026/1463. Citation anchors below name this version.

Read DR0–DR8/DRC, lines 2785–2935, including both full proofs.
Distinct weighted Vandermonde columns, nonzero multipliers,
redundancy R and support size t<R are required. DR2
(`drc:lem-locator-recurrence`) characterizes support-span membership
by R-t recurrence equations. DR6–DRC (`drc:thm-exact-compiler`)
give a union of pivot ratios over determinantal zero fibers, bounded
by the sum of those fiber sizes. L057 already specializes R=8,t=4,
multiplier x and eta_j=s_(j+1). No changed hypothesis or recurrence
reproof is needed. No twelve estimate for the triangle fibers is supplied.

The proof's zero full recurrence direction, with a solvable full
system, gives a common support intersection excluded from transverse
counting. L057's both-zero vectors arise after quotienting missing
shared columns; its restored equations (9)–(10) still have to hold.
The source's full-vector zero case does not discard these quotient
cases. This distinction is already covered by the ready criterion review.

Read `drc:prop-exact-slope-linearization`, DRC1–DRC2 and its complete
proof, lines 2936–2966. Under the same hypotheses each support
determines at most one finite transverse slope. The incidence's slope
image is exactly the compiler set; its size is the sum of fixed-slope
zero-fiber sizes. This is a counting identity, not an upper bound on
eligible slopes. The explicit aggregation qualification prevents
using a fixed-slope fiber estimate without summing over slopes.
No suitable simultaneous triangle fiber estimate is provided.

Read `thm:bounded-residual-kernel-ray` and
`thm:single-mds-circuit-ray`, including both proofs, lines 1370–1460.
Every counted error support must lie in one fixed U. The bounds are
(t+1)|F|^kappa(U) and, for |U|=R+1 and t<R, binom(R+1,2).
The reused R=8,t=4 circuit bound is 36, already too weak, and the
additional triangle supports need not stay in its nine-label base union.
The circuit proof charges slopes to equalities between affine coordinate
functions in a single circuit lift; L041 expressly distinguishes moment
compatibility from an affine lift through the three actual errors.
Neither source statement is imported as a triangle bound.

Read `thm:fixed-core-determinacy-ray` and its full proof, lines
3000–3055. A fixed agreement core C_0, of size c<=k, must belong
to every selected exact-a noncommon witness; the bound is
binom(n-c,k-c+1). The proof interpolates both rows on C_0 and
assigns each slope a determining subset using fixed-support uniqueness.
L057/L058 supply no prescribed nonempty core for all additional witnesses.
The empty core is allowed but supplies no improved count over the existing
general determining-subset bound.
A core of the base triple cannot substitute for a core of the counted
family. No new core specialization or chart-replacement result is derived.

## Reused stronger-result and ingredient coverage

Read and reuse `2026-10-08-nine-union-simultaneous-recovery-count.md`.
Guruswami–Kopparty, *Explicit Subspace Designs*, March 2013
[author manuscript](https://www.math.utoronto.ca/swastik/subspace-designs.pdf),
section 4.2 Theorem 14 and Claims 15–16, printed pp. 9–10, require
structured full-degree Frobenius/scaling root blocks that are pairwise
disjoint. Their summed intersection-dimension bound concerns the
constructed vanishing-polynomial subspaces. The arbitrary overlapping
four-support moment spans here have no supplied identification satisfying
those hypotheses. Its earlier full-proof extraction is reused, not freshly
retrieved or extended by an unproved duality.

The same assessment covers Goyal–Guruswami–Sun–Wootters,
*Locality of Curve-Decoding and Improved Proximity Gaps*,
[arXiv:2607.08516v1](https://arxiv.org/html/2607.08516v1), Definitions
2.12 and 3.7, Theorem 3.27(1) with proof and Theorem 5.6.
The deterministic theorem needs an established design inequality
tau(r)<R_V(U); the RS theorem samples independent uniform evaluation
points and has further length/field-size hypotheses. These premises
have not been established for fixed H and the relaxed triangle systems.
Conditional normalized-weight descent supplies neither premise.

Read and reuse `2026-10-07-six-coordinate-twelve-incidence-bound.md`
and the BCHKS comparison in
`2026-10-07-six-coordinate-triple-equality-obstruction.md`.
Tamo, [arXiv:2312.12962v1](https://arxiv.org/pdf/2312.12962v1),
Theorem 1.2 and Theorem 5.1 with proof, printed pp. 2 and 15–16,
concern planar polynomial incidence and average-radius lists around one
word. No incidence-preserving identification with this pencil is supplied,
and the saved list bound is too large. Ben-Sasson–Carmon–Habock–Kopparty–Saraf,
*Improved Proximity Gaps for Reed–Solomon Codes*, November 11, 2025
[author version](https://www.math.toronto.edu/swastik/rs-proximity-gaps-2025.pdf),
Theorems 1.3 and 4.6, printed pp. 8 and 28–29, have previously inspected
proofs. The saved dimension-eight comparison uses degree-rate 7/16:
Theorem 1.3 ends at 7/32, below the cell, and Theorem 4.6's coefficient
exceeds sixteen. These unchanged comparisons supply no twelve import.
No finite-constant repair or new numerical bound is attempted.

Reuse Hall, *Notes on Coding Theory*, GRS chapter, Theorem 5.1.1
and full proof, printed pp. 63–64, from
`2026-10-05-two-block-moment-obstruction.md`; and Marquez-Corbella–Pellikaan,
*A characterization of MDS codes that have an error correcting pair*,
FFAA 40 (2016), 224–245, section 5, Definitions 5.1–5.2, Lemma 5.3
and subsequent GRS shortening formula, printed pp. 7–8 of the
2016-02-29 accepted manuscript, from
`2026-10-07-six-coordinate-triple-equality-obstruction.md`.
Their precise citation/specialization record was read in L041 and
`2026-10-07-nine-coordinate-triple-compatibility.md`. Distinct labels
and unit multipliers give dimension eight and distance nine; the seven
successive deletions retain positive dimensions and nonzero differences,
covering L041's one-dimensional shortened kernel. No hypothesis has
changed, so no new standard-theorem extraction or reproof is necessary.

## Duplicates, failures and search limits

Read L010's hypotheses/count/equality statement, L041's full local
statement and standard-input specialization, L057's complete recovery
statement, L058's full proof/audit, and L056's hypotheses/conclusion.
L010 gives sixteen total; L041/L057 give local compatibility; L058
gives conditional weight descent. None supplies the strict count.
Repeating descent is not an advance on this TARGET. L056's h/d-tag
classification and audited computational constraints use different
supports and quotient cases, so its tau=1 numerical result is not a
triangle input. No duplicate of the requested bound was found in these
scoped records; this is not a novelty assertion.

Read ATTEMPTS/008–009,022–024 in full. Preserve the nonsingular
prime-field generator stop, zero-syndrome-kernel blindness and fixed
common-coordinate triple stop. They do not classify arbitrary triangles.
Individual degree sums merely reproduce locator capacities, support-only
recentering admits an abstract survivor, and the unqualified singleton
triple exclusion has an actual tau=1 counterexample. These are individual
route failures, not global bans. The available new input is audited
L058's conditional descent coupled with complete L057 recovery;
determinant-only generation, support counts and replayed capacities
are not discriminating tests of the present target.

Actual new queries issued October 10:

- `"Reed Solomon" "triangle" "correlated agreement"`
- `"Reed-Solomon" "syndrome" "pencil" count`
- `"Shortening Bounds for Reed–Solomon MCA" twelve`
- `"mutual correlated agreement" "sixteen"`
- `"Reed-Solomon" "affine line" "exact" "count" shortening`
- `"Reed Solomon" "triangle" "twelve"`
- `"MDS" "syndrome" "secant" line intersection`
- `"mutual correlated agreement" "fixed" "subfield"`

Hits included the inspected author source, broader MCA papers, campaign
pages, decoding/random-domain summaries and unrelated storage/lattice
items. Only the primary passages specified above were newly inspected
as theorem coverage. Snippets, repository summaries and campaign claims
are unread leads, not bounds. Failed search does not establish novelty.
Parked ABF26/Jo/ECCC source issues remain independent and nonessential
to this local target; no blocked source is assumed as a premise.

## Ready continuation and qualifications

One bounded mathematical attempt on the unchanged TARGET is covered.
Use L010 and audited L041/L057/L058, retaining original finite gates,
both-zero pivots, zero recovered weights and parameter deduplication.
Invoke L058 only conditional on thirteen distinct additional actual
recoveries supplied by L057. Any proposed finite prime-field reduction
must justify passage back to E!=0: rho, gamma_i, lambda and the original
excluded direction have not descended. The literature review supplies
no finite maximum, rational original chart or chart-replacement theorem.

Continue on a uniform exclusion of thirteen, or a rigorous partial
simultaneous restriction or informative bounded test that changes the
next decision. Refutation requires a gated pencil with thirteen distinct
additional original finite parameters satisfying all eight moments and
every L057 exclusion. Sampled maxima, support totals, projected tests
alone and repeated descent do not settle the threshold. If only known
capacities are reproduced, save the attempt and reassess the mechanism.

This literature turn derives no new result and changes no lemma,
mathematical script, DAG or argument overview. EXPLORE approves the
subsequent bounded attempt; no twelve bound or originality is certified.
Full and supporting Mathlib coverage remain **not checked**, with no
absence claim. Other patterns, arbitrary extraction and challenge
definitions remain open; the global interval remains 11/q–16/q.
