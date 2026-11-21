# Grouped half-sum absolute envelope — 17 November 2026

Canonical [C019u](../lemmas/C019u-grouped-half-sum-quartic-upper-bound.md)
groups the finite half-sums with H^2 and pays all moving coefficient
variation. It proves a complete O(X^(251/250)q^16) upper bound for
the reference and actual pairs, short of O(X).

WHY IT FAILS: replacing the signed grouped coefficients by d_4
forgets mollifier cancellation. The resulting diagonal costs Xq^16;
the off-diagonal estimate costs Z_*q^16 with Z_*=N_*^2L^4=O(XL^4).
Their sum does not meet the required scale. These are upper costs,
not demonstrated growth of the actual moment. The exact signed
diagonal and variation budgets in C019u (8) remain unpaid. Moreover
the half-sum norm is only a sufficient majorant for the real pair,
so failure of that norm would not disprove M2.

A refined continuation must preserve arithmetic signs, beginning with
the low-index budget in the checkpoint, rather than repeat the divisor
envelope. Stop1403 remains valid for the separate termwise approach;
C019t's transfer remains available with its audit qualification.
No root or RH obstruction has been established here.
