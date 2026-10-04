# L017 — The compensated forest free operator gives the existing Gaussian Ward response

## Hypotheses

Fix an admissible mesh and the SU(2) relative box of L003. Keep L008's
displacement, strains and two quadratic forms, L009's endpoint-averaged
generator V_a and one-color linearization K_a, and L010's Wilson-flow
probes at tau = 1/16. Use L016's boundary-rooted forest F and its
compensated slice generator. All roots and other boundary vertices are
pinned. No ultraviolet limit is taken in the calculation below.

Write d_0 for the relative differential from vertices to links and d_1
for that from links to plaquettes. Put L_a = d_1* d_1 and
Delta_a = L_a + d_0 d_0*. All cochain inner products have weight a^4.
Let I_F insert the remaining-link components, with zeros on forest links,
and let pi_F restrict to those components. Define the real path potential
and linear retraction, for one color, by

\[
(\Phi_F A)(v)=a\sum_{f\in\gamma_v}\epsilon_{vf}A_f,
\qquad \Phi_F A=0\quad\hbox{on the boundary},
\qquad R_F=1-d_0\Phi_F. \tag{1}
\]

Here gamma_v is the path from the fixed root to v, with the same signed
edge convention as L016. The sum need not be spatially local.

For the Gaussian calculation use L011's coordinate scaling theta = g x
on the remaining links: the connection is A = I_F x/a. Let D_1 = a d_1
be unscaled edge-to-plaquette incidence and put

\[
H_F=(D_1 I_F)^T(D_1 I_F),\qquad \Sigma_F=H_F^{-1}. \tag{2}
\]

The transpose in (2) is for ordinary stored link coordinates. For each
color let x have normalized density proportional to exp(-x^T H_F x/2),
and let the three colors be independent. Expectation for this forest
Gaussian is denoted E_F. It is the existing quadratic Wilson law, not
the nonlinear forest measure.

## Conclusion

The linearization of the compensated forest generator is

\[
k_F=\pi_F R_F K_a I_F,\qquad
I_F k_F=R_F K_a I_F,\qquad
\operatorname{Tr}k_F=\operatorname{Tr}K_a=0. \tag{3}
\]

Thus in the rescaled exponential coordinates its vector field is
k_F x + O_a(g) on bounded sets, including first coordinate derivatives.
The reduced diagonal entries need not vanish individually. The forest
Gaussian Ward insertion is

\[
\mathcal I_F^0(x)=\sum_{c=1}^3(x^c)^T H_F k_F x^c
                     -3\operatorname{Tr}k_F
=I^G_{V_a}\bigl((I_Fx^c/a)_c\bigr),
\qquad E_F\mathcal I_F^0=0, \tag{4}
\]

with exactly L009's insertion on the right. In particular the path
compensator changes no curvature action variation but cannot in general
be omitted from the reduced operator.

Let O^F_(i,a) be the leading, centered forest-coordinate coefficient of
L010's nonlinear probe, for i = 3,6. It is

\[
O^F_{i,a}(x)=\sum_c\left[
q_{i,a}\bigl(e^{-\tau L_a}I_Fx^c/a\bigr)
-E_Fq_{i,a}\bigl(e^{-\tau L_a}I_Fx^c/a\bigr)\right]. \tag{5}
\]

These probes agree pointwise with the restrictions of L008's Hodge-flow
Gaussian probes, including their centering. Their two Ward responses obey

\[
E_F[D O^F_{i,a}(x)[(k_Fx^c)_c]]
=\operatorname{Cov}_F(O^F_{i,a},\mathcal I_F^0)
=W^G_{i,a}. \tag{6}
\]

Consequently L009's existing equation W^G_a = C_a(1,1)^T + r_a and its
free residual limit apply unchanged. This supplies an explicit operator
compatible with L011's Hessian. It adds no estimate of its interacting
coefficient Gamma_(i,a), physical-boundary terms, or the matched reflected
error required to be <= c_box/2.

## Proof

### 1. Linear path reduction and its actual generator

