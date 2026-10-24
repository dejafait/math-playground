# Twisted ordinary middle image — proposed harmonic metric bounds

TARGET: Test uniform two-sided bounds for the actual harmonic L2 metric of F tensor p_1^*L^{-1} in a holomorphic frame of L147's rank-24 middle image near each split parameter.
CHECKED: 2026-10-23
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused October 16 elliptic-family/L2-metric discovery and stronger-theorem screening; read L112's comparison proof, L146's actual splitting and audit, L147's scope, October 12 twist/index assessments and ATTEMPTS/060/063/066/067; bounded changed-coefficient searches found no inspected matching norm theorem.
SOURCE_EVIDENCE: Reused inspected Bismut--Gillet--Soule III (1988), Section 1(b)-(c), pp. 304-305, Theorem 3.5 and full proof through Lemmas 3.6-3.8, pp. 342-345, and p. 350 Hodge decomposition; directly reread primary assumptions and spectral-bundle setup, pp. 302-304, and Stacks Lemma 13.19.8 (064B) statement on 2026-10-23.
COMPARISON: BGS covers an arbitrary smooth holomorphic Hermitian coefficient, hence also the fixed twist G; it requires neither scalar self-duality nor constant cohomology. L146 supplies the actual rank-(1,26,1) Koszul splitting, replacing L112's rank-(1,52,1) input, but neither BGS nor L112 states this twisted norm estimate.
GAP: Match L146's actual ordinary rank-24 frame with the natural Dolbeault/spectral comparison and prove both direction-independent quotient-norm bounds through the endpoint jump; no estimate is established in this review.
REASON: Separate changed-coefficient source approval is complete; approve exactly TARGET as one later REPRODUCTION specialization of ready tools, retaining the actual metric and all higher coefficients. No source reproof, automatic extension or index effectivity is justified.
LITERATURE_REASON: The saved target changed End_0(F) to F tensor p_1^*L^{-1}; essential coverage required checking the coefficient, natural comparison and lack of scalar self-duality before dependent mathematics.
SCOPE: Hypothetical L071 equality F on the identical marked K3 product/common metric, integral c_1=0, ch_2=-14e_1-21e_2-tau_D, fixed k=(-4,-2,1,2), G=F tensor p_1^*L^{-1}, and L096's finite possibly empty split set; no positivity, scalar self-duality or metric extension is assumed.

The original proposal is retained below as the specification of the
mathematical test. Separate source approval is recorded afterward; no
new norm calculation, lemma or metric theorem is claimed. The main gap is
universal primitive Hodge realization; the intermediate target is one
bounded analytic prerequisite for later curvature and extension work
on the actual twisted image. Those later steps, polystability, any
cardinality constraint, F and split-locus existence, reconstruction
and transport remain independent unresolved obligations.

Essential starting inputs are audited L145/L146's actual algebraic
complex and free ordinary middle stalk, audited L147's global image,
L071's smooth compatible coefficient connection, L094's split line
cohomology and L096's isolated parameter set. The actual source metric
and a smooth Hermitian metric on the fixed line coefficient define the
fibrewise harmonic norm. Its compatibility with the natural ordinary
higher-image identification is part of the proposed test. L112 and
its source assessment are comparison material, not a theorem already
covering this changed coefficient. Only their statements and assessment
scope were checked in step 471; their detailed proof and primary
source proof cases should be read narrowly in the separate comparison.

The required threshold is one holomorphic frame near each selected
split parameter and constants 0<c<=C<infinity bounding the actual norm
above and below by the Euclidean coefficient norm on a full punctured
ball, uniformly in every approach direction. Continue if the natural
spectral comparison and quotient estimates supply these constants.
Abandon this specific bounded-metric mechanism if an actual degeneration
prevents such a comparison or either uniform bound; do not replace the
given metric with an unrelated one or infer failure of F existence.
Z empty makes this local statement vacuous, not a contradiction.

Reuse the exact BGS discovery and proof-case coverage where applicable;
check whether its hypotheses depend on scalar self-duality or only on
smooth proper holomorphic coefficients. Inspect the actual-complex
comparison before any matrix estimate. Do not assume the rank-50
Serre or Hermitian complement from L111/L112 for this rank-24 image.
The October 12 IT failure and automatic-effectivity stop remain: no
whole-base odd IT or global generation is supplied. Boundedness alone
would still give neither bounded curvature nor smooth extension.

Full matching Mathlib coverage is not checked. No cross-notebook input
is proposed. The proposal was REVIEW_REQUIRED at invocation start;
the separate review below discharges that gate without performing the
mathematical attempt or changing the completed L147 audit.

## Separate changed-coefficient source approval, 2026-10-23

This completed LITERATURE step approves exactly TARGET. Its local
advance is filling the essential source scope for a changed coefficient,
not an estimate or progress beyond the inspected literature. Classification
is NOVELTY_UNCHECKED for this source review; the approved mathematical
attempt is REPRODUCTION. No lemma, mathematical script, DAG or argument
overview changes are needed.

**Primary input and reuse boundary.** The precise analytic citation is
Bismut, Gillet and Soulé, *Analytic torsion and holomorphic determinant
bundles III. Quillen metrics on holomorphic determinants*, Comm. Math.
Phys. 115 (1988), 301-351, DOI 10.1007/BF01466774. Reuse the complete
Theorem 3.5/Lemmas 3.6-3.8 proof-case assessment in
`drafts/literature/2026-10-16-split-harmonic-metric-two-sided-bounds.md`
and its comparison-scope supplement
`drafts/literature/2026-10-16-split-harmonic-metric-bounds-critical-audit.md`.
These record the natural smooth relative-Dolbeault comparison, central
derived-fibre comparison and contraction of the high spectral complement.
Their supporting hypotheses and proof cases are unchanged; no fresh
reading of the full paper is needed solely because the bundle changes.

