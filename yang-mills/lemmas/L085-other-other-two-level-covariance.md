# L085 — Exact two-interior-level reduction of the other/other cubic response

## Hypotheses

Keep L048's SU(2) finite Gaussian, actual L010 probes i=3,6 and
L018's residual, straight lower-rooted direction-1 forest, all-face
pinned box, a=8/N and tau=1/16. Take the bare small-coupling coefficient
at each fixed admitted even mesh before refinement. All coordinates,
transposes and norms below are ordinary dimensionless stored ones.
Retain all colors, transverse end edges, plaquettes, axial levels and
exterior heat modes. Write S=Sigma_F, B=B_(i,F), A=A_F, f=f_(i,0),
r=r0. Exactly as in L058, C=S3_top and Y=S3-C. The contribution here is

    O_i(a)=(1/2) kappa(f,r,Y,Y).                         (1)

It contains all ordered pairs of transverse plaquettes at levels
1<=s,t<N, including coincident pairs. No observable is replaced by
its conditional expectation. Use L050's full transverse relative
cochains T,D, Delta_0=T^T T, Delta_T=TT^T+D^T D and P=T Delta_0^-1 T^T.
Thus T phi on an edge v->w is phi(v)-phi(w), DT=0, and pinned vertex
values are zero. Let

    R_st(lambda)=[(L_D+lambda I)^-1]_(s,t),
    (L_D)_(s,t)=2 delta_(s,t)-delta_(s,t+1)-delta_(s,t-1),

with s,t=1,...,N-1. Every spectral function uses the complete spectrum.

## Conclusion

The actual one-color transverse forest links satisfy the exact identity

    K_st=Cov(x_T(s),x_T(t))
        =min(s,t) P+R_st(Delta_T)(I-P).                 (2)

In particular this is a two-interior-level covariance, not an upper-face
source row. Let the full curvature covariance array be

    Hcal=[D K_st D^T]_(s,t=1,...,N-1).

Its nonzero eigenvalues are exactly

    lambda/(lambda+mu_k),   mu_k=4 sin^2(k pi/(2N)),     (3)

where lambda runs with multiplicity over Delta_T on ker P and
1<=k<N. For even N>=2,

    (9/100) N^3(N-1) <= ||Hcal||_HS^2
                          <= (N-1)^3(2N+1) < 3N^4.   (4)

Hence ||Hcal||_HS=Theta(N^2); an O(N^(3/2)) estimate for this complete
array is false. This tests the geometry needed for a possible reuse of
the mixed upper-source estimates. It is not a lower bound for (1).

There is also a complete signed representation with the covariance (2)
already exposed. For a transverse plaquette p write its signed traversal
entries y1,...,y4, and import L062's three rows

    c_p=y1+y2+y3+y4, b_p=y1+y2, q_p=y2+y3.

Let Lambda_p select these rows from the transverse links at its level,
and J_alpha=Lambda_p X_s select them from forest coordinates, where
alpha=(s,p). For beta=(t,q), set

    C_ab=J_alpha S J_beta^T,
    U_ab=J_alpha S B S J_beta^T,
    V_ab=J_alpha S A S J_beta^T,
    Z_ab=J_alpha (S B S A S+S A S B S) J_beta^T.

These are three-by-three blocks. Row replacement notation is that of
L061, with all nonreplaced rows kept. Then

    O_i=3 sum_(alpha,beta) {
             sum_j det C_ab[j:Z_ab]
           + sum_(j!=k) det C_ab[j:U_ab,k:V_ab] }.       (5)

Both connected classes, both residual path orders and all nine
placements remain. The outside coefficient is 3, not the mixed group's
6. This is a specialization of L048's established finite contraction,
not a replacement for it.

For each ordered pair put m=min(s,t) and

    G_ab=Lambda_p P Lambda_q^T,
    H_ab=Lambda_p R_st(Delta_T)(I-P) Lambda_q^T,
    C_ab=m G_ab+H_ab.

The first row and first column of G_ab are zero. Holding the actual
U,V,Z blocks fixed, the expression in braces in (5) is exactly

    m^2 (Z_ab)_11 det (G_ab)_[2,3],[2,3]
          + m L_ab+Q_ab,                              (6)

where, suppressing the pair indices,

    Q=sum_j det H[j:Z]+sum_(j!=k) det H[j:U,k:V],
    L=sum_(j!=k) det H[j:Z,k:G]
       +sum_(j!=k) det H[j:U,k:V,l:G],

and l in the last sum is the unique remaining row. Formula (6) separates
the explicit two-gradient base factor without discarding the other
terms. U,V,Z themselves retain their full mesh and level dependence;
(6) is not a power-counting theorem or an asymptotic expansion in N.

No finite a^3 limit, value, sign, stronger signed power or compensation
with L084 is proved. Both actual probes remain in (5). The signed
estimates for all of (6), boundary effects, finer remainders, other
response jets and the interacting construction are unresolved.

