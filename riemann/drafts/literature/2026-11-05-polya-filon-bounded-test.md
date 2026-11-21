# Three-node Filon test — newly assessed bounded specialization

TARGET: Implement one fixed-cap three-node Filon inclusion test for L814's F,G and first two derivatives on [6.5,40], using 1024 u panels and 50-digit arithmetic, L815's complete tails, and an explicit unresolved-cell cover.
CHECKED: 2026-11-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the completed step585 comparison in 2026-11-05-polya-oscillatory-quadrature-scope.md, including exact-family and local duplicate/failure searches. Newly saved assessment requires separate approval before research; no repeated discovery search is needed.
SOURCE_EVIDENCE: NIST DLMF3.3.1–5,3.3.11–13,3.3.16–18 https://dlmf.nist.gov/3.3 ; Gao–Iserles2017 Section1, Theorem1/(1.5)–(1.6) and exact Filon definition https://link.springer.com/article/10.1186/s40687-017-0110-4 ; fundamental theorem of calculus and integration by parts for finite polynomial moments; step578 primary interval-inclusion assessment; L815 step584 and step583 independently repaired pi.
COMPARISON: Existing three-node interpolation with explicit real C^3 remainder and polynomial-oscillator integration covers the general evaluator. Only actual finite-amplitude derivative bounds, interval arithmetic, panel scaling and a bounded whole-frequency-cell certificate require specialization; no general quadrature reproof or new error theory is requested.
GAP: No new evaluator, achieved width, error budget or exclusion is established. FCC asymptotic constants alone are not validation. Actual third u derivatives and moment arithmetic must be enclosed, with every unresolved cell retained; signed compensation, event orientation, infinity and mixed positivity remain open.
REASON: This changes the failed finite-u box integration mechanism while preserving the exact family and complete tails. One test at declared caps is independently falsifiable; an unsuccessful certificate parks this variant rather than authorizing precision retries.
SCOPE: L016/L019/L020/L021/L814/L815; finite u in [0,3], theta n<=4, x derivative orders0–2 and original67 closed x cells of width1/2 on [6.5,40]. Three-node Lagrange Filon only; no adaptive refinement, root-isolation pass, parameter sweep, all-real reference, cross-notebook input or global extrapolation. Full matching Mathlib coverage unchecked.

Use the full source statements, applicability argument and qualifications
in the step585 comparison. The source theorem's h is adjacent-node
spacing; each panel uses endpoints and midpoint. The amplitudes are
u^j times the finite theta sum or Q, with the existing derivative signs.
Their smoothness is known; rigorous whole-panel third u derivative
bounds and the integrated remainder budget must still be supplied.
Do not differentiate only a midpoint sample or treat a formal derivative
expression as a numerical bound. Publish any load-bearing specialization
in a canonical lemma with hypotheses, proof/citations and Mathlib status.

Integrate the quadratic amplitude against the oscillatory factor, and
enclose the full x interval in each moment calculation. Ordinary
integration by parts and the fundamental theorem are sufficient sources
for finite moments; their actual formulas and outward implementation
must be checked. Cancellation may make intervals wide. Add every panel
remainder, arithmetic error, omitted n-tail and improper u-tail. Keep
the actual and required thresholds separate. The known L815 tails are
for x derivative orders0–2, not arbitrary extra derivatives.

Reuse only the independently justified pi input, and the audited saved
positive normalization enclosure with its stated execution qualification.
The raw Decimal power operation is not generally an inclusion extension.
Use outward repeated multiplication or exact independent verification for
new integer powers. Recheck the actual exp/trig argument ranges and any
new division. A divisor enclosing zero is never inverted. Requested
precision and tolerances are not achieved-error evidence.

Fix 1024 equal closed u panels, 50-digit working arithmetic, and all67
original closed x cells, with no cap escalation. Precomputation of shared
amplitude-node values is permitted. Save partial reasoning before lengthy
work. Save complete intervals for F,G and orders1–2, W,W', every
derivative/remainder bound, input provenance/backend, coverage checks,
comparison with census579, failures and explicit unresolved flags.
Print only the conclusion, actual/required bounds and certificate paths.

A strict same-sign F,G or nonzero-W interval is an existing L814 event
exclusion. An interval containing zero certifies no root. Reuse [0,6.5]
only under L815 step584's qualifications; preserve edge40 and shared
endpoints. Every common/multiple/degenerate possibility outside excluded
cells remains unresolved. This attempt does not include root isolation
or certify a complete event census by implication.

Continue only if at least one previously unresolved complete closed
x cell receives a validated event exclusion. Otherwise stop this fixed
variant and retain its error/failure budget. Width improvement alone is
not a sign result. Any successful implementation/output needs a later
independent audit before reliance. No outcome here resolves the main gap.
This is standard implementation/REPRODUCTION, not a creative sign mechanism.
