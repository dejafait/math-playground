# Affine Laguerre three-coefficient matching stop1592

One mathematical attempt under the pre-existing SPECIALIZE assessment1591.
The exact feasibility classification and full proof are canonical in
[C028j](../lemmas/C028j-affine-laguerre-three-coefficient-admissibility-stop.md).
This is a source-formula specialization, with a separate audit pending.

WHY IT FAILS: the first three coefficient matches force d+alpha_d to
equal the fixed constant S_2^3/S_3^2 and force the scale and translation
uniquely. The admitted positive Gamma weight requires d+alpha_d>d-1,
which eventually contradicts that fixed value. This covers reflected
scales and all degree-dependent boundary choices. The feasibility-first
stop needs no higher actual coefficients, numerical enclosure or retained
cost computation. It does not rule out unmatched Laguerre references,
other positive measures or signed methods, and supplies no actual
root-height lower bound or RH conclusion. Reopening this exact matched
family requires an error or a changed construction, not another scaling
or higher-coefficient sweep.
