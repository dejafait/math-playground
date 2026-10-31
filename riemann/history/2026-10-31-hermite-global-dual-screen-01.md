# 2026-10-31: complete Hermite dual screen

The approved EXPLORE assessment was reused unchanged, with no source
review or new literature approval. [L567](../lemmas/L567-complete-hermite-band-dual-specialization.md)
specializes known chordal decomposition, closed-image and conic
separation theory to the complete finite Hermite problem. It supplies
all dual constraints, including singular cases, and the entire pairing.
This is local reproduction/specialization, not a novelty claim.

The bounded screen at N=64,128,256 found numerical negative complete
D(P_N) values at x=163/4,271/4,447/4. All allowed-square constraints
at these evaluation functionals pass exact integer checks (896
diagonals, 890 edge blocks). Full diagnostics and constraint evidence
are saved in `scripts/hermite-gram/global-dual-screen.json` and
`scripts/hermite-gram/global-dual-evaluation-constraints.json`.

Outcome EXPLORATION: zero certified negative pairings. Two numerical
quadrature meshes agree, but neither a quadrature remainder nor the
complete omitted theta/spatial tails is enclosed. This neither rejects
the sparse Gram cone nor establishes feasibility. The evaluation
points are outside the corresponding L564 intervals; a later rigorous
global rejection would not settle those interval signs, signed Xi
transfer, or the all-degree main gap. L565/L566's parked tests retain
their scopes. PROOF's main assembly is unchanged.

Continue the same ready finite screen with rigorous full pairings at
these fixed rational points before considering an unbounded family.
The first numerical script requires the existing Anaconda Python 2
sympy.mpmath; the exact constraint script uses Python 3. No package
was installed and no shared infrastructure or supervisor state changed.
