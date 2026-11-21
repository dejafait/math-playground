# Contact-weight variation bound: completed source comparison

TARGET: Assess whether bell-shape or variation-diminishing theorems can bound the strict sign changes of C466b's contact weight by 2m-2 under its existing actual-density hypotheses, without assuming complete monotonicity or global PF.
CHECKED: 2026-11-14
DECISION: EXPLORE
SEARCH_EVIDENCE: Step889 searched bell shape, polynomial differential operators, linear combinations of derivatives, variation-diminishing convolution and self-decomposable counterexamples; inspected primary statements listed below and reused assessments883/884/886 plus C466a/C466b and the L874/L611/retained-zero stops. No adequate theorem under the existing actual-density hypotheses was found in this bounded search.
SOURCE_EVIDENCE: Nahmias--Proschan (1979), Definition1.1/Lemma2.1/Theorem2.2, pp92-93; Kwasnicki--Simon arXiv:1910.07752v1, Theorems1.1/1.3, Proposition1.8, Corollary1.9 and the discussion preceding Corollary1.12, pp2-8; Kwasnicki arXiv:1710.11023v3, Sections6.1-6.2, pp19-21 including the smooth one-sided counterexample proof; Simon arXiv:1302.0956v1, main theorem p2 and Section3.2 pp9-11. Exact links and qualifications below.
COMPARISON: The closest arbitrary derivative-combination theorem reaches 2m-2 only with global PF_(2m-1), which is not among C466b's arbitrary-order imports. The bell-shape characterisation requires an unverified transform factorisation/level-crossing condition and concerns individual derivatives. Positive self-decomposability and smoothness alone do not even imply bell shape, by an inspected published counterexample; this does not refute the actual contact-weight bound.
GAP: The actual V still has no proved upper sign-change count. Missing inputs include global PF_(2m-1) or an applicable derivative-combination theorem with independently verified hypotheses; neither local boundary PF nor a finite source certificate at bounded order supplies the arbitrary-order premise.
REASON: Park the proposed inference from the existing density imports through bell shape or universal variation diminution. This is a source-supported limitation, not a disproof for actual Xi. A different finite Hankel-jet root-geometry test is nominated separately and remains REVIEW_REQUIRED.
SCOPE: Completed literature comparison only for the saved target. EXPLORE records that no adequate match was found; it does not approve a mathematical continuation of this parked mechanism or add a new theorem. No lemma or mathematical script was changed.
LITERATURE_REASON: Required first coverage of the new derivative-combination target; scalar-contact assessments883/884/886 do not cover it. No scalar-law or finite-PF recertification was repeated.

## Original nomination (preserved; readiness superseded above)

Essential local input is C466b, using C466a's actual p and L018/L024
normalization. At its hypothetical contact, P is the monic degree-(m-1)
polynomial determined by the real kernel vector, and V is exactly (2)/(14).
The proposed threshold is at most 2m-2 strict sign changes on (0,x_*):
count alternating strictly nonzero values, without treating a tangential
zero as a sign change. This is a target to assess, not an established
bound or a consequence claimed from the audit. Keep arbitrary finite m,
including orders beyond the cited finite PF range; no uniform matrix
computation or order-growing source certificate is proposed.

The new mechanism would constrain the oscillation of the weight itself.
The stopped mechanism only compared scalar amplitudes against that
signed weight. A usable variation bound could inform a later comparison
that splits the integral into controlled sign intervals; locations,
weighted masses and the strict inequality in C466b (7) or (9) would still
need separate estimates. The bound alone would prove neither inward
forcing nor sign preservation. Simultaneous contacts, a barrier, compact
propagation, global PF and L030-L032/C032a remain independent gaps.

The source review should check exact derivative-combination hypotheses:
individual-derivative bell shape must not be silently substituted for
the requested statement about P(partial)^2 p; any real-root condition
on P must be justified, since the current imports do not assert it.
Likewise retain only the stated positive decreasing actual H, not
complete monotonicity or an unproved PF condition. Do not substitute a
stable or other model density for p. Reuse the existing scalar-law
coverage without re-browsing it merely to fill a source quota.

