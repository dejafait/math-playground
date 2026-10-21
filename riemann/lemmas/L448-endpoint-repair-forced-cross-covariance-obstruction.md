# Lemma 448: the localized endpoint repair fails forced-cross covariance feasibility

## Hypotheses

Use exactly L447's endpoint-repaired family, on the original L429
real-H cutoff ray. Put ell=log H, L(t)=log(2+t), I=[H,2H].
Keep its rare components and their probabilities, remaining mass w,
bulk mean m, and conditional raw x- and y-second densities fixed.
All H-dependent integrals, amplitudes and cutoff stages are constants
when differentiating in t. No atom derivatives or inter-H consistency
are assumed.

Write Sigma0 for L443's covariance before L447, Sigma* for L447's
covariance, and retain the complete rare raw matrix

    R=pYY^T+k_+ Z_+Z_+^T+k_- Z_-Z_-^T.

Thus q0=R+w(Sigma0+mm^T), q*=R+w(Sigma*+mm^T).
Below q denotes the scalar q*11, and q0_11 denotes the old scalar.
Use L447's delta=H^-10, alpha_-,alpha_+, alpha=alpha_-+alpha_+,
a(t), mu and finite correction F. In particular

    Sigma*=Sigma0+(a-mu)K+F,
    q=q0_11+w(a-mu), F11=F22=0, 1/4<=w<=1.             (1)

The unchanged prior SPECIALIZE assessment is
`drafts/literature/2026-10-20-endpoint-repair-forced-cross-feasibility.md`.
This is a REPRODUCTION of the assessed matrix/calculus tools with a
quantitative specialization of the existing analytic inputs, not a
new general covariance theorem or a claim of originality.

## Conclusion

For every sufficiently large original stage j, a positive-measure
set of H in [B_j,2B_j) has the following property. The raw cross entry
forced by all temporal x-squared identities,

    r(t)=q'(t)/(2L(t)) a.e.,

cannot be supplied by a positive-semidefinite bulk covariance with
the specified fixed data. More precisely, its forced centered block

    A=Sigma*11, C=Sigma*22,
    B=(r-R12)/w-m1*m2,
    M=[[A,B],[B,C]]                                    (2)

has determinant strictly negative on a positive-measure subset of
the active endpoint layer (of length delta). Here A,C are everywhere
strictly positive. Consequently no choice of the other covariance
entries repairs this block on an eventual ray of all real H.

The separate step-291 critical audit below validates this result. It stops only this
fixed-data all-temporal extension of L447, whose scalar endpoint
repair and finite-test construction remain valid. Changed densities,
widths, y-second data, rare components or laws are not excluded.
Actual/global realization, clipping, capped nondegeneracy, L413's
full-error regulator margin, global mixed positivity and RH remain
unresolved. There is no new actual-theta sign or zero-exclusion range.

## Proof

### Exact centered matrix test and its complete rate budget

L447 gives a Lipschitz representative q at every fixed H. The
weak-derivative uniqueness argument in L446 (1)--(5), using the
inspected Hunter/Bell inputs, therefore applies to this changed q:
all compactly supported temporal tests force r=q'/(2L) a.e.
It does not transfer L446's old-density endpoint obstruction to q.

