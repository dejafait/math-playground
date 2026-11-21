# Corollary C048b: the combined Mellin origin allowance

## Hypotheses

Use C048a's actual kernel and its even Taylor coefficients:

\[
 \Phi(z)=\sum_{m\ge1}(4\pi^2m^4e^{9z/2}-6\pi m^2e^{5z/2})
                       e^{-\pi m^2e^{2z}}
        =\sum_{n\ge0}c_nz^{2n}\quad\hbox{near }0.
\]

Let \(p=\sigma+i\tau\), \(r=|p|\), \(L=\log r\), with
\(L\ge12\) and \(\sigma\ge-r/(4L)\). Put
\(w=W_0(2p/\pi)=U+iV\), \(y=V/2\). For \(\tau>0\), set
\(a_y=\min(y,1/4)\) and use C048a's meromorphic primitive

\[
 O_y(p)=\sum_{n\ge0}\frac{c_n(ia_y)^{2p+2n}}{p+n}
           +2\int_{ia_y}^{iy}z^{2p-1}\Phi(z)\,dz,
 \qquad
 E_o(p)=O_y(p)+2\int_0^1(x+iy)^{2p-1}\Phi(x+iy)\,dx.       \tag{1}
\]

For \(\tau<0\) use the conjugate downward formula; for \(\tau=0\),
the sector implies \(p>0\), and set
\(E_o(p)=2\int_0^1x^{2p-1}\Phi(x)\,dx\). All powers use the
principal logarithm. Define, with branches continued from positive p,

\[
 S(p)=\frac{8\pi^{5/2}e^{9w/4}}{\sqrt{p(1+w)}}
       \exp\{2p\operatorname{Log}(w/2)-2p/w\}.             \tag{2}
\]

