# Lemma 443: exact simultaneous repair of three quadratic occupation tests

## Hypotheses

Use L441's complete repaired Borel family on its eventual real-H ray,
with all L438 selected constraints and tolerances. Write ell=log H,
E_H=H^(-1) integral_[H,2H], L(t)=log(2+t), omega=log 2,
s(t)=sin(omega t), and e(t)=eta(t/H), where
eta(u)=(u-1)^2(2-u)^2 on [1,2]. Keep the high and both intermediate
components, their probabilities, remaining probability w, mean m,
normalized Poisson weight g_H, actual response and curvature, and the
original L429 cutoff unchanged. A later common support onset is allowed;
no cutoff threshold or stage value is changed.

Use L419's exact forms B(X;t)=b(t)^T X, D(X;t)=X^T J(t)X,
positive definite K and Borel six-state realization. The vector b(t)
is distinct from scalar coefficients introduced below. Use L440's
complete x-squared transport polynomial and L442's complete xy and
y-squared polynomials, including their separately audited residuals.
There is no atom-continuity, inter-height consistency, independence,
actual sine-limit or trajectory-realization assumption.

The unchanged prior SPECIALIZE assessment is
`drafts/literature/2026-10-20-exact-quadratic-block-covariance-repair.md`.
The construction below is a REPRODUCTION within that assessed scope.

## Conclusion

There is one jointly Borel family on a full eventual ray of real H,
obtained by a uniformly bounded symmetric bulk covariance change,
for which all three complete quadratic occupation residuals are
**exactly zero at each H**. The change has identically zero 11 entry
and exactly zero w-weighted height mean. Every L441 selected constraint
persists, including exact integrated raw seconds and first B mean,
unchanged conditional x-second density, the first-D tolerance, all
cubic and quartic requirements, support, fixed envelopes and the
same-family capped absolute cubic conclusion for every fixed cap.

The separate step-271 critical audit below validates this local
construction. It is not a new general projection or matrix-realization theorem;
originality is not claimed. Matching these three necessary identities
does not realize an ordinary trajectory, establish the other occupation
identities, evaluate actual clipping, prove capped nondegeneracy or
L413's full-error regulator margin, or supply global mixed positivity,
a new zero-exclusion range or RH. L440 and L442 retain their separations
of their respective unchanged laws.

## Proof

### Exact residual map on an admissible finite coefficient space

Let nu^0 and Sigma^0 denote the complete law and bulk covariance of
L441, and let q^0_ij be its full conditional raw second matrix. Thus,
in L438/L441 notation, with V_ij=e_i e_j^T+e_j e_i^T for i<j,

    Sigma^0=ell g_H K+A_H+(d-bar_d_H)V_12,
    q^0=R+w(Sigma^0+mm^T),
    R=pYY^T+k_+Z_+Z_+^T+k_-Z_-Z_-^T.                 (1)

All of R,m,w,g_H,A_H,d and bar_d_H here are the unchanged inputs,
including every rare-state second and translation term. Set

    A_j(t)=e'(t)s(t)/L(t)+omega e(t)cos(omega t)/L(t)
                                  -j e(t)s(t)L'(t)/L(t)^2,
    T_1=A_1 x^2+2e s xy,
    T_2=A_2 xy+e s(y^2+xz),
    T_3=A_3 y^2+2e s yz.                              (2)