Specialize the tree path-product reduction already used in L016; no new
general tree-gauge theorem is needed. The supporting primary map is
Freidel–Livine, [hep-th/0205268v2](https://arxiv.org/pdf/hep-th/0205268v2),
section 2.1, (2.1)–(2.8). Signed differences telescope on a path starting
at a pinned root, so Phi_F d_0 phi = phi for every relative zero-cochain.
Also, on a forest edge f=(x,y), the difference
Phi_F A(y)-Phi_F A(x) equals a A_f, including a negatively traversed
edge. Hence R_F A has zero forest entries. It changes no curvature since
d_1 d_0 = 0. If A already has zero forest entries, Phi_F A=0 and R_F A=A.
These facts prove that R_F is a projection onto the forest slice, with
kernel im d_0, and give the direct sum

\[
C^1_{\rm rel}=\operatorname{im}d_0\oplus\operatorname{im}I_F. \tag{7}
\]

For U_e=exp(g a A_e^c t^c), L009 gives
X_e=g a (K_a A)_e^c t^c+O_a(g^2). L016's slice path sum therefore has

\[
\omega_v=g(\Phi_F K_a A)(v)^c t^c+O_a(g^2).
\]

Its endpoint adjoint transport is the identity at leading order. Thus its
compensated coefficient on e=(x,y) is

\[
Y_e=g a\left[(K_a A)_e
 +\frac{\Phi_F K_a A(x)-\Phi_F K_a A(y)}a\right]^c t^c
 +O_a(g^2)
=g a(R_F K_a A)_e^c t^c+O_a(g^2). \tag{8}
\]

The derivative of the logarithm at the identity is the identity map.
After restricting to remaining links and dividing by g a, (8) proves
(3) in connection coordinates. Scaling x=a A changes no linear matrix.
Smooth finite products, inverses and the local exponential chart give the
stated bounded-set remainder and its first derivatives at this fixed
mesh. No uniform remainder as a tends to zero is asserted.

In particular, the path potential in (8) is Phi_F K_a A, not Phi_F A.
Differentiating a configuration-dependent gauge retraction before
restriction is essential. This is the tree-derivative retention discussed
in Ligterink–Walet–Bishop,
[hep-lat/0001028v1](https://arxiv.org/pdf/hep-lat/0001028v1), section 3.2,
(55)–(71), with the present pinned roots and generator conventions.

### 2. Trace and quadratic insertion

L009 proves K_a d_0=0. Relative to (7), K_a therefore has zero columns on
the gradient summand, and its diagonal block on the forest summand is
precisely pi_F R_F K_a I_F. Trace is invariant under this change of basis,
so Tr K_a = Tr k_F. L009's zero-diagonal full clover stencil gives the
last equality in (3). This argument does not claim a zero reduced
diagonal or a zero nonlinear divergence.

L003's positive quadratic form on the forest slice makes H_F positive
definite. Indeed its already established closed-cochain criterion shows
that D_1 I_F x=0 implies x=0. Substituting A=I_F x/a into the quadratic
action gives exactly x^T H_F x/2; no determinant from a second gauge
prescription is inserted. Since d_1 R_F=d_1, equation (3) yields

\[
(x^c)^T H_F k_F x^c
=\langle d_1(I_Fx^c/a),d_1K_a(I_Fx^c/a)\rangle_a. \tag{9}
\]

The factors of a agree: each differential contributes 1/a, each
connection x/a another 1/a, and the inner product contributes a^4.
Combining (9) with trace equality proves (4). Gaussian contraction gives
E_F[x^T H_F k_F x]=Tr(H_F k_F Sigma_F)=Tr k_F, so it also proves centering.

Integration by parts for the positive finite Gaussian, applied to a
polynomial O and the linear field k_F x, gives

\[
E_F[D O[(k_F x^c)_c]]
=E_F\left[O\left(\sum_c(x^c)^T H_F k_F x^c
                         -3\operatorname{Tr}k_F\right)\right]. \tag{10}
\]

All boundary terms vanish by polynomial Gaussian decay. Since (4) is
centered, the right side of (10) is its covariance with O. Neither
symmetry of k_F nor commutation with H_F is assumed.

### 3. Full flow, curvature law and the two responses

L010's linear Wilson flow is e^(-t L_a) on the full connection starting
on the slice. Flow is not restricted to remaining links. L003 splits
the Hodge Gaussian orthogonally into transverse and gradient parts, and
L009 gives L_a=Delta_a P_a, with P_a the transverse projection commuting
with Delta_a. On transverse cochains the two heat operators agree; on
gradient cochains L_a is zero and Hodge heat flow remains a gradient.
Therefore, for every full connection A,

\[
d_1 e^{-t L_a}A=d_1 e^{-t\Delta_a}A. \tag{11}
\]

Both q_(3,a) and q_(6,a) depend only on d_1 A by L008. Equation (11)
proves equality of their flowed polynomials pointwise. L003's already
proved equality of normalized forest and Hodge curvature laws makes their
centering constants equal. This proves (5) and identifies the actual
leading Wilson-flow probes, rather than assuming that forest heat flow
is exp(-t H_F/a^2).

The derivative of a gauge-invariant free curvature polynomial annihilates
every gradient direction. By (3), for either lifted probe O_(i,a),

\[
D O^F_{i,a}(x)[(k_Fx^c)_c]
=D O_{i,a}(A)[(R_F K_a A^c)_c]
=D O_{i,a}(A)[(K_a A^c)_c],\quad A^c=I_Fx^c/a. \tag{12}
\]

The factors 1/a in differentiating A account for the coordinate scaling
in the first equality. Since K_a annihilates gradients, the last
polynomial in (12) is itself gauge invariant. L003 therefore identifies
its forest expectation with its Hodge expectation W^G_(i,a). The same
curvature-law argument applies to (4) and their product with the probe.
Together with (10) this proves (6). Only quadratic-level gauge-invariant
polynomials are transferred in this proof; higher forest Taylor vertices
and their Haar-density correction remain those of L011.

For an explicit computation with that Hessian, write the one-color
flowed quadratic as x^T B^F_(i,a) x, with B^F symmetric, and set
M_F=(H_F k_F+k_F^T H_F)/2. The three-color contraction formulas are

\[
W^G_{i,a}=6\operatorname{Tr}(B^F_{i,a} k_F\Sigma_F)
=6\operatorname{Tr}(B^F_{i,a}\Sigma_F M_F\Sigma_F). \tag{13}
\]

They agree since Sigma_F M_F Sigma_F =
(k_F Sigma_F + Sigma_F k_F^T)/2. The factor 6 is two connected pairings
times three independent colors. This is a usable finite matrix form of
the existing response, not an additional cutoff limit or a computation
of an order-g^2 correction.

### 4. Finite checks, reuse and limits

Run `PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 python3 scripts/forest-ward/check_free.py`.
Exact rational arithmetic constructs the clover K_a and signed path map
on an N=4 relative box. For lower direction-1 and reversed upper
direction-2 forests, each with 81 tree links, it checks preservation of
every forest link, K_a d_0=0, total trace equality, and the independent
plaquette-boundary contraction d_1 I_F k_F=d_1 K_a I_F. Each forest has
six nonzero reduced diagonal entries and total trace exactly zero.

The subsequent numerical checks use the corresponding positive forest
and Hodge Hessians. Their curvature covariances agree within 1.8e-15;
Wilson and Hodge heat curvatures agree; the two nonzero sample flowed
responses and both sides of (13) agree within 9e-17. Omitting the path
terms gives maximum curvature-map discrepancies 3/80 and 1/24 in the
two samples. These checks use one-site rational displacement coefficients
and the same averaged-square/clover-product quadratic rules. They are
finite samples, not the original smooth u_a, exact Wilson expectations,
or evidence of a continuum bound. Steps 1–3 prove the comparison for the
original displacement and both specified probes at every admitted mesh.

This is REPRODUCTION of the assessed tree-gauge derivative mechanism and
the existing Gaussian quotient machinery. It supplies the missing
explicit operator and Hessian compatibility, without a claim beyond the
checked literature. L009's free residual and limiting coefficients are
imported unchanged. The nonlinear Haar divergence of L010/L016 need not
vanish; forest paths have no mesh-uniform locality or norm bound here.
Finite interacting matching, complete one-loop contraction, boundary
control and reflected error <= c_box/2 remain missing, as do continuum
field construction, full reflection positivity, infrared control and
finite positive mass. No complete candidate resolution is asserted.

## Mathlib

Coverage of the full compensated forest free comparison: **not checked**.
Coverage of supporting rooted paths, finite matrix traces, Gaussian
integration by parts and Hodge decomposition: **not checked**. No
Mathlib theorem name or direct library link is asserted. The linked
Freidel–Livine section 2.1 and Ligterink–Walet–Bishop section 3.2 results
support tree gauge reduction and retained derivatives; they do not state
this pinned generator/probe comparison. Its finite specialization is
proved above, reusing the existing local Gaussian results.
