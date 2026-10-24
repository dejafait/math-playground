# Lemma 458: lower-band whole-plane theta reduction

## Hypotheses

Use the actual even theta kernel k and transform Ξ, with the
normalization of L269 and L455:

    Ξ(a+iy)Ξ(a−iy)=Σ_{n≥0}D_n(Ξ;a)y^(2n).

Let r tend to infinity through positive real values and m be a positive
even integer satisfying

    7/8≤α=m/r≤31/32, n=m/2,
    h=9/2+α/2, a=sqrt(4π²exp(4r)−h²)>0,
    τ=arctan(a/h)/2, Φ_*=m log r+9r−h−2aτ,
    C₀=(8π²)².

Define exactly the finite signed sum in L457:

    W(j,k)=(jk)^(−1/2)(1−log(jk)/(2r))_+^m,
    S_{r,m}(a)=Σ_{j,k≥1}W(j,k)exp(ia log(k/j)).

The weight is zero when log(jk)≥2r, including equality. No external
zero-free premise or arithmetic sign is assumed.

## Conclusion

There are fixed C,R>0, independent of r,m throughout this closed band,
such that for every admissible r≥R,

    D_{m/2}(Ξ;a)=P_{r,m}(S_{r,m}(a)+ε_{r,m}),
    P_{r,m}=[2^(m−1)/m!]C₀exp(Φ_*)π/a>0,
    ε_{r,m} real, |ε_{r,m}|≤C(1+r)²exp(−r/200).       (1)

This is an additive theta reduction. The separate critical audit below
validates it on its full closed band. It establishes neither a Laguerre
sign nor an every-height assertion.

## Proof

The prior SPECIALIZE
[coverage assessment](../drafts/literature/2026-10-23-lower-band-whole-plane-theta-coverage.md)
covers this target. We specialize L455's explicit proof bounds, rather
than applying its narrower theorem statement. The only new domain
check in its high-strip estimate is supplied below. All other parameter
restrictions are recorded explicitly, so the proof does not extrapolate
a fixed-index asymptotic. This is reproduction of the assessed methods;
no originality is claimed.

### 1. Exact identity, amplitudes and signed primitives

On the present domain

    3/4≤α≤1, 79/16≤h≤319/64, [79/16,319/64]⊂[39/8,5],
    β:=1−α∈[1/32,1/8], a≍exp(2r),
    2πexp(2r+2iτ)=h+ia.                              (2)

Only the parameterwise contour passage in L269 is used, not its
proportional-index asymptotic. At each fixed r,m, τ<π/4, and the
smaller closed strip gives polynomially weighted superexponential
domination, including the vertical edges. Fubini and the shift give

    I=exp(−2aτ)∫_{ℝ²}s^m k(s+x+iτ)k(s−x−iτ)
                                      exp(2iax)ds dx,
    D_{m/2}(Ξ;a)=2^(m−1)I/m!.                        (3)

For u=s+x≥0, v=s−x≥0 the area Jacobian is 1/2. The exact
theta expansion used in L455 (5) has summands

    F_jk=C₀exp(Φ_*)A_jk(u,v)exp(iφ_j(u)−iφ_k(v)),
    A_jk=exp(−9r+h)P(u+v)B_j(u)overline(B_k(v)),
    P(w)=(w/(2r))^m,
    B_j(u)=j⁴exp(9u/2−(h/2)j²exp(2(u−r)))E_j(u),
    E_j(u)=1−3/(2πj²exp(2u+2iτ)),
    φ_j(u)=au−πsin(2τ)j²exp(2u).                     (4)

The theta phases exp(±9iτ/2) cancel. On u≥0 both E_j and
E'_j have uniform bounds. For ℓ=0,1,2,

    |P^(ℓ)(w)|≤C exp((α/2)(w−2r)), w≥0.             (5)

