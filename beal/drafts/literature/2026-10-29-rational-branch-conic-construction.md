# Rational-branch conic: constructive-method source gate

TARGET: Attempt a bounded positive-certificate search for a nonzero-coordinate K-point on L150's eta_class rational-branch conic using at most 5000 prescribed v-tuples and exact substitution replay.
CHECKED: 2026-10-29
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Compared official Sage/PARI/Magma number-field conic methods, Voight and the ready Trager/local square-proposal coverage; queries included Voight Identifying matrix ring algorithms quaternion conic number field Algorithm 6.6, Magma conic number field HasRationalPoint algorithm Simon norm equation, site.pari.math.u-bordeaux.fr rnfisnorminit rnfisnorm cyclic flag norm equations, and Denis Simon Solving norm equations relative number fields S units 2002 pdf; inspected ATTEMPTS/045,052,065,066 only for the specific backend/route distinctions.
SOURCE_EVIDENCE: Direct primary source https://raw.githubusercontent.com/sagemath/sage/develop/src/sage/schemes/plane_conics/con_number_field.py fetched 2026-10-29, has_rational_point lines 58–96 and 259–305 rechecked for square cases, transport and norm delegation; reuse Trager (1976), Section 2, Theorem 2.2, pp.219–220, https://www.cecm.sfu.ca/~mmonagan/teaching/TopicsinCA11/TragerFactor.pdf and the prior inspected PARI/Magma/Voight evidence in drafts/2026-10-29-rational-branch-conic-method-review.md. No complete factorization or negative decision is imported.
COMPARISON: Known complete solvers have additional execution prerequisites and no inspected sufficient runtime/height cap for this instance. A bounded positive-only conic search can instead reuse L148/L149's available standard-library square-root proposals and exact field verification, without complete factorization, units or class groups; this is routine known-method specialization, with no claim that the fixed domain contains a point.
GAP: Explicit coordinates are still absent. Approve only the covered finite positive-certificate experiment and independent exact replay; no complete conic solver, nonsquare conclusion from proposal failure, guaranteed construction or insolubility claim is covered.
REASON: Essential coverage remains adequate for the unchanged capped positive-output attempt. This separate source-gate recovery supplies direct primary URLs and exact TARGET matching; complete norm solving remains parked and no calculation runs here.
LITERATURE_REASON: Supervisor recovery explicitly requires direct source URLs in the ready assessment; repair that process defect without expanding the mathematical scope.
SCOPE: L150's mask 132102 rational-branch K-conic only, at most 5000 prescribed v-tuples, 80000 sign-pattern proposals, fixed precision/reconstruction/bit caps and exact nonzero-coordinate substitution; no box enlargement, backend installation, local retest, M-point construction or pairing.
COVERED_TARGET: Attempt a bounded positive-certificate search for a nonzero-coordinate K-point on L150's eta_class rational-branch conic using at most 5000 prescribed v-tuples and exact substitution replay.

## Exact intended instance and bounded review

Use L138's actual K=Q(alpha), A(alpha)=0, and eta=−907500/(alpha−50).
Use L150's full eta_class representative, mask 132102, without scalar
quotient. The equation is

    b*u^2−q*v^2+(eta−9075)=0,
    q=1/26730000000000,
    b=41236+(356216/25)alpha+(397568/625)alpha^2+(4612/625)alpha^3.

The completed comparison is in
`drafts/2026-10-29-rational-branch-conic-method-review.md`. No implementation,
mathematical derivation, point search or local retest ran in this source
gate. Complete norm solving has no verified executable backend or
sufficient instance resource bound and remains parked. Its source lead
in Simon (2002) was inaccessible; it is not essential to the selected
positive-only method.

The covered experiment chooses

    v=(a0+a1*alpha+a2*beta+a3*gamma)/d,
    ai in {-2,-1,0,1,2}, d in {1,2,3,5,6,10,15,30}, v!=0,

using L149's actual basis beta=(alpha^2+14*alpha+25)/50 and
gamma=(alpha^3+239*alpha^2+4475*alpha+19375)/18750. At most 5000 tuples
(before deduplication) and 16 sign proposals per tuple are permitted.
Use the existing L148/L149 square-root proposal method on
`(q*v^2+9075-eta)/b`: cache four real-root proposals with at most 450
refinements each, Decimal precision 200, rational reconstruction
denominator bound 10^12 and exact rational numerator/denominator bit cap
8192. These bounds ensure finite work; none is asserted sufficient for
finding a point. No complete Trager factorization or negative square
decision is required or approved.

Accept only exact nonzero power-basis u,v with zero remainder of
`b*u^2-q*v^2+eta-9075` modulo A, independently replayed in the actual
maximal-order basis. Bind the full representative and accepted source
certificates, save full evidence on disk and print only counts, caps,
failures and paths. Numerical proposals, their failures and a completed
finite scan are not a proof of nonsquareness or conic insolubility.
Stop at the first exactly replayed point or the fixed caps/domain end.
On no accepted point, preserve unfinished work and park this experiment;
do not enlarge its box or precision without materially new input.

Essential inputs: L135/L138/L145/L147/L149/L150/L151/L152 and the four
complete conic certificate families. L150/L152's conceptual acceptance
and existential goodness are now established; explicit K/M points and
checked coordinate transport are not. A K-point is only one useful
component for later constructive pairing work. The quartic-pair M-point,
cochains, pairing-place support, local halves, mutual pairing, rational
Kummer membership, generation, point control, marked/integer recovery
and other signatures remain unresolved. No cross-notebook input.

This is known-method constructive development, not a protected creative
mechanism. No source-ready new central mechanism was identified in this
focused comparison; do not relabel coordinate extraction as creative to
meet a cadence. ATTEMPTS/065's different raw rational cover box and
ATTEMPTS/066's epsilon pairing remain stopped. The finite K-conic
experiment is independent of the persistent class-backend prerequisite.

## Separate source-gate recovery, 2026-10-29

The preceding turn's evidence and fixed experiment are preserved. This
review puts direct primary URLs in SOURCE_EVIDENCE and aligns TARGET
verbatim with the already covered continuation. Sage's develop source
was retrieved and its actual square and norm branches read, including
the prohibition on requesting a point from the local algorithm. This
confirms the prior method distinction; it supplies no new instance result.

The Trager PDF opened at printed p.219; a subsequent targeted text fetch
timed out. Reuse the earlier recorded pp.219–220 theorem/proof inspection,
not that partial new fetch, for the complete-factorization comparison.
That algorithm is outside the selected positive-only experiment anyway.
No source blocker affects exact positive substitution verification.

Decision remains SPECIALIZE, classification of a later execution remains
REPRODUCTION. This is a process repair, not an advance or a renewed
exploration budget. No mathematical script, lemma or conic search changed.
Mathlib coverage remains unchecked. The exact original caps, replay
requirements, independent gaps and abandonment test above still apply.
