# Fourfold input family stops for one sector quadratic

The exact restricted exclusion is canonical in
[C020p](../lemmas/C020p-sector-sextic-fourfold-input-exclusion.md), with
certificate1471. It covers all real translations/scales, all positive
input quadratics and 1/4<=t<=5/18 for one normalized quadratic factor.
The output has at least four real roots, whereas the saved (2,4)
witness requires exactly two. Independent audit is pending.

WHY IT FAILS: With a fourfold real input root the output retains a
double real root. The remaining quartic has a positively weighted
two-point evaluation that is nonpositive throughout the allowed
parameter interval. It therefore has at least two real roots, including
the equality case at the sector boundary. This is an exact exclusion
of this entire family, not a failed sample. It does not apply after
composing factors or to other real-root multiplicity patterns. The
full sextic count test and actual-Xi transfer remain unresolved.

The corrected60,000-trial collision screen produced no candidate;
its full record and rejected roundoff hit remain under
`scripts/quartic-differential/sector-sextic-collision-discovery-1471.json`.
That screen is not an impossibility proof. Continue with an exact
two-double-root collision elimination within the unchanged target,
retaining singular cases. Keep C020o's distinct inverse-method stop.
