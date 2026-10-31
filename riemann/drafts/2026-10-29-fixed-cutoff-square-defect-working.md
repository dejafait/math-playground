# Fixed-cutoff square defect — working record, 29 October 2026

Approved target and exact G_T/E(T): the unchanged assessment
`literature/2026-10-29-fixed-cutoff-square-defect-test.md`.
This records unfinished reasoning before the finite-sum estimates;
it is not a completed result or a claimed lower bound.

Use L317 (1) only through j=2, L316's phase expansion and L471 (7).
With P_j(t)=sum_{n<=M_T}(lambda(t)-log n)^j n^(-1/2-it),
the frozen affine jets are 2 Re(e^(i theta) i^j P_j).
Their quadratic form minus 4|P_1|^2 is exactly

    R_T=2 Re(P_0 conjugate(P_2)-|P_1|^2)
          +2 Re(e^(2i theta)(P_0 P_2-P_1^2)).

Equivalently, its ordered-pair summand is

    (nm)^(-1/2) log(n/m)^2
       [cos(t log(m/n))+cos(2 theta(t)-t log(nm))].

Thus every diagonal term is zero. No inference about the L1 norm
follows from this cancellation. Planned transfer: retain entering
polynomials M_T<n<=floor(sqrt(t/(2pi))) with their actual activation
intervals; prove their L2 cost, then the quadratic L1 cost. The fixed
and moving phase coefficients must be compared, and the exact
completion curvature retained. Finite integration by parts avoids
depending on the incompletely extracted Hilbert-inequality formulas.

Discriminant remains E(T)=o(T(log T)^3) versus a positive full-scale
lower bound on an unbounded sequence. A bound O(T(log T)^3) is
inconclusive. Preserve any resulting exact residual if neither test
is decided. Individual signs, higher signs and RH remain separate.

## Transfer calculation checkpoint

For each entering index n, retain activation at tau_n=2 pi n^2.
On [tau_n,2T], lambda-log n is bounded, nonnegative and increasing.
Expand each squared norm with pair interval [max(tau_n,tau_m),2T].
Integration by parts, including both endpoints and weight variation,
bounds its off-diagonal sum by O(sqrt(T) log T); the diagonal is O(T).
Thus all three entering jet polynomials have L2 norm O(sqrt(T)).
The fixed jet polynomials have norms O(sqrt(T)(log T)^(j+1/2)).
Cauchy--Schwarz transfers their quadratic forms with L1 cost
O(T(log T)^(5/2)); the largest term is the entering zeroth jet times
the fixed second jet. L317's analytic remainder costs O(T(log T)^2).
Phase replacement and completion curvature are smaller.

The resulting exact residual has a signed integral O(sqrt(T)):
for the sum phase, its nonzero pair coefficients contain log(n/m)^2,
which absorbs the small endpoint phase derivative log(M_T^2/(nm)).
This does not control its absolute integral. Full proof is being
written canonically; no lower bound or little-o defect has been found.

## Completion of this bounded attempt

The transfer and signed estimates above are now proved in canonical
L477, with hypotheses and Mathlib qualifications. The remaining
absolute-norm estimate reaches only O(T(log T)^3). No defect
threshold is decided, no actual sign is obtained, and no generic
phase model or infinite-time average has been substituted. This
working record preserves the partial reasoning; current routing
is recorded only in PROGRESS.md.
