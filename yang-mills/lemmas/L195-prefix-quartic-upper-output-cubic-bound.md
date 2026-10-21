# L195 — Cubic control of the prefix quartic's upper output

## Hypotheses

Use exactly L187 and L194's SU(2) setting: the relative box
(-4,4)^4, admitted even N, a=8/N, straight lower-rooted direction-1
forest, complete displacement and both actual L010 probes i=3,6 at
tau=1/16. The fixed-mesh bare expansion precedes refinement. Work in
ordinary full variable-link coordinates with all physical faces,
normal end edges, constant own-direction modes and heat modes retained.
Vertex potentials are pinned on every boundary vertex.

Keep S, P, A=PAP with both insertion subtractions, M=2SAS,
V=q Phi, H=1-D Phi/2 and U_n=diag(Vn)H-diag(Hn)V unchanged.
For a link vector y write J_y=P Gamma_y P, with Gamma_y as in L194(1).
Thus J_y is skew and M is symmetric and signed. Let Pi be the diagonal
orthogonal projection onto all upper direction-1 normal variable
edges, whose tail has axial level N-1 and whose head is on the
upper pinned face. Pi does not commute with P.

Use the exact full heat expansion from L187(13),

    SB_i=a^2 sum_(k,l) d_(i;kl) n_k e_l^T,  n_k=S e_k,
    sum_(k,l)|d_(i;kl)| p(k)p(l)<=C_(i,p)                 (1)

for every fixed polynomial weight p, with e_l the ordinary normalized
full Hodge modes. All sums in (1) are complete at each mesh.

## Conclusion

Define the upper-output part of the third quartic placement by the
original trace order:

    Q_(3,i,N)^top=-6 a^2 sum_(k,l) d_(i;kl)
                      Tr(Pi J_(e_l) M U_(n_k)^T Pi).   (2)

Then, for both actual probes,

    |Q_(3,i,N)^top|<=C_i N^3.                          (3)

The complementary output part is defined by replacing both Pi in
(2) by I-Pi. It adds exactly to Q_3. Its available bound remains
O(N^(7/2)), by subtraction from L187's complete bound; no improvement
for that part is established here.

In L194's common signed group the upper-output contribution is
-Q_3^top, with the same bound. Equation (3) does not make this term
o(N^3), determine its sign or prove a scaled limit. The sextic retains
its O(N^3 sqrt(log(eN))) bound, and the full joint group retains only
O(N^(7/2)) control. In particular the requested finite a^3-scaled
joint limit remains unproved. The independent f_(i,2),r_0 term, full
compensation, finer asymptotics, finite matching, reflected error
<=c_box/2, continuum axioms and infrared finite mass remain unresolved.
This is a local refinement by standard matrix estimates, with no
progress beyond checked literature claimed.

## Proof

### 1. Select actual output rows before rewriting the trace

L194's signed formula for the complete third placement is
-6 a^2 sum d_(i;kl) Tr(J_(e_l) M U_(n_k)^T). For any finite matrix X,

    Tr X=Tr(Pi X Pi)+Tr((I-Pi)X(I-Pi)).                 (4)

Indeed these two terms sum the disjoint diagonal entries of X.
This proves the exact decomposition, without moving Pi through P,
J_y, M or U_n. The selected rows in (2) are the common output index
of J_y and U_n; neither the inputs of those maps nor the sources of
any covariance are restricted.

On precisely these upper edges, pinned endpoint values give
(D Phi)_g=-V_g. Consequently H_g=I_g+V_g/2 and
(Hn)_g=n_g+(Vn)_g/2. Substitution into U_n gives L187(4)'s exact row
identity

    Pi U_n=Pi{diag(Vn)-diag(n)V}.                       (5)

Thus both double-prefix pieces cancel on this output layer. This
identity is used on the unprojected U_n, before any row selection
in L187's different identity for P U_n. It retains every upper edge.

