# Lemma 464: audited finite local factor comparison and Xi coefficient tail

## Hypotheses

Let Ξ be the actual completion of L018, with the locally uniform paired
product of L024, zero localization of L026 and infinitude of L027.
Multiplicities are retained. Write

    Ξ(t+iy)Ξ(t−iy) = Σ_(p≥0) D_p(Ξ;t)y^(2p),

for real t; y is a complex variable. All logarithms below are natural.
The only additional zero-count input is E. C. Titchmarsh, revised by
D. R. Heath-Brown, *The Theory of the Riemann Zeta-Function*, second
edition (Oxford, 1986), Theorem 9.2, equation (9.2.1), printed p. 211:
N(T+1)−N(T)=O(log T), counting nontrivial zeros with multiplicity.
The primary statement and Jensen proof were inspected in the approved
source assessment; see the [book scan](https://sites.math.rutgers.edu/~zeilberg/EM18/TitchmarshZeta.pdf#page=110).

For the abstract comparison, let

    G(x)=Π_i(1+u_i x+v_i x²)=Σ_(j≥0) g_j x^j,
    u_i>0, 0≤2v_i≤u_i², U=Σ_i u_i<∞,

with infinitely many factors. Let B be a monic real polynomial of
degree M≥1, every complex root having modulus at most R_0≥0.

## Conclusion

Write coeff_p for the coefficient of x^p. For every integer p≥M,
with q=p−M,

    |coeff_p(BG)−g_q|
      ≤g_q { (1+R_0 U/(q+1))^M−1 }.                 (1)

Every g_j is strictly positive. Consequently coeff_p(BG)>0 whenever
p≥M and p−M+1≥2R_0 M U. If M=0, take B=1 and every coefficient
is strictly positive without a threshold. Repeated, nonreal and zero
roots of B are allowed.

For actual Ξ there is one absolute C>0 such that

    D_p(Ξ;t)>0  for all real t≥2 and all integers p≥C log²(t+2). (2)

The constant is existential; no numerical value or effective bounded-
height overlap is asserted. Central zeros of any multiplicity are
included. This statement uses no fixed zero-free half-plane beyond
the unconditional classical strip, and no simplicity assumption.

This reproduces, rather than strengthens, bramble_trace, *Generalized
Laguerre positivity at growing orders*, [paper 41](https://rstation.ai/problems/riemann_hypothesis/papers/41),
displayed v4, 24 October 2026, 07:18 UTC, Section 4.3, (18c)–(18h).
The separate audit is justified because that product estimate was a
previously unaudited component of the source imported in L463.
It does not audit Sections 4.2 or 4.5, the external zero-free premise,
or the full logarithmic-order theorem. No new mathematical discovery,
initial-sign theorem, mixed positivity, or RH resolution is claimed.

## Proof

### 1. Infinite positive products and coefficient comparison

Since Σ_i u_i²≤U² and v_i≤u_i²/2, on |x|≤R we have

    Σ_i |u_i x+v_i x²| ≤ R U + R² U²/2 <∞.

The finite products G_N therefore converge locally uniformly to an
entire G, with G(0)=1. Cauchy's formula gives convergence of every
coefficient and of the derivatives. All finite-product coefficients
are nonnegative. For any fixed j≥1, choose j distinct factors; the
product of their positive linear coefficients is a positive summand
in coefficient j of every subsequent product. Thus g_j>0, and g_0=1.
This argument treats repeated factors as distinct occurrences.

For f_i=1+u_i x+v_i x², coefficientwise comparison gives

    f_i'=u_i+2v_i x ≼ u_i+u_i²x+u_i v_i x²=u_i f_i.

Multiplying by the other nonnegative factors and summing over i≤N
yields G_N'≼U_N G_N, where U_N=Σ_(i≤N)u_i. Taking each coefficient
limit, using U_N→U, proves

    j g_j≤U g_(j−1)  (j≥1).

For q≥0 and k≥1, iterate upward, without any division by a zero:

    g_(q+k)≤g_q U^k/((q+1)(q+2)…(q+k))
            ≤g_q (U/(q+1))^k.                    (3)

Write B=Σ_(k=0)^M b_(M−k)x^(M−k), with b_M=1. The elementary
symmetric formula for its roots, including multiplicities and zero
roots, gives |b_(M−k)|≤binom(M,k)R_0^k. The coefficient in question
is the finite sum Σ_(k=0)^M b_(M−k)g_(q+k). Subtract its k=0 term,
use (3), and sum the binomial expansion to obtain (1).

If q+1≥2R_0 M U, then MR_0 U/(q+1)≤1/2, including the case
R_0=0. Since (1+s)^M≤exp(Ms) for s≥0, the relative remainder is
at most exp(1/2)−1<1. In fact the coefficient is at least
(2−exp(1/2))g_q>0. This proves strictness even at equality in the
threshold. For M=0 the coefficient is g_p>0 directly.

### 2. Exact zero factors and a positive normalization

By L018 and L026, choose the positive-real-part representatives of
the ± zero pairs. They are real γ>4 or occur as γ±id with γ>4 and
0<d<1/2; each conjugate pair has a common multiplicity. Exhaust
L024's product by finite sets closed under conjugation. All following
factor identities are polynomial identities in x=y², for complex y.

For a real representative γ, the two factors in the product of the
shifted Ξ functions give exactly

    (1−(t+iy)²/γ²)(1−(t−iy)²/γ²)
      = F_(γ−t)(x) F_(γ+t)(x)/γ^4,
    F_a(x)=x+a².

For a conjugate pair α=γ+id and conjugate(α), group both paired
factors. Their contribution is

    Q_(γ−t,d)(x) Q_(γ+t,d)(x)/(γ²+d²)^4,
    Q_(a,d)(x)=(x+(a+id)²)(x+(a−id)²)
              =x²+2(a²−d²)x+(a²+d²)².            (4)

Both identities follow by first splitting each paired factor into
its two linear zero factors. The denominators in (4) are
α^4 conjugate(α)^4=|α|^8=(γ²+d²)^4. Thus neither a denominator
nor a square-root normalization has been omitted.

Fix t≥2. Put in B_t only the F_(γ−t) or Q_(γ−t,d) factors for
which |γ−t|<2, with multiplicity. All γ+t factors are far, since
γ+t>6. All other γ−t factors are far as well, including equality
|γ−t|=2. There are finitely many near factors, by discreteness or
the local count below, so B_t is a monic polynomial of some degree M.
Its real-factor roots have modulus a²<4. The two roots of Q_(a,d)
are −(a±id)², whose moduli are a²+d²<17/4. Hence R_0=17/4 is a
common bound. A zero at t gives F_0(x)=x in B_t; its multiplicity
merely repeats this factor.

Divide each far factor by its strictly positive constant term and
let G_t be their product. For real factors u=1/a², v=0. For (4),

    u=2(a²−d²)/(a²+d²)²,  v=1/(a²+d²)²,
    u/sqrt(v)=2(a²−d²)/(a²+d²)≥30/17>sqrt(2),

because a²≥4 and d²<1/4. Thus u>0 and 2v≤u². Also u≤2/a²
for a conjugate-pair factor; for a real factor u=1/a². Section 3
proves Σu<∞. Infinitely many far factors remain by L027, since
only finitely many factors entered B_t.

It remains to prove that the removed scalar converges to a strictly
positive number, including when B_t(0)=0. For a sufficiently large
finite exhaustion containing all near indices, define C_(t,N) as
Ξ(0)² times the positive constant terms of its far factors, divided
by the product of the denominators γ^4 and (γ²+d²)^4 above. Every
factor in this definition is positive. For an entirely far real
index the resulting scalar is

    c_(γ,t)=(1−t²/γ²)².

For an entirely far conjugate-pair index it is

    c_(α,t)=|1−t²/α²|^4.

For the finitely many near indices, only the γ+t constant is used:
the scalar is (γ+t)²/γ^4 for a real index, and
((γ+t)²+d²)²/(γ²+d²)^4 for a conjugate pair. These expressions
stay positive even at γ=t. In particular no scalar uses Ξ(t)⁻²
or divides by a near factor's constant term.

For γ sufficiently large relative to the fixed t, both entirely
far scalars satisfy |c−1|=O_t(γ⁻²), uniformly in 0≤d<1/2.
For example, |t²/α²|≤t²/γ², and expansion of |1−w|^4 at w=0
gives the asserted bound. L024's reciprocal-square summability
implies summability of γ⁻², with multiplicity: since γ>4,
|α|²=γ²+d²≤(65/64)γ². Thus the scalar deviations are absolutely
summable. Eventually |c−1|≤1/2, so |log c|≤2|c−1| for positive
c. Their scalar product therefore converges to a finite positive
limit C_t, after including the finitely many earlier positive factors.
Only fixed-t convergence is required here; no uniform lower bound
on C_t is used in the sign argument.

For every sufficiently large exhaustion, the exact identity is

    Ξ_N(t+iy)Ξ_N(t−iy)=C_(t,N) B_t(y²) G_(t,N)(y²).

L024 supplies locally uniform convergence of the left side, while
Section 1 and the bound on Σu supply it for the far product. Hence

    Ξ(t+iy)Ξ(t−iy)=C_t B_t(y²)G_t(y²), C_t>0.      (5)

The even entire functions of y also define entire functions of x:
on |x|≤R choose either square root with |y|≤sqrt(R); the polynomials
and their limits are independent of that choice. This gives local
uniform convergence in x and coefficient convergence by Cauchy's
formula. In particular D_p(Ξ;t)=C_t coeff_p(B_tG_t). No passage
through a logarithm at a zero, a modulus square at complex y, or
a normalization by Ξ(t) is involved.

### 3. Uniform shells, multiplicities and one absolute threshold

Let Γ be the multiset of positive real parts of all Ξ zeros, including
both γ+id and γ−id separately and every multiplicity. By L018 these
are exactly the positive ordinates counted by the classical N(T).
Titchmarsh's local count yields an absolute A>0 such that

    # {γ in Γ : v≤γ≤v+1} ≤ A log(v+2), v≥0.       (6)

To include the lower endpoint for large v, bound this count by
N(v+1)−N(v−1), and apply the quoted theorem to the two consecutive
unit increments. On the remaining bounded v-range the total number
of zeros is finite; enlarge A, using log(v+2)≥log 2. Thus (6)
includes all endpoints and multiplicities, not merely generic v.

Put L=log(t+2)≥log 4. Degree M counts exactly Γ in (t−2,t+2):
a nonreal pair contributes degree two and two elements of Γ, while
a real zero contributes degree one. Cover the window by four closed
unit intervals starting at t−2,t−1,t,t+1. By (6),

    M≤4A log(t+3)≤8A L.                          (7)

Counting endpoints more than once only enlarges this upper bound.
The coefficient u of each far conjugate pair is at most 2/a²,
and that pair accounts for two elements of Γ. Therefore

    U_t ≤ Σ_(γ in Γ, |γ−t|≥2) 1/(γ−t)²
           + Σ_(γ in Γ) 1/(γ+t)².                (8)

For each integer k≥2, the shell k≤|γ−t|<k+1 is contained in
two intervals of length at most one, after intersecting with γ>0.
Using closed intervals in (6), its count is at most
2A log(t+k+3). Its reciprocal-square weight is at most k⁻².
The shell k≤γ+t<k+1 meets γ>0 in at most one interval of length
one, with count at most A log(k+3). Here γ+t>6, so allowing all
k≥2 only enlarges the sum. These statements also cover truncated
intervals at γ=0 by using [0,1].

Define the finite absolute constants

    S_0=Σ_(k≥2) k⁻²,
    S_1=Σ_(k≥2) log(k+3)/k².

Their convergence follows from the integral test. Since
t+k+3≤(t+2)(k+3), (8) now gives

    U_t≤2A S_0 L+3A S_1≤bL,
    b=A(2S_0+3S_1/log 4).                        (9)

This proves both fixed-center summability and uniformity for every
t≥2, with no unproved zero-density or gap input. Set a=8A and

    C=a/log 4+2(17/4)ab+1.

It is one absolute constant. For p≥C L², equations (7)–(9) imply

    p≥M+2(17/4)M U_t,

so p≥M and p−M+1≥2(17/4)M U_t. If M≥1, apply (1) with
R_0=17/4 and multiply by the positive C_t in (5). If M=0,
every coefficient of G_t is positive already. This proves (2).
All statements are simultaneous over the specified t and p because
A, a, b, R_0 and C are independent of both. ∎

The audit passes the exact approved product comparison, without
changing the source's conclusion. The bound leaves an initial segment
of order log²(t+2) unchecked and supplies no compensation for possible
negative low coefficients. Its growth is weaker than L463's imported
logarithmic threshold, but its proof does not require that import's
external zero-free premise or saddle estimates. The older finite-sign
and count/gap countermodels are not contradicted.

## Mathlib

Full matching coverage and supporting formalizations of the local
zero count, product regrouping and coefficient comparison have not
been checked. No absence assertion, Lean verification or computational
certificate is claimed. The proof above is an informal reproduction
using the named classical input and the stated canonical results.
