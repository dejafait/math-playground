# L008 — The anticyclotomic tangent obstructs the CM fiber trace

## Hypotheses

Let F = Q_p, with p > 3, G = G_Q, and H = G_K for an imaginary
quadratic field K. Choose complex conjugation tau of order two, so
G = H semidirect-product <tau>. Coefficient rings have trivial G-action.
For an H-character a write a^tau(h) = a(tau h tau).

Let psi: H -> F^times be continuous of finite order and put
chi = psi/psi^tau. Assume chi != 1. Let R = F[[T]] and let
u_T: H -> R^times be a continuous character with u_0 = 1. Set

\[
\xi_T=u_T/u_T^\tau=1+T d+O(T^2),\qquad d:H\longrightarrow F.
\]

Assume d != 0. Let nu_T be the G-character with restriction
(u_T u_T^tau)^(-1) to H and value 1 at tau. This extension exists
because u_T u_T^tau is tau-invariant. Define

\[
M_R=\bigl(\operatorname{Ind}_H^G(\psi u_T)
       \otimes_R\operatorname{Ind}_H^G(\psi^{-1}u_T)\bigr)
       \otimes_R\nu_T.
\tag{1}
\]

Use A = F[epsilon]/(epsilon^2), with R -> A sending T to epsilon,
and write M_A and M_0 for the resulting specializations. At T = 0,
M_0 = Ind(psi) tensor Ind(psi)^dual. Let tr_0: M_0 -> F be its
ordinary trace; dividing it by 2 to normalize the scalar projector
does not affect the assertions.

## Conclusion

There is a G-equivariant decomposition

\[
M_R\simeq\operatorname{Ind}_H^G\xi_T\oplus
          \operatorname{Ind}_H^G\chi.
\tag{2}
\]

The trace tr_0 has no A-linear G-equivariant lift M_A -> A. More
precisely, in the coset bases specified below,

\[
\operatorname{Hom}_{A[G]}(M_A,A)
 =F\cdot\epsilon(e_1^*+e_2^*);
\tag{3}
\]

every such morphism reduces to zero. The obstruction to tr_0 lies
in the quadratic-character summand of H^1(G,M_0^dual); its
restriction to H is -d(e_1^*-e_2^*), and it is nonzero.

Even allowing corrections involving another representation does
not repair the lift: for any nonzero finite-dimensional F-representation
V of G, there is no A-linear G-map

\[
V_A\otimes_A M_A\longrightarrow V_A
\]

whose reduction is id_V tensor tr_0, where V_A is the constant
deformation of V. Without the assumption d != 0, the trace lifts to
first order exactly when d = 0.

Applied to the normalized diagonal CM family in
[the source normalization](../foundations/09-cm-diagonal-deformation.md),
this rules out a regular family contraction extending the fiber trace,
already modulo T^2. It does not rule out a map existing only on the
fiber, an operation on an individual cohomology class, or a derived
geometric construction. There is no new rational-rank bound.

## Proof

**Inducing characters and normalization.** In each induced rank-two
representation choose the coset basis for {1,tau}. An element h of H
acts diagonally by a(h),a^tau(h), and tau exchanges the basis vectors.
Let e_1,e_2 denote the tensor basis vectors using matching cosets,
and f_1,f_2 those using different cosets. After multiplying by nu_T,
the four H-characters are respectively

\[
\frac{(\psi u_T)(\psi^{-1}u_T)}{u_Tu_T^\tau}=\xi_T,
\quad \xi_T^{-1},\quad
\frac{(\psi u_T)((\psi^\tau)^{-1}u_T^\tau)}{u_Tu_T^\tau}
 =\chi,\quad \chi^{-1}.
\]

The value nu_T(tau) = 1 means tau exchanges e_1,e_2 and exchanges
f_1,f_2 without an extra sign. Since xi_T^tau = xi_T^(-1) and
chi^tau = chi^(-1), this proves (2) as a G-module decomposition,
not just after restriction to H. At T = 0 the e-vectors correspond
to the two diagonal matrix units; the f-vectors are off-diagonal.
Thus tr_0(e_1) = tr_0(e_2) = 1 and tr_0(f_1) = tr_0(f_2) = 0.

**All possible first-order corrections.** Multiplicativity of xi_T
implies d(hh') = d(h)+d(h'), and conjugation gives d^tau = -d.
On the first summand of M_A the matrices are

\[
\rho_A(h)=\begin{pmatrix}1+\epsilon d(h)&0\\0&1-\epsilon d(h)\end{pmatrix},
\qquad
\rho_A(\tau)=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\tag{4}
\]

