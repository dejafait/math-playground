# Archived succinct trace audit sketch — 2026-09-24

The existing rank obstruction and its archived draft were inspected and preserved. This step tests the different mechanism selected in the preceding checkpoint; it does not reopen the rank inference.

**Gap.** A clocked diagonal construction needs one fixed polynomial-time NP verifier. Compressing a computation lasting n^k or longer into a circuit does not by itself bound the time required to verify every transition, independently of the simulated machine's exponent k.

**Intermediate target and downstream use.** Determine the complexity of validating a supplied circuit that outputs the configuration at each binary time address. A sound polynomial-time validator could help place a succinct diagonal construction in NP, but polynomial-size descriptions of the needed traces and the all-machines diagonalization would remain separate gaps. The test here is only validation of the proposed compression.

**Discriminating test.** Reduce circuit tautology to local consistency of a trace for a fixed stationary machine, keeping the initial and final configurations correct and the binary horizon description length linear in the tautology input arity. If this works, generic validation carries a coNP-complete obligation and the compression alone cannot establish the required NP verification bound. This would stop the unrestricted-validator shortcut, without asserting P != NP or ruling out restricted trace formats. If the reduction fails because of genuine configuration or endpoint constraints, isolate that restriction and assess whether it gives a validator.

**Completion.** The sketch was saved before writing the proof. [L002](../lemmas/L002-succinct-trace-validity.md) completes the reduction and its complexity consequences. It strengthens the original stationary-start sketch by using an ordinary initial configuration followed by a one-step accepting computation, padded by the standard halting self-loops. Correct endpoints, legal encodings, the first transition, strict interior addresses, and full input-length bounds are checked in that proof. The preselected failure test succeeded. A supplementary sparse-defect case also quantifies the failure of uniform local sampling.

**Required threshold.** The desired verifier runs in N^d for a fixed d, where N is the full supplied description length, not in a polynomial in the numeric time horizon T. Also distinguish a deterministic validator (whose existence here would imply P=NP) from an NP certificate for validity (whose existence would imply NP=coNP), and distinguish validation of every supplied description from existential selection of a different trace description for the same computation.

No complexity separation or candidate resolution is claimed. This archive carries no unfinished proof or current action.
