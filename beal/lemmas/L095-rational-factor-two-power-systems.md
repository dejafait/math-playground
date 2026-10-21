# L095 — Rational factors reduce to two simultaneous power systems

## Hypotheses

A,B,C are positive integers, A^3+B^5=C^11, and gcd(A,B,C)=1.
Let E and phi be as in L093. Define the integral homogeneous forms

    Q(m,n)=3m²+mn+n²,
    H(m,n)=55n^8+165mn^7+594m²n^6+1100m³n^5
           +2145m^4n^4+2475m^5n³+2970m^6n²+1782m^7n+1215m^8.

## Conclusion

If E has a rational direct factor, then gcd(C,15)=1 and the given
triple arises from one of the following two systems. In both, m,u,a
are positive integers with gcd(m,u)=1 and gcd(m,55)=1.

I. C=5m+u^5, H(m,C)=a³, A=ma, B=Q(m,C)u.

II. C=m+5^10 u^5, H(m,5C)=5^11 a³, A=ma, B=Q(m,5C)u.

Conversely, positive m,u,a satisfying either system, gcd(m,u)=1,
gcd(m,55)=1 and gcd(C,15)=1 give a positive primitive solution and
a rational direct factor of its E. The reduced rational root is m/C
in I and m/(5C) in II. This is a finite two-system reduction, not an
emptiness result or a complete solution of the rational-factor branch.

## Proof

By L093, E is the full degree-eleven étale algebra. By the Chinese
remainder theorem for coprime polynomial factors, a rational direct
factor is equivalent to a rational root of phi(t)−s, s=B^5/C^11.
Conversely any rational root is simple and splits off Q. Pairwise
coprimality of A,B,C follows from the equation and gcd one: a prime
dividing two bases divides the third. In particular, for every prime p,

* if v_p(s)>0, it is a positive multiple of five;
* if v_p(s)<0, it is a negative multiple of eleven;
* zero is the only other possibility.

Write a rational root as m/n with n>0 and gcd(m,n)=1. The quadratic
3t²+t+1 is positive on R, and

    phi'(t)=−165t²(3t²+t+1)^4.

Thus phi is strictly decreasing: its derivative is strictly negative
except at the isolated point zero. Since phi(0)=1, phi(1/5)=0 and
0<s<1, we have 0<m/n<1/5. Hence m>0 and L=n−5m>0. Clearing
denominators gives the exact identity

    s=Q(m,n)^5 L/n^11.                                      (1)

For a prime p dividing n, reducedness gives p not dividing m. Thus
Q(m,n) modulo p is 3m² and L modulo p is −5m. Away from 3 and 5
both are units, so v_p(s)=−11v_p(n); in particular v_p(C)=v_p(n).
If p does not divide n, (1) has nonnegative valuation, so p cannot
divide C. We now handle the two exceptional denominator primes fully.

At 3, put k=v_3(n)>0 and h=v_3(Q). Here L is a unit. If k>=2,
Q=3m²+mn+n² has valuation h=1, so v_3(s)=5−11k<0, which is not
a multiple of eleven. This is impossible. If k=1, h>=1 and
v_3(s)=5h−11. For h=1,2 this is negative and not divisible by eleven;
for h>=3 it is positive and not divisible by five. It cannot be zero
for integral h. Thus 3 does not divide n, and consequently 3 does not
divide C. This argument permits arbitrarily large h in the k=1 case;
it does not assume away cancellation in Q.

At 5, put k=v_5(n)>0 and b=v_5(L). Now Q is a unit. If k>=2,
b=1, so v_5(s)=1−11k is negative and not divisible by eleven, an
impossibility. If k=1, b>=1 and v_5(s)=b−11. Values 1<=b<=10 are
negative and not divisible by eleven. For b=11 the valuation is zero;
for b>11 a positive valuation requires b−11 divisible by five.
Consequently the only possible case has k=1 and b=11+5j for j>=0,
and v_5(s)>=0. Thus 5 does not divide C either, and v_5(n) is zero
or one. Combining all primes gives

    n=d C,  d in {1,5},  gcd(C,15)=1.                       (2)

In particular all primes, including eleven, are accounted for. No
restriction that eleven avoid a coordinate was imposed. Equation (1)
now gives

    (B/Q)^5=L/d^11.                                       (3)

