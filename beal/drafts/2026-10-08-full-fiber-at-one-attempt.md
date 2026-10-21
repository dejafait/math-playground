# Fixed whole fiber at one: certification attempt

Start: 2026-10-08, using the unchanged SPECIALIZE assessment in
`drafts/literature/2026-10-08-full-fiber-at-one-local-algebra.md`.

The main gap is global emptiness for the surviving signatures, including all
five L032 twists. The sole intermediate target is the complete Q5-algebra
comparison B_1 versus A. L033 supplies m; L034 supplies the complete monic F1
and y reconstruction; L035 and L037 supply the whole-fiber interpretation;
L036 supplies primitive scalar membership at 1. A certified match could
establish nonemptiness of both local images. An intrinsic invariant mismatch
rejects this scalar only. Neither result decides image strictness or global
emptiness.

Continuation test: account for twelve dimensions on each side and either
certify every factor pairing or prove a complete-algebra invariant mismatch.
If repeated residue blocks cannot be certified within this bounded attempt,
save their exact polynomials and required versus actual lifting bounds;
do not infer a decision from finite precision. General lifting and
unramified-extension classification are imported from the assessed Milne and
Clark theorems, rather than reproved. ATTEMPTS/008–010 and the L037 encoding
remain intact; local records contain no completed comparison for this pair.

Initial implementation fact: python3 has no SymPy, and the preceding source
review found no gp/sage. Use exact integer and finite-field arithmetic without
installing packages. No mathematical result is asserted at this checkpoint.

Completed: [L038](../lemmas/L038-fixed-fiber-at-one-local-algebra-mismatch.md)
proves the complete factor-degree mismatch [1,11] versus [6,6]. Every
residue block is irreducible and occurs once; all lifting resultants are
units, so there is no unresolved ramified block or precision threshold.
The exact script and full certificate are under `scripts/full-fiber-at-one/`.
The Frobenius chains, Bezout identities and input coefficients were read in
full through selected JSON fields. No factor pairing exists. Outcome
NEGATIVE / REPRODUCTION: reject only j=1, preserve all other image/global
gaps, and record the fixed-scalar stop in ATTEMPTS/011. The next proposed
independently testable scalar is j=2; no factor data for it was computed.
