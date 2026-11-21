# Corollary C048q: complex scaling defeats this absolute Rice closing budget

## Hypotheses

Use C048k's actual entire interpolation and finite kernel, with the
normalizations and principal branches in C048l:

\[
 E(s)=\frac{\sqrt\pi\,4^{-s}I(s+1/2)}{Z\Gamma(s+1/2)},
 \quad Z=\gamma_0>0,\quad E(k)=\gamma_k/\gamma_0,
 \quad B_d(s)=\frac{d!}{\prod_{k=0}^d(s-k)},\quad F_d^I=E B_d.
\]

Integers d>=3 tend to infinity. Set

\[
 \ell=\log d,\quad h=d/\ell,\quad D=d/\ell^2,
 \quad c=-1/4,\quad b=d+1/2.
\]

Let R_d be the positively oriented rectangle with real edges c,b and
heights +-h. With the principal value Log(-i/d)=-ell-i*pi/2, put

\[
 W_d(s)=F_d^I(s)\exp\{s\operatorname{Log}(-i/d)\},\qquad
 A_d(i)=\frac1{2\pi}\int_{\mathrm{top,right,bottom\ of}\ R_d}
                         |W_d(s)|\,|ds|.
\]

Reuse C048l's uniform actual-I relative comparison, explicit main-term
identities and unweighted closing bound, including their existential
common onset. No RH, actual-Xi sign, nonvanishing of U_d(i), infinite
opening, or bound on signed cancellation is assumed.

## Conclusion

For the exact target in assessment1679/1680,

\[
 \lim_{d\to\infty}\frac{\log A_d(i)}{h}=\frac\pi2,
 \qquad A_d(i)=\exp\{(\pi/2+o(1))d/\log d\}\longrightarrow+\infty.
                                                               \tag{1}
\]

In particular A_d(i)>=exp(pi*h/3) eventually. The lower bound comes
from the actual top-edge subarc c<=Re(s)<=c+1/ell, not a point value.
The exact finite normalization is

\[
 U_d(i):=\frac{J_d(i/d)}{\gamma_0}
       =\frac{(-1)^d}{2\pi i}\int_{\partial R_d}W_d(s)\,ds.
                                                               \tag{2}
\]

Thus this rectangle fails the absolute closing test at this single
nonreal scaled argument. This REPRODUCTION specialization supplies a
local informative obstruction, not a new general Rice theorem or
progress beyond the assessed source tools. It says nothing about the
size of the signed sum of closing integrals, other contours, other
arguments, a compact nonreal-zero mass bridge, H_d=o(d), S_F=0, or RH.
Independent conceptual audit1683 below accepts (1)--(2) without
correction under the stated C048k/C048l contracts.

## Proof

### Imported inputs and exact finite normalization

