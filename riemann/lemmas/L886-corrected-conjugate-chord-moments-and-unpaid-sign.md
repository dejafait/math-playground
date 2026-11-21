# Lemma 886: corrected conjugate chords reduce the sign test to unpaid real moments

## Hypotheses

Retain L847's actual entire function and positive real coefficients,

\[
 G(z)=\tfrac18\xi(\tfrac12+\tfrac{\sqrt z}{2})
       =\sum_{n\geq0}a_nz^n,\qquad a_n>0.
\]

Assume the matched conjugate branch of L882 under L879's stationarity
hypotheses, as specified in L884. Thus the graph is smooth, real and
periodic, J=det(I-iDu) is nowhere zero, and real radial variations
supported compactly in the nonzero-density set have zero first
variation. The four fixed fibers have the same two simple conjugate
G-zero labels. Their complementary radial Jordan interiors have no
G zeros and their boundaries have exactly those two simple G zeros.
Retain all other zeros, multiplicities and simultaneous contacts.
Neither a nonreal zero nor such a graph is asserted to exist.

Let sigma=x+iy=rho*exp(i*theta) be the upper label, with y>0,
rho>0 and 0<theta<pi. Use L883's full single-valued primitives H_j,
including their negative powers. Put

\[
 r=(a_0,a_1,a_2),\quad t=2\pi r,\quad
 S(b,c)=b_0c_2-2b_1c_1+b_2c_0,\quad q(b)=S(b,b),
\]
\[
 \ell=2\pi-2\theta,\qquad
 v=\ell r-2\operatorname{Im}H(\sigma),\quad w=t-v,
 \quad(\alpha,\beta,\gamma)=(q(v),S(v,w),q(w)).       \tag{1}
\]

These are the actual fixed-lift vectors. Naming the lower label first
exchanges v,w and alpha,gamma, leaving beta and the requested
disjunction unchanged. No convexity, chord inclusion, zero-free disk,
sector bound, nonzero d=a1^2-a0*a2, or uniform label bound is assumed.

## Conclusion

For x!=0 define the real chord vector

\[
 c_j=2\int_0^y\operatorname{Re}
             \frac{G(x+is)}{(x+is)^{j+1}}\,ds,
       \qquad j=0,1,2.
\]

The exact winding correction is

\[
 v=\mathbf1_{x>0}t-c,\qquad
 w=\mathbf1_{x<0}t+c.                                  \tag{2}
\]

In particular, with u=sgn(x)c, the unordered pair {v,w} is
{u,t-u}. Write

\[
 B(s)=\frac{G(x+is)}{(x+is)^3},\quad
 U_0=2\int_0^y\operatorname{Re}B(s)\,ds,\quad
 U_2=2\int_0^y s^2\operatorname{Re}B(s)\,ds,\quad
 V_1=2\int_0^y s\operatorname{Im}B(s)\,ds.
\]

Then

\[
 c=(x^2U_0-U_2-2xV_1,\ xU_0-V_1,\ U_0),\qquad
 D=U_0U_2+V_1^2,
\]
\[
 p=S(u,t)=2\pi\operatorname{sgn}(x)
 \{(a_2x^2-2a_1x+a_0)U_0-a_2U_2
                         +2(a_1-a_2x)V_1\},\qquad
 Q_0=q(t)=-8\pi^2d.                                    \tag{3}
\]

The three full bilinear quantities, ordered as u,t-u, are

\[
 q(u)=-2D,\qquad S(u,t-u)=p+2D,\qquad
 q(t-u)=Q_0-2p-2D.                                     \tag{4}
\]

Thus a branch exclusion by L884 requires at least one of the exact
signed conditions

\[
 (-2D)(p+2D)\geq0,\qquad
 (Q_0-2p-2D)(p+2D)\geq0.                               \tag{5}
\]

The quantities p and Q_0 retain the residue cross terms and residue
square. They cannot be omitted from this test.

The through-zero case x=0 is retained by a finite left detour. Define
the entire functions

\[
 e_j(z)=\frac{G(z)-\sum_{n=0}^j a_nz^n}{z^{j+1}},
 \qquad e_j(0)=a_{j+1}.
\]

For sigma=iy the complete vector, including the detour, is

\[
 v_j=\pi a_j-b_j-2\int_0^y\operatorname{Re}e_j(is)\,ds,
 \qquad (b_0,b_1,b_2)=(0,2a_0/y,2a_1/y),\quad w=t-v.
                                                               \tag{6}
\]

No principal value, discarded negative power or shrinking-detour
estimate is used. Formula (6) holds for every detour radius between
zero and y after the pieces have been combined exactly.

There is also a full-product sufficient certificate using the actual
coefficients, valid for all x including zero. For an integer N>=2
and any rho_*>rho, set

