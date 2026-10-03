# Fixed tensor packet — completed calculation record

The ready SPECIALIZE assessment is [the existing local-hull screening](literature/2026-10-03-hull-transport-screening.md), including its exact COVERED_TARGET. This calculation reuses that assessment. Source retrieval only recovered its already-read definitions and displayed transitions; no fresh literature search or changed-target calculation is authorized here.

The gap tested is whether the two stated constraints on beta suffice for Dupuy–Hilado (6.5)–(6.6) after the full lattice automorphism orbit. A valid failure could exclude this auxiliary justification from numerical output work. It would not establish failure of the native enclosure or finite B ≥ A. The discriminating threshold is the rounded orbit hull itself, not an unsaturated lattice inclusion.

Let pi = sqrt(2), K = Q_2(pi), a = 1 tensor pi, and Phi(x tensor y) = (xy, x sigma(y)). The exact logarithm calculation gives log(O_K^times) = 4 Z_2 + pi Z_2 and I_K = Z_2 + (pi/4) Z_2. For I = I_K tensor I_K, the basis images are e1 = (1,1), e2 = (pi/4,pi/4), e3 = (pi/4,-pi/4), e4 = (1/8,-1/8). Its coordinate hull has radius 8 in both K components.

The different is (2pi). The tensor order T consists of (x,y) in O_K^2 with x-y in 2pi O_K, and its conductor is (2pi O_K)^2. Both beta_2 = 1 tensor 2pi and beta_1 = 2pi tensor 1 satisfy beta O_L subset T and component valuation 3/2 = sum(diff)-max(diff). They arise by omitting either of the tied maximal-different factors.

For beta_2, a/beta_2 = 1/2, so rounding to exponent floor(1/2-3/2) = -1 is exact, including the automorphism orbit. For beta_1, a/beta_1 = (1/2,-1/2); its action on the I basis is e1 -> 4e4, e2 -> e3/2, e3 -> e2/2, e4 -> e1/16. Its full GL_4(Z_2) saturation is I/16, with component hull radius 128, exceeding the rounded I/2 hull radius 16. The basis swap e1 <-> e4 sends the image of e4 to e4/16 and supplies a direct witness.

The initial save left the analytic logarithm argument, conductor checks and complete automorphism saturation unfinished. These are now proved in [L007](../lemmas/L007-tensor-log-shell-rounding-depends-on-beta.md), with the exact finite matrix checks in [the computation output](../scripts/tensor-hull/result.json). The favorable beta is essential to interpreting the outcome: a failing admissible choice alone does not refute the existential packet bound.

The new evidence excludes a beta-independent justification of this saturated transition. Before saturation the coordinate hulls are equal, so merely checking the multiplier's component absolute values misses the failure. The [native theorem](../foundations/04-native-local-enclosures.md) is imported on its own input a O_L, not this enlarged intermediate lattice. Neither the local radii nor their ratio has been identified with normalized A or B, and the required finite B >= A remains untouched.

The source's bad places exclude residue characteristic 2, and its other-place scalar is 1. The nonunit scalar in this screened packet is therefore not an actual theta-pilot instance. The beta-only objection to an existential bound stops here; a different scalar with the canonical beta is a distinct target requiring a fresh assessment. No calculation of that changed target is included in this step.

Outcome: NEGATIVE; kind: RESEARCH; classification: POTENTIALLY_NEW in the bounded-search sense only. The different formula and native enclosure are known imports; the explicit logarithm/orbit test is a specialization, and the checked literature did not provide its two-choice counterexample. There is no certified novelty or candidate essential IUT flaw. This is one informative mathematical attempt, not an uninformative exploration or a reset of the parked defect/quotient sequence.

Prior redundancy check: L001–L006 and ATTEMPTS/001–006 concern normalization, collapse, markings or blocked global source correspondence. None computes this actual tensor log-shell or its saturated rounding transition. Their failures remain in force. No original IUT initial theta data or Ind3 envelope is asserted here.

Mathlib coverage: full fixed-packet statement and supporting log/exp, local-field and lattice-action results **not checked**. Primary references are Dupuy–Hilado arXiv:2004.13108v2, Definition 4.3.1, Theorem 2.8.1, Remark 2.8.2 and (6.5)–(6.7); the native IUT IV Propositions 1.2(ii), 1.4(iii) remain citation inputs, not a theorem being reproved.