## Proof

### 1. Evaluate the two-prefix covariance with both interval endpoints

Import L026(2),(6)–(9)'s exact forest lift and relative tensor spectrum;
no nonlinear vertex is transferred to an unmodified Hodge polynomial.
For the Hodge field z this gives, at every interior level,

    x_T(s)=z_T(s)+T phi_s,
    phi_s=sum_(ell=0)^(s-1) z_1(ell).

The two terms are independent because the full Hodge covariance is
component diagonal. Their covariances are, respectively,
R_st(Delta_T) and T Cov(phi_s,phi_t) T^T. This uses Dirichlet axial
vertex coordinates for z_T and Neumann axial edge coordinates for z_1.

Here is the finite interval computation of the latter, without dropping
the constant axial edge mode. Let B0 be the (N-1)-by-N matrix
(B0 h)_s=h_s-h_(s-1), with edge indices 0,...,N-1. Then
L_E=B0^T B0 is the edge Neumann Laplacian, with endpoint diagonal 1,
and L_D=B0 B0^T. Let h_s have entries 1_(ell<s). It satisfies

    h_s^T h_t=min(s,t),     B0 h_s=-e_s.

For every lambda>0 the exact resolvent identity is

    lambda (L_E+lambda I)^-1
       =I-B0^T (L_D+lambda I)^-1 B0.                  (7)

For example, multiply on the left by L_E+lambda I, use
(L_E+lambda I) B0^T=B0^T(L_D+lambda I), and obtain lambda I.
All these matrices are invertible where an inverse appears. Sandwiching
(7) between h_s^T and h_t yields

    h_s^T (L_E+lambda I)^-1 h_t
          =[min(s,t)-R_st(lambda)]/lambda.            (8)

The endpoint conditions and the constant mode have been retained in
L_E; neither is replaced by an infinite interval approximation.

Apply (8) on every transverse vertex eigenmode. L050's cochain
intertwining Delta_T T=T Delta_0 and projection identities imply

    T Cov(phi_s,phi_t) T^T
           =[min(s,t) I-R_st(Delta_T)] P.

Adding the direct transverse covariance proves (2). The intertwining
holds on the full relative cochain spaces, including edges meeting a
fixed face; no interior-only edge restriction was used.

As normalization checks, the upper zero axial mode gives
Cov(u,u)=N Delta_0^-1 and Cov(x_T(s),u)=s T Delta_0^-1.
Consequently the centered field xi_s=x_T(s)-(s/N)Tu has covariance

    Cov(xi_s,xi_t)=[min(s,t)-st/N]P
                        +R_st(Delta_T)(I-P).          (9)

At s=t=N-1 this is (1-1/N)P+R_(N-1,N-1)(Delta_T)(I-P),
consistent with L050's noise covariance since R_(N-1,N-1)=1-b_N.
This is a base-law check, not independence of xi from f or r, nor a
justification for replacing the observables by conditional means.

### 2. Test the complete curvature array over every axial level

L050's identities give D^T D=Delta_T(I-P). To verify it directly,
Delta_T P=TT^T follows from Delta_T T=T Delta_0, so subtraction from
Delta_T=TT^T+D^T D gives the assertion. In particular D is injective
on ker P, and its singular value on a Delta_T eigenvector there is
sqrt(lambda). Formula (2) removes the gradient block upon applying
D at both ends. Diagonalize L_D with all its N-1 sine modes, and
Delta_T on ker P. The resulting curvature covariance eigenvalues are
precisely (3), with zeros on the orthogonal complement of the curvature
range. Orthogonality of both finite transforms justifies the exact
Hilbert–Schmidt trace formula

    ||Hcal||_HS^2
       =sum_(lambda in ker P) sum_(k=1)^(N-1)
                         [lambda/(lambda+mu_k)]^2.   (10)

There are 3N(N-1)^2 transverse edges and (N-1)^3 vertex gradients.
T is injective because Delta_0 is positive. Thus dim ker P is
(N-1)^2(2N+1), and every summand in (10) is at most 1. This proves
the upper bound in (4).

For the lower bound use the actual tensor-product modes from L026.
For each triple k_2,k_3,k_4 with N/2<=k_j<=N-1, all indices are
positive. The three component edge modes span a three-dimensional
space with common eigenvalue

    lambda=4 sum_(j=2)^4 sin^2(k_j pi/(2N)) >=6.

Within that space the gradient of its vertex sine mode spans one
dimension; its orthogonal two-dimensional complement is in ker P.
Different triples are orthogonal, so this supplies exactly
2(N/2)^3 usable eigenvectors. Every axial eigenvalue mu_k is at most
4, and therefore lambda/(lambda+mu_k)>=3/5. Retaining all N-1 axial
modes on this transverse subspace in (10) gives

    ||Hcal||_HS^2 >= (9/25) 2(N/2)^3 (N-1)
                    =(9/100)N^3(N-1).

