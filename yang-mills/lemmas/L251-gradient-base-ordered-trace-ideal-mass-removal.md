# L251 — Stronger inverse removal in the ordered gradient-base trace

## Hypotheses

Use L250's exact SU(2) relative cube, lower-rooted direction-1 forest,
sufficiently large admitted even N, a=8/N, tau=1/16, stored coordinates,
bare-first order and actual probes i=3,6. Retain every transverse source
and normal end edge, axial level, allowed constant component index and
complete exterior heat sum. There is no outside factor 3.

Let S_(i,N) be precisely L250(2), including its smooth cumulative h,
finite raw path rows, endpoint filters and continuum heat matrix.
Define S_(i,N,epsilon) by replacing its two occurrences of
G=(T^T T)^(-1) by G_epsilon=(T^T T+epsilon I)^(-1), changing no
other factor. Assume 0<epsilon<=1 and N sqrt(epsilon)>=1.
Use the full finite scalar vertex spectrum and the filtered W energy
bound from L103 and L250. All imported qualifications remain in force.

## Conclusion

There is C_i independent of N and epsilon such that

    |S_(i,N)-S_(i,N,epsilon)|<=C_i N^3 epsilon^(3/4).    (1)

Consequently, at epsilon=N^(-2/3),

    |R_gx(i,N)-S_(i,N,N^(-2/3))|<=C_i N^(5/2).         (2)

Thus inverse removal for this particular ordered smooth trace fits
the requested component budget at a mass with inverse square-root
length N^(1/3). Neither that length nor (2) establishes a boundary
or coefficient-freezing estimate. The remaining comparison is

    |S_(i,N,N^(-2/3))-a^(-3)K_(i,G)|
                                <=C_i N^(5/2)log(eN)^2,             (3)

against exactly L104(6). It is not proved here. No improved complete
remainder exponent, quantitative L011 assembly, interacting comparison
or Yang--Mills construction follows. This new partial specialization
has passed the separate critical audit in proof section 5, relative
to the stated imported inputs.

## Proof

### 1. Positive inverse errors on the complete scalar space

Write Delta=T^T T and H=G-G_epsilon. H is positive, with multiplier
epsilon/[lambda(lambda+epsilon)]. The scalar space has Dirichlet
vertices; this does not assign scalar boundary conditions to relative
edge components. Its exact eigenvalues are

    lambda_m=4 sum_(j=1)^3 sin^2(pi m_j/(2N)),
    m in {1,...,N-1}^3.

Thus lambda_m>=c|m|^2/N^2. Shells max_j m_j=r contain at most C r^2
labels, and Tr G<=C N^3. Put M=N sqrt(epsilon), so 1<=M<=N.
Splitting the full shells at M gives

    Tr H <= C N^3 sqrt(epsilon),
    Tr(Delta H) <= C N^3 epsilon,
    ||Delta H||_HS <= C N^(3/2) epsilon^(3/4).          (4)

For the first bound, low shells use H<=G and cost at most
C N^2 M. High shells use H<=epsilon G^2 and cost at most
C epsilon N^4 sum_(r>M) r^(-2)<=C epsilon N^4/M.
Each is at most C N^3 sqrt(epsilon). For the second bound,
Delta H=epsilon(Delta+epsilon)^(-1)<=epsilon G, so the stated
trace bound follows directly. For the square of the third bound,
the multiplier is epsilon^2/(lambda+epsilon)^2. Low shells
cost C M^3 and high shells cost
C epsilon^2 N^4 sum_(r>M) r^(-2)<=C epsilon^2 N^4/M.
Both equal the claimed scale C N^3 epsilon^(3/2).
Empty high ranges contribute zero, and integer endpoints change
only fixed constants. These estimates include the lowest scalar
eigenvalues and every source row; no spectral cutoff is made.

### 2. Trace norm for the two singly differentiated placements

Temporarily fix k,l,t and write d=M_(h^N_(k,t)),
W=W^u_t and Z=D^T zeta^v_(l,t). The spaces are as in L250:
T,E,W map finite pinned vertices to relative transverse edges,
and D,zeta map edges to plaquettes. Put U=||u_1||_infinity.
L250(8) gives ||W G^(1/2)||<=C U, hence the quadratic-form bound

    W^T W<=C U^2 Delta.                               (5)

This follows by conjugating the bounded positive matrix
G^(1/2) W^T W G^(1/2) by Delta^(1/2); it does not commute W
with any inverse. Also ||E||<=C.

