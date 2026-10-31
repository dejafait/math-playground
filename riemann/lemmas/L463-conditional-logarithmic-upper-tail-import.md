# Lemma 463: conditional logarithmic upper-tail positivity (source import)

## Hypotheses

Let Ξ(z)=ξ(1/2+iz) be the actual entire completion of L018. For real a define

    H_a(y)=Ξ(a+iy)Ξ(a−iy)=Σ_(n≥0) D_n(Ξ;a)y^(2n).

The variable y is complex and coefficients are holomorphic Taylor
coefficients. This is not a modulus-square definition for complex y.

Retain precisely L461's external premise: OpenAI, *The Quasi-Riemann
Hypothesis: A Zero-Free Half-Plane Re s > 7/8*, September 30, 2026,
Theorem 1.1, specialized to ζ, at commit
`1581d4cbdd69a0faf34b2089614fe2a814316a6a`. Thus ζ has no zeros in
Re(s)>7/8; the pole at 1 is allowed and no boundary exclusion is assumed.
The [pinned source](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex)
and [external-input register](../foundations/2026-10-quasi-riemann-input.md)
specify the retained manuscript/import-closure audit limitations.

The Xi conclusion is stated by bramble_trace, *Generalized Laguerre
positivity at growing orders*, [rStation paper 41](https://rstation.ai/problems/riemann_hypothesis/papers/41),
displayed v4, 24 October 2026 at 07:18 UTC, Theorem 1b, equation (4b),
with definitions (1)–(2). The statement and version were checked on
25 October 2026. Its proof is Sections 4.2–4.5, including the tail
overlap and shifted-saddle cases (18a)–(18n). Those cases have source
coverage in the [assessment](../drafts/literature/2026-10-25-initial-laguerre-sign-coverage.md),
but the original import did not independently audit the manuscript.
The bounded source-proof audit below now verifies Section 4.5 at
sigma_0=7/8, using C465a for the already audited unconditional overlap.
It does not audit the external zero-free manuscript or the whole paper.

Fix a real c_0>3/8. All logarithms are natural.

## Conclusion

There exists A_(c_0)>2π such that, simultaneously for every real a
with |a|≥A_(c_0) and every integer n≥0 satisfying

    2n ≥ c_0 log(|a|/(2π)),

one has D_n(Ξ;a)>0. The onset is independent of n and there is no
upper order cutoff. Centers with Ξ(a)=0, of any multiplicity, are
included under the same quantifiers.

The onset is existential, with no effective bound or asserted overlap
with any finite verified height range. No conclusion at c_0=3/8,
uniformity as c_0 decreases to 3/8, or sign below this order threshold
is asserted. Originally recorded as a KNOWN_IMPORTED conditional
partial result, this now also has a REPRODUCTION audit of the stated
conditional implication. Neither is a verification of the external
zero-free theorem or of RH, a stronger conclusion or a new positivity
result.

## Proof

### Original source-import argument

The cited Theorem 1b assumes 1/2≤σ_0<1 and no ζ zeros in
Re(s)>σ_0. It supplies, for each fixed c_0>σ_0−1/2, a single
T_(c_0,σ_0) such that its expression ℒ_p(Ξ;t) is strictly positive
at every t≥T_(c_0,σ_0) and every order 2p≥c_0 log(t/(2π)), with
no upper order restriction. Take σ_0=7/8, using exactly the retained
external premise. The resulting lower requirement is c_0>3/8.
Increase the supplied onset if necessary to obtain A_(c_0)>2π.

Equation (2) of the source uses Ξ(t)=ξ(1/2+it), the completion of
L018. Equation (1) defines ℒ_p(f;t) as [y^(2p)]f(t+iy)f(t−iy).
Hence its p is exactly the present n. Explicitly, multiplying the
Taylor series gives

    D_n(Ξ;a)=Σ_(j=0)^(2n) (-1)^(j+n)
                    Ξ^(j)(a)Ξ^(2n−j)(a)/(j!(2n−j)!),

since i^j(−i)^(2n−j)=(−1)^(j+n). Entirety justifies this finite
coefficient identity at every center. It agrees with source (1),
with no rescaling by the auxiliary Hardy normalization b(t).
Thus the source sign is precisely D_n(Ξ;t)>0 for positive t in
the stated range.

For a≤−A_(c_0), set t=−a=|a|. Evenness from L018 gives the
identity of entire functions of y

    H_(−t)(y)=Ξ(−t+iy)Ξ(−t−iy)
             =Ξ(t−iy)Ξ(t+iy)=H_t(y).

Consequently D_n(Ξ;−t)=D_n(Ξ;t), and the same onset and order
inequality apply to negative centers.

The source theorem has no nonvanishing condition at t itself.
Its all-order extension includes repeated and zero local roots
(Sections 4.2–4.4), rather than dividing by Ξ(t)^2. The coefficient
identity and evenness argument above likewise never divide by Ξ(a).
Thus no central-zero exclusion, simplicity assumption, or additional
onset depending on n or multiplicity has entered this specialization.
This invokes the full cited theorem, not a reproof of its analytic
estimates. ∎

### Critical application audit — 25 October 2026

Verdict: the stated application passes without correction. This checks
the import and its elementary specialization, not either manuscript.
The primary page still displays v4, 24 October 2026, 07:18 UTC.
Definitions (1)–(2) and Theorem 1b (4b) match the citation above.

For normalization, each term contributing to degree 2n has indices
j and 2n−j. Its phase is
i^j(−i)^(2n−j)=i^(2n)(−1)^(2n−j)=(−1)^(n+j).
The two Taylor denominators are exactly those displayed above;
there is no extra (2n)! or b(a)^2 multiplier. The source coefficient
index p is n here, whereas its auxiliary total degree is 2p.
Entirety permits coefficient extraction from the locally convergent
product. The product is even in y and real for real y by L018's
conjugation symmetry, so its coefficients are real and the sign
comparison has its ordinary real meaning.

The source order quantifier follows its height quantifier with a
single T_(c_0,σ_0). Fixing σ_0=7/8 and taking, for example,
A_(c_0)=max(T_(c_0,7/8),2π+1) preserves every allowed integer n.
For negative a, evenness identifies entire products, hence every
coefficient; replacing t by |a| preserves the exact logarithm and
uses that same onset. No separate limit in n is taken.

The central-zero qualification was checked against source
(18e)–(18h): zero roots remain in the finite local factor, with
positive normalization defined without division by Ξ(t)^2.
Section 4.5, (18k)–(18n), supplies the lower-order range and its
overlap with Theorem 1a. These are inspected source cases, not
independently verified estimates. In particular the import invokes
the theorem, not formula (4) outside its stated range.

No new mathematical input or DAG edge is needed: L018 supplies the
completion and symmetries, while the two external statements remain
explicit hypotheses with their recorded versions and audit limits.
No boundary exclusion, effective height, initial sign, or RH conclusion
has entered this audit. The coefficient and symmetry proof above
remains the complete local applicability argument.

### Critical shifted-saddle audit — 31 October 2026

Verdict: Section 4.5, (18i)--(18n), passes at the approved fixed
sigma_0=7/8 and every fixed 3/8<c_0<1. The primary page still displays
v4, 24 October 2026, 07:18 UTC. This independently checks the conditional
analytic implication, using the already audited C465a for the tail;
the zero-free premise is retained without re-auditing its source.
The following replay records all estimates needed for a common onset.

Write d=3/8, ell=log(t/(2pi)), N=2p and c=N/ell. Here N is the
source's total coefficient degree, and p is this lemma's Laguerre
index. Constants below may depend on fixed c_0 and subsequently fixed
neighborhoods and angles, but not on t or N. Work initially with
c_0<=c<=1 and t sufficiently large. The analytic tools are the standard
named Borel--Caratheodory theorem, Hadamard three-circles theorem,
Cauchy derivative estimates, and Gaussian integral. For strip
Phragmen--Lindelof and polynomial vertical growth use Titchmarsh,
*The Theory of the Riemann Zeta-function*, second edition revised by
Heath-Brown (1986), Section 5.1, (5.1.1)--(5.1.5), pp. 95--96
([primary scan](https://sites.math.rutgers.edu/~zeilberg/EM18/TitchmarshZeta.pdf)).
The functional equation and sector Stirling/digamma formulas are the
standard inputs [DLMF 25.4.2](https://dlmf.nist.gov/25.4.E2) and
[DLMF 5.11.1--5.11.2](https://dlmf.nist.gov/5.11). C465a's proof is
not repeated. Replaying the saddle is necessary because the earlier
application audit explicitly excluded its relative-error estimates.

**Logarithm and derivatives.** Set sigma_0=7/8 and
F(s)=(s-1)zeta(s)/(s+1). On Re(s)>sigma_0 this is holomorphic and
nonzero: the only pole of zeta is canceled with F(1)=1/2, s=-1 is
outside, and the zero-free premise excludes the remaining zeros.
The half-plane is simply connected. Its analytic logarithm g can be
fixed by the Euler branch for Re(s)>1. This does not posit a logarithm
of zeta across its pole.

Fix a sufficiently small delta>0. About z_v=2+iv put

    R_2=2-sigma_0-delta/8,
    R_1=2-sigma_0-delta/4,
    R=2-sigma_0-delta/2.

These fixed radii satisfy 1/4<R<R_1<R_2. On the inner disk of radius
1/4, the absolutely convergent Euler logarithm is bounded uniformly
in large |v|, and the logarithm of (s-1)/(s+1) is O(1/|v|).
Thus |g| is bounded there. Polynomial vertical growth bounds Re(g)
above by C log(|v|+3) on the disk of radius R_2. The center value is
already bounded. Borel--Caratheodory, with the positive gap R_2-R_1,
therefore bounds |g| on radius R_1 by C_delta log(|v|+3).
Hadamard three-circles gives on radius R

    |g| <= C_delta (log(|v|+3))^a,
    a=log(4R)/log(4R_1),   0<a<1.

For sigma_0+delta<=Re(s)<=2, center a disk at s of radius delta/4
inside the R-disk about 2+i Im(s). Indeed its furthest possible
distance is at most 2-sigma_0-3delta/4<R. Cauchy's estimates bound
g^(j), 0<=j<=4, there by C_delta,j (log(|Im(s)|+3))^a.
Subtract the local logarithm of the rational regularizer; it and its
first four derivatives are O_delta(1/|Im(s)|). This yields the same
bounds for the Euler-continued local log zeta. On Re(s)>=2 the
Euler logarithm and these derivatives are bounded directly. The
argument works at both height signs and at heights t+O(1), uniformly.
In particular log|zeta| is bounded on both sides by O(ell^a) in
each fixed strictly smaller zero-free half-plane. The reciprocal
estimate is a conclusion of this argument, not an added assumption.

**Exact Xi amplitude.** Put s=1/2+it, gamma(z)=pi^(-z/2)Gamma(z/2),
Q_t(y)=Xi(t+iy)Xi(t-iy), and

    b(t)^2=((t^2+1/4)^2/4) gamma(s)gamma(1-s)>0.

Using L018's reflection and completion formulas gives the exact
identity Q_t(y)/b(t)^2=K_t(y)zeta(s+y)zeta(1-s+y), where

    K_t(y)=[(s+y)(s+y-1)(1-s+y)(y-s)/(t^2+1/4)^2]
              gamma(s+y)gamma(1-s+y)/[gamma(s)gamma(1-s)].

The identity first holds where the completion formulas apply directly;
the identity theorem extends it across each fixed y-disk, since at
large t none of its gamma or zeta poles lies in that disk.
On any fixed y-disk and a slightly larger disk, K_t is holomorphic
and nonzero for large t, and K_t(0)=1. Sector Stirling gives
(log K_t)'=ell+O(1/t) uniformly: the polynomial logarithmic
derivatives cost O(1/t), and the two gamma logarithmic derivatives
sum to ell+O(1/t). The sectors about the positive and negative
imaginary axes stay a fixed distance from the negative real axis.
Integration from zero and Cauchy on the larger disk give

    k_t(y)=log K_t(y)-ell y=O(1/t),
    k_t^(j)(y)=O_j(1/t),  1<=j<=4.

For real y in the disk, K_t(y)>0 since both its polynomial pair
and gamma pair are conjugate products. Its logarithm fixed at zero
is therefore real there. Choose a fixed thin convex neighborhood U
of a slightly enlarged segment [c_0,1], with closure contained in
Re(y)>d. The two zeta factors have no zeros on U under the retained
premise. The preceding logarithm bounds and the compatible conjugate
Euler branches give an analytic e_t on U such that

    Q_t(y)/b(t)^2=exp(ell y+e_t(y)),
    sup_U |e_t^(j)| <= C ell^a,  0<=j<=4,  a<1,

after shrinking U once to leave a fixed Cauchy margin if necessary.
Take a smaller common U when taking the maximum of the finitely many
exponents; that maximum is still below one. On the real segment e_t
is real, and Q_t(r)=|xi(1/2+r+it)|^2>0. This logarithm is only used
on U, never at the center y=0 or on the whole Cauchy disk.

**Uniform real saddle and local error.** Choose a fixed h>0 so that
[c_0-h,1+h] is inside U and c_0-h>d. On that segment set
q_t(r)=r(ell+e_t'(r)). It is real and

    q_t'(r)=ell+e_t'(r)+r e_t''(r)=ell+O(ell^a)>ell/2.

At the endpoints q_t(c_0-h)<c_0 ell and q_t(1+h)>ell once t is
large, since the endpoint margins are h ell and the errors O(ell^a).
Thus q_t(r)=N has exactly one solution on the segment for every
c_0 ell<=N<=ell. Its equation gives |r-c|<=C ell^(a-1).
The curvature satisfies

    B=N+r^2 e_t''(r)=N+O(ell^a),
    C_1 ell <= B <= C_2 ell

with positive constants for large t. All these onsets are independent
of the particular allowed N.

Choose a fixed beta>0 small enough that r exp(i theta) lies in U
for every such r and |theta|<=beta, after increasing the onset so
r stays in a smaller segment. In the Cauchy integral the phase
relative to its value at zero is

    V(theta)=ell r(exp(i theta)-1)
               +e_t(r exp(i theta))-e_t(r)-iN theta.

Its first derivative at zero vanishes exactly; its second is -B.
Its third and fourth derivatives are O(ell) throughout the arc,
by the chain rule and the bounded r interval. For w=ell^(-2/5),
Taylor's theorem with an integral remainder gives

    V(theta)=-B theta^2/2+R(theta),
    |R(theta)|<=C ell |theta|^3<=C ell^(-1/5)   (|theta|<=w).

Consequently |exp(R)-1|<=C ell |theta|^3 on this interval. Dividing
the integrated error by the full Gaussian integral sqrt(2pi/B)
gives at most

    C ell [integral_R |theta|^3 exp(-B theta^2/2) dtheta]
                  /sqrt(2pi/B)
       = O(ell B^(-3/2))=O(ell^(-1/2)).

Extending the truncated Gaussian to R has relative error
O(exp(-kappa ell^(1/5))) with a fixed kappa>0, since B w^2 is
bounded below by a positive multiple of ell^(1/5). Thus the small
arc contributes

    Q_t(r)/(r^N sqrt(2pi B)) (1+O(ell^(-1/2))).

This is a relative error at the exact saddle, even when e_t(r) is
large and negative. Neither e_t(r) nor r has been frozen at c.

**Intermediate angles.** Let g(theta)=Re(e_t(r exp(i theta))).
Since e_t'(r) is real, g'(0)=Re(i r e_t'(r))=0. The chain rule
and the first two derivative bounds give |g''(theta)|<=C ell^a
throughout the fixed arc. Therefore

    |g(theta)-g(0)|<=C ell^a theta^2.

Meanwhile ell r(cos(theta)-1)<=-k ell theta^2 for a fixed k>0.
As a<1, increasing the onset gives Re(V(theta))<=-(k/2)ell theta^2
on the whole arc. Its part w<=|theta|<=beta is at most
O(sqrt(ell) exp(-k' ell^(1/5))) relative to the preceding main term.
No estimate requiring a<1/2 has entered. Evenness Q_t(-y)=Q_t(y)
and even N make the arc about angle pi exactly equal to the arc
about zero, including orientation and coefficient phase.

**Complementary angles.** Fix epsilon>0 small enough that
v_0=d+epsilon<1/2. The logarithm bound on Re(s)=1/2+v_0 gives,
for every fixed eta_0>0, |zeta|<=C(1+|Im(s)|)^eta_0. The functional
equation and Stirling give exponent v_0+eta_0 on its reflected line
Re(s)=1/2-v_0. The strip between them contains no pole (its right
edge is below one); zeros inside cause no difficulty for modulus
convexity. Polynomial vertical growth supplies the growth hypothesis
for strip Phragmen--Lindelof. It follows that, uniformly for
0<=u<=v_0 at large |v|,

    |zeta(1/2+u+iv)|<=C |v|^((v_0-u)/2+eta_0).

For u>=v_0 in a fixed bounded interval, use the logarithm estimate,
and then absolute convergence beyond real part two. In the Xi product
the heights are +/-t+O(1). The exact K_t formula supplies modulus
exp(ell u+O(1/t)); reflection y -> -y covers negative real parts.
Taking eta_0 small enough for each requested eta>0 yields

    |Q_t(y)|/b(t)^2 <= C_eta t^(max(v_0,|Re(y)|)+eta)

uniformly on the fixed disk containing the Cauchy circle. This also
checks that the two zeta factors' losses have both been paid.

For an explicit positive gap budget, put r_-=(c_0+d)/2. Enlarge
the onset so r>=r_-. Choose epsilon<min((c_0-d)/8,1/16), and fix
the preceding beta. Then

    Delta=min(r_- -v_0, r_-(1-cos(beta)))>0.

Outside the two arcs, |Re(y)|<=r cos(beta), so
r-max(v_0,r cos(beta))>=Delta. Also
Q_t(r)/b(t)^2=exp(ell r+e_t(r)) with |e_t(r)|<=C ell^a.
Choose eta<Delta/4. The entire remaining contour, divided by one
Gaussian main term, is at most

    C sqrt(ell) exp(-(Delta-eta)ell+C ell^a+O(1))
       <= C' sqrt(ell) exp(-Delta ell/2)

for one further common onset. This is smaller than ell^(-1/2).
The factor r^(-N) cancels before this comparison. A bounded disk
and fixed constants ensure that replacing log t by ell adds only O(1).

**Assembly and qualifications.** Cauchy's formula now gives, uniformly
in the entire interval c_0<=N/ell<=1,

    D_p(Xi;t)=2 Q_t(r)/(r^N sqrt(2pi B))
                         (1+O_c_0(ell^(-1/2))).

The coefficient is real, the prefactor positive, and the uniform error
is eventually smaller than 1/2. This proves strict positivity on that
band. Fix the already audited C465a constant 3/4>1/2. Its single
onset supplies every integer N>=3ell/4. Taking the maximum of that
onset and the finitely many onsets above covers every integer
N>=c_0 ell: N<=ell is in the audited band, while N>ell belongs to
C465a. Equality and integer rounding leave no gap. For c_0>=1,
C465a alone already covers all the required orders. The earlier
evenness application handles negative centers without another onset.

Central zeros of any multiplicity are allowed throughout: Q_t is
entire on the Cauchy disk, the logarithm is taken only near the positive
saddle with r>d, b(t)>0, and no step divides by Xi(t). No zero-free
assertion on Re(s)=7/8, uniformity as c_0 decreases to 3/8, effective
onset, low-order sign or all-height positivity is obtained. The direct
local inputs for this audited assembly are L018 and C465a. The earlier
source-import argument and application audit remain above as history;
their explicit exclusion of source-proof auditing describes those
earlier checks, not this bounded analytic replay. The entire external
zero-free manuscript remains unaudited here. ∎

## Mathlib

Full matching coverage for this conditional, simultaneous upper-tail
statement has not been checked; absence is not asserted. No Mathlib
formalization or external zero-free manuscript/import-closure verification
is claimed. The added analytic replay is informal; it uses the named
classical complex-analysis theorems above. Their supporting Mathlib
coverage has not been checked in this step.
