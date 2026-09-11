# Current notebook state

STATUS: IN_PROGRESS

Workflow: choose exactly one mode at turn entry using GOAL.md and PROMPT.md. Existing incomplete Lean proofs take priority over research; never do both in one turn.

Current checkpoint: the Lean backlog is nonempty. L001–L011, L031, and L034 are labeled fully validated; L028 is conditional on unformalized moment inequalities and remains backlog. Other pending entries remain explicitly unvalidated. Reinspect current files rather than relying on these counts or labels alone.

Interrupted Lean work: scripts/lean/Rh/L012.lean contains paired-series estimates, holomorphicity, and unfinished unpaired uniform convergence. Its last build failed; it is NOT a validated full proof. Resume from the actual source and fresh diagnostics. The zeta identity and removable value are still unfinished. No further proof work was performed during the workflow-instruction update.

Deferred research checkpoint (not an action while Lean backlog exists): L231 gives second-derivative and sawtooth estimates, neither reaching o(B_0). L230's P=F_H+o(B_0) remains the current informal result. Once all existing full statements are Lean-validated at turn entry, investigate the third-derivative test for L230's paired b sums for 1<=k<=floor(N^(1/4)), summed over e<=N^(1/4), leaving higher frequencies explicitly unproved. Cancellation, the signed comparison, and RH remain unproved.

Next action: In a LEAN CATCH-UP turn, resume L012 using the local Lake project, complete and validate as much of its existing full statement as possible, then record the exact remaining checkpoint without doing new research.
