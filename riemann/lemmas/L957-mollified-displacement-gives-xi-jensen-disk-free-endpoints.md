# Lemma 957: a mollified displacement bound gives actual-Xi disk-free endpoints

## Hypotheses

Let ζ be the Riemann zeta function and Ξ(z)=ξ(1/2+iz), with the exact
zero correspondence and strict strip of L018. Count zeros with their
full orders. For real T tending to infinity put

    W_T = sum_{β>1/2, T-1<=γ<=2T+1} m(β+iγ)(β-1/2),

where the sum is over distinct nontrivial ζ zeros. Let J(Ξ) be the
union of the closed disks centered at Re z with radius |Im z|, over
nonreal Ξ zeros z. A conjugate pair supplies the same disk twice; the
union counts it once. No RH, simplicity, zero separation, or assumption
about zeros of a mollifier is made.

## Conclusion

As T tends to infinity through all real values,

    W_T <= (log(5)/(4π)) T + O(T/log T).

Consequently W_T<=T/4 for all sufficiently large T, and

    meas([T,2T] intersect J(Ξ)) <= 2W_T <= T/2.

In particular there is a real t_T in (T,2T) outside every closed Ξ
Jensen disk, and it may also be chosen with Ξ(t_T)≠0. The onset is not
made effective here. This is an unconditional, known-method
specialization, accepted by the focused conceptual audit of 9 November
2026 (step122) recorded below. It supplies an endpoint premise, not
Kim's sign-sensitive critical count or RH.

## Proof

### Imported moment and reason for the specialization

