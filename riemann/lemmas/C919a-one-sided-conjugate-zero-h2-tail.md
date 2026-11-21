# Corollary 919a: a one-sided complete conjugate-zero H2 tail budget

## Hypotheses

Use exactly L919's actual family F(lambda,z), logarithmic H2,
opposite-pair multiset with full multiplicities, R=100,
D=diag(1,200,40000), head A including |zeta|=100, and strict-tail
matrix E. The parameter satisfies 0<=lambda<=1/20. In particular

    D H2 D = A+E,
    E = sum_(|zeta|>100) w(zeta) w(zeta)^T,
    w(zeta) = (zeta^(-2),200 zeta^(-4),40000 zeta^(-6))^T.

The transpose is algebraic. No RH, real-zero, simplicity, constant
census, continuously indexed zeros or head-margin hypothesis is made.

## Conclusion

Uniformly on the entire closed parameter band, in real quadratic-form
order,

    E >= -epsilon_* I_3 >= -epsilon I_3,
    epsilon_* = 133662268399/267363281250000000000,
    epsilon = 1/2000000000,
    epsilon_* < epsilon < B/100 = 5691/10^11,
    B = 5691/10^9.                                      (1)

Thus epsilon_* is approximately 4.999275435 times 10^(-10), rounded
up here for display only; (1) uses exact rationals. The prospective
hundredfold threshold passes. This is a quantitative specialization
of known strip, conjugate-block and zero-count methods, not a new
general theorem beyond those methods.

Consequently a separately established uniform head margin
inf_lambda lambda_min(A(lambda))>epsilon would suffice for strict
H2 positivity on this band. No such margin, its feasibility, head
reality/census/separation, signs at other degrees, contacts,
initialization or global continuation is proved. In particular (1)
is a lower bound, not a bound for ||E||, and does not prove RH.

## Proof

### Imported strip theorem and the local units

Import de Bruijn's strip theorem as stated in D. H. J. Polymath,
*Effective approximation of heat flow evolution of the Riemann xi
function, and a new upper bound for the de Bruijn-Newman constant*,
Research in the Mathematical Sciences 6 (2019), article31,
arXiv:1904.12438v2 (4 August 2019), Theorem3.2:
https://arxiv.org/html/1904.12438v2#S3 .
If t0 is real, y0>0, and H_(t0) has no zero x+iy with x real and
y>y0, then for each t>t0 it has no zero with
y>sqrt(max(y0^2-2(t-t0),0)). The source's proof imports de Bruijn,
Theorem13; we import the theorem, not a new proof. The ordinary-strip
application is also explicit in the proof of Proposition3.3 there.
No hypotheses of that separate barrier proposition are used.

L919 verifies the exact source normalization

    F(lambda,z)=8 H_(4lambda)(2z).

At zero time, L058 gives F(0,z)=Xi(z), and L018 identifies its zeros
with s=1/2+iz in the ordinary open critical strip. Therefore local
zeros satisfy |Im z|<1/2; source H_0 zeros satisfy |Im z|<1.
Apply Theorem3.2 with t0=0,y0=1 and t=4lambda for lambda>0.
Conjugation, from L058 (equivalently the source symmetry), supplies
the lower half-plane bound as well. Converting source zeros 2zeta
back to local units gives

    |Im zeta| <= (1/2)sqrt(1-8lambda) <= 1/2.             (2)

Here 0<4lambda<=1/5, so the square root is positive. At lambda=0,
use the initial ordinary-strip bound directly, not the theorem's
strict t>t0 conclusion. Hence (2) with the non-strict final bound
holds throughout the closed band. If a tail zero were purely
imaginary, (2) would give |zeta|<=1/2, contradicting |zeta|>100.
No simplicity or zero motion is needed for this location theorem.

### Realification, multiplicities and convergence

The elementary conjugate rank-one identity used here is the one in
W. Ding, L. Qi and Y. Wei, *Inheritance Properties and Sum-of-Squares
Decomposition of Hankel Tensors: Theory and Algorithms*,
arXiv:1505.02528v4 (17 September 2015), Section3.2, printed p12:
https://arxiv.org/pdf/1505.02528v4#page=12 .
Only the displayed conjugate-block algebra is imported; no finite
rank, nonsingular-leading-block or positive-semidefinite theorem
from that section is assumed. To apply it, L919's scalar zeta^(-4)
has been absorbed as (zeta^(-2))^2 in w. This is an exact square,
with no square-root choice and no replacement by a modulus square.

Write a=Re w and b=Im w, real vectors. Since w(-zeta)=w(zeta),
these vectors do not depend on the representative of an opposite
class. On a pair of distinct conjugate classes, the two w vectors
are conjugates, even if a representative was chosen with opposite
sign. Their sum of rank-one terms is exactly

    w w^T + conjugate(w) conjugate(w)^T
        = 2 a a^T - 2 b b^T.                            (3)

