# A single-field endpoint witness as an eventual-field disproof

Reviewed 2026-09-25. The proposed challenge-level endpoint objection used the
[smooth witness](../lemmas/C001a-smooth-endpoint-witness.md), which has a
nonempty proper safe set in the frozen model. The witness and its full proof
are retained; no error in its model-only claim was found.

WHY IT FAILS: A safe radius at one field size does not certify the
[official statement's](https://proximityprize.org/) unspecified sufficiently
large field hypothesis. The
[constant-code bound](../lemmas/L002-constant-code-field-size-saturation.md)
shows that for this fixed length every radius becomes safe above an explicit
field-size threshold. Thus this witness cannot refute an eventual assertion
as field size grows. If the source assumes an attained maximum exists, a
non-attainment witness is excluded directly. The alternative reading that
requires only a nonempty safe set still has the endpoint issue, but neither
that reading nor the current paper-to-model bridge is certified. No reviewed
disproof of the intended challenge follows. This stops the unqualified
single-field inference, not research on the sharp threshold or field-size scope.
