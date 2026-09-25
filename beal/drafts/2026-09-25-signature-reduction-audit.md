# Exponent reduction and theorem-scope audit — 2026-09-25

This records one focused informal step. It is not a candidate proof of Beal.

## Starting state and relevance

The shared instructions, local goal, checkpoint, entire overview, and DAG were read before selecting work. The existing local changes contain L001 and its completed unrestricted-congruence obstruction; preserve that branch. No recorded result reduces the global signature space. The previous checkpoint selected this audit, so it is neither a duplicate local-solubility test nor a repeated stop review.

The gap is uniform exclusion of positive primitive integer solutions for all exponent triples above two. The proposed intermediate target is a proof that it suffices to consider exponents in S = {4} union {odd primes}, together with precisely qualified exclusions obtainable from Fermat's Last Theorem and Darmon–Merel. Its downstream use is to select a genuinely remaining family for a global descent or modular argument. Emptiness of every remaining family is still unproved.

The discriminating test is whether each original exponent admits a divisor in S, the resulting power substitution preserves positivity and primitivity, and every claimed application of Darmon–Merel respects signs, exponent ranges, and the definition of nontriviality. Continue with a restricted global family if these checks succeed; abandon any claim that the cited theorems cover all reduced signatures if an explicit family misses their hypotheses. The required endpoint is zero positive primitive solutions, not finiteness or a reduction to infinitely many signatures.

## Reasoning saved before completion

For n > 2 choose an odd prime divisor if one exists; otherwise n is a power of two at least four, so 4 divides n. Replacing A by A^(x/r) for a chosen divisor r preserves exactly the primes dividing A, including when A = 1. Perform this independently in all three coordinates, without dividing bases or assuming a common exponent.

The located Darmon–Merel Main Theorem has square exponent n >= 4 and cube exponent n >= 3. Its cube clause has a historical full-modularity hypothesis; a separate precise modularity citation is needed. For a repeated odd prime p, C^p - A^p = B^s can be rewritten as C^p + (-A)^p = B^s. This sign change fails for repeated exponent 4. In addition, n = 3 is outside the square clause, so reducing a fourth power to a square does not settle (3,3,4).

The currently visible boundaries are (3,3,4), the ordered signature (4,3,4), repeated odd exponents with a distinct third prime at least five, and signatures with all three exponents distinct. These are boundaries of these direct theorem applications, not claims that the literature leaves every example open. The exact surviving conditions and completed proofs remain to be written.

## Completed source checks

Mauldin's primary problem page was reread on 2026-09-25 and matches the recorded positive-integer target. The nominated AMS page again failed retrieval. Darmon–Merel's author-hosted PDF was reread at its definitions and Main Theorem. Breuil–Conrad–Diamond–Taylor, Theorem A, was then read in Breuil's hosted paper and supplies exactly the missing full-modularity hypothesis. Precise primary citations are retained in foundations/02-standard-results.md. Mathlib lookup is not needed for this informal reduction and remains not checked.

## Completed assessment

[L002](../lemmas/L002-prime-four-signature-reduction.md) proves the reduction for every allowed divisor choice and both directions of the global existence equivalence. [C002a](../lemmas/C002a-darmon-merel-signature-exclusions.md) gives the qualified exclusions and defines the residual set. The achieved result is exact reduction plus unconditional exclusions of several infinite families, using named theorems. It falls short of the required zero-solution conclusion on the infinite residual set; it is not a candidate proof of Beal or an assertion of new literature results.

The informal checks covered n = 3, n = 4, powers of two, exponents admitting several divisor choices, and bases equal to one. Every signed auxiliary equation was written explicitly. The proposed extension of the square clause to repeated exponent three fails the exact control example 1^3+2^3=3^2. Moving an even fourth power with a sign also fails algebraically. These two failures explain why the residual set cannot be discarded by unqualified theorem matching.

The outcome is ADVANCE because the notebook now has a relevant exact reduction and proved global-family exclusions; no exploration turns remain outstanding. Direct use of these clauses is exhausted at the displayed scope. A distinct global factorization mechanism is justified for a surviving repeated-cube family; the local-solubility obstruction still rules out relying on unrestricted residues alone. No numerical search for Beal solutions was needed for this step.
