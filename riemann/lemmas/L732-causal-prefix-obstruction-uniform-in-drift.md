# Lemma 732: causal prefix obstruction uniform in complex drift

## Hypotheses

Let zeta be the Riemann zeta function, mu the ordinary Möbius function,
Lambda the von Mangoldt function with Lambda(1)=0, and
psi(x)=sum_(n<=x) Lambda(n) for real x>=1. Fix one nontrivial zero
rho=beta+i gamma with 1/2<=beta<1, of its actual finite multiplicity m>=1.
All constants and onsets below may depend on this fixed zero, including m.

Use L729's definitions

    H=L²((1,infinity),dx/x²),
    rho_k(x)=floor(x/k)-floor(x)/k,
    ell=log N,
    g_N=sum_(k<=N)mu(k)(1-log k/ell)rho_k,

for integers N>=2; rho_1=0. No neutrality condition on a probe from
L729 is needed here. Define

    J_N(a)=sum_(j=1)^N |a j-psi(j)|²/[j(j+1)],   a in C,
    Q_N^head=integral_1^(N+1) |1-g_N(x)|² dx/x²,
    R_N=ceil(N log N),
    Q_N=integral_1^(R_N+1) |1-g_N(x)|² dx/x².

No RH, simplicity, zero-free half-plane improvement, reciprocal-derivative
moment, subpower upper estimate, or assumption on an N-dependent drift
is made.

## Conclusion

There are c_rho>0 and an integer N_rho>=2 such that, for every integer
N>=N_rho,

    inf_(a in C) J_N(a) >= c_rho N^(2 beta-1),             (1)
    Q_N >= Q_N^head >= c_rho N^(2 beta-1)/(log N)².        (2)

This is a canonical import of bramble_trace, *A logarithmic-prefix
Nyman–Beurling criterion and transferred zero bounds*, rStation paper
47/v1, 24 October 2026, Section 7, Proposition 4, equations (37)--(48)
and the final divisor identity:
https://rstation.ai/problems/riemann_hypothesis/papers/47/v1 .
The primary v1 statement and complete proof were inspected on 2026-11-03.
The replay below audits this manuscript's contour, causal support,
multiplicity and drift-uniformity claims; it is not a new oscillation
theorem. Pintz, arXiv:2608.24878v2, Theorem 6.1, is the source's
methodological antecedent, not a directly applicable theorem here.
Neither its Gaussian filter nor paper 47's other theorems are inputs.

## Proof

### Elementary analytic bounds used in the contour audit

We use the standard meromorphic continuation of zeta, its sole simple
pole at 1, its Euler product on Re w>1, Chebyshev's theorem
psi(x)<=C_0 x (x>=1), Cauchy's residue theorem, Fubini and
Cauchy--Schwarz. Chebyshev's constant is enlarged if necessary to
hold on the whole indicated interval. No bound for 1/zeta in the
critical strip is used.

To make the source's polynomial-growth input explicit, the elementary
Euler summation identity is

    zeta(w)=w/(w-1)-w I(w),
    I(w)=integral_1^infinity {x} x^(-w-1) dx,    Re w>0, w!=1.  (3)

For Re w>1 it follows from
integral_1^infinity floor(x)x^(-w-1)dx=zeta(w)/w
and floor(x)=x-{x}; absolute convergence of I then continues the
identity to Re w>0. Differentiation under that integral is justified
uniformly on compact subsets of Re w>0 by x^(-1-delta)(1+log x).
For sigma=Re w>0,

    |I(w)|<=1/sigma,
    |I'(w)|<=1/sigma²,
    zeta'(w)=-1/(w-1)²-I(w)-w I'(w).

Consequently, on every fixed strip delta<=Re w<=B with delta>0,
both zeta(w) and zeta'(w) are O_(delta,B)(1+|Im w|) as
|Im w| tends to infinity. This deliberately coarse bound suffices
for every finite rectangle below. This verification specifies the
decay needed for the manuscript audit, rather than asserting that
an unspecified polynomial bound is dominated by a fixed denominator.

### Holomorphy, boundedness and exact causal support

Put kappa=beta-1/4, so 1/4<=kappa<3/4, and, for the contour
variable s, put z=s+rho-kappa=s+1/4+i gamma. Use exactly the
source's filter

    G(s)=(z-1)² zeta(z)/[(s-kappa)^m(s+1)^8].             (4)

At z=1 the numerator removes the zeta pole. At s=kappa the
order-m zero of zeta removes (s-kappa)^m. These are distinct
points because rho!=1. The remaining possible pole s=-1 is
outside Re s>-1. Thus G, with removable values assigned, is
holomorphic on Re s>-1.

