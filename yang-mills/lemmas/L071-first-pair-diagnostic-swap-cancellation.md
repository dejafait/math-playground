# L071 — Coordinate swap removes the diagnostic's Psi_24 probe sector

## Hypotheses

Keep L070 section 6's diagnostic (9) at an admitted even mesh N,
a=8/N, tau=1/16, and its ordinary stored relative one-cochain
coordinates. In particular retain its upper positive (1,mu) curvature
rows U_mu, centered transverse lifted-link rows V_mu, all levels
1<=s<N, every normal end edge, and the prescribed zero boundary
evaluations. The right lift is precisely L026's direction-1,
lower-rooted forest retraction with separately pinned upper vertices.
Sigma=Delta^(-1) and H=exp(-tau Delta/a²) are L018's full
four-dimensional Hodge operators.

Split L008's antisymmetric potential as Psi=Psi^A+Psi^B, where
Psi^A has only its 13/31 entries and Psi^B only its 24/42 entries.
For i=3,6 let Q_i^A,Q_i^B be the symmetric stored-coordinate
quadratic matrices obtained from L008(2), using the displacement
and strain of the indicated potential separately. All coefficients
are formed by the same central differences as in L008. Then
Q_i=Q_i^A+Q_i^B by linearity of the forms in those coefficients.
Keep the diagnostic's weight u_(a,1) fixed at its actual value.
Define D_(i,a)^alpha by replacing only Q_i with Q_i^alpha in
L070(9) or its identical finite trace (10), alpha=A,B.

This concerns a Gaussian diagnostic, not the original first-pair
trace, any nonlinear probe jet, or the complete response coefficient.

## Conclusion

At every admitted mesh and for both i=3,6,

    D_(i,a)^B=0,                 D_(i,a)=D_(i,a)^A.        (1)

The cancellation includes the full relative spectrum and all axial
levels. It establishes no sign, limit or bound on D_(i,a)^A, and no
coefficient, O(N²) bound or logarithm for L070's original trace.

## Proof

### 1. The swap preserves the relative Hodge operators

Let S exchange coordinates 2 and 4 and leave coordinates 1 and 3
fixed. Its pullbacks T_0,T_1,T_2 on relative lattice cochains include
the orientation of the mapped cells. Each is an orthogonal signed
permutation in the ordinary stored-coordinate inner product; it
preserves the boundary-pinned domains. T_j²=I. Put T=T_1.

The incidence matrices obey D_0 T_0=T D_0 and D_1 T=T_2 D_1:
both sides evaluate the same oriented endpoint difference or oriented
plaquette boundary. Orthogonality therefore gives

    T Delta T^T=Delta,       T Sigma T^T=Sigma,
    T H T^T=H.                                           (2)

The inverse exists by L018. The heat identity follows from the
finite-dimensional exponential. There is no restriction to axial-zero
modes or exchange with a cutoff limit in (2).

### 2. The actual diagnostic's bilinear matrix is even

Write sigma for the index permutation (2 4), and write Sy for the
same permutation on transverse vertex triples. L026's pinned prefix
potential is

    phi_x(s,y)=sum_(ell=0)^(s-1) x_1(ell,y),  1<=s<N,

with zero values at every boundary vertex. Since S fixes component 1,
the axial coordinate and its lower and upper faces,

    phi_(Tx)(s,y)=phi_x(s,Sy),       R_F T=T R_F.           (3)

The second identity follows from the first and incidence covariance.
It includes transverse boundary vertices and the separately pinned
upper face; no smooth extension of that face is being assumed.

Let U_mu,V_mu now denote exactly the row maps in the hypotheses,
not the cochain pullbacks. Because 1<mu for mu=2,3,4, S sends the
positive (1,mu) orientation to positive (1,sigma(mu)). It permutes
their transverse endpoint averages and, by (3), the lifted-link
averages. Thus, including the zero boundary conventions,

    (U_mu Tx)(y)=(U_(sigma(mu))x)(Sy),
    (V_mu Tx)(s,y)=(V_(sigma(mu))x)(s,Sy).                (4)

