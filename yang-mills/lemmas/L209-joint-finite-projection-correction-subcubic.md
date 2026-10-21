# L209 — The jointly contracted finite-projection correction is subcubic

## Hypotheses

Use L185–L187, L196, L202 and L205's fixed-mesh SU(2) setting:
relative box (-4,4)^4, admitted even N, a=8/N, straight lower-rooted
direction-1 forest, complete compact displacement and both actual
L010 probes i=3,6 at tau=1/16. All coordinates and transposes are
ordinary stored-link coordinates. Vertex values are pinned on every
physical face; all variable normal end edges remain. Keep the full
heat sums, constant own-direction modes and both residual subtractions.

Write Delta for the dimensionless relative one-form Hodge Laplacian,
G_0=(D^T D)^(-1), P=I-DG_0D^T, S=P Delta^(-1), A=PAP=A^T,
E_A=S^(1/2)AS^(1/2), V=q Phi, H=I-D Phi/2, R=I-D Phi.
Here q is the endpoint sum and Phi is the actual pinned lower prefix.
Let Z and X=2ZAZ be L205's polynomial approximation at its prescribed
mass and degree. Put F_pol=Delta Z. Thus ||F_pol||<=1+eta, where
eta is uniformly bounded and tends to zero, and

    ZAZ=S^(1/2)F_pol E_A F_pol S^(1/2).               (1)

No coefficient or prefix is commuted through F_pol in this formula.
L205's signed response functional is denoted Q_(i,N)[X].

Use the exact full heat expansion from L185 and L187, but project
its right column using the already established B_i=B_i P:

    SB_i=a^2 sum_(k,l) d_(i;kl) n_k y_l^T,
    n_k=S e_k, y_l=P e_l,
    sum_(k,l)|d_(i;kl)|p(k)p(l)<=C_(i,p)              (2)

for every fixed polynomial p. This changes neither the probe nor its
coefficients d_(i;kl). In particular D^T y_l=0 exactly.

## Conclusion

For n=n_k and y=y_l define the full link maps

    Y_n=diag(Vn)-diag(Rn)V,
    Bcal_y=H^T diag(y)V-V^T diag(y)H=-2 Gamma_y.      (3)

Then the complete four-term contraction of L187 has the exact form

    Q_(i,N)[X]=6a^2 sum_(k,l)d_(i;kl)
                      Tr(A Z Y_(n_k)^T P Bcal_(y_l) Z). (4)

Define Qhat_(i,N) by deleting just the displayed P in (4). Then

    |Q_(i,N)[X]-Qhat_(i,N)|
                       <=C_i N^2 sqrt(log(eN))=o(N^3), (5)
    G_(i,a)=-Qhat_(i,N)+o(N^3),                      (6)

where G is the original joint cubic probe-jet group in L202.
In particular Qhat=O(N^3), by the previously established bound,
but its scaled limit and coefficient remain unproved.

The cancellation behind (5) is the exact pinned identity

    D^T Bcal_y=diag(D^T y)Phi-q^T diag(y)
              =-q^T diag(y)  when D^T y=0.           (7)

It is used on the whole signed contraction, before estimating its
finite Green correction. Formula (5) does not remove a projection
from an individual factor of L187(7), commute it across a multiplier,
or assume smoothness of VP. Both prefixes remain in Y and Bcal.
Their long plateaus, upper jumps, all covariance cross terms, all
physical faces and the heat sums are retained in Qhat.

This is a local specialization of standard finite incidence, spectral
and Hilbert--Schmidt estimates, not a claim of progress beyond the
checked sources. There is no joint limit, coefficient or compensation
claim. The independent f_(i,2),r_0 term, finer asymptotics, finite
matching, interacting reflected error <=c_box/2, continuum axioms
and infrared finite positive mass remain unresolved.

## Proof

### 1. Use co-closed exterior columns without changing either probe

Multiply L185(3)'s expansion for B_i by P on the right, and then by
S on the left. Since B_i P=B_i and P=P^T, this proves (2).
The polynomially summable coefficients are unchanged.

