# Lemma 395: short-mollifier physical discriminant and response-tail transfer

## Hypotheses

Use the fixed actual functions and ordinary derivatives of L390, including
F=F_0, G, the positive envelope A, f=F/A, T=1+t, L(t)=log(2+t),
R=Q/A, E=R^2, the physical normalization Delta and its leading expression
d. In particular set

    x=f, y_jet=f'/L, z=f''/L^2, U=x^2+y_jet^2+z^2,
    M=(z^2+3xz/2+x^2/16-y_jet^2)/2,
    K=((z-x/4)-i y_jet)^2/2,
    Z_+=zeta(5/2+it), c=1/(4 pi),
    d=c^2 (M |Z_+|^2 + Re(K E Z_+^2)).

For every real H>1 put ell=log H, Y=H^(1/100), and

    P_H(t)=sum_(n<=Y) mu(n)n^(-1/2-it)(log(Y/n)/log Y)^2.

Here Y is the mollifier length and y_jet is an ordinary normalized jet;
they are different quantities. For every integer N>=1 let
Z_(+,N)=sum_(n<=N)n^(-5/2-it), let d_N replace Z_+ in d by
Z_(+,N), and put eta_N=sum_(n>N)n^(-5/2).

No RH, zero simplicity, noncoincidence, phase independence, discriminant
sign, or common-zero estimate is assumed. H is real and tends to infinity;
the critical-jet derivative orders and exponent 1/100 are fixed.

## Conclusion

There are finite constants C>0 and H_0>=40, independent of N and H,
such that for every real H>=H_0 and every integer N>=1,

    (1/H) integral_[H,2H] U |P_H|^2 <= C,                    (1)
    (1/H) integral_[H,2H] |Delta-d| |P_H|^2 <= C/log H,      (2)
    (1/H) integral_[H,2H] |d-d_N| |P_H|^2 <= C eta_N.        (3)

All integrals are sharp, with their actual endpoints. Constants and onset
are existential, not numerically evaluated. Thus the limsup tail threshold
in the approved target follows from the stronger uniform bound (3).
In particular the signed weighted means of Delta and d differ by o(1),
and the limsup difference between those of d and d_N is at most C eta_N.
One may first take H to infinity at fixed N, then N to infinity in this
absolute comparison. No existence or value of a signed mean limit, fixed-
head coefficient formula, growing-twist carrier bound, positive witness,
eventual sign, zero-count estimate, extended positivity range or RH follows.

## Proof

This is a local REPRODUCTION under the prior SPECIALIZE assessment
`drafts/literature/2026-10-11-mollified-physical-transfer.md`.
The scalar moment theorem is imported, not reproved. The application is
needed because L390's unweighted norms do not control this growing weight.

### Scalar input and ordinary Hardy jets

