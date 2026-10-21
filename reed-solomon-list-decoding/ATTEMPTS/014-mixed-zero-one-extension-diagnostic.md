# Mixed (0,1) diagnostic — parked after exact nonexclusion

The approved fixed-assignment test is completed in
[L024](../lemmas/L024-full-mixed-zero-one-extension-psd.md), with full
generator and independent-audit certificates under scripts/finite-support/.
It tests exactly the two full mixed (0,1) blocks without tuning the assignment.

WHY IT FAILS: Both blocks are positive semidefinite, so these necessary
constraints cannot exclude this particular prescribed extension. Its
objective remains above threshold. Passing them proves neither full
scalar/SDP feasibility nor a realizable packing or list. Together with
L023's full-zero result, this gives a reason to park further individual
block tests and assess full scalar inequalities as a different diagnostic.
That proposed test remains outside the approved scope and needs separate
review; no full scalar calculation has been performed here.
