# Printed shifted-Wronskian criterion: Gaussian stop

The approved n=2,3 normalization test is proved in
[L875](../lemmas/L875-dimitrov-gaussian-wronskian-sign-audit.md).
The n=2 case passes; n=3 is the first exact mismatch. All of the
source's moment, Hankel and growth hypotheses are checked there, as are
its determinant orientation and positive-leading convention.

**WHY IT FAILS.** The Gaussian has an entire zero-free Fourier transform,
but its literal W(p_2,p_3;ix) is strictly positive. Therefore the negative
sign required by Dimitrov1311.0596v1 Theorem2 cannot be used as a necessary
condition in the stated normalization. This stop concerns that printed
criterion, not every result in the paper, another version, Newman's
stronger measure class, or RH. The audit stops without repairing the
indices or sign, sweeping higher degrees, or applying anything to theta.
L563's earlier different-paper phase failure is preserved independently.
