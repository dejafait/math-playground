# L023 — Radial action contraction and its vanishing quadratic Wick part

## Hypotheses

Keep L020's SU(2) box, relative cochains, two original Wilson-flow
probes, displacement, and tau = 1/16. Take g to zero at each fixed
mesh before discussing mesh refinement, as in L011. Select only

\[
G^{\mathrm{act}}_{i,a}
=-\kappa_0(f_{i,0},r_0,S_{4,\mathrm{rad}}),\qquad
S_{4,\mathrm{rad}}=-\frac1{96}\sum_p|(D x)_p|^4,
\quad D=ad,\quad i=3,6.
\tag{1}
\]

This is the radial summand of S4 in L011, not its BCH terms, the
radial flow correction, or the radial contributions to the higher
residual jets. Cumulants have L011's finite-partition definition.

In orthonormal cochain coordinates let Delta be the relative one-form
Hodge Laplacian, E_t = exp(-t Delta), and A^c = Delta^(-1/2) xi^c,
with three independent standard Gaussian vectors. Use L008's
B_i = Delta^(-1/2) Q_i Delta^(-1/2), and set

\[
H=d\Delta^{-1/2},\qquad T_i=E_\tau B_i E_\tau,
\qquad
f_{i,0}=\sum_c(\xi^c)^T T_i\xi^c+\text{constant},
\qquad
r_0=\sum_c(\xi^c)^T R_a\xi^c+\text{constant}.
\tag{2}
\]

R_a is L009's symmetric whitened residual matrix. Constants in the
observables do not affect (1). Transposes and trace norms below are in
these orthonormal bases. For the plaquette row h_p of H put

\[
v_p=h_ph_p^T,\quad
\alpha_{i,p}=h_pT_i h_p^T,\quad
\beta_p=h_pR_a h_p^T,\quad
\chi_{i,p}=h_pT_iR_a h_p^T.
\tag{3}
\]

## Conclusion

For each of the two actual probes the exact finite-mesh contraction is

\[
G^{\mathrm{act}}_{i,a}
=\frac54\sum_p\left(\alpha_{i,p}\beta_p
                    +2v_p\chi_{i,p}\right).
\tag{4}
\]

The quadratic Wick part of the radial action has the sharper bound

\[
\varepsilon_a:=\|R_a E_\tau\|_1\longrightarrow0,\qquad
\left|\frac52\sum_p v_p\chi_{i,p}\right|
\le\frac52 M_i\varepsilon_a=o(1),\quad M_i=\sup_a\|B_i\|<\infty.
\tag{5}
\]

The other, fourth-chaos pairing class obeys only the bound established
here

\[
\left|\frac54\sum_p\alpha_{i,p}\beta_p\right|\le C_i/a.
\tag{6}
\]

Thus the quadratic Wick part has no unsuppressed cutoff logarithm.
Equation (6) is too weak to decide the radial action term's logarithm
or its boundedness. No full Gamma coefficient, interacting reflected
error <= c_box/2, continuum theory, or mass gap is proved.

## Proof

### 1. Transfer and normalization

All three selected polynomials depend only on linear curvature:
the leading flowed probe is quadratic in d E_tau A, the leading
residual is L009's gauge-invariant quadratic insertion, and the radial
action is fourth order in D x. L003's finite linear quotient therefore
transfers their joint moments, and hence their cumulant, from the
forest law to the Hodge law. This does not transfer higher nonlinear
jets or the coordinate Haar density.

In stored coordinates x = a A_stored, so D x = a^2 d A_stored.
The orthonormal coordinate vector of a cochain is a^2 times its stored
vector. Consequently the stored circulation is exactly H xi in (2),
without an additional mesh factor. This uses the same normalization
as L020. Polarization of the leading flowed probe gives T_i in (2).

### 2. Contract every connected pairing

Fix a plaquette, write h=h_p and Y_c=h xi^c, and temporarily use n
colors. Put F=sum_c (xi^c)^T T xi^c and
R=sum_c (xi^c)^T R_a xi^c. Each Y_c has variance v=h h^T. The exact
Gaussian Wick decomposition is

\[
\left(\sum_cY_c^2\right)^2
=\sum_{b,c}:Y_b^2Y_c^2:
 +2(n+2)v\sum_c:Y_c^2:+n(n+2)v^2.
\tag{7}
\]

For b different from c the two within-color contractions contribute
v(:Y_b^2:+:Y_c^2:), and for b=c the fourth power has six quadratic
contractions and constant 3v^2. Summing gives (7).

