# Fixed published seven-primary Sha import — audit coverage

TARGET: Critically audit L082's exact conductor-389 seven-primary Sha import, checking model identification, theorem range, computational-source qualification and the torsion-to-primary argument.
CHECKED: 2026-10-18
DECISION: IMPORT
SEARCH_EVIDENCE: Reuse the exact-target comparison and duplicate/failure checks in drafts/literature/2026-10-18-fixed-seven-integral-leading-term.md and the approved import assessment; no changed curve, prime or theorem is proposed.
SOURCE_EVIDENCE: Stein--Wuthrich, Math. Comp. 82 (2013), Theorem 12.3 and adjacent identification/proof, p.1788, https://wstein.org/papers/mcom2649-iwasawa-alg.pdf#page=32 ; theorem text checked again during step 311. L034 records Cremona Table 2 p.257 row 389A1, Chapter 4 p.105 and exact ecdata model identification; L030/L033 record minimality and ordinary seven.
COMPARISON: The published fixed-case theorem supplies Sha[7]=0; audit only its precise application and the elementary primary-torsion passage in L082. No new theorem discovery, regulator computation or all-prime assertion is covered.
GAP: No essential source coverage is missing for this fixed audit; the original authors' computational execution remains unreplayed and must stay explicitly qualified.
REASON: The newly assembled known-result application needs a separate critical audit, with adequate unchanged mathematical source coverage reused rather than rediscovered.
SCOPE: L082 and only its exact model, prime, source applicability and group argument; no independent replay of Stein--Wuthrich or Cremona computations, no L026 hypotheses or arbitrary-curve assertion.

Separate coverage approval was completed in step 312. The unchanged research
audit is ready; further literature requires a changed hypothesis or specific
source correction. The audit must test the source's proved statement
against its distinct conjectural-order consistency statement, verify the
exact model via L034 rather than rank/conductor uniqueness, and check that
no finite-Sha assumption enters the least-exponent argument. Any actual
model mismatch or source correction requires reassessment. A successful
audit supports only the fixed seven-primary conclusion. Mathlib coverage
remains not checked. Inputs: L030, L033, L034 and L082; the original
computational-source qualification is unresolved by design.

## Separate coverage approval — 2026-10-18, step 312

Reused the two assessments named above and inspected L082, L034's exact
model-identification passage, and histories 310–311. Retrieved the published
Stein–Wuthrich offprint again, inspecting Theorem 12.3 and its entire short
proof, the preceding curve identification and Remark 12.4 on printed p.1788.
The theorem separates a proved p-torsion conclusion from a statement about
the conjectural order modulo p. Its proof cites the preceding computation;
it does not provide a transcript suitable for independent replay here.
The existing assessment already records the ordinary algorithm's relevant
proof cases on pp.1783–1784 and Section 12.4 on pp.1787–1788. No new external
search, theorem-level coverage or correction was obtained.

The exact-model source chain is recorded in L034: corrected Cremona Table 2,
p.257, row 389A1; Chapter 4, p.105; and the author's allgens row with vector
[0,1,1,-2,0]. Reuse this inspected chain; conductor and rank alone are not
an identification. No new source-blocking obligation was found. The later
research audit must still independently assess the application and the
written least-exponent argument in L082; this approval does not mark that
audit complete or rederive its group-theoretic conclusion.

Main gap: arbitrary E/Q of analytic order at least two still lacks equality
of rational rank and analytic order. The intermediate target is precisely
the TARGET above. Its downstream use is a critically checked fixed
seven-primary arithmetic input, independent of unfinished order/descent
work. Continue on exact model/range/source agreement; stop and reassess on
a model mismatch, corrected theorem, or hidden finiteness premise. All
original computational-source qualifications remain. This repeat approval
is STALLED as mathematical progress, not a new discovery or source advance.
