# Corollary C019a: the actual theta score fails the fifth Jensen test

## Hypotheses

Let K be exactly the full theta kernel in L019, with the theta
transformation of L016. Near zero define

    G(z)=log(K(-iz)/K(0)), G(0)=0; h(z)=G'(z), a_k=h^(k)(0).

The logarithm is initially local, not an asserted entire logarithm.
Use the derivative convention

    J_5(h;X)=sum_(k=0)^5 binom(5,k) a_k X^k.

All numerical enclosures below are strict rational inequalities, not
rounded numerical premises. No hypothesis concerning Xi zeros is used.

## Conclusion

J_5 has three simple real zeros and two simple nonreal, purely imaginary
zeros. There is no real entire Laguerre--Polya (LP) function whose
derivatives of orders zero through five agree with this local h.
In particular, an exponent with derivative in LP cannot match this G
through order six. This is a local obstruction to that sufficient
exponent class, not a disproof of RH or of weaker approximation schemes.

## Proof

**The complex germ and exact symmetries.** The L019 series defines a
holomorphic function on |Im u|<pi/4. On each compact subset there,
Re(e^(2u)) has a positive lower bound; every fixed differentiated
summand is bounded by a constant times a fixed polynomial in n times
exp(-c n^2), c>0. Thus the series and all fixed derivatives converge
normally. The same argument applies to A(u)=e^(u/2)psi(e^(2u)), and
termwise differentiation gives K=(2D^2-1/2)A on this strip.

The real theta transformation gives

    A(-u)=A(u)+sinh(u/2).

Both sides are holomorphic on the connected strip, so the identity
theorem extends this equality there. The operator 2D^2-1/2 annihilates
sinh(u/2), and reflection commutes with D^2. Therefore K(-u)=K(u).
Its series also gives K(conjugate u)=conjugate K(u). L019 gives K(0)>0.
On a sufficiently small disk K(-iz)/K(0) is nonzero and has the unique
holomorphic logarithm with value zero at zero. Uniqueness and parity
give G(-z)=G(z); conjugation and K's parity give G(conjugate z)=
conjugate G(z). Hence h is odd with real Taylor coefficients and

    a_0=a_2=a_4=0.

**Certified derivatives of the full series.** Put v=pi n^2 e^(2u).
The n-th kernel summand is e^(u/2) Q_0(v)e^(-v), with

    Q_0(v)=8v^2-12v,
    Q_(j+1)(v)=(1/2-2v)Q_j(v)+2v Q_j'(v).

Consequently, for 0<=j<=6,

    K^(j)(0)=sum_(n>=1) Q_j(pi n^2)e^(-pi n^2).

The reproducible exact interval calculation is
`python3 scripts/theta-score/jensen-five-1326.py`. Its complete certificate
is `scripts/theta-score/jensen-five-1326.json`: all seven Q polynomials,
all eight retained summand intervals for each derivative, pi and
exponential bounds, omitted tails, log derivatives and sign tests.
Only Python integer/Fraction arithmetic determines bounds; Decimal
is used solely for display. Intervals have denominator 2^256. Every
operation rounds the lower endpoint down and upper endpoint up;
division checks that zero is excluded from its denominator interval.

Here are the elementary bounding details needed to reproduce the
certificate. Machin's identity pi=16 atan(1/5)-4 atan(1/239), with
alternating sums of respectively 120 and 40 terms and the next term
as remainder bound, encloses pi. For completeness, if a=atan(1/5)
and b=atan(1/239), tan(4a)=120/119 and tan(4a-b)=1; the angle is
in (0,pi/2), so 4a-b=pi/4. For 0<=x<=4*8^2, set t=x/1024<1.
The alternating exponential sums through terms 61 and 60 respectively
bound exp(-t) below and above. Raise the resulting positive interval
to power 1024 by interval repeated squaring. Monotonicity of exp(-x)
handles an interval argument at its opposite endpoints.

For the omitted n>=9 terms, write Q_j(v)=sum_d c_(jd)v^d and
B_j=sum_d |c_(jd)|4^d. Since deg Q_j=j+2<=8 and 3<pi<4,

    |Q_j(pi n^2)|<=B_j n^16,
    exp(-pi n^2)<2^(-4n^2).

Indeed e^3>sum_(k=0)^4 3^k/k!=131/8>16. The ratio of successive
n^16 2^(-4n^2) is at most 2^16 2^(-4(2n+1))<1/2 for n>=9.
Thus each absolute omitted tail is bounded by

    T_j=2 B_j 9^16 2^(-324)<10^(-60).

Add [-T_j,T_j] to the retained sum. This includes the entire omitted
series; no truncation is identified with the actual kernel.

Let r_j=K^(j)(0)/K(0) for j=2,4,6. Since K is even, differentiation
of its local logarithm, followed by u=-iz, gives exactly

    a_1=-r_2,
    a_3=r_4-3r_2^2,
    a_5=-(r_6-15r_4 r_2+30r_2^3).

These formulas can also be checked by expanding log(1+r_2 u^2/2!+
r_4 u^4/4!+r_6 u^6/6!+O(u^8)). Exact interval evaluation gives

    1.78678 < K(0) < 1.78680,
    18.72690 < a_1 < 18.72691,
    -143.01494 < a_3 < -143.01493,
    -1548.74555 < a_5 < -1548.74554.

