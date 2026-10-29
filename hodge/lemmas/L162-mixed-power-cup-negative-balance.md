# L162 — The mixed first/second-power cup has the cancelling sign

## Hypotheses

Retain exactly L161's conditional geometric data: identical marked
projective K3 factors X=S_1 x B with the common hyperkahler metric g,
ordered triple (I,J,K), Kahler class h and full tensor tau_D; preferred
dual HE lines L,L_B with k=(-4,-2,1,2), k.h=0, k^2=-14 eta,
integral_S eta=1 and Dk=4k. Write e_1=eta tensor 1, e_2=1 tensor eta
and P=e_1e_2. The hypothetical locally free rank-two F is
Omega-polystable, Omega=h_1+h_2, has integral c_1(F)=0 and

    ch(F)=2-14e_1-21e_2-tau_D+62P.

Use L071's actual compatible connection, L147's ordinary images
M=R^1p_{2*}(F tensor p_1^*L^{-1}) and W=R^2p_{2*}(F tensor p_1^*L^{-1}),
and L157's full line multiplicities m_t and opposite transforms.
M is locally free and h-polystable; W is one residue field at each
point of the finite set Z, with 0<=z=|Z|<=119. Retain L160's actual
positive middle sheaf E_+ and its unevaluated connecting map:

    0 -> E_+ -> M^vee --delta--> W^dagger -> H^2(P_+) -> 0,
    P_+=Rp_{2*}(F tensor p_1^*L),
    W^dagger=mathcal Ext^2_B(W,O_B).

Set T_(e,d)=p_1^*L^e tensor p_2^*L_B^d, Q_s=F tensor T_s and
V_s=H^1(X,Q_s). All product metrics and connections are the specified
tensor/dual ones. Fix the single parallel unit determinant wedge A
of L159. Let R_s be its anti-linear harmonic opposite operator on V_s,
as applied with W retained in L160 and L161. Put

    s=(-1,-1), t=(-1,-2),
    sigma_i=omega_J+i omega_K on factor i,
    x=[bar(sigma_1)], y=[bar(sigma_2)] on X,
    Vol_1=Vol(S_1), Vol_2=Vol(B).

No existence of F, nonempty Z, vanishing of delta, or multiplicativity
of harmonic representatives is assumed.

## Conclusion

For nonzero v in V_s and w in V_t, write the actual opposite cups as

    C(v,R_s v)=f_v x+g_v y, C(w,R_t w)=f_w x+g_w y.

All four coefficients are strictly negative real by L160/L161.
Let beta_h be the harmonic representative of C(v,w) in
H^2(X,T_(-2,-3)). Then the actual mixed product is

    C(v,w) C(R_s v,R_t w)
      = - ||beta_h||^2_L2 / (4 Vol_1 Vol_2) xy.          (1)

The three-plus-sign polarized identity therefore reads

    ||beta_h||^2_L2 / (4 Vol_1 Vol_2)
       = f_v g_w+g_v f_w > 0.                          (2)

Thus this bounded mixed-cup sign test produces cancellation, not the
proposed exclusion m_1*m_2=0. Under coexistence it requires a nonzero
actual mixed cup. It does not prove coexistence is realizable, assign
that cup, or show that all geometric constraints are compatible.
This NEGATIVE / REPRODUCTION specialization changes the route decision:
park the proposed exclusion by this sign test. The separate critical
audit below preserves this verdict. It gives no bound on z, lower comparison, F construction,
other-stable-type exclusion, transport or universal Hodge realization.

## Proof

**Scope and sources.** Reuse the invocation-start SPECIALIZE assessment
`drafts/literature/2026-10-25-mixed-first-second-power-cup-sign.md`.
Its exact target was the mixed determinant-cup test above. A possible
exclusion would restrict same-sign line coexistence in the hypothetical
kernel's middle image, while leaving the independent global gaps open.
The stopping criterion also permits an identified failed comparison or
cancellation. ATTEMPTS/069,/089,/090 remain valid; none of their finite
relaxations is rerun. The result is a local specialization of inspected
tools, not a claim of progress beyond those sources or originality.

