# Lemma 827: six compensated reciprocal theta moments are Stieltjes feasible

## Hypotheses

Use L795's actual positive theta moments

\[
m_j=\int_0^\infty u^{2j}K(u)\,du\quad(j\ge0),
\qquad s_j=4^j(1/2)_j\frac{m_0}{m_j}\quad(0\le j\le5).
\]

Use only the finite polynomial evaluator and complex analytic error of
L778 and L791's coefficient normalization, not its fitted model or model
roots. Thus, for

\[
G(w)=\xi(1/2+\sqrt w/2)/8=\sum_{j\ge0}a_jw^j,
\qquad \gamma(j)=8\,4^j j!a_j,
\]

L778's saved coefficient intervals enclose the exact polynomial P_0,
and its analytic bound is

\[
|G(w)-P_0(w)|\le E_G<3.141\cdot10^{-48}\quad(|w|\le1600).
\]

The inherited analytic proof, directed Decimal integration, correctly
rounded exp/sqrt, provenance and software contracts are those of L778
and its step433 audit. These remain explicit trusted inputs. The new
finite arithmetic below uses exact Python integers and Fraction; neither
the inherited binary nor the new program is formally verified. This
result passed the separate finite audit in step641 below, subject to
these inherited contracts.

## Conclusion

Both real Hankel matrices

\[
H_0=(s_{i+j})_{i,j=0}^2,\qquad
H_1=(s_{i+j+1})_{i,j=0}^2
\]

are positive definite. Consequently there exists a positive Borel
probability measure \(\nu\) on \([0,\infty)\) with

\[
\int_0^\infty x^j\,d\nu(x)=s_j\qquad(0\le j\le5).
\]

This is one finite specialization of known truncated moment criteria.
It establishes neither a measure matching every j nor actual Bernstein
membership, a lower-oscillation theorem, polynomial real-rootedness,
mixed/shifted sign transfer or RH. An atom at zero is allowed; no
particular representing measure is identified. No novelty beyond the
sources checked is claimed.

## Proof

