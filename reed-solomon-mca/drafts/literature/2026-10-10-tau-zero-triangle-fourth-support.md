# Tau-zero triangle fourth-support criterion — completed source comparison

TARGET: Determine an exact additional-four-support recovery criterion for L041's tau=0 union-nine pattern (n_01,n_02,n_12)=(1,1,1), retaining arbitrary original finite parameters and initially zero recovered weights.
CHECKED: 2026-10-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Six narrow affine-syndrome, fixed-support recurrence and triangle queries on 2026-10-10; compared L041, L043 and L016's analytic quotient with L010 and ATTEMPTS/008–009,022–024; scoped local searches found no matching triangle criterion in the checked records.
SOURCE_EVIDENCE: Reinspected Chojecki live author TeX v9.2, dated July 17, 2026, DR0–DR8/DRC, lines 2785–2935, including both complete proofs and zero-direction cases; reused inspected Hall Theorem 5.1.1 pp. 63–64 and Marquez-Corbella–Pellikaan section 5 pp. 7–8 through the saved extracts named below.
COMPARISON: DR2 and DR6–DRC cover full fixed-support recurrence membership and finite transverse recovery over F; L041 already supplies this triangle's local weights, but L016/L043 eliminate a different shared-column configuration and do not supply the triangle specialization or its count.
GAP: Eliminate the three pair-only shared columns, make the projected label test usable in the three L041 free weights, and recover every lost coefficient and fourth weight with the original finite exclusions; this specialization is not yet proved.
REASON: Essential coverage is ready for one bounded REPRODUCTION attempt on the unchanged TARGET; this review approves applicability and an elimination task, without deriving or certifying its criterion.
SCOPE: Exact TARGET only: F=F_(97^20), fixed order-sixteen H in F_97, k=8, pinned four-omission cell, L041 local converse tau=0 and (n_01,n_02,n_12)=(1,1,1), three distinct original finite gamma_i, arbitrary F weights, nonzero lambda and all three pair-weight gates; any additional four-support, initially zero recovered weights, unrestricted original excluded direction. No equality, rational chart, count bound or extraction premise.
LITERATURE_REASON: The changed three-pair-only pattern was REVIEW_REQUIRED; its zero-direction and recovery scope needed separate comparison rather than reuse of the ready tau=1 assessment verbatim.

The local setup remains F_(97^20), the fixed order-sixteen H, k=8 and
the pinned radius cell. Use L041's local converse with three distinct
original finite gamma_i, nonzero lambda and the full nonzero-weight
gates at the three pair-only coordinates. There are no triple-common
labels; each support has two singleton labels. Treat these as the
specified L041 hypotheses, not as a new classification result.

Essential local inputs to assess are L010 and audited L041. L043 is a
method comparison, not a theorem for this changed pattern; L056 closes
the tau=1 branch and supplies motivation only. Reuse the saved primary
recurrence extraction in
`2026-10-08-nine-union-fourth-support-incidence.md` where adequate,
after checking its hypotheses and proof cases. Compare the existing
`2026-10-07-nine-coordinate-triple-compatibility.md` assessment too.
No cross-notebook input is proposed.

The sought criterion must handle every additional four-support, all
projected ranks and zero projected directions, actual full eight-moment
membership, every finite denominator, the three base-parameter exclusions,
and initially vanishing recovered weights. An equivalent restatement of
linear-system membership alone is not a count improvement. The plausible
downstream use is a simultaneous additional-parameter bound for another
L041 branch. Neither a count nor extraction of this pattern from every
equality pencil is assumed or established.

Continue only if the specialization produces usable projected label tests
and explicit equations in the three pair weights, with complete recovery
of the information lost by quotienting. If the attempt yields only the
generic recurrence restatement, or an unresolved exceptional case, save
that gap and reassess before counting. A source/local formula matching the
whole target should be imported rather than reproved. The L056 audit
selected this continuation without attempting it; today's work remains
literature-only.

## Primary result and exact applicability

