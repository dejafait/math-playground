# L161 — E,E: ordered gauge reduction and two same-vertex bounds

## Hypotheses

Keep L155–L157's SU(2) relative cube (-4,4)^4, a=8/N through
sufficiently fine admitted even meshes, straight direction-1
lower-rooted forest, both actual L010 probes at tau=1/16, and the
bare expansion at fixed mesh before refinement. Retain the complete
compact displacement, both residual insertion subtractions, every
action plaquette, all pinned normal end links, the upper axial jump,
the constant axial edge mode and the entire exterior heat spectrum.
The full cubic tensors are formed before forest restriction.

Use their ordinary stored-coordinate matrices D=D_0, L, Sigma,
Phi, R, A and E, and L156(8)'s h_k=R v_k and c_(i;kl). Define

    F=Phi Sigma,       E=Sigma-D F-F^T D^T.                    (1)

F is a vertex-by-link cross-covariance matrix. It is not K=Phi Sigma
Phi^T and is not an independent noise covariance. E remains signed.
Put hats on operators for their three-color diagonal extensions.
All vertex potentials vanish on every physical face. For a colored
exterior column h set B_h phi=[h,phi_tail+phi_head], as in L157,
and Q_A(h)=Ahat B_h-B_(Ahat h), Q_L(h)=Lhat B_h-B_(Lhat h).

For h=h_k t_c and ell=h_l t_c define the symmetric full-link matrices

    M_(beta gamma)=T_R(h,e_beta,e_gamma),
    N_(epsilon zeta)=T_S(ell,e_epsilon,e_zeta).             (2)

Here e_beta are combined link/color coordinate vectors, and T_R,T_S
are the complete degree-three Taylor tensors of the residual and
action, respectively, exactly as in L156. Their quadratic matrices
are A and L/2. In particular M depends on k,c and N on l,c.

## Conclusion

The entire E,E sector of the approved cubic residual/action response
has the exact finite identity

    H_i^EE=sum_(k,l,c) c_(i;kl) [
       -36 Tr(M Sigmahat N Sigmahat)
       -12 Tr(Q_A(h) Fhat N Sigmahat)
        -6 Tr(Q_L(ell) Fhat M Sigmahat)
        -   Tr(Q_A(h) Fhat Q_L(ell) Fhat)
        -6 Tr(Dhat^T B_(Ahat h) Fhat N Fhat^T)
        -3 Tr(Dhat^T B_(Lhat ell) Fhat M Fhat^T)].          (3)

No variable multiplier, covariance or projection has been commuted
in these traces. Define J_(i,R2) and J_(i,S2) to be the sums of the
fifth and sixth displayed terms, with their coefficients -6 and -3.
These are precisely the terms with both prefix gradient ends at the
residual vertex or both at the action vertex. Then

    |J_(i,R2)|<=C_i N,       a^3 J_(i,R2)->0,
    |J_(i,S2)|<=C_i N^3,                           i=3,6. (4)

The full squared prefix cross-covariance satisfies

    0<=F F^T<=M_ax tensor G^2,
    ||F||_HS^2<=C N^6,                                    (5)

where (M_ax)_st=min(s,t), 1<=s,t<=N-1, and G is the inverse
three-dimensional scalar Dirichlet Laplacian on transverse vertices.
The domination in (5) concerns F F^T, not E.

Thus one identified complete group in E,E is subcubic, and another
is cubic-bounded. The first four traces in (3) still have no bound or
scaled limit established here. The sixth trace, and L158–L159's two
mixed branches, have no established cubic-scaled limits or coefficients.
Consequently there is no cubic bound, vanishing result or compensation
coefficient for the complete response. Other jets, finer powers and
logarithm, finite matching, interacting reflected error <=c_box/2,
continuum axioms and infrared finite mass remain unresolved.
This is standard-method local progress, with no claim of discovery
beyond the sources checked in the unchanged assessment.

## Proof

### 1. Contract the full signed tensors before removing gradients

L155's connected contraction, in L156's combined-color convention,
has outside factor -36. Insert the full heat expansion of the exterior
U_i line. For symmetric M,N,E its remaining index contraction is

    sum_(beta,gamma,epsilon,zeta)
       M_(beta gamma) N_(epsilon zeta)
       Ehat_(beta epsilon) Ehat_(gamma zeta)
       =Tr(M Ehat N Ehat).                                (6)

This uses the actual full tensors. Forest entries vanish only in the
complete covariance, and cannot be removed in the separate E sector.
The expression is an algebraic trace of signed matrices, with no
Gaussian law assigned to E.

L157(7)'s polarized gauge identity, with its distinct quadratic
normalizations at the two vertices, gives

    M Dhat=-Q_A(h)/6,        N Dhat=-Q_L(ell)/12.          (7)

