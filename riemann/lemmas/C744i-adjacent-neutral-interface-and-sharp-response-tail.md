# C744i: Exact neutral adjacent interface and its undiminished L2 response tail

## Hypotheses

Put ell=log(3)/2, d=log(2), a=d/sqrt(2), and use the complex inner
product linear in its first argument. All functions are extended by
zero. Let N_neut denote L743(2)'s class

    {h in C_c^infinity(0,ell;C): integral e^(x/2)h(x)dx
                                =integral e^(-x/2)h(x)dx=0}.

Write Rf(x)=f(ell-x) and (tau g)(x)=g(x-ell). Use the complete
energy and its Hermitian polarization in L741 and L744(6). On N_neut the
single-cell energy is exactly

    E(h)=integral_R m(t)|F_h(t)|^2 dt/(2pi),
    F_h(t)=integral h(x)e^(-itx)dx,
    m(t)=Re psi(1/4+it/2)-log(pi).                         (1)

There is no single-cell arithmetic delay because ell<d, and the pole
product is zero by the two exact moments. The adjacent polarization
H(f,tau g) still includes the arithmetic delay d.

The positivity E(h)>=c_*||h||_2^2, c_*=8.9e-18, is the existing
L741(6) specialization of Xuefeng Zhu, *Weil positivity in compact
windows*, arXiv:2608.24827v2 (2 September 2026),
[Corollary6.3](https://arxiv.org/html/2608.24827v2). Its external
computation has not been locally replayed. This corollary does not
reprove that theorem or assume RH.

For each integer N>=1 define the Hankel operator K_N on L2(0,ell)
by the kernel

    k_N(x+y),    k_N(t)=e^(-(2N+1/2)t)/(1-e^(-2t)), t>0,

and put

    (J_d h)(x)=1_(d-ell,ell)(x) h(d-x),
    X=K_1+a J_d,     C=pi/2+a.                           (2)

The named operator input is Perfekt--Pushnitski, *On the spectrum of
the multiplicative Hilbert matrix*, Ark. Mat.56 (2018),163-183,
[Lemma2.1, printed p166](https://archive.intlpress.com/site/pub/files/_fulltext/journals/arkiv/2018/0056/0001/ARKIV-2018-0056-0001-a010.pdf):
a half-line Hankel kernel bounded by A/(x+y) has L2 norm at most A*pi.
We import its upper bound and prove the particular neutral lower
bound below. The digamma normalization and logarithmic asymptotic
are already justified in L741(13)-(18) and L744(6)/(8); the latter is

    |m(t)-log(|t|/(2pi))|<=2/t^2, |t|>=1.                 (3)

L744's scalar sources are [NIST DLMF5.11.2](https://dlmf.nist.gov/5.11.E2)
and its [remainder statement, 5.11(ii)](https://dlmf.nist.gov/5.11#ii),
applied to z=1/4+it/2 in the right half-plane. Their specialization
is reused, not reproved here.

## Conclusion

The exact adjacent pairing and relative constant are

    H(f,tau g)=-<X Rf,g>,
    beta_1=sup_(nonzero h,g in N_neut) |<Xh,g>|/sqrt(E(h)E(g)). (4)

The two completion terms and the response with rate 1/2 vanish
exactly. The entire K_1 tail and the n=2 delay in (2) remain.

For every fixed N>=1, the neutral compression has the sharp norm

    sup_(nonzero h,g in N_neut) |<K_N h,g>|/(||h||_2||g||_2)
      =sup_(nonzero h in N_neut) <K_N h,h>/||h||_2^2=pi/2. (5)

Thus deletion of any fixed number of slow exponential responses
does not lower this L2 tail norm. This is a specialization of the
classical Carleman mechanism, not a claim of a new general theorem.

The exactly neutral smooth sequence used for (5) has E(h_T)->infinity,
<J_d h_T,h_T>->0, and ||h_T||_2->1. Consequently its complete
adjacent energy ratios tend to zero, not to 1/2. Formula (5) does
not refute the fixed beta_1<1/2 target.

A sufficient, still unpaid certificate for that target is one number
mu>0 such that, for every h in N_neut and for both signs,

    E(h) +/- 2<Xh,h> >= mu ||h||_2^2.                    (6)

It would give beta_1<=C/(2C+mu)<1/2. No value mu>0 valid on the full
class is established here. The finite-dimensional diagnostics below
are neither an upper bound for beta_1 nor a certificate of (6).

This is the local analytic reduction in the single approved step482
attempt. It remains unaudited separately; all distant interactions,
non-neutral directions, odd signs and global positivity remain open.

## Proof

### 1. The complete cross form and exact cancellations

L741(21)-(24), with k(t)=2e^(-t/2)/(1-e^(-2t)), says

    H(f,tau g)
      =-1/2 integral_0^ell integral_0^ell
         [k(ell+s-y)-4cosh((ell+s-y)/2)] f(y)overline(g(s)) dy ds
       -a integral_(d-ell)^ell f(ell+s-d)overline(g(s))ds. (7)

This is the complete polarization, including its factor 1/2 and
the single active delay. The n=3 endpoint delay is zero. The local
scalar has no cross term on disjoint supports.

Set v=ell-y and h(v)=Rf(v). Reflection preserves N_neut, since

    integral e^(sigma v/2) Rf(v)dv
      =e^(sigma ell/2) integral e^(-sigma y/2) f(y)dy=0

for sigma=+1,-1. Each term in cosh((s+v)/2) factors into one moment
of h and one conjugate moment of g. Both terms therefore vanish;
this is an equality, not a favorable-sign deletion. The arithmetic
integral becomes <J_d h,g> with the interval in (2).

For t>0 the geometric series gives

    k(t)/2=sum_(n>=0) e^(-(2n+1/2)t).

For the given compactly supported smooth h,g their supports have
positive distance from zero, so the double integrals of the absolute
series converge. Fubini applies. The n-th integral is

    [integral e^(-(2n+1/2)v)h(v)dv]
      overline([integral e^(-(2n+1/2)s)g(s)ds]).

The n=0 response is zero. Summing the remaining terms gives K_1
exactly. This proves the first equality of (4), keeping the whole
singular tail and prime delay. Reflection changes F_f(t) into
e^(-it ell)F_f(-t). Since m is even, (1) gives E(Rf)=E(f).
As R is an involution of N_neut, the supremum equality in (4) follows.

### 2. Boundedness and the upper bound in (5)

For t>0,

    1-e^(-2t)=integral_0^(2t) e^(-u)du >= 2t e^(-2t).

Therefore, for N>=1,

    0<k_N(t)<=e^(-(2N-3/2)t)/(2t)<=1/(2t).              (8)

Apply the cited Carleman domination theorem to zero extensions on
the positive half-line and restrict its output to (0,ell). It gives
||K_N||<=pi/2. The geometric response sum also shows positivity on
interior smooth tests. By L2 density and boundedness this extends
to the full space, where K_N is self-adjoint. The same norm bound
holds on N_neut and proves both upper bounds in (5).

J_d is self-adjoint by x->d-x on the invariant interval (d-ell,ell),
and has norm one. In particular ||X||<=C. No energy-norm conclusion
below 1/2 is inferred from this L2 estimate.

### 3. Smooth Carleman sequence and exact moment correction

Choose a fixed 0<delta<d-ell. Let phi be a real smooth function
with 0<=phi<=1, phi(t)=0 for t<=0 and phi(t)=1 for t>=1.
For T>2 define chi_T(t)=phi(t)phi(T-t), extended by zero outside
[0,T], and

    u_T(x)=T^(-1/2)x^(-1/2) chi_T(log(delta/x)), x>0.

This is in C_c^infinity(0,ell), supported in
[delta e^(-T),delta]. With t=log(delta/x),

    ||u_T||_2^2=T^(-1) integral_0^T chi_T(t)^2dt ->1,
    ||u_T||_1<=2sqrt(delta)/sqrt(T).                     (9)

Use L743 Section3's fixed smooth right inverse for the two moment
functionals: choose a nonnegative interior bump chi positive on an
interval, set b_sigma(x)=chi(x)e^(sigma x/2), and let

    G_(sigma,tau)=integral chi(x)e^((sigma+tau)x/2)dx.

That section proves G positive definite and the exact right-inverse
property. If q_T has components integral e^(sigma x/2)u_T(x)dx,
then q_T=O(T^(-1/2)) by (9). Put

    v_T=sum_tau (G^(-1)q_T)_tau b_tau,   h_T=u_T-v_T.

The moments of h_T are exactly zero, not approximately zero.
Both ||v_T||_2 and ||v_T||_1 are O(T^(-1/2)), because the two fixed
bumps have finite norms. Hence h_T is a real member of N_neut,
||h_T||_2->1, ||h_T||_1=O(T^(-1/2)), and h_T is nonzero eventually.
The correction need not share the shrinking support of u_T.

### 4. The sharp lower bound and the prime term

Let A have kernel 1/(x+y) on (0,ell). For the nonnegative u_T,
the change of variables in (9) gives exactly

    <A u_T,u_T>
       =1/T integral_R integral_R
          chi_T(t)chi_T(s)/(2cosh((t-s)/2)) dt ds.

For each fixed r, the normalized overlap
T^(-1) integral chi_T(t)chi_T(t-r)dt tends to one: both cutoffs
are one except in endpoint sets of bounded length, depending on r.
The overlap lies between zero and one. Dominated convergence against
the integrable kernel 1/(2cosh(r/2)) gives

    <A u_T,u_T> -> integral_R dr/(2cosh(r/2))=pi.         (10)

The last integral follows from z=e^(r/2), giving
integral_0^infinity 2 dz/(1+z^2)=pi.

For fixed N, the difference k_N(t)-1/(2t) extends continuously to
t=0, with value 1/4-N, by the Taylor expansions of the two
exponentials. It is therefore bounded on [0,2ell]. By (9),

    |<K_N u_T,u_T>-1/2<A u_T,u_T>| <= M_N||u_T||_1^2 ->0.

The norm bound in (8) and ||v_T||_2->0 show that replacing u_T
by h_T changes the pairing by a quantity tending to zero. Thus
<K_N h_T,h_T>->pi/2. Together with ||h_T||_2->1 this proves (5).
The limit is for each fixed N; it is not uniform in growing N.

Because u_T is supported below delta<d-ell, J_d u_T=0. Its
boundedness and ||h_T-u_T||_2->0 give <J_d h_T,h_T>->0. Thus the
complete numerator for the pair (Rh_T,h_T) tends in modulus to pi/2.

### 5. Why this is not a counterexample in the energy metric

The real continuous symbol m is bounded below: it is continuous
on every compact interval and tends to infinity by (3). Fix M>=0
with m>=-M. For any B>0 choose R_B so m(t)>=B whenever |t|>R_B.
By ||h_T||_1=O(T^(-1/2)),

    integral_(|t|<=R_B) |F_(h_T)(t)|^2 dt/(2pi)
       <=(R_B/pi)||h_T||_1^2 ->0.

Plancherel and (1) therefore imply

    E(h_T)>=B||h_T||_2^2
       -(B+M) integral_(|t|<=R_B)|F_(h_T)(t)|^2dt/(2pi).

Its limit inferior is at least B. Since B is arbitrary, E(h_T)
tends to infinity. Smoothness makes each individual energy finite.
Reflection preserves E, so (4) for (Rh_T,h_T) has denominator
E(h_T) and bounded numerator. The ratio tends to zero. The sharp
L2 tail obstruction must not be advertised as a beta_1 obstruction.

### 6. The unpaid positive-margin test

If (6) held, its two signs would give

    E(h)>=2|<Xh,h>|+mu||h||_2^2.

Since |<Xh,h>|<=C||h||_2^2, this implies
|<Xh,h>|<=b E(h), b=C/(2C+mu). The Hermitian diagonal bound gives
the same cross bound. Indeed, after a complex phase adjustment to g,
the real part of <Xh,g> equals its modulus. Polarization bounds that
real part by

    b/4 [E(h+g)+E(h-g)]=b/2 [E(h)+E(g)].

Rescale the nonzero h and g to have equal energies; E is positive
by the cited L741 input. This yields |<Xh,g>|<=b sqrt(E(h)E(g)).
Thus (6) would suffice, but no assertion of (6) is made.

### 7. Exact normalization of the finite-dimensional locator

The exploratory script uses the following expression, not a discarded
boundary term. For a smooth interior neutral h, or a neutral polynomial
on (0,ell) extended by zero, put q_0(t)=k(t)-1/t, with q_0(0)=1/2.
The full prime-free neutral energy is

    E(h)= integral_0^ell V(x)|h(x)|^2dx
          +1/4 integral_0^ell integral_0^ell
             |h(x)-h(y)|^2/|x-y| dx dy
          -1/2 integral_0^ell integral_0^ell
             q_0(|x-y|)h(y)overline(h(x)) dx dy,
    V(x)=-gamma-log(2pi)-1/2 log(x(ell-x)).                (11)

To obtain (11), use L741(14)'s q=k-1/t-4cosh(t/2) in the
generator. The distributional derivative of the causal log kernel
is the limit of 1_(t>epsilon)/t+log(epsilon)delta_0. Pair it with
h, take the real part and symmetrize. The compensating diagonal is

    -log(epsilon)-1/2 [log(x/epsilon)_+
                              +log((ell-x)/epsilon)_+],

which tends to -1/2 log(x(ell-x)). The remaining symmetrized
difference is the double integral in (11). For smooth interior
functions the squared difference is O(|x-y|^2), and all limits follow
by dominated convergence. For polynomials the same bound holds on the
closed interval, and the endpoint layers have integrals
O(epsilon(1+|log(epsilon)|)); they also tend to zero. The generator's
scalar supplies -gamma-log(2pi). The bounded regular kernel supplies
the last term. Its omitted cosh part is exactly the zero pole
product, as in Section1. Polynomial zero extensions have Fourier
decay O(1/|t|), so their logarithmic form energies are finite; this
also agrees with L741's stated form domain. This does not turn them
into members of the smooth class N_neut.

For the orthonormal shifted Legendre polynomials p_n, the middle
quadratic term in (11) is diagonal with entries H_n=sum_(j=1)^n 1/j
(H_0=0). The following short polynomial calculation is included to
verify the factor and normalization in the numerical implementation;
it carries no novelty claim. The symmetric polynomial operator

    (L p)(x)=integral_0^ell (p(x)-p(y))/|x-y| dy

preserves polynomials of degree at most n, and direct division gives

    L(x^n)=2H_n x^n-sum_(j=1)^n ell^j x^(n-j)/j.

Its symmetry in L2 and orthogonality of p_n to lower degrees force
L p_n=2H_n p_n. The double-difference quadratic form is
<Lh,h>/2, proving the stated entries. The other matrices in the
script are direct quadratures of V, q_0, k_1 and J_d, with two
numerically projected moment rows.

The reproducible locator is
`python3 scripts/adjacent-neutral/interface-diagnostic-482.py`;
its full output is `scripts/adjacent-neutral/interface-diagnostic-482.json`.
At polynomial degree128 and quadrature order1024 it reports a
largest absolute relative eigenvalue about0.467919 and a smallest
L2 eigenvalue about0.065717 for the two matrices E+/-2X. These are
floating-point diagnostics only. There are no enclosures for
quadrature, rounding, exact moment projection, or the complementary
infinite-dimensional space, and no certified smooth witness. They
establish neither the upper target nor its failure. The proof of
(4)-(5) and the conditional implication (6) do not depend on them.

## Mathlib

Full matching Mathlib coverage of this exact neutral interface,
sharp compressed response-tail norm, and certificate implication
has not been checked. Availability is unknown; no formalization or
absence claim is made. The named Carleman theorem, Plancherel and
the already-cited digamma identities are supporting inputs, not a
formal proof of beta_1<1/2 or of RH.