Let an invariant functional take values a,b in A on e_1,e_2.
Equivariance under h gives epsilon d(h)a = epsilon d(h)b = 0.
Choose h with d(h) != 0. Since d(h) is a nonzero element of the
field F, these equations force a,b into epsilon F. Equivariance
under tau then gives a = b. Conversely these conditions suffice.
On the other summand choose h with chi(h) != 1. Both chi(h)-1 and
chi(h)^(-1)-1 are nonzero scalars, hence units of A, so invariance
forces the functional to vanish on f_1,f_2. This proves (3), allowing
arbitrary first-order corrections on all four basis vectors. In
particular none can have reduction tr_0.

If d = 0 instead, the first summand modulo T^2 is Ind_H^G 1,
and the functional (1,1,0,0) is an invariant lift. This proves the
exact first-order criterion, without claiming a higher-order lift.

**The obstruction as a Galois class.** Put N_A = Hom_A(M_A,A),
with the usual dual G-action, and N_0 = M_0^dual. The sequence
0 -> epsilon N_A -> N_A -> N_0 -> 0 identifies its left term with
N_0. Lift tr_0 as the constant row t_+ = e_1^*+e_2^*. Its connecting
cocycle is

\[
b(g)=\frac{g\cdot t_+-t_+}{\epsilon},\qquad
b(h)=-d(h)t_-,\quad b(\tau)=0,\quad t_-=e_1^*-e_2^*.
\tag{5}
\]

These formulas follow by inverting (4) for the dual action.
The line F t_- is trivial on H and has tau-action -1: it is the
quadratic character eta_K of G/H. Hence (5) takes values in that
line, consistently with d^tau = -d. The group-action identity
proves the cocycle relation; changing the chosen lift changes b by
a coboundary. Project a purported coboundary onto F t_-. Its
restriction to H is zero, since H acts trivially there. But (5)
restricts to the nonzero homomorphism -d t_-. Thus the obstruction
class is nonzero. No restriction-to-H computation has silently
forgotten the action of complex conjugation.

**Corrections involving V.** Suppose a map P as in the conclusion
existed. On V_A tensor e_1 its reduction is id_V, so in a fixed
basis write this restriction as P_1 = I+epsilon B. Equivariance
under h, with rho_V its action on V, requires

\[
(I+\epsilon B)(1+\epsilon d(h))\rho_V(h)
 =\rho_V(h)(I+\epsilon B).
\]

The coefficient of epsilon, multiplied on the right by rho_V(h)^(-1),
says B+d(h)I = rho_V(h)B rho_V(h)^(-1). Taking matrix traces gives
(dim_F V)d(h) = 0. Characteristic zero and d != 0 contradict this.
The e_1 subspace is H-stable, so values of P on other summands cannot
change this equation. A nonzero scalar multiple of tr_0 is equally
obstructed, by dividing P by that scalar.

**Arithmetic application and its limits.** The source's equation
(2.4) already includes the critical twist; it identifies the actual
family with V_p E tensor the right side of (2). Take u_T = Psi_T
from its equation (2.3). Then d(h) = l(h)-l(tau h tau). The source
identifies xi_T with the universal character of a Z_p-extension.
Since xi_T(h) = (1+T)^{l(h)-l(tau h tau)}, an identically zero d
would make xi_T trivial, contradicting universality. Thus d != 0.
This test avoids an unproved local-inertia normalization.

The source's T = v^(-1)(1+S)-1 has T = 0 at weight one and derivative
v^(-1) != 0. Thus a nonzero diagonal tangent is still nonzero in T.
The regularity condition chi(overline{mathfrak p}) != 1 in the
checked application implies chi != 1. Equations (2)--(5) therefore
apply to that normalized family, with no assumption of a classical
tame-twist identity and no accumulating-points hypothesis from L007.
A family morphism regular at this fiber would reduce to the excluded
first-order map, so it cannot extend this trace. A ramified test
curve with zero first derivative would not test the nonzero tangent
considered here.

The rank-two application remains conditional on the missing Kummer
membership in L006. In particular this representation obstruction
does not imply non-Kummer membership of kappa or invalidate its
existing cohomological specialization. It only blocks the specified
regular contraction as a proof of that membership.

## Mathlib

Coverage of the full obstruction statement: **not checked**.
Supporting results on induced representations, dual numbers, group
cohomology, and matrix traces: **not checked**. The proof is given
above. The direct source links in the foundation identify equation
(2.3), Remark 2.6/(2.4), and Section 5.1, which supply the actual
arithmetic family and its coordinate. They do not assert the full
lifting obstruction or the missing Kummer-membership theorem.
