# Lemma 573: fixed-cutoff microscopic density cap loss

## Hypotheses

Let T tend to infinity through arbitrary real values. Put

    L=log T, h=1/L, M=floor(sqrt(T/(2 pi))), N=M^2,
    J=[T+h,2T-h], A_M(t)=sum_(n<=M)n^(-1/2-it),
    F_M(t)=|A_M(t)|^2,
    D_h(t)=F_M(t+h)-2F_M(t)+F_M(t-h).

These are C481a's definitions; M is fixed for each T throughout all
integrals, including translated ones. All sums are finite and include
their integer endpoints. No RH, zero hypothesis, independent phases,
moving cutoff, positive density premise or residual comparison is
assumed. The numerical definitions below make sense for T>=e^2;
analytic estimates are asserted for all sufficiently large real T.

## Conclusion

There is an absolute C_*>0 such that

    integral_J (|D_h(t)|-min(|D_h(t)|,L^4))dt <= C_* T.   (1)

In particular, define

    I(T)=integral_J |D_h(t)|dt,
    I_cap(T)=integral_J min(|D_h(t)|,L^4)dt.

Then 0<=I(T)-I_cap(T)<=C_*T, and

    |I(T)/(T L)-I_cap(T)/(T L)| <= C_*/L -> 0.          (2)

If I(T)>=c T L for a fixed c>0 at all sufficiently large real T,
then I_cap(T)>=c' T L eventually for every fixed 0<c'<c. Conversely,
I_cap(T)>=c T L implies I(T)>=c T L at the same heights. Thus the
existence of some positive eventual constant in these two lower-bound
premises is equivalent. The same statements hold on any specified
unbounded sequence of heights. The forward comparison does not assert
the identical constant c for the capped premise at the same heights.

By C481a, either positive premise would give a positive lower bound
of order T L^3 for its ratio norm. No instance of either positive
premise is established here. Nothing compares that norm with the full
residual, settles either defect threshold, saves negative mass or
proves a Xi sign. This is a reproduction/specialization of the cited
finite mean-square theorem and elementary finite estimates; no
mathematical novelty beyond the checked sources is claimed.

## Proof

### 1. Imported sharp finite mean square

