# Lemma 484: nonvanishing Haar error for a short real Euler-phase truncation

## Hypotheses

Let T tend to infinity through positive real values, and set

    y=T^(1/1000), X=T^(1/100)=y^10.

Let P_y be the finite set of primes p<=y. On the finite torus
G_y=(S^1)^(P_y), let mu_y be probability Haar measure and define

    F_y(z)=product_(p<=y) (1-p^(-1/2)z_p)
                            /(1-p^(-1/2)conjugate(z_p)),
    h_y(z)=Re F_y(z).

Every denominator is nonzero. An integer is y-smooth if all its
prime divisors are <=y, including the integer 1. Write v_p(a) for
the nonnegative integer prime valuation. Let V_T be the complex
linear span in L2(mu_y) of the characters

    product_(p<=y) z_p^(v_p(a)-v_p(b)),

where a,b are positive y-smooth integers with a,b<=X. No restriction
is imposed on the coefficients of the approximating element of V_T.
No actual-height distribution, zeta approximation, RH, residual
weight, or independence of actual prime phases is assumed.

## Conclusion

With lambda=log(11/10),

    liminf_(T->infinity) inf_(P in V_T) ||h_y-P||_L2(mu_y)
        >= (1/8) sqrt((10/11) lambda^11/11!) > 0.          (1)

More precisely, for all sufficiently large T, put

    J_y={p prime: y^(10/11)<p<=y},
    Q_y=product_(p in J_y)(1-1/p),
    w_p=1/(p-1),
    e_11(w)=sum_(S subset J_y, |S|=11) product_(p in S)w_p.

The finite-T bound is

    inf_(P in V_T) ||h_y-P||_2^2 >= Q_y e_11(w)/64,      (2)

and its right side tends to (10/11)lambda^11/(64*11!).
Empty subset sums have their usual value zero when |J_y|<11.

This is a specialization of standard compact-group Fourier theory
and Mertens' product theorem, with an explicit coefficient/support
calculation. The exact bound was not identified in the assessed
sources; no originality is claimed. It obstructs vanishing global
Haar L2 error for this specified rational-frequency rectangle only.
It neither bounds the actual-height signed correlation nor its
residual-weighted truncation error. In particular it establishes no
negative-mass estimate, Xi sign, or implication for RH. The lower
bound is small but fixed; no useful finite-height magnitude is claimed.
The separate critical audit in Section 5 found no correction necessary;
it does not constitute an independent audit of the imported sources.

## Proof

### 1. Imported inputs and applicability

