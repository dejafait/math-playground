# Four frozen witness hull — step 350 working record

The approved target is exactly the convex hull of L088,L090,L092,L094
at L086's columns, as assessed in
`drafts/literature/2026-10-19-fixed-column-four-witness-convex-hull.md`.
Main gap: arbitrary-center 67/68-agreement safety, bracket 955–957.
The intermediate test can either preserve an included-anchor mixture for
further constraints or stop these four directions together. It cannot
exclude all fixed-column completions or change the RS boundary.

Before calculation, the complete hypotheses/scaling passages of all four
lemmas, L094's original/raw row formulas and L095's rejection framework
were inspected. ATTEMPTS/071 and /078 retain the capped full-row stop and
the last fixed-assignment rejection. The ready source assessment already
records the other relevant failures and exact finite-LP coverage; it is
reused. No external literature refresh is necessary.

Plan: bind the full four z/raw vectors, identical column parameters and
positive scales; retain 85 domain rows,90 kernel equations,500 types/3000
presentations,36 forced entries,28 selected equalities,45 signs and all
81 modes, including full anchor and whole singular ranges. Reconstruct
the rational 81-by-4 remainder matrix from the original/raw formulas.
Accept only a rational simplex witness passing every row, or a rational
nonnegative row combination strictly negative at every vertex, with
independent full substitution. Missing binding/range evidence is
inconclusive. Do not enlarge the hull or restart the stopped prescriptions.

Ancestral foundations/04,09,10,12 PSD,uniqueness,whole-kernel and
normalization contracts remain conditional. Scalar upper rows, other
anchors/columns/base/pairs,global moments,RS realization and 955–957 are
independent unresolved steps.

## Completed bounded attempt

The exact hull calculation finds a unit-weight separator on
mode32=(3,5). Its four normalized vertex values are respectively in
[-20451752,-20451751),[-18663385,-18663384),[-2716330,-2716329),
[-3232205,-3232204). Consequently every mixture is strictly below
-2716329 against the required zero. The canonical proof and exact
artifact specifications are in
[L096](../lemmas/L096-four-frozen-witness-convex-hull-is-excluded.md).
The 81-by-4 original/raw calculation and independent verifier pass
1662 and 916 checks with no failures. This is NEGATIVE / RESEARCH /
REPRODUCTION,actual calculation; it stops this hull only. No LP solve,
free-moment solve,hull enlargement or stopped full-row/conic restart
was needed. All four individual subsystem results remain preserved.

Two implementation issues preceded the final result. The first run
looked for `norm` in the original reconstruction,whose corresponding
field is `positive_raw_normalization`; it raised KeyError before a
sign verdict. Its pre-row binding certificate is preserved at
`scripts/finite-support/four-witness-hull-initial-binding.json`.
The next run reconstructed every original/raw mode successfully but
compared L090's saved 43-row control vector using the 17-new-only-row
order. Nine `vertex_own_controls` comparisons failed. Preserve this
full intermediate result at
`scripts/finite-support/four-witness-hull-control-order-failure.json`.
The final run uses L090's actual `zero_old_block_modes` order. All
mathematical inputs,coefficient arrays and target remain identical;
every complete final control and raw identity passes. No failed check
is treated as mathematical evidence or suppressed.

The first documentation check found PROOF.md at 103 lines after adding
three lines. Integrating the new summary and trap text into the existing
paragraphs retains all prior content and restores the 100-line limit.
The scoped checker then passes: 102 nodes,383 unique edges,acyclic,
complete file coverage,valid links and compact overviews. The new DAG
row records the four vertex inputs and their actual fixed source
contracts; L084's equality parametrization is not a new input because
this hull argument uses the already frozen complete vectors directly.
Next is separate approval of the new critical-audit scope,marked
REVIEW_REQUIRED; no further mathematical target is attempted today.
