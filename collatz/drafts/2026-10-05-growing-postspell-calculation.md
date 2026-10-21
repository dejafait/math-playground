# Growing-only postspell chain calculation

Ready input: `drafts/literature/2026-10-04-growing-postspell-initial-size.md`
(EXPLORE), saved before this invocation. Task: the exact K=1,...,5 screen
over 2<=J<=4, 3<=H<=5 with tail E^2, followed by a bounded symbolic
test of uniform initial-size control for J>=2,H>=3. Inputs: L020/L021's
positive affine offsets and imported whole-word parity coding/CRT.

The main gap is universal eventual descent. The intermediate target is
an initial-root bound n>=F(K), F(K) tending to infinity, uniform over
the full growing-only alphabet. It could exclude infinite chains of
these words; entry into the alphabet, other tails and compensation
remain independent unresolved gaps. No universal result is presumed.

Continue only if exact minima and symbolic constraints expose a bound
whose constants remain controlled for arbitrary J,H, or produce a
guarded counterexample to a specific proposed bound. Larger finite
minima alone are insufficient. Preserve internal exact E^2 tails and
the unconstrained parity at the final endpoint.

L005's fixed-word estimate is not uniform and its transferred sharp
bound fails. L008's density estimate retains a growing boundary error.
Neither failed argument will be reused. Prior unfinished L020/L021
work is preserved. Attempts 009–011 remain parked.

## Completed result

Outcome: NEGATIVE / RESEARCH / REPRODUCTION. The canonical arithmetic
and finite proof are in L022. The full 66,429-chain certificate is
`scripts/growing-postspell/result.json`; 132,863 guarded replays have
zero failed checks. A mixed two-word chain undercuts the repeated-(2,3)
minimum, and a four-word witness keeps every E^2 tail exact. The full
alphabet affine positive-endpoint estimate is negative for every K.

The five finite minima increase, but no uniform divergence for the full
alphabet is proved. Stop the repeated-word transfer and the vacuous
affine estimate; preserve Attempt 012. Do not enlarge the screen without
a new mechanism. A separate source comparison of extendible postspell
inverse rigidity is proposed; no decoder is derived or approved here.
This changes a route using exact new counterexamples, without a claim
of progress beyond the inspected finite-coding machinery.
