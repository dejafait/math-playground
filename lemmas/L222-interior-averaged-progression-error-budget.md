# Lemma 222: interior averaged progression-error budget

**Hypotheses.** Use L220's exact functions, arithmetic coefficients
and signed identity, with the scales and interior intervals A,J of
L221. Restrict a to A and m to J in that identity, retaining every
integer c,d in [8N/5,17N/10]. Denote the resulting sums by
Q_box, M_box, E_box. Thus Q_box=M_box+E_box exactly. In sums
below a,m,c,d are integers in these intervals, and (a,m)=1.
Set

B_box=8 sum_(c,d) sum_(a,m; (a,m)=1)
 (phi(a)/a) D(m)
 sum_(k<=K; (k,am)=1) |mu(k)|/k.

This is the uniform progression-error budget, not the actual sum
of absolute errors. Constants below are positive and fixed, and
N is sufficiently large and real.

**Conclusion.**

|E_box| <= B_box,
c N³h/log N <= B_box <= C N³h (log N)²,                 (1)
c N²h/(log N)² <= M_box <= C N²h.                      (2)

In particular B_box/M_box >= c N/log N tends to infinity.
Averaging this uniform-error budget over a and m therefore does
not establish E_box=o(M_box). No lower bound on |E_box|, and no
failure of the actual little-o assertion, is claimed.

**Proof.**

The first inequality follows directly by applying |Delta_m(jk)|<=8
to L220's exact identity, then taking absolute values of its finite
Möbius coefficients. Restricting the indices does not change that
identity or replace any exact cell length or arithmetic weight.

For the upper bound, drop the coprimality restrictions and use
phi(a)/a<=1 and sum_(k<=K)1/k<=1+log K. There are O(N)
choices of a and O(N²) choices of c,d. It remains to bound
sum_(m in J)D(m). Write J0=|J|=h/(4π), and let
T=floor(sqrt(max J)). Since m=2N²+O(h)>0 on J, T=O(N).
The number d(m) of divisors of m is at most twice the number
of its divisors at most sqrt(m), by pairing r with m/r;
a square's middle divisor is harmlessly counted twice. Hence

sum_(m in J)D(m) <= sum_(m in J)d(m)
 <= 2 sum_(1<=r<=T) #{m in J:r divides m}
 <= 2 sum_(1<=r<=T) (J0/r+1)
 <= 2J0(1+log T)+2T = O(h log N).

The last equality uses h comparable to N^(3/2), so the O(N)
endpoint error is smaller. This establishes the upper bound in (1)
without any maximal-divisor estimate or distribution theorem.

For the lower bound retain only k=1 and the divisor j=1 implicit
in D(m). Both absolute coefficients equal one for every retained
pair, regardless of its other prime factors. L221's finite prime
union argument supplies at least cNh pairs in A times J with
(a,m)=1. Its elementary totient inequality gives uniformly
phi(a)/a>=c/log N. Finally there are at least cN² ordered c,d
pairs. Multiplying these bounds, and the factor 8, proves the
lower bound in (1). This argument concerns the uniform budget:
it does not assert that any Delta_m(1) is large or has a fixed sign.

The lower bound in (2) is precisely the restricted sum used in
L221's proof: F_m>=c/N on A times J, at least cNh coprime
pairs, S_K(am)>=1/4, and the two uniform totient bounds.
For the upper bound, L220's main term is nonnegative, and its
per-(a,c,d) bound O(h/N) applies also to the restricted m sum.
Summing over O(N³) triples gives O(N²h). Dividing the lower
bound for B_box by this upper bound proves the ratio assertion.

## Scope of the obstruction

The calculation improves the crude use of a maximum of D(m)
to an average on the actual short interval J. Even after that
improvement, the uniform endpoint budget is much larger than the
real main term. Merely summing that budget cannot prove the
requested signed cancellation estimate. This does not exclude a
bound obtained by estimating the actual errors, exploiting their
signs or showing that most are small. In particular the exact
lengths and coprimality constraints cannot be treated as independent
random variables on the basis of this calculation.

If E_box=o(M_box) were proved by another argument, then
Q_box/M_box would tend to one. Since Q_box is a nonnegative
restriction of Q_N, (2) would rule out Q_N=O(N³). This remains
conditional. Neither the signed exterior comparison nor RH is
resolved by the budget audit.

## Verification and formalization

Verification is analytic: finite restriction of L220's identity,
absolute coefficients, divisor pairing including perfect squares,
interval counts with endpoint error one, and the coprime-pair and
totient inequalities proved in L221. All sums are finite; h grows
faster than N, and log N/N tends to zero. Formalization would
require these finite sums and uniform asymptotic comparisons.
There is no numerical distribution claim or new external theorem.

**Mathlib.** The availability of a Mathlib theorem for this full statement has not yet been established. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/

**Lean proof status.** Not yet formalized or validated. This status does not assert that the mathematical statement is incorrect.

**Lean proof command.**

Not available until a complete Lean proof has been validated.

**Lean proof code.**

Not yet available.
