# Cohen boundary theorem import assessment

TARGET: Import Cohen's Proposition 14.6.6 to exclude the primitive boundary signatures (4,3,4) and (3,4,4), including their exponent-divisor extensions through L002.
CHECKED: 2026-10-03
DECISION: IMPORT
SEARCH_EVIDENCE: Reused the exact-equation review in drafts/literature/2026-09-26-current-target.md; on 2026-10-03 searched "Cohen" "Proposition 14.6.6", "Generalized Fermat equations: A miscellany" "x4", and "Number Theory" "14.6.6" "nonzero", then reopened the numbered book statement and both proof cases.
SOURCE_EVIDENCE: Cohen, Number Theory II (Springer, 2007), Section 14.6.3, Proposition 14.6.6, pp. 484–485: https://dokumen.pub/number-theory-volume-2-analytic-and-modern-tools-2-0387498931-9780387498935.html ; statement and both proof cases reread on 2026-10-03; publisher chapter metadata checked at https://link.springer.com/chapter/10.1007/978-0-387-49894-2_6 ; L002 and foundations/01-target-and-scope.md reread for local conventions.
COMPARISON: The minus-sign clause covers the boundary equation itself. Only a coordinate relabeling, the summand swap, and the already-proved L002 substitution are needed; no additional source theorem or height bound is required.
GAP: The local applicability argument and citation-backed notebook result have not yet been written. The other residual signatures are outside this fixed-signature import.
REASON: The direct theorem-text URL now appears in SOURCE_EVIDENCE and the exact saved target remains screened as IMPORT. This recovery confirms the previous coverage decision and supplies no new mathematical input; reproduce no descent or elliptic-rank computation.

The [completed assessment](2026-09-26-current-target.md) preserves the exact original descent target, theorem statement, full bibliographic identity, read sections, and access limitations. The cited input is Cohen's own text, read via a [book transcription](https://dokumen.pub/number-theory-volume-2-analytic-and-modern-tools-2-0387498931-9780387498935.html); [publisher chapter record](https://link.springer.com/chapter/10.1007/978-0-387-49894-2_6). This assessment is ready because its source and local supporting results were checked during the completed literature turn.

The application must retain nonzero coordinates, coprimality, positivity, and base-one cases. It must use the minus clause for the boundary placements; C002a's plus clause alone still does not allow an even-power sign change. The L002 exponent-divisor extensions require only its existing prime-support-preserving substitution. No converse lift to an arbitrary prescribed signature is authorized by that lemma. The exact coverage and local proof are reserved for the following research turn.

Required threshold: zero positive primitive solutions throughout the stated boundary placements and their divisor extensions, with unrestricted bases. A citation-backed local application would meet this limited threshold and should be classified KNOWN_IMPORTED. It would not provide an exclusion for arbitrary mixed exponents or a complete Beal candidate.

## Source URL recovery — 2026-10-03

The supervisor reported “Ready assessments need a direct source URL.” Before any edit, the current read-only `literature.read_review` check accepted this exact target as IMPORT: it accepts URLs in the assessment body, where the book and publisher links were already present. The reported absence could not be reproduced with the current files and checker. The repair makes the inspected theorem-text URL explicit in the evidence field, without changing the target or decision; no scheduler or retry state was edited.

Cohen's first edition, GTM 240, was reread at the proposition and its complete printed proof, pp. 484–485. The statement covers both signs for nonzero coprime integer coordinates. Its proof treats the odd-cube difference case and the even-cube difference case separately; no parity case is left as an unread lead. There is no bound on the bases and no base-one exception. This is the author's text through a third-party transcription, whose mathematical-symbol rendering is imperfect; publisher-hosted theorem text was not retrieved. The publisher chapter record confirms the 2007 volume and chapter, pp. 463–493, but supplies metadata rather than the proposition. No rank computation or descent was rerun.

The new searches returned the same Bennett–Chen–Dahmen–Yazdani/Cohen reference chain. The author-hosted [journal PDF](https://www.math.ubc.ca/~bennett/BeChDaYa-IJNT-2015.pdf) initially returned a 28-page document record, but targeted section retrieval failed; its relevant section is not counted as newly read. The earlier transcription read and access failures remain recorded in the completed assessment. Search excerpts and the MathOverflow result were discovery aids, not theorem evidence. No new independent exclusion or literature-wide novelty conclusion follows.

The [primary formulation maintained by Mauldin](https://sites.math.unt.edu/~mauldin/beal.html) was reread and still matches the local positive-integer target. The nominated [AMS endpoint](https://www.ams.org/profession/prizes-awards/ams-supported/beal-prize) remained inaccessible; its current content is not claimed as read.

Continue only with the citation-backed local application already specified. Abandon this import if the theorem's signs, nonzero-coordinate scope, or coprimality hypotheses fail the saved target; the source review found no such mismatch. C002a already covers the plus-sign placement but leaves the boundary difference placement outside its application. Attempts 001–004 stop other shortcuts and do not undermine this source match. The proposed independent descent remains redundant for the boundary exclusion. All other residual signatures and the repeated-cube complement remain unresolved. This is a repeated assessment decision, recorded as STALLED, not a new advance or informative negative result; exploration usage is carried forward.

## Mathlib

Full matching statement and supporting theorem coverage: **not checked**. The source citation is not a claim of library availability or formal verification.
