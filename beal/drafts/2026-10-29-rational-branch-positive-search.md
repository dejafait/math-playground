# Bounded rational-branch positive-certificate attempt

Approved target: attempt the mask 132102 K-conic search in
`drafts/literature/2026-10-29-rational-branch-conic-construction.md`.
The prior SPECIALIZE assessment is reused unchanged; execution is
REPRODUCTION of a known positive-proposal method, not new conic theory.

Main gap: residual primitive Beal signatures remain open. Intermediate
target: one exact affine point with u,v nonzero on L150's eta_class
rational-branch conic. Such coordinates could supply one input to the
later constructive pairing calculation. L148's rational-radical stop and
ATTEMPTS/065's raw rational isotropy box are different fixed tests.

Essential inputs: L138's actual K/model, L135's maximal-order basis,
L147/L149's entire 39-column source order, L150's full representative,
and accepted L152 existence. Bind the four complete conic certificate
families and their replays. No cross-notebook input is used.

Fixed test: denominators in order 1,2,3,5,6,10,15,30, then coefficient
tuples in lexicographic order on {-2,-1,0,1,2}^4; omit v=0. This visits
at most 5000 prescribed tuples. Use Decimal precision 200, four cached
root brackets with exactly 450 bisections each, at most 16 signs per
tuple and 80000 total proposals, denominator reconstruction cap 10^12,
and rational bit cap 8192. Stop at the first exactly accepted point or
the fixed domain/caps. Preserve the full search and replay evidence.

Accept only exact field substitution with u,v nonzero, independently
replayed in the maximal-order basis. A failed proposal or exhausted box
does not prove nonsquareness or insolubility. On exhaustion park this
experiment, with no automatic enlargement. Explicit M-coordinates,
transport, cochains, pairing, rational Kummer membership, generation,
point control and integer/signature recovery remain separate gaps.

## Execution and limits

Run `python3 scripts/pair-genus-two/rational_branch_positive_search.py`.
Full inputs, SHA-256 bindings, all exact v/target coefficients and all
numerical screening values are saved in
`scripts/pair-genus-two/rational-branch-positive-search-certificate.json`.
The producer authenticates all four complete conic families and replays,
reconstructs the entire mask 132102 product in the prescribed source
order, checks the actual basis/root map, and matches both exact square
coefficients against L150's saved conic.

The completed fixed scan visits 5000/5000 tuples, omitting eight zero
tuples: 4992 nonzero v values, with duplicates retained. Every trial is
`unresolved_negative_approximation`: at least one of its approximate
real evaluations is negative. Thus there are zero sign proposals out
of cap 80000, no reconstructed candidate u, and no accepted point.
All four root proposals use exactly 450 refinements, 1800 total, at
precision 200. Maximum exact rational size is 85/8192 bits. The producer
reports 85079 checks and no failures. These checks authenticate inputs,
caps and this search execution; they do not certify a real sign,
nonsquareness or a negative conic theorem. The numerical values were
proposal screens only, even though all screens had the same outcome.

As prescribed by the prior method review, independent maximal-order
point replay is not invoked because no exact point was found. No lemma
or argument change follows. Mathlib coverage for this fixed experiment
is unchecked. This is mathematical EXPLORATION, with no advance beyond
the checked known methods and no informative insolubility result.

Two source-schema adapter failures occurred before any tuples or root
refinements. They remain in
`scripts/pair-genus-two/rational-branch-positive-search-initial-schema-failure.json`
and `scripts/pair-genus-two/rational-branch-positive-search-initial-helper-binding-failure.json`.
The repair distinguishes the dyadic producers' single helper hash from
the replays' different single helper hash; it preserves all source
checks. No mathematical trial was repeated to repair these failures.

Park this fixed search without box/precision enlargement. L150–L152's
existence and existential goodness remain accepted; explicit coordinates
remain absent. The next proposed mechanism is a source-level test of
odd-degree base change and Richelot-isogeny descent, which is outside
the present coverage and requires a separate literature turn. No such
base-change or pairing reduction is asserted here.
