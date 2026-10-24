# Lemma 455: uniform subendpoint whole-plane theta reduction

## Hypotheses

Use the actual even theta kernel k and transform Ξ of L269, with
Ξ(a+iy)Ξ(a−iy)=Σ_{n≥0}D_n(Ξ;a)y^(2n). Let r tend to infinity
through positive real values, and let m be a positive even integer with

    31/32≤α=m/r≤63/64, n=m/2,
    h=9/2+m/(2r), a=sqrt(4π²exp(4r)−h²)>0,
    τ=arctan(a/h)/2,
    Φ_*=m log r+9r−h−2aτ, C₀=(8π²)².

Define the full finite sum, including its cutoff, by

    W(j,k)=(jk)^(−1/2)(1−log(jk)/(2r))_+^m,
    S_{r,m}(a)=Σ_{j,k≥1}W(j,k)exp(ia log(k/j)).

Here the positive-part power is zero when log(jk)≥2r, including
equality. This is exactly the sum in L454. No zero-free half-plane
assumption is needed for the present reduction.

## Conclusion

There are fixed C,R>0 such that every admissible r≥R and even m obey

    I_n(a)=C₀exp(Φ_*)π/a ·[S_{r,m}(a)+ε_{r,m}],
    |ε_{r,m}|≤C(1+r)²exp(−r/200), ε_{r,m} real,          (1)
    D_n(Ξ;a)=P_{r,m}[S_{r,m}(a)+ε_{r,m}],
    P_{r,m}=[2^(m−1)/m!]C₀exp(Φ_*)π/a>0,              (2)

where I_n is L269's theta double integral. Thus the requested fixed
exponential rate exists, with K=2 and κ=1/200, uniformly on the
entire band. This is an additive reduction, not a sign theorem.
It is a local uniform specialization of the smaller-strip and
stationary-phase methods. The separate critical audit below validates
the reduction on its full stated domain, without a sign application.

## Proof

The approved comparison is
[the uniform-sector assessment](../drafts/literature/2026-10-23-subendpoint-theta-sector-reduction-coverage.md).
L324–L325 prove the smaller-strip mechanism at α=3/4; their
stated conclusions are not invoked at changed α. The proof below
retains their explicit identities and elementary estimates and supplies
uniform bounds for every changed parameter. L453's bounded-offset
mass estimates are not used. The recheck is necessary because α<1
by a fixed amount allows growing coefficient mass.

### 1. Parameterwise identity and exact summands

Uniformly on this band,

    3/4≤α<1, 39/8≤h≤5,
    a/(2πexp(2r))→1,
    2πexp(2r+2iτ)=h+ia.                               (3)

L269's contour identity is parameterwise and does not require the
proportional-index hypothesis of its asymptotic conclusion. For each
fixed pair a,n, the strip with height τ<π/4 supplies polynomially
weighted superexponential domination for the shift and Fubini. Hence

    I_n(a)=∫_{ℝ²}F(s,x)ds dx,
    F=exp(−2aτ)s^m k(s+x+iτ)k(s−x−iτ)exp(2iax),
    D_n(Ξ;a)=2^(m−1)I_n(a)/m!.                         (4)

No uniform contour domination as τ→π/4 is asserted here.
Uniform errors will follow from the estimates below.

In the positive same-sign quadrant use u=s+x≥0, v=s−x≥0;
ds dx=(1/2)du dv. Direct substitution of the exact theta series,
as in L324, gives F=Σ_{j,k}F_jk, where

    F_jk=C₀exp(Φ_*)A_jk(u,v)exp(iφ_j(u)−iφ_k(v)),
    A_jk=exp(−9r+h)P(u+v)B_j(u)overline(B_k(v)),
    P(w)=(w/(2r))^m,
    B_j(u)=j⁴exp(9u/2−(h/2)j²exp(2(u−r)))E_j(u),
    E_j(u)=1−3/(2πj²exp(2u+2iτ)),
    φ_j(u)=au−πsin(2τ)j²exp(2u).                      (5)

