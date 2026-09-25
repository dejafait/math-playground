# L006 — The complementary plaquette has one dimension-four bulk mixing channel

## Hypotheses

Work in pure SU(2) gauge theory with the trace normalization and Wilson coupling of L003 and L005. For the operator classification, consider real, gauge-invariant local polynomials in the connection curvature \(\mathcal F_{\mu\nu}\) and its covariant derivatives. Assign engineering dimensions \([\mathcal F]=2\), \([D]=1\), and \([g]=0\). Coefficients are independent of position. There are no matter fields, external tensors, boundary normals, inverse derivatives, or gauge-variant insertions in this class. We classify operators of dimension at most four before centering; a multiple of the identity has dimension zero.

Require covariance under the full hypercubic group \(H_4=(\mathbb Z/2)^4\rtimes S_4\), including independent coordinate reflections. The representation sought is that of diagonal traceless symmetric tensors: reflections act trivially on their component labels, permutations permute the four diagonal entries, and their sum is zero. The classification concerns homogeneous bulk counterterms. Applying it to the divergent part of an interacting lattice insertion would additionally require locality and power counting in that regulator; these analytic assertions are not hypotheses secretly asserting a constructed continuum limit.

For the lattice statements use the fixed cube, even meshes \(a=8/N\), relative boundary conditions, reflection, test \(f=f_*\), and constants of L005. A plaquette trace is unchanged on reversing orientation. At a vertex x with a full elementary neighborhood, let \(\mathcal C_{\mu\nu}(x)\) be the four unoriented elementary \(\mu\nu\) plaquettes having x as a vertex. Define

\[
\widehat h_{\mu\nu,a,g}(x)
=\frac1{g^2a^4}\sum_{p\in\mathcal C_{\mu\nu}(x)}
\bigl(P_p-\mathbb E_{a,g}P_p\bigr),
\qquad \widehat h_{\nu\mu}=\widehat h_{\mu\nu},
\]
\[
\widehat F^D_{a,g}(f)
=a^4\sum_x f(x)
\bigl(\widehat h_{12,a,g}(x)-\widehat h_{34,a,g}(x)\bigr).
\]

For sufficiently small a, every vertex with f(x) nonzero has this neighborhood inside the box. The sum may be restricted to those vertices. This is an average of plaquette traces, not the square of a clover-averaged curvature. Write \(\widehat Q^D_{a,g}\) for its reflected second moment and \(\widehat q^D_a\) for its quadratic Gaussian coefficient.

## Conclusion

The dimension-at-most-four bulk polynomial space contains exactly one copy of the diagonal traceless representation and none at dimension below four. Its three-dimensional space is

\[
V_-=
\operatorname{span}\{h_{12}-h_{34},\ h_{13}-h_{24},\ h_{14}-h_{23}\},
\qquad
h_{\mu\nu}=\frac1{2g^2}\sum_c(\mathcal F^c_{\mu\nu})^2.
\]

Every hypercubic-equivariant linear mixing map on the dimension-four polynomial space restricts to a scalar on V_- and has no component from V_- into another channel or the identity. Thus one coefficient is sufficient to parametrize the allowed bulk dimension-four matching of this multiplet, if such matching exists. The classification does not prove that the coefficient is finite, determine its value, or establish an interacting remainder estimate.

The site-centered lattice representative transforms exactly as this triplet. It has the exact smearing identity

\[
\widehat F^D_{a,g}(f)
=F_{12,a,g}(f_{12,a})-F_{34,a,g}(f_{34,a}),
\]
\[
f_{\mu\nu,a}(z)=\frac14\sum_{\epsilon,\eta=\pm1}
f\left(z+\frac a2(\epsilon e_\mu+\eta e_\nu)\right),
\qquad
\|f_{\mu\nu,a}-f\|_\infty\le\frac{a^2}{4}\|D^2f\|_{\mathrm{op},\infty}.
\]

In the quadratic law, its reflected coefficient differs by at most \(C_fa^2\) from the center-smeared coefficient of L005, for a finite constant independent of sufficiently small a. In particular,

