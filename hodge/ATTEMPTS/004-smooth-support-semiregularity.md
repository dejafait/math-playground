# Attempt 004 — Smooth-support semiregularity for the cubic correspondence

Date: 2026-09-25. Outcome: rejected for the embedded support of C_1; singular deformation methods remain open.

The proposed shortcut was to treat the smooth source of L006's pushforward as a smooth embedded surface in S x S and apply a normal-bundle semiregularity calculation along the extra RM direction. The geometric audit and the correct first-order formulation are in [L007](../lemmas/L007-cubic-correspondence-deformation-model.md).

**WHY IT FAILS.** The reduced support has two transverse surface branches at the pair of zero-section points over infinity. Its codimension-two ideal needs four generators, so the support is neither smooth nor lci there. Its normal sheaf has a four-dimensional fibre at that point and is not the rank-two normal bundle assumed by the shortcut. A smooth resolution mapping onto this support is not an embedding. Generalized singular semiregularity still requires a suitable obstruction space and an injectivity calculation. The computed local first-order deformations are all induced by ambient coordinate changes, so this failure of hypotheses is not a nonzero global obstruction, a failure of every cycle representative, or a counterexample to the Hodge conjecture.
