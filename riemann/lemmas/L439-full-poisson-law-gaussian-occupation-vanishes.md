# Lemma 439: the full Poisson law has vanishing Gaussian occupation statistic

## Hypotheses

Use exactly L438's complete law nu_(H,t), with uniform height marginal
dt/H on [H,2H], ell=log H, its high component, both signed intermediate
components, and its translated six-state bulk. Keep L429's already chosen
cutoff j(H), without enlarging its thresholds. Thus j(H)->infinity,
M_j<=ell^(1/8), E_H P_j=1+o(1), and the normalization of L438 is
N_H=E_H(wP_j)=1+o(1), g_H=P_j/N_H. Here

    P_j(t)=product_(p<=p_j) (1-1/p)/|1-p^(-1/2-it)|^2,
    M_j=product_(p<=p_j) (1+p^(-1/2))/(1-p^(-1/2)),
    E_H=H^(-1) integral_[H,2H].

The complete bulk has atoms m +/- sqrt(3) Sigma^(1/2) u_i, where
m=O(1), Sigma=ell g_H K+A_H is positive definite,
||A_H||=O(ell^(1/2)), K is fixed, and the u_i are exactly L419's
orthonormal Borel basis as retained in L438. No basis is replaced.
All constants are uniform on an eventual real-H ray.

Use L424's fixed test

    Q(a,b,d)=exp(-a^2-b^2)[b^2(1-2a^2)+ad(1-2b^2)].

The prior EXPLORE assessment is
`drafts/literature/2026-10-19-full-three-prime-law-occupation-defect.md`.

## Conclusion

For this unchanged complete family,

    E_nu |Q(X/sqrt(ell))| -> 0.                         (1)

In particular limsup |E_nu Q(X/sqrt(ell))|=0: the proposed nonzero
leading-scale occupation defect does not occur. This stops precisely
that fixed test at the o(1) scale. It does not establish the much smaller
O(1/(H log H)) trajectory budget, realize the law by a C^2 function,
or settle actual clipping, capped nondegeneracy, L413's full-error
regulator margin, global mixed positivity or RH. The local extension
is POTENTIALLY_NEW only in the limited source-comparison sense;
originality is not established. The separate step-255 critical audit
below validates precisely this absolute o(1) conclusion.

## Proof

