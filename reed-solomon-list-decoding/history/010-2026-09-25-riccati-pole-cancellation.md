# 2026-09-25 — Riccati pole cancellation and unfiltered counts

Read the shared and local rules, current checkpoint, full overview,
DAG, relevant proofs, failure record, and existing changes. The active
notebook had no pre-existing changes; unrelated notebook changes were
preserved. Rechecked the [prize statement](https://proximityprize.org/);
the threshold and source qualifications are unchanged. The
[focused draft](../drafts/2026-09-25-riccati-pole-cancellation.md)
preserves the target, discriminating test, and saved reasoning.

[L009](../lemmas/L009-riccati-divisors-and-unfiltered-counts.md) proves
an exact divisor parametrization of polynomial Riccati solutions.
The resulting count is independent of field size but exponential in
the degrees. More decisively, its subspace construction gives
superpolynomially many unfiltered solutions at fixed odd characteristic,
within the relevant degree scale. The
[stopped proposal](../ATTEMPTS/002-riccati-unfiltered-polynomial-count.md)
records why a polynomial count before agreement filtering is unavailable.

The outcome is NEGATIVE, not a repeated stop review. Exploration turns
are 0/3 after this informative obstruction; STATUS remains IN_PROGRESS.
The result closes the pole-cancellation question for the tested class
but leaves the main small-characteristic filtered-list bound and sharp
boundary unresolved. There is no common-center large-list witness or
complete target candidate. The exponential sufficient field condition
does not follow from the source's existence proviso.

Pairwise differences obey linear equations even though the original
equation is nonlinear. Their possible root multiplicities away from
zeros of a therefore motivate weighted agreement counting as the
subsequent direction. No such count is asserted here. This change of
mechanism retains the classification and responds to new evidence.

`python3 scripts/riccati-families/verify.py` passed 17 exhaustive cases
covering 35,531 polynomials, 4,309 divisor tests, and 56 parameter
recoveries, plus identities for 84 distinct subspace solutions.
The output is retained under `scripts/riccati-families/`. These finite
checks do not substitute for the full informal proofs or enumerate a
prize list. Mathlib coverage is not checked.

L009 uses L008 for rational derivative constants and the minimal
homogeneous generator, so that is its sole direct mathematical input
in the DAG. The subspace identity and count are proved within L009.
The required documentation checker passed with ten nodes and seven
edges, with bytecode writes disabled to keep shared infrastructure
read-only. `git diff --check -- .` passed. The graph edge was checked
against the proof; structural validation does not verify mathematics.
