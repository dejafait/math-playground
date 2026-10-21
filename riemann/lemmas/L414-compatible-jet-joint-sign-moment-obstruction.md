# Lemma 414: compatible-jet moments admit joint-sign avoidance

## Hypotheses

Use the exact positive finite constants c=1/(4pi), a_*,b_*,beta_*,kappa_*
and Psi of L410 (2), with stars distinguishing constants from response
coordinates. Let C be the entire rational matrix in L401 (2), in its
stated order, and Gamma=(c^2 Psi/zeta(2)) C. No entry or constant is
rounded or changed. Use the actual positive envelope A of L367 and
alpha=A'/A, q=(log A)'' of L370. The selected local-jet relaxation is
the one specified in the step-138 SPECIALIZE assessment
`drafts/literature/2026-10-15-jet-supported-moment-feasibility-review.md`.

Precisely, for every sufficiently large real H, ell=log H, a state is
(t,x,y,z,v_0,v_1,v_2,a,h), H<=t<=2H. Put T=1+t, L=log(2+t),
X=(x,y,z), U=|X|^2, omega=(ax,ay,az,hx,hy,hz), and convert by

    P_0=x, P_1=y+alpha x/L,
    P_2=z+2alpha y/L+(q+alpha^2)x/L^2,
    V_0=v_0, V_1=v_1+alpha v_0/L,
    V_2=v_2+2alpha v_1/L+(q+alpha^2)v_0/L^2.

Define the exact physical polynomials

    ell_F=P_1^2-P_0 P_2, Ccal=V_1^2-V_0 V_2,
    Bcal=2P_1 V_1-P_0 V_2-P_2 V_0,
    Delta=Bcal^2-4 ell_F Ccal.

Require support on {Delta<=0 or Bcal>=0} and fixed finite positive
E_j,D_j,K independent of H satisfying

    |P_j|<=E_j T^(1/2)L^(-j), |V_j|<=D_j (j=0,1,2),
    Ccal>=1/(128 pi^2 zeta(5/2)^2),
    zeta(5/2)^(-2)<=a^2+h^2<=zeta(5/2)^2,
    |v_0-ca|, |v_1+ch/2|, |v_2+ca/4|<=K/L.

The moment requirements on this same law are

    E Delta=-a_* ell+o(ell),
    E Delta^2=b_* ell^4+o(ell^4),
    E(Delta Bcal)=beta_* ell^2+o(ell^2),
    E(Delta Bcal^2)=kappa_* ell^4+o(ell^4),
    E |Bcal|^3=O(ell^(9/4)),
    E[Delta omega_i omega_j]=Gamma_ij ell^4+o(ell^4) (i<=j),
    E U^2=O(ell^4), E U^(3/2)=O(ell^(9/4)).             (1)

Use the established actual-family quartic inputs L390, L393, L401 and
L405 and annulus bounds of L368. These do not assume an unknown limiting
joint distribution. The relaxation imposes no uniform t marginal,
single global pair F,G, actual Euler-series realization at the model t,
first Bcal mean, or regulator margin. Its law need not be the actual law.

## Conclusion

Such a law exists for every sufficiently large real H, with one fixed
set of bound constants and a common onset. The first and cubic means
in (1) hold exactly. Both absolute power-three bounds improve to O(ell^2).
All 21 matrix limits and the other quartic limits have the exact required
coefficients. All moments are absolutely integrable. The law is given
explicitly below by a weighted pushforward and one atom. The cited
measurable-map theorem optionally replaces it by at most 29 atoms at
each H; numerical coordinates for those atoms are not asserted.

Consequently P(Delta>0,Bcal<0)=0 and the negative-Bcal clipped square
mean is nonpositive. These selected compatible-jet constraints cannot
force that joint sign or a positive clipped mean. This does not decide
the actual clipped mean, L413's scale/full-error obligation, common-zero
counts, global mixed positivity, or RH. The separate step-141 critical
audit below validates this selected-relaxation conclusion. POTENTIALLY_NEW
describes the original construction's limited prior source comparison,
not certified originality or a new zeta-moment theorem.

