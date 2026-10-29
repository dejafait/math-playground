# Lemma 465: growing-radius analytic audit for the actual Xi function

## Hypotheses

Use the actual entire completion Ξ(z)=ξ(1/2+iz) of L018. Fix
c_0>1/2. Let t tend to positive infinity, put ell=log(t/(2π)) and
R=ell², and let n=2p be a positive even integer satisfying

    c_0 ≤ c=n/ell ≤ R.

All constants below are independent of t, n and c in this range;
the onset and constants may depend on the fixed c_0 and on the
fixed arc angle chosen below. No RH, simplicity, central nonvanishing
or additional zero-free half-plane is assumed.

The classical analytic inputs, with their exact scope, are:

- Sector Stirling and digamma asymptotics, [NIST DLMF 5.11.1,
  5.11.2 and 5.11(ii)](https://dlmf.nist.gov/5.11), in closed sectors
  avoiding the negative real axis. Analytic remainders are
  differentiated only using Cauchy's estimates on larger disks.
- The absolutely convergent zeta and differentiated Dirichlet
  series and Euler product, [DLMF 25.2.1, 25.2.6 and
  25.2.11](https://dlmf.nist.gov/25.2), for real part greater than one.
  For its reciprocal use Titchmarsh, revised by Heath-Brown,
  *The Theory of the Riemann Zeta-Function*, second edition,
  Oxford (1986), (1.1.4), printed p. 3: the absolutely convergent
  Möbius series in that same domain.
- Titchmarsh, Theorem 3.5 and proof, printed pp. 49–50:
  ζ(σ+iv)=O_A(log |v|), uniformly for
  1−A/log|v|≤σ≤2, |v| sufficiently large, with fixed A>0.
  We need only 1≤σ≤2, with negative heights supplied by conjugation.
- Classical strip convexity (the Phragmén–Lindelöf principle),
  Titchmarsh, Section 5.1, (5.1.1)–(5.1.5), printed pp. 95–96.
  In particular, for each fixed ε>0,
  |ζ(σ+iv)|≤C_ε |v|^((1−σ)/2+ε) uniformly on 1/2≤σ≤1
  at large |v|. The uniform-strip specialization is explained below.
  The [primary book scan](https://sites.math.rutgers.edu/~zeilberg/EM18/TitchmarshZeta.pdf)
  supplies all three cited Titchmarsh passages.

This audits the A=2 specialization of bramble_trace,
*Generalized Laguerre positivity at growing orders*,
[paper 41](https://rstation.ai/problems/riemann_hypothesis/papers/41),
displayed v4, 24 October 2026 07:18 UTC, Sections 3–4.2,
(8)–(18b). The source already states the result. The independent
reproduction is needed to check its growing-domain uniformity;
it is not a novelty claim. The approved source-scope assessment
predates this audit. Sections 4.4–4.5 are not proved here.

## Conclusion

The source's growing-disk gamma, amplitude, complementary-arc and
Xi-gauge estimates pass for the stated range. More explicitly,
choose 0<β<π/2 such that c_0 cosβ>1/2 and set

    d=1−cosβ,
    η=min(c_0−1/2, c_0 d)>0.

Define b and the local analytic Hardy function Z as in the proof,
with b(t)>0 and Ξ(z)=−b(z)Z(z). Define D_p(f;t) as the coefficient
of y^(2p) in f(t+iy)f(t−iy). Then, uniformly in the stated range,

    D_p(Z;t) = 2 ell^n/n! |ζ(1/2+c+it)|² (1+e_Z),
    D_p(Ξ;t) = 2 b(t)² ell^n/n! |ζ(1/2+c+it)|² (1+e_Ξ),

where both real relative errors satisfy

    |e_Z|+|e_Ξ| ≤ C_(c_0,β) [ n^(−1/2)
                       + sqrt(n) exp(−η ell/2)
                       + R²/t + R²/t² ].                 (1)

Consequently these errors are O_(c_0)(ell^(−1/2)); both coefficients
are strictly positive beyond one common existential height onset
throughout c_0 ell≤2p≤ell³. Choosing β as a fixed function of c_0
absorbs its dependence. No numerical onset is evaluated.

This supplies no signs below c_0 ell, no endpoint c_0=1/2 result,
no effective bounded-height coverage, and no RH or mixed positivity.
The arbitrary-order overlap with L464 is a separate assembly, not
a conclusion of this lemma. L464 and L463 are context, not proof inputs.

## Proof

### 1. Domains, logarithms and the exact identity

Take t sufficiently large that ell≥1 and 4R<t/8. Write
s=1/2+it and γ(w)=π^(−w/2)Γ(w/2). For all |y|≤4R the points
s±y and 1−s±y have imaginary part of magnitude comparable to t.
Their halves lie in a fixed sector |arg w|≤3π/4 and have modulus
comparable to t. No gamma pole, gamma zero or zeta pole occurs on
these disks. Slightly larger sectors still avoid the negative real
axis. Hence analytic logarithms g(w)=log γ(w) exist on the upper
and lower disks; choose them by the analytic log-Gamma branch in
that cut plane, so g(conj w)=conj g(w).

For |z−t|≤4R put a(z)=1/2+iz and a_*(z)=1/2−iz and define

    b(z)=(z²+1/4)/2 · exp((g(a(z))+g(a_*(z)))/2).

The polynomial factor has no zero on this disk. On its real
interval, b is positive and equals

    (z²+1/4)/2 · π^(−1/4)|Γ(1/4+iz/2)|.

Thus b has no zero anywhere on the disk and has an analytic
logarithm k, real on the real interval. Define Z(z)=−Ξ(z)/b(z).
This is holomorphic even when Ξ(t)=0. The completion formula gives

    Z(z)=exp((g(a(z))−g(a_*(z)))/2) ζ(a(z)).       (2)

L018 initially gives that formula where Re a(z)>0. Both sides
are holomorphic on the full disk, so the identity theorem extends
it there. The same argument extends the functional equation
γ(w)ζ(w)=γ(1−w)ζ(1−w) to the shifted disks: it follows from
ξ(w)=ξ(1−w) by cancelling w(w−1), which is nonzero here.

Set

    h(y)= [g(s+y)+g(1−s+y)−g(s−y)−g(1−s−y)]/2,
    P(y)=Z(t+iy)Z(t−iy),
    F(y)=ζ(s+y)ζ(1−s+y).

Multiplying (2) at t±iy and replacing ζ(s−y) by
γ(1−s+y)ζ(1−s+y)/γ(s−y) gives, exactly,

    P(y)=exp(h(y)) F(y),   P(−y)=P(y).             (3)

Thus exp(h) is the source's H_y^(−1), with its anchored logarithm
h(0)=0. No square-root sign is inferred from its square alone.
For real y, the paired g-values are conjugate, so h(y) is real.
All the identities hold on a neighborhood of |y|≤2R, sufficient
for every later contour and straight segment.

### 2. Uniform gamma remainder and its derivative

Sector digamma expansion gives, uniformly on these domains,

    g'(w)= 1/2 Log(w/(2π)) − 1/(2w) + O(t^(−2)).  (4)

Here Log is the principal logarithm, compatible with the chosen
upper and lower analytic domains. To differentiate the analytic
remainder, use circles of radius κt for a small absolute κ>0
about w, within a slightly larger fixed sector. Its supremum is
O(t^(−2)), so Cauchy gives derivative O(t^(−3)). Consequently

    g''(w)=1/(2w)+1/(2w²)+O(t^(−3)).              (5)

This uses sector expansions, not bounded-real-part vertical Stirling.

Direct differentiation of h gives

    h'(y)=1/2 [g'(s+y)+g'(1−s+y)
                         +g'(s−y)+g'(1−s−y)].

For |y|≤2R, each upper logarithm in (4) is
Log(it/(2π))+O((1+R)/t), and each lower logarithm is
Log(−it/(2π))+O((1+R)/t). These are uniform estimates on disks
away from the logarithm cut. The two leading arguments cancel,
and the one-quarter sum of the four logarithms is ell. Thus,
with r(y)=h(y)−ell y,

    |r'(y)|≤C R/t,       |r(y)|≤C |y| R/t≤2C R²/t.  (6)

The second bound integrates the first along the segment from zero,
using r(0)=0. In particular exp(r)=1+O(R²/t) uniformly, since
R²/t tends to zero. For real y, exp(r(y)) is strictly positive.
This establishes (18a), including its analytic branch and derivative.

### 3. Amplitude estimates on arcs and chords

Let W_c be the union of segments from c to ce^(iθ), |θ|≤β.
Every point y in W_c has |y|≤c and Re y≥c cosβ. Put
σ_* =1/2+c_0 cosβ>1. The absolutely convergent series bounds
both zeta factors of F by ζ(σ_*).

The derivative bound can be made uniform even after multiplication
by c. For σ≥σ_*, the differentiated series implies

    |ζ'(σ+iv)| ≤ Σ_(m≥2)(log m)m^(−σ)
              ≤ 2^(−(σ−σ_*)) Σ_(m≥2)(log m)m^(−σ_*).

On W_c, σ=1/2+Re y≥σ_*+(c−c_0)cosβ. Hence

    |F(y)|≤C,     |F'(y)|≤C exp(−κc),
    κ=(log 2)cosβ>0,                              (7)

where the constant absorbs the fixed c_0. This argument works
for both zeta heights independently; no cancellation is assumed.
Define E(y)=exp(r(y))F(y). From (6)–(7),

    |E(y)|≤C,
    c|E'(y)|≤C(cR/t + c exp(−κc))≤C.              (8)

Here c≤R and R²/t=o(1), so the last constant is uniform.
For real c, F(c)=|ζ(1/2+c+it)|². The reciprocal Möbius series
gives |ζ(σ+it)|≥1/ζ(σ) for σ>1. Thus

    E(c)=exp(r(c)) |ζ(1/2+c+it)|²
        ≥ [2 ζ(1/2+c_0)²]^(−1)=:e_0>0            (9)

at all sufficiently large t. Integrating (8) along a chord of
length |ce^(iθ)−c|≤c|θ| gives

    |E(ce^(iθ))−E(c)|≤C|θ|≤(C/e_0)|θ|E(c).       (10)

This proves all parts of (18b). In particular the lower bound is
on the positive shifted amplitude, not on Ξ(t) or ζ(1/2+it).

### 4. Zeta bounds across the entire complementary arc

We first justify the uniform interpretation of the classical
convexity input. Fix 0<δ<1/4. On σ=1+δ the Dirichlet series
is bounded; on σ=−δ the functional equation and sector Stirling
give O_δ((1+|v|)^(1/2+δ)). Apply strip Phragmén–Lindelöf to
( s−1 )ζ(s)/( s+2 ), removing the pole inside the strip and
introducing no pole there. Its finite-order growth is the one
in Titchmarsh Section 5.1. Interpolation of the boundary powers
on [−δ,1+δ] gives exponent

    (1/2+δ)(1+δ−σ)/(1+2δ) = (1+δ−σ)/2.

The strip estimate is uniform on 1/2≤σ≤1; removing the rational
factor at |v|≥2 changes its constant only. Choosing δ≤2ε gives
the claimed bound with any prescribed fixed positive loss ε.
This avoids assuming uniformity merely from pointwise convexity
exponents. Both height signs follow by conjugation.

Now take y=u+iv with |y|≤R and u≥0. The heights in F(y) are
t+v and −t+v, whose absolute values belong to [t−R,t+R].
They are comparable to t, and their logarithms differ from log t
by O(R/t). In the bounded strip 1/2≤σ≤1 the convexity exponents
are bounded, so this replacement of heights changes constants
uniformly. Choose the loss for each factor to be ε/2. For
0≤u≤1/2 the product bound is

    |F(y)|≤C_ε t^(1/2−u+ε).

Combining this with (3) and (6) gives

    |P(y)|≤C_ε t^(1/2+ε),     0≤u≤1/2,           (11)

since exp(ell u)t^(−u)=(2π)^(−u)≤1.

For u≥1/2, first use Theorem 3.5 on 1≤1/2+u≤2.
It bounds both factors by C log t, including σ=1 and shifts
arbitrarily close to it. For 1/2+u≥2, their absolute series are
bounded by ζ(2). Thus for every fixed ε>0,

    |F(y)|≤C_ε t^ε,
    |P(y)|≤C_ε exp(ell u)t^ε,      1/2≤u≤R.      (12)

This split covers the whole transition without a divergent
1/(σ−1) constant. Evenness gives identical estimates after
replacing y by −y if its real part is negative.

On |y|=c outside the two arcs of angular radius β about ±c,
we therefore have u=|Re y|≤c cosβ. Divide (11)–(12) by
exp(n)=exp(ell c). Since

    c−max(1/2,c cosβ)≥η,

choose 0<ε<η/2. In (11) convert only the fixed power
 t^(1/2+ε)=(2π)^(1/2+ε)exp((1/2+ε)ell).
In (12) retain exp(ell u) exactly and convert only t^ε.
Both give the uniform estimate

    |P(y)|≤C exp(n) exp(−η ell/2).                (13)

No factor such as (2π)^c is absorbed in a constant. This is
essential because c grows to R.

### 5. Xi gauge, including the cancellation and derivatives

The analytic k=log b above satisfies, by direct differentiation,

    k''(z)=2(1/4−z²)/(z²+1/4)²
           −1/2 [g''(a(z))+g''(a_*(z))].         (14)

The first term is O(t^(−2)) uniformly for |z−t|≤2R.
By (5), g''(w)=1/(2w)+O(t^(−2)). Individually its leading
terms have size O(1/t), but their sum cancels to the required
order because, exactly,

    1/a(z)+1/a_*(z)=1/(z²+1/4).

Thus (14) is O(t^(−2)) on the whole disk, with a uniform constant.
This calculation is needed; bounding the two terms separately
would not establish the claimed gauge precision.

Let

    j(y)=k(t+iy)+k(t−iy)−2k(t),
    Q(y)=exp(j(y))=b(t+iy)b(t−iy)/b(t)².

Then j(0)=j'(0)=0. Integration of (14), or the exact expression
j'(y)=i[k'(t+iy)−k'(t−iy)], gives

    |j'(y)|≤C |y|/t²,     |j(y)|≤C |y|²/t²,
    Q(y)=1+O(|y|²/t²),    |Q'(y)|≤C |y|/t²       (15)

for |y|≤2R. Each integration path stays in the stated disks.
Q is analytic and even. On the real y-axis it is positive:
b respects conjugation on its disk, and Q(y)=|b(t+iy)|²/b(t)².

Consequently

    Ξ(t+iy)Ξ(t−iy)/b(t)² = Q(y)P(y).              (16)

On W_c the amplitude A(y)=Q(y)E(y) has a uniform bound,
a positive lower bound at c, and c|A'(y)|≤C, by (8) and (15).
It therefore satisfies (10) with A in place of E. On all of the
complement |Q|≤2 for sufficiently large t, preserving (13).
At the real saddle,

    A(c)=|ζ(1/2+c+it)|²
                    (1+O(R²/t)+O(R²/t²)).       (17)

No division by a potentially vanishing central zeta or Xi value
has occurred. Central zeros of arbitrary multiplicity are allowed.

### 6. Cauchy extraction with the factorial normalization

This argument applies to P with amplitude A=E, and to QP with
amplitude A=QE. On the positive arc, Cauchy's formula reads

    c^(−n)/(2π) ∫_(−β)^β
           exp(n exp(iθ)−inθ) A(c exp(iθ)) dθ.    (18)

For constant amplitude A(c), integration over the full circle is
exactly A(c)ell^n/n!. Its omitted part has absolute value at most
C c^(−n) exp(n cosβ) A(c). Real Stirling at integer n gives

    c^(−n) exp(n)/(ell^n/n!) = n! exp(n)/n^n
                            ≤C sqrt(n),         (19)

with an absolute constant for every n≥1. Thus the truncated
constant-amplitude error is at most

    C A(c)ell^n/n! · sqrt(n)exp(−nd).

For the varying amplitude use (10). Since 1−cosθ≥aθ² for a
fixed a>0 on |θ|≤β, its error relative to A(c)ell^n/n! is at most

    C sqrt(n) ∫_(−β)^β exp(−anθ²)|θ| dθ
        ≤ C/sqrt(n).                            (20)

The negative arc makes exactly the same contribution: P and QP
are even and exp(−inπ)=1 for even n. Hence the two main arcs
supply twice the main term, with the errors just bounded. The
complement is bounded by (13), times at most 2 for Q; after (19)
and division by the uniform positive A(c), its relative error is
at most C sqrt(n)exp(−η ell/2). Also nd=c ell d≥η ell,
so the constant-amplitude arc truncation is absorbed by that bound.
We obtain

    coefficient of y^n in P or QP
      =2 A(c)ell^n/n! · [1+O(n^(−1/2)
                             +sqrt(n)exp(−η ell/2))].

Substituting (9), (6), and (17) proves (1); products of small
error terms are absorbed after a single larger onset. Multiplying
the QP formula by b(t)² gives precisely D_p(Ξ;t), with no missing
factorial or index change. Coefficients are real because the original
functions are real on their real interval; hence the relative error
can be chosen real.

Finally n≥c_0 ell and n≤ell³ imply n^(−1/2)≤C ell^(−1/2)
and sqrt(n)≤ell^(3/2). The fixed exponential saving beats this
power, while R²/t=ell^4/t and R²/t² tend to zero faster than
ell^(−1/2). One onset therefore makes both errors less than 1/2
for all allowed integers simultaneously. Every main factor is
positive by (9) and b(t)>0. This proves the stated positivity.

All infinite series used above converge absolutely in a fixed
half-plane strictly to the right of one, except for the explicitly
cited classical strip bounds. Analytic continuation and Cauchy
integration take place on finite disks with positive pole distance.
There is no unproved infinite interchange or positivity assumption.

## Mathlib

Full matching theorem and supporting formalizations were not checked
in this step. Availability is unknown, not established absence.
The proof uses named sector Stirling, absolute Dirichlet convergence,
strip Phragmén–Lindelöf, the zeta functional equation and Cauchy's
formula; the precise mathematical citations and applicability checks
are given above. No formal verification is claimed.
