# L226 — Derivative-weighted projection error in the co-closed trace

## Hypotheses

Use L090 and L225's finite SU(2) Gaussian, relative all-face cube,
straight lower-rooted direction-1 forest, admitted even N, a=8/N,
tau=1/16 and actual probes i=3,6. The bare expansion is taken at
fixed mesh first. All coordinates and norms below are ordinary stored
coordinates. Retain all axial levels, relative end rows, component
constant modes, coincident plaquettes and exterior heat labels.

Use L090's transverse-link space E, Delta_E, transverse incidence T,
vertex Laplacian Delta_0, co-closed projection Q, circulation Cc,
actual alternating H_k and generator G0. For 0<epsilon,delta<=1 put

    R_epsilon=(Delta_E+epsilon I)^(-1),
    Q_delta=I-I_ax tensor T(Delta_0+delta I)^(-1)T^T,
    D_delta=Q_delta-Q,
    K_epsilon=R_epsilon Q,
    K_(epsilon,delta)=R_epsilon Q_delta,
    H_k^h=Q H_k Q,       H_k^delta=Q_delta H_k Q_delta,
    L_N=log(eN).

T_epsilon is L225's trace. T_(epsilon,delta) is exactly L090's
projection-regularized trace: in both orientations of L090(5), replace
both H^h by H^delta and both K_epsilon by K_(epsilon,delta), leaving
G0 and the real symmetric c_(i;kl) unchanged. No projection is
differentiated and no coefficient or covariance is commuted past H_k.

## Conclusion

Uniformly in these masses and meshes,

    |T_epsilon-T_(epsilon,delta)|
      <= C_i[N^3 delta^(3/4)epsilon^(-1/2)
                         +N^(5/2)sqrt(L_N)].             (1)

Consequently L225 gives

    |T_hh-T_(epsilon,delta)|
      <= C_i[N^3 sqrt(epsilon)
             +N^3 delta^(3/4)epsilon^(-1/2)
             +N^(5/2)sqrt(L_N)].                         (2)

In particular,

    |T_hh-T_(N^-1,N^(-4/3))|
                         <= C_i N^(5/2)sqrt(L_N).        (3)

This comparison resolves the projection-removal error at the proposed
sector threshold. It does not bound the remaining regularized trace:
its localization, coefficient-freezing and boundary comparison still
need uniform quantitative control. L090's fixed-parameter limit is
not used at these varying masses. Other component rates, interacting
reflected error <=c_box/2, continuum axioms and finite positive mass
remain unproved. This is not a Yang–Mills construction candidate.

## Proof

### 1. Sum the projection difference over the complete transverse spectrum

The relative intertwining in L090(14)--(15) implies that Q_delta,
Q and D_delta commute with Delta_E and R_epsilon. They are symmetric;
Q_delta and D_delta are positive contractions. D_delta is zero on
co-closed fields, and on a normalized transverse gradient of vertex
energy lambda its eigenvalue is delta/(lambda+delta). In particular,

    Cc D_delta=0.                                       (4)

This is the finite relative cochain identity curl grad=0, including
all normal end rows. It involves the gradient *range* of D_delta;
it does not say H_k D_delta=0.

For transverse vertex modes, r=max(m_2,m_3,m_4)>=1 has at most Cr^2
labels and lambda>=4r^2/N^2. There are N-1 axial copies. Hence

    ||D_delta||_HS^2
       <= C N sum_(r=1)^(N-1) r^2 min(1,delta^2 N^4/r^4)
       <= C N^4 delta^(3/2).                            (5)

Here is the estimate for all delta, including below the box scale.
Set R=N sqrt(delta). If R>=1, the shells r<=R contribute at most
C N R^3. The remaining shells contribute at most
C delta^2 N^5 sum_(r>R) r^-2 <= C delta^2 N^5/R.
Both expressions equal C N^4 delta^(3/2) up to constants; empty
ranges contribute zero. If R<1, all shells contribute at most
C delta^2 N^5, which is at most C N^4 delta^(3/2).
There is no transverse vertex zero mode. This gradient-sector count
removes none of the component constant modes in the full edge space.

### 2. Keep the derivative estimate and its physical boundary collar

The row-product proof of L090(7) in fact applies to any matrix J
on E for which the displayed norms exist:

    ||H_k J||_HS <= C a p(k)[||nabla J||_HS
                       +a||J||_HS+||E_partial J||_HS].   (6)

