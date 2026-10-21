# L142 — Exact curvature witness stops the mixed-calibration quartic bound

## Hypotheses

Retain L071/L131's hypothetical locally free rank-two bundle F on the
identically marked K3 product X, slope-polystable at the common product
metric, with integral c_1(F)=0 and
c_2(F)=14e_1+21e_2+tau_D. In particular tau_D^2=156e_1e_2,
Dh=2lambda h, s=q(h,h)>0 and 1<lambda<5/4. Existence of F is not assumed
as an established result. L131 supplies its conditional actual SU(2)
connection and the volume and mixed pairing conventions.

For the algebraic test alone let V=H direct sum H have the Euclidean
product metric and product complex orientation. Let W be the real space
of two-forms invariant under simultaneous quaternionic rotations, the
ten-dimensional module in Fowdar's Section 2, (2.6)–(2.7), cited below.
Let T_1,T_2,T_3 be orthonormal in su(2) for -tr(AB), and allow every
K=sum_j T_j alpha_j with alpha_j in W. Define, with even-form wedge
multiplication in the determinant,

    C(K) = [det(1+iK/(2pi))]_4,
    Q(K) = *(C(K) wedge C(K)),
    L(K) = *(C(K) wedge Psi),
    Psi = omega_{I,1} wedge omega_{I,2}.

The star is for the stated metric and orientation. No weak positivity,
Hodge self-duality, nonzero individual coefficients, or realization as
curvature of the prescribed global F is imposed on this universal test.

## Conclusion

The characteristic threshold in the approved test is exactly

    gamma_req = 93/(2lambda^2) > 744/25 > 0.

There is an exact admissible triple with

    Q(K)=0,  L(K)=1/(2pi^2),  Q(K)/L(K)^2=0.

Consequently no universal inequality Q(K)>=gamma L(K)^2 holds for
any gamma>0, and in particular none holds above gamma_req. This stops
only the registered fixed-Psi quartic obstruction. It does not exclude
F, establish F, assert that this triple occurs in F, or settle the
universal rational Hodge conjecture. Other functionals and extra global
curvature constraints have not been tested.

The outcome is NEGATIVE / POTENTIALLY_NEW under the prior EXPLORE
assessment. The local specialized witness was not matched in that
bounded source comparison; this is not a certified originality claim.
The separate step-450 critical audit below preserves the result and its
limited stop conclusion; the audit is EXPLORATION / REPRODUCTION.

## Proof

### Normalization and the conditional downstream comparison

