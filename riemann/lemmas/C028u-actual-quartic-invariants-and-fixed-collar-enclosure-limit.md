# Corollary C028u: actual quartic invariants and fixed-collar enclosure limit

## Hypotheses

Use C028d's actual monic reciprocal Jensen polynomial P_4, its centered
Q_4(y)=P_4(y-b_1), and b_j=j!*I_(2j)/((2j)!*I_0), j=1,...,4.
Here I_(2j) are L021's full-theta half-line moments. Actual roots may
be complex and have multiplicity; all their power sums below are formal
algebraic sums, with no conjugation. Use C028q's actual cubic convention
and S_2=b_1^2-b_2>0.

For the reference, use exactly C028t's theta probability plus two positive
unit atoms at a,b and its degree-four monic orthogonal polynomial.
Its centered empirical root moments V,T,Q divide by4, with g=T/V^(3/2)
and k=Q/V^2. Fix B=[-1/4,1/4]x[3/4,5/4], x0=(0,1), and both affine
orientations e=+1,-1. Assume L917/audit197's unchanged complete panel0
moment containment under L037's Decimal-library contracts. This includes
I_8 as well as I_0,I_2,I_4,I_6, on the closed panel containing lambda=0.
No source refinement, actual-root reality, global image or RH assumption
is made. The finite propagation uses exact rational outward arithmetic.

## Conclusion

Write Q_4(y)=y^4+q_2*y^2+q_3*y+q_4. Then

    q_2=-6*(b_1^2-b_2),
    q_3=4*(b_3-3*b_1*b_2+2*b_1^3),
    q_4=b_4-4*b_1*b_3+6*b_1^2*b_2-3*b_1^4.

Its formal centered empirical quantities and normalized target are

    V_actual=-q_2/2=3*S_2>0,
    T_actual=-3*q_3/4, Q_actual=q_2^2/2-q_4,
    gamma=T_actual/V_actual^(3/2), k_actual=Q_actual/V_actual^2.

The saved conditional calculation encloses

    -744/1000 < gamma < -725/1000,
    1963/1000 < k_actual < 2010/1000.

A real affine change of the reference roots, centered and scaled to
variance V_actual with sign e, matches the monic Q_4 exactly if and only
if e*g=gamma and k=k_actual. This is a finite coefficient criterion,
not proof that a parameter solution exists.

The single natural Cramer-polynomial interval evaluation prescribed in
attempt1925 produces the following full Gram-determinant enclosure on B:

    [-438269648433368794543018463498687592783409986321/10^50,
      332483056580617137275351700964754866217649303471/(5*10^49)]. (1)

This enclosure contains0; it lies strictly inside[-4383/10^6,6650/10^6].
Thus that implementation cannot perform its required Gram divisions.
It reaches neither a residual-range exclusion nor a Krawczyk inclusion
for either orientation. This is an inconclusive enclosure failure;
the exact positive Gram matrix is not singular. No matching,
nonmatching, outside-collar result, uniform-degree cost or RH claim follows.
The formula specialization and arithmetic are reproduction of known
methods, not a new discovery beyond the assessed sources.

## Proof

### Coefficients and affine/Newton equivalence

Specialize C028d's coefficient convolution at d=4. Its linear coefficient
vanishes identically after translation, and the k=2,3,4 terms are exactly
the three displayed q's. For a monic depressed quartic, Newton's identities
give P_1=0,P_2=-2q_2,P_3=-3q_3,P_4=2q_2^2-4q_4. Divide by4 to obtain
the displayed formal moments. These identities hold for algebraic roots
with multiplicity even when they are complex; they are not absolute
power sums. The cubic normalization agrees with C028q at d=4.

Let m be the reference empirical mean, and put
sigma=e*sqrt(V_actual/V), translation=-sigma*m. C028t's positive reference
measure has four simple real zeros, hence V>0. The affine reference roots
then have empirical mean0, variance V_actual, third moment sigma^3*T,
and fourth moment sigma^4*Q. The third and fourth moments match precisely
when e*g=gamma and k=k_actual. With leading coefficient1 and equal first
four power sums, Newton's triangular identities give equality of every
coefficient of the two degree-four polynomials. Conversely equality of
the polynomials gives equality of those sums. This proves the criterion
without assuming reality of actual roots or existence of any matching sites.

### Imported construction and verification methods