\[
\lim_{g\downarrow0}\widehat Q^D_{a,g}(f)=\widehat q^D_a(f)
\quad\text{at fixed a},\qquad
\lim_{a\downarrow0}\widehat q^D_a(f)=q^D_{\rm box}(f)
\ge2c_{\rm box},
\]
\[
\widehat q^D_a(f)\ge c_{\rm box}>0
\quad\text{for all sufficiently fine even meshes}.
\]

These remain separated Gaussian statements in a fixed box. The O(a^2) assertion is not an estimate of the change in the interacting reflected form.

## Proof

### 1. Exhaust the polynomial candidates

The adjoint action of SU(2) on its three-dimensional real Lie algebra is the rotation action on \(\mathbb R^3\). A rotation-invariant linear functional is zero: invariance under the rotations by pi about each coordinate axis makes each coefficient zero. Thus a monomial with one curvature factor, or one covariant derivative of a curvature factor, cannot be a nonzero gauge-invariant polynomial. This includes \(\mathcal F\), \(D\mathcal F\), and \(DD\mathcal F\); all are adjoint-valued at the insertion point. Derivatives of constants vanish.

At dimension four, the only remaining possibility is two curvature factors with no derivatives. An invariant bilinear form on their color indices is a multiple of the Euclidean dot product. Indeed its matrix B satisfies \(R^{\mathsf T}BR=B\) for every three-dimensional rotation R. The rotations by pi about the coordinate axes eliminate off-diagonal entries, and rotations permuting coordinate axes equate the diagonal entries. This argument does not assume that B was symmetric. It leaves exactly \(\sum_c\mathcal F^c_e\mathcal F^c_{e'}\), with e and e' unordered coordinate planes. Products of linear color invariants vanish. Thus, apart from the identity, the entire candidate space is spanned by these 21 quadratic plane monomials.

Under a coordinate sign change \(s=(s_1,s_2,s_3,s_4)\), the curvature in plane \(e=\{\mu,\nu\}\) has character \(\chi_e(s)=s_\mu s_\nu\). A quadratic monomial with plane labels e,e' has character \(\chi_e\chi_{e'}\). This character is identically one if and only if e=e': otherwise reflect any coordinate in their symmetric difference. Since the representation sought has trivial reflection character, its image must lie in the span of the six squares \(h_e\). Averaging a putative image over the 16 reflections explicitly kills every other character. In particular, complementary cross products and pseudoscalar curvature contractions do not add another even channel.

The six squares are linearly independent polynomials: one may vary one curvature plane at a time. Such values can also be realized as curvature jets at a point by choosing a connection linear in the coordinates and zero at the point. No differential Bianchi relation imposes a pointwise linear relation among those squares. Below dimension four, only the constant remains. It transforms as a singlet and cannot form a nonzero diagonal traceless multiplet.

### 2. Prove multiplicity one, rather than only a tree decomposition

Let V be the six-dimensional real vector space with basis the plane squares. Let C exchange each plane with its complement. The negative eigenspace of C is exactly V_- in the conclusion. It has dimension three and is invariant under S_4.

Every matrix M on V commuting with S_4 has constant entries on the orbits of ordered pairs of planes. There are exactly three such orbits: equal planes, planes sharing one coordinate, and complementary planes. Therefore

\[
M=\alpha I+\beta A+\gamma C,
\]

