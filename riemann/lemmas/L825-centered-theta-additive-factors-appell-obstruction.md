# Lemma 825: centered theta additive factors fail common-symbol lowering

## Hypotheses

Use the actual positive theta kernel K of L019, its finite positive moments
m_j=M_(2j) from L021, and L795's actual polynomials

\[
 \gamma(j)=j!m_j/(2j)!,\quad R_j=\gamma(j)/\gamma(0),\qquad
 P_d(x)=\sum_{j=0}^d(-1)^j\binom dj R_jx^j.
\]

Only d=2,3 is considered. Use L791's audited gamma intervals through j=3,
under L778's uniform complex analytic error and the trusted evaluator/software
contracts reviewed in steps433/478. These are computer-assisted informal
inputs, not formally verified or independently attested transcendental
computations. No fitted model, L823 cubic calculation, L824 quartic result,
real-rootedness or RH assumption is used. Fix the symmetric finite-free
additive operation at each degree in the convention below.

## Conclusion

Set

\[
 h_2=R_1/R_2,\quad h_3=R_2/R_3,\qquad
 u_2=1/R_2-h_2^2,\quad u_3=3R_1/R_3-3h_3^2,
\]
\[
 v_3=-1/R_3+3R_1h_3/R_3-2h_3^3.
\]

The centered monic polynomials are

\[
 C_2(y)=P_2(y+h_2)/R_2=y^2+u_2,\qquad
 C_3(y)=P_3(y+h_3)/(-R_3)=y^3+u_3y+v_3.
\]

For each d=2,3 there is exactly one real monic Q_d satisfying
Q_d boxplus_d Q_d=C_d. They are

\[
 Q_2(y)=y^2+u_2/2,\qquad Q_3(y)=y^3+(u_3/2)y+v_3/2.
\]

Their entire derivative defect is the constant

\[
 Q_3'(y)-3Q_2(y)=\Delta=(u_3-3u_2)/2,
 \qquad 9.582501<\Delta<9.582502.                 \tag{1}
\]

Thus no one formal constant-coefficient differential symbol f(D) in these
fixed monic centered coordinates has Q_d=f(D)y^d for both d=2,3.
This stops only that common-symbol realization. Degree-dependent symbols,
other realizations, individual factor signs, actual polynomial hyperbolicity,
mixed/shifted transfer and RH remain unresolved by this result. This is a
known-method specialization; its local arithmetic passed the separate step631
audit under the inherited contracts and is not claimed as a discovery beyond
the sources checked.

## Proof