Import H. M. Bui and R. R. Hall, *On the derivatives of Hardy's function
Z(t)*, arXiv:2304.05178v1 (11 April 2023),
[mollifier definition, Proposition 1 and Section 3 (6)–(8)](https://arxiv.org/html/2304.05178v1#S3),
printed pp. 6–8. Proposition 1 applies on sharp [H,2H] to fixed real
polynomials Q_1,Q_2, P(0)=0, and fixed 0<vartheta<4/7. Take
vartheta=1/100, P(u)=u^2, and Q_1(X)=Q_2(X)=X^r, r=0,1,2
(X^0=1). Its left side is the weighted squared modulus of
zeta^(r)(1/2+it)/ell^r. Its finite constant and O(1/ell) error give

    (1/H) integral_[H,2H] |rho_r|^2 |P_H|^2 <= B_r,
    rho_r(t)=zeta^(r)(1/2+it)/ell^r.                       (4)

The conjugate factor is the complex s-derivative at 1/2-it, so no
ordinary-height derivative sign enters (4). All hypotheses hold:
P(0)=0, P(1)=1, and 0<1/100<4/7. There are only three fixed
polynomial choices, so one fixed onset works for all of them.

Write Hcal(t)=e^(i theta(t))zeta(1/2+it) for the real Hardy function;
this notation avoids confusion with H and with Z_+. The gamma carrier
of L366 is Q=(t^2+1/4)Gamma(1/4+it/2)pi^(-1/4-it/2).
Gamma conjugation and positivity of t^2+1/4 give

    R^2=pi^(-it)Gamma(1/4+it/2)/Gamma(1/4-it/2)
       =e^(2i theta(t)).

Hence R/e^(i theta) is one constant sigma in {1,-1} on the connected
positive ray. Both factors are continuous and nonzero; no division by
zeta is made. The exact identity f=-R zeta(1/2+it) of L390 gives
f=-sigma Hcal, with the same constant sign for every ordinary derivative.
This identification is valid at zeros as well.

For clarity the ordinary jet conversion can be checked by exact product
differentiation. Set h=theta'/ell. On this dyadic interval, (6) of the
source (also L390's controlled carrier estimates) gives
theta'=ell/2+O(1), theta''=O(1/H). Thus h is uniformly bounded and
h=1/2+O(1/ell). The exact formulas are

    Hcal=e^(i theta) rho_0,
    Hcal'/ell=i e^(i theta)(rho_1+h rho_0),
    Hcal''/ell^2=e^(i theta)(-rho_2-2h rho_1-h^2 rho_0
                                      +i theta'' rho_0/ell^2).    (5)

In particular the second derivative has the minus sign i^2=-1.
Its theta'' term is retained. These formulas give the leading
i^j e^(i theta)(1/2+X)^j operator of source (7); the omitted-from-leading
terms are bounded by C ell^(-1) sum_(r<=j)|rho_r| for j<=2.
Using (4), their weighted L2 norm is O(1/ell), consistent with the
source's Schwarz error control in (8). We need only the upper bounds:
bounded coefficients in the exact formulas (5), (4), and
|sum_(r=1)^m a_r|^2<=m sum_(r=1)^m |a_r|^2 show

    (1/H) integral_[H,2H] |f^(j)/ell^j|^2 |P_H|^2 <= B
                    for j=0,1,2,                           (6)

with a single fixed B. This does not differentiate P_H. No smooth
endpoint replacement or signed bracketing is used.

Pointwise L(t)>=ell on [H,2H]. Therefore |f^(j)/L(t)^j|^2 is at
most |f^(j)/ell^j|^2. Applying this nonnegative inequality separately
to (6), then adding the three bounds, proves (1). In particular no
asymptotic remainder in L or in a carrier derivative is differentiated.

### Complete physical error

Here we use the pointwise proof and physical audit in L390, rather than
its unweighted L2 conclusion. With g=G/A and
v_j=g^(j)/(T^2 L^j), the complete response triple is uniformly bounded,
and differs from

    (c Re(RZ_+), -c Im(RZ_+)/2, -c Re(RZ_+)/4)

by O(1/L), through ordinary order two. The full absolute derivative
series |Z_+^(j)|<=sum n^(-5/2)(log n)^j, j<=2, supplies fixed constants;
no head N is used here. L390's exact common-envelope identity is

    Delta=(xv_2-zv_0)^2
           -4(xv_1-y_jet v_0)(y_jet v_2-zv_1)
           +(4q/L^2)(xv_1-y_jet v_0)^2,
    q=(log A)''=O(T^(-2)).                               (7)

The first two terms evaluated at the leading triple give d. Every
minor is O(sqrt(U)); its change is O(sqrt(U)/L). Products of minors
therefore change by O(U/L), uniformly at zeros too. The last term,
retained with its sign and factor four, is O(U/(T^2 L^2)). Consequently

    |Delta-d| <= C_0 U/L                               (8)

for one fixed constant C_0 on an eventual ray. This is precisely L390's
pointwise physical bound, including complete response derivatives and
envelope curvature. Multiplying by the nonnegative |P_H|^2, integrating,
and using L>=ell and (1) proves (2).

### Uniform complete-response tail

The absolute series gives |Z_+|,|Z_(+,N)|<=zeta(5/2)=B_0 and
|Z_+-Z_(+,N)|<=eta_N for every N and every real t. Thus

    ||Z_+|^2-|Z_(+,N)|^2| <= 2B_0 eta_N,
    |Z_+^2-Z_(+,N)^2| <= 2B_0 eta_N.

The displayed quadratic polynomials satisfy |M|+|K|<=B_1 U for one
absolute constant B_1, and |E|=1. It follows that

    |d-d_N| <= C_1 eta_N U,                            (9)

where C_1 is independent of N. This is a value replacement in the
leading expression: all physical response derivatives have already
been accounted for in (8), and no differentiated tail is dropped.
Integration of (9) against |P_H|^2 and (1) proves (3).
Taking the maximum of these fixed constants and onsets proves the
claimed simultaneous uniformity. Integral triangle inequalities give
the stated signed-mean comparisons, without asserting those means' signs
or limits. All three approved thresholds are met; the independent
carrier and coefficient calculations remain unresolved.

### Separate critical audit — 2026-10-11, step 61

The prior SPECIALIZE assessment
`drafts/literature/2026-10-11-mollified-physical-transfer-audit.md`
authorizes this independent REPRODUCTION audit of (1)–(3).
All three conclusions pass without changing hypotheses or mathematical
inputs. The checks below establish usability of this specialization,
not a new scalar moment theorem or a signed-mean evaluation.

**Scalar convention and sharp interval.** Directly rechecked the cited
Bui–Hall v1 mollifier definition, Proposition 1 and (6)–(8). Its two
operators differentiate independent complex shifts alpha and beta in
zeta(1/2+alpha+it) zeta(1/2+beta-it). For Q_1=Q_2=X^r their product at
zero is |zeta^(r)(1/2+it)|^2/ell^(2r), by conjugation of the analytic
zeta function and its complex derivatives. There is no factor (-1)^r:
beta is not the real height variable. The actual P_H is precisely the
source mollifier with fixed exponent 1/100 and polynomial u^2.
The three finite source constants and error bounds give (4) for real
H beyond one maximum of three onsets, already on [H,2H]. No smoothing,
new derivative-moment theorem or interchange with a height limit is used.

**Hardy identification and derivatives.** L366 (1) says
F=-Re(Q zeta(1/2+it)). Since A=|Q|>0 and
R^2=e^(2i theta), the continuous nonzero quotient R/e^(i theta) is a
constant sigma in {1,-1}. Thus Q zeta/A=sigma Hcal is real, which
justifies replacing the real part and gives exactly f=-sigma Hcal.
This argument neither divides by zeta nor changes sign across its zeros.
For fixed H, ell is constant under ordinary height differentiation.
Applying d/dt to e^(i theta) zeta gives the factor i on both theta'
and the complex zeta derivative. A second application gives coefficients
-1, -2 theta', -theta'^2 and +i theta'' on zeta'', zeta', zeta and
zeta, respectively, exactly (5) after division by ell^2.
The bounds on theta' and theta'' in source (6) make every coefficient
uniformly bounded, so the elementary square-of-a-sum inequality and (4)
give (6). The positive comparison ell/L(t)<=1 proves (1) without
differentiating L or P_H. Every bound remains valid at vanishing jets.

**Physical normalization and complete response.** Rechecked L390's
exact identity against the ordinary minors and positive-envelope
normalization in L370. If a_1=xv_1-y_jet v_0,
a_2=xv_2-zv_0 and a_3=y_jet v_2-zv_1, the corresponding minors of f,g
are T^2 L a_1, T^2 L^2 a_2 and T^2 L^3 a_3.
The common-envelope cancellation therefore gives
a_2^2-4a_1a_3+4q a_1^2/L^2, with the plus sign and factor four in (7).
In L390's exact response derivative formulas, b/T^2=c+O(1/t),
phi'/L=1/2+O(1/L), and all three complete Z_+ derivative series
are bounded. The b', b'', phi'' and Z_+' and Z_+'' terms are all
included in its O(1/L) normalized response error; no derivative of an
asymptotic remainder is needed. Its onset has no dependence on N.

For an independent polynomial check, writing a=Re(RZ_+) and h=Im(RZ_+),
the leading triple gives

    c^2 {[(z+x/4)^2-y_jet^2] a^2
          -y_jet(x-4z) a h/2 + xz h^2}.

Its |RZ_+|^2 coefficient is M, and its (RZ_+)^2 coefficient is K:
the imaginary part of K is y_jet(x-4z)/4, whose real projection gives
the displayed mixed term. This confirms the complete d in (8).
Each minor has size at most C sqrt(U) and changes by at most
C sqrt(U)/L; expanding products gives an error at most C U/L.
The retained curvature contributes at most C U/(T^2 L^2), which is
absorbed for t>=40. Multiplying this pointwise inequality by |P_H|^2
and using (1) gives (2); an unweighted norm alone would not do so.

**Tail constants and order of limits.** The two quadratic response
differences are bounded by 2 zeta(5/2) eta_N for every N and t.
For instance |M|+|K|<=2U follows directly from 2|xz|<=x^2+z^2
and (z-x/4)^2<=2z^2+x^2/8. Thus (9) holds with
C_1=4c^2 zeta(5/2), independently of N, before integration.
Only the response values are replaced here; all response derivatives
were handled in (8). If C_U bounds (1) and C_0 is the fixed physical
constant in (8), one may take
C=max(C_U,C_0 C_U,C_1 C_U), enlarging the onset only for the three
scalar moments and the fixed physical estimates. This verifies the
simultaneous quantifiers in (1)–(3), including arbitrarily small or
large fixed N. No interchange of the H and N limits is required.

The audit finds no missing hypothesis or error at the approved scale.
The complete mollified carrier and coefficient remain uncomputed; a
tail comparison cannot assert existence, positivity or even a value of
their signed mean. Eventual sign, total pencil margin, common-zero
upper bounds and global mixed positivity remain independent gaps.

## Mathlib

Full matching mollified ordinary-jet moment and physical-discriminant
transfer coverage is not checked. No Lean verification or library absence
is claimed. Elementary product differentiation and integral inequalities
would support the application but would not replace the imported analytic
moment theorem. This is a known-source specialization, not a new scalar
moment theorem or an RH candidate. The separate step 61 audit validates
(1)–(3) with unchanged hypotheses and conclusions.