These are matrix equalities for arbitrary link and vertex inputs.
Both residual subtractions are included in T_R and A. Since
D^T A=D^T L=0, multiplying (7) on the left by Dhat^T gives

    Dhat^T M Dhat= Dhat^T B_(Ahat h)/6,
    Dhat^T N Dhat= Dhat^T B_(Lhat ell)/12.                (8)

In particular the right sides are symmetric. Their endpoint sums
include pinned end edges; (7) is the gauge identity on the full pinned
domain and makes no smooth extension of the upper jump.

Recombine L160's exact signed blocks into (1), and write V=Dhat Fhat
just for this expansion. The nine terms of Tr(M Ehat N Ehat) pair
by transpose and cyclicity as follows:

    Tr(M Sigmahat N Sigmahat)
    -2 Tr(M V N Sigmahat)-2 Tr(M V^T N Sigmahat)
    +2 Tr(M V N V)
    +Tr(M V N V^T)+Tr(M V^T N V).                         (9)

For example Tr(M V N Sigmahat)=Tr(M Sigmahat N V^T),
and Tr(M V N V)=Tr(M V^T N V^T), by transposition and cyclicity
with symmetric M,N,Sigma. No equality between the two distinct
single-gradient placements is assumed. Equations (7)–(8) give

    Tr(M V N Sigmahat)=-Tr(Q_A(h) Fhat N Sigmahat)/6,
    Tr(M V^T N Sigmahat)=-Tr(Q_L(ell) Fhat M Sigmahat)/12,
    Tr(M V N V)=Tr(Q_A(h) Fhat Q_L(ell) Fhat)/72,
    Tr(M V N V^T)=Tr(Dhat^T B_(Ahat h) Fhat N Fhat^T)/6,
    Tr(M V^T N V)=Tr(Dhat^T B_(Lhat ell) Fhat M Fhat^T)/12.

The second identity uses transpose once to keep F, rather than F^T,
in the displayed order. Multiply (9) by -36 and sum the exterior
columns and colors. This proves (3), including all signs and factors.
There is no extra two-action factor 1/2 or additional color factor.

### 2. The squared prefix matrix, with the full spectrum retained

L026's relative product spectrum makes the component-1 block of
Sigma, on a normalized transverse scalar Dirichlet mode of eigenvalue
lambda>0, equal to (L_E+lambda I)^(-1). Phi uses only this component.
Let H be the (N-1)-by-N matrix H_(s,r)=1 for r<s, zero otherwise,
with s=1,...,N-1 and r=0,...,N-1. The axial edge difference B has
(B z)_s=z_s-z_(s-1), L_E=B^T B, and L_D=B B^T. L156(6)'s
finite prefix identity, retaining both ends and the constant edge mode,
is exactly

    H(L_E+lambda I)^(-1)H^T=(M_ax-R_D(lambda))/lambda,
    R_D(lambda)=(L_D+lambda I)^(-1).                       (10)

Differentiate this finite-matrix identity with respect to lambda.
Every inverse is smooth for lambda>0; differentiating an inverse gives
-R_D^2 and -(L_E+lambda I)^(-2). Therefore

    H(L_E+lambda I)^(-2)H^T
       =M_ax/lambda^2-R_D(lambda)/lambda^2
                             -R_D(lambda)^2/lambda.      (11)

Its left side is positive. The two subtracted matrices on the right
are positive, since R_D is symmetric positive. Thus it is bounded
above by M_ax/lambda^2 in the positive matrix order. The transverse
eigenmodes are orthogonal and complete, and Sigma does not mix link
components. Assemble their blocks to obtain the first assertion in
(5). This is not an approximation of the prefix or a boundary truncation.

The trace of M_ax is N(N-1)/2. L156's full transverse spectrum bound
lambda_q>=4|q|^2/N^2 for q in {1,...,N-1}^3 gives

    Tr G^2<= (N^4/16) sum_q |q|^(-4)<=C N^4.

Indeed each shell max q_j=m has at most 3m^2 indices and |q|>=m,
so the full sum is bounded by 3 sum_(m>=1)m^(-2). Taking traces
in (5) proves ||F||_HS^2<=C N^6. The colored matrix satisfies
||Fhat||_HS^2=3||F||_HS^2. Low transverse modes and the constant
axial edge mode are present in (10)–(11), including the actual pinned
upper prefix. No uniform Hodge-energy norm estimate for E is used.

### 3. Norms of the exterior-contracted cubic matrices

For a fixed polynomial p of the heat mode labels,

    ||M||<=C p(k),                 ||N||<=C p(l).         (12)

