# Nonunitary cusp: fixed complex-power rectangles lose useful precision

2026-10-11, BSD-167. The fixed model arithmetic and complete finite
failed enclosure are preserved in
[L050](../lemmas/L050-nonunitary-cusp-arithmetic-and-failed-enclosure.md),
with the original certificate in `scripts/nonunitary-cusp/certificate.json`.

## WHY IT FAILS

The 96-bit schedule replays correctly but does not attain its width:
actual normalized width exceeds 2^2000, while the required width is
strictly below 2^-20. All complete Fourier tails meet 2^-38 and the
independent target-period interval is narrow and positive. The large
width is already in the finite complex-power rectangle sums: repeated
rectangular multiplication loses real/imaginary error correlations at
low-height transport points. The worst retained point requires 4860
terms and has positive q coordinates with rectangular l1 bound greater
than one. This stops this fixed representation/schedule, not L049 or
nonunitary-cusp enclosure production. Preserve the evidence and replace
powering complex rectangles with fresh reduced phases and a positive
real attenuation interval; test that representation against the same
full-replay and width threshold. Do not merely enlarge truncations or
round a numerical value to a rational. The unchanged target has existing
SPECIALIZE coverage; no new source assessment or BSD assertion follows.
