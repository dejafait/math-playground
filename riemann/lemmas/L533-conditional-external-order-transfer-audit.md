# L533 — Conditional external-order transfer: audit

## Hypotheses

Work over F=Q(sqrt(-3)). Let beta_* be the supremum of {1/2} and
the real parts in [1/2,1] of zeros of primitive finite-order Hecke
L-functions over F. Poles are not zeros. Fix sigma_0 in [7/8,1) with
beta_*>sigma_0. No beta_*<=7/8 conclusion is assumed. The earlier
beta_*<=11/12 input used in L532 is not needed for this conditional step.

Fix l_x,l_y>0, ell>=0, h=1-l_x+ell>0, z_0=17/50,
0<d_min<d_max<infinity and 0<e<10^(-3). Real geometry, losses and a
finite slot system precede the primitive target eta. When prime slots are
present, their lengths ell_i>0 are fixed, sum to ell, and their scales
are P_i=Z^ell_i; each W_i is smooth on a fixed compact annulus in (0,infinity).
Fix the target's arithmetic data, excluded primes and test functions.
Put X=Z^l_x, Y=Z^l_y,
U=Z^d, d_min<=d<=d_max, and

\[
 C(s)=s+l_x/2-1+h/6,\qquad T=Z^\tau>2,
 \quad 0<\tau\le d_{\min}/100.
\]

Assume the following source interfaces, individually. They are not claims
that the entire arithmetic construction has been verified.

1. **Physical identity and full correction.** An independently specified
   physical quantity has the absolutely convergent high representation
   of `def:stage-high-data` in the source cited below. The contribution
   of a fixed finite physical bin B is its restriction to B in

   \[
   \frac1{(2\pi i)^3}\int_{(3)}\int_{(3)}\int_{(2)}
   X^{1/2-z}Z^{s+z-1}Y^{w-1}e^{(s+z-1)^2}M(z)\widehat W_1(w)
   \sum_{u\in B}q_u^{-z}\overline{\xi(u)}
   \frac{\zeta_F^S(6z)L^S(w,\chi_\bullet(u))}
        {L^S(s,\eta\overline{\chi_\bullet(u)})}
   \mathfrak H_{\eta,u,Z}(s,w,z)\,dz\,dw\,ds.                 \tag{1}
   \]

   Here |xi(u)|<=1. The full correction is holomorphic in neighborhoods
   of the source regions

   \[
   \mathcal D_1(\epsilon_0)=\{\Re s\ge.51,\ \Re z\ge.34,
   \ \Re w\ge-.01,\ \Re(s+w)\ge1+\epsilon_0\},\quad\epsilon_0>0,
   \]
   \[
   \mathcal D_2=\{\Re s\ge7/8,\ \Re z\ge33/200,
                   \ \Re w\ge19/20\}.
   \]

   For every fixed real box K in either region and fixed D>0 it obeys
   |H|<=C Z^B_H(1+|Im s|+|Im w|+|Im z|)^J_H for q_u<=Z^D.
   These constants and finite degrees are uniform in rows and heights,
   and fixed before tau or an external differentiation order is chosen.
   No nonvanishing of H or its local factors is required. M and W_1-hat
   have all polynomial decay orders on the compact real ranges used;
   M's real argument stays strictly positive.
2. **Global and buffered bounds.** The bin is chosen before contour
   motion, has q_u comparable to U with fixed comparison constants,
   contains O(U) rows, and has labels i,a with .51<=a<=beta_*.
   The labels range over the fixed finite grid of `lem:buffered-bins`.
   The retained family contains the original zero-extended numerator,
   denominator, finite ray twists and conjugates. Its primitive members
   are nonprincipal, have conductor O_eta(U), and deleted-factor radical
   O_eta(U). Bounded principal-presentation rows excluded by that detector
   are outside this bin statement.

   Assume the global polynomial strip bounds and reciprocal bounds on
   Re s>=beta_*+v for fixed v>0 supplied by `lem:hecke-strip-growth`,
   `lem:logarithmic-control` and `lem:deleted-euler-factors`. Use absolute
   Euler bounds farther right. These bounds are uniform in rows, with
   fixed polynomial conductor and height degrees. For clarity, principal
   upper/logarithmic bounds in the cited input concern
   (s-1)zeta_F(s)/(s+1); only its reciprocal bound passes directly to
   1/zeta_F. Deleted-factor inverse bounds require positive real part;
   negative-strip uses here are upper bounds only.

   On Re v>=a+6e, |Im v|<=(3i+2)T, assume the original presentations
   are zero-free and their values and reciprocals are O_eta,e,epsilon
   (U^epsilon). On Re v>=a+8e in the applicable compact real range
   assume their logarithmic derivatives are O_eta,e(log U). Assume the
   reflected numerator estimate on Re w=1-a-6e from the same source.
   Thresholds may depend on fixed tau and losses, but orders do not.
