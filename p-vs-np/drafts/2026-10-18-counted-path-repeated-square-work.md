# Step 320 — repeated-self-AND obstruction work checkpoint

Approved target and coverage: `drafts/literature/2026-10-18-counted-path-repeated-square-obstruction.md` (pre-invocation EXPLORE). One proof attempt; no new source review or cross-notebook input.

Main gap: unrestricted SAT decision/separation. Intermediate target: a genuinely used conjunction/self-AND ER family forcing |D|>=n-k and M>=2^(n-k) at actual original T. Downstream use: determine whether L080/L081's structural promises can hold universally for supplied short proofs, without claiming alternative-certificate hardness. Continue only with legal ancestry, polynomial full bits, chain length >k, n>2k and unbounded (n-k)/log₂(T+2); otherwise preserve the precise failed assumption.

Inputs inspected: L080 hypotheses; L081 hypotheses; L082 full replacement proof through its cardinality qualification; L027 full signed-unit/accumulator/encoding template; foundations/05 ER convention. Reuse the supplied assessment's duplicate/failure comparison. L027's HWB theorem is not an input to the intended bound.

Unfinished construction: F has units x_1,...,x_n, NOT x_1. Positive conjunction gates c_2,...,c_n; n² successive fresh s_t iff s_(t-1) AND s_(t-1), with s_0=c_n. All core gates true at all ones. H=n²+n-1 core gates. L027's positive/negative accumulator device uses every core signed unit and its own definitions in final ancestry. Conservative R_*=11H+n+2 records and gamma-code bound T<=128(R_*+n+3)ceil(log₂(R_*+2)) need checking for this instance. If n-|D|>k, all n² square gates are counted on one retained ancestry path. L082 can then transfer the unrestricted-set lower bound to arbitrary M. The actual cutoff/finite start and complete proof remain to be finished; this checkpoint is not a result.

Completed: the canonical all-size proof is now L083. The pending inequalities and complete ancestry/encoding checks above are resolved there, with n=2^r, r>=10. Outcome NEGATIVE for universal structural coverage, not an optimal-certificate or SAT lower bound. Separate critical audit remains pending; this draft preserves the unfinished checkpoint rather than duplicating the proof.
