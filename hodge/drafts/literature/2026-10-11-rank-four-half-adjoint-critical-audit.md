# Rank-four half-adjoint critical audit — source coverage approved

TARGET: Assess source coverage for a critical audit of L087's half-adjoint construction, common lifting cocycle, exact-h factor stability and nonspin survivor constraints.
CHECKED: 2026-10-11
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Read complete L087, relevant L052/L061/L079 passages, histories 207--208 and ATTEMPTS/056; reused prior group/lifting coverage and searched the essential projective-plus-determinant connection passage and primary accessible versions, with queries and inspected ranges below.
SOURCE_EVIDENCE: Reused Choe--Hitching 2203.06645v2 introduction, Section 2.3 and Theorem 4.2; Grove--Ziller 0801.0767v1 Proposition 1.8 and (1.10)--(1.11); Yoshioka math/0411538v2 Lemmas 1.2--1.4, 3.1, Definition 3.1, (3.3) and Proposition 3.6; inspected Huybrechts Chapter 9 Section 4.2, Remark 4.8(i), Theorem 4.9, pp. 181--182; Perego 1910.01867v1 Lemma 2.25 with full proof, Lemmas 2.32--2.34 and determinant discussion, pp. 18--24; Coelho's 2019 dissertation Lemmas 2.16--2.17 with full proofs and Theorem 2.13 proof, pp. 22--23,26.
COMPARISON: The known Chern, determinant and compact-Kähler correspondence inputs cover a separate audit at the unchanged real h; central-cover and twisted-index coverage is reusable. Neither curve factorization nor a projective holomorphic structure alone supplies the prescribed ordinary-lift Chern connection or exact-h stability.
GAP: Critically check L087's actual holomorphic parallel half-adjoints, shared sign cocycle and normalized tensor comparison, prescribed ordinary-lift metric and Chern connection, individual simplicity/indices and formal nonspin witnesses; no mathematical verification of these specializations is performed here.
REASON: Approve one bounded critical audit of the existing conditional calculation, using precise known inputs; local compatibility and cocycle identifications still need mathematical checking, while existence and common-kernel construction remain outside coverage.
SCOPE: L087 under conditional L079 K_4 at (-13,-14), full negative tensor, identical metric, actual compatible connection, integral c_1=0, c_2=8 and local freeness; L052 exact perpendicular lattice and L061 ordinary/twisted conventions. Audit only; no renewed index filter, existence, other image branches or transverse transport.
COVERED_TARGET: Critically audit L087's half-adjoint construction, common lifting cocycle, exact-h factor stability and nonspin survivor constraints.

## Completed source comparison

2026-10-11. This is a literature-only coverage approval, not the
critical mathematical audit. The universal gap is algebraicity of all
primitive rational (2,2)-classes; locally a common holomorphic F with
the prescribed full negative tensor remains missing. The intermediate
target is reliability of L087's conditional branch constraint. A
sound constraint could inform a later common-kernel construction or
exclusion; neither this review nor the constraint supplies that kernel.

LITERATURE_REASON: The new critical-audit target requires essential unread local Chern-connection and determinant passages beyond the reusable group/index assessment, to compare ordinary-lift compatibility at exact real h.

The [prior specialization assessment](2026-10-11-rank-four-orthogonal-spin-factor-constraints.md)
and [rank-three lifting assessment](2026-10-06-nonflat-rank-three-projective-lift.md)
already contain theorem-level lifting, characteristic and index
comparisons. Reuse them. L079's aggregate-index stop, L086's natural
projector stop and ATTEMPTS/056's half-adjoint stop are different
completed tests; their surviving cases must remain preserved. The
audit is a correctness check, not a renamed restart of any filter.

## Primary inputs and their exact limits

