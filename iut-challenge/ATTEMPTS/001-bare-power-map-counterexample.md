# Bare power-map counterexample

Assessed on 2026-09-24 as part of the initial source audit.

The attempted shortcut was to infer an IUT flaw from an abstract identification of p with p² while computing both lattice volumes in the same normalized p-adic field. [L001](../lemmas/L001-cyclic-monoid-isomorphism-does-not-control-volume.md) gives the exact elementary calculation. Its relevance and primary-source overlap are recorded in the [audit](../drafts/2026-09-24-source-and-normalization-audit.md).

WHY IT FAILS: the monoid isomorphism does not preserve the fixed valuation, and being executable in one field does not establish the original comparison properties. No full initial Θ-data, log-theta-lattice, or image family under (Ind1)–(Ind3) was supplied. The example therefore refutes only a weakened implication. Treating it as an IUT counterexample would change the hypotheses at precisely the point being investigated. This stops the bare power-map shortcut; it does not decide whether the original comparison succeeds or prohibit a test of the actual maps.
