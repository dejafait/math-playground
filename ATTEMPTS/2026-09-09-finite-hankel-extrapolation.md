# Attempt: infer all-degree positivity from increasingly many finite Hankel tests

Date: 2026-09-09

Outcome: failed finite-to-infinite inference; the finite actual-Ξ certificates remain valid.

The mathematical counterexample or obstruction is proved in [Lemma 57](../lemmas/L057-any-fixed-number-of-hankel-tests-can-coexist-with-nonreal-zeros.md).

**WHY IT FAILS.** A fixed finite collection of strict positivity tests is stable under small changes of finitely many coefficients, while nonreal zeros can be introduced arbitrarily far along the strip. Thus no finite number of these tests, even combined with all the established generic structural conditions, supplies the all-degree condition. The quantifiers are crucial: for each N a possibly different a_N is chosen; no single nonreal-zero function is claimed to pass every degree, which would contradict the proved criterion. A successful RH argument must control the entire family uniformly, using more specific information about Ξ.
