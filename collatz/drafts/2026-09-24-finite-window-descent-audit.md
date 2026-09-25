# Finite-window descent audit, 2026-09-24

The initial proposal and calculation were saved before writing the proof. The assessment is now complete.

## Gap and candidate selection

The unresolved gap is universal eventual descent for every positive starting integer greater than 1. There are no previous local lemmas, attempts, or unfinished edits; the initial DAG is empty. Changes in other notebooks were inspected by status only and are outside this step.

Three possible mechanisms were compared without undertaking three investigations:

1. A finite residue correction to logarithmic size with a uniform bounded return time. This offers a finite certificate to test, and a necessary condition can be checked exactly before trying any optimization.
2. Variable-length excursions, allowing the return time and arithmetic state to depend on the start. This avoids a fixed time window, but no bound forcing the eventual excursion product below 1 is available here.
3. An exceptional-orbit exclusion strengthening almost-everywhere results. Density statements alone leave individual exceptional integers, so this needs an additional arithmetic mechanism that has not been supplied.

Select only the first mechanism for this step. No local duplicate or recorded failure exists. Arbitrarily long odd prefixes are elementary; no novelty over the literature is claimed. The point of the test is to decide whether this specific proposed certificate deserves further work.

## Intermediate target and discriminating test

Seek positive integers q,K,N and a function h on the residues modulo q such that, with V(n)=log(n)+h(n mod q), every n>N has some 1<=j<=K satisfying V(T^j(n))<V(n). The base integers up to N would separately have to reach 1. Strict decrease suffices because V has finite sublevel sets; an infinite chain of strictly decreasing endpoint values would be impossible within the finite initial sublevel set.

This is a sufficient strategy, stronger than the exact target. The required sign is negative for at least one j in a common finite window at every sufficiently large start; an average negative sign is insufficient.

Test whether n=2^(K+1) q t-1 supplies arbitrarily large starts whose first K shortcut iterates grow while retaining residue -1 modulo q. If it does, h cancels and the certificate is impossible for every q,K,h; abandon this bounded-window scheme. If the proposed witnesses fail, first derive the exact residue transitions before attempting any certificate search.

## Saved calculation to review

Candidate identity for 0<=j<=K: T^j(n)=3^j 2^(K+1-j) q t-1. This would keep all these terms odd and in residue -1 modulo q, while multiplying n+1 by 3/2 at every step. A proof must check every parity assumption and the quantifiers in q,K,t; finite examples alone will not establish it.

## Completed assessment

The identity and all its parity and residue conditions hold, as proved in [L001](../lemmas/L001-finite-residue-bounded-window-obstruction.md). The potential change is greater than j log(3/2), uniformly positive for every 1<=j<=K, whereas the certificate requires a negative change for at least one such j. Increasing a fixed modulus or fixed window cannot repair this obstruction. The proof allows arbitrary corrections h and arbitrarily large starts, so finite exceptions cannot repair it either.

The exact integer check in scripts/finite-window/check_obstruction.py passed for 3,072 starting values and 38,400 shortcut transitions; [result.json](../scripts/finite-window/result.json) retains the output. This only checks the algebra's implementation and indexing; it does not supply the universal proof.

This one-turn investigation ends with an informative NEGATIVE and no unresolved calculation in this draft. Stop the fixed-window finite-residue certificate route. Variable-length blocks remain a materially different possibility because they can traverse the entire long growing prefix before comparing endpoints; whether the subsequent divisions compensate for that growth is still unresolved. No complete Collatz proof or disproof is proposed.