If d=1, the rational number B/Q has integral fifth power, so it is
an integer u>0. (In reduced form its denominator's fifth power must
divide its numerator's fifth power.) Thus L=u^5, B=Qu and
C=5m+u^5. If d=5, at every prime except five, (3) says v_p(L)
is a nonnegative multiple of five. At five the preceding calculation
says v_5(L)=11+5j. Unique factorization in Z therefore gives
L=5^11 u^5 with u>0 an integer. Equation (3), using positivity,
gives B=Qu, and 5C−5m=L gives C=m+5^10 u^5. Reducedness implies
gcd(m,u)=1 in either case; in II it also gives 5 not dividing m.

The full complementary equation is retained by the polynomial identity

    n^11−Q(m,n)^5(n−5m)=m³ H(m,n).                         (4)

This follows by binomial expansion; the coefficients displayed above
include all eleven degrees. Substitution of the original equation and
(2) yields

    (d^11 A³)=m³ H(m,dC).                                 (5)

For d=1, H=(A/m)^3 is an integer, so A/m is an integer a>0.
For d=5, reducedness gives gcd(m,5)=1. For every prime dividing m,
(5) implies v_p(A)>=v_p(m), since H is integral and p is not five.
Therefore m divides A and again A=ma with a>0. Formula (5) gives
exactly the respective H equations in I and II.

It remains to check the extra restriction gcd(m,55)=1. If eleven
divides m, reducedness makes n an eleven-adic unit. Every coefficient
of H except the last is divisible by eleven, the constant coefficient
55 has valuation one, and every other term then has valuation at least
two (including 1215m^8). Hence v_11(H)=1, inconsistent with (5),
whose right-hand H value has valuation divisible by three. If d=1
and five divides m, n is a five-adic unit. The constant term has
valuation one, the linear term has valuation at least two and every
term of higher m degree also has valuation at least two. Thus
v_5(H)=1, inconsistent with H=a³. For d=5, five was already excluded
from m. This proves gcd(m,55)=1. It excludes neither eleven dividing
C nor eleven dividing u, and uses no missing coordinate-divisor case.

For the converse in I, gcd(m,C)=gcd(m,u^5)=1. Also gcd(u,C)=1:
a common prime would divide 5m, hence would be five, but five is
excluded from C. A common prime of Q(m,C) and C divides 3m²,
and thus would be three, excluded from C. Consequently gcd(B,C)=1.
Identity (4) and H=a³ now give C^11−B^5=(ma)^3=A³.
All bases are positive, and gcd(B,C)=1 ensures primitivity. The reduced
fraction m/C is a root, since C−5m=u^5.

In II, gcd(m,5)=1 and gcd(m,u)=1 give gcd(m,C)=1. Moreover
gcd(u,C)=1, and a common prime of Q(m,5C) and C would divide
3m², again impossible. Thus gcd(B,C)=1. Formula (4), with
n=5C and n−5m=5^11u^5, gives

    5^11(C^11−B^5)=m³ 5^11 a³,

so the same equation and primitivity follow. The fraction m/(5C) is
reduced, positive and less than 1/5, and (1) gives its root property.
This completes both converses.

The calculation uses only the standard Chinese remainder theorem,
unique factorization of integers, and elementary polynomial identities;
no theorem-classification reproof is intended. The prior EXPLORE
assessment is `drafts/literature/2026-10-18-ordered-three-five-eleven-rational-factor.md`.
The elementary specialization is recorded because the checked source
does not supply these coefficient-one systems. Its classification is
POTENTIALLY_NEW in the limited search-policy sense, not a claim of
originality. L094 is contextual and is not a proof input. Other
reducible types, the irreducible case, both systems' emptiness and all
other residual signatures remain unresolved. Independent critical
audit is recorded below. Exact identity and residue checks are reproducible with
`python3 scripts/rational-factor/check_identities.py`; all thirteen checks
pass, with the full certificate at
`scripts/rational-factor/identity-certificate.json`. The finite arithmetic
is supporting verification; the valuation and converse arguments above
are essential and are not inferred from a sample.

### Independent critical audit — 2026-10-18

Verdict: **PASS without correction**, for the exact equivalence stated
above, not for emptiness of either system. The prior EXPLORE assessment
is `drafts/literature/2026-10-18-ordered-three-five-eleven-rational-factor-audit.md`.
The proof uses only L093's cover and etaleness, the named polynomial
Chinese remainder theorem and integer unique factorization. No local
rational factor is promoted to a global one; no L094 assertion or new
external theorem is needed.

The following independently checked valuation table is exhaustive for
primes dividing the reduced denominator. The permitted valuation set is
{0} union 5 Z_{>0} union (−11 Z_{>0}), by original primitivity.

| Prime and denominator valuation | Numerator valuations | Valuation of s | Consequence |
| --- | --- | --- | --- |
| p different from 3,5; k>0 | v_p(Q)=v_p(L)=0 | −11k | v_p(C)=k |
| p=3; k>=2 | v_3(Q)=1, v_3(L)=0 | 5−11k<0 | Impossible modulo 11 |
| p=3; k=1 | h=v_3(Q)>=1, v_3(L)=0 | 5h−11 | h=1,2 gives −6,−1; h>=3 gives positive residue 4 modulo 5; zero impossible |
| p=5; k>=2 | v_5(Q)=0, v_5(L)=1 | 1−11k<0 | Impossible modulo 11 |
| p=5; k=1 | v_5(Q)=0, b=v_5(L)>=1 | b−11 | b=1,...,10 impossible; exactly b=11+5j, j>=0 survives |

Here the k>=2 claims have unique lowest-valuation terms 3m² and −5m,
respectively. At k=1 no upper bound on h or b has been imposed. For
every prime not dividing n, integrality of Q^5 L gives v_p(s)>=0,
so that prime cannot divide C. Thus the table proves n=C or 5C,
including primes dividing C at eleven, and excludes 3 and 5 from C.
The b=11 case is retained: s is then a five-adic unit, not a positive
valuation case. A reduced numerator cannot vanish, since 0<s<1 and
strict monotonicity put m/n in (0,1/5).

For n=C, the rational fifth root B/Q of the integer L is an integer;
for n=5C, the complete valuation list gives L=5^11 u^5, including
v_5(u)=0 when b=11. Hence B=Qu in both cases. The complementary
identity has degree eleven, so substituting n=dC gives precisely
d^11 A³=m³ H(m,dC), without an omitted scale factor. For d=1,
integrality of (A/m)^3 proves m divides A. For d=5, each prime
dividing m is different from five, and
3v_p(A)=3v_p(m)+v_p(H)>=3v_p(m) proves the same assertion.
This yields H=a³ or 5^11 a³ exactly, without a rational cube twist.

The restrictions on m also pass: at eleven dividing m the constant
term 55n^8 has valuation one and every other term has valuation at
least two. At five dividing m in system I the same unique-minimum
argument applies. Both contradict the required cube valuation; system
II already excludes five from m by reducedness. No prime dividing u
or C is inadvertently removed by this argument.

For the reverse implications, system I gives gcd(m,C)=1 and
gcd(u,C)=1 using gcd(C,5)=1. System II gives both using gcd(m,5)=1
and gcd(m,u)=1. In each system any prime dividing Q(m,dC) and C
would divide 3m², contradicting gcd(C,3)=1 and gcd(m,C)=1. Thus
gcd(B,C)=1, which proves primitive reconstructed bases once the
equation is established. Substitution into the complementary identity
gives C^11−B^5=(ma)^3 in I and gives this same equation after
cancelling exactly 5^11 in II. Positive m,u,a make all three bases
positive. The respective fractions are reduced and lie in (0,1/5);
their root identities follow from L=u^5 and L=5^11u^5. L093 then
applies to each reconstructed triple, so the Chinese remainder theorem
really supplies a rational direct factor in both converses.

Independent finite verification uses multinomial coefficients for
(1+t+3t²)^5, rather than the original convolution routine. It checks
every coefficient of phi and H, every derivative coefficient, all
thirteen original assertions and the certificate's complete counts,
failures and denominator list. Run
`python3 scripts/rational-factor/audit_identities.py`; the thirteen
replayed assertions and six audit comparisons pass with no failures.
The full evidence and original certificate hash are in
`scripts/rational-factor/audit-certificate.json`. These checks support
the identities and finite residues only; the exhaustive table and
converse reasoning above supply the unbounded proof. No mathematical
correction, new branch exclusion or originality claim results from
this audit. No additional mathematical input is used.

## Mathlib

Full matching coverage of this two-system reduction: **not checked**.
The Chinese remainder theorem and unique factorization are named
standard inputs; no formal verification or absence claim is made.
