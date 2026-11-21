# Conceptual audit nomination: signed obstruction for two positive constructions

TARGET: Critically audit C681c's uniform lower bound ||T_(n,theta)||_2>=exp(-19*n/2000) for every convex blend of L673 and L681, including the signed saddle limits, complementary edges, finite-product errors and rational point-to-norm transfer.
CHECKED: 2026-11-02
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 72 reused the unchanged prescribed-node positive-quadrature assessment (duplicate/failure comparison) and displaced-signed-angular-sampling assessment (Theorem 2 statement and proof-reading limits); read C681c Sections 1--6 and L666 source statement/(6) only to compare invoked inputs and delimit the audit. No repeated browsing or novelty claim.
SOURCE_EVIDENCE: NIST DLMF Section 1.10(iv), (1.10.8), as inspected in L681's saved audit; Danchenko--Semin arXiv:1503.06476v1, Section 1.1 Theorem 2 and complete proof, PDF pp.1--2,6--7, as inspected in the signed-angular-sampling assessment. The exact source statements and applicability checks are retained in C681c Sections 1 and 6.
COMPARISON: These sources supply the residue identity and rational circle quadrature, but not this family's signed asymptotics, the exponent barrier 121/13000, a uniform blend obstruction or its finite-product remainder. The audit must verify that specialization; no theorem about arbitrary positive weights is claimed.
GAP: Independently validate the analytic logarithm branches, O(1) derivative errors, Gaussian domination and sign, all complementary contour costs, uniformity in theta and the enlarged simple-pole completion including -R. Source manuscripts retain their recorded audit qualifications.
REASON: Separate literature approval completed in step 72: saved essential coverage is sufficient for this exact audit and SPECIALIZE remains ready. This approves execution of a later REPRODUCTION conceptual audit, not the truth of C681c. No mathematical audit, new theorem or source discovery is claimed.
LITERATURE_REASON: The supervisor required separate approval of the new audit nomination; this turn checks its source boundary against the saved primary readings, without repeating the already adequate search.
SCOPE: Exactly TARGET with n=12q+3, q>=1, x=-5/4, R=11/8, the unrounded L673 nodes, the two unchanged positive weight families, theta in [0,1] possibly n-dependent, unit anchor and normalized continuous L2. No arbitrary-weight impossibility, effective onset, original H estimate or Xi transfer is covered.

The main gap is actual-Xi all-degree mixed positivity. This audit is
needed before using the new signed obstruction to stop the blend route.
The prior finite C681b test did not prove an asymptotic obstruction, and
C681a only stopped a fixed-rectangle absolute-integrand estimate.
Neither is a premise of C681c.

Essential inputs are L666 (6) and its rational quadrature source scope,
L673's exact nodes, positive weights, contour identity and scalar helper
proofs, and L681's weights, Robin kernel identity, imaginary-root census
and contour estimates. The canonical result is
`lemmas/C681c-positive-blend-signed-saddle-obstruction.md`; the full
scalar evidence is `scripts/one-sided-hankel/positive-blend-saddle-certificate.json`
with its generator in the same directory. The certificate checks constants,
not the signed asymptotic argument.

Direct source links and qualifications:

- [DLMF (1.10.8)](https://dlmf.nist.gov/1.10#E8): finite meromorphic
  residue theorem with no boundary pole and positive orientation;
  source reading reused from the discrete-Robin audit assessment.
- [Danchenko--Semin v1](https://arxiv.org/pdf/1503.06476v1), Theorem 2:
  finite distinct interior set containing zero, reflected completion,
  ordinary orders <=s and combined zero/infinity orders <=2s-1.
  Its full Theorem 2 proof was inspected; its use of Theorem 1 retains
  the prior qualification that the latter proof was not independently audited.

Check the real saddle signs at two potentially different locations;
a common profile is unnecessary. Verify the shift from limiting to finite
log derivatives is O(1), not merely o(n), and that the singular numerator
normalization in P is independent of the integration variable. Verify
the complete rescaled tails, actual Robin height Y_n, positive residual
at -1 and all pole orders after adding W_(-R). In particular no point
evaluation controls an L2 norm without the stated rational formula.
The lower-bound exponent must remain strictly below 1/100 after every
polynomial loss; existence of an onset is sufficient for this target.

Continue on validation or a precise repair within this exact claim;
reject the stop if a load-bearing gap cannot be repaired. Arbitrary
positive weights and original H/support/realization/Xi signs remain open.
Full matching Mathlib coverage is unchecked. This is a separate audit
nomination, not an RH candidate or a second mathematical attempt.

## Separate scope approval — step 72, 2 November 2026

The assessment is ready for the exact TARGET above. This is a literature
and process gate only; its unchanged SPECIALIZE conclusion is not new
mathematical evidence. The present step is honestly STALLED with respect
to mathematical/source progress, while making the required next audit
executable. No source blocker was found within the saved reading scope.

The source-level comparison uses the actual inputs of C681c, not a
hypothetical general quadrature theorem. Its Section 1 invokes the finite
residue theorem recorded in the discrete-Robin audit assessment, with
positive orientation, finitely many interior singularities and no boundary
singularity. Section 6 invokes Danchenko--Semin v1 Theorem 2 at radius
and order parameter one, whose saved complete statement and proof reading
are in the displaced-angular assessment, pp.1--2 and 6--7. L666 retains
the same statement and its finite rational formula (6). The added anchor
parameter -R is an application obligation for the enlarged reflected
pole set, not a new quadrature theorem. The audit must check its complete
pole census, multiplicities, origin/infinity behavior, normalization and
phase-selected observation. No application inequality is certified here.

C681c Sections 2--5 present explicit family estimates and a direct Taylor
and Gaussian-tail argument, rather than importing an unspecified saddle
point theorem. Thus no additional general asymptotic source is essential
for auditing this written proof. Those estimates, analytic branches,
finite-product derivative errors and tail domination remain precisely the
unverified mathematics. An audit must read their complete evidence; the
22 scalar checks do not discharge those obligations. Theorem 1 underlying
Danchenko--Semin Theorem 2 remains independently unaudited as already
recorded; using the precisely cited standard input does not assert its
independent manuscript verification. Full matching Mathlib coverage stays
unchecked.

The duplicate/failure comparison is unchanged: L673 and L681 are the two
specified constructions; C681a stops an absolute fixed-rectangle estimate,
C681b is finite-size evidence, and the signed-blend ATTEMPTS record merely
points to unaudited C681c. None substitutes for its conceptual audit or
rules out arbitrary weights. The bound sought remains exp(-19*n/2000),
uniform in n-dependent theta, with existential onset. Validation or a
precise repair permits retaining this family-specific stop; an irreparable
load-bearing gap requires withdrawing that stop, while preserving the
record. H/support/realization and actual-Xi mixed signs remain independent.

Creative discovery is deferred only to resolve this essential analytic
stop audit. No new central mechanism is justified by this source gate;
renaming another blend fit would repeat the stopped construction.
