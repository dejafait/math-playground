# Full quadratic Grunsky defect: nomination1311, completed review1312

TARGET: Assess a full quadratic Grunsky-defect representation of the actual 3-by-3 block (S_(m+n))_(1<=m,n<=3) using f_b(z)=z/(1+sum_(j=1)^5 b_j*z^(j+1)), real b_j, tau>0 and positive diagonal weights, including exact infinite-sum support, unit-disk univalence and local duplicates before nominating one bounded test.
CHECKED: 2026-11-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Review1312 reused1302/1303/1310 and1308, read L030/C032a, C030y's general extraction, relevant C030z passages and fixed1253/unit-disk1311 stops; scoped Grunsky assessment/attempt searches and the external queries recorded below found tools and a Gram-defect overlap, not a realization theorem for these actual sums. No novelty inference.
SOURCE_EVIDENCE: Teo hep-th/0305005v2 Sections2.1-2.2, Faber recurrence,(2.3)-(2.4),(2.8)-(2.12), formal-extension paragraph; Beckermann-Stylianopoulos arXiv1606.00553v2 Section1(1.1)-(1.4), Section2 Lemma2.2(2.6)-(2.9) and its proof; Ponnusamy-Wirths arXiv1704.08184v1 Theorem1, proof(2)-(4), Remark1. Primary links, hypotheses and reuse qualifications below.
COMPARISON: The full quadratic defect is an established Grunsky contraction/Gram construction, not a new positivity mechanism by itself. Faber identities cover a later exact support and coefficient specialization for this finite Laurent family; they do not solve its six inverse equations. C030y/C030z linear stops and1302's inverse-spectral near-match do not settle the changed prescription. Univalence has usable sufficient coverage, with poles checked separately.
GAP: Specialize the full-support identities and decide a necessary compatibility test or certify an actual witness; formal feasibility leaves analytic univalence unpaid. No inspected theorem identifies this defect with the actual S_(m+n). All-degree positivity, initialization and singular cases remain unresolved.
REASON: Essential method-level coverage is adequate for one bounded finite calculation, with no claimed feasibility, support cutoff or analytic realization proved in this literature turn. The separate calculation assessment1312 is newly ready and requires next-turn approval before research.
LITERATURE_REASON: Invocation-start REVIEW_REQUIRED changes linear prescribed coefficients to a full quadratic defect and fixes a rational family; exact-support and analytic-hypothesis comparison were essential unread coverage. Ready1303/1310 algebraic and contraction assessments were reused.
SCOPE: Completed literature-only comparison of the saved target. The unchanged proposal and limitations below are historical nomination text. Calculation assessment1312 covers only this five-coefficient family and first three indices; no new lemma, mathematical script, parameter test or source-dependent derivation was performed here.

## Proposed mechanism and bounded test

The following nomination is preserved verbatim as proposed work. Read the
completed comparison below for current source coverage; its former
unread-source statements describe the nomination, not review1312.

The main gap is actual-Xi algebraic-square positivity L030-L032/C032a.
The proposed intermediate target concerns only the first3-by-3 actual
shifted block, not all degrees. Let c_mn use C030z's negative mixed-log
convention and impose d1=1,d2,d3>0. The proposed equations are

    delta_mn/m - sum_(k>=1) k*c_km(f_b)*c_kn(f_b)
        = tau*d_m*d_n*S_(m+n), 1<=m,n<=3.

This is a proposed system, not an asserted identity. For analytic use,
f_b must be holomorphic and univalent on the full unit disk, including
the absence of poles there. Real b_j are specified; no oddness or extra
zero-index freedom is imposed. The full sum must be justified. Whether
the rational family's reciprocal Laurent form gives exact finite
support in these columns is an explicit review obligation, not a fact
derived in this nomination. A bound for omitted terms is not a license
to drop their contribution to the deficit.

Its plausible downstream use is an actual mixed-form certificate from
the classical quadratic contraction inequality. It could establish a
finite input while exposing the missing structure for an all-degree
construction. Such a construction, uniform analytic control and every
larger block would remain unpaid. A positive raw-theta covariance or
an assumed positive actual Hankel block does not meet the purpose.

