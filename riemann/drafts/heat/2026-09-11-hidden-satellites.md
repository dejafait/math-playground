# Hidden-satellite checkpoint — 2026-09-11

Candidate, unproved pending checks: centers X_n=2^n, b_n=1−2^{-n}; satellite distance d_n=16^{-n}, height increment δ_n=d_n². In (x²,b) coordinates the consecutive-center chord slope is t_n=1/(6·8^n). Satellite slope δ_n/(2X_nd_n+d_n²) is less than d_n/(2X_n)=1/(2·32^n)<t_n because 3<4^n. Thus each satellite lies strictly below that chord and cannot maximize any linear penalized score. Every center has upward contribution at least 2/(1+d_n²)>1 from its satellite. All positive zeros interleave strictly in both coordinates and heights, and reciprocal squares sum geometrically.

Resume by checking strict chord exclusion for every penalty, existence of maximizers, interleaving, and the all-penalty lower bound. If valid this refutes favorable-penalty-subsequence existence even in Lemma 74's monotone class; it does not concern theta heat slices or RH.

Completed: the candidate is proved in Lemma 75, including the strict all-penalty exclusion, product properties, and convergent full upward sum. Exact supplementary checks passed. No draft assertion is needed as a DAG input; the active next action is in PROGRESS.md.
