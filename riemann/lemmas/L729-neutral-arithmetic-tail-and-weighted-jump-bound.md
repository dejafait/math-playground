# Lemma 729: neutral arithmetic tail and weighted jump bound

## Hypotheses

Let H=L²((1,∞),dy/y²), with inner product
⟨v,w⟩=∫₁^∞v(y)conj(w(y))dy/y², linear in the first entry.
For integers m≥1 define

    rho_m(y)=floor(y/m)-floor(y)/m.

For m≥2 put a_m=(m-1)/(2m), f_m=rho_m+a_m, using the same floor
formula also on [0,1), and set

    K_m(t)=∫_t^∞ f_m(y)dy/y²  (t>0),
    T_m(n)=sum_(j≥1) K_m(jn)  (integer n≥1).

Take integers N,K≥2, L=log N, the ordinary Möbius function mu, and
the von Mangoldt function Lambda (Lambda(1)=0). Define

    g_N=sum_(n≤N) mu(n)(1-log(n)/L)rho_n,
    u=sum_(m=2)^K c_m rho_m,    c_m complex,
    A(u)=sum c_m a_m,           B(u)=sum c_m T_m(1),
    K_u(t)=sum c_m K_m(t),      T_u(n)=sum c_m T_m(n).

Assume A(u)=B(u)=0. Define the conjugate-linear functional

    Q(u)=-sum_(k≥1) Lambda(k)conj(K_u(k)).

The convergence of the defining series is proved below. No RH, zero-free
region, simplicity, derivative moment, or representer assumption is made.

## Conclusion

For all such N,K,u,

    |L⟨1-g_N,u⟩-Q(u)|
      ≤ zeta(2)/(4N) sum_(m=2)^K m|c_m|,

    sum_(m=2)^K m|c_m|
      ≤ 3 sqrt(2) zeta(3/2) K^(5/2) ||u||_H.

In particular their combination is a uniform bound with constant
3 sqrt(2) zeta(2) zeta(3/2)/4 multiplying K^(5/2)/N times ||u||.
The exact error identity is

    L⟨1-g_N,u⟩-Q(u)
      =sum_(n>N) mu(n)(L-log n)conj(T_u(n)).

All infinite series in this identity converge absolutely. These are a
cited reproduction of the arithmetic part of bramble_trace, *Fixed and
growing neutral gradients of the anchored Selberg–Möbius approximant*,
rStation paper 18, v3, 22 October 2026, equations (4), (6)–(8), (36)–(40):
https://rstation.ai/problems/riemann_hypothesis/papers/18 .
The current URL was inspected on 2026-11-03 and labeled v3; the /v3 URL
was inaccessible. The source is an unreviewed manuscript. The complete
replay below justifies these estimates independently, retaining the
complex convention and first jump. It imports no other manuscript claim.

## Proof

### Periodic primitive and absolute tails

The functions rho_m, f_m are m-periodic: increasing y by m adds one
to floor(y/m) and m to floor(y). On [j,j+1), 0≤j<m,

    f_m(y)=(m-1-2j)/(2m).

Thus F_m(t)=∫₀^t f_m(y)dy is piecewise linear, with

    F_m(j)=j(m-j)/(2m),    0≤j≤m.

In particular F_m(m)=0, so F_m is periodic. Its maximum is attained
at an integer nearest m/2, and its minimum is zero. Consequently

    0≤F_m(t)≤P_m=floor(m²/4)/(2m)≤m/8,    t≥0.

Since f_m is bounded, K_m(t) exists absolutely for each t>0.
Integration by parts on [t,R], followed by R→∞, gives

    K_m(t)=-F_m(t)/t²+2∫_t^∞ F_m(y)dy/y³.

Each of the two nonnegative quantities being subtracted is at most
P_m/t². Hence, without an additional factor two,

    |K_m(t)|≤P_m/t²,
    |T_m(n)|≤P_m zeta(2)/n².                         (1)

