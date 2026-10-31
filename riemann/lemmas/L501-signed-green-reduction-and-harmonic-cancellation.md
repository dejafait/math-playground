# Lemma 501: signed Green reduction and the surviving amplitude covariance

## Hypotheses

Use the actual completed xi and zeta of L018, with all zero
multiplicities. For sufficiently large real T put

    L=log T, delta=log L/L, a(t)=|zeta(1/2+it)|^2,
    M_0=integral_T^(2T) a(t) dt, mu=M_0/T,
    Q_4=integral_T^(2T) a(t)^2 dt.

Fix real C-infinity profiles chi,kappa,psi, independently of T, with
0<=chi,kappa<=1, chi(x)=0 for x<=1/4, chi(x)=1 for x>=1/2,
kappa(sigma)=1 for sigma<=1, kappa(sigma)=0 for sigma>=5/4,
and psi>=0 supported in [-3,3], psi>=1 on [-2,2]. Define

    Phi(sigma)=chi((sigma-1/2)/delta) kappa(sigma),
    Psi(u)=psi(u/delta),
    w(v)=integral_T^(2T) a(t) Psi(v-t) dt,
    f(sigma,v)=Phi(sigma)w(v).

Write p_0=integral_R psi, p_inf=sup_R psi. For distinct nontrivial
zeros rho=beta+i gamma with multiplicity m_rho set

    G(t)=sum_rho m_rho Phi(beta) psi((gamma-t)/delta),
    S=integral_T^(2T) a(t)G(t) dt,
    W_delta=integral_T^(2T) a(t)
        sum_{rho: beta>1/2+delta/2, |gamma-t|<=2delta} m_rho dt.

The sums in these integrals are finite. Retain the strict beta cutoff
and closed ordinate windows in W_delta; S is a smooth majorant, not
asserted equal to W_delta. Let

    H_xi=integral_R2 log|xi(sigma+iv)| Phi''(sigma)w(v) d sigma dv,
    V_xi=integral_R2 log|xi(sigma+iv)| Phi(sigma)w''(v) d sigma dv.