## Proof

The prior assessment covers this exact feasibility target. Its existing
moment and atomic-theorem coverage is reused. The specialization needed
here is the support construction with mixed scales and exact curvature;
the inspected sources do not already supply that construction.

### Exact model response and the quartic measure

Write M=zeta(5/2), m=1/M. For m^2<=a^2+h^2<=M^2 choose the
model envelope response triple

    v=(ca,-ch/2,-ca/4).                                (2)

This is a permitted choice of states, not an assertion that actual
response errors vanish. Their complete errors are retained below.
All model states have t=H. Put L_H=log(2+H), r_H=q(H)/L_H^2. Define

    b(X;a,h)=c[a(x/4-z)-hy],
    d(X;a,h)=c^2[((z+x/4)^2-y^2)a^2
                          -y(x-4z)ah/2+xz h^2],
    b_H(X;a,h)=b(X;a,h)-2r_H c a x,
    d_H(X;a,h)=d(X;a,h)+4r_H c^2(-xh/2-ya)^2.          (3)

L370's exact product identity and L405 (2) give Bcal=b_H and Delta=d_H
after the prescribed P,V conversion. L390's displayed polynomial for
the leading response is exactly d. Also, direct conversion gives

    Ccal=c^2(a^2+h^2)/4-r_H c^2 a^2.                 (4)

Thus b_H is odd and homogeneous of degree one in X; d_H is even and
homogeneous of degree two. On |X|=1 and the response annulus all these
functions and omega are uniformly bounded for large H, and

    |b_H-b|+|d_H-d|<=C |r_H|,
    r_H=O(H^(-2)L_H^(-2)).                           (5)

Use tau for an auxiliary actual height in [H,2H]. Let X_act(tau) be
L401's actual envelope jet, R_act=|X_act| and n=X_act/R_act where
R_act>0. Set n=(1,0,0) at R_act=0; its weight below is zero. Let
a_act,h_act be the actual response coordinates at tau. Define a
positive measure mu_H on S^2 times the compact response annulus by

    integral F(n,a,h) dmu_H
      = (1/(H ell^4)) integral_[H,2H] R_act(tau)^4
                F(n(tau),a_act(tau),h_act(tau)) dtau.  (6)

Its mass W_H is bounded uniformly by L390's U^2 envelope. The annulus
follows from L368's absolute right-line upper and lower bounds. This
is a direct pushforward of known continuous functions, not an assumption
about a limiting joint distribution, independent phases or phase visits.

In integrals against mu_H let b_H,d_H and omega have unit critical
argument n. Then simultaneously

    integral d_H^2 dmu_H -> b_*,
    integral d_H b_H^2 dmu_H -> kappa_*,
    integral d_H omega_i omega_j dmu_H -> Gamma_ij (i<=j). (7)

To check every replacement, L390/L401 at the actual height tau give
|Delta_act-d(X_act;a_act,h_act)|<=C R_act^2/ell and
|Delta_act|+|d|<=C R_act^2. L405 gives
|Bcal_act-b(X_act;a_act,h_act)|<=C R_act/ell and
|Bcal_act|+|b|<=C R_act. Also |omega_act|<=C R_act.
The absolute differences for Delta_act^2 versus d^2, for
Delta_act Bcal_act^2 versus d b^2, and for each
Delta_act omega_act,i omega_act,j versus d omega_act,i omega_act,j
are therefore <=C R_act^4/ell. After integration and division by
H ell^4 they cost O(1/ell). Homogeneity identifies the latter ideal
averages with the corresponding mu_H integrals. Substituting b_H,d_H
then costs O(|r_H|W_H)=O(|r_H|) for each of the 23 expressions,
by (5) and boundedness on the unit sphere and annulus. The actual limits
are exactly L393, L405 and L401. This proves (7), with their known
little-o errors plus O(1/ell+|r_H|). Actual response errors are not
discarded, and this replacement is never used for the lower-scale
first or cubic means, nor for the support condition.

