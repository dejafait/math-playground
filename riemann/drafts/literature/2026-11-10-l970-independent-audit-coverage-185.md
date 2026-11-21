# L970 independent audit — method coverage approved

TARGET: Independently audit L970's fixed n=2 certificate, checking outward arithmetic, both tails, every cell's quadrature bound and complete signed propagation against the saved certificate.
CHECKED: 2026-11-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused step183's exact integrated-moment searches and theorem comparisons in 2026-11-10-integrated-theta-variance-review-182.md; inspected step184's construction history, L970 and the complete construction script, and narrowly checked the preceding marginal audit coverage and finite-Li failure. Retrieved only newly essential Python arithmetic documentation and the precise DLMF remainder; no generic sign search or novelty inference.
SOURCE_EVIDENCE: Directly read NIST DLMF3.5(i), equations3.5.1-3 and C^2 hypotheses; Python3.15.2 decimal documentation, Decimal construction, copy_abs/copy_negate, Context methods/settings, rounding modes and signals; Python3.15.2 fractions documentation, Fraction construction and Rational operations. Local Python reports3.15.2. L019, L966(2)-(4),(11)-(13) and L967(5) delimit actual inputs. Step183's probability/covariance comparisons are reused, not reread as new evidence.
COMPARISON: The cited calculus and arithmetic contracts cover the enclosure method, not L970's effective constants, implementation or saved endpoints. L019/L966 supply actual positivity and integrability but not certified numerical errors. The required specialization is independent checking of the finite elementary certificate; no source theorem is asserted to imply its moment boxes or Q's sign automatically.
GAP: Independently verify every effective analytic and arithmetic obligation in L970, including the full selected aggregate values and all 3072 cells; neither PASS nor a certificate preview suffices. All-index L966(16) and L030-L032/C032a positivity remain unproved.
REASON: Step185 supplies adequate source/method coverage for one independent REPRODUCTION audit of the existing fixed-index result. No essential source is blocked; proceed to mathematics without repeating generic literature review.
LITERATURE_REASON: This audit is the newly essential continuation of the REVIEW_REQUIRED construction nomination; directed decimal semantics were outside the prior quadrature assessment's inspected implementation scope.
SCOPE: Only n=2,b=1/4,h=5184,N=3072,u in[0,3],theta m<=4 and the existing L970 proof/code/certificate. Preserve original evidence if a correction is necessary. No new finite index, profile, mesh optimization, all-n extension, zero-free region or RH-dependent input is approved.

## Relevance and retained failures

The main gap is actual-Xi all-degree positivity L030-L032/C032a;
this route needs all-index R_n<=N_n in L966(16). The intermediate
target is the independent audit above. A sound quantitative base case
could support a separately assessed uniform mechanism, but higher
indices and their changing signed partitions remain independent gaps.
L968 supplies the audited conditional downstream implication only.