A third cumulant is unchanged by constants in any argument. With F
and R centered it is E[F_centered R_centered (S-E S)]. Wick products
are orthogonal across chaos orders. Against the fourth-chaos part of
(7), the two F legs and the two R legs must all join the action vertex.
For the action indices b=c there are 24 such contractions; for each
ordered b different from c there are 8. Thus

\[
\kappa(F,R,\sum_{b,c}:Y_b^2Y_c^2:)
=8n(n+2)(hT h^T)(hR_a h^T).
\tag{8}
\]

For the quadratic term, the standard connected quadratic-form
contraction is

\[
\kappa(F,R,\sum_c:Y_c^2:)
=4n\big(hTR_a h^T+hR_aT h^T\big)
=8n hTR_a h^T.
\tag{9}
\]

The two scalars in parentheses agree by transpose because T and R_a
are symmetric. Equivalently, every connected pairing of the three
quadratic vertices forms a triangle. Multiplying (9) by 2(n+2)v
and combining with (8), the negative radial action sign in (1)
cancels its coefficient -1/96. The result is

\[
\frac{n(n+2)}{12}\big(\alpha\beta+2v\chi\big).
\]

For n=3 this is (4). No independence between different plaquettes
was used: the action is a sum of single-plaquette fourth powers, so
cumulant multilinearity suffices. The pairing classes are distinguished
by zero or one internal action-vertex pair. Disconnected pairings are
exactly those removed by the third cumulant.

The independent check
`python3 scripts/combined-ward-response/check_radial_action_pairings.py`
enumerates connected eight-field pairings in 16 exact rational cases,
with one through four colors and indefinite symmetric matrices. It
checks the two classes separately and saves
`scripts/combined-ward-response/radial-action-pairings-certificate.json`.
This finite test is a sign/color-factor check, not a box asymptotic proof.

### 3. Strengthen the heat-smoothed residual estimate

L009 proves convergence of each fixed matrix entry of R_a to zero.
For (5) we require convergence of entire fixed mode columns, which
does not follow from entry convergence alone. The actual local stencils
give that additional fact.

On one-cochains set L_a=d* d and write K_a for L009's linearized
generator. Define the unwhitened symmetric residual operator

\[
N_a=\frac12(L_aK_a+K_a^*L_a)-Q_{3,a}-Q_{6,a}.
\tag{10}
\]

Then R_a=Delta^(-1/2) N_a Delta^(-1/2). Q_(i,a) here are the unflowed
quadratic-form operators from L008, so there is no heat in (10).
All coefficients in (10) are supported in a fixed interior compact
set for sufficiently fine meshes.

Let f_(k,a) be a normalized relative product one-form mode, including
its component in the label k. The eigenvalues obey L009's bounds
|k|^2/16 <= lambda_(k,a) <= pi^2 |k|^2/64. There is a fixed positive
spectral gap. For each fixed k,

\[
\|N_a f_{k,a}\|_a\longrightarrow0.
\tag{11}
\]

Here is the stencil justification, including the adjoint term. The
clover and endpoint maps are finite averages of shifts. K_a is a
finite average of u_a times one incidence difference of the input.
Its adjoint reverses these shifts and places that difference on the
product with u_a. The Q_i are d* W_(i,a) d, where W_3 is the bounded
diagonal plaquette-weight average and W_6 is the bounded symmetric
combination of clover averages and shear weights. Thus L_a K_a and
K_a* L_a have differential order at most three, and Q_i order at
most two. For fixed k, the sampled sine/cosine modes and each needed
forward/backward difference converge uniformly on the coefficient
support to the corresponding smooth mode and derivative. All the
shifted coefficient derivatives converge there as well. In particular
K_a* converges to K*=(u contraction composed with d)*, with the
derivatives of u retained; it is not obtained by merely negating K.

The continuum limit of (10) is
N=one-half (d*d K+K* d*d)-Q_3-Q_6. L009's compact-displacement
identity q_V=q_3+q_6, followed by polarization, gives N=0 as a
distributional differential operator. Its smooth compactly supported
output on a fixed mode is therefore zero. The uniform consistency
just established, and the bounded volume of the box, prove (11).
Boundary stencils do not contribute because these coefficients and
all their shifts vanish near the faces. The relative modes and
Laplacian themselves keep the physical boundary conditions.

There is also a bound uniform in a and all allowed labels,

\[
\|N_a f_{k,a}\|_a\le C(1+|k|)^3.
\tag{12}
\]

