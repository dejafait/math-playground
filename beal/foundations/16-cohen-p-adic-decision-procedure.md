# Cohen's effective p-adic decision procedure — source scope

## Hypotheses

Fix a rational prime p. Work over Q_p with its normalized discrete valuation, and with a finite formula using rational constants, polynomial equations, Boolean operations and quantifiers. Valuation expressions must have nonzero arguments, or separately handle zero. Integer variables, if used, have the additive operations allowed by the source, not unrestricted integer multiplication. Residue-ring sorts have a fixed finite level for each occurrence.

## Conclusion

Cohen supplies an effective elimination procedure for the test functions defined in Section 2. For Q_p the resulting residue-ring questions are decidable because those rings are finite. Thus this scope includes deciding closed polynomial/valuation formulas. This is an imported general algorithm, not an implemented decision of the notebook's local image, a numerical precision cutoff, or a complexity guarantee.

## Proof

Citation only: Paul J. Cohen, *Decision Procedures for Real and p-Adic Fields*, **Communications on Pure and Applied Mathematics 22** (1969), no. 2, 131–151, [DOI](https://doi.org/10.1002/cpa.3160220202), [primary article scan hosted by the University of Chicago](https://math.uchicago.edu/~shmuel/lg-readings/Cohen-1969-Communications_on_Pure_and_Applied_Mathematics.pdf).

Inspected: Section 2's field assumptions and Theorem 2.1, p.136; simple/test/effective-function Definitions 1–4, pp.137–138; graph theorem A_n, p.140, and the root-case discussion through p.144; Theorem 3.1 and its field-, residue-ring- and integer-variable elimination cases, pp.144–145; Section 4's relative-decision qualifications, p.146. Theorem 3.1 is the essential import. Its common-cell intersection condition retains a common field witness across the predicates being eliminated. No reproof of that procedure is proposed.

Application to a finite product algebra, its projective curve points, a complete modular fiber isomorphism and descent classes requires an explicit faithful encoding over Q_5. That specialization is unfinished and belongs to the separately approved research attempt. The source does not supply this encoding or assert that power conditions restrict the image.

## Mathlib

Full effective p-adic decision procedure and its proposed algebra/image specialization: **not checked**. Supporting valuation and Hensel declarations: **not checked**. Unknown coverage is not evidence of absence.
