# Step56 — approved Schur–Ostrowski test, working record

The startup EXPLORE assessment is
`drafts/literature/2026-11-09-l938-simplex-majorization-scope-54.md`;
its COVERED_TARGET matches the current Next action. This turn performs
only its 48 rational two-block tests, with no grid enlargement.
The full startup overview and DAG were supplied and read. Existing
notebook changes, including L938/L939 and the prior assessment, are
preserved. The fixed-cell and contact/score stops are contrasts.

The central gap remains L030–L032/C032a all-degree mixed positivity.
The intermediate target is global Schur-concavity of the full arithmetic
S_12 average of L939(4), using L938's 34 rows, twelve factors, factorials
and M_0^12 normalization. A positive exact pairwise derivative product
refutes that sufficient mechanism; no positive value is inconclusive.
The possible downstream use is a balanced-simplex comparison for the
finite-energy density. Theta ordering, integral/variation transfer,
endpoint signs, contacts, other degrees and global continuation are
independent unpaid steps. An algebraic obstruction requires none of them.

## Derivation before calculation

Write N=12, d=12, and F_alpha=product_k ((2k)!)^alpha_k. For a row's
fixed exponent list k_1,...,k_12, arithmetic averaging at (q^m,1^(12-m))
is a uniform average over the binomial(12,m) subsets of exponent slots
assigned to the q block: each subset occurs m!(12-m)! times in S_12.
Thus the row's restriction is

    (c_alpha/F_alpha)/binomial(12,m) * sum_(|I|=m) q^(sum_(i in I) k_i).

Call the sum of these row polynomials H_m(q). At this block vector,
symmetry gives partial_i Pbar=H_m'(q)/m in the first block. Euler's
degree-twelve identity gives partial_j Pbar=(12H_m-qH_m')/(12-m)
in the second. At t=(q^m,1^(12-m))/s, s=mq+12-m, the exact discriminator is

    D_ij=(q-1)/(m(12-m)s^12) * (s H_m'(q)-12m H_m(q)).

This uses ambient partial derivatives before restriction. The script
will also compute their difference by fixing the two labelled exponent
slots at i and j and averaging the remaining ten slots, then compare
all polynomial coefficients row by row. Both constructions must retain
the factorial denominator and average, not sum, over permutations.

This was the saved pre-calculation record. The completed result and
full proof are now canonical in L940, with the complete certificate at
`scripts/heat/l938-schur-obstruction-56.json`. Fifteen exact positive
values close the global Schur-concavity mechanism; 1278 checks pass.
No Decimal or theta approximation entered the test. The prior pending
work is completed; the sole current continuation is in PROGRESS.md.
