# L225 — Uniform mass-removal error for the actual co-closed trace

## Hypotheses

Use L090's hypotheses and ordinary dimensionless coordinates: the finite
SU(2) Gaussian on the relative all-face cube, straight lower-rooted
direction-1 forest, admitted even N, a=8/N, tau=1/16, and the actual
probes i=3,6. The bare expansion is taken at fixed mesh first. All
interior axial levels, relative end rows, component constant modes,
ordered coincident plaquettes and exterior heat labels remain.

Import L090's space E, Delta_E, Q, K=Delta_E^(-1)Q, G0 and
H_k^h=Q H_k Q. Put, for 0<epsilon<=1,

    K_epsilon=(Delta_E+epsilon I)^(-1)Q,
    J_epsilon=K-K_epsilon,
    L_N=log(eN).

Let T_epsilon denote exactly L090's trace (5) with both K occurrences
replaced by K_epsilon, leaving Q, G0, H_k^h and c_(i;kl) unchanged:

    T_epsilon=(1/2) sum_(k,l)c_(i;kl) {
      Tr(H_k^h G0 K_epsilon (H_l^h)^T K_epsilon)
     +Tr(H_k^h K_epsilon G0^T (H_l^h)^T K_epsilon) }.

L089 defines T_red and controls T_hh-T_red, including the original
exterior-circulation terms and both curvature-form subtractions.
No assertion about T_epsilon at varying epsilon is imported from
L090's fixed-epsilon limit.

## Conclusion

There are constants independent of N and epsilon such that

    Tr(Delta_E J_epsilon^2) <= C N^4 epsilon,              (1)

    ||H_k^h J_epsilon||_HS
      <= C p(k)[N sqrt(epsilon)+sqrt(N L_N)],             (2)

    |T_red-T_epsilon|
      <= C_i[N^3 sqrt(epsilon)+N^(5/2)sqrt(L_N)],         (3)

    |T_hh-T_epsilon|
      <= C_i[N^3 sqrt(epsilon)+N^(5/2)sqrt(L_N)].         (4)

Here p is a fixed polynomial controlled by L088's complete heat sum,
enlarged as in L090. In particular, at epsilon=N^-1,

    |T_hh-T_(N^-1)| <= C_i N^(5/2)sqrt(L_N).             (5)

Thus the requested O(N^(5/2)L_N^2) bound for T_hh is equivalent to
that bound for this precise varying-mass trace. Neither bound is
established here. The unresolved part is quantitative control of the
massive trace with its exact transverse projection and variable
coefficients. No complete-response rate, interacting error estimate,
continuum construction or mass-gap claim follows.

## Proof

### 1. Estimate the full resolvent difference before splitting norms

The commuting Q is an orthogonal projection. The finite spectral theorem
therefore bounds the left side of (1) by the full component sum

    sum_rho epsilon^2 / [rho (rho+epsilon)^2].            (6)

The eigenvalues and multiplicities here are those used in L089(5) and
L090(8)--(10). For shell r=max_j m_j>=1 there are at most C r^3
labels, including all component multiplicities, and
rho>=4r^2/N^2. There is no full zero eigenvalue: the axial label on
E is Dirichlet and positive. Zero own-direction component labels
remain in the count. For each summand in (6), use both inequalities

    epsilon^2/[rho(rho+epsilon)^2] <= rho^-1,
    epsilon^2/[rho(rho+epsilon)^2] <= epsilon^2 rho^-3.

Set R=N sqrt(epsilon). If R>=1, the sum of shells r<=R is at most

    C N^2 sum_(1<=r<=R) r <= C N^2 R^2=C N^4 epsilon.

The complementary shells contribute at most

    C epsilon^2 N^6 sum_(r>R) r^-3
      <= C epsilon^2 N^6 R^-2=C N^4 epsilon.

An empty part contributes zero; extending the upper shell limit to
infinity only increases the bound. If R<1 there are no low shells,
and all of (6) is bounded by C epsilon^2 N^6, which is at most
C epsilon N^4 because N^2 epsilon<1. This proves (1) uniformly,
including masses below the finite-volume spectral scale. It does not
assume that the covariance is bounded uniformly in operator norm.

### 2. Retain the staggered boundary term

J_epsilon=K F(Delta_E), with
F(rho)=epsilon/(rho+epsilon) in [0,1]. Thus it is an admissible J
in L090(7). Its natural-difference energy is the left side of (1).
Moreover J_epsilon^2<=Delta_E^-2 as commuting positive operators.
L090(8)--(9), with the full fixed-width collar E_partial, gives

    ||J_epsilon||_HS <= C N^2 sqrt(L_N),
    ||E_partial J_epsilon||_HS <= C N^(3/2)sqrt(L_N).

