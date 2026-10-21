# L127 — Common geodesy kills the four-branch normal-jet map

## Hypotheses

Retain the full conditional setting and notation of L126. In particular,
X=B x Y consists of the identical marked projective complex K3 surfaces
with common hyperkähler metric g, ordered structures I,J,K, real ample
class h and Omega=p_1^*h+p_2^*h. Normalize integral_S eta=1 and set
e_1=eta tensor 1 and e_2=1 tensor eta. The full integral mixed tensor
tau_D has self-adjoint cup operator D with
D[sigma]=2lambda[sigma], sigma=omega_J+i omega_K, and 1<lambda<5/4.
Suppose F is holomorphic locally free of rank two, Omega-slope-polystable,
with integral c_1(F)=0 and ch_2(F)=-14e_1-21e_2-tau_D.

Use L118's actual opposite map f:B -> M_H^s(2,0,-19), its common smooth
hyperkähler connection-moduli germ at z, and its normalized metric G.
Thus f^*G=2lambda g and its parametrized differential is parallel for
the ambient Levi-Civita connection and the original source connection.
L126 supplies the finite normalization nu:B -> Z of the reduced image.
Assume z has exactly four preimages b_i, whose distinct quaternionic
tangent lines span quaternionic dimension two. For I write V=T_zM,
dim_C V=78, U=sum_i im L_i of complex dimension four, and
L_i=df_{b_i}:V_i=T_{b_i}B -> U. Use L126's W_2, E_2, C_2 and Nbar.
Neither F existence nor occurrence of this collision is asserted.

## Conclusion

The actual map Nbar:U^ann -> C_2 is zero. Consequently the actual
algebraic normalization quotient has length

\[
 \operatorname{length}_{\mathcal O_{Z,z}}
       ((\nu_*\mathcal O_B)_z/\mathcal O_{Z,z})
       =7+\dim C_2
       =\begin{cases}
          10,& A=t\,\mathrm{id},\quad t\in\mathbf R\setminus\{0,1\},\\
           9,& A\text{ is not scalar},
         \end{cases}                                      \tag{1}
\]

Here A is L126's fourth tangent graph after the other three tangents
are made the two axes and diagonal. This is a conditional
REPRODUCTION/specialization of known connection and normal-coordinate
tools. The separate critical audit below preserves it. It evaluates the local defect,
without excluding or producing a collision, constructing F, computing
a global defect, supplying a cycle or transverse transport, or resolving
universal primitive rational Hodge realization.

## Proof

