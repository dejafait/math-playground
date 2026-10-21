# Lemma 390: full-tail square-moment reduction and the four-factor contour budget

## Hypotheses

Use the fixed actual F=F_0,G,A,T=1+t,L=log(2+t),D and Delta of
L366/L370 on t>=40. All derivatives below are ordinary height
derivatives. Set

    f=F/A, R=Q/A=exp(i phi), E=R^2,
    Z=zeta(5/2+it), c=1/(4 pi),
    x=f, y=f'/L, z=f''/L^2, U=x^2+y^2+z^2,
    M=(z^2+3xz/2+x^2/16-y^2)/2,
    K=((z-x/4)-i y)^2/2,
    d=c^2 (M |Z|^2 + Re(K E Z^2)).

Q is the gamma carrier in L366. On a dyadic interval define
||h||_(2,H)=(H^(-1) integral_[H,2H] |h|^2)^(1/2), and ell=log H.
There are no zero, sign, independence or RH assumptions.

## Conclusion

Uniformly for sufficiently large real H,

    ||Delta-d||_(2,H)=O(ell),
    ||Delta||_(2,H)+||d||_(2,H)=O(ell^2),
    H^(-1) integral (Delta^2-d^2)=O(ell^3).              (1)

The complete leading square is

    d^2/c^4 = (M^2+|K|^2/2)|Z|^4
              +2 M |Z|^2 Re(K E Z^2)
              +(1/2) Re(K^2 E^2 Z^4).                (2)

In particular the k=1 projected polynomial is retained. It does not
vanish as an identity in the real critical jets. No assertion about
its actual mean, either separately or after summation, follows.

For Z_N=sum_(n<=N) n^(-5/2-it), let d_N be d with Z replaced by Z_N.
With eta_N=sum_(n>N) n^(-5/2), uniformly in N>=1 and large H,

    ||d-d_N||_(2,H) <= C eta_N ell^2,
    |H^(-1) integral (d^2-d_N^2)| <= C eta_N ell^4.     (3)

Thus full response tails are not an obstacle to a leading-coefficient
limit once fixed-head moments have been evaluated. This does not
justify a cutoff growing with H in a twisted-moment theorem.

The direct extension of L383's absolute height-rectangle bounds gives
only O_N(H^2) for the unnormalized k=1 integral, against the needed
o(H ell^4). It therefore fails to certify its neglect at the leading
scale. This is a failure of that bound, not a lower bound on the
integral, a disproof of the proposed asymptotic, or proof that the
harmonic contributes to its leading coefficient. No beta is obtained.

## Proof

This is a local REPRODUCTION of the existing polynomial, ordinary
carrier differentiation and moment-norm estimates. The prior EXPLORE
assessment is `drafts/literature/2026-10-10-discriminant-second-moment-leading-scale.md`.
No new moment theorem is imported or claimed. The family-specific
reduction is necessary because the earlier contour result has two
critical factors, whereas (2) has four.

### Complete leading-jet replacement

