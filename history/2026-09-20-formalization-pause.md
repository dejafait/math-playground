# Formalization paused by user

The user requested informal research with global relevance checks, and explicitly paused all Lean work until a later decision to validate a candidate argument. No Lean proof work was performed in this policy update. Existing sources and lemma changes are preserved. The former current checkpoint below is archived context, not an active task.

# Current notebook state

STATUS: IN_PROGRESS

Workflow: choose exactly one mode at turn entry using GOAL.md and PROMPT.md. Existing incomplete Lean proofs take priority over research; never do both in one turn.

Current checkpoint: the Lean backlog is nonempty. L001–L016, L031, and L034 are labeled fully validated; L028 is conditional on unformalized moment inequalities and remains backlog. Other pending entries remain explicitly unvalidated. Reinspect current files rather than relying on these counts or labels alone.

Current Lean work: LEAN CATCH-UP proved L017’s real absolute-integral evaluation and summability of the theta-term absolute integrals for Re(s)>1. L017 remains partial: the sum–integral interchange and full gamma–zeta identity are open. Mathematical text and prior changes are preserved.

Deferred research checkpoint (not an action while Lean backlog exists): L231 gives second-derivative and sawtooth estimates, neither reaching o(B_0). L230's P=F_H+o(B_0) remains the current informal result. Once all existing full statements are Lean-validated at turn entry, investigate the third-derivative test for L230's paired b sums for 1<=k<=floor(N^(1/4)), summed over e<=N^(1/4), leaving higher frequencies explicitly unproved. Cancellation, the signed comparison, and RH remain unproved.

Next action: In `scripts/lean/Rh/L017.lean`, justify termwise integration of the theta Mellin series using `thetaTerm_summable_integral_norm` and `hasSum_integral_of_summable_integral_norm`, first supplying individual summand integrability from the real-power exponential majorant.
