# Spatial block elimination with a coefficient norm

The exact certificate, full proof, constants and qualifications are in
[L687](../lemmas/L687-spatial-block-polynomial-dual-cost-stop.md).
This preserves L686's different sparse-support advance and stops only
the specified coefficient-norm certificate when at least ceil(n/90)
family nodes are discarded. Arbitrary retained blocks, angular choices
and additional polynomial factors are included in that stop.

WHY IT FAILS: Each discarded node forces a zero of the spatial dual.
After normalizing its coefficient cost on the disk of radius R/r=44,
finite disk zero removal bounds every retained value by a factor at
most 48^(-K). The full angular weight envelope cannot recover that
cost once K>=n/90: the certified value divided by the required
original-D scale is <5*exp(-79*n/30000). This is an upper bound for a
lower certificate, not for V. A different observation norm or a
multiplier retaining all nodes is not ruled out; its signed response
and complete cost would require an independent test.