### Exact orientation and cubic normalization

Set S_H=integral |d_H b_H| dmu_H. This is uniformly bounded above.
Choose a fixed B_max>0 bounding |b_H| on the compact state set for all
sufficiently large H. Since

    integral d_H b_H^2 dmu_H
       <= integral |d_H| b_H^2 dmu_H <= B_max S_H,

(7) and kappa_*>0 give S_H>=kappa_*/(2B_max)>0 eventually. Hence

    lambda_H=S_H/beta_*                              (8)

is bounded above and below by fixed positive constants. Convergence of
lambda_H is unnecessary.

At each (n,a,h) choose s_H in {1,-1}: if d_H>0 choose the sign making
s_H b_H>=0; if d_H<0 choose the sign making s_H b_H<=0; if d_H=0
take +1. At b_H=0 take +1. This is a Borel rule and gives exactly

    d_H(s_H n)=d_H(n), b_H(s_H n)=s_H b_H(n),
    d_H(s_H n)b_H(s_H n)=|d_H(n)b_H(n)|.              (9)

The support condition holds including both axes. Every product
omega_i omega_j is unchanged by this common critical-jet reversal.
Response phases are not independently changed or averaged.

Push (lambda_H^4 ell^4)^(-1) mu_H forward to the model states

    t=H, X=lambda_H ell^2 s_H n, (a,h) unchanged,
    v as in (2), P,V by the exact product conversion. (10)

This rare component has mass p_H=W_H/(lambda_H^4 ell^4)=O(ell^(-4)),
less than 1/2 eventually. By homogeneity its contributions are exactly

    E_rare Delta = M_H := lambda_H^(-2) integral d_H dmu_H=O(1),
    E_rare(Delta Bcal)=ell^2 S_H/lambda_H=beta_* ell^2,
    E_rare Delta^2=ell^4 integral d_H^2 dmu_H,
    E_rare(Delta Bcal^2)=ell^4 integral d_H b_H^2 dmu_H,
    E_rare[Delta omega_i omega_j]
                   =ell^4 integral d_H omega_i omega_j dmu_H. (11)

The signed scalar M_H is unrelated to M=zeta(5/2). All formulas retain
curvature through the exact d_H,b_H and hold for all sufficiently large
real H, not just along a sequence.

### A bulk atom fixes the first mean

Place the remaining mass 1-p_H at t=H, (a,h)=(1,0), response (2),
and X=(0,Y_H,0), Y_H>=0. This response is in the annulus. Equation
(4) gives C_H=c^2(1/4-r_H)>0 eventually. At this atom Bcal=0,
ell_F=Y_H^2 and Delta=-4C_H Y_H^2 exactly. Define

    Y_H^2=(a_* ell+M_H)/(4C_H(1-p_H)).               (12)

The numerator is eventually positive because a_*>0 and M_H=O(1);
the denominator is bounded below by a fixed positive constant. Thus
Y_H=O(sqrt(ell)). The combined first mean equals -a_* ell exactly.
The atom has Delta<0 and Bcal=0. It contributes nothing to either
Bcal mixed moment and only O(ell^2)=o(ell^4) to Delta^2 and each
Delta omega_i omega_j. Equations (7), (11) and (12) now prove all
signed moments in (1), with the first and cubic moments exact. The
quartic errors are ell^4 times the little-o terms in (7), plus the
stated O(ell^2) bulk contributions where present.

### Absolute envelopes, fixed constants and local compatibility

The rare component has |X|=lambda_H ell^2, so

    E_rare U^2=W_H ell^4,
    E_rare U^(3/2)=W_H ell^2/lambda_H,
    E_rare |Bcal|^3=(ell^2/lambda_H) integral |b_H|^3 dmu_H. (13)

