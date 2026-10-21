# Core-conditioned pair/theta working checkpoint

Approved target: Establish a sound core-conditioned pair-plus-recursive-theta upper-bound reduction and its exact local threshold test for 68-agreement support families.

Inputs read: L001, C001a, L020, and foundations/07-core-conditioned-theta-source.md. Reused SPECIALIZE assessment: drafts/literature/2026-10-06-core-conditioned-pair-theta-reduction.md. Preserve ATTEMPTS/010 and all earlier stopped certificates. This is a REPRODUCTION proof attempt, with no SDP implementation.

Construction under examination: for every 61-core C use all 7-subsets of H minus C; impose pair edge-zero constraints for intersections of size at least three and the source's recursive constraints for precisely the labeled nonsingular L020 triples, on one shared lifted matrix. An actual local family should admit its indicator outer-product lift. PSD should handle zero diagonals without division. The 3-subset cliques should imply the ordinary packing cap.

Counting to verify: each selected 68-support contributes binomial(68,61) incidences; all cores number binomial(1024,61). Local maxima may depend on C. Exact threshold comparison must retain integer rounding and threshold T=65537^28/2^128. No improved local cap, symmetry reduction, sufficient certificate, actual relaxed optimum realization or safety at 67 agreements is assumed.

Continue if the same lift supports both constraint sets and the incidence multiplicities are exact. Abandon an unsound formulation; if only the reduction succeeds, report it with the quantitative gap. Save the finished proof in L027 rather than treating this working note as evidence.

Completed: the canonical proof is lemmas/L027-core-conditioned-pair-theta-reduction.md. All soundness and counting obligations hold; no improved cap was obtained. Exact arithmetic is saved in scripts/finite-support/core-theta-threshold-results.json. The canonical proof, rather than this checkpoint, records the result and its limitations.