To justify this extension beyond J=K F(Delta_E), its proof only
uses the four actual B^T M Cc and Cc^T M B placements of H_k,
the coefficient bounds |M|<=Ca p(k), neighboring differences
<=Ca^2 p(k), bounded shift multiplicity and the product-difference
identity on existing rows. None uses QJ=J. The Cc J terms are
bounded by natural component differences, and the Cc^T M B J
terms are expanded by that product identity. A shift crossing a
physical face contributes the input value in the fixed-width collar
E_partial. Thus (6) retains all staggered jumps, including normal
components with non-Dirichlet end values. Its natural energy is
||nabla J||_HS^2=Tr(J^T Delta_E J).

Apply (6) first to R_epsilon, then to J=R_epsilon D_delta. Both
matrices are symmetric spectral contractions of R_0=Delta_E^-1:
their squares are bounded by R_0^2 in the positive operator order.
L090(8)--(9) therefore gives, for either matrix J,

    ||J||_HS<=C N^2 sqrt(L_N),
    ||E_partial J||_HS<=C N^(3/2)sqrt(L_N).              (7)

These are positive spectral comparisons, not entrywise comparisons.
The natural energy of R_epsilon is bounded by Tr R_0<=C N^4,
using the same complete four-dimensional shell count as L090(10).
For R_epsilon D_delta, the scalar inequality
x/(x+epsilon)^2<=1/(4epsilon), x>=0, and (5) give

    ||nabla(R_epsilon D_delta)||_HS
                   <= C N^2 delta^(3/4)epsilon^(-1/2).

It follows, with a=8/N, that

    ||H_k R_epsilon||_HS<=C p(k) N,
    ||H_k R_epsilon D_delta||_HS<=C p(k) E_N,
    E_N=N delta^(3/4)epsilon^(-1/2)+sqrt(N L_N).          (8)

For the first bound, sqrt(N L_N) and sqrt(L_N) are bounded by
constant multiples of N for N>=2. For the second they are absorbed
by sqrt(N L_N). No smallness of the collar as delta decreases is
claimed or required at the selected threshold.

### 3. Use exact gradient annihilation on the other projection placement

There are two projection placements in each H_k. Their exact difference
is

    H_k^delta-H_k^h=D_delta H_k Q+Q_delta H_k D_delta.    (9)

By (4) and L089's expression for H_k, the right-gradient product is
exactly

    H_k D_delta=-Cc^T M_(b_k) Bq D_delta
                         +Cc^T M_(q_k) Bb D_delta.      (10)

In particular both terms with Cc on the right have vanished, while
both remaining terms retain their multipliers and paths in order.
Since Cc^T Cc<=Delta_E as relative quadratic forms,

    ||R_epsilon Cc^T||^2
       =||R_epsilon Cc^T Cc R_epsilon||
       <=||R_epsilon Delta_E R_epsilon||<=1/(4epsilon).

The bounded path norms and coefficient bounds from L090(6), together
with (5), yield

    ||R_epsilon H_k D_delta||_HS
       <= C a p(k)epsilon^(-1/2)||D_delta||_HS
       <= C p(k)N delta^(3/4)epsilon^(-1/2).            (11)

Transpose the first term of (9) after multiplying it by R_epsilon
on the right. Since H_k^T=-H_k and Q commutes with R_epsilon,
its norm is bounded by (11). The second term is bounded by (8)
because D_delta commutes with R_epsilon and Q_delta is a contraction.
Thus

    ||(H_k^delta-H_k^h)R_epsilon||_HS<=C p(k)E_N.        (12)

Skew-symmetry of both H_k^delta and H_k^h gives the same bounds
for the corresponding transposed left products. No projection
commutes past H_k or its variable coefficients in this argument.

### 4. Telescope every changed factor in both orientations

Let Q_s be either Q or Q_delta, H_k^s=Q_s H_k Q_s, and K_t be
either K_epsilon or K_(epsilon,delta). These are notation for the
endpoints of a finite telescoping expansion, not new approximations.
Commutation with R_epsilon and contraction of Q_s,Q_t imply from
(8) and (12) that

    ||H_k^s K_t||_HS<=C p(k)N,
    ||(H_k^delta-H_k^h)K_t||_HS<=C p(k)E_N,
    ||H_k^s(K_(epsilon,delta)-K_epsilon)||_HS
       =||Q_s H_k R_epsilon D_delta Q_s||_HS
       <=C p(k)E_N.                                    (13)

For the equality in the last line, use K_(epsilon,delta)-K_epsilon
=R_epsilon D_delta and commute Q_s only with these spectral factors.
All transposed placements obey (13), because K_t and its difference
are symmetric and every H_k^s and H_k^delta-H_k^h is skew-symmetric.

