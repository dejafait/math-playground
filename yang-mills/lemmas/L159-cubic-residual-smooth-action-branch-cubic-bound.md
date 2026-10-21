# L159 — The smooth-action mixed branch is cubic-bounded

## Hypotheses

Keep L156–L158's hypotheses: SU(2), relative box (-4,4)^4,
a=8/N through admitted even meshes, the straight direction-1
lower-rooted forest, the complete compact displacement and both actual
L010 probes at tau=1/16. Expand at fixed mesh before refinement.
Use their full-link A,L,Sigma,R,Phi,K and h_k=R v_k, the heat
coefficients c_(i;kl), and L157's B_h. All norms and transposes are in
ordinary stored coordinates. A hat denotes the three-color extension.
Keep both insertion subtractions, all action faces, pinned end links,
the upper jump, constant axial prefix and complete exterior heat sums.

Consider exactly L158's second branch

    V_i=sum_(k,l,c) c_(i;kl)
       Tr[Sigmahat Ahat B_(h_k t_c) Khat
                           B_(L h_l t_c)^T Rhat].         (1)

No positivity is assumed for the signed remainder E or either probe.

## Conclusion

For each actual probe, with a mesh-independent constant,

    |V_i|<=C_i N^3.                                     (2)

Together with L158 this yields only

    H_i=T_i+V_i+H_i^EE+O_i(N),
    |T_i|+|V_i|<=C_i N^3.                               (3)

Thus the complete mixed sector is cubic-bounded. Neither branch has a
proved scaled limit here, and H_i^EE remains uncontrolled. O(N^3)
does not prove the requested o(N^3), vanishing, a compensation
coefficient, finer asymptotics or any interacting comparison. No
continuum construction or mass gap follows. This is a finite-matrix
and tensor-energy specialization, without an originality claim.

## Proof

### 1. Keep the covariance order and localize only the residual input

Write Delta=Sigma^-1=L+D_0 D_0^T. Its unscaled norm is bounded,
and L026's spectrum gives ||Sigma^(1/2)||<=C N. Also

    ||Sigma^(1/2) A Sigma^(1/2)||<=C N.                  (4)

To check (4), use L018's actual
A=(L K_a+K_a^T L)/2-Q_3-Q_6. L028's composition in stored
coordinates is K_a=a^-1 E_a M_a C_a D_1, with bounded averaging
and coefficient maps. Since L<=Delta,
||D_1 Sigma^(1/2)||<=1. Moreover L commutes with Delta and
L Sigma L<=L, so ||Sigma^(1/2)L||<=C. Each Q_j is
D_1^T W_j D_1 with bounded W_j (including the shear clovers).
These facts bound the two generator terms by C/a and both
subtractions by C. Since a=8/N, (4) follows. It is a bound for
the complete residual form, not smooth consistency on a rough input.

Choose a diagonal link cutoff chi with norm at most one, equal to
one on the input support of A, and supported in a fixed compact
interior enlargement. L028's complete stencil, including adjoint
coefficient derivatives, gives A chi=A for all sufficiently fine
meshes. On this enlargement L150's actual interior mode lift gives
||h_k||_infinity<=C a p(k) for a fixed polynomial p. Therefore
L157's Tr K<=C N^5 implies

    X_k=Sigmahat^(-1/2) chihat B_(h_k t_c) Khat^(1/2),
    ||X_k||_HS<=C a p(k) (Tr K)^(1/2)
                  <=C p(k) N^(3/2).                    (5)

Here ||Sigma^(-1/2)||=||Delta^(1/2)||<=C, and the endpoint-sum
incidence in B_h has bounded norm. No global O(a) bound across
the upper jump is used. The cutoff changes no trace in (1).

Put q=L h_l=L v_l. L156's action-mode calculation gives a smooth
extension, separately on each link component, satisfying

    ||q||_C^r<=C a^3 p(l),       r=0,1,2,
    D_0^T q=0.                                         (6)

The C^r norm uses physical coordinates. For clarity, q is a bounded
sum of sampled sine/cosine product modes obtained from
a^3 lambda_l^(-1/2) d_a^* d_a f_l. Each derivative raises only
the fixed polynomial in l. This is valid at normal end edges and
does not differentiate the forest jump. The exact second identity
is D_0^T L=0; smoothness alone would not give it.

The factor requiring a prefix estimate is

    Z_l=Khat^(1/2) B_(q t_c)^T Rhat Sigmahat^(1/2).

We will prove

    ||Z_l||_HS<=C p(l) N^(1/2).                         (7)

### 2. The true prefix covariance and its transport sandwich

