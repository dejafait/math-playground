# First-zero resolvent: direct ODE comparison nomination2263

TARGET: Assess direct one-dimensional comparison criteria for log-concavity of the first-zero sine resolvent, including the oscillatory ODE, Neumann origin condition and decay at infinity, and nominate one bounded test that does not assume paired-density joint log-concavity.
CHECKED: 2026-11-21
DECISION: EXPLORE
SEARCH_EVIDENCE: Review2264 searched forced Helmholtz/log-concave forcing/Neumann comparison and Kennington/Korevaar concavity principles; checked three candidates and local C919s/C919t plus notes2257/2260; full queries/access qualifications are in 2026-11-21-first-zero-ode-source-notes-2264.md.
SOURCE_EVIDENCE: Inspected Keady1985 Theorem1 pp181-182 and boundary/proof discussion pp182-184, DOI10.1017/S0004972700004676; Gallo-Moraschi-Squassina2026 Theorem4.1 with complete proof4.1-4.8, Remarks4.2-4.3, Theorem4.4 statement and Theorem5.1 boundary cases, DOI10.1017/prm.2026.10177; Kennington1985 indexed excerpts only, not an import.
COMPARISON: Keady's homogeneous planar Dirichlet theorem and the general principle's global boundary application do not cover the forced oscillatory half-line Neumann/decay problem; Gallo-Moraschi-Squassina's exact stationary solution-variable monotonicity requirement supplies one necessary hypothesis test, not a curvature theorem here.
GAP: No direct marginal-preservation import or justified boundary/forcing specialization was found; the sign of the specialized logarithmic stationary source derivative is uncalculated, while positivity, even extension, quotient identity, actual-Xi applicability and iteration remain open.
REASON: The source comparison is complete within the three-candidate bound; proceed only to the separately nominated strict-monotonicity test after gate approval, retaining all source/boundary mismatches and earlier stops.
LITERATURE_REASON: Changed mechanism from paired-density curvature to a forced one-dimensional oscillatory boundary problem; notes2257 cover its solution formula, not the needed curvature comparison.
SCOPE: Completed source comparison and one bounded nomination only; no proof, parameter tuning, numerical marginal test, actual-kernel enclosure extension or repetition of the completed joint-density audit.

## Review2264 disposition

The paragraphs below are the preserved pre-review nomination, including
its then-outstanding source questions. They are not a second current
action. Review2264 is recorded in
[source notes2264](2026-11-21-first-zero-ode-source-notes-2264.md).
The next bounded test and its qualifications are in
[monotonicity assessment2264](2026-11-21-first-zero-ode-monotonicity-test-2264.md).
No generic comparison or new identity was proved in completing this
review. The optional Kennington access issue does not prevent the
covered conditional matching calculation.

## Preserved nomination before review2264

## Exact object and remaining hypotheses

Keep the original generic first-zero question: K is positive, even
and smooth on R, (log K)''<0 everywhere, and for every m>=0 and
B>0, exp(B|u|)|K^(m)(u)| tends to zero at both infinities.
Let x be its least positive real cosine zero, multiplicity allowed,
and write

    G_x(u)=x integral_0^infinity K(u+t)sin(xt)dt, u>=0.

The comparison to assess concerns the inhomogeneous equation
G_x''+x^2 G_x=x^2 K, the origin condition G_x'(0)=0, and decay
at infinity. These formulas are documented for the fixed model in
C919s and are proposed interfaces for the general source comparison;
this nomination proves no generalization. Establishing positivity,
the smooth even extension, the quotient identity and every use of
those boundary data remains necessary for any future generic claim.
The target sign would be (G_x')^2-G_x G_x''>=0 on the half-line.
No such sign or new identity is asserted here.

The source review must check the sign of the zeroth-order term and
the inhomogeneous forcing explicitly. A theorem for a positive
resolvent of -d^2/du^2+lambda, a homogeneous ground state, or a finite
Dirichlet interval is not automatically applicable. Do not presume
that a least Fourier zero is a principal eigenvalue condition.
Search exact terminology and stronger results, and inspect relevant
primary theorem hypotheses and proof cases before choosing a test.

Continue only if a source matches these conditions or supplies a
precise additional condition with one independently testable sign
threshold. Otherwise record the specific mismatch and reject that
comparison mechanism; do not return to a generic paired-density
assertion or repeat the existing approvals. Review at most three
concrete source candidates. No current candidate has been checked.

C919s and C919t are the essential local comparisons. Notes2257 and2260
record the nearest source searches and failures. Preserve the closed
quartic u=1 calculation, the fixed log-cosh density test and actual-Xi
enclosure stops. This is a new source target, not permission to retune
any of those tests. It leaves actual-Xi applicability, iteration and
all-degree transfer open even if the comparison succeeds. No
cross-notebook result is proposed. Full matching Mathlib coverage
remains unchecked. A later mathematical continuation requires its own
saved ready assessment and any separate approval required by the gate.
