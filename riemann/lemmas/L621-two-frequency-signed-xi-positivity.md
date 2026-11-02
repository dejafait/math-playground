# Lemma 621: eventual positivity of the two-frequency signed Xi form

## Hypotheses

Use the actual Xi of L018 and the zero-safe normalization of L471:

    A(t)=(t^2+1/4) pi^(-1/4)|Gamma(1/4+it/2)|/2,
    Z(t)=-Xi(t)/A(t),   W(t)=D_1(Xi;t)/A(t)^2.

Fix a nonnegative w in C_c^infinity((0,1)) with integral 1. Put
L=log T, w_XT(t)=w((t-X)/T), T<=X<=2T, and let T tend to
infinity. Let p be any prime in [T^(1/22),2T^(1/22)]. Set

    M(t)=a_1+a_p p^(-it),     |a_1|^2+|a_p|^2=1,
    U(t)=c0 Z(t)+c1 Z'(t)/L,  c0^2+c1^2=1.

The a coefficients are complex and the c coefficients real. They,
p and X may depend arbitrarily on T. Derivatives are ordinary real
derivatives. No RH, simplicity, spacing, nonvanishing or zero-free
half-plane hypothesis is imposed.

Import Hughes–Young, *The twisted fourth moment of the Riemann zeta
function*, J. reine angew. Math. 641 (2010), 203–236,
[arXiv:0709.2345v2, Theorem 1.1/(11)–(17) and the following
holomorphy remark, printed pp. 3–5](https://arxiv.org/pdf/0709.2345v2#page=3).
Its arithmetic proof and complete-sum holomorphy are named imports.
L619 supplies the untwisted, coefficient-uniform application, its
complex Hardy phase comparison and absolute shifted fourth bounds.
The present specialization and L619's used H=T application passed
the separate critical audit in Section 6 on 1 November 2026.
The underlying arithmetic manuscripts remain named imports and
have not been independently audited in this notebook.

## Conclusion

Uniformly in all the stated parameters,

    integral_R w_XT W |M|^2 U^2 dt
      = T L^6 [ (28 c0^2+c1^2)/(840 pi^2) + O_w(r(T,p)) ],       (1)

where

    r(T,p)=p^(-1/2)+1/L+T^(-35/176)/L^4+1/(T^2 L^2)=o(1).      (2)

In particular, beyond one existential onset depending on w only,

    integral_R w_XT W |M|^2 U^2 dt >= T L^6/(1680 pi^2)>0.       (3)

This is a bounded reproduction/specialization of known twisted
fourth-moment inputs, not a new arithmetic theorem. It stops the
specified growing-prime two-frequency negative-sign detector. It
does not determine the fine sign of its off-diagonal correlation,
prove pointwise first signs or negative-mass saving, exclude
exceptional heights, give higher signs, or resolve RH. No effective
onset or full amplified Gram factorization is asserted.

## Proof

### 1. Exact coefficient square and the required spectral margin

Define the real d and complex z by

    d=integral w_XT W U^2 dt,
    z=integral w_XT p^(-it) W U^2 dt.

Since W and U are real on the support, the integral with p^(it)
is conjugate(z). The coefficient identity is exactly

    integral w_XT W |M|^2 U^2 dt
      =d+2 Re(a_p conjugate(a_1) z).                            (4)

Both diagonal terms are untwisted, including the p,p term: its
ratio reduces to 1, with no residual 1/p coefficient. For each
fixed real c vector the entire amplifier matrix is

    [ d             z ]
    [ conjugate(z)  d ],

whose eigenvalues are d+|z| and d-|z|. We will bound its full
smaller eigenvalue uniformly in the c vector, not the sign of z.

Apply L619 with H=T, delta=1/26 and sigma=1/88; these satisfy
0<delta<1/13 and 0<sigma<min(1/4,13delta/4). With

    B(c)=(28 c0^2+c1^2)/(840 pi^2)>=1/(840 pi^2),
    e0=1/L+T^(-21/88)/L^4,

it gives, with the full Xi completion already included,

    d/(T L^6)=B(c)+O_w(e0+(1+e0)/(T^2 L^2)).                  (5)

The new task is an absolute bound for z, not a reproduction of
L619's finite untwisted coefficient calculation.

### 2. All six twisted main terms and source admissibility

Write q=(alpha,beta,gamma,delta), ell=log(t/(2pi)), and

    J(q)=zeta(1+alpha+gamma) zeta(1+alpha+delta)
         zeta(1+beta+gamma) zeta(1+beta+delta)
         /zeta(2+alpha+beta+gamma+delta),
    R_hk(q)=J(q) B_(alpha,beta,gamma,delta,h,k)(0).

Here B is exactly the finite Euler product in Hughes–Young (14),
not a limiting substitute. The complete sum from (17) is

    S_hk(t;q)= R_hk(alpha,beta,gamma,delta)
      + exp(-ell(alpha+beta+gamma+delta))
                           R_hk(-gamma,-delta,-alpha,-beta)
      + exp(-ell(alpha+gamma)) R_hk(-gamma,beta,-alpha,delta)
      + exp(-ell(alpha+delta)) R_hk(-delta,beta,gamma,-alpha)
      + exp(-ell(beta+gamma)) R_hk(alpha,-gamma,-beta,delta)
      + exp(-ell(beta+delta)) R_hk(alpha,-delta,gamma,-beta).      (6)

For coprime (h,k)=(p,1) or (1,p), the source formula for the
four-zeta integral is (1/sqrt(p)) integral w_XT S_hk plus its
raw error. We retain both orientations. Choose eta=1/88 and
T0=T in that theorem. Our support is contained in [T,3T], and
w_XT^(j)=O_(w,j)(T^(-j)); the smoothing condition follows from
1/2+1/88<1. Also, uniformly beyond one onset,

    hk=p<=2T^(1/22)<=T^(2/11-1/88),

because the exponent margin is
2/11-1/88-1/22=1/8>0. Shifts bounded by a fixed multiple of
1/L are admissible. Thus the raw error is bounded by

    E_p=C_w T^(3/4+1/88) p^(7/8)
        <=C'_w T^(3/4+1/88+7/176)
        =C'_w T^(141/176).                                  (7)

There is no extra p^(-1/2) on this error. We import the arithmetic
theorem rather than reprove its divisor estimates or use a
coefficient-growth corollary with coefficients sqrt(p)a_p.

### 3. Uniform prime factors and collision-safe complex bounds

For b=(b1,b2,b3,b4), use normalized shifts

    q(b)=(i b1,i b2,-i b3,-i b4)/L.

First work on |b1|=3, |b2|=4, |b3|=5, |b4|=6. Every polar
linear form in any J in (6) is, up to sign, i(bj-bk)/L, and
|bj-bk|>=1 there. Its magnitude is also O(1/L). The Laurent
expansion at the simple zeta pole therefore bounds each numerator
factor by O(L); the denominator near zeta(2) is bounded away from
zero. Hence every J is O(L^4). All exponentials in (6) are O(1)
uniformly for t in [T,3T].

We must check the B factors rather than silently absorb their p
dependence. For any transformed q in (6), all its coordinates have
modulus <=6/L. Beyond one onset log(p)/L<=1/10. From the source's
finite divisor sum (13),

    |sigma_(u,v)(p^j)| <= (j+1) exp(3j/5).

For (h,k)=(p,1), source (14) is the quotient

    N_p/D_p,
    N_p=sum_(j>=0) sigma_(alpha,beta)(p^j)
                     sigma_(gamma,delta)(p^(j+1)) p^(-j),
    D_p=sum_(j>=0) sigma_(alpha,beta)(p^j)
                     sigma_(gamma,delta)(p^j) p^(-j).          (8)

For (1,p), increment the first divisor function instead. These
series converge absolutely and locally uniformly in this whole
shift polydisc. Put v=exp(6/5)/p. For sufficiently large T, v<=1/20,
and the same bounds apply after every transformation in (6):

    |D_p-1| <= sum_(j>=1)(j+1)^2 v^j
             <= (1+1/20)/(1-1/20)^3-1
              =1541/6859 <1/2,
    |N_p| <= exp(3/5) sum_(j>=0)(j+1)(j+2) v^j
            <= 2 exp(3/5)/(1-1/20)^3 <32000/6859.

Here exp(3/5)<2. Thus D_p is nonzero throughout the polydisc,
all these B factors are analytic there, and |B|<32000/5318<8.
The identical estimate holds when the other divisor function is
incremented. In particular no term p^(-shift) has been replaced
by 1. Such terms can have nonvanishing normalized-shift dependence.

Together these facts bound each of the six terms on the separated
product of circles by C L^4. Import the complete-sum holomorphy
in the remark after source (17): its apparent shift poles cancel.
The local factors above create no extra poles. The complete sum,
not its individual summands, is holomorphic on a neighborhood of
the enclosed polydisc. Successive one-variable maximum principles
therefore give

    sup_(|bj|<=2) |S_hk(t;q(b))| <= C L^4.                    (9)

This step does not bound isolated singular summands at collisions.
Neither differentiation nor evaluation of such summands there is
used. The imported holomorphy is essential, not numerical evidence.

### 4. Hardy phase, absolute error, and fixed-jet extraction

Let F(t,b) be the product of the four zeta factors with shifts
q(b), and set

    H_hk(b)=integral w_XT(t)(h/k)^(-it)
                         product_(j=1)^4 Z(t+bj/L)dt/(T L^4).

Use the analytic Hardy phase comparison proved in L619 Section 3:
for |bj|<=2,

    product_j Z(t+bj/L)=Phi(t,b)F(t,b),
    Phi(t,b)=exp(i(b1+b2-b3-b4)/2)(1+O(1/L)),                 (10)

uniformly on the whole real support and these complex shifts.
The leading factor is independent of t and bounded on this
polydisc. By (7), (9) and integral w_XT=T, the integral with
that leading factor, divided by T L^4, is

    O_w(p^(-1/2)+T^(-35/176)/L^4).                           (11)

To pay the phase error, L619 Section 3, with H=T and sigma=1/88,
gives the local absolute shifted fourth bounds

    integral w_XT |zeta(1/2+it+u)|^4 dt
       =O_w(T L^4+T^(67/88)),   |u|<=2/L.

For a negative-height factor conjugate first. Holder with respect
to the nonnegative measure w_XT dt then gives

    integral w_XT |F(t,b)| dt=O_w(T L^4+T^(67/88)).

The twist has modulus 1 on the real integration variable. Thus
(10)'s integrated phase error is O_w(T L^3+T^(67/88)/L).
Combining this with (11) proves the holomorphic bound

    sup_(|bj|<=2) |H_hk(b)|
      <=C_w [p^(-1/2)+1/L+T^(-35/176)/L^4].                  (12)

The smaller term T^(-21/88)/L^5 is absorbed by 1/L. This bound
intentionally does not resolve a cross term's fine sign. It is
sufficient for comparison with the fixed diagonal spectral margin.

The compact support makes H_hk holomorphic by differentiation
under a finite integral, uniformly on compact shift sets. Set

    Q=partial_1 partial_2-(partial_1^2+partial_2^2)/2,
    V=(c0+c1 partial_3)(c0+c1 partial_4).

Exactly, with M and the twist independent of the b variables,

    Q V H_hk(0)
      =integral w_XT (h/k)^(-it)(Z'^2-ZZ'') U^2 dt/(T L^6).   (13)

Cauchy's formula on the four unit circles bounds the operation
QV by 3(|c0|+|c1|)^2 times the supremum in (12), hence by six
times that supremum. The factors 2! from partial_1^2 and
partial_2^2 cancel their 1/2 coefficients. This is fixed-order
complex Cauchy extraction; it never differentiates an error known
only on real shifts. In particular all differentiated prime-factor
dependence is covered by the complex bound, not discarded.

### 5. Actual Xi curvature and the complete spectral decision

Use the exact L471 identity, with a=log A,

    W=Z'^2-ZZ''-a'' Z^2,    |a''(t)|<=C T^(-2) on [T,3T].     (14)

L619 Section 5 gives, uniformly for c0^2+c1^2=1,

    integral w_XT Z^2 U^2 dt <= C_w T L^4.

This follows from its nonnegative Z^4 and Z^2(Z'/L)^2 integrals
and U^2<=2c0^2 Z^2+2c1^2(Z'/L)^2. Consequently each twisted
curvature cost is at most C_w T^(-1)L^4, or
C_w/(T^2 L^2) after division by T L^6. For the entire coefficient
square the same bound holds with twice the constant, since
|M(t)|^2<=(|a_1|+|a_p|)^2<=2. No sign of a'' is needed.

Equations (12)–(14) therefore prove

    |z|/(T L^6)<=C_w r(T,p).                                (15)

The p^(it) term is its actual conjugate; it has not been omitted.
Combining (5), (15), and T^(-21/88)<=T^(-35/176), the smaller
eigenvalue of the full two-by-two matrix obeys

    (d-|z|)/(T L^6) >= B(c)-C_w r(T,p).                     (16)

Also 2|a_1 a_p|<=1, so (4) gives the two-sided error (1).
The actual absolute costs on the signed scale are bounded by

    cross main:   C_w T L^6/sqrt(p),
    Hardy phase:  C_w T L^5,
    raw source after extraction: C_w T^(141/176)L^2,
    Xi curvature: C_w T^(-1)L^4.

Dividing these by T L^6 gives precisely the terms in (2).
Their required comparison is with the fixed lower margin
1/(840 pi^2), not a proposed decaying off-diagonal sign.
Since p>=T^(1/22), r<=T^(-1/44)+1/L+T^(-35/176)/L^4
+1/(T^2 L^2) tends to zero. Choose one T_w so that all earlier
uniform estimates hold and C_w r<=1/(1680 pi^2). Equation (16)
proves (3), for every admissible coefficient vector and X,p.
This is an existential, coefficient-uniform choice of onset.

All identities are zero-safe and remain valid at real Xi zeros
of any multiplicity. No logarithm of Z or Xi, assumed sign,
local zero statistic, contour interchange with an infinite moment
sum, or pointwise conclusion from a signed average is used. The
only infinite local series in the application have the explicit
geometric majorants in Section 3. L620 supplies the contextual
coefficient convention and a different, pure-height stop; its
concentration conclusion is not a mathematical input here.

### 6. Separate conceptual application audit — 1 November 2026

The bounded audit passes under the named imports. This certifies
only (1)–(3) in the stated family, replacing the provisional detector
stop by an audited one. No broader sign or arithmetic theorem is
claimed. The original proof and certificate remain preserved.

**Arithmetic scope and orientations.** Checked the cited v2 source
(11)–(17) and its holomorphy remark against (6)–(8), using the prior
Section 6.5 source comparison. Its h-side increment is on the second
divisor function; its k-side increment is on the first. Both match
(8). The source remainder is raw, without a square-root divisor.
At eta=1/88, T0=T, the support/derivative conditions hold; the length
margin is 1/8 and the error exponent is
3/4+1/88+7/176=141/176. The factor 2 in p's upper bound changes
only the constant and the existential onset. There is no use of
an amplified theorem with unverified coefficient-growth conditions.

**Complete complex domain.** On the separated circles, every normalized
polar linear form is a signed difference of two distinct r_j=i b_j,
with modulus at least 1; the corresponding zeta shift has modulus
at least 1/L. For each of the six permutations, every
shift has modulus at most 6/L throughout the enclosed polydisc.
The divisor bound follows term by term: p^(-u k-v(j-k)) has modulus
at most exp(3j/5) when log p/L<=1/10. Thus the normal convergence,
1541/6859 denominator perturbation, and 32000/6859 numerator bound
hold on the whole polydisc for either increment. In particular
|D_p|>=5318/6859 and |B|<32000/5318<8, independently of p.
These strict bounds also provide a neighborhood of each closed
polydisc where the factors are holomorphic. The zeta denominator
stays in a fixed zero-free neighborhood of 2 by continuity and
zeta(2)>0; this is not a zeta zero-free half-plane assumption.

The source's complete-sum pole cancellation is a separate essential
import. Local denominator nonvanishing alone would not prove it.
Together they make the full S_hk holomorphic inside the separated
contour. Four successive maximum principles extend its boundary
O(L^4) bound to the small polydisc. The same argument bounds the
untwisted six-term error used in L619; no single pole term is
evaluated at a collision. The constants in these arguments have no
coefficient dependence.

**Untwisted margin and phase transfer.** L619's separate used-scope
audit replays the exact six-term coefficients and gives B(c)>=
1/(840 pi^2), with E=T^(67/88). Its compatible gamma branches give
the complex phase comparison on the full support, not merely at
the center t=T. For every complex shift u in the required disk,
the positive fourth moment has source shifts
(u,u,conjugate(u),conjugate(u)); negative-height factors are handled
by conjugation. These are covered by the same holomorphic bound.
Holder therefore pays the phase replacement by an absolute
O(T L^3+E/L) before differentiation, even for a twisted integral.
After division by T L^4 the smaller E/(T L^5) is absorbed by 1/L.
The resulting H_hk is itself holomorphic, since the integration
support is compact and the shifted Hardy functions are holomorphic
on a common neighborhood. Hence the complex bound (12) legitimately
feeds Cauchy's formula. Its Q cost is 1+1+1=3, and its V cost is
(|c0|+|c1|)^2<=2. No prime-factor derivative or error derivative is
discarded, and M is never differentiated.

**Completion and spectral comparison.** Directly differentiating
Xi=-AZ gives (14), without dividing by Xi. The paired reciprocal
gamma arguments sum to 1/(t^2+1/4), which is why the curvature is
O(T^-2), rather than a bound obtained by adding two O(T^-1)
terms. The nonnegative moments in L619 control Z^2 U^2 by O(T L^4);
the modulus-one twist and |M|^2<=2 retain this control. The resulting
curvature error on the normalized signed scale is 1/(T^2 L^2).

Finally the p,p term in (4) is exactly d. With vector (a_1,a_p),
the displayed Hermitian matrix gives the cross coefficient
2 Re(conjugate(a_1) a_p z) and eigenvalues d+|z|, d-|z|. Normalizing
the source error after QV gives T^(-35/176)/L^4. The untwisted
T^(-21/88)/L^4 is smaller, since 21/88=42/176>35/176;
its extra curvature product is absorbed once e0 is bounded.
Thus the actual total error is the stated C_w r(T,p)=o(1),
uniformly even when all permitted parameters depend on T. Taking
it below half the fixed margin proves (3). This comparison requires
no fine cross sign, simplicity, effective onset, or sign at an
individual height. None of those independent gaps is resolved.

## Mathlib

Full matching coverage of Hughes–Young's shifted twisted moment,
its complete-sum holomorphy and this completed-Xi spectral
specialization was not checked and is unknown. The elementary
finite coefficient and Cauchy arguments here are informal proofs,
not Lean verification. No claim of absence from Mathlib is made.
