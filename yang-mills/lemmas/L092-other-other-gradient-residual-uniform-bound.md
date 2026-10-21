# L092 — The gradient diagonal residual is uniformly bounded after whitening

## Hypotheses

Keep exactly L091's finite SU(2) forest Gaussian, actual L010 probes
i=3,6, actual L018 residual A_0, straight lower-rooted direction-1
forest, relative all-face pinned box, admitted even N, a=8/N and
tau=1/16. Take the bare small-coupling coefficient at fixed mesh
before refinement. Use ordinary stored-coordinate transposes and
norms. Keep every interior axial level, transverse end row, ordered
plaquette pair including coincidences and exterior heat mode.

Import K_g=M tensor P, V_g=Pcal V Pcal and L091's whitened
blocks A_k,J_k,D_k,E,F,H. Here M_st=min(s,t), P=T G T^T,
G=(T^T T)^(-1), and E=K_g^(-1/2) V_g K_g^(-1/2) on im Pcal.
The letter E in this formula is L091's residual block; below the
space of interior transverse links is denoted mathcal E.

Use the compact displacement and exact endpoint/clover filters of
L065. In particular its conclusion (1), proved with all axial edge
frequencies and end edges retained, applies to

    A_11=I_1^T A_0 I_1,
    H_T=I_N tensor Delta_0,   Delta_0=T^T T,
    |f^T A_11 f|<=C f^T H_T f.                         (1)

This is the scalar diagonal form statement of L065, not an assumed
extension of its displayed axial-zero-to-all-axial operator to vectors.

## Conclusion

Uniformly over sufficiently fine admitted meshes,

    -C K_g<=V_g<=C K_g,       ||E||<=C.                 (2)

Consequently one diagonal crossed trace in L091(4) satisfies

    R_E(i,N)=sum_(k,l)c_(i;kl) Tr(J_k^T E J_l),
    |R_E(i,N)|<=C_i N^3.                               (3)

Its a^3-scaled values are bounded; no convergence, sign, vanishing
or compensation is claimed. The same bound also sharpens the already
subleading two-gradient sector to |T_gg|<=C_i N.

L091's other diagonal crossed trace Tr(J_k H J_l^T) and the pair
2 Tr(J_k^T F D_l) still have only the prior O(N^4) and O(N^(7/2))
generic bounds. Its gradient-base F pair remains O(N^3). Nothing
here controls F by the scalar form (1), or supplies the joint limit
-4 gamma D_i required before the outside factor 3. The complete
other/other coefficient, other response jets, N^2 remainders, slower
powers/logarithm, matching, interacting error <=c_box/2, continuum
axioms, reflection positivity, infrared control and finite positive
mass remain unresolved. No candidate solution exists.

## Proof

### 1. Specify the actual gradient row and both pinned interval ends

Let mathcal V be the tensor product of the N-1 interior axial vertices
and the transverse pinned vertex space, mathcal A the tensor product
of the N axial edges and that transverse vertex space, and mathcal E
the interior-level transverse link space. Let I_T embed mathcal E
into full relative one-forms with component 1 zero, and I_1 embed
mathcal A as component 1. They exhaust the four link components.

Write B for the axial prefix matrix tensored with the transverse
vertex identity. Its scalar entries are

    B_(s,ell)=1_(ell<s),  1<=s<N, 0<=ell<N.

Let B0 be the axial edge-to-vertex difference of L085, with
(B0 h)_s=h_s-h_(s-1). On the exact finite interval,

    B0 B^T=-I,  B B^T=M tensor I,
    L_D=B0 B0^T,  L_E=B0^T B0.                         (4)

For the first identity, row s of B^T is the vector h_s from
L085(7)–(8), and B0 h_s=-e_s. The other identities follow from
the overlap of the two prefixes and the pinned difference stencil.
L_E includes its constant axial edge mode and endpoint diagonal 1.
There is no deletion of the upper edge or replacement by an infinite
interval, even though the prefixes stop before that edge.

Put Tcal=I_(N-1) tensor T, G_v=I_(N-1) tensor G, and

    R_v=(L_D tensor I+I tensor Delta_0)^(-1),
    Sigma_1=(L_E tensor I+I tensor Delta_0)^(-1),
    R_E=(L_D tensor I+I tensor Delta_T)^(-1).

L026's exact component tensor decomposition gives
Sigma=I_T R_E I_T^T+I_1 Sigma_1 I_1^T. L085's forest lift gives
the actual gradient row map

    H_g=Pcal I_T^T+Tcal B I_1^T,
    K_g=H_g Sigma H_g^T,
    V_g=H_g Sigma A_0 Sigma H_g^T.                     (5)

The last identity uses L018's gauge-invariant residual and quotient
law. Only the linear rows of the already contracted expression are
lifted. No unmodified nonlinear cubic is transferred to the Hodge law.
All transverse end edges are included in T and Pcal.

For clarity choose the full vertex-to-link incidence mathscr D with
tail-minus-head orientation. Its tensor expression is

    mathscr D=I_T Tcal+I_1 (B0^T tensor I).

It has exactly the relative gauge-gradient image of L018's D_0
(the overall sign follows the incidence convention). Thus
A_0 mathscr D=0 and mathscr D^T A_0=0. In this orientation (4)
also directly checks H_g mathscr D=Tcal-Tcal=0. Both axial
boundary vertex values are pinned, as required for this gradient.

### 2. Identify the covariance column modulo an exact gauge gradient

On each complete transverse vertex eigenmode lambda>0, set
R_D(lambda)=(L_D+lambda I)^(-1) and
R_A(lambda)=(L_E+lambda I)^(-1). The exact identity is

    R_A(lambda) B^T-B^T/lambda
                     =B0^T R_D(lambda)/lambda.        (6)

