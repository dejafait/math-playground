# L162 — The complete action-two-gradient E,E group is subcubic

## Hypotheses

Keep L161's SU(2) relative cube (-4,4)^4, a=8/N through sufficiently
fine admitted even meshes, straight direction-1 lower-rooted forest,
complete compact displacement and both actual L010 probes at tau=1/16.
The bare expansion is taken at fixed mesh before refinement. Use
ordinary stored-coordinate norms and L161's D,L,Sigma,F=Phi Sigma,
full residual cubic matrix M=T_R(h,.,.), exterior columns h=h_k t_c,
ell=h_l t_c and heat coefficients c_(i;kl). Hats denote three-color
diagonal extensions. Retain both residual insertion subtractions, all
action faces and normal end links, the upper pinned jump, constant
axial mode and entire exterior heat spectrum. Full tensors precede
forest restriction. Neither E nor either probe is assumed positive.

Let S be the uncolored endpoint-sum matrix from pinned interior vertex
potentials to links; boundary values in both D and S are zero. For a
colored link column q define W_q linkwise by (W_q z)_e=[q_e,z_e], so
B_q=W_q Shat. Define exactly L161's sixth complete trace group

    J_(i,S2)=-3 sum_(k,l,c) c_(i;kl)
          Tr[Dhat^T B_(Lhat ell) Fhat M Fhat^T].          (1)

## Conclusion

For both actual probes there is a mesh-independent constant C_i with

    |J_(i,S2)|<=C_i N^(5/2),       a^3 J_(i,S2)->0.       (2)

The full prefix cross matrix, including its upper end, satisfies

    ||D F||_HS^2<= (9/8) N^5,                            (3)

and L161's residual-two-gradient group remains O(N), also subcubic.
Thus both same-vertex double-gradient groups in L161(3) vanish at
cubic scale. The first four ordered traces and the scaled limits of
the two mixed branches still remain unresolved. No complete-response
bound, vanishing, compensation coefficient, finer powers/logarithm,
finite matching, interacting reflected bound <=c_box/2, continuum
construction or infrared finite mass follows. This is local progress
using the assessed finite-matrix method, without a novelty claim.

## Proof

### 1. Co-closed transport moves one actual difference

Use the colored polarized form of L159's exact co-closed skew
transport. The edgewise verification below fixes its sign in (1);
it does not reprove L159's differently ordered mixed-branch bound.

For any colored q and pinned colored vertex fields x,y, the edgewise
identity, with t and b denoting tail and head, is

    <x_b-x_t,[q_e,y_t+y_b]>
      +<x_t+x_b,[q_e,y_b-y_t]>
      =2<x_b,[q_e,y_b]>-2<x_t,[q_e,y_t]>.

Summing every edge, including those with one boundary endpoint, gives

    Dhat^T W_q Shat+Shat^T W_q Dhat
                  =2 diag_v ad((Dhat^T q)_v).           (4)

Boundary endpoint terms vanish because x,y are zero there; their
incident edge contributions at an interior vertex remain in D^T q.
This proves (4) without a cutoff or a coefficient replacement.

Here q=Lhat ell=(L h_l)t_c=(L v_l)t_c. L156's exact L D=0 and
D^T L=0 imply Dhat^T q=0. Its full global estimate (10) gives
||q||_infinity<=C a^3 p(l) for a fixed polynomial p, including normal
end rows. The endpoint-sum map has norm at most 4: each row has at
most two unit entries and each column at most eight. The SU(2) bracket
has ||ad(q_e)||<=|q_e| in the stated orthonormal color convention.
Consequently (4) gives the exact ordered identity and estimate

    Dhat^T B_q=-Shat^T W_q Dhat,
    ||Dhat^T B_q Fhat||_HS
          <=4 ||q||_infinity ||Dhat Fhat||_HS.           (5)

No transpose of a differently ordered response is used. In particular,
q is not cut off to the compact residual region: such a cutoff could
destroy co-closedness. Gauge annihilation removes the forest jump
from q exactly; the jump remains in F and is counted next.

### 2. Full-prefix energy with both axial ends

Let n=N-1, (M_ax)_st=min(s,t), s,t=1,...,n, and G the inverse
three-dimensional scalar Dirichlet Laplacian Delta_T. L161(5) supplies
the positive finite-matrix order

    0<=F F^T<=Y=M_ax tensor G^2.                        (6)

