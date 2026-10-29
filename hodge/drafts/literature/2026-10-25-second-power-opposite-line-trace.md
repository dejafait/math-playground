# Second-power opposite line multiplicities — coverage review

TARGET: Test whether L160's W-retaining trace mechanism forces m_-2*m_2=0 for 0<=z<=119 using coefficients F tensor p_1^*L^{+/-1} tensor p_2^*L_B^{+/-2}.
CHECKED: 2026-10-25
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 529 compared L157 all-power and L158-L160 coefficient scopes, reused steps 511/521/523/525/527, and checked histories 52* and ATTEMPTS/089,/090; targeted external searches for hyperholomorphic opposite line powers and cohomology cup multiplicities found general machinery, with no inspected matching exclusion theorem.
SOURCE_EVIDENCE: Refreshed Verbitsky alg-geom/9307008v1 (29 July 1993), Section 4 setup pp. 12-13, Theorem 4.1 and Corollary 4.3 pp. 15-16, doubled-dual proof p. 17, https://arxiv.org/pdf/alg-geom/9307008v1; freshly checked Stacks 36.23.1 (0FLN), statement and both proofs, https://stacks.math.columbia.edu/tag/0FLN; accessed 2026-10-25; reuse the precise derived, Demailly and BBHR read registers below.
COMPARISON: General sources allow locally free hyperholomorphic coefficients and their duals, arbitrary line-valued Kunneth, and derived projection/base-change with W retained; L157 covers all nonzero integral opposite powers. Neither these sources nor L160 state the second-power exclusion or its four actual strict trace comparisons.
GAP: A separate proof attempt must identify all four actual degree-one edges and full m_-2,m_2 multiplicities, justify both strict normalized trace signs, and check every changed adjacent cup target and polarized quartic sign, retaining W and delta throughout.
REASON: Essential general source coverage is adequate for the exact bounded second-power test under SPECIALIZE; only its data-specific applicability and contradiction remain to prove, with no matching conclusion imported or essential source blocker identified.

The following is the retained invocation-start proposal, superseded as to
coverage by the completed comparison below. It was not a source approval, second research
attempt or claim of novelty. Preserve the exact target while assessing
it. Reuse the inspected theorem cases in the first-power assessments
where their hypotheses continue to apply; do not repeat broad discovery
without a specific gap. A failed local duplicate search is not evidence
that the statement is absent from the literature.

The main gap remains universal primitive rational Hodge realization.
The proposed intermediate restriction could narrow the remaining actual
line spectrum of M beyond the first-power result. It does not promise
an improved bound on z or exclusion of all possible kernels. L157's
higher-power additive compatibility and ATTEMPTS/089,/090 remain
recorded limits; do not rerun their finite tests or select free cup maps.

Essential proposed inputs are L071's actual connection, L147's ordinary
M and W, L157's full multiplicities and opposite H_2,H_-2, L158's
coefficient-product method, L159's operator/raw-trace calculation and
audited L160's forward edge. Retain the identical marked K3 factors,
common g,h and ordered triple, preferred dual line connections,
k=(-4,-2,1,2), k.h=0, k^2=-14 eta with integral eta=1, and hypothetical
locally free Omega-polystable rank-two F with integral c_1=0 and
ch=2-14e_1-21e_2-tau_D+62P. Retain 0<=z<=119, W the ordinary sum
of residue fields on Z, and its unevaluated connecting map delta.
F existence, other stable types, lower control on z and transport
remain unresolved. No cross-notebook input is proposed.

The continuation test is whether the precise four coefficients have
the needed degree-one detection and two strict signs, and whether
their actual adjacent targets permit the same quartic contradiction.
If those obligations have adequate sources, approve only that bounded
test; if a bridge fails, identify it and park this extension. If the
restriction is already supplied by an inspected stronger theorem,
import it with its exact applicability instead. None of these verdicts
is reached in the present proposal.

## Completed source comparison — step 529

LITERATURE / EXPLORATION / REPRODUCTION; actual task literature_comparison.
This changes coverage for the exact TARGET, not any mathematical conclusion.
LITERATURE_REASON: The new second-power coefficients were REVIEW_REQUIRED;
compare their scope once, reusing the ready first-power and all-power sources.
No lemma, mathematical script, PROOF.md or DAG.md is changed. Mathematical
exploration usage remains one since step 526; this review spends none.

**Precise reusable scope.** The assessments
[all-power transforms](2026-10-24-double-line-twist-summand-spectrum.md),
[harmonic operator](2026-10-24-dual-coefficient-quaternionic-trace-sign.md),
[operator audit](2026-10-24-dual-coefficient-trace-sign-critical-audit.md),
[positive-z comparison](2026-10-24-positive-z-opposite-coefficient-trace-obstruction.md)
and [positive-z audit](2026-10-24-positive-z-trace-critical-audit.md)
provide the existing primary read registers. L157's canonical statement
already quantifies over every nonzero integral r, including r=2,-2;
its opposite concentration, negative forward comparison and full signed
multiplicities can be used within their hypotheses. L158 and L159 remain
first-power, z=0 statements; only their indicated coefficient-product
method and actual operator construction are candidate methods here.
L160's conclusion remains first-power at arbitrary allowed z. It supplies
the established W-retaining dual-truncation framework, not the desired
second-power exclusion. No broad general theorem requires reproof.