Each first-orientation trace has the order
Tr(A G0 K B^T K'), where A and B are the corresponding H factors.
Its cyclic form Tr(K' A G0 K B^T) is bounded by
||K' A||_HS ||G0|| ||K B^T||_HS. A change in either H or either
K therefore replaces exactly one of the two O(p N) factors by
O(p E_N). Each second-orientation trace has the order
Tr(A K G0^T B^T K'); its two Hilbert--Schmidt factors are A K
and B^T K'. The identical conclusion holds for all four changes
there. This accounts for all eight telescoping terms, with no
identification or omission of the two original generator orientations.

L090(2) gives ||G0||<=CN. Thus each changed trace has absolute bound

    C p(k)p(l)N^2 E_N
       =C p(k)p(l)[N^3 delta^(3/4)epsilon^(-1/2)
                                 +N^(5/2)sqrt(L_N)].

Sum using L088's complete bound sum|c_(i;kl)|p(k)p(l)<=C_i,
enlarged as in L090, and retain the original factor 1/2. This proves
(1). L225(4) then proves (2), already including L089's exterior-
circulation remainder and both curvature-form subtractions. Substitution
epsilon=N^-1 and delta=N^(-4/3) proves (3): both power terms are
N^(5/2). Only uniform finite inequalities receive this substitution.

### 5. Scope of the partial advance

This is a local REPRODUCTION of finite spectral and Hilbert--Schmidt
methods within the unchanged approved quantitative-sector assessment.
The needed specialization is (10) in the actual two-orientation trace;
an unweighted operator bound for both resolvents would lose its gain.
The finite-dimensional spectral theorem and trace ideal inequalities
are the standard inputs; no general matrix-decay theorem is reproved
or imported with changed hypotheses. No originality beyond the
sources checked is claimed.

The remaining T_(N^-1,N^(-4/3)) has not been compared with its
canceled frozen trace at the required rate. In particular L090(17)'s
geometric polynomial estimate and its fixed-degree freezing argument
have not been made uniform at these masses. Neither sublinear
propagation nor a signed coefficient-freezing bound follows from (3).
The separate critical audit below accepts the projection specialization.
L225 and the older analytic inputs are imported, not re-audited here.

### 6. Separate critical audit of every projection placement

The 2026-10-18 audit accepts (1)--(3) relative to the imported L088
heat expansion, L089 remainder, L090 coefficient/relative-cochain
identities and L225 mass-removal estimate. In particular this is not
an audit of L225, a stronger rate, or a claim beyond the sources checked.
The following checks concern the specialization in sections 1--4.

**Spectrum and rank.** The transverse vertex space has three strictly
positive indices; its normalized gradient map is injective. Thus there
is one difference eigenvalue delta/(lambda+delta) per vertex mode,
not one per edge component. There are N-1 axial copies and at most
C r^2 transverse labels at max index r. The shell majorant in (5)
is therefore C N sum r^2 min(1,delta^2 N^4/r^4). With
R=N sqrt(delta)>=1, its low part is <=C N R^3 and its high part
is <=C delta^2 N^5/R. For R<1 the entire sum is
<=C delta^2 N^5<=C N^4 delta^(3/2). This verifies (5) in both
regimes, including empty shell ranges. Edge component modes with zero
own-direction index remain in the ambient covariance spectrum; they
are not extra vertex-gradient modes and have not been removed.

**Row-product extension and collar.** Formula (6) is a columnwise
estimate, so it needs no spectral or co-closed condition on J.
In B^T M Cc J the bounded path norm and ||M||<=Ca p(k) leave
||Cc J||_HS<=||nabla J||_HS. In Cc^T M B J each interior
incidence difference is expanded as in L090(7). Its two contributions
are respectively bounded by Ca p(k) times a shifted component
difference of J, and Ca^2 p(k) times a shifted value of J.
Every path has a fixed number of shifts; each input row occurs a
bounded number of times. Existing neighboring rows give the natural
Dirichlet or Neumann interval energy of that component. Every exception
to this comparison lies in a fixed-width physical collar and is bounded
by its actual row value, with coefficient Ca p(k). Squaring and summing
these bounded-multiplicity estimates proves (6) for arbitrary J, with
every column retained. It imposes no zero boundary value on a normal
edge and uses no estimate across an upper zero-extension jump.

For J=R_epsilon or R_epsilon D_delta, simultaneous diagonalization
of the commuting symmetric factors gives J J^T<=R_0^2. The imported
component eigenfunctions have squared value <=16/N^4 at every row,
including normal end rows. The full four-dimensional trace bound
Tr R_0^2<=C N^4 log(eN) consequently gives
(R_0^2)_(ee)<=C log(eN). A collar has O(N^3) rows, so its squared
norm contribution is <=C N^3 log(eN), as used in (7).
This is a positive-operator diagonal comparison, never an entrywise
comparison of kernels. The unrestricted energy is
Tr(Delta_E R_epsilon^2)<=Tr R_0<=C N^4. On the difference,
the scalar maximum x/(x+epsilon)^2<=1/(4epsilon), together with
(5), gives squared energy <=C N^4 delta^(3/2)/epsilon.
Insertion into (6) yields both parts of (8). In particular the collar
costs sqrt(N log(eN)) after the outer factor a, without a hidden
delta-dependent improvement. The a^2||J|| term costs only
C sqrt(log(eN)) and is absorbed. This verifies the claimed uniformity.

**Two placements inside H.** Curl of a relative gradient is zero on
the actual finite cochains, including normal end rows. Since D_delta
has gradient range, the two right-circulation terms in L089(1) vanish
in H_k D_delta. Its two left-circulation terms survive exactly as
(10). The quadratic-form inequality Cc^T Cc<=Delta_E proves
||R_epsilon Cc^T||<=1/(2 sqrt(epsilon)); bounded path norms,
the coefficient factor a and (5) give (11). This does not assume
H_k D_delta=0. In the exact difference (9),

    ||D_delta H_k Q R_epsilon||_HS
       =||R_epsilon Q H_k^T D_delta||_HS
       <=||R_epsilon H_k D_delta||_HS,

where only the commuting Q and R_epsilon are exchanged. The other
term satisfies

    ||Q_delta H_k D_delta R_epsilon||_HS
       <=||H_k R_epsilon D_delta||_HS.

Thus (11) controls the first placement and (8) controls the second.
Their sum proves (12); neither variable multiplier crosses a projection.

**Count and order in the trace.** Each original orientation contains
six occurrences of Q: two in each H^h and one in each K. Replacing
the two H factors and two K factors gives four grouped differences
per orientation. Each H difference is itself the two-term identity
(9). Hence the eight grouped telescoping terms in section 4 cover
all twelve projection replacements across the two orientations.
All unchanged factors at a telescoping endpoint obey the same bounds:

    H_k^s K_t=Q_s H_k R_epsilon Q_s Q_t,
    H_k^s (K_(epsilon,delta)-K_epsilon)
                 =Q_s H_k R_epsilon D_delta Q_s.

Only commuting spectral factors have moved. Their right and left
contractions give the O(p(k)N) and O(p(k)E_N) bounds in (13).
Symmetry of each K and skew-symmetry of each H, including its
difference, give the corresponding left-product bounds by transposition.

For the first orientation write its cyclic order as
Tr(K' A G0 K B^T). The four changes place the difference in exactly
one of K'A and K B^T: respectively K' Delta A, Delta K' A,
K Delta B^T or Delta K B^T. For the second orientation use
Tr((A K) G0^T (B^T K')); its four differences likewise change exactly
one of the two parenthesized Hilbert--Schmidt factors. In every case
the changed factor is <=C p E_N, the other <=C p N, and the
remaining generator has norm <=C N. Thus each grouped term is
<=C p(k)p(l)N^2 E_N in its original order. This verifies that
no inverse is bounded separately by epsilon^-1 and no generator
orientation is identified with the other or discarded.

Finally sum the absolute bounds with the complete imported polynomial
heat envelope and the original factor 1/2. This gives (1). L225
and L089 then give (2) with both residual subtractions retained.
At epsilon=N^-1, delta=N^(-4/3),
delta^(3/4)epsilon^(-1/2)=N^(-1/2), so both power terms in
(2) are N^(5/2); its collar is N^(5/2)sqrt(log(eN)). This proves
(3) using uniform finite inequalities only. No varying-mass use of a
fixed-parameter limit occurs. The audit finds no mathematical defect
in this comparison relative to the stated inputs. The full sector's
downstream bulk and boundary arguments and the independent interacting
construction requirements are not established by this audit.

## Mathlib

Full matching result: **not checked**. Supporting relative cochain,
finite spectral, Hilbert--Schmidt trace, and power-sum coverage:
**not checked**. Unknown availability is not evidence of absence.
