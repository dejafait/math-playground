# L143 — Mixed product Weitzenböck coupling is indefinite

## Hypotheses

Retain L071's marked K3 product X=S_1 x S_2, identical hyperkähler
metrics g, ordered parallel structures I,J,K and the full integral
tensor tau_D. Suppose F is locally free of complex rank two,
slope-polystable at the real product Kähler class h_1+h_2, with
integral c_1(F)=0 and ch_2(F)=-14e_1-21e_2-tau_D. Use its actual
compatible determinant-one unitary connection A supplied by L131.
Existence of F is hypothetical.

Write R=R_A=P+K_m+Q for its two pure form-leg blocks and mixed
block. Indices a,b run over the first oriented orthonormal four-frame,
and mu,nu over the second; thus (K_m)_{a mu}=R_{a mu}.
All derivatives below couple A and the product Levi-Civita connection.
For su(2) coefficients use the positive invariant pairing
<U,V>=-tr(UV)/2. A positive constant change of this pairing changes
none of the sign or zero assertions.

The pointwise algebraic test uses the entire real thirty-dimensional
space of simultaneous-quaternionic invariant su(2)-valued two-forms
on H direct sum H. Its two pure ASD blocks are independent. It imposes
no unproved global-curvature realization on a pointwise tuple.

## Conclusion

The actual mixed projection satisfies

\[
0=\nabla_A^*\nabla_A K_m+\mathcal C(P,K_m,Q),\qquad
\mathcal C_{a\mu}=-2\sum_b[P_{ab},(K_m)_{b\mu}]
                 -2\sum_\nu[(K_m)_{a\nu},Q_{\nu\mu}].       \tag{1}
\]

In particular, on the compact product,

\[
0=\int_X\bigl(|\nabla_A K_m|^2+\mathcal E(P,K_m,Q)\bigr)dV,
\qquad
\mathcal E=\sum_{a,\mu}\langle\mathcal C_{a\mu},(K_m)_{a\mu}\rangle.
                                                               \tag{2}
\]

Here is its full algebraic sign and zero-locus test. Choose real
four-by-four matrices M_0=1 and M_1,M_2,M_3 specified in the proof,
with M_i M_j=-delta_ij+epsilon_ijk M_k. Write uniquely

\[
P_{ab}=\sum_{k=1}^3p_k(M_k)_{ab},\quad
Q_{\mu\nu}=\sum_{k=1}^3q_k(M_k)_{\mu\nu},\quad
(K_m)_{a\mu}=\sum_{s=0}^3A_s(M_s)_{a\mu},                 \tag{3}
\]

where every coefficient belongs to su(2). For cyclic (k,i,j)=(1,2,3),
(2,3,1),(3,1,2), put U_k=[A_0,A_k] and V_k=[A_i,A_j]. Then

\[
\boxed{\mathcal E=16\sum_{\mathrm{cyc}}
 \bigl(\langle q_k-p_k,U_k\rangle-
       \langle p_k+q_k,V_k\rangle\bigr).}                 \tag{4}
\]

Equation (4) equal to zero describes the entire zero locus. More
precisely, for fixed mixed coefficients:

* If all A_s commute, the coupling vanishes for every P,Q.
* Otherwise its zero set in the eighteen real pure-block coefficients
  is a proper linear hyperplane, and both signs occur.

There are exact invariant tuples with both pure blocks nonzero,
|K_m|^2=8 and energy -32 or +32. There are also noncommuting tuples
with K_m nonzero and energy zero. Consequently no universal favorable
sign E>=0, nor its opposite, holds on this domain. The universal
mixed Bochner sign mechanism is parked. This conclusion excludes no
global F, realizes no curvature tuple globally, and supplies no cycle
or transverse transport. The universal primitive Hodge gap remains.
This is a NEGATIVE / REPRODUCTION specialization of the inspected
general formula; no originality is claimed. The separate critical audit
below preserves the scoped conclusion without a substantive correction.

## Proof