Both classes have the same multiplicity, by L058. For multiplicity
m, (3) is multiplied by m; equivalently both classes occur m times
in the opposite-pair multiset. A conjugation-fixed opposite class
is real or purely imaginary: conjugate(zeta)=zeta or -zeta. The
purely imaginary case is excluded from the tail by (2); a real
class has b=0 and contributes the nonnegative matrix a a^T once
per multiplicity copy. Thus there is no extra division by two.

Define U=sum a a^T and V=sum b b^T over every strict-tail opposite
class, with all its copies. These sums converge in matrix norm:

    ||a a^T||+||b b^T|| = ||a||^2+||b||^2 = ||w||^2
       = |zeta|^(-4)+40000|zeta|^(-8)
                         +1600000000|zeta|^(-12).

L919(10) at powers 4,8,12 bounds the full sum. Its version at an
arbitrary radial cutoff T>=100 makes the remaining sum tend to zero
uniformly in lambda. Hence all regrouping in (3) is absolutely
justified, and both U,V are positive semidefinite with

    E=U-V.                                               (4)

This is a pointwise definition at each parameter with uniform tail
bounds. It asserts neither continuity of a sharp radial cutoff nor
a continuous enumeration of zeros. Boundary zeros remain in A.

### The opposing component and its complete bound

For zeta=x+iy, r=|zeta|, put q=1/zeta. For every positive integer m,
factor the difference q^m-conjugate(q)^m to obtain

    2|Im q^m| <= |q-conjugate(q)| m |q|^(m-1),
    |Im zeta^(-m)| <= m |y| r^(-m-1).                    (5)

Indeed the factor multiplying q-conjugate(q) is a sum of m terms,
each of modulus |q|^(m-1), and |Im q|=|y|/r^2. This elementary
estimate supplies the effective specialization; no new strip or
zero-count estimate is being reproved. Applying (5) at m=2,4,6
and then |y|^2<=1/4 from (2) gives

    ||b||^2 <= (1/4)[4r^(-6)+640000r^(-10)
                                   +57600000000r^(-14)]
            = r^(-6)+160000r^(-10)+14400000000r^(-14).    (6)

Use L919(10) at T=100, for p=6,10,14, and its proved log100<5:

    sum_(|zeta|>100) |zeta|^(-p) <= T_p,
    T_p = [4p/(5(p-1))]100^(1-p)(5+1/(p-1)).             (7)

This counts all complex zeros in opposite classes with their full
multiplicities, pays every remote shell and requires no tail
reality. Combining (6)-(7),

    trace V = sum ||b||^2 <= T_6+160000T_10+14400000000T_14
       = 39/78125000000 + 23/31640625000000
                                +2079/3300781250000000000
       = epsilon_*.                                     (8)

For any real unit vector c, Cauchy-Schwarz and (4) give

    c^T E c = sum (c^T a)^2 - sum (c^T b)^2
            >= -sum ||b||^2 >= -epsilon_*.

Both square sums are convergent by the preceding norm estimate;
no conditionally convergent subtraction is used. This proves the
one-sided bound. Its positive part U is retained, not estimated by
epsilon, so it makes no assertion that ||E||<=epsilon.

The exact rounding reserve is

    epsilon-epsilon_* = 9686113/133681640625000000000 > 0,
    B/100-epsilon = 5641/10^11 > 0,
    B/epsilon = 11382.

Thus the test (1) passes in exactly L919's scaled matrix units.
The conditional head implication follows by adding quadratic forms
and congruence by the invertible D. Its premise remains unresolved.

### Finite verification and qualifications

Run `python3 scripts/heat/one-sided-conjugate-tail-2147.py`.
All 14 exact arithmetic checks pass, with no failures. The full finite certificate is
`scripts/heat/one-sided-conjugate-tail-2147.json`; its exact operands,
weighted terms, rounding/threshold reserves and all checks were
inspected. It verifies rational arithmetic only. The strip theorem,
its zero-time endpoint treatment, multiplicities, algebraic squares,
regrouping and complete tail are justified above and by L919.
No quadrature, finite zero census, head sweep, cutoff change, grid
refinement or numerical inference about RH is involved.

### Independent conceptual audit, 21 November 2026 (step2149)

The entire stated closed-band lower bound (1) is accepted, with the
unchanged constants, cutoff and multiplicity convention. No mathematical
defect was found. This verifies the existing quantitative specialization;
it produces neither a stronger estimate nor a new general theorem.
The head implication remains conditional.

