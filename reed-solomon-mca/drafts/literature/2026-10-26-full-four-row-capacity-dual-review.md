# Full-locus capacity mechanism — completed source comparison

TARGET: Assess a stratified nonnegative support-weight certificate for excluding twelve degree-four rows on the full original four-row locus (35,522,477,566).
CHECKED: 2026-10-26
DECISION: EXPLORE
SEARCH_EVIDENCE: Step 514 searched fractional hypergraph capacity/cover duality, determinantal rank stratification, exact quadruple terminology and their Reed–Solomon combinations; compared the specified local maps, fixed-family results and failed rank/encoding routes. Queries, primary passages and limitations are below; no novelty inferred.
SOURCE_EVIDENCE: Boyd–Vandenberghe, Convex Optimization (2004), sections 5.1.3 and 5.2.1–5.2.3, printed pp. 216,224–227; Stacks Lemma 27.22.1 Tag 089T, Lemmas 15.8.4(3)/15.8.7 Tags 07ZA/07ZC, and Theorem 10.34.1 Tag 00FV, live versions inspected 2026-10-26; reuse the recorded arbitrary-field/exact-polynomial coverage identified below.
COMPARISON: Known finite LP duality covers coordinate-weight certificates and fractional obstructions for a fixed support mask; known rank and Grassmannian tools cover all characteristic-97 planes. None of the inspected sources identifies this full four-row locus or proves a capacity bound below eight on all its realizable masks. L164 covers only one family.
GAP: Obtain a complete geometric cover with exact sub-eight coordinate-weight certificates, or an exact realizable plane/stratum carrying a fractional packing of size at least eight; neither is supplied here. A merely possible support mask is not a realizable obstruction.
REASON: Essential method coverage now supports one bounded full-locus mechanism test, with exact rank-zero/boundary and realizability obligations. This literature-only step establishes no new bound, locus calculation or lemma; a new ready continuation is recorded separately for approval next turn.
LITERATURE_REASON: The incoming REVIEW_REQUIRED target changes from fixed-family integer capacity to a uniform geometric-stratum certificate; existing coverage lacks this exact duality/rank-stratum comparison.
SCOPE: Source comparison for precisely L109's original S/J/maps and quadruple (35,522,477,566), E the algebraic closure of F_97, all four restricted ranks exactly one, original eligible additional labels, degree-four residual capacities and nonnegative coordinate weights only. No coding sufficiency, other quadruple, genericity, finite-field descent or uniform challenge assertion.

## Proposed bounded target and relevance

The unresolved gap is uniform twelve-row exclusion. The proposed test
keeps the exact original S/J, maps and four labels, but would allow
nonnegative support weights to depend on the rank stratum of the plane.
The desired certificate would cover every additional eligible rank-one
support with weight at least one while assigning total residual
degree-four capacity strictly below eight. This is a proposed certificate
specification, not an established inequality or mathematical result.
The full four-row locus has not been identified with L162's family.

The comparison below supports a bounded test, not a proof or practical
complexity guarantee. Continue with a complete cover and strict bound,
or stop the pure coordinate-weight mechanism with a realized fractional
obstruction. An incomplete cover is only exploration. Do not retry the
fixed-family construction, unconditional finiteness, or an unchanged
large feasibility encoding. Coding realization, arbitrary representation,
source identification and sharp radius remain independent gaps.

## Inspected primary results and applicability

S. Boyd and L. Vandenberghe, *Convex Optimization*, Cambridge University
Press, 2004, [author PDF](https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf),
714-page online file inspected 2026-10-26: section 5.1.3 p. 216 gives
the feasible-multiplier bound; section 5.2.1 pp. 224–225 derives standard
and inequality LP duals; sections 5.2.2–5.2.3 pp. 225–227 state weak
duality and strong duality with the refined affine Slater condition
and dual attainment. The refinement permits nonstrict affine constraints,
including zero capacities. Read both LP sign conventions and the
feasibility/finite-value qualifications. For a finite incidence matrix A
and nonnegative residual capacities b, the standard pair is

    maximize 1^T x,  Ax<=b, x>=0;
    minimize b^T w,  A^T w>=1, w>=0.

