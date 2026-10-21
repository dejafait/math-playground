# Free-pair shells-5–8 unchanged-witness precheck

Work in progress, step rsld-2026-10-20-355-free-pair-batch-precheck.
The pre-existing SPECIALIZE assessment is
`literature/2026-10-20-free-pair-shell-batch-precheck.md`; its companion
specifies the exact support. No optimization or witness retuning is allowed.

Main gap: arbitrary-center safety at 68 agreements. Intermediate target:
construct both original affine source families on the approved joint
support with free pairs, then test only L022/L023's unchanged extension.
A common feasible point with M>=K+1 stops this finite support; any exact
failed row or rational negative vector rejects only the unchanged point.
Caps are 20000 variables and 200000 scalar/pair rows after source equality
reduction. Exceedance is a resource stop, not a mathematical exclusion.

Essential inputs: L001,C001a,C012a,L019,L021,L022,L023 and foundations/04.
L024 and ATTEMPTS/012–018,067,068,071,079 are comparison evidence only.
No ancestral L053–L096 Schur costs, ranks or fixed-column constraints
enter this model. Known-source assessment and recorded stops were read.

Potential downstream use is the established uniform-in-m support transfer
if a sufficient free-pair dual can later be found. Independent unresolved
gaps include 67 agreements, global triple moments, labeled restrictions,
RS realization, and the qualified ABF/ArkLib comparison. The 955–957
bracket stays unchanged. Full matching Mathlib coverage is not checked.

Completed: the generator constructs 7386 source classes, 32151 ordered
closure orbits, 7208 free variables and 71756 scalar/pair rows, within
both caps. The unchanged witness passes all 166 matrices simultaneously.
The independent verifier imports no generator routine: factorial/full-u
beta reconstruction agrees on all original orbit maps and 42915 affine
coefficients; every scalar/pair row and matrix entry is reconstructed.
Full congruence multiplication checks 471 positive and one zero pivot.
The exact objective is unchanged, with floor(M)>T and M>=floor(T)+1.
There are no verification failures. Canonical reasoning is in L097.

Commands completed successfully:

    python3 scripts/finite-support/free_pair_shell_batch.py
    python3 scripts/finite-support/verify_free_pair_shell_batch.py

Full model/witness and independent evidence are respectively
`scripts/finite-support/free-pair-shell-batch-results.json` and
`scripts/finite-support/free-pair-shell-batch-verification.json`.
The initial state and both concise run logs are preserved alongside them.
The scripts adapt the L022 generator/auditor structure and keep the two
source reconstructions independent. No solve, retuning or ancestral
Schur contract was used. A duplicated terminal failure-exit line in the
new verifier was removed after the first successful run; this changes
no coefficient, check or result.

Decision: stop the entire prescribed finite support as a sufficient
threshold certificate, preserving all earlier stops. This is new local
negative evidence, a reproduction of assessed tools, not a discovery
beyond the sources checked. No full-SDP feasibility or RS boundary claim
is made. L097's separate critical audit is proposed with REVIEW_REQUIRED
coverage; no new mathematical target is approved here.

Scoped documentation validation passed:
`python3 ../scripts/docs/check_structure.py --problem reed-solomon-list-decoding`.
The overview initially exceeded its 100-line cap by two lines after the
new paragraph; joining the related existing L033/L034 paragraphs retained
all mathematical text and restored the cap. The new DAG row uses only
L021,L022,L023, matching the actual witness and source-specialization inputs;
no ancestral shell lemma supplies an unrecorded mathematical premise.
