# Lemma 453: uniform rounded-endpoint Laguerre margin

## Hypotheses

Use the actual theta transform Ξ and the coefficients defined by
Ξ(a+iy)Ξ(a−iy)=Σ_{j≥0}D_j(Ξ;a)y^(2j). Let a tend to infinity
through positive real values and put

    R=log(a/(2π))/2, n=ceil(R/2), m=2n.

Let r>0 be the solution of

    (2πexp(2r))²=a²+(n/r+9/2)²,
    h=n/r+9/2, τ=arctan(a/h)/2,
    Φ_*=m log r+9r−h−2aτ, C₀=(8π²)².

Assume the precise external input used in L452: OpenAI,
*The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane Re s > 7/8*,
September 30, 2026, [Theorem 1.1 at the pinned commit](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex)
`1581d4cbdd69a0faf34b2089614fe2a814316a6a`, in its zeta specialization.
It asserts nonvanishing for Re(s)>7/8, allowing the pole at 1; it
does not exclude boundary zeros. The
[external-input register](../foundations/2026-10-quasi-riemann-input.md)
retains the verification qualifications. Its complete manuscript proof
and formal import closure have not been independently audited locally.
We use the separately audited L452 (1), not an independent proof of
this external hypothesis or its paired-parameter conclusion (2).

## Conclusion

Put

    σ=1+2/r, B=|ζ(σ+ia)|²,
    P=[2^(m−1)/m!] C₀ exp(Φ_*) π/a >0.

There are fixed constants and one real onset such that, for every a
beyond that onset, including the ceiling jump heights,

    D_n(Ξ;a)/(P B)=1+O(r^(−1/6)),                         (1)
    D_n(Ξ;a)/P ≥ B/2 ≥ 1/[2(1+r/2)²] >0.                (2)

Thus D_{ceil(log(a/(2π))/4)}(Ξ;a)>0 for every sufficiently large
real a, under the pinned external input. Constants and onset are
existential, not numerically evaluated. This is a local specialization
of the endpoint sector and Mellin methods, not a new zero-free theorem.
The separate critical audit below validates this conditional result.
It supplies one index at each
large height, not the initial segment of smaller indices, global mixed
positivity, bounded exterior-height coverage, or a resolution of RH.

## Proof

### 1. Exact ceiling domain

The saddle equation has a unique positive solution: its left side is
strictly increasing, its right side strictly decreasing, and their
difference changes sign between zero and infinity. Taking logarithms
gives the exact identities

    r=R+(1/4)log(1+h²/a²), h=9/2+m/(2r).                 (3)

For R≥1, r≥R and n<R/2+1 give h≤5+1/R≤6. Consequently

    0<r−R≤9/a², 0≤m−R<2,
    −9/a²≤m−r<2.                                       (4)

The non-strict lower bound is sufficient; the first inequality follows
from log(1+x)≤x. At a=2πexp(4k), R=2k and n=k, so r>m
and h<5. This checks the side of the endpoint that a direct h>5
application would miss. Immediately to the right of a jump, n rises
by one, but (4) still holds. No continuity of the rounded index is used.

All estimates below are uniform on the slightly larger proof domain

    r≥8, m even, r−1≤m≤r+2,
    h=9/2+m/(2r), a²=4π²exp(4r)−h².                    (5)

In particular 39/8≤h≤21/4, m→∞, and a/(2πexp(2r))→1
uniformly there. By (4), the requested parameters eventually lie in
(5). Write ν=h−4=1+(m−r)/(2r); thus

    1−1/(2r)≤ν≤1+1/r.                                 (6)

### 2. Exact weights and their full discrete tails

Retain the actual exponent m, and define

    W(j,k)=(jk)^(−1/2)(1−log(jk)/(2r))_+^m,
    J={j≥1:log j<3r/4},
    T=Σ_{j,k∈J}W(j,k)exp(ia log(k/j)),
    S=Σ_{j,k≥1}W(j,k)exp(ia log(k/j)).                   (7)

Both sums are finite. The weights decrease in each positive real
coordinate on [1,∞), with value zero beyond the cutoff. For 0≤L<2r,
put u=L/(2r). From log(1−u)≤−u−u²/2 and m≥r−1,

    Q(L):=exp(L/2)(1−L/(2r))^m
       ≤exp((r−m)u−m u²/2)
       ≤e exp(−L²/(16r)).                              (8)

Extend Q by zero for L≥2r; (8) still holds. Monotone sum-integral
comparison, retaining the two coordinate edges and the corner, gives

    Σ_{j,k≥1}W(j,k)
       ≤1+2∫₀^∞Q(u)du+∫₀^∞LQ(L)dL=O(r).             (9)