Set n=N-1, M_st=min(s,t) for s,t=1,...,n, and let G be the
inverse transverse scalar Dirichlet Laplacian. L156's exact formula
gives 0<=K<=Y=M tensor G. L156–L157's full-spectrum estimates give

    Tr K<=C N^5,  ||M||_HS<=C N^2,  Tr M<=C N^2,
    ||G||_HS<=C N^2,                 Tr G<=C N^3.        (8)

In particular ||Y||_HS<=C N^4. The constant axial edge mode is
already included in K; M is a dominating operator, not a replacement
law for the signed remainder or for the full forest covariance.

For any real vertex matrix O, positivity implies

    ||K^(1/2) O K^(1/2)||_HS^2
       =Tr(K O K O^T)<=Tr(Y O Y O^T).                   (9)

Indeed first replace the first K against the positive O K O^T;
then cycle the trace and replace the other K against O^T Y O.
No commutation of O with either positive matrix is required.

Let S be the endpoint-sum incidence and M_q the diagonal link
multiplier. Consider the scalar vertex transport

    O_q=S^T M_q D_0.                                   (10)

Its diagonal at v is (D_0^T q)_v, hence is exactly zero by (6).
If e joins interior vertices v,w, its two off-diagonal entries are
q_e and -q_e, with the signs of the oriented incidence. Thus O_q
is skew, including all contributions from edges with one pinned
endpoint to its canceled diagonal. This statement uses the full
action column on all faces; cutting it off would spoil the identity.

Let J_j be the skew nearest-neighbor vertex matrix in direction j,
with entries +1 on forward neighbors and -1 on backward neighbors,
omitting boundary vertices. Evaluate the smooth component q_j at
vertex positions to obtain a diagonal vertex multiplier m_j.
Comparing each edge midpoint sample with its endpoint sample in
(10), and using (6), gives

    O_q=sum_(j=1)^4 m_j J_j+F,
    ||F||<=C a^4 p(l).                                 (11)

Each row and column of F has bounded degree and entries at most
C a^4 p(l); its diagonal remains zero. Normal end edges are
accounted for by the exact diagonal cancellation, not by extending
a pinned potential nonzero beyond the boundary.

### 3. Variable coefficients in the mixed energy

For any smooth sampled scalar multiplier m with physical C^2 norm
at most b, one has

    ||Y^(-1/2) m Y^(1/2)||<=C b,
    ||Y^(1/2) m Y^(-1/2)||<=C b.                        (12)

Here b also bounds the scalar itself. To justify the finite-boundary
claim, let B be the n by n backward difference:
(B x)_1=x_1, (B x)_s=x_s-x_(s-1). Then
M^-1=B^T B. Let D_T be the complete transverse Dirichlet gradient,
including end edges. Exactly

    ||Y^(-1/2)x||_2=||(B tensor D_T)x||_2.               (13)

The axial boundary in (13) is lower anchored and upper free; it is
not a second Dirichlet condition on M. Multiplication preserves this
domain. Extend x by zero at lower axial and transverse boundary
vertices just for the difference formulas. A two-direction finite
product identity expands the mixed difference of m x into a shifted
m times the mixed difference of x, plus shifted first differences of
m times first differences of x, plus a mixed difference of m times
a shifted x. Explicitly, with corners indexed 00,10,01,11, it is

    m_11(x_11-x_10-x_01+x_00)
    +(m_11-m_10)(x_10-x_00)
    +(m_11-m_01)(x_01-x_00)
    +(m_11-m_10-m_01+m_00)x_00.

There are four terms on each mixed rectangle. Sampled
smoothness bounds their coefficient factors by C b, C b/N and
C b/N^2 respectively. Boundary rectangles obey the same identity,
because the zero x values are retained and m has its smooth extension.
Shifts have bounded multiplicity in the squared-norm sums.

The lower-anchored axial Poincare inequality ||x||<=N||B x||
follows by summing its backward differences. The transverse
Dirichlet spectral gap gives ||x||<=C N||D_T x||.
Applying these inequalities on the tensor slices yields

    ||D_T x||+||B x||<=C N||(B tensor D_T)x||,
    ||x||<=C N^2||(B tensor D_T)x||.

The four product terms therefore bound the norm of the mixed
difference of m x by C b times (13). This proves the first
inequality of (12); the second is its transpose, as m is real
diagonal. This proof keeps both the lower anchor and every transverse
end edge; it assumes no commutator gain for a rough multiplier.
By (6), (12) applies to m_j with b=C a^3 p(l).

### 4. Full tensor estimates for the skew transport

For the axial skew matrix J=B^T-B (up to an irrelevant overall
sign), B M B^T=I. Hence

    ||M^(1/2) J M^(1/2)||_HS<=2 (Tr M)^(1/2)<=C N.

For example each of M^(1/2) B M^(1/2) and its transpose is
bounded in HS norm by ||B M^(1/2)|| (Tr M)^(1/2);
the operator factor is one. Thus

    ||Y^(1/2) J_1 Y^(1/2)||_HS<=C N^3.                 (14)

