# Positive unit residues do not prevent inverse-Blaschke cancellation

The approved small-cluster test produced the exact two-pole construction
in [C645d](../lemmas/C645d-two-pole-inverse-blaschke-cancellation.md).
Its proof passed a separate conceptual audit on 1 November 2026,
without a mathematical correction; the audit is recorded canonically
in C645d. The construction
uses L645's unchanged complex factors and grid, with both poles inside
the assessed strip and a fixed positive distance from the disk boundary.

WHY IT FAILS: Positive residues acquire complex phases after division by
the grid factor. C645d constructs an admissible second pole at distance
O_delta(1/n) where the factor is exactly the negative of its anchor value.
The two unit residues then cancel in the normalized sum for every n
beyond an explicit delta-dependent threshold. This is an exact zero,
not an insufficient polynomial gain or a numerical near-cancellation.
Thus no lower bound can follow solely from the assessed cluster geometry
and positive unit residues. Actual-Xi realization, symmetries, interpolation,
other poles and contour estimates remain independent; the construction
neither supplies an off-line Xi zero nor refutes RH or every detector.

Preserve the original C645a/C645b stops and C645c's qualified rate result.
After the successful independent scrutiny, reopening this shortcut requires
a materially different constraint or weight that excludes or detects
the exact cancellation; repeating the positivity-only premise is not
a new mechanism.
