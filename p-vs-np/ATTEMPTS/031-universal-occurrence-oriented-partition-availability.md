# Attempt 031 — Logarithmic oriented partitions for all occurrence pairs

The tested premise was that every L087 pair produced from an unsatisfiable
width-at-most-three CNF meets L094's oriented common contiguous partition
cutoff in the unchanged original M. It allowed independent reversal of
blocks, rather than only directed common blocks.

**WHY IT FAILS.** [L095](../lemmas/L095-occurrence-pair-oriented-partition-obstruction.md)
gives an explicit unsatisfiable family with two runs of positive unit
clauses and an opposing-unit core, retaining L087's appended gadget.
Distinct occurrence copies force at least 2n-1 blocks, whereas the complete
original encoding has M<2^16(n+2)^3. The actual cutoff fails for n=2^t,
t>=6. This elementary specialization of unsigned breakpoint reasoning
passes the separate step-372 all-size critical audit and carries no
originality claim. The audit preserves the count, complete encoding bound
and stated infinite-range threshold; its proof is canonical in L095.

Stop this universal partition-availability route.
L094's restricted supplier remains valid on its promised inputs. These
formulas have immediate unit refutations; other witnesses, alternative
representations, general ER data and unrestricted SAT remain open.
Attempts 018/030 and all unfinished work are preserved. A later research
continuation must test a different mechanism, rather than merely changing
this partition route's name or retrying its disproved universal premise.