For finite rectangular matrices the trace-ideal inequality
||AB||_1<=||A||_HS||B||_HS applies. Factoring through the positive
square root of H and using (5), we obtain

    ||E H W^T||_1
      <=||E H^(1/2)||_HS ||H^(1/2) W^T||_HS
      <=C U [Tr H Tr(Delta H)]^(1/2)
      <=C U N^3 epsilon^(3/4),

    ||T H E^T||_1
      <=||T H^(1/2)||_HS ||H^(1/2) E^T||_HS
      <=C [Tr(Delta H) Tr H]^(1/2)
      <=C N^3 epsilon^(3/4).                          (6)

For clarity, the first use of (5) is
Tr(H^(1/2) W^T W H^(1/2))<=C U^2 Tr(Delta H).
It uses positivity of H only, not entrywise positivity of a kernel
or positivity of the signed response. The other trace identity is
||T H^(1/2)||_HS^2=Tr(Delta H).

These are the placements for which L103(19)--(20) used only
Hilbert--Schmidt error bounds with epsilon^(1/4). The trace norm
permits all remaining factors in these two words to stay in operator
norm. No separate absolute kernel moment is invoked.

### 3. All four telescoping terms in their original order

For J=G or G_epsilon, finite cyclicity gives the exact edge trace

    F(J)=Tr[(T J T^T)d(E J W^T)Z]
                           -Tr[(T J E^T)d(T J W^T)Z].              (7)

This is L250's ordered trace with the same J in both positions.
Put A_J=T J T^T, B_J=E J W^T, C_J=T J E^T and D_J=T J W^T.
For both choices of J, (5) and Tr G<=C N^3 imply

    ||A_J||<=1,              ||D_J||<=C U,
    ||B_J||_HS<=C U N^(3/2), ||C_J||_HS<=C N^(3/2).   (8)

For example J=G^(1/2)(Delta J)G^(1/2), with ||Delta J||<=1,
and ||T G^(1/2)||=1. Factor B_J with E G^(1/2) in
Hilbert--Schmidt norm and the remaining factors in operator norm.
The analogous factorization of C_J uses G^(1/2)E^T.
Every norm is on the full finite space.

With subscripts H denoting the same formulas with J replaced by H,
the two doubly differentiated errors satisfy

    ||A_H||_HS<=C N^(3/2)epsilon^(3/4),
    ||D_H||_HS<=C U N^(3/2)epsilon^(3/4).             (9)

Indeed factor them using T G^(1/2), Delta H and either
G^(1/2)T^T or G^(1/2)W^T. All exterior factors are bounded,
and (4) supplies the middle Hilbert--Schmidt norm.

The complete difference is precisely

    F(G)-F(G_epsilon)
      = Tr[A_H d B_G Z]+Tr[A_(G_epsilon) d B_H Z]
        -Tr[C_H d D_G Z]-Tr[C_(G_epsilon) d D_H Z].   (10)

For the first term pair A_H and B_G in Hilbert--Schmidt norms.
For the second use the trace norm of B_H in (6), with
A_(G_epsilon), d and Z in operator norm. For the third use the
trace norm of C_H in (6), with d, D_G and Z in operator norm.
For the fourth pair C_(G_epsilon) and D_H in Hilbert--Schmidt
norms. Thus each term is at most

    C N^3 epsilon^(3/4) ||d|| U ||Z||.               (11)

There is no use of ||G|| or ||G^(1/2)|| as an unweighted operator.
No multiplier has crossed G, H, T or a projection. In particular
the noncompact cumulative coefficient d stays in its displayed
position; its bounded supremum is sufficient here.

### 4. Complete heat sum and the finite mass schedule

L250's global coefficient bounds give
||d||<=C p(k) and ||Z||<=C p(l), for a fixed polynomial p,
uniformly in t and N. Its complete continuum heat matrix obeys
|c_(i;kl)|<=C_i exp[-c0(|k|^2+|l|^2)].
Consequently (11) is absolutely summable over both exterior labels,
including continuum labels absent from the finite mesh in this smooth
comparison. All allowed constant component indices remain.

The normalization in L250(2) is unchanged:

    a^3 S_(i,N)=a^4 sum_(k,l)c_(i;kl) sum_t(at)F(G),
    a^4 N^3 sum_(t=1)^(N-1)(at)<=C.

