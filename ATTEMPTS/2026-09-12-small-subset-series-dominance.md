# Small-subset dominance for the heat-center series — 2026-09-12

Attempt: lower-bound the explicit S(t) from L138 by retaining one or a small selected collection of terms, evaluating that collection, and subtracting the absolute mass of all remaining terms.

WHY IT FAILS: [Lemma 139](../lemmas/L139-absolute-series-mass-and-dominance-obstruction.md) proves that any o(sqrt(t)) selected terms contain a vanishing proportion of the absolute series mass. Even exact evaluation of the selected sum leaves a negative reverse-triangle lower estimate for sufficiently large t. This rules out this specific dominance method, including adaptive selection, but does not rule out estimates that exploit cancellation in the complementary sum or a lower bound for the full series. The theta cancellation question and RH remain unresolved.
