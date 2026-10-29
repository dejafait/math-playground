# Quartic class-generator attempt — work checkpoint

The approved target is exactly: Determine a certified Minkowski-bound
prime-ideal generating set for the class group of L133's quartic field.
Coverage is the preexisting SPECIALIZE assessment
`drafts/literature/2026-10-25-pair-quartic-class-generators.md`.
Inputs are L133 and audited L134, including the final integral basis and
complete multiplication table in `scripts/pair-genus-two/quartic-order-certificate.json`.
There is no cross-notebook input. Earlier ATTEMPTS/019,045,058 concern
different obstructions and are preserved; no backend probe is planned.

Main gap: primitive exclusion for all residual Beal signatures. This one
intermediate target could support class relations and descent, while units,
quotient ranks, point control, retained equations and recovery remain open.
The test is complete producer/replay evidence within the assessment's fixed
caps, including all exceptional subspaces. Stop on any incomplete domain,
failed equality, signature failure or cap, saving the failed evidence.

Implementation plan: exact sign intervals; rational Minkowski upper cutoff;
complete rational prime sieve by trial division; complete modular factor
trial divisions at regular primes; RREF enumeration of every subspace at
2,3,5, ideal-invariance and inclusion-maximality witnesses; full preimage
lattices, norms and multiplication closure. Replay will import accounting
only, reconstruct field multiplication from the displayed integral basis,
and independently verify complete domains, divisibility, lattice indices,
closure and maximality. No class number or relations follow from this list.

State before lengthy execution: no generator result yet; new scripts and
their persistent ledger will retain all phases and failures without resets.

## Completed bounded result

Canonical statement, full proof, sources and qualifications are now in
`lemmas/L135-pair-quartic-class-group-generators.md`. The four real-root
intervals and strict rational Minkowski bound give U=159. All 37 rational
primes are covered; the final list contains 26 regular linear-factor ideals
and six exceptional ideals. All 1399 exceptional subspaces are enumerated
once per execution. The independent replay passes 1409026 checks.
Both executions together use 342350 polynomial divisions, 2798 exceptional
subspaces, 11711 subspace tests and 34536079 instrumented scalar operations;
all fixed caps pass. Full exact evidence, rejected candidates, replay and
ledger are in `scripts/pair-genus-two/quartic-class-{certificate,verification,ledger}.json`.
No failed execution, arithmetic correction or cap stop occurred. One source
comment was corrected to describe the regular-prime dimension argument
actually used, removing a reference to a minor calculation never performed;
no executable line changed after the successful replay. An uninspected
ideal-factorization theorem number was removed from the draft proof before
completion; the standard named unique-factorization theorem is used instead.

This is a specialization/reproduction of known mathematics, not a new class
generation theorem. The result can support class relations and descent but
does not provide them. A separate critical proof audit of L135 is the sole
proposed continuation, with its new exact-target assessment REVIEW_REQUIRED.
All original limitations, prior stops and unfinished work are preserved.
