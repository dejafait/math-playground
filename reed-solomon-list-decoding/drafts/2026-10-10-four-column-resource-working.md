# Four-column resource attempt — working record

The turn-start EXPLORE assessment is
`drafts/literature/2026-10-10-four-column-packing-resource-test.md`.
Work is restricted to its exact target. Main gap: arbitrary-center
safety at 67/68 agreements. Test: the finite five-subset resource LP
for nine-sets on at most four columns, retaining the complete F_107
quartic graph baseline and leaving two embedding points unused.

Compatibility with the imported graph baseline follows because a
graph has one point per column; each proposed extra block meets at
most four columns. Extra/extra compatibility remains a packing
constraint, relaxed by counting each five-subset at most once.
Column profiles of extra blocks are partitions of nine with at most
four parts; resource profiles are partitions of five with at most
four parts. A block profile a uses, for resource profile b, the sum
of products of binomial(a_i,u_i) over 0<=u_i<=a_i with sum u_i=5
and positive entries sorting to b. Actual capacities count all
five-subsets of Omega with that profile, including all choices of
their columns; baseline graph blocks use only the five-column type.

Plan: solve this finite LP with exact rational arithmetic and save
all coefficients, capacities, primal/dual values, row checks and
threshold comparison in `scripts/finite-support/`. Verify coefficients
independently by enumerating all 126 five-subsets of a representative
nine-point block. Verify capacities independently by labeled column
occupancies. An upper allowance <=19800269675 stops this restricted
threshold-crossing mechanism; a larger exact optimum is nonexclusion,
not a packing. No new columns or source augmentations enter this test.

Relevant existing failures ATTEMPTS/019,021,024,026 were checked and
concern other mechanisms. No completed local duplicate was found in
the targeted script/source-note search. Canonical L041 hypotheses,
condition (A), benchmark 19800268651 and audited L042 were read for
the conditional downstream interpretation. An actual ordinary packing
above 19800269675 could obstruct that uniform cap after 1024 deletions;
resource feasibility cannot. Cross-core consistency, common-center
realization, ABF comparison and 67/68 safety remain unresolved.

No matching Mathlib theorem or supporting declarations have been
checked. The known graph construction is imported from Xu–Chen v4,
Proposition 2.2, not reproved.

Completed: canonical L043 records the exact optimum and its full
counting/compatibility proof. Certificate and independent reconstruction
are `scripts/finite-support/four-column-resource-results.json` and
`scripts/finite-support/four-column-resource-audit-results.json`.
The latter passes all 79 checks; all relevant exact witnesses, matrix,
capacities and slacks were inspected. The integer total allowance is
32368000878>19800269675, so this upper diagnostic is nonexcluding.
Preserve the construction question; no added packing is established.
Separate critical proof review remains pending, with new coverage
marked REVIEW_REQUIRED rather than approved in this research turn.