L389's Hardy identification and its proof of (6), importing Bui--Hall,
*On the derivatives of Hardy's function Z(t)*,
[arXiv:2304.05178v1, Theorem 3 and its defining asymptotic](https://arxiv.org/html/2304.05178v1),
give for j=0,1,2

    H^(-1) integral |f^(j)/L^j|^4 = O(ell^4).

Consequently ||U||_(2,H)=O(ell^2). This uses fixed orders only and
holds on the sharp interval by restriction of the nonnegative moment.

Put g=G/A=Re(R b Z), with the exact polynomial b of L368 (3).
On the positive ray its complete series and derivatives satisfy
|Z^(j)|<=M_j for j<=2. The controlled gamma formulas of L368 give

    b/T^2=c+O(1/t), b'=O(t), b''=O(1),
    phi'/L=1/2+O(1/L), phi''=O(1/t).

Here phi is the phase of Q, not Qb: subtracting the explicitly bounded
phase derivatives of b in L368 (8) gives the stated estimates. These
are estimates for separate exact derivatives, not derivatives of an
unspecified remainder. Direct differentiation gives

    (RbZ)'=R(i phi' bZ+b'Z+bZ'),
    (RbZ)''=R(((i phi''-phi'^2)b+2i phi'b'+b'')Z
                   +(2i phi'b+2b')Z'+bZ'').

It follows, uniformly and with the infinite series retained, that
v_j=g^(j)/(T^2 L^j) have leading values

    (v_0,v_1,v_2)=(c a,-c h/2,-c a/4)+O(1/L),
    a=Re(RZ), h=Im(RZ).                              (4)

All actual and leading v_j are uniformly bounded. T^2 and L^j are
pointwise divisors here; no derivative of a divisor is dropped.

L370's common-envelope identity is exactly

    Delta=Q_0(x,y,z;v_0,v_1,v_2)+4q/L^2 (xv_1-yv_0)^2,
    Q_0=(xv_2-zv_0)^2-4(xv_1-yv_0)(yv_2-zv_1),
    q=(log A)''=O(T^(-2)).                           (5)

Because Q_0 is quadratic in each jet triple, replacing the bounded
response triple using (4) changes it by at most C U/L. The retained
curvature term is at most C U/(T^2 L^2). Therefore the total error
has norm O(ell), including at all zeros of either original function.

For a direct algebra check put u=c a, v=-c h/2. Substitution of the
leading triple (u,v,-u/4) into Q_0 gives

    [(z+x/4)^2-y^2]u^2 + y(x-4z)uv +4xz v^2.

Writing A_0=(z+x/4)^2-y^2, this is

    c^2[A_0 a^2-y(x-4z)ah/2+xz h^2].

The coefficient of |RZ|^2 is (A_0+xz)/2=M. The complex coefficient
of (RZ)^2 is

    (A_0-xz)/2+i y(x-4z)/4
       =((z-x/4)-iy)^2/2=K.

This proves the formula for d and the first bound in (1).
Since |M|+|K|<=C U and Z is uniformly bounded, ||d||_(2,H)=O(ell^2).
The same bound for Delta follows either by addition or L389.
Cauchy--Schwarz applied to (Delta-d)(Delta+d) gives the last bound
in (1), with all endpoints retained.

### Projection and full-tail checks

Squaring M|Z|^2+Re(K E Z^2), using M real, |E|=1 and
(Re w)^2=(|w|^2+Re(w^2))/2, proves (2) exactly. For example the
formal real jet x=1,y=z=0 gives M=K=1/32, so its k=1 coefficient
2MK=1/512 is not the zero polynomial. This algebraic check does
not assert that this jet occurs for actual f or rule out cancellation
in the height integral.

The absolute series gives |Z-Z_N|<=eta_N, with |Z|,|Z_N|<=M_0.
Thus |d-d_N|<=C eta_N U, while |d|+|d_N|<=C U. Taking the norms
and then Cauchy--Schwarz proves (3). Since eta_N tends to zero,
these are uniform leading-scale bounds before the head limit.
The discarded derivative series were already retained in the error
in (4); no derivative tail is silently set to zero in this passage.

### The unmatched contour case

It suffices to test a fixed N, so every expanded right-line head
product gives a fixed rational twist, bounded on the closed height
strip |Im tau|<=1 with constants depending on N. Extend L(t) there
by Log(2+tau), nonzero for large Re tau. Use the holomorphic E and
its root R from L383 (13)--(15). Exactly on this rectangle,

    f=-R U_+=-R^(-1)U_-,
    U_+(tau)=zeta(1/2+i tau),
    U_-(tau)=zeta(1/2-i tau),
    |E(x+iy)| asymp H^(-y).                          (6)

Ordinary differentiation represents each f^(j)/L^j, j<=2, as
R^(-1) times a linear combination of U_-^(r)/L^r, r<=j. The
coefficients are uniformly bounded: R'/R=i Omega=O(ell) and
Omega'=O(1/H), from the separately controlled polygamma formulas.
The alternative positive-height representation is equally valid.

The polynomial MK is homogeneous of degree four in these f jets.
In the k=1 complex term of (2), representing all four factors by
the negative-height version leaves carrier

    E R^(-4)=E^(-1).                                (7)

Thus the upper rectangle has the *growing* carrier H^y. L381 (18)
on circles of radius 1/ell, extended by Cauchy's formula through
order two, bounds each selected normalized zeta jet by
C H^(1/2-y/2), 0<=y<=1. The coefficients just described and fixed
twists are bounded. Multiplying all four estimates and (7) yields

    C_N H^y H^(2-2y)=C_N H^(2-y).

Its integral over either vertical edge is
C_N(H^2-H)/log H=O_N(H^2/ell). On the upper horizontal edge,
all U_- jets are on real part 3/2 and bounded by their absolute
series, while E^(-1)=O(H). The edge has length H, giving O_N(H^2).
All factors are holomorphic: poles have real height zero and no
chosen logarithm crosses its cut. Thus there are no missing residues
or ignored connectors. The conjugate k=-1 term has the reflected
lower-rectangle bounds. Reflecting only some critical factors cannot
remove this issue: (6) makes that change an exact functional-equation
identity; no balanced theorem with a slow weight follows from it.

For comparison the k=2 carrier after the same reflection is
E^2 R^(-4)=1. Its horizontal estimate is O_N(H), but the same
coarse four-factor vertical estimate is still O_N(H^2/ell).
This additional endpoint budget is not silently treated as solved.
The k=0 term admits a balanced representation with two factors of
each orientation; the previously inspected Hughes--Young Theorem 1.1
is the appropriate source for its fixed-twist smooth moments, but no
coefficient application or sharp transfer is asserted here.

The displayed k=1 absolute budget divided by the required H ell^4
is of order H/ell^4 and does not tend to zero. This compares the
available error certificate with the threshold; it is emphatically
not a lower bound on the true integral or even the optimal bound
from all possible contour methods. Polynomial cancellation, signed
horizontal analysis or a separate unequal-orientation moment input
might improve it. They have not been proved in this attempt. In
particular real-part cancellation between the two conjugate terms
must not be assumed. The approved test therefore stops before beta
calculation, preserving (1)--(3) as partial inputs.

### Separate critical audit — 2026-10-11

The prior SPECIALIZE assessment
`drafts/literature/2026-10-10-signed-k1-projection-audit.md` includes
this physical input to L391. The following REPRODUCTION audit verifies
(1)--(3) and the scope of the stopped absolute certificate. No hypothesis,
conclusion or mathematical input is changed.

**Complete response and envelope.** In L368 (3), exactly
b=(t^2/4-3/16-it/2)/pi. Thus b/T^2=c+O(1/t),
b'=(t/2-i/2)/pi and b''=1/(2pi). If phi is the phase of Q,
phi'=Re Psi(1/4+it/2)/2-(log pi)/2 and
phi''=-Im Psi'(1/4+it/2)/4. The separately controlled expansions
used in L368 give phi'/L=1/2+O(1/L) and phi''=O(1/t).
The absolutely convergent full Z series supplies |Z^(j)|<=M_j
for j=0,1,2. In the two displayed product derivatives above, the
terms b'Z/(T^2 L) and bZ'/(T^2 L) cost O(1/(tL)) and O(1/L).
In the second derivative, the leading term is -phi'^2 bZ/(T^2 L^2);
the phi'' term costs O(1/(tL^2)), the phi'b' term O(1/(tL)),
the b'' term O(1/(t^2L^2)), the phi'bZ' term O(1/L),
and the b'Z', bZ'' terms O(1/(tL^2)), O(1/L^2).
These bounds give exactly (4), uniformly on the ray. They include
every response derivative, without truncating a series or differentiating
the pointwise divisors.

For the normalized ordinary minors, write
a_1=xv_1-yv_0, a_2=xv_2-zv_0, a_3=yv_2-zv_1.
The unnormalized minors of f,g are respectively T^2 L a_1,
T^2 L^2 a_2 and T^2 L^3 a_3. Substitution in L370 (4) therefore
gives exactly (5), including the plus sign and factor 4q/L^2.
This uses g=G/A before differentiating. A change O(1/L) in its
bounded normalized triple changes each minor by O(sqrt(U)/L).
Products of two minors consequently change by O(U/L), and the
curvature term is O(U/(T^2 L^2)). These estimates hold when any
jet vanishes.

**Polynomial and square.** For response triple (u,v,-u/4), the
three minors become xv-yu, -(z+x/4)u, and -yu/4-zv.
Their discriminant is
[(z+x/4)^2-y^2]u^2+y(x-4z)uv+4xzv^2.
With u=ca, v=-ch/2 this gives the displayed physical polynomial.
Since Re[(A+iB)(a+ih)^2]=A(a^2-h^2)-2Bah,
its complex coefficient has real part (A_0-xz)/2 and imaginary
part y(x-4z)/4, exactly the stated K. This checks the sign of the
mixed ah term as well as M. Squaring the real expression gives all
three terms in (2), with no missing conjugate or factor two.
The formal jet (1,0,0) checks the nonzero coefficient but plays no
role as an actual-function premise.

**Norms and complete tails.** L389 (3), (6) identifies f with a
constant sign times the ordinary Hardy function and imports Bui--Hall,
arXiv:2304.05178v1, Theorem 3, as cited above. Its nonnegative
fourth-moment restriction gives integral U^2/H=O(ell^4), using
U^2<=3(x^4+y^4+z^4). Consequently the pointwise O(U/L) error
has norm O(ell), whereas d and Delta have norms O(ell^2).
Schwarz gives exactly O(ell^3) for the square-mean difference.
All constants are fixed for all sufficiently large real H.

Let M_0=zeta(5/2). Both |Z| and |Z_N| are at most M_0, so
||Z|^2-|Z_N|^2|<=2M_0 eta_N and
|Z^2-Z_N^2|<=2M_0 eta_N. Together with |E|=1 and
|M|+|K|<=CU these prove the uniform pointwise tail inequality
in the original proof. Its two norm consequences (3) follow without
a constant depending on N. The response derivative errors are already
included in (4), so this last replacement concerns only values of Z.

**Earlier failed certificate.** The negative-height representation of
four critical factors supplies R^(-4)=E^(-2). The k=1 carrier is
therefore E^(-1), of size H^y on the upper rectangle. The inherited
four jet bounds give H^(2-2y), and their product gives H^(2-y).
The stated connector and horizontal budgets follow, respectively
O_N(H^2/ell) and O_N(H^2). The k=2 carrier cancels instead, but
that same coarse endpoint certificate still exceeds the required
scale. This verifies what failed, not a lower bound for either actual
integral. L391's separately audited signed implementation can coexist
with this historical failure; no part of (1)--(3) depends on that failure.

The physical reduction and full-tail transfer pass unchanged. This
audit imports the already inspected moment theorem and checks its
application; it is not a new four-factor theorem or a beta evaluation.

## Mathlib

Full matching four-factor actual discriminant reduction/moment
coverage is not checked. Polynomial identities, Cauchy--Schwarz and
holomorphic contour support would not establish the missing moment.
No Lean verification, library absence or novelty beyond the checked
sources is claimed. This result is not an RH candidate and does not
change the established positivity or zero-exclusion ranges.
