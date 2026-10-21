# L032 — Exact symmetry reduction of the full upper-face pairing

## Hypotheses

Keep L008's exact cutoff rho, the two potentials Psi_13 and Psi_24,
the box D=(-4,4)^4, relative one-form modes and tau=1/16. Keep L030's
leading residual N_2 and L031's signed functional I_i, i=3,6. These
are one-color operators; the selected three-color action response
has the normalization already specified in L030.

Write u=u^A+u^B, where A uses only Psi_13 and its antisymmetric
partner, and B uses only Psi_24 and its partner. This splits the
coefficients of the original displacement; it does not change the
original probes. Let Q_i^A,Q_i^B and N^A,N^B be the operators obtained
by applying L008's and L030's formulas separately to these potentials.
In particular N^A+N^B=N_2. Write a mode label as k=(c;k_1,...,k_4),
where c is its one-form component. Let

\[
 Z=\{k:c=1, k_1=0, k_2,k_3,k_4\ge1\},
 \qquad \lambda_k=(\pi/8)^2\sum_j k_j^2.
\]

Define the bilinear, absolutely convergent sum

\[
 F_i(\alpha,\beta)=8\sum_{k\in Z}\sum_\ell
 \frac{e^{-\tau(\lambda_k+\lambda_\ell)}}{
             \lambda_k^2\lambda_\ell}
 (Q_i^\alpha)_{k\ell}(N^\beta)_{\ell k},
 \qquad \alpha,\beta\in\{A,B\}.                 \tag{1}
\]

## Conclusion

For both original probes the mixed contributions vanish exactly:

\[
 F_i(A,B)=F_i(B,A)=0,
 \qquad I_i=F_i(A,A)+F_i(B,B).                  \tag{2}
\]

In each surviving sum one may restrict the second index to

\[
 \ell_j\equiv k_j\pmod2\quad(j=1,2,3,4).        \tag{3}
\]

In particular ell_1 is even, but its one-form component is still
unrestricted. In F_i(A,A) one may further restrict to ell_1>=2:
the 13-potential contribution comes entirely from nonzero even axial
frequencies. In F_i(B,B), ell_1=0 is allowed only with component 1;
all other components, and the remaining component-1 modes, have
positive even axial frequency.

These statements retain the heat factors, both inverse-Laplacian
weights and all transition coefficients. They do not evaluate either
surviving sum or give it a sign. Thus they neither establish nor
exclude a nonzero a^(-2) term in L030's selected action class. They
give no cancellation with other action/measure/insertion/flow terms,
no complete logarithm, no reflected-error bound and no mass gap.

## Proof

### 1. Linearity and convergence

The displacement and its formal order-t correction are linear in
Psi. The diagonal strains, shear strains and their corrections are
linear in that displacement. Consequently L030's K(t), Q_3(t) and
Q_6(t) are linear in Psi. The operator L(t) is independent of Psi,
so the symmetric action variation and its residual coefficient are
also linear. This proves the asserted splitting of Q_i and N_2.

Each split potential has the same smooth compact support as the
original one. Its Q_i satisfies the bounded curvature-form estimate
used in L031, and its N has compact smooth coefficients and order at
most five. The positive relative spectral gap and the two Gaussian
heat factors therefore give the same absolute convergence argument
as L031 for every sum in (1). Splitting and reindexing the sums are
legitimate. No trace cyclicity for an unbounded differential operator
is required below.

### 2. Covariance of the entire formal stencil

For a signed coordinate permutation g preserving the cube, let U_g
be pullback on real one-forms, and use the corresponding pullback on
two-forms. These maps are unitary. They preserve the relative
boundary conditions and permute the explicit relative mode basis
up to signs. They commute with Delta and its heat and inverse powers.

Here covariance means

\[
 U_g Q_i[\Psi]U_g^{-1}=Q_i[g^*\Psi],\qquad
 U_g N_2[\Psi]U_g^{-1}=N_2[g^*\Psi].             \tag{4}
\]

This holds separately for the triplet and shear, not just for their
sum. To verify it for the actual stencil, under a coordinate sign
change partial_j and partial_j^3 acquire the same sign, whereas
partial_j^2 is unchanged. Under a permutation their indices are
permuted. Hence D_j(t), the plane averages C_mu nu(t), and the link
averages E_nu(t) transform with their stated tensor indices. The
contraction sum_nu partial_nu^3 Psi_mu nu defining u^(2), as well as
the first-derivative contraction defining u, transforms as a
one-form. The w_mu(t) are permuted without signs; s_mu nu(t) acquires
the signs of its two indices and is permuted.

