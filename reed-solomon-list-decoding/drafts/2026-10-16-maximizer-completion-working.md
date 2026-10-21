# Exact maximizer completion — working record, step 252

Approved target: test simultaneous seven-shell PSD completion at L072's
exact maximizer with the original 36 nonnegative new/new variables.
Use the prior SPECIALIZE assessment
`literature/2026-10-16-maximizer-simultaneous-seven-shell-completion.md`.
This is one REPRODUCTION calculation, not a literature turn.

Main gap: arbitrary-center safety at 67/68 agreements; the 955–957 bracket
does not change. The intermediate target is only the included-anchor
five/six/seven matrix at u=0,v=v_dagger,w=w_star. A rational assignment
would retain a nonexclusion witness; an exact original-row separator
would reject this point. Continue only with all 64 original inequalities,
36 signs, 28 forced entries, 270 types/1620 presentations, singular
ranges and anchor correction checked. An unresolved basis search is
not an infeasibility result.

Inputs: L061,L062,L065,L067,L068,L069,L071,L072 and foundations/04,09,10,12.
The source review found no duplicate changed-point verdict. Preserve
ATTEMPTS/049–054. L070's old particular solution is not reused. Its
coefficient-only row transform may be reused after exact verification,
but its right-hand side must be recomputed. L067's positive-weight rows
are necessary equalities because its dual is exactly zero on this plane.
If reduction is used, check its changed-point consistency and translate
every result back to the original system. A separating combination may
use sign rows and may add the old zero dual to remove negative weights
introduced when lifting equalities.

Unresolved independent requirements: seven/seven scalar upper rows,
other points/anchors and excluded-anchor matrices, global moments,
measures and common-center RS realization. No global bound follows.

Completed: canonical L073 gives an exact rational nonnegative completion.
The full original/fresh reduced system was saved before basis discovery.
The constructor passes 2911 checks and the independent original-row
verifier passes 4793, including a fresh 36-by-36 defining-basis solve and
all 306 reduced-block principal minors. Both full failure lists are empty.
All 64 mode rows and 36 signs pass, with 35 positive variables/one zero
and 23 positive mode slacks/41 zeros. Complete evidence is in
`scripts/finite-support/maximizer-completion-results.json` and
`scripts/finite-support/maximizer-completion-verification.json`.
The original-row basis provides a compact exact definition; no rounded
parameter or numerical optimizer status enters the proof. This is an
included-anchor nonexclusion result only; dedicated critical review is
pending and the main gap is unchanged.
