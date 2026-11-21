# Fixed two-cell contact budget — working record, step193

Research invocation under the pre-existing EXPLORE assessment
`drafts/literature/2026-11-09-contact-two-cell-peano-budget.md`.
The supplied source assessment is reused; no new literature review,
parameter sweep, cut adjustment or multiplier enlargement is authorized.

Main gap: L030–L032/C032a actual-Xi all-degree mixed positivity.
Intermediate target: the exact fixed two-cell Budget>=0 at genuine
d=2 actual-theta contacts, 0<lambda<1/20, ||c||_2=1. Its possible
downstream use is a sufficient finite-degree boundary-flux input;
contact existence, initialization, tangency and higher degrees remain
independent gaps. Essential local inputs are L019/L058/L874/L915/L916;
the optional L914 support reduction is not used.

The canonical residual and score formulas, the full three-row null
system, the actual pushforward density and the prior global-convex
and density-dual stops have been read. L915's non-strict square-kernel
concavity and strict h'>19/10 apply without contact assumptions.
Its named Csordas source includes even analyticity at the origin;
L916 proves only an interior inverse statement, so the endpoint must
still be checked. Source coverage for the compact Peano representation
is already approved; the application must pay its boundary terms.

Plan for this one attempt: verify the endpoint extension and whole
exterior image; derive the exact endpoint-corrected compact identity
and exterior orientation; then retain all null rows in a quantitative
attempt to control the cell masses and the exterior cost. The decisive
test is Budget>=0, not the identity or a noncontact example. If the
first attempt leaves that bound unpaid, stop this pilot without moving
the cuts x=1/4,1. No claim or numerical contact certificate exists yet.

Unfinished at the initial checkpoint: endpoint C2 proof, signed
correction, full-tail estimate and independent contact budget sign.
The sections below preserve the completed attempt and its unpaid bound.
No new lemma, mathematical script, DAG edge or overview change results.

## Endpoint and full exterior

Fix any stipulated lambda and normalized nonzero c, retaining H2>=0
and all three rows H2*c=0. Write B(x)=log K(sqrt(x)),

    h(x)=-1-2x*(lambda+B'(x)),
    a=-1, d=h(1/4), b=h(1), L=b-a.

L915's named Csordas input gives an even analytic positive kernel
near u=0. Therefore log K(u) has an even convergent Taylor series
there, so B extends real analytically to a neighborhood of x=0.
In particular h(0)=a and

    h'(0)=-2*(lambda+B'(0))>19/10,
    h''(0)=-4*B''(0).