Reuse Gautschi, *Orthogonal Polynomials: Computation and Approximation*,
OUP2004, Section2.1.1, Theorem2.1,(2.1.1)-(2.1.3),pp52-54, as assessed
in source-notes1908/1920 and instantiated in C028t. The positive full-theta
density has every absolute moment; two positive atoms preserve strictly
positive norm for every nonzero polynomial. Thus the moment construction
applies. The factor3 normalizing the modified measure cancels from the
coefficient equations. Its probability base moments have no factorials:
beta_0=1,beta_2=I_2/I_0,beta_4=I_4/I_0,beta_6=I_6/I_0 and odd beta_j=0.

For prospective nonlinear verification the imported authority is Rump,
*Verification methods: Rigorous results using floating-point arithmetic*,
Acta Numerica19(2010),287-449, corrected author PDF,
[Theorem13.3,(13.1)-(13.9),PDF pp87-89](https://www.tuhh.de/ti3/rump/intlab/ActaNumerica2010.pdf),
and interval range inclusion (5.16)-(5.17),PDF p28. Source-notes1924
assesses its full statement/proof. For C^1 f and a complete box-Jacobian
enclosure, strict inclusion of -R*f(x0)+(I-R*J(B))*X in int(X) is a
sufficient root certificate, X=B-x0. Failure to establish this condition
does not show nonexistence. Here f_e=(e*g-gamma,k-k_actual). The Gram
division failure occurs before this condition can even be evaluated.
No general construction or verification theorem is reproved.

### Full finite evidence and its inclusion argument

Reproduce with

```text
python3 scripts/heat/two-site-actual-collar-1925.py
python3 scripts/heat/two-site-actual-collar-check-1925.py
```

Complete outputs have the same stems with .json. The producer checks
every accepted audit197 input hash, its passed status and empty failure
list, and equality of all five selected raw moment records to the accepted
audit. It retains complete original decimal endpoints, including I_8;
it checks that panel0 is exactly[0,1/5120]. I_0 has positive lower bound.
The actual b_j retain j!/(2j)!, and every actual variance divisor is
strictly positive in the finite propagation. No moment midpoint replaces
an interval. Repeated use of an input may overestimate; no unproved
correlation is used to narrow any range.

For reference moments s_j=beta_j+a^j+b^j, j=0,...,7, the equations are
H*c=-t, H_ij=s_(i+j),t_i=s_(i+4),0<=i,j<=3. The producer collects all
five Cramer determinants over rationals in beta_2,beta_4,beta_6,a,b,
then their two partial derivatives. It evaluates every collected polynomial
once on B. At the fixed point x0 it first substitutes exact sites before
evaluation, recomputes C028t's full quotient and normalization derivatives,
and takes the exact rational inverse of each oriented point-Jacobian
midpoint. The independent check verifies both midpoint inverses by exact
matrix multiplication. Neither is used after the collar divisor fails.

The arithmetic helper is the audited1921 Fraction implementation, with
grid10^(-50): lower endpoint floor, upper endpoint ceiling; multiplication
uses all four endpoint products, division rejects a zero-containing
divisor, and square roots satisfy exact squared-endpoint inequalities.
The new integer-power operation uses the endpoint powers and includes0
for an even positive power whose input crosses0. This is the exact range
of that univariate power. Induction over each arithmetic expression
therefore supplies inclusion. In particular(1) encloses the whole
collar determinant despite overestimation.

The checker independently replays all6,530 expression nodes, all result
copies and the complete division records. A dual permutation expansion
of the unspecialized moment determinants, instead of the producer's
Laplace expansion followed by differentiation, agrees in every coefficient
of all15 polynomial components. It also checks complete input provenance,
the target's quoted weaker rational bounds and both midpoint inverses.
The saved checker has no failures. These are finite arithmetic and
symbolic checks, not independent Decimal verification or a nonlinear
existence certificate. The producer contains an unexecuted branch for a
paid collar divisor; no correctness of unexecuted Krawczyk arithmetic is
needed or claimed for this result.

The exact Gram determinant is positive by the positive-measure argument
in C028t, but(1) has strictly negative lower and positive upper endpoints.
One must stop before reciprocal evaluation. The same divisor is used for
both affine orientations, so neither reaches its full residual/Jacobian.
No changed representation, subdivision, site/radius sweep, nonlinear
solver or source-moment refinement was performed. This establishes only
the stated bound and the implementation's inconclusiveness. The main
all-degree positivity and H_d=o(d) gaps remain open.

## Mathlib

Full matching coverage is unchecked; unknown availability is not absence.
The conditional Decimal input and finite rational certificate are not
formalized in Lean. Newton identities and finite matrix arithmetic are
standard supporting methods, with no claim here of an inspected matching
Mathlib theorem. Reference: https://leanprover-community.github.io/mathlib4_docs/.
