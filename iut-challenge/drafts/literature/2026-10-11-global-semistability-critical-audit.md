# Everywhere-semistability application — critical-audit source coverage

TARGET: Critically audit L049's everywhere-semistability application and same-curve 3-adic packet retention.
CHECKED: 2026-10-11
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the ready global-semistability-after-torsion-adjunction and L045 audit assessments; searched the active literature, foundations, histories and ATTEMPTS for Raynaud, Theorem 3.5 and L049; compared the entire written L049 with the source scope and read the relevant L045/L048 input statements and retention passages. No new general search was needed.
SOURCE_EVIDENCE: Reinspected Silverberg–Zarhin (1995), Definition 3.1 p.405 and full Theorem 3.5 including its exceptional n=2 case and proof citation p.406; Milne Elliptic Curves second edition (2021), II.6.3 pp.70–71, including its characteristic-zero proof case. Reused L045's completion-source coverage and audited L048; precise links and qualifications below.
COMPARISON: The inspected criterion and geometric torsion theorem cover the exact audit obligations at levels 5 away from residue characteristic 5 and 6 at 5; the difference to check is L049's application at each completion and logical retention of the unchanged curve and fields, not a new reduction theorem.
GAP: Essential source coverage is ready for the saved independent audit; its mathematical verdict remains deferred. Selected field-of-moduli model conditions, other-place parameter orders, sufficient initial data and original finite B>=A remain unresolved.
REASON: This separate review supplies the missing audit-specific comparison while reusing adequate construction coverage; it authorizes only verification of the written specialization and any precise correction or narrowing within that scope.
SCOPE: Exactly TARGET, with direct local inputs L045 and audited L048; verify every finite completion, complete geometric torsion, the identity unramified extension, semistability rather than splitness, and same-curve retention. No new curve, field or stronger conclusion is approved.

LITERATURE_REASON: The newly selected audit was REVIEW_REQUIRED; this turn compares its written scope with ready primary coverage and checks the two load-bearing statements, without repeating discovery on the already approved construction target.

## Inspected source statements and relevance

The ready construction assessment is
`drafts/literature/2026-10-11-global-semistability-after-torsion-adjunction.md`.
Its literature search already located the exact full-torsion theorem,
stronger subgroup variants and original reference. No novelty or need
for a reproof follows from this audit target.

Reopened [Silverberg–Zarhin, Ann. Inst. Fourier 45(2) (1995),
403–420](https://www.numdam.org/article/AIF_1995__45_2_403_0.pdf),
Definition 3.1, printed p.405, and Theorem 3.5 with its proof reference,
printed p.406 (PDF pages 3 and 4, zero-based). The theorem assumes an
abelian variety over a discretely valued field, a torsion level prime
to the residue characteristic, and all level-n points defined over
an unramified extension. Its n>=3 branch gives semistability at that
valuation. The extraction prints the bound as n>3; both proposed
levels are strictly greater than 3, so even that reading covers the
entire application. The separate n=2 branch has henselian and
separably closed residue hypotheses and a different conclusion;
it is unused. Definition 3.1 concerns an extension of an abelian
variety by an affine torus, without a splitness condition.

The theorem cites Grothendieck, SGA7 I, LNM 288 (1972), Expose IX,
Proposition 4.7. The prior assessment records failed access to the
original scan and distinguishes the supplemental transcription.
No new original-scan inspection is claimed. The accessible published
full statement suffices for this audit; that historical access
failure is not an essential blocker. The paper's weaker isotropic
subgroup theorem and Neron–Ogg–Shafarevich good-reduction criterion
are not substituted for Theorem 3.5.

Reopened [Milne, Elliptic Curves, second edition (2021)](https://www.jmilne.org/math/Books/EC2.pdf),
II, Proposition 6.3, printed pp.70–71 (PDF pages 74–75,
zero-based). It gives geometric m-torsion free of rank two over
Z/mZ when m is prime to field characteristic. Read its complex
lattice proof and explicit characteristic-zero transfer, the case
used here; the characteristic-p lifting case is independent of
this application. Thus the source covers both algebraic closures
in L049's completion argument, including completions of residue
characteristic 2, 3 or 5. Field characteristic must remain distinct
from residue characteristic. The later audit must check the actual
base-change injection and that its use concerns one equation.

The reused assessment
`drafts/literature/2026-10-11-global-torsion-adjunction-critical-audit.md`
covers L045's embedded completion input, using Milne, Algebraic
Number Theory v3.08 (2020-07-19), section 8 before Proposition 8.1,
pp.135–136. No fresh completion construction or local field
identification is needed for L049. L048's audited statement already
retains the same reselected E_0, F, H, N and absolute Tate-parameter
valuation; the next audit checks retention without redoing those
independent proofs.

## Approved bounded review scope

Essential local inputs are L045 and audited L048, retaining L044–L047
and L042 through them. Check full geometric torsion after every
completion, the two exhaustive residue-characteristic cases, the
identity unramified extension, the meaning of semistability and the
same E_0,F,u,w,H,N and absolute v_3(q_0)=30. Do not assume q_0=3^30,
everywhere splitness, selected Q(j_E)-model conditions, other-place
parameter orders or sufficient initial data. Confirm direct DAG inputs
and all stated retention, rather than reprove the reduction criterion.
Reuse the prior primary-source coverage if sufficient; any essential
missing source must be identified before dependent mathematics.

Pass if the unchanged written hypotheses meet the cited theorem and
all retained conclusions concern the same curve and fields. Otherwise
record and repair or narrow the precise failed case. Original finite
B>=A, native/input/action/pilot/essentiality bridges remain unresolved.

This is source approval, not the completed mathematical audit or a
new result. L049 is the existing canonical application, so a duplicate
semistability lemma is unnecessary. The recorded stops in
ATTEMPTS/022,025,026,027 remain distinct: their excluded exact fields
or exact Tate curve are not resurrected by this review. Downstream
use is reliable reduction-type screening of the retained global
packet; semistability alone does not settle the selected-model
conditions or the main comparison gap. Full matching Mathlib coverage
is unchecked; no absence claim is made. No lemma, mathematical script,
PROOF or DAG change is needed in this literature-only turn.