For harmonic preservation use Verbitsky, *Hyperholomorphic bundles over
a hyperkahler manifold*, [alg-geom/9307008v1, 29 July 1993](https://arxiv.org/pdf/alg-geom/9307008v1),
Section 4, Propositions 4.2-4.3, Theorem 4.1 and Corollary 4.3,
PDF pp. 14-16, and the doubled-dual proof of Theorem 4.2.A, p. 17.
Use its harmonic operator only, not a scalar-ring assertion or an
endpoint-injection assertion. The compact product and the actual
invariant-curvature connections satisfy its hypotheses by L071/L157.
The coefficient line used below is hyperholomorphic; its sum with its
dual has the parallel Hermitian-exchange real structure. The triple
(-I,J,-K) gives the ordinary (0,q) convention, as checked in L159.

For coefficient Hodge theory and Serre integration use Demailly,
*L2 vanishing theorems for positive line bundles and adjunction theory*,
[alg-geom/9410022v3, 28 February 1995](https://arxiv.org/pdf/alg-geom/9410022v3),
Section 4.A (4.3)-(4.4'), pp. 27-28. The bases are compact Hermitian
and all coefficients here are locally free. For the actual Dolbeault
product and its signs use Section 1.A (1.1)-(1.3), pp. 4-5, and
[Stacks Lemma 20.31.3, 0FP3](https://stacks.math.columbia.edu/tag/0FP3)
and [15.59, 0GWN](https://stacks.math.columbia.edu/tag/0GWN).
For line-valued Kunneth use
[Stacks Lemma 36.23.1, 0FLN](https://stacks.math.columbia.edu/tag/0FLN):
the projective factors are quasi-compact and quasi-separated and
Tor-independent over Spec(C), an affine base. The lines are locally
free, so these actual derived/coherent cups are covered. No general
Hodge, duality or Kunneth theorem is reproved; the representative and
sign calculations below are the difference not supplied by a citation.

**Classes and targets with W retained.** L160 identifies dim V_s=m_1,
and L161 identifies dim V_t=m_2. Their forward degree-one edges are
H^0(M tensor L_B^{-1}) and H^0(M tensor L_B^{-2}); W is retained in
degree two. The opposite transforms are independently concentrated.
For the positive partners E_+ embeds in M^vee and agrees with it off Z.
Thus nonzero sections are detected off Z in the forward direction and
on some fibre in the opposite direction. These are precisely the
actual edges used in L160/L161, including the unevaluated delta, so
their independently strict two-trace inequalities apply to v and w.
Neither W=0 nor a perfect section pairing at positive z is imported.

Order the four inputs as (v,R_s v,w,R_t w). Their weights are
(-1,-1),(1,1),(-1,-2),(1,2). L157 gives zero endpoints for every
nonzero line power and h^1(L^n)=7n^2-2, on either factor; O has
cohomology dimensions (1,0,1). Kunneth gives all six pair targets:

| Cups | Target weights | Degree-two target |
| --- | --- | --- |
| C_12, C_34 | (0,0), (0,0) | Cx+Cy for each |
| C_13, C_24 | (-2,-3), (2,3) | H^1(L^(-/+2)) tensor H^1(L_B^(-/+3)) |
| C_14, C_23 | (0,1), (0,-1) | zero for each |

The two mixed targets each have dimension (28-2)(63-2)=26*61=1586.
For (0,+/-1), every degree-two Kunneth summand vanishes: the nonzero
power has zero endpoints and H^1(O)=0. In particular the mixed
targets cannot be discarded by the equal-power adjacent-target test.
All three pair partitions have total weight zero and land in Cxy.

**Raw opposite product and harmonic correction.** Let alpha and gamma
be the unique harmonic representatives of v and w, and put
beta=A(alpha wedge gamma), a closed T_u-valued (0,2)-form, u=s+t.
For a line coefficient use its anti-linear Hermitian isometry
tau_u:T_u -> T_-u. Define on its degree-two forms

    S_u(l tensor a)=tau_u(l) tensor J(bar(a)),           (3)

where J acts exteriorly. This balanced map is anti-linear, isometric
on forms and in L2, and S_-u S_u=Id since J^2=+Id in degree two.
The doubled-dual harmonic theorem just cited implies S_u takes the
harmonic space onto its opposite-coefficient harmonic space. This is
not an assertion that S_u commutes with bar-partial on arbitrary forms.

In unit determinant frames write alpha=f_1 a+f_2 b and
gamma=f_1 c+f_2 d, keeping their separate unit line frames implicit.
L159's coefficient opposite is r(f_1)=f_2, r(f_2)=-f_1, with line
duality. If j(a)=J(bar(a)) on one-forms, direct calculation gives

    beta=a wedge d-b wedge c,
    A(R_s alpha wedge R_t gamma)
      =j(a) wedge j(d)-j(b) wedge j(c)=S_u beta.         (4)

Thus the coefficient determinant contributes plus conjugation, with
no extra minus. Both sides of (4) are closed, since both opposite
forms are harmonic. This proves closedness of S_u beta in this
specific case without a cochain-commutation assumption.

Let H_u denote orthogonal harmonic projection. An anti-unitary map
that bijects harmonic subspaces also bijects their orthogonal
complements: inner products are conjugated, so orthogonality is
preserved in both directions. Consequently

    H_-u S_u beta=S_u H_u beta=S_u beta_h.             (5)

Coefficient Hodge theory for a closed form says beta-beta_h is
bar-partial exact. By (4)-(5), S_u beta-S_u beta_h is also exact,
because S_u beta is closed and (5) is its harmonic projection.
This does not apply S_u to a primitive for the first exact term.
It follows that C(R_s v,R_t w) is represented by S_u beta_h,
and their cohomology product is represented by beta_h wedge S_u beta_h.
Replacing either closed factor by an exact correction changes this
product by an exact form, hence has zero Serre integral. No wedge
of harmonic forms has been assumed harmonic.

**Harmonic bidegrees and the normalized sign.** For the external line
T_u with its product metric, exterior products of harmonic factor
forms are harmonic: on a factor-bidegree (p,q) the Dolbeault operator
is dbar_1+(-1)^p dbar_2 and its adjoint has the corresponding graded
formula. Expanding their anticommutator cancels the cross terms,
leaving Delta_1 tensor 1+1 tensor Delta_2. The harmonic external
products therefore realize the cup-defined Kunneth isomorphism.
Their dimensions equal the cohomology dimensions, so uniqueness of
harmonic representatives shows they span the full harmonic space.
For u=(-2,-3) only factor bidegree (1,1) survives. Thus beta_h has
one anti-holomorphic covector from each factor at every point.

Use L159's oriented unit coframes. Write e_1,e_2 for the two (0,1)
unit covectors on S_1 and d_1,d_2 for those on B, and E=e_1 wedge e_2,
D=d_1 wedge d_2. In this paragraph these are covectors, not the
topological classes e_i in the hypotheses. Then

    j(e_1)=-e_2, j(e_2)=e_1,
    e_a wedge j(e_c)=-delta_ac E,
    d_b wedge j(d_d)=-delta_bd D,
    bar(sigma_1)=2E, bar(sigma_2)=2D.

In a unit frame l of T_u write beta_h=sum z_ab l e_a wedge d_b.
The opposite line frame evaluates against l to one. In the product
with (3), moving d_b past j(e_c) contributes minus. Hence

    beta_h wedge S_u beta_h
      =-sum_(a,b,c,d) z_ab bar(z_cd)
           (e_a wedge j(e_c))(d_b wedge j(d_d))
      =-sum_(a,b)|z_ab|^2 E wedge D
      =-(|beta_h|^2/4) bar(sigma_1) wedge bar(sigma_2).  (6)

The first minus is essential: the two negative surface pairings
alone would give the wrong sign. The product metric makes these
mixed wedge basis vectors orthonormal, so the sum is the full norm.

Normalize the H^4(O_X) coefficient by integrating against
sigma_1 wedge sigma_2. Since sigma_i wedge bar(sigma_i)=4 dvol_i
and the factor two-forms have even degree, the denominator is

    integral_X bar(sigma_1) bar(sigma_2) sigma_1 sigma_2
        =16 Vol_1 Vol_2 > 0.

The numerator from (6) is -4 integral_X |beta_h|^2 dvol_X.
The analytic/Serre normalization cancels in the ratio. Equations
(4)-(6) prove exactly (1), with all coefficient evaluation and
orientation signs fixed by the same conventions as L160/L161.

**Quartic balance and the stopping verdict.** L158's local polarized
identity applies to these changed line weights without its z=0
concentration assumption: the rank-two self-cup is locally 2a wedge b,
its square is zero, and polarization gives all three pair partitions
with coefficient +8. The lines have equal total weight, so it glues
and passes to the actual cohomology cups by the cited comparison.
It yields

    C_12 C_34+C_13 C_24+C_14 C_23=0.

The last term vanishes by the checked targets. The first term is
(f_v g_w+g_v f_w)xy, strictly positive in this normalization; the
second is (1), nonpositive. Since xy is nonzero, their sum gives
(2). In particular beta_h cannot be zero when v,w are nonzero.

There is no sign contradiction: the required cancellation has exactly
the sign furnished by the actual harmonic opposite. This does not
choose a norm or cup value independently; (2) is a necessary identity
for hypothetical actual classes. Additional constraints might exclude
coexistence, but none is supplied by this bounded test. Park this
mixed sign exclusion and preserve the earlier finite-relaxation stops.
No numerical computation or mathematical script is needed.

**Separate critical audit — 2026-10-25, step 535.** This is
RESEARCH / EXPLORATION / REPRODUCTION, actual task proof_audit, under
the invocation-start SPECIALIZE assessment
`drafts/literature/2026-10-25-mixed-power-cancellation-critical-audit.md`.
The audit finds no substantive error and proves no stronger conclusion.
It checks the previously unverified mixed-cup specialization, rather
than certifying originality or assuming compatibility of a kernel.

The complete L162 proof and audited L161 were read, together with
L159's operator and trace comparison, L160's W-retaining edges, and
the relevant actual-connection, ordinary-image, full-multiplicity and
polarized-cup passages of L071, L147, L157 and L158. The source coverage
is reused; the degree-independent primary operator case was checked
directly in the cited Verbitsky v1, Section 4 setup, Propositions
4.2-4.3 and Theorem 4.1 with proof (PDF pp. 12-15), the harmonic
preservation sentence in Corollary 4.3 (p. 16), and the doubled-dual
paragraph (p. 17). Neither its displayed group formula in arbitrary
degree nor its scalar-ring or endpoint-injection claims is needed.
ATTEMPTS/069,/089,/090,/091 retain their stated limitations.

For the degree-two extraction, take B_u=T_u direct sum T_-u with
the parallel anti-unitary involution

    T(l,lambda)=(tau_u^-1(lambda),tau_u(l)).

Its invariant curvature comes from the actual tensor/dual line
connections, not from a flatness assertion. With the triple
(-I,J,-K), the source's positive-type connection differential is our
dbar. Its conjugate-J operator is T on coefficients and exterior
J-conjugation on forms. On the T_u summand this is exactly S_u.
The source defines the conjugated differential and proves equality
of its Laplacian with the original one in every degree. Since the
conjugating operator is anti-unitary, its adjoint conjugates as well;
thus that equality implies harmonic preservation in degree two.
The doubled Laplacian is block diagonal, so extraction really maps
the harmonic T_u space to the harmonic T_-u space. A possible minus
in the cotangent convention is squared in degree two. This argument
does not infer a group action from the source's degree-one formula.

The formula S_u is balanced over complex scalars: moving a scalar
between its coefficient and form factors conjugates it on either
side. Its pointwise metric and product L2 metric are preserved.
The dual metric gives tau_-u tau_u=Id, while exterior J-conjugation
squares to (-1)^q in degree q. Hence S_-u S_u=Id here, and the
harmonic correspondence is onto. Anti-unitarity then carries the
orthogonal complement of the harmonic space onto its opposite
complement, proving (5) on all L2 degree-two forms.

Independently expand the determinant in paired unit line frames.
For alpha=f_1 a+f_2 b and gamma=f_1 c+f_2 d, their partners have
rows (-j(b),j(a)) and (-j(d),j(c)). Their determinant is therefore
j(a) wedge j(d)-j(b) wedge j(c), with the same unit wedge A as for
beta=a wedge d-b wedge c. This proves (4) with plus conjugation.
Both alpha,gamma and their partners are harmonic and dbar-closed;
A and line evaluation are parallel holomorphic maps. Therefore
beta and S_u beta are separately closed actual cup representatives.

Coefficient Hodge decomposition now gives smooth degree-one forms
eta,xi with the indicated opposite line coefficients such that

    beta-beta_h=dbar eta,
    S_u beta-S_u beta_h=dbar xi.

The second equality uses closedness of S_u beta and its harmonic
projection (5), independently of the first equality. Explicitly,

    beta wedge S_u beta-beta_h wedge S_u beta_h
      =dbar(eta wedge S_u beta+beta_h wedge xi).

Here both other factors are closed and beta_h has even degree two.
Thus both exact corrections disappear from the actual cohomology
product and its Serre integral. No action of S_u on eta is used.

For the product harmonic space, the exterior-product Dolbeault
differential and its adjoint have the graded tensor signs. In their
anticommutator the cross terms cancel, leaving the sum of factor
Laplacians. External products of factor harmonics consequently lie
in the kernel. Their classes form the cup-defined Kunneth basis;
coefficient Hodge theory equates its dimension with the full
harmonic dimension. They therefore span, and the zero endpoints of
both nonzero line powers leave only factor-degree (1,1). This
justifies using the mixed covector basis in (6), without claiming
closure of harmonic forms under arbitrary products.

For completeness, in the order (v,R_s v,w,R_t w), the six targets
are (12),(34):(0,0); (13):(-2,-3); (24):(2,3);
(14):(0,1); (23):(0,-1). The last two vanish by their three
degree-two Kunneth terms, including H^1(O)=0. The two surviving
mixed spaces each have dimension (7*4-2)(7*9-2)=1586.
The opposite spaces are Cx+Cy. All three pair partitions have
total weight zero. This uses neither forward concentration at Z
nor a perfect pairing of positive-z section spaces: the strict
traces for v and w are exactly the separate L160/L161 conclusions,
whose class detection retains W and delta.

In the mixed orthonormal basis, only the diagonal index terms
survive e_a wedge j(e_c)=-delta_ac E and
d_b wedge j(d_d)=-delta_bd D. Moving the second-factor covector
past the first-factor partner contributes one additional minus.
The full coefficient is consequently -sum|z_ab|^2 ED, not its
positive. Since bar(sigma_1)bar(sigma_2)=4ED, this is (6), with
the usual exterior norm and no factorial. Wedging with
sigma_1 sigma_2 gives numerator -4||beta_h||^2_L2 and denominator
16 Vol_1 Vol_2. Even-degree reordering gives no further sign.
This verifies precisely the factor 1/(4 Vol_1 Vol_2) in (1).

Finally the degree-one determinant cup is symmetric, because its
coefficient and exterior interchanges each give minus. The square
of its local self-cup 2a wedge b is zero. Polarization in four
commuting labels gives coefficient +8 for each of the three even
pair products, in the displayed input order and with equal total
line weight. This local identity therefore applies also at
positive z: it requires none of L158's z=0 section perfection.
The zero (14),(23) targets remove precisely the last term. The
remaining terms have coefficients f_v g_w+g_v f_w>0 and
-||beta_h||^2_L2/(4 Vol_1 Vol_2), respectively. Their sum is zero,
so (2) is the necessary balance and beta_h is nonzero. This is
cancellation, not a contradiction or a constructed mixed cup.

The bounded verdict survives the audit with unchanged hypotheses
and direct mathematical inputs. It adds no bound on z or exclusion
of a stable type, and supplies no F, transport or primitive Hodge
realization. The sign mechanism stays parked; a new exclusion needs
an independently testable constraint beyond (2). No mathematical
script or new lemma is required.

## Mathlib

Full matching coverage for the mixed-coefficient harmonic-projection,
Serre-integral and determinant-cup specialization is **not checked**.
Finite-dimensional orthogonal projection and exterior algebra would
only support parts of the calculation, not the imported analytic
theorems or actual coefficient comparisons. Unknown coverage is not
absence. The separate critical audit above checks (4)-(6) and the
scope of the negative verdict; no complete solution is claimed.
