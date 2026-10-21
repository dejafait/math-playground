# Actual split harmonic metric bounds — proposed critical audit

TARGET: Critically audit L112's natural spectral comparison and uniform two-sided bounds for the actual harmonic L2 metric at split parameters.
CHECKED: 2026-10-16
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the unchanged estimate assessment and its discovery/overlap search; searched L112/L111 comparison citations and read ATTEMPTS/063/066/067 plus history/318; directly inspected BGS III pp. 304--305 and 342--345 and Stacks 064B for the new audit scope.
SOURCE_EVIDENCE: Bismut--Gillet--Soulé III, Comm. Math. Phys. 115 (1988), DOI 10.1007/BF01466774, section 1(b)--(c), pp. 304--305, Theorem 3.5 and full proof including Lemmas 3.6--3.8, pp. 342--345; Stacks Lemma 13.19.8, tag 064B, statement inspected 2026-10-16.
COMPARISON: These sources cover the natural relative-Dolbeault and finite spectral comparisons and stalkwise projective chain representatives; they do not certify L112's actual-frame compatibility or norm inequalities. The unchanged estimate assessment supplies adequate discovery and metric-theorem screening.
GAP: The later mathematical audit must check L112's specified derived identification, smooth central chain map, minimal fibre dimensions, given-metric quotient identity and both uniform bounds; no essential additional source is currently identified.
REASON: Approve the exact critical audit as a REPRODUCTION specialization of the existing tools; approval is separate from execution and does not certify L112 or invalidate its completed attempt.

The completed proof attempt is canonical in L112. It used the unchanged
`drafts/literature/2026-10-16-split-harmonic-metric-two-sided-bounds.md`
assessment, which remains SPECIALIZE and is not changed here. This assessment does not perform the critical audit or claim a new
mathematical input. Primary references and full source qualifications remain in
that reusable assessment and in the canonical proof; no unread lead
is a premise.

The concrete audit should test whether the chosen comparison represents
the natural ordinary higher-image frame and remains a smooth chain map
at the central jump. It must verify that central residual isomorphisms
give degreewise invertibility on a neighborhood, and that the finite
quotient norm is the metric of the given smooth coefficient family.
Both inequalities must cover one full punctured ball with fixed
positive finite constants. The shrinking boundary vector may not be
normalized using an unproved bounded inverse.

Essential mathematical inputs are L112 and audited L111, retaining
corrected L108 and L110, L094/L095 and L071 through the latter.
The hypothetical F, full negative tensor and identical common metric
remain fixed. Z is finite and may be empty. No ordinary split base
change, uniform harmonic projection, metric extension, curvature
integrability, semistability or bound on |Z| may be assumed.

A later audit continues only if the actual comparison and both bounds
survive; a specific mismatch requires repair or downgrade of L112.
Even a successful audit would leave extension, curvature, semistability,
cardinality, kernel existence, transport and universal primitive rational
Hodge realization unresolved. Full matching Mathlib coverage is not checked.

## Separate scope approval, 2026-10-16

LITERATURE_REASON: The supervisor requires separate approval of the newly saved audit target; this review tests chain-map and derived-fibre scope using ready coverage, without repeating broad discovery or invoking another metric theorem.
SCOPE: Exactly TARGET for hypothetical F with the unchanged full negative tensor and common smooth metric, L111's actual minimal complex, finite possibly empty Z and the ordinary stable-open higher-image metric.

This is a literature-only scope approval. It adds no theorem or estimate,
and does not re-audit L111. The completed step is STALLED in the shared
outcome vocabulary: it supplies a ready, actionable audit assessment but
no new mathematical evidence or newly necessary source input. Classification
is NOVELTY_UNCHECKED; the later approved proof audit is REPRODUCTION.

**Primary scope comparison.** Theorem 3.5 identifies smooth scalar
extension of ordinary higher images with relative Dolbeault cohomology
for a smooth proper holomorphic map and holomorphic bundle. Its proof
constructs a finite holomorphic representative and natural smooth map;
Lemma 3.7 checks the derived fibre and Lemma 3.8 contracts the high
spectral complement. Section 1(b)--(c) supplies smooth cutoff bundles,
metrics and projections. Read the complete proof cases on pp. 342--345,
not just the determinant corollary. The product projection with coefficient
End_0(F) and its given smooth metrics meets these hypotheses; no constant
cohomology rank or coefficient positivity is added. These are reusable
tools, not a source theorem asserting L112's bounds. See the
[primary scan](https://www.imo.universite-paris-saclay.fr/~jean-michel.bismut/Bismut/1988b.pdf#page=42).

[Stacks 064B](https://stacks.math.columbia.edu/tag/064B) identifies homotopy-
and derived-category morphisms from bounded-above projective complexes
in an abelian category. Its intended use here is in modules over the
analytic local ring, with finite free source. It does not declare analytic
locally free sheaves projective objects globally. The audit must check
stalkwise representatives and the finite spreading argument explicitly;
it must also distinguish the holomorphic total Dolbeault complex from
the relative smooth complex used after scalar extension. A derived
isomorphism without the specified natural identification is insufficient.
No new specialization of this theorem is proved in this review.

**Duplicate and failure comparison.** The estimate assessment already
screens the stronger-looking Mourougane--Takayama theorem: its coefficient
positivity and its metric do not match. That rejection is reused, without
new browsing. L112 is the existing proposed estimate; another lemma would
be a duplicate. ATTEMPTS/063, /066 and /067 remain preserved: neither a
singular-quotient metric identification, automatic surface metric extension,
nor a duality-only numerical bound is approved here. The actual Koszul
splitting is the distinguishing retained input. No broader route reopens.

**One later audit and its stopping test.** Trace the actual frame through
the chain maps; check zero central differentials and all 52 derived middle
classes before testing invertibility. Then inspect the exact quotient
metric and constants on a full punctured ball, including both axes.
Continue only if both fixed bounds 0<c<=C<infinity survive for the given
metric. A precise failure requires repair or downgrade in canonical L112;
no surrogate metric or shrinking directionwise bound is acceptable.
This is an audit specification, not its mathematical execution.

The downstream use remains a prerequisite for later analytic extension
work on the normal summand. Curvature, connection/metric extension,
semistability, |Z|, existence of F, transport and universal primitive
rational Hodge realization remain independent gaps. No new source access
blocker remains. Full matching Mathlib coverage is not checked. No new
lemma, mathematical script, DAG edge or PROOF.md change is warranted.
