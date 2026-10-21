# L157 — Mixed cubic sector: remove the smooth residual column

## Hypotheses

Keep every hypothesis and convention of L155 and L156: SU(2), the
relative box (-4,4)^4, a=8/N through admitted even meshes, straight
lower-rooted forest, the complete displacement and both actual L010
probes at tau=1/16. Take the bare expansion at fixed mesh first.
Full-link Taylor tensors precede covariance splitting. Both residual
insertion subtractions and all action plaquettes remain.

Use L156's full-link matrices A,L,Sigma,R,Phi,K,C_g,E,U_i and its
heat expansion (8), with exterior columns h_k=R v_k and coefficients
c_(i;kl). A hat means the three-color diagonal extension. All norms
are ordinary stored-coordinate norms. Set h_(k,c)=h_k t_c. For a
colored link field h define the vertex-to-link matrix

    (B_h phi)_e=[h_e,phi(tail e)+phi(head e)].               (1)

The bracket and color inner product are L156's. Vertex potentials
vanish on all physical faces, and normal end links are retained.
For a symmetric color-diagonal link matrix F put

    Q_F(h)=F B_h-B_(F h).                                  (2)

Define H_i^mix as the sum of the (C_g,E) and (E,C_g) terms in
L156's exact expansion of H_i=-kappa(f_(i,0),r_1,S_3).
This sector uses E=C-C_g, which is symmetric but need not be positive.

## Conclusion

The complete mixed sector has the exact signed trace

    H_i^mix=-sum_(k,l,c) c_(i;kl)
       Tr[Q_Ahat(h_(k,c)) Khat Q_Lhat(h_(l,c))^T Ehat].     (3)

In particular, define the retained trace

    J_i=-sum_(k,l,c) c_(i;kl)
       Tr[Ahat B_(h_(k,c)) Khat Q_Lhat(h_(l,c))^T Ehat].     (4)

Then, for each actual probe,

    H_i^mix=J_i+P_i,       |P_i|<=C_i N,
    a^3 P_i -> 0.                                         (5)

Thus only the part with A on the rough link slot remains in this
mixed sector at cubic scale. In (4) both action terms in Q_Lhat
remain, including the term with L on its exterior column. No bound,
scaled limit or sign for J_i or the E,E sector is established. With
H_i^EE denoting L156's E,E term, the complete identity gives only

    H_i=J_i+H_i^EE+O_i(N).                                (6)

L156's O(1) two-gradient sector is included in this error. In particular
(6) does not prove cubic boundedness or vanishing of H_i. No complete
compensation, finer power/logarithm, interacting reflected bound,
continuum theory or mass gap follows. This is a local specialization
of finite gauge Taylor and matrix estimates, without an originality claim.

## Proof

### 1. One-gradient identity and the signed contraction

For the gauge-invariant scalar F in L156(4), polarize its unrestricted
link argument as x=h+t z. The coefficient of t is

    6 T_F(h,z,D_0 phi)
       =-<A_F h,[z,phi_tail+phi_head]>
        -<A_F z,[h,phi_tail+phi_head]>.                    (7)

Here F_2(x)=<x,A_F x>. Unlike the two-gradient specialization, z
is unrestricted, so the second term is retained. Invariance of the
color inner product gives

    <A_F h,[z,s phi]>=-<z,B_(A_F h) phi>,
    <A_F z,[h,s phi]>=<z,A_F B_h phi>.

Consequently the right side of (7) is -z^T Q_(A_F)(h) phi.
Apply this with A_F=A for the residual and A_F=L/2 for the action.
The two tensors evaluated on one gradient are therefore respectively
`-z^T Q_Ahat(h) phi/6` and `-z^T Q_Lhat(ell) phi/12`.
Both insertion subtractions are included in A; no separate force
summand is declared gauge invariant.

For any real vertex-to-link matrices M,N, the algebraic contraction
of z^T M phi with z^T N phi, assigning Ehat to the two z slots and
Khat to the two phi slots, is

    sum_(j,m,alpha,beta) M_(j,alpha) N_(m,beta)
             Ehat_(j,m) Khat_(alpha,beta)
       =Tr(M Khat N^T Ehat).                              (8)

This uses symmetry, not positivity, of E. It defines no independent
noise law with covariance E. L155/L156's full combined-color tensor
contraction has coefficient -36. Its two mixed terms are equal by
simultaneously exchanging the two rough slots of both symmetric
tensors. Thus their coefficient after (7) is

    -2*36*(1/6)*(1/12)=-1.

Insert L156(8)'s actual heat expansion, including its external color
sum. Equation (8) proves (3). Expanding its Q_Ahat gives (4) and

    P_i=sum_(k,l,c) c_(i;kl)
       Tr[B_(Ahat h_(k,c)) Khat
              (Lhat B_(h_(l,c))-B_(Lhat h_(l,c)))^T Ehat]. (9)

These are finite identities at every mesh. All cancellations of
forest rows occur only in the complete covariance, as in L156.

### 2. Global pinned operator bounds

L026's complete relative spectrum gives ||Sigma||<=C N^2. The
unscaled incidence D_0 has uniformly bounded operator norm. On each
axial line Phi is the lower-prefix matrix with at most N entries in
any row or column. Its row/column-sum bound gives ||Phi||<=N;
setting its boundary vertex outputs to zero preserves this bound.
In particular ||R||=||I-D_0 Phi||<=C N, with the upper jump retained.

