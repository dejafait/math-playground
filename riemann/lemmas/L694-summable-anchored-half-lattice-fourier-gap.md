# Lemma 694: summable shifts in the anchored half-lattice Fourier gap

## Hypotheses

Use L693's Fourier conventions F_(2pi)f(t)=integral f(x)exp(-2*pi*i*t*x)dx
and F_ang f(omega)=integral f(x)exp(-i*omega*x)dx, with their tempered
distribution extensions. The spatial anchor is 0 and all atom masses
are one. The interval of vanishing is allowed to be arbitrarily narrow;
no reflection symmetry of the spatial measure is imposed.

## Conclusion

There exist real e_m, m in Z, such that

    sup_m |e_m|<=1/8,       sum_m |e_m|<infinity,
    mu=delta_0+sum_(m in Z) delta_(m+1/2+e_m)

is a positive translation-bounded tempered measure whose angular Fourier
transform vanishes on a nonempty open interval I contained in (0,2*pi).
Nonanchor gaps are at least 3/4, every nonanchor atom is at distance at
least 3/8 from 0, and all masses remain one.

The added conclusion relative to L693 is absolute summability. It follows
by a two-norm specialization of Lev's existing Picard construction, not
by a matching theorem statement in the inspected source. This is
development of the known method, with no claim of originality. The separate
conceptual audit of 3 November 2026 (step 113) accepts the proof under
the stated hypotheses; its limit and prescription checks are recorded
below. It provides neither
an effective gap width nor a spatial tail rate, finite logarithmic bound,
complex-frequency estimate, rational-W bound, H/support or Xi realization.
In particular, it does not close actual-Xi all-degree mixed positivity.

## Proof

### Named input and the precise specialization

