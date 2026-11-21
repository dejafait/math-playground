# Lemma 728: compact triangular Mobius contour identity, with corrected trivial-zero term

## Hypotheses

Use the actual Riemann zeta function and zero correspondence of L018.
Fix an integer N>=2, put ell=log N, and let K be a compact subset of

    {s in C : 0<Re(s)<1 and zeta(s)!=0}.

All powers of the positive number N use its real logarithm. Define

    V_N(s)=sum_(1<=n<=N) mu(n)*(1-log(n)/ell)*n^(-s),
    g_s(z)=N^(z-s)/(zeta(z)*(z-s)^2),
    R_N(rho,s)=Res_(z=rho) g_s(z).

Here rho runs over distinct nontrivial zeros, with its entire
multiplicity included in the residue. No RH, simplicity, bound on
1/zeta'(rho), or moment hypothesis is assumed.

## Conclusion

There is an increasing sequence H_j tending to infinity such that

    S_N(s)=lim_(j->infinity) sum_(|Im(rho)|<H_j) R_N(rho,s)          (1)

exists uniformly on K, and

    V_N(s)=1/zeta(s)-zeta'(s)/(ell*zeta(s)^2)
           +(S_N(s)+T_N(s))/ell,                                (2)

where the trivial-zero series is absolutely and uniformly convergent
on K and equals

    T_N(s)=sum_(k>=1) N^(-2k-s)/(zeta'(-2k)*(2k+s)^2)
          =N^(-s)/pi * sum_(k>=1)
             (-1)^k*(2pi)^(2k+1)*N^(-2k)
             /((2k)!*zeta(2k+1)*(2k+s)^2).                       (3)

The heights can be selected independently of N,K from Inoue's good
heights; the estimates below hold for all sufficiently large j for
each fixed K,N. Any such good-height sequence has the same limit.
The convention in (1) is essential: this proof asserts neither
absolute convergence of individual nontrivial-zero residues nor
convergence with arbitrary height cutoffs or rearrangements.

Formula (2) is the compact specialization of BCF Lemma 2, with a
normalization repair: its v1 display for F_s has prefactor pi, whereas
its own displayed value of zeta'(-2k) requires 1/pi, as in (3).
Only the positive argument 1/N is used; no entire dependence on the
argument of a factor x^s is asserted.

All uniformity here is for fixed N and compact K away from zeros.
There is no full-line L2 interchange, no estimate tending to zero as
N grows for the mollifier norm, no sign conclusion and no RH claim.

## Proof

### 1. Precise imports and reason for the audit

S. Bettin, J. B. Conrey and D. W. Farmer, *An optimal choice of
Dirichlet polynomials for the Nyman-Beurling criterion*,
[arXiv:1211.5191v1, 22 November 2012](https://arxiv.org/pdf/1211.5191v1),
Lemma 2 and proof, printed p. 6, give this residue identity. The
limiting convention and horizontal estimates are not specified there.
The printed trivial-zero normalization also needs the correction in
Section 4 below. These are the reasons for supplying the following
applicability proof, not a claim of a new explicit-formula method.
BCF Lemma 3 and Theorem 1 have additional RH/simplicity/negative-moment
hypotheses and are not imported.

Shota Inoue, *Some explicit formulas for partial sums of Mobius
functions*, Journal de Theorie des Nombres de Bordeaux 33 (2021),
273--315, [doi:10.5802/jtnb.1162](https://www.numdam.org/item/10.5802/jtnb.1162.pdf),
Proposition 1, p. 279, supplies the following unconditional input.
For alpha>=13, T>=T0(alpha), and 1<=Q<=(log T)^(alpha/4), some
H in [T,2T] satisfies the stated reciprocal bound simultaneously for
1/2<=sigma<=2 and primitive characters with modulus at most Q.
Take alpha=13,Q=1. The character of conductor one has L=zeta, so

    sup_(1/2<=sigma<=2) |1/zeta(sigma+iH)|
       <= B(T):=exp(C_0*(log log T)^2).                           (4)

Conjugation gives the same estimate at -H. Fix a sufficiently large
T_* and apply (4) with T_j=3^j*T_*, obtaining H_j in [T_j,2T_j].
These heights are increasing. Functional equation reflection makes
both horizontal lines free of zeta zeros also for Re(z)<1/2.
In particular no nontrivial zero lies at either ordinate +/-H_j.

We also import the functional-equation lower estimates in Inoue
Lemma 2, p. 288, (4.6)--(4.7). With A=2pi*e and q=1 their reciprocal
forms give, wherever the reflected zeta factor is nonzero, for
z=sigma+it, sigma<=1/2, |t|>=1,

    |1/zeta(z)| <= C*(A/|z|)^(-sigma)*|z|^(-1/2)
       *exp(-|t|*atan((1-sigma)/|t|))*|1/zeta(1-z)|.              (5)

For |t|<=1 and sigma=-a, a=m+1/2, m a positive integer, they give

    |1/zeta(-a+it)|
       <= C*(A/|-a+it|)^a*a^(-1/2)*|1/zeta(1+a-it)|.             (6)

Only these lower estimates and (4) are needed from Inoue. Their
use follows the edge cases of his Theorem 4 proof, pp. 297--298,
but our kernel has (z-s)^(-2), and s ranges over K. Constants in
(5)--(6) are absolute here. The absolutely convergent Euler product
gives |1/zeta(u+iv)|<=zeta(u) for u>1. The standard functional
equation for zeta, also underlying (5), is used at trivial zeros.
These named inputs are cited, not reproved arithmetic results.
Every use of (5)--(6) below has a nonzero reflected factor: either
(4) and conjugation apply on [1/2,2], or its real part is at least
2 and the Euler product applies. Thus reciprocation never assumes
zero-freeness in an unproved region.

An empty K is vacuous. Otherwise, for the rest of the proof write

    delta=min_(s in K) Re(s)>0,
    b=max_(s in K) Re(s)<1,
    B_0=max_(s in K) |Im(s)|.

Take H=H_j>max(2B_0+2,2A,2). All estimates are uniform for s in K.

### 2. The right edge and the integer endpoint

The integral

    I_infinity(s)=(1/(2pi*i))*integral_(2-i infinity)^(2+i infinity)
                   g_s(z) dz

is absolutely convergent. On Re(z)=2 the numerator has modulus
N^(2-Re(s)), |1/zeta(z)|<=zeta(2), and

    integral_R dt/|2+it-s|^2=pi/(2-Re(s))<=pi/(2-b).

Consequently the absolutely convergent expansion
1/zeta(z)=sum_(n>=1) mu(n)n^(-z) can be integrated termwise,
uniformly for s in K. With w=z-s each term is n^(-s) times

    (1/(2pi*i))*integral_(c-i infinity)^(c+i infinity) x^w/w^2 dw,
    c=2-Re(s)>0, x=N/n.

This integral is log x for x>1 and zero for 0<x<=1. For completeness,
shift first to Re(w)=-R when x>1, or to Re(w)=R when x<1,
sending the horizontal heights to infinity at fixed R. Their
integrals vanish as O_R(height^(-2)); the new vertical integral has
absolute value at most x^(-R)/(2R), respectively x^R/(2R), and
tends to zero as R grows. The only crossed residue in the first
case is log x at w=0. When x=1, the antiderivative -1/w gives
zero directly on the infinite vertical line. Thus the n=N term is
exactly zero, without a half-endpoint contribution. It follows that

    I_infinity(s)=sum_(n<N) mu(n)n^(-s)*log(N/n)=ell*V_N(s).       (7)

Let I_H be the right-edge integral truncated to ordinates [-H,H]
in the z variable. Since |t-Im(s)|>=|t|/2 for |t|>=H,

    sup_K |I_H-I_infinity| <= C_(K,N)/H.                         (8)

The shift of imaginary origins w=z-s therefore causes no endpoint
or height-selection ambiguity.

### 3. A finite rectangle, including all multiplicities

For a=m+1/2, m>=1, use the rectangle with vertical edges -a and 2
and ordinates +/-H. Normalize every integral by 1/(2pi*i).
Let U_(a,H) be the top edge from 2+iH to -a+iH; L_(a,H) the
left edge oriented upwards; and D_(a,H) the bottom edge from
-a-iH to 2-iH. The residue theorem, with positive orientation, is

    I_H+U_(a,H)-L_(a,H)+D_(a,H)
       =A_N(s)+S_(N,H)(s)+T_(N,a)(s),                          (9)

where

    A_N(s)=ell/zeta(s)-zeta'(s)/zeta(s)^2,
    S_(N,H)(s)=sum_(|Im(rho)|<H) R_N(rho,s),
    T_(N,a)(s)=sum_(k>=1, 2k<a)
                N^(-2k-s)/(zeta'(-2k)*(2k+s)^2).

The residue A_N is the derivative at z=s of N^(z-s)/zeta(z).
If rho has multiplicity m_rho, put
h_rho(z)=(z-rho)^(m_rho)/zeta(z), holomorphic near rho. Then

    R_N(rho,s)=1/(m_rho-1)! *
       [d^(m_rho-1)/dz^(m_rho-1)
         (h_rho(z)*N^(z-s)/(z-s)^2)]_(z=rho).                  (10)

This includes every multiplicity and does not divide by zeta'(rho)
unless m_rho=1. There are finitely many nontrivial zeros in (9).
By L018 they all have 0<Re(rho)<1, so their set in this rectangle
is independent of a. The other zeros are the simple zeros -2k.
The reciprocal of zeta has a zero, not a pole, at z=1; it is
regular at z=0. Thus (9) contains every residue and no extraneous
one. Since K excludes zeta zeros, z=s never coincides with a rho.

### 4. Trivial residues and the normalization repair

The functional equation

    zeta(z)=2^z*pi^(z-1)*sin(pi*z/2)*Gamma(1-z)*zeta(1-z)

at z=-2k gives

    zeta'(-2k)=(-1)^k*pi*(2k)!*zeta(2k+1)/(2pi)^(2k+1).

This is also the derivative formula printed in BCF's proof.
Reciprocating it gives precisely (3). In particular k=1 yields

    zeta'(-2)=-zeta(3)/(4pi^2),
    Res_(z=-2) g_s(z)=-4pi^2*N^(-2-s)/(zeta(3)*(2+s)^2).

The printed prefactor pi in BCF's F_s would instead give -4pi^4
in the last numerator. The discrepancy is a factor pi^2 in that
display, not a contour sign or a zero-multiplicity convention.
We use the residue definition (3) throughout.

Each term of (3) has absolute value at most

    2*N^(-delta)*(2pi/N)^(2k)/((2k)!*(2k+delta)^2),

because zeta(2k+1)>1. This is summable for fixed N, proving absolute
uniform convergence and T_(N,a)->T_N uniformly on K. Only real
logarithms of positive N occur, so no branch choice is hidden here.

### 5. Far-left edge at fixed height

For a>=3/2, |1/zeta(1+a-it)|<=zeta(1+a)<=zeta(2). Formula (5)
for 1<=|t|<=H, and (6) for |t|<=1, give on Re(z)=-a

    |1/zeta(-a+it)|<=C*(A/a)^a*a^(-1/2).

Here the exponential factor in (5) is at most one and |z|>=a.
Also |z-s|>=a+delta and |N^(z-s)|<=N^(-a-delta). Therefore

    sup_K |L_(a,H)|
       <=C*H*N^(-delta)*(A/(N*a))^a*a^(-5/2) -> 0             (11)

as a tends to infinity through the chosen half integers, for each
fixed H. No estimate uniform in growing H is inferred from (11).

### 6. Both horizontal edges

Throughout either edge, |z-s|>=H-B_0>=H/2. On 1/2<=sigma<=2,
(4) and conjugation give |1/zeta(sigma+/-iH)|<=B(T_j).
On -1<=sigma<=1/2, reflect by (5); 1-sigma lies in [1/2,2],
so the same good-height estimate applies. Since |sigma|<=1 and
|z| is comparable to H on this interval, (5) implies

    |1/zeta(sigma+/-iH)|
       <=C*B(T_j)*H^(sigma-1/2)<=C*B(T_j).

The portions with -1<=sigma<=2 therefore contribute at most

    C_(K,N)*B(T_j)/H^2                                       (12)

on each edge. This estimate uses the squared, shifted kernel itself.

For sigma=-r<=-1, the reflected reciprocal is bounded by zeta(2).
Dropping the nonpositive exponential in (5) and using |z|>=H gives

    |1/zeta(-r+/-iH)|<=C*(A/H)^r*H^(-1/2).

Thus, uniformly in the finite left endpoint a, the absolute integral
over its remaining horizontal portion is at most

    C*N^(-delta)*H^(-5/2)*integral_1^infinity (A/(N*H))^r dr
      =C*N^(-delta)*H^(-5/2)
         *[A/(N*H)]/log(N*H/A).                              (13)

Here N*H>A by the stipulated threshold. In particular the infinite
horizontal integrals U_H,D_H exist absolutely as a tends to infinity,
uniformly on K. Explicitly, for a'>a>=1 the difference of the
integrals ending at -a' and -a is bounded by

    C*N^(-delta)*H^(-5/2)*(A/(N*H))^a/log(N*H/A).

At fixed H this tends to zero uniformly on K, since A/(N*H)<1.
Both limiting edges satisfy the sum of the bounds (12)--(13).
For the bottom edge the reciprocal estimate uses conjugation of
zeta, while |(-H)-Im(s)|>=H-B_0 deals with general complex s;
we do not assume s is real.

### 7. The ordered limit and its precise scope

First let a tend to infinity in the finite identity (9), at fixed
good H. Sections 4--6 justify all three limits uniformly on K:

    I_H+U_H+D_H=A_N+S_(N,H)+T_N.                              (14)

Then let H=H_j tend to infinity. Since H_j is between T_j and 2T_j,
B(T_j)=H_j^(o(1)); thus (12) tends to zero, as does (13).
Together with (8), equation (14) proves uniform convergence

    S_(N,H_j) -> I_infinity-A_N-T_N

on K. More explicitly the supremum of the difference from this limit
is bounded by

    C_(K,N)*(H_j^(-1)+B(T_j)*H_j^(-2)
                    +H_j^(-7/2)/log(N*H_j/A)).               (15)

The right side tends to zero. It also proves independence of the
chosen sequence within this good-height convention. Substituting
(7) gives (1)--(2). No exchange of the two contour limits was used.

The compact contour test therefore passes after the normalization
repair. It supplies an exact interface, not cancellation in a norm.
In particular (15) has constants depending on N,K, excludes s=rho,
and gives no uniform integrable majorant on the full critical line.
BCF's conditional norm argument cannot be appended without its
additional hypotheses or a separately proved replacement. This is
a reproduction and repair of a known identity, not progress beyond
the checked sources toward unconditional full-line decay.

### 8. Independent conceptual audit, 2026-11-03, step 230

The compact statement and all steps (1)--(15) pass independent review.
No substantive correction to the identity or its bounds was needed.
The reciprocal-domain qualification and explicit Cauchy tail after
(13) above make two existing uses of the estimates explicit.

The primary statements of Inoue Proposition 1 and Lemma 2 were
checked again: Q=1 is allowed; reciprocation negates both the power
of A/|z| and the exponential; the small-height estimate applies on
every chosen negative half-integer line. BCF v1 p. 6 was checked
against the functional equation: its derivative formula agrees with
(3), and its displayed F_s prefactor does not. The k=1 residue in
Section 4 independently fixes both sign and normalization.

The right-edge interchange is dominated by the summable coefficients
|mu(n)|/n^2 times N^(2-delta)/|2+it-s|^2. The kernel
1/|2+it-s|^2 has integral at most pi/(2-b), uniformly in s.
The shifted imaginary origin covers the
same complete vertical line. The x=1 antiderivative is valid there,
so no endpoint half-weight has been omitted. Positive rectangle
orientation gives exactly the minus sign on the upward left edge in
(9); all zero residues, including repeated ones, are retained.

The left-edge bound tends to zero at fixed H and is not asserted
uniformly for growing H. Both infinite horizontal tails are uniformly
Cauchy by the displayed bound after (13). Their remaining bounded
real-part intervals use (4), with reflection only where its nonzero
factor was verified. These facts validate (14) before H increases.
The right-edge error is O_(K,N)(1/H), while the finite horizontal
parts are O_(K,N)(B(T_j)/H^2) and the far parts are
O_(K,N)(H^(-7/2)/log(N*H/A)). Since B(T_j)=H_j^(o(1)), every term
in (15) vanishes. This establishes the claimed compact-uniform
convergence and independence within the good-height convention.

L018 is the sole direct local lemma input; the Euler product,
functional equation, residue theorem and the two precise Inoue
imports are used as stated above. No missing positivity premise,
RH, simplicity, reciprocal-derivative bound, rearrangement of an
infinite zero sum, or interchange with a full-line norm was found.
The proof still supplies no uniform integrable bound as K expands
or N grows. The audit validates this local interface only.

## Mathlib

Full matching coverage, Inoue's good-height theorem, and this precise
ordered residue identity have not been checked in Mathlib. No absence
claim is made. Supporting residue calculus, zeta functional equations
and summability formalizations would not alone establish the complete
statement. Reference: [Mathlib documentation](https://leanprover-community.github.io/mathlib4_docs/).