Expand the remainder exactly:

    E=Sigma-D_0 Phi Sigma-Sigma Phi^T D_0^T,
    ||E||<=C N^3.                                        (10)

Let Pi=Sigma L. The relation L D_0=0 and
Delta=L+D_0 D_0^T imply Delta L=L^2=L Delta.
Hence Pi is symmetric positive and Pi^2=Pi; the positivity and
invertibility of Delta follow from L026's spectrum. Thus ||Pi||<=1.
Multiplication of (10) on the right by L gives the exact identity

    E L=(I-D_0 Phi) Sigma L=R Pi,
    ||E L||=||L E||<=C N.                               (11)

No prefix is commuted through a variable coefficient or a resolvent.

L156(6) proves 0<=K<=M tensor G, where M_st=min(s,t) and
G=Delta_0^(-1) is the three-dimensional scalar Dirichlet inverse.
For transverse indices k in {1,...,N-1}^3 its eigenvalues satisfy
lambda_k>=4|k|^2/N^2. Shells max k_j=m contain at most 3m^2
indices. Therefore

    Tr G <=(N^2/4) sum_k |k|^(-2)
          <=(3N^2/4)(N-1),
    Tr M=sum_(s=1)^(N-1) s <=N^2/2,
    Tr K<=Tr M Tr G<=C N^5.                             (12)

This bound includes every transverse mode and the constant axial
edge mode already present in L156's exact prefix formula. The
three-color trace is 3 Tr K.

### 3. Exterior bounds and the subcubic error

The bounded number of incidence endpoints and fixed color constants
in (1) give

    ||B_h||<=C ||h||_infinity.                           (13)

Indeed each matrix row and column has uniformly bounded degree;
the row/column-sum norm inequality applies also at pinned endpoints.
L156(9)--(10) give, for a fixed polynomial p of the mode labels,

    ||A h_k||_infinity<=C a^5 p(k),
    ||L h_k||_infinity<=C a^3 p(k).                       (14)

Both identities use A R v=A v and L R v=L v before smooth estimates,
so the upper jump is never differentiated as a smooth extension.
We also need only the weaker global bound

    ||h_k||_infinity<=C p(k).                            (15)

To check (15) without deleting the upper face, L156's physical mode
definition gives ||v_k||_infinity<=C a p(k). Each prefix contains
at most N such samples, so ||Phi v_k||_infinity<=C Na p(k).
Taking an endpoint difference and using Na=8 proves (15), including
the omitted upper axial edge and every transverse end edge. This
argument does not assume the sharper compact-interior O(a) bound
at the pinned jump.

If Khat is positive, |Tr(Khat X)|<=Tr(Khat)||X|| for any real X:
diagonalize Khat and bound each diagonal entry of X in that basis.
Use cyclicity in each of the two terms in (9). For the action term
with Lhat B_ell, equations (11)--(15) give

    |Tr(B_(Ahat h) Khat B_ell^T Lhat Ehat)|
       <=Tr(Khat)||B_ell|| ||Lhat Ehat|| ||B_(Ahat h)||
       <=C p(k)p(l) N^5 N a^5
       <=C p(k)p(l) N.                                  (16)

For the other action term, (10) instead gives

    |Tr(B_(Ahat h) Khat B_(Lhat ell)^T Ehat)|
       <=C p(k)p(l) N^5 a^3 N^3 a^5
       <=C p(k)p(l).                                    (17)

L156(8) proves the mesh-uniform summability of
sum_(k,l)|c_(i;kl)|p(k)p(l) over the full allowed spectrum for each
actual probe. Summing (16)--(17), including the three exterior colors,
proves (5). Equation (6) follows from the exact four-sector splitting
and L156's O(1) estimate, with no other response jet added.

### 4. Verification and the remaining test

Run `PYTHONDONTWRITEBYTECODE=1 python3 scripts/combined-ward-response/check_cubic_single_gradient.py`.
The full certificate is
`scripts/combined-ward-response/cubic-single-gradient-certificate.json`.
All 1728 one-cycle action basis tests of (7) have exact rational
error zero. Two further comparisons directly contract the cubic
Taylor tensors with a gradient covariance and an indefinite symmetric
color-diagonal E, and compare with (3). The direct and reduced values
are respectively -53 and -72, with exact zero error. These check the
one-gradient normalization, bracket signs and the factor for both
mixed placements; they are not actual-probe or cutoff calculations.
Bounds (10)--(17) are analytic, not extrapolations of those checks.

The attempted extension of L156 therefore removes the part (9), but
not the complete mixed sector. In (4), A B_h acts on a rough vertex
input after multiplication by h; it is not B_(A h). Substituting the
smooth estimate (14) for that composition would drop the second term
of (7) without justification. The remaining useful test is a signed
estimate of (4), possibly together with E,E. No growth, exhaustion
of that mechanism, or failure of a full-response cancellation is
inferred from this unresolved trace.

## Mathlib

Full matching theorem: **not checked**. Supporting finite gauge Taylor
identities, trace inequalities and relative-cochain spectrum: **not
checked**. Unknown coverage is not absence. Reuse the unchanged
[assessment](../drafts/literature/2026-10-12-cubic-residual-action-cubic-scale.md).
No new external theorem is imported or reproved. The finite
specialization is necessary to retain the signed remainder, rough
residual slot, both mixed placements and the global pinned jump.