**Scope and known tools.** Reuse the pre-invocation SPECIALIZE assessment
`drafts/literature/2026-10-18-four-branch-geodesic-normal-jets.md`.
The general finite-order holomorphic coordinate tool is imported from
Higashijima--Itou--Nitta, *Normal Coordinates in Kähler Manifolds and the
Background Field Method*, hep-th/0203081v3 (17 June 2002),
[Section 3.1, equations (3.1)--(3.3), (3.7), PDF pp. 7--9, and Appendix A](https://arxiv.org/pdf/hep-th/0203081v3#page=7).
At quadratic order the torsion-free Kähler connection admits
holomorphic coordinates with Christoffel symbols zero at the centre.
Only this finite-order statement for a smooth Kähler metric is used;
no convergence of infinite normal-coordinate expansions is needed.
The inspected stronger submanifold compatibility in Jentsch--Weingart,
*Riemannian and Kählerian normal coordinates*, Asian J. Math. 24 (2020),
369--416, Corollary 4.9, pp. 391--392, is not needed. In particular,
no assertion that an arbitrary smooth Kähler metric is real analytic
is imported. L118 supplies geodesy; L126 supplies coordinate invariance
and the entire normalization-length formula. None is reproved here.

**One ambient connection and the full Hessians.** Take one holomorphic
ambient chart w=(w^1,...,w^78) centred at z in the common germ, and
independent holomorphic source charts u=(u^1,u^2) centred at b_i.
Choose their linear parts to realize the given tangent bases. The
actual analytic branch maps are holomorphic, hence have expansions

\[
 f_i(u)=L_i u+Q_i(u)+O(|u|^3),\qquad
             Q_i(u)=\tfrac12 d^2f_i(0)(u,u).              \tag{2}
\]

Let Gamma_M:Sym^2 V -> V be the bilinear array of ambient Christoffel
coefficients at z in this chart, and Gamma_i:Sym^2 V_i -> V_i the
source array at b_i for nabla^g in its chosen chart. For a Kähler
metric the Levi-Civita connection preserves type, so these arrays
are complex bilinear in the (1,0) tangent slots; torsion-freeness
makes them symmetric. Their coefficient functions need only be smooth.
No holomorphicity of the connection coefficients is assumed.

Complexify L118's real parametrized geodesy identity and evaluate it
on the holomorphic coordinate fields partial_a, partial_b at b_i.
The coordinate formula for that identity, in each ambient component
alpha, is

\[
 \partial_a\partial_b f_i^\alpha(0)
  +\sum_{\beta,\gamma}\Gamma^\alpha_{M,\beta\gamma}(z)
        (L_i)^\beta_a(L_i)^\gamma_b
  =\sum_c(L_i)^\alpha_c\Gamma^c_{i,ab}(b_i).
                                                               \tag{3}
\]

There is no derivative of Gamma_M in this second-jet identity. The
same array Gamma_M occurs for all four branches because their values
are the same point z in the same connection chart. The pullback metric
scale is the fixed positive constant 2lambda; its Levi-Civita connection
is nabla^g, precisely the source connection in L118. Thus no scale
factor or extra second fundamental form belongs in (3). Contracting
the two source slots with u and using (2) gives the full vector identity

\[
       2Q_i(u)=L_i\Gamma_i(u,u)-\Gamma_M(L_i u,L_i u).
                                                               \tag{4}
\]

**Passage to the annihilator quotient.** Fix ell in U^ann. Since every
image of L_i lies in U, applying ell to (4) kills the entire source
connection term, even though the four Gamma_i may differ. Define the
single homogeneous quadratic polynomial on U

\[
             P_\ell(v)=-\tfrac12\ell(\Gamma_M(v,v)).       \tag{5}
\]

Then for each i, ell(Q_i(u))=P_ell(L_i u). The tuple of these four
quadratics lies in E_2 by its definition as the common tangent
restriction image. Its class in C_2=W_2/E_2 is therefore zero. This
proves Nbar(ell)=0 for every ell and hence rank Nbar=0. It retains
both the source terms and the factor between Hessian and Q_i until
their disposition is justified.

Equivalently, the imported finite-order holomorphic normal coordinates
can make Gamma_M zero at z in one chart for all branches. Equation (4)
then makes Q_i tangent to im L_i, which U^ann annihilates. This is
consistent with (5), without a simultaneous full holomorphic
linearization claim or a replacement of holomorphic coordinates by
real exponential coordinates. The direct calculation (3)--(5) is the
needed applicability argument, not a reproof of a general normal-
coordinate or totally-geodesic theorem.

**Formal comparison and algebraic length.** For a smooth complex
algebraic germ, a holomorphic chart gives formal coordinates on its
completed complex local ring: choose algebraic regular parameters,
expand the holomorphic chart in them, and apply the formal inverse
function theorem to its invertible linear part. The same holds on
each smooth source branch. Taylor expansion of these actual maps
therefore gives exactly permissible formal branch coordinates in
L126, with the same second coefficients (2). Only this finite Taylor
jet and its invertible linear part are used. No convergence of a
formally constructed infinite normalization is involved. L126's
coordinate-independence argument identifies Nbar under these changes;
vanishing thus holds also in its original formal coordinates.

Apply L126's already audited length formula with s=0 and its exhaustive
tangent ranks dim C_2=3 or 2. This gives (1) for the actual algebraic
quotient, using its complete cubic tail and exact finite-module
completion descent. Those arguments remain in L126; a jet preview
alone is not being used to infer an algebraic length here.

The arbitrary complex branch examples in L126 with s>0 cannot obey
the common parametrized geodesy used in (3). Their relaxed conclusions
and the independent stops in ATTEMPTS/070--072 are preserved. This
local calculation supplies no global defect identity or exclusion,
and leaves F existence, collision occurrence and transport unresolved.

**Separate critical audit, 2026-10-18 (step 383).** Reuse the pre-existing
SPECIALIZE assessment
`drafts/literature/2026-10-18-four-branch-geodesic-jet-critical-audit.md`.
The full proof above, L118's parametrized identity and common-germ
comparison, and L126's completed audit have been checked. No
load-bearing error or stronger conclusion was found. In particular:

1. **The connection is common to the four actual maps.** L118 compares
   the algebraic coarse germ with the connection germ using an actual
   stable slice family and the natural deformation map. Its metric
   normalization is independent of the parameter and of the scalar
   choice of a stable fibre metric: the scalar cancels in End, and
   unitary gauge preserves trace. Hence four source neighborhoods
   mapping to z can all be compared in one target chart with one
   connection. They are not four independently rescaled target germs.
   L118's identity (4) is precisely parallelness of the differential
   for that connection and the original source connection. Multiplying
   g by the constant 2lambda does not change its Levi-Civita connection.

2. **Complexification and the Hessian.** The tensor nabla df is zero
   on real tangent vectors, so its complex-bilinear extension is zero
   on the two (1,0) coordinate fields as well. Holomorphicity of f_i
   makes their images (1,0); the Kähler connections preserve that
   subbundle. With coordinate fields on the source, its components
   are exactly partial_a partial_b f_i plus Gamma_M(L_i partial_a,
   L_i partial_b) minus L_i Gamma_i(partial_a,partial_b).
   The connection rule is evaluated once at the point; it contains
   no derivative of Gamma_M and needs no holomorphic connection
   coefficients. Torsion-freeness gives symmetry. The homogeneous
   quadratic Taylor term is half the Hessian, so contracting the
   identity gives (4) with the displayed factor two and signs.

3. **The full source terms disappear only after annihilation.** For
   ell in U^ann, L_i Gamma_i(u,u) belongs to im L_i, hence is killed
   for every i regardless of its source coefficients. The remaining
   polynomial is the restriction of the single element
   -ell(Gamma_M(v,v))/2 of Sym^2 U^*. Gamma_M is allowed to take
   values outside U; applying ell first gives a scalar quadratic
   on U. Thus no curvature-invariance or connection-invariance of
   U is assumed. Its four restrictions are in E_2 by definition,
   so their class is zero in C_2. This checks Nbar on its entire
   domain, not merely a selection of normal coordinate functions.

4. **The analytic jets belong to the actual completed pullback.**
   Choose algebraic regular parameters x at z and t_i at b_i.
   Their differentials are bases, so their analytifications are
   holomorphic local coordinates by the inverse function theorem.
   In these coordinates the algebraic morphism has convergent
   component germs x composed with f_i. Their Taylor series are
   exactly the images of x under the completed algebraic local-ring
   map. Indeed this is true for each generator and hence for
   polynomials and their limits in the maximal-ideal topology.
   Any chosen analytic ambient chart w has a convergent expression
   w(x) with invertible linear part, and likewise u_i(t_i) on each
   source. Taylor series give invertible formal changes of variables
   in the completed rings. Taylor expansion commutes with these
   compositions (each coefficient depends on finitely many terms).
   Consequently the four analytic expansions in (2) are the same
   completed branch pullbacks expressed in permissible coordinates.
   This identifies the maps, not just abstract power-series rings.
   L126's invariance then applies: source quadratic changes contribute
   im L_i and ambient changes contribute a common quadratic restriction.
   Neither real exponential coordinates nor convergence of a formal
   normal-coordinate construction enters this comparison.

5. **The numerical lengths use the whole quotient.** L126 identifies
   the completed actual normalization algebra with exactly four
   smooth branch factors. Its complete filtered lifting gives
   rho(m^3)=product_i n_i^3, so every higher branch term has already
   been accounted for. The remaining target dimension is 24; the
   constant and linear image has rank 1+4, and the remaining image
   rank is dim E_2+rank Nbar. With rank Nbar=0 this gives
   24-5-dim E_2. L126's two exhaustive tangent ranks are 9 when
   A is real scalar and 10 otherwise, yielding respectively 10
   and 9. Its faithful-flat descent and closed-fibre length one
   identify these with the lengths of the original finite algebraic
   quotient, rather than merely dimensions of a truncated preview.

This is RESEARCH / REPRODUCTION / EXPLORATION: confirmation of an
existing conditional specialization, not a second mathematical advance
or a result beyond the inspected sources. The direct mathematical
inputs remain L118 and L126. The latter retains finite normalization
and distinct tangents from L120 and L121. No new lemma, graph edge or
mathematical script is required. The arbitrary complex branch models
of L126 do not satisfy the common geodesy identity when Nbar is nonzero;
they are not counterexamples to the present hypotheses. ATTEMPTS/070--072
remain intact. F existence, collision occurrence, global defect
consequences, transport and universal primitive Hodge realization remain
unresolved. No simultaneous all-orders holomorphic linearization has
been proved or used by this audit.

## Mathlib

Full matching coverage for this common-connection normal-jet
specialization and the resulting actual-image lengths is **not checked**.
Unknown coverage is not evidence of absence. The Kähler coordinate
tool is cited above, and the conditional geometric and algebraic
inputs remain L118 and L126. No Lean or numerical verification is claimed.