**Primary harmonic comparison.** Refreshed Verbitsky's preprint Section 4
setup, Laplacian proof, Corollary 4.3 proof and doubled-dual case at the
locations in SOURCE_EVIDENCE. The coefficient is hyperholomorphic with a
parallel real structure; the doubled-dual construction handles a general
coefficient. These hypotheses do not bound line exponents or require
projection IT. The proposed coefficients use the same actual connections
and dual tensor powers already treated in L157. The extracted opposite
map and strict traces still require a specialization check; they are not
stated by the source. Neither the printed endpoint-injection assertion
nor its scalar cohomology-ring display is an input.

Reuse Demailly, *L2 vanishing theorems for positive line bundles and
adjunction theory*, alg-geom/9410022v3, 28 February 1995, Sections 1.A
pp. 4-5 and 4.A (4.3)-(4.4') pp. 27-28
([primary version](https://arxiv.org/pdf/alg-geom/9410022v3)). Its locally
free coefficient Dolbeault/Serre-integral scope does not distinguish
first from second line powers. It does not supply restriction harmonicity
or strictness. Reuse the raw-restriction method, not such an extra claim.

**Changed product targets.** Stacks Lemma 36.23.1 (0FLN) assumes
quasi-compact, quasi-separated factor maps and Tor-independence over the
base; the global version also requires an affine base. The projective
K3 factors over Spec(C) meet these assumptions, and the proposed tensor
powers are locally free, hence quasi-coherent inputs. Read both displayed
proofs, including the affine K-flat case and open-cover induction; the
first proof's omitted compatibility verification remains omitted. This
covers the changed line-valued cup targets. Their actual degree-two
vanishings and the resulting quartic contradiction remain mathematical
checks for the next turn, not conclusions of this review.

**Derived and transform support reused.** Stacks 20.54.2-3 (01E6),
20.13.4 (01F2), 36.30.1 (0A1H), 36.31.3 (0BDK), and 48.15.7 (0BRT)
retain the scopes recorded in steps 511/525/527: finite locally free
base tensors, bounded-below Leray, proper perfect pushforward/base change,
open concentration, and smooth-proper relative duality of dimension two.
The smooth projective projections and locally free coefficients retain
these hypotheses; take O_X as the separate perfect input in 0A1H.
The general cup/counit/trace register is 20.31.3/7/8
(0FP3/0FP6/0H99), 48.12.4 (0AAB), and 48.7.1 (0B6J).
The previously omitted proof of 0H99 is not newly claimed as read.
No source permits erasing W, evaluating delta, or assuming ordinary
base change at Z. BBHR, *A hyperkahler Fourier transform*, DGA 8 (1998),
239-249, Definition 2 p. 244 and Section 3.3 Lemmas 1-2/Theorem 3
pp. 245-246, is reused through L157's already proved all-power scope,
not newly applied to a forward coefficient that lacks IT.

**Search and failures.** New queries were `hyperholomorphic bundle
opposite line powers cohomology cup product multiplicity K3` and
`"hyperholomorphic" "tensor" "Theorem 4.1"`. They did not yield an
inspected matching multiplicity theorem. Search-only leads about motives,
moduli and homogeneous-space cup products are not inputs; their theorem
contents were not inspected for this target. The local scoped search of
October 24 assessments, histories 52* and ATTEMPTS/089,/090 found no
second-power trace proof. This supports no originality claim. The
additive compatibility stop and the freely assigned cup relaxation
remain valid limits; the proposed actual-connection test uses a different
constraint and does not reopen their exhausted finite calculations.

**Approved test, not proved result.** Approve exactly TARGET under
SPECIALIZE for a later bounded REPRODUCTION attempt. Retain all essential
inputs and unresolved assumptions listed in the proposal above. Check
full multiplicities through L157; then the W-retaining actual edges,
nonzero fibre detection in both directions, the two strict traces with
one determinant normalization, all adjacent targets and quartic signs.
Continue only if these bridges justify the exact exclusion or identify
a specific informative failure. If a bridge fails, record it and park
this extension rather than assign maps or invoke positive IT. No improved
bound on z, F existence, other-type exclusion, lower comparison, transport
or primitive Hodge realization is claimed. Full matching Mathlib coverage
is not checked, not absent. No cross-notebook input is used.

This newly completed assessment awaits the supervisor's separate approval
before its mathematical invocation. The source-review outcome itself is
complete; no second research attempt occurred during this turn.
