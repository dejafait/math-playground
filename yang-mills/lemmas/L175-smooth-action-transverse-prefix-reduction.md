# L175 — Only transverse prefix transport can survive in V at cubic scale

## Hypotheses

Keep L159's exact V_i, i=3,6: SU(2), relative box (-4,4)^4,
a=8/N through admitted even meshes, straight direction-1 lower-rooted
forest, complete compact displacement, both actual L010 probes at
tau=1/16, and bare expansion at fixed mesh before refinement.
Use L156's ordinary-coordinate A,L,Sigma,R,Phi,K, heat columns h_k
and coefficients c_(i;kl). Define F=Phi Sigma, a cross matrix, and
let S be the endpoint-sum map from interior vertices to variable links.
Pinned endpoint values are zero; all normal end links remain.

Separate the actual residual only as

    A=A^gen-Q_3-Q_6,   A^gen=(L K_a+K_a^T L)/2.          (1)

The Q forms are exactly L018(2)/L028's distinct triplet and shear
forms. No positivity of them, A, either probe, or signed E is assumed.
Put q_l=L h_l=L v_l. Its smooth componentwise extension is the finite
relative-mode trigonometric extension in L159(6), not an extension of
h_l across the upper forest jump. Let m_(j,l) be the diagonal vertex
multiplier obtained by evaluating its j-component at vertex positions.
Let J_j have +1 on forward neighboring vertex entries and -1 on
backward entries, with boundary vertices omitted. This fixes its sign
and scale. For a scalar link field h write M_h for its link multiplier.

## Conclusion

Define the one-color, fully ordered finite trace

    W_i=-6 sum_(k,l) c_(i;kl) sum_(j=2)^4
          Tr[K m_(j,l) J_j F A^gen M_(h_k) S].           (2)

The trace is over interior vertices; every axial level, transverse
boundary row and heat mode remains. Then

    V_i=W_i+O_i(N^(5/2) log(eN)^(1/4)),
    a^3(V_i-W_i) -> 0.                                  (3)

More precisely, the direct Hodge part is
O_i(N^(5/2) log(eN)^(1/4)); the prefix contributions from Q_3 and
Q_6 are each O_i(N^2); after retaining A^gen, the axial transport
and midpoint transport error are each O_i(N^(5/2)). All are estimated
before removal. In particular |W_i|<=C_i N^3 by L159 and (3).

No convergence or value of a^3 W_i is proved. The V_i limit and the
complete-response vanishing question remain open. Other response jets,
finer asymptotics, interacting reflection error and continuum/infrared
construction remain unresolved. This is local standard-method
REPRODUCTION, without a claim of novelty beyond the sources checked.

## Proof

### 1. Exact direct/prefix split, including color and sign

For fixed k,l write h=h_k and q=q_l. L157's colored endpoint map is
B_(h t_c)=M_h S tensor b_c, where b_c phi=[t_c,phi]. In the stated
SU(2) normalization Tr(b_c b_c^T)=2. Summing the three exterior
colors gives 6, so L159(1) is exactly

    V_i=6 sum_(k,l) c_(i;kl)
          Tr[Sigma A M_h S K S^T M_q R].                 (4)

Expand only R=I-D_0 Phi in its original position and cycle the
resulting finite traces. Set

    O_q=S^T M_q D_0,
    D_i=6 sum c Tr[Sigma A M_h S K S^T M_q],
    P_i(B)=-6 sum c Tr[K O_q F B M_h S].                 (5)

Here B is a link matrix, not a probe or endpoint map. Exactly

    V_i=D_i+P_i(A^gen)-P_i(Q_3)-P_i(Q_6).                (6)

No multiplier has been commuted with Sigma, K or F. The prefix retains
F A^gen M_h S in that order; no action-Hessian branch coefficient is
assigned to it. The minus sign in (2) comes from R's prefix term.

### 2. Common supported factor and improved direct factor

