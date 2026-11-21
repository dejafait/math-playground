# Step648 — bounded fixed Mellin diagnostic, working record

Approved input assessment: `drafts/literature/2026-11-05-direct-mellin-fixed-laguerre-test.md`
(SPECIALIZE, present at invocation). Main gap: actual-Xi all-degree
mixed positivity. Target: only the first Laguerre scalar of actual E
at zero. Negative excludes the assessed product class; a pass or
inconclusive result ends this diagnostic, without a point/order sweep.

Inputs read: L828 Section2, C828a Section1, L016/L018/L019/L021;
step647's full source comparison. No completed duplicate was found in
the narrowly scoped direct-factor/failure search. No cross-notebook input.

Before numerical work the two-stage cap is fixed: 8192 real boxes with
40 decimal digits; only if inconclusive, 131072 with 60 digits. Both
integrate t=log(x) on [-20,1], retain theta terms n=1,...,4, and separately
bound x<exp(-20) and x>e. No other point or derivative order is allowed.

Write J_j=int_0^infinity (log x)^j P(x) dx, j=0,1,2. Absolute logarithmic
domination near zero follows from x^(-1/4)(1+|log x|^2) for |s|<=1/8;
at infinity the existing superexponential envelope dominates. Thus
M'(0)/M(0)=2J_1/J_0 and M''(0)/M(0)=4J_2/J_0. Reciprocal-gamma
normalization and E(0)=1 give

    E'(0)^2-E(0)E''(0) = pi^2/2 - 4[J_2/J_0-(J_1/J_0)^2].

The half-integer trigamma constant is imported from DLMF5.15.4 at n=1,
whose exact formula was checked during implementation; 5.4.13 alone
is a digamma reference and does not supply this constant. No
distinguished Bernstein-gamma representation is assumed.

Effective envelope planned: sum n^4 exp(-pi(n^2-1))<2, so
P(x)<=80 exp(9x/2-pi exp(2x)). For n>=2, consecutive terms have ratio
at most (3/2)^4 exp(-5pi)<1/2 and the first is 16exp(-3pi)<1/2.
This proves the constant using 3<pi and pi^2<10.
The four-term remainder is positive and at most 50000exp(-75) on x>=0:
the first omitted term's upper envelope decreases with x, and the
remaining n-ratio is below 1/2. On the finite transformed interval its
jth integrated absolute error is at most 21 e 20^j times that bound.

At a=exp(-20), P<=80exp(9a/2-3) on [0,a]. The absolute logarithmic
integrals there are a, 21a, 442a; retain their signs (+,-,+).
For x>=b=e>2 and j<=2, |log x|^j<=x^2<=exp(x). Since exp(4)>54,
the tail is bounded by 80exp(-151)/318<exp(-140), for each j, using
the decreasing derivative of 11x/2-3exp(2x).

Backend: Python decimal directed elementary arithmetic; exp's documented
correctly rounded half-even output is expanded by adjacent representable
numbers. Both installed docstring and official Python3.15 documentation
were checked. Machin's formula with rational alternating-series bounds
will enclose pi. All arithmetic failures must leave an INCOMPLETE report.
Completion: the two stages finished; the first was inconclusive and
the second passed the necessary condition. Full proof and restrictions
are now canonical in `lemmas/L829-direct-mellin-fixed-laguerre-test.md`.
Complete computation and exact recorded-arithmetic verification reports
are in `scripts/direct-mellin/`. No global membership or Xi sign follows.