Import the scalar principal-block case of Stephen Boyd and Lieven
Vandenberghe, *Convex Optimization*, Cambridge University Press,
2004, corrected seventh printing 2009,
[Appendix A.5.5, printed pp. 650--651, (A.13)--(A.14)](https://www.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf#page=664).
The real symmetric block in (2) is PSD exactly when A,C>=0 and
B^2<=AC. The singular case requires B=0 if either diagonal is zero.
Here L447 (15) makes both diagonals positive. Fixing the full raw
y-second density, R,w and m fixes C through
C=(q*22-R22)/w-m2^2; fixing q likewise fixes A.
Equation (2) subtracts every rare and translation contribution before
applying the theorem. No raw covariance is mistaken for a centered one.

If the block is PSD, its exact reconstruction gives

    |q'| <= 2L (|R12|+w|m1*m2|+w sqrt(AC)) a.e.         (3)

We establish the following bounds with constants uniform in H,t
and the unchanged stage:

    ||R|| <= C0(H^(1/3)+sqrt(ell)),
    |m| <= C0,
    ||Sigma*|| <= C0(ell^(9/8)+alpha),
    alpha <= C0 H^(1/3).                               (4)

For the first bound, L445 (1) gives the exact high matrix
(u/V)X0 X0^T, where u=|X0|^2 and
V=max(ell^6,sqrt(2)u). Thus its norm is at most u/sqrt(2).
The analytic estimate |X0|=O(H^(1/6)) used here is justified in the
next subsection. The two intermediate matrices each have norm
sqrt(ell) F_±/h_±, by L438 (10); both ratios are uniformly bounded.
In particular the full R12 is bounded by the same matrix norm,
regardless of either direction's tie or sign reversal.
The bound on m is L438 (14)--(15). The last two bounds are precisely
L447 (6)--(10), (15), retaining its finite correction and recentering.

Since A,C<=||Sigma*||, (3)--(4) imply the uniform necessary bound

    |q'(t)| <= C1 ell H^(1/3)                           (5)

at almost every point where the block passes. This uses all fixed
terms in (3); none is omitted as negligible without a bound.

### A coarse uniform modulus for the old density

We need only

    Lip_I(q0_11) <= C2 H^2.                             (6)

This is a quantitative addition to L445's fixed-H regularity, not
an assumption that its unspecified Lipschitz constants were uniform.
We prove it from that lemma's exact branch formulas.

First, the shrinking-disk estimate proved in L391's (10)--(11) and
its critical audit bounds zeta by C H^(1/6) on disks of radius
1/ell about 1/2+it, including endpoint heights. The left half of a
disk uses its already checked functional-equation estimate
H^[1/6+(13/18)u], 0<=u<=1/ell; the extra factor is bounded.
The right half uses its strip bound. The analytic function has no
pole in these disks. Apply the standard Cauchy derivative estimate
at orders k=0,1,2,3 to that same scalar disk bound:

    |zeta^(k)(1/2+it)| <= C_k H^(1/6) ell^k.             (7)

L391 states its derivative application only through order two.
Here order three follows directly by the same Cauchy formula
k! radius^(-k) sup|zeta|, not by pretending the stated range includes
three or importing a new derivative-moment theorem. The underlying
scalar input is the already imported Bourgain Theorem 5 (0.5),
*Decoupling, exponential sums and the Riemann zeta function*,
[arXiv:1408.5794v2, p. 2](https://arxiv.org/pdf/1408.5794v2#page=2),
with epsilon=1/168, as specialized in L391. It is not reproved here.

Let s=1/4+it/2 and let
U(t)=Gamma(s)/|Gamma(s)| times pi^(-it/2), of modulus one.
L366's completed-zeta identity gives exactly
f=F_0/A=-Re[U zeta(1/2+it)]. The sector-qualified Stirling/Cauchy
estimates used in L366 (12) give

    |U^(k)|=O(ell^k), 0<=k<=3.

To check the additional fixed order, write
(log U)'=(i/2)(Re psi(s)-log pi). Stirling gives psi=O(ell)
on a fixed-radius complex neighborhood of s in the right half-plane.
Cauchy on a smaller fixed disk gives psi',psi''=O(ell).
Consequently the first three logarithmic derivatives of U are
O(ell), and differentiating the exponential gives the displayed
bounds. The same calculation for log|Gamma(s)| gives the required
third derivative of log A; no exponentially large inverse envelope
is introduced. These are fixed-order consequences of the already
used analytic Stirling estimate.

Leibniz applied to (7), followed by differentiation of the positive
normalizations L and L^2, now gives

    |X0| <= C H^(1/6), |X0'| <= C H^(1/6) ell,
    0<=u<=C H^(1/3), |u'|<=C H^(1/3) ell.               (8)

The response inputs have uniform first-derivative bounds O(ell).
For completeness, gamma recurrence in L366's exact right-line
formula gives

    G/A=Re[P2(t) U(t) zeta(5/2+it)],
    P2(t)=-(3/2+it)(1/4+it/2)/(2pi).

Every derivative through three of the right-line zeta series is
absolutely bounded by sum_n (log n)^k n^(-5/2).
Thus |(G/A)^(k)|<=C H^2 ell^k for k<=3. Differentiating
v_j=(G/A)^(j)/(T^2 L^j), j<=2, gives v_j'=O(ell).
For e=(log A)''/L^2 the preceding gamma bounds give e'=O(ell)
(in fact much smaller); e and v_j themselves are bounded by the
existing inputs. L445's polynomial formulas therefore give
b',C'=O(ell), where C here denotes its scalar response form.
The response carrier a+ih=U zeta(5/2+it) also has derivative
O(ell). The uniformly nonzero denominators in L445's n_-, h_-,
and m then give Lipschitz bounds O(ell) for these bounded quantities.

For the positive direction, use L445 (2), rather than differentiating
the selected vector: M=max(|b^T c1|,|b^T c2|) is O(ell)-Lipschitz,
and h_+=(M^2-4C E_*)M has the same bound. Its positive lower margin
persists at all ties. Both reciprocals 1/h_± are O(ell)-Lipschitz.
L438 (6) and L445's smooth fixed torus functions give a uniform
O(1) bound on the temporal Lipschitz constant of F_H(theta(t)):
the coefficient vector a_H tends to zero and the trigonometric
polynomial and smooth density are fixed. Positive/negative parts
preserve this bound. Hence all intermediate scalar terms in
L445 (3)--(5) have at most a fixed power of ell as Lipschitz constant.

For the high branch put tau=u/V=min(u/ell^6,1/sqrt(2)).
Equations (8) and the elementary Lipschitz rule for min give

    Lip(tau)<=C H^(1/3)ell^(-5).

Since p=tau^2 and the high x-second is tau*x0^2, their Lipschitz
constants are bounded respectively by
C H^(1/3)ell^(-5) and
C(H^(2/3)ell^(-5)+H^(1/3)ell). They are both O(H).
These estimates cover u=0 and the max boundary without selecting
a derivative there. It follows from L445 (5) that Lip(w)=O(H).

Finally let y be the largest prime in the original product P_j.
The original cutoff bound, as checked in L446, gives y<=ell^(1/4)
and P_j<=ell^(1/8) for all H in the stage. Direct logarithmic
differentiation of this finite positive product yields

    |P_j'| <= C P_j sum_(p<=y) (log p)/sqrt(p)
            <= C ell^(1/8) y log(2+y)=O(ell).

Here every factor's denominator is at least
(1-1/sqrt(2))^2, so the constant is uniform. No derivative in H
or in j(H) is taken. L438 gives N_H bounded above and below,
||A_H||=O(sqrt(ell)) and bounded d_H. Accordingly the bracket
ell P_j/N_H+(A_H)11+m1^2 in L445 (6) has supremum
O(ell^(9/8)) and Lipschitz constant O(ell^2).
Multiplying by w adds O(H ell^(9/8)+ell^2).
Adding the high and intermediate contributions proves (6), since
H ell^(9/8)+ell^2+O(H)+O(ell^(3/2))=O(H^2).
The zero-11 fields of L443 do not alter this exact scalar formula.

### Forced endpoint variation versus the PSD budget

L446 (4) supplies, in each sufficiently late original interval
[B_j,2B_j), a positive-measure set E_j on which the old complete
endpoint defect J0 satisfies |J0|>d0=1/(4sqrt(2)).
L447 (8)--(10) give |j_-|,|j_+|<=C3/ell and define the nonnegative
active amplitude by division of |J0| by the appropriate |j_±|.
Thus, for every H in E_j,

    alpha >= (d0/C3) ell > 0.                           (9)

Exactly one endpoint is active. Denote it by e, and let s be the
point delta inward from it. At e the active cutoff is one; at s
it is zero, because rho is supported in (-1,1). The opposite
cutoff vanishes at both points for large H. Therefore (1) gives
the exact endpoint difference

    q(e)-q(s)=q0_11(e)-q0_11(s)
                  +alpha*w(e)-mu*(w(e)-w(s)).          (10)

This is the same formula for either active endpoint; no orientation
of the signed derivative is assumed. By (6), delta=H^-10,
w>=1/4 and L447 (11),

    |q(e)-q(s)| >= alpha/4-C2 H^-8-mu
                >= alpha/8 >= c4 ell,                 (11)

eventually, uniformly for H in E_j. In the last step use
0<=mu=O(H^(-32/3)) and (9). All rare, normalization and translation
variations are in q0_11 and hence in its proved modulus; they cannot
silently cancel the bump.

If (2) were PSD almost everywhere on this layer, (5) and absolute
continuity of q would instead imply

    |q(e)-q(s)| <= integral_layer |q'|
                 <= C1 delta ell H^(1/3)
                 =C1 H^(-29/3) ell.                   (12)

This contradicts (11) for every sufficiently large H in E_j.
The required variation is at least c4 ell, while the allowed/required
ratio in (12) is at most (C1/c4)H^(-29/3), tending to zero.
No numerical threshold or derivative value at an endpoint is used.

The derivative exists a.e. and the entries in (2) are measurable.
If the failure set had measure zero, (12) would follow. Hence it
has positive measure within the layer. Since A,C>0 everywhere,
failure is exactly B^2>AC and det M<0 a.e. on that set.
The nondifferentiability null set itself supplies no evidence and
can be removed. Since B_j tends to infinity and every late E_j has
positive measure, this excludes an eventual all-real-H extension.
L447's equality J_H[q]=0 remains intact; it fixes an integral,
whereas (11)--(12) test the local covariance constraint.

### Separate critical audit — 2026-10-20, step 291

This RESEARCH / REPRODUCTION / proof_audit uses the unchanged prior
SPECIALIZE assessment
`drafts/literature/2026-10-20-endpoint-forced-cross-critical-audit.md`.
The statement and proof (1)--(12) pass in their fixed-data scope.
No hypothesis, exponent, argument or direct mathematical input needs
correction. The following checks validate the local specialization;
they do not independently reprove the imported source theorems or
claim progress beyond those sources.

**Exact response and third-order analytic bounds.** L366 gives
F_0=-p Re[Gamma(s) pi^(-s) zeta(1/2+it)], where
p=t^2+1/4, s=1/4+it/2 and A=p|Gamma(s)|pi^(-1/4).
Thus f=-Re[U zeta(1/2+it)] with precisely the U in this proof.
For v=5/2+it, xi_c(v)/v=(v-1)Gamma(v/2)pi^(-v/2)zeta(v)/2.
Using v/2=s+1 and Gamma(s+1)=s Gamma(s) in
G=-p Re[xi_c(v)/v] gives exactly

    G/A=Re[-(3/2+it)s U zeta(5/2+it)/(2pi)].

This checks the sign, factor two and polynomial degree without
differentiating an asymptotic formula. Gamma recurrence is imported
from [NIST DLMF 5.5.1](https://dlmf.nist.gov/5.5.E1).

L391's scalar disk estimate, including its audited reflected half,
holds at heights slightly beyond both endpoints. The exponent on
Re z=1/2-u is 1/6+(13/18)u, so for u<=1/ell its extra factor
is at most exp(13/18). Its right-half strip exponent differs from
1/6 by O(1/ell) as well. The pole at 1 is outside every disk here.
The fixed-order Cauchy formula
[DLMF 1.9.30--31](https://dlmf.nist.gov/1.9.E31), applied at radius
1/ell, therefore gives (7), including k=3, with constants independent
of H and the stage. This applies the same scalar bound to one more
fixed derivative; it does not extend an unproved moment theorem.

For the gamma terms take disks of radius 1/8 about s. Their real
parts are positive and, eventually, their arguments lie in the fixed
sector |arg z|<=3pi/4. Gamma is pole-free and zero-free there.
The sector-qualified psi expansion and complex remainder in
[DLMF 5.11.2 and 5.11(ii)](https://dlmf.nist.gov/5.11)
give sup|psi|=O(ell); Cauchy on smaller disks gives
psi',psi''=O(ell). Along the real t interval a local phase of U has

    (log U)'=(i/2)(Re psi(s)-log pi).

Its next two derivatives are O(ell), so U^(k)=O(ell^k) for k<=3.
Likewise log A=log p+Re log Gamma(s)-(log pi)/4 has the needed
first three derivatives bounded by O(ell); the rational derivatives
of log p have no large-height singularity. In particular e and e'
in the normalized curvature have the asserted bounds.

Leibniz in the exact f formula now gives f^(k)=O(H^(1/6)ell^k)
for k<=3. Differentiating f'/L and f''/L^2, retaining their L'
terms, proves (8). On the right zeta line all three differentiated
series converge absolutely, since sum (log n)^k/n^(5/2)<infinity.
The degree-two polynomial above then gives
(G/A)^(k)=O(H^2 ell^k), k<=3. Explicitly,

    v_j'=(G/A)^(j+1)/(T^2 L^j)
                          -v_j(2/T+j L'/L), j<=2.

This is O(ell). Thus b,C and the smooth negative direction and
mean have uniformly controlled derivatives. No inverse critical-line
zeta value, exponential inverse-envelope bound or H derivative enters.

**All branches in the old-density modulus.** Independently from
L445 (1), tau=u/V=min(u/ell^6,1/sqrt(2)), p=tau^2, and the high
x-second is tau x0^2. Their product Lipschitz estimates are

    Lip(p)=O(H^(1/3)ell^-5),
    Lip(tau x0^2)=O(H^(2/3)ell^-5+H^(1/3)ell)=O(H).

The formulas agree at u=0 and at the scale switch. Sign reversals
cancel before this calculation. For the positive intermediate,
both selected unit candidates have x-square 4/9 and the identical
quadratic value E_*. Therefore max(|b.c1|,|b.c2|) and its exact
h_+=(M^2-4CE_*)M supply the scalar formulas across every tie.
Their lower margins, and the negative direction's nonzero norm and
h_- margin, make both inverse h functions O(ell)-Lipschitz.
The fixed torus functions and bounded a_H give Lip(F_H)=O(1),
also after sign splitting. Hence the intermediate mass derivatives
cost O(ell^-3/2) and their x-second Lipschitz constants cost
O(ell^3/2). In particular Lip(w)=O(H) holds everywhere in the
Lipschitz sense, not just on smooth selection pieces.

The original cutoff implies y<=ell^(1/4) and P_j<=ell^(1/8).
Logarithmic differentiation of each positive Poisson factor bounds
|P_j'| by C P_j sum_(p<=y)(log p)/sqrt(p). Bounding the sum by
y log(2+y) gives O(ell^(3/8)log ell)=O(ell).
This is uniform in j and requires no infinite Euler product.
L438's 1/2<=N_H<=2, ||A_H||=O(sqrt(ell)) and bounded d_H
are uniform constants or bounds with all parameters held fixed in t.
The full bracket in L445 (6) thus has supremum O(ell^(9/8)) and
Lipschitz constant O(ell^2). Including the w factor costs
O(H ell^(9/8)+ell^2)=O(H^2). Adding both intermediate terms and
the high term proves (6). L443's zero-11 corrections introduce no
unseen selection terms. Every term in q0_11 has been accounted for.

**Centered budget and both endpoint choices.** The fixed raw
diagonals determine A and C only after subtracting R and wmm^T.
L447's F is off-diagonal, so F11=F22=0, and its strict eigenvalue
bound gives A,C>0 everywhere. Reconstruction of raw entry 12 is
r=R12+w(B+m1m2). The cited scalar PSD criterion therefore gives
(3) with precisely the complete rare term and translation shown.
The high matrix has norm tau u<=u/sqrt(2)=O(H^(1/3)); both
intermediate matrices cost O(sqrt(ell)). L447's covariance norm
is O(ell^(9/8)+alpha), with alpha=O(H^(1/3)), and m stays bounded.
Since L=O(ell), this proves (5) with one constant for the whole ray.

L446's audited conclusion supplies measurable E_j of positive
measure in every sufficiently late original [B_j,2B_j), with
|J0|>d0. The upper bound |j_±|<=C3/ell, together with their
strict signs, gives alpha>=d0 ell/C3. Exactly one amplitude is
then nonzero. For either active endpoint e and its inward point s,
the cutoff equals one at e and zero at s. Consequently (10) is
valid with the same orientation q(e)-q(s) in both cases.
The reverse triangle inequality, w(e)>=1/4, |w(e)-w(s)|<=1,
Lip(q0_11)<=C2 H^2 and mu=O(H^-32/3) give (11). In particular
the signed old-density difference cannot cancel the localized bump.

**Measure quantifiers and the stop.** For each such H, q is its
pointwise Lipschitz representative on the entire closed layer.
Weak uniqueness from L446 fixes r=q'/(2L) a.e. on its interior;
no endpoint derivative is required. If the block were PSD a.e.,
absolute continuity and (5) would give (12). Its upper bound
divided by (11)'s lower bound is O(H^-29/3), uniformly in E_j.
After one common onset this is impossible for every H in E_j.
The entries and their a.e. derivatives are measurable. Removing
the nondifferentiability null set, a zero-measure failure set would
give the very a.e. bound just contradicted. Thus det M<0 on a
positive-measure temporal subset for each of these H. No uniform
lower bound for either measure is claimed or needed. Since B_j
tends to infinity, this rules out an eventual all-real-H extension.

The scalar equality J_H[q]=0 and all finite identities in L447
remain valid. This audit validates only the fixed-width, fixed-data
obstruction, not any obstruction for changed widths, densities,
y-second data or laws. All global realization and RH gaps persist.

## Mathlib

Full matching coverage of this fixed-data endpoint-layer obstruction
has not been checked. The matrix input is the cited Schur-complement
theorem; the analytic tools are standard Cauchy estimates, the
already imported scalar zeta bound and sector-qualified Stirling.
The weak-derivative/AC input is the Hunter/Bell interface cited in
L446. Their precise specialization is given above. Unknown Mathlib
availability is not evidence of absence, and this write-up is not
a formal verification or an independent audit of those source results.
