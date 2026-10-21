# Pairwise branch data do not supply minimal normalization defect

Tested route: infer length r-1 for the normalization quotient solely from
smooth flat quaternionic totally geodesic branches, finite unramified
normalization and reduced isolated off-diagonal coincidences.

WHY IT FAILS: [L122](../lemmas/L122-three-quaternionic-lines-normalization-defect.md)
computes the reduced union of the two coordinate quaternionic lines and
the diagonal in H^2. It retains the tested local properties but has
normalization defect four, against two required. The pair sums are
maximal; the simultaneous sums restrict to squared branch maximal ideals.
The canonical proof checks every degree and the whole off-diagonal scheme.
This is a REPRODUCTION/specialization of the assessed gluing tools; the
separate 2026-10-18 critical audit in L122 preserves it. It stops the inference from these selected
local data, not a formula using the additional actual K3 metric and global
F hypotheses. Actual-image gluing remains unresolved; no kernel or Hodge
class is excluded or constructed.