Insert these bounds and (1) into L090(7):

    ||H_k J_epsilon||_HS
      <= C a p(k)[N^2 sqrt(epsilon)
                   +a N^2 sqrt(L_N)+N^(3/2)sqrt(L_N)]
      <= C p(k)[N sqrt(epsilon)+sqrt(N L_N)].

This preserves the collar on every physical face, including normal
end rows that are not scalar Dirichlet rows. Since Q J_epsilon
=J_epsilon and Q is a contraction, left multiplication by Q proves
(2). Also H_k^h is exactly skew-symmetric and J_epsilon is symmetric,
so the same bound applies to J_epsilon(H_k^h)^T and J_epsilon H_k^h.
No boundary extension or multiplier commutation is involved.

### 3. Telescope all four covariance replacements in their actual order

Write A=H_k^h and B=H_l^h temporarily, with no change of the residual.
L090(2),(11) and the contraction
K_epsilon=K Delta_E(Delta_E+epsilon I)^(-1) give

    ||G0|| <= C N,
    ||A K||_HS+||A K_epsilon||_HS <= C p(k) N,
    ||B K||_HS+||B K_epsilon||_HS <= C p(l) N.

The two differences in the first generator orientation are exactly

    Tr(A G0 K B^T K)-Tr(A G0 K_epsilon B^T K_epsilon)
      =Tr(A G0 J_epsilon B^T K)
       +Tr(A G0 K_epsilon B^T J_epsilon).                (7)

In the first term use cyclicity to pair J_epsilon B^T with K A;
in the second pair K_epsilon B^T with J_epsilon A. The remaining
G0 is bounded in operator norm. Finite Hilbert--Schmidt
Cauchy--Schwarz and skew-symmetry of A,B bound each term by

    C p(k)p(l)[N^3 sqrt(epsilon)+N^(5/2)sqrt(L_N)].       (8)

The other generator orientation has difference

    Tr(A K G0^T B^T K)-Tr(A K_epsilon G0^T B^T K_epsilon)
      =Tr(A J_epsilon G0^T B^T K)
       +Tr(A K_epsilon G0^T B^T J_epsilon).              (9)

Here pair A J_epsilon with B^T K in the first term and
A K_epsilon with B^T J_epsilon in the second. Equations (2) and
the preceding full-covariance bounds again give (8). These estimates
do not transpose one orientation into the other or differentiate any
base-law projection zero. The signed residual is never made positive.

L088(5), with L090's enlarged polynomial, states
sum_(k,l)|c_(i;kl)|p(k)p(l)<=C_i uniformly in N for each actual
probe. Summing (7)--(9) with the original factor 1/2 proves (3).
Every external heat label remains; no cutoff is introduced in that sum.
Finally L089(4) bounds |T_hh-T_red| by C_i N^2 sqrt(L_N), which
is absorbed in (4). Setting epsilon=N^-1 proves (5). The stated
equivalence at the larger threshold follows by the triangle inequality
in both directions, not by existence of a varying-mass limit.

### 4. Qualification and downstream test

This is a local REPRODUCTION using the assessed finite spectral,
product-difference and trace methods. The necessary specialization is
the uniform weighted full-spectrum sum (6), replacing L090(12)'s
coarser separate low/high norm bounds. Existing qualitative vanishing
is not reproved, and no general matrix-decay theorem is reproved or
used outside its inspected hypotheses. No originality beyond the
sources checked is claimed.

Equation (5) resolves only the mass-removal part of the approved
quantitative target. L090(16)'s projection estimate still has a
mass-dependent constant, and its polynomial freezing/collar estimates
are stated at fixed degree. They must be controlled uniformly before
using epsilon=N^-1 in the remaining trace. In particular L090(22)
does not imply that a^3 T_(N^-1) tends to zero or gives its rate.
Both original probes and generator orientations, all boundary rows
and the exact heat weights must remain in that further estimate.
The complete coefficient's other rates and the interacting reflected
error <=c_box/2 remain independent unresolved requirements.

### 5. Separate critical audit of mass removal

The 2026-10-18 audit accepts (1)--(5) relative to the imported L088
heat expansion, L089 complete-sector remainder and L090 finite
generator, coefficient and relative-cochain estimates. It checks the
specialization in sections 1--3, rather than recursively auditing those
inputs. No stronger rate or originality claim is made.

