# L102 — Remove the left orientation from the gradient-base crossed pair

## Hypotheses

Use L091's exact gradient-base crossed pair R_gx for SU(2), both actual
L010 probes i=3,6, L018's residual, the straight lower-rooted direction-1
forest and the relative all-face fixed-link box (-4,4)^4. Let N be
sufficiently fine, admitted and even, a=8/N and tau=1/16. Take the bare
small-coupling coefficient at fixed mesh before refinement. Coordinates,
transposes and norms are ordinary dimensionless stored ones. Retain all
interior axial levels, transverse end rows, ordered plaquette pairs
including coincidences and the complete exterior heat sum.

Import L088/L091's actual level-diagonal skew matrices Omega_k and real
symmetric coefficients c_(i;kl,a). Write P=Pcal, Q=Qcal,

    K_g=M tensor P_T, M_st=min(s,t),
    K_h=(L_D tensor I+I tensor Delta_T)^(-1) Q,
    Omega_(gg,k)=P Omega_k P, Omega_(gh,k)=P Omega_k Q.

Here P_T=T G T^T, G=(T^T T)^(-1) on transverse pinned vertices.
Use L092/L093's exact maps C=Tcal G_v B, H_g,
G_T1=I_T^T K_a I_1 and the full off-diagonal residual covariance V_gh.
The generator retains all actual endpoint/clover filters and the compact
displacement. Set Q_0=Q_3+Q_6, the actual curvature forms rather than
the co-closed projection Q. Let F_Q be L093's whitened gh block of
the Q_0 covariance insertion; A_k and J_l below are L091's whitened
alternating blocks, not residual matrices.

## Conclusion

Define the two actual gradient-base generator orientations by

    G_L(i,N)=sum_(k,l)c_(i;kl,a)
      Tr(Omega_(gg,k) H_g K_a I_T K_h Omega_(gh,l)^T K_g),
    G_R(i,N)=sum_(k,l)c_(i;kl,a)
      Tr(Omega_(gg,k) C G_T1^T Q Omega_(gh,l)^T K_g),
    G_Q(i,N)=2 sum_(k,l)c_(i;kl,a) Tr(A_k F_Q J_l^T).       (1)

Then, with no outside factor 3 included,

    R_gx=G_L+G_R-G_Q,
    |G_L|<=C_i N^(5/2), |G_Q|<=C_i N^2,
    |R_gx-G_R|<=C_i N^(5/2), |G_R|<=C_i N^3.              (2)

In particular a^3(R_gx-G_R)=O_i(N^(-1/2))->0. Existence and value
of the scaled limit of this pair are now exactly the remaining
questions for a^3 G_R; neither is established. This G_R has a gradient
base covariance and is distinct from L093's co-closed-base R_R.

The quantitative input is an estimate in the actual unsandwiched order:

    ||K_g Omega_(gg,k)||_HS
      =||Omega_(gg,k) K_g||_HS<=C p(k) N^(1/2).           (3)

It uses the complete signed plaquette-layer sum before taking norms.
It does not improve the unrestricted crossed residual norm or extend
L065's scalar bound to a transverse right input.

The complete other/other limit and comparison with -12 gamma D_i remain
open. Co-closed-base R_R and transverse H still lack cubic control;
the E/H functionals are unevaluated. Other response jets, finer powers
and logarithm, matching, interacting error <=c_box/2, continuum axioms,
reflection positivity, infrared control and finite positive mass remain
independent gaps. No candidate solution exists.

## Proof

### 1. Transfer the signed layer identity through the exact isometry

Put U=T G^(1/2). Then U^T U=I and UU^T=P_T on the actual finite
relative transverse spaces. At level s let S_(k,s) be the edge matrix
P_T Omega_k(s) P_T. The circulation selector annihilates T exactly.
Consequently the four path/curvature terms in L088(3) vanish after
this two-sided projection. Composing the remaining two terms with
T on both sides gives precisely L087(10)'s vertex matrix

    Xi_(k,s)=sum_p f_(k;s,p)(b_p^T q_p-q_p^T b_p),

where b_p,q_p in this display are the telescoped vertex rows of
L087(9), not the original link rows. Thus

    U^T S_(k,s) U=G^(1/2) Xi_(k,s) G^(1/2),
    S_(k,s)=U [G^(1/2) Xi_(k,s) G^(1/2)] U^T.             (4)

The second equality follows because S_(k,s)=P_T S_(k,s) P_T.
Isometry invariance of the Hilbert--Schmidt norm and L087(11)--(13)
therefore give

    ||S_(k,s)||_HS<=C a^3 p(k) N^(3/2),                  (5)

uniformly in s. This imports the proved signed first-difference gain:
interior neighboring plaquettes pair, and wedges with a pinned vertex
vanish. All transverse end edges and all planes remain. It is not the
O(a^2) estimate of an unsummed circulation multiplier. No smoothness
or localization of the rough input is used.

Omega_(gg,k) is level diagonal. The (s,t) block of K_g Omega_(gg,k)
is exactly M_st S_(k,t). Distinct blocks are orthogonal in the
Hilbert--Schmidt inner product, so

    ||K_g Omega_(gg,k)||_HS^2
       =sum_(s,t) min(s,t)^2 ||S_(k,t)||_HS^2
       <=C a^6 p(k)^2 N^3 sum_(s,t) min(s,t)^2
       <=C a^6 p(k)^2 N^7<=C' p(k)^2 N.                (6)

For the last inequality there are fewer than N^2 pairs and each
min(s,t)^2<=N^2, and a=8/N. Transposition and
Omega_(gg,k)^T=-Omega_(gg,k) show that its opposite-order product
has the same norm. This proves (3). Both full interior-level indices
and their exact weights remain; no prefix is replaced by a local value.

