# Fixed complex-order certificate — published result ready for import

TARGET: Certify complex order two for E=[0,1,1,-2,0] by a rigorous complex L-function certificate independent of BSD.
CHECKED: 2026-10-08
DECISION: IMPORT
SEARCH_EVIDENCE: Searched exact curve with rigorous/certified analytic rank, Cremona derivative algorithms, and rigorous analytic-rank methods; inspected the corrected book's analytic-rank determination, Table 1/4 entries, errata, and the authors' LMFDB reliability statement. Local comparisons covered foundations/01--02, L031/L034, point assessments, history/086--090 and ATTEMPTS/022--023.
SOURCE_EVIDENCE: Cremona, Algorithms for Modular Elliptic Curves, corrected online second edition (CUP, 1997), Section 2.13 pp.42--44, especially p.44's final verification paragraph; Chapter 4 p.106; Table 1 p.157 row 389A1; Table 4 p.327 row 389A. Cremona--Sutherland's reviewed LMFDB reliability statement, last edited 2024-03-08, specifies rigorous analytic ranks <=3 at conductor <=500000.
COMPARISON: Published analytic-order verification covers the exact target independently of BSD; import the computational result with its source qualifications instead of treating rounded derivative or Sha columns as certificates. No new derivative algorithm or discovery is needed.
GAP: Coverage is ready. A later research turn must record the cited result canonically, verify model and L-function conventions, and assemble its comparison with audited L034. Original analytic execution and a full numerical-error transcript have not been independently replayed here; the arbitrary-curve gap remains open.
REASON: Primary inspection changes the route from prospective derivative computation to an adequate published fixed-order import. This literature-only approval derives no lemma and changes no mathematical argument.
SCOPE: Only this exact model, published small-conductor analytic-order result, necessary finite-Euler-factor convention check, and comparison with audited L034; no derivative recomputation, refined BSD formula, full Sha finiteness or general complex/p-adic comparison is approved.

## Relevance and bounded test

Main gap: rank equals complex order for arbitrary E/Q of order at least
two. Intermediate target: exact fixed complex order two. Its downstream
use is to finish the complex comparison for the existing arithmetic/p-adic
worked certificate, as documentation of a known case.

Continue with the cited import after matching curve and conventions.
Abandon if the published verification is withdrawn, the model mismatches,
or the analytic-order result assumes BSD. Do not manufacture an interval
from printed decimal places. Independent replay is a distinct target
requiring review; it is unnecessary for this citation-based import.

## Primary evidence inspected

1. **Published analytic determination.**
   [Cremona Section 2.13, pp.42--44](https://johncremona.github.io/book/fulltext/chapter2.pdf#page=36)
   gives the Mellin derivative argument. Proposition 2.13.1 assumes a
   weight-two newform, Fricke eigenvalue epsilon=(-1)^(r-1), and order
   at least r. Its r=2 use needs lower vanishing first. The p.44 discussion
   distinguishes exact central vanishing from derivative nonvanishing
   computed to sufficient precision. Its final paragraph reports eighteen
   order-two cases up to level 1000, with separate arithmetic verification.
   That published determination is selected for import, not a deduction
   from small numerical values. No derivative formula is applied here.
   Its original computation is not replayed.

2. **Exact instance and column meanings.**
   [Table 1, p.157](https://johncremona.github.io/book/fulltext/table1.pdf#page=49)
   identifies 389A1 with coefficients 0,1,1,-2,0, in one isogeny class.
   [Table 4, p.327](https://johncremona.github.io/book/fulltext/table4.pdf#page=15)
   lists 389A, rank 2, and L^(2)(1)/2! approximately 0.7593165003.
   The [Table 4 introduction, p.313](https://johncremona.github.io/book/fulltext/table4.pdf#page=1)
   identifies entries with curve NX1 except 990H.
   [Chapter 4, p.106](https://johncremona.github.io/book/fulltext/chapter4.pdf#page=3)
   explicitly reports equality of analytic and arithmetic ranks in these
   entries, while treating positive-rank Sha predictions as approximate.
   The latter play no role. This is a cited computational analytic result,
   not an exact decimal leading coefficient.

3. **Rigor qualification from the data authors.**
   [John Cremona and Andrew Sutherland, Reliability of elliptic curve
   data over Q](https://www.lmfdb.org/knowledge/show/rcs.rigor.ec.q),
   reviewed knowl rcs.rigor.ec.q, last edited 2024-03-08, section
   “Mordell-Weil group and generators, and BSD invariants”, specifies
   rigor for analytic rank at most three and conductor at most 500000.
   It separately disclaims guaranteed precision for special-value, period
   and regulator approximations. Thus the published order assertion and
   decimal-value precision have different qualifications. The individual
   LMFDB curve page returned reCAPTCHA and was not inspected; the book
   supplies the essential exact identification. This supporting author
   documentation is not an independent numerical replay.

4. **Corrections and rejected conditional method.** The author's
   [errata, 26 September 2003](https://johncremona.github.io/book/errata.pdf)
   was inspected in full; no correction affects this analytic entry or
   Section 2.13. Bober, *Conditionally bounding analytic ranks of elliptic
   curves*, Open Book Series 1 (2013), 135--144,
   [abstract/introduction, pp.135--136](https://msp.org/obs/2013/1-1/obs-v1-n1-p07-s.pdf#page=2),
   retains BSD/GRH for general arithmetic-rank bounds and distinguishes
   small-rank exact methods. Those conditional bounds are not inputs.
   General search hits claiming complete BSD solutions were not inspected
   theorem inputs and provide no evidence used here.

## Applicability and deferred mathematical assembly

The current [Clay problem page](https://www.claymath.org/millennium/birch-and-swinnerton-dyer-conjecture/)
still links [Wiles's official description](https://www.claymath.org/wp-content/uploads/2022/05/birchswin.pdf).
Printed p.2 states the all-curve rank assertion for the incomplete series
and separates the refinement in Remark 1; p.4 states the analytic-order
zero/one theorem. This matches foundations/01--02.

The canonical import must match Table 1 to L030, specify the full finite
Euler-factor L-function, and check the passage to foundations/01's
incomplete series. Use the standard elliptic local Euler factors and named
Hasse bound for that necessary convention check; no removed factor may
silently be allowed to vanish at s=1. Local-factor conventions also appear
in Cremona Section 2.8, (2.8.3)--(2.8.4), p.29, inspected here. Archimedean
completion is separate. No refined leading coefficient follows merely
from changing conventions.

If explaining lower vanishing alongside the imported result, reuse the
named low-order theorem in foundations/02 and audited L034's independent
rational-rank input, retaining the theorem's direction. Do not assume the
general rank equality or transfer p-adic order to complex order. These
are deferred applicability checks, not new deductions in this turn.

Essential local inputs are L030 (exact model), audited L034 (arithmetic/
p-adic certificate), and foundations/01--02. L031 was read as an alternative
error-method lead; its twist-five value is not an untwisted derivative
certificate. Reproving its methods adds no necessary hypothesis to this
covered import. The point assessment's model/label provenance is reusable.
ATTEMPTS/022--023 and L033's stopped schedule remain intact; neither is a
failure of this distinct source import. No existing canonical local result
already supplies this fixed complex-order claim.

Mathlib coverage for the full fixed analytic-order computation and its
arithmetic comparison: not checked; no absence claim is made. Approval
is saved for a later research invocation. No lemma, mathematical script,
DAG row or PROOF.md argument changes here.