The certificate checks these rational enclosures against its complete
integer endpoints, also checks the three computed odd kernel derivative
intervals contain zero, and records no failed test. The symmetry proof,
rather than a numerical smallness decision, sets odd derivatives to zero.

**Root decision.** We have

    J_5(h;X)=X(C+B X^2+A X^4),
    A=a_5, B=10a_3, C=5a_1.

The same certificate gives

    2625391.45 < B^2-4AC < 2625391.46,
    -145016.06 < AC < -145016.05.

Hence A and C are nonzero, the quadratic Ay^2+By+C has two distinct
real roots of opposite signs, and neither is zero. The positive root
gives two simple real X roots; the negative root gives two simple
purely imaginary X roots. The factor X supplies a simple zero at zero
because C!=0. This proves the full root count, including degree and
multiplicity.

**Known criterion and scope.** T. Craven and G. Csordas, *Jensen
polynomials and the Turan and Laguerre inequalities*, Pacific J. Math.
136(2) (1989), 241--260, pp.241--242, (1.3)--(1.4), states the
Jensen necessity for a real entire LP function with coefficients
gamma_k=phi^(k)(0): every sum binom(n,k)gamma_k X^k has only real
zeros. See also (2.1)--(2.3), p.242, for normalization and derivatives:
[publisher PDF](https://msp.org/pjm/1989/136-2/pjm-v136-n2-p03-s.pdf).
No positive-coefficient hypothesis or Turan converse is used. Applying
this cited necessity to any hypothetical entire LP extension with the
same six h derivatives contradicts the certified n=5 polynomial.
This imports the known criterion; the actual-kernel jet and rigorous
tail bounds are its local specialization, not a new general theorem.

L020 explains the possible downstream relevance of a valid global
exponent construction. This failure supplies no actual-Xi mixed sign,
no zero-location assertion, and no exclusion of real-axis, integral or
transform approximations without separately proved closure hypotheses.
Entire exponent continuation, admissible approximations, initialization,
singular blocks, identification and all-degree positivity remain open.

**Separate fixed audit1328 (17 November 2026).** The strip argument
was checked on arbitrary compact subsets: their positive lower bound
for Re(e^(2u)) gives a summable polynomial-times-Gaussian majorant for
each fixed derivative. The theta identity has the stated plus sign;
applying 2D^2-1/2 annihilates its sinh term. For conjugation of the
logarithm, conjugating K(-iz) first gives K(i conjugate z), which
equals K(-i conjugate z) by evenness. Thus neither parity nor reality
is inferred from small computed odd coefficients. Expanding the local
logarithm through degree six independently verifies all three displayed
a_j formulas. The Jensen coefficients are derivatives, not ordinary
Taylor coefficients. Only the cited necessity for a hypothetical real
entire LP function is used. For an exponent matching G through order
six, its derivative matches h through order five, so the asserted
jet exclusion has exactly the claimed scope.

The independent rational audit is reproducible with
`python3 scripts/theta-score/jensen-five-audit-1328.py`; its full
certificate is `scripts/theta-score/jensen-five-audit-1328.json`.
It uses rational endpoints rounded outward on a 2^512 grid, Machin
sums of lengths 140 and 50, and direct monomial evaluation of each
Q_j rather than Horner evaluation. It checks every stored pi, v,
exponential, retained summand, full derivative, logarithmic derivative
and quadratic interval by containment of its independent enclosure.
All seven polynomial coefficient lists and exact tail constants are
also checked. These are complete mathematical endpoint comparisons;
decimal displays and stored success flags do not establish them.

The exponential bound uses a different positive series. For each
rational endpoint x put t=x/512, with 0<=t<1/2. If
S_100=sum_(k=0)^100 t^k/k!, then

    S_100 <= exp(t) <= S_100 + (t^101/101!)/(1-t/102).

The upper bound follows since successive omitted-term ratios are
at most t/102<1. Reciprocating this positive interval encloses
exp(-t); nine outward-rounded squarings enclose exp(-x).
Monotonicity handles the opposite endpoints of x. All operations
use exact fractions with rational floor/ceiling, and division
excludes zero. The omitted n>=9 tail uses the original proved
majorant, independently recomputed: its ratio is bounded by
2^(-60)<1/2, and every T_j is less than 10^(-60).

All 132 audit checks pass, with no failed enclosure or root condition.
Replaying the original producer leaves certificate1326 byte-identical;
its SHA256 is recorded in the audit certificate. A<0<C, AC<0 and D>0
give two distinct nonzero opposite-sign y roots. Under y=X^2 each
nonzero root produces two simple roots (the derivative factor 2X
does not vanish); the remaining X factor has a simple zero since
C>0. Thus all five roots and their multiplicities are accounted for.
This validates the existing known-criterion specialization, without
adding a theorem beyond the checked sources or a new Xi sign input.
The proof and the independent computation both retain the weaker
approximation and global realization gaps stated above.

## Mathlib

Full matching coverage for this actual-theta score calculation and the
Jensen necessity has not been checked. L016 records supporting Gaussian
Poisson summation and smooth-series facts; those are not a full matching
theorem for this corollary. Unknown coverage is not claimed absence.
