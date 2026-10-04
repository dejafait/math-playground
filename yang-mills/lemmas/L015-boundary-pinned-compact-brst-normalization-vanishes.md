# L015 — Boundary-pinned compact BRST normalization vanishes

## Hypotheses

Fix an even N >= 2, a = 8/N and the SU(2) lattice in [-4,4]^4.
Let V_int be its interior vertices, v = (N-1)^4, and E_rel its positively
oriented links not contained in the geometric boundary. Links contained
in that boundary are fixed to the identity; normal links touching it
remain variables. Thus the link manifold and allowed site gauge group are

\[
X=SU(2)^{E_{\rm rel}},\qquad
\mathcal G=SU(2)^{V_{\rm int}},\qquad
U^h_{xy}=h_x^{-1}U_{xy}h_y,
\tag{1}
\]

with h_x = 1 at boundary vertices. Integrate every compact group factor
with normalized Haar measure. For g > 0 use the Wilson action

\[
S_W(U)=\frac4{g^2}\sum_p\left(1-\tfrac12\operatorname{Tr}U_p\right).
\tag{2}
\]

Choose an anti-Hermitian basis t^a with -2 Tr(t^a t^b) = delta_ab and
[t^a,t^b] = f^{ab}{}_d t^d; its real structure constants are totally
antisymmetric. At each interior vertex introduce real b_x^a and
independent odd c_x^a, bar c_x^a, with c_x = c_x^a t^a. All these site
variables are zero at boundary vertices. Use the odd left derivation

\[
sU_{xy}=-c_xU_{xy}+U_{xy}c_y,\qquad
sc_x=-c_x^2=-\tfrac12[c_x,c_x]_{\rm graded},\qquad
s\bar c_x^a=i b_x^a,\qquad sb_x^a=0.
\tag{3}
\]

Define the globally smooth lattice Landau potential and its interior
gauge condition by

\[
\mathcal V(U)=-\tfrac12\sum_{e\in E_{\rm rel}}
 \operatorname{Re}\operatorname{Tr}U_e,\qquad
R_x^aF(U)=\left.\frac{d}{dt}F(U^h)\right|_{t=0},\quad
h_x=e^{t t^a},\quad h_z=1\ (z\ne x),\qquad
f_x^a=R_x^a\mathcal V.
\tag{4}
\]

Adding the fixed boundary links to the potential only adds a constant.
Put M_xy^{ab} = R_y^b f_x^a. For positive auxiliary width alpha > 0,
take the standard gauge fermion and its BRST-exact action

\[
\begin{aligned}
\Psi_\alpha&=-\sum_{x,a}\bar c_x^a
       (f_x^a+i\alpha b_x^a/2),\\
S_{{\rm gf},\alpha}=s\Psi_\alpha
 &=\tfrac\alpha2|b|^2-i(b,f)+(\bar c,Mc).
\end{aligned}
\tag{5}
\]

There are q = 3v ghost pairs. Let B be Berezin integration with any fixed
nonzero top-degree orientation, for example
B[product_j(-bar c_j c_j)] = 1. For a smooth gauge-invariant O on X define
the unnormalized functional

\[
I_\alpha(O)=\int_XdU\,e^{-S_W(U)}
 \int_{\mathbb R^q}db\,mathcal B
       [O(U)e^{-S_{{\rm gf},\alpha}(U,b,c,\bar c)}].
\tag{6}
\]

All compact gauge copies are retained with their Berezin determinant
signs. No logarithm chart, restricted-copy region, absolute determinant,
singular potential or BRST-breaking term is substituted.