Import Chern–Weil from Xianzhe Dai, *Lectures on Dirac Operators and
Index Theory*, notes dated 7 January 2015,
[Theorem 3.2.3 and (2.11), printed pp. 43–44](https://web.math.ucsb.edu/~dai/book.pdf#page=43).
The invariant determinant defines closed forms representing the Chern
classes of a unitary connection. Its homogeneous-degree definition is
used here; the suspect expanded c_2 formula on p. 45 is not used.

Over the commutative ring of even forms, a trace-zero two-by-two matrix
A satisfies det(1+A)=1-tr(A^2)/2. Set A=iK/(2pi). Since
tr(T_j T_k)=-delta_jk, this gives directly

    C(K)=tr(K wedge K)/(8pi^2)
        =-(alpha_1^2+alpha_2^2+alpha_3^2)/(8pi^2).       (1)

This is the determinant convention specified in the assessment. In
particular its sign agrees with the surface ASD case: a nonzero ASD
alpha has alpha^2 negative in the surface complex orientation, so
-(alpha^2)/(8pi^2) has positive charge. The theorem itself is imported;
(1) is its necessary exact-rank normalization, not a reproof.

L071's full square, including all of the mixed tensor, gives

    J = integral_X c_2(F)^2 = 2*14*21+156 = 744.

Indeed e_i^2=e_i tau_D=0 by factor degree and integral_X e_1e_2=1.
L131's pairing and volume give

    M = integral_X c_2(F) Psi = 2lambda s,
    V_X = (s/2)^2 = s^2/4.

Thus J V_X/M^2=744/(16lambda^2)=93/(2lambda^2). From
0<lambda<5/4 the strict lower bound is 744/25.

To specify precisely the proposed use, if the universal inequality held
with gamma>0, Chern–Weil applied to the actual conditional connection
would give integral_X Q=J and integral_X L=M, with Riemannian volume
measure. The elementary integral Cauchy–Schwarz inequality would imply

    J >= gamma integral_X L^2 >= gamma M^2/V_X.

Hence gamma>gamma_req would contradict the characteristic data. This
calculation uses no replacement of an integral of a product by a product
of integrals. It identifies the threshold, not a valid inequality.

### Exact invariant triple

Choose oriented orthonormal coframes x_0,...,x_3 and y_0,...,y_3 on
the two quaternionic summands such that

    omega_{I,1}=x_0 x_1+x_2 x_3,
    omega_{I,2}=y_0 y_1+y_2 y_3,
    vol=x_0 x_1 x_2 x_3 y_0 y_1 y_2 y_3.

Juxtaposition of forms denotes wedge throughout. For clarity, on each
factor the pullbacks on one-forms may be chosen as

    I*: (x_0,x_1,x_2,x_3) -> (-x_1,x_0,-x_3,x_2),
    J*: (x_0,x_1,x_2,x_3) -> (-x_2,x_3,x_0,-x_1),

with the same formulas for y and K=IJ. These conventions have the
stated Kähler forms and complex orientation.

Put z_i=x_i+y_i and

    alpha=z_0 z_1-z_2 z_3,    beta=z_0 z_1 z_2 z_3.

The addition map (u,v)->u+v is quaternionic-linear. On its target
H, the two-form epsilon_0 epsilon_1-epsilon_2 epsilon_3 is ASD:
star(epsilon_0 epsilon_1)=epsilon_2 epsilon_3. It is invariant under
the common quaternionic rotations, as is also checked directly by the
I* and J* formulas. Equivalently its skew endomorphism commutes with
I and J, hence with every unit quaternion generated by them. Pullback
along addition therefore places alpha in W. Addition need not be an
isometry for this invariance argument.

This uses precisely the invariant-form characterization in Udhav Fowdar,
*Examples of Deformed Spin(7)-Instantons/Donaldson–Thomas Connections*,
Commun. Math. Phys. 405 (2024), article 183,
[Section 2, (2.5)–(2.7)](https://link.springer.com/article/10.1007/s00220-024-05060-0).
No Spin(7) equation or four-form positivity consequence is imported.
The explicit equivariant pullback verifies this witness's specialization
rather than attempting to reprove the representation theorem.

Take T_1=diag(i,-i)/sqrt(2), which has -tr(T_1^2)=1, and complete it
to an orthonormal basis of su(2). Set

    alpha_1=alpha,    alpha_2=alpha_3=0,    K=T_1 alpha.

A universal assertion over all three coefficients must include this
triple. One nonzero coefficient does not change the two-dimensional
coefficient representation or impose a global splitting of F.

The actual matrix determinant can additionally be checked without any
trace identity: its diagonal entries are
1-alpha/(2sqrt(2)pi) and 1+alpha/(2sqrt(2)pi), giving exactly
1-alpha^2/(8pi^2). Since alpha^2=-2beta, (1) becomes

    C(K)=beta/(4pi^2).                                  (2)

### Full exterior-product calculation

The decomposable form beta uses only the four independent forms z_i,
so beta^2=0 identically. Therefore Q(K)=0, with no discarded terms.
To evaluate the other functional, only the real (2,2) factor-bidegree
part of beta can pair with Psi. Expanding Psi gives

    Psi=(x_0 x_1+x_2 x_3)(y_0 y_1+y_2 y_3).

In the full expansion of beta, exactly two terms can contribute to
beta Psi: x_0 x_1 y_2 y_3 pairs with x_2 x_3 y_0 y_1, and
x_2 x_3 y_0 y_1 pairs with x_0 x_1 y_2 y_3. Both terms have
coefficient +1 in beta: moving the two y forms past the two x forms
has even sign. Both resulting top forms equal +vol. Every other term
repeats a one-form or has excess degree in one factor. Thus

    beta Psi=2vol,
    C(K) Psi=vol/(2pi^2),
    L(K)=1/(2pi^2) != 0.                               (3)

In particular the mixed pairing does not vanish merely because C(K)
is decomposable. The forms z_i are not declared orthonormal; all stars
and coefficients in (2)–(3) use the original product orthonormal frame.
For any gamma>0 the proposed inequality at this triple would read
0>=gamma/(4pi^4), which is false. The actual ratio zero is strictly
below gamma_req>744/25. This establishes the stated stop without an
optimization, conjectured best constant, or curvature-realization claim.

An independent exact exterior-algebra check is reproducible by
`python3 scripts/mixed-calibration/check_quartic_witness.py`.
It writes `scripts/mixed-calibration/quartic_witness_certificate.json`:
all nine checks pass, including I,J,K invariance, the complete square,
the mixed top coefficient, product complex orientation and the full
characteristic number. The displayed proof establishes the result;
this finite check only corroborates its signs and arithmetic.


### Separate critical audit — 2026-10-21, step 450

The unchanged pre-invocation EXPLORE assessment is
`drafts/literature/2026-10-20-mixed-calibration-witness-critical-audit.md`.
This audit is RESEARCH / EXPLORATION / REPRODUCTION, actual task
proof_audit. It finds no substantive error, stronger exclusion or global
realization. The original witness's source-comparison classification
is preserved; checking it again is not another mathematical advance.
The cited Fowdar and Dai inputs are reused within their approved scopes.

**Full invariant domain.** On the target quaternionic line let A be the
skew endomorphism defined by a(u,v)=g(Au,v), for
 a=epsilon_0 epsilon_1-epsilon_2 epsilon_3. The displayed I* sends each
of epsilon_0 epsilon_1 and epsilon_2 epsilon_3 to itself; J* sends them
to -epsilon_2 epsilon_3 and -epsilon_0 epsilon_1, respectively. Thus
I*a=J*a=a. Since I and J are orthogonal, I^{-1}AI=A and J^{-1}AJ=A.
Consequently A commutes with I,J,IJ and every unit quaternion
r_0 id+r_1 I+r_2 J+r_3 IJ. This proves continuous quaternionic
invariance, not merely invariance under the finite group generated by
I and J. Addition intertwines these actions, so its pullback alpha
belongs to the required W. Its metric distortion is irrelevant to
invariance and is not used to compute a Hodge star. The coefficient
T_1 is skew-Hermitian and trace free, with -tr(T_1^2)=1; two zero
coefficients are permitted by the actual universal quantifier.

**Determinant, degree and signs.** The entries of iK/(2pi) have even
degree and commute as scalar forms, so the ordinary two-by-two
determinant identity applies despite noncommuting coefficient matrices.
Its degree-four term is -tr((iK/(2pi))^2)/2, namely
tr(K wedge K)/(8pi^2). In the coefficient expansion all cross traces
vanish by orthonormality. For this particular diagonal K the direct
product (1-alpha/(2sqrt(2)pi))(1+alpha/(2sqrt(2)pi)) independently
fixes the same negative sign and factor. Writing A_0=z_0 z_1 and
B_0=z_2 z_3 gives A_0^2=B_0^2=0 and A_0 B_0=B_0 A_0=beta, hence
alpha^2=-2beta and C=beta/(4pi^2). Decomposability forces beta^2=0.

For the complete top pairing, the Psi terms x_0 x_1 y_0 y_1 and
x_2 x_3 y_2 y_3 require beta complements selecting both x_i and y_i
for some index i, which beta cannot contain. The remaining Psi terms
have exactly the complements x_2 x_3 y_0 y_1 and x_0 x_1 y_2 y_3.
Each complement has coefficient +1 in beta; reordering each full
product to the original product volume has even sign. Thus beta Psi
is exactly 2vol. Also omega_1^2 omega_2^2=4vol, verifying the complex
orientation used by the star. These checks preserve Q=0 and
L=1/(2pi^2), without treating the z_i as an orthonormal frame.

**Full characteristic comparison.** L071's retained full operator
has divisor eigenvalues 2lambda_i and 4, and six copies of each
2lambda_i on T. For z^3+z^2-2z-1, Vieta gives sum lambda_i=-1 and
sum_{i<j}lambda_i lambda_j=-2, hence sum lambda_i^2=5.
The complete trace square is therefore 4*5+16+6*4*5=36+120=156.
Self-adjointness and even factor degree identify this with the full
mixed tensor square. The pure terms contribute 2*14*21=588; all
pure/mixed cross terms and pure self-squares vanish by factor degree.
Thus J=744, with no rational N/T projection treated as integral.
The full dual-basis contraction against h tensor h is q(Dh,h)=2lambda s.
The pure terms do not pair with Psi. Each K3 volume is s/2, so the
product volume is s^2/4 and J V_X/M^2=93/(2lambda^2)>744/25.

L131 supplies the actual conditional determinant-trivial compatible
connection, so its coefficients do lie in the tested domain if F
exists. Dai's determinant Chern--Weil theorem applies to its closed
Chern form; Psi is closed and the product is compact. Hence a valid
positive pointwise bound would integrate to J>=gamma integral L^2,
and Cauchy--Schwarz gives integral L^2>=M^2/V_X. Only a strict
constant gamma>gamma_req would give a contradiction. The exact witness
instead refutes every positive gamma on the full domain. Global
irreducibility does not exclude a one-coefficient value from that
universal algebraic domain, and no occurrence in F is asserted.

The existing script's entire wedge and pullback implementation and all
certificate forms were inspected. Its rerun passes 9/9 checks with no
failures, preserving the certificate at
`scripts/mixed-calibration/quartic_witness_certificate.json`.
The script corroborates the proof; its threshold strings and hard-coded
156 do not independently prove the characteristic calculation, which
was checked above using L071/L131. No new functional, optimizer,
curvature-realization theorem or global nonexistence conclusion enters.

## Mathlib

Full matching coverage of the specialized witness, determinant/form
normalization and conditional threshold has not been checked. No
absence or formal verification is claimed. The informal proof imports
the named Chern–Weil theorem and invariant-form characterization and
writes out the complete finite exterior calculation.
