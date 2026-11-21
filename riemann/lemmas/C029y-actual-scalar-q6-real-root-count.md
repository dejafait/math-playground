# C029y — The prescribed actual scalar Q_6 has two distinct real zeros

## Hypotheses

Use the exact coefficients of C029n Section1 and the finite normalization
of C029q, retaining every odd term. Explicitly, set

    S=sin(pi/8)/sqrt(2)>0, s=sqrt(2)>0, X=pi,
    epsilon_j=1,1+s,-1,-1-s according to j=0,1,2,3 modulo4,
    v_n=-n! sum_(h=0)^n
        4^h(4^(h+1)-1) B_(2h+2) (2X)^(h+1) epsilon_(n-h)
        /((n-h)!(2h+2)!),                0<=n<=8,
    q_k=4k(k-1)v_(k-2)+(8k^2+12k+7)v_k
        +(2k+3)(2k+5)v_(k+2),           0<=k<=6,
    A_(6,k)=6!/((6-k)!6^k) q_k,
    Q_6(x)=sum_(k=0)^6 w_k A_(6,k) x^k,
    w_k=(2k+1)!!/(2k)!!.

Omit the first term of q_k for k=0,1; v_n=u_n/S and q_k=beta_k/S.
Bernoulli numbers use B_1=-1/2 and the exact recurrence

    B_0=1,
    B_m=-(1/(m+1))sum_(j=0)^(m-1) binom(m+1,j) B_j.