Continue only if a primary theorem or a clearly isolated difference has
an applicable hypothesis set and reaches the stated threshold. Otherwise
record the precise unmet hypothesis and park this particular bound;
do not perform a new proof in the review turn or reopen bare retained-zero
domination. This new assessment is deliberately not ready.

Inherited source locators (no fresh source inspection in step888):

- [Sra Hub v1](https://hub.valency.io/works/W_pr5z5huy_v1), Section2.1,
  Lemma2.2, Proposition2.3, Lemma2.4 and AppendixB.
- [Steutel--van Harn (2004)](https://www.nzdr.ru/data/media/biblio/kolxoz/M/MV/Steutel%20F.%2C%20van%20Harn%20K.%20Infinite%20divisibility%20of%20probability%20distributions%20on%20real%20line%20%28Dekker%2C%202004%29%28ISBN%200824707249%29%28546s%29_MV_.pdf),
  ChapterV Theorems2.11/2.16 equation(2.23), ChapterIII Theorem10.4.
- [Sra author v3](https://suvrit.github.io/papers/riem-xi/riem-xi-v3.pdf),
  Theorems1.2/3.4/C.9 and PropositionA.1: inherited finite-PF overlap
  and complete-monotonicity caution, not a newly audited import.

Full Mathlib coverage of this new target has not been checked.

## Completed comparison, step889

The main gap is still L030-L032/C032a's actual-Xi all-degree
algebraic-square positivity. The intermediate threshold assessed here
is S^-(V;(0,x_*))<=2m-2, with strict sign changes counted after
discarding zeros. Its proposed use is a later decomposition into sign
intervals for C466b (7)/(9); it would not settle their locations,
weighted masses, strict forcing, simultaneous contacts or propagation.
The gate test was an applicable primary theorem reaching this threshold
without importing complete monotonicity or arbitrary-order global PF.
No such applicable theorem was established in this review.

### Closest theorem for the actual operator type

Steven Nahmias and Frank Proschan, *Sign changes in linear combinations
of derivatives and convolutions of Polya frequency functions*,
International Journal of Mathematics and Mathematical Sciences 2(1)
(1979), 91-101, [DOI](https://doi.org/10.1155/S0161171279000090),
[primary paper mirror](https://pdfs.semanticscholar.org/90a6/fe59b32831ed9f78537fff77b251332b9421.pdf),
Definition1.1 and Theorem2.2, pp92-93:
for fixed n>=1, a PF_(n+1) function f has at most n strict sign
changes in any real combination sum_(j=0)^n b_j f^(j), with the
derivatives in question existing. Their definition of S discards zero
values, matching this target. Read Lemma2.1's finite-difference/
variation-diminishing proof and Theorem2.2's alternative weak
Chebyshev-system justification. The latter refers to Karlin, p50,
and Karlin--Studden, p22; those books were not newly inspected.

For the operator in C466b (14), the required source premise at
n=2m-2 is global PF_(2m-1). Its coefficients may be arbitrary real
numbers: no real-root assumption on P is needed by this theorem.
C466b supplies lower signed derivative minors at one contact and
C466a supplies boundary PF in an order-dependent neighborhood.
Neither is the stated global premise. The inherited author-v3
finite-order claim remains unaudited here and in any event does not
cover arbitrary m. This comparison therefore supplies no actual-V
bound, even though the conditional source conclusion has the right
size. It also shows why checking roots of P would explore a different
mechanism rather than verify a hypothesis of Theorem2.2.

### Bell shape is a different hypothesis and a different conclusion

Mateusz Kwasnicki and Thomas Simon, *Characterisation of the class of
bell-shaped functions*, [arXiv:1910.07752v1, 17 October2019](https://arxiv.org/pdf/1910.07752v1),
Theorems1.1/1.3, Proposition1.8 and Corollary1.9, pp2-6:
weak bell shape is characterised by a Fourier-transform representation
(1.1) with integer level-crossing, integrability and regularity
conditions, equivalently a PF factor convolved with an AM-CM factor.
Proposition1.8 characterises unit-mass variation-diminishing convolution
on bounded Borel inputs by global PF. These are additional hypotheses,
not consequences supplied by positive decreasing H. Bell shape counts
sign changes of individual derivatives, not arbitrary combinations.
The pp8 discussion preceding Corollary1.12 restricts when f+a f'
remains bell-shaped by a level-crossing condition. The printed first
sentence of that corollary has f in a place where the preceding
discussion uses f_a; no corrected theorem is silently imported here.

No representation required by this source has been verified for the
actual density p, nor is a sign-changing input of controlled variation
provided for a PF factorisation. In particular, formal convolution
with P(partial)^2 delta is not an application of the bounded-Borel-input
statement. No theorem for arbitrary P(partial)^2p under bell shape
alone was identified. No assertion that such a theorem is impossible
or that the actual p fails bell shape is made.

### An inspected obstruction to using self-decomposability as a shortcut

Mateusz Kwasnicki, *A new class of bell-shaped functions*,
[arXiv:1710.11023v3, 27 November2018](https://arxiv.org/pdf/1710.11023v3),
Sections6.1-6.2, pp19-21, gives positive self-decomposable densities
which are not bell-shaped, including smooth one-sided examples.
Read the rational-Laplace-transform example's second-derivative sign
test, the decreasing canonical-kernel check in Section6.2, and the
one-sided PF approximate-identity convolution that preserves the excess
sign changes while smoothing the density. This refutes the two generic
self-decomposability conjectures discussed in Simon's Section3.2.
It is a published obstruction to that shortcut, not an actual-Xi or
hypothetical-contact counterexample. No countermodel is constructed here.

Thomas Simon, *Positive stable densities and the bell-shape*,
[arXiv:1302.0956v1, 5 February2013](https://arxiv.org/pdf/1302.0956v1),
main theorem p2 and Section3.2 pp9-11, concerns stable densities and
states the wider self-decomposable claims as conjectures. Those
conjectures must not be cited as theorems; the later obstruction above
changes the decision on assessment883's formerly unread stable-density
lead. No stable density is substituted for the actual p.

### Search, limitations and route decision

Queries actually used included `bell shaped functions polynomial
differential operator linear combinations derivatives sign changes
Kwasnicki Simon`, `Schoenberg variation diminishing convolution
derivatives polynomial differential operator bell shape`,
`"bell-shaped" "linear combinations" derivatives`,
`"bell-shaped" "polynomial" "differential" sign`,
`"self-decomposable" "bell-shaped" counterexample Kwasnicki`, and
the exact Nahmias--Proschan title. The inspected primary sources above
are distinguished from discovery snippets; no novelty inference follows
from the search. Narrow local searches checked the contact/Volterra/
reciprocal literature, attempts and histories for overlap and root claims.
C466a/C466b and the relevant L874/L611 conclusions were read.

The FSU report and publisher page for Nahmias--Proschan failed to open;
the primary-paper mirror supplied Definition1.1, Theorem2.2 and its
relevant argument. Schoenberg's 1948 PMC landing page was accessible,
but its PDF returned a download notice; its theorem was not inspected
there. Proposition1.8 above provides the inspected primary formulation,
so this is not a persistent essential source blocker. The connector's
PDF screenshots failed; extracted primary text was used. OCR in the
older PDFs is imperfect; no malformed displayed counterexample formula
is copied or used as a certificate. Full Mathlib coverage was not checked.

Outcome: NEGATIVE source comparison, KNOWN_IMPORTED. The new evidence
is the exact PF_(2m-1) hypothesis of a matching combination theorem and
the published smooth self-decomposable obstruction. This parks the
source route under the present assumptions; it does not refute the
target's actual-density conclusion, change C466b's audit or close any
RH gap. The scalar-domination, L874/L611 and fixed-U12 stops remain.

The separately nominated next target concerns finite Hankel-jet root
geometry rather than sign variation from a global density class; it is
recorded in assessment889 as REVIEW_REQUIRED. No proof, new root
example or new variation estimate is given in this literature turn.