The latter two are O(ell^2). The bulk contributes O(ell^2) to U^2,
O(ell^(3/2)) to U^(3/2), and zero to |Bcal|^3. This proves all
absolute envelopes in (1), even with O(ell^2) for both power-three
quantities. All critical triples are O(ell^2) and responses are in a
fixed compact set, so every signed moment is absolutely integrable
at each H, not merely conditionally defined.

Here are explicit choices of qualitative pointwise bounds. L370 gives
q(t)=O((1+t)^(-2)) on an eventual ray. Since alpha'=q and alpha at
a fixed height is finite, integration proves alpha is bounded there.
Fix A_0>=|alpha| and Q>=|q| on that ray. For L>=1, the conversion
and (2) permit the fixed positive constants

    D_0=1+cM, D_1=1+cM(1/2+A_0),
    D_2=1+cM(1/4+A_0+Q+A_0^2), K=1.                (14)

The three model response errors are exactly zero by choice of states,
while the actual response errors were fully retained in proving (7).
For |r_H|<=1/8, (4) gives uniformly

    Ccal>=c^2(a^2+h^2)/8>=c^2/(8M^2)
          =1/(128 pi^2 zeta(5/2)^2).                (15)

This includes response zeros and the bulk atom. The ordinary P_j are
O(ell^2) by the bounded conversion matrix. Since for each j<=2
ell^2 L_H^j/(1+H)^(1/2)->0, the choices E_0=E_1=E_2=1 work
after enlarging a single finite onset. All constants are fixed before
H; they may be enlarged by fixed factors. No claim is made for smaller
independently specified response constants.

Every state satisfies the exact ordinary/envelope conversion. Indeed one
can assign local Taylor derivatives of f as x,L_H y,L_H^2 z and of g
as T_H^2 v_0,T_H^2 L_H v_1,T_H^2 L_H^2 v_2 at H. Multiplication
by the actual A produces exactly the displayed P,V. This concerns
each local jet, and does not assert one global pair realizing all states.
The actual data at tau are used only in (6); the output states have
changed critical scale and sign and height t=H. Thus the height marginal
is a point mass and the response need not equal its actual value at H,
as permitted in the relaxation. Their joint law is the prescribed
pushforward, with no phase independence assumption.

### Optional atomic replacement and limitation

