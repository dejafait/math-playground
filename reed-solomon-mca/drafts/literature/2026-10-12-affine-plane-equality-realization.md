# Affine-plane equality-realization source comparison

TARGET: Determine whether L072's sixteen-support family can be realized by an L010 equality pencil for any bijective H-labeling over F_(97^20).
CHECKED: 2026-10-12
DECISION: EXPLORE
SEARCH_EVIDENCE: October 12 targeted affine-plane/RS-syndrome, fixed-evaluation higher-order MDS and secant-transversal queries found no inspected theorem deciding the exact family; reused ready moment/exterior assessments and compared the specific local exclusions and sampling stop below.
SOURCE_EVIDENCE: Rechecked BGM arXiv:2206.05256v4 Definitions 1.4/1.8, Theorem 1.12 and Corollary 1.15 with proof; read del Campo August 2012 dissertation III.D.1, printed pp. 29–30, and Sottile alg-geom/9510017v1 Section 7.1, printed pp. 14–15, including the graph/eigenline and finite-field construction passages; reused Hall Theorem 5.1.1 and the recorded exterior comparisons.
COMPARISON: Known RS independence and the existing four-support alternating construction supply tools, not this family's answer. Generic/selectable-evaluation MDS results do not certify fixed H; four-subspace transversals give a conditional description, not compatibility with all sixteen supports. L024/L027/L029 exclude different families.
GAP: A uniform necessary moment obstruction for every H-labeling, or an actual full-weight original-chart realization satisfying every L010 equality gate, remains missing; neither genericity nor positive finite sampling decides it.
REASON: The changed realization scope lacked essential coverage at startup; this separate source review now permits one bounded uniform moment-compatibility attempt without deriving its conclusion or claiming novelty.
SCOPE: Exactly L072's displayed sixteen blocks under every bijection of its abstract vertices to fixed H in F_97, with weights and finite parameters in F_(97^20). Approves one uniform quotient/exterior-kernel proof attempt using L010 and L026's existing arbitrary-four-support construction; any claimed realization must pass all L010 gates. Does not approve a new positive-only label-sampling campaign or other support families.

## Exact gap, intermediate target and downstream use

The main local gap is excluding sixteen bad parameters in the frozen
four-omission cell, whose allowable integer count is fifteen. Uniform
triangle twelve and extraction of a useful actual-error pair remain open.
L072 has already refuted extracting such a pair from balance and the
triangle alone. Its full table is the fixed family here; auxiliary F_4
coordinates encode incidence only, with no embedding into characteristic 97.

The intermediate target is a labeling-independent necessary moment
condition that excludes this family, or a rigorously checked realization
showing that exclusion fails. Essential inputs are L072's complete table
and L010's moment/equality conditions; L026's generic-four-support
annihilator construction is an available method, while L057 fixes the
triangle's meaning. No cross-notebook input is proposed.

The chosen first test is uniform elimination of the common alternating
kernel for these sixteen support subspaces. The required sufficient
threshold for that linear obstruction is rank 28 in the full exterior
square of the eight-dimensional syndrome space, for every bijection to H.
This is a proposed threshold, not a rank computed in this turn. A future
attempt must justify its application to the displayed blocks and separately
handle dependent syndrome directions. A nonzero kernel vector need not be
decomposable and therefore need not represent a pencil.

Downstream, exclusion would remove this concrete obstruction to stronger
moment-based extraction. A realization of all sixteen actual events would
test the proposed uniform triangle bound directly. Neither an exclusion
of one family nor a partial moment solution resolves arbitrary supports
or the challenge's uncertified ABF26 qualifications. The global interval
remains 11/q–16/q.

## Local coverage, duplicates and recorded failures

Read L072 in full after the supplied overview/DAG; read L010's statement,
kernel/eight-column proof, locator converse and same-support argument.
Read L024's full fixed-eight-block lift proof, L027's quotient construction
and first elimination stage, and L026's necessary equations and the
paragraph headed “Arbitrary-label matrix and bounded test.” The latter
already constructs annihilator rows for any four-element E subset H:
coefficient vectors of X^r P_E(X), 0<=r<4, with P_E the support quartic.
Their six pairwise alternating rows are the ready linear test. Its moment
offset, basis independence and extension-field qualifications are retained;
no new general construction or decoding theorem needs reproof here.

