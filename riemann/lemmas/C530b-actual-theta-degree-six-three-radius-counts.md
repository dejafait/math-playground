# C530b — Actual theta degree-six polynomials have two real roots at three fixed radii

## Hypotheses

Use the actual positive coefficients c0,c2,c4,c6 and the normalization
of C530a. In particular its four proved wider rational display intervals
are available under its explicit CPython/libmpdec trust assumptions.
No quadrature is repeated here. Set m_j=c_(2j)/c0 for j=0,1,2,3,
so m_0=1 exactly, and define

    p_r(t)=sum_(j=0)^3 (-1)^j m_j r^(2j) P_(2j)^(3/4)(t/2;pi/2).

The basis and its normalization are imported from Dan Romik,
*Orthogonal polynomial expansions for the Riemann xi function*,
arXiv:1902.06330v3 (5 May 2019), Appendix A.4 (A.21), (A.27)
and the finite diagonal formula (3.26),
[versioned primary text](https://arxiv.org/html/1902.06330v3).
The relevant general cubic identities and strict discriminant/root
cases have already been proved and audited in L530. Its atomic moments
and endpoint signs are not inputs here. Exact Python integer/Fraction
arithmetic is trusted for the new finite certificate.

## Conclusion

At each of r=9/32,1/3,1, p_r has degree six, exactly two real roots
and four nonreal roots. All six complex roots are simple. Thus this
actual degree-six family fails six-real-root initialization at the
specified first radius 9/32. The three counts do not demonstrate a loss
between those radii, or exclude changes at intermediate radii.

This is a known-method specialization with no originality claim or
RH candidate. It settles no infinite-family,
all-degree, eventual Hermite-index or Xi-transfer question. The new
arithmetic certificate and its specialization passed the separate
independent audit2073 below; C530a's earlier audit is reused as input.

## Proof

### Applicability and interval propagation

C530a gives c0>=0.48099000592797654>0 and positive enclosures of the
other three coefficients. Finite decimal endpoints in that statement
are exact rationals. If [l_j,u_j] is its interval for c_(2j), then

    m_0=1,
    m_j in [l_j/u_0,u_j/l_0]  (j=1,2,3).

These three intervals form an enclosing box even though all ratios
share c0. Discarding their correlations enlarges the possible set;
no independence or exact simultaneous endpoint attainment is assumed.

Put s=r^2, A=m_1 s, B=m_2 s^2, C=m_3 s^3. At all three radii these
numbers are strictly positive. L530's general coefficient identities,
in the same basis normalization, give p_r(t)=P_r(t^2), where

    P_r(z)=d+cz+bz^2+az^3,
    d=1+3A/4+21B/32+77C/128,
    c=-A/2-17B/24-2401C/2880,
    b=B/24+25C/288,
    a=-C/720.

Thus d>0,c<0,b>0,a<0; in particular the degree and constant term
are nonzero. This application needs no distinct-root assumption or
root-velocity theorem. We use the finite polynomial definition itself,
without any infinite-series limit, flow uniqueness or Xi transfer.

The new script implements exact rational interval addition,
multiplication by the minimum/maximum of all four endpoint products,
and division by an interval excluding zero via its reciprocal interval.
Repeated multiplication encloses powers, including negative bases;
it does not assume that repeated occurrences are independent values.
Each operation encloses the actual expression by elementary interval
inclusion. No precision rounding, midpoint roots or coefficient replay
is used. The exact quotient interval above is the only division used
in normalization. Reporting decimals are separately rounded outward
using integer floor/ceiling; they do not feed later calculations.

### Complete sign evidence

For each radius the complete rational coefficient intervals and the
five complete rational term intervals of

    Delta=b^2 c^2-4ac^3-4b^3 d-27a^2 d^2+18abcd

are saved in `scripts/pollaczek/actual-theta-three-radius-2072.json`.
Their interval sum encloses the actual discriminant. The following
exact rational decimal hulls of the coefficient intervals provide
strict signs, including the leading coefficient and constant term:

| r | d interval | c interval | b interval | a interval |
| --- | --- | --- | --- | --- |
| 9/32 | [1.002412618873733152,1.002412618873735291] | [-0.001615711340418757,-0.001615711340417214] | [0.000001129429212631,0.000001129429212651] | [-0.000000000448886055,-0.000000000448886054] |
| 1/3 | [1.003399044561369468,1.003399044561372643] | [-0.002280542389772174,-0.002280542389769809] | [0.000002250855407953,0.000002250855407994] | [-0.000000001244094581,-0.000000001244094580] |
| 1 | [1.033443666776554843,1.033443666776673721] | [-0.023722428087901768,-0.023722428087765547] | [0.000232705118567023,0.000232705118577731] | [-0.000000906944949545,-0.000000906944949410] |

The outward discriminant hulls are given compactly as intervals for
10^30 Delta; every displayed endpoint below is an exact integer:

| r | Lower endpoint of 10^30 Delta | Upper endpoint of 10^30 Delta |
| --- | --- | --- |
| 9/32 | -706707801790 | -706707796204 |
| 1/3 | -5176945526570 | -5176945482696 |
| 1 | -633399164714355219 | -633399120925907765 |

In all three cases the upper endpoint is strictly less than the
required threshold zero. No sign interval contains zero.

### Root counts and multiplicity

Apply L530's proved cubic sign argument separately at each radius.
The strict alternating coefficient signs imply P_r(-x)>0 for all
x>=0. Negative discriminant means exactly one real cubic root and
one nonreal conjugate pair, all distinct. Its real root is therefore
strictly positive. It gives the two real roots +/-sqrt(z) of p_r;
the other two cubic roots give four nonreal roots. No other real
t can occur because real t has t^2>=0.

Every complex cubic root z is nonzero since d>0, and simple since
Delta<0. At any root t of p_r, therefore,

    p_r'(t)=2t P_r'(t^2) != 0.

This is precisely L530's multiplicity case and establishes simplicity
of all six roots, including the four nonreal ones. It also verifies
the degree-six count without treating a sign interval as equality.

### Reproduction and qualifications

Run from the notebook:

    python3 scripts/pollaczek/actual_theta_three_radius_2072.py

The script writes the full certificate named above. All 18 checks
pass, and `/failures` is empty. The source display strings and their
presence in C530a, positive denominator, all complete normalized
intervals, scaled moments, cubic coefficients, five discriminant
terms and final discriminants were inspected in full. The reporting
hulls were also inspected, rather than used as previews of unexamined
sign evidence. The proof relies on interval inclusion and strict signs,
not on the pass label alone. The source and template file hashes are
recorded for provenance. Backend correctness remains a trust assumption.

There were exactly three radius evaluations. No radius grid, higher
degree, coefficient precision change, collision search, or new
quadrature was performed. The finite initialization obstruction does
not refute RH, eventual full-family root control, or the possibility
of a different actual-input invariant. Root counts and multiplicities
outside the three named tests remain unproved here.

### Independent arithmetic and multiplicity audit — 21 November 2026

Run from the notebook:

    python3 scripts/pollaczek/actual_theta_three_radius_audit_2073.py

The full evidence is
`scripts/pollaczek/actual-theta-three-radius-audit-2073.json`.
All 60 checks pass, with an empty failure list. The audit imports no
code from the generator. It parses the four rational intervals directly
from C530a's table, checks the original source/template hashes, encloses
normalization with a positive denominator, and reconstructs g_0 through
g_6 from L530's imported recurrence. Thus its coefficient construction
does not assume the displayed cubic coefficient expressions. It obtains
the same even basis and all the complete saved ratio, scaled-moment,
coefficient, five-term discriminant and final discriminant intervals.
It checks the reporting hulls and both canonical sign tables exactly.

As a second discriminant calculation, it encloses the determinant of
the following Sylvester matrix using the complete permutation formula:

    S = [[a,b,c,d,0], [0,a,b,c,d],
         [3a,2b,c,0,0], [0,3a,2b,c,0], [0,0,3a,2b,c]].

The standard resultant-discriminant identity used in L530's independent
audit is Delta=-det(S)/a. Here the degree is exactly three and a<0
throughout its interval, so the reciprocal operation is legitimate.
Every endpoint product is enclosed by its minimum and maximum, each
permutation has its inversion-parity sign, and the sum encloses det(S).
Repeated appearances of coefficients only enlarge this interval;
they do not assert independence. Dividing its negative by the nonzero
leading-coefficient interval encloses the actual discriminant. This
alternative calculation gives the following exact integer hulls:

| r | Lower endpoint of 10^30 Delta via resultant | Upper endpoint |
| --- | --- | --- |
| 9/32 | -706707819065 | -706707778929 |
| 1/3 | -5176945663132 | -5176945346135 |
| 1 | -633399320879449555 | -633398964760813456 |

All upper endpoints are strictly below zero. Full rational resultant
and alternative discriminant intervals, not just these hulls, were
inspected along with every reconstructed coefficient/discriminant
interval, the source ratios, recurrence polynomials and all 60 checks.
The original certificate2072 remains unchanged. Exact Fraction
arithmetic and C530a's CPython/libmpdec contract remain trust assumptions;
this is independent local code/proof verification, not external review
or formal verification of the backend.

The logical audit also checks the complete multiplicity case. Since
P_r(-x)=d-cx+bx^2-ax^3>0 for x>=0, its unique real root is positive.
The real cubic with Delta<0 has three distinct roots, exactly one real.
Its two nonreal roots cannot be squares of real numbers. Since d>0,
none of its roots is zero; hence each of the six roots of P_r(t^2)
satisfies 2t P_r'(t^2)!=0. This verifies all real/nonreal counts and
all complex multiplicities. Neither flow distinctness through other
radii nor any limiting argument is needed. No radius, degree or
coefficient precision was changed and no quadrature was rerun.

## Mathlib

Matching coverage of this actual-theta finite certificate and its
normalization has not been checked; availability is unknown. The
standard cubic discriminant argument is reused from L530 and the
analytic coefficient inputs from C530a. No Lean formalization or
claim of absent supporting algebraic results is made.
