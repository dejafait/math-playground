# L829 — Actual Mellin factor passes the fixed first Laguerre test

## Hypotheses

Use exactly C828a's positive even density
\[
 P(x)=\sum_{n\ge1}(4\pi^2n^4e^{9x/2}-6\pi n^2e^{5x/2})
                 e^{-\pi n^2e^{2x}},\qquad p(x)=P(x)/Z,
 \quad Z=\int_{\mathbb R}P(x)\,dx>0.
\]
As in L828 Section2, set
\[
 M(s)=\int_0^\infty x^{2s}p(x)\,dx\quad(\Re s>-1/2),
 \qquad E(s)=\frac{\sqrt\pi\,4^{-s}M(s)}{M(0)\Gamma(s+1/2)}.
\]
Here \(x^{2s}=\exp(2s\log x)\), with the real logarithm for \(x>0\),
and \(M(0)=1/2\). Only the unconditional density and entire-continuation
construction in those results is used. No Bernstein representation,
product-class membership, real-zero premise, or RH is assumed.

The computer-assisted enclosure uses CPython3.15.2, libmpdec4.0.1 and
the documented Decimal arithmetic contract described below. Correct
implementation of this standard numerical backend and Python integer
arithmetic is a software assumption; this is not a formal verification
of either implementation.

## Conclusion

