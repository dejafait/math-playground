# Frozen anisotropic cancellation — completed audit source scope

TARGET: Critically audit L299's complete frozen anisotropic bulk cancellation, including row-sum convergence, fixed-slice determinant factors and zero-momentum integration.
CHECKED: 2026-10-28
DECISION: EXPLORE
SEARCH_EVIDENCE: Reused the completed anisotropic constant-field assessment, its exact-statement/stronger-result primary searches and ATTEMPTS/047--050 screen; read L299 hypotheses and sections 1--4 to identify the new audit obligations. No unchanged anisotropic search was repeated; reopened the cited primary Gaussian theorem statements and essential proof cases.
SOURCE_EVIDENCE: Reused the prior Burgio--Feo--Peardon--Ryan, Giordano and Luescher--Weisz comparisons at their recorded versions and equation ranges; directly read Bauerschmidt--Brydges--Slade arXiv:1907.05474v2 (11 November 2019), section 2.1 pp. 29--33, Definitions 2.1.1--2, Proposition 2.1.6 with proof, Proposition 2.1.9 including the degenerate case and Corollary 2.1.11 with proof. These cover finite Gaussian algebra, not L299's kernel or determinant matching.
COMPARISON: L299 identifies this covariance-removal tensor by finite log-determinant Taylor algebra instead of importing a background-gauge self-energy statement; the frozen weighted identity goes beyond the exact specializations established by the inspected sources, without claiming originality.
GAP: The conceptual audit must check the complete external-curl kernel estimates, density phase/overlap factors, real Fourier/color multiplicities and singular-momentum passage. Source coverage is sufficient for this bounded audit; no audit acceptance or variable-source estimate is recorded here.
REASON: Step 540 separately completes source coverage for the continuation first written in step 539. The exact target is ready for one conceptual audit, using the existing literature comparison and explicit local proof rather than assuming a background-gauge theorem identifies this coefficient.
LITERATURE_REASON: The supervisor required separate approval of the new audit continuation; L299 introduced kernel, cofactor and infrared proof claims not audited by the prior construction assessment. This turn checks their source scope, without deriving or approving those claims.
SCOPE: SU(2) infinite lattice, constant rho in [1/2,3/2], raw-edge own-slice Wilson jets, fixed unweighted transverse covariance and full unchanged density; no variable-source or relative-box conclusion.

## Exact proof to review

Read `lemmas/L299-frozen-anisotropic-constant-field-cancellation.md`.
Its essential local inputs are L279 L280 L282 L283 L287 L289 L297.
Reuse `2026-10-28-anisotropic-constant-field-bulk-cancellation.md`
for the source comparison; the target's gauge, weight interval and
coefficient convention have not changed. L298 supplies context for
the intended downstream residue application, not an anisotropic
finite-box estimate.

The new proof has three load-bearing steps. The complete cubic
kernel, including external-curl placements, is asserted to decay as
(1+distance)^-6 uniformly in rho, using actual translation-invariant
anchor differences. The cofactor identity for the Hessian compressed
to the fixed slice cancels both the exponential-coordinate factor
and the gauge-overlap factor, retaining lambda(p) in the denominator
of the physical determinant. Finally the integrable Taylor coefficient
is a second momentum derivative of log(lambda kappa), whose small
sphere flux tends to zero in dimension four. These are proof claims
for audit, not assumptions imported from gauge invariance.

The exact-rational script and its full certificate under
`scripts/anisotropic-bulk/` test 80 selected diagonal symbol values.
They are diagnostics only. They do not establish the tensor identity,
its off-diagonal entries, row-sum convergence or regulator passage.

Continue only if the separate audit accepts the exact density and
Wilson normalization, projection factors, all cubic parts and the
integrable zero-momentum limit under the stated hypotheses. A failure
must be repaired in the canonical proof or retained as an obstruction;
numerical agreement is insufficient. Even acceptance would leave
source localization, relative boundaries, other L297 residues, higher
remainders, continuum axioms and positive mass unresolved.

Full matching Mathlib coverage has not been checked. This file approves
only the saved conceptual audit target for a later research turn;
it does not accept L299 or authorize a variable-source lemma.

## Completed source review (step 540)

The main gap remains construction of the interacting continuum theory
and positive mass. The intermediate target is acceptance or correction
of L299's claimed complete frozen tensor identity. If accepted, it could
support a separately assessed source-localization test for L297's
remaining residues. No such downstream estimate follows from this review.

The duplicate/failure comparison is reused from the completed
`2026-10-28-anisotropic-constant-field-bulk-cancellation.md`, especially
its sections “Search, reuse and prior failures” and “Exact uncovered
difference and permission for later work”. The isotropic cancellation
is already covered; the metric tree weights and background-field
self-energy results do not identify the independently weighted fixed-slice
covariance-removal tensor. ATTEMPTS/047--050 remain preserved evidence,
not a global prohibition on the exact Wilson-specific identity.

Reopened primary input: Bauerschmidt--Brydges--Slade,
*Introduction to a Renormalisation Group Method*, LNM 2242 (2019),
[arXiv:1907.05474v2](https://arxiv.org/pdf/1907.05474v2),
printed pp. 29--33 (PDF pages 38--42, zero-based).
The setting is a finite real index set and a symmetric positive
semidefinite covariance. Proposition 2.1.6 evaluates polynomial Gaussian
convolution by a finite Laplacian expansion; its proof uses uniqueness
for a finite system of ODEs. Proposition 2.1.9 proves the Gaussian
moment-generating identity, reducing a degenerate covariance to its
support. Corollary 2.1.11 adds independent Gaussian covariances.
For finite real transverse coordinates these hypotheses permit the
pairing algebra without a positive-definite ambient covariance.
They do not justify an infinite row sum, an infrared limit, complex
Fourier multiplicities, or Wilson/density matching. Those remain local
proof obligations. The cited propositions need no reproof; inspecting
L299's different matching and convergence claims is necessary.

The bounded audit must explicitly compare L299(11)'s four cubic
placements with its full kernel, then check (14)'s normalization,
(15)--(20)'s coordinate/gauge overlap and both density jets, and
(21)--(24)'s coefficient and infrared passage. In particular pointwise
Taylor expansion is not a uniform finite-background chart. Acceptance
requires a valid ordinary-row-sum identification and controlled singular
flux, including off-diagonal tensor entries. A failed factor or
uncontrolled passage requires correction or a retained obstruction;
the 80 symbol diagnostics cannot decide acceptance. This specifies a
test, not its outcome. No essential source is blocked and no additional
unread lead is required to attempt this exact audit. No lemma or
mathematical script was changed.