### 2. The upper-output energy factor

The complete relative Green estimate used in L194, proof section 1,
gives Sigma_gg<=C on every variable edge. Positive domination
0<=S<=Sigma therefore gives S_gg<=C. There are (N-1)^3 upper normal
variable edges, so

    ||Pi S^(1/2)||_HS^2=Tr(Pi S Pi)<=C N^3.             (6)

L187(12) separately retains the full upper prefix covariance:

    ||Pi V S^(1/2)||_HS<=C N^2.                        (7)

This is not inferred from a small covariance on the upper face.
Its positive comparison is the last interior vertex value of
Phi S Phi^T<=U tensor G, giving (N-1)Tr G=O(N^4).
L187(14)–(15) give, for the actual external n_k,

    ||n_k||_infinity<=C p(k),
    ||Vn_k||_infinity<=C N p(k).                       (8)

The first bound holds globally before retraction, including the upper
normal edge; it asserts no smoothness for a rough tilted column.
Apply (5)–(8) and the triangle inequality to obtain

    ||Pi U_(n_k) S^(1/2)||_HS
      <=||Vn_k||_infinity ||Pi S^(1/2)||_HS
         +||n_k||_infinity ||Pi V S^(1/2)||_HS
      <=C p(k)(N^(5/2)+N^2)
      <=C' p(k) N^(5/2).                               (9)

### 3. Signed trace estimate and the entire external sum

Put E=S^(1/2) A S^(1/2). The complete residual form bound imported
in L187, proof section 5, is ||E||_op<=C N, and
M=2S^(1/2) E S^(1/2). No positivity of E is required.
L187(17) gives

    ||J_(e_l) S^(1/2)||_HS<=C N^(3/2).                 (10)

Indeed J_(e_l) S^(1/2)=P Gamma_(e_l) S^(1/2), since
P S^(1/2)=S^(1/2); thus the stated bound has exactly the original
projected order. Left multiplication by Pi is a contraction in
Hilbert–Schmidt norm even though Pi and P need not commute.
Set X=Pi J_(e_l) S^(1/2), Y=Pi U_(n_k) S^(1/2). Then the trace in
(2) is exactly 2 Tr(X E Y^T). Finite-dimensional Hilbert–Schmidt
Cauchy–Schwarz and the ideal inequality give

    |Tr(Pi J_(e_l) M U_(n_k)^T Pi)|
       <=2 ||X||_HS ||E||_op ||Y||_HS
       <=C p(k) N^5.                                  (11)

Multiply by 6a^2, sum |d_(i;kl)|p(k) using the complete summability
in (1), and use a^2=64/N^2. This proves (3). All remaining covariance
rows and every mode remain in (6)–(11). No finite fixture or spectral
truncation is needed for this analytic estimate.

By (4) and L187 the complementary part is bounded by
C_i(N^(7/2)+N^3)=O(N^(7/2)). L194 subtracts the whole Q_3 from its
sextic, so (2) has a minus sign in that group. Neither trace
decomposition nor any inequality here permits discarding its
cubic-scaled value. Restricting the projected product identity
P U_n=P{diag(Vn)-diag(Rn)V} to interior output rows would require
retaining the nonlocal projection across the upper layer; (5) does
not justify such a restriction. The complete bulk/joint estimate
and controlled approximation remain open.

## Mathlib

The matching actual-probe upper-output estimate and its supporting
lattice bounds: **not checked**. Supporting finite trace decomposition,
Hilbert–Schmidt Cauchy–Schwarz and ideal inequality coverage:
**not checked**; this is no assertion of absence. The matrix inequalities
are standard named inputs. The required specialization is the pinned
upper row (5), its full covariance count and the exact output selection
in (4); no general Gaussian or flow theorem is reproved.
The unchanged
[ready assessment](../drafts/literature/2026-10-14-joint-cubic-probe-jet-scale.md)
covers this intermediate estimate within the original joint-group test.