The bounded decision is whether exact known support/compatibility and
univalence results permit one falsifiable test of these six equations
in this fixed five-coefficient family. A decisive violated necessary
condition stops this family; a rigorously compatible solution with
paid univalence would retain it as a finite input. Formal feasibility
alone leaves analytic realization unresolved. If the source comparison
shows the proposed use merely assumes the desired Hankel sign or
cannot control the full sum, reject that mechanism without a sweep.
No free increase in Laurent degree or altered equation is authorized.

## Reuse, failures and continuation limits

Essential local definitions and actual-input context: L025,L030,L032,
C032a,C030y,C030z,L019,L021,L027,L036,L037,L917. The1307 outer boxes
may be used later only with their inherited arithmetic contracts; no
new boxes or signs are supplied here. The algebraic-square convention
and index shift must be checked against L030 before a later application.
No RH, all-degree Hankel premise or cross-notebook input is authorized.

Preserve C030y's fixed-weight stop, C030z's unit-disk stop1311,
four-point failure1307, uniform-H2 and1297/1302/1200 stops. The
inspected1302 near-match of Ammari-Colbrook concerns local inverse
spectral stability and a linear Hankel part with a quadratic remainder;
it does not realize this exact defect. It is not a ready theorem input.
Source comparison must also distinguish the established quadratic
Grunsky inequality from the new and unproved inverse representation.
Full matching Mathlib coverage is unchecked.

This nomination prioritizes a changed central mechanism after the
linear stop, while retaining the source gate. The next turn is
literature_comparison, standard/high. Finite coefficient elimination,
if eventually approved, remains calculation/specialization. A genuine
analytic realization construction would need its own source-ready
proof_attempt/creative target and precise bounded obstruction; none
is approved merely to meet the creative scheduling preference.

## Completed source comparison1312 — 17 November 2026

The main gap remains L030-L032/C032a's actual algebraic-square sign
in every degree. The intermediate target is only the specified three
indices. Its use would be a finite mixed-form input after independent
analytic realization; a formal match alone supplies no sign. This
review performs no coefficient expansion or actual-parameter test.

### Inspected primary statements

