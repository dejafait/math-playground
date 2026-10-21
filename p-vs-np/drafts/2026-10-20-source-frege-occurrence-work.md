# Step 382 — source-Frege occurrence interface work

Approved target: the COVERED_TARGET in
`literature/2026-10-20-source-frege-occurrence-product-witness.md`.
Main gap: unrestricted SAT decision/separation. This attempt supplies only
a proof-dependent exact-product witness, not short proofs or universal W₂.

Construction being checked: choose one occurrence representative per
source variable and uniformly substitute the entire supplied Frege proof,
sending foreign proof variables to an existing gadget occurrence. Keep
the exact source CNF tree as C_F and put C=C_F∧(gadget clause conjunction).
For G=C∧U, use group projections/case elimination to derive guarded leaf
equivalences, then bottom-up connective congruence to derive G→θF.
Append the substituted proof of ¬θF and a fixed contradiction template,
obtaining an assumption-free proof of ¬G. This avoids guarding or
unfolding the source proof's arbitrary intermediate formulas.

Next checks within this attempt: full written-proof polynomial before
applying L097's generic corrected extraction; exact complement convention;
reuse J to recover fg rather than f g̃; empty clauses, singletons, constants,
foreign symbols and reference reuse. Continue only if both formal
identities and one fixed polynomial in original Q hold. No source search,
new inference rule, proof-availability premise or new coverage decision
is needed. Full result, if completed, will be canonical in L098; this
file is a saved work note, not a second proof or dependency index.

Completion: the full informal construction and original-Q ledger are now
in `lemmas/L098-source-frege-occurrence-product-affine-abp-witness.md`
(notebook-relative path). Its independent critical audit is still pending.
Scoped documentation validation passes; that validates storage structure,
not mathematical correctness. No script or executable certificate was run.