**Normalization and endpoints.** L019's explicit kernel is exactly
4Phi(u/2): multiplication by four produces coefficients 8pi^2 and
-12pi and exponents 9u/2, 5u/2, and 2u. Substitution u=2w contributes
another factor two, changes the heat exponent to 4lambda*w^2 and
changes cos(zu) to cos(2zw). Thus the source time and spatial argument
in L919 really are 4lambda and 2z. L018's open critical strip implies
|Im zeta|<1/2 at lambda=0; multiplication by two gives the source
height bound 1. For every lambda in (0,1/20], Polymath Theorem3.2 with
t0=0 and y0=1 applies at the strictly later time 4lambda. Its height
bound, divided by two, has square 1/4-2lambda, ranging from below 1/4
down to 3/20. Real-type symmetry supplies the lower half-plane with
the same multiplicities. This checks both endpoints without extending
the theorem to t=t0, invoking simple-zero motion, or assuming RH.

**Classes and infinite realification.** The involution zeta -> -zeta
has no fixed zero because F(lambda,0)>0. Even reciprocal powers make
w independent of the representative. A nonreal, nonimaginary class
and its conjugate are distinct and have equal multiplicity; a real
class is fixed. A purely imaginary tail class is impossible by the
height bound. In (3), a class pair of multiplicity m contributes
2m aa^T-2m bb^T. Summation over both classes supplies two copies
of aa^T and two of bb^T for each multiplicity copy, reproducing
exactly those factors.
A real class contributes m aa^T and nothing to V. There is no second
division by two after L919 has already passed to opposite classes.

For any radial cutoff T>=100 the sum of the norms of the U and V
summands beyond T is bounded by the weighted sum of L919(10) at
p=4,8,12 with weights 1,40000,1600000000. Each bound tends to zero
uniformly on the closed time band. The same bound controls the
original algebraic rank-one series. Hence taking conjugation-invariant
finite radial sums and passing to the limit gives E=U-V in matrix
norm. Both Gram sums are positive semidefinite and absolutely
convergent. No continuous zero labeling, continuity of the sharp
head, shell truncation, or conditional interchange has been used.
Zeros on radius 100 belong to A at every time, as required.

**Opposing cost and ordering.** The difference-of-powers factorization
has m summands, all of modulus |q|^(m-1), and
|q-conjugate(q)|=2|Im zeta|/|zeta|^2. It therefore gives (5) also
when the imaginary part vanishes. Squaring the three component
bounds and using |Im zeta|^2<=1/4 gives exactly the powers 6,10,14
and weights 1,160000,14400000000 in (6). L919(10) counts every
strict-tail class with multiplicity. For a real unit vector c,
the convergent sum of (c^T b)^2 is at most trace V, while the
convergent sum of (c^T a)^2 is nonnegative. This proves the claimed
real quadratic-form lower bound, not an absolute-norm bound. Adding
a separately paid head margin and applying invertible congruence by D
is valid; no such head premise was inferred from the tail.

Run `python3 scripts/heat/one-sided-conjugate-tail-audit-2149.py`.
The script independently reconstructs the integrated power bound as

    (4p/5)100^(1-p)(5/(p-1)+1/(p-1)^2),

checks all three weighted contributions, every stored finite comparison,
the exact epsilon and B/100 reserves, endpoint scaling and decimal
rounding. All 37 checks pass. The full certificate is
`scripts/heat/one-sided-conjugate-tail-audit-2149.json`; its complete
tail and checks fields were inspected. The original certificate remains
byte-for-byte unchanged. This is rational arithmetic verification only;
the analytic obligations are checked above, not by that program.

An auxiliary audit probe incorrectly conjectured that the original
display 4.999275435 times 10^(-10) was rounded down. Its failed comparison
is preserved in `scripts/heat/one-sided-conjugate-tail-display-probe-2149.json`
with the corresponding program. Exact adjacent-decimal comparisons
instead confirm that the original display was already rounded up.
No correction to the corollary or its constants is needed.

Direct mathematical inputs remain L018,L058,L919. L019/L063/L874
are inherited through L919's normalization/product convention; the
audit adds no new premise or dependency. Finite-head feasibility,
other degrees, contacts, initialization and global assembly remain
unproved. Full matching Mathlib coverage remains unchecked.

## Mathlib

Full matching coverage for this one-sided heat-family tail result
is not checked. L919 records inspected supporting Jensen coverage
`AnalyticOnNhd.circleAverage_log_norm` at
https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Complex/JensenFormula.html#AnalyticOnNhd.circleAverage_log_norm .
That supports its existing count input, not this full corollary.
The imported de Bruijn strip theorem and effective realification
specialization have no matching Mathlib declaration checked here;
unknown availability is not evidence of absence.
