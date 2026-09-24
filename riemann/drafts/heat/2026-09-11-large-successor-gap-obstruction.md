# Draft: large successor gaps and common selection

2026-09-11. Candidate obstruction, not yet promoted at this checkpoint.
Take S_k=2^(8k), d_k=2^(3k), and remove S_k+1,...,S_k+d_k−1
from the positive integers to form P. The interpolation has an unbounded
jump after S_k, but globally x_j≤j^(3/4)+(3/4)j^(1/8).
For n∈P, D=ceil(n^(3/8)), and n<j≤n+D, expect
x_j−x_n≤3n^(1/8). A jump Δ_n=n^(−1/8) then makes the sum of
these D terms bounded below by an absolute positive constant.
Choose marked n_l in any proposed subsequence so n_l≥2^(8l),
and add these jumps to a positive summable baseline. This should defeat
every common subsequence even though the successor gaps are unbounded.

Resume by auditing: disjoint missing intervals, global upper bound,
explicit lower bound for the jump at S_k, constants for the D terms,
and height budget including all later marked jumps. Later jumps increase
the denominator too, so bound all height differences by the total H.

Completed audit: the construction and explicit lower bound 1/9 are now
proved in Lemma 103. This draft is retained as the interrupted-work checkpoint.