The diagonal quadratic form sum_(mu<nu)(w_mu+w_nu)F_mu nu^2 is
unchanged by the induced relabeling. The shear form
sum_(mu<nu)s_mu nu sum_alpha F_mu alpha F_nu alpha is likewise
unchanged: the two signs of alpha cancel, and the remaining two
are precisely those of s_mu nu. This check retains its polarization
factors. The endpoint contraction M(t), exterior derivative d(t)
and their compositions transform between the corresponding form
spaces. Unitary conjugation preserves adjoints, including all
derivatives of multiplication coefficients. Thus every term of
L030's residual formula transforms as in (4), before extracting
the coefficient of t. Extraction preserves the identity. Compact
support removes physical-boundary terms when those adjoints are
evaluated on modes.

### 3. Coordinate swap eliminates both mixed sums

Let S exchange coordinates 2 and 4, including their one-form
components. Since the same even rho occurs in all coordinates,
chi is invariant. Viewing the potentials as antisymmetric tensors,

\[
 S^*(\chi x_1x_3\,dx_1\wedge dx_3)
       =\chi x_1x_3\,dx_1\wedge dx_3,
\]
\[
 S^*(\chi x_2x_4\,dx_2\wedge dx_4)
       =-\chi x_2x_4\,dx_2\wedge dx_4.
\]

Consequently Q_i^A and N^A are even under U_S, while Q_i^B and N^B
are odd. The swap preserves Z and both eigenvalues in (1). In the
chosen one-form basis U_S f_k=f_(S k) with no sign: it permutes
components and scalar sine/cosine factors. In particular it swaps
k_2,k_4 when k is in Z. Reindexing k and ell by this involution
multiplies F_i(alpha,beta) by epsilon_alpha epsilon_beta, where
epsilon_A=1 and epsilon_B=-1. Each mixed sum equals its negative,
and hence vanishes. Linearity now proves (2). This is cancellation
between complete mode orbits; it does not assert that each mixed
matrix product vanishes individually.

### 4. Reflections restrict parity but retain nonzero axial modes

Let R_j reflect coordinate j. Both split potentials are invariant
as antisymmetric tensors: reflecting one of the two participating
coordinates changes both its factor x_j and its covector dx_j,
and reflecting either other coordinate leaves its even rho unchanged.
Equation (4) thus makes each Q_i^alpha and N^alpha commute with U_Rj.

In L008's relative basis, a normal component uses a cosine in its
own direction and sine factors in the other three. A sine of index
k_j acquires (-1)^(k_j+1) on reflection about zero. A cosine acquires
(-1)^k_j, including the constant cosine of index zero. In the normal
case pullback also reverses the one-form component. Thus in every
case, independent of component,

\[
 U_{R_j}f_k=(-1)^{k_j+1}f_k.                    \tag{5}
\]

A matrix entry of an operator commuting with this involution is
zero when its two eigenvalues differ. Applying this to each Q and
N proves (3). Since k_1=0, ell_1 must be even. A relative mode with
component other than 1 uses a sine in direction 1, whose index is
positive; its allowed even indices therefore start at 2. Only
component 1 can have ell_1=0, precisely the modes in Z.

### 5. The 13 sector has no doubly axial-zero entry

We verify the global compression, rather than using only the affine
core test. For the 13 potential, u^A_2=u^A_4=0, and u^A_3 is an
axial total derivative of a compactly supported function. Its
order-t correction is an axial third derivative of that function.
Both have zero axial integral. Hence every transverse averaged
velocity bar u_j(t) in L031(4) is zero. The axial integral of w_1(t)
also vanishes by compact support. The transverse averaged diagonal
and shear weights in L031(5)–(6) are therefore zero on the whole
transverse cube, including the transition region.

For an axial-zero component-1 input, shear pairs involving index 1
have no common nonzero curvature component, as in L031's compression
calculation. Thus J*Q_i^A(t)J=0 for both i, and the compressed K(t)
in L031(4) is zero. Since L(t)J=J mathcal L(t), its compressed
symmetric action variation is zero too, giving J*N^A J=0 after
coefficient extraction. In particular (Q_i^A)_(k ell)=0 whenever
both labels are in Z. The preceding parity argument shows that all
remaining labels contributing to F_i(A,A) have ell_1>=2. This
proves the final restriction without removing any surviving mode.

The general flow and stress-matching sources in the saved SPECIALIZE
assessment are reused within their recorded scopes; none assigns a
value to this fixed-box residual pairing. The argument here verifies
the tensor covariance and mode sectors of the particular stencil,
rather than reproving perturbative flow renormalizability. The
specialization is local progress; originality beyond checked sources
is not certified.

## Mathlib

Coverage of the complete signed-functional reduction: not checked.
Coverage of supporting unitary conjugation, reflection eigenspaces,
and absolutely convergent reindexing: not checked. No full matching
Mathlib theorem or certified sign of either functional is asserted.
