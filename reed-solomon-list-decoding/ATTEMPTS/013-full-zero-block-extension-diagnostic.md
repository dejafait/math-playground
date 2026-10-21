# Full zero-index blocks — fixed-extension exclusion parked

WHY IT FAILS: [L023](../lemmas/L023-full-zero-block-extension-psd.md)
certifies both full (0,0) matrices as PSD for L022's prescribed
extension. Independent reconstruction checks every source coefficient,
matrix entry, old overlapping value and congruence identity, including
all zero rows. Consequently these two blocks cannot exclude this
extension with its unchanged above-threshold objective. This is not
full-SDP feasibility: new scalar rows and other blocks remain unchecked,
and no packing or unsafe RS list follows. Another diagnostic must test
a different constraint, with separate scope approval; the selected-batch
stop remains intact. Complete generation and audit evidence is in
`scripts/finite-support/full-zero-block-*.json`.
