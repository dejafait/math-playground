# Finite divisor inversion does not make the shifted prefix I+o(1)

The exact shifted congruence, its finite-cutoff correction, and the
explicit coefficient-vector calculation are proved in
[L624](../lemmas/L624-exact-divisor-congruence-and-persistent-shift.md).
Its application retains L622/L623's unaudited status and named imports.

WHY IT FAILS: The attempted o(1) estimate for the shifted prefix map
after V_N is false. A unit harmonic coefficient vector is sent by V_N
to Mobius coefficients, and one permitted microscopic shift multiplies
its prefix by n^(-tau/log T). Its norm deformation has a strictly
positive limit at the fixed length exponent 1/100. Thus growing T
does not remove this coefficient-correlated deformation, even after
the exact finite inverse. The first scaled derivative also persists.
This is a different obstruction from freezing an individual local
factor before congruence. It does not lower-bound the error in K_c,
refute its proposed B(c)/2 margin, or prove a negative direction:
the six-term signed extraction, normalization, and infinite boundary
can still compensate. Discarding that boundary on the basis of the
zero-shift Gram inequality is unjustified after signed extraction.

The full congruence test ended without a signed comparison. A further
attempt must use the retained normalized-log deformation and boundary,
or a different mechanism. Repeating an o(1) prefix claim, increasing
a floating matrix, or transferring the prefix sign to the full sum
would not address the recorded obstruction. No detector-family-wide
positivity or RH claim was obtained.