The actual factor satisfies the strict bounds
\[
 \boxed{\quad 0.0548<E'(0)^2-E(0)E''(0)<0.1226.\quad}
 \tag{1}
\]
Thus it passes this single necessary Laguerre condition. This does not
establish global Laguerre–Pólya or Runckel product-class membership,
any all-point or higher-order inequality, an Xi sign, or RH. The fixed
diagnostic is finished: neither more points nor more orders are inferred
as an authorized continuation. The result is a local actual-data
specialization of known tests, not a new preservation theorem or a
claimed discovery beyond the literature checked.

## Proof

### 1. Absolute differentiation and the scalar reduction

C828a Section1 proves boundedness of \(p\) near zero and the effective
shape of its superexponential tail, independently of any zero assertion.
For \(|s|\le1/8\), \(x^{2\Re s}\le x^{-1/4}\) on \(0<x\le1\).
Multiplication by \(1+|\log x|^2\) is integrable against a bounded
density there. On \(x\ge1\), the superexponential bound dominates
\(x^{1/4}(1+|\log x|^2)\). These are absolute majorants for the
integrand and its first two complex derivatives. Differentiation under
the Mellin integral is therefore valid, with the factor **2** retained
in each derivative of \(x^{2s}\).

Write \(J_j=\int_0^\infty(\log x)^jP(x)\,dx\), \(j=0,1,2\).
Normalization cancels, giving
\[
 \frac{M'(0)}{M(0)}=2\frac{J_1}{J_0},\qquad
 \frac{M''(0)}{M(0)}=4\frac{J_2}{J_0},\qquad J_0>0.
\]
Since \(E(0)=1\), it is positive near zero on the real axis, where
logarithmic differentiation of its definition gives
\[
 E'(0)^2-E(0)E''(0)
 =\psi'(1/2)-4\left[\frac{J_2}{J_0}
                         -\left(\frac{J_1}{J_0}\right)^2\right].
 \tag{2}
\]
The linear term \(-s\log4\) has zero second derivative; it has not
been omitted from the definition of E. Import
\(\psi'(1/2)=\pi^2/2\) from NIST DLMF **5.15.4**, at integer \(n=1\)
(empty finite sum), [exact formula](https://dlmf.nist.gov/5.15.E4).
This pinpoints the trigamma reference: 5.4.13, cited in the earlier
assessment, is the digamma value and alone would not pay this constant.
The additional exact formula was inspected during implementation;
no mathematical scope or hypotheses were changed.

### 2. Effective positive-series envelope

For \(x\ge0\), put \(v=\pi n^2e^{2x}\). The nth summand is
\(2v(2v-3)e^{x/2}e^{-v}>0\). Dropping its negative component gives
\[
 P(x)\le4\pi^2e^{9x/2-\pi e^{2x}}
             \sum_{n\ge1}n^4e^{-\pi(n^2-1)}
       <80e^{9x/2-\pi e^{2x}}.                 \tag{3}
\]
For clarity, the sum in (3) is less than two: its n=1 term is one;
its n=2 term is \(16e^{-3\pi}<16e^{-9}<1/2\), and for \(n\ge2\)
the ratio of consecutive terms is at most
\((3/2)^4e^{-5\pi}<(81/16)e^{-15}<1/2\).
Use also \(3<\pi\) and \(\pi^2<10\). The certificate encloses pi
and checks each stated elementary exponential inequality.

Let \(P_4\) retain precisely n=1,2,3,4. The ratio for the positive
upper envelopes of the omitted terms, starting at n=5, is at most
\((6/5)^4e^{-33}<1/2\). Consequently
\[
 0<P(x)-P_4(x)
 \le8\pi^2 5^4e^{9x/2-25\pi e^{2x}}
 <50000e^{-75}=:\epsilon_\theta\qquad(x\ge0).       \tag{4}
\]
Indeed \(9x/2-25\pi e^{2x}\) has negative derivative on this
half-line, so its maximum is \(-25\pi<-75\).
This is a uniform real-box bound, not a claim about complex boxes.

### 3. Singular endpoint and infinite tail

Take \(a=e^{-20}\), \(b=e\). On \([0,a]\), (3) gives
\(P(x)\le C_a=80e^{9a/2-3}\). Direct integrations give
\[
 \int_0^a|\log x|^jdx=a(1,21,442)_j\quad(j=0,1,2).
\]
Thus the endpoint contributions to \((J_0,J_1,J_2)\) lie respectively
in \([0,C_aa]\), \([-21C_aa,0]\), \([0,442C_aa]\).
No numerical box crosses this logarithmic endpoint.

For \(x\ge b>2\), each \(|\log x|^j\), \(0\le j\le2\), is at
most \(x^2\le e^x\). The latter follows since
\(x-2\log x\) is nondecreasing for \(x\ge2\), and is positive at 2.
Let \(H(x)=11x/2-3e^{2x}\). Since \(e^4>54\),
\(H(2)<-151\) and \(H'(x)\le11/2-6e^4<-318\) for \(x\ge2\).
Therefore every absolute tail is bounded by
\[
 \int_b^\infty|\log x|^jP(x)dx
 \le80\int_2^\infty e^{H(x)}dx
 <80e^{-151}/318<e^{-140}.                       \tag{5}
\]
The certificate checks \(e>2\), \(e^4>54\), and the final comparison.

### 4. Complete finite real-box enclosures

Substitute \(t=\log x\) on \([a,b]\):
\[
 \int_a^b(\log x)^jP_4(x)dx
     =\int_{-20}^1 t^je^tP_4(e^t)dt.               \tag{6}
\]
The precise two-stage cap, saved before numerical work, was
\((40\text{ decimal digits},8192\text{ boxes})\), then only if
inconclusive \((60,131072)\). Each grid is uniform with exact dyadic
width \(21/N\). There is no tolerance-driven extension or third stage.
Every integrand on every closed real interval is enclosed by ordinary
interval arithmetic in the positive expression
\[
 P_4(x)=e^{x/2}\sum_{n=1}^4 2v_n(2v_n-3)e^{-v_n},
 \qquad v_n=\pi n^2e^{2x}.
\]
The interval range times the exact width encloses that cell's integral;
addition encloses the full integral in (6). Squaring t uses its actual
interval square, including zero where appropriate. The uniform
additional absolute error from (4) is bounded by
\(21e20^j\epsilon_\theta\), since \(e^t\le e\) and \(|t|\le20\).
This real-box argument uses neither analytic quadrature nor an
unverified holomorphy assertion for a numerical neighborhood.

Pi is enclosed using Machin's formula
\(\pi=16\arctan(1/5)-4\arctan(1/239)\), with exact rational
alternating-series bounds after respectively 80 and 30 terms. The
formula can be checked by the tangent addition formula:
\(\tan(4\arctan(1/5))=120/119\), and subtraction of
\(\arctan(1/239)\) gives tangent one, with angle between zero and
\(\pi/2\). The alternating remainder is at most the next term.
All rational-to-decimal conversions are outward.

The implementation uses Decimal Context operations with ROUND_FLOOR
and ROUND_CEILING. For exp, the correctly rounded half-even answer is
expanded to its previous and next representable numbers; monotonicity
then encloses exp on any input interval. See the official
[Python3.15 Decimal.exp contract](https://docs.python.org/3/library/decimal.html#decimal.Decimal.exp),
also checked in the installed backend's docstring. No floating-point
power or uncertified decimal pi constant is used. Invalid operations,
division through zero, overflow, underflow, subnormals and clamping
cause failure, not a silently accepted interval. Addition and
multiplication rounding are already included in every displayed bound;
there is no extra unpaid roundoff term.

Reproduce from the active notebook:

```text
python3 scripts/direct-mellin/fixed_laguerre_648.py
python3 scripts/direct-mellin/verify_recorded_648.py
```

Full certificate:
`scripts/direct-mellin/fixed-laguerre-certificate-648.json`.
Every cell's exact grid endpoints, three range enclosures and integral
enclosures are preserved in the two compressed JSONL files named
in its quadrature sections. The JSON also preserves all block sums,
endpoint/series/tail errors, full load-bearing intervals, software
versions, input/program hashes, checks and failures. All failures are
empty. These complete selected evidence fields were inspected, rather
than inferred from a bounded preview.

The first stage's scalar interval was
\([-0.44992121,0.63175496]\), so it was **inconclusive**, not positive.
The final stage gives the outward enclosure
\[
 \begin{split}
 E'(0)^2-E(0)E''(0)\in[&0.05483050444395944555729961932487534328353652685202958368407,\\
                       &0.12250047081840447956054443873929538459571947302593165526828].
 \end{split}                                                    \tag{7}
\]
For scale, the endpoint errors in the three J data are at most
\(8.210\,10^{-9},1.724\,10^{-7},3.629\,10^{-6}\);
the theta errors are at most
\(7.646\,10^{-27},1.530\,10^{-25},3.059\,10^{-24}\);
each infinite tail is below \(1.581\,10^{-61}\).
The full J intervals and ratio/variance enclosures are retained exactly
under `/stages/1/evaluation`, not rounded to these illustrative scales
before (2) is evaluated.

The separate verification script reads **every** recorded cell in both
stages and uses exact Fraction arithmetic to check grid coverage,
width-times-range inclusions, accumulated integral bounds, additive
error propagation, and the rational interval substitution in (2).
Its report is `scripts/direct-mellin/recorded-arithmetic-verification-648.json`.
This verifies the recorded arithmetic; it does not independently
reimplement the transcendental backend or replace the analytic bounds
above. Equation (7), together with (2), proves (1) under the stated
software contract. The scoped independent audit is recorded next.

### 4a. Independent mathematical audit and complete replay (step650)

The audit accepts the preceding argument under precisely its stated
software assumption. It uses L828 Section2 only for the density-based
Taylor subtraction, reciprocal-gamma cancellation and definition of E;
the representation-conditioned identity with a Bernstein-gamma function
and its zero assertions are not inputs. C828a Section1 supplies the
unconditional normalized density. Its use of L019 identifies P=K/2;
the explicit effective envelopes needed here are checked in Sections2–3
above, without assuming any Fourier sign.

In particular, the endpoint derivative majorant is integrable because
the exponent -1/4 is greater than -1. At infinity the same majorant
with x^(1/4) is integrable against (3). The second logarithmic derivative
of M contributes four times the logarithmic variance, and the second
derivative of -log Gamma contributes minus trigamma. Negating this
second logarithmic derivative gives exactly (2). The linear 4^(-s)
normalization does not affect it. These checks exclude a missing factor
two or four, an incorrect trigamma sign, and use of a conditional zero
premise.

For (3), the n>=2 tail has initial term less than 1/2 and ratio less
than 1/2, so it sums to less than one. For (4), the omitted n>=5
envelopes sum to less than twice their first term, whose exponent is
decreasing on x>=0; 8*pi^2*625<50000. The signed endpoint enclosures
use the exact integrals a,21a,442a and the fact log x<0 there. For
the infinite tail, log weights are bounded by x^2<=exp(x) on x>=2;
H(2)<-151 and H'(x)<-318 suffice on the whole half-line. Thus no
sampling of the endpoint or infinite tail is used. The middle-interval
theta error pays the complete length 21, maximum Jacobian e and
maximum weight 20^j, independently of quadrature subdivision.

The interval evaluator was inspected completely, including every
arithmetic method, conversion, context and exception trap. Exact
integers and rational-to-Decimal conversions avoid ambient-context
rounding; nontrivial arithmetic uses the explicit directed contexts.
Both Machin partial sums have even length, so their exact rational
alternating remainders give valid outward pi bounds. Monotonic exp
and adjacent numbers in the half-even context enclose each endpoint's
true exponential under the cited contract. The square operation
includes zero when its argument straddles zero. The positive summand
expression and Jacobian in (6) agree exactly with the program.

Run `python3 scripts/direct-mellin/audit_fixed_650.py`. It checks the
original evaluator and construction-input hashes, reconstructs every
range and integral in all 8192+131072 original cells at their original
precisions, and compares each complete cell with the preserved record.
It also compares both complete stage objects, including all block sums,
analytic-error constants, checks, ratios and scalar intervals. Output
streams are intercepted for comparison; step648 artifacts are not
rewritten. There is no new point, derivative order, precision stage or
grid. The reviewed evaluator is reused, rather than an independently
implemented exp backend; the latter remains the explicit assumption.

The separate exact-Fraction verifier was rerun with a new report path.
It checks coverage, every range-times-width enclosure, exact sums and
final propagation without relying on Decimal rounding for those checks.
All 139264 cell replays, both full-stage comparisons and exact-rational
checks passed, with no failures. Complete audit evidence is
`scripts/direct-mellin/fixed-laguerre-audit-650.json` and
`scripts/direct-mellin/recorded-arithmetic-replay-650.json`.
The final interval is unchanged from (7); the first stage remains
inconclusive. This validates a local specialization of a known
necessary test, with no new result beyond the sources checked and no
claim about global membership or Xi zeros.

### 5. Restricted downstream interpretation

Import the necessary inequality by citation: M. L. Patrick,
*Extensions of inequalities of the Laguerre and Turan type*,
Pacific J. Math. **44** (1973),675–682,
[(1.1), Theorem1/(2.3)/(2.15), pp675–679](https://msp.org/pjm/1973/44-2/pjm-v44-n2-p26-s.pdf).
It applies to real Laguerre–Pólya canonical products with real zeros,
square-summable reciprocal zeros, real linear exponent and nonpositive
quadratic exponent. It gives \(f'(x)^2-f(x)f''(x)\ge0\) at every real x,
allowing equality and multiple zeros. In particular it includes the
nominated normalized Runckel products
\[
 e^{\beta s}\prod_j(1+s/a_j)e^{-s/a_j},\qquad
 \beta\in\mathbb R,\ a_j>0,\ \sum_j a_j^{-2}<\infty,
\]
including finite or empty products. The sufficient sampling theorem
is H.-J. Runckel, *Zeros of entire functions*, Trans. AMS **143**
(1969),343–362, [type(A) p356 and Theorem4 p357](https://www.ams.org/tran/1969-143-00/S0002-9947-1969-0252641-X/S0002-9947-1969-0252641-X.pdf).
Its applicability and the actual factorial interface were assessed in
step647; this calculation does not import actual E's membership.
Passing one necessary condition has no converse in either theorem.
C828a's separate complete-Bernstein exclusion remains separate evidence.

## Mathlib

Full matching coverage for this actual Mellin scalar and certified
calculation is **not checked**. No absence is inferred. The analytic
inputs, special-function constant and necessary inequality are the
precisely cited results above; no formal verification of the scripts,
Decimal implementation or the numerical enclosure is claimed.
