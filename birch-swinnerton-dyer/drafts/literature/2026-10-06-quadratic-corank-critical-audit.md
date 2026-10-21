# Coverage request for the conditional corank proof audit

TARGET: Critically audit L026's residual witness matching, infinitude-to-corank implication, classical parity and primitive coefficient squeeze, checking that no granted corank, finite Sha or rational-rank premise enters.
CHECKED: 2026-10-06
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the prior quadratic-coefficient assessment and its targeted searches; narrowly read L026, L002/L004, control/divisibility foundations, L021 hypotheses and ATTEMPTS/021; reopened Kim primary definitions and corollary proof cases for the changed audit scope. No novelty claim or broad discovery search.
SOURCE_EVIDENCE: Kim author text dated 2025-05-12, Sections 1.2.2/1.4, Theorem 1.8(1)-(6), Corollaries 1.11/1.12 and Corollary 1.11 proof (printed pp. 4, 6-9); reuse inspected Sakamoto Section 1.1 and Stein--Wuthrich Proposition 7.2/Theorem 7.3 from the prior assessment, and Greenberg Theorems 1.2/1.5 from foundations/03.
COMPARISON: The source package covers the exact written audit: integral witness definitions and classical corank statements, control with finite errors, and one-way divisibility for the fixed primitive ordinary series. Finite-Sha clauses and rational-rank conclusions are explicitly outside the imported scope.
GAP: No essential unread source case remains for this audit; the actual proof audit, including implication directions and coefficient normalization, remains for the next research turn. Uniform coefficient production, rational membership and complex-order equality are unresolved.
REASON: Approve a critical audit of the existing known-source specialization, not a new theorem or a reproof; source coverage is adequate for every named implication and the later audit must decide correctness.
LITERATURE_REASON: The newly specified critical audit required separate approval of its concrete implication directions and source boundaries; reuse adequate coverage and return to mathematics next turn.
SCOPE: Exactly the TARGET under L026's full retained arithmetic, residual-family and certified primitive-coefficient hypotheses; audit or repair its existing specialization only.
Essential inputs are L026, L002 and L004, Kim Corollaries 1.11/1.12,
and the residual/integral definitions cited in L026. L021's witness
discussion is reusable context, but its corank-two theorem must not be
used to establish that same corank. No cross-notebook input is needed.
Retain non-CM E/Q, p>=5 good ordinary/non-anomalous, residual
surjectivity, prime-to-p Manin/Tamagawa factors, local p-torsion
vanishing, residual-family nonvanishing, central vanishing, sign +1
and certified a_2!=0 in the fixed primitive normalization.

Approve only if the saved source coverage addresses those hypotheses
and the written implication directions. Otherwise name the exact
missing source case. The mathematical audit should test for a hidden
finite-Sha/rational-rank assumption or normalization mismatch and
repair any discovered error. Uniform coefficient production, rational
Kummer membership, finite Sha and complex-order equality remain
unresolved regardless of this audit's outcome. This assessment approves the source scope for a later audit; it establishes no
new mathematical result and does not certify L026 correct.


## Completed source comparison

The main gap is rational rank versus complex order at analytic rank at least
two. The intermediate target is the exact L026 audit above. Its downstream
use is validation of the conditional corank input to L023-L025; neither
point realization nor a coefficient-production theorem is supplied.
Continue only if the later audit verifies each implication on these
hypotheses; abandon or repair an application requiring granted corank,
finite Sha, positive rational rank, or a different primitive normalization.

Primary source reopened: Chan-Ho Kim, *The structure of Selmer groups and
the Iwasawa main conjecture for elliptic curves*, dated May 12, 2025,
[Sections 1.2.2 and 1.4](https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf#page=4),
[Theorem 1.8](https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf#page=7),
and [Corollaries 1.11/1.12](https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf#page=8).
The definitions specify the auxiliary congruences, coefficient ideal,
period and residual reduction. Theorem 1.8 separates classical Selmer
structure (1)-(3) from the finite-Sha additions (4)-(6). Corollary 1.11's
first assertion uses the former theorem; its subsequent global assertion
chooses an ordinary prime using further main-conjecture inputs. L026 only
imports the first assertion at its fixed prime. Corollary 1.12 states
classical corank parity with the same integral nonvanishing premise; its
preceding proof explanation invokes (3.5). These are the relevant cases,
not rational-rank parity or an unconditional witness-production claim.
No further original proof of those imported theorems is required.

The prior assessment's Sakamoto comparison remains in scope: Section 1.1,
Documenta Math. 27 (2022), pp. 1892-1894. L021's granted-corank conclusion
must not be used. L002's arithmetic paragraphs expose finite generation
and the finite control errors. The saved Greenberg Theorems 1.2/1.5
coverage therefore covers infinitude-to-corank auditing without a new
source search. L004 explicitly permits k=0; the later audit must use
its inequality rather than its k=n rational-rank conclusion.

Reuse Stein--Wuthrich, Math. Comp. 82 (2013), Sections 3/3.3/6 and
Proposition 7.2/Theorem 7.3, printed p. 1778, as fully assessed in
2026-10-06-quadratic-coefficient-selmer-corank.md and foundations/05.
The fixed primitive ordinary series, trivial branch, real Neron period,
unit root and cyclotomic generator remain unchanged. Residual
surjectivity, p>=5 and good ordinary reduction match that assessed
representation case. Kato's original Theorem 17.4 is imported through
this checked elliptic formulation; its original proof was not reread.
Functional-equation Taylor parity and module/power-series comparisons
are elementary audit obligations already written in L026, not missing
literature or new derivations in this turn.

Duplicates and failures: the construction assessment is ready and reused;
this turn adds approval for the distinct critical audit. ATTEMPTS/021's
finite-defect-removal failure is retained. No primitivity-to-F=0 inference
is authorized. No new unread lead is essential. Mathlib full and supporting
coverage remains not checked; no absence claim is made. Classification of
this source-scope comparison is NOVELTY_UNCHECKED, with no mathematical
novelty asserted; the ensuing mathematical audit should be REPRODUCTION.
