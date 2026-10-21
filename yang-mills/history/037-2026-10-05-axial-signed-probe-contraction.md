# 2026-10-05 — Actual axial signed response: finite-mesh exploration

Reused the unchanged SPECIALIZE assessment and preserved prior changes.
One bounded calculation tested L027's interior axial one-internal-pair
class for the actual two probes. Its new canonical verification subsection
in [L027](../lemmas/L027-axial-ordered-action-wick-loop-growth.md) records
the exact estimator justification, full-mode covariance calculation,
64 samples per admitted mesh N=24,32, and all numerical qualifications.
No new mathematical bound or lemma was established.

Outcome EXPLORATION, REPRODUCTION: the sampled common path contribution
dominates both totals at these meshes, while the triplet curvature mean
changes sign. This directs attention to the actual exterior factors; it
does not certify signs, growth or boundedness. The full certificate is
`scripts/combined-ward-response/axial-signed-response-certificate.json`.
All 14 checks passed and complete checks/failures were inspected; complete
stored-data audits reproduce the summaries. No progress beyond the
checked sources, logarithmic coefficient or reflected-error bound is claimed.

The [working note](../drafts/2026-10-05-axial-signed-probe-contraction.md)
retains the missing quantitative residual and forest-lift estimates.
Continue analytically within the same approved combined-response target;
two meshes do not justify a cutoff fit or further sweep. ATTEMPTS/011–012
and L019's cancellation obligations remain. The argument and DAG are
unchanged; the overview is therefore preserved. Scoped documentation
validation and notebook whitespace checks passed (27 nodes, 70 edges).