Reuse the exact source comparisons and queries in
[step183's assessment](2026-11-10-integrated-theta-variance-review-182.md).
Its Biane-Pitman-Yor ordinary Li signs and Csordas moment inequalities
do not supply this regularized two-point observable. The BL comparison
requires extra curvature/integrability and does not automatically pay
the full signed expression. No reproof or further retrieval of these
unchanged comparisons is necessary for this audit.

L967/L969/C969a stop specific pointwise payment rules, not integrated
positivity. Keep those outcomes and
`ATTEMPTS/2026-11-10-finite-li-index-mixed-degree-import-limit-158.md`:
a finite ordinary Li index does not furnish a mixed degree. L970 is
the existing construction, not a duplicate independent audit. Neither
the limited local search nor this source approval certifies originality.

## Primary method statements and implementation contract

[NIST DLMF3.5.1](https://dlmf.nist.gov/3.5.E1) states the elementary
trapezoidal formula with remainder -h^3 f''(xi)/12 for real C^2
functions on a compact interval, h its length and xi interior.
[3.5.2-3](https://dlmf.nist.gov/3.5.i) state the composite formula.
Read the hypotheses and remainder directly. Version1.2.8 is the
previously recorded source version; this turn did not independently
verify the live site's release number. The audit must check that the
actual finite integrands and cell derivative enclosures meet these
hypotheses and that the local errors are completely summed. The
theorem supplies no effective derivative bound or improper tail.
It need not be reproved.

[Python3.15.2 decimal documentation](https://docs.python.org/3/library/decimal.html)
documents explicit Context precision, rounding, exponent limits and
signals. ROUND_FLOOR and ROUND_CEILING round toward negative and
positive infinity. Decimal construction from integers/decimal strings
retains their digits independently of context precision. copy_abs and
copy_negate are exact and context-independent. Context arithmetic
methods operate under that context; flags are sticky. Decimal.exp
uses ROUND_HALF_EVEN, so directed contexts alone do not supply directed
transcendental evaluation. These are library contracts, not evidence
that every operation in the construction uses them correctly.

[Python3.15.2 fractions documentation](https://docs.python.org/3/library/fractions.html#fractions.Fraction)
specifies rational arithmetic and exact numerator/denominator
construction; a finite Decimal can be converted to a Fraction with
the same value. Binary-float input has its own represented value and
must not be silently identified with a desired decimal rational.
The audit can therefore check finite decimal endpoints as rationals.

No interval-library correctness theorem is imported. Check the custom
IV operations and their uses, including conversions, signed products,
reciprocals excluding zero and powers, against these contracts and
elementary interval order rules. Check that default-context operations,
nonfinite results or uncharged exponent-range effects cannot enter a
load-bearing enclosure. Inexact/Rounded signals are expected for
directed rational rounding and are not themselves failures.

The rational Machin/arctangent and exponential-tail arguments are
self-contained claims in L970, using tangent addition with branch
control, the alternating-series remainder and geometric comparison.
Their coefficients, range reduction and all hypotheses belong to
the audit. This review neither derives nor accepts them. No new
external special-function sign theorem is needed to check those
finite arguments. Reproducing their verification is necessary because
the code has no imported theorem certifying its endpoints.

## One bounded audit and discriminator

Read L970's complete proof and the construction script; inspect full
selected `/pi`, `/improper_tail`, `/moments`, `/ratios`, `/checks`,
`/signed_propagation` and failure fields of the saved JSON. The scoped
inspector was used here only for exact `/parameters` and a `/cells`
schema/length preview. That preview has not checked any cell bound.
The mathematical audit must cover every cell, not selected examples,
and retain complete verification evidence on disk with concise output.
Use `python3 ../scripts/loop/inspect_json.py` for bounded selections;
`--full` is appropriate for selected load-bearing aggregate values.

Check the Machin branch and exact alternating bounds, rational
Taylor tail, range reduction, repeated squaring and negative-argument
reciprocation. Check all H derivatives, both derivative polynomials,
the finite product rule, the omitted-m geometric majorant and its
cell integration, and the improper-u majorant, slope and integral.
Then verify trapezoidal weights, all cells' local C^2 remainders,
moment endpoints and strictly positive denominators. Verify that
both negative terms are charged, that strictness uses only established
I_2(b)>0, and that the claimed conservative lower endpoint
423263556/10748505625 is justified. This lists claims to check; none
is newly proved here. A replay is useful only after verifying its
mathematical enclosure logic. Preserve the original certificate;
replay to a distinct artifact if needed rather than overwriting it.

Continue only if every relevant inequality and enclosure is justified
and a strict complete lower endpoint survives. A missed tail, inward
rounding, unsupported derivative bound or signed-coefficient error
requires correction and fresh verification before accepting the claim.
If that cannot be repaired within this certificate, record the precise
obstruction and stop this certificate; do not infer Q<=0. No floating
point substitute, isolated-index accumulation or all-n extrapolation
is permitted by this scope.

Essential inputs are L019 and audited L966 plus L967(5)'s coefficients
and normalization. L018/L024/L026 are inherited through L966; L968 is
downstream context and L969/C969a are contrasts. No RH, simplicity,
Stieltjes law, numerical moment premise, unverified zero table or
cross-notebook input is assumed. Full matching Mathlib coverage for
the sign and effective certificate remains unknown and was not checked.

This source-only approval makes no audit finding. Recommend
proof_audit/conceptual_audit, deep_research/xhigh: the load-bearing
issue is the joint analytic enclosure and signed propagation, beyond
arithmetic replay alone. Creative central-gap work remains desirable,
but the necessary certificate audit comes first and no assessed
uniform mechanism is presently supplied. Do not label this routine
specialization creative or invent another finite sign to fill a quota.
