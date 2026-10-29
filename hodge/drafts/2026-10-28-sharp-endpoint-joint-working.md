# Joint endpoint feasibility — step 602 working record

2026-10-28. RESEARCH / proof_attempt. Invocation-start gate:
`drafts/literature/2026-10-28-sharp-endpoint-joint-bracket-compatibility.md`
(EXPLORE). Only its exact joint finite-data target is being attempted.
Existing notebook changes and ATTEMPTS/092–095 are preserved.

Main gap: uniform primitive algebraic realization; even existence of the
conditional equality kernel F is unresolved. Intermediate target: an
exact simultaneous quadratic witness or incompatibility at s=781,t=46.
A witness would park exclusion using just the retained identities; a
contradiction could exclude this conditional endpoint. Neither settles F
or the Hodge conjecture. Stop if the complete retained checklist cannot
be instantiated; name the missing datum rather than claim exclusion.

## Saved partial reduction, not yet a checked result

Use p=2*pi*i, delta=delta_B, gamma=delta/p^2, d=2*lambda,
and a=d^2-16+14s. In the fixed point coordinates let b_z(h) denote
B_z(rho_z(h),rho_z(h)), and C(h)=sum_z b_z(h). L168/L169/L178 give
Q_U=delta/d times the coordinate dot product and w_k(z)=p^(-2).
Thus Q_U(beta,w_k)=gamma*C/d.

At the endpoint dim K_N=15. The nondegenerate fourteen-dimensional
image J from L177 and the nondegenerate k-line from L178 exhaust K_N.
If the full residual equations hold, the prospective normal bracket is
v(h)=p*C(h)*g(phi^(-1)k)/a. Its norm would reduce cyclicity to
sum_z b_z(h)^2=14*C(h)^2/a. All signs and both scalar factors still
need checking before this is used. The five domain radical directions
must be handled explicitly; rank equality alone is not their proof.

The fibre construction must retain E_z of dimension 52, weights +2,-2,
both Omega_z and B_z, a two-dimensional B-isotropic but Omega-symplectic
KS plane, Q_z=(ad(h_z)K_z)^perp_Omega, and a 48-dimensional normal
complement containing one common 46-dimensional section space. The
alternating pullback is common to all points. Arbitrary point quadrics
or independent rescalings of their coordinates do not meet the gate.

Current attempt: exploit symplectic linear evaluations in the normal
48-space to realize a constrained family of section quadrics, then test
the exact quartic equation above. This is a prospective construction,
not a claim about actual evaluations or geometric realizability.

## Construction saved before exact verification

Put r=(16-d^2)/14, alpha^2=(s-r)/s and epsilon=r/s. For a primitive
s-th root zeta, at point j use z=zeta^j and
a_j=alpha+z+(epsilon/2)z^(-1), b_j=z^4,
c_j=(1-a_j^2)z^(-4). Then a_j^2+b_j*c_j=1. On each of 23
symplectic coordinate pairs (x_i,y_i), use the evaluation matrix
T_j=[[(a_j+1)/b_j,1],[(a_j-1)/2,b_j/2]]. Its determinant is one
and it should pull back the symmetric split form to
[[-c_j,a_j],[a_j,b_j]]. Thus the common alternating form is retained
and the section quadric is -c_j X+2a_j T+b_j Y, with
X=sum x_i^2, T=sum x_i*y_i, Y=sum y_i^2.

The Laurent supports in all products lie between -12 and 8. Summing
over all 781 roots keeps only the constant coefficient. The intended
identities are sum a_j=s*alpha, sum b_j=sum c_j=0,
sum a_j^2=s and all five other second moments zero. Consequently
sum q_j=2s*alpha*T, sum q_j^2=4s*T^2, exactly the required quartic
identity because a=14s*alpha^2. This is a fixed degree-two map on H;
the auxiliary roots are fixed coefficients, not section variables.

Complete each fibre by a 2-dimensional unused normal symplectic pair
and a 4-dimensional KS block, for 26+26 weight spaces. On that block
take kappa_1=e_+1+e_-2 and
kappa_2=(d/2)(e_-1-e_+2). Their symmetric pairing is zero and
their alternating pairing is d. The planes K and A*K are alternating
orthogonal, with the latter pairing -4d. Hence the ordinary image
is K plus the 48-dimensional normal space, with symmetric radical K.

For the global model retain the actual q,D,phi,k as abstract prescribed
domain data. Set K_N=L_(2mu) plus L_(2nu) plus Ck, endowed with
gamma*q((d-D^2/d)x,y)-(gamma*s/d)q(x,k)q(y,k), and g equal to
the projection along L_d. This is nondegenerate in dimension 15.
The five radical directions have zero image in this model; moreover
at the endpoint their vanishing follows from surjectivity of g and
nondegeneracy, rather than being an added actual-family assumption.
Adjoin the fixed tangent Gram block gamma*d*q and the point block
(delta/d)*dot to construct E and all cohomological inclusion,
projection, residual and Atiyah maps explicitly. Verification pending.

SymPy is unavailable in the current python3 environment. If a symbolic
certificate is used, it will use exact standard-library arithmetic;
no dependency installation or numerical fit is needed.

## Completion

The full construction and proof are canonical in
`lemmas/L179-joint-endpoint-root-of-unity-witness.md`. All five retained
finite-data conditions were instantiated. Outcome NEGATIVE: the exact
witness parks exclusion using those identities alone. This is not an
actual F or an evaluation of its section quadrics. Independent audit
is pending; the prior paragraphs remain the saved working reasoning.

The standard-library script `scripts/joint_endpoint/check_witness.py`
passes 21 exact checks, with complete coefficient evidence in
`scripts/joint_endpoint/L179-exact-certificate.json`. The first run's
wrong expected determinant sign (-4d^2 rather than +4d^2) is preserved
in `scripts/joint_endpoint/L179-first-run-certificate.json`; it was
corrected after inspecting the complete residual and determinant.
All nondegeneracy and global scalar/Gram arguments are in L179.