### 2. Split the actual insertion and check the factors

Unwhitening L091's definitions on the positive gradient and co-closed
subspaces gives the finite trace identity

    Tr(A_k F J_l^T)
       =Tr(Omega_(gg,k) V_gh Omega_(gh,l)^T K_g).          (7)

Indeed A_k=K_g^(1/2) Omega_(gg,k) K_g^(1/2),
F=K_g^(-1/2) V_gh K_h^(-1/2), and
J_l=K_g^(1/2) Omega_(gh,l) K_h^(1/2). Multiplying these in
their displayed order cancels only adjacent square roots on their
own ranges; cycling the remaining K_g^(1/2) gives (7).

L092(10) fixes the exact covariance representative. Apply L093(11)
to the same gh insertion, retaining both generator orientations:

    V_gh^gen=(H_g K_a I_T K_h+C G_T1^T Q)/2,
    V_gh=V_gh^gen-V_gh^Q.                               (8)

The applicability argument is already proved in L093, section 3:
C I_1^T L=H_g and L I_T K_h=I_T Q on the relative spaces;
both A_gen and Q_0 annihilate full gauge gradients. No scalar
polarization or differentiated base-law projection zero is involved.
L091's R_gx is twice the sum of (7). Substituting (8) cancels that
2 against the generator's 1/2 and gives exactly (1)--(2)'s identity.
The Q insertion instead retains its factor 2 and its negative sign.
L085's outside factor 3 is not part of any trace in this lemma.

### 3. Bound the left orientation in its actual order

Import the exact-order estimates L093(1),(13):

    ||H_g K_a I_T||<=C/a,
    ||K_h Omega_(gh,l)^T||_HS<=C p(l) N.                 (9)

The first uses a pinned axial prefix identity with compact coefficient
support; it is not a bound on C G_T1^T Q. The second retains the full
relative spectrum, exterior-circulation terms and staggered end rows.
Their hypotheses are unchanged here. Enlarge one fixed polynomial p
to cover (5),(9), so L088/L091's full heat bound still gives

    sum_(k,l)|c_(i;kl,a)|p(k)p(l)<=C_i.                 (10)

Cycle one summand of G_L, then use finite-matrix trace
Cauchy--Schwarz and the operator ideal inequality in exactly this order:

    |Tr(K_g Omega_(gg,k) H_g K_a I_T K_h Omega_(gh,l)^T)|
      <=||K_g Omega_(gg,k)||_HS ||H_g K_a I_T||
                                     ||K_h Omega_(gh,l)^T||_HS
      <=C p(k)p(l) N^(1/2) a^(-1) N
      <=C' p(k)p(l) N^(5/2).                           (11)

No covariance, multiplier or projection has been commuted across an
insertion. Summing (11) with (10) proves the G_L bound for both probes.
This bound gains a half power relative to the cubic threshold; it
does not assert an unscaled limit or an O(N^2) bound for G_L.

### 4. Remove only the bounded curvature subtraction

L093, section 4, imports L089(11)'s full Hodge bound
||Sigma^(1/2) Q_0 Sigma^(1/2)||<=C and proves that the resulting
complete forest insertion has a mesh-uniform whitened norm. Its
off-diagonal block F_Q is consequently bounded by C. This is the
same Q_0 and same pair of forest row maps as in (8), including all
prefixes; positivity of Q_0 is unnecessary.

L091(10),(12) gives ||A_k||_HS<=C p(k)N^(1/2) and
||J_l||_HS<=C p(l)N^(3/2). Hence

    |Tr(A_k F_Q J_l^T)|<=C p(k)p(l)N^2.                 (12)

Summing (12) with its factor 2 proves |G_Q|<=C_i N^2. Equations
(11)--(12) prove the error bound in (2), and multiplication by
a^3=(8/N)^3 makes that error vanish. Finally L091(5)'s already proved
|R_gx|<=C_i N^3 and the exact identity give |G_R|<=C'_i N^3 by
the triangle inequality. This last bound is a consequence of the
complete signed pair's bound, not a new operator bound on its reverse
residual or an evaluation of its coefficient.

All exterior series rearrangements are legitimate: the finite matrices
at each mesh have the displayed polynomial bounds, and (10) controls
their absolute sums. Thus no exterior mode, residual placement,
ordered orientation or coincident plaquette has been dropped.

### 5. Relevance and limitations

The completed bounded test supplies a controlled signed reduction of
the actual gradient-base pair. Its remaining G_R keeps the order
C G_T1^T Q and the undifferentiated K_g on the other side of the
alternating matrix. L100's co-closed-base R_L limit, L101's scalar E
limit and L065's component-1 form theorem do not evaluate this trace.
Its full prefix and cross-component residual still need a separately
justified limit mechanism. In particular (2) establishes neither a
limit nor a sign for G_R or R_gx, and no compensation with L084.

This is one RESEARCH / REPRODUCTION attempt under the unchanged ready
EXPLORE assessment
`drafts/literature/2026-10-10-other-other-cubic-leading-scale.md`.
Known finite contraction, signed layer and prefix estimates are
imported with unchanged hypotheses. The new local specialization is
(3) in the unsandwiched gradient-base order and its use in (11).
It is standard-method local progress, with no claim of originality
beyond the checked sources. No numerical script or IEEE premise is
needed; any later numerical comparison with gamma D_i must retain
L084/L082's qualifications. Structural validation is not verification
of these mathematical estimates.

## Mathlib

Full matching gradient-base reduction: **not checked**. Supporting
finite block traces, Hilbert--Schmidt isometry invariance, operator
ideal inequalities and absolute-series summation: **not checked**.
Unknown availability is not evidence of absence. No new external
Ward or flow theorem is invoked or reproved.
