# Lemma 695: a fixed summable tail can have exponential absolute angular cost

## Hypotheses

Use L666's family with q>=1, n=12q+3, M=n/3, h=27/(10n),
x=-d=-5/4, R=11/8, U=121/64, and t_j=j/n for 0<=j<n.
For a fixed real sequence e in l1(Z) with sup_m |e_m|<=1/8, use
only -2q<=m<2q and retain the fixed anchor and unit original masses:

    a_m(e)=x+i*h*(m+1/2+e_m),
    B_u(v)=product_(0<=j<n) R*(v-t_j*u)/(U-t_j*v/u),
    W_a(u)=B_u(x)/B_u(a),
    T_M(v)=sum_(0<=k<M) v^k,
    G_(n,e)(u,zeta)=R^(-1)*sum_(a in Z_e) W_a(u)*T_M(a*zeta/R),
    A_n(e)=mean_(T x T) log|G_(n,e)|.

For an integer H>=0 set e_m^(H)=e_m for |m|<=H and zero otherwise.
For each available index define the full spatial-polynomial difference

    Delta_(m,n)(u,zeta)=R^(-1)*[
      W_(a_m(e))(u)*T_M(a_m(e)*zeta/R)
        -W_(a_m(0))(u)*T_M(a_m(0)*zeta/R)],
    C_(n,H)=sum_(available |m|>H) sup_(|u|=|zeta|=1)
                                      |Delta_(m,n)(u,zeta)|.

This is a specified absolute termwise cost. The exact signed difference
is G_(n,e)-G_(n,e^(H))=sum_(available |m|>H) Delta_(m,n), whose
supremum norm is at most C_(n,H), not necessarily equal to it. All
M moments, j=0 and the denominator angle 1/u remain present.

## Conclusion

For every fixed H and every allowed e,

    [A_n(e^(H))-A_n(0)]/n -> 0.                         (1)

In particular the proposed ordered tail test is sufficient for, and
in fact equivalent to, the desired fixed-profile lower-liminf bound:

    lim_(H->infinity) limsup_(q->infinity)
      [A_n(e^(H))-A_n(e)]_+/n=0
      iff liminf_(q->infinity) [A_n(e)-A_n(0)]/n>=0.    (2)

It is not an independently established small-tail estimate.

There is an explicit fixed admissible summable profile

    e_m=1/[16*(m+1)^2] for m>=0, and e_m=0 for m<0,    (3)

with sup |e_m|=1/16 and sum |e_m|<=1/8. Its tail mass satisfies
sum_(|m|>H)|e_m|<=1/[16*(H+1)], but for each H and all admissible
n>=max(20000,10000*(H+2)),

    C_(n,H) >= exp(n/10000000)/(8800*n^2).              (4)

Thus even this fixed l1 profile admits no termwise absolute tail
bound uniform in n that tends to zero with its l1 tail, and no
subexponential upper bound for this particular absolute cost.
This rules out a direct dominated-tail/absolute-error closure of the
approved test. It does not lower-bound the signed difference, estimate
its negative logarithmic part, or refute (2). No linear loss in A_n,
fixed-profile countersequence to its target, full-cube estimate,
H/support transfer, Xi realization or RH conclusion is obtained.

This is an elementary family-specific specialization of existing
product and sparse-head estimates. It supplies local method-stop
evidence, not a claimed new general theorem or certified originality.
The result has not received a separate critical audit.

## Proof

### Scope and existing inputs

The invocation-start EXPLORE assessment is
`drafts/literature/2026-11-03-summable-displacement-complete-log-transfer.md`.
The attempt uses its approved fixed-profile analytic head-tail test.
L692's audited sharper inequality, rather than its coarse n/100
corollary, pays the head. L690 gives the audited baseline. L657
supplies absolute logarithmic integrability, including torus zeros,
and the exact complete identity A_n=m_0+Z_n-P_n for every profile here.

