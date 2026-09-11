# Large-prime divisor-count checkpoint — 2026-09-14

Candidate argument (unproved at checkpoint): for fixed u=ab and p,
m0 lies in an interval of length O_t(N^(3/2)), so only
O_t(N^(3/2)/p+1) multiples occur. For each m0, the exact interval
(m0-1)^2 <= u cd < m0^2 permits O(1) integer products cd.
The elementary divisor bound then gives O_epsilon(N^epsilon)
opposite pairs per product. First pairs with p|ab number at most
O_t(N^(3/2)/p+N), uniformly up to 2N. Summation above Q should
therefore give O_(t,epsilon)(N^epsilon [N^3/Q+N^(5/2)log N+N^2]).

Resume by verifying both first-factor orientations, the strict endpoint
convention, and a self-contained divisor bound. If these hold, choose
Q=N^(5/12) and epsilon=1/12. No phase independence is needed since
selected tuples form a subset of the full box. Existing work preserved.

Completed: the endpoint and rounding checks hold. The full proof is
stored in `lemmas/L209-large-prime-tail-by-product-counting.md`.
The same argument also controls the entire tail above N^(1/4).
No failed attempt or numerical assumption was needed.