Indeed multiply the left side by L_E+lambda I. The result is
-L_E B^T/lambda=B0^T/lambda by B0 B^T=-I. Multiplying the
right side gives the same expression, because
(L_E+lambda I) B0^T=B0^T(L_D+lambda I). Invertibility proves
(6). This calculation includes lambda's full transverse spectrum,
the constant axial edge mode and both interval endpoints.

Define C=Tcal G_v B, a map from mathcal A to mathcal E. Then

    H_g Sigma=C I_1^T+Tcal G_v R_v mathscr D^T.         (7)

To verify its transverse block, use the full relative intertwining
Delta_T T=T Delta_0, imported through L085, to obtain

    Pcal R_E=Tcal G_v R_v Tcal^T.

For its component-1 block, transpose (6) on every transverse vertex
eigenmode. It gives

    B Sigma_1-G_v B=G_v R_v (B0 tensor I).

Multiplication by Tcal is precisely the component-1 part of (7).
The transverse co-closed modes have zero image under both sides of
the transverse identity. Thus these two block checks prove (7) on
the full relative link space, without assuming an input is smooth
or omitting a pinned row. G_v and R_v commute since they are tensor
spectral functions on mathcal V; no variable multiplier is commuted.

Insert (7) and its transpose into (5). The two gauge-gradient
corrections vanish against the actual symmetric A_0, yielding

    V_g=C A_11 C^T.                                   (8)

The representative C^T y is an arbitrary component-1 field. It may
contain all axial frequencies. Equation (8) is an identity modulo
gauge gradients of covariance columns, not a claim that the original
forest gradient field has only component 1, or that F vanishes.

### 3. Its transverse energy is exactly the prefix covariance

Since B acts only axially, B H_T=(I_(N-1) tensor Delta_0) B.
Using (4) and G=Delta_0^(-1) therefore gives the exact identity

    C H_T C^T
       =Tcal G_v (M tensor I) Tcal^T
       =M tensor P=K_g.                               (9)

For any y in mathcal E apply L065(1) to f=C^T y. Equations
(8)–(9) give |y^T V_g y|<=C y^T K_g y. This is the first
assertion of (2). Conjugate by the positive inverse square root of
K_g on im Pcal; the spectral theorem for the symmetric result proves
||E||<=C. No inverse is asserted on the co-closed nullspace of K_g.

The off-diagonal row remains explicit rather than being removed by
this specialization. With H_h=Qcal I_T^T, the tensor covariance gives
Sigma H_h^T=I_T K_h. Equation (7) consequently yields

    Pcal V Qcal=C (I_1^T A_0 I_T) K_h.                (10)

The middle matrix includes every cross-component generator output
and both symmetric generator orientations in A_0. Bound (1) is a
diagonal scalar form bound; it supplies no estimate on that middle
matrix. Polarization of (1) controls only two component-1 inputs.
In particular it cannot be applied to (10)'s transverse right input.
No positivity of A_0, block diagonalization or automatic F reduction
is assumed. Equation (10) is a concrete retained input for a later
joint trace test, not an additional bound on F.

### 4. Apply the actual exterior heat bounds

L091(9)–(12) supplies a mesh-independent polynomial p with

    ||J_k||_HS<=C p(k) N^(3/2),
    ||A_k||_HS<=C p(k) N^(1/2),
    sum_(k,l)|c_(i;kl)|p(k)p(l)<=C_i.

Hilbert–Schmidt Cauchy–Schwarz and (2) give

    |Tr(J_k^T E J_l)|<=C p(k)p(l) N^3.

Summing the complete exterior expansion proves (3), with every heat
mode and both probes retained. Likewise T_gg is the complete sum
of Tr(A_k E A_l^T) in L091(15), so the same calculation gives its
stated O(N) sharpening. No exterior orientation, coincidence or
residual placement is deleted. L091 fixes all factors: R_E belongs
to R_i before L085's outside factor 3, rather than to the mixed
group with factor 6.

This is one bounded RESEARCH / REPRODUCTION attempt under the unchanged
assessment `drafts/literature/2026-10-10-other-other-cubic-leading-scale.md`.
It imports L065's existing scalar theorem and justifies the previously
unproved row specialization by (6)–(9); it does not reprove that scalar
theorem. This is local finite Gaussian progress, with no originality
claim beyond the sources checked. No numerical diagnostic or IEEE
assumption is needed for (2)–(3); any later comparison with D_i still
retains L082's saved-table/IEEE qualifications.

### 5. Supplemental exact interval check

Run from the notebook:

    PYTHONDONTWRITEBYTECODE=1 python3 scripts/combined-ward-response/check_other_other_gradient_lift.py

The complete certificate is
`scripts/combined-ward-response/other-other-gradient-lift-certificate.json`.
All 12 cases N=2,4,6,8 and lambda=1/7,1,5 have actual maximum
entry error 0 against required error 0, with no failures. Exact
rational arithmetic checks B0 B^T=-I, lambda times (6), L_E's
constant mode, and (9) in scalar-potential coordinates, where the
pure representative is B/lambda and its covariance is M/lambda.
Every error entry is retained in the certificate. These are endpoint
and normalization checks; they neither test a cutoff limit nor replace
the analytical identities for the full transverse spectrum and actual
residual in sections 1–4.

## Mathlib

Full matching gradient-row identity and bound: **not checked**.
Supporting finite spectral theorem, resolvent intertwining and
Hilbert–Schmidt inequalities: **not checked**. Unknown availability
is not evidence of absence. The proof is exact finite-matrix algebra
plus the explicitly applicable scalar input L065, not a continuum
Ward or flow-finiteness theorem application.