The imported finite Rice template is P. Flajolet and R. Sedgewick,
*Mellin transforms and asymptotics: Finite differences and Rice's
integrals*, Theoret. Comput. Sci.144(1995),101--124,
[Section2 Lemma1/(6), pp104--105](https://algo.inria.fr/flajolet/Publications/FlSe95.pdf).
It requires analyticity on a domain containing the enclosed integers
and the finite contour. The separate polynomial-growth/infinite-opening
statements are not used. Principal logarithms, exponentials and powers
are as in [NIST DLMF4.2.3/19/27--29](https://dlmf.nist.gov/4.2).
Assessment1679 and source-notes1680 checked exactly these hypotheses;
the full-argument gamma inputs behind C048l are
[DLMF5.11.1 and 5.11(ii)](https://dlmf.nist.gov/5.11).
No source theorem is reproved. The specialization is necessary because
these sources do not supply this degree-uniform weighted edge bound.

For each fixed d, E(s)exp(s Log(-i/d)) is entire. The only poles of
W_d in the closed rectangle are the simple poles k=0,...,d, all in
its interior. At k its residue is

\[
 (-1)^{d-k}\binom dk\frac{\gamma_k}{\gamma_0}(-i/d)^k.
\]

Multiplying their sum by (-1)^d gives (2), since
(-1)^k(-i)^k=i^k. This checks the integer samples and normalization
without a second factorial or a change of branch. Positive orientation
traverses the left edge downwards, so an upward-left-segment formula
would have prefactor (-1)^(d+1)/(2pi*i). All closing sides remain in
(2); their signed sum is only bounded in modulus by A_d(i).

For s=x+iy, the principal-power identity gives exactly

\[
 |\exp\{s\operatorname{Log}(-i/d)\}|=e^{-\ell x+\pi y/2}.
                                                               \tag{3}
\]

It is essential to retain y and its sign. In particular the top and
bottom multipliers have different moduli.

### Uniform lower comparison on a top-edge subarc

Write F_d=F_d^I. C048l(7)--(13) give on the entire top edge

\[
 \log|F_d(x+ih)|=G_d(x)+r_d(x),\qquad
 \rho_d:=\sup_{c\le x\le b}|r_d(x)|\longrightarrow0,       \tag{4}
\]

where p=x+1/2+ih, z=x+1+ih, q=d+1-x-ih and

\[
 H(v)=(v-1/2)\operatorname{Log}v-v+\tfrac12\log(2\pi),
\]
\[
 G_d(x)=\log\frac{2\pi\sqrt\pi\Gamma(d+1)}Z-x\log4
       +\log|S(p)|-\pi h-\Re\{H(z)+H(p)+H(q)\}.           \tag{5}
\]

Here S is C048l's exact nonzero Lambert main term. The error in (4)
is a two-sided logarithmic comparison for the actual I, uniformly:
|I/S-1|<=epsilon_d with epsilon_d=(17/10)(log(2d))^(9/2)/h->0,
and the other errors are O(1/h+exp(-2pi*h)). Once epsilon_d<1/2,
|I/S|>=1-epsilon_d and |log|I/S||<=2epsilon_d. Thus no zero of I
occurs on the subarc. We never differentiate r_d or I/S.

We need a lower bound on variation, whereas C048l's decreasing
main-term estimate was an upper bound. Bound the absolute derivative
of the explicit (5). All three arguments p,z,q have positive real
part, h<=|p|,|z|,|q|<=2d eventually. Consequently, with principal
logarithms,

\[
 |\operatorname{Log}v|\le\ell+\log2+\pi/2,
 \quad |H'(v)|\le\ell+\log2+\pi/2+1/(2h)
 \quad(v=p,z,q).                                           \tag{6}
\]

For w=W_0(2p/pi), C048l(8),(13) give, uniformly on this edge,

\[
 \Re w>0,\quad |\Im w|<\pi/2,\quad 1\le|w|\le2\ell,
 \quad |w'|\le1/h,
\]
\[
 \frac{S'(p)}{S(p)}=2\operatorname{Log}(w/2)
       +\frac94w'-\frac1{2p}-\frac{w'}{2(1+w)}.             \tag{7}
\]

The eventual lower bound |w|>=1 follows from the uniform Re(w)>=1
argument in C048l Section1. Since |1+w|>=1 and
|arg(w)|<pi/2, for ell>=2,

\[
 |S'/S|\le2(\log\ell+\log2+\pi/2)+13/(4h).
\]

Using z'=p'=1, q'=-1, (5)--(7) therefore imply

\[
 |G_d'(x)|\le3\ell+2\log\ell+C+19/(4h)\le4\ell          \tag{8}
\]

eventually, with one absolute constant C independent of x,d. This
only differentiates explicit analytic functions in positive-real-part
domains. It uses full arguments, not a growing-shift gamma shortcut.

Set delta_d=1/ell. For every x in [c,c+delta_d], an actual subinterval
of [c,b], integrating (8) gives G_d(x)>=G_d(c)-4. Equation (4) then
gives the uniform actual-integrand lower bound

\[
 \log|F_d(x+ih)|\ge\log|F_d(c+ih)|-4-2\rho_d.             \tag{9}
\]

C048l(18)--(21) established, for the actual I and this same joint
limit,

\[
 \log|F_d(c+ih)|=-(\pi-1/2+o(1))D.                       \tag{10}
\]

This is a two-sided asymptotic, not its unweighted upper-bound
consequence. It uses the exact corner gamma cancellation and the
I-only limit at h=d/ell; no fixed-degree limit for B_d is substituted.

On the subarc, (3) is at least exp(pi*h/2+ell/4-1). Combining
(9),(10) and integrating its full length delta_d yields

\[
 A_d(i)\ge\frac1{2\pi\ell}
 \exp\{\pi h/2+\ell/4-(\pi-1/2+o(1))D-5-2\rho_d\}.
                                                               \tag{11}
\]

This lower bound retains the relative error and a nonzero integration
length at each d. Since D/h=1/ell, ell/h->0 and log(ell)/h->0,
it proves liminf log A_d(i)/h>=pi/2, and in particular eventual
divergence. A lower bound on one closing side suffices for this
nonnegative integral; no conjugation of the multiplier was made.

### Upper bound on all three closing sides

Every point of their union satisfies x>=c and y<=h. Therefore (3)
is at most d^(1/4)exp(pi*h/2) on the entire union, including the
bottom and the middle of the right edge. If A_d denotes C048l's
unweighted three-side integral, its proved A_d<=exp(-D) gives

\[
 A_d(i)\le d^{1/4}e^{\pi h/2}A_d
          \le\exp\{\pi h/2+\ell/4-D\}.                    \tag{12}
\]

Thus limsup log A_d(i)/h<=pi/2. Together with (11) this proves
(1). All eventual estimates have finitely many uniform onset
conditions, so one onset works for every integer d thereafter.
No effective value of that onset is asserted. Signed cancellation
in (2) remains entirely unestimated.

### Independent conceptual audit1683 — 19 November2026

This audit reuses assessment1681, separately approved1682, and the
inspected primary-source records1680/1660/1676. It checks the finite
specialization and both uniform estimates, not the underlying Rice
or Stirling theorems. The whole argument passes without correction.
This establishes an audited local input, not a stronger estimate or
a discovery beyond the sources already assessed.

**Finite identity and branch.** C048k supplies the unconditional
entire E, the samples E(k)=gamma_k/gamma_0 and the fixed positive
constant Z=gamma_0. For each d the multiplier is entire in s;
its base -i/d is nonzero and its chosen logarithm is fixed.
The rectangle contains exactly the integer kernel poles 0,...,d
and none on its boundary. Direct evaluation of the residue sum gives

    (-1)^d sum_(k=0)^d (-1)^(d-k) binom(d,k) E(k) (-i/d)^k
      = sum_(k=0)^d binom(d,k) (gamma_k/gamma_0) (i/d)^k
      = J_d(i/d)/gamma_0.

The factor d! already belongs to B_d, so no further factorial is
introduced. The positive contour traverses the left edge downwards.
The real part of (x+iy)(-ell-i*pi/2) is -ell*x+pi*y/2,
verifying (3), in particular its opposite height signs. Equation (2)
therefore retains the correct four sides and normalization.

**Actual uniform comparison.** Throughout the top edge the real
parts of p,z,q are at least 1/4,3/4,1/2 respectively, and their
moduli lie between h and 2d eventually. Thus C048l's full-argument
gamma remainders, actual-I comparison and sine identity all apply
on the same entire interval [c,b]. With epsilon_d as in (4) and
exp(-2pi*h)<1/2, they give the explicit sufficient bound

    rho_d <= 2 epsilon_d + 1/(2h) + 2 exp(-2pi*h) -> 0.       (A1)

Indeed the three gamma logarithmic errors are each at most 1/(6h).
The sine correction is log|1-exp(-2pi*h+2pi*i*x)| and has
modulus at most 2 exp(-2pi*h). Finally epsilon_d<1/2 implies
1-epsilon_d<=|I/S|<=1+epsilon_d and |log|I/S||<=2epsilon_d.
This last two-sided comparison makes I nonzero everywhere on the
edge. The other factors are also nonzero there, so all logarithms
of moduli used in (4) and (9) are defined. No pointwise-only error,
upper-envelope substitution or differentiated remainder is used.

**Explicit derivative and full subarc.** C048l's uniform Lambert
contract gives Re(w)>=1, 1<=|w|<=2ell and |arg(w)|<pi/2
eventually. For ell>=2 this implies

    |Log(w/2)| <= log(ell)+log(2)+pi/2.

The logarithmic derivative (7) retains every prefactor term;
|w'|<=1/h and |1+w|>=1 bound the three small terms by
13/(4h). For v=p,z,q, h>=1 makes log|v| nonnegative, and
|Log(v)|<=ell+log(2)+pi/2. Since H'(v)=Log(v)-1/(2v),
the triangle inequality in the exact derivative of G_d gives

    |G_d'(x)| <= 3ell+2log(ell)+7log(2)+5pi/2+19/(4h)
              <= 4ell                                      (A2)

for every x in [c,b] beyond one onset. The q derivative has sign
-1; (A2) bounds its absolute contribution and does not reverse
C048l's one-sided monotonicity estimate. Integrating (A2) over
0<=x-c<=1/ell gives G_d(x)>=G_d(c)-4. Applying (A1) at
both endpoints gives precisely (9), uniformly on that full subarc.
Its length is 1/ell, not zero, and it lies in [c,b].

**Corner input, integration and limits.** C048l(21) is the actual
two-sided corner limit in the joint degree/height scaling used here.
Its I-only asymptotic is independent of d before h=d/ell is
substituted, and its gamma quotient uses full moving arguments.
Thus it is applicable in (10). On the whole chosen subarc the
multiplier is at least exp(pi*h/2+ell/4-1). Integrating (9)
with this bound, with the factor 1/(2pi) in A_d(i), yields (11).
After division by h that lower bound reads

    log A_d(i)/h >= pi/2-(pi-1/2+o(1))/ell
       +[ell/4-log(ell)-log(2pi)-5-2rho_d]/h.                (A3)

The bracket divided by h tends to zero. The lower limit is
therefore at least pi/2; it is not inferred from a corner value
without controlling an integration interval.

On all three closing sides, including the bottom and the right
midpoint, x>=c and y<=h. Equation (3) hence bounds the multiplier
by exp(ell/4+pi*h/2). C048l's complete unweighted integral has
exactly the same 1/(2pi) normalization, so (12) gives

    log A_d(i)/h <= pi/2+ell/(4h)-1/ell.                    (A4)

Here D/h=1/ell, ell/h=ell^2/d->0 and log(ell)/h->0.
Equations (A3)--(A4) prove the claimed limit. The integral is finite
for each d, since the compact boundary has no pole, and is positive
eventually by (11). Choosing a limiting error less than pi/6 yields
A_d(i)>=exp(pi*h/3) eventually, which diverges as h->infinity.

There are only finitely many onset requirements: the C048l domains,
epsilon_d<1/2, the sine bound, h>=1, ell>=2, (A2), subarc inclusion,
the corner asymptotic and the unweighted closing estimate. Each
holds for every sufficiently large d with constants independent of
x; their maximum is a common onset. No effective degree is claimed.
The direct mathematical inputs remain exactly C048k and C048l;
their further inputs are used through those established contracts.
No DAG edge changes. Signed cancellation, nonvanishing of U_d(i),
other arguments or contours, compact mass and Xi transfer remain
unproved. The audit confirms only this rectangle's absolute-budget
stop and does not turn it into a disproof of RH.

## Mathlib

Full matching coverage of this degree-dependent actual theta-Mellin
weighted closing obstruction has not been checked. No theorem
absence is asserted. The finite Rice, principal-power and gamma
inputs are cited above; supporting formal-library availability is
not claimed to formalize (1).