**Imported operation and necessary condition.** Marcus, Spielman and
Srivastava, *Finite free convolutions of polynomials*,
[arXiv:1504.00350v2](https://arxiv.org/pdf/1504.00350v2), 3 July2019,
Definition1.1, equations(1)–(2), printed pp.2–3, define for monic
p(y)=sum_i(-1)^i a_i y^(d-i), q(y)=sum_i(-1)^i b_i y^(d-i),

\[
 (p\boxplus_d q)(y)=\sum_{k=0}^d(-1)^k y^{d-k}
  \sum_{i+j=k}\frac{(d-i)!(d-j)!}{d!(d-k)!}a_ib_j.
                                                        \tag{2}
\]

This algebraic formula does not require real roots. No application of its
real-root preservation theorem is made. Arizmendi–Perales,
[arXiv:1611.06598v2](https://arxiv.org/pdf/1611.06598v2), 7 March2017,
Propositions3.4/3.6 and proofs, printed pp.7–8, supply general monic
coefficient/cumulant inversion without a positive root premise. We need only
the degree2/3 equations of (2), written explicitly below to fix the actual
normalization and prove uniqueness, rather than reprove general inversion.

Campbell, *Free infinite divisibility, fractional convolution powers, and
Appell polynomials*, [arXiv:2412.20488v3](https://arxiv.org/html/2412.20488v3),
18 December2025, (1.1), Section1.4/(1.24)–(1.26), gives the Appell lowering
condition for a common formal constant-coefficient symbol. Indeed D commutes
with f(D) on polynomials (only finitely many terms act in each degree), so
D f(D)y^3=3 f(D)y^2. This necessary identity requires no entire or
Laguerre–Pólya hypothesis. The centered monic orientation here is specified
directly; no transport of factors through reciprocal Jensen orientation
is assumed. The prior SPECIALIZE assessment is
`drafts/literature/2026-11-05-centered-theta-factor-appell-test.md`.

**Centering and all coefficient equations.** Positivity of the actual
moments implies R_2,R_3>0. The two monic polynomials before translation are

\[
 x^2-2(R_1/R_2)x+1/R_2,\qquad
 x^3-3(R_2/R_3)x^2+3(R_1/R_3)x-1/R_3.
\]

Substitution x=y+h_d cancels their next-to-leading terms. Expanding all
remaining terms gives exactly C_2,C_3 above, including the constant v_3.
The center is unique since translating a monic degree-d polynomial changes
its next coefficient by d h. No degree-dependent dilation is introduced.

For an arbitrary real monic quadratic q=y^2+a y+b, (2) gives

\[
 q\boxplus_2 q=y^2+2ay+2b+a^2/2.
\]

Equality with C_2 forces successively a=0 and b=u_2/2, proving existence
and uniqueness. For an arbitrary real monic cubic q=y^3+a y^2+b y+c,
the complete expansion of (2) is

\[
 q\boxplus_3 q=y^3+2ay^2+(2b+2a^2/3)y+2c+2ab/3.
\]

Equality with C_3 forces a=0, b=u_3/2, c=v_3/2. Conversely these values
give every coefficient of C_3, proving existence and uniqueness, including
the constant equation. Differentiation now cancels both the quadratic
and linear coefficients of Q_3'-3Q_2; its constant is Delta. There is no
uncompared coefficient and no sign premise in these identities.

**Certified actual arithmetic.** Full evidence is
`scripts/central-jacobi/centered-appell-629.json`; reproduce with
`python3 scripts/central-jacobi/centered_appell_629.py` from this notebook.
The script imports only the Q interval class of step478's rational checker.
Its endpoints are exact Fractions. After each addition, multiplication
and reciprocal operation they round outwards to the 10^(-100) grid by
integer floor/ceiling. Multiplication takes extrema of all four endpoint
products; squaring accounts for a zero-crossing interval; division checks
a strictly nonzero denominator. These elementary enclosure operations
need no Decimal backend for the new arithmetic. Correlations are enlarged,
never presumed independent for actual data.

The complete gamma and actual-a endpoints were inspected before use,
along with the complete relevant step478 audit checks, failures and
inherited error. Current hashes of the source and L791 certificate match
step478. The entire inherited evaluator equals the step433 replay, both
saved audits report PASS with no failures, and all step478 checks pass.
For j=0,1,2,3 the new calculation explicitly retains the coefficient
error E_G/1600^j with 0<E_G<3.141*10^(-48), verifies containment in each
saved actual-a interval, and verifies gamma(j)=8*4^j*j!*a_j containment
and strict positivity. The analytic Cauchy estimate and original evaluator
contracts remain premises of L778/L791; these finite checks do not
independently rebuild or attest that evaluator.

It then encloses R_1,R_2,R_3, both centers, all depressed coefficients,
all factor coefficients and Delta using the entire saved gamma intervals.
For orientation only, outward six-place coefficient enclosures are

\[
 -150.692065\le u_2\le-150.692064,\quad
 -432.911190\le u_3\le-432.911189,\quad
 -105.366979\le v_3\le-105.366978.
\]

The computation uses the full rational endpoints, not these displays.
The exact saved Delta interval is strictly inside (9.582501,9.582502),
which proves (1). The algebraically identical rearrangement

\[
 \Delta=\frac32\left(R_1/R_3-(R_2/R_3)^2-1/R_2+(R_1/R_2)^2\right)
\]

also has an enclosure strictly on the positive side and overlapping the
first. This is a consistency check, not an independent analytic audit.
The report passes 27 finite checks with no failures and retains complete
input, intermediate and output endpoints, hashes and the required exact
threshold zero. No additional quadrature, precision campaign, adjusted
normalization or further degree was tested. A nonzero constant contradicts
the imported necessary lowering condition and gives precisely the stated
restricted stop; it says nothing against RH.

### Separate finite audit, 5 November 2026 — step631

The prior SPECIALIZE assessment
`drafts/literature/2026-11-05-centered-theta-appell-audit-scope.md`
covers exactly this audit. No mathematical defect was found. In particular,
the two translations are performed after monic normalization, with no
reversal or dilation. The displayed general self-convolution equations
contain every coefficient, including 2c+2ab/3 for the cubic constant.
Their next-to-leading equations force a=0, and their remaining equations
then force precisely the stated b,c. This proves uniqueness over the
reals without any root assumption. The entire derivative defect has
coefficients (0,0,Delta) in descending order. A formal f(D) acts finitely
on each polynomial and commutes with D, so nonzero Delta contradicts
its required lowering identity even without analyticity or an LP premise.

L021's expansion and G(w)=xi(1/2+sqrt(w)/2)/8 give
a_j=m_j/[8*4^j*(2j)!] and gamma(j)=8*4^j*j!*a_j. L778's bound (5)
is uniform for the analytic difference on the full closed complex disk
|w|<=1600. Thus the Cauchy error is E_G/1600^j, additional to the
original polynomial coefficient widths. All four additions, gamma
normalizations and strictly positive denominator intervals were checked
using complete endpoints. No real-axis estimate was substituted.
The complete inherited evaluator matches step433's saved replay; all
six step629 input hashes, the L791 source hash and the step478/433
source hashes match. The saved audits and their complete relevant checks
and failures were inspected. This reuses their analytic/software
premises; it does not independently verify the transcendental backend.

Independent checker: `python3 scripts/central-jacobi/audit_631.py`.
It imports no step478 Q arithmetic for its independent calculation.
Its rational endpoints use exact Fraction arithmetic without rounding:
addition adds endpoints, multiplication takes all four endpoint products,
reciprocal reverses the endpoints after excluding zero, and squaring
uses zero as the lower bound when appropriate. Each operation therefore
encloses its real image. Enlarging correlated quantities preserves
containment of the actual values. Sparse multivariate rational expansion
independently checks every translated coefficient, the full finite-free
formula in both degrees, factor existence and every derivative coefficient.
All thirteen saved numerical intervals contain their independent exact
recomputations, including the cubic constant. The full independent Delta
interval and its rearrangement both lie strictly inside
(9.582501,9.582502); the exact necessary threshold remains zero.

Full evidence is `scripts/central-jacobi/audit-631/audit-report.json`:
PASS, 100 checks, no failures. It retains complete exact endpoints,
symbolic expansions, hashes and actual/required thresholds. A separately
labelled same-code replay reproduces every field of the original
step629 certificate in `scripts/central-jacobi/audit-631/centered-appell-629-replay.json`;
this consistency check is distinct from the independent arithmetic.
The first checker run stopped on step433's string-list check schema,
before the numerical enclosure stage; its full failure report is preserved
as `scripts/central-jacobi/audit-631/audit-report-first-pass.json`.
The reader now handles that schema explicitly. No original program or
certificate was overwritten. This validates the finite restricted stop,
not an additional sign theorem, alternate realization or RH conclusion.

## Mathlib

Full matching coverage is unchecked. No presence or absence assertion is
made for this specialized factorization and arithmetic obstruction. Named
inputs are the cited finite convolution formula and Appell differentiation;
the inherited analytic evaluator and backend are not formally verified.
