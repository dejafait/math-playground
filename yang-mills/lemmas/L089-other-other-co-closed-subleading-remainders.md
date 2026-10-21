# L089 — Subleading remainders in the finite co-closed trace

## Hypotheses

Use exactly L088's SU(2) finite Gaussian, actual L010 probes i=3,6,
actual L018 residual, straight lower-rooted direction-1 forest,
all-face relative pinned box, admitted even N, a=8/N and tau=1/16.
The bare small-coupling coefficient is taken at fixed mesh first.
All norms are in ordinary dimensionless stored coordinates. Retain
all interior axial levels, transverse end rows, ordered plaquette
pairs including coincidences, and the full exterior heat expansion.

Import K_h, V_h, Qcal, Cc, Bb, Bq, f_k, b_k, q_k and the real
symmetric coefficients c_(i;kl) from L088. In particular K_h is the
full two-level co-closed covariance, not a frozen covariance. Split
L088's actual alternating matrix, before projection, as

    F_k=Bb^T M_(f_k) Bq-Bq^T M_(f_k) Bb,
    H_k=Bq^T M_(b_k) Cc-Cc^T M_(b_k) Bq
                       +Cc^T M_(q_k) Bb-Bb^T M_(q_k) Cc,
    Omega_k=F_k+H_k.                                    (1)

Write F^h_k=Qcal F_k Qcal and H^h_k=Qcal H_k Qcal.
The superscript h always projects both rough endpoints only; it does
not project the exterior columns or change either actual observable.

L009's actual quadratic residual in the full Hodge law has matrix
A_0=A_gen-Q_0, up to an irrelevant centering constant, where A_gen
is the symmetric matrix of q_(V,a) and Q_0 is that of q_(3,a)+q_(6,a).
Let E_h denote the full Hodge row map used in L088, proof section 2,
and Sigma the Hodge covariance. Define

    K_h=E_h Sigma E_h^T,
    V_gen=E_h Sigma A_gen Sigma E_h^T,
    V_curv=E_h Sigma Q_0 Sigma E_h^T,
    V_h=V_gen-V_curv.                                   (2)

These are actual finite matrices with the displacement, strain,
clover and endpoint filters unchanged. Define only the reduced trace

    T_red=sum_(k,l)c_(i;kl)
                Tr(H^h_k V_gen (H^h_l)^T K_h).           (3)

This is not the frozen principal diagnostic in L088.

## Conclusion

For each actual probe, with L_N=log(eN),

    |T_hh-T_red| <= C_i N^2 sqrt(L_N),
    a^3(T_hh-T_red)=O_i(sqrt(L_N)/N) -> 0.               (4)

More specifically, every term containing F^h in the exact expansion
of L088's trace has joint absolute bound C_i N^2 sqrt(L_N), and
the remaining V_curv trace has absolute bound C_i N^2. Thus the
actual exterior-circulation terms and bounded curvature-form residual
subtractions cannot supply an a^-3 coefficient in this sector.

No limit for T_red or T_hh follows. In particular (4) does not compare
the finite trace with its canceled frozen symbol. The six remaining
rough sectors besides T_gg and T_hh still lack scaled control. Their
joint contribution together with T_red would need limit -4 gamma D_i
before L085's outside factor 3 to compensate L084. No sign, complete
other/other limit, finer power/logarithmic estimate, finite matching,
interacting error <=c_box/2, continuum construction or mass assertion
is made. The log in this upper bound is not a response-log coefficient.

## Proof

### 1. Sharpen only the spectral trace that is needed

Import the exact relative spectrum in L086, proof section 1. For
R=(L_D tensor I+I tensor Delta_T)^(-1), its eigenvalues are rho_k^-1,
where rho_k>=4|k|^2/N^2. The labels satisfy 1<=k_1<N; for each of
the three transverse edge components, its own transverse index is
in 0,...,N-1 and the other two are in 1,...,N-1. There is no zero
mode. The shell max_j k_j=m has at most C m^3 labels, counting all
components. Consequently

    Tr R^2 <= C N^4 sum_(m=1)^(N-1) m^3/m^4
            <= C' N^4 log(eN).                           (5)

The second inequality is the elementary harmonic-sum bound
sum_(m=1)^(N-1) 1/m<=1+log N. Qcal commutes with R, and
K_h=R Qcal is its positive spectral restriction, so

    ||K_h||_HS <= C N^2 sqrt(L_N).                        (6)

This sharpens the deliberately coarse Tr R^2<=C N^6 in L086.
It is an exact full-spectrum bound with pinned boundary conditions;
no infinite-grid approximation or low-mode replacement is used.

### 2. A finite-matrix estimate without commuting multipliers

For any positive semidefinite finite matrix K, bounded rectangular
maps B,C into the same row space, and row multiplier M, Hilbert--
Schmidt Cauchy--Schwarz gives

    ||K^(1/2) B^T M C K^(1/2)||_HS
           <= ||B|| ||C|| ||M|| ||K||_HS.                (7)

For completeness, set X=B K B^T and Y=C K C^T. The square of the
left side is Tr(M Y M^T X). Its absolute value is at most
||M Y M^T||_HS ||X||_HS, which is at most
||M||^2 ||C||^2 ||B||^2 ||K||_HS^2. This proves (7) using just
the standard finite-matrix Cauchy--Schwarz and operator ideal
inequalities. In particular M is never commuted through K.