**Imported formula and applicability.** Import Oliveira–Waldron,
*Yang-Mills flow on special-holonomy manifolds*, Advances in Mathematics
376 (2021), 107418, [arXiv:1812.10866v2, section 4.1, (4.6),
PDF p. 11](https://arxiv.org/pdf/1812.10866v2#page=11).
For a smooth metric connection and an adjoint-valued two-form omega,
with Delta_A=d_A^*d_A+d_A d_A^*, their normal-frame formula is

\[
\begin{aligned}
(\Delta_A\omega)_{ij}={}&(\nabla_A^*\nabla_A\omega)_{ij}
 -[R_{ik},\omega_{kj}]+[R_{jk},\omega_{ki}]\\
 &+R^g_{ik\ell k}\omega_{\ell j}
  +R^g_{ik\ell j}\omega_{k\ell}
  -R^g_{jk\ell k}\omega_{\ell i}
  -R^g_{jk\ell i}\omega_{k\ell}.
\end{aligned}                                                   \tag{5}
\]

Its hypotheses hold for the actual smooth SU(2) connection, including
when factor restrictions are reducible. The cited general formula is
imported, not reproved; the work here is its product specialization.

Use omega=R before projecting. Bianchi gives d_A R=0. The actual
connection is HYM of slope zero, hence coefficientwise primitive
of type (1,1). For the closed product Kähler form Omega, the Kähler
star identity is *R=-R wedge Omega^2/2 in complex dimension four.
It implies d_A *R=0 and therefore d_A^*R=0. Thus Delta_A R=0.
This uses the same HYM/star identities recorded in L131; it does
not assert Delta_A K_m=0. L095's ASD-complex harmonicity is a
different assertion and is not needed as an input to this proof.

**Full form-leg projection.** On substituting omega=R, the two
bracket terms in (5) add to -2 sum_k[R_{ik},R_{kj}]: antisymmetry
gives [R_{jk},R_{ki}]=-[R_{ik},R_{kj}]. For i=a,j=mu, summing
k=b in the first factor gives -2[P_ab,(K_m)_bmu], and summing
k=nu in the second gives -2[(K_m)_anu,Q_numu]. These are all
summands. In this mixed output neither P/P, P/Q, K_m/K_m nor Q/Q
can occur: the intermediate index lies in exactly one factor and
the two end indices lie in different factors. P/K_m and K_m/Q
both remain; no pure curvature block has been discarded.

The first and third Riemann terms in (5) are Ricci contractions,
zero by Ricci-flatness of both factors. For the second term
R^g_{ak ell mu}, any nonzero product-curvature tensor would have
all four indices in one factor, impossible for a and mu. The fourth
term R^g_{mu k ell a} vanishes for the same reason. This checks
all four Riemann terms separately; Ricci-flatness alone was not
used to delete the full Riemann action.

The product splitting of two-form legs is Levi-Civita parallel.
Its projection acts trivially on coefficients and so commutes
with the coupled derivative and rough Laplacian. The mixed output
of the rough term is precisely nabla_A^*nabla_A K_m. This proves
(1). The mixed two-form norm is sum_a,mu |(K_m)_amu|^2, with
no extra factor two: the usual half-sum over antisymmetric indices
counts these components once. Pair (1) with K_m and integrate.
Compactness and absence of boundary give (2), retaining the real
positive coefficient pairing. No commutation with d_A is asserted.

**Entire invariant module and energy contraction.** Use quaternion
coordinates (1,i,j,k) on both factors, oriented by the I-complex
orientation. Let M_k be minus right multiplication by i,j,k,
respectively. Explicitly their two-forms are

\[
M_1: dx^0\wedge dx^1-dx^2\wedge dx^3,\quad
M_2: dx^0\wedge dx^2+dx^1\wedge dx^3,\quad
M_3: dx^0\wedge dx^3-dx^1\wedge dx^2.                   \tag{6}
\]

Here (M_k)_ab denotes the displayed skew two-form matrix. These
matrices obey M_k^t=-M_k, M_k^2=-1 and M_1M_2=M_3, with cyclic
versions. They commute with left multiplication I,J,K. The latter's
real centralizer consists of right quaternion multiplication: a
commuting map is determined by its value on 1, since its values on
i,j,k are the left translates of that value. Thus the mixed invariant
matrices are exactly span_R(1,M_1,M_2,M_3); the invariant skew pure
matrices are exactly span_R(M_1,M_2,M_3). The forms in (6) are ASD
in the chosen orientation. This explicitly realizes the full ten-real-
dimensional invariant two-form module from Fowdar, *Examples of Deformed
Spin(7)-Instantons/Donaldson–Thomas Connections*,
Communications in Mathematical Physics 405 (2024), 183,
[section 2, (2.6)](https://link.springer.com/article/10.1007/s00220-024-05060-0).
It justifies every tuple in (3), with 3(3+3+4)=30 real variables,
rather than restricting to a selected mixed direction.

Invariance of the coefficient pairing says
< [u,v],w >=<u,[v,w]>. Applying it to both terms of (1) gives

\[
\begin{aligned}
\mathcal E&=2\sum_{a,b}\langle P_{ab},B^1_{ab}\rangle
           +2\sum_{\mu,\nu}\langle Q_{\mu\nu},B^2_{\mu\nu}\rangle,\\
B^1_{ab}&=\sum_\mu[(K_m)_{a\mu},(K_m)_{b\mu}],\qquad
B^2_{\mu\nu}=\sum_a[(K_m)_{a\mu},(K_m)_{a\nu}].
\end{aligned}                                                    \tag{7}
\]

Both sums over pure indices here are full ordered sums, not
half-sums. Substitute (3). In B^1 the matrix product is M_s M_t^t;
in B^2 it is M_s^t M_t. Antisymmetry of [A_s,A_t] eliminates
s=t and combines each pair s<t with its reverse. The pairs (0,k)
contribute -2U_k M_k and +2U_k M_k respectively, while pairs of
nonzero distinct indices contribute -2V_k M_k to both. Therefore

\[
B^1=-2\sum_{\mathrm{cyc}}(U_k+V_k)M_k,\qquad
B^2= 2\sum_{\mathrm{cyc}}(U_k-V_k)M_k.                  \tag{8}
\]

Finally sum_ab(M_k)_ab(M_l)_ab=4delta_kl. Inserting (8) in (7)
gives exactly (4), including its factor sixteen and both signs.

For a fixed mixed tuple, (4) is a linear functional of p_k,q_k.
It vanishes identically in them precisely when U_k+V_k=U_k-V_k=0
for all k, equivalently when all six pairwise brackets [A_s,A_t]
vanish. With the usual identification of su(2) with R^3, brackets
are a nonzero multiple of the vector cross product. Pairwise
commutation therefore means that the four coefficients lie in a
common real line, allowing the all-zero case. Otherwise the linear
functional is nonzero, and its zero set is a proper hyperplane;
choosing a pure tuple and its negative gives both signs. This proves
the stated exhaustive zero-fibre description, not merely sample
vanishing values. In particular E=0 does not imply K_m=0.

**Exact tuples and decision.** Use the orthonormal su(2) basis

\[
T_1=\begin{pmatrix}i&0\\0&-i\end{pmatrix},\quad
T_2=\begin{pmatrix}0&1\\-1&0\end{pmatrix},\quad
T_3=\begin{pmatrix}0&i\\i&0\end{pmatrix},
\quad [T_1,T_2]=2T_3
\]

with cyclic bracket identities. Set A_0=T_1,A_1=T_2,A_2=A_3=0,
so K_m=T_1 M_0+T_2 M_1 and |K_m|^2=4+4=8. For real numbers
r,s take P=rT_3M_1, Q=sT_3M_1. Only U_1=2T_3 is nonzero in
(4), giving E=32(s-r). In (1) the P term is -4rK_m and the Q
term is +4sK_m, independently checking the sign and multiplicity.

The choices (r,s)=(2,1),(1,2),(1,1) yield -32,+32,0, with both
pure blocks nonzero and noncommuting mixed coefficients. They
are all simultaneous-quaternionic invariant by (3). They need
not occur on an actual F to refute a universal algebraic sign.
The favorable sign in (2) would be E>=0, since it would force
nabla_A K_m=0; (2,1) violates it exactly. Even that parallelness
would need a further assessed argument to imply a contradiction.
No global conclusion follows from these pointwise tests alone.

**Verification and qualifications.** Reproduction command:
`python3 scripts/mixed-weitzenbock/check_product_coupling.py`.
The full certificate is
`scripts/mixed-weitzenbock/product_coupling_certificate.json`.
It checks the quaternion matrices, invariant type, ASD orientation,
norms, both full ordered commutators against (1), both expressions
in (8), (4), and the exact positive/negative/zero tuples. The
quadratic projection is checked on every thirty-dimensional coordinate
vector and pair sum; twenty further integer tuples exercise the energy
reduction. All 485 cases and nine aggregate checks pass, with no
failures. These are corroboration of the complete derivation above,
not a replacement for it or a realization theorem. The wrong-sign
threshold is zero; the actual value is -32.

The fixed-charge constraints are integral constraints and have not
been substituted for pointwise control of P,Q,K_m. This result does
not rule out a different global identity, an estimate using additional
differential constraints, or a different representative. It neither
reopens L142's different quartic functional nor resolves the main gap.

### Separate critical audit — 2026-10-21, step 454

This RESEARCH / REPRODUCTION audit uses the pre-invocation SPECIALIZE
assessment `drafts/literature/2026-10-21-mixed-product-weitzenbock-critical-audit.md`.
It finds no substantive error or stronger conclusion. Outcome EXPLORATION
records a completed verification, not another NEGATIVE or mathematical
advance. The universal pointwise sign route remains parked.

**Source and actual equation.** Reopened Oliveira–Waldron v2,
section 4.1 (4.6)–(4.11), the norm convention after (4.13), and the
complete Proposition 4.1 projection/integration proof, PDF pp. 11–13.
Equation (5) agrees term by term with the first line of source (4.6).
In source (4.8), the coefficient-valued contracted bracket is symmetric
in its two two-form arguments; substituting the curvature therefore
gives exactly the factor two in (1). No sign is imported from a norm
estimate or from the compatibility-preservation conclusion. The real
underlying unitary bundle is a metric bundle, and its su(2) endomorphisms
are preserved by the coupled connection and commutator. Restricting
the source identity to them introduces no bracket factor. The chosen
positive pairing is a constant rescaling of the real trace pairing.

L071's stable-product passage and L131's determinant argument supply
the actual connection with zero Einstein constant, even with reducible
factor restrictions. Bianchi and the primitive Kähler star identity
apply to its full curvature and give Delta_A R=0. The form-leg
projection is parallel for the product connection. For mixed output,
the intermediate first-factor index forces P/K_m, and the second-factor
index forces K_m/Q; there is no third possibility. In the two contracted
Riemann terms Ricci is zero; in each uncontracted term the first and
last indices lie in different factors, so product curvature is zero.
Thus neither pure block nor a non-Ricci Riemann contribution was silently
discarded. Integration uses the mixed norm once per unordered mixed
pair, in agreement with the source's half-sum convention. Harmonicity
in an ASD deformation complex is not used in this deduction.

**Full module, signs and zero fibres.** Reopened Fowdar's version of
record, section 2 (2.5)–(2.7). The invariant summand is defined by
invariance under each of the three induced complex structures; it does
not require irreducible holonomy. In the displayed frames, these are
left quaternion multiplication and a mixed matrix must commute with
all three. Its value on 1 determines it, proving the four-dimensional
centralizer assertion. The skew part gives exactly the three displayed
ASD matrices on each factor. Consequently all thirty coefficient
variables, with independent pure blocks, belong to the stated domain.

The pairing identity applied to the first term of (1) gives
+2 sum_ab <P_ab,sum_mu[K_amu,K_bmu]>; applied to the second it gives
+2 sum_munu <Q_munu,sum_a[K_amu,K_anu]>. Both are ordered sums.
For the (0,k) coefficient pair, M_0 M_k^t=-M_k and
M_0^t M_k=M_k, fixing the opposite U signs in (8). For the cyclic
(i,j) pair, both products equal -M_k, fixing both V signs.
The reversed coefficient pair doubles each contribution. The ordered
matrix norm is four, so (4) has coefficient sixteen, not eight.

For fixed A, the pure-block functional has coefficient vectors
-16(U_k+V_k) and 16(U_k-V_k). Positive definiteness makes it identically
zero precisely when both vanish for every k. Adding and subtracting
then kills all six pairwise brackets. This includes A=0 and every
commuting tuple. In every other case its kernel has real dimension
seventeen in the eighteen-dimensional pure space. This checks all
zero fibres, including cancellation between nonzero pure blocks;
zero scalar energy is not a conclusion that either K_m or C vanishes.

For the explicit noncommuting A, [T_3,T_1]=2T_2 and
[T_3,T_2]=-2T_1 give C_P=-4rK_m and C_Q=4sK_m directly.
With |K_m|^2=8 the three energies are exactly -32,32,0.
The negative witness has both pure blocks nonzero and violates the
required lower bound zero. This is a pointwise algebraic test only.

**Complete evidence and limits.** Read the full script and every field
of `scripts/mixed-weitzenbock/product_coupling_certificate.json`, including
all matrices, all five witness tuples, the normalization, sign requirement,
zero equation, and both empty failure lists. Rerunning the reproduction
command passes 9/9 aggregate checks and 485 exact cases. Coordinate
vectors and pair sums exhaust the quadratic projection identity by
polarization; they do not by themselves exhaust a cubic energy identity.
The latter rests on (7)–(8), independently checked above, with the
twenty integer samples only corroborating it. No symbolic zero-locus
classification is inferred from samples. No mathematical input or DAG
edge changes. This audit proves no global tuple realization, F exclusion,
parallelness, cycle construction or transport, and leaves universal
primitive Hodge realization unresolved.

## Mathlib

Full matching coverage of this product coefficient-valued identity,
its specialization or its zero-locus statement has not been checked.
Unknown availability is not evidence of absence. No formal verification
is claimed.