The relative vertex incidence on the cube has
D^T D=L_D tensor I+I tensor Delta_T, with L_D the one-dimensional
vertex Dirichlet Laplacian. This follows by summing the squared
coordinate differences with zero potential at every physical face,
as in L026's relative product spectrum. Since D^T D is positive,
trace monotonicity against it in (6), without commutation, gives

    ||D F||_HS^2
       =Tr[(D^T D)F F^T]
       <=Tr(L_D M_ax) Tr G^2+Tr M_ax Tr G.              (7)

The exact axial counts are

    Tr M_ax=n(n+1)/2,
    Tr(L_D M_ax)=2 sum_(s=1)^n s
                    -2 sum_(s=1)^(n-1) s=2n.           (8)

Equivalently the latter contains 1 from the lower normal edge,
n-1 from the interior differences, and n from the upper normal edge.
The upper pinned jump contributes at this same order and is retained.
M_ax is a positive dominating matrix, not a new prefix law.

For all transverse indices q in {1,...,N-1}^3, the unscaled spectrum
satisfies lambda_q>=4|q|^2/N^2 (use sin(pi q_j/(2N))>=q_j/N).
The shell max q_j=m has at most 3m^2 indices. Therefore the complete
spectrum, including its lowest modes, obeys

    Tr G <= (3N^2/4)(N-1) <=(3/4)N^3,
    Tr G^2 <=(3N^4/16) sum_(m=1)^(N-1) m^-2
             <=(3/8)N^4.                               (9)

The final inequality uses 1+integral_1^infinity x^-2 dx=2.
Equations (7)--(9), 2n<=2N and n(n+1)/2<=N^2/2 yield (3).
They also give directly from (6)
||F||_HS^2<= (3/16)N^6, consistent with L161.
Colored squared norms have exactly three times the one-color values.
The axial constant mode was retained in L161's derivation of (6);
no internal spectral truncation or smooth upper extension occurs here.

### 3. Estimate the complete action group in its actual order

For finite compatible matrices O,F,M the Frobenius inequality gives

    |Tr(O F M F^T)|
         <=||O F||_HS ||M F^T||_HS
         <=||O F||_HS ||M|| ||F||_HS.                   (10)

This requires no positivity of O or M. L161(12) proves
||M||<=C p(k) from the compact full residual tensor and the actual
interior O(a) exterior column; both subtraction tensors are included.
Apply (5), (3), (6)--(9) and (10), with O=Dhat^T B_q. The individual
summand in (1), including its fixed color factors, is bounded by

    C a^3 p(l) N^(5/2) p(k) N^3
                     =C p(k)p(l) N^(5/2),              (11)

where a=8/N. L156(8)'s complete heat expansion has uniform
sum_(k,l)|c_(i;kl)|p(k)p(l)<=C_i. Sum every exterior mode and color
and retain the outside -3 exactly once. This proves (2), with
|a^3 J_(i,S2)|<=C_i N^-1/2. No other trace order is altered.
Together with L161's O(N) residual group, precisely these two groups
are removed at cubic scale; the remaining response terms are retained.

### 4. Finite checks and limits of their evidence

Run `PYTHONDONTWRITEBYTECODE=1 python3 scripts/combined-ward-response/check_cubic_action_double_gradient_difference.py`.
The complete certificate is
`scripts/combined-ward-response/cubic-action-double-gradient-difference-certificate.json`.
It checks (4) on a pinned graph with two independent cycles, including
an explicitly non-co-closed control with nonzero diagonal, and all
three exterior color directions. For actual co-closed graph action
columns it checks (5) and equality of the original and transported
trace with signed symmetric link matrices. Rational transverse-mass
prefix cases verify (7)'s energy domination and (8)'s exact upper-end
count, with complete matrices and positive pivots saved to disk.
All 55 rational identities, nine signed transport cases and nine
prefix cases pass, with maximum exact identity error zero and no
failures. The non-co-closed control has a nonzero retained diagonal.
These finite checks test signs, endpoints and order, not either
actual probe's value or a continuum response. The bounds for every
admitted mesh and both actual probes are the analytical proof above.

## Mathlib

Full matching theorem: **not checked**. Supporting incidence product
identities, trace monotonicity, tensor spectra and Frobenius inequalities:
**not checked**. Unknown is not absence. Reuse the unchanged
[target assessment](../drafts/literature/2026-10-12-cubic-residual-action-cubic-scale.md).
No external theorem is newly imported or reproved. The finite
specialization is needed to recover the co-closed transport difference
lost in L161's operator-norm count, with the pinned upper end retained.
