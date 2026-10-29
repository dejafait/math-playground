# Fourfold star and actual Leray splitting — source comparison

TARGET: Assess whether the product-metric fourfold star operator descends to H^2(X,End_0(F)) and preserves L165's actual orthogonal Leray summands.
CHECKED: 2026-10-26
DECISION: EXPLORE
SEARCH_EVIDENCE: Step 577 searched coefficient fourfold-star/harmonic Serre duality, star/Leray splitting and higher-direct-image harmonic metrics; inspected the primary passages below and L116/L165's actual arrows, reusing the prior isotropy and coefficient-Lefschetz assessments. No matching actual-summand preservation theorem was found; this is not an absence or novelty claim.
SOURCE_EVIDENCE: Read Cao–Leung 1407.7659v2 p. 2 and Section 2.1, pp. 8–9, Lemma 2.1/Corollary 2.2 with full proofs, and Section 2.2; Chakrabarti–Shaw (2012), Sections 2.2–2.4, equations (7)–(15), Lemma 2 and Corollary 1 with proofs; Mourougane–Takayama (2008), Theorem 1.1 and introduction pp. 905–906. Precise conventions and scope limits follow.
COMPARISON: Harmonic descent has primary coverage using a parallel normalized volume and holomorphic Hermitian coefficient bundle; full SU(4) holonomy is not used in that proof. Neither this descent nor the inspected relative-Hodge statement compares the fixed metric with L165's actual j,r,a. The latter statement requires coefficient Nakano semipositivity, not supplied here.
GAP: Preservation of i(K) and ker R for the fixed metric remains undecided; no actual harmonic representatives or metric-adjoint comparison of j,r,a is provided. Trace-free and volume conventions must be retained in any eventual specialization. Positivity of an actual bracket remains a separate gap.
REASON: The bounded source test supplies descent coverage but no evaluable actual-arrow comparison. Park this metric-splitting mechanism under its stated test, without claiming nonpreservation or a source-access blocker. EXPLORE records the search comparison, not authorization to assume preservation; reopening needs a specified actual-map or analytic input.
SCOPE: L071/L116/L165's identical marked K3 product with fixed common metric/triple/forms and actual compatible connection; hypothetical locally free rank-two product-polystable F, integral c_1=0 and ch=2-14e_1-21e_2-tau_D+62P; actual j,r,a, all of H^2(X,End_0(F)), unknown t and finite reduced possibly empty Z. No SU(4)-holonomy, integrability of sections, star-fixed bracket or F existence is assumed.

## Purpose and the bounded test

Primitive Hodge realization and existence of F remain the main gaps.
L165 shows that complex scalar isotropy with an unrestricted complement
cannot constrain the point quotient. L167 distinguishes that pointwise
fact from a homogeneous polynomial identity, but does not evaluate its
actual terms. An independently specified metric real structure
compatible with the actual summands could provide additional geometric
information for that identity. This is a possible use, not an assertion
that preservation alone gives positivity or an exclusion.

Use L165's notation E=H^2(X,V), V=End_0(F), K=H^1(B,M),
U=H^0(B,W), i=H^2(j), R=H^2(r), A=H^2(a). Its existing conclusion
is E=i(K) orthogonal-direct-sum ker R for the complex Serre form Q,
with A identifying ker R with U. The question concerns these exact
summands and the fixed product metric and volume, not a newly chosen
positive real form. L168 may be used for its actual quotient-adjoint
identification if needed; L167 is downstream motivation. No
cross-notebook theorem is proposed.

First retrieve primary definitions of the fourfold antilinear star on
End_0(F)-valued (0,2)-forms, including the Hermitian-adjoint and volume
normalizations. Check square, trace-free preservation and commutation
with the harmonic projection under the actual connection. In
particular distinguish a holomorphic-volume metric construction from
the stronger SU(4)-holonomy hypotheses of a DT4 moduli theorem. The
product has additional holomorphic forms; do not reuse an irreducible
Calabi–Yau moduli statement without its hypotheses.

Search the exact summand-preservation statement, relative Hodge theory,
adjoints of Leray maps and known obstructions. Reuse the prior duality
and scalar-isotropy sources where unchanged. Test whether the sources
give a concrete comparison of the metric star with the actual
inclusion/retraction, or merely permit changing the splitting. Neither
complex Q-orthogonality nor L116's additive derived splitting settles
that comparison. No new commutator identity is derived by this proposal.

Continue only if these definitions and hypotheses yield a bounded
actual-map test that can decide preservation. If the accessible result
needs unavailable holonomy, harmonic metrics, uncontrolled Green data
or a freely chosen splitting, record that obstruction and park this
mechanism. Even if preservation holds, the actual bracket's relation
to the resulting real structure is a separate unresolved question;
never assume it is star-fixed or positive.

Preserve ATTEMPTS/068,/077,/080,/092–094, the harmonic-operator warning
and the step-576 invariance-only stop. This is not a reopening of
scalar-isotropy-only exclusion or cyclicity-only vanishing. Empty Z
and U=0 must be included. Matching Mathlib coverage is not checked.
No new mathematical result, script or creative attempt is approved.

## Completed comparison — step 577

The preceding purpose and test record the invocation-start proposal.
This section completes that source review; no new lemma, mathematical
script or commutator identity is derived. Outcome: EXPLORATION /
LITERATURE / NOVELTY_UNCHECKED, not progress beyond the sources.