3. **Complete finite external coordinates.** Once the target and slots
   are fixed, all buffered arguments used to verify the central estimate
   below have imaginary parts

   \[
   \gamma_j+\sum_{k=1}^m a_{jk}v_k+b_j,
   \quad |\gamma_j|\le(3i+1)T,\quad |b_j|\le H_0,              \tag{2}
   \]

   with one fixed finite matrix (a_jk), m>=3, and fixed H_0. The list
   includes the three original heights Im s, Im w, Im z even if a column
   is zero, and every further external witness/dyadic/prime frequency.
   Internal measures are not silently converted into external coordinates.
   The matrix is an input; its completeness for `lem:high-bin` is not
   established here. Pure twists have been put in the arithmetic arguments,
   leaving untwisted external transforms.
4. **External density and smoothness.** Whenever an external integral or
   trace is estimated, its kernel is nonnegative and jointly Borel in
   heights and a compact set of real parameters. In a fixed invertible
   linear change of external coordinates it is bounded by the physical
   Gaussian/Mellin product times a density rho satisfying
   sup_(r,Z,v)(1+|v|)^L |rho_(r,Z)(v)|<infinity for every integer L>=0.
   This is pointwise, not merely almost everywhere on full-dimensional
   space. The change and its inverse have fixed coefficients. The tests
   have uniformly bounded smooth seminorms at each requested external
   order. Their supports/real ranges and any number of external variables
   do not grow with N or Z. Relevant domains and arithmetic factors are
   Borel, jointly so for real-interval integrations.

   On each discarded domain or join, assume a bound Z^B(1+|v|)^J
   for its arithmetic factor, with finite B and J>=0 fixed before tau,N. A fixed
   additional factor (1+T)^H is permitted when arising from bounded
   retained base heights in (2); H>=0 is also fixed first. All extended
   coordinates must preserve reciprocal buffers or use global bounds.
   An internal measure with only a fixed weighted L1 bound remains inside
   the arithmetic factor at that fixed order. If it depends on the row,
   no common-density row norm inequality is inferred without an additional
   common-measure hypothesis.
5. **Full central estimate with fixed internal orders.** On the eventual
   retained physical contours, H is a sum of a fixed finite nonempty set
   of pieces. For each piece and each point, B is partitioned into at most
   C(1+log Z)^D sets. On each such set C_nu assume

   \[
   \sum_{u\in C_\nu}|L^S(w,\chi_\bullet(u))H^{(\lambda)}_{\eta,u,Z}|
   \le C_\eta U^{R+\delta/2+\epsilon_c}
       Z^{\ell(z_0-1/2)+g+\epsilon_c}(1+T)^{A_\eta},          \tag{3}
   \]

   where delta=2a-1, epsilon_c>=0, A_eta>=0 is finite, and (R,g)
   range over a fixed bounded set. The constants and A_eta are uniform
   in retained points, row subsets and moving labels. All retained
   internal moment/profile/row-selection orders have already been fixed,
   independently of tau,N. Equation (3) concerns the complete expressions
   after any auxiliary integrations: their discarded contributions have
   already been included using global/absolute estimates. The pieces
   need not extend holomorphically or have separately measurable labels.

These are the global, buffered, density and internal-profile contracts of
the approved audit. In particular (3) is not deduced from a merely truncated
auxiliary expression. L532 hypothesis 6 is the downstream interface being
tested, not an assumed theorem; L531 is further downstream context.