Import Matthew P. Young, *A short proof of Levinson's theorem*,
Arch. Math. **95** (2010), 539–548,
[DOI 10.1007/s00013-010-0199-9](https://doi.org/10.1007/s00013-010-0199-9),
[published PDF](https://www.math.ntnu.no/emner/MA3001/2020v/2022v_MA3004/Young.pdf):
the mollifier definition on p540, Lemma3/(3.1)–(3.3) on p541, and
the zero-shift extension at the end of Section5, pp544–545. In its
notation, at scale S, 0<θ<1/2 and real P with P(0)=0, P(1)=1,

    integral w(t)|ζ(1/2+it) ψ(σ0+it)|² dt
      = [1 + θ^(-1) integral_0^1 P'(u)² du] integral w(t)dt
        + O(S/log S),

for smooth 0<=w<=1 supported in [S/4,2S], with
|w^(j)|<=C_j(S/log S)^(-j). Here σ0=1/2-R/log S and
ψ(σ0+it)=sum_{n<=S^θ} μ(n)n^(-1/2-it)P(log(S^θ/n)/log(S^θ)).
Fix R=1; the last expression is independent of R. The combined
Lemma3 formula includes zero shifts by holomorphy. No limit R→0 or
separate singular diagonal is used.

The arithmetic theorem is imported, not reproved. The work below
checks its contour and endpoint use for this particular mollifier.
It uses the standard named Littlewood rectangle lemma; a primary
statement is Aleksander Simonič, *Explicit zero density estimate for
the Riemann zeta-function near the critical line*,
[arXiv:1910.08274v2](https://arxiv.org/pdf/1910.08274v2), Section4.2,
pp29–30. Section4.4, pp31–32, gives the argument-estimation method for
his different mollifier. Its final constants are not applied here.
Jensen's formula for holomorphic functions on disks is the other
standard named complex-analysis input. The elementary growth and
normalization estimates below justify its use without importing an
argument bound for a different function.

### 1. One fixed mollifier and the padded moment

Fix S=2T, θ=1/4, X=S^(1/4), P(u)=u, and define

    a_n = μ(n) log(X/n)/log X  (n<=X),
    M_X(s) = sum_{n<=X} a_n n^(-s),    F(s)=ζ(s)M_X(s).

Thus a_1=1, all a_n are real, and |a_n|<=1. The cutoff X need not
be an integer; n<=X has its usual meaning. X remains fixed in every
contour and limiting operation at this T. In the imported formula
ψ(σ0+it)=M_X(1/2+it). At zero shifts, the mixed x,y derivative
in Young's (3.3) acts on P(x+u)P(y+u)=(x+u)(y+u) and equals 1;
both unit-interval integrals therefore equal 1. This gives 1+1/θ=5.

Put Δ=S/log S. Choose a fixed smooth function η with 0<=η<=1,
η(x)=0 for x<=0, and η(x)=1 for x>=1. Set

    w(t)=η((t-(T-2-Δ))/Δ) η(((2T+2+Δ)-t)/Δ).

Then w=1 on [T-2,2T+2], its support is contained in
[T-2-Δ,2T+2+Δ], and |w^(j)|<=C_j Δ^(-j), with constants
independent of T. For sufficiently large T this support lies inside
[S/4,2S]. Its mass is T+O(Δ). Positivity and the imported moment give

    integral_{T-2}^{2T+2} |F(1/2+it)|² dt
      <= 5T + O(T/log T).                                      (1)

This is one height-scale mollifier; there is no dyadic change inside
this integral. The big-O constants below are uniform in T and in the
subsequent choices of horizontal endpoints.

### 2. The right boundary has a bounded logarithmic integral

On Re s>=4, let A(s)=ζ(s)-1 and B_X(s)=M_X(s)-1. Their absolutely
convergent Dirichlet series have absolute coefficient sums at σ=4
at most

    q=sum_{n>=2} n^(-4)
      <=2^(-4)+integral_2^infinity x^(-4)dx=5/48.

Hence |F(s)-1|<=2q+q²<=505/2304<1/4. In particular Re F(s)>3/4.
The power series log(1+A) and log(1+B_X) converge absolutely and
give analytic logarithms on a neighborhood of Re s>=4 (the same
argument already works at σ=3). Their sum is a logarithm of F,
normalized to tend to zero as Re s tends to infinity. It agrees on
Re s>=4 with the principal logarithm of F. Write its Dirichlet series
as

    log F(s)=sum_{n>=2} c_n n^(-s),
    sum_{n>=2}|c_n|n^(-4)<=2 sum_{k>=1} q^k/k=-2 log(1-q).

There is no constant term. Absolute convergence justifies integration
term by term on any finite vertical interval. Since
|integral_a^b n^(-it)dt|<=2/log n, for all real a<b,

    |integral_a^b log F(4+it)dt|
      <= -4 log(1-q)/log 2.                                    (2)

Thus the real logarithmic integral on this edge is O(1), rather than
an unexamined O(T) loss. The normalized argument at 4+it is bounded
uniformly as well, for example by 2[-log(1-q)]<1.

### 3. Uniform horizontal argument bounds for this F

Here are the growth estimates needed for Jensen's formula. Partial
summation of the absolutely convergent defining ζ series first gives,
for Re s>1,

    ζ(s)=s integral_1^infinity floor(x)x^(-s-1)dx
        =s/(s-1)-s integral_1^infinity {x}x^(-s-1)dx.

The last integral converges locally uniformly on Re s>0, so the
identity theorem extends this expression there away from s=1. Thus,
for 1/4<=Re s<=31/4 and |Im s| comparable to T,

    |ζ(s)|<=|s/(s-1)|+4|s|<=C T.

Also |M_X(s)|<=sum_{n<=X}n^(-1/4)<=C X^(3/4). These elementary
bounds are intentionally crude: only log of polynomial growth is
needed. They imply |F(s)|<=C T^(19/16) in that fixed strip at the
heights in question, including negative heights by conjugation.

For τ in [T-2,2T+2] define the holomorphic function

    G_τ(z)=(F(z+iτ)+F(z-iτ))/2.

For large T both terms are holomorphic on a neighborhood of
|z-4|<=15/4: their possible ζ poles are outside this disk. Real
Dirichlet coefficients and analytic continuation give
G_τ(x)=Re F(x+iτ) for real x. By Section2, G_τ(4)>3/4. On the
outer disk the preceding bounds give |G_τ|<=C T^(19/16).

Apply Jensen's formula centered at 4. Choose a radius R in
[29/8,15/4] on which G_τ has no zero. If n_τ is the number of
its zeros, with multiplicity, in |z-4|<=7/2, the formula implies

    n_τ log(29/28)
      <= log(C T^(19/16)) - log(3/4).

This follows by retaining just those zeros, each contributing at
least log(R/(7/2)), and bounding the circle mean by the logarithm
of the maximum. Such R exists since G_τ is not identically zero.
In particular n_τ=O(log T) uniformly in τ.

Suppose F has no zero on [1/2,4]+iτ. Start its continuous argument
at 4+iτ with the normalization of Section2, and continue horizontally
left. At most n_τ points of [1/2,4] have Re F(x+iτ)=0. Between
successive such points the image lies in one open half-plane, so a
continuous argument lies in an interval of width π. Continuity at
the partition points therefore bounds the absolute argument by
1+π(n_τ+1) on the whole segment, including its endpoints. This
also handles a tangency of the real part to zero. Consequently

    sup_{1/2<=x<=4} |arg F(x+iτ)|=O(log T).                     (3)

No lower bound for |F| close to an interior zero, no simplicity,
and no zero-spacing estimate were used.

### 4. Littlewood's lemma and the critical-line limit

F is holomorphic on a neighborhood of the compact positive-height
rectangle [1/2,4]+i[T-2,2T+2] and not identically zero. It has only
finitely many zeros there. Choose

    a in (T-2,T-1),    b in (2T+1,2T+2)

so that neither horizontal segment [1/2,4]+ia or [1/2,4]+ib
contains a zero of F. This is possible by avoiding finitely many
ordinates. Let h=b-a=T+O(1). All zeros in the closed padded window
used in W_T now have ordinate strictly between a and b.

Choose α>1/2 tending down to 1/2 while avoiding the finitely many
real parts of zeros in the rectangle, so the left edge is also free
of zeros. The right edge is free of zeros by Section2. The general
Littlewood rectangle identity, with arguments normalized on the right
edge and continued horizontally, is

    2π sum_{F(ω)=0, α<Re ω<4, a<Im ω<b} ord_ω(F)(Re ω-α)
      = integral_a^b log|F(α+it)|dt
        - integral_a^b log|F(4+it)|dt
        + integral_α^4 arg F(x+ib)dx
        - integral_α^4 arg F(x+ia)dx.                           (4)

The named lemma applies to arbitrary rectangle heights a,b; the
dyadic heights displayed in the cited source are its application,
not a restriction of the identity. The two horizontal arguments are
compatible: start with the Section2 logarithm at 4+ia, continue up
the right edge, and then left along the top. The value at 4+ib is
exactly the same analytic logarithm used to start Section3's top
argument, not an independently chosen principal value plus 2πk.
The bottom argument starts from that same logarithm at 4+ia. These
are the boundary normalizations of the stated Littlewood identity;
no single logarithm inside the rectangle is assumed. There is no
pole within this positive-height rectangle. Equations (2) and (3)
bound the last three terms in absolute value by O(log T), uniformly
as α decreases.

We justify convergence of the first integral, including zeros on
Re s=1/2. For each fixed T, factor the finitely many such zeros on
the segment as

    F(s)=H(s) product_j (s-1/2-iγ_j)^(m_j).

Choose a sufficiently narrow neighborhood of that segment containing
no other zeros; its existence follows from discreteness and compactness,
and from the zero-free endpoints. H is holomorphic and nonzero there,
so log|H(α+it)| converges uniformly. The remaining factors are locally
integrable even when m_j>1. With δ=α-1/2>0, their logarithmic
difference is

    (1/2)log(δ²+(t-γ_j)²)-log|t-γ_j|
      =(1/2)log(1+δ²/(t-γ_j)²)>=0.

Its integral over [a,b] is at most
δ integral_0^infinity log(1+u^(-2))du<=δ(3+log 2).
The last bound uses log(1+u^(-2))<=log 2-2log u for 0<u<=1,
and <=u^(-2) for u>=1. Thus each factor converges in L1, proving
local log integrability and convergence of the whole integral.
This is a limit at fixed T; a uniform factorization radius is not
needed, since (2)–(3) already have uniform constants. In particular,
the singular-factor error is bounded by
δ(3+log 2) sum_j m_j. This tends to zero at each fixed T before T
varies; no uniform bound on that multiplicity sum is being imported.

The zero sum in (4) is finite. Each weight tends to its positive
part at α=1/2; zeros on the limiting line have zero weight. We obtain

    2π sum_{F(ω)=0, 1/2<Re ω<4, a<Im ω<b}
           ord_ω(F)(Re ω-1/2)
      <= integral_a^b log|F(1/2+it)|dt + O(log T).              (5)

Every ζ zero counted by W_T lies inside this rectangle, by L018's
strict strip. Its order as a zero of F is at least its order as a
zero of ζ, since M_X is entire. All extra mollifier contributions
on the left of (5) are nonnegative. Dropping them is an inequality,
not an assumption that M_X has no zeros. Hence the left side of (5)
is at least 2π W_T.

### 5. Strict displacement budget

Concavity of the real logarithm on the interval of length h gives

    integral_a^b log|F(1/2+it)|dt
      <= (h/2) log((1/h) integral_a^b |F(1/2+it)|²dt)
      <= (T/2)log 5 + O(T/log T).                              (6)

For completeness, apply concavity first to |F|²+ε and let ε
decrease to zero. The integrability proved above and monotone
convergence after subtracting a fixed upper bound justify this
limit. Equation (1) and [a,b] contained in [T-2,2T+2] give the
second inequality; h=T+O(1), so its normalization introduces only
O(1) besides O(T/log T).

Combining (5) and (6) yields

    W_T <= (log 5/(4π))T + O(T/log T).

All constants are independent of the selected a,b and of real T.
The strict comparison log 5<2<π follows, for example, from
e²>1+2+2=5 and π>3. Therefore log 5/(4π)<1/4. Since
(T/log T)/T tends to zero, the desired W_T<=T/4 holds for every
sufficiently large real T. No numerical evidence is needed.

### 6. Closed disks and an admissible endpoint

L018 sends a ζ zero β+iγ to z=γ+i(1/2-β) with the same
multiplicity. Each nonreal Ξ conjugate pair has one representative
with β>1/2. Its disk intersects the real axis in

    [γ-d,γ+d],    d=β-1/2 in (0,1/2).

If this interval meets [T,2T], then
T-1/2<γ<2T+1/2, hence its representative is included in the
closed padded W_T window. This also excludes any contribution from
remote or negative ordinates for large T. That window contains only
finitely many zeros. Summing interval lengths, retaining orders
m>=1, and allowing overcounts from overlaps or coincident disks gives

    meas([T,2T] intersect J(Ξ))
      <= sum_{padded right zeros} 2m(β+iγ)(β-1/2)
      =2W_T<=T/2.

All intervals here are closed, and only finitely many can meet the
compact interval. Thus the complement has measure at least T/2
and contains a point in (T,2T) outside every closed disk; a boundary
contact has not been counted as avoidance. The real zeros of Ξ in
[T,2T] form a finite set by L018 and nontriviality, so removing them
still leaves a possible t_T. This proves the stated endpoint claim. ∎

**Qualifications.** This discharges only the positive, sufficiently-high
endpoint-existence target. A negative-endpoint symmetry specialization,
Kim's count application, its critical multiplicities/signs, and any
global implication remain separate work. L956 is a contrast: its
generic strip model has no Young-moment hypothesis. The density-only
and charged-block stops are not contradicted. The present first-moment
bound is O(T) with a sufficient explicit coefficient, not o(T), no
zero-free region, and not an exclusion of any off-line zero. No
newness beyond the checked sources is asserted.

### Conceptual audit — 9 November 2026, step122

The separate audit accepts the stated coefficient, uniform error and
closed-disk conclusion. It imported Young's Lemma3, rather than
reproving its arithmetic estimate, and rechecked the published weight
conditions p540, formula (3.3) p541 and combined-term holomorphic
extension pp544–545. The choice R=1 disappears from the mollifier
evaluated at σ0+it; zero shifts are admitted directly by that extension.
The fixed cutoff X=(2T)^(1/4) and the derivative constants of the
smooth weight meet the source hypotheses for every sufficiently large
real T, not just a subsequence or an integer cutoff.

The right-edge Dirichlet logarithm has no constant term, and its
absolute coefficient bound is independent of X; this is what makes
(2) O(1). The actual-F Jensen disk stays in Re s>=1/4 at imaginary
heights comparable to T. Its center lower bound is >3/4, its growth
is O(T^(19/16)), and its inner and outer radii give the positive gap
log(29/28). Thus (3) is uniform even when a permitted horizontal
segment approaches a zero arbitrarily closely. Multiple zeros of
G_τ and tangencies of Re F do not invalidate the half-plane argument.
The branch compatibility and multiplicity-weighted fixed-T limit are
made explicit above; neither requires zero separation or simplicity.

For bookkeeping, the moment and smoothing losses are O(T/log T),
the interval-length change is O(1), the right-edge integral is O(1),
and the two horizontal integrals are O(log T). The last quantity is
O(T/log T) for sufficiently large T. No error from the critical-line
limit survives. Since F=ζM_X is a holomorphic product in the rectangle,
its orders add; retaining them before discarding extra nonnegative
orders proves the direction of (5). The closed padded window lies
strictly between a and b, regardless of zeros on its original edges.

Finally L018 pairs β>1/2 with 1-β at the same ordinate. One pair
supplies one real disk interval of length 2(β-1/2), so the union
factor is exactly the upper bound 2W_T, not 4W_T. Every disk meeting
[T,2T] belongs to the finite padded family. Its closed union has the
stated measure bound, and deleting the finite set of real Xi zeros
still leaves an admissible interior point. The strict analytic
comparison log 5<2<π supplies the required margin without numerical
evidence. No proof failure was found in this scope. This validation
establishes a local known-method input; it gives no new critical sign,
negative-endpoint specialization, effective onset, or RH conclusion.

## Mathlib

Full matching coverage has not been checked and is unknown. The
imported mollified moment, its transfer and the endpoint statement
are not claimed formally verified. Jensen's formula, logarithmic
integrability, and Dirichlet-series facts are supporting analytic
inputs, not an identified formal theorem for the complete result.
[Mathlib documentation](https://leanprover-community.github.io/mathlib4_docs/).
