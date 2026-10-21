# Lemma 441: a bounded prime-2 covariance repair of one occupation test

## Hypotheses

Use L438's complete Borel family, exact actual response and curvature,
uniform height marginal dt/H on [H,2H], and every selected constraint
and tolerance in its hypotheses and conclusion. Write ell=log H and E_H
for this height average. Keep its high and both intermediate components,
remaining mass w, mean m, normalized Poisson weight g_H and the original
L429 cutoff j(H) unchanged. Qualitative physical constants may be enlarged
once as permitted there; consistency between different H and trajectory
realization are not required.

Use L419's exact B=b(t)^T X, D=X^T J(t)X and positive definite K, and
its Borel six-state realization for a positive definite covariance.
Use precisely L440's omega=log 2, e_H(t)=eta(t/H),
eta(u)=(u-1)^2(2-u)^2 on [1,2], and transport polynomial T_H in (1).
Its separately audited complete residual for the unchanged L438 law is
omega/(30 sqrt(2))+o(1), with all raw-second terms retained.

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-20-prime-two-occupation-covariance-repair.md`.
Only an absolutely bounded bulk xy covariance perturbation and its
constant integrated recentering are used.

## Conclusion

There is a modified Borel family nu_tilde with the same rare components,
height/response marginal and cutoff, satisfying every L438 selected
constraint, for which

    E_nu_tilde T_H=o(1).                              (1)

The six integrated raw seconds and first B mean remain exactly ell K
and -b0. The conditional raw x-second density is unchanged at every
height. The support still avoids {D>0,B<0}; all cubic/quartic tolerances,
fixed-prime limits, envelopes and L438's same-family capped absolute
cubic conclusion hold. The covariance change is uniformly bounded
independently of H and the cutoff stage.

This local REPRODUCTION specializes the assessed matrix and calculus
inputs; it makes no originality claim. The separate step-263 critical
audit below validates precisely this stated scope. It cancels one residual at scale o(1), not its exact finite-H
identity or the complete family of occupation identities. It supplies
no actual/global realization, actual clipping, capped nondegeneracy,
L413 full-error regulator margin, mixed positivity or RH consequence.
L440 remains correct for its unchanged law.

## Proof

### Explicit perturbation and its constant recentering

All letters below without a tilde refer to L438. Its covariance and
full second calibration are

    Sigma(t)=ell g_H(t)K+A_H,
    W_H=E_H w,
    A_H=-(Q+E_H[wmm^T])/W_H,
    E_H(wg_H)=1,
    Q=E_H[pYY^T+k_+Z_+Z_+^T+k_-Z_-Z_-^T].            (2)

The saved bounds give w>=1/4, E_H(1-w)=O(ell^(-5/2)), m=O(1),
||A_H||=O(sqrt(ell)), bounded J,b, and constants c_i,C_i>0 with

    lambda_min(Sigma)>=c_1 ell^(7/8)-C_1 ell^(1/2),
    ||Sigma||<=C_2 ell^(9/8),
    tr(J Sigma)<=-c_3 ell^(7/8)+C_3 ell^(1/2).        (3)

These hold on the full eventual real-H ray under the original cutoff.
Let V=e1 e2^T+e2 e1^T, so ||V||=1 and its only nonzero entries
are V_12=V_21=1. Define

    d(t)=-omega sin(omega t)/sqrt(2),
    bar_d_H=E_H[w(t)d(t)]/W_H,
    E_H^mat(t)=(d(t)-bar_d_H)V,
    Sigma_tilde(t)=Sigma(t)+E_H^mat(t).               (4)

The superscript distinguishes the matrix E_H^mat from the averaging
operator. Equivalently the new constant correction is
A_tilde_H=A_H-bar_d_H V and the variable addition is d(t)V.
Both are confined to the xy entries. Since w is nonnegative,
|bar_d_H|<=omega/sqrt(2), and therefore

    ||E_H^mat(t)||<=sqrt(2) omega,
    E_H[w E_H^mat]=0.                               (5)

In fact exact integration of sin(omega t) on [H,2H] gives
|E_H sin(omega t)|<=2/(H omega). Hence

    |bar_d_H|<=C[H^(-1)+ell^(-5/2)].                 (6)

Only the integrated loss E_H(1-w) is used here; no uniform smallness
of the high probability is assumed. All constants in (5)--(6) precede
H and its cutoff stage.

### Supported Borel realization

By the Rayleigh quotient inequality and (3)--(5), Sigma_tilde is
positive definite eventually with a lower bound c ell^(7/8), and
||Sigma_tilde||=O(ell^(9/8)). Since the matrix perturbation has rank
at most two and J is bounded,

    |tr(J E_H^mat)|<=2||J|| ||E_H^mat||=O(1).

Thus tr(J Sigma_tilde)<=-c' ell^(7/8) on one common eventual ray.
These are uniform pointwise estimates, including response projection
zeros and every cutoff stage. Increasing the final onset changes no
threshold or value of the original function j(H).

Import the real Schur--Horn theorem from Eric A. Carlen and Elliott H.
Lieb, *Short proofs of theorems of Horn and Mirsky on diagonals and
eigenvalues of matrices*,
[arXiv:0904.0734v2](https://arxiv.org/pdf/0904.0734v2), 13 May 2009,
pp. 1--2, Horn theorem following (1.1), proof through (1.2).
The real symmetric matrix S J S, S=Sigma_tilde^(1/2), has eigenvalues
majorizing the constant diagonal tr(S J S)/3. The theorem supplies
an orthogonal realization of that diagonal. L419's deterministic
two-rotation construction supplies the additionally needed Borel basis
u_1,u_2,u_3, including its equality and tie branches. No reproof of
Schur--Horn or continuity of that basis is used.

Assign probability 1/6 to each of m+xi_i and m-xi_i, where
xi_i=sqrt(3)S u_i. The resulting bulk mu_tilde has mean m,
centered covariance Sigma_tilde, and central symmetry. Each centered
atom satisfies

    xi_i^T J xi_i=tr(J Sigma_tilde)<=-c' ell^(7/8),
    |xi_i|<=sqrt(3||Sigma_tilde||)=O(ell^(9/16)).

Because m,J are bounded,

    D(m+/-xi_i)<=-c' ell^(7/8)+C ell^(9/16)+C<0       (7)

for all six atoms on one common ray. No comparison of the old and
new atom directions is required. Put

    nu_tilde=p delta_Y+k_+ delta_Z_++k_- delta_Z_-+w mu_tilde. (8)

The masses are unchanged and sum to one. L438's rare support and
(7) prove avoidance of {D>0,B<0}. The extra parameter integral in
(4) is Borel after t=Hu, u in [1,2], because w is Borel and locally
bounded and W_H>=1/4. The covariance square root is continuous on
positive definite matrices, and L419's finite branches are Borel.
Thus (8) is one jointly Borel family with the original uniform height
and actual-response marginal. All states are bounded at each fixed H,
as in L438, so the displayed integrals exist.

### Complete seconds, first means and selected correlations

Let C_H(t) be the unchanged full conditional raw second matrix in
L440 (3). Since the rare components and mean are unchanged, exactly

    C_tilde_H(t)-C_H(t)=w(t)E_H^mat(t).              (9)

Integrating (9) and using (5) gives E_nu_tilde XX^T=ell K exactly.
This retains all four even and both tiny odd second tolerances with
zero error; the latter are O(H^(-2/3)ell^-1) and
O(H^(-2/3)ell^-3). There is no bounded integrated residual to charge
against those tolerances. The 11 entry of (9) is identically zero.
Consequently every x-second correlation is exactly the same as before,
including the W^2 correlation with error o(ell) and all separately
fixed-prime limits. No additional Poisson averaging or actual moment
theorem is needed, and the original cutoff is untouched.

The mean of every fiber is also unchanged. Therefore E_nu_tilde B=-b0
exactly, meeting the original O(ell^-1+H^(-1/2)ell^2) allowance.
For the first D mean, (9) gives

    |E_nu_tilde D-E_nu D|
        =|E_H[w tr(J E_H^mat)]|=O(1).              (10)

L438's -a_* ell+o(ell) asymptotic is thus preserved with its original
tolerance. No stronger constant-term matching is claimed or required.

### Cubic, quartic, physical and cap bounds

For any centrally symmetric centered finite law of covariance S_0
translated by m, direct expansion of D B gives

    E(DB)=(b^T m)tr(J S_0)+2m^T J S_0 b
                                      +(m^T Jm)(b^T m). (11)

The odd centered terms vanish, the quadratic terms use the covariance,
and the remaining term is the displayed constant. Applying this identity
to both old and new bulk laws gives the exact difference

    E_mu_tilde(DB)-E_mu(DB)
       =(b^T m)tr(J E_H^mat)+2m^T J E_H^mat b=O(1)  (12)

uniformly at every height. In particular, for any bounded fixed test
U(t), the full weighted signed cubic changes by at most C||U||_infinity.
L438's three original O(ell) remainders for U=1, cos(t log 2), and
the fixed P are preserved. So is every separately fixed three-prime
cosine coefficient with its o_v(ell^2) error. Formula (12) concerns
signed conditional cubics; it is not an absolute third-moment bound.

For the latter and for quartics, use fresh size bounds, allowing the
selected basis to change discontinuously. All new bulk states have
norm O(ell^(9/16)), by (7) and bounded m. Each of the 23 selected
quartics has bounded actual-response coefficients and absolute value
at most C|X|^4. Its new bulk integral is O(ell^(9/4))=o(ell^4).
The unchanged high component still preserves its actual quartic
integrand exactly, and the unchanged intermediates add O(ell^(7/2)).
Thus every quartic coefficient, including signed and zero coefficients,
and the O(ell^4) fourth envelope persist. Both absolute third envelopes
receive O(ell^(27/16)) from the bulk, O(ell^2) from the intermediates,
and O(ell) from the high component, within the original O(ell^(9/4))
allowance. No closeness of the new and old quartic values is asserted.

The response annulus, positive response C bound, its derivative bounds
and exact curvature remain actual and unchanged. The high states and
their bounds are unchanged; intermediate states have norm ell^(3/2)
and new bulk states O(ell^(9/16)). L438's bounded exact conversion to
physical jets and ell^3 L(t)^j/T(t)^(1/2)->0 uniformly for j<=2
therefore allow one fixed enlargement of the qualitative constants on
the whole real-H ray. None depends on the cutoff stage or later cap.

Finally |DB|<=C|X|^3 uniformly. For any fixed lambda>0 the new bulk
contribution to the capped absolute cubic is bounded by

    E_H[w E_mu_tilde(|DB| min(1,|X|/(lambda ell^2)))]
       <=C/(lambda ell^2) E_H[w E_mu_tilde |X|^4]
       =O_lambda(ell^(1/4)).                       (13)

The unchanged high and intermediate bounds are respectively O(ell)
and O_lambda(ell^(3/2)). Their sum with (13) is o(ell^2), exactly
the conclusion of L438 (3). The family and its support onset were
chosen without lambda; only the final cap comparison may depend on
that fixed parameter. This verifies every preservation obligation.

### Full occupation residual

The occupation input is J. B. Lasserre, D. Henrion, C. Prieur and
E. Trelat, *Nonlinear optimal control via occupation measures and
LMI-relaxations*, SIAM J. Control Optim. 47 (2008), 1643--1666,
DOI 10.1137/070685051,
[arXiv:math/0703377v1](https://arxiv.org/pdf/math/0703377v1),
Sections 2.1--2.3, (2.7), (2.10)--(2.12), pp. 3--5.
L440 already specializes its C^1 finite-interval identity to this
phi_H and the ordinary dynamics x'=L y, with zero endpoint values.
At each fixed H the bounded states fit its finite compact setting.
We reuse that necessary identity and L440's audited full residual;
no derivative of w, the selected basis or the cutoff is taken.

The x-second entry is unchanged exactly by (9), so all three x^2
terms of T_H, including e_H' and L', have identical integrals.
Its sole remaining term is 2e_H sin(omega t)xy. Therefore the
complete difference, not only a formal bulk leading coefficient, is

    E_nu_tilde T_H-E_nu T_H
       =2 E_H[e_H sin(omega t)w(t)(d(t)-bar_d_H)]
       =-sqrt(2)omega E_H[e_H w sin^2(omega t)]
                   -2bar_d_H E_H[e_H w sin(omega t)]. (14)

The rare components, bounded translation and all entries of the old
constant correction are retained in E_nu T_H. Their estimates are
precisely those established in L440; none is discarded anew here.

For a fixed nonzero k omega, integration by parts gives
|E_H[e_H exp(ik omega t)]|<=C_k/H, including both endpoints
(indeed eta vanishes there). The identity sin^2=(1-cos(2omega t))/2
and integral_1^2 eta=1/30 imply

    E_H[e_H w sin^2(omega t)]
        =1/60+O(H^(-1)+ell^(-5/2)),
    E_H[e_H w sin(omega t)]
        =O(H^(-1)+ell^(-5/2)).                     (15)

Replacing w by 1 costs at most ||eta||_infinity E_H(1-w), which
proves the stated errors even when the high mass is not pointwise
small. Equations (6), (14)--(15) yield

    E_nu_tilde T_H-E_nu T_H
       =-omega/(30 sqrt(2))+O(H^(-1)+ell^(-5/2)).   (16)

Adding L440's complete residual omega/(30 sqrt(2))+o(1) proves (1).
This uses no new sine moment, independence, moving-prime limit or
strengthened cutoff. All parameter choices are explicit and bounded;
all limiting statements are along the full eventual real-H ray.

The positive limit in L440 is consequently not robust against this
specific allowed covariance perturbation. The exact finite-H trajectory
identity, other occupation tests, actual clipping, the regulator margin
and the main positivity gap remain unresolved.

### Separate critical audit — 2026-10-20, step 263

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-20-bounded-covariance-repair-critical-audit.md`.
This RESEARCH / REPRODUCTION / proof_audit validates the construction
as stated. The complete proof was checked against L419's exact forms
and Borel implementation, L438's full moment/support/cap interfaces,
L429's original cutoff and L440's audited complete residual. No source
hypothesis, coefficient, tolerance or cutoff needs repair. The cited
Schur--Horn and occupation theorems are imported in their stated scopes;
the following checks concern this local specialization.

