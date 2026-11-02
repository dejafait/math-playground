# Small-cluster residue cancellation — bounded continuation coverage

TARGET: Test a three-pole unit-residue cluster for cancellation of the inverse-Blaschke residue sum on L645's unchanged logarithmic grid.
CHECKED: 2026-11-01
DECISION: EXPLORE
SEARCH_EVIDENCE: Reuse the completed derivative-free-pick-contour-detector assessment's meromorphic interpolation, polefinding and residue searches, plus its scoped duplicate/stop checks. No inspected source gives the small-cluster lower bound or cancellation family proposed below; no novelty is inferred.
SOURCE_EVIDENCE: Reconfirmed Beck et al., A First Course in Complex Analysis, Section 8.1, Theorems 8.1.5/8.1.7 and proofs https://complexanalysis.org/web/sec_residue-thm.html ; reconfirmed Zakeri Section 8.3 finite-Blaschke division paragraph following Example 8.33 https://zakerimath.com/CAbook/COM.html . Reuse L645 finite-Pick coverage: Bolotnikov (2010), definitions (1.1)–(1.7), Theorem 1.1 pp.151–153 https://files.ele-math.com/articles/oam-04-08.pdf . Reuse parent overlap review: Bello Hernández–de la Calle Ysern 1211.5573v1 Theorem 2.2/Lemma 2.3 pp.5–8 https://arxiv.org/pdf/1211.5573v1 ; Austin–Kravanja–Trefethen (2014) Sections 4.1/4.3 https://people.maths.ox.ac.uk/trefethen/austin_kravanja_trefethen_revised.pdf .
COMPARISON: Known contour calculus keeps all poles, while the assessed meromorphic approximation sources control different approximants or samples. The local detector instead evaluates an analytic residual through the derivative. The proposed cluster tests whether positive unit residues suffice to rescue an inverse-Blaschke-weighted contour detector without a spacing assumption.
GAP: Establish or obstruct the proposed separation-free small-cluster noncancellation bound below. Actual zero configurations, boundary estimates, contour selection, larger clusters and actual PSD remain independent gaps. No such bound or counterexample is asserted.
REASON: A finite, independently testable part of the derivative-free central-gap mechanism survives source comparison. A separate creative research attempt may test it after approval, using citations for the standard tools and proving only the stated difference. This is not a theorem import or a novelty claim.
SCOPE: Only the small-cluster test and its precise implication or limitation for this contour mechanism. No actual-Xi sign, off-line zero, zero separation, meromorphic norm bound or new zero-free region may be assumed. The exact target and family are unchanged; the 1 November source-URL recovery review below completes the missing provenance. Research remains subject to the supervisor gate.

## Proposed test, not established mathematics

Fix delta in (0,1/2), a=3/2, d=a-delta and R=a-delta/2, as in
L645. Let n>=5 be an integer, corresponding to n=floor(log gamma)
when the logarithmic grid is used. In the translated variable
z=s-(2+i gamma), use exactly z_j=i j/n, 0<=j<n, and the proposed
complex finite-Blaschke factor

    B_n(z) = product_(0<=j<n) R(z-i j/n)/(R^2+i(j/n)z).

This is the complex product, not C645c's product of moduli at -d.
A future proof must check denominators and conventions explicitly.

Consider synthetic clusters consisting of z_0=-d and at most two
additional distinct points z_k. Require every additional point to satisfy

    |z_k+d| < delta/8,   -3/2 < Re z_k < -1,   |z_k| < R.

Give every point unit residue. None is a grid node. These are proposed
test configurations, not claimed zeros of Xi. No zero-existence or
realization hypothesis is imported. The proposed normalized quantity is

    S_n = B_n(-d) sum_(z_k in cluster) 1/B_n(z_k).

The bounded question is whether there exist c_delta>0 and N_delta such
that |S_n|>=c_delta for every n>=N_delta and every permitted cluster,
or whether an explicit permitted family gives exact cancellation for
unbounded n. Seek exact cancellation, or a rigorously quantified loss
large enough to destroy the proposed detector's exponential gain;
small floating-point values or an unquantified limit are insufficient.
One- and two-pole subfamilies are allowed. No calculation, asymptotic
expansion or cancellation construction has been made in this source turn.

