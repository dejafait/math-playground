# Lemma 478: complete residual moments and a failed termwise certificate

## Hypotheses

Use L477 (1)--(2) with its exact theta and fixed cutoff
M=floor(sqrt(T/(2pi))) on the closed interval [T,2T]. Put L=log T,
let T tend to infinity through arbitrary real values, and set

    c_nm=log(n/m)^2/sqrt(nm),             1<=n,m<=M,
    U(t)=sum_(n,m<=M)c_nm exp(it log(m/n)),
    V(t)=sum_(n,m<=M)c_nm exp(-it log(nm)),
    C(t)=exp(2i theta(t)) V(t).

Thus U is real and R_T=U+(C+conjugate(C))/2 exactly. No zero,
spacing, random-phase or external zero-free assumption is made.
The retained analytic phase input is

    2theta'(t)=log(t/(2pi))+O(T^(-2)),
    2theta''(t)=1/t+O(T^(-3)),             T<=t<=2T.       (1)

Write I_k=integral_T^(2T)|R_T(t)|^k dt for k=2,4.

The certificate tested here expands the complete even powers, keeps
constant phases exactly, and bounds each remaining integral separately
in absolute value: for a nonconstant linear phase use
min(T,2/|log r|), and for a phase retaining theta use the uniform
second-derivative bound C_k sqrt(T). The constants C_k>=1 are fixed
sufficient constants for the stated derivative test. This is a
specified majorant, not an optimal estimate for an individual integral.

## Conclusion

The finite expansions and grouped moment/error formulas (2)--(7)
below retain all ratio/product cross terms, coincidences, endpoints
and stationary points. If D_2 is the complete constant-phase mass,
then

    0<D_2<=C L^8.                                          (8)

In the U C cross term there is a fixed positive-density box of indices
with interior stationary points. Its coefficient sum, multiplied by
sqrt(T), is comparable to T^(3/2), as proved in (10)--(12).
Consequently the specified absolute-integral majorant E_2 satisfies

    E_2>=c T^(3/2),
    max(0,T D_2-E_2)=0                   eventually.        (9)

Thus this certificate supplies no positive lower bound for I_2 and
cannot certify I_2^(3/2)/I_4^(1/2)>=c T L^3. This is an informative
failure of the specified bound, not a bound on the actual signed
error, the true quotient, or integral |R_T|. There is no RH conclusion,
little-o conclusion, or rejection of L477's fixed square.
The exact arithmetic regrouping (13) isolates a possible next target;
its cancellation is not proved here. This bounded attempt specializes
standard interpolation and derivative tests, without a claim of
novelty beyond the sources checked. A separate critical audit remains.

## Proof

### 1. Both complete even powers

Straight finite multiplication gives

    R_T^2=U^2+|V|^2/2
             +2 Re(exp(2i theta) U V)
             +(1/2) Re(exp(4i theta) V^2),                 (2)

and

    R_T^4=U^4+3U^2|V|^2+(3/8)|V|^4
      +2 Re(exp(2i theta)[2U^3 V+(3/2)U V^2 conjugate(V)])
      +2 Re(exp(4i theta)[(3/2)U^2 V^2
                                      +(1/4)V^3 conjugate(V)])
      +2 Re(exp(6i theta) U V^3/2)
      +2 Re(exp(8i theta) V^4/16).                         (3)

For example, expand (U+(C+conjugate(C))/2)^4. The charge-zero
parts of its quadratic and quartic C terms are respectively
3U^2|V|^2 and 6|V|^4/16. The charge-one part consists of
2U^3 C and (3/2)U C^2 conjugate(C), with their conjugates.
This checks all binomial factors and includes every cross term.

For an exact grouping not reliant on distinct frequencies, use atoms
(q,r,w) indexed as follows, including zero coefficients if desired:

    (0,m/n,c_nm), (1,1/(nm),c_nm/2), (-1,nm,c_nm/2).

R_T is their sum w exp(i(2q theta+t log r)). For k=2,4 define
a_k(q,r) to be the sum of products of weights over all ordered k-tuples
of these atoms with total charge q and rational product r. These are
finite, nonnegative numbers; equality of rational products is exact,
not approximate. Then

    R_T(t)^k=sum_(q,r) a_k(q,r)
                             exp(i(2q theta(t)+t log r)),
    |q|<=k,   D_k=a_k(0,1),
    I_k=T D_k+sum_((q,r)!=(0,1)) a_k(q,r) J(q,r),
    J(q,r)=integral_T^(2T)exp(i(2q theta(t)+t log r))dt.      (4)

