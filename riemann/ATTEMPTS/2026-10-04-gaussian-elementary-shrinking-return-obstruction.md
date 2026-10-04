# Elementary shrinking-window return certificate — 2026-10-04

The target is the actual large-frequency first sign of L357's
Gaussian-regulated family, for fixed regulators approaching zero.
The full test and precise arithmetic threshold are proved in
[L364](../lemmas/L364-gaussian-joint-gamma-window-return-threshold.md).
The gamma harmonics have adequate error at the shrinking window mass;
the elementary prime-frequency implementation fails. This does not
prove absence of visits or positivity of the actual spectrum.

WHY IT FAILS: the cosine-power bump needs degree at least a constant
times (log H)² to distinguish the required prime-phase window. The
integer-product separation bound then makes its sufficient averaging
length exceed H already using the prime 2. Optimizing that degree does
not repair this particular upper-error certificate. L364 isolates a
strictly stronger, explicit logarithmic-form input that would suffice;
it remains unproved until a separate primary-source assessment. This
fixed-regulator test is distinct from L336's coupled endpoint quantifier,
and all earlier route stops and actual-zeta ranges are preserved.