Indeed, for t=w/(2r)>0 divide by the exponential on the right.
The result is (m)_ℓ/(2r)^ℓ t^(m−ℓ)exp(−m(t−1)); its
maximum is at t=1−ℓ/m and is uniformly bounded because m/r≤1.
For sufficiently large r, m>2 and continuity gives zero derivatives
of the relevant orders at w=0. This proves all boundary versions too.

Translation y=u−r+log j changes φ_j up to a constant into
f_a(y)=a(y−exp(2y)/2). L455's primitive proof applies unchanged:
on every finite interval either sign has integral at most C/sqrt(a),
and on a single side of |y|≤ε, ε=1/100, at most C/a.
For completeness, remove |y|≤a^(−1/2), then use the monotonic
derivative a(1−exp(2y)); integration by parts bounds each remaining
integral by endpoint reciprocal slopes and their variation. The slopes
are at least c sqrt(a), or c_ε a on the fixed exterior sides.
These constants do not involve α or the translated endpoints.

Two primitives anchored at the finite lower endpoints bound a signed
rectangular integral by their product bound times

    V(A)=|A(upper corner)|+∫_{upper edge}|A_u|
                    +∫_{other upper edge}|A_v|+∫∫|A_uv|. (6)

This is two integrations by parts. Lower terms vanish by anchoring;
the two upper edges and corner are included. All infinite-rectangle
limits below have an absolute-integrability majorant.

### 2. Complete mass, discrete tail and boundary strips

The elementary mass and tail bounds L455 (8)–(9) require only
α≥3/4 and the original product cutoff. Here is their domain check.
Writing L=log(jk), dominate W by the α=3/4 weight and put

    Q_*(L)=exp(L/2)(1−L/(2r))^(3r/4), 0≤L<2r.

It is zero thereafter, and
log Q_*≤L/8−3L²/(32r)≤r/24. Monotone comparison of both
integer coordinates with integrals, keeping the corner and both edges,
therefore gives

    ΣW≤1+2∫₀^{2r}Q_*+∫₀^{2r}LQ_*
       ≤C(1+r)²exp(r/24).                            (7)

Set b=19r/20. In the discrete tail log j≥b−ε start the
comparison at K−1, where K=ceil(exp(b−ε)). Eventually
B=log(K−1)≥47r/50. The edge and double integrals are bounded
by ∫_B^{2r}(1+L)Q_*(L)dL. On this interval
(log Q_*)'≤−11/53 and Q_*(47r/50)<exp(−r/200).
The last inequality follows exactly from log(100/53)>19/30:
with q=47/153, the first two positive terms of its logarithmic
series give 2(q+q³/3)−19/30=39877/107447310>0.
Transpose and take the union to obtain

    Σ_{max(log j,log k)≥b−ε}W
                   ≤C(1+r)²exp(−r/200).              (8)

These bounds include the cutoff equality, where W=0.

Let L₀=r/20, V=101r/100. Gaussian moment summation in (4),
before bounding P, gives for e,f∈{0,1}, with d=39/32,

    Σ|∂_u^e∂_v^f A_jk|
      ≤C exp(r−(u+v)/2)Σ_{ℓ=0}²|P^(ℓ)(u+v)|
        ·exp(−d[exp(2(u−r))+exp(2(v−r))]).            (9)

