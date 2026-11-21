# C466z — Actual-h buffered local current chart

## Hypotheses

Use C466a's actual entire function
\[
 c_0=\xi(1/2)>0,\qquad h(w)=\xi(1/2+\sqrt w)/c_0,
\]
with the completion convention in C466n(11). Retain C466a's
external critical-strip, symmetry, paired-product, counting and
verified-low-zero qualifications when interpreting this chart as a
chart for its imported reciprocal density. The analytic estimates
below use only the actual completion, c_0>0 and classical
right-half-plane identities; they do not reprove that density input.

Let D={w:|w-1|<1/4}. The logarithm B on D is normalized by
B(1)=log h(1) real. Its existence is proved below. Put
\[
 x=B'(1),\quad
 H_x(z)=\sum_{j=1}^3\{B(1+z_j)-x(1+z_j)\},\quad
 \mathcal B=\{z\in\mathbb C^3:|z_j|<1/4\}.
\]
All gradient and holomorphic Hessian norms are the standard Hermitian
norms in C466y. Use its unit-flat raw flow from X(0,u)=iu, with
S=-2 log Delta+H_x, on the first maximal interval in
\(\mathcal B\setminus\{\Delta=0\}\), with no restart.

## Conclusion

The normalized logarithm exists, x is real, and the following are
explicit admissible constants for C466y on the entire polydisc:
\[
 R=\frac14,\qquad M_1=120,\qquad M_2=1000,\qquad
 a=\frac1{16},\qquad T_0=\frac1{1920},                 \tag{1}
\]
\[
 H_0=3\left[\log\!\left(
 \frac{3\Gamma(3/4)\zeta(3/2)}{8c_0\pi^{3/4}}\right)-x\right],
 \quad
 x=\frac43-\frac{\log\pi}{4}+\frac{\psi(3/4)}4
                   +\frac{\zeta'(3/2)}{2\zeta(3/2)}.    \tag{2}
\]
These give H_x(0)=H_0 real and
\[
 \sup_{\mathcal B}\|\nabla H_x\|_2\le120,\qquad
 \sup_{\mathcal B}\|D^2H_x\|_{\rm op}\le1000,\qquad
 r_*:=\sqrt3a+M_1T_0=\frac{\sqrt3+1}{16}<\frac3{16}<R. \tag{3}
\]
The expression for H_0 is an exact finite real constant, not an
existential compactness constant or a claimed numerical enclosure.

For every complex or real chi in C_c^infinity(\mathcal B), the full
forms beta=Psi^*(chi Omega) and gamma=Psi^*(dchi wedge Omega), where
\[
 \Omega=F\,dz_1\wedge dz_2\wedge dz_3,\quad
 F(z)=\Delta(z)^2e^{-H_x(z)}
     =\Delta(z)^2\prod_{j=1}^3\frac{e^{x(1+z_j)}}{h(1+z_j)}, \tag{4}
\]
have coefficientwise bounded zero extensions to
Q=(0,T_0) times (-a,a)^3 and satisfy
\[
                     d\bar\beta=\bar\gamma
                     \quad\hbox{in distributions on }Q. \tag{5}
\]
There is no first outer exit at or before T_0, including simultaneous
outer/collision events. All initial diagonals, triple collisions,
arbitrary relative spacings and complete time/parameter coefficients
are covered, on precisely the first-lifetime convention of C466y.

This supplies one actual-weight local chart. It asserts no determinant
sign, time-zero trace, global contour identity, patch-interface or
tail payment, restart, all-order positivity, or implication to RH.

## Proof

### Imported analytic tools and why specialization is needed

The completion formula is C466n(11), and its exact center derivative
is C466n(14); no numerical nodes or center enclosures from that result
are used as uniform estimates. We import zeta's Dirichlet series,
derivative series and Euler product from
[DLMF 25.2.1, 25.2.6–7 and 25.2.11](https://dlmf.nist.gov/25.2),
valid for Re(s)>1, and nonvanishing there from
[DLMF 25.10(i)](https://dlmf.nist.gov/25.10#i).
Gamma has no zeros and poles only at nonpositive integers;
psi=Gamma'/Gamma, and the convergent formulas used below are
[DLMF 5.2(i), 5.2.2](https://dlmf.nist.gov/5.2),
[5.7.6](https://dlmf.nist.gov/5.7#E6) and
[5.15.1](https://dlmf.nist.gov/5.15#E1).

The holomorphic-logarithm theorem is Stefan Adams, *MA3B8 Complex
Analysis*, 18 March 2020,
[Lemma 10.12, pp.102–103](https://warwick.ac.uk/fac/sci/maths/people/staff/stefan_adams/complexanalysis2020.pdf):
a nowhere-zero holomorphic function on a simply connected open domain
has a holomorphic logarithm, with value selectable among its logarithms
at one point. These sources, with the generic current C466y/audit983,
were assessed in review984 before this attempt. They are imported,
not reproved. The needed specialization is the domain check, absolute
majorants, Hermitian constants and strict buffer; the source theorems
do not themselves state these chart constants.

### Domains and the normalized branch

For w in D use the principal q=sqrt(w), and set s=1/2+q, v=s/2.
Since Re(w)>3/4 and |w|<5/4,
\[
 \Re q=\sqrt{(|w|+\Re w)/2}>\sqrt3/2>5/6,
 \quad 5/6<|q|<\sqrt5/2<9/8.
\]
Consequently
\[
 \Re s>4/3,\quad |s|<13/8,\quad
 \Re v>2/3,\quad |v|<13/16<1,\quad
 |s-1|>1/3.                                             \tag{6}
\]
The square root is holomorphic on D. Neither polynomial factor s or
s-1 vanishes; Gamma(v) is holomorphic and nonzero; zeta(s) is
holomorphic and nonzero by Re(s)>1; and pi^(-s/2) never vanishes.
The completion therefore makes h holomorphic and nowhere zero on D.
Since D is simply connected the cited logarithm theorem applies.
At w=1 all completion factors and c_0 are positive, so h(1)>0.
Choose B(1)=log h(1) real. Uniqueness of the normalized branch and
conjugation show B(conjugate(w))=conjugate(B(w)); it agrees with
the real logarithm on D intersect (0,infinity). Thus x is real.

### Uniform zeta and Gamma bounds

We give complete tail majorants rather than sample values. For
sigma>=4/3 the integral comparison for the decreasing function
t^(-sigma) gives
\[
 \sum_{n\ge1}n^{-\sigma}\le1+\int_1^\infty t^{-4/3}\,dt=4.
\]
The absolutely convergent Euler product also gives
\[
 |\zeta(s)^{-1}|=\prod_p|1-p^{-s}|
 \le\prod_p(1+p^{-\sigma})
 \le\prod_p(1-p^{-\sigma})^{-1}=\zeta(\sigma)\le4.       \tag{7}
\]
All inequalities follow first for finite prime products and then by
absolute convergence; no information on critical-strip zeros enters.

For n>=2 and t in [n-1,n], n^(-sigma)<=t^(-4/3) and
log n<=log(t+1)<=log t+log 2. Thus for k=1,2,
\[
 \sum_{n\ge2}(\log n)^k n^{-\sigma}
 \le\int_1^\infty(\log t+\log2)^k t^{-4/3}\,dt.
\]
Substitution y=log t and integration by parts give
integral_1^infinity (log t)^j t^(-4/3) dt = j! 3^(j+1)
for j=0,1,2. Since log 2<1, the k=1 and k=2 majorants are,
respectively, 9+3 log 2<12 and
54+18 log 2+3(log 2)^2<75. The cited derivative series therefore
give, uniformly on (6),
\[
 |\zeta'(s)|<12,\qquad |\zeta''(s)|<75.
\]
Absolute locally uniform convergence justifies their use for complex
s; the same majorants cover the whole chart. Combining with (7),
\[
 \left|\frac{\zeta'}\zeta(s)\right|<48,\qquad
 \left|\left(\frac{\zeta'}\zeta\right)'(s)\right|
 \le\left|\frac{\zeta''}\zeta\right|
       +\left|\frac{\zeta'}\zeta\right|^2<300+2304=2604. \tag{8}
\]

For Re(v)>2/3, |v|<1, the cited combined digamma series and
trigamma series are
\[
 \psi(v)=-\gamma_E-1/v+\sum_{k\ge1}\frac{v}{k(k+v)},
 \qquad \psi'(v)=\sum_{k\ge0}(k+v)^{-2}.
\]
Use |v|^(-1)<3/2, |k+v|>=k+Re(v)>k, 0<gamma_E<1,
and sum_(k>=1) k^(-2)<=1+integral_1^infinity t^(-2)dt=2.
The elementary Euler-constant bound follows directly from the
harmonic-sum/integral comparison defining gamma_E. It follows that
\[
 |\psi(v)|<1+3/2+2<5,\qquad
 |\psi'(v)|<9/4+2<5.                                    \tag{9}
\]
The very same majorants prove uniform absolute convergence on this
chart; in particular no value-only asymptotic remainder has been
differentiated.

### Logarithmic derivatives and Hermitian bounds

Let L(s)=xi'(s)/xi(s) on the image in (6). Logarithmic
differentiation of the nonzero completion factors gives
\[
 L(s)=\frac1s+\frac1{s-1}-\frac{\log\pi}{2}
       +\frac12\psi(s/2)+\frac{\zeta'(s)}{\zeta(s)}.
\]
Using (6), (8), (9) and log pi<2,
\[
 |L(s)|<\frac34+3+1+\frac52+48<56,
\]
\[
 |L'(s)|<\frac9{16}+9+\frac54+2604<2620.                \tag{10}
\]
The second bound follows by differentiating this displayed identity;
the Gamma contribution is psi'(s/2)/4. It does not assume any
logarithm of xi outside the zero-free region just checked.

The chain rule for the normalized B on D gives
\[
 B'(w)=\frac{L(s)}{2q},\qquad
 B''(w)=\frac{L'(s)}{4q^2}-\frac{L(s)}{4q^3}.
\]
Since |q|>5/6, these imply uniformly on all of D
\[
 |B'(w)|<\frac35\,56=\frac{168}5<34,
\]
\[
 |B''(w)|<\frac9{25}\,2620+\frac{54}{125}\,56
              =\frac{120924}{125}<1000.                 \tag{11}
\]
In particular |x|<34. Each gradient coordinate of H_x is
B'(1+z_j)-x, of modulus <68. Its holomorphic Hessian is diagonal
with entries B''(1+z_j); in Hermitian operator norm a complex
diagonal matrix has norm the maximum modulus of its entries. Hence
\[
 \|\nabla H_x\|_2<68\sqrt3<120,
 \qquad \|D^2H_x\|_{\rm op}<1000.
\]
Here (68 sqrt3)^2=13872<14400=120^2. These are whole-box
bounds, without a center-to-box inference or numerical sampling.
Substitution s=3/2,q=1 in the completion and in B' gives exactly
(2), consistent with C466n(14). Every factor there is finite,
Gamma(3/4), zeta(3/2), c_0 and pi are positive, and the stated
real logarithm is therefore finite. This establishes the required
normalization H_x(0)=H_0 as well as its explicit value.

### Buffered application of the existing current theorem

With (1), M_1 T_0=1/16, and sqrt3<2 proves precisely (3).
Thus 0<a<R, T_0>0 and every hypothesis of C466y holds on
the same open polydisc, with no change of metric or time variable.
Since exp B(w)=h(w), exponentiating the definition of H_x gives
(4) exactly, including its complex phase and normalization; no
branch-dependent multiplier is dropped.

Apply C466y by citation. It supplies no outer exit, bounded complete
beta/gamma coefficients, their coefficientwise zero extensions and
the distributional identity (5), including its O(epsilon^(1/4))
full cutoff-error bound with the constants in C466y(20),(24)
evaluated at (1),(2). All those constants are finite: for example
the exponent (4M_2+M_1^2)T_0 is 115/12 and
E_0=exp(-H_0+15 sqrt3/2). No reproof of its singular-flow,
support or collision argument is needed. The test domain Q is
open; the theorem supplies no trace at time zero or its spatial
edges. C466k's phase obstruction and C466t's unbuffered-event
obstruction remain intact. This is a reproduction/specialization
of assessed tools and an audited local result, not a claimed
advance beyond the checked literature or an RH candidate.

### Independent applicability audit — 14 November 2026, step988

This audit uses invocation-start SPECIALIZE assessment ready986,
including the primary-source locator repair987. Its inspected DLMF
identities and Adams Lemma10.12 are reused with exactly their recorded
domains. C466y's conceptual audit983 is an established input; no generic
singular-current theorem or density construction is reproved here.

**Whole disk and logarithm.** On D, |w|>=Re(w)>3/4, so
(|w|+Re(w))/2>3/4. The principal square root therefore has
Re(q)>sqrt(3)/2>5/6, while |q|=sqrt(|w|)<sqrt(5)/2<9/8.
Adding 1/2 and then dividing by two gives every inequality in (6);
in particular Re(s-1)>1/3 and hence |s-1|>1/3. Thus neither
polynomial factor vanishes, the Gamma argument stays away from all
its poles, and the Euler product applies on the entire image, not
just the real center. The nonzero completion factors prove the
logarithm theorem's hypotheses before it is used. Positivity of the
factors at s=3/2 fixes B(1) real. The holomorphic function
overline(B(overline(w))) is another logarithm with that same value;
their difference is a continuous 2*pi*i integer and vanishes at 1.
They agree throughout D. This verifies the real normalization and x.

**Every series tail.** The bound n^(-sigma)<=t^(-4/3) on
[n-1,n], n>=2, follows from t<=n and sigma>=4/3. Also
0<=log n<=log t+log2 there. Multiplication, integration on each
unit interval and summation prove both differentiated-zeta majorants
without requiring (log t)^k t^(-sigma) to be decreasing. The three
integrals are 3,9,54; consequently the bounds are <12 and <75.
The summable interval majorants establish uniform absolute convergence
over the full image. Finite Euler products give the reciprocal bound
in (7), and their absolutely convergent limits preserve it. Thus
48 and 2604 in (8) cover both quotient terms with no missing tail.

For Gamma, retain the combined term v/[k(k+v)] in the digamma
series. Its modulus is <1/k^2, while |1/v|<3/2. The k=0
trigamma term is <9/4 and the remaining terms are bounded by 1/k^2.
The common sum is <=2. Together with 0<gamma_E<1 these give
both bounds in (9) on the whole domain and uniform summable tails.
No differentiated asymptotic error or uncombined divergent series
is used.

**Chain rule, constants and normalization.** Directly summing the
terms for L gives 221/4<56. Its differentiated terms sum to
9/16+9+5/4+2604=41837/16<2620. Here the signs of the two
reciprocal derivatives do not affect their absolute bounds, and the
Gamma derivative has the factor 1/4. Since ds/dw=1/(2q) and
d(1/(2q))/dw=-1/(4q^3), the displayed B'' identity is exact.
Its majorant is 120924/125<1000, and |B'|<168/5<34.
Subtracting the same x in every gradient coordinate gives <68 per
coordinate, not <34. Hence the Hermitian gradient bound follows
from 3*68^2=13872<14400. The diagonal complex Hessian has singular
values |B''(1+z_j)|, proving the asserted operator bound.

At s=3/2 the polynomial completion factor is
(1/2)(3/2)(1/2)=3/8. Thus h(1) is exactly the positive quantity
inside the logarithm in (2). Substituting q=1 into B'=L/(2q)
gives precisely C466n(14) and (2), including the factors 1/4 and
1/2 on the Gamma and zeta terms. Every denominator is nonzero.
This proves the exact finite real H_0=3(log h(1)-x); no enclosure
or center-value certificate is substituted for a uniform estimate.

**Complete application.** H_x is holomorphic on the same open
polydisc and has exactly the Hermitian bounds required by C466y.
The prescribed raw unit-flat first-lifetime flow is its flow with
H=H_x. We have M_1*T_0=1/16 and sqrt(3)<2, so
r_*=(sqrt(3)+1)/16<3/16<1/4. This strict Euclidean-ball buffer
is the hypothesis excluding every outer approach, including one
simultaneous with collision; no componentwise or speed-only
substitute is made. Exponentiating exp B=h gives (4) with its
full complex phase and its c_0 normalization intact.

For completeness the constants in the invoked theorem specialize to
E_0=exp(-H_0+15sqrt(3)/2), E=E_0 exp(115/12),
Lambda*T_0=40/3 and

\[
 G=8^{-13/2}E_0^{3/4}(6\sqrt2+15)<\infty.
\]

Indeed 2a=1/8, so this last expression is exactly C466y(20),
not a new integral estimate. For any chi, set C_0=||chi||_infinity
and C_1=sup||dchi|| in that theorem's real covector norm. Its
complete coefficient bounds (18) become

\[
 |\bar\beta_{123}|\le C_0E\,8^{-6},\qquad
 |\bar\beta_{tij}|\le C_0E(6\sqrt2+15)8^{-5},\qquad
 |\bar\gamma_{t123}|\le4C_1E(6\sqrt2+15)8^{-5}.
\]

For every compactly supported scalar test phi on Q the full error
in C466y(24) is bounded by

\[
 8\,2^{1/4}\|\phi\|_\infty C_0B_\theta
 e^{40/3}\sqrt{\log(2)/1920}\,G\,\epsilon^{1/4}
 \longrightarrow0.
\]

This retains all time/parameter coefficients and arbitrary complex
chi, every initial diagonal and triple collision, and coefficientwise
zero extension on the open Q. The audited C466y therefore supplies
exactly d bar(beta)=bar(gamma), with its stated orientation and no
boundary trace or restart. Its smooth survivor and compact-support
arguments apply with unchanged hypotheses.

**Verdict and limits.** The full C466z statement passes without a
mathematical correction. The Adams link above now uses the inspected
/people/staff/ locator; this is editorial, not an additional input.
Direct mathematical inputs remain C466a, C466n and C466y as in the
DAG; C466x is used through C466y. The result validates one actual-h
local realization obligation by reproduction/specialization of the
assessed tools. It is no discovery beyond the sources checked.
External density qualifications remain in force. C466k/j/t and
stop948 are comparisons, not assumptions or refuted results.
Residual determinant phase, time-zero trace, global interfaces and
tails, all-order signs and Xi transfer remain open. No mathematical
script, formal verification or RH candidate is claimed.

## Mathlib

Full matching coverage has not been checked. The source assessment
covered the primary analytic identities and generic C466y, not a
Mathlib theorem for this explicit actual-h chart. Holomorphic
logarithms, convergent special-function series, the chain rule and
finite-dimensional Hermitian norm estimates are supporting standard
inputs; exact Mathlib theorem names for the required forms have not
been checked. Unknown availability is not evidence of absence. No
formal verification or numerical certificate is claimed.
