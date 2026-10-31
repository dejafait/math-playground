# Lemma 485: restricted Maples--Rodgers local density second moment

## Hypotheses

Let N(sigma,U) count nontrivial zeta zeros beta+i gamma with
beta>sigma and 0<gamma<U, with their full multiplicities. All
logarithms are natural. Take real T>=2, 1<=H<=T^(1/4), and
1/2<=sigma<=1. Write L=log T and d=sigma-1/2.

The source is Kenneth Maples and Brad Rodgers, *Bootstrapped zero
density estimates and a central limit theorem for the zeros of the
zeta function*, International Journal of Number Theory 11 (2015),
2087--2107, [arXiv:1404.3080v2, 4 June 2016](https://arxiv.org/html/1404.3080v2),
also [the versioned PDF](https://arxiv.org/pdf/1404.3080v2).
Use these two cited inputs, with constants uniform in the displayed
parameters:

1. Theorem 2.4, printed p. 5: for fixed b in (0,1), U>=2,
   and 1/2<=s<=1,

       N(s,U) <= C_b U log U exp(-b(s-1/2)log U).          (D)

2. Corollary 4.2, Section 4, printed pp. 8--10: put

       Q(x)=1/[pi(1+x^2)],
       ||w||_Q=pi sup_x (1+x^2)|w(x)|,
       M_1 eta(x)=sum_(ell in Z) sup_[ell,ell+1) |eta|
                                     *1_[ell,ell+1)(x),
       epsilon_T(eta)=sum_(|ell|>sqrt(T)) log(|ell|+2)
                                     sup_[ell,ell+1) |eta|.

   For a nonnegative macroscopic weight w of finite Q-norm and
   a test function for which the right side is finite, the conclusion
   at the fixed exponent 3 is

       integral_R w(t/T)/T
          |sum_rho eta(L(gamma-t)/(2pi))|^3 dt
       <= C ||w||_Q [||M_1 eta||_1^3
                              +(epsilon_T(eta) L)^3].     (M)

   The sum includes all nontrivial zeros with multiplicity and both
   signs of the ordinate. We use only w=Q and eta(x)=Q(x/H).
   The cell supremum is the convention actually used in the source's
   proof; a maximum on a half-open cell need not be attained.

The arithmetic inputs behind (D) and (M), including Selberg/Jutila
and Fujii's corrected count-moment theorem, remain citations, without
an independent manuscript audit. Corollary 4.2 is imported within its
stated hypotheses; no assertion that every intermediate line of its
proof has been audited is made. Standard conjugation and functional-
equation symmetries of zeta preserve zero multiplicities. No RH,
simplicity, spacing, selected-value moment, or external fixed-half-plane
premise is used. In particular, general-weight equation (19) and
Lemma 4.3 are not imported.

## Conclusion

There is an absolute C, independent of T,H,sigma, such that

    (1/T) integral_0^T
       |N(sigma,t+H/log T)-N(sigma,t)|^2 dt
        <= C H^2 T^(-(sigma-1/2)/4).                    (1)

This is precisely the k=2,c=1/4 specialization of the source's
Proposition 2.5, printed p. 5. It is a reproduction of a known
conclusion, with a restricted repair of the normalization and
upper-tail steps in Section 4, (18)--(23), printed pp. 10--12.
It is not a new zero-density theorem or an independent audit of the
source's arithmetic inputs. The strict beta>sigma convention is
retained, including at sigma=1/2 and sigma=1. No closed-horizontal-
endpoint theorem, padded-height kernel application, weighted pair-mass
estimate, positivity statement, or RH conclusion is asserted.

## Proof

### 1. Fix the displacement scale and use only upper-tail density

First take T>=16. For each zero put

    A_rho(T)=(beta-1/2)log T,  alpha=d log T.

This is exactly source equation (8). The relevant upper-tail cutoff
in the A variable is alpha, not d. We establish the following estimate
for every alpha>=0, still with this one base T:

    sum_(rho: gamma != 0) Q(gamma/T)
                    1_{|A_rho(T)|>alpha}
        <= C T log T exp(-alpha/2).                     (2)

All sums count each multiplicity separately. For positive ordinates
at height U=n^2 T, n>=1, one has exactly

    A_rho(U)=A_rho(T) log U/log T.

If alpha/log T>=1/2 the strict selected set is empty, since nontrivial
zeros have 0<beta<1. Otherwise reflection beta -> 1-beta at the same
positive ordinate shows that its cumulative count is

    #{rho:0<gamma<U, |A_rho(T)|>alpha}
      =2 N(1/2+alpha/log T,U)
      <=2 C_(1/2) U log U
                         exp(-(alpha/2) log U/log T)
      <=2 C_(1/2) U log U exp(-alpha/2).                (3)

Here (D) is used with the fixed b=1/2; at alpha=0 the critical-line
zeros are excluded on both sides of the equality. In normalized
coordinates the cutoff at height U is alpha log U/log T, so (3)
does not silently reuse A_rho(T) as A_rho(U).

Partition the positive ordinate axis into [(n-1)^2 T,n^2 T),
intersected with (0,infinity). In each bin Q(gamma/T) is at most
Q((n-1)^2), and its selected count is bounded by (3). A zero at
gamma=n^2 T belongs to the next bin, whose cumulative upper endpoint
is strictly larger; no equality zero is lost. Consequently the
positive-ordinate sum is at most

    C exp(-alpha/2)
       sum_(n>=1) Q((n-1)^2) n^2 T log(n^2 T)
      <= C' T log T exp(-alpha/2).

The constant is uniform in T>=16: after division by T log T the
summands are bounded by a constant times
Q((n-1)^2)n^2(1+log n), a summable sequence (its tail is
O((1+log n)/n^2)). Conjugation supplies the same bound for negative
ordinates. This proves (2). Only cumulative upper-tail counts were
used; no passage from tail bounds to arbitrary piecewise-continuous
weights, as in the source's (19), is needed.

### 2. Uniform Cauchy convolution bound

Put a=2pi H/log T and q_T(t)=Q(t/T)/T. For T>=16 and
H<=T^(1/4), one has 0<a<=T, since
a/T<=2pi T^(-3/4)/log T<1 at T=16 and the latter expression
decreases thereafter. For every real y,

    integral_R q_T(t) Q((y-t)/a) dt
        <=12 (a/T) Q(y/T)
        <= C H/(T log T) Q(y/T).                       (4)

Here is an elementary bound, avoiding an implicit normalization of
the Cauchy convolution. If |y|<=T, q_T(t)<=1/(pi T), while
integral_R Q((y-t)/a)dt=a. Since Q(y/T)>=1/(2pi), the
integral is at most 2(a/T)Q(y/T). If |y|>T, split at
E={t:|t|>=|y|/2}. On E, q_T(t)<=4q_T(y), so the integral
over E is at most 4(a/T)Q(y/T). On its complement,
|y-t|>|y|/2, so Q((y-t)/a)<=4a^2/(pi y^2). The integral
of q_T on that complement is at most 1. As a<=T and y^2>T^2,

    4a^2/(pi y^2) <= 8(a/T)Q(y/T).

Adding the two pieces proves (4), with constants independent of y,H,T.

### 3. Keep the actual far-tail error in the count moment

Let eta=Q_H, where Q_H(x)=Q(x/H). The evenness and monotone
decrease of Q on [0,infinity) give

    ||M_1 Q_H||_1=2 sum_(m>=0) Q(m/H)
        <=2/pi+2 integral_0^infinity Q(x/H) dx
        =2/pi+H <= C H.                                (5)

For |ell|>sqrt(T)>=4 and u in [ell,ell+1),
|u|>=|ell|-1>=(3/4)|ell|. Thus

    sup_[ell,ell+1) Q_H <= C H^2/ell^2,
    epsilon_T(Q_H)
        <= C H^2 sum_(ell>sqrt(T)) log(ell+2)/ell^2
        <= C H^2 log T/sqrt(T).                        (6)

The last inequality follows by comparison with the integral of
log(x+2)/x^2; integration by parts bounds its tail by
C log(R+2)/R for R>=4. In particular,

    epsilon_T(Q_H) log T
        <= C H [H (log T)^2/sqrt(T)]
        <= C H [T^(-1/4)(log T)^2] <= C' H.             (7)

The last factor is bounded on T>=16 (write it as x^2 exp(-x/4),
x=log T); it tends to zero. Since ||Q||_Q=1, (M), (5) and
(7) imply, for

    W(t)=sum_rho Q((gamma-t)/a),

that

    integral_R q_T(t) W(t)^3 dt <= C H^3.               (8)

The source's assertion following (23) that epsilon_T(Q_H) itself
decreases to zero throughout the allowed H range is not correct.
Indeed take H=T^(1/4) and R=sqrt(T). There are at least R/2
integers R<ell<=2R. Each contributes at least
(log T)/(10pi R), because log(ell+2)>=(log T)/2 and
Q(ell/H)>=1/[pi(1+4R)]>=1/(5pi R). Hence
epsilon_T(Q_H)>=(log T)/(20pi). Together with (6) it is of
order log T at this endpoint. This does not invalidate (8): the
quantity required by (M) is epsilon_T(Q_H)log T=O(H),
which (7) proves uniformly. We have not dropped the far-tail term.

### 4. The two Holder steps

Define the nonnegative selected sum

    V(t)=sum_(rho:gamma != 0) 1_{|A_rho(T)|>alpha}
                                      Q((gamma-t)/a).

By Tonelli, (4) and (2),

    integral_R q_T(t)V(t)dt
        <= C H/(T log T)
             sum_(rho:gamma != 0) Q(gamma/T)
                                   1_{|A_rho(T)|>alpha}
        <= C H exp(-alpha/2).                          (9)

For a finite zero sum, Holder with exponents 4 and 4/3 gives

    (sum f_rho q_rho)^2
        <= (sum f_rho^4 q_rho)^(1/2)
                                      (sum q_rho)^(3/2),

where q_rho=Q((gamma-t)/a) and f_rho is the selected indicator
(zero also when gamma=0). Since f_rho^4=f_rho, passage through
increasing finite subsets gives V(t)^2<=V(t)^(1/2)W(t)^(3/2).
Cauchy--Schwarz for the positive measure q_T(t)dt, followed by
(9) and (8), now yields

    integral_R q_T(t)V(t)^2 dt
       <= (integral_R q_T V)^(1/2)
                                  (integral_R q_T W^3)^(1/2)
       <= C H^2 exp(-alpha/4).                         (10)

All exchanges and limiting inequalities involve nonnegative terms.
Equivalently one can integrate the finite-subset inequalities first
and use monotone convergence; (8)--(9) supply the required finite
integral bounds. No absolute-convergence or dominated-limit premise
about a signed series is implicit here.

### 5. The one-sided indicator and endpoints

For 0<=t<=T, put h=H/log T. The difference in (1) is exactly
the count of beta>sigma and positive gamma in [t,t+h), with
the convention at gamma=0 excluded. Such a zero satisfies
A_rho(T)>alpha and

    0 <= L(gamma-t)/(2pi) < H/(2pi).

For every real x,

    1_{0<=x<=H/(2pi)} <= C_0 Q(x/H),
    C_0=pi(1+1/(4pi^2)).                               (11)

This follows from the minimum of Q on [0,1/(2pi)]; outside
the interval the left side is zero. Therefore the count difference
is at most C_0 V(t), even when t is itself a zero ordinate.
Also Q(t/T)>=1/(2pi) on [0,T]. Integrating (11) squared
and then using (10) proves

    (1/T) integral_0^T |N(sigma,t+h)-N(sigma,t)|^2 dt
       <=2pi C_0^2 integral_R q_T(t)V(t)^2 dt
       <= C H^2 exp(-alpha/4)
        = C H^2 T^(-d/4).

This accounts for both the missing constant in the source's final
indicator comparison and the window's factor 2pi. The earlier
choice alpha=d log T accounts for its missing displacement factor.
At sigma=1 the count is empty. At sigma=1/2 the strict selection
excludes beta=1/2 and the bound remains uniform. Repeated zeros
have been repeated in every sum; no assertion of simplicity or
distinct ordinates entered any Holder step. The strict vertical
definition of N gives [t,t+h), not an unannounced closed-count
convention. The closed interval in (11) is only a pointwise majorant.

For 2<=T<=16 the allowed H and h lie in fixed compact intervals.
All counted zeros lie in one fixed bounded rectangle, which contains
finitely many zeros with finite orders. The left side of (1) is
therefore uniformly bounded, while H^2 T^(-d/4)>=16^(-1/8).
Increasing the absolute constant extends the result to the stated
full range. No effective numerical value of C is claimed.

The replay thus recovers the exact approved threshold from the two
named count-only inputs. It does not require repairing or adopting
the arbitrary-weight assertion (19). L471's pair-quotient weights,
the mesoscopic sector of its negative-mass majorant, and all-degree
mixed positivity remain separate unresolved questions; these are
prospective uses, not inputs to this proof.

## Mathlib

Full matching coverage for (1) has not been checked. Coverage for
the imported density and count-moment theorems and supporting
measure-theoretic inequalities has likewise not been checked.
Unknown availability is not an absence claim. The complete restricted
specialization and repairs are above; the primary mathematical inputs
remain the explicitly cited Theorem 2.4 and Corollary 4.2.
