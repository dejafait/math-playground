# Sparse Hankel bound to a full boundary residual — completed coverage

TARGET: Establish the full principal-part reduction and boundary lower bound for C645g's sparse positive-residue family under exact grid interpolation.
CHECKED: 2026-11-01
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the completed full-pole-hankel-boundary-mechanism and three-moment-contour-transfer searches; compared C645f (8)–(12), C645g (1)–(6) and its application qualification, and recorded scalar/finite-Hankel failures. Retrieved specific primary decomposition, projection and simple-pole cases; no unchanged broad search or novelty inference.
SOURCE_EVIDENCE: Baratchart–Chevillard–Qian (2016), Section 2 pp.18–21, Theorem 2/(17)–(19) pp.24–25 and analytic-term removal in (25) pp.27–28, https://www.must.edu.mo/images/SCSE/qiantao/QianTao_P147.pdf ; Beck et al., Theorem 8.1.7(i) and its complete simple-pole proof, https://complexanalysis.org/web/sec_residue-thm.html . Parent assessments retain the other inspected calculus sources.
COMPARISON: Standard meromorphic decomposition and Hardy projection cover the analytic framework. C645f checks identical grid factors in a smaller family; C645g supplies the quantitative norm input. The full F/P application still needs finite-pole, grid-removal, bounded-remainder and scaling verification; no new operator theorem or spectral bound is needed.
GAP: Establish the stipulated synthetic transfer by local specialization; no identity or boundary lower bound for F-P is proved in this literature turn. Actual-Xi census/clearance/realization and an independently smaller upper bound remain open.
REASON: Essential source coverage is adequate for the unchanged saved target. Proceed next to the bounded mathematical application, importing the standard tools and proving only their precise applicability and normalization.
LITERATURE_REASON: The saved REVIEW_REQUIRED nomination adds a full meromorphic F and holomorphic P beyond the audited rational q; this separate review checks that application scope rather than repeating the norm audit.
SCOPE: Exactly the synthetic hypotheses, q, g, constants and desired conclusions below; retain neighborhood regularity, complete distinct simple-pole list, exact interpolation, positive integer residues and M<=kappa_delta*n. No weaker regularity, higher-order poles, actual-Xi transfer, new upper bound or Nehari/AAK reproof is approved.

The nomination and decision test below are preserved. Their pending-review
language records the earlier proposal; the completed comparison at the end
supersedes that source status without proving the proposed mathematics.

## Proposed target and unchanged norm input

Retain C645g's complete hypotheses and definitions: fixed
0<delta<1/2, 0<eta<delta/2, d=3/2-delta, R=3/2-delta/2, x=-d,
integer n>=5, t_j=j/n, the exact complex B_n, distinct finite Z in
|a|<=R-eta containing x and avoiding every grid point, positive integer
residues r_a, and M=sum r_a<=kappa_delta*n. Use the audited explicit
c_delta and kappa_delta from C645g, without strengthening them.

Introduce F meromorphic on an open neighborhood of the closed disk
|z|<=R whose complete pole set in that closed disk is exactly Z,
each pole simple with residue r_a. Let P be holomorphic on a
neighborhood of that closed disk and satisfy P(it_j)=F(it_j)
at every grid point. F, P and Z may depend on n. No positive-real
property, symmetry, degree restriction on P or actual-Xi realization
is imposed. Neighborhood sizes may depend on the data.

For |zeta|=1 define the full boundary symbol

    g(zeta) = B_n(x) [F(R*zeta)-P(R*zeta)] / B_n(R*zeta).

Keep q exactly as defined in C645g (2), including its factor 1/R,
complex amplitudes, normalized circle L2 measure and strictly negative
Hardy modes. The proposed mathematical task is to justify the full
principal-part reduction, all grid removals and any holomorphic
remainder, and then prove or identify a failure of the desired relations

    H_g = H_q,
    max_(|z|=R) |F(z)-P(z)|
        >= c_delta exp(-delta*n/8) / |B_n(x)|.

These are targets, not results of the audit turn. In particular do not
discard an unspecified analytic part or identify the norm of an
operator with the boundary norm of a chosen symbol. The proof, if
available, must retain the exact scale and use the appropriate
one-sided norm comparison. No reproof of Nehari/AAK is requested.

## Separate review and decision test

Essential local mathematical inputs for the proposed transfer are
C645g's audited norm estimate and C645f's exact factor/grid calculations
within their stated scopes. C645c's rate is already used in C645g;
its conditional zeta envelope data are not imported. C645d's scalar
cancellation and C645b's envelope limits remain preserved comparisons.

The next turn should reuse the parent source assessments, compare the
primary hypotheses for removal of finite principal parts and the Hardy
projection application, and set IMPORT, SPECIALIZE or EXPLORE only if
coverage is adequate. Read additional primary material only if that
comparison reveals an essential gap. No unread lead is an input.

Continue to a later mathematical application if the complete pole list,
regularity, interpolation and normalization permit the proposed bridge.
Otherwise identify the exact missing hypothesis and refine or stop this
application. Even a successful transfer supplies a necessary boundary
size only: the actual sparse census with this coefficient, contour
selection/clearance, interpolant realization and an independently
smaller upper bound remain unresolved. No RH candidate or novelty claim.
Full matching Mathlib coverage is unchecked. No cross-notebook input.