**Exact recentering and both matrix margins.** V has eigenvalues
1,-1,0. Since 1/4<=w<=1, W_H>=1/4 and bar_d_H is an average
of d with respect to the probability measure w dt/(H W_H).
Thus |bar_d_H|<=omega/sqrt(2), and the norm bound in (5) follows.
More importantly, E_H[w(d-bar_d_H)]=0 exactly. To check the stronger
bound (6), write E_H(wd)=E_H d-E_H((1-w)d). The first term
has modulus at most sqrt(2)/H by endpoint integration; the second
is at most (omega/sqrt(2)) E_H(1-w). Division by W_H proves
(6) without assuming p is uniformly small.

The perturbation subtracts at most sqrt(2)omega from the least
eigenvalue of Sigma and adds at most 2sqrt(2)omega||J|| to its
J trace in absolute value. These fixed bounds, together with the
O(ell^(1/2)) original matrix correction, are dominated by the
positive and negative ell^(7/8) margins in (3). Its upper norm
remains O(ell^(9/8)). The original cutoff already yields these
bounds at every real H in every stage; taking a later common onset
neither changes j(H) nor adds a threshold test.

**Every atom and Borel dependence.** For a real symmetric 3-by-3
matrix, its largest eigenvalue is at least its trace average and
its two largest sum to at least twice that average. This verifies
the constant-diagonal majorization required by the cited real
Schur--Horn theorem. L419's finite rotation construction supplies
the separate Borel choice: a strict branch solves
A eta^2+2e eta-B=0 with A,B>0, an equality branch takes a
coordinate vector, and the complementary trace determines the last
value. The branches exhaust ties and do not require eigenvector or
basis continuity. Applying them to SJS is legitimate because S is
the positive square root of the positive definite changed covariance.