\[
 v_j^{(N)}=\ell a_j-2\operatorname{Im}
       \sum_{\substack{0\leq n\leq N\\n\ne j}}
                  \frac{a_n\sigma^{n-j}}{n-j},
 \qquad w^{(N)}=t-v^{(N)},
\]
\[
 E_j=\frac{2\rho^{-j}G(\rho_*)}{N+1-j}
                \left(\frac{\rho}{\rho_*}\right)^{N+1},
 \qquad E=\max_{0\leq j\leq2}E_j.                       \tag{7}
\]

Then |v_j-v_j^(N)|<=E_j. Define alpha_N,beta_N,gamma_N using the
same S-products of v^(N),w^(N), and put

\[
 E_\alpha=8\|v^{(N)}\|_\infty E+4E^2,\quad
 E_\beta=4\|t-2v^{(N)}\|_\infty E+4E^2,\quad
 E_\gamma=8\|w^{(N)}\|_\infty E+4E^2.
\]

For h=alpha or gamma, the corresponding exact product is
nonnegative if

\[
 h_N\beta_N\ \geq\ |h_N|E_\beta+|\beta_N|E_h+E_hE_\beta.
                                                               \tag{8}
\]

No actual conditional label has been shown to satisfy (5) or (8).
No uniform signed estimate of U_0,U_2,V_1, or of the finite-product
margin in (8), is proved. In particular this is an exact reduction
and a sufficient error test, not a nonnegative product, branch
exclusion, stationary graph, or advance toward RH beyond the checked
source results. The bounded chord attempt ends as EXPLORATION.
This lemma has not received an independent conceptual audit.

## Proof

### Coverage and imported input

The invocation-start EXPLORE assessment
`drafts/literature/2026-11-07-conjugate-signed-chord-test.md`
covers exactly this corrected-chord test. L883 already supplies
the locally normal Laurent primitives and the tracked identity

\[
 \frac{G(z)}{z^{j+1}}\,dz=dH_j(z)+a_j\,dz/z.             \tag{9}
\]

