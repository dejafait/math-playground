# Lemma 848: actual-G exchange-diagonal compatibility and a failed extension

## Hypotheses

Use the actual entire function and positive radius of L018/L775,

\[
 G(z)=\frac18\xi\left(\frac12+\frac{\sqrt z}{2}\right)
     =\sum_{n\geq0}a_nz^n,\qquad a_n>0,\qquad
 R=R_1>0,\qquad RG'(R)/G(R)=1,
 \qquad C=R^2/G(R)^2>0.
\]

Evenness defines G without choosing a square-root branch. Retain the
full r=2,k=1 form, graph, and coordinate orientation of audited L847:

\[
 \omega=C\frac{G(z_1)G(z_2)(z_1-z_2)^2}{z_1^3z_2^3}
                    dz_1\wedge dz_2,\qquad
 z_j=R e^{u_j(t,s)+i\theta_j},\quad(\theta_1,\theta_2)=(t,s),
 \qquad \Phi_u^*\omega=q_u(t,s)\,dt\wedge ds.                 \tag{1}
\]

For the general diagonal identity, u is real C^2, 2pi-periodic in each
coordinate, and exchange-equivariant: u_2(t,s)=u_1(s,t). Define

\[
 h(m)=u_1(m,m),\qquad b(m)=(\partial_1-\partial_2)u_1(m,m),
 \qquad z(m)=R e^{h(m)+im},\qquad
 K_u(m)=\lim_{\delta\to0}\frac{q_u(m+\delta,m-\delta)}{\delta^2}.
                                                               \tag{2}
\]

The limit uses the scalar density in the original coordinate order.
It is not the coefficient of dm wedge ddelta, which would have the
additional coordinate determinant -2.

The construction below reuses audited L778's actual-G polynomial P_0,
its 97 interval coefficients, and its uniform error
|G-P_0|<3.141e-48 on |z|<=1600. Its analytic and trusted-software
qualifications are retained. No RH, prescribed zero list, simplicity,
nonvanishing of G on an arbitrary graph, or nonzero complex Jacobian
is assumed. In particular the identity (3) below retains every zero.

## Conclusion

Every graph in the stated exchange-equivariant class has the exact limit