These conventions are Alexey Kuznetsov, *Expansion of the Riemann Xi
Function in Meixner–Pollaczek Polynomials*, Canad. Math. Bull. 51(4)
(2008), 561–569, [primary source](https://doi.org/10.4153/CMB-2008-055-0),
equations(4)/(13) pp563/566, Proposition4.1 p567 and Jensen-weighted
family pp568–569. Proposition4.1 supplies the scalar weights, not the
root count asserted here. This calculation uses only the finite formulas;
no analytic transform, convergence assertion or RH assumption is used.

## Conclusion

Q_6 has actual degree six, is square-free, and has exactly **two** distinct
real zeros. Consequently it does not have the four distinct real input
nodes sought in assessment2059. This stops only that N=6 sufficient-
condition baseline. It does not refute a possible later input condition,
C029m's eventual Hermite-index hypothesis, or RH. The certificate below
is a standard finite specialization of Sturm's theorem, independently
audited in step2063; no novelty beyond the checked sources is asserted.

## Proof

### Exact construction and coefficient bounds

The half-angle identity in C029n reduces every coefficient to an ascending
polynomial in X with coefficients a+b*s, a,b rational. There is no scalar
coefficient fitting. The two sets of rational weights used are exactly

    6!/((6-k)!6^k): 1,1,5/6,5/9,5/18,5/54,5/324,
    w_k:           1,3/2,15/8,35/16,315/128,693/256,3003/1024.

In particular Q_6 is a scalar coefficient polynomial, not U_6 expressed
in monomials. No p_k basis recurrence is applied to Q_6. Its coefficients
are A_(6,k) multiplied by w_k individually, with no N=7 weights or
additional normalization. The program reconstructs v_0,...,v_8 and
q_0,...,q_6 by the formulas above, and checks exact equality of every
coefficient with C029n's saved finite input. Its full exact coefficient
arrays are retained in the certificate, including all odd entries.

Here and in the tables below, terminating decimals denote exact rationals.
Let c_k=w_k A_(6,k). Rational interval Horner evaluation gives

| k | lower bound for c_k | upper bound for c_k |
| --- | ---: | ---: |
| 0 | 2.789485175631 | 2.789485175632 |
| 1 | -3.474516922717 | -3.474516922716 |
| 2 | 2.545404642650 | 2.545404642651 |
| 3 | -1.131162447929 | -1.131162447928 |
| 4 | 0.263740465179 | 0.263740465180 |
| 5 | -0.016173270452 | -0.016173270451 |
| 6 | -0.002622342462 | -0.002622342461 |

Thus the actual degree is six and every odd coefficient is nonzero.

For completeness, the input and error certificates are elementary.
For d=5,239 define

    R_d=sum_(j=0)^47 (-1)^j/((2j+1)d^(2j+1)),
    E_d=1/(97d^97).

The finite geometric identity integrated on [0,1/d] gives
R_d<arctan(1/d)<R_d+E_d. C029n proves the branch-correct Machin identity
pi=16 arctan(1/5)-4 arctan(1/239) by tangent addition and an angle in
(0,pi/2); the program rechecks its rational tangent identity and angle
lower bound. Consequently pi is enclosed by

    [16R_5-4(R_239+E_239), 16(R_5+E_5)-4R_239].

Round those endpoints outward to the grid 10^(-60). If
b=floor(sqrt(2*10^120)), positive square-root bounds are
[b/10^60,(b+1)/10^60]; the two strict squared-endpoint inequalities
are checked using integers. Both input intervals agree exactly with
C029n's saved intervals. The exact arctangent terms, remainder bounds
and rational endpoints are included in the certificate.

For intervals I=[a,b], J=[c,d], addition uses [a+c,b+d]; multiplication
uses the minimum and maximum of ac,ad,bc,bd. Negation reverses endpoints.
If 0 is not in J, its reciprocal is [1/d,1/c], with division defined by
multiplication. After each operation, outward rounding to the same fixed
10^(-60) grid preserves inclusion: the lower endpoint is floored and
the upper endpoint is ceiled after multiplication by 10^60. These rules
enclose each actual value by induction. Horner evaluation of a+b*s and
then the polynomial in X therefore gives valid coefficient enclosures.
All calculations use integers and Fraction, without floating point or
an assumed decimal expansion. The table is a further outward rounding
to 12 decimal places; it is not used as the input to the Sturm calculation.

### Signed Euclidean chain and nondegeneracy

Define the actual real-polynomial Sturm sequence by

    f_0=Q_6, f_1=Q_6',
    f_(j+1)=-rem(f_(j-1),f_j),

stopping at a nonzero constant. To enclose a polynomial remainder, keep
ascending coefficient intervals for the current remainder r and divisor b.
Whenever deg(r)>=deg(b), let h=deg(r)-deg(b), and enclose
gamma=lc(r)/lc(b) by interval division. For each lower divisor coefficient
b_j, replace the coefficient of x^(h+j) by its old interval minus
gamma's interval times b_j's interval. The actual leading coefficient
cancels identically in r-gamma*x^h*b; delete this coefficient because of
that exact identity. No small interval is treated as zero. The certificate
also records that the interval subtraction for each canceled coefficient
contains zero. Lower coefficients are always retained.

Induction through the long divisions now encloses the actual remainder:
the true divisor leading coefficient is separated from zero, its quotient
is enclosed, all lower updates preserve inclusion, and the discarded
coefficient is algebraically zero. Negating the remainder enclosures
therefore encloses the actual next f_j. Each expected leading remainder
coefficient below excludes zero, proving its actual degree rather than
silently assuming a generic degree. The complete trace records two
quotient steps per division, all updated lower coefficients, all canceled
top enclosures and every resulting polynomial. There are five divisions,
with remainder degrees 4,3,2,1,0; no sign or division failed at the fixed
precision, and there was no precision or degree sweep.

| j | deg(f_j) | lower bound for lc(f_j) | upper bound for lc(f_j) |
| --- | --- | ---: | ---: |
| 0 | 6 | -0.002622342462 | -0.002622342461 |
| 1 | 5 | -0.015734054771 | -0.015734054770 |
| 2 | 4 | -0.101767444082 | -0.101767444081 |
| 3 | 3 | 0.032023192510 | 0.032023192511 |
| 4 | 2 | 4.603808895006 | 4.603808895007 |
| 5 | 1 | 0.064226166983 | 0.064226166984 |
| 6 | 0 | -28.021997028792 | -28.021997028791 |

The final constant is nonzero. Division by it has identically zero
remainder; the Euclidean algorithm therefore gives gcd(Q_6,Q_6')=1.
Thus Q_6 is square-free. Every use of division above has a certified
nonzero denominator. Correlations among coefficient intervals only
widen the enclosures; the inclusion induction does not require their
independence.

### Sturm variations and the threshold

Import the classical **Sturm theorem**, precisely Michel Coste,
*An Introduction to Semialgebraic Geometry*, October2002, Section1.1,
Theorem1.1 pp5–6 and Proposition1.4 p7
([primary notes](https://users.fmf.uni-lj.si/cimpric/courses04/seminar/SAG.pdf)):
for a square-free real polynomial
and the signed remainder sequence starting with f,f', the number of its
real zeros in (a,b), with endpoints not roots, equals V(a)-V(b), where
V counts successive sign changes after zeros are omitted. For the whole
real line take the limiting signs at negative and positive infinity.
Every f_j has a nonzero leading coefficient, so these limiting signs
are its leading sign times (-1)^deg(f_j), and its leading sign,
respectively. The certified degrees and leading signs give

    at -infinity: -, +, -, -, +, -, -;     V=4,
    at +infinity: -, -, -, +, +, +, -;     V=2.

There are therefore 4-2=2 real roots. Square-freeness makes them simple
and distinct. This is below the required count four. The nonreal roots
of this scalar polynomial are not claimed to be nonreal zeros of U_6
or Xi; no unproved transfer theorem is being used in either direction.

Reproduction, relative to the active notebook:

    python3 scripts/pollaczek/actual_scalar_q6_2061.py

Full exact construction, rational input intervals, all coefficient and
chain intervals, complete long-division traces, signs and checks are in
`scripts/pollaczek/actual-scalar-q6-2061.json`. It reports CERTIFIED,
actual count2, required count4, threshold false, and no failed checks.
The program is a finite arithmetic certificate of the displayed proof,
not a numerical root preview. Independent audit2063 is recorded below.

### Independent audit2063

The separate program
`scripts/pollaczek/actual_scalar_q6_audit_2063.py` imports no original
mathematical implementation and leaves certificate2061 unchanged. It
reconstructs the exact coefficient arrays from the displayed formulas,
using a separately specified Bernoulli table checked against every defining
recurrence. Jensen weights are obtained as products of (6-h)/6, and
the scalar weights as (2k+1)binom(2k,k)/4^k. All v, q, A and Q entries,
including every odd entry, agree exactly with the original and, where
present, C029n's certificate.

Its interval endpoints are integers representing multiples of 10^(-60).
Multiplication takes the extremal integer products followed by outward
integer division by 10^60; division takes the extrema of the four exact
endpoint ratios with the same outward rounding. Exact rational scaling
and addition handle coefficient constants without rounding them first.
These are independent implementations of the inclusion rules above.
Every saved arctangent term, remainder bound, Machin interval and squared
sqrt(2) endpoint is checked; the two tangent doublings and final tangent
identity also agree. The branch is justified by the positive lower angle
bound and 4theta-phi<4/5<1<pi/2, the last inequality following from
arctan(1)>1/2 by its integral. Thus the audit does not infer the branch
from a rational tangent identity alone.

Replayed Horner evaluation agrees with every full saved coefficient
interval and derivative entry. The audit compares all five complete
division traces: both quotient coefficients, both exact-cancellation
enclosures, every lower update, each signed remainder, and every saved
chain coefficient. Each leading sign excludes zero and the degrees are
6,5,4,3,2,1,0. The exact cancellation identity in the proof, rather than
zero containment alone, justifies deletion. The nonzero terminal constant
therefore proves the actual real-polynomial gcd is a unit.

A second enclosure construction evaluates coefficient polynomials by
direct powers and sums, instead of Horner order, and constructs its own
complete signed remainder chain. It has the same degrees and leading
signs, with terminal constant in
[-28.021997028792,-28.021997028791]. Both constructions give infinity
variations 4 and2 and hence the same two distinct real roots by the cited
real-coefficient theorem. No rational proxy polynomial replaces Q_6.

Reproduce with `python3 scripts/pollaczek/actual_scalar_q6_audit_2063.py`.
All 75 checks pass. Full reconstructed Q coefficients, both complete
chains, all replayed traces and the direct-power traces are retained in
`scripts/pollaczek/actual-scalar-q6-audit-2063.json`. An initial audit-code
failure compared equivalent rational strings 0 and0/1; its evidence remains
in `scripts/pollaczek/actual-scalar-q6-audit-2063-formatting-failure.json`.
Comparing rational values resolves that formatting issue; it revealed no
mathematical disagreement and required no changed input bound. This audit
validates only the finite stop, not any analytic or eventual hypothesis.

Replay2193 checks all 75 audit conditions and matches the complete2063
report, with unchanged hashes for every original input artifact. Full
replay evidence is `scripts/pollaczek/actual-scalar-q6-replay-2193.json`;
run `python3 scripts/pollaczek/actual_scalar_q6_replay_2193.py`.
This repeats the completed verification and adds no mathematical result.

## Mathlib

The full matching Q_6 theorem and formal real-root-count coverage remain
unchecked. Review2062 inspected
[Mathlib.Algebra.Polynomial.Sturm.Sequence](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Polynomial/Sturm/Sequence.html):
`Polynomial.sturmSeq`, `sturmSeq_cons`, `zero_notMem_sturmSeq` and
`dvd_of_mem_sturmSeq` support algebraic sequence properties. This module
does not supply the needed real-root count; coverage elsewhere is unknown.
The finite source formulas and Coste's real-coefficient Sturm theorem are
the cited mathematical inputs; no partial-node transfer is imported.