This is an actual full-spectrum lower bound, not a frozen-symbol or
finite-mesh diagnostic. It excludes an O(N^(3/2)) bound on this array
but supplies no lower bound after indefinite observable contractions.

### 3. Place the exact covariance in the imported complete contraction

L058 identifies Y with all transverse cubic vertices at 1<=s<N.
Import L062(3)'s polynomial identity and L048(4) to write

    Y=-(1/2) sum_alpha c_alpha dot (b_alpha cross q_alpha).

This remains valid with pinned zero rows. Import the color-isotropic
Isserlis determinant identity and normalized quadratic tilt from
L061, proof section 2. Its applicability here is unchanged: the same
three independent colors, symmetric actual B,A, positive S and finite
Gaussian integrable neighborhood are used. Only the two row selectors
are changed, to the two interior vertices. With
S(alpha0,beta0)=(S^-1-2alpha0 B-2beta0 A)^-1, that identity gives

    (1/2) E_(alpha0,beta0)[Y^2]
        =(3/4) sum_(alpha,beta)
                   det[J_alpha S(alpha0,beta0) J_beta^T].      (11)

The +3/4 is (1/2) times the two cubic factors (+1/4) times the
Isserlis color factor 6. The normalized mixed derivative of (11)
is (1/2) kappa(f,r,Y,Y): the other four-cumulant partitions vanish
by parity, exactly as in L048(7). This is not an unnormalized moment.
The covariance derivatives are 2SBS, 2SAS and
4(SBSAS+SASBS). Therefore differentiation of each determinant gives
all three same-row replacements and all six distinct-row replacements,
each with factor 4. This proves (5), including its outside factor 3.
It is the restriction and row regrouping of the existing L048 identity;
its Wick pairing enumeration need not be repeated.

Only after this differentiation do we insert (2) into the remaining
base block C_ab. The covariance identity (2) has not been asserted
under the tilted law. In particular no derivative of its transverse
projection zeros has been deleted. Both length-three path orders in Z
are kept, and the ordered pair sum includes alpha=beta.

### 4. Separate the explicit two-gradient base factor

The first row of Lambda_p is the plaquette circulation. Since DP=0
and PD^T=0, G_ab has zero first row and first column. Expand each
determinant of (5) using C=mG+H only in its unreplaced rows.

A same-row replacement has two base rows. Its degree-two term in m
vanishes unless the replaced row is row 1, because otherwise a base
row is row 1 of G and is zero. In the remaining term, expansion on
the first column leaves exactly Z_11 det G_[2,3],[2,3], with positive
cofactor sign. The degree-one terms replace a second row k by G and
are precisely the first sum defining L. The degree-zero terms form
the first part of Q. A distinct-row replacement has only one base
row, giving the second part of Q and the second sum in L. There is
no degree-two term in that class. This proves (6) for arbitrary
U,V,Z, hence for both actual probes without assuming their signs.

The decomposition exposes an undamped two-level gradient factor and
the interior curvature resolvent, but it does not control the signed
sums multiplying them. In particular the m^2 expression alone cannot
be assigned a cutoff power because Z_11 still carries the actual heat,
residual, inverse-covariance and level dependence. The terms of L and
Q may compensate it. No term is removed from the required limit.

### 5. Scope of this bounded attempt

The saved EXPLORE assessment is
`drafts/literature/2026-10-10-other-other-cubic-leading-scale.md`.
L048's known finite contraction is imported, not rediscovered. The
necessary additional specialization evaluates the two-interior-level
covariance left open by that contraction and quantifies the change
from an upper-source row to a full axial array. This is local
REPRODUCTION of finite Gaussian and relative spectral methods; it
does not claim a new theorem beyond the sources checked.

Equations (2)–(10) are proved analytically using exact finite matrices
and all their modes; no numerical script or assumed numerical trend
is needed. The normalization in (11) checks the original outside 1/2
and distinguishes the other/other group from the mixed group. The
failed O(N^(3/2)) array estimate is specific new evidence against
transferring that upper-source estimate to this region. It is not
evidence that the a^3-scaled signed limit fails or that it is nonzero.
The finite-limit test against -12 gamma D_i remains unresolved.
L082's saved-table/IEEE qualifications remain attached to the signs
of that comparison value; this lemma uses no numerical D_i value.
Other jets, N^2 remainders, slower powers and logarithms, matching,
interacting error <=c_box/2, continuum axioms, reflection positivity,
infrared control and finite positive mass remain independent gaps.

## Mathlib

Full matching coverage: **not checked**. Supporting finite resolvent,
Gaussian tilt/Isserlis, cochain and spectral coverage: **not checked**.
Unknown availability is not evidence of absence. The named Gaussian
theorems are imported through L048/L061 with their hypotheses checked
above; no general Gaussian theorem or continuum Ward theorem is
reproved or assigned new boundary hypotheses.
