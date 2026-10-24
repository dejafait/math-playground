# Step 430 — fixed constant-template reception work

Approved target: prove reception and full-bit instantiation bounds for
fixed constant-bearing tautology templates in L108's exact four-rule
system. Prior SPECIALIZE coverage is
`drafts/literature/2026-10-23-four-rule-constant-template-reception.md`.

Main gap: unrestricted SAT. Intermediate target: exact assumption-free
proof existence and a library-dependent full-bit instantiation bound.
Downstream use: supply logical templates before a separately assessed
occurrence/parity composition. Continue if the constant-premise replay
preserves every literal rule and the exact endpoint; abandon this
specialization on an extra rule, residual assumption, unremoved name or
unpaid formula expansion. L107 and Attempt 036 stop the old presentation,
not this different system. No applicable duplicate was found in the
targeted local comparison; the prior source review is reused.

Working argument (not yet a canonical proof): replace true/false by
distinct atomic formulas p/q, constrain them by nonlogical axioms p and
NOT q, and apply Shoenfield's cited propositional consequence theorem.
Replay atomic images simultaneously; the two added axioms become true
and NOT false and all four rules commute literally with replacement.
Then select one fixed finite proof per library member. Each slot has
only a library-dependent number of occurrences across that entire
proof; instantiation copies the supplied tree at each occurrence once.
Charge actual names, all unused supplied trees/alphabet if retained,
framing and backward references. Need distinguish the unbounded
preparation of a library from efficient instantiation after it is fixed.

Remaining independent gaps: source/occurrence composition, original-Q
integration, short proof availability, M-only bounds, universal W₂,
arbitrary ER data and unrestricted SAT. No implementation is claimed.

Completed: the canonical proof and precise encoding qualifications are
in L109. The working proposal above is preserved as unfinished-stage
context; it is superseded by that proof. A separate critical audit is
proposed, with REVIEW_REQUIRED coverage, rather than performed here.
