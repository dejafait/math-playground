# 2026-10-11 — Fixed rational witness fails integer realization

One approved RESEARCH/REPRODUCTION calculation establishes
[L056](../lemmas/L056-fixed-witness-prime-five-nonintegrality.md): L055's
literal unshifted root is nonintegral, because 5 divides its integer
denominator and its integer numerator is 4 modulo 5. The proof matches
the shifted endpoint convention to the imported integer affine theorem,
includes every numerator summand and explicitly justifies cancellation.
This is local progress on an omitted arithmetic constraint, without a
claim of new general mathematics beyond the inspected affine machinery.

The complete certificate is
`scripts/postspell-word-count/fixed-witness-integer-certificate.json`:
1229 primes through 10000, 34422 checks and no failures. Independent
compressed triple and closed-offset evaluations agree, including exact
lifted division at 11; additional obstructions occur at 431 and 5233.
The separate written-table certificate checks all 25 printed rows directly
with period-four arithmetic and confirms their contribution sum is 44.
The bounded target is complete, and the literal integer allocation stops.
No general allocation exclusion, parity realization or Collatz result is
claimed. Preserve L055 and [Attempt 026](../ATTEMPTS/026-fixed-count-total-tail-exclusion.md):
the real subsystem remains feasible and restricted cycle exclusion remains
through 24. No new failed approach file is needed for this successful
diagnostic. Mathematical exploration usage remains zero after ADVANCE.

PROOF.md adds only the changed arithmetic conclusion and its trap checks;
DAG.md adds L056's direct mathematical inputs. The next action is an
independent audit of L056 after a separate literature approval of the
new REVIEW_REQUIRED continuation. That placeholder is not a second
completed source review and does not approve new mathematics this turn.