Each of A,A^gen,Q_3,Q_6 has fixed range and both supports in a common
compact interior enlargement for sufficiently fine meshes. L028's
compositions, including their adjoints, give this directly from compact
displacement and strain support. Choose a link cutoff chi equal to one
on their input supports. It changes none of the traces. L159's proof,
applied to the separate compositions, gives

    ||Sigma^(1/2) B Sigma^(1/2)||<=C N, B=A or A^gen,
    ||Sigma^(1/2) Q_j Sigma^(1/2)||<=C, j=3,6.           (7)

Indeed K_a=a^-1 E M C D_1 with bounded coefficient/average maps.
Since L commutes with Delta=Sigma^-1 and L<=Delta,
||Sigma^(1/2)L||<=C and ||D_1 Sigma^(1/2)||<=1. These bound
each generator orientation by C/a. Each Q is D_1^T times a bounded
plane matrix times D_1, retaining both shear clovers, so its bound
in (7) holds without positivity of the plane matrix.

Put X_h=Sigma^(-1/2) chi M_h S K^(1/2). L159's interior
||h_k||_infinity<=C a p(k), bounded ||Sigma^(-1/2)|| and endpoint
incidence, and L157's Tr K<=C N^5 give

    ||X_h||_HS<=C p(k) N^(3/2).                         (8)

The polynomial p may be enlarged a fixed number of times. Smoothness
is used only on the residual input, never across the upper jump.

For the direct term set Z_q^0=K^(1/2) S^T M_q Sigma^(1/2).
Finite trace Cauchy--Schwarz and the Hilbert--Schmidt ideal inequality
give exactly

    ||Z_q^0||_HS^2=Tr[Sigma M_q S K S^T M_q]
       <=||Sigma||_HS ||M_q S K S^T M_q||_HS
       <=C ||Sigma||_HS ||q||_infinity^2 ||K||_HS.       (9)

L156(7) gives ||K||_HS<=C N^4; L159(6) gives
||q_l||_infinity<=C a^3 p(l) globally, including normal end edges.
The full spectrum of L026 gives

    ||Sigma||_HS<=C N^2 sqrt(log(eN)).                  (10)

To check (10), each component has one edge index in {0,...,N-1}
and three vertex indices in {1,...,N-1}, eigenvalue >=4|r|^2/N^2,
and at most 4m^3 indices with max r_j=m. Its inverse-square sum is
at most (N^4/4) sum_(m=1)^(N-1) 1/m. Sum the four components and
take the square root. Constant axial edge modes remain included;
there is no zero eigenvalue or removed low-frequency sector.

With a=8/N, (9)-(10) prove

    ||Z_q^0||_HS<=C p(l) log(eN)^(1/4).                (11)

The direct summand is
6 Tr[(Sigma^(1/2) A Sigma^(1/2)) X_h Z_q^0].
For compatible finite matrices,
|Tr(B X Z)|<=||B|| ||X||_HS ||Z||_HS. Equations (7),(8),(11)
give its bound C p(k)p(l) N^(5/2) log(eN)^(1/4).
This improves the previous cubic count without an operator-smallness
claim about K.

### 3. Bound both Q forms in the actual prefix order

For a vertex matrix O define
Z(O)=K^(1/2) O Phi Sigma^(1/2). The exact Gram identity is

    ||Z(O)||_HS^2=Tr[K O K O^T],                        (12)

using Phi Sigma Phi^T=K, not independence of any fields.
L159(16) gives ||Z(O_q)||_HS<=C p(l) N^(1/2), because the action
column is the same globally co-closed q_l=L h_l with all faces retained.

The prefix summand in P_i(B) equals
-6 Tr[(Sigma^(1/2) B Sigma^(1/2)) X_h Z(O_q)].
The Q bound in (7), (8), and (12) therefore give
C p(k)p(l) N^2 for each of Q_3 and Q_6 separately. Their signs
stay as in (6). They are subcubic in V_i, not deleted from the full
residual or from the separate T_i branch.

### 4. Remove axial and midpoint-error transport, retaining transverse transport

The exact identity D_0^T q=0 makes O_q's diagonal zero. Its two
off-diagonal entries across an interior edge are q_e,-q_e.
Normal end edges enter the diagonal cancellation before boundary
vertices are omitted. Thus L159(10)-(11), with the forward sign
specified above, give

    O_q=sum_(j=1)^4 m_(j,l) J_j+E_l,
    ||E_l||<=C a^4 p(l).                               (13)