Import Michael Curran, *Correlations of the Riemann zeta function*,
arXiv:2303.10123v2, Lemma 2.3
([primary statement](https://arxiv.org/html/2303.10123v2#S2)):
for any finite complex coefficients a_k supported on k<=N,

    integral_T^(2T)|sum_(k<=N)a_k k^(-it)|^2 dt
         =(T+O(N)) sum_(k<=N)|a_k|^2.                  (3)

The error constant is absolute and uniform in the coefficients and
length. Only this unconditional lemma is imported, not the paper's
RH-dependent shifted-zeta conclusions. It is the sharp finite
Montgomery--Vaughan mean-square input: see also Montgomery--Vaughan,
*Hilbert's Inequality*, J. London Math. Soc. (2) 8 (1974), 73--82,
Corollary 3, pp. 75 and 82, DOI 10.1112/jlms/s2-8.1.73.
The source extraction qualifications are retained in the completed
assessment `drafts/literature/2026-10-31-truncated-microscopic-density-review.md`.
We use Curran's explicit finite statement (3), without reproving
Hilbert's inequality or replacing a finite mean by its diagonal.

Define d_2(k;M) to count ordered pairs n,m<=M with nm=k. Finite
multiplication gives exactly

    A_M(t)^2=sum_(k<=N) d_2(k;M)/sqrt(k) * k^(-it).     (4)

The support is N=M^2, rather than M. In particular N<=T/(2 pi).
Every coefficient in (4) satisfies (3)'s hypotheses. If C_MV is an
absolute nonnegative upper-error constant in (3), then

    integral_T^(2T)|A_M(t)|^4dt
       <=(T+C_MV N) sum_(k<=N)d_2(k;M)^2/k.            (5)

### 2. Elementary coefficient norm with full support

Write d_j(k) for the number of unrestricted ordered factorizations
of k into j positive integers. For a prime power p^a the allocation
of its a exponents among j factors gives

    d_2(p^a)=a+1, d_4(p^a)=binom(a+3,3).

For every integer a>=0,

    binom(a+3,3)-(a+1)^2=(a+1)a(a-1)/6>=0;

at a=0 the difference is zero as well. Choices at distinct primes
are independent by unique factorization, so these formulas multiply
and prove d_2(k)^2<=d_4(k), including k=1. The restricted count is
nonnegative and at most d_2(k). Consequently

    sum_(k<=N)d_2(k;M)^2/k
      <=sum_(k<=N)d_4(k)/k
       =sum_(x_1 x_2 x_3 x_4<=N)1/(x_1 x_2 x_3 x_4)
      <=(sum_(n<=N)1/n)^4 <=(1+log N)^4.               (6)

The last enlargement is only an upper bound of a nonnegative finite
sum: every x_j in its original support is <=N. The final harmonic
inequality follows by comparison of sum_(2<=n<=N)1/n with
integral_1^N dx/x. No divisor asymptotic is needed. This is the
two-factor version of L481's finite coefficient method, not an
application of its full-residual lower bounds or stopped interpolation.

Set C_0=1+C_MV/(2 pi). Equations (5)--(6) now give

    integral_T^(2T) F_M(t)^2dt <= C_0 T(1+log N)^4.      (7)

Using the weaker O(N log N) mean-square error would lose a logarithm
at this support. Equation (7) retains the essential sharp error.

### 3. Translated difference and removed mass

The three F_M values are nonnegative. Weighted Cauchy--Schwarz gives

    |D_h(t)|^2
      <=4(F_M(t+h)^2+2F_M(t)^2+F_M(t-h)^2).             (8)

Indeed apply Cauchy--Schwarz to the two vectors
(sqrt(1),-sqrt(2),sqrt(1)) and
(F_M(t+h),sqrt(2)F_M(t),F_M(t-h)).
For T>=e^2 the intervals are nonempty and

    J+h=[T+2h,2T], J=[T+h,2T-h], J-h=[T,2T-2h]

all lie inside [T,2T]. Substitution and nonnegativity in (8) therefore
give, with every endpoint retained,

    integral_J |D_h(t)|^2dt
      <=16 integral_T^(2T)F_M(x)^2dx
      <=16 C_0 T(1+log N)^4.                           (9)

No mean-square theorem on a translated interval is being assumed.
The cutoff stays fixed when substituting x=t+h or x=t-h.

For any x>=0 and B>0, x-min(x,B)=(x-B)_+<=x^2/B:
the left side is zero if x<=B and is at most x<=x^2/B otherwise.
Apply this with x=|D_h(t)|, B=L^4 and integrate (9). Since
N<=T/(2 pi)<=T and L>=2,

    0<=I(T)-I_cap(T)
       <=16 C_0 T(1+log N)^4/L^4 <=81 C_0 T.           (10)

Thus C_*=81 C_0 is permissible, with the same absolute onset as
the imported estimate. This proves (1) and (2) uniformly for real T.
Floors and integer transitions in M affect neither N<=T/(2 pi) nor
any absolute constant above.

If I(T)>=cTL, (10) gives I_cap(T)>=T(cL-C_*), which is at least
c'TL once L>=C_*/(c-c'). The converse follows pointwise from
min(x,L^4)<=x. These arguments apply unchanged on an unbounded
sequence. Finally C481a's inequality I(T)<=L^(-2)integral|U_T|
gives the stated conditional downstream consequence, with its exact
fixed-cutoff ratio component. It supplies no missing premise.

## Mathlib

Full matching and supporting Mathlib coverage have not been checked.
The imported analytic theorem remains a cited informal input. The
finite algebra, divisor-count comparison, compact integrations and
tail inequality are proved above; this is not a formal verification.
Unknown availability is not evidence of absence.
