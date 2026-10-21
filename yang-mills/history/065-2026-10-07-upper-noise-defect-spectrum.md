# 2026-10-07 — Exact boundary defect and realizable nonsmall quartic

STEP_ID: YM-20261007-065-upper-noise-defect-spectrum

Within the unchanged SPECIALIZE response target,
[L050](../lemmas/L050-upper-face-noise-defect-spectrum.md) resolves L049's
whole-edge noise defect into its gradient and zero-divergence spectral
parts, with a fractional-energy bound and exact low-mode cutoff rate.
A four-vertex actual potential product rules out uniform relative
smallness of Z. Seven rational, three integer and five numerical checks
pass in `scripts/combined-ward-response/upper-noise-spectrum-certificate.json`;
the numerical checks are diagnostics, not rigorous enclosures.
This is local reproduction of standard finite spectral methods, not a
new source-level renormalization result or an actual response evaluation.

[ATTEMPTS/017](../ATTEMPTS/017-uniform-conditional-quartic-smallness.md)
preserves the stopped shortcut. Continue by signed contraction of the
explicit fractional kernel with the actual probe/residual, retaining R,
E, cross plaquettes and the remaining L011 jets. No scaled compensation,
complete cutoff logarithm, matching, reflected error <=c_box/2 or
continuum/infrared construction follows. The prior assessment is reused
unchanged and no supervisor state or earlier work is altered.