Here x=exp(u), y=exp(v) changes the double integral of W into
∫∫Q(u+v)du dv. This explains the density factor exp(L/2) in Q.

For an integer K≥3 and B_K=log(K−1)>0, the same comparison gives

    Σ_{j≥K,k≥1}W(j,k)
      ≤∫_{K−1}^∞W(x,1)dx+∫_{K−1}^∞∫₁^∞W(x,y)dy dx
      ≤C(r/B_K+r)exp(−B_K²/(16r)).                     (10)

For the first integral use ∫_B^∞exp(−L²/(16r))dL
≤(8r/B)exp(−B²/(16r)); for the second use
∫_B^∞L exp(−L²/(16r))dL=8r exp(−B²/(16r)).
Thus every cutoff K=ceil(exp(3r/4+O(1))), with the O(1) in a
fixed bounded interval, has tail O(r exp(−r/64)), since B_K≥r/2
eventually. This includes the exact strict boundary of J and both
clipped-patch boundaries below. By symmetry and the union bound,

    |S−T|≤C r exp(−r/64).                              (11)

These bounds are independent of the phase a. They do not assert that
S is positive at arbitrary a with r held fixed.

### 3. Positive-sector stationary patches and complement

The parameterwise contour identity in L269 is valid here: for each
fixed a,n, τ<π/4, and the analytic theta kernel has polynomially
weighted superexponential domination on this smaller strip. Hence

    I_n(a)=∫∫F(s,x)ds dx,
    F=exp(−2aτ)s^m k(s+x+iτ)k(s−x−iτ)exp(2iax),
    D_n(Ξ;a)=2^(m−1)I_n(a)/m!.                         (12)

Its proportional-index asymptotic is not used. On
D₊={s+x>r/4,s−x>r/4}, use the exact algebra of L288, with
coordinates ξ,η in place of its p,q. Put

    b=log(jk)/2, d=log(k/j)/2,
    ξ=(s−r+b+x−d)/sqrt(2), η=(s−r+b−x+d)/sqrt(2),
    v=(ξ+η)/sqrt(2), s=r−b+v, c₀=2sqrt(2),
    α_j=(log j−3r/4)/sqrt(2),
    f(y)=−(a/2)(exp(c₀y)−1−c₀y).

The absolute Jacobian is one, and D₊ becomes ξ>α_j, η>α_k.
After division by C₀exp(Φ_*), the exact summand is

    exp(ia log(k/j)) H_jk(ξ,η) exp(if(ξ)−if(η)),
    H_jk=G_jk E,
    G_jk=(jk)^(−1/2)(s/r)^m
         ·exp(9v−(h/2)(exp(c₀ξ)+exp(c₀η)−2)),
    E=(1−3exp(−c₀ξ)/(2V_+))(1−3exp(−c₀η)/(2V_-)),
    V_±=πexp(2r±2iτ), |V_±|=sqrt(a²+h²)/2.             (13)

The algebra uses the saddle identities, not h>5. On D₊, s>r/4;
log(s/r)≤(s−r)/r gives

    G_jk≤(jk)^(−ν)g_h(ξ)g_h(η),
    g_h(y)=exp(−(h/2)(exp(c₀y)−1−c₀y)).               (14)

Let M_h(y)=(1+exp(c₀y))g_h(y). Derivatives in each variable
through order one, including the mixed derivative, obey

    |∂_ξ^e∂_η^f H_jk|≤C(jk)^(−ν)M_h(ξ)M_h(η),
    e,f∈{0,1}.                                       (15)

Indeed the first logarithmic derivative of G in ξ is
m/(sqrt(2)s)+9/sqrt(2)−h sqrt(2)exp(c₀ξ), and the
mixed logarithmic derivative is −m/(2s²). Both are controlled
because m/s≤4m/r and m/s²≤16m/r². The same holds in η.
For E, exp(−c₀ξ)/|V_+|≤exp(−r/2)/(πj²) on D₊;
each derivative only supplies a fixed factor. No division by E occurs.

Uniformly in (5), define

    B_h(A)=sup_{y≥A}M_h(y)+∫_A^∞M_h(y)dy.

Substitution t=exp(c₀y) writes M_h as
exp(h/2)(1+t)t^(h/2)exp(−ht/2). Since h stays in the fixed
band in (5), its full supremum and integral are bounded, and

    B_h(A)≤C (A≤0), B_h(A)≤C exp(−exp(c₀A)) (A≥0).

With J₀=exp(3r/4), this implies

    Σ_j j^(−ν)B_h(α_j)≤C(1+r).                         (16)