The analytic identity is imported from M. Krishnapur, *Zeros of Random
Analytic Functions*, [arXiv:math/0607504v1, 20 July 2006, Section 2.2,
equations (2.2.1)--(2.2.2), printed p. 14/PDF p. 23](https://arxiv.org/pdf/math/0607504v1#page=23):
for a non-identically-zero holomorphic F on an open connected set and
g in C_c^infinity of that set,

    integral log|F| Delta g = 2pi sum_{F(rho)=0} m_rho g(rho).   (PL)

This is the deterministic distributional zero-measure identity; no
random-field assertion is used. The application checks below are needed
because the test depends on T and delta. The source identity is not
reproved.

For the quantitative fallback only use the following cited inputs.
L471 Section 3, importing Bui--Hall, *On the derivatives of Hardy's
function Z(t)*, [arXiv:2304.05178v1, 11 April 2023, equation (1)](https://arxiv.org/html/2304.05178v1),
gives M_0=T L+O(T), hence M_0<=C_2 T L beyond a fixed onset.
Its Theorem 3 and Section 7, at derivative orders (0,0,0,0), give
Q_4<=C_4 T L^4, as imported in L471 Section 4. L471's identification
with the same Hardy function gives |Z(t)|^2=a(t).

Use the inputs recorded in L485 from Maples--Rodgers, *Bootstrapped
zero density estimates and a central limit theorem for the zeros of
the zeta function*, IJNT 11 (2015), 2087--2107,
[arXiv:1404.3080v2, 4 June 2016, Theorem 2.4 and Proposition 2.5,
printed p. 5](https://arxiv.org/html/1404.3080v2). With
N(sigma,y)=#{rho:beta>sigma, 0<gamma<y}, counting multiplicities,
Theorem 2.4 at fixed b=1/2 and L485's restricted k=2,c=1/4
reproduction of Proposition 2.5 give, uniformly for the shown parameters,

    N(sigma,U)<=C_D U log U exp(-(sigma-1/2)log U/2),       (D)
    integral_0^U [N(sigma,s+H/log U)-N(sigma,s)]^2 ds
        <=C_485 U H^2 exp(-(sigma-1/2)log U/4),             (M)

where U>=2, 1/2<=sigma<=1 and, in (M), 1<=H<=U^(1/4).
The arithmetic/manuscript audit qualifications in L471/L485 remain;
no selected-amplitude moment or general-weight extension is imported.
No RH, simplicity, spacing, independence, external half-plane estimate,
or conjectural weighted log approximation is assumed.

## Conclusion

Both curvature integrals are absolutely convergent, and exactly

    H_xi+V_xi = H_zeta+V_zeta = 2pi S >= 2pi W_delta >=0.   (1)

Here H_zeta,V_zeta replace log|xi| by log|zeta|. The sum of the
two completion-factor contributions is zero. More generally every
real C^2 harmonic function h on the rectangle Omega specified in
the proof has zero combined contribution. This includes the real part of every
finite Dirichlet/prime polynomial with coefficients and cutoff fixed
for the given T. It does not justify deleting either curvature term.

For such h put R_h(sigma,v)=log|zeta(sigma+iv)|-h(sigma,v) and

    K_delta(sigma,u)=Phi''(sigma)psi(u/delta)
                      +delta^(-2)Phi(sigma)psi''(u/delta),
    C_mix=(1/(2pi)) integral_T^(2T) (a(t)-mu)
                  integral_R2 R_h(sigma,t+u) K_delta(sigma,u)
                                      d sigma du dt.

Integrands are zero outside the compact test supports, so h is only
evaluated in Omega. All these integrals are absolutely convergent for fixed T. The signed
mixed remainder is independent of h and satisfies the exact relations

    C_mix=integral_T^(2T) (a(t)-mu)G(t) dt,
    S=mu integral_T^(2T) G(t) dt+C_mix.                    (2)

The available, uniform estimates are

    0<=mu integral_T^(2T) G(t) dt
        <=C T delta L^2 exp(-delta L/8),                   (3)
    |C_mix|<=14 p_inf sqrt(3 C_485 C_4)
                      T delta L^3 exp(-delta L/32).       (4)

Constants and one sufficiently large onset can depend on the fixed
profiles and cited constants, but not on T. With delta L=log L,
the mean term divided by T delta L^2 is O(L^(-1/8)), whereas
the bound in (4) divided by that scale is O(L^(31/32)). Compared
with the requested upper bound C T delta L^2 L^(-c), c>0 fixed,
the latter certificate has the divergent factor L^(31/32+c).

Thus (1)--(4) do NOT prove the approved signed-curvature bound or an
improvement for W_delta. For this smoothed test, a positive-part saving
for C_mix of some fixed power of L would suffice, together with (3),
and is still missing. Merely replacing log|zeta| by a harmonic prime-log
main term leaves exactly this uncontrolled remainder. This is a local
specialization of known identities/count/moment inputs and a diagnostic
stop of that implementation, not new zero-density mathematics, a lower
bound on the actual covariance, or an obstruction to every signed method.
The result awaits separate critical audit.

## Proof

### 1. Compact support, differentiation and logarithmic singularities

Choose a common onset with 0<delta<=1/8, T>3 and all cited moment
bounds available. Since a is continuous on [T,2T], it is bounded and
integrable there. For each fixed T and each integer j>=0,

    w^(j)(v)=integral_T^(2T) a(t) delta^(-j)
                                      psi^(j)((v-t)/delta) dt.   (5)

Differentiation follows by dominated convergence: the smooth profile
derivative is globally bounded and the t interval is fixed and finite.
The same argument gives continuity of each derivative. In particular
w is C_c^infinity, supported in [T-3delta,2T+3delta]. No derivative
of the sharp t interval indicator is taken. Tonelli and (5) give

    integral w=delta p_0 M_0,
    ||w^(j)||_1<=delta^(1-j)||psi^(j)||_1 M_0.              (6)

Phi is C_c^infinity, supported in
[1/2+delta/4,5/4], and is 1 on [1/2+delta/2,1]. Smoothness at
the support endpoints follows from the constant profile extensions.
Its derivative supports are disjoint: chi can vary only between
1/2+delta/4 and 1/2+delta/2, where kappa=1; kappa can vary only
between 1 and 5/4, where chi=1. Consequently

    ||Phi''||_1=delta^(-1)||chi''||_1+||kappa''||_1,
    ||Phi||_1<=3/4.                                      (7)

Thus f is a compact smooth plane test. Work on the open rectangle

    Omega={sigma+iv: 1/2+delta/8<sigma<3/2,
                                T-1<v<2T+1},

which contains supp(f) strictly. It contains neither the pole of zeta
nor a pole or zero of q(s)=s(s-1)pi^(-s/2)Gamma(s/2)/2. The
Gamma assertion follows from its standard nonvanishing/holomorphy in
Re(s/2)>0, recorded in the foundations. Both xi and zeta are
holomorphic and not identically zero on Omega. By L018 their zeros
there agree, with multiplicities, and every such zero has 0<beta<1.

On every compact neighborhood of supp(f) there are finitely many zeros.
Locally at a zero rho, factor F(s)=(s-rho)^m b(s), b holomorphic and
nonzero. Then log|F(s)|=m log|s-rho|+log|b(s)|; the logarithmic
singularity is locally absolutely integrable because
integral_0^epsilon r|log r|dr<infinity. Away from these neighborhoods
log|F| is bounded on the remaining compact set. This proves the
absolute integrability needed for H_xi,V_xi,H_zeta,V_zeta separately.
Values assigned at the zeros themselves are irrelevant to these
Lebesgue integrals.

It also proves every triple-integral interchange used below. Indeed,
after v=t+u the integral of the absolute value is bounded by a finite
constant, for this fixed T, times the integral of |log|zeta||+|h|
on a compact rectangle. The t weights a(t), a(t)-mu and all profile
derivatives are bounded on their finite domains. These qualitative
bounds justify Fubini; no uniform quantitative estimate for the mixed
logarithm is inferred from compactness.

### 2. The completion and every harmonic main term cancel

On Omega, L018 gives xi=q zeta and log|xi|=log|q|+log|zeta|
away from their zeros, hence almost everywhere. The function log|q|
is smooth and harmonic because q is holomorphic and nonzero there.
For any real C^2 harmonic h on a neighborhood of supp(f), integration
by parts twice in each coordinate, with no boundary terms, gives

    integral h (Phi''w+Phi w'')=integral Phi w Delta h=0.   (8)

Compact support suffices; no logarithm of zeta across a zero is used.
Using h=log|q| proves H_xi+V_xi=H_zeta+V_zeta exactly. Formula
(8) also applies to Re P(s) for any holomorphic P near the support.
In particular a finite sum of c_n exp(-s log n), or a finite prime-power
sum, is entire. Its length and coefficients may depend on the frozen
parameter T without changing (8). A cutoff varying with sigma or v
need not be holomorphic; no claim about such approximations is made.

Apply (PL) to f and xi to obtain

    H_xi+V_xi=2pi sum_rho m_rho Phi(beta)w(gamma)=2pi S.   (9)

The finite sum and the t integral may be interchanged directly. If
beta>1/2+delta/2 and |gamma-t|<=2delta, then Phi(beta)=1 and
psi((gamma-t)/delta)>=1; all other summands in G are nonnegative.
This proves (1), including equality ordinates and all multiplicities.
Zeros on the horizontal selection equality beta=1/2+delta/2 may
contribute to S, even though W_delta excludes them. At the lower
support equality beta=1/2+delta/4, Phi=0. None is lost silently.

For each t in [T,2T], the test Phi(sigma)psi((v-t)/delta) is also
compactly supported in Omega. Apply (PL) to zeta and subtract (8)
for this test. The change of variable u=v-t gives

    integral_R2 R_h(sigma,t+u)K_delta(sigma,u) d sigma du
                              =2pi G(t).                 (10)

This verifies both signed terms and the normalization in C_mix.
Multiplying (10) by a(t)-mu and integrating is legitimate by Section
1 and yields (2). It also proves the independence of h. No estimate
on an RH-dependent prime-log approximation has entered the argument.

### 3. The ordinary mean is small, with a strict selected count

Let U=3T, ell=log U and sigma_0=1/2+delta/4. For the common
large onset, L<=ell<=2L and

    0<T-3delta<2T+3delta<U.

Only zeros with beta>sigma_0 and these positive ordinates contribute
to integral_T^(2T)G. Each contributes at most delta p_0 times its
multiplicity, because 0<=Phi<=1 and the clipped t integral of psi
is at most its full integral. With (D),

    integral_T^(2T) G(t)dt
        <=delta p_0 N(sigma_0,U)
        <=p_0 C_D delta U ell exp(-delta ell/8)
        <=6p_0 C_D T delta L exp(-delta L/8).              (11)

Both strict conventions in N are respected: the lower beta equality
has Phi=0, and contributing ordinates are strictly below U.
Multiplication by mu<=C_2 L proves (3), with
C=6p_0 C_D C_2. It uses only ordinary mean amplitude and total
selected count; no independence assertion is present.

### 4. The centered term retains the old separation loss

The pointwise majorant is

    G(t)<=p_inf #{rho: beta>sigma_0, |gamma-t|<=3delta}.

Put s=t-(7/2)delta and H=7delta ell. The closed displayed ordinate
window lies strictly inside [s,s+7delta), so

    G(t)<=p_inf [N(sigma_0,s+H/ell)-N(sigma_0,s)].        (12)

For one common sufficiently large onset, the translated t interval
lies in [0,U] and 1<=H<=U^(1/4). For example H is comparable to
log L, whereas U^(1/4) grows as exp(L/4), so a fixed onset suffices
for all larger real T. Formula (M) and the nonnegative integrand
therefore imply

    integral_T^(2T) G(t)^2 dt
        <=49 p_inf^2 C_485 U delta^2 ell^2
                                         exp(-delta ell/16).    (13)

The vertical padding in (12) handles both closed endpoints; the strict
beta threshold is unchanged. The estimate retains all multiplicities.
Since mu is the exact mean,

    integral_T^(2T) (a(t)-mu)^2 dt=Q_4-M_0^2/T<=Q_4.

Cauchy--Schwarz, (13) and Q_4<=C_4 T L^4 yield

    |C_mix|<=7p_inf sqrt(3 C_485 C_4)
              T delta ell L^2 exp(-delta ell/32),

which gives (4) using ell<=2L and ell>=L. All constants remain
independent of the moving delta and real height T.

Finally exp(-b delta L)=L^(-b) at the stipulated scale. This proves
the stated actual-versus-required comparisons. More explicitly, if
(C_mix)_+<=C T delta L^2 L^(-c) were proved for some c>0,
(2)--(3) would give S<=C' T delta L^2 L^(-min(c,1/8)). Conversely
such a bound for S implies the same bound for (C_mix)_+, since the
mean term in (2) is nonnegative. This equivalence for the smoothed
statistic only locates the missing signed estimate; it does not prove
it or equate it to RH. The upper bound (4) supplies no lower bound
on C_mix or W_delta, and cannot refute a stronger saving.

The exact harmonic cancellation is the diagnostic result of this
attempt. The residual representation (10) by itself is a restatement
of a weighted count. Using (4) repeats amplitude/count separation.
Accordingly this implementation stops unless a separately justified
nonharmonic weighted-error estimate or a different mechanism is supplied.
Kernel transfer, other scales, complementary negative mass and individual
Xi signs remain unresolved.

## Mathlib

Full coverage of this weighted compact-test specialization, the uniform
count estimates and the mixed-moment statement has not been checked.
Unknown availability is not evidence of absence. The mathematical inputs
are the precise cited deterministic identity and the local applications
of the named count/moment sources, with the qualifications above. No
formal verification or new source theorem is claimed.