The same statement holds for normal end edges: swapping axes maps
the included endpoint pair to the included endpoint pair and maps a
zero boundary value to zero. Factors 1/a² and 1/a are unchanged.

Only Psi^A contributes to u_(a,1), namely
u_(a,1)=nabla_3^c(chi x_1x_3). The product chi uses the same rho in
coordinates 2 and 4; neither the central difference in direction 3
nor its argument changes under S. Consequently
u_(a,1)(s,Sy)=u_(a,1)(s,y). The level factor sa is also invariant.
Substitute (4) into the complete finite sum defining P_a in L070(9)
and relabel y and mu. This proves

    P_a(Tx,Tz)=P_a(x,z).                                 (5)

If P_a(x,z)=x^T M_a z, (5) means T^T M_a T=M_a. It holds for
every pair of stored inputs, so also
T^T M_a^sym T=M_a^sym. No symmetry of M_a itself is assumed.

### 3. The Psi_24 part of either actual probe is odd

The potential parities used in L032 are exact on this grid too:

    S^*Psi^A=Psi^A,             S^*Psi^B=-Psi^B.          (6)

Indeed the scalar factors chi x_1x_3 and chi x_2x_4 are invariant,
whereas dx_2 wedge dx_4 changes sign. Central differences commute
with relabeling of coordinates. Hence displacement, diagonal strain
and shear computed from S^*Psi are exactly the pullbacks of those
computed from Psi, with their respective tensor indices.

For completeness this covariance applies separately to L008's two
discrete representatives. Under S the four plaquettes through each
vertex in a plane are permuted, and a reversed plane orientation
changes F's sign. In the triplet this sign disappears in each F²;
the coefficient w_mu+w_nu is relabeled. Its average of four squares
is retained. In the shear, clover averages transform as an
antisymmetric two-tensor. In
sum_alpha bar F_(mu alpha) bar F_(nu alpha) the contracted alpha
indices transform together, giving the same symmetric two-index
transformation as the coefficient s_mu nu. For an unordered pair
mu<nu, reversing its order merely interchanges the two commuting
real factors. Thus the shear sum and its normalization are retained.
All vertex sums are permuted within the relative domain.

It follows for either form that
q_(i,a)(Tx/a;Psi)=q_(i,a)(x/a;S^*Psi). Since T=T^T and
Q_i depends linearly on Psi, equality of these quadratic forms gives

    T Q_i^A T^T=Q_i^A,          T Q_i^B T^T=-Q_i^B.       (7)

Any additive Wick-centering constants do not alter these quadratic
matrices or the finite diagnostic definition.

### 4. Finite trace cancellation

Set K_i^B=Sigma H Q_i^B H Sigma. Equations (2) and (7) imply
T K_i^B T^T=-K_i^B. Equations (5) and L070(10) therefore give

    D_(i,a)^B
      =Tr[M_a^sym K_i^B]
      =Tr[T M_a^sym K_i^B T^T]
      =-Tr[M_a^sym K_i^B]
      =-D_(i,a)^B.

These are traces of finite real matrices, so D_(i,a)^B=0.
Linearity in Q_i proves (1). In particular it is cancellation of
complete symmetry orbits, not a claim that individual heat-mode
summands or samples vanish.

The row averages and sa remain the diagnostic's chosen maps.
Nothing here identifies them with the original two-link paths or
controls their replacement error, axial normalization, variable
coefficients or physical-boundary trace remainders. Those are still
independent obligations before using (1) for an original coefficient.

## Mathlib

Coverage of the full specialized diagnostic cancellation: **not
checked**. Supporting finite orthogonal conjugation, incidence
covariance and trace invariance: **not checked**. No full matching
theorem or absence claim is asserted. The ready SPECIALIZE assessment
is reused; this is a reproduction of finite symmetry algebra for the
specified discrete representatives. It does not reprove general flow
renormalizability or extend the cited bulk matching theorems to this
physical-boundary problem.