For j≤J₀, use j^(−ν)≤j^(−1)J₀^(1/(2r))≤e^(3/8)/j.
For j>J₀, compare the decreasing function
x^(−ν)exp(−(x/J₀)²) with its integral. After x=J₀t, the
factor J₀^(1−ν)≤e^(3/8) and the remaining integral on t≥1
is uniformly bounded, since ν is bounded away from zero.
Equations (15)–(16) prove absolute integral summability and bound
the sum of rectangular variations by C(1+r)². All corner and
edge terms are included in the variation as in L300.

Every interval primitive of exp(±if) is O(a^(−1/2)); on an
interval wholly outside [−ε,ε], ε=1/100, it is O(a^(−1)).
To verify this uniformity, f' is monotone, vanishes only at zero,
and has size at least c sqrt(a) outside |y|≤a^(−1/2), and
at least c_ε a on the fixed exterior. The central length bound
and integration by parts using the variation of 1/f' prove both
claims, with arbitrary interval endpoints. Partition each translated
D₊ outside its ε-square into at most four rectangles. One of the
two primitives has the stronger bound there. The rectangular
integration-by-parts identity, (15) and (16), therefore give

    Σ_{j,k}|complementary summand integral|
       ≤C exp(Φ_*)(1+r)²a^(−3/2).                      (17)

Lower terms vanish when primitives are anchored at their lower
endpoints; the upper corner and both edges are bounded by the
variation. Absolute integrability justifies unbounded limits and
termwise summation. Thus no endpoint term was discarded.

For the patches, retain L299's finite-square calculation with the
changed exponent. A nonempty clipped square requires
log j,log k<3r/4+sqrt(2)ε, hence s₀=r−b≥r/5 eventually.
On its full ε-square, factor H=W(j,k)A_b E with

    A_b=exp(m log(1+v/s₀)+9v
            −(h/2)(exp(c₀ξ)+exp(c₀η)−2)).              (18)

Here A_b(0,0)=1; all first and mixed derivatives needed for
rectangular variation are uniformly bounded because m/s₀ and
m/s₀² are bounded. Also E−1 has variation O(1/a). Use the
exact phase change

    Y=sgn(ξ)sqrt((exp(c₀ξ)−1−c₀ξ)/4),
    Z=sgn(η)sqrt((exp(c₀η)−1−c₀η)/4).

It is a smooth diffeomorphism on the fixed interval with derivative
one at zero and bounded inverse derivatives. The phase becomes
−2aY²+2aZ². On the central square of radius ρ=a^(−2/5),
replacing the transformed amplitude by its value one costs O(ρ³).
The other rectangles cost O(a^(−3/2)/ρ), using one Fresnel tail
primitive and one full primitive. Extending the constant central
integral to the plane adds O(a^(−3/2)/ρ+a^(−2)/ρ²).
The E−1 term costs O(a^(−2)) by its variation. The full patch
integral is therefore

    C₀exp(Φ_*)exp(ia log(k/j))W(j,k)
       ·[π/(2a)+O(a^(−11/10))],                       (19)

uniformly over every potentially clipped index. Any clipped patch
has absolute signed integral at most C exp(Φ_*)W(j,k)/a by
the same bounded primitives and variation. Full patches with
log j,log k<3r/4−sqrt(2)ε lie inside D₊. All remaining
patches and the discrepancy from J² lie in the tail (10).
Summing (19) with (9), bounding that tail, and adding (17) yields

    ∫_{D₊}F=C₀exp(Φ_*)π/(2a)
      ·[T+O(r a^(−1/10)+r exp(−r/64)+(1+r)²a^(−1/2))]. (20)

This rechecks the growing-index and clipped-boundary issues rather
than invoking a fixed h>5 dominated limit.

### 4. Same-sign boundary strips

Use the exact L295 amplitude on u=s+x≥0, v=s−x≥0:

    A_jk=exp(−9r+h)((u+v)/(2r))^m j⁴k⁴
       ·exp(9(u+v)/2−(h/2)(j²exp(2(u−r))+k²exp(2(v−r))))
       ·E_j(u)overline(E_k(v)),
    E_j(u)=1−3/(2πj²exp(2u+2iτ)),
    φ_j(u)=au−πsin(2τ)j²exp(2u).                      (21)

The original summand is C₀exp(Φ_*)A_jk exp(iφ_j−iφ_k)
and ds dx=du dv/2. Write H=m/(2r). For ℓ=0,1,2,
maximizing t^(m−ℓ)exp(−m(t−1)) gives

    |(d/dw)^ℓ(w/(2r))^m|≤C exp(H(w−2r)), w≥0.         (22)