These are precisely L440's and L442's complete polynomials. Their
ordinary C^2 trajectory integrals are zero, with both endpoint terms
zero. The necessary finite-interval identity is imported from
J. B. Lasserre, D. Henrion, C. Prieur and E. Trelat, *Nonlinear optimal
control via occupation measures and LMI-relaxations*, SIAM J. Control
Optim. 47 (2008), 1643--1666, DOI 10.1137/070685051,
[arXiv:math/0703377v1](https://arxiv.org/pdf/math/0703377v1),
Sections 2.1--2.3, (2.7), (2.10)--(2.12), pp. 3--5. The local
specializations in L440/L442 use state (x,y), continuous control z,
x'=Ly, y'=Lz-(L'/L)y, and finite compact boxes for each fixed H.
They need no uniform box as H grows. We use those polynomials, not
a sufficiency theorem for occupation measures. No Borel kernel, atom,
probability, cutoff or H-dependent coefficient is differentiated.

Define the exact old residuals, using (1), by

    r_1=E_H[A_1 q^0_11+2e s q^0_12],
    r_2=E_H[A_2 q^0_12+e s(q^0_22+q^0_13)],
    r_3=E_H[A_3 q^0_22+2e s q^0_23].                  (3)

These are finite-H integrals of the complete law, not replacements
by its limiting coefficients. L441 and audited L442 give, as real
H tends to infinity under the unchanged cutoff,

    r_1=o(1), r_2=o(1),
    r_3=omega/(360 sqrt(2))+o(1).                     (4)

In particular the residual vector is uniformly bounded on one ray.

Put W_H=E_H w, mu_H=E_H(ws)/W_H and h_H(t)=s(t)-mu_H. L441 gives
1/4<=w<=1 and E_H(1-w)=O(ell^(-5/2)), so

    E_H(w h_H)=0 exactly, |mu_H|<=1, |h_H|<=2.         (5)

For three real coefficients a_H,b_H,c_H, held fixed within this H
interval, use the additional covariance field

    F_H(t)=h_H(t)(a_H V_12+b_H V_13+c_H V_23).         (6)

Its 11 entry vanishes at every height, and E_H(w F_H)=0 entrywise.
Replacing the bulk by a centered symmetric law with covariance
Sigma^0+F_H and the same translation m changes the full raw seconds
by exactly w F_H. Hence its changes in the three complete residuals
are, without error,

    (delta r_1,delta r_2,delta r_3)^T
      =M_H(a_H,b_H,c_H)^T,
    M_H=[[2C_H,0,0],[D_H,C_H,0],[0,0,2C_H]],
    C_H=E_H(e s w h_H), D_H=E_H(A_2 w h_H).          (7)

Indeed only q_12 changes in T_1 because q_11 is fixed; T_2 sees
the changed q_12 and q_13, while q_22 is fixed; T_3 sees only q_23.
Thus no factor two from symmetry of a raw matrix has been incorrectly
added to the single monomial xz. Every slow derivative is retained
in D_H. This calculation imposes the exact mean constraints before
solving the residual equations.

### Uniform conditioning and an exact bounded solution

For each fixed nonzero integer k, integration by parts, with e zero
at both endpoints and integral |e'| bounded independently of H, gives

    |E_H[e exp(ik omega t)]|<=C_k/H,
    |E_H s|<=2/(H omega), integral_1^2 eta=1/30.       (8)

Let delta_H=E_H(1-w). Since W_H>=1/4,

    |mu_H|<=4[2/(H omega)+delta_H],
    E_H(e w s)=O(H^(-1)+delta_H),
    E_H(e w s^2)=1/60+O(H^(-1)+delta_H).             (9)

The last line uses s^2=(1-cos(2omega t))/2 and replaces w by 1
at absolute cost at most ||eta||_infinity delta_H. It uses no
pointwise smallness of the removed rare mass. Subtracting the exact
recentring term mu_H E_H(e w s) proves

    C_H=1/60+O(H^(-1)+ell^(-5/2)), C_H>=1/120        (10)

on a full eventual real-H ray. Also L>=ell, |L'|<=1/H and
||e'||_infinity=O(1/H) imply ||A_2||_infinity=O(1/ell), hence

    |D_H|<=2||A_2||_infinity=O(1/ell).              (11)

Consequently det M_H=4 C_H^3 is uniformly bounded below by
4/120^3>0. Both M_H and its inverse are uniformly bounded there.
For a precise standard linear-algebra input, import the full-row-rank
least-norm/right-inverse theorem in Stephen Boyd, *EE263: Introduction
to Linear Dynamical Systems*, Autumn 2007--08, Lecture 8,
[Least-norm solutions of underdetermined equations](https://web.stanford.edu/class/archive/ee/ee263/ee263.1082/lectures/min-norm.pdf),
slides 8-2--8-7 and 8-9: for full-row-rank A the minimum-norm solution
of A u=y is A^T(AA^T)^(-1)y. To meet the source's m<n convention,
use A=[M_H 0] of size 3 by 4; (10) verifies its full row rank.
The fourth coefficient multiplies the zero field and its minimum-norm
value is zero. The remaining three coordinates can be evaluated by
triangular substitution:

    a_H=-r_1/(2C_H),
    b_H=-(r_2+D_H a_H)/C_H,
    c_H=-r_3/(2C_H).                                (12)

This is an explicit evaluation and uniform-conditioning check for the
imported result, not a reproof of the general projection theorem.
Equations (4), (10)--(12) give

    a_H=o(1), b_H=o(1),
    c_H=-omega/(12 sqrt(2))+o(1),
    sup_t ||F_H(t)||<=2(|a_H|+|b_H|+|c_H|)<=C_F.     (13)

Here C_F is a fixed finite constant independent of H and the Poisson
stage. The V_ij each have operator norm one. Definition (12) uses
the exact residuals (3); (4) is used only to prove boundedness and
the displayed limits. Substitution in (7) gives r+M_H(a_H,b_H,c_H)^T=0
exactly at every H in the ray. No small asymptotic error is left to
be absorbed in an equality.

### Jointly Borel supported realization on the same cutoff ray

L441's uniform matrix margins, with fixed positive constants, are

    lambda_min(Sigma^0)>=c_1 ell^(7/8)-C_1 ell^(1/2),
    ||Sigma^0||<=C_2 ell^(9/8),
    tr(J Sigma^0)<=-c_3 ell^(7/8)+C_3 ell^(1/2).      (14)

By (13), Sigma^*=Sigma^0+F_H is positive definite eventually, with
lambda_min(Sigma^*)>=c ell^(7/8) and ||Sigma^*||=O(ell^(9/8)).
The trace perturbation is bounded by
|tr(J F_H)|<=3||J|| C_F=O(1), because J is uniformly bounded.
Thus tr(J Sigma^*)<=-c' ell^(7/8) on one common eventual ray.
These are pointwise estimates at every height, including response
projection zeros, every Borel selection branch and every cutoff stage.

Import the real Schur--Horn theorem in Eric A. Carlen and Elliott H.
Lieb, *Short proofs of theorems of Horn and Mirsky on diagonals and
eigenvalues of matrices*, [arXiv:0904.0734v2](https://arxiv.org/pdf/0904.0734v2),
13 May 2009, pp. 1--2, Horn theorem after (1.1), proof through (1.2).
Apply it to the real symmetric matrix S J S, S=(Sigma^*)^(1/2).
Its eigenvalues majorize the constant diagonal tr(SJS)/3: in
decreasing order the first eigenvalue is at least the average and
the first two sum to at least twice the average. L419's deterministic
two-rotation implementation, including equality and tie branches,
supplies the extra Borel choice of orthonormal basis u_1,u_2,u_3 with
u_i^T SJS u_i=tr(SJS)/3. No continuity or closeness to the old selected
basis, and no Borel assertion beyond the source's scope, is presumed.

Let mu^* assign probability 1/6 to each of m+xi_i and m-xi_i, where
xi_i=sqrt(3)S u_i. Its mean is m and centered covariance is Sigma^*.
Each centered quadratic value is tr(J Sigma^*)<=-c' ell^(7/8), and
|xi_i|<=sqrt(3||Sigma^*||)=O(ell^(9/16)). Bounded m,J imply

    D(m+/-xi_i)<=-c' ell^(7/8)+C ell^(9/16)+C<0.      (15)

Thus every new bulk atom is strictly in the negative cone, with one
support onset. Define

    nu^*=p delta_Y+k_+ delta_Z_++k_- delta_Z_-+w mu^*.  (16)

The unchanged rare components retain their support orientation;
(15) therefore proves complete avoidance of {D>0,B<0}.

All integrands in (3), (5) and (7) are jointly Borel on H<=t<=2H
and locally bounded on compact eventual-H intervals, as are the
unchanged full matrix inputs (1). After t=Hu their parameter
integrals are Borel. The denominators W_H and C_H are bounded away
from zero on the chosen ray, so (12) and (6) are jointly Borel.
Taking the positive matrix square root and L419's finite Borel branches
gives a jointly Borel kernel (16). Its masses still sum to one at
each height, preserving the uniform height and exact actual-response
marginal. Taking the maximum of the finitely many onsets above changes
no value or threshold of the original cutoff j(H).

### Exact seconds, first means and every selected tolerance

The full conditional raw matrix of (16) satisfies exactly

    q^*-q^0=w F_H,
    E_H(q^*-q^0)=0, (q^*-q^0)_11=0.                 (17)

This uses unchanged m and rare components; the translated centered
laws have zero centered mean, so no cross term is omitted. Hence
E_nu^* XX^T=ell K exactly, including both tiny odd tolerances
O(H^(-2/3)ell^-1) and O(H^(-2/3)ell^-3). All conditional x-second
correlations are identical to L441's at every height, so the selected
W^2 correlation and all separately fixed-prime limits keep their
original o(ell) errors without any new averaging. The conditional
vector mean is unchanged, giving E_nu^* B=-b0 exactly, within its
original O(ell^-1+H^(-1/2)ell^2) allowance. For first D,

    |E_nu^* D-E_nu^0 D|=|E_H[w tr(J F_H)]|=O(1),     (18)

which fits the original -a_* ell+o(ell) requirement. No constant-term
first-D identity is claimed.

For any centered symmetric law with covariance Sigma and translation
m, expansion of the exact forms D and B gives

    E(DB)=(b^T m)tr(J Sigma)+2m^T J Sigma b
                                      +(m^T Jm)(b^T m).

The odd centered terms vanish; the two quadratic centered terms use
the covariance. Applying this identity to the old and new bulk yields
the exact signed difference

    E_mu^*(DB)-E_mu^0(DB)
        =(b^T m)tr(J F_H)+2m^T J F_H b=O(1)         (19)

uniformly in height. For any fixed bounded test U(t), the complete
weighted signed cubic consequently changes by O(||U||_infinity).
This preserves L438's three original O(ell) remainders for U=1,
cos(t log 2) and the fixed P, and every separately fixed three-prime
cosine coefficient with its o_v(ell^2) error. The same family works
for all fixed characters; no actual sine limit, atom continuity or
growing-character uniformity is asserted.

Fresh absolute bounds, rather than closeness of selected atoms, control
the other moments. All new bulk states have norm O(ell^(9/16));
their fourth and third costs are respectively O(ell^(9/4)) and
O(ell^(27/16)). Every selected quartic has bounded response
coefficients and modulus at most C|X|^4. The high integrands remain
exactly the old actual quartic integrands; the unchanged intermediates
cost O(ell^(7/2)). Both their addition and the new bulk addition are
o(ell^4), preserving all 23 signed, zero or positive coefficients and
the O(ell^4) fourth envelope. Each absolute third envelope is bounded
by the high O(ell), intermediate O(ell^2) and new bulk
O(ell^(27/16)) costs, within O(ell^(9/4)). These constants precede
the choice of fixed test or cap.

The actual response annulus, its positive C bound, derivative bounds
and curvature remain exact. High and intermediate states are unchanged;
the new bulk size is as above. L438's exact bounded conversion to
physical jets and the uniform limit ell^3 L(t)^j/T(t)^(1/2)->0 for
j<=2 permit one fixed enlargement of qualitative physical constants,
independent of H and the cutoff stage, as allowed in the hypotheses.

Finally, because |DB|<=C|X|^3, for every fixed lambda>0 the new bulk
capped absolute cubic is at most

    C/(lambda ell^2) E_H[w E_mu^* |X|^4]
                                    =O_lambda(ell^(1/4)).         (20)

The unchanged high and intermediate terms are O(ell) and
O_lambda(ell^(3/2)). Their sum is o(ell^2). The family, all fields
and the support onset were chosen before lambda; only the final
convergence onset in this cap bound may depend on the fixed cap.

By (17) the full occupation change is precisely (7), so the exact
solution (12) applies to the supported family (16). This completes
all three finite-H equalities together with all preservation checks.
The result removes this finite diagnostic as an obstruction to this
bounded covariance repair. Other occupation tests and every independent
realization, clipping, regulator and RH positivity gap remain open.

### Separate critical audit — 2026-10-20, step 271

This RESEARCH / REPRODUCTION / proof_audit uses the unchanged prior
SPECIALIZE assessment
`drafts/literature/2026-10-20-exact-quadratic-block-critical-audit.md`.
The complete proof was checked against L419's exact forms and finite
Borel branches, L438's full selected tolerances, L440's complete first
polynomial, L441's audited preservation interface and L442's audited
remaining polynomials and residuals. The result passes as stated:
no coefficient, hypothesis, cutoff, argument or direct input needs
repair. The precise primary citations above are reused in their assessed
scopes; this verifies their local application, not the general theorems.

**Complete equations and exact solution.** For the ordinary dynamics
x'=Ly and y'=Lz-(L'/L)y, differentiation of x^2, xy and y^2 contributes,
respectively, 2Lxy, L(y^2+xz)-(L'/L)xy and
2Lyz-2(L'/L)y^2. Differentiating e s/L contributes one further
normalization derivative. Thus the three A_j in (2) have exactly the
coefficients -1,-2,-3, and both endpoints vanish. Only x,y are
differentiated; C^2 for the scalar trajectory suffices. No differentiable
law or third derivative is presumed.

The full conditional matrix is (1), including R and mm^T. Replacing
only the centered covariance changes it by w F_H. With the convention
V_ij=e_i e_j^T+e_j e_i^T, the raw entries change by
w h_H a_H, w h_H b_H, w h_H c_H in positions 12,13,23.
The diagonal entries do not change. Reading the individual monomials
in (2) now gives exactly the rows (2C_H,0,0), (D_H,C_H,0),
(0,0,2C_H). In particular xz contributes C_H b_H, not twice that
quantity. This verifies (7) without discarding any rare or slow term.

Let epsilon_H=H^-1+E_H(1-w). The exact recentering gives
E_H(w h_H)=0, with W_H>=1/4. Integration of the fixed frequency
gives mu_H=O(epsilon_H) and E_H(e w s)=O(epsilon_H).
Integration by parts for e cos(2omega t), and
integral_1^2 eta=1/30, gives
E_H(e w s^2)=1/60+O(epsilon_H).
Therefore C_H=1/60+O(epsilon_H)+O(epsilon_H^2).
Here E_H(1-w)=O(ell^(-5/2)), uniformly along the saved real-H ray;
no pointwise small rare mass is used. This proves the claimed eventual
lower bound 1/120. All three terms of A_2 are bounded by C/ell,
so |D_H|<=2||A_2||_infinity=O(1/ell).

More explicitly the inverse, in the coefficient ordering of (7), is

    M_H^-1=[[1/(2C_H),0,0],
            [-D_H/(2C_H^2),1/C_H,0],
            [0,0,1/(2C_H)]].

Its entries are uniformly bounded on one full eventual ray. This
also verifies the rank hypothesis of Boyd's imported theorem for
[M_H 0]; the extra minimum-norm coordinate is zero. L441/L442
provide bounded complete residuals with the limits (4), not equations
with their errors removed. Substituting those exact residuals in (12)
gives successively 2C_H a_H=-r_1,
D_H a_H+C_H b_H=-r_2, and 2C_H c_H=-r_3.
The limit of c_H is
-(omega/(360 sqrt(2)))/(1/30)=-omega/(12 sqrt(2)).
Consequently all coefficients and the field are bounded as in (13).
The full new residuals are zero at each H, not merely o(1).

**Uniform matrix margins, both signs and parameter dependence.**
The exact K in L419 is positive definite: its x,z block has
determinant 1/180 and its remaining diagonal is 1/12. Its exact
J=b b^T-4 Ccal Fmat includes curvature; J and b are bounded.
The L438/L441 margins (14) therefore apply to the actual response.
Adding F_H subtracts at most C_F from the least eigenvalue and
changes the J trace by at most 3||J|| C_F. These constants are
absorbed by the ell^(7/8) margins, since both ell^(1/2) and 1
are smaller orders. The upper covariance norm remains O(ell^(9/8)).

For S=(Sigma^*)^(1/2), SJS is real symmetric, and its decreasing
eigenvalues majorize its constant trace-average diagonal: the first
is at least the average and the sum of the first two is at least
twice the average. This checks real Schur--Horn's hypothesis.
The additional Borel implementation is L419's finite construction.
In a strict branch its rotation parameter solves
A eta^2+2e eta-B=0 with A,B>0; hence the radicand exceeds e^2,
the numerator is positive and the denominator is nonzero.
An equality branch selects a coordinate vector by first index.
The remaining two-dimensional trace is twice the average, so its
diagonals either both equal that average or strictly straddle it.
The second rotation or equality branch exhausts those cases.
All branch sets are Borel. Possible discontinuities or large rotation
parameters do not affect the unit lengths of the resulting basis.

For each i, xi_i=sqrt(3)S u_i has quadratic value tr(J Sigma^*).
For either sign, the translation error is at most
2||J||||m||sqrt(3||Sigma^*||)+||J||||m||^2=O(ell^(9/16))+O(1).
Since 9/16<7/8, all six translated atoms have strictly negative D
on a common ray. Their signed pairs have mean m and centered
covariance (1/3)sum_i xi_i xi_i^T=Sigma^* exactly.
The unchanged rare support and masses retain the required orientation
and total probability one.

After t=Hu, the integrals defining r, mu_H, C_H and D_H have
jointly Borel, locally bounded integrands on compact parameter
rectangles. The old cutoff has only finitely many stages on each
compact H interval. Parameter integration is therefore Borel, even
at its jumps. W_H and C_H are bounded away from zero on the final
ray; inversion, the positive matrix square root and the finite branches
preserve Borel measurability. Taking the maximum of the finitely many
onsets restricts the ray without changing any cutoff stage or threshold.

**All preservation requirements and quantifiers.** The exact zero
weighted mean of F_H proves (17) entrywise. Thus the six raw second
entries remain ell K, including the two odd entries with allowances
O(H^(-2/3)ell^-1) and O(H^(-2/3)ell^-3). The 11 entry vanishes
pointwise, so every conditional x-second correlation is unchanged,
including the selected W^2 and separately fixed-prime limits.
The conditional mean vector is unchanged, giving first B=-b0
exactly. First D changes by O(1)=o(ell), which fits precisely the
original -a_* ell+o(ell) requirement; it need not vanish exactly.

For a centered symmetric vector xi of covariance Sigma, expansion
of D(m+xi)B(m+xi) kills the odd centered terms. The surviving terms
are (b^T m)tr(J Sigma), 2m^T J Sigma b and
(m^T Jm)(b^T m). Thus the signed difference is exactly (19).
Its O(1) bound preserves each old O(ell) cubic remainder, even
for the fixed large polynomial P, and every fixed character's
o_v(ell^2) remainder. No absolute third-moment cancellation is inferred.

The new atoms have norm O(ell^(9/16)). Their fourth and absolute
third costs are O(ell^(9/4)) and O(ell^(27/16)).
The fourth cost is o(ell^4), as is the unchanged intermediate
O(ell^(7/2)) cost; the high component keeps each quartic integrand
exactly. This verifies all 23 quartic coefficients, including zero
and signed ones, and the fourth envelope. The absolute third costs,
with the high O(ell) and intermediate O(ell^2) terms, fit both
original O(ell^(9/4)) envelopes. The exact response and physical
conversion are unchanged; the same uniform polynomial-log versus
T^(1/2) comparison gives one fixed enlargement of physical constants.

Finally the absolute cap inequality is
|DB|min(1,|X|/(lambda ell^2))<=C|X|^4/(lambda ell^2).
The resulting new bulk cost O_lambda(ell^(1/4)), unchanged high
O(ell) and unchanged intermediate O_lambda(ell^(3/2)) are each
o(ell^2). The coefficients, basis, support onset and family were
chosen before lambda or any subsequently fixed character. Only their
convergence comparisons may have test-dependent onsets. No independence,
actual sine limit, growing-character uniformity or atom continuity
enters any check.

This validates the finite-block compatibility result using known tools.
It leaves other occupation identities, actual/global realization,
clipping, capped nondegeneracy, L413's full-error margin and global
mixed positivity unresolved. L440/L442's unchanged-law separations and
L441's narrower repair retain their scopes. The direct mathematical
inputs and argument have not changed, so the DAG row remains correct.

## Mathlib

Full matching coverage of this law-specific exact repair, its uniform
conditioning and Borel support construction has not been checked;
unknown availability is not absence. The general projection, real
Schur--Horn and necessary occupation results are imported by the precise
citations above. L419 supplies Borel branches beyond the pointwise
matrix source, while L440/L441/L442 supply the audited residual inputs.
The finite specialization and preservation proof here is informal,
not a Lean or numerical certificate. The separate step-271 audit above
validates its stated scope; it does not establish Mathlib coverage.
