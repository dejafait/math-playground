# Free-pair coupled shells-5–8 support — insufficient for the threshold

WHY IT FAILS: [L097](../lemmas/L097-free-pair-shell-batch-common-witness.md)
provides one unchanged common rational witness for every constraint of
the approved free-pair batch. All 166 matrices, 71688 scalar rows and
68 pair rows pass independent exact reconstruction. The objective is
at least floor(65537^28/2^128)+1, so integer flooring cannot make a
sufficient upper certificate from this support. Stop this entire support
without a solve, retuning, enlargement or sequence of isolated block tests.
This is no statement about its optimum, full SDP feasibility, a packing,
RS realization or the 955–957 boundary. Original coefficient maps,
slacks and congruences are in the `free-pair-shell-batch-*.json`
certificates under `scripts/finite-support/`. Separate critical proof
review in step 357 retains the finite certificate: full source reconstruction,
actual-set reanchoring and all 1498 principal minors pass, including the
singular zero row and strict integer endpoint. See L097 for the canonical
proof and complete audit evidence; prior stops remain intact.