This is precisely L455 (10): the one-variable fourth/sixth Gaussian
moments give Σ_j(|B_j|+|B'_j|)≤Cexp(5r−u/2)
exp(−d exp(2(u−r))). Their constants are uniform on [39/8,5],
which contains (2); differentiating P needs only its displayed three
orders. The Gaussian bounds follow by scaling its moment integral and
maximum for exp(2(u−r))≤1, and by extracting the exponential for
larger arguments. Thus no index sum at a fixed index replaces (9).

For w=u+v≤53r/50,

    exp(r−w/2)|P^(ℓ)(w)|≤Cexp(−r/200).              (10)

To check this, t=w/(2r)≤53/100 and
t^(m−ℓ)≤t^(3r/4−ℓ). The product t^(3r/4−ℓ)exp(r(1−t))
is increasing up to 53/100 for large r. Its endpoint has the strict
exponential rate just proved for (8); the factor t^(−ℓ) there is
a fixed constant. The endpoint t=0 is covered by continuity.

For high strips the changed beta domain must be checked afresh.
Equations (5) and (9) imply the global integrable majorant

    Σ|∂_u^e∂_v^f A_jk|
      ≤Cexp(βr−β(u+v)/2)
           exp(−d[exp(2(u−r))+exp(2(v−r))])
      ≤Cexp(r/4−(u+v)/128)
           exp(−d[exp(2(u−r))+exp(2(v−r))]).          (11)

The second inequality follows from β≤1/8≤1/4 and
β/2≥1/64≥1/128, for every u,v≥0. It does not use L455's
old beta interval. It proves absolute termwise integrability at each
parameter as well as uniform edge and area estimates.

On [0,L₀]×[0,V], (9)–(10) bound the summed (6) by
C(1+r)²exp(−r/200). On [0,L₀]×[V,T], (11) bounds it by
Cexp(r/4−d exp(r/50)), uniformly in T; the remaining integrals
of exp(−(u+v)/128) are bounded. Use two C/sqrt(a) primitives,
then let T→∞ using absolute integrability and Fatou for the sum of
moduli. Transpose the rectangles and subtract the intersection once.
Restoring the Jacobian and C₀exp(Φ_*), the complete strip union
B_+={u,v≥0:min(u,v)≤r/20} satisfies

    Σ|∫_{B_+}F_jk ds dx|
      ≤Cexp(Φ_*)(1+r)²exp(−r/200)/a.                (12)

The faster high-strip error has been absorbed. Every finite boundary
term is retained through (6).

### 3. Translated interior, full infinite complement and patches

In D_+={u,v>r/20}, use y=u−r+log j, z=v−r+log k.
The domain is y>η_j=log j−b, z>η_k=log k−b. The exact
translated amplitude H_jk from L455 (14) is

    H_jk=(jk)^(−1/2)((2r−log(jk)+y+z)/(2r))^m
       ·exp((9/2)(y+z)−(h/2)(exp(2y)+exp(2z)−2))E,
    E=(1−3exp(−2y)/(2V_+))(1−3exp(−2z)/(2V_-)),
    V_±=πexp(2r±2iτ).

The carrier is exp(ia log(k/j))exp(if_a(y)−if_a(z)).
On this domain the polynomial argument is positive. Applying (5)
and the bounded original E_j,E'_j gives

    |∂_y^e∂_z^f H_jk|≤C(jk)^(−ν)M_h(y)M_h(z),
    ν=(1+α)/2≥15/16≥7/8,
    M_h(t)=(1+exp(2t))exp(ht−(h/2)(exp(2t)−1)).       (13)

This is L455 (15) with its exact exponent retained before weakening.
The tangent polynomial changes the linear coefficient to h and the
index power to −ν. No division by the polynomial or by E is used.
The original bounds on E_j are invoked only on u,v≥0.

For B_h(η)=sup_{t≥η}M_h(t)+∫_η^∞M_h(t)dt,

    B_h(η)≤C for η≤0, B_h(η)≤Cexp(−exp(2η)) for η≥0.

Substitution q=exp(2t) proves both statements uniformly on [39/8,5]:
the full integral and supremum are finite and the polynomial factors
are absorbed by exp((h/2−1)q) on q≥1. Put J=exp(b). The
head sum of j^(−7/8) is O(J^(1/8)); its full tail weighted by
exp(−(j/J)²) is also O(J^(1/8)), by integral comparison.
Consequently (13) bounds the total integrals and rectangular variations
on arbitrary translated subrectangles by C J^(1/4)=Cexp(19r/80).
This includes all growing and exterior indices and proves the needed
parameterwise absolute termwise integrability.

Assign Q=[−ε,ε]² separately to each index pair. Its complement
in the translated domain is at most four rectangles. Each has one
primitive O(1/a) and one O(a^(−1/2)). Equation (6) now gives

    Σ|∫_{D_+ outside assigned Q}F_jk ds dx|
                ≤Cexp(Φ_*)a^(−3/2)exp(19r/80).      (14)

All moving edges and corners are included. Unbounded limits are
legitimate by (13); no boundary amplitude is assumed zero at a finite
edge, and no divergent uncut power sum is used.

For every nonempty clipped patch, log j,log k<b+ε. Thus
d_jk=2r−log(jk)>r/10−2ε and throughout its full assigned square
d_jk+y+z≥r/12 eventually. Factor H_jk=W(j,k)A E with

    A=exp(m log(1+(y+z)/d_jk)+(9/2)(y+z)
                                  −(h/2)(exp(2y)+exp(2z)−2)).

The mean value theorem bounds its logarithm, and

    (log A)_y=m/(d_jk+y+z)+9/2−h exp(2y),
    (log A)_yz=−m/(d_jk+y+z)².

Together with the analogous z and pure second derivatives, m≤r
and h∈[39/8,5] give bounded first and mixed derivatives and
variation of A. Also A(0,0)=1. On this full fixed square E−1
and its needed derivatives are O(1/a). Equation (6) therefore bounds
every clipped patch by Cexp(Φ_*)W(j,k)/a.

For the full square use the exact real change

    Y=g(y), Z=g(z),
    g(t)=sgn(t)sqrt((exp(2t)−1−2t)/2), g'(0)=1.

Its inverse and needed derivatives are bounded on this fixed interval.
The opposite phases become −aY²+aZ², with cancelling constants;
the transformed amplitude, including inverse Jacobians, equals one
at the origin and has bounded first and mixed variation. For
ρ=a^(−2/5), the central amplitude replacement costs O(ρ³).
In the exterior rectangles use one Fresnel tail primitive
O(1/(aρ)) and one full primitive O(a^(−1/2)), with (6).
The constant central Gaussian extends to the plane with error
O(a^(−3/2)/ρ+a^(−2)/ρ²). The opposite full Fresnel factors
multiply to π/a, by DLMF §7.2(iii), (7.2.6)–(7.2.9), as
inspected in the assessment; no parameter-uniform source theorem is
being assumed. The E−1 variation costs O(a^(−2)). Therefore
each full patch, including its area Jacobian, is

    C₀exp(Φ_*)exp(ia log(k/j))W(j,k)
                         [π/(2a)+O(a^(−11/10))].    (15)

All constants are uniform over potentially clipped pairs.

If both log indices are <b−ε the full square is inside D_+.
Sum their errors using (7). All other nonempty clipped patches are
in (8), which pays for their integrals and for replacing the good-pair
leading sum by the entire S. Equality at b−ε is assigned to the
tail; equality at b+ε has zero patch area. If log(jk)≥2r no
patch can be nonempty for large r, because 2b+2ε<2r, but its
integral remains in (14). Thus the product cutoff deletes no integral
from the error accounting. We obtain

    ∫_{D_+}F ds dx=C₀exp(Φ_*)π/(2a)(S+δ),
    |δ|≤C[(1+r)²exp(r/24)a^(−1/10)
          +(1+r)²exp(−r/200)+exp(19r/80)a^(−1/2)].   (16)

### 4. Mixed sectors, positive normalization and one onset

The entire h interval in (2) lies in C294b's hypotheses, and
h−9/2=m/(2r)=n/r exactly. That theorem therefore bounds each
whole mixed sector, including its area Jacobian, by

    Cexp(Φ_*−γ₀r)/a,
    γ₀=(3/4)log 2−1/2>1/54.                         (17)

Its proof retains both finite-boundary primitives, the summed Gaussian
variation and all infinite-edge limits; no extension of its domain is
needed. This is a direct use of its conclusion.

The two same-sign quadrants and two mixed sectors partition the plane
up to null boundaries. Evenness of k and evenness of m imply that
the shifted integrand satisfies F(−s,x)=F(s,x). Reflection has
absolute Jacobian one and takes the positive same-sign quadrant onto
the negative one. It doubles (16) once, taking π/(2a) to π/a.
There is no second reflection factor. Add both strip errors (12) and
both mixed sectors (17), then divide by C₀exp(Φ_*)π/a.
Every complete normalized error is covered by

    C[(1+r)²exp(r/24)a^(−1/10)
      +(1+r)²exp(−r/200)+exp(19r/80)a^(−1/2)
      +exp(−γ₀r)+exp(r/4−d exp(r/50))].             (18)

Uniformly by (2), the first exponential rate is 19/120 and the
third is 61/80. Both exceed 1/200, as does γ₀>1/54;
the high-strip term is faster still. Hence (18) is at most
C(1+r)²exp(−r/200). The finitely many lower bounds on r in the
argument have a common maximum independent of the closed-band
parameters; this yields one R and one C. No integer cutoff transition
or band endpoint is omitted.

Interchanging j,k conjugates S without changing its weights, so S
is real. The original real-contour I is real by conjugation and
t↦−t. Thus the error is real. Finally the exact coefficient factor
in (3) yields P in (1). Independently, the whole-line transform is
2Ξ and its product has coefficient 4D_n. For its original kernel
variables p,q, set s=(q−p)/2, t=(q+p)/2: the Jacobian is 2,
the coefficient power (q−p)^m is (2s)^m, and evenness gives
k(t−s)=k(s−t). Thus 4D_n=2^(m+1)I/m!, consistent with (3). Every
factor in P is strictly positive. This proves (1). ∎

L457 is a prospective downstream arithmetic input, not a premise of
this proof. Its conditional sign assembly and an every-height transfer
are not performed. L323's r/4 strip failure and L327's Gram obstruction
are preserved: this proof uses r/20 and the full original signed sum.
Smaller indices, bounded heights, global mixed positivity and the
selected-law/regulator gaps remain unresolved. This partial reduction
is not a candidate resolution of RH.

### Separate critical audit — 2026-10-24

Verdict: (1) passes on the entire stated real-r/even-m domain, with
one C,R. This audit uses the unchanged SPECIALIZE
[assessment](../drafts/literature/2026-10-24-lower-band-theta-critical-audit-coverage.md),
whose TARGET is exactly the action at invocation start. It independently
checks the written lower-band proof; L455's narrower correctness verdict
is not applied as a theorem on this band. No repair of (1), new direct
mathematical input or downstream sign assembly is needed.

**Exact identity and changed domain.** The endpoints are
h=79/16 and 319/64, inside [39/8,5], with
beta=1-alpha in [1/32,1/8]. In L269 the shift/Fubini argument
precedes and is independent of its proportional-index asymptotic.
At each fixed parameter the smaller strip has positive cosine and
polynomially weighted superexponential domination; it suffices for
(3), without a bound uniform as tau tends to pi/4. Direct substitution
of the theta summands gives (4): the two exp(±9i tau/2) factors
cancel, and translation supplies j^4 exp(-(9/2)log j)=j^(-1/2)
and the carrier exp(ia log(k/j)). Also
pi sin(2tau) exp(2r)=a/2, giving exactly f_a in each variable.
The displayed amplitude, saddle relation and finite arithmetic sum
therefore have no shifted exponent or residual constant phase.

**Complete discrete mass and cutoffs.** W is decreasing in each
positive coordinate and is bounded by the 3r/4-exponent weight,
including zero at log(jk)=2r. The sum-integral comparison in (7)
includes the corner, both edges and the double-integral density L.
Its log-density bound is
L/8-3L^2/(32r)=r/24-3(L-2r/3)^2/(32r).
For the tail the first interval starts at K-1, covering the first
retained integer even when exp(b-epsilon) is integral. Its logarithm
is eventually at least 47r/50, uniformly in m. The edge plus double
integral is bounded by the stated integral of (1+L)Q_*.
The logarithmic slope there is at most -11/53, and the exact positive
rational difference in (8) proves a rate strictly better than 1/200.
The transposed tail covers every nongood pair, including those with
no patch. These are bounds for the complete discrete sums, rather
than continuum approximations to a growing family.

**Strip derivatives, integrability and boundaries.** Differentiating
B_j uses bounded E_j,E'_j and only the fourth and sixth Gaussian
moments; splitting the Gaussian leaves d=39/32 uniformly on the
containing h band. Product differentiation uses exactly P,P',P''.
For 0<t<=53/100 the low-strip derivative bound reduces to
t^(3r/4-ell) exp(r(1-t)); it is increasing eventually, and its
endpoint exponent is the same strict negative exponent as in (8).
At t=0 all relevant derivatives vanish once m>2.

In the high-strip bound (11), beta<=1/8 gives beta*r<=r/8,
and beta/2>=1/64. Thus the weaker displayed
exp(r/4-(u+v)/128) bound holds throughout the new band.
When v>=101r/100 the Gaussian supplies
exp(-d exp(r/50)); every remaining edge and area integral is
uniformly finite. Equation (6) retains both upper edges and the
corner, and anchored primitives remove only the lower terms.
Absolute integrability justifies each infinite limit and Fatou the
sum of moduli. The strip intersection is itself a low rectangle;
its signed integral is bounded before the triangle inequality is
applied to the union. This verifies (12) without subtracting moduli
or silently dropping a boundary.

**Entire translated complement.** The tangent exponential changes
the exact index power to -(1+alpha)/2 and the linear exponent to h.
In particular nu>=15/16, so the weaker summable-with-tail comparison
using 7/8 is legitimate. Bounds on the original E_j,E'_j are used
only in the actual translated domain. Both the supremum and integral
in B_h are finite uniformly; after q=exp(2t), the remaining
polynomial is absorbed by exp((h/2-1)q), whose exponent stays
positive by a fixed amount. For j>exp(b), the retained
exp(-(j/exp(b))^2) factor controls the full infinite tail.
The head and tail each cost O(exp(b/8)), so their product costs
exp(19r/80), also for nonintegral exp(b).

For each index pair the complement of its assigned square is at most
four rectangles, with their actual moving endpoints. Each has one
fixed-exterior primitive O(a^(-1)) and one unrestricted primitive
O(a^(-1/2)). The rectangular variation is bounded by (13) before
summing; finite corners and edges survive until (6) bounds them.
The same majorant justifies unbounded limits. This proves the full
budget (14), including stationary centers outside the sector.

**Uniform full and clipped patches.** Nonempty patches satisfy
d_jk>r/10-2epsilon, hence d_jk+y+z>=r/12 on their full assigned
square eventually. The logarithmic derivatives in Section 3 and
(log A)_yy=-m/(d_jk+y+z)^2-2h exp(2y), together with the
z analogue, are uniformly bounded since m<=r. The exponent itself
is bounded by the mean value theorem. Thus A, its needed derivatives
and variation have one bound for every potentially clipped pair.
On the same fixed square E-1 and its first/mixed derivatives are
O(a^(-1)), independently of the indices.

The radicand defining g, divided by t^2, is smooth and strictly
positive through zero. The coordinatewise inverse has bounded
derivatives, g'(0)=1, and its Jacobians preserve the central amplitude
one and bounded first/mixed variation. In the central square
rho=a^(-2/5), absolute amplitude replacement costs rho^3=a^(-6/5).
Every exterior rectangle has a Fresnel tail primitive
O(1/(a*rho)) and a full primitive O(a^(-1/2)), costing
a^(-11/10) with the retained edges and corners. Extending the
constant central Gaussian adds at most
O(a^(-3/2)/rho+a^(-2)/rho^2); the latter term is a^(-6/5).
The E-1 variation costs O(a^(-2)). The opposite scalar Fresnel
factors multiply to pi/a, and ds dx=(1/2)dy dz gives pi/(2a).
This verifies the per-weight expansion (15) before multiplication
by the complete mass (7).

Equality at b-epsilon belongs to the tail (8); equality at
b+epsilon leaves zero patch area. Every nonempty patch has
log(jk)<2b+2epsilon<2r eventually. Consequently the product-cutoff
equality cannot hide an omitted patch, and the corresponding actual
summand remains covered by the complement (14). Both replacement
of clipped patches and completion to the full finite S are paid for
by the same discrete tail. This verifies all terms of (16).

**Mixed sectors, normalization and common onset.** C294b's proof
applies with p=m and H=m/(2r) on this containing h interval.
Its Gaussian sum and polynomial derivative bounds remain uniform;
its positive-tail exponent 2H-1/2 lies in [1/4,1/2], which gives
an integrable common majorant. The two anchored primitives and the
vanishing superexponential upper edges justify its whole-sector
bound including the Jacobian 1/2. Its exact inequality
log 2>56/81 gives gamma_0>1/54>1/200. No h>5 statement is
used here.

Evenness of k and even m give F(-s,x)=F(s,x) exactly. This
maps the positive same-sign quadrant to the negative one and doubles
pi/(2a) once. Independently the whole-line transform 2Xi gives
coefficient 4D_n; the original linear change of kernel variables has
Jacobian 2 and power factor 2^m. It follows that
4D_n=2^(m+1)I/m!, consistent with (3) and the stated P.
There is no additional sign, factorial or reflection factor.

Uniformly a is comparable to exp(2r). The complete normalized
patch-mass and complement errors therefore have decay rates
1/5-1/24=19/120 and 1-19/80=61/80. The clipping and strip
rate is 1/200, the mixed-sector rate exceeds 1/54, and the
high-strip double exponential is faster. Each meets (1), with at
most (1+r)^2. All eventual conditions used above depend only on
fixed containing intervals, m>=7r/8 and finitely many thresholds
on r; their maximum is a common R. This covers all admissible real
r, even m, closed-band endpoints and integer cutoff transitions.
Conjugate interchange of j,k makes S real, and the original
real-contour integral is real, so epsilon is real. Every factor
in P is strictly positive.

The audit validates a local reproduction of the assessed methods,
with no mathematical discovery beyond the checked source mechanisms.
It imports no zero-free premise and proves no arithmetic margin,
Laguerre sign, every-height transfer or RH consequence. L323's
larger-strip failure and L327's PSD obstruction keep their original
scopes. All remaining low-index, bounded-height and mixed-positivity
gaps are unchanged.

## Mathlib

Full matching coverage has not been checked; absence is not asserted.
Supporting contour shifts, theta identities, Gaussian moment sums,
Fresnel integrals, rectangular integration by parts and Tonelli/Fubini
coverage have not been checked here. The scalar Fresnel input is
[NIST DLMF §7.2(iii), equations 7.2.6–7.2.9](https://dlmf.nist.gov/7.2#iii).
The assessed Csordas coefficient identity, *Fourier transforms of
positive definite kernels and the Riemann ξ-Function*,
[arXiv:1309.0055v2](https://arxiv.org/html/1309.0055v2),
Lemma 3.6 and Theorem 3.7, (3.10)–(3.14), is used only through
the already normalized local identity (3), not as a positivity theorem.
The proof gives the changed-domain uniform estimates because neither
that source nor L455's narrower conclusion states this result.