To see this directly, normalized product modes have uniformly bounded
point amplitude on the fixed box. Each incidence difference introduces
a frequency 2 sin(pi k_j/(2N))/a <= pi k_j/8. Each shift has norm
one and each finite average is bounded. The discrete product rule
for a forward difference is
D_j(fg)=(D_j f)(shift_j g)+f D_j g; backward differences have the
reversed rule. Iterate these rules in the operators of (10).
Smooth u_a,w_a,s_a and their coefficient differences through order
two are uniformly bounded. At most three differences hit a mode.
The resulting point bound C(1+|k|)^3 also bounds its weighted L2
norm by a uniform constant times that expression. This proof does
not use a mesh-dependent inverse inequality.

The spectral gap and Delta^(-1/2) f_(k,a)=lambda_(k,a)^(-1/2) f_(k,a)
now imply both

\[
\|R_a f_{k,a}\|_a\to0\quad\text{for fixed }k,
\qquad
\|R_a f_{k,a}\|_a\le C'(1+|k|)^3\quad\text{for all }a,k.
\tag{13}
\]

Expand R_a E_tau as a sum of rank-one mode columns. The trace norm
of a rank-one operator x f_k* with normalized f_k is ||x||, so

\[
\|R_a E_\tau\|_1
\le\sum_{k\text{ allowed}}
 e^{-\tau\lambda_{k,a}}\|R_a f_{k,a}\|_a.
\tag{14}
\]

The terms are bounded by
C'(1+|k|)^3 exp(-tau |k|^2/16), summable over the four-dimensional
labels and their finitely many components. Extend absent labels by
zero as in L009. Each fixed term tends to zero by (13); dominated
convergence proves epsilon_a -> 0. This is a one-sided trace-norm
statement for the actual residual, stronger than L009's doubly
heat-weighted response convergence. It gives no unflowed operator-norm
smallness and no asserted rate.

### 4. Bound the two classes without hidden smoothing

L020 proves ||H||<=1 and 0<=v_p<=1, since HH*=P_ex. Put V=diag(v_p).
Cyclicity of the finite trace and the trace-ideal inequality give

\[
\left|\sum_p v_p\chi_{i,p}\right|
=|\operatorname{Tr}(V H T_i R_a H^*)|
\le\|T_i R_a\|_1
\le M_i\|E_\tau R_a\|_1
=M_i\varepsilon_a.
\tag{15}
\]

The last equality uses adjoint invariance of trace norm. In particular
V need not commute with heat or have smooth spatial coefficients.
This proves (5).

For the other class, |beta_p|<=||R_a|| v_p<=C/a by L020. For a real
matrix M, sum_p |M_pp|<=||M||_1, by pairing M with the diagonal
matrix of the diagonal signs. Consequently

\[
\sum_p|\alpha_{i,p}|\le\|H T_i H^*\|_1
\le\|T_i\|_1\le M_i\operatorname{Tr}(E_\tau),
\tag{16}
\]

uniformly in a. Combining these estimates gives (6). Unlike the
radial flow term, the action occurrence has no time integration
yielding L020's O(a^2) small factor. The unflowed diagonal beta_p
is not controlled by (14): its row can include arbitrarily high modes.
Replacing it by low-mode convergence would be an invalid interchange.

### 5. Relevance and literature qualification

Equation (5) eliminates one whole pairing class of a separate action
summand in the exact L011 expansion. The class in (6) remains a
specific unflowed local-loop test; its estimate neither establishes
nor refutes logarithmic growth. L021's complete radial flow bound
and L022's nonlinear transfer obstruction remain distinct results.
All remaining action, measure, observable and insertion terms must
still be retained in the full coefficient. The reflected-error bound
c_box/2 and the main construction/mass-gap gaps are unchanged.

This is reproduction/specialization of connected Gaussian contractions
and local-stencil consistency, not a claim of progress beyond the
checked literature. The saved SPECIALIZE assessment
`drafts/literature/2026-09-26-current-target.md` reads Luescher–Weisz,
[*Perturbative analysis of the gradient flow in non-abelian gauge
theories*, arXiv:1101.0963v2](https://arxiv.org/pdf/1101.0963v2),
sections 7 and 8.2. Their flow-renormalizability result is supporting
bulk context; it does not evaluate this bare-normalized all-face-box
action summand. The specialization is needed for the actual residual
and probe stencils, not to reprove that general theorem.

## Mathlib

Coverage of the full selected action contraction and one-sided
trace-norm limit: **not checked**. Coverage of supporting Wick products,
Gaussian cumulants, finite-difference product rules, trace ideals and
dominated convergence: **not checked**. No Mathlib theorem is asserted
to match the full statement. The primary flow result linked above is
supporting literature, not a match for (4)–(6).
