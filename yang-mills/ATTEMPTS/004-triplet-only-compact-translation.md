# Triplet-only normalization by a compact local translation

Tested 2026-09-25. Try to normalize the site-centered SU(2) stress triplet by a local displacement whose strain contains only diagonal traceless components, with the displacement supported inside the fixed box.

## WHY IT FAILS

[L007](../lemmas/L007-local-translation-normalization-obstruction.md) proves that every smooth compactly supported displacement with zero off-diagonal strain is zero. An affine diagonal displacement has the desired strain but moves the boundary and retains surface terms. An explicit compact divergence-free localization removes the singlet, while leaving shear in its transition region. Thus geometry alone cannot discard the off-diagonal stress response. This stops only the proposed operator-level triplet-only projection: probe-specific cancellations or a jointly normalized triplet/shear system remain possible. Neither has been established here, and the exact finite-lattice Haar identity still contains an uncontrolled matching residual.