In detail each endpoint evaluation differs from the edge-midpoint
sample by C a times q's physical C^1 norm, itself O(a^3 p(l)).
E_l has bounded row/column degree and zero diagonal. No action-column
cutoff or smooth extension of the forest lift is used.

Put Y=M tensor G, M_st=min(s,t) on 1,...,N-1 and G the transverse
Dirichlet scalar inverse. L156 gives 0<=K<=Y. For every real O,

    Tr[K O K O^T]<=Tr[Y O Y O^T].                       (14)

First replace K against the positive O K O^T, then the other K
against O^T Y O. This requires no commutation. L159(12), in its
lower-anchored and upper-free axial mixed energy, gives
||Y^(1/2) m_(j,l) Y^(-1/2)||<=C a^3 p(l).
The global physical C^2 hypothesis holds for precisely the action-mode
extension specified here. L159(14)-(15) give

    ||Y^(1/2) J_1 Y^(1/2)||_HS<=C N^3,
    ||Y^(1/2) J_j Y^(1/2)||_HS<=C N^(7/2), j=2,3,4.

An overall sign of J_1 in its anchored-difference representation does
not affect these norm bounds. Consequently (12)-(14) give

    ||Z(m_(1,l) J_1)||_HS<=C p(l),
    ||Z(m_(j,l) J_j)||_HS<=C p(l) N^(1/2), j=2,3,4.     (15)

Also ||Y||_HS<=C N^4. The weighted inequality
||Y^(1/2) E_l Y^(1/2)||_HS<=||E_l|| ||Y||_HS gives

    ||Z(E_l)||_HS<=C p(l).                             (16)

For that inequality, diagonalize Y, use
2 lambda_r lambda_s<=lambda_r^2+lambda_s^2, and bound each row and
column squared norm of E_l by ||E_l||^2. No symmetry of E_l is needed.
The axial domain remains lower anchored and upper free, with all
transverse Dirichlet end edges, as in L159.

Use (7),(8),(15)-(16) for P_i(A^gen), replacing O_q first by its
axial piece and then by E_l. Each error is bounded by
C p(k)p(l) N^(5/2). The remaining trace is exactly (2), with m before
J and F before A^gen. No parity, freezing or covariance-replacement
claim has been made for that remaining trace.

### 5. Full heat sum, threshold and verification

L156(8) gives sum_(k,l)|c_(i;kl)|p(k)p(l)<=C_i uniformly over
the complete spectrum for every fixed p. Thus every displayed bound
sums for both actual probes without a mode cutoff. Equations
(6),(11),(15),(16) prove (3), since

    a^3 N^(5/2) log(eN)^(1/4)
       =512 N^(-1/2) log(eN)^(1/4) -> 0.

These estimates are analytic and use no numerical heat enclosures.
Run `python3 scripts/combined-ward-response/check_smooth_action_prefix_reduction.py`.
The full certificate is
`scripts/combined-ward-response/smooth-action-prefix-reduction-certificate.json`.
Its exact finite sign/order/color and squared Gram/Cauchy--Schwarz
checks concern algebra only. Mesh-uniform estimates and actual-mode
applicability are the analytic proof above, not mesh extrapolations.

This is a successful subcubic error reduction, not an evaluated limit.
The retained transverse transport still has only a cubic bound.
Its signed limit, in the full prefix order with upper action
contributions retained, remains the missing step in this branch.

### 6. Separate critical audit of the preceding reduction (2026-10-21)

Verdict: (3) is accepted without correction, relative to the stated
L026/L028/L156/L157/L159 mode, covariance and residual inputs. This
audit checks the removed terms and their applicability; it does not
independently reprove those upstream inputs or any downstream static
rate. It uses the unchanged EXPLORE coverage in the ordered-static
assessment dated 2026-10-20, checked 2026-10-21. There is no claim of
progress beyond the sources checked.