Here is the local coefficient argument for the full residual matrix.
L149(4)–(6)'s ordered words have uniformly bounded length and fixed
degree. The force coefficients have bounded entries, and the generator
coefficients have their single factor 1/(2a) with bounded sampled u_a.
L155(2)'s complete residual cubic consequently has coefficients bounded
by C/a for its force/vector part and C for both insertion parts,
since the sampled tilde b and strain coefficients are bounded. All
these tensors have support in a fixed compact interior enlargement
of the displacement/strain support and a uniformly bounded stencil
radius. Each fixed tensor entry receives a bounded number of local
placements; the bound is independent of N.

On this enlargement L150's interior exterior-column estimate gives
||h_k||_infinity<=C a p(k). Contracting one leg of the cubic with
h_k therefore bounds every entry of M by C p(k). Each row and column
has uniformly bounded degree, including the bounded color dimension.
The row/column-sum operator norm inequality proves the first part of
(12). This keeps the full residual force/clover and both subtractions;
the upper jump is outside their compact support.

For N the ordered action cubic of L155(8) has fixed coefficients on
each plaquette and uniformly bounded local degree, including physical
faces. L157(15) gives the global actual-column bound
||h_l||_infinity<=C p(l). Thus the same row/column argument proves
the second part of (12). No O(a) global bound for this column is used;
its upper jump remains in N.

For arbitrary colored w, the bounded-degree endpoint map implies
||Dhat^T B_w||<=C||w||_infinity. L156(9)–(10) first use exact gauge
annihilation A h_k=A v_k and L h_l=L v_l, then prove

    ||Dhat^T B_(Ahat h)||<=C a^5 p(k),
    ||Dhat^T B_(Lhat ell)||<=C a^3 p(l).                 (13)

The residual smooth-column estimate includes the adjoint coefficient
derivatives and both subtractions. The action estimate retains all
normal end rows. Neither differentiates the pinned forest jump as
though it were a smooth field.

### 4. Bound the two complete same-vertex groups

For compatible real matrices X,Y,F,

    |Tr(X F Y F^T)|<=||X|| ||Y|| ||F||_HS^2.             (14)

This follows from the trace Cauchy–Schwarz inequality applied to
X F and F Y (with a transpose as needed): their HS norms are at most
||X|| ||F||_HS and ||Y|| ||F||_HS. Positivity or symmetry of X,Y
is not required. Equations (5),(12)–(14) bound the fifth term of (3)
by C a^5 p(k)p(l) N^6= C p(k)p(l) N, and the sixth by
C a^3 p(k)p(l) N^6=C p(k)p(l) N^3, absorbing the fixed length 8.

L156(8) gives uniform summability of
sum_(k,l)|c_(i;kl)|p(k)p(l) for either actual probe. Summing every
exterior mode and the three exterior colors proves (4).
Only J_(i,R2) is thereby removed at cubic scale. The second bound
does not identify a scaled limit, and no estimate is assigned to
the four other traces in (3).

### 5. Exact checks and their qualifications

Run `PYTHONDONTWRITEBYTECODE=1 python3 scripts/combined-ward-response/check_cubic_ee_gauge_reduction.py`.
The full certificate is
`scripts/combined-ward-response/cubic-ee-gauge-reduction-certificate.json`.
All 99 rational identities have error zero. Eighteen complete
contractions on a four-edge pinned cycle compare an independent
four-index contraction of both original E lines against all six
ordered trace terms. They use positive and negative residual scalings,
three exterior colors, different column profiles and actual graph
prefix retractions. The direct action Taylor tensor is
-omega epsilon/12; the test residual is a scalar multiple of that
action, not either actual residual/probe pair. The single- and
double-gradient matrix equalities are checked separately in each case.

Nine squared-prefix cases (N=4,6,8 and three positive rational lambda
values each) check (11) exactly; complete rational LDL pivots also
verify the positive differences and trace inequalities in those cases.
Rational lambda values test the algebra, not actual sine eigenvalues.
The bounds for all meshes and both actual probes are the analytical
arguments in sections 2–4. Finite checks alone give no cutoff response
or actual-probe sign. Full tensors, signed correlations, physical
faces, the upper jump and the heat/low-frequency tails remain in (3).

## Mathlib

Full matching theorem: **not checked**. Supporting finite gauge Taylor
identities, matrix inverse derivatives, Schatten inequalities and
relative tensor spectra: **not checked**. Unknown is not absence.
Reuse the unchanged
[target assessment](../drafts/literature/2026-10-12-cubic-residual-action-cubic-scale.md).
No new external theorem is imported or reproved. These finite
specializations are needed to retain the actual trace order and
endpoint terms after the failed global energy shortcut, rather than
inferring a response estimate from that shortcut's norm obstruction.