Import Christian Bayer and Josef Teichmann, *The proof of Tchakaloff's
Theorem*, Proc. Amer. Math. Soc. 134 (2006), 3035--3040,
DOI [10.1090/S0002-9939-06-08249-9](https://doi.org/10.1090/S0002-9939-06-08249-9),
[arXiv:math/0502473v2, Corollary 2, pp. 3--4](https://arxiv.org/pdf/math/0502473v2).
For a positive measure concentrated on a measurable set, an integrable
N-coordinate measurable map has its integral preserved by at most N
positive atoms in that set. This is precisely the theorem inspected
in the prior assessment; it is imported without reproof.

Apply it at each H to the constructed law and the 29 coordinates

    (1,Delta,Delta^2,Delta Bcal,Delta Bcal^2,|Bcal|^3,
      (Delta omega_i omega_j)_(i<=j),U^2,U^(3/2)).

The state set is Borel, by its fixed-height polynomial inequalities and
continuous envelope coefficients. The map is measurable and absolutely
integrable as proved above; the constant coordinate preserves mass one.
The atoms belong to the same support, retaining all pointwise bounds.
Thus the finite replacement preserves every moment and estimate, with
their H-independent constants. This supplies no numerical atom locations,
uniform positions, strong duality or actual-function realization.

Finally Bcal<0 on this support implies Delta<=0, so pointwise
Delta Bcal^2 1_(Bcal<0)<=0. This statistic is absolutely integrable by
the same boundedness (and directly for the optional finite law). Hence
the selected-information inference fails even with the complete matrix.
This extends the scope of L410's scalar obstruction, without deciding
the actual statistic or the independent regulator-margin problem.

### Separate critical audit — 2026-10-15, step 141

This REPRODUCTION proof_audit uses the unchanged SPECIALIZE assessment
`drafts/literature/2026-10-15-compatible-jet-law-critical-audit.md`.
The conclusion passes within precisely the stated relaxation. This
checks the local construction; it is neither a new zeta-moment theorem
nor evidence of originality beyond the sources checked. The already
audited quartic inputs are imported in their existing scopes, not
reproved or extrapolated to higher moments.

**Exact conversion, including curvature.** Write r=q/L^2 at one
fixed height and use the prescribed six converted jets. Expansion gives

    ell_F=y^2-xz-r x^2,
    Ccal=v_1^2-v_0 v_2-r v_0^2,
    Bcal=B_0-2r x v_0, B_0=2y v_1-x v_2-z v_0.

Every alpha term cancels. In the discriminant the r^2 terms cancel
as well, while the r coefficient is

    4[(y^2-xz)v_0^2+(v_1^2-v_0 v_2)x^2-B_0 x v_0]
       =4(xv_1-yv_0)^2.

The remaining quadratic minor polynomial is exactly L390 (5).
Substituting (2) yields every term of (3): the cross term of d is
-c^2 y(x-4z)ah/2, and its curvature term is
4r c^2(-xh/2-ya)^2. Thus (3)--(4) are exact, with no division by
a response, a critical jet, or a Wronskian. In particular these are
valid at either sign boundary. L367's T^2 and L^j divisors occur
after ordinary differentiation. Assigning the two Taylor triples
listed above therefore proves local compatibility without imposing
derivatives on a proposed global family of output states.

**All quartic coordinates and their normalization.** The actual
annulus is m<=|zeta(5/2+i tau)|<=M, since its carrier has modulus
one; L368 proves both inequalities with the complete Euler series.
The map in (6) is Borel, including the zero-jet convention, and

    W_H=(H ell^4)^(-1) integral U_act^2=O(1).

For each of the 23 quartic observables, the complete actual-to-leading
replacement is bounded in absolute value by C R_act^4/ell. For the
mixed scalar use

    Delta_act Bcal_act^2-d b^2
       =(Delta_act-d)Bcal_act^2+d(Bcal_act^2-b^2);

for the square use (Delta_act-d)(Delta_act+d). For every matrix entry
use (Delta_act-d) omega_i omega_j, with |omega_i omega_j|<=C R_act^2.
The input estimates in L390/L401/L405 give these bounds uniformly
on the sharp interval, including zeros. Their normalized integrals
are O(1/ell). Moving the output curvature to r_H is a separate
O(|r_H|W_H) operation on the compact unit state set; it is not a
substitution of tau=H into actual jets or an actual lower-scale mean.

To see explicitly that no matrix entry is lost, let e_i be the six
fixed standard coordinate vectors in L401's stated ordering. Its
quadratic-form asymptotic gives the six diagonal limits from e_i.
For each of the fifteen pairs i<j subtract the e_i and e_j limits
from the e_i+e_j limit and divide by two. The coefficient is
(c^2 Psi/zeta(2)) C_ij, including every zero entry and the exact
off-diagonal factor. The finite union has one eventual onset and a
common little-o bound; no H-dependent vector is used. The physical
weight omega has no factor c. Consequently (7) retains all 21 exact
Gamma entries, as well as b_* from L393 and kappa_* from L405.

**Nonzero normalization and boundary support.** With B_max fixed,
the positive limit kappa_* gives S_H>=kappa_*/(2B_max), while
compact boundedness and W_H=O(1) bound S_H above. Positivity of the
finite constant beta_* from L410 therefore puts lambda_H between
two fixed positive constants. No limiting law or convergence of
lambda_H is required. The orientation can equivalently be written
s_H=-1 when d_H b_H<0 and +1 otherwise. At d_H>0 it makes
b_H(s_H n)>=0; at d_H<0 support already holds, and it makes the
product d_H b_H(s_H n) nonnegative. At d_H=0 every choice is
allowed; at b_H=0 both orientations leave Bcal=0. Thus (9) and
the support condition hold exactly on both axes. All omega_i change
by the same sign, preserving every product omega_i omega_j.

**Mixed scales and the bulk atom.** Put rho=lambda_H ell^2.
A homogeneous observable of degree k in X contributes
lambda_H^(k-4) ell^(2k-4) times its oriented mu_H integral on the
rare component. Applying this separately at k=2,3,4 reproduces
every equality in (11); orientation is used for the cubic one.
In particular its coefficient is S_H/lambda_H=beta_*, not
beta_*/ell or a quartic approximation. Also p_H=O(ell^(-4))<1/2.
At the bulk atom direct conversion gives Bcal=0, ell_F=Y_H^2 and
Delta=-4C_H Y_H^2. Its first-mean contribution is exactly
-a_* ell-M_H, canceling the complete signed rare contribution.
Since M_H=O(1), formula (12) has a positive numerator eventually.
The bulk quartic contributions are O(Y_H^4)=O(ell^2), hence are
negligible at ell^4, and both mixed Bcal moments vanish there.
This verifies the first mean and cubic mean exactly, without a
lower-order error imported from a quartic replacement.

**Uniform bounds, integrability and the atomic citation.** The same
degree calculation gives all three equalities in (13). The bulk
adds O(ell^2) and O(ell^(3/2)) to the two U envelopes, respectively.
Thus both power-three requirements hold with O(ell^2). These are
absolute estimates, so there is no conditional-moment issue. Since
q=O(T^(-2)), integration of alpha'=q gives a fixed bound A_0 for
alpha. The three constants D_j in (14) bound each displayed V_j
by the triangle inequality, and K=1 is permitted. If |r_H|<=1/8,
the coefficient of a^2 in Ccal/c^2 is at least 1/8 and that of h^2
is 1/4; (15) follows on the whole annulus, including a=0 or h=0.
Both components have |X|<=C ell^2 with C independent of H.
Therefore |P_j| L_H^j/T_H^(1/2) tends uniformly to zero for j<=2,
and E_j=1 works after one further fixed onset. Taking the maximum
of this finite collection of onsets covers every sufficiently large
real H. No numerical values for them, or smaller prescribed D_j,
are asserted.

At each such H the law has bounded support in a finite-dimensional
Borel state set and every listed coordinate is bounded and measurable.
There are exactly 6+21+2=29 coordinates in the optional map. The
cited Bayer--Teichmann Corollary 2 applies to this already constructed
positive law; its constant coordinate retains total mass one, and
its atoms lie in the same allowed set. It supplies no feasibility
before construction and no uniform positions or actual realization.
This use needs neither strong duality nor a moment-cone interior.

**Scope of the obstruction.** The clipped statistic is integrable
and nonpositive pointwise on the support, so its mean is nonpositive.
No regulator, global phase realization or first Bcal mean is inferred.
For clarity, the present law actually has

    E Bcal=ell^(-2) lambda_H^(-3) integral s_H b_H dmu_H
           =O(ell^(-2)),

because its bulk Bcal is zero. Thus it does not match L369's actual
negative limiting first Bcal mean. That comparison identifies the
stated omission; it is not an input to this existence proof or a
solution of an enlarged feasibility problem. Adding that constraint
requires a separate assessment and mathematical attempt. L410's
scalar obstruction and L412/L413's distinct stops are not superseded.
The main actual clipped-statistic, full-error regulator and global
positivity gaps remain open. No mathematical script or numerical
fit was used in this audit; the complete calculations are above.

## Mathlib

Full matching coverage for this construction, the measurable-map atomic
theorem and complete zeta-moment inputs has not been checked. Neither
absence nor formal verification is claimed. The classical theorem is
used only after an integrable law has been constructed. No solver,
floating-point fit or numerical certificate is a mathematical input.