Przemek Chojecki, *Shortening Bounds for Reed–Solomon MCA*,
[live author TeX v9.2](https://raw.githubusercontent.com/przchojecki/rs-mca/main/RS_MCA_Paving_v9.2.tex),
dated July 17, 2026, reinspected October 10. The mutable source is not
certified identical to ePrint 2026/1463. Citation anchors are
`drc:lem-locator-recurrence` (DR2) and `drc:thm-exact-compiler`
(DR6–DRC); read definitions and both full proofs, lines 2785–2935.
For distinct weighted Vandermonde columns with nonzero multipliers,
redundancy R and support size t<R, DR2 equates span membership with
the R-t locator recurrences. Its proof identifies the annihilator as
multiples of the support polynomial and checks its dimension.
The compiler treats arbitrary syndrome pairs: a nonzero recurrence
direction and proportional recurrence vectors give a unique finite
parameter through a nonzero pivot. With zero direction there is either
no solution or a common intersection, excluded from transverse slopes.
The pivot charts exhaust all nonzero directions; the support census is
only an upper bound on distinct slopes.

Use the substitutions already verified in L043's import and audit:
R=8, t=4, a=12, eta_j=s_(j+1) for j=0,...,7, and nonzero
column multiplier x for x in H. These source hypotheses do not depend
on how the three base supports intersect and impose no prime-subfield
restriction on syndromes. Thus their unchanged recurrence coverage
applies to the triangle as well. This is source applicability, not a
new triangle elimination formula. The compiler operates on the full
recurrence vector: a both-zero vector after removing shared columns
must still be lifted and cannot be declared common from that quotient
alone. Zero recovered weights are allowed by span membership; full
weight needs a separate gate.

Reuse the exact distance/shortening coverage behind audited L041:
J. I. Hall, *Notes on Coding Theory*, Theorem 5.1.1 and proof,
printed pp. 63–64 of the undated
[author-hosted GRS chapter](https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf),
as extracted under “Primary theorem and applicability” in
`2026-10-05-two-block-moment-obstruction.md`;
I. Marquez-Corbella and R. Pellikaan, *A characterization of MDS codes
that have an error correcting pair*, FFAA 40 (2016), 224–245,
[DOI 10.1016/j.ffa.2016.04.004](https://doi.org/10.1016/j.ffa.2016.04.004),
section 5, Definitions 5.1–5.2, Lemma 5.3 and the following GRS
shortening formula, printed pp. 7–8 of the
[2016-02-29 accepted manuscript](https://pure.tue.nl/ws/files/93073933/16_02_29_ECP_MDS.pdf),
as extracted under “Primary shortening input” in
`2026-10-07-six-coordinate-triple-equality-obstruction.md`.
These saved extracts were read today; the PDFs were not freshly retrieved.
L041 already checks seven deletions, dimensions 8 through 2 before
deletion, and nonzero label differences. Its local converse supplies
the triangle's exact weights and automatic nonpersistence for tau=0.
No general distance, shortening or annihilator reproof is needed.

## Stronger results, local overlap and failures

Reuse the circuit/ray comparison in
`2026-10-07-nine-coordinate-triple-compatibility.md`: the inspected
single-MDS-circuit theorem assumes every counted error is inside one
fixed nine-set and supplies bound 36. Only the three base errors here
are assumed inside U; it supplies neither a fifteen bound nor the
desired additional-support description. The more general compiler is
an exact algorithmic test, not a sharp triangle count. General MCA
and subspace-design comparisons in the existing assessments are not
refreshed, since this step seeks fixed-support recovery, not a new
global estimate. Unread ABF26, Jo and campaign leads remain unread;
none is assumed in the local reduction or used for a novelty claim.

Read full L041, L010's kernel/uniqueness and same-support passages,
L016's analytic recurrence and quotient, and L043's statement, imported
recurrence and complete scoped audit. L016/L043 remove two shared
columns in a tau=1 configuration; their universal classification and
finite count cannot be transferred to the three pair-only coordinates.
The normalized triangle weights themselves are already in L041 and
must be cited rather than rediscovered. L042 and L056 are not inputs:
L041's tau=0 converse already addresses nonpersistence, whereas L056
counts candidates for L043's other pattern.

ATTEMPTS/008–009 record determinant-only zero-kernel blindness and a
stopped fixed-label generator. This attempt must retain quotient lifts
and arbitrary extension weights, rather than revive that enumeration.
ATTEMPTS/022–024 record the insufficiency of isolated degrees,
support-only recentering, and the false exclusion of every same-tag
triple. Their obstruction evidence is preserved; none bans this different
triangle target. No count follows by adding individual support tests.

## Searches and bounded ready attempt

Queries performed on October 10:

- `"Reed Solomon" "affine" "syndrome" "fixed support" recurrence`
- `"mutual correlated agreement" "triangle" support`
- `"Reed Solomon" "quotient" "locator recurrence"`
- `"Reed-Solomon" "three" "pairwise" "syndrome" affine support`
- `"mutual correlated agreement" "nine" support`
- `"Shortening Bounds for Reed" "triangle"`

Results were generic decoding or broader MCA leads, with no inspected
matching triangle theorem. Search snippets, secondary pages and unrelated
papers are not theorem evidence; no novelty inference follows from these
searches. Primary evidence for readiness is the recurrence/compiler
proofs plus the reused coding inputs and local audited results.

The ready REPRODUCTION attempt has exactly the TARGET's scope. Name the
three pair-only labels and the two singleton labels per error using
L041. Substitute its existing local weights into the actual affine
syndrome pencil, retaining lambda and all gamma differences. For each
additional K, eliminate the recurrence columns at the pair-only labels
absent from K. Determine, rather than assume, the relevant ranks and
zero/proportional systems. Seek label-only projected tests and explicit
conditions in the three normalized pair weights; recover the eliminated
coefficients before solving for the four actual K-weights. Verify all
eight moments, every finite denominator, all three base exclusions and
same-support failure. Keep vanishing recovered coefficients as relaxed
recoveries and state separately when they give a full four-error.
No projected rank, universal support, rational descent or count is
established in this review. A mere generic rank-test restatement does
not meet the continuation test. L010 and audited L041 are essential
local inputs; L016/L043 supply comparison methods only. Exact and
supporting Mathlib coverage for this changed criterion is **not checked**.
No cross-notebook result, new lemma or mathematical script was used.