For 0≤w≤7r/4 the stronger bound has the factor exp(−r/256).
Indeed t=w/(2r)≤7/8; for large m the maximum on this range
is at 7/8, and its value is at most C exp(−m d), where
d=−log(7/8)−1/8≥1/128. Since m≥r−1, this is at most
C exp(−r/256). At w=0 all relevant polynomial derivatives
vanish for m>2, so no division by w is used.

Put y=u−r+log j, z=v−r+log k and

    M_h^*(t)=(1+exp(2t))exp(ht−(h/2)(exp(2t)−1)).

Equations (21)–(22) and the product rule give, for e,f∈{0,1},

    |∂_u^e∂_v^f A_jk|≤C(jk)^(−ν)M_h^*(y)M_h^*(z),    (23)

with the extra exp(−r/256) whenever u+v≤7r/4. The mixed
derivative uses only the three polynomial derivatives just bounded;
E_j,E'_j are uniformly bounded on u≥0. Combining the tangent
exponential with (21) gives exactly the index power (jk)^(−ν).

The tail function B_h^*(Y)=sup_{t≥Y}M_h^*(t)+∫_Y^∞M_h^*(t)dt
satisfies the same bounds as above, with exp(2Y) in place of
exp(c₀Y). The proof of (16), now with J₀=exp(r), gives
Σ_j j^(−ν)B_h^*(−r+log j)≤C(1+r). Thus (23) also
justifies absolute termwise integration on the whole quadrant.

Partition [0,r/4]×[0,∞) at v=3r/2. On the lower rectangle
u+v≤7r/4, so two O(a^(−1/2)) primitives and (23) give a
summed signed bound C(1+r)²exp(−r/256)/a. These primitive
bounds follow from translating φ_j to a(y−exp(2y)/2), as in
L301, and are uniform over all j and all interval endpoints.
On the upper rectangle retain the lower translated endpoint:

    Σ_k k^(−ν)B_h^*(r/2+log k)
       ≤CΣ_k k^(−ν)exp(−exp(r)k²)
       ≤C exp(−exp(r)/2).                             (24)

Here ν>0 and the remaining Gaussian series is bounded uniformly.
The same two-primitive estimate makes this part smaller than the
lower part. Transpose the rectangles and subtract their intersection
[0,r/4]². The intersection also has the curvature saving. All
corner and edge terms are included in the rectangular variation,
and absolute integrability permits infinite upper limits. Restoring
the factor and Jacobian in (21), for
S₊={u,v≥0,min(u,v)≤r/4}, we obtain

    |∫_{S₊}F|≤C exp(Φ_*)(1+r)²exp(−r/256)/a.           (25)

This retains the polynomial curvature that a plain tangent bound
would lose.

### 5. Both mixed sectors, uniformly across h=5

We recheck C294b's whole-sector proof on the fixed band
39/8≤h≤21/4, instead of using its statement outside h≤5.
On x>|s| use u=x+s≥0, v=x−s≥0 and ds dx=du dv/2.
With q(u)=(h/2)exp(2(u−r)), set

    B_j(u)=j⁴exp(9u/2−q(u)j²)E_j(u),
    Abar_jk=exp(−9r+h)((u−v)/(2r))^m B_j(u)B_k(v).

The exact summand is
C₀exp(Φ_*)exp(9iτ)Abar_jk exp(iφ_j(u)+iφ_k(v)).
The Gaussian moment inequality in C294b,

    Σ_j j⁴(1+qj²)exp(−qj²)≤Cq^(−5/2)exp(−q/2),