Directly retrieved the primary assumptions and finite spectral-bundle
setup on printed pp. 302-304 in the
[author scan](https://www.imo.universite-paris-saclay.fr/~bismut/Bismut/1988b.pdf).
They allow a holomorphic Hermitian vector bundle and smoothly varying
fibre Kähler metrics. The product projection is smooth proper holomorphic,
and the given metric on F tensored with a fixed smooth Hermitian metric
on L^{-1} is smooth and positive across the split parameter. This is a
coefficient-scope check, not a choice of new fibrewise HE metrics.
Neither a scalar bilinear self-pairing nor coefficient positivity occurs
in this reduction. The central ordinary and derived fibres must remain
distinct. The source supplies no stated two-sided bound for the actual
ordinary frame.

The original long author URL timed out. The short ~bismut URL returned
the assumptions and spectral setup; subsequent attempts to reload the
later theorem pages and screenshots mostly timed out. They do not count
as fresh inspections of the complete proof. The later proof coverage
above is explicitly reused from the saved October 16 assessment, rather
than inferred from an abstract or a search snippet. Local curl failed
DNS, and Springer's landing page offered only a preview. No essential
unread result is needed for this unchanged general reduction, and no
source-access recovery route is opened.

Also directly read [Stacks Lemma 13.19.8, tag 064B](https://stacks.math.columbia.edu/tag/064B):
maps from a bounded-above projective complex in the homotopy and derived
categories agree. Here the intended category is modules over the analytic
local ring, with finite free source; this is not a claim of global
projectivity of locally free analytic sheaves. The later attempt must
retain the specified derived identification and justify spreading its
finitely many comparison and homotopy identities to one neighborhood.

**What changes, and what cannot be imported.** L112's proof uses scalar
self-duality only through the earlier construction of its own algebraic
Koszul summand. That is comparison material, not a theorem about G.
For G the replacement input is audited L146's actual full splitting,
equations (9)-(12), and its natural identification of the degree-one
free complement with the ordinary middle stalk. Its independent trace
and unit test is already recorded there; this review does not reproduce
or strengthen it. L145 supplies the actual perfect representative and
endpoint jump, and L147 supplies the global rank-24 sheaf. Analytification
must preserve these specified maps and all coefficients. Replacing ranks
alone, or importing the rank-50 Serre/Hermitian complement, is insufficient.

The remaining finite-dimensional harmonic-quotient step needs a positive
Hermitian inner product, not a scalar Serre form on G with itself. It is
therefore within the inspected analytic toolkit. Nonetheless, the actual
smooth comparison, its central derived-fibre invertibility and the metric
identification are proof obligations for the next attempt. This paragraph
assesses their source scope; it does not construct those maps or establish
their estimates. Boundedness of a jumping harmonic projection and a
uniform inverse for its small nonzero eigenvalues are not approved inputs.

**Duplicates, stronger results and failures.** L112 already treats the
adjoint coefficient, so its general comparison machinery should be reused
rather than reproved; the precise changed-coefficient conclusion is not
one of its statements. Reuse the October 16 rejection of Mourougane--Takayama,
*Hodge metrics and the curvature of higher direct images* (2008), Theorem
1.1 and the pp. 1-2 metric distinction: no Nakano semipositivity of G is
given, and that Hodge metric is not automatically the requested metric.
No new claims from that paper's unread proof are used. The October 12
line-twist and index assessments still block whole-base odd IT and
automatic jumping-cycle effectivity. ATTEMPTS/060's strict-Euler stop,
/063's missing singular-quotient metric bridge, /066's automatic surface
extension failure and /067's duality-only bound failure remain intact.
The actual new algebraic splitting and direct elliptic comparison make
this a distinct, independently testable prerequisite, not a repeated
automatic-extension inference.

Bounded external queries included “Bismut Gillet Soule 3.5 smooth 1988
III”, “harmonic metric cohomology jump bounded higher direct images L2”,
the exact BGS III title and DOI, and primary-author URL variants. The
unchanged October 16 discovery covers standard small-eigenvalue reduction
and the stronger metric-theorem comparison. New search hits on singular
fibrations, analytic torsion and flat local systems were not inspected
as candidate matching theorems and supply no premise. A failed search
does not establish novelty or exhaustive absence.

**Approved next test.** Use L071, L094, L095, L096, L145, audited L146
and audited L147 with the hypothetical F, fixed k, common metric and
possibly empty Z unchanged. Match the actual rank-(1,26,1) complex to the
finite spectral complex before passing to its ordinary rank-24 frame.
Then test the actual harmonic quotient norm for constants 0<c<=C<infinity
on a full punctured ball, retaining both axes and every approach direction.
A natural-comparison mismatch or failure of either bound stops this
mechanism; neither a surrogate metric nor directionwise estimates meet
the target. This is exactly the saved mathematical action, not a new
continuation requiring another discovery round.

Even success supplies no bounded curvature, metric limit, connection
extension, polystability, cardinality bound, F or split-locus existence,
reconstruction, transport or universal primitive Hodge realization.
Z empty makes the local assertion vacuous. Full matching Mathlib
coverage remains not checked; no absence claim or cross-notebook input
is made. Import the cited general tools without reproof, and derive only
the stated actual-frame specialization in the later mathematical turn.