The projected columns have the following bounds, including adjacent
values on each staggered component grid:

    ||y_l||_infinity<=C a^2 p(l),
    max_(adjacent x,x') |y_l(x')-y_l(x)|<=C a^3 p(l). (8)

Here values on missing transverse-face rows are their zero sine
extensions. To justify (8), use L026(6)–(7)'s product basis and
L187, proof section 4's explicit P block: at a fixed multi-index
with all indices positive, P is an orthogonal matrix on at most
four components, I-dd^T/|d|^2. If an own-direction index is zero,
its sole allowed component is already co-closed. Thus P e_l is a
bounded combination of at most four normalized product modes at
that same multi-index. Their amplitudes are O(a^2), and one adjacent
difference gains at most C a(1+|l|). This proves (8) with a fixed
polynomial. It is not a supremum contraction assertion for P on
arbitrary link fields.

### 2. Contract the whole projection before inequalities

L187's pinned product identity gives P U_n=P Y_n. Its exact modal
third-placement formula, with X=2ZAZ, is

    -6 Tr(P Gamma_y X U_n^T)
       =6 Tr(A Z U_n^T P Bcal_y Z)
       =6 Tr(A Z Y_n^T P Bcal_y Z).

This proves (4), including its factor 6. The factor 2 from X and
the factor -1/2 from Gamma_y have both been applied once.

To prove (7), retain Phi D=I on the actual pinned vertex domain
(L196). Therefore H D=D/2 and V D=q, giving

    D^T Bcal_y
       =D^T diag(y)q Phi/2-q^T diag(y)(I-D Phi/2)
       =(D^T diag(y)q+q^T diag(y)D)Phi/2-q^T diag(y).

For a single oriented edge with interior endpoints, its contribution
to D^T diag(y)q+q^T diag(y)D has diagonal entries -2y_e,2y_e
at tail and head and zero off-diagonal entries. If one endpoint is
pinned, restrict this same identity to the interior endpoint; it
still holds. Summing all edges proves

    D^T diag(y)q+q^T diag(y)D=2 diag(D^T y).

This proves (7) on the full domain, including both axial end layers.
The cancellation uses the two orientations of Bcal jointly. A
separate estimate on either H^T diag(y)V or V^T diag(y)H would
retain the prefix on its divergence and lose this identity.

### 3. A smooth endpoint multiplier between the two finite energies

We require the following ordered bound:

    ||G_0^(1/2) q^T diag(y_l) S^(1/2)||_HS
                                      <=C p(l)sqrt(log(eN)). (9)

First prove an energy estimate, for every pinned vertex vector phi:

    ||Delta^(1/2) diag(y_l)q phi||
                                      <=C a^2 p(l)||D phi||. (10)

L003, proof section 2, identifies the component Laplacians with
one own-direction edge interval and three transverse vertex
intervals. On an edge interval the quadratic form is the sum of
squares of adjacent edge differences, with no additional endpoint
penalty. On a vertex interval it includes the differences to the
two pinned endpoint values. These are exactly the forms of DD^T
and D^T D, respectively; their four tensor summands give Delta.

For component mu, q_mu phi is phi at the two endpoints added.
Its norm is at most 2||phi||. In a transverse direction its
differences are sums of two corresponding differences of phi,
including differences to a pinned face. In direction mu, the
difference of consecutive endpoint sums is
phi_(r+2)-phi_r, the sum of two consecutive vertex differences.
Only consecutive edge rows enter that edge-interval energy.
Consequently, by (u+v)^2<=2u^2+2v^2 and bounded overlap,

    ||q phi||<=C||phi||,
    sum_(mu,nu)||delta_nu(q_mu phi)||^2<=C||D phi||^2.

Zero extension on a transverse face is legitimate here because
phi is pinned; this is not a zero extension of its axial prefix.
The elementary product difference for diag(y_l)q phi, followed
by (8), now bounds the left side of (10) by

    C p(l){a^2||D phi||+a^3||phi||}.

The finite vertex Dirichlet spectrum gives ||phi||<=C N||D phi||.
Since aN=8, (10) follows. Every own-direction end row and every
transverse boundary difference has been included in this estimate.