L915 gives h'(x)>19/10 for x>0 as well. Integrating from zero gives
h(x)>=a+(19/10)*x, hence h maps [0,infinity) bijectively onto
[a,infinity). The ordinary inverse function theorem at zero, applied
to the analytic extension, supplies an inverse on a neighborhood of a;
it agrees on the right with the global inverse. Thus H=h^(-1) extends
with H(a)=0 and belongs to C^2[a,b]. Its right endpoint derivatives are

    H'(a)=1/h'(0),
    H''(a)=4*B''(0)/(h'(0))^3.

In fact it is smooth on the whole closed half-line in the local
extension sense. There is no division by sqrt(x) at the origin in
this argument. In particular a<d<b and L>0. The cell extrema of H''
are finite and attained. L916's inverse theorem alone would not have
paid this endpoint step.

Let nu be L915's exact square-coordinate probability law and let
mu=h_*(-Q*nu). Because h is one-to-one, its pushforward preserves the
Jordan decomposition, so |mu|=h_*(|Q|*nu). All polynomial moments of
nu are finite by L058. L874/L915 also give

    integral |h(x) Q(x)| dnu(x)<infinity.

The latter uses the integrable K' term after multiplication by the
density, not a bound for an unweighted reciprocal of K. Consequently
mu has finite total variation and finite absolute first moment, and
integral H d|mu|=integral x|Q| dnu is finite. The global cancellations
are integral dmu=integral y dmu=0, with absolute integrability.

The endpoint interpolant is exactly ell(y)=(y-a)/L. Therefore the
full exterior quantity is

    D=integral_(1,infinity) |x-(h(x)-a)/L| |Q(x)| dnu(x),
    0<=D<=integral_(1,infinity) [x+(h(x)-a)/L]|Q(x)| dnu(x)<infinity.

No exterior interval or theta summand has been discarded. The inverse
is defined at every point of this exterior. The measures have no atoms
at the two cuts; including a finite endpoint in either part changes
none of these integrals.

## Compact Peano application and its orientation

Define M0, M1, wa, wb and J exactly as in the approved assessment,
using the restriction of mu to [a,b]. The endpoint weights satisfy
wa+wb=M0 and a*wa+b*wb=M1. Hence J(1)=J(y)=0. Moreover

    |J(f)|<=(|mu|([a,b])+|wa|+|wb|)*||f||_infinity.

Thus J is a continuous linear functional on C[a,b] annihilating
affine functions. H' is absolutely continuous on this compact interval
because H is C^2. Apply the s=2 case of the named Peano theorem in
Diethelm (1997), Theorem 1.1, p.727,
https://ems.press/content/serial-article-files/34945?nt=1 .
This is the previously inspected theorem; its general proof is not
reproduced here. Its kernel is Kc(t)=J((y-t)_+), with factorial 1.
It yields

    J(H)=integral_a^b H''(t)*Kc(t) dt.

Because H(a)=0, H(b)=1 and the global affine moments of mu vanish,

    -Phi = integral H dmu
         = J(H)+integral_(b,infinity) [H(y)-ell(y)] dmu(y).

In particular the signed endpoint corrections do not disappear by
assuming that the restricted measure has zero moments: the correction
is exactly integral_[a,b] ell dmu=wb. The exterior restores the
global cancellation.

On cell Ij let mj=inf H'', Mj=sup H'', and retain Pj,Nj from the
assessment. Then

    integral_Ij H''*Kc >= mj*Pj-Mj*Nj,
    -Phi >= sum_j (mj*Pj-Mj*Nj)-D = Budget.

The negative-part mass Nj is nonnegative, so its coefficient is -Mj.
A downward replacement of mj or an upward replacement of Mj weakens
this lower bound in the correct direction. This establishes the
proposed interface only, not Budget>=0 or a flux sign.

## One attempt to pay the masses using all three null rows

Write

    t_n(x)=[z^(2n)] cos(z*sqrt(x))/g_lambda(z),
    V_i(x)=sum_(j=0)^2 c_j*t_(i+j+2)(x),       i=0,1,2.

These are finite polynomials, even when some coordinates vanish.
L874 gives integral t_n dnu=0 and integral x*t_n' dnu=-S_n.
Its justified integration by parts applied to the same individual
polynomial gives integral h*t_n dnu=-2*S_n. It follows that the
complete three-row system is retained as

    integral V_i dnu=0,
    integral h*V_i dnu=-2*sum_(j=0)^2 S_(i+j+2)*c_j=0,
                                                    i=0,1,2.

Explicitly these last equations use (S2,S3,S4), (S3,S4,S5) and
(S4,S5,S6), respectively. No row, support pattern, PSD premise or
actual-theta dependence is replaced by a free moment model. Symmetry
of the double sum gives the exact residual reconstruction

    Q(x)=-2*sum_(i=0)^2 (i+1)*c_i*V_i(x).

For a<=t,y<=b define the positive Green kernel

    G(t,y)=(min(t,y)-a)*(b-max(t,y))/L.

The chord of (y-t)_+ minus that function is G(t,y). Since
mu=h_*(-Q*nu), the signs therefore give

    Kc(t)=integral_0^1 Q(x)*G(t,h(x)) dnu(x)
         =-2*sum_(i=0)^2 (i+1)c_i
                      *integral_0^1 V_i(x)*G(t,h(x)) dnu(x).

This identity is for the corrected compact kernel, not the uncorrected
restriction of a globally cancelled signed measure. In particular
neither the positivity of G nor the three signed zero integrals above
assigns a sign to the V_i-weighted core integrals.

Set Wj(y)=integral_Ij G(t,y) dt. For explicit evaluation on these
fixed cells only,

    W1(y)=(y-a)*(b-y)/2-(y-a)*(b-d)^2/(2L),  a<=y<=d,
    W1(y)=(b-y)*(d-a)^2/(2L),                d<=y<=b,
    W2(y)=(y-a)*(b-y)/2-W1(y).

Both Wj are strictly positive on (a,b). Applying the triangle
inequality row by row, without claiming a sign for a cancellation,
gives the independently valid bounds

    Pj+Nj <= Uj,
    Uj=2*sum_(i=0)^2 (i+1)|c_i|
                    *integral_0^1 |V_i(x)|*Wj(h(x)) dnu(x),
    Cj=max(|mj|,|Mj|),
    Budget >= -sum_j Cj*Uj-D = B_abs.

All these integrals are finite. Also Uj>0: if r is the largest
nonzero coordinate, V_i has degree i+r+2 and leading coefficient
c_r*(-1)^(i+r+2)/(2(i+r+2))!, so it is nonzero for each i. At least
one |c_i| is positive, nu has positive density, and a nonzero polynomial
cannot vanish on an interval. Thus the displayed positive weights
give a strictly positive term in Uj. This argument treats r=0,1,2
without invoking L914 or dividing by a coordinate.

The exact achieved-versus-required comparison at the already certified
parameter lambda=1/40 is

    required: Budget>=0,
    obtained: Budget>=B_abs,
    B_abs=-C1*U1-C2*U2-D < -U2/26620 < 0.

Indeed b=h(1) belongs to I2 and L916 proves H''(b)<-1/26620 there,
so C2>1/26620. This is an exact bound for the attempted absolute
enclosure; no new numerical evaluation or contact sample was used.
It is NOT an upper bound for Budget and proves neither Budget<0 nor
the existence of a contact at this parameter. Nor does it prove that
the three null rows cannot support a better estimate. Passing to
absolute values has lost the signed row cancellations needed for a
positive core surplus. The full exterior D remains unpaid, even
though its finiteness and orientation are now justified.

## Stop and scope

The attempted rowwise payment does not certify the required sign.
Its decisive unpaid claim is an independent lower bound for
sum_j(mj*Pj-Mj*Nj) at least D under the full actual contact system.
The row identities and absolute enclosure above do not supply it.
Per the approved stop test, this first pilot ends here; the cuts,
parameter band, multiplier class and number of cells are unchanged.
There is no sweep, inferred contact, emptiness result or actual-contact
counterexample. All-degree positivity and RH are untouched.

Outcome: EXPLORATION, classification REPRODUCTION. The compact
interface and elementary bounds are an incomplete attempt, not a new
canonical mathematical input. No lemma is created for these standard
identities. Full and supporting Mathlib coverage for this application
remain unchecked, not asserted absent. No mathematical script is
needed for the exact inequalities used here.
