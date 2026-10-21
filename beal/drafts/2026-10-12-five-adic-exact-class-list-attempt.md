# Exact five-adic class list — working attempt

2026-10-12. Approved target: Compute a certified exact list of L060's whole-fiber connecting classes at five, retaining both scalar disks and all class collisions.

Main gap: global primitive integer emptiness. Intended downstream use: a faithful local membership test in a future global class intersection; global classes, other places and integer lifting remain unresolved. Reuse the supplied SPECIALIZE assessment and L033–L035, L037–L040, L060. ATTEMPTS/010,012 remain parked.

Bounded test: certify both full residue factorizations as one rational and one unramified degree-eleven factor, reverse reconstruction including 2T, all 550 scalar/embedding pairs modulo 125, and exact fifth-power collision decisions. Stop short of an exact-list claim if any part fails.

Work in progress: choose the integral polynomial H2 from L039 as a fixed unramified model. Test classes using a unit's (5^11−1)st power modulo 25; justify both directions using an explicit fifth-root solver modulo 125 and the already imported strong Hensel theorem. Save every embedding, collision witness and noncollision label on disk. This is a specialization attempt, not an established result yet.

Completed attempt: the bounded splitter at residue four first failed because the assumed degree-eleven residue factor is false. Complete factorization is 1+1+5+5, uniformly excluding that disk; residue two is 1+11 and reconstructs the entire fiber for every scalar. The surviving 275 pairs give exactly 55 classes, each with five members. Full proof, explicit five-seed Frobenius list, exact realization and finite-root completeness are canonical in L061; construction and separate full arithmetic replay are in `scripts/five-adic-exact-list/`. All 275 collision witnesses and 1,485 noncollision pairs pass, along with 55 explicit-representative comparisons. This is a local REPRODUCTION advance; independent proof audit and all global gaps remain. The initial failed splitting function remains preserved in the script, although the corrected finite factorization supplies the final route.
