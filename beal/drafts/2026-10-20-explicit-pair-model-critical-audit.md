# L110 critical audit working record

2026-10-20. Target: Critically audit L110's explicit hyperelliptic model,
inverse maps, transported s,z and exceptional charts.
Prior ready coverage:
`literature/2026-10-20-explicit-pair-model-critical-audit.md` (SPECIALIZE).

The main gap is primitive positive integer exclusion in residual Beal
signatures. This bounded audit checks a model that could support later
rational-point work. It does not address rational-point completeness,
degree-nine root recovery, other factors, either L095 integer system or
minus-eleven. Continue with the model only if the exact Q-field, original
scalar/marking and proper charts pass; repair or withdraw failing claims.

Read L110's full proof and producer, L109's definitions, quotient
identification and completed audit, the construction assessment and
history/378. Reused the ready source comparison; the scaling and
seven-adic failure records remain applicable and are not reopened.
Existing unfinished L108 work is preserved.

Initial review: the untwisted ordered auxiliary field is correctly
distinguished from the marked extension. Full invariant-field generation,
exact arithmetic and local-ring charts still require the independent
checks. The certificate's complete coefficient lists and both components
of every residual have been read. These zero residual records alone are
not verification.

Implementation preflight: system python3 has no SymPy, Flint, Sage or
cypari2. Use an independent standard-library exact polynomial quotient
implementation; do not alter the original producer or certificate.
Full certificate maps, including the scalar, will be consumed and checked
coefficient by coefficient. No calculation or audit outcome is claimed yet.

First independent run completed the exact identities and full map comparison.
Its gcd tests failed because `reduce(gcd, [-1])` leaves the singleton
negative rather than returning an absolute gcd. The independent polynomial
primitive-part normalization therefore reported the unit −1. This is an
audit implementation error, not evidence against L110. Preserved the full
first report at `scripts/pair-genus-two/model-audit-initial-sign-failure.json`;
changed the content normalization to absolute gcd before setting leading
sign, and rerun the same checks. No original certificate was overwritten.

Completed: the canonical full audit is in
`lemmas/L110-explicit-pair-genus-two-model.md`. The independent replay
passes all 86 checks, with complete coefficients/maps and both components
of every residual verified. Its output is
`scripts/pair-genus-two/model-audit-certificate.json`. Field generation,
the exact twist and every exceptional chart are justified in the lemma;
the computation alone is not used as proof of those geometric claims.

No correction to L110's mathematical conclusion was needed. Record
RESEARCH / EXPLORATION / REPRODUCTION, actual task type proof_audit:
verification of existing work, not a new mathematical input or a Beal
advance. This uses one mathematical exploration turn since L110.
DAG and PROOF are unchanged because the assembled argument did not change.
The proposed rank-bound continuation is uncovered and saved separately
as REVIEW_REQUIRED; no rank mathematics was undertaken or approved.
