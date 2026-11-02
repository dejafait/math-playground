# Bounded two-packet audit — working notes

Target: the unchanged EXPLORE target in
`literature/2026-11-01-aggregate-horizontal-energy-test.md`; audit only
C614a and its used L614 reductions. Main gap: actual-Xi all-degree
signs at unbounded heights. Passing this audit could support a later
general energy/count test, whose coverage and proof remain open.

Analytic review so far: L614's norm specialization, ordered-pair formula,
aligned-depth bound, small-spacing bound and v-monotonicity have been
checked directly. C614a's small-depth Taylor remainder, completed-square
constant and large-depth integral reduction agree with those formulas.
Zero depths retain both labels. No pairwise algebraic square is changed
to a modulus square. Source coverage is reused; no new source theorem
or general-family claim is being assessed here.

Completed: every stored partition node was checked, all binary64 bounds
replayed exactly and a separately implemented 50-digit directed-decimal
calculation certified every full box. All rational floors pass, zero
failures. Original and unfinished certificates are preserved. Full proof,
audit details and qualifications now reside in canonical C614a;
`scripts/aggregate-energy/two-packet-audit.json` holds per-cell evidence.
The exact three-packet continuation is nominated as REVIEW_REQUIRED;
no mathematical test of that changed scope was performed. General
families, zeta weights, charge conversion and Xi signs remain unresolved.
