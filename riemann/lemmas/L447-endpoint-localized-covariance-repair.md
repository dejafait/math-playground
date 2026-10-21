# Lemma 447: an endpoint-localized covariance repair of the exact scalar defect

## Hypotheses

Use L443's complete jointly Borel family on its eventual real-H ray,
with ell=log H, E_H=H^(-1) integral_[H,2H], and L(t)=log(2+t).
Denote its bulk covariance by Sigma0, its full raw second matrix by
q0, and its scalar 11 entry by q0_11. Retain L438's exact high and
both signed intermediate components, their probabilities, remaining
mass w, translation m, actual response and curvature, and the original
L429 cutoff j(H), without altering any stage or threshold. In particular

    q0=R+w(Sigma0+mm^T), 1/4<=w<=1, E_H q0=ell K,
    K=[[1,0,-1/12],[0,1/12,0],[-1/12,0,1/80]].

Use L419's exact forms B=b(t)^T X and D=X^T J(t)X, with bounded
b,J,m, K positive definite and tr(JK)<=-delta0<0 uniformly.
The matrix J(t) is distinct from the scalar functional below.
The selected tolerances are the entire L438/L443 list, including
the same-family capped absolute cubic for every fixed positive cap.
No bound on derivatives of the new covariance is imposed.

The pre-existing SPECIALIZE assessment is
`drafts/literature/2026-10-20-endpoint-localized-bulk-covariance-repair.md`,
with its exact covered construction-or-obstruction target. This is
a REPRODUCTION using the assessed cutoff, positive-matrix and
finite-correction tools. The scalar peak input also reuses the
previously inspected Bourgain theorem in
`drafts/literature/2026-10-10-discriminant-unequal-orientation-projection.md`
and its signed-k1 audit assessment. No new zeta theorem or originality
claim is made.

## Conclusion

There is a jointly Borel replacement of only the bulk covariance and
its six-state realization, on one eventual ray of all real H, for
which the complete continuous x-second density q satisfies exactly

    J_H[q]:=q(2H)/L(2H)-q(H)/L(H)
                 +integral_H^(2H) q(t)L'(t)/L(t)^2 dt=0.       (1)

It retains the exact integrated raw matrix ell K, exact first B
mean, every original selected tolerance, strict negative bulk support,
fixed physical envelopes, and all three exact finite occupation
identities of L443. At each fixed H, q is Lipschitz on [H,2H].
The principal covariance change is a nonnegative multiple of K
supported within distance H^-10 of the two endpoints; its exact
weighted recentering and finite-block corrections are uniformly
O(H^(-32/3)) elsewhere. All original rare endpoint terms are retained.

The separate step-287 critical audit below validates this local
selected-law construction. It removes L446's scalar endpoint obstruction by changing the
density, and leaves L444/L446's original stops valid. Although the
formal entry q'/(2L) is integrable and now has zero height integral,
it is not asserted to be the new law's xy entry or a feasible covariance
entry. Other temporal identities, derivative-forced covariance
feasibility, inter-H consistency, actual/global realization, clipping,
capped nondegeneracy, L413's full-error margin and global mixed
positivity remain unresolved. This is neither an RH candidate nor a
new actual-theta sign or zero-exclusion range.

## Proof

### Complete pointwise endpoint bounds

L443 gives, with constants independent of H and of the original stage,

    lambda_min(Sigma0)>=c1 ell^(7/8),
    ||Sigma0||<=C1 ell^(9/8),
    tr(J Sigma0)<=-c2 ell^(7/8)                             (2)

after one common onset. L445 proves that q0_11 and w themselves,
with all their stated branch values, are Lipschitz at each fixed H.
Its exact expression, writing u=|X0|^2, x0=(X0)_1 and
V=max(ell^6,sqrt(2)u), is

    q0_11=u x0^2/V
      +sqrt(ell)[(4/9)F_+/h_++F_- (n_-)_1^2/h_-]
      +w[ell P_j/N_H+(A_H)_11+m_1^2].                    (3)

The calibration and denominators in the second term have fixed
uniform bounds; P_j/N_H<=2ell^(1/8), ||A_H||=O(sqrt(ell)),
and m is bounded. The extra L441/L443 fields have zero 11 entry.
For every t, including u=0 and the max boundary,

    0<=u x0^2/V<=x0^2/sqrt(2).                           (4)

