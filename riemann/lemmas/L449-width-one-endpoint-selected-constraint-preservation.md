# Lemma 449: width-one endpoint repair preserves the selected constraints

## Hypotheses

Use L443's family and L447's notation on the original L429 eventual
real-H ray. In particular ell=log H, L(t)=log(2+t), E_H is normalized
integration on [H,2H], q0=R+w(Sigma0+mm^T), and

    R=pYY^T+k_+Z_+Z_+^T+k_-Z_-Z_-^T,
    E_H q0=ell K, K=[[1,0,-1/12],[0,1/12,0],[-1/12,0,1/80]].

Keep all rare states, probabilities, w, m, response, curvature and
cutoff unchanged. Use the same fixed smooth rho as L447, valued in
[0,1], one near zero and supported in (-1,1). Change only delta
from H^-10 to 1 in L447's defining formulas, and recompute all their
parameter integrals, amplitudes and finite corrections at this width.
Every such parameter is constant when differentiating in t.

This is a REPRODUCTION under the pre-existing SPECIALIZE assessment
`drafts/literature/2026-10-20-width-one-endpoint-forced-cross.md`.
The result concerns the selected-moment relaxation. No trajectory,
inter-H consistency, derivative bound on selected atoms or covariance
feasibility of the derivative-forced cross is assumed.

## Conclusion

The width-one formulas define one jointly Borel supported family on
an eventual ray of all real H. The constructed family retains every
L438/L443 selected constraint: exact integrated raw seconds and first
B mean, all three exact finite occupation identities, the first-D
and weighted-second tolerances, all signed cubic remainders and every
separately fixed three-prime cosine limit, all 23 quartic coefficients,
both absolute third envelopes, the fourth envelope, fixed physical
bounds, strict negative bulk support and the same-family vanishing
capped absolute cubic for every fixed positive cap. Its complete
x-second density q is Lipschitz at fixed H and satisfies J_H[q]=0
with the actual endpoint values, where J_H is L447 (1).

Writing a for the nonnegative endpoint bump, alpha for its sole
possibly nonzero amplitude and mu for its exact weighted mean, the
changed estimates are

    alpha=O(H^(1/3)), epsilon=alpha/H=O(H^(-2/3)),
    mu<=4epsilon, E_H[w|a-mu|]<=2epsilon,
    E_H a^2=O(H^(-1/3)), E_H a^(3/2)=O(H^(-1/2)).       (1)

The centered derivative-forced x,y block has the exact test (10)--(12)
below. Its PSD, or a positive-measure failure at arbitrarily large H,
is NOT proved. In particular the constructed family's own xy entry
is not identified with q'/(2L). The separate step-302 critical audit
below validates (1)--(8) and the full selected-preservation claim;
(9)--(12) are outside that audit's scope. This is a partial input,
not a complete feasible extension, an actual clipping result, an RH
candidate or a novelty claim. Other
temporal/mean identities, inter-H/global realization, capped
nondegeneracy, L413's full-error margin and global mixed positivity
remain unresolved.

## Proof

### Width-dependent amplitudes, recentering and finite correction

Set chi_-(t)=rho(t-H), chi_+(t)=rho(2H-t), W_H=E_H w and
v_±=E_H(w chi_±)/W_H. For H>2 their restricted supports are disjoint,
each of length at most one. Thus 0<=v_±<=4/H. Put
d_±=w(chi_±-v_±) and j_±=J_H[d_±]. The original complete density
q0_11 and defect J0=J_H[q0_11] are unchanged. L447 (3)--(6), which
precede its choice of width, give

    0<=q0_11<=C H^(1/3), |J0|<=C H^(1/3)/ell.