Conjugation pairs make (4) real. Since theta''>0 eventually,
only q=0,r=1 is a constant phase. In particular no theta term is
silently added to D_k.

For q=0,r!=1, direct integration, retaining both interval endpoints,
gives |J|<=min(T,2/|log r|). For q!=0, (1) gives uniformly

    |(2q theta+t log r)''|=|q/t+O_k(T^(-3))|
                               >=|q|/(4T).

Apply Tao, *247B Lecture Notes 8*, Section 2, Lemma 2.5 (printed
p. 5), k=2 derivative case, lambda=1 and c=|q|/(4T).
It gives |J|<=C_k sqrt(T) for 1<=|q|<=k. The phase is real and
smooth, the derivative bound holds on the entire closed interval,
and the constant is uniform in r and T. This includes interior and
endpoint stationary points; no first-derivative condition is needed.
The primary source and proof were inspected in the invocation-start
assessment: [author's notes](https://www.damtp.cam.ac.uk/user/gold/pdfs/teaching/notes8.pdf).
Thus, with exactly the specified majorant,

    E_k=sum_(r!=1) a_k(0,r) min(T,2/|log r|)
                   +C_k sqrt(T) sum_(q!=0,r) a_k(q,r),
    |I_k-T D_k|<=E_k,                    k=2,4.             (5)

No infinite sum, independence, separation assumption or limit
interchange occurs. Formula (5) is a full lower estimate for I_2
and upper estimate for I_4, even when its lower estimate is zero.

For completeness, dyadic blocks give, for each fixed j>=0,

    sum_(n<=M)log(M/n)^j/sqrt(n)<=C_j sqrt(M),
    S=sum_(n,m<=M)c_nm<=C M.                               (6)

The first inequality follows by summing
C sqrt(M)2^(-h/2)(1+h)^j on M/2^(h+1)<n<=M/2^h,
including the final block containing 1. The second follows from
|log(n/m)|^2<=2log(M/n)^2+2log(M/m)^2 and factorization.
The total atom weight is 2S. Hence (4)--(5) are finite, and the
simple pointwise bound |R_T|<=2S also gives the complete upper bound

    I_4<=T(2S)^4<=C T^3.                                  (7)

It is very weak; it does not replace any missing second-moment lower
bound. No polynomial length is reduced when expanding either power.

### 2. The complete second-moment constant phase

For coprime a,b<=M with a!=b, the coefficient of frequency b/a
in U is

    u_ab=log(a/b)^2 H_floor(M/max(a,b))/sqrt(ab),
    H_j=sum_(d<=j)1/d.

This follows by writing n=da,m=db, so it groups every coincidence.
Set v_h=sum_(nm=h;n,m<=M)c_nm, also keeping every factorization.
Equation (2) then gives exactly

    D_2=sum_(a,b<=M;gcd(a,b)=1;a!=b)u_ab^2
                              +(1/2)sum_(h<=M^2)v_h^2.

There are no other constant phases. In the first sum,
|log(a/b)|<=log M and H_j<=1+log M, so it is at most
(log M)^4(1+log M)^2(sum_(a<=M)1/a)^2=O((log(2M))^8).
In the second sum,

    v_h<= (log M)^2 d(h)/sqrt(h),
    sum_(h<=M^2)d(h)^2/h <=(1+log(M^2))^4.

Here d(h)^2<=d_4(h): each pair d,e dividing h maps injectively to
(gcd(d,e), d/gcd(d,e), e/gcd(d,e), h/lcm(d,e)), an ordered
four-factor factorization of h. Summing d_4(h)/h and enlarging to
four independent factors <=M^2 proves the displayed harmonic bound.
Both contributions are therefore O(L^8). For M>=2, u_12>0,
so D_2>0. This proves (8) with constants uniform in real T.

### 3. A positive-density stationary box for the failed majorant

The exact U C term in (2) has, for every n,m,k,l<=M, positive
coefficient c_nm c_kl and phase

    f(t)=2theta(t)+t log(m/(nkl)).

Take all integer tuples in the following closed boxes:

    .89M<=n<=.91M,    .24M<=m<=.26M,
    .79M<=k<=.81M,    .49M<=l<=.51M.                       (10)

For sufficiently large M there are at least c M^4 such tuples.
Every tuple has

    alpha M^2 <= nkl/m <= beta M^2,
    alpha=(.89*.79*.49)/.26 >1,
    beta =(.91*.81*.51)/.24 <2.                           (11)

Since X^2=T/(2pi) and M=floor X, X^2/M^2 tends to 1
uniformly through real T. Therefore (1) implies, uniformly over
(10), f'(T)<-delta and f'(2T)>delta for some fixed delta>0
and all sufficiently large T. Also f''>0 on [T,2T]. There is
exactly one interior stationary point. In fact it stays a fixed
positive fraction of T away from the endpoints: solving f'=0
in (1) gives t_*=2pi(nkl/m)(1+O(T^(-2))), and (11) is bounded
away from 1 and 2. This statement locates the point only; no
stationary-phase asymptotic is asserted or used.

On (10), log(n/m)>=log(.89/.26)>0 and
log(k/l)>=log(.79/.51)>0. All four indices are at most M.
Consequently c_nm c_kl>=c/M^2. The uniform second-derivative
majorant, even restricted to this box, has mass

    sqrt(T) sum_((n,m,k,l) in (10))c_nm c_kl
                  >=c sqrt(T) M^2 >=c' T^(3/2).           (12)

Its upper bound is C sqrt(T)S^2<=C' T^(3/2) by (6).
All coefficients are nonnegative; exact frequency grouping preserves
their total weight. In (4), every U C atom contributes to charge one
with coefficient c_nm c_kl, and its conjugate contributes to charge
minus one with the same coefficient. Other terms cannot subtract
these weights. Thus E_2 in (5) is at least twice C_2 times the
left side of (12). Combining (8) and (12),
E_2/(T D_2)>=c sqrt(T)/L^8 tends to infinity. This proves (9).

This does not bound |J| below, nor the absolute value or sign of
the sum of the stationary integrals. It shows that applying the
specified uniform bound separately and then adding loses all
constant-phase lower information, even before the linear-phase
errors are charged. Optimized estimates or cancellation between
terms are separate possibilities, not excluded by this calculation.

### 4. Interpolation, limitations and a precise remaining sum

Tao, *245C Notes 1: Interpolation of L^p spaces*, 30 March 2009,
Lemma 9, gives log-convexity on an arbitrary measure space
([primary statement and Holder proof](https://terrytao.wordpress.com/2009/03/30/245c-notes-1-interpolation-of-lp-spaces/)).
Use Lebesgue dt on [T,2T], p_0=1, p_1=4 and theta=2/3.
It gives ||R_T||_2<=||R_T||_1^(1/3)||R_T||_4^(2/3), hence

    integral |R_T| >= I_2^(3/2)/I_4^(1/2)     if I_4>0.

All norms are finite because R_T is a continuous finite sum.
If I_4=0, continuity gives R_T identically zero and both moments
vanish; division is not made. Equations (5), (7), (9) cannot
produce a positive certificate for this quotient in either case.
No upper bound on the actual quotient follows from their failure.

The surviving cross term admits an exact arithmetic grouping:

    integral_T^(2T) exp(2i theta(t))U(t)V(t)dt
       =sum_(m<=M;h<=M^3) g_(h,m) J(1,m/h),
    g_(h,m)=1/sqrt(hm)
       *sum_(nkl=h;n,k,l<=M)log(n/m)^2 log(k/l)^2.          (13)

This is just the substitution h=nkl, with no discarded terms.
The stationary region has h/m comparable to T/(2pi), including
(11). Estimating the *signed grouped sum* in (13), rather than
its coefficientwise second-derivative majorant, is a materially
refined target. No asymptotic transform, rational exponential-sum
bound or arithmetic cancellation theorem is imported or approved
here. Even its evaluation would leave the other terms of I_2,
the needed I_4 scale, L477's defect threshold, negative-mass saving,
initial signs at unbounded heights and all-degree positivity open.

## Mathlib

Full matching result: not checked. Supporting finite sums, harmonic
estimates, Holder interpolation and oscillatory-integral bounds:
no specific declarations checked. Unknown availability is not absence.
The imported mathematical inputs are exactly the two Tao statements
cited above and L477's residual/analytic phase hypotheses. The finite
expansions and positive-density budget were proved here because those
sources do not state an estimate for this complete chirped residual.
This is a failed specified certificate, not a reproof of a known
residual-moment theorem or a proof of impossibility of the target.