Its standard source is Jiří Lebl, *Guide to Cultivating Complex
Analysis*, v1.10, 5 November 2026,
[Theorem 4.4.2/Proposition 4.4.3, pp104-108](https://www.jirka.org/ca/ca.pdf#page=104),
with [Theorem 4.3.3/Corollary 4.3.4, pp100-101](https://www.jirka.org/ca/ca.pdf#page=100)
for primitives and lifted integration. Proposition 4.4.3 is imported
as a stated standard result; its source proof is an exercise, not a
proof claimed to have been read. Reuse L883's checked specialization
instead of reproving these theorems. The work below is a contour and
bilinear specialization, classified REPRODUCTION, with no originality
claim. The reviewed quadrature and reverse-triangle results supply
no sign here and are not used as sign inputs.

### Chord orientation and the full residue correction

For x!=0 the straight chord is a compact path in C*; its distance
from zero is at least |x|. Real coefficients give conjugate values
at x+is and x-is. Orienting the chord from sigma to its conjugate,

\[
 \int_{\sigma}^{\overline\sigma}
                 \frac{G(z)}{z^{j+1}}\,dz=-i c_j.        \tag{10}
\]

If x>0 its continuous argument decreases from theta to -theta.
If x<0 its continuous argument increases from theta to 2pi-theta.
The modulus has the same value at both endpoints. Comparing these
increments with ell in (1), equation (9) gives A=-ic+it when x>0
and A=-ic when x<0. Since v=-iA, this proves (2), with both signs
checked. This argument compares explicit primitives in C*; it does
not deform a chord inside either zero-free radial domain. Other
G zeros are zeros of the differential, not extra poles.

For z=x+is, the three integrands in c are respectively the real
parts of z^2B, zB and B. Expanding z and z^2 gives the first formula
in (3). Directly,

\[
 \begin{split}
 c_0c_2-c_1^2
 &=(x^2U_0-U_2-2xV_1)U_0-(xU_0-V_1)^2\\
 &=-U_0U_2-V_1^2.
 \end{split}
\]

This proves q(u)=q(c)=-2D. Substitution in S(u,2pi*r) gives p in
(3), and q(2pi*r)=-8pi^2d. Bilinearity gives
S(u,t-u)=p-q(u) and q(t-u)=q(t)-2p+q(u), proving (4).
For x<0 the ordering is (v,w)=(u,t-u); for x>0 it is reversed.
Therefore (5) is exactly the requested disjunction in either order.
L884 supplies its consequence for the conditional stationary branch.
There has been no division by d, a product or a moment.

### Finite detour through the imaginary-axis case

Fix 0<epsilon<y. Use the path from iy down to i*epsilon, then the
left semicircle z=epsilon*exp(i*phi), pi/2<=phi<=3pi/2, then down
from -i*epsilon to -iy. It lies in C* and its argument increases
by exactly pi. Decompose the differential, with every polar term,

\[
 \frac{G(z)}{z^{j+1}}\,dz
 =\sum_{n=0}^{j-1}a_nz^{n-j-1}\,dz+a_j\,dz/z+e_j(z)\,dz.
                                                               \tag{11}
\]

The polar sum is zero for j=0; for j=1 it is a0*z^-2; for j=2
it is a0*z^-3+a1*z^-2. Its single-valued primitive is respectively
0, -a0/z, or -a0/(2z^2)-a1/z. Its endpoint increment on the whole
finite path is therefore 0, -2i*a0/y, or -2i*a1/y.
For explicit cancellation, a term b*z^-2 integrates over the two
vertical pieces to 2i*b*(1/epsilon-1/y), and over the semicircle to
-2i*b/epsilon. A z^-3 term has exactly cancelling vertical pieces
and zero semicircle increment. These statements concern finite
epsilon; no divergent piece is discarded or assigned a limit.

The residue integral is i*pi*a_j. The entire e_j has an entire
primitive, so its full detoured integral equals its straight-chord
integral -2i integral_0^y Re e_j(is) ds. Combining these three
contributions before multiplying by -i proves (6). In particular,
the entire-tail replacement alone is not the original differential.

### Actual coefficient errors and the attempted sign test

Equation (1) and L883's local normal convergence give, for N>=2,

\[
 |v_j-v_j^{(N)}|
 \leq 2\sum_{n>N}\frac{a_n\rho^{n-j}}{n-j}
 \leq\frac{2\rho^{-j}}{N+1-j}\sum_{n>N}a_n\rho^n.
\]

All omitted exponents n-j are positive. Positivity of the actual
coefficients and rho<rho_* give

\[
 \sum_{n>N}a_n\rho^n
 \leq(\rho/\rho_*)^{N+1}\sum_{n>N}a_n\rho_*^n
 \leq(\rho/\rho_*)^{N+1}G(\rho_*).
\]

This proves (7) without omitting the finitely many negative powers
or the residue; those were included exactly in v^(N). Every bound
is allowed to depend on the label. For a fixed label and rho_* the
error tends to zero, but no label-uniform cutoff follows.

For real vectors b,c,
|S(b,c)|<=4||b||_infinity||c||_infinity. Write
v=v^(N)+e and w=w^(N)-e, with ||e||_infinity<=E. The exact errors are
2S(v^(N),e)+S(e,e) for alpha,
S(e,t-2v^(N))-S(e,e) for beta, and
-2S(w^(N),e)+S(e,e) for gamma. Their absolute bounds are precisely
E_alpha,E_beta,E_gamma above. Expanding each full product once more
gives

\[
 |h\beta-h_N\beta_N|
 \leq|h_N|E_\beta+|\beta_N|E_h+E_hE_\beta,
\]

which proves the sufficient test (8), including its equality case.

The bounded signed test does not pay this threshold. The moment
representation exposes why coefficient positivity alone is not an
immediate termwise sign argument: when x<0, the actual a3 term in
B(s) contributes 2*a3*y to U0, whereas the actual a4 term contributes
2*a4*x*y<0. Their U2 contributions likewise have opposite signs.
This termwise calculation is legitimate because the G series is
uniformly absolutely convergent on the compact chord and division
by z^3 is bounded there. It is not a counterexample to the sign of
the complete sums, nor a proof that a stronger coefficient inequality
cannot decide (5). For x=0 the exact tail in (6) similarly has the
convergent alternating expansion

\[
 \int_0^y\operatorname{Re}e_j(is)\,ds
   =\sum_{k\geq0}\frac{(-1)^k a_{j+1+2k}y^{2k+1}}{2k+1}.
\]

No decreasing-term or signed-remainder estimate is assumed for it.
The original radial domains do not by themselves provide a pointwise
sign for these chord integrands; in particular chord inclusion was
never among the hypotheses. No specified actual nonreal labels are
available for a finite certificate, and no uniform margin has been
derived. Thus (5) and (8) remain unpaid actual-function conditions.
This stops the present corrected-chord sign attempt, not the graph
route or any future estimate with materially new signed information.
The prior circular-sector obstruction in L885 is only a comparison;
it is not a mathematical input to this calculation.

## Mathlib

Full matching and supporting Mathlib coverage for this specialization
was not checked. No absence claim is made. The analytic input is the
cited Laurent/primitive theorem as already specialized in L883;
the remaining finite bilinear identities and bounds are proved above.
