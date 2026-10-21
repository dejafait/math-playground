# Step 374 — small-core occurrence witness working note

The ready SPECIALIZE target is unchanged. Main gap: unrestricted SAT
decision/separation; intermediate target: the original L087 product with a
supplied source core of at most floor(log₂ M) clauses. Downstream use is a
restricted W₂ supplier without a global order promise. Continue only if
formal branch closure and every original-M cost can be justified; a
surviving branch or a failed paid interface stops this construction.

Inspected L087's occurrence testers, L035's original-only graph interface,
L090's complete construction and separate audit, and Attempts 018/030/031.
The existing source comparison is reused, with no additional browsing.
Existing notebook changes and all earlier failures are preserved.

Working argument: query all s≤3c selected occurrence names. If their bits
disagree within an old-variable group, every completion fails E. Otherwise
they induce an old-variable assignment on the core; unsatisfiability gives
a false selected clause, so every completion fails D. Each restricted
factor separately has an increasing-multilinear representation in its own
order. L026's injectivity therefore makes that factor formally zero.
L090's branch witness can be the zero graph; its common residual order
assumption is not needed by the other components.

Pending ledger: t=2^s≤M³, not M. Reuse the pre-cutoff bound
K(t+1)²(M+2)^12, then check annotation extraction/verification as well.
Source CNFs with arbitrarily many empty clauses are a potential encoding
pitfall: M measures the explicit occurrence pair, not a separately supplied
source serialization. Prefer a constructor operating on the unchanged pair
and clause-index annotation, with branch closure verified by Boolean
reachability on each restricted tester. Actual y_(j,k) occurrence names
identify the queried set; appended gadget indices bound clause indices.
Do not assert that scanning an arbitrarily redundant source file costs
polynomial time in M.

Completed in L096: the constructor receives the unchanged pair and
canonical clause indices, extracts their occurrences, and verifies
sufficient branch closure directly on each Boolean tester. Source-to-pair
provenance remains L087's input promise; a second source serialization is
not read or charged to M. The complete formal assembly and R^18 ledger
are canonical in L096. Separate scope approval and critical audit of this
interface remain pending; this work note is not an audit certificate.