For each i and each sign, the centered atom has quadratic value
3 u_i^T SJS u_i=tr(J Sigma_tilde), while its norm is at most
sqrt(3||Sigma_tilde||). Translation changes its quadratic value by
at most 2||J||||m||sqrt(3||Sigma_tilde||)+||J||||m||^2.
The exponent 9/16 is strictly below 7/8, proving strict D<0 for
all six translated atoms on one common ray. The signed pairs have
mean m and covariance (1/3) sum_i xi_i xi_i^T=Sigma_tilde.
All rare atoms and masses remain as in L438, so their support and
the total mass one are retained. Parameter integration after t=Hu
preserves Borel measurability: the old inputs are locally bounded and
have finitely many cutoff stages on each compact H interval. Dividing
by W_H, taking the positive square root and making the finite Borel
choices therefore produces one jointly Borel family.

**All selected moments.** The full conditional raw matrix changes
by exactly w(d-bar_d_H)V; no translated-mean cross term is missing,
since both centered laws have zero mean and the same translation.
Its integrated change vanishes entrywise. This preserves all six
seconds exactly, including the two odd tolerances of orders
H^(-2/3)ell^-1 and H^(-2/3)ell^-3. Its 11 entry is zero at each
height, so every specified x-second correlation is unchanged exactly,
not merely at leading scale. The conditional first vector mean is
also unchanged, giving exact first B=-b0. For first D, the absolute
change is at most 2 sup||J|| sup||E_H^mat|| E_H w=O(1), which
is o(ell) and hence fits precisely L438's original first-D tolerance.

