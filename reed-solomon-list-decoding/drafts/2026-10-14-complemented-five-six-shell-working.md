# Complemented fixed-witness calculation — working checkpoint

Approved target: Test the complete complemented anchored five/six-shell matrix at L062's unchanged represented moments.

Main gap: arbitrary-center safety at 67/68 agreements, bracket 955–957.
The intermediate target is the complete excluded-anchor source matrix on
layers 0,5,6. A negative mode excludes only the unchanged witness; a full
exact PSD pass parks this necessary diagnostic. No retuning is authorized.

Reuse the supplied SPECIALIZE assessment
`drafts/literature/2026-10-14-complemented-five-six-shell.md` and inputs
L021,L053,L056,L059,L060,audited L061 and audited L062. The source
coefficient is p_(l+m-i-j)-y, with y=x(triple)/rho, not d5 or d6.
All p_0 through p_12 and Boolean/forbidden entries must be retained.
The anchor row is zero and must be checked before removing it. Do not
subtract p_l*p_m*J. All 49 product modes, shared 2-by-2 rectangles,
new-only modes and all six full-region presentations are required.

Prior duplicate/failure check: ATTEMPTS/015 uses different moments;
038 parks the included five-shell only; 043 parks the simultaneous
included-anchor matrix; 044 parks its represented scalar rows. None
evaluates this affine complement. Their stop evidence remains intact.

Continuation/abandonment test: exact complete block PSD certificate or
an exact negative mode/vector. Repair any dictionary/normalization
mismatch before a verdict. Other assignments, unrepresented rows,
global PSD/moments, labels, measures, packings and RS realization remain
unresolved. Mathlib matching coverage is not checked.

First calculation: `scripts/finite-support/complemented_five_six_shell.py`
passes 2445 reconstruction checks; all 49 complete affine source blocks
are PSD and all five anchor cases vanish. Full fractions, presentations,
pair-minus-included blocks and minors are saved in
`scripts/finite-support/complemented-five-six-shell-results.json`.
Independent `verify_complemented_five_six_shell.py` now passes 2814
checks after correcting one audited-witness list-schema access. All
85 normalized pivots are positive, with minimum exactly 1/2; full
subset-action and signed rectangular comparisons agree. The completed
finite result is canonical in L063; this working note is not a second
proof. Separate critical proof review remains pending under a new
REVIEW_REQUIRED assessment. No input, objective or boundary changed.
