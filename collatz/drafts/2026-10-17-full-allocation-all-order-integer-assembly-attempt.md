# Full-allocation all-order integer assembly — step 271

The prior SPECIALIZE assessment is
`literature/2026-10-17-full-allocation-all-order-integer-assembly.md`.
The main gap is universal eventual descent. The approved intermediate
target combines L074's audited cyclic rigidity with C073a's audited
literal-simplex unshifted nonintegrality; it could support a separately
reviewed actual-word application. Other pairs, unrestricted cycles,
entry and divergence remain independent gaps.

Continuation test: identify the exact row-0 cut after rotation and match
the complete allocation, every endpoint and every own-input non-strict
J guard. Abandon this assembly if any of those hypotheses differs; do
not repair a mismatch by adding H/seed, a minimum location, actual-word
realization or primitive/count-ray assumptions.

Saved reasoning before writing the canonical proof: L074 implies that
the permutation is cyclically literal. Let q be the original chronological
position of indexed row 0. Then pi((q+i) mod 25)=i. Put
t_i=s_((q+i) mod 25) for 0<=i<=25. The indexed b_i and a_i stay
attached to their rows. C073a applies to t with exactly the original
allocation; its tested coordinate is t_0-23/11=s_q-23/11. The old
closing edge occurs at i=24-q, and the new closing edge is the old
edge q-1 to q (indices modulo 25). Thus all-junction unshifted
integrality contradicts C073a, without asserting nonintegrality of
each junction or of a predetermined chronological s_0-23/11.

Reused the ready source assessment and inspected canonical L074/C073a,
the full L055 pair table and L051 endpoint/guard definitions. Attempts
026–031 and the fixed-allocation assemblies are narrower or concern
stopped diagnostics; no new arithmetic computation is needed.

Completed: the full rotation and hypothesis match are now canonical in
[C074a](../lemmas/C074a-full-allocation-all-order-integer-exclusion.md).
The continuation test passed at the level of this assembly; independent
critical audit remains pending. No new calculation or source theorem
was needed, and no actual-word consequence was derived.
