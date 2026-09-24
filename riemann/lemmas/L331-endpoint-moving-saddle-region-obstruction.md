# Lemma 331: endpoint moving-saddle region and curvature obstruction

**Hypotheses.** Let r=2n tend to infinity and
a=a_n=sqrt(4π²exp(4r)−25), as in L303. Write

g(s)=ζ′(s)/ζ(s),  x₀=(r+1)/(2r),  σ₀=1/2+x₀,
Q=Q_r=r^(2/3)(log r)^(1/3),  E_r=(1+r)²exp(−r/256).

Where ζ(1/2+x+ia) is nonzero and x>0, define the real function

H_r(x)=2rx−(r+1)log x+log|ζ(1/2+x+ia)|².

Use the classical Vinogradov–Korobov zero-free region and its
logarithmic-derivative estimate, cited precisely below. The proposed
certificate seeks a real stationary point of H_r with positive second
derivative inside that region, before making a saddle approximation
to L303's integral.

**Conclusion.** The exact conjugate-pair derivatives are

H_r′(x)=2r−(r+1)/x+2 Re g(1/2+x+ia),                       (1)
H_r″(x)=(r+1)/x²+2 Re g′(1/2+x+ia).                       (2)

Here is a sufficient local criterion. For r≥2 and 0<d≤1/8, suppose
g is analytic on a neighborhood of |s−(σ₀+ia)|≤2d and

M=sup_(|s−(σ₀+ia)|≤2d)|g(s)| ≤ rd/4.                     (3)

Then H_r has exactly one stationary point x_* in [x₀−d,x₀+d],
its curvature is at least r/2 throughout that interval, and

|x_*−x₀|≤M/r≤d/4.                                        (4)

For a sufficiently small fixed D>0 the cited inputs make a disk of
radius 2d with d=D/(8Q) available, but provide only M=O(Q).
Condition (3) instead requires a bound of order r/Q. The ratio of
these two scales, and of the resulting Cauchy curvature envelope to
the kernel curvature, is

Q²/r=r^(1/3)(log r)^(2/3) →∞.                             (5)

These are failures of a sufficient estimate, not lower bounds on
the actual g, an actual displacement, or an actual curvature.

The failure is realizable by nonvanishing conjugate-paired models:
even bounded models with bounded reciprocals, logarithmic derivatives
O(Q) throughout Re s≥1−D/Q, and limit 1 as Re s→∞ can have no real
stationary point anywhere in the corresponding x-region. A second
such model has a stationary point exactly at x₀ with negative
curvature. Thus these analytic envelopes and conjugation alone do
not imply the desired local saddle. The models are not ζ and are
not asserted to have its Euler product or functional equation.

No actual saddle is excluded, no Mellin sign or margin above E_r is
proved, and no Laguerre sign or zero-exclusion range is extended.

**Proof.** On a zero-free disk about x₀, choose local analytic
logarithms of ζ(1/2+z+ia) and ζ(1/2+z−ia), conjugate at x₀.
Conjugation of ζ makes their sum real on the real interval. Hence

h_r(z)=2rz−(r+1)Log z
       +log ζ(1/2+z+ia)+log ζ(1/2+z−ia)

restricts to H_r there. Differentiation gives (1) and (2), because
g and g′ also respect conjugation. In particular the two first
derivatives add; conjugacy does not remove their real part. Along
the vertical direction through a real point x,

h_r(x+iv)=H_r(x)+ivH_r′(x)−v²H_r″(x)/2+O_x(|v|³).

Thus positive H_r″ is the local vertical Gaussian-decay condition
at a stationary point. This Taylor identity asserts no uniform
cubic remainder or complementary-contour bound.

For the local criterion, put F(x)=2r−(r+1)/x. Since 2rx₀=r+1,

F(x)=2r(x−x₀)/x,  F′(x)=(r+1)/x².

The interval in (3) is contained in (0,1): x₀≤3/4 and d≤1/8,
while x₀≥1/2. At its endpoints F has opposite signs and absolute
value at least 2rd. The perturbation 2 Re g has modulus at most
2M≤rd/2, so H_r′ also has opposite endpoint signs. Cauchy's
derivative estimate on the circle of radius d about each point
σ=1/2+x+ia, |x−x₀|≤d, gives |g′(σ)|≤M/d≤r/4.
Consequently (2) implies H_r″≥r−2(r/4)=r/2 on the interval.
Continuity and strict increase of H_r′ prove existence and
uniqueness. At its zero, (1) gives

|x_*−x₀|=x_*|Re g(1/2+x_*+ia)|/r≤M/r,

since x_*<1. This proves (3)–(4).