### Primary statements and essential proof cases

[Cao–Leung, *Donaldson–Thomas theory for Calabi–Yau 4-folds*,
arXiv:1407.7659v2, 24 September 2015](https://arxiv.org/pdf/1407.7659v2#page=8),
p. 2 and Section 2.1, pp. 8–9: the antilinear star uses a Hermitian
bundle metric and normalized parallel holomorphic volume. Its square
on (0,2)-forms is one. Lemma 2.1 identifies the formal Dolbeault
adjoint through this star; Corollary 2.2 gives harmonic descent.
The complete proof uses the parallel volume, not equality of holonomy
with SU(4). Thus the product's extra holomorphic forms do not obstruct
this cited construction. Normalize the product volume with the fixed
metric; the originally fixed volume may differ by a constant, which
must be tracked before comparing real eigenspaces or positivity.
The analytic definition does not need an integral polarization; the
paper's separate polarized-moduli hypotheses must not be imported
as conclusions for a real Kähler class. Section 2.2, pp. 9, through
Remark 2.6 discusses resolution metrics and their dependence, not the
actual Leray arrows. This does not approve a replacement splitting.

[Chakrabarti–Shaw, *L² Serre duality on domains in complex manifolds
and applications*, Trans. AMS 364 (2012), 3529–3554](https://people.se.cmich.edu/chakr2d/pubs/serre.pdf#page=4),
Sections 2.2–2.4, pp. 3532–3535: equations (7),(10),(11) define the
antilinear coefficient-dual star by evaluation and the Hermitian
pairing, with target the dual coefficient bundle. Equations (12)–(15),
Lemma 2 and Corollary 1 give its square and adjoint identities; their
proofs use the graded evaluation rule and Stokes. Compactness removes
the distinct minimal/maximal-domain issue (p. 3532).
For endomorphisms the trace identification and Hermitian metric use
the matrix Hermitian adjoint in a unitary frame, not coefficient
conjugation leaving matrix units fixed. Restricting the End(F)
statement to End_0(F) requires retaining its trace-free orthogonal
summand and induced connection. These are coefficient conventions
and applicability obligations, not a new assertion about i(K).
No cited functoriality identifies an algebraic Serre adjoint with
a Hermitian adjoint of the actual truncation inclusion.

[Mourougane–Takayama, *Hodge metrics and the curvature of higher
direct images*, Ann. ENS 41 (2008), 905–924,
Theorem 1.1, pp. 905–906](https://www.numdam.org/item/10.24033/asens.2084.pdf#page=2)
assumes a smooth proper surjective Kähler map with connected fibres
and a Hermitian coefficient bundle of Nakano semipositive curvature.
It gives locally free Nakano semipositive canonical-twisted higher
direct images. Their introduction specifies the pulled-back Hodge
metric, distinguishing it from the fibrewise harmonic metric.
The map hypotheses fit p, and the relative canonical line is
trivialized here; Nakano semipositivity of V is not an input.
This theorem therefore supplies no comparison of L165's summands.
Its later curvature proof was not needed after this hypothesis failure
and was not inspected or imported.

### Search boundary, duplicate check and decision

Queries included `Cao Leung Donaldson Thomas Calabi Yau fourfolds star
operator End E harmonic Serre duality`, `Calabi Yau fourfold star
operator Leray splitting harmonic bundle relative cohomology`,
`"Calabi-Yau" "star" "Leray" bundle`, `"Serre duality" "Hodge star"
"Hermitian" endomorphism`, `"higher direct images" "Hodge star"
vector bundle`, and `"Leray" "orthogonal" "harmonic" "vector bundle"
star`. Irrelevant star-name hits and secondary summaries were not
theorem evidence. No Leray comparison occurs in the Cao–Leung text
search; that limited fact is not a general nonexistence claim.

Read L165 through the proof of the actual orthogonal lift and L116
through construction of the actual trace-adjoint retraction. These
use complex bilinear duality and avoid harmonic representatives.
Reuse unchanged coverage in the global-isotropy assessment and the
coefficient-Lefschetz audit: neither supplies independent factorwise
harmonic actions. ATTEMPTS/068,/077,/080,/093 and /092–094 remain
preserved, as does step 576's distinct stabilizer-image stop.
No metric-orthogonal Leray splitting, star-fixed Yoneda bracket,
nonempty Z, or F existence is assumed. For Z empty the quotient
question is vacuous; this does not decide positive-support cases.

The continuation test fails to yield an evaluable comparison, rather
than disproving preservation. Park this mechanism pending a concrete
comparison with the fixed harmonic projection/actual arrows; arbitrary
real forms or uncontrolled Green-operator data do not reopen it.
Actual section quadrics, the complementary operation and primitive
realization remain unresolved. Full matching Mathlib coverage for
coefficient star, harmonic descent and actual Leray compatibility was
not checked; no absence is claimed.

An independent next source target is the trace–Atiyah semiregularity
map on the actual obstruction space. The complementary-operation
assessment explicitly left semiregularity as an unread lead; it is
not ready mathematics. ATTEMPTS/004 concerns singular embedded
support, and /009 concerns specific negative syzygy presentations;
neither is a global ban on the locally free F question. This proposal
gets its own REVIEW_REQUIRED assessment and no theorem application
in this turn.
