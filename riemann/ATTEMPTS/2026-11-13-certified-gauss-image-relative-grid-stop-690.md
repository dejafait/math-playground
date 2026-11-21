# Image-relative conversion stop690

The gate-approved finite Gauss setup target was attempted with one
rational mesh,16 initial bisections, at most12 Newton updates and an
unchanged640-bit node grid. C998l is the canonical proof and citation
record. The complete stopped trace and unscaled rational replay are
`scripts/separation-seven/certified-gauss-newton-690.json` and
`scripts/separation-seven/certified-gauss-newton-replay-690.json`.

WHY IT FAILS: The conversion loop requires its dyadic search cell to
be as narrow as the actual Newton image, irrespective of the requested
output accuracy. At the second positive degree63 root's sixth update,
the image width is<=2^-1033. At depth640 a still-required exact halving
has a half-integral grid index and is forbidden. Two reflected output
nodes already meet both radii, but all-node completion fails. This is
a prescription-specific precision stop, not a general Newton or work
lower bound. A183800 partial ledger is not a full setup upper bound.
Do not retune this stopped run. A future, separately executed
prescription can test output-tolerance-capped conversion, checking all
nodes, weights and costs rather than importing success from this trace.
