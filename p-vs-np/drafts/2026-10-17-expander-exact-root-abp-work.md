# Exact expander-root ABP attempt — step 288

Approved target: determine polynomial-full-bit affine ABPs for every unchanged
L032 representative and zero H_i on L031's family, meeting L037 without a
deletion promise. The existing SPECIALIZE assessment is
`drafts/literature/2026-10-17-expander-exact-root-affine-abp-data.md`.

Main gap: unrestricted SAT decision/separation remains open. The local gap is
general ER-to-ABP data; this attempt tests only the supplied expander family.
Downstream use: apply L037 to these data even where L074 stops L073.
Continue only with all-root occurrence, graph, dictionary and bit-time bounds
in actual T; abandon this conversion if a required copied root exceeds every
fixed polynomial. Attempts 020/021/028 remain intact.

Inputs read: L031 definitions/encoding, complete L032 and its audit, L037's
receiving hypotheses/conclusion and assembly checks; reused inspected
Raz–Shpilka Lemma 2 Step 1 cases from the saved assessments. No new source
machinery or optional prescribed pair-table conversion is needed.

Unfinished calculation saved before assembly: counting every scalar, variable
and binary operation as one formula occurrence gives |p_i|=3,
|R_i|=6i−1 and |h|=12m−1. The positive circuit-root total appears to be
3m²+17m−6. Both sigma choices have exactly m negative eta_k, so signed U_k
add 2m occurrences. Each accumulator uses one earlier accumulator occurrence
and one separately expanded U_k. Check all sums, both signs, m=1, independent
output copies and full original-axiom framing before accepting the result.

No conclusion or audit verdict is claimed by this working checkpoint.

Completed attempt: the full all-root proof and receiving ledger are now in
canonical L075, `lemmas/L075-expander-exact-root-affine-abp-data.md`.
Its data bound is O((T+2)³ log(T+2)), with one conservative K(T+2)^8
bound for both aggregate bits and deterministic bit time. L037 applies.
This is a local REPRODUCTION advance; independent critical audit remains
pending. The saved unfinished calculation above is retained as provenance.