On any fixed vertical strip 0<=Re s<=A, where A>=3,
(3) gives, as |Im s| tends to infinity,

    G(s)=O_(rho,A)(|Im s|^(-m-5)).                        (5)

Indeed the numerator is O(|Im s|³), while the denominator has
order m+8; the shift by the fixed gamma does not change these
orders. This estimate is only used above a height depending on
rho,A. On each remaining compact segment holomorphy supplies
boundedness. It follows in particular that the following integral
converges absolutely for each real h:

    r(h)=(1/(2 pi i)) integral_(Re s=3) exp(hs) G(s) ds.   (6)

For fixed h, shift from Re s=3 to Re s=0 along rectangles.
There are no poles; (5) makes both horizontal integrals tend to
zero, since exp(h Re s) is bounded on this fixed strip. Therefore

    r(h)=(1/(2 pi)) integral_R exp(iht)G(it)dt,
    |r(h)|<=M_rho,
    M_rho=max{1,(1/(2 pi))integral_R |G(it)|dt}<infinity.  (7)

This bound is uniform in all real h. The integral also makes r
continuous by dominated convergence.

For causal support, fix A>=A_0(rho)>3 large enough that on Re s=A,
|z-1|<=C_rho |s| and |s-kappa|>=|s|/2. The absolute Dirichlet
series bounds |zeta(z)| by zeta(Re z)<=zeta(2), independently
of A and Im s; also |s+1|>=|s|. Hence

    |G(A+it)|<=C_rho |A+it|^(-m-6),
    integral_R |G(A+it)|dt<=C'_rho A^(-m-5).              (8)

For each fixed A the shift from 3 to A is justified by (5).
Thus |r(h)|<=C''_rho exp(Ah)A^(-m-5). Now let A tend to
infinity. For h<=0 this tends to zero, including h=0. We have
proved r(h)=0 for h<=0 with no omitted physical tail. Horizontal
limits were taken at each fixed A first; no uniform rectangular
limit in A was presumed.

### All complex anchors and absolute Mellin interchange

If |a|>=C_0+1, the reverse triangle inequality gives

    |a j-psi(j)|>=j,
    J_N(a)>=sum_(j<=N) j/(j+1)>=N/2.                     (9)

Since 0<=2beta-1<1, this already implies (1) with constant 1/2.
It remains to treat |a|<=C_0+1, uniformly in that closed complex
disk. Set h_a(x)=a floor(x)-psi(x). Then
|h_a(x)|<=(2C_0+1)x uniformly there.

For Re z>1, termwise integration of the absolutely convergent
floor and von Mangoldt sums, followed by the logarithmic derivative
of the absolutely convergent Euler product, gives

    integral_1^infinity h_a(x)x^(-z-1)dx
      =a zeta(z)/z+zeta'(z)/[z zeta(z)].                 (10)

In particular the plus sign on the logarithmic derivative arises
because the Mellin transform of psi is -zeta'/(z zeta).

Let Y=N+1. By (7) the finite integral

    V_a(Y)=integral_1^Y h_a(x)x^(-1-rho+kappa)
                             r(log(Y/x))dx             (11)

exists. Its value is unchanged when the upper limit is infinity,
by the causal support just proved. Substitute (6) on Re s=3.
The absolute double integral is bounded by a constant times

    Y³ integral_R |G(3+it)|dt
       * integral_1^infinity x^(-13/4)dx <infinity,      (12)