Sum (11) with these exact weights. This proves
|a^3(S_(i,N)-S_(i,N,epsilon))|<=C_i epsilon^(3/4),
and hence (1), since a^(-3)=N^3/512.
L250(3) already gives |R_gx-S_(i,N)|<=C_i N^(5/2),
including L102/L103's removed terms once. At epsilon=N^(-2/3),
N sqrt(epsilon)=N^(2/3)>=1 and
N^3 epsilon^(3/4)=N^(5/2). The triangle inequality proves (2).
The schedule enters only the proved finite inequality, never a
qualitative fixed-mass limit.

The cumulative endpoint, upper primitive, raw paths and heat matrices
are unchanged from L250. Normal end rows and all Green inputs remain
in every trace norm. The result does not reopen the stopped operator,
termwise-commutation or factorwise-absolute-moment shortcuts. Its
downstream use requires a separate quantitative estimate of (3);
the coarse absolute-walk loss of L249 does not establish it.

This is RESEARCH / REPRODUCTION under the unchanged EXPLORE assessment
`drafts/literature/2026-10-20-gradient-base-crossed-quantitative-remainder.md`.
The finite-dimensional spectral theorem and Schatten Holder inequality
are standard named inputs. The shell count and four actual ordered
placements are written out because existing L103/L250 conclusions
do not state this improved inverse error. No general source theorem
is reproved, and no originality beyond the checked sources is claimed.

### 5. Separate critical audit, 2026-10-20

The audit accepts (1)--(2) under the unchanged EXPLORE assessment
`drafts/literature/2026-10-20-gradient-base-complete-remainder-critical-audit.md`.
This is RESEARCH / REPRODUCTION: verification of this local input,
without a new exponent or a claim of progress beyond checked sources.
L250's accepted comparison and its upstream qualifications are imported.

**Spectrum and trace ideals.** The scalar vertices are Dirichlet in all
three transverse coordinates, so their labels are exactly the three
positive indices displayed above. Allowed constant relative-edge modes
are not scalar vertex zero modes and are not removed by this labeling.
For H=G-G_epsilon the three multipliers in (4) are respectively
epsilon/[lambda(lambda+epsilon)], epsilon/(lambda+epsilon), and
epsilon/(lambda+epsilon) in Hilbert--Schmidt norm. The full shell split
at M=N sqrt(epsilon) gives respectively N^3 sqrt(epsilon), N^3 epsilon
and N^(3/2)epsilon^(3/4), with no missing lowest shell. The second
bound uses Tr G, and the third uses the squared multiplier, not its
trace. They hold before choosing the mass.

With V the scalar vertex space and H_e the transverse relative edge
space, T,E,W:V->H_e and Z:H_e->H_e. The energy inequality (5) follows
from ||W G^(1/2)||<=C U by conjugation with Delta^(1/2); it does not
require W to be a gradient. Consequently the two factors of E H W^T
have squared Hilbert--Schmidt norms at most C Tr H and
C U^2 Tr(Delta H). The analogous factors of T H E^T have squared
norms Tr(Delta H) and C Tr H. Schatten Holder therefore gives the
two trace norms (6), with every row of both spaces retained. H is
positive only in these factor estimates; the response is signed.

**All four placements.** Cycling the literal vertex trace gives (7)
as endomorphisms of H_e. Its first product difference is
A_H d B_G+A_epsilon d B_H, and its second is
C_H d D_G+C_epsilon d D_H, with the latter subtracted. Thus (10)
has exactly the four necessary placements and their original order.
For the first and fourth use Hilbert--Schmidt pairs (A_H,B_G) and
(C_epsilon,D_H). The energy factorizations in (9) cost
N^(3/2)epsilon^(3/4), and their partners cost N^(3/2).
For the second and third use the trace norms (B_H,C_H); all their
remaining factors are bounded in operator norm by (8). These give
N^3 epsilon^(3/4) in every case. Neither d nor Z crosses an inverse.
The noncompact d needs only its supremum at this stage.

The same fixed polynomial mode envelope controls d and Z, and the
continuum Gaussian heat majorant sums it over both full labels.
In particular

    a^4 N^3 sum_(t=1)^(N-1)(at)=(8^5/2)(1-1/N).

Thus normalization contributes no additional N power. Multiplying
back by a^-3 and choosing epsilon=N^(-2/3) gives N^(5/2).
Adding L250's original-pair comparison once proves (2). The audit
does not infer localization from this estimate, audit L250's ancestry,
or establish a complete L011 or interacting remainder.

## Mathlib

Full matching ordered gradient-base inverse-removal theorem: **not
checked**. Supporting finite spectral calculus, Schatten Holder
inequality, positive trace monotonicity and finite shell bounds:
**not checked**. Unknown coverage is not evidence of absence.
No numerical premise or mathematical script is used.