**Real metric and ordinary Chern connections.** Huybrechts,
*Lectures on K3 Surfaces*, author-hosted prepublication draft
(2015 work), [Chapter 9 Section 4.2, Definition 4.7,
Remark 4.8(i) and Theorem 4.9, printed pp. 181--182,
PDF pp. 181--182](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=181).
Read the complete Chern-connection and HE discussion through the
theorem. The correspondence applies to holomorphic vector bundles
on a compact Kähler manifold with its given Kähler form; no rational
or integral polarization is required. Remark 4.8(i) covers line-bundle
HE metrics. Theorem 4.9 identifies HE metrics with slope-polystability,
and the following definition specifies equal-slope stable summands.
This supports using the actual h for both lifts and their determinants.
It does not identify a prescribed projective connection with the
projectivization of a chosen lift's Chern connection. That is a local
compatibility obligation in the next audit, not an imported conclusion.

**Local connection operations.** Perego,
*Kobayashi--Hitchin corrispondence for twisted vector bundles*,
[1910.01867v1, 4 October 2019](https://arxiv.org/pdf/1910.01867v1),
Lemma 2.25 and its full proof, printed pp. 18--19; Lemmas 2.32--2.34
with tensor gluing and wedge/determinant discussion, pp. 22--24.
These inspect metric/holomorphic compatibility, Chern uniqueness,
curvature type and induced tensor, End, exterior and determinant
connections. Use the ordinary specialization (twist one and zero
B-field) for the ordinary lift. For sign-twisted local factors retain
their specified local cocycle; do not assume an arbitrary B-field
normalization. The already inspected published Propositions 3.9--3.12
and 3.15, pp. 36--38, remain covered in the
[orthogonal assessment](2026-10-05-flat-transform-orthogonal-residual.md).
The 119-page arXiv manuscript and 95-page publication have different
pagination; the new lemma citations refer to the manuscript only.
No twisted HE-existence theorem is needed to evaluate descending indices.

**Projective plus determinant lead, and its limitation.** Rui Coelho,
*Selected Topics in Complex Geometry*, LMU dissertation (2019),
[Chapter 2 Lemmas 2.16--2.17, pp. 22--23, and Theorem 2.13 proof,
p. 26](https://edoc.ub.uni-muenchen.de/24808/1/Coelho_Rui.pdf#page=22),
read complete indicated proofs. Lemma 2.17 assumes a projectively
holomorphic smooth vector bundle and a holomorphic determinant.
It constructs a projective connection compatible with the determinant
holomorphic structure by local frames and partition of unity. The
theorem's proof uses scalar (0,2) curvature and determinant trace to
obtain integrability. This is supplementary comparison: it neither
preserves an arbitrarily prescribed projective unitary connection nor
asserts compatibility with an already specified holomorphic lift or
an HE metric. Do not substitute it for L087's local Chern argument.
The related Coelho--Kotschick journal article (2021), DOI
10.1112/blms.12435, was an unread full-text lead; only its preview was
available. The inspected dissertation, not that preview, is the source.

**Group, two central covers and real Euler invariant.** Reuse
[Choe--Hitching 2203.06645v2](https://arxiv.org/pdf/2203.06645v2),
introduction p. 1 and Section 2.3 p. 5; rechecked the group table and
central-cover boundary statement. Theorem 4.2's complete proof was
previously inspected; its curve/isotropic-subbundle assumptions cannot
be used for K3 factorization. Reuse and rechecked
[Grove--Ziller 0801.0767v1](https://arxiv.org/pdf/0801.0767v1),
Proposition 1.8 with spin and nonspin proof cases, pp. 7--8, and
the coefficient exterior decomposition and (1.10)--(1.11), p. 8.
Its compact simply connected base hypothesis applies; no group action
is required by these passages. They cover associated real SO3 bundles,
their common obstruction and Pontryagin/Euler relations. They do not
prove holomorphic parallel descent or uniqueness of a holomorphic
normalized tensor: the audit must check those via the actual local
transitions, both central kernels and the stated H^1(S,mu_2) input.

**Twisted factors and separate indices.** Reuse and rechecked
[Yoshioka math/0411538v2](https://arxiv.org/pdf/math/0411538v2),
Section 1.1 and Lemmas 1.2--1.4 with proof, PDF p. 2;
Lemma 3.1 with proof, PDF p. 6; Definition 3.1 and (3.3),
PDF p. 7; Proposition 3.6 and its trace-obstruction
paragraph, PDF p. 8. The congruence concerns locally
free Y-sheaves; the Mukai pairing uses their descending derived Hom.
The dimension bound assumes simplicity, without a general-polarization
hypothesis. The analytic twisted-gluing/Y-sheaf equivalence is in
Section 1.1, (1.5). L087 must verify simplicity and the applicable
descending Hom on its actual factors before using these inputs.
L087's existing PDF-page references are retained: extracted page
footers at paragraph boundaries do not establish a numbering error.
No lemma is edited during this literature-only turn.

## Separate audit obligations and stopping test

Check the full L087 proof, not only displayed conclusions, with L079's
conditional input and L052/L061 conventions. Require coefficient star
to preserve the actual induced connection and holomorphic structure;
retain its real rank-four Euler class. Compare the actual Spin(4)
sign cocycle of both local SL2 factors, cancellation in the coefficient
representation and the central mu_2 ambiguity after ordinary determinant
normalization. For an ordinary lift check the projective metric and
determinant metric define a genuine global Hermitian metric, and that
the resulting local Chern connections glue and preserve its given
(0,1) operator. Simplicity and polystability must be established before
strict stability or the determinant-zero section bound is used.

Check the two separate descending End indices and every spin,
ordinary-nonspin and nonzero-Brauer case without assigning ordinary
Chern classes to twisted objects. Audit L087's formal witnesses and
congruences, retaining arbitrary determinants until a zero-slope test
is actually invoked. A missing connection/cocycle justification or
incorrect specialization requires a scoped correction or qualification;
if the proof survives, retain only its necessary constraints and stop
the exhausted filter. Neither outcome decides actual K_4 or F existence.

Queries: “projective determinant connection Hermitian Einstein lift
vector bundle”, “Perego Kobayashi Hitchin correspondence twisted vector
bundles arxiv”, and “Coelho Kotschick Lifts projective bundles applications
string manifolds arxiv”. The Perego repository retrieve and bitstream
URLs failed; arXiv supplied the missing local rules. The Coelho--Kotschick
publisher full-text URLs were forbidden; the author dissertation supplied
the specified weaker comparison. Direct shell retrieval lacked DNS, but
browser primary sources were accessible. No essential source blocker
remains for this bounded audit. No originality is inferred from searches.

Mathlib full matching coverage remains not checked; no absence claim.
No lemma, mathematical script, DAG or PROOF.md changed. This supplies
local source coverage only, with no progress beyond the known results
checked and no new Hodge class or complete candidate.

## Exact continuation and boundaries

The completed mathematical attempt is L087. Its canonical proof retains
L079's actual conditional stable K_4 and parallel real reduction, L052's
unchanged h and perpendicular lattice, and L061's lifting/index
conventions. The main universal primitive Hodge gap remains open;
common F existence, other L079 image branches and transverse transport
are independent. No cross-notebook input is needed.

The next turn is the separately approved mathematical critical audit,
using the exact obligations above. Verify the two central cocycles
and the mu_2 ambiguity in normalized ordinary tensor recovery.
Distinguish R's real Euler class from K's complex top Chern class.
Retain nonzero w and alpha and keep all compatible examples explicitly
formal. A later mathematical audit must check the complete proof and
its exact hypotheses, not merely the numerical preview.

L087 proves neither K_4 nor common-kernel existence and does not exclude
the nonspin branch. Do not restart the exhausted necessary-index filter
without a materially different test. Full Mathlib matching coverage has
not been checked; no absence claim is made.