All formulas are exact; h=9/2+m/(2r) is used below, not an
approximation h≈5. The factors E_j and E'_j are uniformly bounded
on u≥0.

For ℓ=0,1,2, the elementary tangent bound is uniform:

    |P^(ℓ)(w)|≤C exp((α/2)(w−2r)), w≥0.              (6)

Indeed for t=w/(2r)>0, the ratio is
(m)_ℓ/(2r)^ℓ ·t^(m−ℓ)exp(−m(t−1)). Its maximum is at
t=1−ℓ/m and is uniformly bounded since m/r≤1 and m→∞.
At w=0 the derivatives vanish eventually. This also justifies (6)
when those derivatives occur in product rules at the boundary.

Translation y=u−r+log j changes φ_j, up to a constant, into

    f_a(y)=a(y−exp(2y)/2).

On every finite interval, either sign of exp(if_a) has a primitive
bounded by C a^(−1/2). Outside [−ε,ε], ε=1/100 fixed, the
bound is C_ε/a. To see this, remove |y|≤a^(−1/2), whose
length is O(a^(−1/2)). On each remaining side the derivative
a(1−exp(2y)) is monotone and has modulus at least c sqrt(a).
Integration by parts bounds the integral by the reciprocal endpoint
slopes and the variation of their reciprocal, of the same size.
On each fixed exterior side the lower slope is c_ε a instead.
These estimates are uniform in all interval endpoints and indices.

We use L324's rectangular integration-by-parts identity in the
following explicit form. With primitives anchored at the lower
endpoints, an amplitude A on a finite rectangle has signed integral
bounded by the product of the two primitive bounds times

    |A(upper corner)|
    +∫_{upper horizontal edge}|∂_u A|
    +∫_{upper vertical edge}|∂_v A|
    +∫_{rectangle}|∂_u∂_v A|.                        (7)

The lower-edge terms vanish by anchoring; both upper edges and the
corner are retained. Each unbounded limit below is justified by an
absolute-integrability bound, not a formal boundary deletion.

### 2. Complete coefficient mass and clipping tail

For nonnegative real L<2r put

    Q_*(L)=exp(L/2)(1−L/(2r))^(3r/4),

and extend it by zero. Since α≥3/4, the actual weight W is
pointwise bounded by the α=3/4 weight W_* with the same cutoff.
The inequality log(1−t)≤−t−t²/2 gives

    log Q_*(L)≤L/8−3L²/(32r)
               =r/24−3(L−2r/3)²/(32r)≤r/24.

The weights W_* decrease in each positive real coordinate. The
monotone sum-integral comparison, including the corner and both
coordinate edges, consequently gives

    M:=Σ_{j,k}W(j,k)
      ≤1+2∫₀^{2r}Q_*(L)dL+∫₀^{2r}LQ_*(L)dL
      ≤C(1+r)²exp(r/24).                             (8)

The density exp(L/2) comes from x=exp(u), y=exp(v) in
the double integral; it is not dropped.

Let b=19r/20. The complete discrete tail satisfies

    Σ_{max(log j,log k)≥b−ε}W(j,k)
       ≤C(1+r)²exp(−r/200).                          (9)

For completeness, set K=ceil(exp(b−ε)) and B=log(K−1).
Eventually B≥47r/50. The j≥K tail of W_* is bounded by
∫_B^{2r}(1+L)Q_*(L)dL, using the edge integral and the
double integral as in (8). On L≥47r/50,

    (log Q_*)'(L)=1/2−(3r/4)/(2r−L)≤−11/53.

Also Q_*(47r/50)=exp(r[47/100+(3/4)log(53/100)])
<exp(−r/200). This last strict rate is exact: with q=47/153,

    log(100/53)=2Σ_{k≥0}q^(2k+1)/(2k+1)
       >2(q+q³/3)>19/30,

where the final rational difference is 39877/107447310.
The same bound holds on the transposed tail. Integrating over
length at most 2r and using their union proves (9), including
indices with stationary points outside the retained domain.