All endpoints are allowed; F_m is continuous at integers and absolutely
continuous on compact intervals. Let S=sum_(m=2)^K P_m|c_m|. Finite
linearity gives |K_u(t)|≤S/t² and |T_u(n)|≤S zeta(2)/n².
Since 0≤Lambda(k)≤log k for k≥2, Q(u) is absolutely convergent.

For r=0,1 the double divisor series is absolutely summable, because

    sum_(n,j≥1) |mu(n)|(log n)^r |K_u(jn)|
      ≤ S zeta(2) sum_(n≥1) (log n)^r/n² <∞,

where (log n)^0=1. Thus regrouping by k=jn is legitimate. The elementary
Möbius inversion identities are

    sum_(d|k)mu(d)=1_(k=1),
    sum_(d|k)mu(d)log d=-Lambda(k).

For clarity, the first follows by expanding the product over distinct
prime factors. For k>1 write log d as the sum of log p over primes
dividing the squarefree d. For each p|k the resulting signed sum is
-log p times the product of (1-1) over the other distinct primes.
It is -log p exactly when k is a power of p and zero otherwise;
at k=1 the logarithmic sum is zero. This proves the second identity
without an analytic input. Regrouping therefore gives

    sum_(n≥1)mu(n)T_u(n)=K_u(1),
    sum_(n≥1)mu(n)log n T_u(n)
      =-sum_(k≥1)Lambda(k)K_u(k).                    (2)

### Complete Gram identity and neutral cancellation

We replay the complete identity rather than omit its physical tail.
For integers n≥1 and Y≥1, finite summation yields

    ∫₁^Y floor(y/n) f_m(y)dy/y²
      =sum_(j≤Y/n) K_m(jn)-floor(Y/n)K_m(Y).

Indeed floor(y/n)=sum_(j≥1)1_(y≥jn); within the finite integral
there are only finitely many terms. The last term tends to zero as
Y→∞ by (1), and the series tends absolutely to T_m(n). The separate
integrals here need not converge absolutely after Y→∞; their limits
exist by this displayed identity. Taking the difference with 1/n times
the n=1 identity, whose integrand difference is bounded, proves

    ∫₁^∞ rho_n(y)f_m(y)dy/y²=T_m(n)-T_m(1)/n.

Also

    ⟨rho_n,1⟩=-log n/n.                             (3)

One elementary verification of (3) uses y=1/x and
rho_n(1/x)={1/x}/n-{1/(nx)}. For epsilon>0 the integrals of the two
floor terms on x∈[epsilon,1] are

    ∫_epsilon^1 floor(1/(nx))dx
      =H_floor(1/(n epsilon))/n-epsilon floor(1/(n epsilon)),
    (1/n)∫_epsilon^1 floor(1/x)dx
      =H_floor(1/epsilon)/n-(epsilon/n)floor(1/epsilon).

Their difference tends to -log n/n, since H_M=log M+gamma+o(1)
and the epsilon terms have difference tending to zero. This includes
n=1, when both sides are zero. The difference integrand is bounded,
so this limit is its ordinary integral on (0,1).

Since rho_m=f_m-a_m, (3) gives the full Gram identity

    ⟨rho_n,rho_m⟩=a_m log(n)/n+T_m(n)-T_m(1)/n.       (4)

In the complex convention, multiplying (4) by conj(c_m) and summing
therefore gives

    ⟨rho_n,u⟩=conj(A(u))log(n)/n
                 +conj(T_u(n))-conj(B(u))/n
              =conj(T_u(n)).

Moreover ∫₁^∞rho_m(y)dy/y²=K_m(1)-a_m, directly from the definition
of K_m. Thus ⟨1,u⟩=conj(K_u(1)) when A(u)=0. Conjugate (2), using
real mu and Lambda, and substitute these pairings. The result is

    sum_(n≥1)mu(n)conj(T_u(n))=⟨1,u⟩,
    sum_(n≥1)mu(n)log n conj(T_u(n))=Q(u).

