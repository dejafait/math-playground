# L097 — The rational-factor octic is irreducible over Q

## Hypotheses

Let H(m,n) be the integral homogeneous degree-eight form defined in
L095. All factorization assertions here concern Q[m,n], before any
integer substitution.

## Conclusion

H is irreducible over Q. Its factorization over Q consists of H itself,
up to nonzero rational units. The form H(m,5n) is also irreducible,
as is its nonzero rational scalar multiple 5^(-11)H(m,5n).
Thus neither simultaneous system in L095 admits a nontrivial rational
factor-by-factor cube descent of its octic equation. This does not
exclude integer solutions or descent over a larger field.

## Proof

Put h(X)=H(X,1). Its coefficients in ascending degree are

    55, 165, 594, 1100, 2145, 2475, 2970, 1782, 1215.

The first eight coefficients divided by eleven are exactly

    5, 15, 54, 100, 195, 225, 270, 162.

The leading coefficient is 1215=11*110+5, and the constant
coefficient is 55=11*5, not divisible by 121. Eisenstein's criterion
at the prime eleven therefore proves h irreducible over Q. The
criterion is imported from J. S. Milne, *Fields and Galois Theory*,
v5.10 (September 2022), Proposition 1.16, printed pp.12–13
([author PDF](https://www.jmilne.org/math/CourseNotes/FT.pdf));
Proposition 1.13 supplies its integral-factor reduction. These are
the primary results inspected in the prior SPECIALIZE assessment
`drafts/literature/2026-10-18-rational-octic-factor-descent.md`.
No reproof or input-specific factorization theorem is assumed.

To check the homogeneous passage explicitly, any factors of a
homogeneous polynomial in Q[m,n] can be taken homogeneous. Indeed,
the lowest and highest total-degree pieces of a product of two
nonzero polynomials are the products of their respective extreme
pieces, and are nonzero since the polynomial ring is a domain.
If the product has only one total degree, the widths of the two
degree ranges sum to zero; each factor has only one total degree.
Suppose then H=FG with homogeneous factors of positive degrees.
Dehomogenizing at n=1 gives h=F(X,1)G(X,1). Irreducibility of h
forces one of these factors to be a nonzero constant. A homogeneous
degree-d polynomial with constant dehomogenization must be c*n^d.
For d>0 this would make n divide H, contrary to
H(m,0)=1215m^8. Thus no such factorization exists. Also
H(0,n)=55n^8, so neither coordinate is an omitted factor; both
projective coordinate boundary values are nonzero when the other
coordinate is nonzero. The coefficient content is one: the first
eight coefficients have gcd eleven and gcd(11,1215)=1. There is
no nonunit integer content hidden in the asserted factorization.

The substitution (m,n) -> (m,5n) is an automorphism of Q[m,n],
with inverse (m,n) -> (m,n/5). It preserves irreducibility, and
multiplication by 5^(-11) is multiplication by a unit. This treats
the second system's argument scale and its right-hand factor 5^11.
In system I the retained equations are C=5m+u^5 and H(m,C)=a^3;
in system II they are C=m+5^10u^5 and H(m,5C)=5^11a^3.
In both cases the positive integers m,u,a, gcd(m,u)=1,
gcd(m,55)=1 and gcd(C,15)=1 remain required as in L095.
No condition on these domains was dropped to infer emptiness.
Irreducibility simply prevents splitting H into smaller rational
polynomial factors and then assigning cube twists to those factors.
It says nothing prohibiting cube values of an irreducible form,
and does not test factors appearing after a further nonlinear
substitution or after extension of the coefficient field.

The exact arithmetic is reproduced by
`python3 scripts/rational-factor/check_octic_irreducibility.py`.
Its complete certificate is
`scripts/rational-factor/octic-irreducibility-certificate.json`.
The proof above supplies the unbounded polynomial conclusion;
the certificate checks every coefficient used by the criterion.
This is a reproduction/specialization of the assessed elementary
method, not a claim of a new irreducibility criterion or Beal result.
The separate critical audit is recorded below.

### Independent critical audit — 2026-10-18

Verdict: **PASS without mathematical correction**, confined to the
polynomial irreducibility and mechanism scope stated above. The prior
SPECIALIZE assessment is
`drafts/literature/2026-10-18-rational-octic-irreducibility-audit.md`.
The citation locator now includes the criterion's statement on p.12
as well as its proof on p.13; this is a bibliographic clarification.

The displayed H in L095 was parsed independently of the original
script's hard-coded array. All nine monomials have total degree eight
and give the following complete comparison:

| Degree of m | Coefficient | Quotient by 11 for lower coefficients |
| --- | --- | --- |
| 0 | 55 | 5 |
| 1 | 165 | 15 |
| 2 | 594 | 54 |
| 3 | 1100 | 100 |
| 4 | 2145 | 195 |
| 5 | 2475 | 225 |
| 6 | 2970 | 270 |
| 7 | 1782 | 162 |
| 8 | 1215 | remainder 5 |

An additional independent identity check used the multinomial formula
q_k=sum 5!/(a!b!c!) 3^c, summed over a+b+c=5 and b+2c=k, for
the coefficients of (1+X+3X²)^5. With q_k=0 outside 0<=k<=10,
the coefficients of 1−(1−5X)(1+X+3X²)^5 are
delta_(k,0)−q_k+5q_(k−1). Degrees zero through two vanish and
degrees three through eleven are exactly the nine H coefficients.
This checks transcription against L095's defining complementary
identity, rather than merely comparing two copies of an array.

Eleven is prime, the leading coefficient has remainder 5 modulo eleven,
and the constant has remainder 55 modulo 121. Thus all hypotheses of
Milne's nonmonic Eisenstein criterion hold. The gcd of the first eight
coefficients is eleven (already gcd(55,165,594)=11); the full content
is one. Primitivity is compatible with the integral-factor reduction,
though rational scalar units would not affect rational irreducibility.

For the homogeneous argument, extreme nonzero total-degree pieces
cannot cancel in a product: the unique lowest-degree contribution is
the product of the two lowest pieces, and likewise at the highest
degree. Hence a factorization of homogeneous H has homogeneous
factors. Substitution n=1 is injective on the space of homogeneous
polynomials of a fixed degree, since its monomials have distinct
m-degrees. In particular neither factor becomes zero. A factor whose
specialization is constant is c*n^d, so a positive-degree such factor
would contradict H(m,0)=1215m^8. The other boundary value
H(0,n)=55n^8 independently excludes m as a factor. The origin is
not a projective point and supplies no missing boundary case.

For system II, the inverse substitution n -> n/5 exists over Q;
5^(-11) is a unit in Q[m,n]. Therefore 5^(-11)H(m,5C)=a³
has the asserted irreducible left-hand polynomial in the independent
variables m,C. This argument is not an integral-ring automorphism
or a claim that 5^(-11)H(m,5C) has integral coefficients. The original
system retains its precise integrality, positivity and gcd conditions.
System I uses H(m,C) directly. Neither argument asserts irreducibility
after substituting C=5m+u^5 or C=m+5^10u^5. Consequently the stop
is exactly the absence of smaller rational polynomial factors before
those nonlinear substitutions. Cube values, substituted factorizations,
number-field descent and integer emptiness remain undecided.

Every one of the seven original checks was independently recomputed;
all eleven top-level certificate fields were compared, including the
empty failure list, the factor-degree field and its stated proof basis.
Six additional checks pass: the full key set, nine distinct monomials,
three vanishing initial coefficients, all nine identity coefficients,
primality of eleven, and byte-identical original-script replay. The
complete audit evidence is
`scripts/rational-factor/octic-irreducibility-audit-certificate.json`.
Its multinomial formula above and parsed monomials specify the exact
independent calculation; the original replay command remains the one
given above. No mathematical script was changed. The reported factor
degrees [8] are a consequence of the cited criterion and this proof,
not an independently executed factorization oracle. Direct descent
requires at least two positive-degree rational factors and fails that
test. No new mathematical input, signature exclusion or originality
claim is supplied by this audit.

## Mathlib

Full matching coverage of this particular homogeneous octic statement:
not checked. Eisenstein's criterion is the cited mathematical input;
no formal verification or absence claim is made.
