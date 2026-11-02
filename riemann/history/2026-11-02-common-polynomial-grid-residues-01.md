# 2 November 2026 — common polynomial and retained grid residues

STEP_ID: 2026-11-02-common-polynomial-grid-residues-01.
Completed one proof_attempt under the unchanged ready angular EXPLORE
assessment. Outcome NEGATIVE, classification REPRODUCTION: an informative
restriction on the degree-M initial-prefix simplification, not a new
uniform angular bound or progress beyond the inspected sources.

[C645y](../lemmas/C645y-common-polynomial-retained-grid-energy.md)
contains the complete residue/orthogonal energy identities, exact
common-polynomial constraint, raw-sample rate comparison and the
specialization of C645t that stops every initial prefix through
ceil(n/2). The latter includes the first M coefficients. All remaining
grid terms are retained in the canonical full identity; they have not
been bounded. C645y's separate conceptual audit is outstanding.

The exact rational certificate in
`scripts/one-sided-hankel/common-polynomial-grid-certificate.json`
passes 35 aggregate checks and 41 prefix equalities, including oblique
rotations and repeated polynomial zeros. These are finite normalization
checks, not verification of the missing uniform estimate.

The refined mathematical test uses the later grid coefficients with
the same common degree-M polynomial, at squared threshold exp(-n/16).
Its precise proposal is in
`drafts/2026-11-02-common-polynomial-grid-residues-working.md`;
the exact Next action and unchanged NEXT_REVIEW remain in PROGRESS.md.
The angular target and all Xi realization/sign gaps remain open.
No new assessment or source import, cross-notebook input, scheduler
state edit, or token accounting was used. Existing work was preserved.

To keep the overview within its byte limit, its C645r/v/w detail was
condensed to a subfamily-bound reference. The displaced specifics remain:
audited C645r has odd m, n=3m, r in [1/4,9/20] and angular norm
at least c sqrt(n) exp(-.030504 n); audited C645v/w have the r=.54
subfamily with eventual lower bound c sqrt(n) exp(n/200). Their
canonical proofs and hypotheses are unchanged.