Import the coefficient estimate of Nir Lev, *An example concerning
Fourier analytic criteria for translational tiling*, Rev. Mat. Iberoam.
**38** (2022), 1975--1991, DOI
[10.4171/RMI/1318](https://doi.org/10.4171/RMI/1318),
[Lemma 4.3, p.1984, equation (4.6)](https://ems.press/content/serial-article-files/39104).
In [arXiv:2007.09930v3, Section 4.3](https://arxiv.org/html/2007.09930v3#S4.SS3)
this estimate is (4.10). The source's Sections 4.5--4.9, especially
Lemmas 4.5--4.7 and (4.19), (4.23), define the supported-distribution
operator and its small coefficient-sup Picard iteration. Section 4.10,
(4.24)--(4.26), passes from interval indicators to unit counting masses.
These are primary inputs; the termwise coefficient estimate is imported,
not reproved. The necessary extra argument is its l1 summation and the
identification of the resulting limit for the exact anchored data.

Fix a=1/8, b=3/8 and l=7/16. Choose once and for all a smooth real even
Phi supported compactly in (-l,l), equal to one on [-b,b]. For functions
or distributions on the unit circle, write

    f-hat(k)=<f,exp(-2*pi*i*k*t)>,
    ||f||Y=sup_k |f-hat(k)|,       ||f||A=sum_k |f-hat(k)|.

Here Y is Lev's real Banach space of distributions supported in [-l,l]
with real bounded coefficients. A is the Wiener space of absolutely
convergent Fourier series. The inclusion A into the coefficient-sup
space is continuous since ||f||Y<=||f||A. Elements of A intersect Y
are viewed as supported functions on (-1/2,1/2) and extended by zero
to the real line when needed. Write c(T)=(T-hat(n))_n.

For real sequences alpha of sup norm at most one, Lev defines

    R(alpha)(t)=sum_n E_n(alpha_n;t),
    E_n(u;t)=exp(2*pi*i*n*t)
             *(exp(2*pi*i*u*t)-1-2*pi*i*u*t)/(2*pi*i*t)*Phi(t).       (1)

The value at t=0 is the smooth removable value. Each E_n is supported
in [-l,l] and has the Hermitian symmetry giving real coefficients.
The series is the distributional sum specified in the source.

Apply the imported Lemma 4.3 to

    varphi(v)=(exp(2*pi*i*v)-2*pi*i*v)/(2*pi*i),

whose derivative vanishes at zero, with exponent m=2. After modulation
by exp(2*pi*i*n*t), its conclusion is: there is a fixed C>0 such that
for all real |u|,|v|<=r<=1 and k,n in Z,

    |[E_n(v)-E_n(u)]-hat(k)|
          <= C*r*|v-u|/(1+|k-n|^2).                              (2)

C depends only on the already fixed Phi and varphi, not on r, n, k or
the later cutoff width h. This is also the termwise application in
Lev's Section 4.7. Put K=sum_(j in Z)(1+j^2)^(-1)<infinity.

### The l1 estimate and compatibility with the source's sum

For alpha,beta in l1 with sup norms at most r, Tonelli applied to the
nonnegative bound (2) gives

    sum_n ||E_n(beta_n)-E_n(alpha_n)||A
          <= C*r*K*sum_n |beta_n-alpha_n|.                        (3)

Thus the difference series converges absolutely in the Banach space A.
Its sum equals R(beta)-R(alpha) from the source: the finite sums are
identical, A convergence implies distributional convergence, and the
distributional limit is unique. Taking alpha=0, and noting R(0)=0,
shows that R maps the small-sup part of l1 into A intersect Y. In
particular, with q=C*K*r,

    ||R(beta)-R(alpha)||A<=q*||beta-alpha||1,
    ||R(alpha)||A<=q*||alpha||1.                                 (4)

For arbitrary bounded real alpha,beta in that sup ball, the source's
distributional convergence and the sum of (2) at each fixed k give

    ||R(beta)-R(alpha)||Y<=q*||beta-alpha||infinity.                (5)

Every coefficient series here is absolutely convergent since K is
finite. These estimates do not require a small l1 norm of alpha or beta.

Choose r=min(1/8,1/(4*C*K)) now, so 0<r<=1/8 and q<=1/4. This choice
depends only on the fixed kernel, not on the prescribed smooth data.

### Persistence and convergence of the same Picard iteration

Suppose Q is in A intersect Y and d=||Q||Y<=r/2. There is no smallness
requirement on ||Q||A. If d=0 then Q=0 and T=0 suffices. Otherwise use
the source's ball B=B(Q,1) and map, with different letters for the data:

    B={T in Y: ||T-Q||Y<=d},
    H(T)=Q-R(c(T)),           T_0=Q,   T_(j+1)=H(T_j).             (6)

For T in B, ||T||Y<=2d<=r. By (5) with the zero sequence,

    ||H(T)-Q||Y<=q*||T||Y<=2q*d<=d,
    ||H(T)-H(U)||Y<=q*||T-U||Y,              T,U in B.             (7)

Hence this is exactly Lev's supported-distribution Picard map, on an
invariant ball with a smaller permitted threshold. Its limit in Y is
the unique fixed point in B. No separate l1 fixed point is substituted.

Since T_0=Q is in A, (4) proves inductively that every T_j is in A.
Also

    ||T_j||A <= (1+q+...+q^j)*||Q||A <= ||Q||A/(1-q),
    ||T_1-T_0||A <= q*||Q||A,
    ||T_(j+1)-T_j||A <= q^(j+1)*||Q||A.                         (8)

For the last inequality, apply (4) to c(T_j),c(T_(j-1)); they have
sup norms at most r, and their l1 difference norm is the A norm of
T_j-T_(j-1). The geometric sum proves convergence in A to a limit T.
Its A norm is at most ||Q||A/(1-q). The support and real-coefficient
conditions are closed under A convergence, as checked below. Thus the
limit is in A intersect Y, whose inclusion into Y is continuous, so it
is the same Y fixed point, and c(T_j) converges in l1 to c(T).
Alternatively (4) passes the nonlinear term directly to the A limit.
Thus, putting alpha=c(T),

    T+R(alpha)=Q,
    ||alpha||infinity<=r,          ||alpha||1<=||Q||A/(1-q)<infinity. (9)

Reality and support are retained: all iterates have real coefficients
and vanish outside [-l,l] on the circle; A convergence gives coefficient
convergence and uniform convergence of their Fourier-series functions.
Their limit therefore has the same reality and support. In particular
no weak limiting assertion is being used to infer l1 summability.

### The exact reflected anchored prescription meets these hypotheses

Choose a fixed smooth Psi with support compactly in (-l,l), satisfying
Psi(-t)=conjugate(Psi(t)) and Psi(t)=-1/(2*pi*i*t) for
t in (-b,-a) union (a,b). This is the cutoff used in Lev's Section 4.10;
it can be chosen smooth at zero by making it vanish near zero. Fix
M=max(1,||Psi||infinity). All of Phi, C, K, r, Psi and M have now been
chosen before h.

Use L693's real even cutoff eta, with 0<=eta<=1, eta=1 on [-1/2,1/2]
and support in [-1,1]. Set

    c=1/4,       h=min(1/32,r/(8*M))>0,
    chi(t)=eta((t-c)/h)+eta((t+c)/h),
    S(t)=-exp(pi*i*t)*chi(t),
    P(t)=Psi(t)*S(t),                Q(t)=P(-t).                   (10)

The support intervals of chi are disjoint and strictly inside
(-b,-a) union (a,b). S, P and Q are smooth and compactly supported
there, and each has the required Hermitian symmetry. Their periodic
extensions are smooth, so Q belongs to A intersect Y: for k!=0, two
integrations by parts bound |Q-hat(k)| by
||Q''||L1/(4*pi^2*k^2), while |Q-hat(0)|<=||Q||L1. These derivatives
may grow when h shrinks; only finiteness is used.

The actual small norm, including multiplication and reflection, obeys

    d=sup_k |Q-hat(k)|<=integral |P(t)|dt
       <=M*integral chi(t)dt<=4*M*h<=r/2.                        (11)

Thus (9) applies to Q=(Psi*S)(-t), not to S alone. The threshold has
been fixed before h; no smallness or h-uniform bound for ||Q||A has
been asserted. This selects a possibly narrower version of L693's same
smooth prescription, exactly as permitted in the assessed target.

### Limit identification, unit masses and the fixed anchor

Let F_n be the signed indicator of the interval from n to n+alpha_n:
it is 1_[n,n+alpha_n] for alpha_n>=0 and -1_[n+alpha_n,n] otherwise.
Since sum |alpha_n|<infinity, F=sum F_n converges in L1, with
||F||L1<=sum |alpha_n|. For real t the identity

    F-hat_n(-t)=exp(2*pi*i*n*t)
                *(exp(2*pi*i*alpha_n*t)-1)/(2*pi*i*t)

has the continuous value alpha_n at t=0, and its absolute value is
at most |alpha_n|. Hence these Fourier transforms sum uniformly. On
(-b,b), where Phi=1, splitting the linear term off as in (1) gives

    F-hat(-t)=T(t)+R(alpha)(t)=Q(t),
    F-hat(t)=P(t)=Psi(t)*S(t).                                  (12)

The linear Fourier series is absolutely convergent to T. The nonlinear
series agrees with the A sum already identified in (3). This proves
the source's reflection convention for this same l1 limit.

Distributional differentiation gives F'=delta_Z-delta_Lambda, where
Lambda={n+alpha_n:n in Z}. Indeed it holds for every signed interval;
L1 convergence permits differentiation in distributions, and the
counting sums are locally finite because the shifts are bounded. Thus
on (-b,b),

    F_(2pi)(F')=2*pi*i*t*P(t)=-S(t).

The multiplier identity holds on a neighborhood of supp S, and both
sides are zero off that support. By the standard Poisson summation
formula F_(2pi)delta_Z=delta_Z, and since b<1/2,

    F_(2pi)delta_Lambda=delta_0+S             on (-b,b).          (13)

This retains unit counting masses. Put e_m=alpha_m and translate this
counting measure by 1/2, then add the fixed spatial atom at 0. L693's
translation formula, or multiplication of (13) by exp(-pi*i*t), yields

    F_(2pi)mu=1+delta_0-chi                  on (-b,b).          (14)

On J=(c-h/2,c+h/2), chi=1 and the frequency atom at zero is absent.
Equation (14) annihilates every test function supported in J. The
angular convention gives the gap I=2*pi*J, a nonempty open interval
in (0,2*pi). Explicitly its test-function pairing is
<F_ang mu,phi>=2*pi*<F_(2pi)mu,t -> phi(2*pi*t)>; thus the distributional
meaning and scale are unchanged from L693.

Finally ||alpha||infinity<=1/8 gives the same separation and
translation-boundedness estimates as L693. In particular every nonanchor
point has distance at least 3/8 from zero, consecutive ones are at least
3/4 apart, and the anchor is a distinct atom of mass one. The counting
measure is positive and tempered. Equation (9) supplies its absolutely
summable real displacements. No unsmoothed finite Fourier sum, spatial
moment, complex-frequency continuation or logarithmic limit was used.

### Independent conceptual audit: norms, limits and prescription

Step 113 reused the approved assessment
`drafts/literature/2026-11-03-summable-anchored-gap-audit-scope.md`
and checked the cited primary arXiv v3 Section 2 and Sections 4.3--4.10,
including Lemma 4.3's complete proof and the distributional summation,
fixed-point, reflection and differentiation cases. The published
page/equation references above are reused from the source assessment.
This is an audit of the stated specialization, not a new source search
or an independent certification of the entire article.

For the imported estimate, varphi'(v)=exp(2*pi*i*v)-1 vanishes at zero.
Moreover E_n(v)-E_n(u) is precisely exp(2*pi*i*n*t) times the source's
psi_(u,v), including the removable value at t=0. Modulation changes k
to k-n. The chosen real even Phi satisfies the source's Hermitian
cutoff hypotheses. Consequently one fixed C works for both (3) and (5).
The double series in (3) has sum at most C*r*K*||beta-alpha||1;
it is not a rearrangement of a merely conditionally convergent series.
For a smooth circle test f, A convergence implies distributional
convergence, for example by

    |<V,f>| <= ||V||A * integral_T |f(t)|dt.

This proves the required compatibility with the source's sum. For
bounded sequences in (5), the coefficient sum is bounded by
C*r*||beta-alpha||infinity*K; the source's Lemma 4.5 identifies those
coefficients with its distributional limit. No A assertion is made
for arbitrary bounded input.

The geometric differences in (8) give the explicit audit bound

    ||T-T_j||A <= q^(j+1)*||Q||A/(1-q),       j>=0.                (15)

All iterates lie in B, since 2q*d<=d/2<=d. The A limit is supported
in [-l,l] because A convergence implies uniform convergence and every
iterate vanishes on the complementary open set. Its coefficients are
real by coordinate convergence. Hence the limit belongs to Y, remains
in the closed ball B, and is the same Y limit by ||V||Y<=||V||A on
this subspace. Equation (4) also passes R(c(T_j)) to R(c(T)) in A.
This establishes the fixed-point equation in both senses; neither a
weak-limit l1 inference nor a small ||Q||A assumption is needed. The
case d=0 is valid because zero Fourier coefficients determine the zero
distribution on the circle.

The data check does not replace the source's general multiplier norm
by a supremum norm. Lev's Section 4.10 uses ||Psi||A for a general
pseudomeasure. Here P is an actual smooth function, so the separate
direct estimate ||Q||Y<=||P||L1<=||Psi||infinity*||chi||L1 proves
(11). The two occurrences of a multiplier bound are not interchangeable.
Reflection sends Q-hat(k) to P-hat(-k) and preserves the coefficient
supremum and Hermitian symmetry. All constants precede h. The choices
h<=1/32 and c=1/4 put the positive support in [7/32,9/32], strictly
inside (a,b), and similarly on the negative side. Thus Psi has the
required exact value throughout a neighborhood of supp S. Finite
||Q''||L1 suffices for membership in A; its size is not used to set r.

Finally, L1 convergence of the signed intervals gives uniform Fourier
convergence, and (3) gives uniform convergence of the nonlinear
Fourier-series functions. These justify the two splits in (12),
including t=0, for the same alpha. For a Schwartz test f, the endpoint
series is also absolutely convergent directly:

    sum_n |f(n)-f(n+alpha_n)|
        <= ||f'||infinity * sum_n |alpha_n|.

It therefore equals the distributional derivative of F with sign
delta_Z-delta_Lambda. Equations (13)--(14) follow with +S and -chi,
respectively. The added spatial atom transforms to the constant one;
it is not another frequency atom. Translation preserves all masses,
the separation estimates prevent collisions, and the angular pairing
has Jacobian 2*pi. No cancellation or limiting operation changes the
fixed anchor or a unit counting mass.

All tested claims pass. The only textual clarification is to make the
support/reality condition explicit before using the inclusion into Y;
the original proof already supplied its closure argument. There is no
substantive error repair, stronger theorem, added mathematical input or
finite-transfer conclusion. The result remains a local development of
Lev's method, without certified originality or a claim about RH.

## Mathlib

Full coverage of this l1 specialization or Lev's prescription theorem
has not been checked. Banach fixed points, absolute convergence and
Fourier/distribution operations are standard supporting mathematics;
no matching Mathlib theorem names are asserted. Unknown coverage is not
evidence of absence.