Expanding (m+xi)^T J(m+xi) times b^T(m+xi), centered symmetry
kills the linear and cubic centered terms. The surviving terms are
exactly (11), including the factor 2 in m^T J S_0 b. Subtracting
the old expression leaves (12); bounded m,b,J and E_H^mat make
it uniformly O(1). Multiplying by w and any fixed bounded test and
integrating therefore preserves all three old O(ell) cubic remainders
and every separately fixed character's o_v(ell^2) remainder. This
uses signed centered symmetry only, not an absolute cubic cancellation.

Fresh atom-size estimates suffice for all remaining moments. The new
bulk fourth and third costs are respectively O(ell^(9/4)) and
O(ell^(27/16)). The former is o(ell^4), preserving all 23 signed,
zero or positive quartic coefficients with the unchanged exact high
integrands and intermediate O(ell^(7/2)) costs. The latter, together
with the old high O(ell) and intermediate O(ell^2) costs, fits both
O(ell^(9/4)) absolute third envelopes. The fourth envelope is still
O(ell^4). No closeness of reselected atoms has been used. The exact
response/curvature data remain unchanged; bounded physical conversion
and the uniform limit ell^3 L(t)^j/T(t)^(1/2)->0 for j<=2 give
one fixed enlargement of qualitative physical constants.