## Completed source comparison — 1 November 2026

Main gap: actual-Xi signs at unbounded heights/all-degree mixed positivity.
The intermediate target connects the audited synthetic norm input to a
complete boundary residual. It could extend this detector beyond three
poles under the stipulated small census coefficient. Actual-Xi census,
clearance, interpolant realization and a smaller upper bound remain open.

### Primary statements and relevant cases inspected

L. Baratchart, S. Chevillard and T. Qian, *Minimax principle and lower
bounds in H2-rational approximation*, J. Approx. Theory **206** (2016),
17–47, [published PDF](https://www.must.edu.mo/images/SCSE/qiantao/QianTao_P147.pdf),
[DOI](https://doi.org/10.1016/j.jat.2015.03.004).
Section 2, pp.18–21, specifies normalized circle norms, strictly negative
Hardy modes, contractive orthogonal projections and finite pole-residue
decomposition. Equation (17), p.24, uses domain H2 and projection of the
symbol times the input. Theorem 2/(19), pp.24–25, identifies the bounded
symbol's operator norm with distance to H-infinity at index zero, not
with its own boundary norm. Section 5.2/(25), pp.27–28, explicitly
discards an H2 term under negative projection; the complete display and
following explanation were inspected. These are standard inputs, not
new estimates. No general AAK proof or rational matrix calculation
needs reproduction here.

M. Beck et al., *A First Course in Complex Analysis*, online unversioned
[Theorem 8.1.7(i)](https://complexanalysis.org/web/sec_residue-thm.html),
accessed 1 November 2026. Read the simple-pole statement and complete
proof case: its Laurent expansion is the residue divided by z-a plus
an analytic Taylor series. This supplies the local principal-part tool,
without identifying residues after a particular rational division.
Reused the parent contour assessment's inspected residue theorem, ML
bound and finite-Blaschke division argument, retaining their regularity.
Laurent's theorem 7.3.6 in the same text was inspected as supporting
context; its full proof is not claimed audited or needed as a new input.

### Exact applicability boundary

The saved neighborhood and clearance hypotheses match the regular
boundary framework, subject to checking the quotient's singularities.
No uniform neighborhood size or bound on the analytic remainder is
requested. Arbitrary holomorphic P remains allowed: degree constraints,
behavior at infinity and a positive-real condition are not imported
from other interpolation results.

The next mathematical step must inspect all grid points and every pole
in the complete finite Z. Reuse C645f (8)–(12) only with an explicit
scope check; its one-to-three-pole conclusion is not imported for the
larger family. Verify the transformed simple principal parts with r_a
retained, then verify a remainder holomorphic near the closed disk.
Its product with every H2 input must satisfy the Hardy projection
hypothesis. An assertion about the projection of the symbol alone does
not suffice for equality of the full operators.

Retain C645g (2)'s 1/R, normalized circle measure, strictly negative
modes, exact complex amplitudes and explicit constants. The final
norm comparison must be one-sided, not equality with the norm of this
chosen boundary representative. These are checks for the subsequent
application, not a derivation of either proposed relation above.

The sources settle the standard tools, but not these particular grid
zeros, residues and scale factors; a local applicability proof is
therefore justified. No strengthened estimate, interpolant construction
or operator-theorem reproof is approved. Matching Mathlib coverage
remains unchecked, with no absence or formal-verification claim.

### Duplicate, failure, access and decision record

Reused the queries and theorem comparisons in the full-pole-hankel and
three-moment-contour assessments named in SEARCH_EVIDENCE. The targeted
local search checked the deferred principal-part scope in the
positive-residue assessment and C645g audit history. No completed full
F/P transfer was found in those checked records; this is not a global
novelty search. C645f is a restricted predecessor; C645g explicitly
leaves this application open.

C645d's exact scalar cancellation, recorded in
`ATTEMPTS/2026-11-01-inverse-blaschke-unit-residue-noncancellation-stop.md`,
does not license cancellation of the full operator. The September
finite-Hankel extrapolation and strip-positivity stops, already assessed
in the parent review, retain their finite-to-infinite and positivity
obstructions. None is reopened or treated as a global ban. No new
zero-free estimate or cross-notebook theorem is proposed.

Retrieval was limited to the primary passages identified above. A
guessed supplementary zeros/poles URL was unavailable; the accessible
simple-pole case and local grid proof leave no essential dependence on
that URL. No persistent source blocker or unread essential input remains.

Decision: SPECIALIZE for the unchanged TARGET. The continuation test is
a complete principal-part/Hardy-operator argument with exact scaling and
the proposed boundary threshold. A surviving grid term, unremoved pole
or missing bounded-analytic multiplier premise requires a precise
failure report and refinement or stopping of this synthetic application.
Even success leaves every actual-Xi assumption stated above unresolved.

Outcome: EXPLORATION, a completed new source-scope comparison. No new
lemma, mathematical script, estimate, RH candidate or proof assembly
change. This review approves a later specialization, not its conclusion.