Import L088(5): for a fixed mesh-independent polynomial p,

    ||f_k||_infinity<=C a^2 p(k),
    ||b_k||_infinity+||q_k||_infinity<=C a p(k),
    sum_(k,l)|c_(i;kl)|p(k)p(l)<=C_i.                    (8)

The path maps have uniform bounded row and column multiplicity,
including pinned end rows. Since K_h^(1/2)Qcal=K_h^(1/2), the
projections in F^h disappear adjacent to these square roots. Apply
(7) to both terms of F_k, using (6) and (8), to obtain

    ||K_h^(1/2) F^h_k K_h^(1/2)||_HS
       <=C a^2 p(k) N^2 sqrt(L_N)
       <=C' p(k) sqrt(L_N).                              (9)

No neighboring exterior coefficients are replaced by constants.
The actual nonzero circulation is retained in the entire estimate.

For H_k, import L088(7),(9):

    ||Cc K_h^(1/2)||<=1,
    ||Bb K_h^(1/2)||_HS+||Bq K_h^(1/2)||_HS<=C N^2.

For example the first term of H_k is bounded by
||K_h^(1/2) Bq^T||_HS ||M_(b_k)|| ||Cc K_h^(1/2)||,
and its transpose has the same bound. The two q_k terms obey the
same estimate with Bb. Hence

    ||K_h^(1/2) H^h_k K_h^(1/2)||_HS
                      <=C a p(k) N^2<=C' p(k) N.        (10)

### 3. Retain the actual residual and then remove its bounded part

L088(8) gives V_h=K_h^(1/2) W_h K_h^(1/2) on the co-closed
subspace, with ||W_h||<=C N. The identical row-map argument applies
to (2). L009(17) specifies A_gen and the following paragraph
identifies Q_0's whitened matrix as B_(3,a)+B_(6,a). Their norms
are mesh uniformly bounded. L020, proof section 3, equation (11)
and its preceding inequality give separately

    ||Sigma^(1/2) Q_0 Sigma^(1/2)||<=C,
    ||Sigma^(1/2) A_gen Sigma^(1/2)||<=C N.              (11)

The same coordinate normalization is used in L088's applicability
check; the whitening removes physical/stored scale factors. More
explicitly, for any y and either A_*=Q_0 or A_gen,

    |y^T E_h Sigma A_* Sigma E_h^T y|
       <=||Sigma^(1/2) A_* Sigma^(1/2)||
                         y^T K_h y.

Thus V_curv=K_h^(1/2) W_curv K_h^(1/2) with
||W_curv||<=C, and V_gen has the corresponding O(N) bound.
Extend these factorizations by zero off the co-closed subspace.
L018's gauge-invariant lift justifies the residual split in (2);
no cubic vertex is transferred to an unmodified Hodge law.

For any two alternating matrices E_k,E_l and any such W, cyclicity
and finite Hilbert--Schmidt Cauchy--Schwarz give

    |Tr(E_k K_h^(1/2) W K_h^(1/2) E_l^T K_h)|
       <=||W|| ||K_h^(1/2) E_k K_h^(1/2)||_HS
                 ||K_h^(1/2) E_l K_h^(1/2)||_HS.        (12)

Insert Omega^h=F^h+H^h into L088(6), which already contains all six
distinct-row placements with their correct orientation. Subtract
only the H^h,V_h,H^h trace. The three remaining types in (12) have
bounds, before their heat coefficients are summed,

    F,V_h,F: C p(k)p(l) N L_N,
    F,V_h,H: C p(k)p(l) N^2 sqrt(L_N),
    H,V_h,F: C p(k)p(l) N^2 sqrt(L_N).                  (13)

All three are retained, including both mixed exterior orientations.
Sum their absolute values with (8). Since sqrt(log(eN))<=C N for
N>=2, this costs at most C_i N^2 sqrt(L_N).

Finally V_h=V_gen-V_curv, and the H^h,V_curv,H^h trace is bounded
by C_i N^2 using (10), (12) and ||W_curv||<=C. Its sign is minus
in that exact difference, but the absolute estimate suffices. This
proves (4), because a^3=512/N^3. Ordered pairs, coincident vertices,
both residual placements, the two-level resolvent and every heat
mode are present throughout. No extra factor 3 has been introduced.

### 4. Scope and downstream use

This is one bounded proof attempt under the unchanged EXPLORE
assessment `drafts/literature/2026-10-10-other-other-cubic-leading-scale.md`.
The complete finite contraction is imported from L048 through
L085/L088. Their hypotheses and normalization are unchanged. The
additional specialization replaces one coarse resolvent estimate
by its full four-dimensional shell sum and applies standard finite
matrix inequalities to the actual trace. It is local REPRODUCTION,
not a claim of originality beyond the sources checked.

L088's frozen cancellation concerns a separately frozen diagnostic.
After (4), an actual co-closed leading coefficient could only come
from T_red. Showing that T_red is o(N^3) still requires a finite
comparison or signed identity controlling variable path coefficients,
displacement, projections and physical boundary corrections. These
are not established by (5)--(13). Nor does this proof estimate any
of the six remaining rough sectors. The comparison with the mixed
coefficient keeps L082's saved-table/IEEE qualifications. Independent
response-jet and Yang--Mills construction gaps remain as stated.

## Mathlib

Full matching coverage: **not checked**. Supporting finite spectral,
Hilbert--Schmidt Cauchy--Schwarz, operator ideal and harmonic-sum
coverage: **not checked**. Unknown availability is not absence.
No new external theorem, continuum Ward identity or flow-finiteness
claim is used to replace this isolated bare finite-box calculation.

