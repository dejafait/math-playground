# Global semistability after torsion adjunction — source assessment

TARGET: Determine whether L048's curve over F=Q(zeta_60,E_0[30]) is semistable at every finite place while retaining its established 3-adic packet.
CHECKED: 2026-10-11
DECISION: IMPORT
SEARCH_EVIDENCE: Scoped searches in October 10–11 assessments, foundations and ATTEMPTS found no earlier everywhere-semistability coverage; external searches for Raynaud full-torsion semistability and Serre–Tate reduction located SGA7 I IX.4.7 and Silverberg–Zarhin's published Theorem 3.5, whose full statement was read rather than inferred from a snippet.
SOURCE_EVIDENCE: Silverberg–Zarhin, Semistable reduction and torsion subgroups of abelian varieties, Ann. Inst. Fourier 45(2) (1995), 403–420, Definition 3.1 p.405 and Theorem 3.5 p.406, https://www.numdam.org/article/AIF_1995__45_2_403_0.pdf; its reference [7] identifies Grothendieck, SGA7 I, LNM 288 (1972), Expose IX Proposition 4.7; Dupuy–Hilado arXiv:2004.13228v1 (28 April 2020), Definitions 5.3.1/5.5.1, Remark 5.3.2 and section 5.7.4, https://arxiv.org/html/2004.13228v1#S5.SS3.
COMPARISON: Raynaud's criterion covers full n-torsion unramified at a discrete valuation when n>=3 is prime to its residue characteristic; levels 5 for p!=5 and 6 for p=5 cover the unchanged full rational 30-torsion hypothesis, including p=2,3,5. Only citation and applicability are needed; no new reduction theorem or reproof is justified.
GAP: Source coverage for everywhere semistability is ready; the canonical application to L048's same curve and field is deferred to a separate research turn. Semistability over F does not prove the selected field-of-moduli multiplicative-model condition, other-place parameter orders, sufficient initial data or original finite B>=A.
REASON: The prior one-place audit did not cover this target; the newly inspected precise criterion now covers every finite residue characteristic without changing F or E_0, so dependent mathematical work may proceed after the separate approval of this changed assessment.
SCOPE: Exactly TARGET for L048's same reselected E_0/Q and F=Q(zeta_60,E_0[30]), using L045's full rational torsion and L048's retained embedded H,N packet; approves a known-result import with explicit local applicability, not everywhere split reduction or sufficient initial theta data.

LITERATURE_REASON: Everywhere reduction is outside the approved one-place L048 audit; a precise torsion criterion and its residue-characteristic restrictions were essential missing coverage.

## Primary theorem and inspected cases

[Silverberg and Zarhin's published paper](https://www.numdam.org/article/AIF_1995__45_2_403_0.pdf#page=5)
states the Raynaud criterion as Theorem 3.5, printed p.406
(zero-based PDF page 4). For an abelian variety X over a field K
with a discrete valuation v, assume n is prime to the residue
characteristic and all points of X[n] are defined over an extension
unramified over v. For n>=3 the conclusion is semistable reduction
at v. The separate n=2 case requires a henselian valuation ring
and separably closed residue field and gives reduction only after
a specified extension; that branch is not used. The PDF extraction
sometimes drops the equality stroke in inequalities. Our proposed
levels 5 and 6 are strictly greater than 3, so this does not affect
the application. Definition 3.1, p.405, uses the identity component
of the Neron special fiber: an abelian variety extended by a torus.
It does not assert good reduction or a split torus.

The theorem's proof reference is the original named Raynaud
criterion: A. Grothendieck, *Modeles de Neron et monodromie*,
SGA7 I, Lecture Notes in Mathematics 288, Springer (1972),
Expose IX, Proposition 4.7, within pp.313–523. No reproof is needed.
The [French transcription](https://grothendiecksga.com/read/sga7/fr/9-4.html)
was inspected at 4.7–4.7.4 for statement and proof cases. It reduces
to a strictly local trait and a faithful finite action on the
semiabelian special fiber, then invokes Serre's rigidity lemma
4.7.1; n=2 is the exceptional exponent-two case. This is supplemental
source orientation, not independently authenticated scan evidence.
The original scanned PDFs at SLMath, the old MSRI address and
iut-theory.org were inaccessible through the web tool; a direct
SLMath download failed DNS. None is claimed read. The published
Theorem 3.5 supplies the complete usable statement independently
of that access failure, so there is no essential source blocker for
this import. Serre–Tate good reduction and the paper's weaker
maximal-isotropic-subgroup hypotheses are not substituted for it.

The applicability checklist for the later canonical import is:

| Residue characteristic p | Torsion level to use | Required source condition |
| --- | --- | --- |
| 2 or 3 | 5 | Full 5-torsion rational; 5 prime to p |
| 5 | 6 | Full 6-torsion rational; 6 prime to 5 |
| Any other prime | 5 | Full 5-torsion rational; 5 prime to p |

Both levels divide 30. The application must explicitly retain the
full geometric torsion, its rationality after completion, and the
identity unramified extension. It must use the local discrete
valuation, not apply n=30 at primes dividing 30. No new field,
curve, precision, disjointness assumption or coefficients are
required. These are applicability checks for the next turn; no
new lemma or mathematical script is supplied in this literature turn.

## Downstream relevance and qualifications

Reused the existing packet-field-role and full-torsion assessments,
then rechecked the [versioned Dupuy–Hilado text](https://arxiv.org/html/2004.13228v1#S5.SS3).
Definition 5.3.1(3) requires full rational 30-torsion and sqrt(-1).
Condition (4) instead concerns multiplicative reduction for every
model over Q(j_E) at selected odd-characteristic places. Condition
(5) imposes separate restrictions on ell, parameter orders and
[F:Q(j_E)]. Definition 5.5.1 adds the selected places, multiplicative
subspace and canonical generator. Everywhere semistability over F
is not stated there as an extra independent sufficient condition.
Thus the present target supplies a consequence of the already
retained torsion prerequisite, useful for an eventual other-place
reduction screen; it cannot replace the distinct selected-place
requirements. Remark 5.3.2 distinguishes native 6-torsion from this
exposition's 30-torsion. No native-definition equivalence is imported.

The main gap remains original finite B>=A. The intermediate target
is exactly TARGET. L045 and audited L048 are the essential local
inputs for the later application. Retain L044–L047 and L042's
Omega,H,N through them, M>=max(M_tors,31), v_3(3)=1 and
v_3(q_0)=30, without q_0=3^30. The continuation test passes at
source-comparison level: a precise criterion has no uncovered
finite residue-characteristic case. Continue with the cited import
only; stop or revise if its hypotheses cannot be matched to the
unchanged full torsion or if retention requires a field enlargement.

No duplicate local global-semistability result was found in the
scoped search; this does not claim novelty. ATTEMPTS/022,025,026,027
were checked and remain intact: excluded fields and exact-curve
globalization are different targets. No original-IUT flaw, complete
candidate or progress beyond the checked known theorem is claimed.
Full matching Mathlib coverage is unchecked; it is unnecessary for
the cited informal import. Native/input/action realization, marked
pilot transport, essentiality and original finite B>=A remain open.

The [official announcement](https://zen.ac.jp/news/0ul6zqed9-0),
dated 2023-07-07, was rechecked on 2026-10-11: its inherent-flaw
target and separate adjudication conditions agree with the existing
scope record. This source review does not address adjudication.
