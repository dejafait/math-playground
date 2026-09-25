# 2026-09-24 — Primary statement and independent-link test

Read the shared policies, local target and checkpoint, entire overview, and empty DAG. The active notebook had no unfinished changes, lemmas, or failed approaches. Existing changes outside this notebook were left untouched.

The [source audit](../foundations/01-target-and-scope.md) confirms the official formulation and its finite-mass condition. [Lattice foundations](../foundations/02-lattice-and-reflection-conventions.md) distinguish named reconstruction and lattice positivity results from the missing continuum estimates.

The named gap was physical nontriviality after cutoff removal. The selected intermediate target was the exact beta = 0 plaquette fluctuation limit and its reflection quotient. The discriminating threshold was a positive centered reflection norm, rather than ordinary nonzero variance. This was one coherent soluble-endpoint test, not a survey claiming to settle all strong-coupling routes.

[L001](../lemmas/L001-independent-plaquette-noise-has-trivial-reflection-space.md) proves the white-noise limit in all smeared joint laws and moments, and the collapse of the entire positive-time polynomial reflection quotient. Its exposed-edge argument proves exact independence and replaces the more general connected-cumulant idea saved in the [draft](../drafts/2026-09-24-independent-link-continuum-test.md). No numerical evidence is used.

Decision: informative negative result. The [direct endpoint attempt](../ATTEMPTS/001-independent-link-plaquette-continuum.md) is stopped. The achieved reflection norm is zero, whereas a surviving nonvacuum state requires a strictly positive value; the vacuum-only quotient also has no finite excited mass. This narrows a construction route and does not reduce the unresolved existence claim to a proved criterion. Exploration turns used: zero inconclusive turns.

The reason for moving toward published ultraviolet constructions is that the exactly soluble endpoint cannot retain physical states in the tested sector. An existing cutoff-removal construction may expose an observable estimate worth strengthening. Magnen–Rivasseau–Sénéor (1993), *Construction of YM4 with an infrared cutoff*, is identified in the official bibliography, reference [29]; its proof and relevant lower bounds have not yet been audited here. The sole current action is recorded in PROGRESS.md.

Mathematical review checked the unique-edge argument, the distinction between one orientation and all plaquettes, the separate proof of moment convergence, and factorization for arbitrary positive-time polynomials. L001 has no earlier local lemma inputs, so the DAG has one isolated node. Mathlib coverage is explicitly not checked.

Validation: `python3 ../scripts/docs/check_structure.py --problem yang-mills` passed with one node and zero edges; `git diff --check -- .` also passed. No computational approximation was needed for the mathematical test.
