# Two-observation compact scalar cost stop1798

19 November2026. Approved fixed-width interpolation screen1796/1797
stopped before scalar evaluation. The full restricted cost proof is
[C033x](../lemmas/C033x-compact-excision-scalar-preflight-cost-stop.md),
with its exact four-radius certificate in
`scripts/smoothed-law/two_observation_compact_cost_1798.json`.

WHY IT FAILS: The prescribed C033m compact subtraction allocates
profile error d<epsilon/12. Its small-endpoint allowance forces a
small cutoff, which makes the displayed first-derivative midpoint
allowance require more nodes than the entire operational cap, already
at epsilon=2^-8. The proof does not use the stopped common spatial
disk, huge quadrature execution or a rounded solve. Failure belongs
to this particular allowance and literal evaluator, not the actual
errors, transform values, singularity, all evaluators or existence
of a TV<=2 interpolant. No matrix or TV conclusion was reached.

Park this implementation. A separate source review is nominated for
direct positive-real Levy-time scalar evaluation with explicit tails;
that different mechanism remains uncovered and no new derivation is
approved. All previous stops and unfinished work are preserved.