Starting from L159(1), the two color factors are b_c and b_c^T,
so their trace is +2, not -2. The three exterior colors give +6.
The factor -6 in the prefix comes only from R=I-D_0 Phi. Cycling
that term gives K S^T M_q D_0 Phi Sigma B M_h S, exactly the
order K O_q F B M_h S. Linearity in B then gives (6), with each
Q form subtracted once. The distinct Q_3 average-of-squares and
Q_6 polarized-clover representations in L028 proof section 1
both have bounded plane coefficients; they need not be positive.
Compact coefficient support and bounded stencil range justify chi
separately for both generator orientations and both Q forms. No
localization of q or of a covariance source is made.

The direct term's improvement is genuine. Its Z factor squared is
the trace of Sigma against M_q S K S^T M_q, a symmetric positive
Gram matrix. Schatten Cauchy--Schwarz followed by the ideal inequality
gives (9), also for sign-changing q. For each relative component the
max-index shell has (m+1)m^3-m(m-1)^3<=4m^3 labels. Together with
the lower eigenvalue bound this gives the complete inverse-square
sum in (10), including the own-direction constant mode. Thus
||Z_q^0||_HS^2<=C p(l)^2 log(eN)^(1/2), since the powers
N^2, a^6 and N^4 cancel. Multiplication by the N generator
bound and N^(3/2) X bound yields precisely the first error in (3).
For either Q, its bounded whitened norm instead gives
1*N^(3/2)*N^(1/2)=N^2 in the unchanged prefix order.

For the transport identity, the row-v diagonal of S^T M_q D_0
is (D_0^T q)_v. The actual q=L h_l=L v_l has this value zero
on the full relative space. An interior oriented edge has row-tail,
column-head entry +q_e and its reverse entry -q_e, agreeing with
the stipulated J_j. Normal end edges contribute to that diagonal
identity before pinned vertex columns are omitted. Their omission
therefore creates no uncounted diagonal term. The product-mode
extension of q in L156(10)/L159(6), including normal end rows,
has physical C^1 norm O(a^3 p(l)); endpoint/midpoint differences
give O(a^4 p(l)) with bounded row and column multiplicity. This
is smoothness of L v_l, not of the forest jump or a rough column.

The tensor energy used for (15) has M^-1=B^T B with the lower
anchor and free upper end. The complete transverse Dirichlet
gradient retains both end edges. L159(12)'s mixed product rule and
the two slice Poincare inequalities apply to this smooth multiplier
without a boundary cutoff. The axial skew factor costs N^3 in HS
norm, so its multiplier a^3 leaves O(p(l)); the transverse factor
costs N^(7/2), leaving O(p(l) sqrt(N)). For the nonsymmetric
midpoint error, (14) and the weighted HS inequality in section 4
give a^4 ||Y||_HS=O(p(l)). The axial and midpoint errors consequently
cost N*N^(3/2)*1=N^(5/2). None of these steps treats the signed
response as positive or commutes a multiplier through K, F or Sigma.

Every estimate has a fixed polynomial mode envelope. L156(8)'s
complete double heat summability therefore applies separately to
the direct term, both Q terms, axial transport and midpoint error,
for each actual probe. The final bound is O(N^(5/2)log(eN)^(1/4)),
strictly subcubic; no constant mode, action face or heat label is
deleted. The existing exact checker was rerun: all ten identities
have error zero and both squared trace inequalities pass, with no
failures in the complete saved certificate. Those synthetic checks
verify algebra only; the uniform count above is analytic.

This closes L175's preceding-reduction qualification in the audited
static-coefficient chain, relative to its explicit upstream imports.
It changes no bound, trace definition or mathematical dependency.
It does not imply isolated cubic vanishing, finer asymptotics,
quantitative L011 assembly, or any interacting/construction result.

## Mathlib

Full matching theorem: **not checked**. Supporting finite trace
Cauchy--Schwarz, Schatten ideal inequalities, covariance Gram identities
and relative-cochain spectral sums: **not checked**. Unknown coverage
is not absence. Reuse the unchanged
[assessment](../drafts/literature/2026-10-12-cubic-residual-action-cubic-scale.md).
No new external theorem is imported or reproved. The specialization
gets a subcubic error in this covariance order while retaining the
action column, distinct Q forms and pinned domains.

