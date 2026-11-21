# Independent audit coverage for the actual fixed-pair certificate

TARGET: Critically audit L778's actual fixed-pair certificate, including evaluator tails, contour homotopy, multiplicity, DFT aliasing and L777 error transfer.
CHECKED: 2026-11-04
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step432 reused the step430 primary comparison, read L778 and the relevant L776/L777 scope, step431 notes and named Fredholm/q-Pascal stops; searched official Python Decimal and mpdecimal rounding contracts and inspected pinned CPython v3.15.2 context initialization and exp/sqrt dispatch. Queries and read limits below; no novelty inference.
SOURCE_EVIDENCE: Reuse Johansson 1802.07942v1 Sections2/2.1 and4 and L776/L777's assessed identities. Newly read Python3.15.2 decimal contracts, mpdecimal4.0.1 Context/Arithmetic Functions, and CPython v3.15.2 Modules/_decimal/_decimal.c context initialization and exp/sqrt wrappers cover the changed backend, including allcr=1. These are software contracts, not an audit of the installed binary or L778.
COMPARISON: Known argument-principle, Cauchy, rational-Hankel and norm-error methods cover the audit mechanism; the Python/libmpdec contracts support scrutiny of the directed-Decimal alternative already permitted by step430. No source supplies L778's actual enclosures. Independently checking its elementary analytic estimates and implementation is the remaining specialization; no new general theorem is required.
GAP: The source gate is paid; the analytic audit remains entirely unpaid: normalization, all evaluator tails, complete contour homotopy and counts, multiplicity, derivative/root uncertainty, DFT alias exclusion and full L777 transfer. Saved rational checks do not independently verify these obligations or the installed backend.
REASON: Separate coverage approval is complete for the unchanged audit target. Proceed to one conceptual proof audit using the existing methods and the now documented Decimal backend contracts; do not repeat source discovery or infer growing-order control from one pair.
LITERATURE_REASON: The new independent-audit target includes a directed-Decimal entire-theta evaluator and rational contour/DFT error implementation not independently assessed in the earlier FLINT-oriented source comparison; reuse general theorem coverage and check only that implementation scope.
SCOPE: Independent scrutiny of L778 and its two step431 scripts/certificates only; no radius sweep, growing-order bound, coefficient-sign discovery or RH candidate audit.

## Original nomination — source status superseded by step432 below

The exact claim awaiting scrutiny is a one-pair original-norm interval
strictly below one, not a possible complete RH solution. The input is
L017/L018's completion, L776's audited conditional sign formula and
L777's audited conditional error transfer. L021 fixes the coefficient
conventions through L776. No cross-notebook input is needed.

Essential proof cases for the eventual audit are the complete uniform
theta and u tails, Cauchy moment integration on complex disks, polynomial
interval uncertainty versus the additional E_G, every contour image
enclosure and nonvanishing homotopy, multiplicity from the total count,
the derivative residue including root uncertainty, zero-free F on the
larger disk, the one negative Laurent mode and its excluded DFT alias,
and the two Gram factors/full-product error. Check Decimal's exact
rounding contract against the operations actually used. The exact
rational saved-data checks pass, but are not a substitute for these
analytic obligations.

The next invocation is source-gate approval only because this assessment
is new. If the comparison is adequate without new source discovery,
reuse the existing primary statements rather than reopen general
Fredholm literature. Subsequent mathematical scrutiny should be
proof_audit/conceptual_audit, deep_research/xhigh: the homotopy and
analytic interval errors are delicate. No protected creative target is
manufactured; a growing-order mechanism still lacks an independent
uniform actual-F/reciprocal budget. Mathlib matching coverage is unchecked.

## Completed source comparison — step432, 2026-11-04

This literature-only step approves the unchanged target for a later
mathematical audit. It proves no enclosure, norm, coefficient sign or
new lemma. L778 remains unaudited. The main gap is actual-Xi all-degree
mixed positivity; this intermediate target can establish whether one
fixed-pair benchmark is trustworthy. No complete RH route is supplied.

### Reuse, overlap and failures

Read the prior fixed-pair assessment's complete step430 primary comparison,
the full L778 proof, L777's conditional certificate/error-transfer scope,
L776's hypotheses and normalization, and the step431 working/history notes.
Inspecting the interval primitives in `scripts/actual-fredholm/fixed_pair_431.py`
identified the backend operations whose contracts need coverage; no script
was executed or modified. No certificate values were reverified here.
The step423 shifted-boundary stop and L765's recorded q-Pascal endpoint
norm obstruction concern distinct transfers and do not reject this
fixed-pair original norm. Neither provides independent audit evidence.
The existing finite-data checker explicitly excludes the analytic work,
so repeating its PASS would not complete the proposed audit.