Import the compact abelian group Fourier theorem: characters form
an orthonormal basis of complex L2 for probability Haar measure,
with Parseval and orthogonal projection onto any finite character
span. Use the finite-product tensor factorization. A precise source
is T. Tao, *245C, Notes 2: The Fourier transform*, 6 April 2009,
Exercise 15, Lemma 17, Theorem 21 (finite-torus proof case) and
Corollary 22
([primary notes](https://terrytao.wordpress.com/2009/04/06/the-fourier-transform/)).
For each T our torus is finite dimensional and its measure is the
product of the normalized circle measures. No theorem uniform in
dimension or limit of infinite tori is invoked.

Import the classical unconditional Mertens product asymptotic

    M(x):=product_(p<=x)(1-1/p)
         = e^(-gamma)/(log x) * (1+o(1)) as x->infinity. (3)

See T. Tao, *Mertens' theorems*, 11 December 2013, Theorem 1/(3)
and Section 1
([primary statement and proof](https://terrytao.wordpress.com/2013/12/11/mertens-theorems/)).
The saved source assessment inspected the strong o(1) logarithmic
form, which implies (3). A harmonic-prime estimate with only O(1)
error would not suffice here. These inputs are cited, not reproved;
the remaining work is the exact specialization below.

### 2. Exact coefficients and the real-part reflection

Fix a prime p, let r=p^(-1/2), and write z in S^1. The geometric
series for (1-r z^(-1))^(-1) converges absolutely uniformly on S^1
since 0<r<1. Multiplication by 1-rz gives

    (1-rz)/(1-r z^(-1))
      = -rz + (1-r^2) sum_(j>=0) r^j z^(-j).            (4)

Thus, using the convention q_p(z)=sum_k a_p(k)z^k,

    a_p(1)=-r,
    a_p(-j)=(1-r^2)r^j  for integers j>=0,
    a_p(k)=0            for integers k>=2.              (5)

These coefficients are real and their squared sum is

    r^2+(1-r^2)^2 sum_(j>=0)r^(2j)=1.                 (6)

For each fixed y there are finitely many factors in F_y. Their
absolutely uniformly convergent series may therefore be multiplied
and integrated termwise. For k=(k_p) in Z^(P_y), its Fourier
coefficient is exactly

    c_y(k)=product_(p<=y)a_p(k_p).                      (7)

No bound on the absolute coefficient sum uniform in y is required
or asserted. The finite product and (6) show that |c_y(k)|^2,
summed over all integer vectors k, is a probability law with
independent coordinates and marginal probabilities

    Pr(K_p=1)=1/p,
    Pr(K_p=-j)=(1-1/p)^2 p^(-j)  (j>=0),
    Pr(K_p>=2)=0.                                      (8)

All coefficients in (7) are real. Since h_y=(F_y+conjugate(F_y))/2,
its coefficient at k is

    d_y(k)=(c_y(k)+c_y(-k))/2.                         (9)

This reflection is retained; a lower bound for F_y alone would
not establish the asserted real-part lower bound.

### 3. A reflected-zero set outside the approximation space

Define the reduced numerator and denominator of k by

    A(k)=product_(p<=y)p^(max(k_p,0)),
    B(k)=product_(p<=y)p^(max(-k_p,0)).

Unique factorization shows that k is a character represented in
V_T if and only if A(k)<=X and B(k)<=X. Indeed any representation
k_p=v_p(a)-v_p(b) has a=g A(k), b=g B(k) with g=gcd(a,b),
and conversely A(k),B(k) themselves give a permitted representation
when both satisfy the bounds. Thus V_T is exactly the finite
character span of that rectangle, even if its defining generators
have repetitions.

Take y large enough that y^(10/11)>2. Let E_y be the set of all
integer vectors satisfying

    k_2=-2,
    #{p in J_y : k_p=1}=11,                            (10)

with every other coordinate unrestricted. On this entire set,
c_y(-k)=0, because its prime-2 coefficient has argument 2 and
a_2(2)=0. Equation (9) consequently gives d_y(k)=c_y(k)/2.
This conclusion holds also for vectors with c_y(k)=0.

The eleven distinct primes in (10) each exceed y^(10/11).
Their product exceeds y^10=X and divides A(k). Hence every
k in E_y is outside the Fourier support of V_T, regardless of
all other coordinates. Large negative coordinates cause no
cancellation in the reduced numerator, since different primes
cannot cancel each other's valuations.

By Parseval, the squared distance to a finite character span is
the sum of |d_y(k)|^2 over its complement. It follows that

    inf_(P in V_T)||h_y-P||_2^2
       >= sum_(k in E_y)|d_y(k)|^2
        = (1/4) sum_(k in E_y)|c_y(k)|^2.              (11)

This is an estimate for all complex approximants, not just a
particular truncation. No real-coefficient restriction was used.

### 4. Complete mass and the growing-prime limit

In the probability law (8),

    Pr(K_2=-2)=(1-1/2)^2*2^(-2)=1/16.                (12)

Prime 2 lies outside J_y. The indicators of K_p=1 for p in J_y
are independent Bernoulli variables with parameter 1/p. Therefore

    Pr(#{p in J_y: K_p=1}=11)
       = product_(p in J_y)(1-1/p)
           * sum_(S subset J_y, |S|=11)
                    product_(p in S) ((1/p)/(1-1/p))
       = Q_y e_11(w).                                 (13)

The unrestricted complement coordinates have total mass one,
by (6), rather than being fixed at zero. Equations (11)--(13)
prove (2), including the factor 1/64.

Both y and y^(10/11) tend to infinity. By (3),

    Q_y=M(y)/M(y^(10/11)) -> 10/11.                    (14)

For 0<=u<=1/2, the convergent elementary series give

    |u/(1-u)+log(1-u)| <= 2u^2.

Since sum_(p>y^(10/11))p^(-2) is bounded by the integer tail
sum_(n>y^(10/11))n^(-2), which tends to zero, (14) yields

    W_y:=sum_(p in J_y)w_p
         = -log Q_y+o(1) -> log(11/10)=lambda.          (15)

Also max_(p in J_y) w_p tends to zero (take maximum zero
for an empty block). Hence

    sum_(p in J_y)w_p^2 <= (max w_p)W_y -> 0.          (16)

For any finite nonnegative list w and integer m>=2, expansion
of W^m into ordered m-tuples shows

    0 <= W^m-m! e_m(w)
       <= binom(m,2) (sum_p w_p^2) W^(m-2).           (17)

Indeed the difference is precisely the contribution of tuples
with a repeated index. For each pair of positions, the sum over
tuples agreeing at those positions is (sum w_p^2)W^(m-2);
the union bound proves (17). This finite identity needs no
Poisson limit theorem or infinite interchange.

Applying (17) with m=11 and using (15)--(16),

    e_11(w) -> lambda^11/11!.                          (18)

Together (2), (14), (18) give the positive limiting lower bound
for the squared distance. Taking square roots gives (1).
All coefficient manipulations above were for a fixed finite
prime set; only the scalar products and sums in (14)--(18)
pass to a growing-prime limit with the displayed justification.

### 5. Separate critical application audit, 30 October 2026

The first critical audit replayed (4)--(18) under the unchanged
SPECIALIZE assessment. No hypothesis, constant or conclusion needed
repair. This verifies the local specialization, not a new obstruction
beyond the one already proved above or a new literature result.

**Coefficients and real reflection.** Independently collecting the
coefficient of z^(-j) in the geometric expansion gives
r^j-r^(j+2), including j=0; the only remaining term is -rz.
Also the numerator and denominator are conjugates on the circle,
so |q_p|=1, agreeing with the squared-coefficient total in (6).
Finite tensoring therefore gives both the exact signed coefficients
and a probability law for their squares. Conjugating a Fourier
series sends its coefficient at -k to its complex conjugate; here
all coefficients are real, so (9) has precisely the stated form.
On k_2=-2 the reflected coefficient contains a_2(2)=0. Hence there
is no cancellation on E_y, and the squared real-part coefficient
is exactly |c_y(k)|^2/4 there.

**Support and full mass.** Reduction of a/b subtracts the minimum
valuation at each prime and leaves exactly A(k)/B(k). A common
factor cannot decrease either reduced integer, proving both
directions of the support test. On E_y the eleven distinct positive
block valuations alone give A(k)>y^10. Neither prime 2 nor any
negative coordinate can reduce this integer. The rectangle is finite
and its distinct characters are orthonormal, so complex orthogonal
projection gives (11) for arbitrary complex approximants. All sums
of squared coefficients are nonnegative: Tonelli on the finitely
many countable coordinate sets justifies summing every unrestricted
coordinate to one. In particular there is no extra product of
zero-coordinate probabilities. For y^(10/11)>2 the prime-2 event
is independent of the block event; its mass is exactly 1/16.
The block specifies exactly eleven successes, so its remaining
coordinates contribute failure probabilities 1-1/p, not restrictions
to k_p=0. This gives Q_y e_11(w) and the factor 1/64 in (2).

**Limit and quantifiers.** Writing alpha=10/11, strong Mertens gives
M(y)=e^(-gamma)(1+o(1))/log y and independently
M(y^alpha)=e^(-gamma)(1+o(1))/(alpha log y), for real y tending
to infinity. Their exact quotient tends to alpha, including cutoffs
at primes. The difference W_y+log Q_y is nonnegative and at most
2 sum_(p>y^alpha)p^(-2), hence tends to zero. Consequently W_y
tends to lambda, is bounded, and sum w_p^2 tends to zero because
max w_p tends to zero. In (17) each repeated ordered eleven-tuple
has an equal pair of positions; summing over the 55 choices gives
an upper bound 55 (sum w_p^2) W_y^9, which tends to zero.
Thus (18) and the exact positive limit on the right of (2) follow.
If D_T denotes the nonnegative infimum distance, (2) gives
D_T>=sqrt(Q_y e_11(w)/64) at every sufficiently large real T.
Taking liminf proves (1) even though the finite torus changes with T;
no limiting Hilbert space or dimension-uniform theorem is needed.

This audit assumes only the cited finite-torus Fourier and strong
Mertens theorems. It verifies no actual-height sampling, independence
of actual prime phases, residual-weighted replacement or Xi sign.
There is no numerical experiment or finite-height certificate here.

## Mathlib

Full matching coverage is not checked. Supporting Fourier,
Haar-measure, geometric-series, Hilbert-projection and Mertens
coverage in Mathlib is also not checked in this step; absence
is not asserted. The cited classical analytic inputs, with the
specific finite-torus and strong-Mertens hypotheses above, suffice
for this informal proof. No formal certificate is claimed.