## Conclusion

Under these contracts, the external analytic transfer passes. Set

\[
 M_k=\max_j|a_{jk}|,\qquad c_k=\frac1{2m(1+M_k)},
 \qquad |v_k|\le c_kT.                                      \tag{4}
\]

One allocation (4) keeps all the arguments (2) in their specified buffered
height ranges for sufficiently large Z. This includes physical Im(z) when
it enters a prime profile. The allocation is used once for the entire list.

There is a finite B_eta, chosen before tau,N, such that the original fixed
bin contribution (1) equals the retained integral on

\[
 \Re s=a+16e,\qquad\Re w=1-a-6e,\qquad\Re z=z_0              \tag{5}
\]

up to O_eta,N,tau(Z^B_eta T^(-N)) for every fixed integer N>=0.
The constants for its physical height box are those from (4).
The retained integral has the source bound

\[
 O_\eta\left(
 Z^{C(\sigma_0)+E_{\max,Z}(d)+(16-6l_y)e
                  +(1+d)\epsilon_c+d\epsilon_d+\epsilon_p}
 (1+T)^{A_\eta}\right),                                    \tag{6}
\]

for each epsilon_d,epsilon_p>0, where E_max,Z is the supremum of

\[
 a-\sigma_0+h(z_0-1/6)-a l_y-\ell/2+g
                  +d(R+\delta/2-z_0)                       \tag{7}
\]

over pairs occurring in (3). An empty bin contributes zero.
Neither A_eta nor B_eta is increased by later external differentiation.
For additional external tails satisfying contract 4, the same independence
holds; it does not establish the still assumed auxiliary accounting in (3).

This is a conditional reproduction of the cited analytic interface, not
a verified application of the whole `lem:high-bin`, a new zero-free region,
initial Xi signs, or RH. It does not replace the arithmetic, internal-order,
or actual-coordinate realization assumptions of L532. No uniform threshold
over targets, effectiveness, or limiting assertion as tau tends to zero
is claimed.

## Proof

