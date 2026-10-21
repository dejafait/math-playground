# L026 critical audit — completed

Approved target: audit L026's shared OBDD reduced-data construction, checking formal identities, ordered-output identification, and complete size and degree bounds for L025. The unchanged gate is `drafts/literature/2026-10-05-obdd-reduced-data-audit.md` (EXPLORE). Reused the construction and coefficient-degree source assessments; checked Attempts 017–018. No new source theorem or cross-notebook input is used.

The main gap is unrestricted uniform SAT complexity. The intermediate threshold is the two formal local H identities and polynomial S,d,h,E required by L025. Their downstream use is the restricted circuit-certificate construction when the supplied common-order width is polynomial. Arbitrary-extension small width, representation conversion, all-certificate hardness and decision transfer remain independent unresolved obligations. Continue if the complete bounds and identities withstand inspection or a concrete defect is repaired; otherwise record the failed claim and restrict the construction.

Saved audit state before diagnostic execution: L026's complete proof and L025's receiving hypotheses/bounds have been read. L020's original axiom convention and ordered commutator recurrence match (6). Expansion (10) retains the order e_a K_a v_b; (11) leaves beta on the left. The common-order multilinear restriction is essential to identifying P with r_i. No defect found so far. Remaining work is to finish the n=0/n=1, signed/base-root and full encoding checks, inspect the diagnostic's exact generic certificate, and rerun its finite checks. This file is an audit record; full proofs remain canonical in L026.

## Verdict and checked obligations

The saved checklist is now completed. No load-bearing error was found. Retain [L026](../lemmas/L026-obdd-reduced-original-axiom-data.md) with its existing hypotheses and bounds; this audit neither strengthens the theorem nor establishes a new mathematical result. No proof repair, dependency change or PROOF.md change is warranted.

| Obligation | Audit finding in the canonical proof |
| --- | --- |
| Original axioms | L020 supplies pair-once commutators; reversing original identifier order is harmless over F₂. The common OBDD order need not be identifier order. Outside-F variables are constants, not new inputs. |
| Suffix commutation, (5)–(6) | The ordered product rule has e on the left and the child representative on the right of the pair placeholder. Terminal values are central field scalars. Recursive calls decrease remaining suffix length. |
| Product identity, (8)–(12) | Checked all four choices in (11), including both off-diagonal products. The commutator term is e_a K_a v_b; beta stays left of both suffix sums. Child W substitutions cancel the child products without any factor permutation. |
| Zero identity and placeholder sectors | K and W have one placeholder per surviving monomial; no recurrence multiplies two placeholder-dependent factors. Cancellation cannot introduce a placeholder-free word. |
| Output identification | P and the supplied output lie in the same increasing multilinear subspace. The decomposition A+y_k B is unique there. The promise concerns all original Boolean assignments, not merely assignments satisfying the unsatisfiable F. |
| Signs and bases | Complemented-terminal diagrams equal 1+r formally; supplied signed roots are the actual circuits 1+r. Auxiliary variable/constant diagrams are formally identified with prescribed base roots. No generic Boolean-equivalence witness is assumed. |
| Degenerate cases | At n=0 products and promised equalities are scalar and H=0. At one remaining level, K and W children are zero constants; unsimplified e times zero may have syntactic degree one, which the bound permits. Repeated/complementary operands and coincident successors need no distinctness hypothesis. |
| Pre-substitution degrees | For s remaining levels, values and K have syntactic degree at most s. Both first W corrections have at most 2s−1; inherited terms have at most 2s−2 for s≥2 and one for s=1. Thus the unsimplified circuits satisfy d=max(1,n), h=max(1,2n−1). |
| Shared-state cost | O(B) diagrams give O(B(n+1)v) states and O(B(n+1)²v) suffix entries. Each of at most T definitions has its own O((n+1)v²) pair table, with no state product across extension histories. This is O(M) gates as stated. |
| Complete encoding | O(B) supplied roots are each charged for up to the entire M-gate DAG. O(T) restored-label/association bits and log(M+2) reference bits per record, plus O(T³) axiom bits, give the stated E. Input records and order also fit. No small-w hypothesis for arbitrary ER is inferred. |
| L025 interface | Abstract nodes count values/signs, not internal arithmetic gates. Fresh ER definition order gives acyclic operands. Representatives are x-only, H use only original placeholders, both formal identities hold, and separate encodings are charged. |

These findings inspect the complete inductions and counts in L026, not just finite diagnostics. L020 is used in its stated ordered commutator scope; L025 is the receiving conditional result. No reproof of Bryant's Boolean algorithms or commutative-to-free-ring import is used. Mathlib coverage remains not checked.

## Reproduced finite diagnostic

Read the complete `scripts/obdd-reduced-data/check_suffix_witness.py`, including its free-word engine, recursive construction, checks and case generator. Inspected the complete `/generic_local_identity` in `scripts/obdd-reduced-data/suffix-witness-results.json` with the shared inspector's `--full` flag: witness, substitutions, full actual/required word lists and zero specialization. An initial lookup at nonexistent `/generic_identity` failed and was corrected; it supplies no mathematical evidence.

Reran `PYTHONDONTWRITEBYTECODE=1 python3 scripts/obdd-reduced-data/check_suffix_witness.py`: exit 0, no failures, 308 cases, 3,960 suffix checks. Maximum tested value syntactic degree is 3 and H degree is 5; each case checks its own max(1,n) and max(1,2n−1) thresholds. Omitted-commutator, omitted-Boolean and reversed-coefficient mutations were detected in 164, 172 and 112 cases. The full certificate remains at that path. No new mathematical script was written. These diagnostics do not verify unrestricted width, formal proof strings or all-size asymptotics.

## Decision

Completed RESEARCH / proof_audit / REPRODUCTION, outcome EXPLORATION: a new critical inspection and diagnostic reproduction with a positive verdict, not a new lemma, repaired error or advance beyond the checked sources. Mathematical exploration usage is now 1 since L026's advance. No P-versus-NP candidate follows.

Do not repeat this unchanged audit. A distinct proposed discriminator is whether a used extension in a polynomial-length ER refutation can force exponential OBDD width for every variable order. The new assessment `drafts/literature/2026-10-05-used-extension-obdd-width.md` is REVIEW_REQUIRED; that target is neither source-assessed nor proved here. It tests unrestricted applicability, not optimal refutation size or hardness of all certificates. Attempts 016–018 and unfinished work are preserved.