Subtracting the finite sum for Lg_N gives the asserted exact error
identity. In particular, no moment asymptotic and no identification
of Q with an H-representer has entered the proof. The n=N coefficient
is zero, as required by the triangular taper.

### Uniform finite-N error

By (1) and |mu(n)|≤1,

    |L⟨1-g_N,u⟩-Q(u)|
      ≤ zeta(2) S sum_(n>N) log(n/N)/n².

For each n>N and x∈[n-1,n], x>0 and
log((x+1)/N)/x²≥log(n/N)/n². Hence, for every integer N≥2,

    sum_(n>N)log(n/N)/n²
      ≤∫_N^∞ log((x+1)/N)dx/x²
      ≤∫_N^∞ (log(x/N)+1/x)dx/x²
      =1/N+1/(2N²)≤2/N.

This comparison does not require log(x/N)/x² to be decreasing at N.
Using S≤(1/8)sum m|c_m| proves the first claimed inequality with
constant zeta(2)/4, uniformly for all N≥2 and every K≥2.

### Weighted jump inversion, including j=1

For integer j≥1 let u_j be the constant value of u on [j,j+1), and
put u_0=0. This matches its actual floor-formula extension on [0,1).
Set C=sum_(m=2)^K c_m/m and extend c_m=0 outside 2≤m≤K. Then

    Delta u_j=u_j-u_(j-1)=sum_(m|j,m≥2)c_m-C,    j≥1.

In particular Delta u_1=-C; it must not be discarded. The finite
Möbius inversion identity applied at m≥2 gives

    sum_(d|m)mu(d)Delta u_(m/d)
      =c_m-C sum_(d|m)mu(d)=c_m.                    (5)

Indeed, applying the first divisor identity twice recovers the
coefficient sequence (with coefficient at 1 equal to zero). The
constant term vanishes because m>1. Neither neutrality assumption
is needed for this coefficient estimate.

For every integer M≥1, the triangle inequality and u_0=0 imply

    sum_(j≤M)j|Delta u_j|
      ≤sum_(j≤M)j|u_j|+sum_(i=1)^(M-1)(i+1)|u_i|
      ≤3 sum_(j≤M)j|u_j|.

The Hilbert norm, including all cells, is

    ||u||²=sum_(j≥1)|u_j|²/(j(j+1)).

Weighted Cauchy–Schwarz, j+1≤2j and M terms give

    sum_(j≤M)j|u_j|
      ≤||u|| (sum_(j≤M)j³(j+1))^(1/2)
      ≤sqrt(2) M^(5/2)||u||.

From (5), retaining the j=1 terms even though m=1 is excluded,

    sum_(m=2)^K m|c_m|
      ≤sum_(d≤K)d sum_(j≤floor(K/d))j|Delta u_j|
      ≤3 sqrt(2)||u|| sum_(d≤K)d floor(K/d)^(5/2)
      ≤3 sqrt(2)K^(5/2)||u|| sum_(d≤K)d^(-3/2)
      ≤3 sqrt(2)zeta(3/2)K^(5/2)||u||.

Thus the divisor sum is summable, rather than harmonic. This proves
the second claimed bound, including K=2 and complex u, and completes
the audit. No numerical computation is used. ∎

The result validates known-source mathematics locally; it is not a new
estimate beyond that source. For growing K it proves a vanishing
neutral-observation error when K^(5/2)/N→0. It supplies no conclusion
at K comparable to N, no full-residual norm bound, no density statement,
no prime-kernel representer, no sign theorem and no dyadic contraction.
In particular no hypothesis equivalent to RH has been established.

## Mathlib

Full matching theorem: not checked; availability is unknown. The finite
Möbius identities, integration by parts and Cauchy–Schwarz are standard
supporting results, but no exact Mathlib declaration has been verified
in this step. No absence claim is made. Supporting documentation index:
https://leanprover-community.github.io/mathlib4_docs/ .