Source: OpenAI, *The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane
Re(s)>7/8*, September 30, 2026, commit
`1581d4cbdd69a0faf34b2089614fe2a814316a6a`,
[primary TeX](https://raw.githubusercontent.com/openai/math/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex).
The precise source results are `lem:external-contour-tails` (rendered
lines 5337–5458), `lem:fixed-bin-contour` (5464–5551),
`lem:bin-contour-accounting` (5662–5799), and the external-order cases of
`lem:smooth-calculus` (1019–1193), `lem:detector-dyads` (4117–4225),
`lem:bin-prime-bound` (14192–14254). The physical application is
`lem:high-bin` (14858–14993). Stable labels identify the theorems; line
numbers are retrieval coordinates. The source claims these conclusions
already. Independent reproduction is justified by the unresolved order and
domain qualifications of the external input, not by a novelty claim.

The upstream assertions retained as contracts are `def:stage-high-data`,
`lem:buffered-bins`, the global results named in hypothesis 2, and
`eq:stage-central-bound`. The correction formulas
`eq:holomorphic-selected-tuple` and `eq:compensated-all-height-majorant`
(8198–8261) are the proposed source realization of hypothesis 1, not
independently verified inputs imported without qualification here.

### Integrated tails and traces

Use the l1 norm on R^m; any fixed norm is equivalent. Suppose
K(v)<=C_L(1+|v|)^(-L) and |F(v)|<=C Z^B(1+|v|)^J on a Borel domain.
Multiplication, followed by an integral of a nonnegative function, gives

\[
 \int_{\max|v_k|>cT}K|F|\le C C_L Z^B
             \int_{|v|>cT}(1+|v|)^{J-L}\,dv.
\]

For q=L-J>m, dilation/radial integration bounds the last integral by
C_(q,m,c) T^(m-q) for T>=1. Taking an integer L>N+J+m proves
O_N(Z^B T^(-N)). For unequal positive box constants use their minimum.
On a coordinate slice v_k=t, instead integrate in m-1 variables:

\[
 \int_{\mathbb R^{m-1}}(1+|t|+|\widehat v_k|)^{-q}
             \,d\widehat v_k
 = (1+|t|)^{m-1-q}
       \int_{\mathbb R^{m-1}}(1+|u|)^{-q}\,du.
\]

This is finite for q>m-1. Thus L>N+J+m-1 suffices for the trace,
including t=+c_kT and t=-c_kT. Restricting a positive integral to the
permitted domain only reduces it. Uniform joint Borel hypotheses permit
Tonelli and integration over compact real intervals of bounded length.
These are trace estimates, not consequences of an integrated tail alone.

If a fixed factor (1+T)^H remains from a base height, request decay
N+ceil(H) instead of N. For T>=1 it is then absorbed with a fixed
constant. The scale exponent B is unchanged. This also handles a global
polynomial bound evaluated at gamma+A v with |gamma|<=C T:
1+|gamma+A v|<=C'(1+T)(1+|v|). No replacement of T by Z^tau is needed
in B. A finite sum of errors takes the maximum of their fixed B's;
any predetermined polynomial multiplicity contributes a fixed scale
degree. Neither operation depends on N or the subsequently chosen tau.

For (1), in the order (Im s,Im z,Im w), the map to
(Im(s+z),Im z,Im w) has determinant one and fixed inverse. On a compact
real box the kernel is, up to a bounded real Gaussian factor,

\[
 e^{-y_1^2}|M(r_z+iy_2)|\,|\widehat W_1(r_w+iy_3)|.
\]

Each factor has arbitrary polynomial decay. Choosing the same sufficiently
large order on each non-Gaussian factor gives a bound by
C_L(1+|y|)^(-L), hence by C'_L(1+|v|)^(-L). Its full L1 norm is uniformly
finite. The same argument applies after adjoining a density satisfying
hypothesis 4 and a fixed invertible linear change. This square invertible
kernel change is distinct from the generally rectangular matrix (a_jk)
of buffered arguments. An L1 density alone would not justify these slice
bounds; no such implication is used.

### Physical contour domains and a common scale degree

First fix the bin and use its finite sum. Its O(U) cardinality, conductor
and radical bounds, real scale powers in (1), global L-bounds and the
full-correction bound give Z^B times a fixed height polynomial on each
of the following global contours. B includes this coarse row count;
the finer arithmetic row estimate (3) is not needed for discarded pieces.
All real ranges and d ranges are fixed and bounded. A finite cover by
real boxes contained in D_1(5e) controls the nonrectangular union of paths
below. Thus the correction assumption on boxes suffices, without assuming
that one large box crossing outside D_1 is valid. Fixed annular comparison
constants can be absorbed into q_u<=Z^(d_max+1) by increasing the threshold.

Starting at (Re s,Re w,Re z)=(3,3,2), move z to z_0 and then s to
beta_*+20e. Here 6Re z>=6z_0>1; no scalar zeta pole is crossed.
The reciprocal remains to the right of beta_*, and w=3 is absolute.
The trace estimates on the compact real segments make the joins vanish
as their heights tend to infinity. All other axes use global estimates,
so Fubini and these contour limits are justified by absolute majorants.

Next move w from 3 to 1-a-6e while s remains beta_*+20e. Throughout,
Re(s+w)>=1+(beta_*-a)+14e>=1+14e. Also Re w>=-6e>-.01,
and the numerator is nonprincipal and entire. Thus H stays holomorphic
and the reciprocal remains global. Numerator strip bounds, including
upper bounds for deleted factors on a possibly negative strip, control
all w-joins. No inverse deleted-factor bound on that negative strip is used.

Now discard the complement of the physical height box from (4) while
s is still on the global line. The integrated estimate gives
O_N(Z^B T^(-N)). In particular no discarded s-height is taken to a line
on which the reciprocal estimate is only buffered.

Move just the remaining s segment to a+16e. Its rectangle satisfies
Re(s+w)>=1+10e and Re s>=a+16e>a+6e. Its height satisfies the buffer
by (4), proved below. Hence the reciprocal is holomorphic there and its
buffered bound holds throughout. The correction and the other scalar
factors have no poles on this rectangle. On either s-join, s is the
denominator's only variable. To bound the positive absolute integral, extend the
z and w height axes, keeping s fixed on its join. These extensions do not
change the denominator's argument. On those axes use the global numerator
and full-correction bounds, not their retained estimates. The coordinate
trace estimate yields O_N(Z^B T^(-N)); the real join length is bounded.
There is no later w- or z-join with a buffered s-axis being extended.

Take B_eta to dominate the finitely many scale degrees just used, including
any fixed buffered loss U^epsilon<=Z^(d_max epsilon). These degrees and
their height orders were fixed without tau,N. This proves the physical
contour assertion. The full H was used throughout. None of its pointwise
pieces, nor a quotient by an individual local factor, was continued.

### A single allocation, including physical Im(z)

For every row j of the stipulated matrix,

\[
 \left|\sum_k a_{jk}v_k\right|
 \le T\sum_k|a_{jk}|c_k
 \le\frac{T}{2m}\sum_k\frac{M_k}{1+M_k}<\frac T2.            \tag{8}
\]

The inequality is strict for a finite matrix; zero columns cause no
problem. Together with (2), this puts the argument below
(3i+3/2)T+H_0. Once T>2H_0, it lies strictly inside (3i+2)T.
Since tau>0 is fixed, that is a legitimate later Z threshold. Every
c_k is positive and at most 1/(2m)<=1/2, as required in the physical
contour argument. Subsequent estimates use subsets of this same box;
they never add another T/2. Constants and the matrix do not change when
N increases.

Here is the load-bearing physical prime-profile check. Write z=r_z+i t_z.
The source main-slot profile contains W_i(y)y^(r_z-1)y^(i t_z), where
y=q_p/P_i. In a Mellin inversion use the untwisted profile
V_(P_i,r_z)(y)=W_i(y)y^(r_z-1)/log(P_i y) for the von Mangoldt version.
Its transform at s=alpha+i v is evaluated at v, while the corresponding
Dirichlet argument is s-i t_z and the scale factor is
P_i^(s-i t_z-1/2). Consequently its imaginary argument is v-t_z,
and the modulus of the scale factor is P_i^(alpha-1/2).
The sign or orientation of a conjugate presentation changes matrix signs
but not (8). Both v and t_z must be columns of the one matrix; any
other separating shifts are additional columns there, not new allowances.
For the two indicated coefficients of magnitude one,
|v-t_z|<= (c_v+c_z)T<=T/(2m); (8) handles the complete argument.

For r_z in a compact real range and y in the fixed annulus, all fixed
logarithmic derivatives of W_i(y)y^(r_z-1) are bounded uniformly. Also

\[
 (y\partial_y)^j\{\log(P_i y)^{-1}\}
 =(-1)^j j!\{\log(P_i y)\}^{-j-1}.                           \tag{9}
\]

For the fixed positive slot length ell_i and P_i=Z^ell_i, log(P_i y)
is bounded below by a positive multiple of log P_i at a later threshold.
Leibniz's rule and (9) therefore give uniform seminorms at every fixed
external order; there is no P_i power proportional to that order. This
checks the physical twist and its seminorm bookkeeping. It does not prove
the row count, the complete selection measure, or the prime/arithmetic
central estimate. Those remain contracted.

### What later differentiation changes

For a smooth function f of logarithmic variables supported in a fixed
compact subset of R^r, integrate (1-Delta)^k f by parts. It gives
|f-hat(v)|<=C_k p_(2k)(f)(1+|v|^2)^(-k). Thus
the weighted Fourier L1 norm of order J is bounded by a seminorm of order
J+r+2 (choose an even 2k>J+r). For an external tail request J+N instead.
For a Mellin trace, integrate derivatives of e^(alpha u)V(e^u) in u;
on a compact alpha range this gives decay (1+|v|)^(-N) with a finite
sum of weighted logarithmic derivative integrals. Annular support removes
boundary terms. For M's underlying smooth-at-zero, Schwartz-at-infinity
test, compact positive alpha ranges give the same endpoint vanishing.
These computations reproduce the relevant part of `lem:smooth-calculus`.

A pure twist V(y)y^(i omega) may equivalently be moved from the transform
to the Dirichlet argument by writing the inversion with the untwisted V,
as in the preceding prime example and source dyadic formula (4154–4162).
One must not estimate derivatives of the twisted profile by powers of
omega and then pretend their orders are fixed. Here omega stays in the
arithmetic factor; the global polynomial bound or buffered range already
accounts for it. All high-order derivatives act on V alone.

Specifically, inverse dyadic tails remain on Re(s+sigma)=2, while their
finite joins stay in the assigned reciprocal buffer. Plain dyadic joins
use global numerator bounds; their absolute-line tails use absolute bounds.
Prime logarithmic-derivative tails likewise stay on the absolute line;
their joins use the allocated buffer. The source bounds in these cases
have fixed scale and height degrees before selecting the external order.
The tail/trace argument above therefore applies to them without asking
for a new internal moment at a larger profile order. Potentially negative
central exponents on a bounded dyadic-length range only increase the
required finite N after tau is fixed; they do not change B or J.

If an internal measure mu is controlled only by
integral (1+|u|)^J d|mu|(u)<=C at a fixed J, integrate it inside F using
that bound and the corresponding fixed internal estimate. It supplies no
bound for a higher weight, and no coordinate trace. If an internal row
estimate requires a common coefficient measure, its commonness is a
separate part of the central contract. None of the above differentiates
mu or reapplies that row estimate to an N-times differentiated profile.

### Retained bound and order of choices

At each retained physical point, apply the triangle inequality to the
full row sum, use (3) on the finitely many pointwise pieces, and majorize
every real exponent by the supremum over all pairs that occur. That
supremum is finite. This gives a measurable, constant-in-height bound
for the original continuous row sum; no integration or measurability of
the individual subdivisions is needed. For every epsilon_p>0 the fixed
pointwise multiplicity (1+log Z)^D is O(Z^epsilon_p).

The remaining reciprocal costs U^epsilon_d. The scalar zeta is absolutely
bounded because 6z_0>1. The physical test kernel has a bounded full L1
norm, so restricting its box cannot increase that norm. In particular,
integration introduces no new power of T into A_eta.

For completeness, the real outside power of Z is

\[
 l_x(1/2-z_0)+a+z_0-1-a l_y-dz_0+(16-6l_y)e.
\]

Adding d(R+delta/2+epsilon_c)+ell(z_0-1/2)+g+epsilon_c,
the reciprocal cost d epsilon_d and multiplicity epsilon_p, then
subtracting C(sigma_0), leaves exactly (7) and the losses in (6).
The identity uses 1-l_x+ell=h. This verifies that tail-order changes
have not been hidden in a modified real exponent.

The order of choices is therefore: fixed geometry and slots; target data,
internal orders, global scale/height degrees, full coordinate matrix and
fixed central estimate; then positive tau subject to the stated height
conditions; then external decay orders large enough for the desired N;
then Z exceeding all thresholds. Fixed base-height polynomials are absorbed
as explained above, not by increasing a degree with N. In particular, for
any desired scale exponent b and fixed tau>0, choosing an integer
N>(B_eta-b)/tau makes Z^B_eta T^(-N)=o(Z^b). This last choice is legitimate
only because B_eta has already been fixed. It says nothing about whether
the assumed central bound or detector height conditions can actually be
realized by the complete arithmetic construction.

The audit establishes precisely this conditional transfer. It leaves the
full list of selection coordinates, the pointwise external-density
contracts in that application, fixed internal moment/profile uniformity,
and full auxiliary central accounting as explicit inputs. The physical
identity/correction construction, bootstrap, H nonvanishing, other row
ranges, manuscript/import closure and all-degree Xi positivity also remain
outside the result. There is no complete candidate resolution here.

## Mathlib

Full matching coverage for this conditional family-003 contour/degree
interface has not been checked. Fourier inversion, integrability and
complex contour theorems would support only parts of the argument; no
matching formal theorem, Lean certificate or import-closure check is
claimed. This audit is an analytic proof replay, with no numerical or
symbolic certificate needed for its norm, domain and quantifier checks.