**Full spectrum, including sub-box masses.** L089(5), importing
L086 section 1, specifies exactly three transverse components. Each has positive
axial index, zero permitted in its own transverse direction, and two
other positive transverse indices. The dimensionless eigenvalues are
rho_m=4 sum_j sin^2(pi m_j/(2N)). Hence rho_m>=4|m|^2/N^2,
max_j m_j=r>=1 has at most C r^3 labels, and there is no full zero
mode. All component multiplicities are included. The sine lower bound
uses 0<=pi m_j/(2N)<=pi/2; no continuum eigenvalue is substituted.

Simultaneous diagonalization of Delta_E and Q gives the eigenvalue
epsilon/[rho(rho+epsilon)] for J_epsilon on its retained subspace.
The weighted trace therefore has the full-space majorant (6). For
R=N sqrt(epsilon)>=1 its low shells satisfy

    low-shell contribution <=C N^2 sum_(r<=R) r
                           <=C N^2 R^2.

Its high shells satisfy

    high-shell contribution <=C epsilon^2 N^6 sum_(r>R) r^-3
                            <=C epsilon^2 N^6/R^2.

Here rho^-1 or epsilon^2 rho^-3, respectively, is bounded for each
summand using the shell's lower eigenvalue. The
two displayed quantities are C N^4 epsilon. The power-sum estimates
hold also for noninteger R, and empty shell ranges contribute zero.
For R<1 all shells use the second estimate, giving
C epsilon^2 N^6<=C epsilon N^4. This verifies the uniform threshold
(1), including epsilon<N^-2; no low mode or component constant mode
has been discarded.

**Physical collar and both sides of the alternating factors.** The
matrix J_epsilon=K epsilon(Delta_E+epsilon I)^(-1) meets precisely
L090(7)'s spectral-contraction hypothesis. In particular QJ=J and
J J^T<=R_0^2, R_0=Delta_E^-1. Each normalized component product
mode has squared value at most 16/N^4 at every existing row, including
normal end rows. The complete shell sum gives Tr R_0^2<=C N^4 L_N,
so (R_0^2)_(ee)<=C L_N. The fixed-width physical collar has at most
C N^3 rows. Positive operator comparison on these diagonal entries
gives exactly the two Hilbert--Schmidt bounds in section 2, without
commuting its row selector through Q or J.

L090(7) retains all path shifts and bounds face-crossing exceptions by
these actual collar values. Its use requires no scalar Dirichlet value
for a normal edge and no smooth extension across a pinned zero.
After multiplication by a=8/N, its three contributions are bounded by

    C p(k)[N sqrt(epsilon)+sqrt(L_N)+sqrt(N L_N)].

The middle term is absorbed by the last. Left multiplication by Q
proves (2), because QJ=J. Symmetry of J and skew-symmetry of
H_k^h give equal norms for the transposed left products. Similarly
K_epsilon=K F_epsilon, with F_epsilon a commuting spectral
contraction, gives ||H_k^h K_epsilon||_HS<=||H_k^h K||_HS;
transposition supplies every other covariance placement used below.
No contraction is moved across H_k^h.

**Four replacements, two orientations.** Put A=H_k^h, B=H_l^h
and J=J_epsilon. The first orientation's two error terms in (7),
after cyclic rotation, have respectively the orders

    Tr((K A) G0 (J B^T)),
    Tr((J A) G0 (K_epsilon B^T)).

The second orientation's two error terms in (9) already have orders

    Tr((A J) G0^T (B^T K)),
    Tr((A K_epsilon) G0^T (B^T J)).

In each line one displayed parenthesized factor has norm at most
C p [N sqrt(epsilon)+sqrt(N L_N)], and the other has norm at most
C p N. The factor between them has operator norm at most C N.
The finite trace inequality |Tr(X G Y)|<=||X||_HS||G||||Y||_HS
therefore yields (8) for all four terms. These are the exact finite
telescoping differences; neither generator orientation is inferred
from the other and no cross term is omitted. The original factor
1/2 remains. L088's enlarged polynomial heat envelope sums their
absolute bounds for both probes. L089(4)'s N^2 sqrt(L_N) remainder
is below N^(5/2)sqrt(L_N), proving (3)--(4).

Finally epsilon=N^-1 makes N^3 sqrt(epsilon)=N^(5/2), proving
(5). The triangle inequality in either direction gives the stated
equivalence at N^(5/2)L_N^2. This substitutes into a uniform finite
inequality, not a fixed-mass limiting theorem. ATTEMPTS/030's warning
thus remains respected. The audit finds no defect and supplies no
bound on T_epsilon by itself; downstream projection, bulk and boundary
results must be invoked separately. It establishes no effective
constant, complete-response rate or interacting construction.

## Mathlib

Full matching result: **not checked**. Supporting finite spectral,
Hilbert--Schmidt trace inequalities, relative-mode shell counts and
power-sum bounds: **not checked**. Unknown coverage is not absence.