The cap estimate uses an absolute inequality, not the signed identity:
|DB| min(1,|X|/(lambda ell^2))<=C|X|^4/(lambda ell^2).
Thus the bulk costs O_lambda(ell^(1/4)); the unchanged high and
intermediate costs are O(ell) and O_lambda(ell^(3/2)). Each is
o(ell^2) for every fixed lambda>0. The family and support onset
were chosen before lambda; only this last convergence onset may
depend on it. All moment claims therefore hold for one family.

**Complete residual, including signs and factors.** L440's polynomial
contains three x^2 coefficients and the cross term
2 e_H sin(omega t)xy. The three x^2 integrals are unchanged
exactly, including both slow derivatives. The changed xy integral is
exactly (14); the old rare, translation and constant-covariance terms
stay inside the complete old residual. No estimate of their new atom
representation is needed because its raw covariance is exact.

The fixed-frequency endpoint bound for e_H is O(1/H), and
integral_1^2 eta=1/30. Hence the unweighted e_H sin^2 mean is
1/60+O(1/H). Inserting w costs O(ell^(-5/2)), and the same
bound controls its inserted e_H sin mean. The recentering term in
(14) is O((H^-1+ell^(-5/2))^2) by (6), smaller than the stated
error. The main change is -sqrt(2)omega/60, exactly
-omega/(30sqrt(2)), verifying (16). Adding the audited full old
residual proves o(1) on the full real-H ray with the original cutoff.
Neither an actual sine moment nor independence nor a derivative of
the Borel kernel has been assumed.

No mathematical defect or missing direct input was found. L440's
unchanged-law separation remains valid. The audit supplies no exact
finite-H cancellation, other occupation identity, actual trajectory,
actual clipping, capped nondegeneracy, L413 margin or RH conclusion.
The direct inputs and mathematical assembly are unchanged.

## Mathlib

Full matching Mathlib coverage for this conditional-law perturbation
has not been checked. The real Schur--Horn and finite-interval occupation
inputs are imported by the precise citations above; L419 supplies the
extra Borel implementation and L440 the already audited complete
residual. No absence claim, numerical certificate or formal verification
is asserted. The new work is the explicit covariance specialization and
its simultaneous preservation estimates, not a reproof of those sources.