L024 depends on eight supports contained in each fixed eight-coordinate
block. Such a block arrangement has not been supplied for L072. L027 and
L029 require their particular cyclic overlap tables, not just regularity;
their conclusions cannot be transferred by renaming the sixteen vertices.
The overview identifies L031's six-support/eight-union exclusion and
L069/L071's useful-pair bounds, but L072 was specifically constructed
against support-only extraction. No containment or applicability of those
results is asserted, and no unnecessary detailed proof was loaded.

ATTEMPTS/027 records the precise balance-only failure. ATTEMPTS/020
records that 256 positive labeled rank checks did not decide a uniform
theorem and stopped that sampling mechanism. ATTEMPTS/016 and /018 were
checked narrowly for the prior incidence and fixed-cyclic scope limits.
The current test changes the support family and seeks a uniform quotient
argument, rather than relaunching those sampled or support-only routes.
A historical sampling stop is not a ban on a genuinely uniform proof.

Reuse the [two-block moment assessment](2026-10-05-two-block-moment-obstruction.md),
the [arbitrary-label assessment](2026-10-05-cyclic-0125-arbitrary-label-rank.md),
and the [overlap assessment](2026-10-05-overlap-factor-universal-rank.md)
for their unchanged ingredient scope. Hall, *Notes on Coding Theory*,
GRS chapter, Theorem 5.1.1 and proof, printed pp. 63–64
([author PDF](https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf)),
assumes distinct evaluation points, nonzero multipliers and 0<k<=n.
H with unit multipliers and n=16,k=8 meets these hypotheses over the full
extension, giving distance nine. This supports L010; it gives no family
realization criterion. The known theorem is cited, not reproved.

## Primary theorem statements and proof cases compared

