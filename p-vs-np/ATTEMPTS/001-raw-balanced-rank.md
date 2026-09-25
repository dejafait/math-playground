# Raw balanced rank as a circuit lower-bound certificate

Tested 2026-09-24. The proposed use was to find exponentially many SAT residual functions, strengthen this to exponential real matrix rank even after choosing the best balanced split, and transfer that bound to unrestricted circuit size.

**WHY IT FAILS.** [L001](../lemmas/L001-balanced-rank-small-circuits.md) supplies SAT slices with exponential rank and residual counts at every balanced split of the free bits, while their decision functions have quadratic-size general circuits. Minimizing over those splits therefore does not repair the false rank-to-size implication. The refutation concerns a universal inference from these statistics alone; it does not prove SAT easy, rule out richer invariants, or ban communication methods with an actual model-transfer theorem. A renewed rank approach needs a specific additional property and a test showing why the small quadratic-parity circuits do not satisfy it.