The imported input is **Neuberger's vanishing theorem for standard
globally smooth compact lattice BRST gauge fixing**, as presented by
M. Testa, *Lattice Gauge Fixing, Gribov Copies and BRST Symmetry*,
[hep-lat/9803025v1](https://arxiv.org/pdf/hep-lat/9803025v1),
section 2, printed pp. 1–2, (1)–(9), especially (6)–(9).
Those equations give zero normalization and zero gauge-invariant
numerators for the invariant finite-dimensional integral with a
nonempty ghost sector and positive real auxiliary Gaussian width.
The original reference is H. Neuberger, *Nonperturbative BRS invariance
and the Gribov problem*, *Physics Letters B* 183 (1987), 337–340,
[DOI 10.1016/0370-2693(87)90974-9](https://doi.org/10.1016/0370-2693(87)90974-9).
Its original full text was not read; the precise usable argument is
Testa's inspected primary presentation. The prior SPECIALIZE assessment
is drafts/literature/2026-10-04-compact-brst-gauge-fixing-normalization.md.

## Conclusion

The integrals in (6) converge coefficientwise, but

\[
\boxed{I_\alpha(1)=0,\qquad I_\alpha(O)=0
       \quad\text{for every }\alpha>0,\ g>0.}
\tag{7}
\]

In fact, the gauge-fixing factor on each compact orbit also vanishes:

\[
z_\alpha(U):=\int_{\mathcal G}dh\int_{\mathbb R^q}db\,mathcal B
 [e^{-S_{{\rm gf},\alpha}(U^h,b,c,\bar c)}]=0.
\tag{8}
\]

Multiplying by finite nonzero auxiliary normalization constants does
not alter these zeros. Hence the standard smooth global prescription
cannot define a normalized Wilson expectation by division, or provide
the proposed nonlinear extension of L014. This is an application of
known mathematics, classified REPRODUCTION; no stronger no-go theorem
or result beyond the checked literature is claimed.

A zero-width Landau prescription would require a separate distributional
definition. The limit of the positive-width family above supplies no
nonzero normalization. No direct singular delta-function integral is
evaluated here. The statement does not obstruct the exact forest measure,
a local noncompact Gaussian, or a formulation with different gauge-fixing
hypotheses. It gives no estimate on the interacting reflected error.

## Proof

### Boundary domains and nonlinear algebra

Every boundary-contained link has both endpoints on the boundary, so
(1) fixes it and (3) gives sU = 0 there. A normal link is transformed
at its interior endpoint and stays an allowed SU(2) link. At a boundary
vertex c = bar c = b = 0 is preserved: sc = -c^2 = 0, s bar c = i b = 0
and sb = 0. No normal derivative condition on a continuum connection or
ghost is imposed by these finite site constraints.

Matrix multiplication uses the exterior algebra of the ghosts. Since
c_x^a c_x^b is antisymmetric, c_x^2 = (1/2)c_x^a c_x^b[t^a,t^b] is
again Lie-algebra valued. The left graded product rule gives

\[
s^2U_{xy}=-(sc_x+c_x^2)U_{xy}
                 +U_{xy}(sc_y+c_y^2)=0,\qquad
s^2c_x=-\bigl((sc_x)c_x-c_x(sc_x)\bigr)=0.
\tag{9}
\]

Nilpotence on b and bar c follows immediately. Thus the boundary
restriction retains the full nonabelian algebra, including the
quadratic ghost term; the free rule sc = 0 is not being used.

There are v = (N-1)^4 >= 1 independent interior site factors, hence
q >= 3. Both X and G are finite products of compact Lie groups without
manifold boundary. The space-time boundary reduces the number of
factors; it introduces no integration boundary into either product.
All plaquette traces are invariant under (1), including plaquettes
adjacent to the fixed boundary, so sS_W = sO = 0.

### Smooth gauge condition, action and convergence

Differentiating the outgoing link as -t^a U and the incoming link as
U t^a gives the explicit interior condition

\[
f_x^a(U)=\tfrac12\operatorname{Re}\operatorname{Tr}
 \left[t^a\left(\sum_{\mu=1}^4U_{x,x+a\hat\mu}
             -\sum_{\mu=1}^4U_{x-a\hat\mu,x}\right)\right].
\tag{10}
\]

All incident links in (10) are allowed variables, including the normal
ones ending on a boundary vertex. This real f and every required
derivative are globally smooth and bounded on X. Acting on a smooth
link function, sF = sum_y,b c_y^b R_y^b F. Thus sf_x^a = sum_y,b
M_xy^{ab}c_y^b. The graded rule applied to (5) gives its displayed
action: the b quadratic term has positive sign in S_gf, and the
Fourier factor in exp(-S_gf) is exp(i(b,f)). Nilpotence implies
sS_gf = 0. Neither a gauge-copy nondegeneracy assumption nor
invertibility of M on every configuration is needed.

Expand the finite exterior exponential coefficientwise. Each coefficient
of any product or derivative used in the cited theorem is a bounded
smooth function on the compact domain times a polynomial in b, with
modulus bounded by

\[
C(1+|b|)^k e^{-\alpha|b|^2/2}
\tag{11}
\]

for finite C,k at fixed N,g,alpha. This is integrable over R^q.
It justifies coefficientwise bosonic integration, the required
differentiations and vanishing auxiliary tails. Constants need not be
uniform in the mesh or in alpha -> 0. The same bounds apply on G
with U fixed. Degenerate Landau copies cause no failure of these
positive-width estimates.

### Invariant integration and cited theorem application

At each interior site the gauge vector fields on X are sums of left
and right invariant link vector fields. They have zero Haar divergence.
The ghost component is
sc_x^a = -(1/2)f^{bc}{}_a c_x^b c_x^c. Its Berezin divergence vanishes:
in sum_a partial_(c_x^a)(sc_x^a), every coefficient has a repeated
index in a totally antisymmetric structure constant. The antighost
component i b_x^a is independent of bar c_x^a, and there is no b
component. Together with (11) and the absence of group-manifold
boundaries, these are exactly the invariant integration hypotheses of
Testa's section 2.

Apply its zero-normalization and zero-numerator conclusion, (6)–(9),
to (6). The gauge condition is smooth globally, the action is BRST
exact, the gauge-invariant Wilson weight is smooth, the continuous
auxiliary width is positive, and q is nonzero. This proves (7)
by citation; no reproof of the parameter-deformation theorem or
Euler-characteristic identity is required.

For (8), apply the same cited result to Haar integration over G,
with fixed U as a parameter and gauge condition f(U^h). On this
manifold set sh_x = h_x c_x and keep sc_x = -c_x^2. Then s^2h_x = 0
and s(U^h)_xy = -c_x(U^h)_xy+(U^h)_xy c_y, so the preceding
algebra and smoothness checks apply verbatim. The h vector fields
are Haar invariant, the group is compact without boundary, and its
ghost sector is nonempty. This proves (8) by the same theorem.

The original Wilson normalization is strictly positive, since its
continuous density is positive on a compact product with positive
Haar mass. It is therefore the added BRST prescription, rather than
the Wilson measure, whose numerator and denominator give an undefined
ratio. A local Gaussian integrates over a different, noncompact
connection space; an exact forest slice uses a different global gauge
representation. Neither is a counterexample to the hypotheses above.
No physical-boundary Ward remainder, ultraviolet bound or positive
mass follows from this finite normalization obstruction.

## Mathlib

Coverage of the full boundary-pinned compact BRST normalization statement:
**not checked**. Supporting Haar-integration, finite exterior-algebra,
Gaussian domination and nonlinear BRST coverage: **not checked**.
No Mathlib theorem or absence is asserted. The precise external match is
Neuberger's theorem as presented in Testa's linked section 2; the
boundary-domain verification above is its applicability specialization.