## Relevance and decision test

The main gap remains actual-Xi signs/all-degree mixed positivity.
This is a probe of a new derivative-free contour mechanism at the
normalization bottleneck: unit residues of F-P are available at the
stipulated simple zero, whereas a useful lower bound on zeta'(rho)
is not. The proposed sum tests the unproved idea that positive residues
cannot cancel after division by the grid factor. A later application
would first have to derive its contour identity from the named residue
theorem, check every other pole and control the boundary uniformly in P.
Those tasks are not assumed completed by defining S_n.

Continue if a usable lower bound is proved for this family, explicitly
retaining the limitations to a small synthetic cluster. Abandon this
universal noncancellation shortcut if an admissible exact-cancellation
family is proved, even with all its poles away from the boundary.
A merely polynomial loss in the normalized sum does not automatically
erase an exponential gain and must not be reported as a decisive stop.
An obstruction here would concern this proposed generic implication,
not actual Xi or RH; it would redirect detector design toward cluster
isolation or a different weight. Failure to decide the bounded test is
EXPLORATION, not evidence for noncancellation.

Essential local input: L645 for the unchanged nodes, complex factors
and temporary interpolants; L018 for the conditional Xi interpretation.
Audited C645b/C645c explain the normalization gap and are comparisons,
not residue-sum lower bounds. L467 remains available for future counts,
but its theorem is not needed for a three-pole synthetic configuration.
No cross-notebook input. Reuse the finite-Pick and holomorphic-zero
source assessments without reproof; cite the primary residue theorem
only if applied. Full matching Mathlib coverage is unchecked.

Creative routing is justified by the precise obstruction: complex
weighting may cancel the positive residues that were meant to replace
the unavailable derivative lower bound. The bounded test is the exact
small-cluster family above. Its outcome would discriminate whether this
central-gap detector deserves development; it would not be a complete
RH argument. Do not repeat the mechanism after an unsuccessful attempt
without materially new input, an informative obstruction or a refined test.

## Source-URL recovery review — 1 November 2026

LITERATURE_REASON: The supervisor reported missing direct source URLs in this ready assessment. This bounded repair reconfirms the essential elementary sources and reuses the parent assessment's completed overlap review; it does not repeat discovery or broaden the mathematical target.

Opened the direct Beck and Zakeri URLs above on 1 November 2026
(unversioned online texts). Beck Theorem 8.1.5 assumes a simple,
positively oriented closed contour, analytic boundary values and finitely
many isolated interior singularities. Its proof uses disjoint small
circles and Cauchy–Goursat, retaining every residue. Theorem 8.1.7(1)
and its Laurent-series proof give the simple-pole limit rule. Neither
result estimates a weighted residue sum. Any eventual contour application
must check the complete singularity set and boundary analyticity;
this review does not apply the theorem to a new integrand.

Zakeri's Section 8.3 paragraph following Example 8.33 states finite
Blaschke division for a disk-valued holomorphic function. It removes
zeros with their orders, then uses boundary modulus and the maximum
principle. This confirms the convention underlying L645; it supplies
no noncancellation theorem for inverse factors. The next research step
must check scaling, denominators and the complex convention for the
saved B_n rather than replacing it by a modulus product.

The Padé and polefinding sources were not newly retrieved: their
previously inspected hypotheses, proof cases and restrictions are reused
from drafts/literature/2026-11-01-derivative-free-pick-contour-detector.md.
Their direct versioned/author URLs are now explicit in SOURCE_EVIDENCE.
The scoped parent duplicate search and the logarithmic-growth stop were
reused; no new local cluster result was found or claimed. No additional
source is essential for testing the exact finite rational family.
Full matching Mathlib coverage remains unchecked.

Decision: retain EXPLORE for the exact saved target, with direct source
provenance repaired. This is a process repair, not a mathematical advance,
an informative negative result or a renewed exploration budget. No new
lemma, script, asymptotic calculation or cancellation construction was
made. The family, thresholds, input IDs and unresolved actual-Xi
assumptions above are unchanged.
