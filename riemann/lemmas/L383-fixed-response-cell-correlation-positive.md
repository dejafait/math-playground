# Lemma 383: positive leading correlation for the fixed response-cell test

## Hypotheses

Use the fixed actual pair F_0,G,A from L366, the normalized real
Wronskian Wcal from L380, and the full increasing response phase Phi
from L372, with G=D cos Phi and D>0. All derivatives are ordinary real
height derivatives. Let ell=log H, h=pi/ell, and let g_j be the eventual
consecutive positive zeros of G. H tends to infinity on that eventual
ray. There is no RH, simplicity assumption on F_0, noncoincidence,
discriminant sign, fourth-moment or common-zero-count assumption.

Use exactly the pi-periodic smooth cutoff in the approved assessment:
for x in [-pi/2,pi/2), set y=8(x+pi/4)/pi and

    chi(x)=exp(1-1/(1-y^2)) if |y|<1, and chi(x)=0 otherwise.

In particular 0<=chi<=1, its support is [-3pi/8,-pi/8] modulo pi,
and it is positive in the interior of this interval. Define

\[
 C_H=\frac1H\sum_{[g_j,g_{j+1}]\subset[H,2H]}
 \int_{g_j}^{g_{j+1}}1_{\{t+h<g_{j+1}\}}
       \chi(\Phi(t))\mathcal W(t)\mathcal W(t+h)\,dt.
 \tag{1}
\]

## Conclusion

Put

\[
 S=\frac{\zeta(5)\zeta(3)^2}{\zeta(6)},\qquad
 \kappa_0=\frac1\pi\int_{-\pi/2}^{\pi/2}\chi(x)\,dx>0,
 \quad
 \kappa_s=\frac1\pi\int_{-\pi/2}^{\pi/2}
                   \chi(x)\sin x\cos x\,dx.
\]

Then

\[
 \frac{C_H}{\log H}\longrightarrow
 c_\chi=\frac{S}{16\pi^2}
       \left(\frac{\kappa_0}{\pi^2}
                         +\frac{4\kappa_s}{\pi^3}\right)
 \ \ge\ \frac{S\kappa_0(\pi-2)}{16\pi^5}>0.       \tag{2}
\]

Thus this fixed diagnostic is eventually positive and fails its sought
negative liminf. It does not show absence of opposite signs inside a
response cell: a positive averaged product cannot do that. Neither
global actual-theta positivity nor the total L367 margin, common-zero
counts, an RH sign or zero-exclusion range is changed. The separate
critical audit below validates this specialization without changing its
coefficient or strengthening its localization conclusion.

## Proof

This is a REPRODUCTION under the pre-existing EXPLORE assessment
`drafts/literature/2026-10-08-wronskian-cell-correlation-test.md`.
It specializes known small-complex-shift moments, using L381's audited
proof and bounds; no novelty beyond the sources checked is asserted.
The new applicability work is the full response-phase localization and
harmonic treatment. In particular no fast phase is used as a Young
weight, and no projection term is discarded.

### 1. Exact localization and normalization

Use L380's notation U=zeta(1/2+it), Z=zeta(5/2+it),
Q=A exp(i phi), b=(t^2/4-3/16-it/2)/pi, T=1+t, L=log(2+t).
Then r=exp(i phi)U is real, F_0=-Ar, and
G=A|bZ|cos Phi. The phase can be chosen so that
Phi=phi+arg b+Im mathscr L(5/2+it), with L372's continuous Euler
logarithm. Constant branch changes have no effect on this cutoff.
Write v=r'/ell and a=(log|bZ|)'. Direct differentiation gives

\[
 \mathcal W=\frac{|bZ|}{T^2L}
       \{-r'\cos\Phi-r\Phi'\sin\Phi+a r\cos\Phi\}.       \tag{3}
\]

The sign here uses L380's convention F_0'G-F_0G'. L368's complete
right-line bounds and lower bound for |Z| imply a=O(1). Uniformly
on [H-1,2H+1], L368 and L372 give

\[
 \Phi'=\ell/2+O(1),\quad
 \Phi(t+h)-\Phi(t)=\pi/2+O(\ell^{-1}),\quad
 |b|/T^2=1/(4\pi)+O(H^{-1}),\quad L=\ell+O(1).       \tag{4}
\]