Use L389's exact identity f=F_0/A=-sigma Z(t), sigma in {1,-1},
so |x0|=|zeta(1/2+it)|. Import J. Bourgain, *Decoupling,
exponential sums and the Riemann zeta function*, J. Amer. Math.
Soc. 30 (2017), 205--224,
[arXiv:1408.5794v2, Theorem 5 (0.5), p. 2](https://arxiv.org/pdf/1408.5794v2#page=2):
unconditionally, for each fixed epsilon>0,
|zeta(1/2+it)|=O_epsilon(t^(13/84+epsilon)).
This is the same source and version imported in L391; its statement
and essential completion cases in Section 4 were inspected in the
reused assessment. Choosing epsilon=1/168 gives exponent 9/56<1/6,
hence the weaker uniform bound |x0|=O(t^(1/6)).
Only this value bound is used; no derivative or moving-shift
specialization, and no reproof of Bourgain, is needed.

Equations (3)--(4) give, throughout [H,2H],

    0<=q0_11(t)<=C(H^(1/3)+ell^(9/8))<=C' H^(1/3).       (5)

This is pointwise at both endpoints, not a conclusion from L446's
outer-H averages. It keeps the full high term even when p is large.
Let J0=J_H[q0_11]. Since E_H q0_11=ell and q0_11>=0, L446's
exact integral bound gives

    0<=integral_H^(2H) q0_11 L'/L^2<=1/ell,
    |J0|<=C H^(1/3)/ell.                                (6)

### Opposite endpoint responses with exact recentering

Fix once and for all a smooth function rho on R, valued in [0,1],
equal to one on a neighborhood of zero and supported in (-1,1).
Import the existence of such a cutoff from J. K. Hunter, *Notes on
Partial Differential Equations*, Chapter 1, section 1.9.1,
[Theorem 1.29 and Example 1.30, printed p. 12](https://www.math.ucdavis.edu/~hunter/pdes/ch1.pdf#page=13).
The ambient open sets can be (-1/2,1/2) compactly contained in
(-1,1). Only dilation and restriction of this fixed cutoff are used.
We do not reprove the cutoff theorem.

Put delta=H^-10 and, on [H,2H], define

    chi_-(t)=rho((t-H)/delta),
    chi_+(t)=rho((2H-t)/delta),
    W_H=E_H w,
    v_-=E_H(w chi_-)/W_H, v_+=E_H(w chi_+)/W_H,
    d_-(t)=w(t)(chi_-(t)-v_-),
    d_+(t)=w(t)(chi_+(t)-v_+).

For large H the supports of the two restricted cutoffs are disjoint,
each of length at most delta. At the associated endpoint its value
is one, and at the other endpoint zero. The functions d_-,d_+ are
Lipschitz at this fixed H, and E_H d_-=E_H d_+=0 exactly. Also

    0<=v_-,v_+<=4delta/H.                                (7)

Let j_-=J_H[d_-] and j_+=J_H[d_+]. Linearity, the endpoint values
and |J_H[w]|<=2/ell+1/ell^2 give

    j_-=-w(H)/L(H)+O(delta/(H ell)),
    j_+= w(2H)/L(2H)+O(delta/(H ell)).                    (8)

Here the cutoff integral in each expression is at most
delta/(H ell^2): use 0<=w chi<=1, L'>=0, L'<=1/H and L>=ell.
The recentering term is at most v_±(2/ell+1/ell^2).
This proves both errors in (8) with constants independent of all
rare values, the stage, and any Lipschitz constants.
Since w>=1/4 and L(H),L(2H)<=2ell eventually, a common onset gives

    -j_->=1/(16ell), j_+>=1/(16ell),
    |j_-|+|j_+|<=C/ell.                                 (9)

Define nonnegative amplitudes by exact finite-H quantities:

    alpha_-=max(J0,0)/(-j_-),
    alpha_+=max(-J0,0)/j_+,
    alpha=alpha_-+alpha_+,
    a(t)=alpha_- chi_-(t)+alpha_+ chi_+(t),
    mu=E_H(wa)/W_H=alpha_- v_-+alpha_+ v_+.

At most one amplitude is nonzero. If J0=0 both vanish. Equations
(6), (9) imply alpha<=C H^(1/3), and exact linearity gives

    J_H[q0_11+w(a-mu)]=J0+alpha_- j_-+alpha_+ j_+=0.      (10)

This uses the entire original J0, including both endpoint values
in (3) and its entire moving-weight integral. No rare term has been
removed or replaced by an average.

For later estimates set epsilon_H=alpha delta/H. Then

    epsilon_H=O(H^(-32/3)), 0<=mu<=4epsilon_H,
    E_H[w|a-mu|]<=2epsilon_H,
    E_H a^2<=alpha^2 delta/H=O(H^(-31/3)),
    E_H a^(3/2)<=alpha^(3/2) delta/H=O(H^(-21/2)).        (11)

Indeed E_H(wa)=W_H mu<=alpha delta/H, and the two terms in
the absolute-value bound sum to twice this quantity. These estimates
also hold when alpha=0. They quantify both recentering and peak cost;
shrinking width alone is not used as a support argument.

### Preserve the three finite occupation equalities separately

First set Sigma1=Sigma0+(a-mu)K. Its full raw matrix changes by
w(a-mu)K and has exactly zero integrated change. Write e=eta(t/H),
s=sin(t log 2), with eta(u)=(u-1)^2(2-u)^2, and use precisely
L443's functions

    A_j=e's/L+(log 2)e cos(t log 2)/L-j e s L'/L^2.

They satisfy ||A_j||_infinity<=C/ell for j=1,2,3.
The three complete residuals at Sigma0 are zero. Their changes at
Sigma1 are exactly

    r1=E_H[A_1 w(a-mu)],
    r2=0,
    r3=(1/12) E_H[A_3 w(a-mu)].                          (12)

For the middle identity, K12=0 and K22+K13=0; for the other two,
K12=K23=0, K11=1 and K22=1/12. Thus |r1|+|r3|<=C epsilon_H/ell.
We do not assume endpoint localization alone preserves these equalities.

Reuse the unchanged L443 correction space. Put

    h=s-E_H(ws)/W_H, C_H=E_H(e s w h), D_H=E_H(A_2 w h).

Because w and the cutoff are unchanged, L443's complete conditioning
proof applies: C_H>=1/120 and |D_H|<=C/ell on one ray. With
V_ij=e_i e_j^T+e_j e_i^T for i<j, take

    z1=-r1/(2C_H), z2=-D_H z1/C_H, z3=-r3/(2C_H),
    F(t)=h(t)(z1 V_12+z2 V_13+z3 V_23).                 (13)

This is the exact triangular right inverse evaluated in L443 (7),
(12), with residual vector (r1,0,r3); no new rank theorem or
unproved extension of that map is used. In particular

    E_H(wF)=0, F11=0, ||F||_infinity<=C epsilon_H/ell.    (14)

Set Sigma*=Sigma0+(a-mu)K+F. The change in the three residuals
from F is (2C_H z1,D_H z1+C_H z2,2C_H z3), precisely the negative
of (12). All three complete identities therefore hold exactly.
The field F has no 11 entry, so (10) is unchanged.
All these residual computations concern raw conditional seconds and
make no differentiability assertion about atoms.

### Positive covariance and strictly negative translated support

Set E=-mu K+F. Equations (11), (14) give ||E||_infinity=O(epsilon_H).
Then Sigma*=Sigma0+aK+E, with a>=0. The assessed quadratic-form
convexity of positive matrices (Boyd--Vandenberghe, *Convex
Optimization*, corrected seventh printing 2009,
[sections 2.2.5--2.3.1, pp. 34--36](https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf#page=48))
applies to Sigma0+aK; the signed correction is controlled separately:

    lambda_min(Sigma*)>=c1 ell^(7/8)+lambda_min(K)a-C epsilon_H>0,
    ||Sigma*||<=C(ell^(9/8)+a),
    tr(J Sigma*)<=-c2 ell^(7/8)-delta0 a+C epsilon_H.     (15)

These are simultaneous pointwise bounds. Thus the interpolation
stays inside the admissible cone even at the peaks, rather than
merely staying close to the old covariance.

Import the real Schur--Horn theorem in E. A. Carlen and E. H. Lieb,
*Short proofs of theorems of Horn and Mirsky on diagonals and
eigenvalues of matrices*,
[arXiv:0904.0734v2, pp. 1--2, Horn theorem following (1.1) and proof through (1.2)](https://arxiv.org/pdf/0904.0734v2).
For S=(Sigma*)^(1/2), the real symmetric matrix SJS has eigenvalues
majorizing its constant trace-average diagonal: its largest eigenvalue
is at least the average and its largest two sum to at least twice
the average. Use L419's deterministic Borel rotation construction
to choose the corresponding orthonormal u_i, including all ties.
The six centered atoms +/-xi_i, xi_i=sqrt(3)S u_i, have covariance
Sigma*, and

    xi_i^T J xi_i=tr(J Sigma*), |xi_i|<=C sqrt(ell^(9/8)+a).

Their translations by the unchanged bounded m have discriminant
at most

    -c2 ell^(7/8)-delta0 a+C epsilon_H
                         +C ell^(9/16)+C sqrt(a)+C.     (16)

The bound C sqrt(a)<=(delta0/2)a+C^2/(2delta0), obtained by
completing a scalar square, holds for all a>=0. Since 9/16<7/8,
(16) is strictly negative after one common onset, for every H,t
and every selected branch. This proves translated support, including
at large endpoint peaks. No closeness of the old and new bases is used.

Replace only the bulk by this equal-probability translated six-state
law mu*, keeping the full law

    nu*=p delta_Y+k_+ delta_Z_++k_- delta_Z_-+w mu*.

All masses remain nonnegative and sum to one. The high and two
intermediate components keep their old sign orientation; the new
bulk has D<0. Hence the complete support still avoids {D>0,B<0}.

### Measurability, regularity and the full real-H quantifier

The inherited parameters and complete pointwise functions q0_11,w
are jointly Borel and locally bounded on the eventual domain
{(H,t):H<=t<=2H}. This includes endpoint evaluation, as recorded
in L445/L446. The endpoint cutoffs are smooth functions of (H,t)
for H>0. Changing variables t=Hu in each parameter integral gives
Borel functions of H; the integrands are bounded on compact parameter
sets. The denominators W_H,-j_-,j_+,C_H have the positive lower
bounds already shown. Thus amplitudes, mu, the finite corrections
and Sigma* are jointly Borel. The positive square root and L419
branches give a jointly Borel probability kernel. The original
height marginal dt/H and exact actual-response marginal are unchanged.
The finite maximum of all onsets changes no cutoff stage or threshold.

At fixed H the final 11 density is exactly

    q=q0_11+w(a-mu).                                    (17)

Both w and q0_11 are Lipschitz by L445, a is smooth, and mu is a
constant in t. Hence this is its specified Lipschitz representative,
including endpoints; there is no null-set redefinition. Applying
the AC integration-by-parts formula already imported in L446 proves
2 integral_H^(2H) [q'(t)/(2L(t))]dt=J_H[q]=0. This only verifies the scalar compatibility
statement. No derivative bound uniform in H is claimed, and no
identification of that formal cross entry with the constructed law
is made.

### Exact moments and all selected error budgets

Let DeltaSigma=(a-mu)K+F. Equations (11), (14) imply

    E_H(w DeltaSigma)=0,
    E_H[w||DeltaSigma||]<=C epsilon_H.                   (18)

The complete raw matrix changes by exactly w DeltaSigma because
the conditional means and all rare components are unchanged.
Consequently E_nu* XX^T=ell K, including both zero odd entries,
and E_nu* B=-b0 exactly. The original tiny odd-second tolerances
and first-B tolerance are met with zero error.

The first-D change is E_H[w tr(J DeltaSigma)]=O(epsilon_H),
within its original o(ell) tolerance. For each bounded complex U(t),

    |E_nu*(U x^2)-E_nu0(U x^2)|
                    <=C ||U||_infinity epsilon_H.       (19)

This retains W^2 x^2 at its o(ell) tolerance and every separately
fixed-prime correlation at o(ell), using their existing coefficients.
No new averaging or actual sine limit is needed.

For any symmetric centered law with covariance Sigma translated by m,
the exact cubic formula, already used in L438/L443, is

    E_mu(DB)=(b^T m)tr(J Sigma)+2m^T J Sigma b
                                         +(m^T Jm)(b^T m).

It applies to both old and new six-state laws. The difference is
linear in DeltaSigma, with uniformly bounded coefficients. Thus
every fixed bounded test U has complete signed-cubic change
O(||U||_infinity epsilon_H). In particular the three original
O(ell) remainders for U=1, cos(t log 2), P(theta(t)) remain, as do
all separately fixed three-prime cosine coefficients with o_v(ell^2)
errors. This argument bounds the difference of signed conditional
cubics; it does not claim a corresponding absolute-cubic identity.

For the remaining quantities use fresh absolute bounds. Equations
(11), (15) and bounded m give, for j=3,4, uniformly over the new
bulk atoms, |X|^j<=C(1+ell^(9j/16)+a^(j/2)). Therefore

    E_H[w E_mu* |X|^4]=O(ell^(9/4))+O(H^(-31/3)),
    E_H[w E_mu* |X|^3]=O(ell^(27/16))+O(H^(-21/2)).      (20)

The constants here are fixed independently of H and the stage.
All 23 selected quartics have bounded actual-response coefficients
and modulus <=C|X|^4. The unchanged high part retains each actual
quartic integrand exactly; the unchanged intermediates cost
O(ell^(7/2)); the new bulk cost in (20) is o(ell^4).
Thus every leading quartic coefficient, including negative or zero
ones, survives. The fourth envelope is O(ell^4). The unchanged
high and intermediate third costs O(ell), O(ell^2), together with
(20), retain both absolute third envelopes O(ell^(9/4)), also
for |B|^3 by bounded b.

For fixed lambda>0 use the globally valid inequality
min(1,|X|/(lambda ell^2))<=|X|/(lambda ell^2). The new bulk
capped absolute cubic is consequently at most

    C/(lambda ell^2) E_H[w E_mu* |X|^4]
                         =O_lambda(ell^(1/4))+o(1).     (21)

The unchanged high cost is O(ell) and the two intermediate costs
sum to O_lambda(ell^(3/2)), as in L438. Their sum is o(ell^2).
This law and its widths/amplitudes were chosen without lambda:
one family works for every separately fixed positive cap.
The large endpoint atoms need not lie below the cap for (21).

Finally, by alpha<=C H^(1/3) and (15), every bulk atom has

    |X|<=C(ell^(9/16)+H^(1/6))<=C' H^(1/6).

The exact ordinary/envelope conversion retained in L438 has bounded
coefficients. Thus each |P_j|<=C H^(1/6) on the bulk for j<=2.
Since H^(-1/3)L(t)^j tends uniformly to zero on [H,2H], these
meet the required |P_j|<=E_j T(t)^(1/2)L(t)^(-j) with fixed
constants and one onset. All rare states already satisfy those
bounds and are unchanged. The response, annulus, positive response
quadratic bound and curvature are actual throughout. At each fixed
H all supports are bounded and all observables are integrable.

Equations (10), (12)--(18) prove the exact scalar and finite-block
claims, and (19)--(21) prove the whole selected tolerance list.
No trajectory or covariance converse to the occupation identities
has been used. Narrow endpoint layers may have very large derivatives;
their derivative-forced cross-entry feasibility is a separate question.

### Separate critical audit — 2026-10-20, step 287

This RESEARCH / REPRODUCTION / proof_audit uses the unchanged prior
SPECIALIZE assessment
`drafts/literature/2026-10-20-endpoint-repair-critical-audit.md`.
The complete statement and proof (1)--(21) pass in their stated
selected-law scope. No hypothesis, formula, cutoff, direct input or
mathematical argument needs correction. The following independent
checks record the load-bearing equalities and uniform estimates.
This validates the local application of the cited tools, not a new
zeta theorem or progress beyond the checked sources.

**Complete endpoint density and scalar input.** L445's pointwise
formula includes pY_1^2=u x0^2/V, both intermediate raw seconds,
and the full w-weighted translated bulk entry. Its zero and max
conventions give (4) everywhere: V>=sqrt(2)u, and the numerator is
zero if u=0. The intermediate terms are O(sqrt(ell)) because F_±,
1/h_± and the unit directions have fixed bounds. The bulk terms
are O(ell^(9/8)+sqrt(ell)+1); the old finite repairs have zero
11 entry. Nonnegativity follows from the full probability law, not
from treating the signed constant (A_H)_11 separately as positive.

L389 identifies x0=-sigma Z without dividing by a zeta value.
Thus the scalar Bourgain theorem cited above applies at every real
height, including zeros. Its fixed epsilon gives
13/84+1/168=9/56<1/6. Squaring the resulting weaker bound and
using H<=t<=2H proves (5) with a single constant, without a bound
on derivative jets or an outer-H average. The exact integrated
11 entry is H ell. Consequently the moving-weight term is at most
H ell/((H+2)ell^2)<=1/ell, which proves (6) with both endpoints
retained. The endpoint peak bound is therefore valid along the
entire original ray, rather than almost everywhere or on a sequence.

**Both endpoint signs and exact scalar cancellation.** On each
restricted support the cutoff length is at most delta, its own
endpoint value is one and its other endpoint value is zero.
Since W_H>=1/4, v_±<=4delta/H and E_H d_±=0 exactly.
For w chi_- the only endpoint term in J_H is -w(H)/L(H);
for w chi_+ it is +w(2H)/L(2H). Each integral term has absolute
value at most delta/(H ell^2). Subtracting v_± J_H[w] costs at
most (4delta/H)(2/ell+1/ell^2). As w>=1/4 and both endpoint
L values are at most 2ell eventually, the leading terms have
absolute value at least 1/(8ell). Their errors are o(1/ell),
proving both strict inequalities in (9) on one real-H ray.

For J0>0 only alpha_- is used, and its contribution is exactly
-J0; for J0<0 only alpha_+ is used and contributes -J0; for
J0=0 both vanish. K11=1 therefore gives precisely (10), not an
asymptotic cancellation. Moreover alpha=O(H^(1/3)), and a is
nonnegative and bounded by alpha on a set of length at most delta.
For epsilon_H=alpha delta/H,
E_H(wa)=W_H mu<=epsilon_H and
E_H[w|a-mu|]<=E_H(wa)+W_H mu<=2epsilon_H.
The other exponents in (11) are
1/3-11=-32/3, 2/3-11=-31/3 and 1/2-11=-21/2.
These are integrated estimates; the full pointwise height alpha
is retained in the support and envelope checks below.

**Integrated matrix and complete finite occupation block.** Replacing
only the bulk covariance changes the raw conditional matrix by
w DeltaSigma, because the translation, centered symmetry, remaining
mass and every rare component are unchanged. For the first change
DeltaSigma=(a-mu)K its integrated value is zero entrywise. Reading
the three exact polynomials of L443 gives (12): the first sees
K11=1, the third sees K22=1/12, and the middle sees K12=0 and
K22+K13=0. In particular no monomial xz is counted twice.
The bound ||A_j||<=C/ell and the preceding absolute integral
give |r1|+|r3|<=C epsilon_H/ell.

The recentered h has E_H(wh)=0 and |h|<=2. Its C_H and D_H
depend only on unchanged e,s,w and L, not on the new covariance.
Thus the audited L443 bound C_H>=1/120 still applies. The full
map on the coefficients of V12,V13,V23 is exactly
(2C_H z1,D_H z1+C_H z2,2C_H z3). Substituting (13) gives
(-r1,0,-r3), with no omitted endpoint or slow term. Also
E_H(wF)=0, F11=0 and ||F||<=C epsilon_H/ell. This proves
simultaneously the three finite equalities, all six integrated
raw-second equalities including both tiny odd allowances, and the
unchanged scalar endpoint equality. The conditional mean is the
same m, so the exact first-B identity is preserved as well.

**Peak support, Borel branches and endpoint representative.** Put
E=-mu K+F. It has norm O(epsilon_H); aK is positive semidefinite
and tr(JaK)<=-delta0 a. Weyl's quadratic-form bounds and
|tr(JE)|<=3||J|| ||E|| give all three bounds in (15).
In particular the signed correction is small compared with the
old ell^(7/8) margins uniformly, even when a is largest.

For the real symmetric SJS, decreasing eigenvalues majorize the
constant trace-average diagonal. L419's two-rotation construction
is valid for every such matrix: equality chooses a coordinate;
otherwise two coordinate diagonals straddle the average. In the
strict branch its radicand e^2+AB exceeds e^2 for A,B>0,
so the positive rotation parameter has a nonzero denominator.
The complementary two-dimensional trace is twice the average;
the equality or strict-straddling case exhausts it. Finite
first-index choices make all these branches Borel. This does
not assume eigenvector continuity or similarity to the old basis.
The resulting symmetric atoms have exactly the prescribed covariance
and centered D value tr(J Sigma*).

For both signs of every translated atom, the additional quadratic
terms are bounded by C sqrt(ell^(9/8)+a)+C, hence by
C ell^(9/16)+C sqrt(a)+C. The inequality
C sqrt(a)<=delta0 a/2+C^2/(2delta0) proves a uniform negative
upper bound from (16): the remaining a coefficient is negative
and ell^(9/16)=o(ell^(7/8)). This checks support even at
the peaks, rather than inferring it from their small measure.

On compact parameter ranges the inherited inputs are locally bounded
and jointly Borel, with finitely many cutoff stages. After t=Hu,
parameter integration over [1,2] preserves Borel measurability.
The positive denominators proved above justify all quotients and
the max choice of amplitudes, including J0=0. The square root
and finite branches therefore yield the required joint probability
kernel. Taking a later common onset restricts the ray but changes
no B_j, j(H) or finite-stage test. No uniform Lipschitz constant
in H or differentiation of j(H) is used.

At fixed H, q=q0_11+w(a-mu) is exactly its Lipschitz pointwise
representative by L445; F11=0 and K11=1 justify that identity
at the endpoints too. AC integration by parts gives
integral q'/L=[q/L]_H^(2H)+integral q L'/L^2=J_H[q]=0.
This checks the factor two and the sign of the derivative of 1/L.
It establishes only the integrated compatibility of the formal
cross entry, not its identification with the law's raw xy entry.

**Every selected tolerance and the same-family cap.** Equation
(18) bounds the full integrated absolute covariance change by
C epsilon_H. First D changes by O(epsilon_H), within o(ell).
Any bounded x-second test changes by at most
C||U||_infinity epsilon_H. The full W^2 test is bounded by the
absolute right-line Euler series, and every fixed prime character
has modulus one. Thus their original o(ell) allowances survive.
The exact symmetric translated cubic formula depends linearly on
Sigma, with bounded coefficients m,b,J. It gives an
O(||U||_infinity epsilon_H) signed-cubic change, preserving both
all fixed-character o_v(ell^2) limits and the three stronger
O(ell) remainders. This is not an estimate of absolute cubic
change and is not used as one.

Fresh new-bulk absolute bounds follow instead from
|X|<=C(1+ell^(9/16)+sqrt(a)). The fourth cost is
O(ell^(9/4))+O(H^(-31/3)); the third is
O(ell^(27/16))+O(H^(-21/2)). The unchanged high component
retains every actual quartic integrand; the intermediates add
O(ell^(7/2))=o(ell^4). Together with the new bulk these
preserve all 23 leading quartic coefficients, regardless of sign,
and the fourth envelope. The high O(ell), intermediate O(ell^2)
and new-bulk third costs fit both original O(ell^(9/4))
absolute-third envelopes, including that of B by bounded b.

For every fixed lambda>0, |DB|<=C|X|^3 and the globally valid
cap bound in (21) give new-bulk cost
O_lambda(ell^(1/4))+O_lambda(H^(-31/3)/ell^2).
The unchanged high and intermediate costs are O(ell) and
O_lambda(ell^(3/2)). All are o(ell^2). No atom is assumed
to lie below the cap, and no family parameter depends on lambda.

Finally alpha=O(H^(1/3)) bounds every new-bulk norm by
C(ell^(9/16)+H^(1/6))=O(H^(1/6)). The exact physical-jet
conversion has bounded coefficients, so the required physical
ratios are O(H^(-1/3)L(t)^j), tending uniformly to zero for
j<=2. This supplies fixed physical constants as permitted in
L438, without a pointwise derivative-jet zeta estimate. The rare
states, actual response, annulus, positive response quadratic
bound and curvature are unchanged. All requirements thus hold
on a common eventual real-H ray, with separately fixed test/cap
convergence onsets as originally stated.

The audit preserves the L444 and L446 stops on their original
fixed-density scopes. No derivative-forced covariance feasibility,
all-temporal compatibility, inter-H consistency or actual/global
realization is proved. It leaves every actual clipping, regulator,
global mixed-positivity and RH gap open. Full matching Mathlib
coverage remains unchecked; this is an informal critical audit.

## Mathlib

Full matching coverage for this supported endpoint covariance repair
has not been checked. The imported smooth cutoff, real Schur--Horn,
positive-matrix and AC calculus results are supporting inputs, not
a formalization of the full law. Bourgain's scalar theorem is imported,
not formally verified here. Unknown Mathlib coverage is not evidence
of absence. No numerical certificate or new mathematical script is
used; the independent informal critical audit is recorded above.