Set phi=G_0^(1/2)v in (10). Since
||D G_0^(1/2)v||=||v||, transpose the resulting operator inequality:

    ||G_0^(1/2)q^T diag(y_l)Delta^(1/2)||_op
                                                     <=C a^2 p(l). (11)

This is an energy bound, not commutation of a multiplier and a
Green operator. The exact factorization in the required order is

    G_0^(1/2)q^T diag(y_l)S^(1/2)
       =[G_0^(1/2)q^T diag(y_l)Delta^(1/2)] P Delta^(-1).

To bound its last factor, L026's dimensionless spectrum has
lambda_k>=4|k|^2/N^2. Each full four-dimensional shell max k_j=r
has at most C r^3 modes across all four components; the allowed
constant own-direction indices are included. There is no full zero
mode. Hence

    ||Delta^(-1)||_HS^2<=C N^4 sum_(r=1)^(N-1)1/r
                                     <=C N^4 log(eN).

The Hilbert--Schmidt ideal inequality and a^2 N^2=64 prove (9).

### 4. Retain the other factor's upper jump and the signed residual

L187(11)–(15) imply the unprojected bound

    ||Y_(n_k) S^(1/2)||_HS<=C p(k) N^3.              (12)

For clarity, its first term is bounded by
||Vn_k||_infinity ||S^(1/2)||_HS<=C p(k)N*N^2.
The part of diag(Rn_k)V off the upper normal layer is bounded by
C p(k)N^(5/2), and its upper part by C p(k)N*N^2.
These are precisely the full-source and layer estimates in L187;
they apply before P is put on the output. In particular (12)
does not declare Rn smooth through its pinned upper jump.

Let

    T_k=G_0^(1/2)D^T Y_(n_k) S^(1/2) F_pol,
    W_l=G_0^(1/2)D^T Bcal_(y_l) S^(1/2) F_pol.

Because G_0^(1/2)D^T is a contraction, (12) gives
||T_k||_HS<=C p(k)N^3. Equation (7) and (9) give
||W_l||_HS<=C p(l)sqrt(log(eN)). The filters are on the right
ends of these factors throughout; their bounded norms suffice.
They have not crossed a prefix, multiplier, D, or finite Green map.

Subtract Qhat from (4), using P-I=-DG_0D^T and (1). For each
mode the difference is exactly

    -6 Tr(E_A T_k^T W_l).

L186(12)'s full residual form estimate is ||E_A||<=C N,
with both subtractions retained. It is a signed operator estimate;
no positivity of A, E_A or X is used. Thus each modal difference
has absolute value at most C p(k)p(l)N^4 sqrt(log(eN)). Multiplying
by the exterior a^2 and summing the entire (2) proves (5).
After multiplication by a^3 its bound is
C_i sqrt(log(eN))/N, which tends to zero.

Finally L205 gives G_(i,a)=-Q_(i,N)[X]+o(N^3), already including
its covariance replacement error O(N^(23/8)). Combining this with
(5) proves (6). The previously known O(N^3) bound transfers to
Qhat; it is not a convergence theorem. No fixed-degree limit is
used at a varying degree, and no plateau or transition is discarded.

All verification in this step is analytic: the pinned edge identity,
the relative component energy product bound, the full spectral sum,
the exact filter placement and the final N powers. No numerical
fixture or mathematical script is used as evidence for this estimate.

## Mathlib

Full matching actual-probe finite-projection comparison and joint
cubic limit: **not checked**. Supporting finite spectral calculus,
incidence product identities and Hilbert--Schmidt ideal inequalities:
**not checked**; unknown coverage is not evidence of absence.
The finite-dimensional spectral theorem and matrix Cauchy--Schwarz
are used in their standard forms. The product and energy arguments
are written out because their boundary domains, smooth exterior
column and original order are essential to this specialization.
No general flow or renormalization theorem is reproved. Reuse the
unchanged [approved assessment](../drafts/literature/2026-10-14-joint-cubic-probe-jet-scale.md)
within its original joint-group target. This result supplies a local
input, with no originality or full-response assertion.
