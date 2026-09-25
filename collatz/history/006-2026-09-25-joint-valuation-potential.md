# 2026-09-25 — Joint valuation potential obstruction

Step `collatz-2026-09-25-006-joint-valuation-potential` concluded NEGATIVE.
The [saved test](../drafts/2026-09-25-joint-valuation-potential.md) records
the gap, intermediate target, and discriminating test. The primary
[source](https://mathprize.net/posts/collatz-conjecture/) was rechecked
and retains the universal positive-integer target. Existing changes and
inactive branches were preserved; edits were confined to this notebook.

[L006](../lemmas/L006-joint-valuation-potential-obstruction.md) constructs
arbitrarily large legal paths of types (2,1),(3,1) returning to the same
pair (v_2(n+5),v_2(11n+19)). The logarithmic increase is at least
log(93/49)>0, whereas the proposed certificate required negative change
on each block. Every function of the pair cancels across the path, so
at least one block instead increases the potential by a uniform positive
amount. This eliminates the proposed linear potential and its nonlinear
extensions using only the same pair of valuations. The
[attempt record](../ATTEMPTS/006-joint-valuation-potential.md) preserves
the reason this route stops.

The main gap remains open: no bound excludes aperiodic infinite words,
and there is no universal eventual-descent proof or complete candidate.
A return of the valuation pair is not a periodic integer orbit. L005's
restricted repetition exclusion is retained. A different possible source
of constraints comes from powers-of-3 divisibility in the inverse maps;
testing compatibility of their backward extensions may constrain mixed
words. Turning any resulting restriction into a uniform starting-height
bound would still require proof. This motivates the new direction without
asserting a completed route. Consecutive exploration turns without an
advance or informative negative remain zero.

Validation: `python3 scripts/joint-valuation/check_potential.py` passed
1,024 odd starts for the exact block domains and shifted identities,
plus 261 members of the witness family, including large parameters.
The [output](../scripts/joint-valuation/result.json) records 5,924 direct
shortcut transitions. All valuation and ratio checks use exact integer
or rational arithmetic. These finite checks supplement the unrestricted
proof; they are not evidence for Collatz convergence.

Mathematical review checked the maximal run conditions, both endpoint
formulas, all six valuations, the ratio lower bound, and the quantifier
over finite exception sets. L002 is the sole prior mathematical input
to L006; earlier potential obstructions and word identities motivate
the test but are not used as premises. Mathlib coverage is not checked.

Documentation validation: `python3 ../scripts/docs/check_structure.py --problem collatz`
passed with six nodes, four edges, complete lemma coverage, valid local
links, and compact overviews. The only new DAG row records L002 as the
mathematical input to L006. Structural validation does not prove the
mathematics or completeness of the input record.
