# Split harmonic metric — bounded proof attempt, step 318

Approved exact target: Test uniform two-sided bounds for the actual stable-open harmonic L2 metric in a local holomorphic frame of L111's free middle sheaf near each split point.
Prior SPECIALIZE coverage: `drafts/literature/2026-10-16-split-harmonic-metric-two-sided-bounds.md`.
Actual task: proof_attempt; classification REPRODUCTION. F is hypothetical;
Z is finite and possibly empty. Main gap: universal primitive rational Hodge
realization. Potential use: quantitative input for later normal-summand work;
no curvature, extension, semistability or cardinality conclusion is sought.

Read actual L111, relevant hypotheses of corrected L108/L110, prior audit
history 316 and ATTEMPTS/063/065/066/067. No duplicate estimate is present
in those results; algebraic freeness alone remains insufficient. Preserve
all prior work and stops.

Candidate mechanism, not yet a certified result: analytify L111's minimal
complex K=(O -> O^52 -> O). Its exact splitting is a rank-two Koszul plane
P and a rank-fifty degree-one summand J. Choose the spectral cutoff below
the first positive central Dolbeault eigenvalue for the given smooth metric.
The small spectral complex has ranks (1,52,1), with zero central
differentials. A compatible smooth comparison from K that is an
isomorphism on the central derived fibre would be degreewise invertible
on a smaller ball. Pulling its smooth positive L2 metric back to K^1
then gives uniform finite-dimensional constants. Off the centre,
ker d1=J+im d0, with im d0 contained in P. In a fixed frame respecting
P+J, minimizing the norm of j+t*d0(1) gives a lower bound by the
Euclidean coefficient norm of j and an upper bound by its own norm.
No division by the shrinking column is needed.

Load-bearing check still to finish: the natural BGS III comparison must
identify this actual holomorphic J frame with ordinary higher-image
sections and give the central derived-fibre quasi-isomorphism, rather
than merely identify ordinary cohomology modules. The spectral harmonic
quotient norm must equal the original fibrewise L2 norm. Continue only
if both are justified and one whole punctured ball admits fixed c,C>0.
A singular arbitrary metric or fixed-radius sphere estimate is not a test.
Even success leaves curvature, extension, semistability, |Z|, F existence,
transport and primitive Hodge realization unresolved.

Completed attempt: the comparison and both inequalities are written
in canonical L112. BGS III's actual comparison proof, pp. 343--345,
supports the natural map and its central derived-fibre identification.
Outcome ADVANCE / REPRODUCTION, pending separate critical audit.
This working note preserves the initial checkpoint; L112 is authoritative
for the complete proof and qualifications.
