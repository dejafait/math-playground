# L098 — Fixed-support cube classes for both rational-factor systems

## Hypotheses

Let H be the homogeneous octic of L095, put h(X)=H(X,1), and write

    h(X)=55+165X+594X²+1100X³+2145X⁴+2475X⁵
         +2970X⁶+1782X⁷+1215X⁸.

By audited L097, K=Q[X]/(h) is a field of degree eight. Let theta
be the residue of X, b=1215, O_K the maximal integer ring, and S the
set of all prime ideals of O_K above the rational primes 3,5,11.
For a prime ideal P, v_P is the additive valuation normalized to have
value one on a uniformizer. Define

    K(S,3)={ [gamma] in K*/K*³ : v_P(gamma)=0 modulo 3
                               for every P outside S }.

Let m,u,a be positive integers, gcd(m,u)=1 and gcd(m,55)=1. Assume
one of the two complete L095 systems, retaining gcd(C,15)=1:

    I:  C=5m+u⁵,       H(m,C)=a³;
    II: C=m+5¹⁰u⁵,     H(m,5C)=5¹¹a³.

All statements concern these fixed integer pairs, without projective
rescaling or assuming theta globally integral.

## Conclusion

The group K(S,3) is finite. Each tuple in system I gives the nonzero
element alpha_I=m−theta*C, with

    [alpha_I] in K(S,3),
    N_(K/Q)(alpha_I)=a³/1215=75*(a/45)³.

Each tuple in system II gives the nonzero element
alpha_II=m−theta*(5C), with

    [alpha_II] in K(S,3),
    N_(K/Q)(alpha_II)=5¹¹a³/1215=15*(125a/9)³.

Thus the respective classes lie in the finite fibers of the induced
norm map K(S,3) -> Q*/Q*³ above [75] and [15]. These are necessary
containing sets; neither their nonemptiness nor a representative list
is asserted. Exceptional-prime components are unrestricted except for
the displayed norm constraints. In particular no prime dividing C is
added to S and no coordinate-divisibility case is deleted.

## Proof

### Exact exceptional support

The polynomial discriminant is

    Disc(h)=3⁴⁷*5⁶*11⁷.                                    (1)

Here is an exact calculation, independent of a maximal-order model.
Set q(X)=3X²+X+1. L095's complementary identity at n=1 and direct
differentiation give

    X³h(X)=1−(1−5X)q(X)⁵,
    3h(X)+Xh'(X)=165q(X)⁴.                                (2)