uniformly over these anchors for each fixed Y. Here h_a=O(x)
and beta-kappa=1/4 have both been included. Thus Fubini and
(10), with Re z=13/4, give

    V_a(Y)=(1/(2 pi i)) integral_(Re s=3) Y^s F_a(s)ds,
    F_a(s)=(z-1)²[a zeta(z)²+zeta'(z)]
              /[z(s-kappa)^m(s+1)^8].                  (13)

### Pole inventory, arbitrary multiplicity and uniform remainder

Move the contour in (13) to Re s=-1/8. Throughout the closed
strip -1/8<=Re s<=3 the real part of z is at least 1/8.
At z=1 both zeta² and zeta' have at most double poles, removed
by (z-1)². The possible z=0 pole is on Re s=-1/4 and is not
crossed; s=-1 is likewise outside. Other zeros of zeta do not
introduce poles, since there is no reciprocal zeta left in (13).

At s=kappa write u=s-kappa=z-rho and
zeta(rho+u)=c_m u^m+O(u^(m+1)), where
c_m=zeta^(m)(rho)/m! is nonzero. Then

    a zeta(rho+u)²/u^m = O_a(u^m),
    zeta'(rho+u)/u^m = m c_m/u+O(1).

Thus the anchor term is regular, and the other term has exactly
one simple pole for every actual m>=1. Its residue in F_a is

    B_rho=(rho-1)² zeta^(m)(rho)
             /[rho (m-1)! (kappa+1)^8] !=0.             (14)

It is independent of a. All factors are nonzero: rho is neither
0 nor 1, kappa+1>0, and m is the actual order of the zero.

By (3), uniformly in |a|<=C_0+1 and in the indicated fixed strip,
the numerator of F_a is O_rho(|Im s|^4) at large height, and
the denominator has order m+9. Consequently

    F_a(s)=O_rho(|Im s|^(-m-5)).                         (15)

The line Re s=-1/8 has none of the enumerated poles. Compact
segments there are uniformly bounded in a, because F_a is affine
in a and the anchor disk is bounded. It follows that

    D_rho:=sup_(|a|<=C_0+1)
        (1/(2 pi))integral_R |F_a(-1/8+it)|dt <infinity.

For fixed Y, (15) also makes the horizontal integrals vanish.
The residue theorem therefore yields the full, uniform identity

    V_a(Y)=B_rho Y^kappa+E_a(Y),
    |E_a(Y)|<=D_rho Y^(-1/8).                            (16)

Choose an onset independent of a so that
D_rho Y^(-1/8)<=|B_rho|Y^kappa/2. Such an onset exists since
kappa+1/8>0. Then |V_a(Y)|>=|B_rho|Y^kappa/2 uniformly over
the disk. No growing-zero uniformity or assumption on the phase
of B_rho is used.

### The weighted estimate and exact prefix transfer

On [j,j+1), h_a(x)=a j-psi(j). Endpoints have zero measure,
so exactly

    integral_1^Y |h_a(x)|² dx/x²=J_N(a),   Y=N+1.        (17)

Apply Cauchy--Schwarz to (11) with factors h_a(x)/x and
x^(-rho+kappa)r(log(Y/x)). By (7), the squared norm of the
second factor is

    integral_1^Y x^(-2beta+2kappa)|r(log(Y/x))|²dx
      <=M_rho² integral_1^Y x^(-1/2)dx
      <=2M_rho² Y^(1/2).                                (18)

Combining (16)--(18) gives, beyond the common onset,

    J_N(a)>=|B_rho|²/(8M_rho²) Y^(2kappa-1/2)
           >=|B_rho|²/(8M_rho²) N^(2beta-1).             (19)

The last comparison uses beta>=1/2. Taking
c_rho=min{1/2,|B_rho|²/(8M_rho²)}>0 combines (9) and (19).
This proves (1) uniformly over all complex a, hence also for
any sequence a=a_N and for the infimum.

Finally put

    alpha_N=sum_(k<=N)mu(k)(1-log k/ell)/k.

The k=1 term is included even though rho_1=0; the k=N
coefficient vanishes. For every integer 1<=j<=N, use the two
finite divisor identities proved in L729,
sum_(k|q)mu(k)=1_(q=1) and
sum_(k|q)mu(k)log k=-Lambda(q), to compute

    sum_(k<=N)mu(k)(ell-log k)floor(j/k)
      =sum_(q<=j)sum_(k|q)mu(k)(ell-log k)
      =ell+psi(j).

Terms k>j were zero before regrouping, so there is no omitted
range. It follows that

    ell g_N(j)=ell+psi(j)-ell alpha_N j,
    ell(1-g_N(j))=(ell alpha_N)j-psi(j),   1<=j<=N.      (20)

This includes j=1 and j=N. Since g_N is constant on these
cells, (17) and (20) give
Q_N^head=J_N(ell alpha_N)/ell². No bound on alpha_N is required.
For N=2, R_N=2, and for integers N>=3, log N>1; thus always
R_N>=N. Nonnegativity of the integrand gives Q_N>=Q_N^head,
proving (2). This also fixes the retained endpoint as [1,N+1),
not [1,N].

The audit validates only this cited necessary condition. At beta=1/2
its conclusion is a constant lower bound for J_N and a log^(-2)
lower bound for the prescribed squared norm, compatible with decay.
For a hypothetical beta>1/2 it forces polynomial growth; it produces
no such zero. It supplies no upper bound, no full-norm decay, no
optimal-coefficient obstruction on the first N cells, and no Xi sign
or RH conclusion. L730/L731 and any saturation or residual-control
assumption were not used. Corollary 5 of the source is not imported.

## Mathlib

Full matching theorem: not checked; availability is unknown. Euler
summation, analytic continuation, the Euler-product logarithmic
derivative, Chebyshev's bound, residue calculus, Fubini and
Cauchy--Schwarz are supporting mathematical inputs. No exact
Mathlib declarations or matching formalized causal-prefix theorem
have been verified in this audit, and no absence claim is made.
