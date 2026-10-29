# L279 — Fixed-mesh coefficient of the exact reflected plaquette pair

## Hypotheses

Keep exactly L003's SU(2) model on the relative cubical lattice in
\(D=[-4,4]^4\), with positive even \(N\), \(a=8/N\), and \(a\) fixed before
\(g\downarrow0\). Links contained in any boundary face are pinned to
identity; normal end links remain variable. All elementary plaquettes
are counted once, with orientation \(\mu<\nu\). Use ordinary
two-dimensional trace, Wilson weight
\(\exp[-\mathcal S(U)/g^2]\), where

\[
P_p(U)=1-\tfrac12\operatorname{Tr}U_p,
\qquad \mathcal S(U)=4\sum_pP_p(U).
\tag{1}
\]

Let \(f=f_*\) be L003's real smooth bump, with integral one and support
in \([-1/4,1/4]^3\times[1,2]\). Write
\(h_+=f\), \(h_-=\theta f\), where \(\theta(x,t)=(x,-t)\).
For either test function put

\[
H_h(U)=4\sum_{p\parallel12}h(z_p)P_p(U),\qquad
F_{a,g}(h)=g^{-2}(H_h-\mathbb E_{a,g}H_h).
\tag{2}
\]

There is no additional \(a^4\) in (2), no flow, and no interacting
composite counterterm. The observable is real, so L003's exact quantity is

\[
Q_{a,g}(f)=g^{-4}\operatorname{Cov}_{a,g}(H_{h_-},H_{h_+}).
\tag{3}
\]

Use L003's exact rooted forest quotient. Let \(E'_a\) be the remaining
variable links; set forest and pinned links to identity. In exponential
coordinates use \(t^c=i\sigma^c/2\),
\(-2\operatorname{Tr}(t^ct^d)=\delta_{cd}\), and
\(U_e=\exp(\vartheta_e^ct^c)\), \(\vartheta=gx\).
Thus \(x_e=aA_e\) in L003's Hermitian-generator convention.
For a smooth function on this slice define its homogeneous Taylor jet by

\[
G_{[m]}(x)=\frac1{m!}\left.\frac{d^m}{du^m}
G(\exp(ux))\right|_{u=0}.
\tag{4}
\]

Set

