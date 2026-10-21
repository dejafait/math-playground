# Fixed minus-three genus: independent audit

Approved target: critically audit L106's fixed-field marked model,
geometric connectedness and normalization genus 75 against its complete
ramification certificate. Reuse the prior SPECIALIZE assessment
`drafts/literature/2026-10-20-fixed-minus-three-genus-audit.md`.

Main gap: integer elimination in both L095 systems and compatibility of
global factors. This audit could make the geometric input reliable for
a later rational-point method. Pass only after checking both directions
of the marked model, actual monodromy, geometric component and constants,
and the complete finite certificate; otherwise record the exact defect.

Initial independent review finds no defect in the linear base change,
prime-degree primitivity or Jordan application. The actual branch types
are even and include a 3-cycle with eight fixed letters. Stored individual
permutations are not a generating tuple. Full arithmetic replay and the
normalization/constants review remain to be completed before accepting
the audit. No rational-point or integer conclusion follows.

ATTEMPTS/045 and ATTEMPTS/046-minus-three-joint-factor-at-seven.md concern
independent mechanisms; their stop evidence is preserved. No new source
search is needed for this unchanged approved scope.

## Completed audit

The full audit is canonical in L106, in its independent-critical-audit
section. The separate script `scripts/global-fiber-genus/audit.py`
reconstructs all original checks and verifies every complete stored action
and cycle, using independent multinomial coefficient arithmetic. Its full
`audit-certificate.json` has 6,822 passing checks and no failures.
Degree 990, unique geometric component and normalization genus 75 pass
review without correction. The scheme comparison, actual monodromy,
closure, full constants and extension of the map are reviewed in L106.

Completed classification: RESEARCH / EXPLORATION / REPRODUCTION,
actual task proof_audit. This is a new verification test of an existing
result, with no new mathematical input or repaired error; it is not
reported as ADVANCE. The mathematical exploration count is one since
step 362's advance. PROOF.md and DAG.md are unchanged because the argument
and inputs did not change; their historical pending-audit wording is
superseded by L106 and the current checkpoint.

For future work only, the unmarked quotient may offer a simpler
rational-point problem, provided the fixed-field lifting condition is
retained. Its genus and lifting test have not been derived or approved
here. The new scope is REVIEW_REQUIRED and receives a separate source
comparison before any mathematical attempt. Both L095 systems, global
factor compatibility and the minus-eleven branch remain open.
