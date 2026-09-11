# Growing exterior buffer checkpoint — 2026-09-11

Draft calculation: under a common strip H and |λ|≤L, L129 and L130 give the absolute exterior imaginary sum at R=A+d at most 4H V(A,d), where

V=((R²+H²)/d²)[B_L/R²+10(log(5R)+1)/R]/log 2.

For fixed H,L and A→∞ this is comparable to R log R/d². Its vanishing is equivalent to d/sqrt(A log A)→∞: split d≤A (R comparable to A) and d>A (R≤2d, so log R/R→0 suffices). The reverse implication follows from R log R≥A log A. This is a sharp threshold for this majorant, not a necessity theorem for actual theta zeros.

Resume: audit both directions for nonmonotone d, store the conditional lemma and direct L129/L130 graph edges, then update history and PROGRESS and run structure validation. No global supremum or strip theorem follows.

Completed: both limit directions and the critical-scale constant were audited and stored in L131. This checkpoint is retained as completed reasoning.
