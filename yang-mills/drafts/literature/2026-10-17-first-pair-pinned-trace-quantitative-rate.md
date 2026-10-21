# First-pair pinned trace — quantitative comparison coverage

TARGET: Determine whether L079's pinned-trace comparison satisfies |a^3 J_(i,N)-2 gamma D_(i,a)| <= C_i N^(-1/2) log(eN)^2 for both actual L010 probes.
CHECKED: 2026-10-17
DECISION: EXPLORE
SEARCH_EVIDENCE: Reuse the complete-coefficient quantitative review's two external queries and notebook-local duplicate/failure search; inspected L079 sections 2–5 and the primary scalar Green statements below. No inspected theorem states this variable-coefficient, full-heat trace estimate.
SOURCE_EVIDENCE: Lawler–Limic Random Walk: A Modern Introduction (2010), author-hosted PDF, section 1.1 pp. 9–10, Theorem 4.3.1 pp. 81–84 and Proposition 4.6.2(a) p. 97 with its transient proof; L079(8)–(18) supplies the exact local comparison and existing qualitative estimates.
COMPARISON: Standard scalar Green asymptotics and the killed-domain identity apply to the three-dimensional nearest-neighbor Laplacian. They do not directly give the required variable-coefficient l2/energy comparison or its heat-summed trace rate. A new bounded attempt on that difference is justified without reproving the named scalar theorems.
GAP: Quantify L079's differentiated-source approximation, monopole energy projection and coefficient freezing with mode dependence controlled before summing the complete heat spectrum. The finite diagnostic remains D_(i,a), so its continuum rate is excluded.
REASON: This isolates an existing qualitative comparison in a fixed physical interior, with accessible standard scalar inputs and an explicit threshold; it is independent of the separate L101 rate obstruction. EXPLORE does not certify novelty or the inequality.
SCOPE: SU(2), relative pinned cube, straight lower-rooted direction-1 forest, admitted even N with a=8/N, tau=1/16, actual probes i=3,6; only L079(2)'s finite-diagnostic comparison is covered.

This assessment is newly written in a literature-only turn. Separate
supervisor approval precedes mathematical work; no rate has been proved.

## Inspected primary input and applicability

Lawler and Limic, [*Random Walk: A Modern Introduction*](https://www.math.uchicago.edu/~lawler/srwbook.pdf),
Cambridge University Press (2010), author-hosted text accessed
2026-10-17. Section 1.1 defines P_d by symmetric finite-range
irreducible increments. Theorem 4.3.1, printed pp. 81–84, gives
G(x)=C_d/J(x)^(d-2)+O(|x|^-d), d>=3; simple random walk is
explicitly included, with its bipartite case addressed before the
proof. Proposition 4.6.2(a), printed p. 97, expresses killed Green
as full Green minus the exit expectation for any lattice subset in
the transient dimensions. Its proof decomposes visits at the exit
time. The nearest-neighbor transverse vertex Laplacian has this
scalar walk representation after accounting for generator
normalization. It is not the four-dimensional relative edge operator.
These scalar results do not state an l2 comparison for differentiated
sources with variable multipliers, a monopole energy-projection rate
or a full heat-summed signed-trace bound. Those remain to be justified.
Import the named results by citation if used; a reproof is unnecessary.

## Precise bounded test

Use the exact J_(i,N), D_(i,a) and gamma of L079(1)–(2), with
L078's reduced trace already obtained by its exact co-closed covariance
cancellation. This avoids the failed upper-axial-profile deletion in
ATTEMPTS/024–025. L079(5)–(6) keep the finite right source, (12)
keeps coefficient differences, and (18) shows where complete modal
uniformity is needed. They are starting identities, not a new estimate.

Seek an N-explicit estimate for those retained comparisons, including
zero extension and all pinned transverse edges. The source is within
the fixed physical compact K of L079, but covariance outputs are not
restricted to K. The full polynomial dependence on exterior mode
indices must be retained before applying actual heat coefficients.
No l2 bound for an undifferentiated infinite monopole, bounded inverse
on all l2, or quantitative Weierstrass theorem is assumed.

Continue if an explicit error meets the stated threshold with constants
independent of N after the complete heat sum. An applicable stronger
bound also passes. If a proposed intermediate norm estimate fails,
preserve the precise obstruction and decide whether a signed trace
estimate still remains independently testable; do not promote that
norm failure to a lower bound for either actual response. If no such
test remains, abandon this mechanism and select a different target.

## Downstream use and unresolved inputs

This would remove one qualitative comparison in L084/L218's mixed
component. It would not prove the complete coefficient's requested
remainder: L080's diagnostic convergence, L101's O(N^(27/10))
replacement, L090 and the later component limits are separate gaps.
The main construction gap remains ultraviolet-uniform interacting
matching with reflected error <=c_box/2, continuum axioms and infrared
finite positive mass.

Essential local inputs: L008 L010 L028 L045 L062 L064 L065 L070
L074 L075 L076 L078 L079. Preserve both probes, their full heat sums,
all relative end rows and modes, both residual subtractions, the actual
forest upper jump, and the finite diagnostic normalization. Imported
qualitative statements receive no unproved uniform rate. No expansion
uniform in coupling is assumed. Mathlib coverage of the full target
and these scalar theorems was not checked; no absence claim is made.