For the standard input, E. C. Titchmarsh, *The Theory of the Riemann
Zeta-function*, second edition revised by D. R. Heath-Brown (1986),
[Section 6.19, p. 135](https://sites.math.rutgers.edu/~zeilberg/EM18/TitchmarshZeta.pdf#page=72),
applies Theorems 3.10–3.11 to (6.19.2). It gives fixed A,C>0 such
that, for sufficiently large |t|, ζ is zero-free and |g(σ+it)|≤C Q(t)
in σ≥1−A/Q(t), where Q(t)=(log |t|)^(2/3)(log log |t|)^(1/3).
The logarithmic-derivative theorem is
[Theorem 3.11, pp. 59–60](https://sites.math.rutgers.edu/~zeilberg/EM18/TitchmarshZeta.pdf#page=34).
These are supporting regional estimates, not statements about the
present integral or its stationary points.

Uniformly for |t−a_n|≤1, log |t|=2r+log(2π)+o(1), so Q(t) is
bounded above and below by fixed positive multiples of Q. Choosing
D>0 sufficiently small puts the rectangle

Re s≥1−D/Q,  |Im s−a_n|≤1

inside the cited region for all sufficiently large r. The disk of
radius 2d, d=D/(8Q), about σ₀+ia_n is strictly inside this rectangle.
It therefore admits analytic g and the bound M≤C₁Q. The ratio of
this supplied upper bound to rd/4 is

32C₁Q²/(Dr),

which diverges. Cauchy gives only |g′|=O(Q²) on the smaller disk,
whereas the bare curvature F′ is comparable to r. Its resulting
lower estimate F′−O(Q²) is not positive. Likewise the formal
displacement scale obtained by dividing O(Q) by bare curvature r
is O(Q/r), larger than the available radius d by the same factor
Q²/r. This is a scale comparison, not an application of (4) when
its hypothesis fails. The actual signed derivatives might be much
smaller or more favorable than these envelopes.

To prove that the envelope-only implication itself fails, fix any
D>0 and set

q=q_r=(2π/a_n)ceil(a_n Q/(2π)).

Then q a_n is an integer multiple of 2π, q/Q→1, q/r→0 and
q²/r→∞. Consider the entire zero-free function

U_r(s)=exp(−exp(−q(s−1))).                                (6)

It respects conjugation and tends uniformly to 1 as Re s→∞.
On Re s≥1−D/Q, |exp(−q(s−1))|≤exp(qD/Q)≤exp(2D) for
large r. Thus |U_r| and |1/U_r| are bounded by constants depending
only on D, and

g_U(s)=U_r′(s)/U_r(s)=q exp(−q(s−1))=O_D(Q),
g_U′(s)=−q² exp(−q(s−1))=O_D(Q²).                         (7)

Because exp(±iqa_n)=1, its conjugate-pair exponent is exactly

H_U(x)=2rx−(r+1)log x−2exp(−q(x−1/2)),
H_U′(x)=F(x)+2q exp(−q(x−1/2)).                           (8)

For x≥x₀ both terms in (8) are nonnegative and the second is
strictly positive. For 1/2−D/Q≤x≤x₀, the lower endpoint exceeds
1/4 for large r, so

F(x)≥−8Dr/Q−4,
2q exp(−q(x−1/2))≥2q exp(−q/(2r))≥q.

Since q/(r/Q)→∞, their sum is strictly positive for all
sufficiently large r. Hence H_U has no real stationary point on
x≥1/2−D/Q, despite all the stated analytic envelopes. Its behavior
outside this region is irrelevant to the claim.

The curvature obstruction can also occur with no displacement.
With the same q, put

u(s)=exp(−q(s−σ₀)),
V_r(s)=exp(u(s)−u(s)²/2).                                 (9)

Again V_r is entire, zero-free, conjugate symmetric and tends to 1
as Re s→∞. In the same half-plane,
|u|≤exp(qD/Q+q/(2r))≤exp(2D+1) for large r. This bounds V_r,
its reciprocal and its logarithmic derivatives as before. Exactly,

g_V(s)=q(u²−u),  g_V′(s)=q²(u−2u²).

At s=σ₀±ia_n, u=1. Therefore the associated exponent satisfies

H_V′(x₀)=0,
H_V″(x₀)=(r+1)/x₀²−2q²<0                               (10)

for sufficiently large r. This is a stationary point with the
wrong curvature; no assertion is made about its other stationary
points. Both models even have stronger uniform value bounds and
nonvanishing than the local zeta estimates used in the test, but
neither is an arithmetic substitute for ζ.

The models establish failure of the local-saddle inference from
these data alone. They do not assert a negative Mellin integral,
let alone a negative actual Laguerre coefficient or an off-line
zeta zero. Even a successful actual local criterion would still
require uniform higher-order errors, a justified contour treatment
and complementary bounds before comparison with E_r in L303.
No contour deformation or infinite interchange is used here. ∎

This stops the tested moving-saddle certificate based only on the
recorded regional modulus estimates. Additional actual arithmetic
information is not excluded. The endpoint lower bound, smaller
indices and passage to every height remain unproved.

**Mathlib.** Full statement: not checked. Supporting analytic
logarithms, conjugation, Cauchy derivative estimates, the intermediate
value theorem and Vinogradov–Korobov estimates: not checked. No
library match or absence is asserted. Titchmarsh's Theorem 3.11 and
Section 6.19, with direct links above, supply regional analytic
inputs only; they are not matches for the local criterion or either
model obstruction, proved here. L303 supplies the full Mellin
integrand and the required positive-error margin.