**L.-P. Teo**, *Analytic functions and integrable hierarchies—
characterization of tau functions*, Lett. Math. Phys.64(2003),75-92,
[arXiv:hep-th/0305005v2](https://arxiv.org/html/hep-th/0305005v2),
Sections2.1-2.2, preprint pp2-6. Reopened the normalized formal classes,
Faber recurrence and coefficient-comparison argument through(2.4).
The source states that Phi_m has degree m and

    Phi_m(g(Z))=Z^m+m*sum_(k>=1) c_mk*Z^(-k).

Reuse1303 for the formal extension, symmetric minus-log convention
and reciprocal identification(2.8)-(2.12). This supports exact column
extraction by polynomial composition when g is finite Laurent. The
later calculation must supply its specialized exponent bounds and all
coefficients, rather than infer support from a short mixed-degree jet.
No cutoff or new polynomial for this family was derived here.

**B. Beckermann and N. Stylianopoulos**, *Bergman orthogonal polynomials
and the Grunsky matrix*, [arXiv:1606.00553v2, 6 July2016](https://arxiv.org/html/1606.00553v2),
Section1(1.1)-(1.4), Section2 Lemma2.2(2.6)-(2.9) and proof.
For an exterior conformal map psi onto the complement of a bounded
simply connected domain G, the normalized symmetric matrix is
C_(n,k)=sqrt((n+1)(k+1))*b_(n+1,k+1). Inequality(1.3) is full-column
contraction. With boundary of planar measure zero, Lemma2.2 identifies
I-C^*C with the Gram matrix of Faber derivatives normalized as(1.4).
The proof uses analytic level curves, Green's formula, uniformly
convergent boundary series, then the zero-area-boundary hypothesis
and l2-column/l1-product control for the boundary limit. No Jordan
boundary is required. Quasiconformality is an additional hypothesis
of Corollary2.3's bounded inverse, which is unnecessary here.

This is an overlap with the proposed quadratic construction, not an
inverse realization theorem. A formal rational expression has no
conformal-map hypothesis. Reuse1310's direct disk inequality for the
necessary analytic sign; invoking the stronger Gram identity additionally
requires its domain and boundary hypotheses. Do not assume a disjoint
welding pair, a zero-area complementary domain, or strict contraction.
Those are distinct hypotheses from this lemma's zero-area boundary.

**S. Ponnusamy and K.-J. Wirths**, *Elementary considerations for classes
of meromorphic univalent functions*, [arXiv:1704.08184v1, 26 April2017](https://arxiv.org/html/1704.08184v1),
Theorem1, proof(2)-(4), Remark1. For meromorphic f on the unit disk,
normalized by f(0)=0,f'(0)=1, the strict condition

    |z/f(z)-z*(z/f(z))'-1|<1 throughout |z|<1

implies meromorphic univalence. The proof factors the holomorphic
remainder as z^2*omega, uses |omega|<=1 and integrates the differential
equation to obtain a nonzero divided difference. Remark1 expressly
allows a simple pole. Accordingly a proposed f_b still needs absence
of denominator zeros in the open disk to meet this notebook's
holomorphic-disk requirement. The sufficient condition is not necessary:
its failure cannot refute the whole family. No coefficient bound or
univalence conclusion for the selected b_j was derived here. Theorem A's
older references are not claimed as independently inspected originals;
Theorem1 and its proof are the primary input used.

### Exact applicability, duplicates and search limits

For the proposed rational expression the required reciprocal map and
normalization are those already covered by Teo and C030y's general
reciprocal identity. Formal coefficients can be computed without an
analytic hypothesis. Analytic signing must instead use the full-disk
inequality, real coefficient convention and the exact complete sum.
The later specialization must verify its index shift against L030 and
its positive diagonal congruence. These are proof obligations, not new
results of this source review. The known Gram construction supplies
no independent actual-Xi identification and cannot replace that work
by assuming the desired Hankel block is positive.

Scoped local comparisons read1302/1303/1310,1308,1250's source review,
the two canonical linear results and their stop records. The inspected
Ammari-Colbrook Theorem3.2/Lemma3.4 comparison in1302 is reused as a
near-disk inverse-spectral result, with prescribed higher remainder,
not an inverse quadratic-defect theorem. No reread was needed. The
local Grunsky-specific search found no completed exact test of these
six full-sum equations; this is a bounded duplicate check, not proof
of novelty. All prior fixed-weight, uniform-H2,1297/1302/1200 and1311
stops are preserved within their original scopes.

External queries included `Grunsky coefficients finite Laurent series
"mN" "zero"`, `Grunsky coefficients "finite" "Laurent" Faber`,
`inverse Grunsky "defect" matrix realization univalent`, `"Bergman
orthogonal polynomials and the Grunsky matrix" arxiv Beckermann
Stylianopoulos`, `"Grunsky" "Laurent polynomial" "univalent"
coefficients`, and rational-univalence/coefficient-condition variants.
The primary Teo and Beckermann-Stylianopoulos identities are stronger
method-level matches than search-only general rational-function leads.
Obradovic-Ponnusamy-Wirths arXiv1604.07733v2 introduction(1) was read
as a secondary lead to the U condition; no theorem from it is needed.
Reade-Silverman-Todorov, *Classes of rational functions*, Contemp.
Math.38(1985),99-103, was located bibliographically, not inspected or
imported. Neither that unread lead nor search snippets decide feasibility.

SPECIALIZE permits the separately nominated exact calculation at
`drafts/literature/2026-11-17-quadratic-grunsky-defect-calculation-1312.md`.
Continue with a full-support reduction and an informative necessary
condition, or a rigorously compatible witness with explicitly stated
analytic status. An exhaustive violated necessary condition stops
this fixed family. No sweep, added Laurent degree, rescaling or presumed
inverse theorem is approved. A favorable finite truncation is invalid.
Routine algebra is not creative; an analytic construction is not yet
specified well enough to justify creative routing. All-degree signs,
initialization, singular blocks and analytic realization remain open.
Actual S2-S6 boxes retain L037's arithmetic contracts and the existing
L917/1307 qualifications. Full matching Mathlib coverage is unchecked;
no cross-notebook input, lemma/script write, DAG/PROOF change or RH
candidate results from this literature-only EXPLORATION.