\[
S_m=\mathcal S_{[m]},\qquad
b_{\pm,k}=(H_{h_\pm})_{[k+2]}\quad(k=0,1,2),\qquad
M_2=\frac1{12}\sum_{e\in E'_a}|x_e|^2.
\tag{5}
\]

All these jets remain on the forest slice. Let \(\langle\cdot\rangle_0\)
be the normalized Gaussian proportional to \(e^{-S_2(x)}dx\).
L003 proves its nondegeneracy. For polynomial random variables define
the finite-moment cumulant

\[
\operatorname{cum}_0(Y_1,\ldots,Y_r)=
\sum_{\pi\in\mathcal P_r}(-1)^{|\pi|-1}(|\pi|-1)!
\prod_{B\in\pi}\left\langle\prod_{j\in B}Y_j\right\rangle_0.
\tag{6}
\]

This uses no convergent moment generating function.

## Conclusion

The requested coefficient exists and is the following finite Gaussian
expression:

\[
\begin{aligned}
\kappa_a={}&\operatorname{cum}_0(b_{-,2},b_{+,0})
 +\operatorname{cum}_0(b_{-,1},b_{+,1})
 +\operatorname{cum}_0(b_{-,0},b_{+,2})\\
&-\operatorname{cum}_0(b_{-,1},b_{+,0},S_3)
 -\operatorname{cum}_0(b_{-,0},b_{+,1},S_3)\\
&-\operatorname{cum}_0(b_{-,0},b_{+,0},S_4+M_2)
 +\tfrac12\operatorname{cum}_0(b_{-,0},b_{+,0},S_3,S_3),\\[2pt]
Q_{a,g}(f)={}&q_a(f)+g^2\kappa_a+o_a(g^2),\\
\kappa_a={}&\lim_{g\downarrow0}g^{-2}[Q_{a,g}(f)-q_a(f)].
\end{aligned}
\tag{7}
\]

Here \(q_a\) is exactly L003's leading reflected coefficient. The
\(M_2\) term is the exponential-coordinate density of the exact quotient
Haar measure; it is not a Ward divergence. No Ward observable or response
coefficient \(\Gamma\) is identified with (7).

For completeness all jets in (7) have an explicit finite matrix formula.
For an oriented plaquette write its four ordered signed edge matrices as
\(X_{p,j}=\epsilon_{p,j}x_{e_{p,j}}^ct^c\); put \(X_{p,j}=0\) for
forest or pinned edges. For \(m=2,3,4\) define

\[
p_m(p;x)=-\frac12
\sum_{\substack{n_1,\ldots,n_4\ge0\\n_1+\cdots+n_4=m}}
\frac{\operatorname{Tr}
(X_{p,1}^{n_1}X_{p,2}^{n_2}X_{p,3}^{n_3}X_{p,4}^{n_4})}
{n_1!n_2!n_3!n_4!}.
\tag{8}
\]

The zeroth power is the identity matrix, including when \(X=0\).
Then the quantities in (5) are exactly

\[
S_m=4\sum_p p_m(p;x),\qquad
b_{\pm,k}=4\sum_{p\parallel12}h_\pm(z_p)p_{k+2}(p;x).
\tag{9}
\]

Thus (6), (8), (9), and the inverse of the positive quadratic form
\(S_2\) specify a finite computation at each mesh; no higher insertion
or action jet is left unspecified. This is an extraction formula, not
an evaluation of the growing lattice Wick sums, a sign assertion, or a
mesh-uniform bound. In particular it does not establish an error
\(\le c_{\rm box}/2\) on any physical running-coupling trajectory.

## Proof

### 1. Exact reduction, jets, and density

Both \(H_{h_\pm}\), their product, and \(\mathcal S\) are gauge
invariant. L003's exact successive Haar integration therefore reduces
their moments and partition function to product Haar on \(E'_a\), with
forest links fixed to identity. The unique minimum is the identity and
its quadratic form is positive definite on this slice. In particular
there are no residual zero modes requiring another determinant. Normal
links at the boundary are among the variables unless they belong to the
forest; links contained in boundary faces are pinned throughout.

The ordered exponential product for \(U_p\) immediately gives (8) by
collecting the coefficient of \(u^m\) in
\(\prod_{j=1}^4\exp(uX_{p,j})\). Its constant plaquette term cancels
the 1 in \(P_p\), and its linear term is zero by tracelessness. For
\(y_p=\sum_j\epsilon_{p,j}x_{e_{p,j}}\), cyclicity of trace gives

\[
p_2(p;x)=-\tfrac14\operatorname{Tr}
\left(\sum_jX_{p,j}\right)^2=\tfrac18|y_p|^2.
\tag{10}
\]

Consequently \(S_2=\tfrac12\sum_p|y_p|^2\) and
\(b_{\pm,0}=\tfrac12\sum_{p\parallel12}h_\pm(z_p)|y_p|^2\).
For \(x=aA\), \(y_p=a^2(dA)_p\), so these have exactly L003's
\(a^4/2\) quadratic normalization. The higher jets in (8) need not be
functions of curvature alone and will not be moved to Hodge gauge.

The reduced coordinate density is a constant times
\(J(\vartheta)=\prod_{e\in E'_a}j(\vartheta_e)\), with

\[
j(v)=\left(\frac{\sin(|v|/2)}{|v|/2}\right)^2,
\qquad
\log J(gx)=-g^2M_2(x)+O_a(g^4|x|^4).
\tag{11}
\]

This is precisely the SU(2) volume calculation in L011 (7), obtained
from the unit three-sphere polar volume. The constant and the Jacobian
\(g^d\), where \(d=3|E'_a|\), cancel in normalized moments. The action
and insertion expansions in these coordinates are

\[
\begin{aligned}
g^{-2}\mathcal S(\exp(gx))
 &=S_2+gS_3+g^2S_4+\cdots,\\
g^{-2}H_{h_\pm}(\exp(gx))
 &=b_{\pm,0}+g b_{\pm,1}+g^2b_{\pm,2}+\cdots.
\end{aligned}
\tag{12}
\]

Relative to \(e^{-S_2}dx\), the unnormalized measure coefficients
through order two are therefore

\[
1+gW_1+g^2W_2,\qquad
W_1=-S_3,\quad W_2=\tfrac12S_3^2-S_4-M_2.
\tag{13}
\]

These are integrated asymptotic coefficients, not a uniform pointwise
expansion on the entire rescaled chart.

### 2. Remainder at the required order

The precise standard asymptotic input is William D. Kirwin,
*Higher Asymptotics of Laplace's Approximation*, Asymptotic Analysis 70
(2010), 231–248,
[DOI](https://doi.org/10.3233/ASY-2010-1016),
[arXiv:0810.1700v2](https://arxiv.org/pdf/0810.1700v2)
(5 June 2010), Theorem 2.1; signed amplitudes are handled in the
Lemma 2.3 argument, and the smooth nondegenerate specialization and
parity are in section 3.2. The inspected statement gives finite
expansions with little-o remainder to any specified finite order when
the phase and amplitude have the corresponding expansions. It supplies
no uniformity as dimension or mesh varies. We apply this known theorem,
rather than reprove general Laplace asymptotics.

Here the phase is \(\mathcal S(\exp\vartheta)\). Choose a smooth
cutoff supported inside a sufficiently small exponential-coordinate
ball and equal to one near zero. L003's unique minimum and Hessian
give \(\mathcal S\ge c_a|\vartheta|^2\) there and a strictly positive
action gap outside any smaller neighborhood of zero in the compact
reduced group manifold. Each amplitude below is bounded on that
manifold. The discarded part of each integral is consequently
\(O_a(e^{-c'_a/g^2})\); division by the partition function, which is
asymptotic to a positive constant times \(g^d\), and by \(g^4\)
preserves its negligibility at every finite power of \(g\).

In the local chart apply the theorem to the four smooth amplitudes

\[
J(\vartheta),\quad
J(\vartheta)H_{h_-}(\exp\vartheta),\quad
J(\vartheta)H_{h_+}(\exp\vartheta),\quad
J(\vartheta)H_{h_-}(\exp\vartheta)H_{h_+}(\exp\vartheta),
\tag{14}
\]

including the cutoff. The chart contains zero internally; the physical
lattice boundary imposes no boundary on this coordinate ball. The
quadratic phase is strictly positive in every direction, all radial
Taylor coefficients are smooth, and compact support gives the required
weighted integrability. Signed amplitudes are permitted. There is no
coupling-dependent centering in (14).

Take the expansion, after removing the common \(g^d\), through degree
six with \(o_a(g^6)\) remainder. Smoothness of all amplitudes and phase
allows this finite order. The normalized single moments can thus be
computed through degree four with \(o_a(g^4)\) remainder, and the joint
moment through degree six with \(o_a(g^6)\) remainder. Their leading
degrees are respectively two and four, because \(H_h\) vanishes to
degree two. The coefficients at the needed orders are exactly those
from (12), (13): higher insertion jets have degree at least five, the
next action term contributes at order \(g^3\) after scaling, and the
next Haar term at order \(g^4\). They cannot contribute to the order
\(g^2\) correction of a scaled single moment or scaled joint moment.

All odd coefficients vanish. Indeed a jet of order \(m\) is homogeneous
of degree \(m\), the Gaussian is even, and the coefficient of odd
\(g\)-degree after scaling has odd total polynomial degree in \(x\).
This is the parity argument for the smooth Laplace specialization; a
symmetric cutoff may be used near zero, and its exterior contributes
only exponentially small terms. In particular no uncancelled order
\(g\) term in \(Q\) obstructs the limit in (7).

Subtracting the product of the two single moments now gives the
covariance through degree six with \(o_a(g^6)\) remainder: a single
moment error \(o_a(g^4)\) is multiplied by another moment of order
\(O_a(g^2)\). Equation (3) therefore has the required \(o_a(g^2)\)
remainder after division by \(g^4\). This argument accounts for both
negative insertion powers and uses neither an exchange of limits nor
formal perturbation theory as a remainder estimate.

### 3. Moving means and connected coefficient

Here is the mean subtraction explicitly. All brackets in this section
are Gaussian. For \(\epsilon\in\{-,+\}\), write

\[
\begin{aligned}
m_{\epsilon,0}&=\langle b_{\epsilon,0}\rangle_0,\\
m_{\epsilon,2}&=\langle b_{\epsilon,2}\rangle_0
 +\langle b_{\epsilon,1}W_1\rangle_0
 +\operatorname{Cov}_0(b_{\epsilon,0},W_2).
\end{aligned}
\tag{15}
\]

The coefficient \(\langle W_1\rangle_0\) is zero by oddness.
Normalization by the partition function subtracts
\(\langle b_{\epsilon,0}\rangle_0\langle W_2\rangle_0\), giving
the covariance in (15). The two possible order-one mean terms,
\(\langle b_{\epsilon,1}\rangle_0\) and
\(\langle b_{\epsilon,0}W_1\rangle_0\), are each zero by oddness.
The rigorous moment expansions just established give

\[
\mathbb E_{a,g}H_{h_\epsilon}
 =g^2m_{\epsilon,0}+g^4m_{\epsilon,2}+o_a(g^4).
\tag{16}
\]

For the joint moment put

\[
\begin{aligned}
n_0={}&\langle b_{-,0}b_{+,0}\rangle_0,\\
n_2={}&\langle b_{-,2}b_{+,0}+b_{-,1}b_{+,1}
                         +b_{-,0}b_{+,2}\rangle_0\\
 &+\langle(b_{-,1}b_{+,0}+b_{-,0}b_{+,1})W_1\rangle_0
   +\operatorname{Cov}_0(b_{-,0}b_{+,0},W_2).
\end{aligned}
\tag{17}
\]

Then \(\mathbb E_{a,g}(H_{h_-}H_{h_+})=g^4n_0+g^6n_2+o_a(g^6)\).
In particular the centered coefficient is

\[
\kappa_a=n_2-m_{-,2}m_{+,0}-m_{-,0}m_{+,2}.
\tag{18}
\]

There is no product of nonzero order-one means. Equations (15)–(18)
retain every moving-mean correction, including the changes caused by
the action and the Haar density.

To check that (18) is (7), expand (6), or equivalently use the formal
source series

\[
\log\left\langle\exp\left[
u\sum_{k=0}^2g^k b_{-,k}
+v\sum_{k=0}^2g^k b_{+,k}
-gS_3-g^2(S_4+M_2)\right]\right\rangle_0.
\tag{19}
\]

At each fixed multidegree only finitely many polynomial moments are
used, so (19) is a formal power series and makes no analytic
moment-generating-function assertion. The coefficient of \(uv\) is
the normalized covariance. At order \(g^2uv\), choosing insertion
orders \((2,0),(1,1),(0,2)\) gives the first three terms of (7).
Choosing one cubic action vertex and insertion orders \((1,0)\) or
\((0,1)\) gives its next two terms with minus signs. A single
\(-g^2(S_4+M_2)\) gives the sixth term, while two copies of
\(-gS_3\) give the last term with factor \(1/2\). The logarithm
enforces exactly the connected subtractions in (18), by the finite
partition identity (6). This is L011's finite-dimensional connected
expansion method applied to the actual pair (2), rather than to its
different Ward/flow pair.

### 4. Identification of the leading term and limitations

The leading term from (16), (17) is
\(\operatorname{Cov}_0(b_{-,0},b_{+,0})\).
By (10), it is the forest-slice covariance of the quadratic curvature
sums with coefficient \(a^4/2\). L003's linear quotient-to-orthogonal
slice map preserves curvature and changes coordinate volume by a
constant; integrating the gradient factor of its Hodge Gaussian leaves
this same curvature law. Subtracting the Gaussian means therefore gives
exactly \(q_a(f)\), including its real reflected insertion and its three
colors. That comparison is used only for the leading term. The cubic
and quartic jets and \(M_2\) in (7) still refer to the forest coordinates
and are not individually identified with Hodge-Gaussian expressions.

The finite Gaussian moments in (7) exist because \(S_2\) is positive
definite and each entry is a polynomial. Combining (18) with the
remainder and leading-term identification proves (7).

No conclusion about the sign or growth of \(\kappa_a\) as \(a\to0\)
follows. The remainder is only fixed-mesh little-o. Even a subsequent
bound on \(\kappa_a\) would leave higher-order uniform control and
composite mixing to establish before the \(c_{\rm box}/2\) comparison
could follow along a specified physical trajectory. Neither this
coefficient nor L003's finite positive Gaussian reflection coefficient
constructs a nontrivial continuum theory, positivity on its full
observable algebra, the infinite-volume limit, other gauge groups, or
a finite positive physical mass. L004's scalar-only warning and the
separate Ward route are not bypassed.

As a limited algebraic check, run
`PYTHONDONTWRITEBYTECODE=1 python3 scripts/exact-reflected-coefficient/check.py`.
It reuses L011's nonzero-cubic, two-distinct-insertion polynomial test
and compares independent normalized moment division with (6)'s
connected expression using exact rational Gaussian moments. Both
second coefficients are \(47/80\); their difference is exactly zero,
as required, and deleting either the cubic or Haar corrections changes
the answer. Full inputs, comparison, failures and source fingerprint are
saved in `scripts/exact-reflected-coefficient/cumulant-certificate.json`.
This checks the connected algebra and sensitivity to omitted terms;
it does not evaluate (7) for the box or prove the analytic remainder.

### 5. Independent critical audit (2026-10-25)

**Verdict:** (7) passes the fixed-mesh audit under the stated hypotheses.
This verifies the specialization and its remainder, not an ultraviolet
estimate or the other parts of L003. No coefficient or hypothesis was
changed. The following checks make the acceptance independent of the
generic polynomial example.

The exact quotient premises in L003 section 1 apply to each of the four
amplitudes (14): all are built from gauge-invariant plaquette traces.
The rooted forest removes one group variable per interior vertex by
Haar invariance, with no residual transformation fixing all forest links.
Every zero-action configuration is flat; path independence in the cube
and the connected pinned boundary make its boundary potential constant,
and fixing that potential at a boundary vertex makes it identity at
every boundary vertex. Forest links then fix the interior potential.
The corresponding real-cochain argument gives a trivial kernel for
the forest quadratic form. Thus neither a second flat saddle nor an
unremoved zero mode invalidates the compact-complement gap. Normal
boundary links are not silently pinned in this argument.

For the jet audit, a reversed edge is exactly \(\exp(-u x_e^ct^c)\),
so the ordered product and factorials in (8) include every term and
preserve noncommutativity. Cyclicity is used only for the quadratic
trace in (10). Since \(\operatorname{Tr}(t^ct^d)=-\delta_{cd}/2\),
its coefficient is \(|y_p|^2/8\), not \(|y_p|^2/4\).
Multiplication by 4 gives both the action and insertion factors in
(12). Also
\(\sin(r/2)/(r/2)=1-r^2/24+O(r^4)\); squaring and taking the
logarithm gives \(-r^2/12+O(r^4)\). Product Haar on precisely
\(E'_a\) therefore gives \(-M_2\) in (13), with no forest-edge
contribution or extra gauge determinant.

For a direct check of all connected signs, abbreviate
\(A=b_{-,0}, B=b_{+,0}, C=b_{-,1}, D=b_{+,1}\),
\(A_2=b_{-,2}, B_2=b_{+,2}, V=S_3, T=S_4+M_2\), and
\(R=V^2/2-T\). Write brackets for Gaussian expectations and define

\[
\begin{aligned}
\mathcal D_R(A,B)={}&\langle ABR\rangle
 -\langle AB\rangle\langle R\rangle
 -\langle AR\rangle\langle B\rangle
 -\langle BR\rangle\langle A\rangle
 +2\langle A\rangle\langle B\rangle\langle R\rangle.
\end{aligned}
\]

Inserting (15) and (17) into (18), without using a generating function,
gives exactly

\[
\begin{aligned}
\kappa_a={}&\operatorname{Cov}_0(A_2,B)
 +\operatorname{Cov}_0(A,B_2)+\langle CD\rangle\\
 &-\bigl(\langle CBV\rangle-\langle CV\rangle\langle B\rangle\bigr)
  -\bigl(\langle ADV\rangle-\langle DV\rangle\langle A\rangle\bigr)
  +\mathcal D_R(A,B).
\end{aligned}
\]

Here \(A,B,A_2,B_2,T\) are even and \(C,D,V\) are odd.
Thus \(\langle CD\rangle=\operatorname{cum}_0(C,D)\), and the
two parenthesized terms are respectively
\(\operatorname{cum}_0(C,B,V)\) and
\(\operatorname{cum}_0(A,D,V)\). Expanding (6) with two labeled
copies of \(V\), using \(\langle V\rangle=0\), gives

\[
\operatorname{cum}_0(A,B,V,V)
 =\mathcal D_{V^2}(A,B)
   -2\langle AV\rangle\langle BV\rangle
 =\mathcal D_{V^2}(A,B).
\]

The last equality uses oddness of both products, not a claim that the
cubic vertex vanishes. Since \(\mathcal D_T(A,B)=
\operatorname{cum}_0(A,B,T)\), linearity in \(R\) proves all seven
terms and the factor \(1/2\) in (7). In particular the two mean
corrections and the partition normalization are both present.

For the analytic order check, in Kirwin v2 Theorem 2.1 take its large
parameter \(k=g^{-2}\), radial phase order \(\nu=2\), amplitude
order \(\lambda=d\), and truncation index 6 (distinct from the mesh
integer \(N\)). Smooth phase expansion through degree 8 and smooth
amplitude expansion through degree 6 suffice; leading amplitude
coefficients may vanish. The resulting error is \(o(g^{d+6})\).
The positive leading quadratic phase, an interior chart minimum and
compactly supported smooth amplitudes verify the theorem's positivity,
local expansion and integrability hypotheses. The exterior gap already
proved makes localization harmless after every required negative power.
This uses Theorem 2.1's little-o statement (2.3), not just the weaker
display (1.3) of Theorem 1.1.

After removing \(g^d\), the denominator has a nonzero constant term.
The single numerators vanish below degree two and the joint numerator
below degree four. Consequently only denominator degrees zero and two enter
their required degrees four and six. Higher action and density jets,
although available for the theorem's remainder, do not enter these
coefficients. Parity kills degrees three in a single moment and five
in the joint moment. If the single-moment errors are
\(r_\pm=o_a(g^4)\), their product expansion through degree six has error
\(O_a(g^8)+O_a(g^2)r_-+O_a(g^2)r_++r_-r_+=o_a(g^6)\).
Together with the joint error this proves the stated \(o_a(g^2)\)
after division by \(g^4\), with no uniformity assertion.

Finally, the real observable identity (3) needs no reflection
invariance of the chosen forest. L003's linear slice map preserves
curvature and has constant Jacobian; the gradient Gaussian integrates
out independently. This identifies the leading covariance with its
defined \(q_a\). None of the higher jets or the coordinate density is
transported by that argument. The audit accepts precisely the finite
coefficient and remainder; growth, sign, physical-trajectory control,
composite mixing, continuum axioms and positive mass remain open.

### 6. Bounded full-coefficient growth attempt (2026-10-25)

This section organizes (7) for the approved logarithmic-growth test.
It proves neither that bound nor its failure. All source derivatives
below concern finite Gaussian polynomial moments; no differentiated
mesh-uniform Laplace remainder is asserted. The hypotheses and forest
slice remain exactly those above.

Index coordinates by a nonforest variable link and a color. Let D be
the unscaled oriented plaquette incidence matrix on these coordinates,
including all plaquettes and three colors. Thus S_2=x^T K x/2 with
K=D^T D>0. Put h_{\pm,p}=h_\pm(z_p) on 12-plaquettes and zero on
other orientations, and define

\[
K_\pm=D^T\operatorname{diag}(h_{\pm,p})D,\quad
K(s,t)=K-sK_--tK_+,\quad C(s,t)=K(s,t)^{-1}.
\tag{20}
\]

The weights are repeated over colors. For real s,t satisfying
(|s|+|t|)F<1, where F=\|f\|_\infty, the inequalities
0<=K_\pm<=F K imply K(s,t)>0. All following expressions are smooth
near (0,0) at fixed mesh. Use exactly the matrix jets (8) to define
symmetric tensors by

\[
\begin{aligned}
V(s,t;x)&=S_3-sb_{-,1}-tb_{+,1}
               =\tfrac16 T(s,t)_{ijk}x_ix_jx_k,\\
W(s,t;x)&=S_4-sb_{-,2}-tb_{+,2}
               =\tfrac1{24}U(s,t)_{ijkl}x_ix_jx_kx_l.
\end{aligned}
\tag{21}
\]

Repeated coordinate indices in this section are summed. Write
T(s,t)=T-sT_--tT_+ and U(s,t)=U-sU_--tU_+; the subscript tensors
are the derivatives of the corresponding insertion polynomials with
the displayed factorial conventions. No tensor projection is made.
Let E_{s,t} denote Gaussian expectation with covariance C(s,t). Then

\[
R(s,t)=\tfrac12 E_{s,t}[V(s,t)^2]
                  -E_{s,t}[W(s,t)]-E_{s,t}[M_2],
\qquad \kappa_a=\partial_s\partial_t R(0,0).
\tag{22}
\]

To verify this finite identity, absorb s b_{-,0}+t b_{+,0} into
the Gaussian in the formal source series (19). The remaining exponent
is -gV(s,t)-g^2(W(s,t)+M_2). Oddness gives E_{s,t}V=0, so the
coefficient of g^2 in its formal logarithm is exactly R(s,t). The
Gaussian normalization contributes no g^2 term. Taking the st
coefficient proves (22) by (19). Each specified coefficient uses
finitely many moments; no convergent moment generating function for
the cubic polynomial or source-asymptotic interchange is needed.
Differentiating the Gaussian expectation inserts the centered quadratic
b_{\pm,0}; differentiating V and W supplies the other insertion jets.
Thus both moving means and all seven terms of (7) are retained.

The cubic polynomial has no internal Gaussian contraction:

\[
T(s,t)_{ijk}C(s,t)_{ij}=0\quad\hbox{for every }k.
\tag{23}
\]

Indeed C(s,t)_{(e,c),(e',d)}=c(s,t)_{ee'}\delta_{cd}, because the
quadratic form is identical for the three colors. Every cubic trace
in (8) is proportional to the alternating tensor, since
Tr(t^c t^d t^e)=\epsilon_{cde}/4. Contracting any two color indices
with \delta makes it zero, regardless of edge indices. This argument
also covers repeated-edge terms and applies to each plaquette before
summing its weight. It proves (23) exactly.

For symmetric rank-three tensors A,B and symmetric matrices X,Y,Z set

\[
\mathcal B(A,B;X,Y,Z)=A_{ijk}B_{lmn}X_{il}Y_{jm}Z_{kn},\qquad
\mathcal U(U;X,Y)=U_{ijkl}X_{ij}Y_{kl}.
\tag{24}
\]

The first expression is symmetric in A,B and under permutation of
X,Y,Z; the second is symmetric in X,Y. Gaussian pairings give

\[
R(s,t)=\tfrac1{12}\mathcal B(T(s,t),T(s,t);C,C,C)
       -\tfrac18\mathcal U(U(s,t);C,C)
       -\tfrac1{12}\operatorname{Tr}C,\qquad C=C(s,t).
\tag{25}
\]

The constants can be checked from the Gaussian moment generating
function exp(z^T C z/2), whose derivatives pair coordinates. There
are three quartic pairings, giving 3/24=1/8. Two cubic vertices have
six pairings with all three legs crossing and nine with an internal
pair at each vertex. The latter vanish by (23); the former have
coefficient (1/2)(6/36)=1/12. Finally E M_2=Tr C/12. This finite
specialization is needed to keep the signed forest expression intact;
it does not reprove or invoke a lattice renormalization theorem.
All physical faces and variable normal links remain in D,T,U and C.

Evaluate everything henceforth at s=t=0 and set

\[
C_-=CK_-C,\quad C_+=CK_+C,\quad
C_{-+}=CK_-CK_+C+CK_+CK_-C.
\tag{26}
\]

These are the source derivatives of C, obtained by differentiating
K(s,t)C(s,t)=I. No entrywise positivity is assumed. Differentiating
(25) gives the complete signed family
\(\kappa_a=\mathcal K_3+\mathcal K_4+\mathcal K_H\), where

\[
\begin{aligned}
\mathcal K_3=\tfrac1{12}\bigl[&
2\mathcal B(T_-,T_+;C,C,C)
-6\mathcal B(T_-,T;C_+,C,C)
-6\mathcal B(T_+,T;C_-,C,C)\\
&+3\mathcal B(T,T;C_{-+},C,C)
+6\mathcal B(T,T;C_-,C_+,C)\bigr],\\
\mathcal K_4=-\tfrac18\bigl[&
-2\mathcal U(U_-;C_+,C)-2\mathcal U(U_+;C_-,C)\\
&+2\mathcal U(U;C_{-+},C)+2\mathcal U(U;C_-,C_+)\bigr],\\
\mathcal K_H={}&-\tfrac1{12}\operatorname{Tr}C_{-+}.
\end{aligned}
\tag{27}
\]

For the cubic term, derivatives can hit distinct tensors (two choices),
one tensor and one covariance (two times three choices for each
placement), the same covariance (three choices), or distinct covariances
(six choices). For the quartic term there is one tensor and two
covariances, giving its four displayed terms. The tensors are affine
in s,t, so no other term occurs. Equations (22) and (25) show that
(27) includes the entire coefficient. No gauge independence or separate
logarithmic bound for the individual \mathcal K terms is asserted.

Here is the estimate obtainable from the existing separated quadratic
input. Set P_\pm=C^{1/2}K_\pm C^{1/2}, so 0<=P_\pm<=F I. The
quadratic Gaussian covariance formula, with all three colors, gives

\[
q_a=\tfrac12\operatorname{Tr}(P_-P_+),\qquad
C^{-1/2}C_{-+}C^{-1/2}=P_-P_++P_+P_-.
\tag{28}
\]

The first identity follows from the two cross pairings in the
covariance of x^T K_-x/2 and x^T K_+x/2; the within-vertex pairing
cancels. With \|\cdot\|_{\rm HS} the Hilbert--Schmidt norm,

\[
\begin{aligned}
\|P_-P_+\|_{\rm HS}^2
&=\operatorname{Tr}(P_+P_-^2P_+)
 \le F\operatorname{Tr}(P_-P_+^2)
 \le F^2\operatorname{Tr}(P_-P_+)=2F^2q_a,\\
\|C^{-1/2}C_{-+}C^{-1/2}\|_{\rm HS}
&\le2F\sqrt{2q_a}.
\end{aligned}
\tag{29}
\]

The inequalities use P_\pm^2<=F P_\pm, multiplication inside a
positive trace, and cyclicity. They do not assume the P matrices
commute. By L003's convergence of q_a, the final bound is uniform
on all sufficiently large even meshes.

This does not yield the requested logarithmic bound. For example the
Haar term is bounded using (29) only by

\[
|\mathcal K_H|\le\tfrac F6\sqrt{2q_a}\,\|C\|_{\rm HS}.
\tag{30}
\]

No adequate estimate for this forest-coordinate norm or its
cancellations against the cubic and quartic contractions is established
here. Nor does (29) bound the internal tensors in (27). Terms with
C_- and C_+ on distinct contraction lines are not automatically
controlled by Tr(P_-P_+). Equation (30) is an insufficient upper
estimate, not evidence of divergence of the Haar term or the sum.

The precise open estimate is
\(|\mathcal K_3+\mathcal K_4+\mathcal K_H|\le C_0\log(eN)\)
for the entire signed expression (27), with C_0 independent of N.
The missing step is to combine its internal forest-coordinate
contractions before an absolute bound, or establish sufficient bounds
without changing the gauge law. This attempt neither excludes nor
establishes power growth. It is an exploratory organization and a
quadratic response estimate, not a resolution or a new growth lemma.

### 7. Integration-by-parts cancellation test (2026-10-25)

Keep the source domain and every finite matrix of section 6. This tests
cancellation in the full coefficient, not a new ultraviolet theorem.
All expectations in this section use C=C(s,t), and K=K(s,t).
The source variables are differentiated only after finite polynomial
Gaussian integration. In particular all changes of insertion means
remain included through (22).

Let the gradient run over all three colors of every nonforest link.
Equation (23) implies
\(\operatorname{Tr}(C\nabla^2 V)=0\); homogeneity gives
\(x\cdot\nabla V=3V\). Integration by parts against the Gaussian
has no boundary term, since its precision matrix is positive definite
and the amplitudes are polynomials. Applying it to V times its
C-weighted gradient gives

\[
 E[(\nabla V)^T C\nabla V]
 =E[V(x\cdot\nabla V-\operatorname{Tr}(C\nabla^2V))]
 =3E[V^2].                                             \tag{31}
\]

Thus the whole two-cubic contribution, including both differentiated
vertices and distinct covariance lines, can be retained as one quartic
expectation. This is a direct finite Gaussian identity; no new external
source or renormalization theorem is used.

There is also an exact integration-by-parts replacement for the Haar
term. Write x_e for the three-color vector at link e and set

\[
 A(s,t;x)=\frac1{60}\sum_{e\in E'_a}|x_e|^2
                    x_e\cdot(K(s,t)x)_e.
                                                               \tag{32}
\]

For a coordinate i, Gaussian integration by parts gives
\(E[(Kx)_i F]=E[\partial_i F]\). Taking
\(F=|x_e|^2 x_{e,c}\) and summing over c=1,2,3 gives
\(\sum_c\partial_{e,c}(|x_e|^2x_{e,c})=5|x_e|^2\).
Consequently E A=E M_2, including with the source-dependent covariance.
The coefficient therefore has the exact signed representation

\[
 \begin{split}
 P(s,t;x)&=W(s,t;x)-\tfrac16(\nabla V)^T C(s,t)\nabla V
                       +A(s,t;x),\\
 R(s,t)&=-E_{s,t}P(s,t;x),\qquad
 \kappa_a=-\partial_s\partial_t E_{s,t}P(s,t;x)\big|_{0,0}.
 \end{split}                                                   \tag{33}
\]

This absorbs the explicit Haar trace, but that operation alone is not
cancellation of its size. Indeed (32) has exactly its expectation for
every admissible source. Differentiating this equality gives
\(\partial_s\partial_t E A=\operatorname{Tr}C_{-+}/12\), the
same uncontrolled quantity as in (27), before combining the other
terms of P. The term containing C in (33) still has internal forest
covariance lines; differentiating it retains C_-, C_+ and C_{-+}.

A direct check on the actual Wilson jets rules out complete pointwise
annihilation of this effective quartic. Choose any nonforest variable
link e, set x_e=r u with a unit color vector u, and set every other
link coordinate to zero. Let
\(d_e(s,t)=\sum_{p\ni e}(1-s h_{-,p}-t h_{+,p})>0\).
Each incident plaquette has holonomy exp(plus or minus r u^c t^c).
Since its trace is 2 cos(r/2), its contribution to the fourth action
jet is -r^4/96 times its source weight. Thus W=-d_e r^4/96.
Every first coordinate derivative of a cubic jet on this configuration
is zero:
its two remaining nonzero color vectors would be parallel, and their
contraction with the alternating color tensor vanishes. This also
covers repeated-edge cubic terms. Finally the diagonal link block of
K is d_e times the three-color identity, so A=d_e r^4/60. Hence

\[
                  P(s,t;x)=\frac{d_e(s,t)}{160}r^4
                  \quad\text{on this configuration}.           \tag{34}
\]

This uses an actual link of the stated box, with every incident face
included, rather than a different one-plaquette measure. It excludes
the proposed pointwise-zero shortcut after (31)–(32). It does **not**
show that E P, its mixed source derivative, or any asymptotic leading
term is nonzero: other configurations and contractions can cancel.
In particular (34) is neither a lower bound on kappa_a nor evidence
of power divergence. Taking absolute values of P would again require
unproved internal covariance estimates and would discard signed
cancellations. The previously proved response estimate (29) supplies
none of those internal estimates.

The bounded attempt therefore establishes no logarithmic estimate,
no failure of that estimate, and no controlled residual of smaller
mesh order. The integration-by-parts identities and test are recorded
to prevent repeating this unsuccessful shortcut. After two exploratory
turns without a mesh estimate, direct contraction rearrangement is
parked. This is not a ban on the full coefficient or on a different,
independently justified representation; the original target and all
independent continuum/remainder gaps remain open.

## Mathlib

Coverage of the full fixed-mesh exact reflected specialization: **not
checked**. Coverage of the supporting high-order Laplace asymptotics,
SU(2) Haar-coordinate formula, finite polynomial cumulants and Gaussian
moment calculations: **not checked**. No full matching Mathlib theorem
or supporting theorem name/link has been inspected. The precise analytic
input is Kirwin's cited Theorem 2.1; L003 supplies the exact forest
reduction and quadratic curvature-law identification, and L011 supplies
the previously proved coordinate-density and connected-expansion
method. This is a reproduction/specialization of known finite-dimensional
mathematics, with no claim of progress beyond the sources checked.

Coverage of section 6's source-weighted tensor identities and
Hilbert--Schmidt response bound: **not checked**. They are proved there
from the finite inputs and Gaussian moments. No new external theorem
or Mathlib result is imported for the mesh-growth question.

Coverage of section 7's finite integration-by-parts identities and
Wilson-jet directional test: **not checked**. They are proved directly
above as part of an unsuccessful growth test, not as a new growth input.
