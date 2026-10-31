# L526 — Common-pole-phase Sonin prime increment

## Hypotheses

Use logarithmic physical coordinates, Fourier transform
`F(t)=integral f(x) exp(-itx) dx`, boundary measure `dm=dt/(2pi)`,
and translation `V_L f(x)=f(x-L)`. Let h be the real bump
`C exp(-1/(1-x^2))` on |x|<1, zero elsewhere, with ||h||_2=1.
Let p tend to infinity through primes and set

    L=log p, r=p^(-1/2), A=sqrt(p)/L, M=L+2,
    f_p(x)=h(x+L/2)+h(x-L/2),
    P_-={q prime:q<p}, P_+={q prime:q<=p}.

The two prime sets use the SAME phase and the scattering convention

    u_inf(t)=pi^(-it) Gamma(1/4+it/2)/Gamma(1/4-it/2),
    u_q(t)=(1-q^(-1/2+it))/(1-q^(-1/2-it)),
    chi_M(t)=4 integral_0^M cosh(v/2) sin(tv)/v dv,
    u_(P,M)(t)=u_inf(t) product_(q in P) u_q(t) exp(i chi_M(t)).

If H_- and H_+ denote the lower and upper half-plane Hardy H^2
boundary spaces, respectively, define the closed subspace

    K_(P,M)={g in H_- : u_(P,M) g in H_+}.

Write S_(P,M) for its orthogonal projection in L^2(dm). This is
the physical Sonin projection after Fourier transformation: the
involution acts by g(t) -> u_(P,M)(-t) g(-t), so reflection turns
its positive-physical-half-line condition into the second Hardy
condition above. The Fourier transform of a function supported in
the positive physical half-line belongs to H_-.

The following cited inputs are used in their stated scopes:

* bramble_trace, *Sharp Schatten asymptotics and Sonin trace
  localization for semilocal Fourier cutoffs*, paper 2, v2,
  16 October 2026, [primary manuscript](https://rstation.ai/problems/riemann_hypothesis/papers/2):
  Section 1 and (5.2) for conventions; Lemma 6.1 and the first
  paragraph of Theorem 6.5's proof for the absolute prime-sum
  error O(A/L); (6.21)--(6.24) for uniform commutators of arbitrary
  Toeplitz-kernel projections. These source proofs have not been
  independently audited here.
* Rajesh K. Srivastava, [MA650 Advanced Hardy Spaces notes](https://fac.iitg.ac.in/rksri/MA650%20Advanced%20Hardy%20Spaces%20Notes%202022.pdf),
  revision 2 May 2026: Lemma 8.6(ii), pp.119--120 (evaluation),
  Theorem 8.8, p.122 (half-plane H^2 Paley--Wiener), and
  Theorem 8.18(i), pp.129--130 (Cauchy representation). Use p=2;
  reflecting its upper-half-plane convention gives the lower
  convention here. Replacing dt by dm changes only fixed constants.
* Gamma reflection [DLMF 5.5.3](https://dlmf.nist.gov/5.5.E3) and
  Stirling [DLMF 5.11.3](https://dlmf.nist.gov/5.11.E3), uniformly
  in closed sectors away from the negative real axis; the
  vertical-line specialization is [5.11.9](https://dlmf.nist.gov/5.11.E9).
* Jordan Bell, [Trace class operators and Hilbert--Schmidt operators](https://jordanbell.info/LaTeX/mathematics/traceclass/),
  18 April 2016, Theorems 18 and 23: products of two
  Hilbert--Schmidt factors are trace class; a trace-class factor
  and a bounded factor permit cyclicity and the ideal norm bound.

No RH, zero-free fixed half-plane, nullvector, or full-Weil identity
for these partial prime sets is assumed. The local application below
passed a separate conceptual audit on 30 October 2026. This validates
its specialization of the cited inputs, not the upstream manuscripts.
The audit reproduced the existing argument; it established no new
mechanism or originality claim.

## Conclusion

Both separate quantities

    T_(P,M)(f_p)=||M_(F_p) S_(P,M)||_HS^2

are finite for every p. As p tends through primes,

    Delta_p=T_(P_+,M)(f_p)-T_(P_-,M)(f_p)
           =O_h(r L^(9/10))=o(rL).                         (1)

For L>2, the added prime contributes exactly -2rL to the signed
archimedean-plus-prime form with the common pole term included.
Consequently the increment of T minus that partial signed form is
`2rL+O_h(r L^(9/10))`. Thus this prescribed Sonin-only increment
does not absorb that leading arithmetic term. This is neither a
sign for a complete Weil form nor a result for an actual nullvector.

## Proof

### 1. A fixed rational background for the changing pole phase

For Im z<=0 put

    d_M(z)=exp(2 integral_0^M cosh(v/2)(exp(-izv)-1)/v dv),
    e_M(z)=(1+iz)^2 d_M(z),
    k_M(v)=cosh(v/2)1_(0,M)(v)-exp(-v).

The first integral is convergent at zero and analytic. The elementary
Laplace identity obtained by integrating the derivative in z is

    integral_0^infinity exp(-v)(exp(-izv)-1)/v dv
        =-log(1+iz).

The logarithm is the analytic branch with value zero at z=0.
Therefore

    log e_M(z)=2 integral_0^infinity
                    k_M(v)(exp(-izv)-1)/v dv.             (2)

Here k_M(v)/v is absolutely integrable: it tends to 1 at zero,
and equals -exp(-v)/v beyond M. Since |exp(-izv)|<=1 in the lower
half-plane, both e_M and its inverse are bounded analytic there,
with bounds at most exp(4 J_M), where

    J_M=integral_0^infinity |k_M(v)|/v dv
        =O(exp(M/2)/M)  (M>=3).                           (3)

For example, split the integral at 1 and M/2; on the last segment
use 1/v<=2/M, and the earlier exponential integral is smaller.
This also proves continuity of their boundary values. The factor
d_M itself need not have a bounded inverse; it is e_M that will
be used for the invertible change of space.

Let b(z)=(z+i)/(z-i), which is inner in the lower half-plane, and
put u_*=u_inf b^(-2). On the real line,

    d_M(-t)/d_M(t)=exp(i chi_M(t)),
    exp(i chi_M(t))=b(t)^(-2) e_M(-t)/e_M(t).

For D_P(t)=product_(q in P)(1-q^(-1/2-it)) and
Phi_(P,M)=D_P e_M, this gives

    u_(P,M)=u_* Phi_(P,M)(-t)/Phi_(P,M)(t).              (4)

Each Phi and its inverse is a bounded lower-Hardy multiplier for
fixed P,M. Their reflected counterparts are bounded upper-Hardy
multipliers. Thus the TWO inclusions in the range identity follow
by multiplication and division in the two Hardy conditions:

    K_(P,M)=Phi_(P,M) K_*,
    K_*={v in H_- : u_* v in H_+}.                       (5)

This is a closed range, not a unitary identification. In particular
no inverse Gram operator can be omitted. The fixed rational factor
in u_* is essential; applying the Euler range argument directly
to d_M would not prove (5).

Explicitly, v in K_* gives Phi v in H_- and
u_(P,M)Phi v=Phi(-t)u_*v in H_+. Conversely, g in K_(P,M)
gives v=g/Phi in H_- and
u_*v=(u_(P,M)g)/Phi(-t) in H_+. All four multipliers used
here are bounded analytic in the appropriate half-plane. Also
K_* is closed as the kernel of the bounded compression
Pi_- M_(u_*) restricted to H_-, where Pi_- is the Hardy projection.

For the two prescribed prime sets, (3) and the prime estimate at
t=0 also give, with an absolute constant C for sufficiently large p,

    ||Phi_(P,M)||_infinity + ||Phi_(P,M)^(-1)||_infinity
        <=exp(C A).                                      (6)

Indeed log product(1-q^(-1/2))^(-1)=O(A), as is the analogous
upper product, and exp(M/2)/M=O(A). The estimates hold throughout
the lower half-plane, as well as on its boundary. No bound uniform
in p by a constant is asserted.

### 2. Evaluations in the fixed background and finite traces

Take v in K_*, and let j=u_*v in H_+. Their boundary L^2 norms
are equal. The following two analytic expressions have equal
boundary values on the real line:

    Z(z)=(z-i)^2 v(z)                    (Im z<0),
    Z(z)=(z+i)^2 u_inf(z)^(-1) j(z)     (Im z>0).         (7)

The reciprocal u_inf^(-1) is holomorphic in the upper half-plane;
its gamma numerator has positive real part in its argument, and
its reciprocal-gamma denominator is entire. Local H^2 boundary
convergence in (7), followed by Morera's theorem on rectangles
crossing the real line, glues the two formulas to an entire Z.
This argument uses equality in local L^1 and does not assume
pointwise boundary regularity in advance.

In detail, on any bounded real interval the polynomial and gamma
factors are bounded in a small closed strip, and the Hardy traces
converge in L^2, hence in L^1. Apply Cauchy's formula in the
upper and lower parts of a crossing rectangle, cut off at heights
plus/minus epsilon. For a point off the line, the internal
horizontal integrals cancel in the limit by this L^1 convergence.
The short vertical pieces tend to zero by the |y|^(-1/2) bound.
The resulting outer contour integral defines one analytic function
through the rectangle and agrees with both formulas. Such rectangles
cover the real line, proving the asserted entire extension.

The Hardy bound is |v(x+iy)|, |j(x+iy)| <= C||v||_2/sqrt(|y|)
in their respective half-planes. Gamma reflection gives, for
Im z>=0 and |z|<=R,

    |u_inf(z)^(-1)|<=exp(C(1+R)log(2+R)).

One direct check replaces 1/Gamma(1/4+iz/2) by
Gamma(3/4-iz/2) sin(pi(1/4+iz/2))/pi. Both gamma arguments then
have positive real part; their absolute values are bounded by the
gamma integrals with those real parts. The sine costs exp(O(R)).
Apply the Cauchy integral formula to (7) on a circle of radius
2R, R>=2. The singular bound |Im z|^(-1/2) at the two crossings
is integrable. It follows that

    max_(|z|<=R) |Z(z)|
        <=exp(C R log(2+R)) ||v||_2.                     (8)

The contour estimate is uniform: its only angular singularity is
|sin(theta)|^(-1/2), whose integral is finite; polynomial powers
of R are absorbed by the displayed exponential.

There is also a polynomial real-line evaluation bound. On the
strip 0<=Im z<=1/4, Stirling's formula gives

    |u_inf(z)^(-1)|<=C(1+|Re z|)^(1/4).

In this strip the two gamma arguments in the modulus ratio have
real parts in a fixed positive compact interval; the sector bound
in the cited Stirling formula is uniform. Cauchy's formula on
the radius-1/4 circle about real t, using (7) above and below the
line, then bounds |Z(t)| polynomially in 1+|t| times ||v||_2.
Division by |t-i|^2=1+t^2 proves, with a fixed exponent C_1,

    |v(t)|^2<=C(1+|t|)^(C_1)||v||_2^2.                  (9)

For clarity, the upper-strip gamma real parts lie in [1/8,3/8].
At large |Re z| both arguments stay in fixed Stirling sectors;
at bounded |Re z| compactness applies and there are no poles.
The ratio costs at most C(1+|t|)^(1/4). On the small circle the
polynomial factors cost C(1+t^2), which cancel on division.
Thus C_1=1/2 is permissible, though only polynomial growth is used.

For each fixed P,M, (5) and its bounded inverse transfer (9) to
K_(P,M), with a finite constant depending on P,M. Its reproducing
diagonal k_(P,M)(t,t) therefore has polynomial growth. For any
smooth compact physical test f, its Fourier transform is Schwartz,
so Tonelli applied to an orthonormal basis of this closed space gives

    ||M_F S_(P,M)||_HS^2
        =integral |F(t)|^2 k_(P,M)(t,t) dm(t)<infinity.   (10)

This proves the two separate finiteness assertions before taking
their difference. It will also justify the weighted traces below.
For nonnegative bounded u, localized notation Tr(uS) below means
Tr(SuS)=||sqrt(u)S||_HS^2 when finite; it does not assert that
the unsandwiched product uS is trace class.

### 3. Uniform localization for the corrected weight

For now let P=P_- and set w_p=|Phi_(P,M)|^2. The strengthened
absolute error in the cited prime-sum estimate yields, for each
fixed b_0>0 and uniformly on |t|<=2L^(b_0),

    log|D_P(t)|^2
      =-4A Re(exp(itL)/(1+2it))+O(A/L).                 (11)

Removing the endpoint prime changes the logarithm by O(r).
The terms of Euler degree at least two are O(L), even using only
the harmonic-sum bound, and are absorbed into O(A/L). The cited
prime estimate applies because 2L^(b_0)<=p for all sufficiently
large p. It is its absolute, not relative, error that is used.

On the real line the exact other weight is

    log|e_M(t)|^2
      =4 integral_0^M cosh(v/2)(cos(tv)-1)/v dv
         +2log(1+t^2).

Splitting at 1 and M/2 and integrating the exponential endpoint
on [M/2,M] gives, on the same frequency range,

    log|e_M(t)|^2
      =4 exp(M/2)/M [Re(exp(itM)/(1+2it))-1]+O(A/L).

For completeness, the integral on (0,1) is
O(1+log(2+|t|)), by |1-cos(tv)|<=min(2,t^2v^2/2).
The middle segment is O(exp(M/4)log M). In the last segment the
integration-by-parts remainder is O(exp(M/2)/M^2), uniformly in
t since |1/2+it|^(-1)<=2. The exp(-v/2) portion is smaller.
These bounds, and 2log(1+t^2), are absorbed in the stated error.
Since exp(M/2)/M=e A+O(A/L), combination with (11) gives

    log w_p(t)=4A [Re(exp(itL) (e exp(2it)-1)/(1+2it))-e]
                   +O_(b_0)(A/L).                      (12)

The crucial envelope is

    R(t)^2=|(e exp(2it)-1)/(1+2it)|^2
          =[(e-1)^2+4e sin(t)^2]/(1+4t^2).

Put d=(e-1)^2-e>0. Positivity follows already from e>8/3 and
the increasing quadratic x^2-3x+1 for x>=8/3. Using sin(t)^2<=t^2,

    R(t)^2 <= (e-1)^2-4d t^2/(1+4t^2),
    R(t) <= e-1-c t^2/(1+4t^2)                           (13)

for an absolute c>0. Thus the envelope still has its maximum at
zero, although its phase and absolute weight differ from the
uncorrected Euler case. On J=[-L^(-2),L^(-2)], (12) also gives

    inf_J log w_p >= -4A-C A/L.                         (14)

Indeed the real part in (12) equals e-1 at zero and differs from
it by O(L^2 t^2) on J: its first derivative at zero is purely
imaginary, and its second derivative on J is O(L^2).
Here L^2 t^2<=L^(-2), so the O(A/L) error still dominates.

We must control evaluations with this SMALL weight. Let
g=Phi_(P,M)v have norm one. By (6), ||v||_2<=exp(C_0 A), and
(14) implies ||v||_(L^2(J,dt))<=exp(2A+O(A/L)).
The same last bound holds for Z=(z-i)^2v on J, up to a constant.

Apply (8) on radius R_0=A/(log A)^3. Its supremum is at most
exp(C_2 A), with C_2 fixed. Approximate Z by its Taylor polynomial
Q_n of degree n=ceil(K A/log A), where K>C_2+10 is fixed.
On |z|<=2L^(b_0), Cauchy's coefficient bound gives

    |Z(z)-Q_n(z)|
      <=2 exp(C_2 A)(2L^(b_0)/R_0)^(n+1)<=exp(-5A)     (15)

for sufficiently large p, since log R_0=log A-O(log log A).
In particular ||Q_n||_(L^2(J))<=exp(2A+O(A/L)).

All constants are independent of the weighted unit vector and p.
In fact log A=L/2-log L, R_0 log R_0=O(A/(log A)^2), and
log(2L^(b_0)/R_0)=-log A+O_(b_0)(log L). Thus the logarithm
of the remainder in (15) is at most
(C_2-K)A+O_(b_0)(A log L/L), which is <=-5A eventually.

Rescale the normalized Legendre basis from [-1,1] to J. Its
degree-j members are bounded at real t by
C sqrt(j+1) L [C(1+L^2|t|)]^j. Cauchy--Schwarz in that basis
therefore gives

    sup_(|t|<=L^(b_0)) |Q_n(t)|
       <=C(n+1)L [C(1+L^(b_0+2))]^n ||Q_n||_(L^2(J)).

The logarithm of this interpolation factor is
O_(b_0)(A log L/L). Combining it with (15), and dividing by
|t-i|^2>=1, proves the UNIFORM weighted evaluation estimate

    sup_(||Phi v||_2=1) |v(t)|^2
       <=exp(4A+O_(b_0)(A log L/L)),   |t|<=L^(b_0).    (16)

The error on J contributes at most sqrt(2)L^(-1)exp(-5A)
to its L^2 norm. Even after the same interpolation factor this
remains exponentially smaller than the bound from (14).
This explicitly accounts for the growing degree; neither the
global exp(C_0 A) inverse cost nor interpolation is treated as a
parameter-independent constant.

Multiplying by w_p(t) gives the reproducing diagonal of the
actual corrected space in (5). Equations (12), (13), (16) imply

    log k_(P_-,M)(t,t)
       <=-c A t^2/(1+4t^2)+C_(b_0) A log L/L.          (17)

Take delta=L^(-2/5) and T=L. Since delta^2=L^(-4/5) dominates
log L/L, use b_0=2 in (17) to conclude

    sup_(delta<=|t|<=2T) k_(P_-,M)(t,t)
       <=exp(-c' A delta^2)                             (18)

for all sufficiently large p. This proves the changed-background
localization; it was not imported from the uncorrected theorem.

Indeed t^2/(1+4t^2)>=delta^2/5 for |t|>=delta and delta<=1,
whereas (log L/L)/delta^2=log L/L^(1/5) tends to zero.
Also 2T<=L^2 eventually, within the b_0=2 evaluation range.

### 4. Exact projection change and the arithmetic scale

Write S=S_(P_-,M), let V be multiplication by exp(-itL), and put

    D=I-rV, B=2I+V+V^*, H=Fourier(h), w=|H|^2,
    G=S D^*D S restricted to ran(S)
       =(1+r)^2 I-r S B S.

Here 0<=B<=4I and (1-r)^2 I<=G<=(1+r)^2 I. Equation (5), with
the same M, gives K_(P_+,M)=D K_(P_-,M), whence the orthogonal
projection onto this range is exactly

    S'=D S G^(-1) S D^*.                                (19)

Centering f_p changes the transform of h+V_Lh by exp(itL/2).
Thus |F_p|^2=wB. All multiplication operators in this sentence
commute. With W=wB, subtract the finite localized traces in (10):

    Delta_p=-r Tr_(ran S)(S W (I-S) B S G^(-1)).          (20)

Indeed D^*D=(1+r)^2 I-rB, whereas its compression is G;
expanding S W D^*D S-S W S G gives -r S W(I-S)BS.
The cyclic rearrangements can first be made between the
Hilbert--Schmidt factors W^(1/2)S and W^(1/2)DS. Their products
are trace class, so no difference of infinite Hardy traces occurs.

More explicitly set X=W^(1/2)DS, a Hilbert--Schmidt map from
ran S to the ambient space, since W^(1/2)D=DW^(1/2).
Then T_(P_+,M)(f_p)=Tr_(ran S)(X^*X G^(-1)), with
X^*X=S W D^*D S. Meanwhile SWS is trace class and
Tr_(ran S)(SWS)=Tr_(ran S)((SWS)G G^(-1)). Subtraction
inside this finite trace gives precisely (20). The source notation
Tr(WS) is used only for Tr(SWS), not to assume WS is trace class.

The corrected S projects onto ker(Pi_- M_(u_(P_-,M))|_(H_-)),
a Toeplitz kernel with bounded unimodular symbol. Consequently the background-independent
commutator estimates (6.21)--(6.24) of the cited source apply to
it, after reflection if needed. In particular, for an even smooth
cutoff theta, equal to one on [-1,1], zero outside [-2,2], and
nonincreasing on [0,infinity), they give, for 0<d<=1 and T>=1,

    ||[S,M_(w theta(t/d) B)]||_1 <= C_h(1+Ld)^(3/2),
    ||[S,M_(w(1-theta(t/T)) B)]||_1
         <=C_(h,N)(1+L)^2 T^(-N).                       (21)

Their scope is all Toeplitz kernels; neither the original
archimedean background nor source (6.20) is being assumed.

Two elementary bounds finish the application. For a multiplier a
whose displayed commutator is trace class,

    |Tr(S a(I-S)BSG^(-1))|
       <=4(1-r)^(-2)||[S,a]||_1.                        (22)

For a nonnegative multiplier u with Tr(uS)<infinity,

    ||S u B(I-S)BS||_1<=32 Tr(uS).                     (23)

To check (23), factor off S sqrt(u), of Hilbert--Schmidt norm
sqrt(Tr(uS)). Expand the other factor as
sqrt(u)B^2S-sqrt(u)BSBS. Each term has Hilbert--Schmidt norm at
most 16 sqrt(Tr(uS)), using commutation with B and ||B||<=4.
The inverse in (20) is still retained and bounded by (1-r)^(-2).

Decompose w into the three nonnegative multipliers

    w theta(t/delta),
    w [theta(t/T)-theta(t/delta)],
    w [1-theta(t/T)].

Equations (21),(22) bound the first and third covariance pieces
by O_h(L^(9/10)) and O_(h,N)(L^(2-N)). For the middle piece,
(10),(18),(23) give O_h(T exp(-c' A delta^2)), since it is
supported in delta<=|t|<=2T. The latter is smaller than every
negative power of L. The covariance in (20) is therefore
O_h(L^(9/10)), proving (1), including its normalization.

Finally, let a_h(x)=integral h(y)h(y+x)dy. It is supported in
[-2,2], is zero at both endpoints, and a_h(0)=1. The
autocorrelation of f_p is

    g_p(x)=2a_h(x)+a_h(x-L)+a_h(x+L).

For L>2 it satisfies g_p(L)=1 and g_p(kL)=0 for every integer
k>=2. It vanishes at the padded endpoints +/-M as well.
Fourier inversion applied to the prime-phase derivative in source
(5.2) gives the exact added arithmetic term

    -2L sum_(k>=1) r^k Re g_p(kL)=-2rL.                (24)

The prime-power series converges absolutely. Centering has
changed no autocorrelation, and the two pole phases are identical,
so their contributions cancel exactly. Each partial signed form
may omit visible primes between p and exp(M); no full-Weil
identity for it was used. Equations (1),(24) prove the conclusion.

Specifically, the derivative of the argument of the added factor
is -2L sum_(k>=1) r^k cos(ktL). The normalization dm=dt/(2pi)
gives integral |F_p(t)|^2 cos(ktL) dm=Re g_p(kL).
The series is uniformly absolutely convergent, and |F_p|^2 is
integrable. This justifies interchange without a limiting trace
formula. At L>2, all cross terms except a_h(0) vanish at L;
all terms vanish at kL for k>=2 and at +/-M, including a_h(2)=0.
The common pole contribution is identical before subtraction,
regardless of the omitted primes.

This parks the prescribed local absorption mechanism. It does
not sign Delta_p itself, prove any collective comparison, or
transfer a trace estimate to L522's conditional nullvectors.
That application would still require full-form identification,
the retained trace/nonresonance hypotheses, a family rate and Xi
transfer. No resolution of RH is claimed.

## Mathlib

Full coverage of this corrected projection result is not checked.
No matching Mathlib theorem is asserted, and the use of standard
Hardy, gamma and Hilbert-space facts above is not a formalization.
The extension beyond the inspected source is the rational
factorization and uniform estimate (18); originality is not
certified by the scoped search. The separate local conceptual audit
validated these applications and the finite-trace assembly, while
retaining the unaudited upstream-source qualification. No Mathlib
coverage or RH implication follows from that audit.
