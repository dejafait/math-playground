# Lemma 926: finite gcd coefficient conditioning with subpower loss

## Hypotheses

Let N>=2 be an integer and c=(c_1,...,c_N) an arbitrary complex
vector. Euler's totient is normalized by phi(1)=1. Put

    b_n=c_n/sqrt(n),
    B_d=sum_(k<=N/d) b_(dk),
    Q(c)=sum_(d<=N) phi(d)|B_d|^2.

All indices are positive integers. Use only L737's finite divisor
factorization and Möbius inversion (5)-(11), with its step261 check;
its moment, Hardy-function, height and bump hypotheses are not inputs.
In particular, its finite identities give

    Q(c)=sum_(m,n<=N) c_m conjugate(c_n) gcd(m,n)/sqrt(m*n),
    b_n=sum_(k<=N/n) mu(k)B_(nk).                         (1)

The imported standard scalar and operator results are:

- Terence Tao, *The divisor bound*, 23 September 2008,
  [equation (3)](https://terrytao.wordpress.com/2008/09/23/the-divisor-bound/):
  for every delta>0 there is D_delta>=1 with
  tau(m)<=D_delta m^delta for every positive integer m. The constant
  is independent of m. The large-prime and finite-small-prime cases
  were inspected in the prior source comparison; that proof is not
  repeated here.
- J. B. Rosser and L. Schoenfeld, *Approximate formulas for some
  functions of prime numbers*, Illinois J. Math. 6 (1962), 64-94,
  [Theorem 15, (3.41)-(3.42), printed pp. 71-72](https://denisevellachemla.eu/Rosser-Schoenfeld-1962.pdf),
  [DOI 10.1215/ijm/1255631807](https://doi.org/10.1215/ijm/1255631807):
  for integer m>=3,

      m/phi(m)<exp(gamma) log log m+5/(2 log log m),

  except m=223092870, at which (3.42) has 2.50637 in place of 5/2.
  Here gamma is Euler's constant. Only the weaker bound with
  2.50637 for every m>=3 will be used. The indices 1,2 are handled
  separately below. No revalidation of the source's numerical constants
  or proof cases is claimed.
- L. Grafakos and R. H. Torres, *A multilinear Schur test and
  multiplier operators*, author manuscript dated 9 February 2000,
  [Section 2, classical Schur theorem, p. 2](https://grafakos.missouri.edu/preprints/multilinear_schur.pdf).
  Its nonnegative-kernel theorem on sigma-finite spaces for
  1<p<infinity specializes to finite counting measure and p=2:
  if positive weights h give weighted row bound R and column bound S,
  the squared l2 operator norm is at most RS. The finite weighted
  Cauchy-Schwarz form of this theorem is also proved in L737 (8)-(9).
  We reuse that bound rather than reprove the general Schur theorem.

The ready SPECIALIZE assessment at invocation start was
drafts/literature/2026-11-09-gcd-coefficient-conditioning-reproduction.md;
its completed source comparison is
drafts/literature/2026-11-09-gcd-coefficient-conditioning-review.md.
There is exact prior overlap with bramble_trace, *Generalized Laguerre
positivity at growing orders*, v3, 23 October 2026,
[Section 5, Lemma 5, (27)](https://rstation.ai/problems/riemann_hypothesis/papers/41/v3).
At shift zero its matrix B_0(d,n)=1_(d|n)sqrt(phi(d)/n) has squared
output norm Q(c), and its claimed squared inverse bound implies the
conclusion below. The compressed proof in that unreviewed manuscript
motivates this canonical verification from the precisely cited standard
inputs. No general scalar or matrix theorem is being reproved.

## Conclusion

For every epsilon>0 there exists a_epsilon>0 such that, simultaneously
for all integers N>=2 and all complex c,

    Q(c)>=a_epsilon N^(-epsilon) sum_(n<=N)|c_n|^2.        (2)

The constant depends only on epsilon. This verifies the source-covered
finite endpoint estimate, classified REPRODUCTION; no new-result claim
is made. The proof does not assert a positive constant uniform at
epsilon=0, a shifted extension or uniformity as epsilon tends to zero.
It does not supply a longer-multiplier moment estimate, a bump projection
bound at a new length, signed realization, transfer or Xi positivity.
L925 is prospective downstream context, not a mathematical input.
Written 9 November 2026; the separate finite audit below validates the
claim under these named imports, without asserting an analytic application.

## Proof

### 1. Uniform scalar allowances, including small indices

Fix epsilon>0 and set delta=epsilon/4. The cited divisor bound gives
one D_delta>=1 valid for all positive integers. Define

    A_delta=max{sqrt(2),
      sup_(x>=3) x^(-delta)
        sqrt(exp(gamma) log log x+2.50637/(log log x))}.

This is finite: the function under the supremum is continuous on
[3,infinity), has positive log log x, and tends to zero at infinity.
The last assertion follows from log log x=o(x^(2delta)) and
1/log log x tending to zero. Thus Rosser-Schoenfeld, with its
exception included by increasing 5/2 to 2.50637, gives

    sqrt(m/phi(m))<=A_delta m^delta    (m>=1).            (3)

For m=1 the left side is 1, and for m=2 it is sqrt(2), so the
chosen maximum covers both without applying the cited theorem there.
All constants so far depend only on delta.

For integer M>=1, integral comparison gives
sum_(k<=M)1/k<=1+log M. Also
log x=integral_1^x dt/t<=integral_1^x t^(delta-1)dt
<=(x^delta)/delta for x>=1. Consequently, with H_delta=1+1/delta,

    sum_(k<=M)1/k<=H_delta M^delta.                     (4)

This remains valid at M=1. It is an elementary allowance, not a new
divisor or totient theorem. No constant depends on N or c.

### 2. The precise inverse and its weighted row and column sums

Set y_m=sqrt(phi(m))B_m, so ||y||_2^2=Q(c). Equation (1) gives
c=A y, where the finite matrix and its absolute majorant are

    A_(n,m)=mu(m/n)sqrt(n/phi(m)) if n|m, and 0 otherwise,
    K_(n,m)=|A_(n,m)|.

This is the inverse of the coefficient-to-y matrix, in the indicated
direction; it is not an estimate of individual Gram entries. The
diagonal factors are nonzero. All sums are finite, so complex phases
and truncation require no limiting interchange.

Choose positive weights h_n=1/sqrt(n), 1<=n<=N. For each row n,
put m=nk to obtain the exact weighted sum

    sum_(m<=N) K_(n,m)h_m/h_n
      =sum_(k<=N/n) |mu(k)|/k * sqrt(nk/phi(nk)).

Since nk<=N and |mu(k)|<=1, (3)-(4), with
M=floor(N/n)>=1, give

    sum_m K_(n,m)h_m/h_n
      <=A_delta N^delta sum_(k<=N/n)1/k
      <=A_delta H_delta N^(2delta)=:R.                  (5)

For each column m the exact weighted sum is instead

    sum_(n<=N) K_(n,m)h_n/h_m
      =sqrt(m/phi(m)) sum_(n|m)|mu(m/n)|
      <=sqrt(m/phi(m)) tau(m)
      <=A_delta D_delta m^(2delta)
      <=A_delta D_delta N^(2delta)=:S.                  (6)

Thus the divisors are counted only in the column estimate; the row
has a harmonic factor, not a count of N multiples. The cutoff 1 is
included in both sums and all weights are strictly positive.

### 3. Squared norm and exponent allocation

The cited finite Schur estimate applied to the nonnegative matrix K,
with (5)-(6), gives ||K||_(2->2)^2<=RS. For complex y,
|(Ay)_n|<=(K|y|)_n, so the same squared norm bound controls A.
It follows that

    ||c||_2^2=||Ay||_2^2
      <=A_delta^2 H_delta D_delta N^(4delta)||y||_2^2
      =A_delta^2 H_delta D_delta N^epsilon Q(c).         (7)

Taking a_epsilon=1/(A_delta^2 H_delta D_delta)>0, with
delta=epsilon/4, proves (2). In particular the exponent epsilon
in (7) belongs to the squared inverse norm; no additional squaring
is omitted. The zero vector satisfies (2), and all nonzero vectors
give Q(c)>0. The constants cover every N>=2 at once, even when the
complex coefficient vector varies arbitrarily with N.

No unproved Xi sign, RH-equivalent premise, infinite sum, analytic
moment uniformity, realization assertion or cross-notebook input was
used. The finite lower bound alone does not close those independent gaps.

### Separate finite audit — 9 November 2026

The invocation-start SPECIALIZE assessment was
drafts/literature/2026-11-09-gcd-coefficient-conditioning-audit.md,
separately approved before this audit. Reuse its completed primary-source
coverage, including the scalar proof cases and Schur hypotheses; no
external theorem is newly asserted or reproved. The scope is exactly
every fixed epsilon>0, all N>=2 and all complex c. L737's finite
identities, rather than its analytic conclusions, are the only local
mathematical input. The following checks independently validate the
load-bearing steps of the existing reproduction.

**Inverse direction and complex normalization.** Write T for the
coefficient-to-y matrix, so T_(m,j)=1_(m|j)sqrt(phi(m)/j).
For fixed n,j, the (n,j) entry of AT is zero unless n|j. If j=nr,
it is

    sqrt(n/j) sum_(k|r) mu(k),

because the intermediate indices are exactly m=nk with k|r.
This is 1 when r=1 and 0 otherwise. Thus AT=I for every finite
prefix, with no boundary contribution; in particular the displayed
A maps the actual y to c. Expanding the finite squared norm of y
gives precisely the Hermitian Q in (1). For complex y, coordinatewise
absolute domination by K|y| is valid and || |y| ||_2=||y||_2.
No restriction to real vectors or entrywise eigenvalue inference occurs.

**Scalar constants and the exceptional integer.** For m>=3,
log log m>0. Replacing 5/2 by 2.50637 therefore weakens the source
bound in the correct direction, and includes m=223092870 directly.
No test at that integer or removal of the exception is needed.
The continuous function defining A_delta has finite maximum on each
compact subinterval of [3,infinity). Its square tends to zero since
x^(-2delta)log log x and x^(-2delta)/(log log x) do, for every
fixed delta>0. The supremum on the whole interval is consequently
finite. At m=1,2 the ratios are 1,sqrt(2), while A_delta>=sqrt(2)
and m^delta>=1. Thus (3) is uniform at these indices as well.
The harmonic allowance uses M>=1, not M>1: at M=1 the sum is 1
and H_delta M^delta>=1. Tao's divisor constant covers m=1 with
tau(1)=1. All three constants depend only on delta, even when N
or the vector changes.

**Both Schur orientations and cutoff.** The actual factors in the
row and column are respectively

    sqrt(n/phi(m)) sqrt(n/m)
      =sqrt(m/phi(m))/k       (m=nk),
    sqrt(n/phi(m)) sqrt(m/n)
      =sqrt(m/phi(m))         (n|m).

The first yields the harmonic sum in (5), with
floor(N/n)>=1 and <=N. The second yields (6), with at most tau(m)
divisors. These are the row ratio h_m/h_n and column ratio h_n/h_m
required by the cited p=2 Schur theorem, on finite counting measure
with positive h. In particular they are not interchanged. Each
individual sum has power at most 2delta. As an explicit cutoff check,
at N=2 the inverse and its majorant are

    A = [[1,-1],[0,sqrt(2)]],
    K = [[1, 1],[0,sqrt(2)]].

With h=(1,1/sqrt(2)), the weighted rows are
1+1/sqrt(2), sqrt(2), and the weighted columns are 1,2sqrt(2).
These agree with the formulas, including the diagonal k=1. They are
covered by the same scalar allowances; no large-N exception is hidden.
For a larger N the same exact diagonal and cutoff arguments apply.

**Squared exponent and result.** Schur gives the squared operator
bound RS, not its square root. Multiplication of (5) and (6) gives
A_delta^2 H_delta D_delta N^(4delta). Since c=Ay and
||y||_2^2=Q(c), this is precisely (7). Setting delta=epsilon/4
therefore proves the stated squared-norm exponent epsilon. The
reciprocal of the finite positive scalar product is one a_epsilon
for every N>=2, including the zero vector. There is no epsilon=0
conclusion or interchange of limits in this argument.

Audit result: the inverse orientation, both weighted sums, exception,
small-index uniformity and squared exponent pass without correction.
This validates the existing source-covered reproduction, not a new
conditioning theorem beyond the inspected sources. No moment error,
longer dictionary, signed realization or Xi sign was audited or obtained.
The mathematical statement and its direct local input are unchanged.

## Mathlib

Full matching coverage of (2) is not checked. Neither the source
assessment nor this reproduction establishes absence from Mathlib.
Supporting finite-matrix, Möbius-inversion, divisor/totient or Schur
theorems have not been matched to exact Mathlib declarations here.
The informal proof uses the explicitly cited standard results above;
it makes no formal-verification claim.
