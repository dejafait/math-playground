# Shortened cubic incidence diagnostic — completed negative test

Gate-approved target: Test whether the prescribed shortened cubic graph packing over F_121 gives an above-threshold incidence-avoiding obstruction to a uniform 60-core bound.

The ready EXPLORE assessment is `literature/2026-10-07-shortened-cubic-four-pattern-test.md`. The main gap is arbitrary-center safety at 68 agreements. This step tests only the fixed eight-position cubic family, not another evaluation set or field. A valid incidence witness stops whole-pattern avoidance; a search miss does not prove it. Exact 60-core size/cap comparison is conditional on complete avoidance and will not be executed after a witness.

Inputs checked: L001's root proof, C001a's finite instance, audited L031's distinction requirements, L027's selected-support and incidence method. ATTEMPTS/019–022 retain the exhausted local model and administrative park; none completes this diagnostic. L030 is comparison only. Reuse the assessment's AGL signed-matrix framework; no generic-rank or asymptotic-existence theorem is applied.

Bounded attempt: look for four cubics of the form h,h+f,h+g,h+f+g. Partition T={0,...,7} into four pairs on which f, g, f-g, f+g respectively vanish. Solve the resulting homogeneous eight-by-eight signed system over F_11. Verify full graph intersections, private points, opposite-edge coordinate reuse, all deleted points and field arithmetic on an actual witness. This is only a search subset of the assessed family, not an assertion of completeness. If successful, translate all polynomials by u to satisfy shortening and check every value exactly in F_11[u]/(u²-2).

Result saved in [L032](../lemmas/L032-shortened-cubic-incidence-counterexample.md): the twentieth tested partition gives f=2X+9X² and g=1+4X+4X²+X³. Translating the four parallelogram polynomials by u gives a complete valid incidence witness inside the shortened family. The full witness object was inspected; the exact script checks all intersections, private parts and field inverses with no failures. This is a negative test of whole-pattern avoidance, not an exhaustive search or an RS-list witness. The conditional cap comparison was not performed.

Unresolved independently: finite labeled 60-core cap/transfer, cross-core consistency, common-center RS realization, 67-agreement safety and ABF comparison. The changed three-support/three-point-overlap continuation requires separate source coverage; no criterion for it was derived here.