The later instance must check feasibility and boundedness before invoking
strong duality. Weak duality alone checks an exhibited certificate or
packing. No LP theorem needs reproof. This pure coordinate dual has no
edge prices; adding x<=1 or pair conflicts changes its dual. Rational
witnesses must be checked exactly, not accepted from a floating solver.
The source does not decide a geometric mask or the threshold eight.

Stacks Project, [Lemma 27.22.1, Tag 089T](https://stacks.math.columbia.edu/tag/089T),
live version inspected 2026-10-26: read the full chart construction,
base-change check and final covering argument. It constructs affine
charts of dimension k(n-k) over Z and proves they cover. Its convention
G(k,n) uses rank-(n-k) quotients, hence rank-k kernels. Take k=2,n=7
for planes in E^7; characteristic 97 is allowed. A later use of basis
charts must justify that convention and retain every pivot boundary.
Alternatively audited C155a supplies the original disjoint-pair product
of projective planes, with field-valued exhaustion; no scheme equality
or general-position assumption is needed or inferred.

Stacks Project, [section 15.8](https://stacks.math.columbia.edu/tag/07Z6),
Lemmas 15.8.4(3) and [15.8.7, Tag 07ZC](https://stacks.math.columbia.edu/tag/07ZC),
live version inspected 2026-10-26: read the minors definition,
base-change proof and residue-field dimension criterion with its proof.
These support determinantal rank tests on chart coordinate rings over
F_97. For the actual four-by-two restricted matrix, rank at most one
uses its two-by-two minors, and rank zero uses all entries. Exact rank
one requires the first condition and exclusion of the second. No
characteristic-zero smoothness, reducedness, or constant-rank assumption
is imported. These tools describe strata but do not compute them here.

Stacks Project, [Theorem 10.34.1, Tag 00FV](https://stacks.math.columbia.edu/tag/00FV),
live version inspected 2026-10-26: read the complete statement and both
proof cases, including localization in part (2). For a finite-type
algebra over the algebraically closed E, a proper ideal has an E-valued
point. A unit-ideal identity can therefore certify an empty affine
branch. Nonzero conditions must first be represented by legitimate
principal-open/inverse branches; no denominator may be silently removed.
This provides neither a degree bound for a certificate nor efficient
elimination. A proper ideal over F_97 is not a point over F_(97^20).

Reuse the already inspected arbitrary-field linear/exterior geometry in
`2026-10-25-l155-segre-locus-and-projection-ranks-review.md` and
`2026-10-25-four-row-finiteness-review.md`, and the exact nonzero-atom
coverage of Gao–Platzer–Clarke, CAI 2011, Theorem 4.1 and Lemmas
4.1–4.2, recorded in `2026-10-25-twelve-row-gated-feasibility-review.md`.
The latter's F_q field equations are not imposed on E-valued planes.
The existing SCIP finite-capacity and Eppstein–Loffler–Strash enumeration
coverage in `2026-10-26-l163-forty-support-compatibility-review.md`
remains adequate for incidence bookkeeping; neither supplies the new
full-locus conclusion. Full matching Mathlib coverage is not checked.

## Search and stronger-result comparison

Queries included `fractional hypergraph matching vertex cover linear
programming duality theorem nonnegative weights capacities`,
`Stacks project determinantal rank loci minors locally closed rank
stratification`, `"stratified" "fractional" "rank" "Reed-Solomon"`,
`"support weights" "Reed-Solomon" capacity`,
`"four-row" "35" "522" "477" "566"`,
`"determinantal" "fractional matching" algebraic`,
`"rank stratification" "linear programming" certificate`, and
`"fractional matching" "Reed-Solomon"`. These bounded searches located
standard fractional packing terminology and general tools, without an
inspected theorem deciding the exact target. Failed exact-term searches
do not establish originality.

The search also located *Dynamic algorithms via the primal-dual method*
(2018), DOI 10.1016/j.ic.2018.02.005, with bounded-edge-multiplicity
fractional hypergraph packing, and coded-storage service-region work.
These are leads, not theorem-level inputs: full relevant proofs were
not inspected. Boyd–Vandenberghe already supplies the essential finite
duality, so these leads create no source blocker or reason to browse
again before the bounded attempt. No dynamic approximation guarantee,
rounding theorem or storage recovery-set theorem is used. In particular
an integrality or graph matching theorem cannot be assumed for these
four-element supports. Reuse the stronger coding/subspace-design
comparison in the October 25 gated-feasibility review: constructed
evaluation sets and generic-position hypotheses are not established for
these frozen original labels. No unread classification is imported.

## Local duplicates and recorded failures

Read L109's full quotient-map and gate reduction, C155a's hypotheses,
conclusion and imported-geometry scope, L162's actual maps and family
statement, L163's eligibility/forty-label statement and certificate
method, and L164's complete incidence proof and audit. L163's 112-label
eligibility enumeration depends only on the four supports, so it can be
reused; its rank-one mask B applies only to L162's family. No census
certificate or audit was rerun in this literature turn.

Read ATTEMPTS/048–049 and /052–053. The first stops rank-only pair
stratification: equal ranks do not identify kernels or later-row loci.
The second stops passed-input audit/large-encoding repetition without
a solving test. L154's formula specifies all gates but solves none.
ATTEMPTS/052 preserves L162's actual infinite family, so no full-locus
argument may assume finiteness. ATTEMPTS/053 stops twelve-row use of
that family, with the canonical separately audited result in L164;
its historical pending-audit sentence is superseded by L164, not a new
reason to repeat the audit.

L159 and L160's statement ranges were compared as possible structural
leads: coincident kernel lines and an exceptional pencil are separated.
They have no independent critical audit and are not established premises
of this proposed attempt. A later full-locus argument may use audited
C155a and original maps directly; using either unaudited reduction as a
load-bearing input would require its own prior review. L162's family
is not asserted to be the exceptional component's complete locus here.

The materially different mechanism is a geometric restriction on which
supports can coexist at one plane, paired with ordinary nonnegative
capacity duality. Reweighting L164's same B, merely counting a new
formula, collecting generic ranks, or enumerating sampled base-field
planes would duplicate exhausted work rather than test this mechanism.

## Later attempt: exact evidence contract

The new continuation assessment is
`2026-10-26-full-four-row-capacity-dual-attempt-review.md`; it is ready
but must receive the supervisor's separate approval next turn. The
following specifies proposed work, not a result proved in this review.

For a plane L on the full locus, the relevant mask consists of all
eligible labels j with rank(Q_j|L)=1. A proposed stratum may use a
certified superset of that mask for a positive upper bound. The residual
capacity at z is b_z=4 minus its incidence count in all four fixed rows.
Seek w_z>=0 covering every available support to weight at least one,
with sum_z b_z*w_z<8. The entire claimed geometric cover, all boundaries
and every original eligible label must be justified. Disjoint strata
are unnecessary, but coverage is essential. No common uniform margin
is assumed; every certified bound must itself be strictly below eight.

For a negative method verdict, give an exact plane (or proven nonempty
stratum with a guaranteed mask), its four exact ranks and a rational
x>=0 on available labels satisfying Ax<=b and 1^T x>=8. A hypothetical
mask or a fractional packing on a superset is insufficient. Such a
witness blocks this pure coordinate certificate at that plane, even
if binary selection, mutual compatibility or coding gates fail. It
does not construct twelve distinct rows or refute the challenge.

Rank zero at an unselected additional row must not discard a plane.
If using exact masks, a label absent from the rank-one mask may have
rank zero OR two; treating every absence as a nonzero minor loses a
branch. Pair conflicts may help separate future geometric strata, but
must not silently enter this pure coordinate dual as extra multipliers.
The LP quantities are rational/real, not finite-field inequalities.

Bound the next attempt to at most three explicitly stated structural
cover/obstruction hypotheses on this one quadruple. Save residual loci
and unfinished reasoning before lengthy algebra. Do not launch all-mask,
all-quadruple or unrestricted elimination sweeps. If no complete cover
or realized obstruction emerges, record the first unresolved branch and
an honest exploration outcome; failure of three guessed weights alone
does not disprove every stratified certificate.