The error in the phase increment comes from integration of the bounded
Euler-phase derivative, not an assumption that this derivative vanishes.
For large H make that error less than pi/16. A supported phase has
representative x in [-3pi/8,-pi/8] within its cell (-pi/2,pi/2).
Its shifted phase lies in [pi/16,7pi/16] in the same cell. Since Phi
is increasing, the same-cell indicator in (1) is exactly one wherever
chi is nonzero. This is an exact eventual statement, not a replacement
of the response grid by a Gram grid.

Each cell meeting either endpoint H or 2H has length O(1/ell), because
Phi'>=ell/3 on [H-1,2H+1] eventually and consecutive zeros differ in
phase by pi. The existence of their endpoints within this enlarged
interval follows from the same lower derivative bound. Excluding those
at most two incomplete cells costs, by L382's global envelope,
O(H^(-1/4)/ell) in the normalized product integral. The bound also holds
at t+h, by applying that envelope on the adjacent dyadic interval if
necessary. Thus

\[
 C_H=H^{-1}\int_H^{2H}\chi(\Phi(t))
           \mathcal W(t)\mathcal W(t+h)\,dt+o(1).       \tag{5}
\]

We will use the jet norm bounds

\[
 H^{-1}\int_H^{2H}(|r(t+u)|^2+|r'(t+u)/\ell|^2)dt
                   =O(\ell),\qquad u=0,h.             \tag{6}
\]

These follow from L381 (9), r'=exp(i phi)(U'+i omega U),
omega=ell/2+O(1), and a fixed smooth majorant on a slightly enlarged
dyadic interval. The same bounds for small complex offsets used below
follow from Young's shift theorem and Cauchy, as detailed in section 2.
L368 gives |Z(t+h)-Z(t)|<=M_1 h. Equations (3),(4),(6) therefore give
in the normalized L2 norm on [H,2H]

\[
 \mathcal W(t)=-\frac{|Z(t)|}{4\pi}
      \{v(t)\cos\Phi(t)+\tfrac12 r(t)\sin\Phi(t)\}
                      +O_{L^2}(\ell^{-1/2}),
\]
\[
 \mathcal W(t+h)=-\frac{|Z(t)|}{4\pi}
      \{-v(t+h)\sin\Phi(t)+\tfrac12 r(t+h)\cos\Phi(t)\}
                      +O_{L^2}(\ell^{-1/2}).          \tag{7}
\]

For example the a r term in (3) has norm O(ell^(-1/2)); every coefficient
replacement in (4) has error O(ell^(-1)), multiplying a jet of norm
O(sqrt ell). Both leading terms have norm O(sqrt ell), so the product
error in (5) is O(1) by Cauchy--Schwarz. This treats both heights and
every term of the real projection.

### 2. The zero phase harmonic, including shifted jets and tails

Let f(z)=sin(z)/z, with its entire value at zero. For a,b in {0,1},
define r_0=r and r_1=r'/ell. We claim

\[
 \frac1{H\ell}\int_H^{2H}|Z(t)|^2 r_a(t)r_b(t+h)dt
                       \longrightarrow S K_{ab},     \tag{8}
\]
where

\[
 K_{00}=2/\pi,\quad K_{10}=2/\pi^2,\quad
 K_{01}=-2/\pi^2,\quad K_{11}=1/(2\pi)-4/\pi^3.     \tag{9}
\]