The ready assessment already inspected Johansson's primary paper,
*Numerical integration in arbitrary-precision ball arithmetic*,
[arXiv:1802.07942v1](https://arxiv.org/pdf/1802.07942v1), Sections2/2.1,
pp.2–4, and4, pp.7–8. Reuse its whole-box analyticity/enclosure obligations
and Cauchy/argument-principle applications. L778 uses Taylor integration,
not the paper's Gaussian quadrature algorithm; its specific Cauchy disks,
Taylor remainders, real integral tails and constants require direct audit.
The named argument principle, Cauchy integral formula/estimates, winding
homotopy invariance, real intermediate value theorem and finite Fourier
orthogonality cover the mechanism. No new theorem or independent source
for L778's particular geometric-series estimates is needed. Their validity
is a proof-audit obligation, not established by this coverage decision.
L776/L777's previously assessed Fredholm and finite-rank inputs are reused;
their hypotheses cannot be replaced by a desired sign or assumed zero list.

### Changed backend: primary contracts and implementation cases

Queries: `site.docs.python.org 3.15 decimal exp sqrt correctly rounded
ROUND_HALF_EVEN next_minus Context`; `site.bytereef.org mpdecimal correctly
rounded exp sqrt decimal arithmetic`. Search summaries were leads only.

Python **3.15.2**, [decimal documentation](https://docs.python.org/3.15/library/decimal.html):
read Decimal construction, `exp`, `next_minus`,
`next_plus`, Context method equivalence, precision/exponent settings and
rounding modes. String/int construction preserves exact input digits;
arithmetic applies the context. Exact sign-copy behavior was also located
in the official documentation search extract, with direct review retained
as an audit obligation.
`exp` promises nearest-even correct rounding; neighbor methods return
adjacent representable values in the specified context. FLOOR/CEILING
give directed arithmetic. Context methods use their own context.
These contracts are the appropriate interface for L778's interval
primitives; they do not certify every caller operation. The script's
nonnegative integer powers use interval multiplication, so an unrelated
general `Decimal.power` guarantee must not be substituted.

mpdecimal **4.0.1**, primary [Context](https://www.bytereef.org/mpdecimal/doc/libmpdec/context.html),
Data Type, Precision and Exponents, Rounding, Signals and Conditions,
Correct Rounding; and [Arithmetic Functions](https://www.bytereef.org/mpdecimal/doc/libmpdec/arithmetic.html),
exp and square-root cases, read. `exp`'s correct-rounding guarantee
depends on `allcr=1`; square root is always correctly rounded to
nearest-even. General power and inverse-square-root are exceptions to
blanket correct rounding. Exponent limits, exceptional signals and
finiteness must still be respected. Merely naming libmpdec would not
resolve the exponential hypothesis.

Pinned [CPython v3.15.2 `_decimal.c`](https://raw.githubusercontent.com/python/cpython/v3.15.2/Modules/_decimal/_decimal.c):
read `context_setattrs` (lines1254–1310), `dflt_ctx`/`context_new`
(1338–1396), `context_init_impl` (1438–1471), default-template setup
(7381–7392), selected Decimal exp/sqrt dispatch cases (4430–4438,4513–4517), and Context
exp/sqrt dispatch (5936–5947,6061–6069). The default struct ends in
`allcr=1`; new contexts copy it or the default template. Constructor
attributes shown do not change that field. Context exp/sqrt dispatch
to `mpd_qexp`/`mpd_qsqrt`. This source comparison supports the documented
Python contract; it does not attest the installed binary or prove the
backend algorithms. The downstream audit may retain the ordinary
trusted-software contract explicitly rather than claim formal verification.

A guessed third-party mpdecimal `context.c` URL returned404 and was not
used; the pinned CPython source and official mpdecimal contracts resolve
the needed interface question. Full libmpdec internals and other versions
were not audited. No essential source remains blocked for this target.

### Approved audit and discriminating test

The next turn should critically audit L778's complete proof against the
actual code and saved evidence. Essential inputs are L017/L018/L021 and
L776/L777, together with the named complex-analysis and arithmetic
contracts above. Pay all following obligations before accepting the norm:

1. Actual-G normalization, compact domination, complete theta/u/cosh tails,
   all cell Cauchy disks and Taylor integration errors, and retention of
   coefficient uncertainty separately from the additional global error.
2. Full parameter coverage, polynomial Taylor boxes, shared polygon
   endpoints and zero-free homotopy; counts with multiplicity, real-root
   bracket, simplicity and the larger zero-free factor disk.
3. Derivative error at the uncertain root and the residue normalization;
   the whole-circle factor lower bound, Laurent annulus, the unique
   negative mode and its DFT exclusion, and all coefficient/tail errors.
4. Both Gram factors and the original Hilbert norm, all three L777 product
   error terms, and directed arithmetic/input/exponent obligations at every
   load-bearing operation. Saved finite checks alone do not pay steps1–3.

Acceptance requires a valid complete enclosure with upper endpoint<1
for the same operator. A concrete invalid tail, homotopy/count, residue,
alias exclusion or error transfer reopens the certificate; an enclosure
crossing1 is inconclusive, not a refutation of the norm condition. Preserve
any failing evidence without a radius sweep or automatic refinement.
This is conceptual_audit work, not creative research or a complete-solution
audit. Other orders, tied moduli, uniform actual-F/reciprocal bounds and
positivity assembly remain open. Those unpaid uniform bounds still block
a justified growing-order creative nomination; the essential independent
audit takes priority. No cross-notebook input; full Mathlib coverage remains
unchecked. No lemma, mathematical script, DAG or PROOF change was made.