For the second identity, the derivative of the first right-hand side
is 5q⁴*(q−(1−5X)q')=165X²q⁴; cancel X² as a polynomial
identity. If beta_1,beta_2 are the roots of q, neither is zero, their
product is 1/3, and (2) gives h(beta_i)=beta_i^(−3). Standard
resultant product identities therefore give

    Res(h,q)=Res(q,h)=3⁸*h(beta_1)*h(beta_2)=3¹¹.

Let theta_1,...,theta_8 be all roots of h. They are distinct by
L097 and characteristic zero, and nonzero since h(0)=55. Using (2),
the product identities give

    product theta_i = 55/b,
    product q(theta_i) = Res(h,q)/b²,
    Res(h,h') = b⁷ * product h'(theta_i)
              = b⁷ * 165⁸ * (Res(h,q)/b²)⁴ / (55/b)
              = 165⁸*3⁴⁴/55
              = 3⁵²*5⁷*11⁷.

Since (−1)^(8*7/2)=1 and b=3⁵*5, division by b proves (1).
Consequently the rational primes dividing 5*b*Disc(h) are exactly
3,5,11. This is a polynomial-discriminant support calculation; it
neither identifies the field discriminant nor assumes Z[theta] is a
maximal order (theta need not be integral).

### Uniform local valuation argument

For system I put n=C, and for system II put n=5C. In I,
gcd(m,n)=gcd(m,u⁵)=1. In II, gcd(m,C)=1 follows from
C=m+5¹⁰u⁵, gcd(m,u)=1 and 5 not dividing m; these also imply
gcd(m,5C)=1. Thus gcd(m,n)=1 in both cases. Since n>0 and theta
has degree eight, alpha=m−n*theta is not zero.

Fix a rational prime p outside {3,5,11}, and any maximal-ring prime
P above p. The polynomial h/b is monic with coefficients in Z_(p),
so theta is integral over Z_(p), hence lies in O_(K,P). This uses
the integral closure, with no power-order maximality assumption.
Both alpha and the polynomial expression below are locally integral.

If p divides n, then p does not divide m. Reduction modulo P makes
alpha equal to the nonzero rational residue of m, so v_P(alpha)=0.
This handles every possible prime divisor of C outside the fixed S.

Otherwise n is a unit. If alpha is a unit there is again nothing to
prove. Suppose v_P(alpha)>0. Write h(X)=sum_(i=0)^8 h_i X^i.
The exact difference-of-powers identity, using h(theta)=0, is

    H(m,n)=alpha*G,
    G=sum_(i=1)^8 h_i*n^(8−i)
                     *sum_(j=0)^(i−1) m^(i−1−j)*(n*theta)^j. (3)

Modulo P we have m=n*theta, and hence

    G = n⁷*h'(theta) modulo P.                            (4)

Because p divides neither b nor Disc(h), the reduction of h still
has degree eight and is squarefree: the reduction of
Res(h,h')=b*Disc(h) is nonzero. Thus h and h' are coprime over
F_p. Their polynomial Bezout identity, evaluated at the residue of
theta in the residue field of P, proves that h'(theta) is a unit.
Equation (4) proves G is a unit. Taking normalized valuations in
(3), with e_P=v_P(p), now gives

    v_P(alpha)=v_P(H(m,n))=e_P*v_p(H(m,n)).                (5)

In system I, v_p(H)=3v_p(a). In system II the same equality holds
at the present p, since p is different from five. Thus (5) is
divisible by three. Together with the two unit cases this covers
every P outside S, with no assumption that p avoids C, m, u or a
beyond the proved gcd(m,n)=1. It proves [alpha] in K(S,3). At
primes in S no valuation divisibility is claimed. Ramification indices
are retained in (5); no unramifiedness assumption is needed there.

This is the fixed-pair specialization of the local complementary-
factor argument in M. Mourao, *Descent on superelliptic curves*,
arXiv:1010.2360v5 (15 May 2012), Sections 2.1–2.3, printed pp.2–4
([primary PDF](https://arxiv.org/pdf/1010.2360v5)). Proposition 2.3
and the subsequent projective construction impose divisibility of the
degree by the exponent; eight is not divisible by three. Accordingly
the projective descent theorem is not imported. The full local
argument (3)–(5) is written here because this fixed-pair, nonmonic
specialization is the difference identified by the prior SPECIALIZE
assessment `drafts/literature/2026-10-18-octic-supported-cube-classes.md`.
No new descent principle is claimed.

### Finiteness and norm scales

For this number field and finite set of maximal-ring primes, import
the multiplicative 3-Kummer exact sequence

    1 -> O_(K,S)*/O_(K,S)*³ -> K(S,3)
                             -> Cl(O_(K,S))[3] -> 1.

The precise input is the unnumbered m-Kummer sequence and following
finiteness paragraph in J. E. Cremona and M. P. Lingham, *Finding all
elliptic curves with good reduction outside a given set of primes*,
Experimental Mathematics 16(3) (2007), 303–312, Section 2, printed p.3
of the [author manuscript](https://johncremona.github.io/papers/egros.pdf).
Take their exponent m=3 and their S to be the full set above 3,5,11.
The S-unit theorem makes the left group finite and finiteness of the
S-class group makes the right group finite, so K(S,3) is finite.
The three-torsion term is retained: no ideal cube is assumed principal,
and no generator is assumed an S-unit times an element cube.

Since h is irreducible and separable, its roots run through every
embedding of K. Its leading coefficient is b, so

    N_(K/Q)(m−n*theta)=product_i(m−n*theta_i)=H(m,n)/b.

Substituting n=C, H(m,C)=a³ gives the first exact norm formula.
Substituting n=5C, H(m,5C)=5¹¹a³ gives the second. In particular
the norm in II uses the actual argument 5C; there is no division by
5⁸ or replacement by the system-I element. The rational identities
1/1215=75*(1/45)³ and 5¹¹/1215=15*(125/9)³ prove the claimed
classes. Norm sends element cubes to rational cubes and therefore
induces the stated map on classes. Its fibers are finite subsets of
the already finite group, with no assertion that either is populated.

Exact arithmetic supporting (1) and the two norm scales is reproduced
by `python3 scripts/rational-factor/check_octic_cube_support.py`.
The complete certificate is
`scripts/rational-factor/octic-cube-support-certificate.json`.
All seven checks pass: a 15-by-15 Sylvester determinant computed by
integer Bareiss elimination agrees with independent rational Gaussian
elimination, the discriminant factors completely as in (1), and both
cube scalings are exact. The displayed resultant calculation and
local proof supply the mathematical argument; finite arithmetic is
not evidence of integer emptiness.

This establishes the approved necessary-containment target as a
reproduction of assessed methods. It supplies no S-unit basis,
S-class three-torsion, representative enumeration, local intersection,
class survival or integer exclusion. The equations for C involving
u⁵ remain required in any later use, as do positivity, primitivity and
all of L095's gcd restrictions. The proof does not reverse this
containment or identify these pairs with projective rational points
on y³=h(x). Other algebra factors and residual signatures remain
independent. The separate critical review is recorded below.

### Independent critical audit — 2026-10-19

Verdict: **PASS without correction**, for the necessary containment and
exact norms stated above. The prior SPECIALIZE assessment is
`drafts/literature/2026-10-18-octic-supported-cube-class-audit.md`.
This validates the local notebook input, not a new descent theorem or
an exclusion of either system. L095 and audited L097 remain the only
direct local mathematical inputs; no DAG edge changes are needed.

The full domains are retained. In I, a common prime of m and C divides
u, contradicting gcd(m,u)=1. In II, such a prime divides 5^10 u^5;
it cannot be five because gcd(m,55)=1, and cannot divide u. Also
five does not divide m, giving gcd(m,5C)=1. Thus both actual pairs
are primitive, even when C is divisible by eleven or other primes.
Their n is positive. An equality m=n*theta would make theta rational,
contrary to L097's degree eight, so all multiplicative classes exist.
No further coprimality with a or u is needed in the local argument.

The coefficients were independently reconstructed from the multinomial
expansion of (1+X+3X^2)^5: its degree-k coefficient is the sum of
5! 3^c/(a!b!c!) over a+b+c=5 and b+2c=k. For
1−(1−5X)(1+X+3X^2)^5, degrees zero through two vanish and the
remaining nine coefficients are exactly the displayed h. Expanding
q^4 the same way verifies every coefficient of 3h+Xh'=165q^4.
Euclidean polynomial remainders over Q give independently
Res(h,q)=3^11 and Res(h,h')=3^52*5^7*11^7. The latter agrees
with both saved determinant values. All 225 entries of the original
Sylvester matrix agree with h and its derivative, not merely its
reported determinant. The sign in the degree-eight discriminant is
positive since 8*7/2=28; division by 1215=3^5*5 gives exactly
3^47*5^6*11^7. The recorded factorization has remainder one.
The root-product argument above has the same scales: Res(q,h)
contains 3^8, product beta_i^(-3)=27, and product theta_i=55/b.
Thus neither a leading coefficient nor a resultant sign was omitted.

For each rational p outside {3,5,11}, h/b is monic over Z_(p).
Every valuation ring O_(K,P) above p contains its integral elements,
so theta, alpha and G are integral there. This conclusion requires
neither global integrality of theta nor maximality of a power order.
The following cases exhaust every such maximal prime P:

| Case | Reason | Normalized valuation of alpha |
| --- | --- | --- |
| p divides n | gcd(m,n)=1 makes m a unit and n*theta lies in P | 0 |
| p does not divide n and alpha is a unit | Local integrality excludes negative valuation | 0 |
| p does not divide n and alpha is not a unit | G reduces to n^7 h'(theta), which is a unit | e(P/p) v_p(H(m,n)) |

For the third row, each summand in (3) reduces to h_i*i*n^7*theta^(i−1),
including i=1 and i=8. Since b and Res(h,h') are units at p,
the reduced polynomials have no common root over any residue extension.
Consequently h'(theta) is a unit, including when the residue of theta
is zero. The rational restriction of the normalized valuation is
v_P(r)=e(P/p)v_p(r). In either system the displayed H value has
v_p(H)=3v_p(a), since p is not five; its product with the integer
e(P/p) is divisible by three. This explicitly includes primes dividing
C, handled by the first row, and primes dividing m or a. At 3,5,11
no assertion of valuation divisibility is needed. The set S is a fixed
sufficient support, not a claim of minimal support or of a field
discriminant equal to the polynomial discriminant.

The cited Cremona–Lingham Section 2 sequence applies to any number
field, finite maximal-prime S and exponent m>1. Here K is a field by
L097 and m=3. Finite generation of S-units makes their quotient by
cubes finite, while the S-class group is a quotient of the finite
ordinary ideal class group. Its three-torsion must remain in the
sequence. No class-number-one, root-of-unity, principality, or
unproved class-group computation is used. Mourao's projective
degree-divisibility hypothesis is not met and is not imported: the
fixed-pair local proof above is the precise assessed specialization.

For the norm, the matrix of multiplication by theta in the basis
1,theta,...,theta^7 has ones immediately below the diagonal and
last column −h_i/b. Its determinant polynomial det(zI−M_theta)
was checked independently at z=−4,−3,...,4 by a Leibniz subset sum,
without using either original elimination routine. All nine values
equal h(z)/b. Both polynomials have degree at most eight, so these
nine distinct exact checks establish their identity. Homogeneity
then gives det(mI−nM_theta)=H(m,n)/b for every rational m,n,
and in particular both actual pairs. Substituting their distinct H
values gives a^3/1215 and 5^11*a^3/1215. The exact identities
75/45^3=1/1215 and 15*(125/9)^3=5^11/1215 verify the claimed
rational cube classes. Norms respect multiplication and cubes, so
the induced norm map is well defined; its fibers are finite because
its domain is finite. No nonemptiness, representative list, or
sufficiency of the norm condition is inferred.

Reproduce the independent arithmetic with
`python3 scripts/rational-factor/audit_octic_cube_support.py`.
The complete evidence is
`scripts/rational-factor/octic-cube-support-audit-certificate.json`.
All fourteen audit checks and all seven original assertion replays
pass, with no failures. The original certificate is preserved and its
SHA-256 recorded. The finite checks verify the polynomial arithmetic;
the exhaustive valuation argument and precise finiteness citation
above supply the unbounded claims. S-unit and S-class arithmetic,
representatives, fifth-power compatibility, integer lifting and other
algebra factors remain unresolved. ATTEMPTS/043–044 are unchanged.

## Mathlib

Full matching coverage of this fixed-pair support specialization and
the multiplicative Kummer exact sequence: **not checked**. Supporting
resultant, integral-closure, norm, S-unit and ideal-class theorems were
not checked in Mathlib. The primary citations above are mathematical
inputs, not claims of formal verification or absence from the library.
