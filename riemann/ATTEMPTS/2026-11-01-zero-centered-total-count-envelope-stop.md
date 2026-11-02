# Total-count envelope does not supply the sparse census

The approved bounded specialization is canonical in
[C645j](../lemmas/C645j-zero-centered-count-envelope-deficit.md).
It uses Bellotti--Wong v2 Theorem 1.1 directly, preserves closed-endpoint
multiplicities, narrows the enclosing slab using beta<1, and halves
the total slab count by reflection. It is a reproduction/specialization
of a known count theorem, not a new zero-density result.

WHY IT FAILS: Even after both geometric improvements, the complete
explicit upper envelope has leading coefficient
sqrt(R_delta^2-1)/(2*pi)+0.10076, whereas C645h needs
delta/[16(1+log(256R_delta/delta))]. C645j also verifies failure of
the numerical certificate at every permitted height, including integer
rounding. An upper envelope being too large does not say that the
actual census is large or false. Park this total-count mechanism as a
source of the original sparse threshold. Preserve C645i's separate
arbitrary-C synthetic stop. Any continuation needs a different estimate
or an independently tested, materially larger admissible census
coefficient; clearance, realization, boundary upper bounds and signs
remain open.