The head bound imports the polynomial root/coefficient theorem already
specialized in L692: F. Brunault and W. Zudilin, *Many Variations of
Mahler Measures*, ISBN 9781108794459,
[Propositions 1.4--1.5, pp.6--7, and Lemma 1.6, p.8](https://assets.cambridge.org/97811087/94459/excerpt/9781108794459_excerpt.pdf).
It is not reproved. Product differentiation and finite Fourier
coefficient extraction below are elementary identities; no general
Mahler-continuity or uniform small-value result is added.

L665's earlier one-node error and outward-pair contour cost are
comparisons, not premises: they do not establish (4) for one fixed
summable profile on the original angular circle. Step 105's finite
optimized vectors depend on n and give no such rigorous conclusion.
L694 motivates studying summable profiles but is not used in this
proof; (3) is not asserted to have a Fourier gap.

### 1. Paying a fixed head and retaining the order of limits

Fix H and set K=H+1. There are at most 2H+1<=2K changed indices in
e^(H). For all sufficiently large q, n>=10^6 and K<=n/40000.
L692 (2), integrated using L657, and L690 (2) therefore give

    A_n(e^(H))-A_n(0)
      >= -log 2-4K*log(5*n^2/(2*K^2))-epsilon_n,
    epsilon_n=64*n^2*exp(22-n/500) -> 0.                (5)

This proves the required lower o(n) loss for a fixed head. There is
also an upper bound independent of n at fixed H, as follows.

Along the vertical segment from x to any allowed a, the original
product has no zero or pole. Its logarithmic derivative in a is

    (partial_a W_a)/W_a
       =-sum_(0<=j<n)[1/(a-t_j*u)+t_j/(U*u-t_j*a)].     (6)

For |u|=1 the two clearances are at least d-1=1/4 and
U-r_*=841/1600>1/2, where r_*=273/200. L666's ordinate bound
|Im a|<9/20 holds on the whole segment. Thus (6) has modulus at
most 6n, and integration from W_x=1 yields

    |W_(x+i*h*v)(u)|<=exp((81/5)*|v|).                 (7)

For an index |m|<=H, both its old and new v have modulus at most
H+5/8. Put rho=r_*/R=273/275. On the spatial circle,
|T_M(a*zeta/R)|<=1/(1-rho) and R^(-1)/(1-rho)=100.
Also L690 (1) implies sup|G_(n,0)|<=9 for n>=30000, because
R^(-1)/(1-d/R)=8 and its error is less than one. Hence

    sup_(T x T)|G_(n,e^(H))|
      <= C_H:=9+200*(2H+1)*exp((81/5)*(H+5/8)).         (8)

In particular A_n(e^(H))<=log C_H. Combining (5), (8) and
A_n(0)=-log R+o(1) proves (1). No lower pointwise bound on G
or exclusion of its circle zeros has been used.

For the limit assertion put b_q=[A_n(e)-A_n(0)]/n and
a_(q,H)=[A_n(e^(H))-A_n(0)]/n. By (1), a_(q,H)->0 for each
fixed H. Since the positive-part map is 1-Lipschitz,

    |[a_(q,H)-b_q]_+-[-b_q]_+|<=|a_(q,H)| -> 0.

Consequently the inner limsup in (2), at every fixed H, is exactly
[-liminf_q b_q]_+ (with the usual extended-real convention). It is
independent of H. This proves (2), without interchanging the q and H
limits or inferring any estimate from summability alone.

### 2. A positive ordinate derivative at the actual angle u=i

For real 0<=y<=1/1000, take a=x+i*y and u=i. Directly from all
the original product factors, including t_0=0,

    log|W_(x+i*y)(i)|
      = (1/2)*sum_j log[(d^2+t_j^2)/(d^2+(y-t_j)^2)]
        +(1/2)*sum_j log[(d^2*t_j^2+(U-t_j*y)^2)
                                      /(d^2*t_j^2+U^2)].

Every denominator is strictly positive. The y derivative is

    sum_j g_(t_j)(y),
    g_t(y)=(t-y)/(d^2+(t-y)^2)
                  -t*(U-t*y)/(d^2*t^2+(U-t*y)^2).      (9)

At y=0 an exact simplification gives

    g_t(0)=t*(U-d^2)*(U-t^2)
                       /[(d^2+t^2)*(d^2*t^2+U^2)]>=0.

For 1/2<=t<=1 this is at least

    (1/2)*(21/64)*(57/64)
            /[(41/16)*(21041/4096)]
      =9576/862681 > 1/100.                            (10)

At least n/4 of the indices 0<=j<n satisfy t_j>=1/2 for n>=2.
Thus sum_j g_(t_j)(0)>=n/400. On the entire y interval in question,
differentiate the two terms of g_t. The elementary inequality
|b^2-a^2|/(a^2+b^2)^2<=1/(a^2+b^2) gives

    |g_t'(y)|<=1/d^2+1/(U-y)^2
                <16/25+9/25=1,                       (11)

because U-1/1000>5/3. Equations (9)--(11) imply

    d_y log|W_(x+i*y)(i)|
      >= n/400-n*y >= 3*n/2000 >= n/1000.              (12)

Since W_x=1, integration also gives
log|W_(x+i*y)(i)|>=n*y/1000. These are real logarithms of nonzero
finite products, not logarithms of the possibly vanishing signed sum.

### 3. A fixed l1 profile with an exponentially costly tail

Choose (3). The integral comparison for sum_(k>=1) k^(-2) gives
sum_m |e_m|<= (1+integral_1^infinity t^(-2)dt)/16=1/8;
the same comparison starting at H+1 gives the stated tail bound.
The cap and L666 admissibility hold for every truncation, without
reflection symmetry or any change of masses.

For n>=20000 set m_n=floor(n/10000). This is an available positive
index, with m_n>=n/20000 and m_n+1<=n. It exceeds H whenever
n>=10000*(H+2). Write

    y_0=h*(m_n+1/2),   y_1=y_0+h*e_(m_n).

Both lie in [0,1/1000]: indeed y_1<=h*(m_n+1)
<=27/100000+27/(10n)<=81/200000<1/1000. Also
y_0>=27/200000. From (12),

    |W_(x+i*y_0)(i)|>=exp(27*n/200000000)
                                  >=exp(n/10000000),
    log[|W_(x+i*y_1)(i)|/|W_(x+i*y_0)(i)|]
      >=n*h*e_(m_n)/1000
       =27*e_(m_n)/10000 >=e_(m_n)/400.

The reverse triangle inequality and exp(s)-1>=s for s>=0 now give

    |W_(x+i*y_1)(i)-W_(x+i*y_0)(i)|
      >=exp(n/10000000)*e_(m_n)/400
      >=exp(n/10000000)/(6400*n^2).                    (13)

This is a lower bound on one actual weight difference, not on a sum
after an absolute-value upper estimate. The constant coefficient of
the complete polynomial Delta_(m_n,n)(i,zeta) equals R^(-1) times
this weight difference. A polynomial's constant coefficient is its
normalized spatial-circle integral, so its modulus is at most the
supremum modulus of that polynomial. Therefore (13), with
6400*R=8800, implies (4). No high spatial coefficient was dropped
from G or from the polynomial used in this inference.

### 4. What this does and does not stop

For every fixed H, (4) implies
liminf_(q->infinity) n^(-1)*log C_(n,H)>=1/10000000,
although the displacement tail tends to zero as H grows. This is
decisive against bounding the tail by that absolute cost and then
passing to a uniform small perturbation of the finite head (8).

It is not decisive against a signed analytic or complete-logarithm
estimate. Large individual contributions may cancel; large values
may also increase the mean instead of decreasing it. No bound for
[A_n(e^(H))-A_n(e)]_+ follows from (4). L657's complete identity
continues to apply, with all numerator zeros, denominator poles,+multiplicities and exceptional slices retained. The sought signed
negative-logarithm estimate and any actual linear-loss subsequence
remain unresolved. No numerical computation is a premise here.

## Mathlib

Full matching coverage of this fixed-profile obstruction is not
checked. Reuse only the supporting root-formula coverage recorded
in L657 and L692:
[Mathlib.Analysis.Polynomial.MahlerMeasure](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Polynomial/MahlerMeasure.html),
including `Polynomial.logMahlerMeasure_eq_log_leadingCoeff_add_sum_log_roots`,
`Polynomial.intervalIntegrable_mahlerMeasure`, and
`Polynomial.mahlerMeasure_mul`. These do not establish the present
product derivative, fixed-profile constants or signed tail target.
No absence claim or formal verification is made.
