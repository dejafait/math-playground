# Lemma 475: cost of the prescribed scale-adapted band scheme

## Hypotheses

Use actual Xi, its completion prefactor P and zero symmetries from
L018, sector normalization from L465, and all definitions in L471.
In particular m_j is the full multiplicity, F_j=Xi/q_j removes
exactly one conjugate pair, and J_j(T) is the actual clipped window.
For sufficiently large real T put L=log T. Uniformly for

    1<=u<L/16,  h=u/L,
    B_u(T)=sum_(j in P_T, u<d_j L<=min(2u,L/16)) m_j d_j^3
       integral_(J_j(T)) (1-v^2)
         |F_j(gamma_j+d_j v)/A(gamma_j+d_j v)|^2 dv,

partition the real axis into width-h half-open cells, with centers
c_k=(k+1/2)h. Use disks of radius 6h and area collars of width h.
No RH, simplicity, separation, occupancy, density or external
half-plane premise is imposed.

## Conclusion

There are absolute C,T_0, independent of u and of selected zeros,
such that for all these T,u,

    B_u(T)<=C T L^3 K(u),
    K(u)=u^(-3) E(7u),
    E(X)=integral_0^X exp(v) min(1,1/v) dv.                 (1)

At v=0 the minimum is defined as 1. In particular

    K(u) ~ exp(7u)/(7u^4),  u->infinity.                  (2)

Thus this envelope has no dyadically summable large-u tail. This
is failure of the prescribed upper-bound comparison, not a lower
bound on B_u or a disproof of any desired band estimate. In a cell
with one simple selected pair the residual-factor compensation is
exactly absent. No additional actual-Xi compensation is proved.
The calculation is a specialization of known tools, with no claim
of progress beyond the inspected literature or a resolution of RH.
The separate critical application audit in Section 6 verifies this
statement without changing its bound or extending the obstruction.

## Proof

### 1. Imported tools and uniform domains

The approved prior assessment is
`drafts/literature/2026-10-28-scale-adapted-band-cost-test.md`.
Reuse these primary inputs within their inspected scope:

* Kevin Broughan, *Equivalents of the Riemann Hypothesis*, Volume
  Two, Cambridge (2017), Theorem 3.3, proof (1),(4), printed
  pp. 26--27: finite Blaschke division at zeros, with repeated
  factors for multiplicities, preserves the disk supremum bound
  ([primary preview](https://api.pageplace.de/preview/DT0400.9781108195430_A31720577/preview-9781108195430_A31720577.pdf#page=48)).
* Titchmarsh, revised by Heath-Brown, *The Theory of the Riemann
  Zeta-Function*, second edition (1986), Theorem 7.2(A), printed
  p. 141: with an absolute constant, for 1/2<=sigma<=2,
  integral_1^V |zeta(sigma+ix)|^2 dx is at most
  C V min(log V,1/(sigma-1/2)), interpreting the second entry
  as infinity at 1/2. Also use its functional equation
  (2.1.9)--(2.1.10), p. 16, and uniform fixed-strip chi
  asymptotic (4.12.3), p. 78/Section 5.1, p. 95
  ([primary scan](https://sites.math.rutgers.edu/~zeilberg/EM18/TitchmarshZeta.pdf#page=75)).
* [NIST DLMF 5.11.9](https://dlmf.nist.gov/5.11.E9), uniformly
  for bounded real gamma arguments and both signs of their large
  imaginary parts; L465 supplies the compatible sector branches.

These are imports, not reproved arithmetic theorems. Bettin's
microscopic shift theorem is not used at growing u. The finite
factor/submean scheme parallels L474, but its microscopic bounded
completion ratio is replaced by the calculation below.

Selected centers satisfy gamma_j in [T-2h,2T+2h], hence occupied
c_k lie in [T-(5/2)h,2T+(5/2)h]. Their radius-7h disks lie
horizontally in [T-(19/2)h,2T+(19/2)h], inside [T/2,3T] at
one fixed large onset. Vertically |y|<7h<7/16, so
1/16<Re(1/2+i(x+iy))<15/16. The completion factors are
holomorphic and nonzero there; all heights are comparable to T.
Reflection puts zeta real parts in [1/2,15/16], within 7.2(A).

### 2. Exact scale costs in a cell

Let the assigned distinct pairs form a finite set S_k and put
M=sum_(j in S_k) m_j. Fix an occupied cell, c=c_k, R=6h, and

    f(w)=Xi(c+Rw)/A(c),  S=sup_(|w|<=1)|f(w)|.

The selected roots have coordinates a_(j,+/-) with
|a|<=sqrt(17)/12<25/72. Every evaluation point
t=gamma_j+d_j v, |v|<=1, has real coordinate |w|<=5/12.
Consequently, with b_a(w)=(w-a)/(1-conj(a)w),

    |1-conj(a)w|>=739/864,
    |b_a(w)|<=660/739<9/10=:rho.                          (3)

Indeed |gamma_j-c|<=h/2, d_j<=2h give the root bound;
|t-c|<=5h/2 gives the evaluation bound. Substituting 25/72
and 5/12 in the elementary Blaschke inequalities gives (3).

Finite division at all 2M selected roots gives f=G product b_a
with |G|<=S. Remove exactly one copy at each root of pair j.
Since q_j(c+Rw)=R^2(w-a_(j,+))(w-a_(j,-)),

    F_j(c+Rw)/A(c)
      =R^(-2) G(w) product_(remaining 2M-2 factors) b_a(w)
        /[(1-conj(a_(j,+))w)(1-conj(a_(j,-))w)].            (4)

All other copies remain, including 2m_j-2 from this pair. Extra
zeros of Xi need not be divided out. L465's sector formula gives
(log A)'=-pi/4+O(1/T) on the real interval. Since h<1/16,
A(c)/A(t) and its reciprocal are bounded absolutely whenever
|t-c|<=7h. Thus (3)--(4) imply

    |F_j(t)/A(t)|^2<=C h^(-4) S^2 rho^(4M-4).

Use d_j^3<=8h^3 and integral_(-1)^1(1-v^2)dv=4/3.
The full contribution of this cell to B_u is bounded by

    C h^(-1) S^2 M rho^(4M-4)<=C h^(-1) S^2.             (5)

The last constant is absolute: if q=rho^4<1, then
M q^(M-1)<=sum_(r>=1) r q^(r-1)=(1-q)^(-2).
No zero-count hypothesis is used. Clipping J_j only reduces the
integral, and a singleton window contributes zero.

### 3. Completion and reflected continuous norm

Write z=x+iy, s=1/2-y+ix. By L018,
P(z)=s(s-1)pi^(-s/2)Gamma(s/2)/2, Xi(z)=P(z)zeta(s).
Bounded-strip Stirling, uniformly for |y|<=7h<7/16 and
T/2<=x<=3T, gives

    |P(x+iy)|^2/A(x)^2
        =(x/(2pi))^(-y)(1+O(1/T)).                       (6)

For clarity, the gamma modulus squared changes its power of x/2
from -1/2 to -1/2-y; its exponential exp(-pi x/2) cancels.
The pi factor contributes pi^y. The ratio of squared polynomial
prefactors is 1+O(1/T), uniformly in the bounded y range.
The gamma relative errors are uniform as well. There is no
holomorphic extension of the real modulus A in this argument.

For y<=0, put v=|y|L. The real part of zeta in (6) is
1/2+|y|. Theorem 7.2(A), positivity and enlargement of the
height interval to [1,3T] show

    integral_(T/2)^(3T) |Xi(x+iy)/A(x)|^2 dx
       <=C T exp(v) min(L,1/|y|).                        (7)

At y=0 use L. The factor (x/(2pi))^|y| is at most
C T^|y|, uniformly in this strip. For y>0 the functional
equation gives
|zeta(1/2-y+ix)|^2=|chi(1/2-y+ix)|^2
                         |zeta(1/2+y+ix)|^2.
Here conjugation changes the negative reflected height to x, and
|chi|^2=(x/(2pi))^(2y)(1+O(1/T)). Multiplication by (6)
again leaves (x/(2pi))^y. This proves (7) for both signs.
The two completion/chi powers partly cancel; the remaining
exp(|y|L) cannot be declared bounded as u grows.

### 4. Area cost, overlap and envelope

Let D_k be the open radius-7h disk at c_k and restore S_k^* for
the supremum S on radius 6h. The submean property of |Xi|^2,
using a radius-h disk about any maximizing point, gives

    (S_k^*)^2<=1/(pi h^2)
                   integral_(D_k) |Xi(z)/A(c_k)|^2 dArea.

Within D_k, A(x)/A(c_k) is bounded by the real-axis estimate in
Section 2. Centers spaced by h give overlap at most 15: a point
in D_k must satisfy |x-c_k|<7h. Sum only the finitely many
occupied disks, enlarge to the enclosing rectangle, and use (7).
The integral in y is, after v=|y|L,

    integral_(-7h)^(7h) C T exp(|y|L) min(L,1/|y|) dy
       =2 C T E(7u).

It follows that sum_k (S_k^*)^2<=C T h^(-2) E(7u).
Multiplying by (5) yields
B_u<=C T h^(-3)E(7u)=C T L^3 u^(-3)E(7u), proving (1).
All sums are finite and the integrands are nonnegative continuous
functions on compact rectangles. The single common T_0 covers
every domain and relative-error estimate, independently of u,
multiplicities and the selected subset.

For X>=1, E(X)=e-1+integral_1^X exp(v)/v dv. Applying
l'Hopital's rule to E(X)/(exp(X)/X), whose numerator and
denominator both tend to infinity, gives limit 1, since the
derivative ratio is 1/(1-1/X). This proves (2). In particular
K(2^r U) grows rather than tends to zero. Although for each T
the admissible sum is finite, its uniform majorant has no tail
tending to zero as U grows: any arbitrarily large fixed band
parameter becomes admissible on increasing T. This statement
concerns the envelope, not the unknown actual band masses.

### 5. The single-pair test and route decision

For one simple pair M=1, the product in (4) is empty, and the
weight in (5) is exactly 1. There is no occupancy gain to offset
the norm cost. This absence is real for the finite-factor tool:
in disk coordinates, f(w)=(w^2+1/16)/(1+1/16) has supremum 1
on the unit disk and roots +/-i/4. They represent a centered
pair with d=3h/2 in the admissible band whenever u<=L/24.
Dividing by q yields the constant (16/17)R^(-2).
Thus finite factorization alone supplies no additional
u-dependent decay for a single pair. This polynomial is only
a test of that local analytic estimate, not an actual-Xi model
or a counterexample to the desired arithmetic estimate.

The prescribed method provides neither summable decay nor an
independently supported compensation condition. Park this
implementation. Reopening it requires materially new arithmetic
selection/cancellation information; merely assuming large M or
a smaller selected norm would insert the missing estimate.
Fixed-u annuli, d_j>1/16 and full B(T)=o(TL^3) remain open.
Even that mass estimate would not give individual signs, all
higher signs or global mixed positivity.

### 6. Separate critical application audit, 29 October 2026

This is the first separate audit of Sections 1--5, under the unchanged
SPECIALIZE assessment
`drafts/literature/2026-10-29-l475-first-critical-audit-coverage.md`.
The primary results in Section 1 are reused in their inspected scope;
this is not an independent proof of those source theorems. No repair
to (1)--(7), new bound, or actual-Xi lower mass estimate is obtained.

**Finite sets, domains and uniform onset.** The entire nonzero Xi has
only finitely many zeros in each compact rectangle. P_T is finite
because 0<d_j<1/2 and its selected ordinates lie in [T-1/2,2T+1/2].
For this band d_j<=2h, giving the sharper center bounds in Section 1.
The outer real padding is (19/2)h<19/32, independent of T,u; its
containment in [T/2,3T] therefore needs only a fixed onset. The full
closed real-part interval [1/16,15/16] is compactly inside Re s>0.
Gamma arguments have real parts in [1/32,15/32], imaginary parts
x/2 comparable to T, and lie in a fixed closed sector avoiding the
negative axis. The polynomial completion factors are nonzero at
these heights. Choose T_0 once to cover these domains and the uniform
gamma/chi remainders, and enlarge it so log T_0>16. No step requires
an onset depending on u, h^(-1), multiplicity or the zero set.

**Finite division and multiplicities.** Half-open cells assign a
boundary center to exactly one cell. In disk coordinates,
|a|<=sqrt(17)/12<25/72 and |w|<=5/12. Thus
1-|a||w|>=739/864 and |w-a|<=55/72, giving
|b_a(w)|<=660/739<9/10. Selected roots are strictly interior;
finite Blaschke division applies to f, holomorphic beyond the closed
unit disk and bounded there. Its quotient is holomorphic after
removing the selected zeros, and has boundary modulus at most S,
so the finite supremum statement applies also with repeated roots.
Unselected zeros, even boundary zeros, create no division issue.

In (4), q_j=R^2(w-a_+)(w-a_-); the two denominator factors
1-conj(a_+)w and 1-conj(a_-)w remain after cancelling precisely
one numerator copy at each root. There are exactly 2M-2 residual
Blaschke factors, even when m_j>1. Squaring therefore gives
R^(-4)rho^(4M-4), not R^(-2) or a multiplicity-free quotient.
After d_j^3 and the dv integral the scale is h^(-1), with the full
sum of multiplicities M. The bound
M(rho^4)^(M-1)<=(1-rho^4)^(-2) is uniform for every integer M>=1.
Empty cells are omitted and singleton clipped windows have integral
zero. Extending J_j to [-1,1] uses only nonnegativity.

**Horizontal versus vertical normalization.** Set a=log A on the real
axis. L465's digamma formula (4), applied at 1/2+ix, gives

    a'(x)=2x/(x^2+1/4)-Im g'(1/2+ix)=-pi/4+O(1/x).

Here g=log(pi^(-s/2)Gamma(s/2)), and the derivative is taken before
restricting to real x. This verifies the derivative assertion without
differentiating a bare vertical Stirling equivalence. Integrating over
|x-c_k|<=7h<7/16 gives both horizontal A ratios bounded by absolute
constants. A itself is used only on the real axis.

For the vertical comparison, the squared polynomial prefactor ratio
is 1+O(x^(-2)); the pi power contributes pi^y, and the squared gamma
ratio contributes (x/2)^(-y)(1+O(x^(-1))). These give (6), uniformly
on the entire bounded y interval, including y=0. The relative error
comes from sector Stirling with remainder, not solely from 5.11.9's
leading equivalence. For y=-b<=0 the completed factor is
(x/(2pi))^b times |zeta(1/2+b+ix)|^2. For y=b>=0, reflection and
conjugation produce the same right-side zeta value, and multiplication
of (x/(2pi))^(-b) by the chi square (x/(2pi))^(2b) again leaves
(x/(2pi))^b, up to a uniform bounded relative factor. Hence both
directions, rather than only one, obey (7).

Theorem 7.2(A) is used on [1,3T] with real part 1/2+b in
[1/2,15/16]. Replacing log(3T) by log T changes an absolute constant
only: min(log(3T),1/b)<=C min(log T,1/b), including b=0 by the
stated convention. Also (x/(2pi))^b<=C T^b uniformly for
x in [T/2,3T] and 0<=b<=7/16. This validates the cumulative-interval
enlargement and (7) without a short-interval or discrete mean theorem.

**Submean, overlap and all scale powers.** A maximum on the closed
radius-6h disk exists. The open radius-h disk about a maximizing point
is contained in the open radius-7h disk, even if the point lies on
the inner boundary. The area submean inequality therefore gives the
factor 1/(pi h^2) as written. At a fixed point, eligible centers lie
in a real interval of length 14h on an h-spaced lattice; at most 15
can occur. The horizontal A comparison is uniform on each disk.
No assumption on how many cells are occupied enters this bound.

With v=bL, min(L,1/b)db=min(1,1/v)dv, including its continuous
value at zero. Thus the two-sided area rectangle contributes
2CT E(7u). The factors h^(-1) and h^(-2) give precisely
T h^(-3)E(7u)=T L^3 K(u). Every zero sum and disk union here is finite;
all integrands are continuous on their compact domains after the
specified entire divisions. Tonelli for nonnegative integrands or
finite additivity suffices; no singular zero-conditioned interchange
or u-dependent constant has entered the calculation.

**Tail quantifiers and the obstruction's scope.** For X>1,
E'(X)=exp(X)/X and (exp(X)/X)'=exp(X)(1-1/X)/X. Both original
functions tend to infinity, so their ratio tends to one. Consequently
K(u)~exp(7u)/(7u^4). More explicitly, for every fixed U>=1 and every
integer r>=0, take T with log T>16*2^r U. The dyadic term
K(2^r U) is then admissible. These terms are unbounded as r grows;
in particular the supremum over T of the finite admissible envelope
tail is infinite for each U. The assertion concerns this majorant,
not the sum of true B_u(T), and it does not exchange two actual-mass
limits or assert that all these bands contain zeros.

For the local polynomial test, |w^2+1/16|<=17/16 on |w|<=1,
with equality at w=1; the stated supremum is exactly one. Its only
zeros are the simple roots +/-i/4. Scaling by R=6h gives d=3h/2,
and dL=3u/2 is in the selected band when u<=L/24. The quotient is
exactly 16/(17R^2). For arbitrarily large u this condition can be met
by increasing T, so the normalized local division estimate cannot
gain a factor tending to zero with u for all such disk functions.
This model imposes no actual-Xi global structure or zeta mean-square
constraint. It establishes neither a lower bound for the global norm
cost nor impossibility of a sharper actual-Xi estimate. The parked
method and its unresolved arithmetic compensation remain exactly as
qualified in Section 5. No repeated audit of this unchanged statement
is warranted.

## Mathlib

Full matching coverage for (1), the band specialization and its
uniform actual-Xi normalization has not been checked. Supporting
finite Blaschke, submean, Stirling, functional-equation and mean-square
coverage is also not checked here; no absence claim is made. The
precise primary results imported above and the written specialization
are the mathematical evidence.
