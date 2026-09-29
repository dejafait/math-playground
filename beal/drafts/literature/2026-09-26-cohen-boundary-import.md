# Cohen boundary theorem import assessment

TARGET: Import Cohen's Proposition 14.6.6 to exclude the primitive boundary signatures (4,3,4) and (3,4,4), including their exponent-divisor extensions through L002.
CHECKED: 2026-09-26
DECISION: IMPORT
SEARCH_EVIDENCE: Reuse the exact-equation searches and completed source chain in drafts/literature/2026-09-26-current-target.md; this target applies the same inspected theorem rather than proposing a new descent or strengthening.
SOURCE_EVIDENCE: Cohen, Number Theory II (2007), Section 14.6.3, Proposition 14.6.6, pp. 484–485, statement and both proof cases read in the linked book transcription; L002 and foundations/01-target-and-scope.md reread for the existing divisor and primitivity conventions.
COMPARISON: The minus-sign clause covers the boundary equation itself. Only a coordinate relabeling, the summand swap, and the already-proved L002 substitution are needed; no additional source theorem or height bound is required.
GAP: The local applicability argument and citation-backed notebook result have not yet been written. The other residual signatures are outside this fixed-signature import.
REASON: The preceding literature review fully screened this narrower import action. Reuse its named citation and access qualifications; reproduce no descent or elliptic-rank computation.

The [completed assessment](2026-09-26-current-target.md) preserves the exact original descent target, theorem statement, full bibliographic identity, read sections, and access limitations. The cited input is Cohen's own text, read via a [book transcription](https://dokumen.pub/number-theory-volume-2-analytic-and-modern-tools-2-0387498931-9780387498935.html); [publisher chapter record](https://link.springer.com/chapter/10.1007/978-0-387-49894-2_6). This assessment is ready because its source and local supporting results were checked during the completed literature turn.

The application must retain nonzero coordinates, coprimality, positivity, and base-one cases. It must use the minus clause for the boundary placements; C002a's plus clause alone still does not allow an even-power sign change. The L002 exponent-divisor extensions require only its existing prime-support-preserving substitution. No converse lift to an arbitrary prescribed signature is authorized by that lemma. The exact coverage and local proof are reserved for the following research turn.

Required threshold: zero positive primitive solutions throughout the stated boundary placements and their divisor extensions, with unrestricted bases. A citation-backed local application would meet this limited threshold and should be classified KNOWN_IMPORTED. It would not provide an exclusion for arbitrary mixed exponents or a complete Beal candidate.

## Mathlib

Full matching statement and supporting theorem coverage: **not checked**. The source citation is not a claim of library availability or formal verification.
