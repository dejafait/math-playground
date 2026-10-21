# 2026-10-05 — Full zero-index fixed-assignment diagnostic

Completed the ready SPECIALIZE target. [L023](../lemmas/L023-full-zero-block-extension-psd.md)
records both full matrices as exactly PSD, with all old overlaps
preserved. Independent factorial/source reconstruction and exhaustive
congruence verification report no failures. The full (0,0) blocks are
parked as an exclusion of this extension; the old selected-batch stop,
above-threshold objective and 955–957 bracket remain unchanged.

This is a REPRODUCTION of the known SDP method and an informative local
NEGATIVE diagnostic, not progress beyond assessed sources or an actual
list construction. No new source review or optimization was performed.
Both raw matrices were saved before elimination. The initial audit
verified all identities with rational multiplication; its saved final
version also passed after integer denominator clearing to make repeated
verification cheaper. The shared JSON inspector needs
PYTHONINTMAXSTRDIGITS=0 for the large certificate integers.

A full mixed (0,1) diagnostic is proposed in
[the pending assessment](../drafts/literature/2026-10-05-mixed-zero-one-witness-test.md).
It tests a different tensor block, but is REVIEW_REQUIRED and receives
separate scope/duplicate comparison before any calculation. No mixed
block was evaluated. Another PSD result there would require reassessing
repeated fixed-assignment block diagnostics.
