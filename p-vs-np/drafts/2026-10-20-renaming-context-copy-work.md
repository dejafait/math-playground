# Step 386 — saved renaming context-copy attempt

Approved target: the exact COVERED_TARGET in
`literature/2026-10-20-substitution-frege-occurrence-transfer.md`.
Reuse that EXPLORE assessment; no new source review is needed.

Main gap: unrestricted SAT decision/separation. Intermediate test:
polynomial original-Q size for literal context copying in the corrected
axiom/MP extraction with supplied variable-renaming inferences. A positive
bound could support a stronger proof-dependent supplier; a negative
family stops only this implementation. Occurrence normalization,
short-proof availability and general transfer remain independent.

Fix the implementation before continuing: propagate requested renaming
contexts backwards from the final output. MP requests both earlier
witnesses, with the translated conclusion as the right multiplier of
the antecedent witness. Renaming requests the parent under the composed
map. A copied local block may be merged only with the same source block
under an action agreeing on its actually occurring labels. Affine labels
are collected over F₂; dictionary-only differences do not count. Permit
discarding graph pieces with no source-to-output path. Do not replace
this implementation by a newly synthesized certificate or factorized
representation of the set of contexts.

Candidate family to check: take X_n=x_1 OR ... OR x_n and the axiom
T_n=X_n -> (true -> X_n), whose translation is a+a² for
a=x_1...x_n. At stage i rename x_i and x'_i, then use the previous
T_n and the axiom T_n -> (rho_i T_n -> T_n) to combine the two
premises back to T_n. Independent swaps may force all 2^n contexts of
the first axiom seed. Finish at the negation of an explicit contradictory
width-three CNF containing all these source variables, using T_n as a
genuine final MP antecedent. Charge the full occurrence package.

Outstanding checks in this attempt: formal placeholder reception even
when names merge; nonzero final and intermediate multipliers; distinct
actions on used seed labels rather than on unused names; final ancestry;
full polynomial input length; scope before occurrence normalization.
Continue only with a uniform polynomial ledger or a rigorous active-copy
lower bound. Preserve a partial result if these obligations do not close.

Completion: the all-size informal obstruction and noninjective reception
are canonical in `lemmas/L099-renaming-literal-context-copy-obstruction.md`
(notebook-relative path). The source family has 2^n distinct used seed
copies with Q≤C(n+2)³. This stops only the fixed whole-seed-copy
implementation, not arbitrary sharing or alternative witnesses.
Separate critical audit remains pending. No mathematical script or
verified translator was produced.