For precision, the analytic input there is Bourgain, *Decoupling,
exponential sums and the Riemann zeta function*, JAMS 30 (2017),
205--224, [arXiv:1408.5794v2, Theorem 5 (0.5), p. 2](https://arxiv.org/pdf/1408.5794v2#page=2).
Its unconditional exponent 13/84+epsilon with epsilon=1/168 is
9/56<1/6. L447 uses only |x0|=|zeta(1/2+it)|=O(t^(1/6)),
and its complete branch formula gives the displayed q0 bound.
No new scalar or derivative theorem is asserted here.

The cutoff part of J_H[w chi_±] has integral at most 1/(H ell^2).
The recentering part costs at most (4/H)(2/ell+1/ell^2), since
|J_H[w]|<=2/ell+1/ell^2. The endpoint values therefore give

    j_-=-w(H)/L(H)+O(1/(H ell)),
    j_+= w(2H)/L(2H)+O(1/(H ell)),
    -j_-,j_+>=1/(16ell), |j_-|+|j_+|<=C/ell.          (2)

The last line follows from w>=1/4 and L<=2ell eventually. Set

    alpha_-=max(J0,0)/(-j_-), alpha_+=max(-J0,0)/j_+,
    alpha=alpha_-+alpha_+, a=alpha_- chi_-+alpha_+ chi_+,
    mu=alpha_- v_-+alpha_+ v_+.

Only one amplitude can be nonzero, including the case alpha=0.
Equations (2) and the complete J0 bound imply alpha=O(H^(1/3)).
Since a is supported on at most one length-one layer and 0<=w<=1,

    E_H(wa)<=alpha/H, mu=E_H(wa)/W_H<=4alpha/H,
    E_H[w|a-mu|]<=E_H(wa)+W_H mu<=2alpha/H,
    E_H a^2<=alpha^2/H, E_H a^(3/2)<=alpha^(3/2)/H.

These prove every estimate in (1). Exact linearity, rather than a
small-error argument, gives

    J_H[q0_11+w(a-mu)]=J0+alpha_-j_-+alpha_+j_+=0.     (3)

For the finite correction use exactly L447 (12)--(14), with its
scalar A_j coefficients from L443 (2). Their uniform suprema are
O(1/ell). The intermediate covariance Sigma0+(a-mu)K changes the
three residuals by

    r1=E_H[A_1 w(a-mu)], r2=0,
    r3=(1/12)E_H[A_3 w(a-mu)], |r1|+|r3|<=Cepsilon/ell.

Let h=sin(t log 2)-E_H[w sin(t log 2)]/W_H. L443's unchanged
C_H=E_H[e sin(t log 2)wh]>=1/120 and D_H=E_H[A_2 wh]=O(1/ell)
apply, because neither w nor the cutoff has changed. Here
e=eta(t/H), eta(u)=(u-1)^2(2-u)^2. With V_ij=e_i e_j^T+e_j e_i^T,
define

    z1=-r1/(2C_H), z2=-D_H z1/C_H, z3=-r3/(2C_H),
    F=h(z1 V_12+z2 V_13+z3 V_23),
    Sigma1=Sigma0+(a-mu)K+F.                           (4)

The exact triangular residual change is
(2C_H z1,D_H z1+C_H z2,2C_H z3)=-(r1,0,r3).
Moreover E_H(wF)=0, F11=F22=0, and ||F||_infinity<=Cepsilon/ell.
Thus all three finite identities are exact, the entire integrated
raw matrix is unchanged, and (3) is unaffected.

### Positive covariance, translated support and measurability

L447 (2), inherited from L443, gives fixed positive constants with
lambda_min(Sigma0)>=c ell^(7/8), ||Sigma0||<=C ell^(9/8) and
tr(J Sigma0)<=-c'ell^(7/8). Since K is positive definite,
tr(JK)<=-delta0<0, and ||-mu K+F||<=Cepsilon, (4) implies

    lambda_min(Sigma1)>=c ell^(7/8)+lambda_min(K)a-Cepsilon>0,
    ||Sigma1||<=C(ell^(9/8)+a),
    tr(J Sigma1)<=-c'ell^(7/8)-delta0 a+Cepsilon.        (5)

This uses the PSD-cone convexity in Boyd--Vandenberghe, *Convex
Optimization*, corrected seventh printing 2009,
[pp. 34--36](https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf#page=48),
and a separately bounded signed perturbation.

Import the real Schur--Horn theorem in Carlen--Lieb,
*Short proofs of theorems of Horn and Mirsky on diagonals and
eigenvalues of matrices*, [arXiv:0904.0734v2, pp. 1--2,
Horn theorem after (1.1) and proof through (1.2)](https://arxiv.org/pdf/0904.0734v2).
For S=Sigma1^(1/2), the eigenvalues of the real symmetric SJS
majorize its constant average diagonal. L447's established six-state
Borel implementation consequently gives centered atoms +/-xi_i
with covariance Sigma1, xi_i^T J xi_i=tr(J Sigma1), and
|xi_i|<=C sqrt(ell^(9/8)+a). It supplies the parameter selection;
no measurable-selection assertion is added to the cited theorem.
After the unchanged bounded translation m their quadratic values are
at most

    -c'ell^(7/8)-delta0 a+Cepsilon+C ell^(9/16)+C sqrt(a)+C.

Using C sqrt(a)<=(delta0/2)a+C^2/(2delta0) shows this is strictly
negative uniformly after one onset. Thus the changed bulk has D<0.
The rare components retain their old orientation, so the full law
still avoids {D>0,B<0}. Its probabilities and height marginal are
unchanged. This is a realization of (4), not of the forced cross.

The inherited inputs are jointly Borel and locally bounded on compact
parameter sets. The fixed translated cutoffs, endpoint evaluations
and parameter integrals after t=Hu are Borel. All denominators in
(2), (4) and W_H are bounded away from zero by the displayed bounds.
The positive square root and the inherited finite Borel branches
therefore give one jointly Borel law on the same cutoff ray, after
taking a maximum of finitely many onsets. At each fixed H, L445's
q0_11 and w are Lipschitz; a is smooth and mu is constant in t.
Consequently q=q0_11+w(a-mu) is its specified Lipschitz representative,
including both endpoints.

### Every selected moment and envelope

Write DeltaSigma=Sigma1-Sigma0. Equations (1), (4) give exactly
E_H(w DeltaSigma)=0 and E_H[w||DeltaSigma||]<=Cepsilon.
The conditional means and all rare states are unchanged. Hence
E_nu XX^T=ell K and E_nu B=-b0 remain exact; the tiny odd-second
and first-B error allowances require no estimate. Bounded J gives
a first-D change O(epsilon)=o(ell). For every bounded complex U,

    |E_nu1(Ux^2)-E_nu0(Ux^2)|<=C||U||_infinity epsilon. (6)

This preserves W^2 x^2 and every separately fixed-prime x-second
correlation at its original o(ell) tolerance. The actual response
coefficients are bounded as in L438; no moving-prime limit is used.

For a symmetric centered law translated by m, expansion of the exact
forms B=b^T X and D=X^T JX gives

    E(DB)=(b^T m)tr(J Sigma)+2m^T J Sigma b
                                      +(m^T Jm)(b^T m).

The odd centered terms vanish. Thus the change between the old and
new bulk signed conditional cubics is linear in DeltaSigma with
bounded coefficients. Its complete U-weighted integral is
O(||U||_infinity epsilon). This preserves the original O(ell)
remainders for U=1, cos(t log 2), and the one fixed P, and every
separately fixed three-prime cosine coefficient with error o_v(ell^2).
The family is chosen independently of v. This argument does not
assert an absolute-cubic cancellation.

For absolute bounds, (1), (5) and bounded m give

    E_H[w E_bulk |X|^4]=O(ell^(9/4))+O(H^(-1/3)),
    E_H[w E_bulk |X|^3]=O(ell^(27/16))+O(H^(-1/2)).     (7)

Each of the 23 quartics has modulus <=C|X|^4 with bounded exact
response coefficients. The unchanged high component retains its
actual quartic integrand pointwise, and the intermediates cost
O(ell^(7/2)). Equation (7) is o(ell^4), retaining every leading
coefficient, including signed and zero ones, and the fourth envelope.
For each absolute third envelope (also for |B|^3), the unchanged
high and intermediate costs are O(ell) and O(ell^2); (7) is within
the original O(ell^(9/4)) allowance.

For each fixed lambda>0, |DB|<=C|X|^3 and
min(1,|X|/(lambda ell^2))<=|X|/(lambda ell^2) give a new bulk cost

    O_lambda(ell^(1/4))+O_lambda(H^(-1/3)/ell^2).       (8)

With L438's unchanged high O(ell) and intermediate
O_lambda(ell^(3/2)) costs this is o(ell^2). No law parameter depends
on lambda. Large endpoint atoms are allowed in this global cap bound.

Pointwise the bulk size is at most C(ell^(9/16)+H^(1/6)). L438's
bounded ordinary/envelope conversion gives |P_j|<=C H^(1/6), j<=2,
so |P_j|/[T^(1/2)L^(-j)]=O(H^(-1/3)ell^j)->0 uniformly on the
height interval. One fixed enlargement of physical constants suffices,
as allowed in the selected relaxation. Rare bounds, exact curvature,
response annulus and positive response quadratic bound are unchanged.
This checks the entire selected list, without imposing the forced cross.

### Complete forced-cross reduction, with no feasibility verdict

Use x0=f, y0=f'/L, z0=f''/L^2 and u=x0^2+y0^2+z0^2. Write

    tau=min(u/ell^6,1/sqrt(2)), k=k_++k_-,
    M=k_+Z_+Z_+^T+k_-Z_-Z_-^T,
    S=ell g_H+(A_H)11+m1^2+a-mu.

L445's exact branch expressions, including zero and max conventions,
give

    p=tau^2, w=1-tau^2-k,
    R=tau X0 X0^T+M, q=tau*x0^2+M11+wS.               (9)

The scalar tau,k,M11,w,S are Lipschitz at this fixed H. M12 is
bounded measurable; no derivative of the possibly discontinuous
selected direction or of M12 will be taken. All temporal x-squared
tests force r=q'/(2L) a.e. by L446's weak uniqueness argument for
this Lipschitz representative. Its AC endpoint formula, (3), implies
E_H r=0 exactly. This imports the Hunter/Bell AC interface as cited
in L446: [Hunter, revision 18 June 2014, Definition 3.1 pp. 47--48
and Theorems 3.60, 3.62--3.63 pp. 79--80](https://math.ucdavis.edu/~hunter/pdes/pde_notes.pdf),
and [Bell, 21 October 2015, Section 1 Theorem 1 and uniqueness
paragraph](https://jordanbell.info/LaTeX/mathematics/sobolev1d/).
The hypotheses are locally integrable weak derivatives and a fixed-H
AC representative with smooth strictly positive L. No converse
trajectory theorem is invoked.

For fixed full raw diagonals, rare terms, w and m, the forced centered
block has entries

    A=ell g_H+(A_H)11+a-mu,
    C=ell g_H/12+(A_H)22+(a-mu)/12,
    B_for=(q'/(2L)-R12)/w-m1*m2.                       (10)

The diagonal formulas use the zero diagonal of every old L441/L443
repair and of F. They are strictly positive by (5). The scalar
Schur-complement criterion in Boyd--Vandenberghe,
[Appendix A.5.5, pp. 650--651, (A.13)--(A.14)](https://www.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf#page=664),
therefore says that this block is PSD exactly when

    |B_for|<=sqrt(A C) a.e.                            (11)

This is applied after every rare and translation term is subtracted.
It is not a claim that (11) holds.

Differentiate the Lipschitz scalar formulas (9) a.e. and use
x0'=L y0, w'=-2tau tau'-k', R12=tau*x0*y0+M12.
The high raw-cross term cancels exactly, leaving

    B_for = tau'*(x0^2-2tau S)/(2Lw)
            +(M11'-k'S-2L M12)/(2Lw)
            +S'/(2L)-m1*m2,
    S'=ell g_H'+2m1*m1'+a'.                           (12)

All H-integral parameters, A_H and mu are fixed in this derivative.
On u<ell^6/sqrt(2), tau'=u'/ell^6; on u>ell^6/sqrt(2), tau'=0.
On the equality set u'=0 a.e., since a differentiable real function
has derivative zero at every nonisolated point of a level set at
which the derivative exists; the isolated points form a countable
set. Thus the formula does not suppress a switch-boundary measure
term. It includes the high probability derivative, both intermediate
raw seconds and probability derivatives, translation, Poisson weight
and the full endpoint derivative a'.

The selected integral estimates (1), (6)--(8) do not bound (12)
pointwise against sqrt(AC). L448's narrow-layer proof also supplies
no verdict here: its old-density modulus error C H^2 delta is now
C H^2, while its necessary variation upper bound is C ell H^(1/3)
on a unit layer. Neither is smaller than its c ell required lower
bound. This observation is only a failed comparison, not a proof of
PSD or of its failure. The unsaturated high term in (12) and the
endpoint derivative must be controlled together with the other terms
to decide (11) for this actual fixed family. No such domination or
actual violating set has been proved in this attempt.

### Separate selected-preservation critical audit — 2026-10-21, step 302

This RESEARCH / REPRODUCTION / proof_audit uses the unchanged prior
SPECIALIZE assessment
`drafts/literature/2026-10-21-width-one-selected-constraints-critical-audit.md`.
The full selected-preservation assertion and (1)--(8) pass. The audit
checks the unit-width application independently of L447's narrow-width
budget and L450's conditional use of this input. No formula, hypothesis,
cutoff, direct input or argument is changed. This validates a local
application of the cited sources, not a new zeta theorem or progress
beyond those sources. The later forced-cross calculation is not audited
here, and no feasible forced covariance is inferred.

**Complete endpoint input and unit-width calibration.** The old density
in L445 (6) retains the high raw second, both intermediate raw seconds,
remaining mass, Poisson normalization, constant matrix and translation.
For V=max(ell^6,sqrt(2)u), its high term obeys
0<=u x0^2/V<=x0^2/sqrt(2), also at u=0 and at the switch.
The two intermediate terms are O(sqrt(ell)); the translated bulk
11 term is O(ell^(9/8)+sqrt(ell)+1). The old zero-11 corrections
do not enter it. L447's audited scalar use of Bourgain, with fixed
epsilon=1/168, gives 13/84+epsilon=9/56<1/6. Thus the complete
pointwise bound q0_11<=C H^(1/3) remains valid at both endpoints
on every original stage. No derivative-jet bound is substituted.
Nonnegativity and integral q0_11=H ell bound the entire moving-weight
integral by 1/ell, giving |J0|<=C H^(1/3)/ell.

The restricted supports now each have length at most one. Their
endpoint values are (1,0) and (0,1), and v_±<=4/H follows from
W_H>=1/4. The cutoff integral in J_H is at most 1/(H ell^2),
while weighted recentering costs at most
(4/H)(2/ell+1/ell^2). The leading endpoint terms have magnitude
at least 1/(8ell), so eventually -j_-,j_+>=1/(16ell).
For J0>0 the lower amplitude cancels J0 exactly; for J0<0 the
upper amplitude does so; for J0=0 both are zero. This proves (3)
with the actual endpoint representative, not only almost everywhere.

In every case alpha<=C H^(1/3), and the active bump occupies at
most one unit layer. Hence E_H(wa)<=alpha/H, W_H mu=E_H(wa),
and E_H[w|a-mu|]<=2alpha/H. In particular mu<=4alpha/H.
The two power integrals have exponents
2/3-1=-1/3 and 1/2-1=-1/2, respectively. These verify all
of (1) at width one, including the zero-defect case. The pointwise
height alpha is retained below; small integrated cost is not a
pointwise support argument.

**Full covariance and all exact finite identities.** Changing only
the centered bulk covariance changes the complete raw matrix by
w DeltaSigma. The unchanged translation contributes the same mm^T
and the rare matrix is identical. Exact weighted recentering gives
E_H[w(a-mu)K]=0 entrywise. In L443's complete polynomials,
T1 sees K11=1, T3 sees K22=1/12, and T2 sees K12=0 and
K22+K13=0. Thus the residual vector is precisely (r1,0,r3)
in (4), with |r1|+|r3|<=C epsilon/ell. This uses the full
raw matrix, without omitting any rare or translation term.

The original h, C_H and D_H depend only on unchanged w,e,L and
the fixed sine. L443's bounds C_H>=1/120 and D_H=O(1/ell)
therefore apply to this exact family. Its three-row map is
(2C_H z1,D_H z1+C_H z2,2C_H z3); substitution gives
(-r1,0,-r3). In particular the xz monomial in T2 has coefficient
one, not two. Also E_H(wh)=0, so E_H(wF)=0 exactly and
||F||<=C epsilon/ell. Every diagonal of F is zero. It follows
that all six integrated raw seconds remain ell K, including the
two zero odd entries with tolerances O(H^(-2/3)ell^-1) and
O(H^(-2/3)ell^-3). The conditional mean is unchanged, so first
B remains exactly -b0. These equalities are not charged to an
asymptotic error. F11=0 preserves the scalar endpoint cancellation.

**Peak support and complete Borel realization.** Write E=-mu K+F;
then ||E||<=C epsilon. Since K>0 and tr(JK)<=-delta0<0,
quadratic-form bounds and |tr(JE)|<=3||J|| ||E|| give (5).
The lower covariance margin dominates E on one eventual ray, even
where a=0; at a peak the additional aK improves that margin.
The negative trace retains the full -delta0 a term.

For S=Sigma1^(1/2), the real symmetric SJS satisfies the constant-
diagonal majorization hypothesis of the cited real Schur--Horn theorem.
L419's Borel implementation applies to any such positive Sigma1.
In its equality branch a first coordinate is chosen deterministically.
Otherwise diagonal entries straddle their trace average; its rotation
formula has positive denominator and radicand e^2+AB>e^2 with A,B>0.
The remaining two-dimensional trace is twice the average, so equality
or strict straddling exhausts the second step. These finite branches
remain Borel at ties. No continuity of selected vectors or comparison
with an old selected basis is needed.

The resulting pairs +/-sqrt(3)S u_i have mean zero, covariance
Sigma1 and quadratic value tr(J Sigma1) exactly. For either sign
after bounded translation, the error is at most
C ell^(9/16)+C sqrt(a)+C. Absorbing C sqrt(a) into
delta0 a/2+C^2/(2delta0) leaves a nonpositive peak term and
-c'ell^(7/8)+C ell^(9/16)+O(1)+C epsilon<0 eventually.
Thus every translated atom has strictly negative D, including the
largest peak. The unchanged rare atoms retain their old orientation;
all probabilities, their sum one, and the height/response marginal
are unchanged.

The original stages have B_(j+1)>=2B_j, and hence finitely many
stages on compact H intervals. Inherited inputs, endpoint evaluations
and cutoffs are jointly Borel and locally bounded there. After t=Hu,
all parameter integrals are Borel. W_H and C_H have fixed positive
lower bounds; -j_- and j_+ have lower bounds 1/(16 log H),
positive locally uniformly, not a claimed global constant. Every
quotient, square root and finite rotation therefore defines one Borel
kernel across the original stage jumps. A later common onset changes
no threshold or stage value. At fixed H, L445 supplies Lipschitz
q0_11 and w with their original branch values; a is smooth and mu
is constant in t. Consequently q=q0_11+w(a-mu) is exactly the
Lipschitz raw entry at both endpoints as well as in the interior.
The cited AC integration-by-parts formula gives integral q'/L=J_H[q]
with the plus sign on integral q L'/L^2. It supplies no trajectory
converse or covariance feasibility assertion.

**Every selected tolerance, including rare and translated costs.**
The full absolute covariance change obeys
E_H[w||DeltaSigma||]<=C epsilon=O(H^(-2/3)). Bounded J gives
a first-D change O(epsilon)=o(ell). Equation (6) applies to the
bounded full W^2 response weight and every fixed prime character,
preserving their o(ell) errors. The actual response bounds are
unchanged, so this uses neither a new tail passage nor a growing-prime
uniformity assertion.

Expanding D(m+xi)B(m+xi) and canceling odd centered terms gives
exactly the cubic identity preceding (7). The surviving covariance
terms are linear with bounded coefficients b,J,m. Thus the signed
change with any fixed bounded weight U is O(||U||_infinity epsilon).
This retains all three original O(ell) remainders, including the fixed
large polynomial P, and every separately fixed three-prime cosine
limit at o_v(ell^2). This is not an absolute-cubic cancellation.

For absolute estimates, |X|<=C(1+ell^(9/16)+sqrt(a)) yields
the new bulk fourth and third costs in (7). Each old bulk cost is
also lower order at its selected scale; no matching of old/new atoms
is required. The unchanged high component preserves every homogeneous
quartic integrand pointwise. L438 (9)--(12) give high third cost
O(ell), intermediate third cost O(ell^2) and intermediate fourth
cost O(ell^(7/2)). Together with new bulk fourth
O(ell^(9/4))+O(H^(-1/3)) these preserve every one of the 23
quartic coefficients, including zero and signed coefficients, and
the O(ell^4) fourth envelope. New bulk third
O(ell^(27/16))+O(H^(-1/2)), together with the unchanged rare
costs, fits both O(ell^(9/4)) absolute third envelopes. Bounded b
also controls |B|^3 in this same calculation.

The global cap inequality, valid even above the cap, bounds the new
bulk by its fourth cost divided by lambda ell^2. This is (8).
The unchanged high O(ell) and intermediate O_lambda(ell^(3/2))
costs leave the total o(ell^2). No parameter depends on lambda or
on a later character: only their convergence onsets may depend on
the separately fixed test. Finally alpha=O(H^(1/3)) gives bulk
norm O(H^(1/6)); bounded exact physical conversion gives ratios
O(H^(-1/3)ell^j)->0 for j<=2. This checks the fixed physical
envelopes on the peaks too. The response annulus, positive response
quadratic bound and curvature are inherited unchanged.

All assertions in the selected-preservation scope therefore hold on
one original eventual real-H ray, with the original fixed-test
quantifiers. L444/L446's fixed-density and L448's narrow-layer stops
remain valid on their scopes. The audit proves no actual excursion,
remaining forced-block PSD verdict, other temporal or mean identity,
global realization, clipping, regulator margin or mixed positivity.

## Mathlib

Full matching coverage of this width-one selected-law specialization
and its forced-cross calculation has not been checked. The cited
cutoff, Schur--Horn, PSD and AC theorems are supporting results; they
are not a formalization or verification of this law. The cutoff is
the one already imported in L447 from Hunter, Chapter 1,
[Theorem 1.29 and Example 1.30, printed p. 12](https://www.math.ucdavis.edu/~hunter/pdes/ch1.pdf#page=13).
No reproof of those general theorems, new mathematical script or
numerical certificate is used. Unknown Mathlib coverage is not
evidence of absence.
The separate step-302 audit is informal validation of the selected
application only; it does not establish additional Mathlib coverage.