### 3. Same-sign boundary strips

Set L₀=r/20 and V=101r/100. Gaussian moment summation in (5)
before estimating the polynomial gives, for e,f∈{0,1},

    Σ_{j,k}|∂_u^e∂_v^f A_jk(u,v)|
     ≤C exp(r−(u+v)/2)Σ_{ℓ=0}²|P^(ℓ)(u+v)|
       ·exp(−d[exp(2(u−r))+exp(2(v−r))]),             (10)

with fixed d=39/32. In detail the one-variable bound is
Σ_j(|B_j|+|B'_j|)≤C exp(5r−u/2)exp(−d exp(2(u−r))).
This follows by splitting exp(−htj²/2), t=exp(2(u−r)),
into two factors and applying
Σ_j j^q exp(−ctj²)≤C_{q,c}t^(−(q+1)/2), q=4,6,
to the remaining factor. The latter estimate follows by comparison
with the integral and maximum when t≤1, and by factoring an
exponential in t when t≥1, as proved in L324. Constants are
uniform since h stays in [39/8,5]. Product differentiation uses
only the three polynomial derivatives shown in (10).

On 0≤w=u+v≤53r/50, each polynomial term satisfies

    exp(r−w/2)|P^(ℓ)(w)|≤C exp(−r/200).              (11)

To verify uniformity, t=w/(2r)≤53/100. The prefactor
(m)_ℓ/(2r)^ℓ is bounded and t^(m−ℓ)≤t^(3r/4−ℓ).
The function t^(3r/4−ℓ)exp(r(1−t)) is increasing on
this interval once (11/50)r>2. At its upper endpoint (11)
follows from the exact logarithmic inequality used in (9).
The derivatives vanish at t=0 eventually.

For the high rectangles a global integrable bound is needed. Put
β=1−α, so 1/64≤β≤1/32. Equations (6) and (10) imply

    Σ_{j,k}|∂_u^e∂_v^f A_jk|
     ≤C exp(βr−β(u+v)/2)
       ·exp(−d[exp(2(u−r))+exp(2(v−r))])
     ≤C exp(r/4)exp(−(u+v)/128)
       ·exp(−d[exp(2(u−r))+exp(2(v−r))]).             (12)

In particular the exact series is absolutely integrable on the
whole quadrant for each parameter. Thus Tonelli and Fubini justify
termwise integration there.

On [0,L₀]×[0,V], (10)–(11) bound the sum of (7) by
C(1+r)²exp(−r/200). On [0,L₀]×[V,T], (12) bounds
it by C exp(r/4)exp(−d exp(r/50)), independently of T:
the edge and area integrals of exp(−(u+v)/128) are uniformly
bounded. This is O(exp(−r/200)). The two primitive bounds
supply a factor 1/a. Passage to T=∞ follows from the absolute
integrability above and Fatou for the sum of moduli. Transpose the
rectangles, subtract their intersection [0,L₀]², and restore
C₀exp(Φ_*) and the Jacobian 1/2. On

    B_+={u,v≥0:min(u,v)≤r/20}

we obtain

    Σ_{j,k}|∫_{B_+}F_jk ds dx|
       ≤C exp(Φ_*)(1+r)²exp(−r/200)/a.               (13)

This estimate keeps stationary points and every rectangular boundary;
it uses neither a divergent uncut index sum nor an absolute-integrand
estimate in place of the oscillatory factor 1/a.

### 4. Interior moving domains and nonstationary complement

In D_+={u>r/20,v>r/20}, set

    y=u−r+log j, z=v−r+log k,
    η_j=log j−b, η_k=log k−b.

The domain becomes y>η_j,z>η_k. Formula (5) becomes

    F_jk=C₀exp(Φ_*)exp(ia log(k/j))H_jk(y,z)
             ·exp(if_a(y)−if_a(z)),
    H_jk=(jk)^(−1/2)((2r−log(jk)+y+z)/(2r))^m
       ·exp((9/2)(y+z)−(h/2)(exp(2y)+exp(2z)−2))E,
    E=(1−3exp(−2y)/(2V_+))(1−3exp(−2z)/(2V_-)),
    V_±=πexp(2r±2iτ), |V_±|=sqrt(a²+h²)/2.           (14)

The polynomial argument is positive on this domain. The translation
has Jacobian one in du dv; ds dx still has factor 1/2.
From (6), the product rule and bounded E_j,E'_j on u≥0,

    |∂_y^e∂_z^f H_jk|
      ≤C(jk)^(−ν)M_h(y)M_h(z), e,f∈{0,1},
    ν=h−4=(1+α)/2≥7/8,
    M_h(t)=(1+exp(2t))exp(ht−(h/2)(exp(2t)−1)).       (15)

The index power is exact before its weakening to −7/8. In fact
the tangent exponential contributes (jk)^(−α/2) and changes
the linear coefficient 9/2 to h. No division by E or by the
polynomial is used in (15).

Define B_h(η)=sup_{t≥η}M_h(t)+∫_η^∞M_h(t)dt. Uniformly
in h∈[39/8,5],

    B_h(η)≤C (η≤0),
    B_h(η)≤C exp(−exp(2η)) (η≥0).                    (16)

Indeed q=exp(2t) changes M_h(t) into
exp(h/2)(1+q)q^(h/2)exp(−hq/2), with dt=dq/(2q).
Both the full supremum and integral are uniformly finite. For q≥1,
the polynomial factors, with or without division by q, can be
absorbed into exp((h/2−1)q) uniformly on this compact h interval.
Integrating the remaining exponential proves (16).

With J=exp(b), integral comparison gives

    Σ_j j^(−ν)B_h(η_j)
      ≤Σ_j j^(−7/8)B_h(log(j/J))≤C J^(1/8).          (17)

For j≤J use 1+∫₁^J x^(−7/8)dx. For j>J use the
decreasing majorant x^(−7/8)exp(−(x/J)²) and substitute
x=Jt in its integral. This controls the full infinite tail.
Equations (15)–(17) bound both summed absolute integrals and
summed rectangular variations on translated subrectangles by

    C J^(1/4)=C exp(19r/80).                          (18)

Thus absolute termwise integration in D_+ is valid at each parameter.

Assign to every pair the square Q={|y|,|z|≤ε}. Its complement
in the translated domain is a union of at most four rectangles:
the two y tails with all z, followed by the two z tails with
|y|≤ε. Empty rectangles contribute zero. One primitive in each
rectangle is O(1/a), the other O(a^(−1/2)). Equations (7)
and (18), followed by absolutely justified unbounded limits, give

    Σ_{j,k}|∫_{D_+\setminus Q}F_jk ds dx|
       ≤C exp(Φ_*)a^(−3/2)exp(19r/80).               (19)

Here Q is assigned separately in each pair's translated coordinates.
All finite moving edges and corners are included in (7); there is
no assertion that their amplitudes vanish.

### 5. Uniform full and clipped patches

A nonempty clipped patch requires log j,log k<b+ε. For these
indices let d_jk=2r−log(jk)>r/10−2ε≥r/11 eventually.
On the full fixed square factor (14) as H_jk=W(j,k)A E,
where

    A=exp(m log(1+(y+z)/d_jk)+(9/2)(y+z)
                 −(h/2)(exp(2y)+exp(2z)−2)).          (20)

On that square d_jk+y+z≥r/12 eventually, so
m/(d_jk+y+z)≤12 and m/(d_jk+y+z)²≤144/r.
The logarithmic term is bounded by the mean value theorem.
Consequently A and its first and mixed derivatives are uniformly
bounded, and A(0,0)=1. The factor E−1 and these derivatives
are O(1/a). The same bounds hold on every clipped rectangle.
Two unrestricted primitives and (7) therefore give the bound
C exp(Φ_*)W(j,k)/a for every clipped patch integral.

For clarity the full-square error is also quantitative. Use L325's
explicit real phase change

    Y=g(y), Z=g(z),
    g(t)=sgn(t)sqrt((exp(2t)−1−2t)/2), g'(0)=1.

The radicand divided by t² extends smoothly and positively
through zero, so the inverse and all derivatives needed on the fixed
interval are bounded. The opposite phases become −aY²+aZ²;
their constant phases cancel. After including the inverse Jacobians,
the transformed A has value one at zero and bounded first and
mixed derivatives and rectangular variation.

Put ρ=a^(−2/5). On |Y|,|Z|≤ρ replacing this amplitude
by one costs O(ρ³), by its Lipschitz bound and the area. The
remaining at most four rectangles cost O(a^(−3/2)/ρ): one
Fresnel tail primitive is O(1/(aρ)), the other O(a^(−1/2)),
and (7) retains their boundary terms. Extending the constant central
integral to the plane costs O(a^(−3/2)/ρ+a^(−2)/ρ²).
The product of opposite full Fresnel integrals is π/a, positive;
this is the scalar normalization from DLMF 7.2.6–7.2.9, with
the usual rescaling. The E−1 contribution is O(a^(−2)) by
its O(1/a) variation and two full primitive bounds. Therefore the
full assigned patch has integral

    C₀exp(Φ_*)exp(ia log(k/j))W(j,k)
                    ·[π/(2a)+O(a^(−11/10))].         (21)

The factor 1/2 is exactly ds dx=(1/2)dy dz. Indeed
ρ³=a^(−6/5), a^(−3/2)/ρ=a^(−11/10), and
a^(−2)/ρ²=a^(−6/5). All constants are uniform in every
potentially clipped index and admissible pair r,m.

If log j,log k<b−ε the full assigned square lies in D_+.
Summing (21) over those pairs costs, after normalization, at most
C(1+r)²exp(r/24)a^(−1/10), by (8). Every remaining
nonempty clipped patch belongs to the tail (9); the signed clipped
bound following (20) pays for all of them. Replacing the good-pair
leading sum by the entire finite S_{r,m} costs the same tail,
including all pairs with no nonempty patch. Adding (19) proves

    ∫_{D_+}F ds dx=C₀exp(Φ_*)π/(2a)[S_{r,m}+δ],
    |δ|≤C[(1+r)²exp(r/24)a^(−1/10)
            +(1+r)²exp(−r/200)
            +exp(19r/80)a^(−1/2)].                   (22)

No limit for a fixed index has been interchanged with the growing
sum. The complete masses and tails have been bounded first.

### 6. Mixed sectors, reflection and assembly

Since 39/8≤h≤5, m=2n and h−9/2=n/r exactly,
C294b applies to both mixed sectors at these same parameters.
It includes absolute termwise integrability and all boundary terms,
and bounds each sector integral by

    C exp(Φ_*)exp(−γ₀r)/a,
    γ₀=(3/4)log 2−1/2>1/54>1/200.                   (23)

No fixed-height-index relation beyond C294b's hypotheses is added.

The positive and negative same-sign quadrants, each partitioned
into its r/20 interior and strips, and the two mixed sectors
partition the plane except for null boundaries. Evenness of k and
evenness of m give F(−s,x)=F(s,x) exactly. This reflection has
absolute Jacobian one and maps the two positive same-sign pieces
to their negative-quadrant counterparts. Thus (22) is doubled
once, changing π/(2a) to π/a. The factors 1/2 in (13),
(22) and C294b already incorporate their coordinate Jacobians.

After division by C₀exp(Φ_*)π/a, (13), (22) and (23)
give (1). To compare every complete error, use (3):

    exp(r/24)a^(−1/10)=O(exp(−19r/120)),
    exp(19r/80)a^(−1/2)=O(exp(−61r/80)).              (24)

The rates 19/120, 61/80 and γ₀ all exceed 1/200.
The high-strip double exponential from (12) is smaller still.
All constants and sufficiently-large-r conditions above are uniform
on the closed α band, so their finitely many onsets have one
common maximum R. There is no excluded band endpoint or integer
cutoff transition.

Interchanging j,k conjugates the finite sum and leaves its weight
and cutoff unchanged; hence S_{r,m} is real. The original
real-contour integral in (4) is real by conjugation and t↦−t.
Thus the error in (1) is real. Finally (4) supplies exactly (2),
with no further factorial, reflection or change-of-variables factor.
This proves the reduction. ∎

L454's separately conditional arithmetic margin is a possible
downstream input, not a premise used above. Combining and auditing
that application is separate from this reduction. No additional
Laguerre sign or zero-exclusion range is claimed here. Smaller
indices, bounded exterior heights, global mixed positivity and the
selected-law/regulator gaps remain unresolved. L323's r/4 strip
obstruction and L327's fixed-band Gram obstruction are preserved;
this proof uses r/20 and retains the original signed sum.

### Separate critical audit — 2026-10-23

Verdict: (1)–(2) pass on the entire stated band, with one C,R.
This review uses the unchanged SPECIALIZE
[audit assessment](../drafts/literature/2026-10-23-subendpoint-uniform-sector-critical-audit-coverage.md).
It checks the explicit proof rather than treating a general stationary
phase citation or fixed-exponent predecessor as a uniform theorem.
The following are checks of the displayed argument, not additional
lemmas or a downstream application.

**Exact identities and domains.** The actual h interval is
[319/64,639/128], contained in [39/8,5]. L269's contour passage
uses only the fixed-parameter smaller-strip domination, which remains
valid here; its proportional-index asymptotic is not used. The strip
evenness and theta series in its inputs give (5) with no residual
phase: the two factors exp(±9iτ/2) cancel. Translation in (14)
gives j⁴exp(−(9/2)log j)=j^(−1/2) in each variable and
the constant phase exp(ia log(k/j)). Thus the weight, carrier and
cutoff match the stated S exactly.

**Mass and cutoff.** For 0≤L<2r, α≥3/4 makes W≤W_*;
both are zero at and beyond 2r. The two monotone integral comparisons
in (8) include the integer corner, coordinate edges and density
exp(L/2). For the clipping tail the first integration starts at K−1,
not K, so it covers the first retained integer, including equality at
the threshold. Its lower logarithmic endpoint is eventually at least
47r/50 independently of m. The exact positive rational difference
39877/107447310 in (9) yields a strict rate greater than 1/200.
This verifies the tail of the full discrete mass, not just a continuum
or fixed-index approximation.

**Boundary strips and derivatives.** Differentiating B_j introduces
only the Gaussian fourth/sixth moments and bounded E_j,E'_j.
The mixed derivative of A_jk uses precisely P,P',P''; the bound
t^(m−ℓ)≤t^(3r/4−ℓ) is applied only for 0<t≤53/100.
The endpoint t=0 has vanishing derivatives once m>2. These facts
justify the summed derivative estimate (10) and the low-rectangle
variation, including its two edges and corner. On the high rectangles,
β∈[1/64,1/32] gives exp(βr−βw/2)≤exp(r/4−w/128).
The second Gaussian is at most exp(−d exp(r/50)); every remaining
edge/area integral is uniformly finite. Parameterwise absolute
integrability permits the infinite-rectangle limit, while Fatou
retains the sum of moduli. The intersection of the two strips is
subtracted once. No boundary is silently discarded.

**Translated complement.** The tangent bound changes the index power
to −ν=−(1+α)/2 and the linear exponent to h. Bounded original
E_j,E'_j suffice on the actual translated domain; no global bound on
exp(−2y)/a on the whole real line is assumed. Both the supremum and
integral in B_h are necessary for corners and edges. Their Gaussian
tail gives the full infinite sum (17), including j>exp(b) and
nonintegral exp(b), and hence exp(19r/80) in (18). Each of the
at most four complement rectangles has one nonstationary primitive;
anchoring at its actual finite lower endpoint retains all moving-edge
terms. The resulting normalized cost is exp(19r/80)a^(−1/2).

**Full and clipped squares.** Every nonempty clipped square satisfies
d_jk>r/10−2ε. Throughout its full assigned square,
d_jk+y+z≥r/12 eventually. In particular the logarithmic derivatives
of A have the explicit forms

    (log A)_y=m/(d_jk+y+z)+9/2−h exp(2y),
    (log A)_yy=−m/(d_jk+y+z)²−2h exp(2y),
    (log A)_yz=−m/(d_jk+y+z)²,

and the corresponding z formulas. They are uniformly bounded, as is
A itself by the mean value bound on its exponent. The lower-order
theta correction E−1 and its first/mixed derivatives are
O(a^(−1)) on this fixed square. The smooth coordinatewise inverse
of g preserves the needed first and mixed variation bounds and the
central value one, since g'(0)=1. With ρ=a^(−2/5), the absolute
central replacement costs a^(−6/5); the signed exterior rectangles
cost a^(−11/10), retaining corners and edges. The two opposite
Fresnel factors multiply to π/a; the coordinate Jacobian makes this
π/(2a). These are per-weight estimates uniform over every potentially
clipped pair, so multiplication by (8) is legitimate. Pairs on the
good-pair boundary are assigned to the tail, and equality at b+ε
leaves a patch of zero area. If log(jk)≥2r, no nonempty patch is
possible eventually; its actual summand is still covered by (19).
Thus the arithmetic cutoff does not delete an uncontrolled integral.

**Mixed sectors and final normalization.** C294b's full proof applies
with p=m and H=m/(2r); its Gaussian sum, polynomial derivatives,
integrable positive-tail exponent and vanishing infinite edges are
uniform on the containing h interval. It supplies γ₀>1/54, with
its Jacobian already present. The reflection s↦−s swaps the two
kernel factors exactly and preserves s^m, doubling the same-sign
contribution once. An independent check of L269's coefficient identity
starts from the whole-line transform 2Ξ: its product contributes
4D_n, the linear variable change contributes 2, and the power gives
2^m. Therefore D_n=2^(m−1)I_n/m!, as in (4).

After the single reflection the normalization is C₀exp(Φ_*)π/a.
The complete normalized errors have rates 19/120, 1/200, 61/80
and γ₀>1/54, with at most (1+r)², and a faster high-strip
double exponential. These follow from a≍exp(2r), uniformly in m/r.
Every derivative condition, patch containment and comparison uses
only a fixed eventual lower bound on r; their finite maximum gives
one R. The cutoff equalities and closed band endpoints are included.
Reality follows from conjugate index interchange and the real-contour
integral. No discrepancy in constants, factorials or reflection was
found, and no repair of the theorem statement was necessary.

This validates a local reproduction of the assessed methods, not a
new sign theorem or progress beyond the checked source mechanisms.
The external zero-free premise is absent from this proof. L454's
conditional sign application, smaller indices, bounded exterior
heights and global mixed positivity remain outside this verdict.
The L323 and L327 obstructions retain their original scopes.

## Mathlib

Full matching Mathlib coverage has not been checked; absence is not
asserted. Supporting Gaussian moment sums, monotone integral comparison,
Fresnel integrals, rectangular integration by parts and Tonelli/Fubini
coverage have not been checked here. The exact contour and coefficient
identity come from L269; the explicit Gaussian-sum and rectangular
methods come from L324, the phase change and scalar stationary
calculation from L325, and the already uniform mixed-sector theorem
from C294b. The scalar Fresnel reference is
[NIST DLMF §7.2(iii), equations 7.2.6–7.2.9](https://dlmf.nist.gov/7.2#iii),
as inspected in the approved assessment on 2026-10-23. No unseen general
parameter-dependent stationary-phase theorem is invoked. The changed
mass, tail, derivative and domain bounds and their assembly are
proved above because the older fixed-exponent conclusions do not
state this uniform theorem.