The audited claim is K. Kawano, *Logarithmic Inequalities of Arbitrary
Order for the Riemann Xi Coefficients*,
[Preprints.org 202611.0383v1, posted 4 November 2026](https://www.preprints.org/manuscript/202611.0383/v1),
Section5.1 (25)-(26), Section5.2 (28), AppendixB's origin paragraphs,
and AppendixC's origin paragraph immediately before C.1. The last
paragraph allocates the combined term in (1) a relative allowance
\(10^{-4}L^{9/2}/r\). No quantitative estimate from that preprint is
assumed here. The prior SPECIALIZE assessment1623 authorizes this
component audit, including an alternative valid proof at the same
normalization. C048a supplies the contour/branch and kernel facts.

## Conclusion

Throughout this closed, unbounded sector,

\[
 \frac{|E_o(p)|}{|S(p)|}
 <10^9L^{5/2}\sqrt r\,e^{-r/32}
 <10^{19}L^{5/2}\sqrt r\,e^{-r/32}
 <10^{-4}\frac{L^{9/2}}r.                                \tag{3}
\]

This pays the nominated combined-origin component, including negative
real parts, reflection and zero height. It is a REPRODUCTION of the
source's allowance by a different estimate: the combined path is
deformed to a straight ray before estimation. The proof needs only
\(\cos V>1/(4L)\) and the first coefficient estimate in (26), and
does not validate every stronger auxiliary bound asserted by the
source. In particular it neither transfers L804's different endpoint
inequality nor discards the finite vertical segment of (1).

This is local validation of known-source mathematics, not a new RH
sign theorem. Other saddle terms, the full relative error (29), zero
counts, inversion and the sufficient Mellin-to-sign bridge remain
unproved here. L030-L032/C032a's actual-Xi positivity gap remains open.
The independent conceptual audit1626 below validates this component
without a mathematical correction. No complete-solution or
formal-verification claim is made.

## Proof

### 1. Quantitative geometry needed for this component

It suffices initially to consider \(\tau\ge0\). C048a proves
\(U>0\), \(0\le V<\pi/2\), and the admissibility of the principal
branch. Write
\(\theta=\arg p\), \(\alpha=\arg w\). The Lambert identity gives

\[
 U+\log|w|=L-\log(\pi/2),\qquad
 \theta=V+\alpha,\qquad \alpha=\arctan(V/U),
 \quad 0\le\theta\le\pi/2+\arcsin(1/(4L)).                \tag{4}
\]

There is no argument wrapping: both arguments and their sum lie
between zero and pi, by the branch geometry in C048a.

First,

\[
 U>3L/4\ge9,\qquad U<L,\qquad |w|<U+2<L+2.              \tag{5}
\]

Indeed \(L/4-\log L-\log(\pi/2)>0\) at \(L=12\), since
\(6\pi<e^3\), and its derivative \(1/4-1/L\) is positive thereon.
For an elementary exact check of the base comparison, use
\(\pi<22/7\), \(e>8/3\), and
\(132/7<512/27\). The exponential bounds used here and below follow
from its power series: the terms through degree three sum to 8/3,
and the remaining tail is less than \((1/24)/(1-1/5)=5/96\),
giving \(8/3<e<11/4<3\). If \(U\le3L/4\), then
\(|w|<\sqrt{(3L/4)^2+4}<L\), which contradicts (4) and that
strict inequality. Now \(|w|>9\), so (4) implies \(U<L\).
Finally \(|w|\le U+V<U+2\).

A sufficient strip clearance is

\[
 \cos V>\frac1{4L}.                                    \tag{6}
\]

If \(V\le1\), use \(\cos1>1/2\). If \(V>1\), put
\(\eta=\arcsin(1/(4L))\) and \(d=\pi/2-V\). The elementary
integral bounds for arctangent and arcsine give

\[
 \alpha>\arctan(1/L)\ge1/L-1/(3L^3),\qquad
 \eta\le\frac{1/(4L)}{\sqrt{1-1/(16L^2)}}<1/(3L).
\]

Thus \(d\ge\alpha-\eta>1/(2L)\). Since \(0<d<\pi/2\),
concavity of sine gives \(\cos V=\sin d\ge2d/\pi>d/2>1/(4L)\).
These estimates hold at the angular and radial boundaries as well.

Put

\[
 q=\sqrt{1+y^2}<\sqrt2,\quad \beta=\arctan y,\quad
 b=|w|/2>9/2,\quad A=\tfrac12-2/U-2/U^2>41/162.
\]

In particular \(b/q>3\), and

\[
 \beta-\alpha-\frac{V}{|w|^2}
 \ge y\left(\tfrac12-2/U-2/U^2\right)=yA.               \tag{7}
\]

Here \(\arctan y\ge y/(1+y^2)\ge y/2\),
\(\alpha\le2y/U\), and \(V/|w|^2\le2y/U^2\).
At \(y=0\) the inequality remains valid with both sides zero.

### 2. Complete-kernel and coefficient bounds

For \(0\le x\le1\), \(0\le t\le y\), (6) implies
\(\Re(\pi e^{2(x+it)})>1/(4L)\). Taking absolute values termwise
in the normally convergent full kernel gives

\[
 |\Phi(x+it)|<14000\sum_{m\ge1}m^4e^{-m^2/(4L)}.
\]

The amplitude constant follows from
\(4\pi^2e^{9/2}+6\pi e^{5/2}<64\cdot200+24\cdot21<14000\).
These elementary exponential bounds follow from \(e<11/4\).
For any \(0<\delta\le1\), the full series satisfies

\[
\begin{split}
 \sum_{m\ge1}m^4e^{-\delta m^2}
 &\le\int_0^\infty(v+1)^4e^{-\delta v^2}\,dv\\
 &\le8\int_0^\infty(v^4+1)e^{-\delta v^2}\,dv\\
 &=3\sqrt\pi\,\delta^{-5/2}+4\sqrt\pi\,\delta^{-1/2}
 <14\delta^{-5/2}.                                    \tag{8}
\end{split}
\]

For the first inequality, on \([m-1,m]\) both factors in its
integrand are at least the corresponding factors of the summand.
The second is convexity of the fourth power. The evaluations use
the Gaussian integral and two integrations by parts, whose boundary
terms vanish. This is the same complete-sum method used in L804,
recomputed on the present strip, not its numerical endpoint theorem.
Consequently

\[
 |\Phi(x+it)|<M_L:=10^7L^{5/2},                          \tag{9}
\]

because \(14000\cdot14\cdot4^{5/2}=6272000<10^7\).

On the disk \(|z|\le1/2\), instead use
\(\Re(\pi e^{2z})\ge\pi e^{-1}\cos1>1/2\).
The same amplitude bound and (8) give
\(\sup_{|z|\le1/2}|\Phi(z)|<196000\cdot2^{5/2}<10^8\).
Here \(e<3\), \(\pi>3\), \(\cos1>1/2\) justify the clearance.
C048a supplies holomorphy on a neighborhood of this disk. Cauchy's
coefficient estimate, in the explicit form
[DLMF1.9.30-31](https://dlmf.nist.gov/1.9#iii), therefore gives

\[
 |c_n|<10^8 4^n.                                       \tag{10}
\]

No truncated theta sum or numerical samples enter these bounds.
The source's second coefficient estimate is unnecessary here.

### 3. A fixed-height identity for the combined contribution

For each fixed \(0<y<\pi/4\), set \(a=1/4\). The sum (1) equals
meromorphically in p

\[
 E_y(p)=\sum_{n\ge0}\frac{c_n(ae^{i\beta})^{2p+2n}}{p+n}
       +2\exp(2p\,i\beta)\int_a^q t^{2p-1}\Phi(te^{i\beta})\,dt,
 \qquad \beta=\arctan y.                               \tag{11}
\]

The exponential here is \(\exp(2p\,i\beta)\), with p the complex
parameter, so its modulus is \(e^{-2\tau\beta}\).
To prove (11), first take \(\sigma>0\). C048a identifies (1) with
the integral along \(0\to iy\to1+iy\). Cauchy's integral theorem
deforms this path to the segment \(0\to1+iy\). The intervening
triangle lies in the theta strip and the principal-log domain apart
from its zero vertex. Removing a small arc there gives a vanishing
\(O(\epsilon^{2\sigma})\) contribution. Splitting the straight
segment at radius a and integrating its uniformly convergent Taylor
series proves (11), including its factor 2 and orientation.

Both sides have meromorphic continuations at this fixed y. C048a
gives the left side. On the right, (10) bounds the Taylor series by
a geometric series with ratio \(4a^2=1/4\), locally uniformly off
the nonpositive integers; the remaining integral is over a compact
segment separated from zero and hence is entire in p. The meromorphic
identity theorem proves (11) everywhere. This identity includes the
finite vertical segment in (1); it has not been omitted or estimated
as a divergent improper integral. The selected sector has no poles,
by C048a. Only now do we evaluate at its numerical height \(y=V/2\).
No analyticity of moving-height summands is asserted.

For \(\sigma>0\) the same identity also gives the unsplit formula

\[
 E_y(p)=2\exp(2p\,i\beta)\int_0^q t^{2p-1}\Phi(te^{i\beta})\,dt. \tag{12}
\]

All points \(te^{i\beta}\), \(0\le t\le q\), lie in the rectangle
of (9), because the endpoint is exactly \(1+iy\).

### 4. Exact normalization and common phase comparisons

Define

\[
 H=2\sigma\log b-2\tau\alpha-2\Re(p/w).
\]

The modulus in (2) is exactly
\(8\pi^{5/2}e^{9U/4}e^H/\sqrt{r|1+w|}\). It is nonzero:
\(p\ne0\), \(U>9\), and exponentials do not vanish. Since
\(|1+w|<U+3\) and \(\sqrt{U+3}<e^U\) for \(U>9\),

\[
 |S(p)|^{-1}<\sqrt r\,e^{-H}.                          \tag{13}
\]

For example, the last elementary comparison follows by squaring
and using \(e^{2U}>1+2U>U+3\). Thus all prefactors in S, not just
its principal exponential, are accounted for.

If \(\sigma\ge0\), set
\(D_q=H-2\sigma\log q+2\tau\beta\). The identity
\(\Re(p/w)=(\sigma U+\tau V)/|w|^2\), (7), and
\(U/|w|^2\le1/U\) yield

\[
 D_q\ge2\sigma(\log(b/q)-1/U)+2\tau y A,
 \qquad \log(b/q)-1/U>8/9.                            \tag{14}
\]

The last bound uses \(b/q>3\), \(\log3>1\), and \(U>9\).
If \(\sigma<0\), set \(D_a=H-2\sigma\log a+2\tau\beta\).
Dropping the favorable term \(-2\sigma U/|w|^2\) gives

\[
 D_a\ge-\frac r{2L}\log(2|w|)+2\tau y A.               \tag{15}
\]

Here \(b/a=2|w|>1\), so the sector bound on sigma has the displayed
inequality direction. Also

\[
 \frac{\log(2|w|)}{2L}
 <\frac{\log((7/3)L)}{2L}
 \le\frac{\log28}{24}<\frac16.                        \tag{16}
\]

Indeed \(2(L+2)\le(7/3)L\), the middle function decreases for
\(L\ge12\), and \(e^4>(8/3)^4>28\).

### 5. The three cases, with their integration prefactors

Suppose first that \(\sigma\ge0\), \(\tau\ge r/2\). Then
\(\theta\ge\pi/6\), and (4) gives
\(V\ge\theta/(1+1/U)>9\theta/10\). Hence \(y>9/40\), so

\[
 D_q>\frac{41}{720}r>r/32.                            \tag{17}
\]

For \(\sigma<0\), necessarily
\(\tau\ge r\sqrt{1-1/(16L^2)}>99r/100\), and
\(\theta>\pi/2\), giving \(y>27/40\). Equations (15)-(16) yield

\[
 D_a>\left(\frac{1353}{4000}-\frac16\right)r
      =\frac{2059}{12000}r>r/32.                       \tag{18}
\]

This includes the sector's negative-real-part boundary. It does not
require the source's stronger r/2 phase claim for that case.

In both cases \(\tau\ge r/2>1\). Let \(B=q^{2\sigma}\) in the
first case and \(B=a^{2\sigma}\) in the second. For \(a\le t\le q\),
\(t^{2\sigma}\le B\); the Taylor endpoint also satisfies
\(a^{2\sigma}\le B\). Since \(|p+n|\ge\tau\), (10)-(11) give

\[
\begin{split}
 |E_y(p)|
 &\le B e^{-2\tau\beta}
       \left(\frac{4\cdot10^8}{3\tau}
                         +2M_L\log(q/a)\right)\\
 &<10^9L^{5/2} B e^{-2\tau\beta}.                      \tag{19}
\end{split}
\]

The geometric series contributes \(4/3\). Also \(q/a<6<e^2\),
so the integral term is less than \(4M_L\). Since \(\tau>1\) and
\(L^{5/2}>1\), its sum with \(4\cdot10^8/(3\tau)\) is less
than \(10^9L^{5/2}\). Equations (13), (17)-(19) give the first
inequality in (3) for these two cases, including \(\sigma=0\) and
the junction \(\tau=r/2\) with nonnegative sigma.

It remains to take \(0\le\tau<r/2\). The sector excludes a negative
sigma in this case, so \(\sigma>\sqrt3\,r/2>4r/5>1\).
Direct integration in (12), using (9), gives

\[
 |E_y(p)|\le\frac{M_L}{\sigma}q^{2\sigma}e^{-2\tau\beta}.
\]

There is no singular pointwise estimate at zero: the integral is
\(\int_0^q t^{2\sigma-1}dt=q^{2\sigma}/(2\sigma)\).
By (14), \(D_q>64r/45>r\). Thus this case gives the stronger bound
\(10^7L^{5/2}\sqrt r\,e^{-r}\), proving (3) here as well.
At \(\tau=y=0\), (12) is exactly the real integral in the
hypotheses with \(q=1\), \(\beta=0\). It proves the zero-height
case directly and does not infer it from a nonuniform limit.

Finally, C048a's conjugation identities for the kernel, primitive,
Lambert branch and principal powers imply
\(E_o(\overline p)=\overline{E_o(p)}\). The branches of S have the
same property (and its modulus certainly does). Reflection therefore
covers the lower half-plane with exactly the same estimate.

### 6. Paying the stated allocation on the entire ray L>=12

The ratio of the source's larger envelope to its allocated allowance is

\[
 F(L)=10^{23}L^{-2}\exp(3L/2-e^L/32).
\]

For \(L\ge12\),
\((\log F)'=3/2-2/L-e^L/32<0\), since \(e^{12}>2^{12}\).
At the endpoint, using \(\log10<3\) and \(\log12>0\),

\[
 \log F(12)=23\log10+18-2\log12-e^{12}/32
             <69+18-128=-41<0.
\]

This proves the last strict inequality of (3) uniformly, without
sampling. No mathematical script or finite certificate is needed.
All other inequalities were likewise established for their full
parameter intervals, not inferred from endpoint samples.

The standard inputs are Cauchy's integral theorem and coefficient
estimate, the Gaussian integral, compactly dominated parameter
integration, and the meromorphic identity theorem. C048a already
establishes their needed kernel and continuation hypotheses. The
new work verifies the source-specific normalization and uniform
constants; it does not reprove a general Mellin or saddle theorem.

### Independent conceptual audit1626 — 18 November 2026

The full proof was checked under the unchanged SPECIALIZE
assessment1624, separately approved in1625. This audit uses C048a
as its sole direct local mathematical input; the older L804 endpoint
inequality and the preprint's quantitative assertions are not premises.
The result is validation of the reproduced allowance, with no correction
to (1)-(19). The following checks record the load-bearing points.

**Geometry and complete modes.** The lower bound in (5) follows by
contradiction from the modulus identity: if \(U\le3L/4\), then
\(|w|<L\), whereas
\(3L/4+\log L<L-\log(\pi/2)\). The latter inequality has a positive
derivative for its difference on \(L\ge12\), and its base case is
\(6\pi<e^3\); \(132/7<512/27\) checks the stated rational comparison.
The other geometry bounds then use \(U>9\), not an asymptotic onset.
For (6), the \(V>1\) case gives
\[
 d>\frac{2}{3L}-\frac{1}{3L^3}>\frac1{2L},
\]
since \(L^2>2\). The \(V\le1\) case includes \(V=0\). Thus the
rectangle and the entire ray of (11) stay strictly within the strip;
there is no lost equality case at either sector boundary.

The complete-sum comparison (8) is termwise on each \([m-1,m]\),
with \((v+1)^4\ge m^4\) and \(e^{-\delta v^2}\ge e^{-\delta m^2}\).
Its two Gaussian integrals give exactly the coefficients 3 and 4
shown there. The inequality \(\delta^{-1/2}\le\delta^{-5/2}\), for
\(0<\delta\le1\), and \(\sqrt\pi<2\) give the strict constant 14.
The amplitude estimates are valid on the whole rectangle and also
the disk: \(\Re z\le1\) suffices for their upper bounds; on the
disk the lower clearance is \(\pi e^{-1}\cos1>1/2\).
For example, \(e<3\) already implies \(e^{9/2}<200\) and
\(e^{5/2}<21\), by squaring and comparing \(3^9<200^2\) and
\(3^5<21^2\). Hence (9)-(10) control the full kernel and every
Taylor coefficient, without a truncation residual. The coefficient
bound is for the coefficient of \(z^{2n}\), so its factor is
\((1/2)^{-2n}=4^n\), with no missing factorial.

**Fixed-height equality and continuation.** At fixed
\(0<y<\pi/4\), the two paths from zero to \(1+iy\) enclose a
triangle whose nonzero points avoid the logarithm cut. The removed
arc has length \(O(\epsilon)\), and the integrand on it has modulus
\(O_p(\epsilon^{2\sigma-1})\). Thus it vanishes for every fixed
\(\sigma>0\). The radial parametrization has
\(z^{2p-1}dz=\exp(2p\,i\beta)t^{2p-1}dt\). Integrating the
factor 2 on \([0,a]\) cancels the factor 2 in \(2p+2n\).
This verifies the orientation, phase and denominator in (11).

On compact parameter sets away from the possible poles, the series
has geometric ratio \(4a^2=1/4\) up to its uniformly controlled
denominator; the finite radial integral is entire. The left side
uses the original primitive plus its entire finite horizontal segment.
The meromorphic identity theorem therefore applies at fixed y on
the plane, before choosing \(y=V/2\). In particular it preserves the
original finite vertical segment for \(y>1/4\); it does not replace
that segment by zero. The sector contains no nonpositive integer.
The denominator estimate \(|p+n|\ge\tau\) is used only in the
two cases with \(\tau>1\), never in the small-height case.

**Normalization and the adverse real part.** Multiplication by
\(\overline w\) gives
\(\Re(p/w)=(\sigma U+\tau V)/|w|^2\), with a plus sign in
front of \(\tau V\). Consequently the phase difference is exactly
\[
 D_t=2\sigma\log(b/t)-\frac{2\sigma U}{|w|^2}
       +2\tau\left(\beta-\alpha-\frac V{|w|^2}\right),
 \qquad t=q\text{ or }a.
\]
For \(\sigma\ge0\), replacing \(U/|w|^2\) by its upper bound
\(1/U\) gives a lower bound. For \(\sigma<0\), the middle term
is positive and may be dropped; because \(\log(b/a)>0\), replacing
\(\sigma\) by \(-r/(4L)\) again gives a lower bound. These are
the two different sign arguments in (14)-(15), not an absolute-value
estimate that would lose the favorable term.

The exact factor in \(|S|^{-1}\) is
\(\sqrt{r|1+w|}e^{-9U/4}/(8\pi^{5/2})\). Since
\(\sqrt{|1+w|}<\sqrt{U+3}<e^U\), it is strictly smaller than
\(\sqrt r\). In particular S is nonzero. A compatible square-root
branch can explicitly be written
\(\exp((\operatorname{Log}p+\operatorname{Log}(1+w))/2)\):
the sector avoids the cut for p and \(\Re(1+w)>1\). This also
checks conjugation for the branch continued from positive p.

**Cases, junctions and the allocation.** Equation (7) has
\(A>41/162\). The first case uses
\(y>9\pi/120>9/40\), so its phase margin is
\((9/40)(41/162)r=41r/720>r/32\).
For negative sigma it uses \(y>9\pi/40>27/40\) and
\(\tau>99r/100\). The exact lower bound after the loss (16) is
\[
 \left(2\frac{99}{100}\frac{27}{40}\frac{41}{162}
           -\frac16\right)r
   =\frac{2059}{12000}r>\frac r{32}.
\]
The integral and Taylor endpoint are both bounded by the same B
in each case. The Taylor sum contributes at most
\(4\cdot10^8/(3\tau)\); the integral contributes less than
\(4\cdot10^7L^{5/2}\). Their sum is strictly below
\(10^9L^{5/2}\), including all fixed prefactors.

The remaining case has \(\sigma>4r/5>1\) and integrates the
power at zero exactly; it obtains \(D_q>64r/45>r\). At zero height
the same real integral is convergent and supplies the bound directly.
The cases include \(\sigma=0\) and \(\tau=r/2\); conjugation
supplies the lower half-plane. None requires taking a uniform limit
as a moving height tends to zero with negative sigma.

Finally, the logarithm of the ratio of the *larger* \(10^{19}\)
envelope to the requested allocation is exactly
\(23\log10-2\log L+3L/2-e^L/32\). Its derivative is negative
on \([12,\infty)\), and its value at 12 is less than \(-41\)
by the stated elementary comparisons. Thus the strict final bound
in (3) holds on the entire unbounded sector, not merely on sampled
points. No mathematical script or numerical certificate is required.

This independently checks one known-source component. It supplies no
estimate for the other saddle terms, no full (29), no zero-count or
inverse-transform conclusion and no actual-Xi mixed-sign theorem.
Those independent gaps and the earlier global-import stop remain.

## Mathlib

Full matching coverage for this moving-sector combined-origin estimate
has not been checked and is unknown. Cauchy theory and Gaussian
integration are supporting mathematical inputs, not a claim of a
matching formal theorem. No absence, declaration-level coverage or
formal-verification claim is made. The displayed analytic proof is
the complete informal evidence for this component.