**Generic MDS.** Brakensiek–Gopi–Makam, *Generic Reed-Solomon Codes
Achieve List-decoding Capacity*,
[arXiv:2206.05256v4](https://arxiv.org/pdf/2206.05256v4), 28 August 2024,
Definitions 1.4/1.8 and Theorem 1.12/Corollary 1.15, printed pp. 4, 6,
8–9, were rechecked. Generic evaluations are independent indeterminates;
MDS(ell) compares common column-span intersection dimensions with a
generic matrix. The corollary's proof uses GM-MDS, dual RS column scaling
and Theorem 1.13. The selectable-evaluation formulation does not promise
prescribed H. These results neither certify that fixed subgroup nor
decide a line meeting sixteen spans at distinct points. Reuse the prior
Lovett and generalized polynomial-code comparisons for the same scope
limitation; their full proofs are not imported. Increasing the ambient
extension does not make the fixed prime-field labels indeterminates.

**Four-subspace transversals.** Abraham Martin del Campo Sanchez,
*Galois Groups of Schubert Problems*, August 2012 dissertation,
[III.D.1, printed pp. 29–30](https://franksottile.github.io/advising/martindelcampo.pdf#page=36),
was read through its graph/eigenvector argument. Four general
a-dimensional subspaces in dimension 2a have pairwise direct sums;
relative to the first two, the others are graphs of isomorphisms
phi_3,phi_4. Eigenlines of phi_4^(-1)phi_3 describe the transversal
two-planes. The source's exactly-a count requires distinct eigenvalues
in its generic split setting. L072's parallel classes motivate checking
this mechanism, but no graph matrices or eigenvalues were constructed.
Repeated eigenvalues, larger eigenspaces and field of definition cannot
be discarded. All remaining support constraints would still be required.

Frank Sottile, *Explicit Enumerative Geometry for the Real Grassmannian
of Lines in Projective Space*,
[alg-geom/9510017v1](https://arxiv.org/pdf/alg-geom/9510017v1#page=14),
31 October 1995, Section 7.1, printed pp. 14–15, was read including its
finite-field case. Three disjoint (a-1)-planes give a Segre family of
transversals; a general fourth plane meets it in a points. The displayed
construction chooses distinct points on P^1 and proves existence of
suitable configurations over fields of size at least a-1. That permits
chosen configurations, not a conclusion about L072's prescribed moment
spans. No generic four-solution count, splitting assertion or existence
claim is imported for H. The 1995 Section 7.1 locator is distinct from
the dissertation's reference to Section 8.1 of the later publication.

**Other reused exterior comparisons.** The October 5 overlap assessment
already inspected Gandini arXiv:1810.11694v3 Theorem 1.1, Proposition 6.1
and Theorems 7.3/7.5, and Boito–Ruatta SNC 2011 Section 3.2,
Proposition 2/Corollary 1 with proof. Their characteristic-zero regularity
and single-quotient gcd-rank conclusions do not supply the prescribed
simultaneous exterior rank in characteristic 97. No reduction or theorem
from them is imported. This ingredient-level comparison is reusable
without rereading large passages; its family-specific approval is not.

## Search record and source limits

Queries issued on 2026-10-12:

- `"Reed Solomon" "affine plane" supports`
- `"higher order MDS" fixed evaluation points Reed Solomon`
- `"rational normal curve" "line" "secant planes" finite field`
- `"affine plane" "Reed-Solomon" realization syndrome`
- `"affine plane" "exterior" "MDS"`
- `"Reed Solomon" "line transversals"`
- `"del Campo" "Galois Groups of Schubert Problems" pdf`
- `"affine plane" "syndrome" "pencil"`
- `"four subspaces" "transversal" eigenvectors`
- `"del Campo" "Galois Groups of Schubert Problems" thesis pdf`

Graph codes with RS constituents, affine-plane incidence parity checks,
decoder interpolation and selectable/random puncturing hits do not state
this simultaneous syndrome-pencil decision. Search snippets are screening
only. Roth's higher-order MDS paper, the newer relaxed-MDS paper and the
secant-preserver/Waring leads were not read at theorem level or imported;
none was identified as an essential matching statement. The primary
BGM, Sottile and del Campo PDFs were accessible. No essential identified
source blocker remains for this bounded local test. Previously blocked
ABF26/Jo inputs remain independent of the pinned-model family question;
this review does not certify them or retry their retrieval.

The bounded search did not establish a matching known exclusion or
construction. That licenses EXPLORE, not an originality claim.

## Approved bounded attempt and continuation/abandonment test

The unchanged TARGET now has EXPLORE coverage for one mathematical turn.
Start from L072's full explicit blocks and L010's actual moment columns;
use the already written L026 annihilator/alternating construction to seek
a labeling-independent quotient elimination. Prove every denominator and
nonzero coefficient needed. Fixed-H or eight-column independence may be
used as justified; neither abstract affine-plane automorphisms nor cyclic
label symmetry may be assumed to preserve moments. This review itself
derives no rank formula, obstruction, lemma or realization.

Continue this mechanism if it produces a complete uniform certificate,
an actual realization, or a new necessary condition with a specific
remaining closure test. An exact rank-deficient labeling abandons the
full-rank linear obstruction, not the realization target; retain its
kernel before considering decomposability and full recovery. If one
uniform elimination pass produces neither a new constraint nor a concrete
testable closure, record the failed inference and reassess rather than
replace universal proof with more positive-only samples.

Any claimed realization must retain arbitrary extension-field weights,
sixteen distinct original finite parameters, all four weights nonzero,
the full eight moments, nonzero-polynomial D and coordinate locators,
the complete L010 splitting/incidence criterion and same-support failure.
No projected solution alone suffices. An exclusion leaves other balanced
families, uniform triangle twelve, universal extraction and challenge
qualifications unresolved. Mathlib coverage of this exact family decision
is **not checked**; unknown availability is not absence. No known theorem
is being reproved and no new lemma or mathematical script was written.
