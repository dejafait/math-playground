# Coprime density error checkpoint

L191 is complete; earlier work is preserved. Proposed step: replace its
inner affine sum by (phi(u)/u) integral_b^t H_m(x) dx for nonempty integer
intervals, and zero for empty intervals. For u>1 zero removal cancels in
Möbius inversion. Divisor-lattice counting discrepancy on [b,x] is at most
2 per squarefree divisor; partial summation costs endpoint size plus variation.
H is bounded and beta=O(N^(-2)), while t-b=O(N^(3/2)).
For each u,m only O(1) floor cells v intersect [-R,R], since R/u=o(1).
With #M=O(h), sum |P(u)|=O(N²), u>=N² and divisor bounds for Q and
2^omega(u), total error should be O_epsilon(h N^epsilon)=o(Nh).
Resume: prove the discrepancy and summation carefully, check rational affine
examples including zero and singleton intervals, and store L192 and history.
The density main term and its signed decay are still unproved.

Completed: L192 proves the uniform discrepancy and total weighted bound.
The exact rational affine and short-window cell checks passed. The proposed
error estimate is now proved; signed density-main-term decay is not.
