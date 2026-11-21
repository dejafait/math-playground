# Lemma 823: actual-theta cubic additive self-convolution factor

## Hypotheses

Use the actual positive theta kernel K of L019, its finite moments
m_j=M_(2j) from L021, and L795's normalization

\[
 \gamma(j)=\frac{j!m_j}{(2j)!},\qquad
 R_j=\frac{\gamma(j)}{\gamma(0)},\qquad
 P_3(x)=1-3R_1x+3R_2x^2-R_3x^3.
\]

Use only L791's audited actual coefficient enclosures through j=3,
with its inherited L778 uniform complex-disk analytic error and trusted
software contracts. These are computer-assisted informal inputs;
the transcendental backend is not independently attested or formally
verified. L791's matching model and model roots are not premises.
Fix symmetric finite-free additive convolution at degree d=3 in the
Marcus–Spielman–Srivastava convention stated below. Factors are real
and monic of degree three; roots with multiplicity are permitted.

## Conclusion

Put

\[
 h=\frac{R_2}{R_3},\quad A=\frac{3R_1}{R_3},\quad
 B=-\frac1{R_3},\quad
 p=A-3h^2,\quad q=-2h^3+Ah+B.
\]

These are well defined. The centered monic actual cubic is

\[
 C(y)=\frac{P_3(y+h)}{-R_3}=y^3+py+q.
\]

There is exactly one real monic cubic Q satisfying
Q boxplus_3 Q=C, namely

\[
 Q(y)=y^3+\frac p2 y+\frac q2.
\]

Its discriminant obeys the rigorous enclosure

\[
 40491457.417703\ \le\Delta(Q)\le\ 40491457.417704.
\]

Thus Q has three distinct real roots. This is a known-method finite
specialization and a local quantitative realization, not a novelty claim
or an advance beyond the checked sources in general root theory. It
establishes no higher-degree factor, common law, degree-uniform signs,
shifted/mixed transfer, all-degree mixed positivity or RH conclusion.
The separate step763 audit below passed under the same inherited contracts.

## Proof