**Imported criterion.** R. E. Curto and L. A. Fialkow,
*Recursiveness, positivity, and truncated moment problems*, Houston
Journal of Mathematics **17**(4) (1991), 603–635,
[Theorem 5.1, printed p625](https://www.math.uh.edu/~hjm/v017n4/0603CURTO.pdf#page=23),
gives the following exact equality criterion for real data
\(b_0,\ldots,b_{2k+1}\), \(b_0>0\): positive representability on
\([0,\infty)\) is equivalent to

\[
(b_{i+j})_{i,j=0}^k\succeq0,\qquad
(b_{i+j+1})_{i,j=0}^k\succeq0,\qquad
(b_{k+1},\ldots,b_{2k+1})^T
   \in\operatorname{Ran}(b_{i+j})_{i,j=0}^k.
\]

The source criterion, including singular cases and equality of the last
moment, is imported, not reproved. The theorem and essential construction
and support cases were assessed in
`drafts/literature/2026-11-05-theta-gamma-reciprocal-moment-scope.md`;
the exact finite calculation was separately approved in
`drafts/literature/2026-11-05-theta-gamma-six-moment-test.md`.
Here k=2, b_j=s_j and b_0=1. Strict positive definiteness will make the
range condition automatic, so no singular numerical inference is used.

**Actual coefficients and all errors.** L791's normalization gives
\(\gamma(j)=j!m_j/(2j)!\). This is a coefficient identity for every
nonnegative j, irrespective of the fitted model's matching limit j=4.
Since \(4^j(1/2)_j=(2j)!/j!\), it follows that

\[
s_j=\frac{\gamma(0)}{\gamma(j)},\qquad s_0=1.
\]

Extract the first six coefficient intervals from
`scripts/actual-fredholm/fixed-pair-certificate-431.json`.
They enclose P_0 coefficients, not yet actual G coefficients. Cauchy's
coefficient estimate on the complex circle of radius1600 gives

\[
|a_j-[w^j]P_0|\le E_G/1600^j.
\]

The program adds a symmetric interval with this radius, using the
complete inherited upper endpoint for E_G, to each coefficient interval
before any normalization or division. The inherited quadrature widths
remain in place; this addition pays the theta, integration and cosh
tails as well. All six resulting lower endpoints are positive. Multiplying
by \(8\,4^j j!\) and dividing the resulting gamma intervals therefore
encloses all six actual s_j. We set s_0=1 exactly, rather than introduce
artificial interval uncertainty by dividing gamma(0) by itself.
For orientation only, s_1,...,s_5 are approximately
43.2806881, 2013.4169775, 99540.9592227, 5188424.4271840,
283433624.1302461; the full intervals, not these decimals, are used.

**Finite arithmetic and positive definiteness.** Every decimal input is
parsed as an exact rational. At each operation the lower endpoint is
rounded down and the upper endpoint up to a multiple of 10^-90 by
integer floor/ceiling. Addition uses summed endpoints; multiplication
uses extrema of the four endpoint products. For a nonzero interval
[l,h], reciprocation uses [1/h,1/l]. These operations enclose the exact
operation by interval monotonicity and inclusion. Thus induction over
the finite expressions retains the actual, correlated coefficients;
allowing independent endpoints only enlarges their enclosing set.
No independence assumption about the true s_j is made.

Form both full matrices from the same six intervals. Their leading
principal determinants are evaluated by the complete Leibniz expansion
(at most six terms, with exact permutation signs). The full certificate
gives the following conservative enclosures; parentheses are strict
except the exact entry 1:

| Matrix | Order1 | Order2 | Order3 |
| --- | --- | --- | --- |
| H_0 | 1 | (140.1990173, 140.1990174) | (5334110.4436894, 5334110.4436896) |
| H_1 | (43.2806880, 43.2806882) | (254353.281348, 254353.281350) | (396820791357.236416, 396820791357.236419) |

All six leading determinants are strictly positive. The matrices are
real symmetric, so the named Sylvester criterion proves positive
definiteness of both actual matrices. This uses all required leading
minors, not merely the two size-three determinants. In particular H_0
is invertible and its range is all of R^3, containing
\((s_3,s_4,s_5)^T\). Curto–Fialkow's full criterion now applies.
The zeroth moment equals 1, so the representing positive measure has
total mass1. This concludes only the stated six-moment assertion.

**Evidence, reproduction and limits.** Run
`python3 scripts/theta-gamma-moments/six_moments_639.py`.
The complete evidence is
`scripts/theta-gamma-moments/six-moment-certificate-639.json`:
status FINITE_STIELTJES_FEASIBLE, no failures. It retains all six original
coefficient intervals, each Cauchy error enclosure, actual a/gamma/s
intervals, both full matrices, every leading minor and the range reason.
Exact source hashes agree with L791's recorded source and L778's audit;
the complete inherited evaluator agrees with the audited step433 replay.
Every consumed evidence file is hash-checked unchanged after calculation.
These checks establish provenance, not independent transcendental
verification. The complete new load-bearing coefficient, moment and
minor intervals and provenance/error checks were inspected in step639.
No sixth fitted-model coefficient or ordinary floating-point output is
used. The separate step641 review below checks the new finite arithmetic.

This passes a necessary finite consistency test of the conditional
Mellin/Bernstein construction discussed in the existing source assessment.
It does not verify that construction's global hypotheses or produce its
infinite law. The bare-reciprocal and common-Favard failures concern
different premises and are not removed by this result. No automatic
degree extension or new sign mechanism follows.

### Independent finite audit — 5 November 2026, step641

Reused the pre-existing SPECIALIZE assessment
`drafts/literature/2026-11-05-six-moment-feasibility-audit.md` for exactly
this six-index statement. No mathematical defect was found. This is
independent validation of a local specialization of known methods, not
a new moment theorem or a sign result beyond the sources checked.

**Normalization and analytic input.** L018/L021 give
\(G(w)=\frac18\sum_{j\ge0}m_j w^j/[4^j(2j)!]\), because
\(\xi(1/2+\sqrt w/2)=\Xi(-i\sqrt w/2)\).
Thus \(m_j=8\,4^j(2j)!a_j\) and
\(\gamma(j)=j!m_j/(2j)!=8\,4^j j!a_j\) for every j. Combining this
with \(4^j(1/2)_j=(2j)!/j!\) proves the stated s normalization,
including j=5; L791's fitted matching model is not used. The underlying
even series removes the apparent square-root branch.

The inspected evaluator and step433 proof in L778 establish a complex
analytic remainder on the whole closed radius1600 disk. Cauchy's
formula on that circle therefore supplies \(E_G/1600^j\) with no extra
factorial, including j=0 and j=5. Coefficient intervals already contain
the cell-integration errors; their widths are retained while adding
the separate theta, infinite-u and cosh-tail error. All six original
intervals, six Cauchy additions, actual coefficients and gamma intervals
were checked before positive division. The analytic proof, directed
Decimal integration and exp/sqrt contracts of L778 remain imported
trusted inputs, rather than conclusions of this finite replay.

**Independent rational arithmetic.** Run
`python3 scripts/theta-gamma-moments/audit_641.py`. The checker imports
no arithmetic from the original program for its independent calculation.
It uses exact Fraction endpoints without intermediate rounding, starting
from the complete six original polynomial intervals and full error upper
endpoint. It checks that every original error, a, gamma and s enclosure
contains its independent result, that all six a and gamma lower endpoints
are positive, and that s_0 is exactly 1. Both full saved matrices are
checked entry by entry against the six s intervals and for symmetry.
Allowing independently varying intervals encloses the actual correlated
data; it does not assume those data are independent.

For a symmetric matrix with rows (a,b,c), (b,d,e), (c,e,f), the independent
size-three calculation uses

\[
\det H=adf+2bce-ae^2-dc^2-fb^2,
\]

and the size-two calculation uses ad-b^2. All entries are strictly
positive here, so squaring a positive interval [l,h] gives exactly
[l^2,h^2]. This expression differs from the original permutation loop.
All six independent leading-minor enclosures lie inside the saved
enclosures and have strictly positive lower endpoints. An additional
unrounded Leibniz check on the saved full matrix intervals confirms
that the original outward-rounded determinant intervals enclose their
claimed expressions. Every conservative bound in the displayed table
also contains the full saved interval. The independent endpoints are
serialized outwards to multiples of 10^-100 only after calculation;
the full evidence retains all coefficient stages, matrices and minors.

**Equality-moment theorem and provenance.** Both actual matrices are real
symmetric and all their leading principal minors are positive, so
Sylvester gives positive definiteness. At k=2 the imported
Curto–Fialkow Theorem5.1 requires the vector (s_3,s_4,s_5) in Ran H_0.
This is exactly the saved vector; H_0 is invertible, so its range is
R^3. The theorem supplies equality of all six moments on [0,infinity),
allowing an atom at zero. The fixed zeroth moment 1 gives total mass1.
There is no inferred singular rank, inequality in place of the last
moment, or assertion of strictly positive support.

The audit verifies every input hash saved by step639, the program hash,
the source hash in both L778's audit and L791's certificate, and equality
of the complete evaluator record with step433's replay. It executes the
unchanged original program with output redirected to
`scripts/theta-gamma-moments/audit-641/six-moment-replay-639.json`; every
certificate field, including runtime, matches the original. All six
consumed source/program/certificate hashes remain unchanged afterwards.
These are provenance checks, not independent transcendental verification.

Complete report:
`scripts/theta-gamma-moments/audit-641/audit-report.json`, PASS,
84 checks, no failures. The full selected input intervals, both matrices,
all six independent minor intervals, theorem-hypothesis record and all
check results were inspected. No degree extension, global Bernstein
membership, lower oscillation, mixed/shifted sign transfer or RH conclusion
was tested or established. Full matching Mathlib coverage stays unchecked.

## Mathlib

Full matching coverage for the actual six data and the cited truncated
Stieltjes theorem is unchecked. Supporting named inputs are Cauchy's
coefficient estimate and Sylvester's criterion; no matching Mathlib
theorem or formal verification is claimed. Unknown availability is not
evidence of absence.
