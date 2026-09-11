# Suffix increment-bound selection — 2026-09-11

The proposed universal zero lower limit for T through suffix minima is
false; see [Lemma 87](../lemmas/L087-sparse-suffix-minima-obstruct-increment-bound-selection.md).

WHY IT FAILS: Suffix minima can consist only of sparse block endpoints.
Summable increment spikes can keep the sufficient bound at least one at
every endpoint. The bound ignores the actual large coordinate jump there;
the full upward contribution in the same example tends to zero. This
failure rules out the bound-selection assertion, not the unrestricted
upward liminf assertion or RH.