The finite Poisson inputs are imported through L429, with their precise
source C. Aistleitner, I. Berkes and K. Seip, *GCD sums from Poisson
integrals and systems of dilated functions*, JEMS 17 (2015), 1517--1546,
DOI 10.4171/JEMS/537, section 3, p. 1527, identity preceding Lemma 1
and (23), [published primary text](https://ems.press/content/serial-article-files/32047?nt=1).
Only its finite-product scope is used; no infinite product measure or
moving-test Haar theorem is invoked. The mean bound and cutoff are
L429's already established actual-height statements. The additional
estimates below are needed because those statements do not themselves
evaluate the nonlinear moving observable. We import Euler's named
theorem sum_p 1/p=infinity through L428; its inspected reference is
D. Rusin, *328K Spring 2017 zeta note*, unnamed theorem, pp. 1--2,
[complete elementary proof](https://web.ma.utexas.edu/users/rusin/328K-17a/zeta.pdf).
No prime number theorem or quantitative prime distribution is needed.

### Actual-height concentration with the existing cutoff

Write y=p_j and S_j=sum_(p<=y) 1/p. An elementary consequence of the
finite product, useful for controlling its frequencies, is

    M_j >= product_(p<=y)(1-p^(-1/2))^(-1)
        >= sum_(n<=y) n^(-1/2) >= sqrt(y).              (2)

Indeed each numerator 1+p^(-1/2) is at least one. Expanding the finite
product of convergent geometric series gives a positive sum over the
integers having no prime factor greater than y; this includes every
integer n<=y. There are y such integers, each at least y^(-1/2).
Consequently y<=M_j^2<=ell^(1/4). This uses the saved cutoff only.

For ell sufficiently large set

    k0=ceil(8 log(ell)/log 2), X=y^k0,
    T_H(t)=sum_(p<=y) sum_(1<=k<=k0)
                          p^(-k/2) exp(i k t log p)/k,
    c_j=sum_(p<=y) log(1-1/p).

The absolutely convergent scalar logarithm series, taken at each of
finitely many radii p^(-1/2)<1, gives the exact real identity

    log P_j(t)=c_j+2 Re T_H(t)+R_H(t),
    ||R_H||_infinity
        <=2 y 2^(-(k0+1)/2)/(1-2^(-1/2))
        =O(ell^(-15/4)).                               (3)

This follows by dropping 1/k from each omitted term and using j<=y.
There is no logarithm branch issue: the real part of -log(1-z) equals
-log|1-z| on |z|<1. Also

    c_j=-S_j+O(1),                                     (4)

uniformly in j, since the difference is bounded by
sum_(n>=2) sum_(k>=2) n^(-k)/k<infinity.

All integers n=p^k in T_H are distinct, by unique factorization, and
lie between 2 and X. Denote their positive coefficients by a_n. Their
sum A satisfies

    A<=sum_(p<=y) p^(-1/2)/(1-p^(-1/2))
      <=C sum_(p<=y) p^(-1/2)<=C log M_j=O(log ell),    (5)

because log((1+r)/(1-r))>=2r for 0<r<1. Their square sum satisfies

    sum_n a_n^2=S_j+O(1),                              (6)

since the k>=2 contribution is bounded by
sum_(n>=2) sum_(k>=2) n^(-k)<infinity.

For a nonzero real frequency u, exact integration over the sharp
interval gives |E_H exp(iut)|<=2/(H|u|). If distinct integers n,m
are at most X, then |log(n/m)|>=1/X: for n>m integrate 1/v on
[m,n]. Thus, retaining every off-diagonal term,

    |E_H |T_H|^2-sum_n a_n^2|<=2 X A^2/H.

Moreover log(nm)>=log 4 for every pair, so

    |E_H T_H^2|<=2 A^2/(H log 4).

Since (2 Re T_H)^2=2|T_H|^2+2 Re(T_H^2), (5)--(6) imply

    E_H(2 Re T_H)^2=2S_j+O(1)+O(X A^2/H).             (7)

These are direct finite exponential-sum estimates at the actual
heights, not an independence assertion. By (2),

    log X=k0 log y<= (2/log 2)(log ell)^2+(log ell)/4,

so X A^2/H->0 as real H->infinity, since H=exp(ell).
Equations (3)--(7) therefore hold uniformly along every allowed
selection of L429's thresholds, including their endpoints.

Euler's theorem and j(H)->infinity give S_j->infinity. On the set
log P_j>-S_j/2, equations (3)--(4) force 2 Re T_H>S_j/3 for every
sufficiently large H. Chebyshev's inequality and (7) yield

    E_H 1_{log P_j>-S_j/2} <= C(S_j+1)/S_j^2 ->0.      (8)

For each fixed delta>0, eventually -S_j/2<log delta, so
{P_j>delta} is contained in this exceptional set. Thus P_j tends
to zero in probability with respect to the actual normalized height
measures, even though E_H P_j->1. The changing height spaces cause
no difficulty: (8) is a finite-H measure estimate.

### Fractional moments without assumed uniform integrability

For each fixed q in (0,1) and delta>0, Holder's inequality gives

    E_H P_j^q
      <=delta^q+(E_H P_j)^q (E_H 1_{P_j>delta})^(1-q).

L429 bounds E_H P_j by two eventually. First let H tend to infinity
in this inequality using (8), then let delta decrease to zero.
Consequently E_H P_j^q->0. In particular, because N_H->1,

    E_H sqrt(g_H)=N_H^(-1/2) E_H sqrt(P_j)->0.          (9)

This proves the needed integrability estimate. It does not assume
uniform integrability of P_j, nor replace the moving test by a fixed
Haar test. No new threshold is added to the cutoff definition.

### Every component and every branch of the exact law

L424 proves the global quadratic bound

    |Q(a,b,d)|<=a^2+b^2+d^2.                          (10)

By L438 (9), the full high component contributes at most
E_H[p|Y|^2]/ell=O(ell^-3) to (1). By L438 (10)--(12), the sum of
the two intermediate raw second integrals is O(ell^(1/2)); hence
both intermediate contributions together are O(ell^-1/2). This
retains their signed directions and needs no lower bound on their
first two coordinates.

For the bulk a second global bound avoids all basis stability issues.
For s>=0, |(1-2s)exp(-s)|<=1, as checked in L424. Also
sup_(u>=0) u exp(-u^2)=1/sqrt(2e). Applying these to the two terms
of Q separately gives

    |Q(a,b,d)|
       <=(|b|+|d|)/sqrt(2e)
       <=sqrt(a^2+b^2+d^2)/sqrt(e).                    (11)

The first term uses b^2 exp(-b^2)<=|b|/sqrt(2e); the second uses
|a|exp(-a^2)<=1/sqrt(2e). In particular no Gaussian suppression
of a state with only a large third coordinate is assumed.

For each actual unit vector u_i and each sign, the normalized atom V
satisfies, with the full correction still present,

    |V|=|m +/- sqrt(3) Sigma^(1/2)u_i|/sqrt(ell)
       <=C ell^(-1/2)+sqrt(3||Sigma||/ell)
       <=C[ell^(-1/2)+sqrt(g_H)+ell^(-1/4)].           (12)

Here ||Sigma||/ell<=g_H||K||+||A_H||/ell, positivity of Sigma
identifies its square-root norm, and sqrt(u+v)<=sqrt(u)+sqrt(v)
for nonnegative u,v. Every Borel branch, equality case and second
selection stage obeys (12), because only |u_i|=1 is used. The
translation is included by the triangle inequality; it is not deleted
or approximated through a compact-Hessian claim.

Averaging (11)--(12) over the six states and multiplying by 0<=w<=1
bounds the complete bulk contribution by

    C[E_H sqrt(g_H)+ell^(-1/4)+ell^(-1/2)]=o(1),       (13)

using (9). Adding (10)'s rare-component bounds proves (1). Thus the
absolute statistic vanishes, with no cancellation between components.
L424's globally bounded chi also makes its kappa correction
O(1/(H ell^2)) for this probability law, so retaining that correction
does not change the zero-limsup conclusion. We do not compare (13)'s
unquantified convergence with L424's smaller trajectory budget.

### Separate critical audit — 2026-10-19, step 255

**Scope and verdict.** The pre-existing SPECIALIZE assessment
`drafts/literature/2026-10-19-full-law-gaussian-vanishing-critical-audit.md`
covers this audit. All of (2)--(13) have been checked against L429's
original cutoff and mean, L438's complete component and matrix bounds,
L424's fixed Q and trajectory identity, and L428's imported Euler
divergence. The conclusion (1) passes without a construction change,
new threshold, new mathematical input or numerical evidence. This is
verification of the local result, not a claim of originality or RH.

**Cutoff and complete logarithm.** The finite geometric product in (2)
contains every integer n<=y because y is itself the largest included
prime. Its positive expansion is legitimate at the finitely many radii
p^(-1/2)<1. Each of its y indicated summands is at least y^(-1/2),
so y<=M_j^2. The already imposed log B_j>=M_j^8 therefore gives
y<=ell^(1/4) for every H in [B_j,B_(j+1)), including the left endpoint.
There is no assumption on the lengths of these stages from above.

For the logarithmic series, the omitted sum at each prime is at most
2^(-(k0+1)/2)/(1-2^(-1/2)); multiplication by twice the number of
primes bounds the complete real logarithmic tail. Since
k0>=8 log ell/log 2, this gives (3)'s O(ell^(-15/4)). The comparison

    sum_(n>=2) sum_(k>=2) n^(-k)
      =sum_(n>=2) 1/(n(n-1))=1

controls both the constant logarithmic remainder in (4) and the
higher-power square sum in (6). The finite Fourier coefficients obey
a_(p^k)=p^(-k/2)/k; prime-power uniqueness prevents cross-prime
diagonal collisions. In (5), 1/(1-p^(-1/2)) is uniformly bounded
by 1/(1-2^(-1/2)), and log((1+r)/(1-r))>=2r gives A=O(log ell).
These constants do not grow with j, k0 or H.

**Sharp-height second moment and exceptional set.** Exact exponential
integration gives 2/(H|u|), with both sharp endpoints retained. For
distinct prime powers n,m<=X, |log(n/m)|>=1/X, while all sum
frequencies satisfy log(nm)>=log 4, including n=m. Summing absolute
coefficient products costs at most A^2 in each case. In particular
there is no unaccounted zero frequency in T_H^2. The identity for
(2 Re T_H)^2 gives the diagonal 2 sum a_n^2 and an error bounded
by 4XA^2/H+4A^2/(H log 4), proving (7). Further,

    log(XA^2/H)<=-ell+O((log ell)^2)+O(log log ell)

whenever A>0; hence that error tends to zero uniformly under the saved
cutoff. This reasoning concerns the actual height variable and uses no
independent prime phases or moving-test equidistribution.

Writing c_j=-S_j+O(1) with a uniform constant and using (3), the event
log P_j>-S_j/2 implies 2 Re T_H>S_j/3 once S_j is large. Markov's
inequality applied to the square (equivalently the uncentered
Chebyshev bound) gives at most 9 E_H(2 Re T_H)^2/S_j^2. Its limit is
zero because Euler divergence and j(H)->infinity give S_j->infinity.
No centering or estimate for E_H T_H is needed. For fixed delta>0,
the inclusion {P_j>delta} subset {log P_j>-S_j/2} holds eventually;
this checks the direction of the comparison in (8).

**Fractional moment and limit order.** At every fixed H, Holder with
exponents 1/q and 1/(1-q) gives

    E_H[P_j^q 1_(P_j>delta)]
       <=(E_H P_j)^q Pr_H(P_j>delta)^(1-q).

On the complementary set the integrand is at most delta^q.
The uniform eventual bound E_H P_j<=2 is L429 (10), not a consequence
of probability convergence. For each fixed delta the limsup is at
most delta^q; only then is delta sent to zero. This verifies (9) with
N_H->1 from L438 (13). These finite-H estimates apply on different
height probability spaces and do not presume uniform integrability of
P_j itself. In particular its nonvanishing first mean is compatible
with the concentration conclusion.

**Complete law, covariance and all basis choices.** L438 (9) gives
E_H[p|Y|^2]=O(ell^-2), including large third coordinates. Its two
intermediate degree-two costs are each O(ell^(1/2)) by (10)--(12).
Applying L424's global quadratic bound after division by ell yields
O(ell^-3) and O(ell^-1/2), respectively. Neither intermediate sign
is canceled or omitted, and pointwise rarity of the high state is
unnecessary.

For completeness the scalar factor |(1-2s)e^(-s)| has maximum one
on s>=0: it decreases on [0,1/2], and the positive branch
(2s-1)e^(-s) has maximum 2e^(-3/2)<1. Also
sup_(v>=0) v e^(-v^2)=1/sqrt(2e). These facts bound the first Q
term by |b|/sqrt(2e) and the second by |d|/sqrt(2e). Cauchy--Schwarz
gives (11) with constant 1/sqrt(e). Thus the estimate is global even
when a and b are small and d is large.

L438 (14)--(15) gives m=O(1), positive definite Sigma, and
||A_H||=O(ell^(1/2)) for its recomputed full matrix. For every actual
unit u_i, ||Sigma^(1/2)u_i||<=sqrt(||Sigma||). The triangle inequality
with ||Sigma||<=ell g_H||K||+||A_H|| proves (12), retaining off-diagonal
entries, the mean, and all equality and second-stage basis branches.
No continuity of the basis is used. Averaging over its six equal
conditional masses and 0<=w<=1 proves (13). Together with the rare
bounds this proves the absolute expectation in (1), not merely a
cancellation in the signed expectation. L424's global chi bound and
uniform height marginal separately give O(1/(H ell^2)) for the kappa
correction.

**Limitations retained.** L424's necessary trajectory test bounds the
signed expectation by its explicit delta_H=O(1/(H ell)). The above
absolute upper bound tends to zero without comparison to delta_H;
it proves neither satisfaction nor violation of that finer condition.
The nonzero-limsup diagnostic is retired at exactly its stated scale.
No actual/global realization, clipping, capped nondegeneracy, full-error
regulator margin, mixed positivity or RH conclusion follows. The direct
mathematical inputs remain exactly those recorded for L439 in the DAG.

## Mathlib

Full matching Mathlib coverage for this moving Poisson concentration
and complete-law occupation comparison has not been checked. The
finite Poisson identity and Euler reciprocal-prime divergence are
imported with the precise references above. Elementary geometric/log
series, sharp exponential integration, Chebyshev and Holder are used
explicitly; supporting formal results would not alone formalize this
complete application. No numerical evidence or mathematical script is
used as proof. The separate informal audit above does not change the
unchecked status of a full matching formalization.
