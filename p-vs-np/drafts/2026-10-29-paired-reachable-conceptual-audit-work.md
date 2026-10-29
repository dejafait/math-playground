# Step 551 — paired-reachable obstruction conceptual audit

Research / proof_audit / REPRODUCTION, using the unchanged ready EXPLORE
assessment `literature/2026-10-29-paired-reachable-support-conceptual-audit.md`.
The supplied overview and DAG were used before detailed proofs; existing
notebook changes and Attempts 058–060 are preserved.

The main gap remains uniform P versus NP. The intermediate target is
L127's original-coordinate K_N generator-support obstruction, whose
downstream use is deciding the assessed O(S) paired-reachable construction.
Retain its provisional stop only if residual membership, full reversed
A_f projection rank and one charge per distinct generator all survive.
Otherwise preserve finite evidence and retract only the unsupported
uniform conclusion. No general-chain obstruction is an audit premise.

## Reasoning saved before replay

Read all of L127, L122 §2 and its conventions, L125 §2, L126 §§1–3,7,
the step-550 source notes, and Attempts 058–060. Existing primary coverage
is adequate and reused; no extra literature search is needed.

The membership argument compares each coefficient at ell+m, with the
same right-closed beta and all coordinates retained. The A_f recurrence
uses incoming, not outgoing, matrix entries; its first N Krylov rows
project to the upper triangular matrix binom(i,ell) mod 2. Column reversal
is a permutation. The minor is selected from projected generators, not
from a purported full E_N basis. Its permutation term charges one row
per column, so arbitrary generator redundancy is harmless. The k=0
case has N=1 and a one-by-one projection. No proof gap found so far.

Read both complete paired-reachable scripts and their imported act,
insert, rank and endpoint helpers. The receiver independently reconstructs
the entire literal graph, constant powers, closed rows and residuals,
then enumerates the full Krylov span by sets. Its exact span/threshold
and minimum-basis checks are finite claims, not evidence of asymptotics.
Replay and full old/new certificate comparison remain to be performed.

## Completion

The conceptual audit passes; the full reasoning is canonical in L127 §7.
Both scripts were replayed and all nested certificate values compared,
with the input-path difference separately received. The 10/10 checks
and all required counts pass, with no failures; complete evidence is in
`scripts/batched-incidence/output-551/`. Outcome: NEGATIVE, validating
the previously provisional restricted stop, not a new stronger theorem.
History 551 records the decision and the new REVIEW_REQUIRED source
target. This draft preserves the pre-replay checkpoint; it is not an
additional lemma source.