\[
 K_u(m)=4C\left(\frac{G(z(m))}{z(m)}\right)^2
                   (1-i h'(m))(1-i b(m))^3.                  \tag{3}
\]

There exist bounded real C-infinity periodic exchange-equivariant
graphs for which K_u(m)>0 for every m. Explicit diagonal data are

\[
 \begin{split}
 d(m)&=\sqrt{600^2-400^2\sin^2m},\qquad
 r(m)=-400\cos m+d(m),\qquad h(m)=\log(r(m)/R),\\
 f(m)&=\frac{G(r(m)e^{im})}{r(m)e^{im}},\qquad
 \phi(m)=\operatorname{Arg}f(m)\quad(-\pi<\operatorname{Arg}<\pi),\\
 \psi(m)&=2\phi(m)-\arctan h'(m),\qquad
 b(m)=\tan(\psi(m)/3).                                      \tag{4}
 \end{split}
\]

These definitions are everywhere legitimate, with a strict margin:

\[
 \operatorname{Re}\frac{G(z)}z+\frac13\left|\operatorname{Im}\frac{G(z)}z\right|
       >\frac{14}{10^9}\quad (|z+400|=600),\qquad
 \frac{K_u(m)}C>4\cdot10^{-16}.                              \tag{5}
\]

One global realization of the data is

\[
 \begin{split}
 u_1(t,s)&=\frac{h(t)+h(s)}2+
                \frac{b(t)+b(s)}4\sin(t-s),\\
 u_2(t,s)&=u_1(s,t).                                        \tag{6}
 \end{split}
\]

However, this particular extension has a strictly negative full density:

\[
 -4.546\cdot10^{-8}<\frac{q_u(0,\pi)}C
                    <-4.545\cdot10^{-8}<0.                 \tag{7}
\]

Thus the proposed all-m diagonal compatibility test passes for the
actual G, while the elementary extension (6) fails the global sign
condition. Neither an everywhere real/nonnegative pullback nor a
neighborhood on which the full complex density is nonnegative has been
constructed. Other extensions with the same diagonal data and other
coupled graphs remain open. This is a local mathematical input for the
contour question, not a new mixed-minor sign or an RH candidate. The
separate conceptual audit below accepts precisely these claims, with
the inherited analytic and trusted-software qualifications.

## Proof

### Coverage, imported inputs and qualification

The invocation-start EXPLORE assessment is
`drafts/literature/2026-11-06-actual-g-radial-graph-full-phase.md`.
The supplied checkpoint specifically nominated the exchange-diagonal
test inside that fixed full-form target. The product obstruction of
L847 is a contrast, not an obstruction to this coupling. Its exact
pullback and graph homotopy are inputs. No contour-existence theorem,
total-reality condition or PDE solvability assertion is imported.

The actual-G evaluator is the already audited input of L778, equations
(2)–(5) and its step433 audit. Only that evaluator is reused; the
Fredholm norm, minor sign and zero count are not needed. Its standard
numerical-complex-analysis comparison is F. Johansson, *Numerical
integration in arbitrary-precision ball arithmetic*,
[arXiv:1802.07942v1, Section2/2.1, pp2–4, Section4, pp7–8](https://arxiv.org/pdf/1802.07942v1).
For the remaining standard inputs use Jiří Lebl, *Guide to Cultivating
Complex Analysis*, version1.10, 5 November2026,
[Theorem3.3.8, p79](https://www.jirka.org/ca/ca.pdf#page=79) and
[Section4.1.1, pp91–92](https://www.jirka.org/ca/ca.pdf#page=91), as
inspected in `drafts/literature/2026-11-06-actual-g-exchange-diagonal-audit.md`.
The former bounds the nth Taylor coefficient by M/r^n when the function
is holomorphic on a neighborhood of the closed radius-r disk and M
bounds its boundary magnitude. Here P_0 is entire and its radius256
disk lies inside the disk used for M. The latter constructs the
principal logarithm on C minus the nonpositive real axis, normalized
at1, with derivative1/z. Its smooth imaginary part is used only after
the sector exclusion in (5). Neither input supplies the actual-G
enclosures or a graph-existence theorem. These are imports, not new
quadrature, logarithm or contour-counting theorems.

Interval arithmetic retains L778's contracts for Python3.15.2,
Decimal1.70 and libmpdec4.0.1: directed basic arithmetic and nearest
correctly rounded exp/sqrt widened by adjacent endpoints. See the
[Python3.15 Decimal documentation](https://docs.python.org/3.15/library/decimal.html)
and mpdecimal's [context/correct-rounding](https://www.bytereef.org/mpdecimal/doc/libmpdec/context.html)
and [arithmetic-function contracts](https://www.bytereef.org/mpdecimal/doc/libmpdec/arithmetic.html).
The inherited implementation uses allcr=1 under the CPython contract
checked in L778. The new calculations report those same versions.
No binary attestation or formal verification is asserted. Exact
Fraction checks below do not replace the inherited analytic input.

The source assessment did not supply these diagonal data or locate an
exact matching graph theorem. The construction's original
POTENTIALLY_NEW classification records that limited
comparison only; this is not a claim of certified originality. The
known evaluator and elementary standard methods are reused explicitly.

### Full diagonal limit, including zeros

At (m,m) write p=partial_1 u_1 and v=partial_2 u_1. Exchange symmetry
gives Du=[[p,v],[v,p]], so h'=p+v and b=p-v. Consequently

\[
 \det(I-iDu)=(1-i h')(1-i b).                               \tag{8}
\]

For t=m+delta and s=m-delta, differentiability gives

\[
 u_1(t,s)=h+b\delta+o(\delta),\qquad
 u_2(t,s)=h-b\delta+o(\delta),\qquad
 z_1-z_2=2z(b+i)\delta+o(\delta).
\]

L847's complete formula is

\[
 q_u=-C\frac{G(z_1)G(z_2)(z_1-z_2)^2}{z_1^2z_2^2}
                       \det(I-iDu).
\]

Divide by delta^2 and take the limit. Since (b+i)^2=-(1-i b)^2,
the two minus signs cancel and give (3). Only the nonzero z_j occur
in denominators. In particular, if G(z(m))=0 the same limit is zero;
no zero was deleted. On the diagonal the two factors in (8) are
nonzero because h',b are finite and real; this is a consequence of
exchange symmetry, not a global Jacobian assumption. If q_u were
everywhere real and nonnegative, its limit K_u would be so as well.

### A complete uniform sector certificate for the chosen circle

The circle |z+400|=600 encloses zero and meets every radial ray once.
Solving its quadratic radial equation gives precisely r in (4).
It satisfies 200<=r<=1000. To cover the entire circle without a
trigonometric enclosure, use four exact rational arcs

\[
 z=-400+600 i^j\frac{1+it}{1-it},\qquad
                  0\le t\le1,\quad j=0,1,2,3.              \tag{9}
\]

They include all endpoints; their denominator has squared modulus
1+t^2>0. Each quadrant starts with 64 dyadic t intervals and may be
bisected up to eight times. The output retains every accepted interval
and each rejected enclosure that caused a refinement. The latter are
enclosure failures, not omitted pieces of the circle.

Let [p_n] be all 97 coefficient intervals for the exact polynomial P_0
in L778, and bound

\[
 M=\sum_{n=0}^{96}\sup|[p_n]|\,1600^n.
\]

For each arc interval, its exact midpoint under (9) is z_c, with
|z_c|<=1000. Directed rectangles enclose z_c, the full arc z, and
z-z_c. Let Delta be the resulting upper bound for |z-z_c| and put
rho=Delta/256. The disk |w-z_c|<=256 lies in |w|<=1256<1600.
The factorial-normalized Taylor coefficients of P_0 at z_c through
degree8 are evaluated by the finite Horner-jet recurrence, retaining
the coefficient and center widths. Cauchy's coefficient estimate gives
the complete remainder bound

\[
 \left|P_0(z)-\sum_{n=0}^8\frac{P_0^{(n)}(z_c)}{n!}(z-z_c)^n\right|
       \le M\frac{\rho^9}{1-\rho},\qquad \rho<1.             \tag{10}
\]

The program adds L778's full error E_G to (10) in both real and
imaginary components before dividing by the nonzero rectangle for z.
Every division rectangle excludes zero, also checked with exact
Fractions in the saved-data validation. This encloses the actual
f=G(z)/z on the whole arc, rather than just its midpoint.

For a rectangle f in [x_-,x_+]+i[y_-,y_+], the quantity

\[
 x_-+\frac13\max(0,y_-,-y_+)                                \tag{11}
\]

is a lower bound for Re f+|Im f|/3. The complete certificate has
261 accepted arcs (64,64,69,64 by quadrant), five retained refinements,
no terminal failures, and exact gap-free partitions of every [0,1].
Its smallest lower bound in (11) is
greater than 1.4825665760907973e-8, hence greater than 14/10^9.
The largest rho is less than .047732<1. All coefficient widths and
all three analytic tails already included in E_G remain present.
The largest added Taylor-tail-plus-E_G bound is less than 1.731e-10;
it is included in (11), not subtracted after declaring a sign.

Reproduce the new application from the notebook directory with

```text
python3 scripts/actual-g-radial-graph/exchange_diagonal_certificate.py --output exchange-diagonal-replay.json
python3 scripts/actual-g-radial-graph/check_exchange_diagonal_certificate.py
```

The original evidence is
`scripts/actual-g-radial-graph/exchange-diagonal-certificate.json`;
the full consistency and point checks are
`scripts/actual-g-radial-graph/exchange-diagonal-validation.json`.
The generator refuses to overwrite an existing output. The validation
checks the original saved certificate: all 97 inherited intervals and
their hashes, all 261 arc margins/division rectangles, the polynomial
bound, each complete Taylor and analytic error, and exact coverage.
Its selected `/checks` field was read completely. This is not an
independent regeneration of the Taylor-jet enclosures or a separate
conceptual audit. Both reports say PASS_PENDING_INDEPENDENT_AUDIT and
have no failures. The full original and refined records are on disk.

The earlier floating-point diagnostic is preserved separately as
`scripts/actual-g-radial-graph/exchange-diagonal-diagnostic.json` and
is not a proof input. Its stronger proposed condition Re f>0 failed.
The validation rigorously confirms that failure at (9) with j=1,t=1/4:
Re f lies between -7.206e-8 and -7.205e-8. The generator's first chosen
point t=1/2 did not certify that stronger failure; its false witness
flag remains recorded. Neither point invalidates the wider sector
proved by (11), and no failed right-half-plane test is hidden.

### Smooth periodic data and the positive limit

Inequality (5) excludes f=0 and the nonpositive real axis. Its principal
argument is therefore smooth and 2pi-periodic. If Re f>=0, its absolute
argument is at most pi/2. If Re f<0, (5) implies
(-Re f)/|Im f|<1/3. In both cases

\[
 |\phi|<\frac\pi2+\arctan(1/3)<\frac{5\pi}{8}.              \tag{12}
\]

For the last strict inequality, tan(pi/8)=sqrt(2)-1>1/3, since
2>16/9. Differentiation of the explicit positive r gives

\[
 h'(m)=\frac{400\sin m}{d(m)},\qquad
 |h'|\le\frac2{\sqrt5}<1.
\]

Thus |arctan h'|<pi/4, and (12) implies |psi|<3pi/2 uniformly
with a strict margin. The definition of b in (4) is smooth, periodic
and bounded, and arctan b=psi/3 on its principal interval. Substitution
in (3) cancels the phase exactly, giving

\[
 K_u=4C|f|^2\sqrt{1+(h')^2}\,(1+b^2)^{3/2}>0.              \tag{13}
\]

For the explicit quantitative bound, Re f+|Im f|/3<=4|f|/3;
(5) therefore yields |f|>(3/4)(14/10^9)>10^(-8).
The two remaining magnitude factors in (13) are at least one.
This proves K_u/C>4e-16 at every m, without a sampled phase branch.

Formula (6) realizes the data on the whole torus: at t=s=m its value
is h, and its first-row derivatives are (h'+b)/2,(h'-b)/2.
Consequently its diagonal tangential and normal derivatives are h',b
as required. It is bounded C-infinity and periodic in both variables,
and satisfies exchange equivariance identically. L847 proves that
this is an oriented embedded radial graph homologous to the coefficient
torus, regardless of any off-diagonal complex tangencies. The diagonal
Vandermonde zero remains: q_u(m,m)=0. We have controlled its leading
quadratic coefficient, not removed that zero or the off-diagonal phase.

### The explicit global extension fails at an antipodal point

At m=0,pi, the circle points are 200,-1000. The function f is real
there and (5) makes it positive. Hence phi(0)=phi(pi)=0. Also
h'(0)=h'(pi)=0, so b(0)=b(pi)=0. At (t,s)=(0,pi), every derivative
of (6) is zero: terms differentiating b are multiplied by sin(t-s)=0,
and those differentiating the sine contain b(0)+b(pi)=0.
Thus Du=0, the full logarithmic Jacobian is 1, and

\[
 z_1=v,\quad z_2=-v,\qquad v=\sqrt{200\cdot1000},\qquad
 \frac{q_u(0,\pi)}C=-\frac{4G(v)G(-v)}{v^2}
                  =-\frac{G(v)G(-v)}{50000}.                \tag{14}
\]

Both points are in the audited evaluator's disk. Direct interval
evaluation, retaining the same coefficient widths and uniform E_G,
gives 0.6848927997<G(v)<0.6848927998 and
0.0033184589<G(-v)<0.0033184590. The full intervals in the validation
give (7), with actual q/C about -4.54557726828626685e-8. Positivity of
both G values and the entire final negative interval are checked;
no assumed zero location or numerical root list is used.

This stops (6) as a nonnegative global contour. It does not refute the
diagonal compatibility construction, nor other exchange-equivariant
extensions that alter values and derivatives away from the diagonal.
The all-angle reality equation and nonnegativity in L847(4), other
orders/shifts, uniform transfer, and actual-Xi all-degree positivity
remain unresolved.

### Separate conceptual audit, 6 November 2026

This RESEARCH / proof_audit used the invocation-start EXPLORE assessment
`drafts/literature/2026-11-06-actual-g-exchange-diagonal-audit.md`.
Classification REPRODUCTION concerns verification of this existing
application, not a mathematical discovery beyond the sources checked.
No defect was found in (1)–(14). The audit does not accept a globally
real or nonnegative graph. It reuses only the already audited evaluator
part of L778, not its Fredholm norm or zero count.

**Algebra and zero handling.** The row convention A_(j,l)=partial_l u_j
in L847 gives the pullback determinant det(I-iA), including both factors
1/i. At a diagonal point exchange symmetry gives A the eigenvalues h',b.
The collision expansion has coefficient 2z(b+i); squaring it and
retaining the leading minus sign of F gives exactly the cubic normal
factor in (3). The limit is in the original dt wedge ds orientation;
transforming the volume element to (m,delta) would introduce -2 and
would describe a different scalar. Only z is divided out. A zero of G
therefore gives K=0, without invalidating the limit. C^2 regularity is
more than sufficient for the expansions and continuity used here.

**Whole-arc enclosure and analytic remainder.** The rational circle
map (9) traverses four closed quarters, with every endpoint retained.
Its real parameter denominator is 1+t^2, always positive. The true
midpoint z_c lies on the circle even though the computed z_c is an
interval rectangle. That exact point has |z_c|<=1000; the radius256
disk is contained in |w|<=1256<1600. All 97 coefficient intervals bound
the exact finite-integral P_0, so their absolute majorant M bounds P_0
on that disk. The descending-index Horner recurrence encloses its normalized
derivatives at the true center; center uncertainty is retained at every
multiplication. The rectangle subtraction includes every z-z_c.
The upward magnitude and rho bound, followed by Cauchy's coefficient
estimate and the geometric series starting at degree9, prove (10).
The complete E_G is added in both components before division by z.
Every division rectangle excludes zero. Formula (11) is the exact
rectangle lower-bound rule, including imaginary intervals crossing 0.

The reviewed primitives perform directed real operations, exact sign
reversal, correct zero-crossing squares and widened nearest sqrt under
the previously inspected software contracts. Complex multiplication
and conjugate-over-modulus-square division use these primitives and
enclose the results despite repeated dependent inputs. Nothing in the new
callers differentiates a sampled error or drops coefficient widths.

Run the fresh full replay and the audit from the notebook directory:

```text
python3 scripts/actual-g-radial-graph/exchange_diagonal_certificate.py --output exchange-diagonal-audit-replay.json
python3 scripts/actual-g-radial-graph/audit_exchange_diagonal.py
```

Both refuse to overwrite their evidence. The full replay exactly
matches every field of the original certificate, including all 261
accepted arcs and all five refinements. The new audit also recomputes
each Taylor coefficient by the distinct finite identity

\[
 \frac{P_0^{(j)}(z_c)}{j!}
   =\sum_{n=j}^{96}\binom nj p_nz_c^{n-j},\qquad 0\le j\le8.
\]

This follows by differentiating the finite polynomial and uses interval
powers and sums rather than the original Horner-jet recurrence. It is
an independent caller check, not a second implementation of the
trusted interval primitives. All resulting Taylor coefficients, full
arc boxes, complete errors and per-record checks are saved in
`scripts/actual-g-radial-graph/exchange-diagonal-conceptual-audit.json`.
Every accepted arc in this second calculation exceeds 14/10^9, with
minimum lower bound
1.482566576090797322326161301092460648952280225611688347026315728679238981e-8.
Exact Fraction checks cover all original records: center membership
and circle equation, the squared displacement bound, full Taylor and
analytic errors, denominator exclusion, interval order, sector margins,
gap-free partitions and both children of every retained refinement.
The five original failed enclosures remain refinement evidence, not
counterexamples or discarded arcs. The first unsuccessful stronger-
sector witness and the later negative-real-part witness are preserved.

The audit report is PASS with no failures. Its complete checks, summary
and antipodal intervals were inspected; all 266 numerical records were
processed by the reviewed implementation. Both calculations used
Python3.15.2/Decimal1.70/libmpdec4.0.1. The contexts flagged only
Inexact/Rounded, with no exceptional arithmetic condition. The separate
`scripts/actual-g-radial-graph/exchange-diagonal-input-provenance.json`
records exact SHA256 equality of the inherited certificate and backend
with the accepted step433 report's original_sha256 and source_sha256.
Thus the 97 coefficient intervals and all analytic tails are precisely
the previously audited input. The theta quadrature was not regenerated.
Original evidence hashes were unchanged. Software remains trusted,
not binary-attested or formally verified.

**Global branch and jets.** Since r is the unique positive radial root,
200<=r<=1000, d>=sqrt(200000), and differentiation gives
r'=400 sin(m)r/d, hence the claimed h'. The sector excludes both 0 and
the nonpositive real axis. Principal Log composed with f gives a
single smooth periodic phi. For Re f<0 the ratio (-Re f)/|Im f|<1/3
gives (12); Re f>=0 also satisfies that strict bound. Combining it with
|h'|<=2/sqrt5<1 gives |psi|<3pi/2. Continuity on the compact circle
makes the gap from the tangent poles uniform. Therefore
arctan(b)=psi/3 on its principal interval; the literal phase
2phi-arctan(h')-3arctan(b) is 0, proving (13), without choosing a
logarithm of the two-variable form. The magnitude bound in (5) follows
from |f|>(3/4)(14/10^9)>10^-8 and the two factors at least 1.

For completeness the two first derivatives of (6) are

\[
 \partial_tu_1=\frac{h'(t)}2+
 \frac{b'(t)}4\sin(t-s)+\frac{b(t)+b(s)}4\cos(t-s),
 \qquad
 \partial_su_1=\frac{h'(s)}2+
 \frac{b'(s)}4\sin(t-s)-\frac{b(t)+b(s)}4\cos(t-s).
\]

They give exactly (h'+b)/2,(h'-b)/2 on the diagonal. Swapping t,s
gives the second row for u_2. This verifies the first jets, smoothness,
exchange symmetry and periodicity of the stated extension. L847's
embedding and homotopy apply because u is bounded and real; no global
complex-Jacobian nonvanishing or reality of q is inferred.

**Antipodal value and scope.** At m=0,pi the actual f is real because G
has real coefficients, and the sector makes it positive. Thus phi=b=h'=0
at those endpoints. The displayed first derivatives all vanish at
(0,pi), as do the derivatives of u_2. The radii there equal
R exp((log(200/R)+log(1000/R))/2)=sqrt(200000). This verifies (14),
with the full determinant equal 1 and the minus sign retained. The
second numerical caller sums the real polynomial by successive powers
at both interval radii, adds the full E_G and verifies positivity of
both G values. Its complete final enclosure is

\[
\begin{split}
-4.54557726828626685158130878893815366270185188004518114298997649999244062224\,10^{-8}
&\le q_u(0,\pi)/C\\
&\le-4.54557726828626685158130875162126452554473114034841066941512419570654095820\,10^{-8}.
\end{split}
\]

It is wholly inside (7). This validates the scoped failure of (6),
not an obstruction to every coupled extension. A positive leading
diagonal coefficient does not establish exact reality or nonnegativity
on any open collar. Those claims, global coupling, other orders/shifts,
uniform transfer and all-degree positivity remain unproved.

## Mathlib

Full matching coverage was not checked; no absence claim is made.
The proof uses standard pullback algebra, Cauchy's coefficient estimate,
the principal logarithm, and the qualified numerical input of L778.
No named Mathlib theorem or formal certificate is claimed for this
actual-G diagonal construction. The separate informal audit above
accepts its scoped claims with the stated numerical qualifications;
neither those claims nor the negative extension point resolves RH.