and bounded E_j,E'_j imply

    Σ_j(|B_j|+|B'_j|)≤Cexp(5r)W₀(u),
    W₀(u)=exp(−u/2−(39/32)exp(2(u−r))).                (26)

The constant is uniform since h stays in the displayed compact band.
Let β=m/r=2h−9∈[3/4,3/2]. For ℓ=0,1,2, maximization at
|w|/r=1−ℓ/m gives

    |(d/dw)^ℓ(w/(2r))^m|
       ≤C2^(−m)exp(−m)exp(β|w|).                     (27)

The derivative prefactor is bounded by β^ℓexp(ℓ), uniformly;
continuity handles w=0. The fact that m is even also retains the
exact real polynomial across u=v. Combining (26)–(27) bounds the
sum of moduli of each first/mixed derivative of Abar by

    Cexp(r)2^(−m)exp(−m)exp(β|u−v|)W₀(u)W₀(v).

The positive-tail integral is at most Cexp((β−1/2)r): after
u=r+t the remaining integrand is exp((β−1/2)t−(39/32)exp(2t)).
It is dominated on t≤0 by exp(t/4), and on t≥0 by
exp(t−(39/32)exp(2t)). The negative-tail integral is at most
1/(β+1/2). Using exp(β|u−v|)≤exp(βu−βv)+exp(βv−βu),
we obtain

    Σ_jk∫∫|∂_u^e∂_v^f Abar_jk|
       ≤Cexp((1/2−β log 2)r)≤Cexp(−γ₀r),
    γ₀=(3/4)log 2−1/2>1/54, e,f∈{0,1}.              (28)

For the last strict inequality one may use
log 2=2∫₀^(1/3)(1−t²)^(−1)dt>56/81.
Equation (28) proves absolute integral summability. Anchor each
φ_j primitive at zero; it is O(a^(−1/2)). Two integrations by
parts then bound each signed summand integral by C/a times its
mixed-derivative integral. Lower edges vanish by anchoring. For
fixed j,k, all upper edges and their integrals vanish by the
polynomial-times-superexponential decay; (28) controls the limiting
derivative integral. Thus the mixed-sector bound is

    C exp(Φ_*)exp(−γ₀r)/a.                             (29)

Reflection x↦−x conjugates F and maps to the other mixed sector,
so (29) holds there too. This step covers both sides of h=5 with
one constant and retains stationary points and boundary terms.

### 6. Whole-plane assembly

The positive and negative same-sign quadrants, with their interiors
and boundary strips, and the two mixed sectors partition the plane
up to null boundaries, exactly as in L302. Evenness of k and the
even integer m give F(−s,x)=F(s,x). Thus the two same-sign
interiors have identical integrals; the same is true of their strips.
The factor π/(2a) in (20) becomes π/a. The Jacobians of the
strip and mixed formulas have already been included and introduce
no extra factor. Equations (11), (20), (25), (29) yield

    I_n/[C₀exp(Φ_*)π/a]=S+ε,
    |ε|≤C E(r), E(r)=(1+r)²exp(−r/256).               (30)

Indeed a is uniformly comparable to exp(2r); the other error rates
are 1/5, 1/64, 1 and γ₀ in r, all strictly greater than 1/256.
The cutoff replacement (11) has already been included. Conjugation
in the original real-contour integral is the substitution t↦−t;
hence I_n is real. Interchanging j,k makes S real, so ε is real.

### 7. Changed-exponent Mellin identity and normalization

Choose c=1/2+2/r, σ=1/2+c=1+2/r and define

    K(v)=Γ(m+1)(2r)^(−m) exp(2r(c+iv))
            ·(c+iv)^(−m−1)/(2π),
    F_a(v)=ζ(σ+i(a+v))ζ(σ+i(v−a)).                    (31)

The scalar inverse Laplace formula used in L303, with exponent m,
is t_+^m/Γ(m+1)=(1/(2π))∫exp((c+iv)t)(c+iv)^(−m−1)dv.
Use t=2r−log(jk) and sum. The absolute majorant is

    Γ(m+1)(2r)^(−m)exp(2rc)/(2π)
      ·ζ(σ)²∫(c²+v²)^(−(m+1)/2)dv <∞.               (32)

Thus Fubini is legitimate for every parameter value, since σ>1
and m>0, and gives the exact identities

    S=∫K(v)F_a(v)dv, ∫K(v)dv=1.                      (33)

The second identity uses t=2r. In particular the Γ factor and
power are m+1, not r+1; no endpoint kernel has been substituted.
The principal analytic logarithm on Re z>0 defines the displayed
powers, though here m is integer. No contour shift crosses a pole.

Here is uniform localization of this kernel. Write

    |K(v)|=P₀(1+(v/c)²)^(−(m+1)/2),
    P₀=Γ(m+1)(2r)^(−m)exp(2rc)c^(−m−1)/(2π).

Stirling's formula gives, with q=2rc=r+4,

    P₀=[sqrt(m)/(c sqrt(2π))]
        ·exp(q−m−m log(q/m))(1+O(1/m))=O(sqrt(r)).    (34)

In (5), 2≤q−m≤5. Taylor's formula for log(1+(q−m)/m)
therefore bounds the exponent by O(1/r) uniformly. For |v|≤c≤1,
log(1+(v/c)²)≥v²/(2c²) and m+1≥r imply

    |K(v)|≤C sqrt(r)exp(−rv²/4).                       (35)

For |v|>c, writing x=|v|/c≥1 gives
(1+x²)^(−(m+1)/2)≤2^(−m/4)(1+x²)^(−m/4−1/2).
For sufficiently large m the latter power is at most (1+x²)^(−2).
The outer integral is O(sqrt(r)2^(−m/4)). In particular,

    ∫|K|≤C,
    ∫_{|v|>V}|K(v)|dv≤Cexp(−(log r)²/8),
    V=log(r)/sqrt(r).                                 (36)

For the inner part of the tail, split the Gaussian in (35) into
two halves and use rV²=(log r)². The outer exponential tail is
smaller. These bounds hold uniformly over the changed exponent.

### 8. Relative freezing and the strict margin

Let g=ζ'/ζ. For |v|≤V the exact quotient identity used in L330 is

    F_a(v)/B=exp(A(v)),
    A(v)=i∫₀^v[g(σ+i(a+t))+g(σ+i(t−a))]dt.             (37)

It follows by differentiating and using the value one at zero;
neither a logarithm branch nor positivity of K is assumed. The
second term is the conjugate of g(σ+i(a−t)). By L452 (1),
applied at both positive heights a±t, and (5),

    M:=sup_{|t|≤V}|g(σ+i(a+t))|≤C(log a)^(1/3)
       ≤C r^(1/3)=o(sqrt(r)).                         (38)

All sufficiently large parameters have 63/64≤σ≤2 and a−V
beyond the fixed onset in L452. Equation (37) then gives
|F_a(v)/B−1|≤2M|v|exp(2M|v|). Integrating with (35) and
putting w=sqrt(r)v bounds the inner relative error by

    C(M/sqrt(r))∫_{ℝ} |w|exp(−w²/4+2(M/sqrt(r))|w|)dw
       =O(r^(−1/6)).                                 (39)

The integral is bounded uniformly once M/sqrt(r)≤1. This is an
integrated estimate, so no supremum-window log r factor is lost.

Only on σ>1 use absolute Dirichlet and reciprocal Euler series:

    |F_a(v)|≤ζ(σ)²≤(1+r/2)²,
    B≥ζ(σ)^(−2)≥(1+r/2)^(−2)>0.                     (40)

The second inequality follows from
|1/ζ(σ+ia)|≤Σ|μ(k)|k^(−σ)≤ζ(σ), and the decreasing-integral
bound ζ(1+2/r)≤1+r/2. Thus (36) bounds the complete outer
relative error by

    C[(1+r/2)^4+1]exp(−(log r)²/8)=o(r^(−1/6)).       (41)

Combining (33), (39), (41) proves S/B=1+O(r^(−1/6)).
The factors in F_a(v) are not treated as conjugates when v≠0;
the derivative estimate, not a positive averaging representation,
justifies this comparison. The tail is compared with B first, not
with the exponentially smaller sector error.

Finally (12), (30) and (40) give the complete real error estimate

    |D_n/(P B)−1|
      ≤C_F r^(−1/6)+C_E(1+r/2)²(1+r)²exp(−r/256).    (42)

The second term is o(r^(−1/6)). Choose one r-onset beyond all
previous onsets and making each term in (42) at most 1/4. This
is possible uniformly on (5). Since r≥R→∞ with a, it yields
one real a-onset for every ceiling position and proves (1)–(2).
The lower normalized margin divided by E(r) is at least

    exp(r/256)/[2(1+r/2)²(1+r)²] →∞.

Every normalization is positive; (12) and the exact reflection in
(30) reproduce the C452a factor with the changed parameters.
This completes the asserted specialization. ∎

The old coefficientwise freezing loss and fixed-r/arbitrary-phase
negative examples remain valid. This proof changes r with the actual
height and uses L452 (1); it does not prove an all-height sign at
fixed r. No assertion about lower indices follows by rounding or
monotonicity. Global mixed positivity, bounded exterior heights and
the selected-law/regulator gaps remain unresolved.

### Critical audit — 2026-10-23

**Verdict and scope.** Equations (1)–(2) pass the separate audit,
conditional on the exact pinned external input in the Hypotheses.
No added mathematical hypothesis or changed conclusion is needed.
The harmless cutoff-range clarification K≥3 in (10) makes its stated
positive denominator explicit; all actual cutoffs tend exponentially
to infinity. This validates the written known-method specialization,
not a new sign principle or an independent certification of the external
manuscript, formal import closure, boundary nonvanishing or RH.

**Ceilings and uniform domain.** For n≥1 the saddle equation's left
side increases strictly from a finite value and its right side decreases
strictly from infinity, while the left side eventually tends to infinity.
There is exactly one positive r. For R≥1, n<R/2+1 and r≥R imply
h<5+1/R≤6, so 0<r−R≤h²/(4a²)≤9/a². Together with
0≤m−R<2 this proves (4). At every exact jump height R=2k,
m=2k<r, and immediately after it the upper bound m−r<2 still
holds. Both sides therefore enter (5) after one real-height onset;
continuity of n is neither asserted nor needed. In (5),
5−1/(2r)≤h≤5+1/r, which is contained in the wider compact
band used throughout the estimates. In particular a is positive and
uniformly comparable to exp(2r), and all polynomial degrees tend to
infinity uniformly. Each later sufficiently-large-r restriction can
therefore be imposed at one common onset.

**Discrete weights and exact algebra.** Since m≥r−1 and r≥8,
(r−m)u≤1 and m u²/2≥L²/(16r) for 0≤u=L/(2r)<1.
This verifies (8), including its density factor. Monotonicity of W
in each coordinate gives the edge/corner comparison (9). For the
one-coordinate tail the two continuous integrals are
∫_B^∞Q(L)dL and ∫_B^∞(L−B)Q(L)dL, respectively, with
B=log(K−1). They are bounded by the two integrals in (10).
For every used cutoff B≥r/2 eventually, proving the uniform
O(r exp(−r/64)) tail, including equality at a strict cutoff.
This is a discrete comparison; no continuous approximation to a
moving integer boundary is assumed.

The positive-sector substitution gives exactly
u=s+x=r−log j+sqrt(2)ξ and
v=s−x=r−log k+sqrt(2)η. Its Jacobian has modulus one.
Using 2πexp(2r+2iτ)=h+ia in the two exact theta summands
gives (13), including exp(ia log(k/j)). The polynomial tangent
bound combines m/r+9=2h with b=log(jk)/2 to produce precisely
(jk)^(−ν), ν=h−4, in (14). It is not replaced by (jk)^(−1).
Since s>r/4, the first logarithmic derivatives of G and its mixed
derivative have the bounds displayed before (16). Bounds on E and
its derivatives use the sector lower limits and do not divide by E.
Consequently (15) holds also where E could vanish.

For the changed index exponent, the head sum in (16) is bounded
by e^(3/8) times a harmonic sum up to exp(3r/4). Its remaining
tail has the scaling factor exp((3r/4)(1−ν))≤e^(3/8) and a
uniformly convergent Gaussian integral. Thus the full rectangular
variation, with its corner, two edges and mixed-derivative area
term, sums to O((1+r)²). The same majorant at derivative order
zero proves absolute integral summability before any interchange.
On each complementary rectangle, one phase primitive has size
O(a^(−1)) and the other O(a^(−1/2)); their product proves (17).
Anchoring at finite lower endpoints removes only those lower terms;
the upper corner and both edge terms are included in the variation.
Infinite upper limits follow from absolute integrability.

**Uniform stationary patches.** A nonempty clipped square has
s₀=r−log(jk)/2≥r/4−sqrt(2)ε, hence s₀≥r/5 eventually.
The full square remains at positive s. The ratios m/s₀ and
m/s₀² stay bounded, so A_b and its first and mixed derivatives
in (18) are uniformly bounded for all such indices. After the exact
phase diffeomorphism, the inverse Jacobian equals one at the origin
and has bounded derivatives. On radius ρ=a^(−2/5), the amplitude
replacement costs O(ρ³)=O(a^(−6/5)). The remaining rectangles
and full-plane extension cost O(a^(−3/2)/ρ+a^(−2)/ρ²),
at most O(a^(−11/10)); retaining E−1 costs O(a^(−2)).
The two opposite Fresnel integrals have product π/(2a), so (19)
has the stated sign and normalization. Clipped rectangles instead
obey the unrestricted O(W/a) primitive bound. Every non-full or
discrepant index is in a tail covered by (10); the total mass of
the full patch errors is O(r a^(−1/10)). This proves (20)
uniformly, with no fixed-index dominated-limit substitution.

**Boundary strips and mixed sectors.** For each ℓ≤2 the polynomial
derivative divided by exp(H(w−2r)) has its maximum at
t=w/(2r)=1−ℓ/m. On t≤7/8 its maximum is at 7/8 for
all sufficiently large m. The resulting bound is
C exp(−m d), d=−log(7/8)−1/8≥1/128, hence
C exp(−r/256). All these derivatives vanish at w=0 once m>2.
Applying the product rule proves (23), including the mixed derivative
without a singular division at zero. The changed exponent ν in the
sum of B_h^* contributes at most exp(r(1−ν))≤e^(1/2),
so the entire sum is O(1+r). The lower strip rectangle and its
intersection retain the curvature saving. On the upper rectangle the
lower translated endpoint gives (24), which is superexponentially
smaller. The two-primitive variation identity retains all finite edge
and corner terms. This establishes (25) for both reflected strips.

For the mixed sectors, (26) follows from the Gaussian fourth/sixth
moment bound with h/4≥39/32, uniformly on the wider band.
The maximum for (27) occurs at |w|/r=1−ℓ/m and its prefactor
is bounded by β^ℓ exp(ℓ), β=m/r∈[3/4,3/2]. Thus the
summed derivative bound uses only derivatives through order two of
the real polynomial and is valid across u=v. The positive and
negative one-variable integrals are bounded by
C exp((β−1/2)r) and 1/(β+1/2), respectively. Combining
these with exp(r)2^(−m)exp(−m) gives exactly
exp((1/2−β log 2)r). The minimum decay satisfies
γ₀=(3/4)log 2−1/2>1/54, since log 2>56/81.
This checks (28) on both sides of five, rather than importing
C294b beyond its stated range. At fixed indices all upper edges
vanish by polynomial-times-superexponential decay; both lower
primitives vanish at zero. The mixed-derivative integral is summable
by (28). Two primitive bounds therefore prove (29), including
stationary indices and sector boundaries.

**Normalization and whole-plane coverage.** The six regions used
in (30) exhaust the plane up to null boundaries. Evenness of k and
the even integer m give F(−s,x)=F(s,x), so the two same-sign
interiors double π/(2a) to π/a. The strip and mixed substitutions
already have Jacobian 1/2. There is no further reflection multiplier.
The remaining error rates in r are 1/5, 1/64, 1 and γ₀, all
strictly greater than 1/256. Thus E(r) absorbs every sector and
cutoff error uniformly. The original real-contour integral and the
index-swapped finite sum are real, which also makes ε real.

The coefficient normalization independently agrees with audited
C452a: the whole-line transform is 2Ξ, coefficient extraction has
factor 1/m!, and evenness followed by u=s+t, v=s−t contributes
Jacobian 2 and polynomial (2s)^m. Dividing by four gives
D_n=2^(m−1)I_n/m!. Each fixed-parameter contour shift stays
inside τ<π/4 with polynomially weighted integrable domination.
Neither a proportional-index asymptotic nor an unproved uniform
contour-shift constant is used for this exact identity.

**Changed Mellin kernel and full relative error.** Scalar inversion
with exponent m, followed by the absolute majorant (32), gives
S=∫K F_a and ∫K=1. The exponent is −m−1 and the gamma factor
is Γ(m+1); replacing either by its r analogue would be invalid.
Here c=1/2+2/r>1/2 ensures σ>1 and absolute Dirichlet-series
Fubini for every parameter, with no contour shift through a pole.
In Stirling's formula q=2rc=r+4 has 2≤q−m≤5, so
q−m−m log(q/m)=O(1/r) uniformly. This verifies the prefactor
O(sqrt(r)), the Gaussian bound (35), and both complete tails
in (36); their constants are uniform on (5).

At |v|≤V the two logarithmic derivatives in (37) are evaluated
at a+t and, after conjugation, a−t. Both are positive heights
beyond L452's fixed onset, and σ eventually lies in its entire
stated strip. Thus M≤C r^(1/3), and the integrated Gaussian
comparison costs O(M/sqrt(r))=O(r^(−1/6)), with no window
supremum log r factor. On the full exterior, the absolute Euler
and reciprocal series are used only at σ>1. They give
|F_a|/B≤(1+r/2)^4 and B≥(1+r/2)^(−2).
The logarithm of the relative tail divided by r^(−1/6) is at
most −(log r)²/8+(25/6)log r+O(1), which tends to −∞.
This validates (41); no modulus-square substitution at v≠0 or
positive-kernel premise enters the comparison.

Finally the additive sector error divided by B is bounded by
C_E(1+r/2)²(1+r)²exp(−r/256), also o(r^(−1/6)).
Both terms in (42) are at most 1/4 for every parameter beyond
one r-onset. The ceiling domain satisfies r≥R→∞, so this
gives one real a-onset, including every jump height. The lower
margin divided by E(r) tends to infinity exactly as stated.
All constants and this onset remain existential. Only one index
per height is signed; no lower-index inference, full mixed
positivity, zero-exclusion extension or RH resolution follows.
The old fixed-r/unit-phase and coefficientwise-freezing failures
retain their distinct quantifiers and are not erased by this audit.

**Mathlib qualification.** Full matching coverage remains not checked.
The audited argument uses the named inversion/Stirling and elementary
oscillatory mechanisms with their hypotheses verified above. The
supporting Euler-log coverage and external Lean artifact retain
L452's explicit qualifications; neither is a local formal verification
of this result or of the external input.

## Mathlib

Full matching theorem: not checked; no absence is asserted. The
supporting contour identity, scalar inversion, Stirling formula,
oscillatory primitives, Euler reciprocal bound and Littlewood
specialization are the local inputs explicitly identified in the proof.
L452 distinguishes its Euler-log supporting coverage and the pinned
external Lean artifact from a Mathlib theorem or a locally verified
build. No additional formal coverage or external-proof audit is claimed.
