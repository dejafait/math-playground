# Pair-free ordered-history attempt — step 537

Invocation-start gate: `drafts/literature/2026-10-28-pair-free-envelope-cover-review.md`
(EXPLORE). The exact approved target is the pair-free bounded cover on
L109's fixed S,J and original 756 whole blocks. Existing changes are
preserved. L169's audited cover/dual method is reused; L167 and L153
supply no mandatory label or symmetry. No cross-notebook input is used.

Main gap: uniform twelve-row exclusion. Intermediate target: a complete
cover with terminal total capacity <=11, or an exact deficient twelve-family.
The former would remove numerical-pair identification for this partition;
coding realization, representation and challenge identification remain gaps.
The latter would stop this exterior-only criterion, not refute the challenge.

## Pair-free cover justification, written before running

For a selected history T use W(T)=sum row(N_a), and the entire envelope
D(W)={a:dim(W+row(N_a))<21}. Start at the empty history and W=0;
its canonical kernel is the full 21-space. If a deficient twelve-family F
exists, sort all twelve of its labels. At every sorted prefix T, every
remaining a has W(T)+row(N_a) contained in W(F), hence is in D(W(T)).
It also exceeds the last label (initially -1), is individually linear
with T and uses only coordinates of residual degree >=1. Thus it belongs
to the complete candidate list. The next label of F is one of the
children. This includes rank zero at the root, all deficient ranks and
zero-increment children. No span is excluded because it has low rank.

At each history the candidate list contains exactly labels passing those
tests. A node closes only if |T|+floor(B)<=11, where B is either the
candidate count or a checked feasible rational coordinate/pair-group dual.
Use L169's precisely cited finite weak duality (Boyd–Vandenberghe,
Convex Optimization, 2004, sections 5.1.3/5.2.1–5.2.3, pp.216,224–227).
Residual coordinate capacities are 4-d_h(T); either I-pair groups or
K-pair groups have capacity one by pairwise linearity. Every candidate
column must have dual coverage >=1. Further candidate conflicts may be
dropped. A failed dual threshold causes branching, never exclusion.
Optional closure members stay optional and may be zero-increment children.
Histories, residual degrees, candidate lists and all child obligations
remain separate; only complete kernels and their extension data are cached.
This is L169's established method specialized to the empty root, not
a new enumeration theorem. Its source comparison is already approved.

If all leaves close, following the sorted labels of F contradicts twelve.
A partial tree proves no uniform exclusion. Every unfinished node and
every not-yet-materialized child must remain explicitly in the frontier;
partly scanned extension vectors retain their tested prefix. Lazy child
kernel construction is an evaluation order, with no pruning rule.

All entries are in F_97, so every specified stack has the same rank
over every extension, by vanishing/nonvanishing minors. No descent of
a chosen decomposable plane is required for this rank statement.
No coding converse, rank-one projection, weight or original-chart gate
is inferred from deficiency. Full matching Mathlib coverage is not checked.

## Counters and stopping conventions

Stop at the first exact twelve-family, 10000 distinct generated deficient
spans (including the empty root), or the shared budget of 1000000
whole-block tests. A producer extension rank evaluation counts one;
a lazy child restriction/kernel evaluation counts one even when its rank
was cached. Reserve one independent replay for each such evaluation,
one original-stack block insertion per member of each new span's generating
history, and 756 independent single-block rank checks. Before each new
evaluation check producer tests plus reserved verification work; stop
when the next evaluation and its check cannot fit. This conservative
reservation may leave a small unused remainder below the cap. Polynomial
construction, dual column arithmetic and cached lookups do not count as
block tests. Original-stack rank/kernel certification is one whole-stack
test charged once per inserted block, not once per scalar arithmetic step.
All actual and reserved counters are saved. Independent verification
uses no pair-free producer routines, reconstructs original blocks via
the audited verifier's polynomial/normalized-quotient construction,
and checks every stored span, tested extension, evaluated child, capacity
column and frontier obligation. It never completes untested suffixes.

The first run will preserve the full certificate under
`scripts/pair-free-envelope/`. A cap is EXPLORATION, not a bound or
an informative mathematical obstruction. Continuation must respect the
same cumulative caps and exploration rules, not restart counters.