**Imported operation and classifier.** A. Marcus, D. Spielman and
N. Srivastava, *Finite free convolutions of polynomials*,
[arXiv:1504.00350v2](https://arxiv.org/pdf/1504.00350v2),
3 July 2019, Definition1.1, equations(1)–(2), printed pp.2–3, define
for degree-d polynomials
f(x)=sum_i(-1)^i a_i x^(d-i),
g(x)=sum_i(-1)^i b_i x^(d-i),

\[
 (f\boxplus_d g)(x)=\sum_{k=0}^d(-1)^k x^{d-k}
 \sum_{i+j=k}\frac{(d-i)!(d-j)!}{d!(d-k)!}a_i b_j.
\]

Here a_0=b_0=1 and d=3. Their Theorem1.3 (Walsh) preserves real
rootedness when both degree-d inputs are real rooted; it is a forward
theorem, not an existence assertion for Q. We do not infer the factor
from hyperbolicity of C. The general finite coefficient/cumulant
inversion is in O. Arizmendi and D. Perales, *Cumulants for finite free
convolution*, [arXiv:1611.06598v2](https://arxiv.org/pdf/1611.06598v2),
7 March 2017, Proposition3.4/(3.2)–(3.3) and Proposition3.6, pp.7–8.
Only the elementary degree-three coefficient equations are needed here;
no general inversion theorem is reproved.

L. E. Dickson, *First Course in the Theory of Equations* (1922),
ChapterIV, Sections44–45, equations(11)–(12), printed pp.53–54
([PDF pages63–64](https://www.gutenberg.org/files/29785/29785-pdf.pdf)),
gives the real monic cubic discriminant and its complete classification:
positive means three distinct real roots, negative means one real root
and a nonreal conjugate pair, and zero means real roots with repetition.
For y^3+cy+e this discriminant is -4c^3-27e^2. We import the
classification, including equality, rather than reprove it. All
coefficients constructed here are real. The approved source comparison
is `drafts/literature/2026-11-05-theta-cubic-free-square-root-scope.md`;
the separately approved calculation scope is
`drafts/literature/2026-11-05-theta-cubic-free-square-root-calculation.md`.

**Normalization and centering.** L019/L021 give 0<gamma(j)<infinity,
so R_3>0. Dividing the displayed P_3 by -R_3 yields
H(x)=x^3-3h x^2+Ax+B. Direct expansion of H(y+h) cancels its
y^2 term and gives the stated p,q. The monic polynomial H has mean
root h, since its x^2 coefficient is -3h. This centers by the mean
root, without assuming those roots real.

To verify the normalization of the numerical input, L021's even Taylor
series gives, for G(w)=xi(1/2+sqrt(w)/2)/8=sum_j a_j w^j,

\[
 a_j=\frac{m_j}{8\,4^j(2j)!},\qquad
 \gamma(j)=8\,4^j j!a_j.
\]

Consequently the R_j here are exactly L791's actual ratios. They are
not the model multipliers or unnormalized moments. L795 gives the same
P_3 without an omitted factorial, binomial coefficient or radius factor.

**Exact factor and uniqueness.** Write a general real monic cubic as
Q=y^3+b y^2+c y+e. Substituting d=3 in the imported coefficient formula
gives exactly

\[
 Q\boxplus_3 Q
 =y^3+2b y^2+(2c+\tfrac23 b^2)y+
                   (2e+\tfrac23 bc).
\]

Indeed the cross weights at k=2 and k=3 are respectively
(2!2!)/(3!1!)=2/3 and (2!1!)/(3!0!)=1/3; the latter occurs twice.
Matching C first forces 2b=0, then 2c=p and 2e=q. Thus the asserted
Q is the unique real monic solution and substitution proves its exact
self-convolution identity. This is an algebraic identity for actual
p,q, not a comparison of uncertain interval endpoints.

**Complete finite sign certificate.** Reproduction command:

`python3 scripts/central-jacobi/cubic_free_square_root_622.py`

Complete evidence:
`scripts/central-jacobi/cubic-free-square-root-certificate-622.json`.
All endpoint strings are converted exactly to Python integer fractions.
Addition uses endpoint sums; multiplication takes the minimum and
maximum of all four endpoint products; division first verifies a
denominator excludes zero and uses its reciprocal interval. Squaring
uses lower endpoint zero when an interval contains zero, otherwise
the smaller endpoint square, and always the larger endpoint square
as upper bound. There is no floating point or finite-precision rounding
in these operations. Correlated occurrences are enclosed independently,
which enlarges rather than invalidates the bound. Coarse printed
decimals use integer floor/ceiling and are separately checked to contain
the exact rational bounds.

The script verifies current hashes against step478's original hashes,
the source hash against both L791 and the L778 audit, and complete
equality of the inherited evaluator with step433's audited replay.
Both inherited audits have PASS status and no failures. It recomputes
every load-bearing actual_a enclosure for j=0,1,2,3 by adding
[-E_G/1600^j,E_G/1600^j] to the corresponding P_0 coefficient interval,
using the saved upper bound for the additional analytic error E_G.
This uses L778's uniform **complex** estimate on |w|<=1600 and
Cauchy's coefficient estimate, not differentiation of a real estimate.
It then checks the entire multiplication by 8*4^j*j! is enclosed
in the saved gamma interval and verifies all four gamma lower bounds
are positive. The exact inherited intervals, error additions, hashes,
relevant prior checks and new checks are saved in the certificate.
No quadrature, zero list, matching-model parameter or new evaluator is
used. The inherited analytic and backend contracts remain premises.

Canceling gamma(0) algebraically, the evaluation uses
h=gamma(2)/gamma(3), A=3gamma(1)/gamma(3),
B=-gamma(0)/gamma(3). The computed outward bounds include

\[
\begin{aligned}
 -432.911190&\le p\le-432.911189,\\
 -105.366979&\le q\le-105.366978,\\
 -216.455595&\le c=p/2\le-216.455594,\\
 -52.683490&\le e=q/2\le-52.683489.
\end{aligned}
\]

Evaluating -4c*c^2-27e^2 on the full rational intervals yields the
stated positive discriminant enclosure; its complete rational endpoints
are saved under `exact_bounds/discriminant` and were inspected in full.
There are 32 passing input/arithmetic/display checks and no failures.
The sign also follows without trusting the narrow displayed discriminant:
c<-216 and |e|<53 imply

\[
 \Delta(Q)>4\cdot216^3-27\cdot53^2=40234941>0.
\]

Dickson's imported classification therefore applies. Multiplicities
were not discarded: the algorithm would leave an interval containing
zero inconclusive unless exact equality were proved. Here strict
positivity certifies simplicity. Walsh preservation may now be applied
to Q and Q at degree three, but that forward consequence adds no
higher-degree assertion. Independent mathematical gaps remain open.

### Independent audit, 13 November 2026 — step763

The approved SPECIALIZE scope is
`drafts/literature/2026-11-13-theta-cubic-factor-audit-762.md`.
Reuse the inspected MSS definition, Arizmendi–Perales finite inversion
and Dickson cubic classifier cited above. This audit validates their
existing finite specialization; it adds no general root theorem or
claim beyond the sources checked. No mathematical defect was found.

**Actual normalization and exact algebra.** The positive moments give
R_3>0 independently of a numerical root computation. L021's entire
even expansion, evaluated at the imaginary argument corresponding to
xi(1/2+sqrt(w)/2), gives a_j=m_j/[8*4^j*(2j)!]. Hence
gamma(j)=8*4^j*j!*a_j, exactly as in the inherited coefficient evidence.
L795's degree-three coefficients are therefore precisely those in P_3.
Dividing by -R_3 gives x^3-3h*x^2+A*x+B; substituting x=y+h
gives y^3+(A-3h^2)y+(-2h^3+Ah+B). Neither operation assumes roots real.

In the alternating-sign MSS convention a general monic cubic
y^3+b*y^2+c*y+e has a_1=-b, a_2=c, a_3=-e.
The k=2 cross weight is 2/3; the two k=3 cross weights are 1/3.
Consequently its self-convolution has coefficients
(1,2b,2c+2b^2/3,2e+2bc/3), with the signs displayed in the proof
above. Matching a centered monic cubic forces b=0, c=p/2, e=q/2
in that order. This proves uniqueness over all real monic cubics,
and substitution proves existence for the exact actual coefficients,
not merely for their enclosures. The standard real cubic classifier
then applies to these real coefficients; equality/multiplicity cases
were retained in the imported theorem, though the strict bound below
excludes equality here.

**Inherited inputs and independent arithmetic.** Run
`python3 scripts/central-jacobi/audit_cubic_factor_763.py`.
The complete audit certificate is
`scripts/central-jacobi/cubic-factor-audit-763.json`.
The checker independently verifies every load-bearing j=0,1,2,3
coefficient/error/normalization record, strict gamma positivity, source
hashes against the two inherited audits, and complete equality of the
inherited evaluator with step433's audited replay. It also checks the
step622 implementation hash and preservation of all original evidence.
The full four inherited records, all new rational bounds, actual/required
thresholds and all 46 checks are saved; all pass, with no failures.
Complete relevant intervals and the new discriminant endpoints were
inspected, not inferred from a preview or a saved PASS flag.

The independently written functional interval operations use exact
Python integer/Fraction arithmetic. After each operation they round the
lower endpoint downward and the upper upward to multiples of 10^-100.
Addition uses the endpoint sums, multiplication all four products, and
division the reciprocal interval of a denominator excluding zero.
Squaring handles zero crossings; cubing uses its monotonicity on the
entire real line. This enclosing rounding only widens the exact real
range. No Decimal operation or transcendental evaluation is performed
by the new checker. For the inherited coefficient inclusion tests,
the error additions and normalization products are instead kept exact.

Independently of step622's association of operations, the audit uses
q=B+h*(A-2h^2) and

\[
 \Delta(Q)=-\frac{2p^3+27q^2}{4}.
\]

The complete resulting intervals fit every original printed coefficient
bound and the claimed discriminant enclosure
[40491457.417703,40491457.417704]. The original exact rational
discriminant endpoints also fit that displayed interval. As a second,
coarse sign check, the new full c,e bounds satisfy c<-216 and |e|<53,
so Delta(Q)>4*216^3-27*53^2=40234941>0. Dickson's classification
therefore certifies three distinct real roots. Walsh preservation is
only a permissible forward consequence after this independent sign
test, not a premise for factor existence or hyperbolicity.

The complex-disk estimate for G-P_0 remains L778's audited analytic
input: Cauchy's coefficient estimate is applied on |w|=1600 to that
analytic difference, not to a merely real pointwise error. The audited
transcendental evaluator, its original input enclosures and its software
contracts remain trusted premises; this audit does not independently
attest its binary or rebuild its numerical integration. Model roots,
new quadrature and zero lists are unused. All degree-uniform,
shifted/mixed and RH-level gaps stated above remain open.

## Mathlib

Full matching coverage is unchecked, including this actual coefficient
certificate and finite-free self-convolution specialization. No theorem
absence or formal verification is claimed. The standard cubic
classification and coefficient identities are used with the precise
citations and elementary specialization above.