For a transverse direction, its skew difference J obeys
||J G^(1/2)||<=2: write it as the sum of the two adjacent
Dirichlet differences at each vertex, whose squared norms are
bounded by four times the full gradient energy. Consequently
||G^(1/2) J G^(1/2)||_HS<=2(Tr G)^(1/2), and

    ||Y^(1/2) J_j Y^(1/2)||_HS<=C N^(7/2), j=2,3,4.    (15)

These are tensor-product HS norms on all axial and transverse
vertices. No internal spectral cutoff is introduced. Factoring the
variable coefficient to the left via (12), (14)–(15) give

    ||Y^(1/2) m_j J_j Y^(1/2)||_HS
       <=C a^3 p(l) N^(7/2)<=C p(l) N^(1/2).

For the error in (11), the weighted HS inequality gives
||Y^(1/2) F Y^(1/2)||_HS<=||F|| ||Y||_HS<=C p(l).
One proof diagonalizes Y and uses
2 lambda_r lambda_s<=lambda_r^2+lambda_s^2 with the row and
column squared-norm bounds for F; no symmetry of F is needed.
Combining these bounds with (9) proves

    ||K^(1/2) O_q K^(1/2)||_HS<=C p(l) N^(1/2).         (16)

### 5. Apply the prefix estimate to the actual ordered trace

Split R=I-D_0 Phi only in Z_l. Its direct part satisfies

    ||Khat^(1/2) B_(q t_c)^T Sigmahat^(1/2)||_HS
       <=C (Tr K)^(1/2) ||q||_infinity ||Sigma^(1/2)||
       <=C p(l) N^(1/2),                              (17)

by (6),(8). For its prefix part, Phi Sigma Phi^T=K gives exactly

    ||Khat^(1/2) B_(q t_c)^T D_0hat Phihat
                                      Sigmahat^(1/2)||_HS^2
       =||Khat^(1/2) B_(q t_c)^T D_0hat Khat^(1/2)||_HS^2.
                                                               (18)

For a fixed exterior color, B_(q t_c)=M_q S tensor b_c,
where b_c phi=[t_c,phi]. Thus B_(q t_c)^T D_0hat is (10)
tensored with b_c^T, whose fixed HS norm is sqrt(2).
Equation (16) bounds (18). Equations (17)–(18) prove (7).
The identity is a covariance Gram identity, not an assertion that
the prefix and Hodge field are independent.

Cyclically rewriting one summand of (1), without moving any
variable multiplier, gives precisely

    Tr[(Sigmahat^(1/2) Ahat Sigmahat^(1/2)) X_k Z_l].

For arbitrary compatible finite matrices,
|Tr(F X Z)|<=||F|| ||X||_HS ||Z||_HS, by the trace
Cauchy–Schwarz inequality and ||F X||_HS<=||F|| ||X||_HS.
Equations (4),(5),(7) therefore bound each summand by
C p(k)p(l) N*N^(3/2)*N^(1/2)=C p(k)p(l) N^3.
L156's complete heat summability, including the three exterior
colors, proves (2). Equation (3) follows from L157 and L158.
No cubic-bounded branch is discarded when making this assembly.

### 6. Finite checks and qualifications

Run `PYTHONDONTWRITEBYTECODE=1 python3 scripts/combined-ward-response/check_cubic_smooth_action_bound.py`.
Its full certificate is
`scripts/combined-ward-response/cubic-smooth-action-bound-certificate.json`.
Exact rational checks verify the co-closed transport diagonal and
skew identities, prefix squared-HS Gram identity, and scalar color
reduction on a pinned two-cycle graph. Separate anchored axial and
Dirichlet transverse matrices check the energy inverses and the
transport squared-HS inequalities at sizes 2,4,7. They verify finite
identities and inequality instances; the uniform estimates and
actual mode applicability are the analytic proof above. No numerical
mesh extrapolation or actual-probe coefficient is asserted.

The route succeeds only at the boundedness threshold. A finite signed
limit still requires controlling the actual trace rather than the
absolute product of its norms. The complete E,E contraction and
other response jets remain independent gaps. Prior failed raw-loop
and forest-transfer mechanisms are not reopened by these estimates.

## Mathlib

Full matching result: **not checked**. Supporting finite Schatten
inequalities, tensor-product energies, Poincare and product identities:
**not checked**. Unknown coverage is not absence. Reuse the unchanged
[assessment](../drafts/literature/2026-10-12-cubic-residual-action-cubic-scale.md).
No new external theorem is imported or reproved. The finite
specialization is needed to justify the true prefix sandwich,
co-closed action column and boundary domains in the ordered branch.
