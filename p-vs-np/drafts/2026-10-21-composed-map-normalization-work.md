# Step 402 — Full-map cache test in progress

The pre-invocation EXPLORE assessment is
`literature/2026-10-21-composed-map-pathwise-normalization.md`; work is
restricted to its exact COVERED_TARGET. No fresh literature search is
needed. L101 §§1–2 supplies the source and materialization conventions;
L087 supplies the occurrence input ledger. Attempts 032–034 have been
checked and are preserved.

Candidate test: h layers, b=2^h parallel renaming choices per layer,
each choice swapping a selected subset of h disjoint variable pairs in
that layer's block. Use disjoint blocks across layers. A fixed axiom T
contains one member of every pair. Each layer returns to the same T by
first-scheme/MP merges but references every renamed premise. A backward
path takes at most one renaming per layer. Choices across h layers
should give 2^(h²) distinct full maps, and distinct requested T formulas.

Unfinished obligations: write every source inference and the exact ¬F
attachment with every map variable occurring in F; verify all-start
depth; prove actual request closure rather than possible-map count;
charge full F, occurrence M/B, maps, instantiation arguments and proof
references in original Q; compare the all-size record lower bound with
every fixed polynomial. No counterexample is certified by this draft.

The main SAT gap, short-proof availability and M-only bounds remain open.
A positive cache bound could feed L098 only after its hypotheses are
checked; a negative result stops only this normalization procedure.

Completed in step 402: canonical L103 now contains the complete source
construction, full-function/request distinction, ordinary-record count,
all-start depth and original-Q ledger. The result is NEGATIVE for the
specified cache, with separate critical audit pending. The provisional
notes above preserve the work checkpoint, not a second canonical proof.
