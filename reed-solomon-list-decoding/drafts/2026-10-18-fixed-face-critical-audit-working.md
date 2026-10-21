# L085 critical audit — saved before calculation

Gate: `literature/2026-10-18-fixed-face-critical-audit.md`, SPECIALIZE.
Target: Critically audit L085's fixed-face certificate and original/reduced zero-plane affine-system equivalence.

The main gap is arbitrary-center safety at 67/68 agreements. This step
tests only the fixed multiplier and equivalence, potentially useful for a
later joint-system feasibility attempt. Retain the result only if every
original coefficient, multiplier transport, zero-row removal, full-rank
basis and inverse pullback passes. Do not run a solver or choose weights.

Manuscript inspection finds the necessary mixed and removed equations
explicit, with the reverse implication supplied by an invertible congruence.
The forward implication uses the assessed PSD trace/kernel theorem;
nonemptiness and minimality are not needed. Empty remaining kernels must
be checked directly, since the source's proper-face wording is restricted.
No mathematical defect is established yet. Independently rebuild the beta
rows and original blocks from complete affine moment records, solve the
canonical weight equations afresh, and verify all 49 coefficient identities.
Import the reviewed underlying mode decomposition with its qualifications;
do not claim a recursive review of every ancestor or L084's parametrization.

Inputs: L076,L078,L082,L083,L084,L085; L021,L053,L073,L075,L079,L081
and foundations/04,09,10,12 retain ancestral contracts. Complete step-290,
292,294,equality,298 and fixed-face certificates are required, preserving
rho,p8,pairs,seven RREF/completion,85 domain rows,45 signs,90 weighted
kernel equations,500 types/3000 presentations,36 forced/45 free moments,
81 modes,full anchor and canonical weights. ATTEMPTS/060–067's point,
weight,equality-only and numerical-run stops remain intact. Existing local
changes are extensive and are preserved. No duplicate L085 critical audit
was found in the specific step-299–301 and fixed-face records inspected.

## Completed audit

Retained L085 under its original ancestor contracts. The full proof and
critical review are canonical in L085, with exact evidence in
`scripts/finite-support/zero-plane-fixed-face-critical-audit.json`.
All 12009 checks pass, zero failures. There are 20 selected empty
compressions, six selected retained base ranks one and two ranks two;
the removed scalar equations remain in every empty case. All affine/raw
trace totals vanish and both inverse pullbacks pass coefficientwise.
No mathematical defect, new exclusion or feasibility verdict was found.
The original argument/DAG is unchanged. L084's complete parametrization
requires its own separately approved critical audit.

The bounded inspector's first `/failures` read omitted
`PYTHONINTMAXSTRDIGITS=0` and hit Python's 4300-digit decoding limit;
rerunning with that setting returned the complete empty failure list.
This was an inspection-command error, not an arithmetic check failure;
no certificate or coefficient changed. Scoped documentation validation
passes (91 nodes, 280 unique edges). Full summary inspection agrees with
the audit's recorded counts and exact zero trace residuals.
