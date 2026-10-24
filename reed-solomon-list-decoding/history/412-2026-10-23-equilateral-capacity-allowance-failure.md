# 2026-10-23 — Complete equilateral allowance fails its capacity test

Completed the gate-approved conditional calculation in
[L110](../lemmas/L110-equilateral-scaling-capacity-allowance-failure.md).
Its complete counts give a maximum allowance at (5,5,5) between
2.38*10^82 and 2.39*10^82 against required bound one. All 41,314
construction checks pass; all 112,867 saved-table checks pass, including
exact cross-comparison of every ratio against the maximum. Full evidence is
`scripts/finite-support/equilateral-capacity-allowance.json`.

Outcome NEGATIVE, kind RESEARCH, classification REPRODUCTION: new local
evidence parks this sufficient certificate, without progress beyond the
inspected tools or an actual capacity/nonexistence verdict. The failure
is preserved in [ATTEMPTS/093](../ATTEMPTS/093-equilateral-scaling-capacity-allowance.md).
L107–L109 and ATTEMPTS/082 retain their stops; no solve was restarted.
Factor existence, full scalar/source lift, PSD, RS realization and
the 955–957 bracket remain unresolved.

Separate critical review, rather than another equilateral calculation,
is proposed in [the audit assessment](../drafts/literature/2026-10-23-l110-critical-audit.md)
with REVIEW_REQUIRED. This neither rejects nor reopens the completed
calculation. A future capacity mechanism needs different marginal
information and a separately assessed, independently testable target.