Here is the required complex-shift justification. Import M. P. Young,
*A short proof of Levinson's theorem*, Arch. Math. 95 (2010), 539--548,
DOI 10.1007/s00013-010-0199-9,
[Lemmas 4--5, (2.1)--(2.3), (4.1)--(4.5), and the Cauchy argument
after (3.4), pp. 540--543](https://www.math.ntnu.no/emner/MA3001/2020v/2022v_MA3004/Young.pdf).
Use the already justified two-diagonal evaluation in L381 section 2.
The scale is 2H; each fixed rational twist m/n satisfies its size
condition eventually. Weights w are nonnegative fixed smooth shapes,
supported in [H/2,3H] with w^(j)=O_j(H^(-j)), within the cited derivative
and support conditions. Only complex shifts of bounded size/ell occur.

For fixed m,n that evaluation, with shifts alpha=i u, beta=-i v,
has leading term

\[
 \frac{\gcd(m,n)}{\sqrt{mn}}\int w(t)
             \int_0^{\log(t/(2\pi))}e^{-i(u-v)y}\,dy\,dt,
                                                               \tag{10}
\]
with error O_{m,n,w}(H) on the product contours
|u|=1/ell and |v-h|=(pi+3)/ell. On them
2/ell<=|u-v|<=(2pi+4)/ell. Thus the same fixed Mellin shift -1/8,
pole cancellation and Gaussian-tail bounds in L381 apply: the auxiliary
factor is O(ell^2(1+|z|^2)), the two retained residues give (10), and
their other factors differ from one by O_{m,n}(1/ell). Increasing the
fixed upper bound for the small shifts changes constants only. The
error O(H^(1-1/8)ell^2) is still o(H). No singular summand is
differentiated separately.

Let R(t)=exp(i phi(t)) and use its nonzero holomorphic extension near
this interval. The reflection identity gives, holomorphically in u,v,

    r(t+u)r(t+v) = R(t+u)/R(t+v)
                   zeta(1/2+i(t+u)) zeta(1/2-i(t+v)).

The exact gamma derivative gives
R(t+u)/R(t+v)=exp(i ell(u-v)/2)(1+O(1/ell)) uniformly on these
contours and the support of w. This follows by integrating
R'/R=i omega, with omega=ell/2+O(1) also at the small complex offsets.
The integral of the absolute value of the zeta pair is O_w(H ell),
by Cauchy--Schwarz and Young with twist one and conjugate shifts.
Hence this carrier replacement costs O_w(H), even with the rational
twist of modulus one. Replacing the endpoint log(t/(2pi)) in (10)
by ell also costs O_w(H). We obtain the holomorphic approximation

\[
 \int w(t)(m/n)^{-it} r(t+u)r(t+v)dt
 =\frac{\gcd(m,n)}{\sqrt{mn}}\left(\int w\right)
       \ell f(\ell(v-u)/2)+O_{m,n,w}(H).             \tag{11}
\]

Both the left side and the displayed main term are holomorphic on the
full product disks. The two-variable Cauchy formula on the specified
contours bounds the error after a u derivatives and b v derivatives
at u=0,v=h by O(H ell^(a+b)). Thus normalized jet errors are O(H).
This is why differentiating a real-shift asymptotic is unnecessary.
Differentiating the entire f gives
K_00=f(pi/2), K_10=-f'(pi/2)/2, K_01=f'(pi/2)/2,
K_11=-f''(pi/2)/4, exactly (9).

Expand the fixed head |Z_N|^2, Z_N=sum_(n<=N)n^(-5/2-it), in (11).
Every ordered pair contributes; the coefficient is
S_N=sum_(m,n<=N)gcd(m,n)/(m^3 n^3), as in L381 (10).
This proves the smoothly weighted version of (8) with S_N.

For sharp endpoints choose fixed smooth brackets with transition
width epsilon H. Although the cross product is signed, its absolute
integral over the two transition regions is bounded by Cauchy--Schwarz
and the two individual jet-square integrals there. A smooth majorant
of those regions has integral O(epsilon H). The twist-one version of
(11), evaluated with coincident real offsets 0 or h and differentiated
as above, bounds each normalized jet-square integral by
O(epsilon H ell)+O_epsilon(H). Such a coincident evaluation uses the
same holomorphic formula, with unequal-radius contours centered at the
chosen offsets and avoiding u=v on their boundaries. On the real line
the jets are real, so these are indeed nonnegative squares. Bounded
|Z_N| does not enlarge the order. Let H tend to infinity and then
epsilon tend to zero. The sharp version follows at every fixed N.

Finally rho_0(N)=sum_(n>N)n^(-5/2) tends to zero, and
sup||Z|^2-|Z_N|^2|<=2 M_0 rho_0(N). Equation (6) bounds the difference
in (8) by O(rho_0(N)), uniformly for large H. Let N tend to infinity
after the height limit. L381's absolutely convergent gcd grouping gives
S_N->S. These estimates prove (8), retaining the entire right-line
tail, all rational collisions and both functional-equation diagonals.

### 3. Every nonzero fixed phase harmonic

For each fixed nonzero integer k and a,b in {0,1}, we prove

\[
 \frac1H\int_H^{2H}|Z(t)|^2 e^{2ik\Phi(t)}
                     r_a(t)r_b(t+h)dt=O_k(1).       \tag{12}
\]

Use a complex height tau with real part in [H,2H+h]. Define

\[
 E(\tau)=\pi^{-i\tau}
       \frac{\Gamma(1/4+i\tau/2)}{\Gamma(1/4-i\tau/2)},\quad
 Z_\pm(\tau)=\zeta(5/2\pm i\tau),\quad
 K(\tau)=\frac{b(\tau)Z_+(\tau)}{b^\sharp(\tau)Z_-(\tau)},
                                                               \tag{13}
\]
where b^sharp has the conjugate polynomial coefficients of b.
On the real axis E=exp(2i phi), K=exp(2i(Phi-phi)), and
|Z|^2=Z_+Z_-. On a neighborhood of |Im tau|<=1, these functions
are holomorphic, E,K are nonzero, and K,K^(-1),Z_+,Z_- are uniformly
bounded. Indeed the zeta lines have real part at least 3/2 there;
their reciprocal Euler series are bounded as well. The polynomial
zeros and gamma poles have real height zero, outside these rectangles.
Choose a holomorphic square root R of E agreeing with exp(i phi) on
the real interval. The exact reflection identity continues to give

\[
 r(\tau)=R(\tau)U_+(\tau)=R(\tau)^{-1}U_-(\tau),
 \qquad U_\pm(\tau)=\zeta(1/2\pm i\tau).           \tag{14}
\]

The roots and logarithms exist on this simply connected zero-free
rectangle; (14) follows by the identity theorem from the real line.
The derivative formulas are

    r'/ell = R(U_+'+i Omega U_+)/ell
            = R^(-1)(U_-'-i Omega U_-)/ell,

where Omega is the paired digamma extension in L381 (17), and
Omega=O(ell) on the rectangle. Sector-qualified Stirling, the same
scalar input used in L381's contour estimate, gives uniformly

\[
 |E(x+iy)|\asymp (x/(2\pi))^{-y}\quad(|y|\le1),
 \qquad |R(\tau+h)/R(\tau)|+|R(\tau)/R(\tau+h)|=O(1).
                                                               \tag{15}
\]
The first estimate follows by dividing the two gamma modulus formulas
and retaining pi^y; the second follows by integrating i Omega over
a segment of length h. Their constants are independent of H.

For k<=-1 use both positive-height expressions in (14) and move the
height contour down to Im tau=-1. The product of the carrier factors
is E(tau)^(k+1)R(tau+h)/R(tau). On the topological lower edge,
both U_+ arguments have real part 3/2, so their values and derivatives
are absolutely bounded. Equations (15) give
|E(x-iy)^(k+1)|<=C_k for 0<=y<=1. The factors K^k and Z_+Z_-
are bounded, so the whole shifted horizontal integral is O_k(H).

For k>=1 use both negative-height expressions in (14) and move up to
Im tau=1. The product carrier is now
E(tau)^(k-1)R(tau)/R(tau+h); its modulus is bounded in the upper
rectangle. Both U_- factors on the shifted edge have real part 3/2,
and the same O_k(H) horizontal estimate holds. In particular k=-1
and k=1 are retained: their carrier exponent is zero, and their
horizontal integrals are bounded by O(H), not declared oscillatory.

On either vertical connector let y be the distance from the real axis.
The selected critical zeta factors then have real part 1/2+y.
L381 (18)--(19), with derivative circles of radius 1/ell, gives

    |U_selected|+|U_selected'|/ell <= C H^(1/2-y/2).

This applies also at the height displaced by h. Its proof uses the
fixed positive strip and the absolute series when a circle extends
past 3/2; all heights remain comparable to H. The bounded Omega/ell
and the carrier powers just checked therefore bound the full vertical
integrand by C_k H^(1-y). Each vertical integral is O_k(H/ell).
No pole of any factor lies in either rectangle. Cauchy's integral
theorem thus proves (12), with all edges and the full Euler factors
retained. This is a height-contour argument, not an application of
Young with the fast weight exp(2ik Phi).

For any continuous pi-periodic q, the standard Fejer uniform-approximation
theorem,
(6),(8),(12) now imply

\[
 \frac1{H\ell}\int_H^{2H}|Z|^2 q(\Phi(t))
                       r_a(t)r_b(t+h)dt
       \longrightarrow S K_{ab}\,\overline q,
 \qquad \overline q=\pi^{-1}\int_{-\pi/2}^{\pi/2}q(x)dx. 
                                                               \tag{16}
\]

Precisely, a uniform approximation error delta contributes O(delta)
to this normalized integral by (6) and Cauchy--Schwarz. Take the height
limit at each fixed finite trigonometric polynomial, using (12) for
each nonzero mode, and then let delta decrease to zero. No uniformity
in k of the contour constants is needed, and no cutoff harmonic is
silently omitted. For the smooth functions below their ordinary
Fourier partial sums also converge uniformly, by two integrations by
parts and absolute summability of their Fourier coefficients.

### 4. Signed assembly and the diagnostic's limitation

Multiply the two leading terms in (7), writing x=Phi(t) and a subscript
h for evaluation at t+h. The complete product is

\[
 \frac{|Z|^2}{16\pi^2}
 \{-\sin x\cos x\,v v_h
   +\tfrac12\cos^2 x\,v r_h
   -\tfrac12\sin^2 x\,r v_h
   +\tfrac14\sin x\cos x\,r r_h\}.                \tag{17}
\]

Apply (16) separately with q equal to chi times each displayed phase
factor. The middle two terms give kappa_0/pi^2 by (9). The first
and last together give

    kappa_s[-(1/(2pi)-4/pi^3)+(1/4)(2/pi)]
                   = 4 kappa_s/pi^3.

Equations (5),(7) have errors o(ell), so (17) proves the limit (2).
Since sin x cos x>=-1/2, kappa_s>=-kappa_0/2. This proves the strict
lower bound in (2), without evaluating a bump integral numerically.

As a normalization check on the same jet calculation, the coincident
values of (11) give normalized r-square coefficient S and v-square
coefficient S/12, with mixed coefficient zero. The phase averages of
cos^2 and sin^2 are both 1/2. Squaring the first expression in (7)
therefore recovers S(1/24+1/8)/(16pi^2)=S/(96pi^2), precisely L381's
unweighted second-moment coefficient. This checks the factors of two
without substituting that same-height theorem for the present proof.

For completeness the intended negative diagnostic would have the
claimed localization consequence: if (1) were negative, one retained
cell would contain a t with chi(Phi(t))>0 and Wcal(t)Wcal(t+h)<0.
Both points are strictly inside that same open cell. Continuity then
gives positive integrals of each signed part there, so the J_H in the
assessment is positive. It also gives an intervening Wronskian zero
with G nonzero, hence not a common F_0,G zero. No multiplicity premise
is needed. But (2) makes this particular C_H positive for every
sufficiently large H, so it supplies none of these witnesses. Other
within-cell diagnostics and actual common-zero counts are undecided.
This completes the single fixed test. ∎

### Separate critical audit, 2026-10-08

This audit uses the pre-existing SPECIALIZE assessment
`drafts/literature/2026-10-08-wronskian-cell-correlation-audit.md`.
The exact shift, cutoff and statistic (1) are unchanged. The prior
primary-source assessment and L381's audited Young specialization are
reused; no stronger moment theorem is presumed. The conclusion survives
without a mathematical repair. These are independent checks of the
specialization, not a new correlation theorem beyond the checked sources.

**Exact phase and localization.** With d=|bZ|, L366 and L368 give
F_0=-Ar and G=Ad cos Phi. Expanding the two derivatives and canceling
A' gives A^(-2)(F_0'G-F_0G')=d[-r' cos Phi+r(d'/d)cos Phi
-r Phi' sin Phi]. Thus all three signs in (3) agree with L380,
including at zeros of either real function. Here d'/d is bounded
because b'/b=O(1/H), Z' is bounded and |Z| has a uniform positive
lower bound. No division by F_0 or G occurs.

The exact carrier has positive real polynomial p=t^2+1/4. Hence
Q/bar Q is precisely E in (13); p introduces no phase. L372's full
Euler phase, not just the gamma phase, gives Phi'=ell/2+O(1) on the
enlarged dyadic interval. Integration over h gives the stated phase
error O(1/ell). Adding pi/2 and an error bounded by pi/16 to the
supported interval [-3pi/8,-pi/8] gives [pi/16,7pi/16], strictly
inside the same cell. This verifies the indicator removal with a
fixed buffer at both ends. Phi'>=ell/3 gives cell length at most
3pi/ell. The two incomplete cells therefore contribute at most
C H^(-1) ell^(-1) H^(3/4)=C H^(-1/4)/ell by L382's envelope,
also at the shifted height. This is o(1).

Both real Hardy jets have squared mean O(ell), using L381 (9)
and r'=R(U'+i omega U). The coefficient errors from L/ell,
Phi'/ell, the phase shift and Z(t+h)-Z(t) are all O(1/ell).
The omitted amplitude-derivative term also has coefficient O(1/ell).
Each thus costs O(ell^(-1/2)) in normalized L2. Multiplying by
a leading term of norm O(sqrt(ell)) costs O(1); the product of the
two errors is O(1/ell). This checks both projections in (7), without
requiring a pointwise Hardy bound for the bulk integral.

**Complex offsets and all four signs.** Young's weight conditions
are met at scale 2H: support [H/2,3H] is contained in [H/2,4H],
and O_j(H^(-j)) is stronger than the required logarithmically
weaker derivative bound. Weights can be taken in [0,1]; a fixed
bounded nonnegative shape is first divided by its supremum and the
formula then multiplied by that constant. Each twist is fixed before
H grows, so its size restriction holds eventually. The contours have
|u-v|>=((pi+3)-pi-1)/ell=2/ell and
|u-v|<=(2pi+4)/ell. Both complex shifts are bounded constants/ell,
and their real parts are eventually below the source's fixed bound.

The two diagonal residues, with alpha=iu and beta=-iv, have combined
leading term (gcd(m,n)/sqrt(mn))(1-x^(-i(u-v)))/(i(u-v)),
x=t/(2pi). All fixed-base factors change this by O_(m,n)(1):
their deviations are O(1/ell), multiplying poles of size O(ell).
L381's audited Mellin move remains valid for these larger fixed
offset constants. The gamma poles remain to the left of -1/8,
the auxiliary polynomial costs O(ell^2(1+|z|^2)), and the far
Mellin tail has its Gaussian domination even near imaginary height
plus or minus t. The integrated remainder is O(H^(7/8)ell^2)=o(H).
The two source diagonals and both off-diagonal orderings are retained.

For clarity, the absolute pair bound used to replace the carrier
also holds at complex offsets. For each |u|<=C/ell,
|zeta(1/2+i(t+u))|^2 is the twist-one shifted product with shifts
iu and -i conjugate(u). Apply the same holomorphic two-diagonal
formula on enclosing unequal-radius shift circles, then the maximum
modulus principle, to bound its weighted integral by O(H ell),
uniformly in this disk. The combined residue has its removable
singularity filled in when the shift sum vanishes. Cauchy--Schwarz
therefore bounds the absolute product at u,v by O(H ell).
The holomorphic carrier ratio is exp(i ell(u-v)/2)(1+O(1/ell)):
integrate R'/R=i Omega along the offset segment, on which
Omega=ell/2+O(1). Its replacement consequently costs O(H).
The varying endpoint log x differs from ell by O(1), also costing
O(H). The resulting elementary integral is
exp(i ell(u-v)/2) integral_0^ell exp(-i(u-v)y)dy
=ell f(ell(v-u)/2), with the entire value used at u=v.

The actual integral and this main term are holomorphic on the full
product disks, even where u=v; only their boundary estimate used
separation. Cauchy's formula for a,b in {0,1} gives error
O(H ell^(a+b)), hence O(H) after the jet normalization.
At z=pi/2, direct differentiation gives
f=2/pi, f'=-4/pi^2 and f''=-2/pi+16/pi^3. Since a derivative
at the first height contributes -ell/2 and one at the second
contributes +ell/2, the four constants are exactly (9).
In particular the mixed one-derivative constants have opposite signs;
reflecting the second height does not replace either by its negative.

**The two harmonic rectangles.** The functions E and K are nonzero
and holomorphic on a slightly enlarged rectangle: the gamma and
polynomial zeros/poles lie at real height zero, and the right-line
zeta arguments stay strictly to the right of 1. Their reciprocals
are bounded by the absolutely convergent Euler series. A holomorphic
square root R exists and agrees with the real carrier after one sign
choice. Critical-line reflection then proves (14) throughout the
rectangle by the identity theorem, without dividing by a critical
zeta value. The differentiated identities use Omega at each respective
height, both bounded by C ell.

Sector-qualified Stirling gives |E(x+iy)| comparable to
(x/(2pi))^(-y): the gamma numerator and denominator have real parts
1/4-y/2 and 1/4+y/2, so their polynomial ratio is (x/2)^(-y),
and pi^(-i(x+iy)) supplies pi^y. Their exponential factors cancel.
The ratio R(tau+h)/R(tau) and its inverse are bounded by integrating
R'/R over length h=pi/ell. For k<=-1 the selected product has
carrier E^(k+1)R(tau+h)/R(tau). On tau=x-iy, 0<=y<=1,
its modulus is O_k(H^(y(k+1)))=O_k(1). Both U_+ factors on the
lower horizontal edge are on real part 3/2. For k>=1 the reflected
product has carrier E^(k-1)R(tau)/R(tau+h), bounded by
O_k(H^(-y(k-1))) on tau=x+iy; both U_- factors on the upper
edge are on real part 3/2. Values and ordinary derivatives there
are absolutely bounded, and division by ell controls the Omega terms.
Each horizontal integral is therefore O_k(H). In particular the
carrier-canceling cases k=-1 and k=1 satisfy this estimate directly;
neither is claimed to decay by oscillation.

On a vertical connector, the selected zeta real part is 1/2+y
in either direction. Applying L381 (18) on radius 1/ell derivative
disks gives |U_selected|+|U_selected'|/ell<=C H^(1/2-y/2),
also at tau+h. The disk's factor H^(1/(2ell)) is bounded, and
any part beyond real part 3/2 uses the absolute series. The full
product is bounded by C_k H^(1-y); its integral is at most
C_k(H-1)/ell. All right-line factors and their reciprocals are
included here. No rectangle contains a pole, so the entire harmonic
integral is O_k(H), giving O_k(1) after division by H and o(1)
after division by H ell. No fast phase has entered Young's weight.

**Sharp endpoints, collisions and limit order.** For a fixed head,
the absolute signed endpoint error is bounded by Cauchy--Schwarz
using the two individual normalized real jet squares. The coincident
version of the holomorphic formula gives their leading constants
1 and 1/12, times ell integral(w), with error O_w(H).
Use unequal-radius circles centered at the coincident offset to
justify both derivatives before setting the offsets equal. A smooth
majorant for the endpoint strips has integral O(epsilon H), so the
normalized product error is O(epsilon)+O_epsilon(1/ell).
First take H to infinity, then epsilon to zero; no positivity of
the original cross product or complex twist is used in bracketing.

Every ordered head pair contributes gcd(m,n)/(m^3 n^3).
Writing m=da,n=db with (a,b)=1 gives total
zeta(5) times sum_(a,b coprime) a^(-3)b^(-3).
The latter is zeta(3)^2/zeta(6), by factoring out the common
divisor in the absolutely convergent unrestricted double sum.
The omitted full right-line tail changes any normalized jet product
by O(rho_0(N)), using (6), uniformly in H. Thus N can tend to
infinity after the sharp height limit, preserving S and every collision.
For the subsequent phase approximation, uniform error delta costs
O(delta) in the normalized integral. H tends to infinity for each
fixed trigonometric polynomial before delta tends to zero. There is
no interchange requiring a bound uniform in the harmonic index.

**Signed coefficient and scope.** Multiplication of (7) gives all four
terms of (17). The two middle terms combine to kappa_0/pi^2;
the first and last give 4 kappa_s/pi^3. Since chi is nonnegative
and nonzero, kappa_0>0 and kappa_s>=-kappa_0/2. The final coefficient
is therefore at least S kappa_0(pi-2)/(16 pi^5)>0. The bulk
projection errors are O(1), each fixed nonzero harmonic is O(1),
and the endpoint cost is o(1); the sequential head, smoothing and
Fourier errors vanish after division by ell. Every required error
is consequently o(ell). The coincident-jet check recovers L381's
S/(96 pi^2), independently confirming the real-projection factor.

The restricted negative-correlation diagnostic remains stopped.
This audit gives no new coefficient, repair, sign range or RH input;
in particular a positive average still permits opposite Wronskian
signs inside individual cells. Matching Mathlib coverage is not checked.

## Mathlib

Full matching coverage of this cell-restricted two-height Wronskian
correlation is **not checked**. Young's shifted moment and the local
gamma, Euler-series and contour estimates are the stated analytic
inputs. Supporting differentiation, Cauchy--Schwarz or Fourier facts
alone would not establish the family-specific asymptotic. Unknown
formal coverage is not evidence of absence or mathematical novelty.