where \(A_{e,e'}=1\) when e and e' share exactly one coordinate, and zero otherwise. If J is the matrix whose entries are all one, then \(A=J-I-C\). A complement-antisymmetric vector has coefficient sum zero, so on V_- we have

\[
C=-I,\qquad J=0,\qquad A=0,\qquad
M=(\alpha-\gamma)I.
\]

This proves both scalar action and absence of mixing out of V_- for an equivariant map on V. It also proves the statement for an equivariant map defined only on V_-: extend that map to V by composing with the equivariant projection \((I-C)/2\).

To identify this representation explicitly, let

\[
U=\{(k_1,k_2,k_3,k_4)\in\mathbb R^4:\sum_\mu k_\mu=0\},
\qquad
\Phi(k)=\sum_{\mu<\nu}(k_\mu+k_\nu)h_{\mu\nu}.
\]

Complementary coefficients have opposite signs. If all pair sums vanish, then all k_mu vanish, so Phi is injective and maps onto V_- by dimension. It is permutation-equivariant. The permutation representation on U is irreducible: in any nonzero invariant subspace choose a vector whose i and j coordinates differ; subtracting its image under (ij) produces a nonzero multiple of \(e_i-e_j\), whose permutation orbit spans U. Hence V_- is precisely the diagonal traceless triplet. The scalar-action argument shows that no second equivalent copy occurs in V. There is also no map to the constant representation: a permutation-invariant linear functional on U has equal coefficients and vanishes on its zero-sum subspace.

For the normalization, put \(s=\sum_e h_e\) and \(t_\mu=2\sum_{\nu\ne\mu}h_{\mu\nu}-s\). L004 identifies these as the bare diagonal stress components in the stated convention and proves

\[
h_{12}-h_{34}=\frac{t_1+t_2-t_3-t_4}{4}.
\]

The new assertion here is the exhaustive multiplicity and lower-dimension classification, not a repetition of that tree identity. Scalar and complement-even plane combinations cannot contaminate a hypercubic-covariant V_- insertion within this polynomial class.

### 3. A local lattice multiplet on one grid

A signed permutation of coordinate axes maps the four plaquettes through x in plane mu nu bijectively onto the four plaquettes through the transformed vertex in the transformed plane. Reversing orientation in this map leaves P_p unchanged. Thus \(\widehat h_{\mu\nu}\) transforms as the same six-plane permutation multiplet, with trivial sign action on component labels. Centering respects this covariance because the cubical Wilson measure and the identity boundary links are invariant under these signed permutations. Consequently its three complementary differences transform exactly as V_-. No assertion equating fields at two different plaquette centers is used.

The normalization agrees with the h variables at leading order. L005's fixed-mesh expansion gives \(P_p=g^2a^4\sum_c(B_p^c)^2/8+O(g^3)\) in canonical potential coordinates, so

\[
\widehat h_{\mu\nu,a,G}(x)
=\frac18\sum_{p\in\mathcal C_{\mu\nu}(x)}\sum_c
\bigl((B_p^c)^2-\mathbb E_G(B_p^c)^2\bigr).
\]

When evaluated on a smooth classical curvature as the mesh shrinks, the four terms tend to \(\tfrac12\sum_c(B^c_{\mu\nu})^2\), which is the canonical tree normalization of L004. This smooth-field observation is not an approximation to a typical interacting field.

For the exact smear identity, interchange the vertex and plaquette sums. Every plaquette p receives the four test values at its vertices, whose average is precisely \(f_{\mu\nu,a}(z_p)\). The coefficient \(1/g^2\) in the vertex sum becomes \(4/g^2\) multiplying that average, as required by the definition of F in L005. There is no surface term because f vanishes near the geometric boundary. Expectation subtraction is linear, so the identity holds for the centered insertions at every positive g.

Each displacement \(v=(a/2)(\epsilon e_\mu+\eta e_\nu)\) has squared length \(a^2/2\), and the four displacements sum to zero. Taylor's formula with integral remainder therefore gives the stated sup norm bound, since the remainder for each displacement is bounded by \(\|D^2f\|_{\mathrm{op},\infty}|v|^2/2\). The operator \(f\mapsto f_{\mu\nu,a}\) commutes with time reflection, including when the plane contains the time direction. This also gives the exact smear identity at the reflected insertion.

### 4. Symmetrization preserves the separated Gaussian lower bound

For a <= 1/2, f and the two averaged tests are supported in

\[
K'=[-1/2,1/2]^3\times[3/4,9/4].
\]

The reflected curvature kernels of both planes are uniformly bounded on K' times K', independently of sufficiently small a. Here is the needed extension of the kernel estimates, rather than an appeal to coincident-field control. In the magnetic mode formula of L003 and electric mode formula of L005, the spatial factors are uniformly bounded, the numerator frequencies are at most \(\Omega_{k,a}^2\), and

\[
\Omega_{k,a}\ge |k|/4,\qquad
\gamma_{k,a}\ge\Omega_{k,a}/2,\qquad
\frac{a}{\sinh(a\gamma_{k,a})}\le\frac1{\gamma_{k,a}}.
\]

The same sinh and cosh inequalities used there bound each mode by a constant times

\[
|k|\exp\bigl(-|k|(t+s)/8\bigr)
\le |k|e^{-3|k|/16}.
\]

The denominator factor \(1-e^{-16\gamma_{k,a}}\) is bounded below by \(1-e^{-2}\). Both three-dimensional mode sums converge absolutely under this common summable bound. The electric contact kernel still vanishes, since reflected and positive times are separated by at least 3/2. Thus there is a finite M such that \(|C^\theta_{e,a}(z,w)|\le M\) on the two relevant plaquette grids in K', for e=12,34.

For a test u on either grid write \(\|u\|_{1,a}=a^4\sum_z|u(z)|\). The total a^4-weight of the grid inside K' is uniformly bounded. The Taylor estimate implies

\[
\|f_{e,a}-f\|_{1,a}\le C_1a^2,\qquad
\|f_{e,a}\|_{1,a}+\|f\|_{1,a}\le C_2
\]

with finite constants independent of the mesh. The three-color centered Gaussian square identity now gives

\[
\begin{aligned}
|q_{e,a}(f_{e,a})-q_{e,a}(f)|
&\le\frac32 M^2\|f_{e,a}-f\|_{1,a}
\bigl(\|f_{e,a}\|_{1,a}+\|f\|_{1,a}\bigr)\\
&\le\frac32 M^2C_1C_2a^2.
\end{aligned}
\]

This follows by subtracting the two products of test values in the double sum; it does not estimate an ordinary variance.

L005 proves independence of the entire complementary Gaussian curvature families, so the mixed centered terms vanish for these different tests too. Hence

\[
\widehat q^D_a=q_{12,a}(f_{12,a})+q_{34,a}(f_{34,a}),
\qquad
|\widehat q^D_a-q^D_a|\le C_fa^2.
\]

The same fixed-mesh joint Laplace argument of L005 applies to these finitely many weighted sums and proves the asserted small-g limit. Finally L005 gives \(q^D_a\to q^D_{\rm box}\ge(3/2)d_{\rm box}^2=2c_{\rm box}\). The O(a^2) difference gives the same limit for the site-centered representative, and therefore its eventual lower bound c_box. This does not exchange the small-g and small-a limits.

### 5. What the matching-space result leaves unresolved

The [lattice stress-tensor source record](../foundations/05-lattice-stress-tensor-matching.md) supplies precedent for finite triplet renormalization, not a value or existence proof for the present matching factor. Symmetry permits an arbitrary scalar function of cutoff and coupling on V_-. It neither forces that function to be finite nor bounds higher-dimensional terms in reflected correlations. Gauge-variant contact identities and operators supported on the boundary are outside the bulk polynomial classification. Position-dependent tensors supplied by boundary geometry are also outside its hypotheses. Keeping the supports in the interior does not by itself prove their effects negligible.

For this symmetrized observable the quantitative comparison still required is, along a specified interacting trajectory and after justified matching,

\[
\left|\widehat Q^{D,\mathrm{matched}}_{a,g(a)}(f)
-\widehat q^D_a(f)\right|\le c_{\rm box}/2.
\]

The present result supplies no bound on this interacting difference. Nor does the O(a^2) test-function change imply a small interacting change: uniform control of the relevant separated correlations would be an additional input. Full limiting observables, reflection positivity on their entire algebra, the infrared limit, other gauge groups, and finite positive physical mass remain unconstructed.

The exact finite checks in `PYTHONDONTWRITEBYTECODE=1 python3 scripts/bulk-triplet-mixing/check.py` enumerate reflection characters and permutation orbits and check the triplet action and plaquette-center geometry. They support the finite algebra; they do not prove a renormalized lattice limit.

## Mathlib

Coverage of the full bulk classification and Gaussian symmetrization statement: **not checked**. Coverage of supporting invariant bilinear forms, finite group representations, Taylor bounds, Gaussian moments, and summable mode estimates: **not checked**. No inspected Mathlib theorem names or direct library links are asserted. The Giusti–Pepe citation is supporting physics literature with different regulator details, not a full match for this statement. The polynomial enumeration, multiplicity argument, lattice smear identity, and separated Gaussian estimate are proved above.
