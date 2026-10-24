# Proposed two-distance capacitated triangle test

TARGET: Test whether any signed edge weight supported on half-distances 5 and 6 separates L098's demands from the triangle cone with capacities min(c_i,c_j,c_h), retaining every actual source orbit.
CHECKED: 2026-10-22
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the weighted-triangle and invariant-cone assessments; checked ATTEMPTS/081–082,088–091 and local box/two-distance references; searched capacitated fractional triangle decomposition linear programming dual edge weights upper bounds and Boyd box-constrained LP duality. No inspected result evaluates these fixed demands.
SOURCE_EVIDENCE: Schrijver III.B (62)–(65), printed p.7, including the explanation after (65); Boyd–Vandenberghe Convex Optimization (2004), Section 5.7.3 Example 5.9 (5.68)–(5.71), pp.257–258, and Section 5.8.1 pp.258–259; reused foundations/12,13 and prior weighted Farkas/averaging assessment.
COMPARISON: L105 relaxes contractions independently, whereas this proposed dual would retain shared triangle variables and their upper capacities; L108's cone verdict explicitly discards capacities. L106's restricted primal support and the stopped full-variable numerical prescription are different tests.
GAP: Prove the local capacitated necessity and exact unordered orbit accounting, then exhaust the two-weight piecewise-linear test; no separator, nonseparation verdict or full source lift is supplied by the citations.
REASON: Primary box-LP dual coverage now supports one separate exact mathematical attempt adding capacities absent from L108; only the local specialization and finite verdict remain to be done.

SCOPE: One two-weight signed edge test, zero outside half-distances 5 and 6, with all actual source orbits and upper capacities; no full-variable solve, additional weight support or primal distance-only identification.
LITERATURE_REASON: The startup target was REVIEW_REQUIRED for the newly added upper capacities and bounded exact test; this review fills those omissions rather than refreshing unchanged ready coverage.

## Completed source approval — step 406

The main gap is arbitrary-center safety at 68/67 agreements. The exact
TARGET above is the intermediate target. A separator could reject L098's
fixed pairs; nonseparation would stop only this restricted diagnostic.
Remaining Boolean lower rows, full scalar/cardinality feasibility, PSD,
other pair prescriptions and RS realization are independent open gaps.

### Primary imports and qualifications

Boyd and Vandenberghe, *Convex Optimization*, Cambridge University Press
(2004), [author PDF](https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf),
Section 5.7.3, Example 5.9, (5.68)–(5.71), printed pp.257–258:
finite real equality-constrained LPs with box bounds have an explicit
piecewise-linear dual obtained by minimizing separately over each bound
interval. Both the multiplier form and full coordinatewise minimization
were read. The example assumes strictly separated endpoints; eliminate
fixed zero-capacity coordinates before invoking that form. Section 5.8.1,
pp.258–259, gives the zero-objective feasibility formulation, positive
homogeneity and weak-duality certificate implication. These provide the
method, not a verdict for this instance. No SDP strict feasibility is
required for a weak-duality certificate.

Schrijver, *New code upper bounds from the Terwilliger algebra and
semidefinite programming*, IEEE TIT 51 (2005), 2859–2866,
DOI 10.1109/TIT.2005.851748,
[author manuscript](https://homepages.cwi.nl/~lex/files/codes.pdf),
III.B (62)–(65), printed p.7, was reinspected including the complete
explanation after (65). It supplies actual triple normalization,
nonnegative upper rows, distance zeros and permutation equalities
preserving t-s. Its proof explanation uses triple counting and
symmetric difference, not just the three pair distances. Retain
foundations/04's impossible-orbit and unused-(61)-prefactor qualifications.

Reuse the primary fixed-cardinality and indicator coverage in
foundations/12,13, and the Farkas and finite averaging source comparison
in `drafts/literature/2026-10-21-distance-dependent-triangle-dual.md`.
No further decomposition existence theorem is needed. The earlier
weighted theorem has no prescribed capacities, and L107 already stops
its common-normalization application. Search results about capacitated
b-matching and an unverified theorem aggregator were not imported.
No search establishes originality or full absence of a matching theorem.

### Local applicability to be justified in the research turn

Essential inputs are L021,L098,L105,L107,L108 and foundations/04,12,13.
L098 fixes N=floor(65537^28/2^128)+1, H=binomial(1024,68), and c_i.
Its proof of the homogeneous contraction and G=g_i D was read, together
with L105's complete scalar interval argument and L107's repetition and
unordered-edge audit. Those supply the existing ingredients for a new
necessity specialization; that specialization is not proved this turn.

Keep the two distinct repeated third supports, each contributing c_i
for i>0, before using distinct-triangle demands (N-2)c_i. At i=0 do not
subtract twice: it is the objective identity. Distinct edges have counts
H*g_i/2, g_i=binomial(68,i)binomial(956,i). Each distinct unordered
triangle has six ordered presentations, including when distances agree;
count presentations, not six distinct index keys. The research proof
must establish its multiplicity formula from the actual set orbits.
L105 already establishes upper=min(c_i,c_j,c_h) from the six presented
bounds. Dropping its lower rows gives a relaxation; upper capacities
alone do not give the full scalar system.

Retain every actual (i,j,t,s), h=i+j-t-s, both null and permitted edges,
and the unchanged t-s-preserving source classes. A null edge forces its
incident triangle capacity to zero, not removal of that source input.
A sum of independent box support contributions may collect equal
coefficients only after all orbit multiplicities have been justified.
That arithmetic collection does not identify distinct primal variables.
No converse source-lift or representing distribution is assumed.

### Bounded test and stopping condition

The next research turn may specialize the cited box dual with signed
edge weights only at distances 5 and 6. Prove its sign convention and
normalization first. Then partition the two-weight plane by the zero
sets of actual triangle-weight sums, intersect with a compact nonzero
homogeneous normalization, and evaluate the resulting linear pieces
exactly. Include boundaries, both signs, axes and the zero vector.
This is a proposed finite test procedure justified by the source's
piecewise-linear form; the local break lines, exhaustive candidate set
and all values must be established in that research turn. Do not assume
that a numerical sample or a single unsuccessful separator is exhaustive.

Bound the work to one enumeration of the 1,500,625 original ordered
entries, one complete six-presentation/multiplicity verification, and
one exact normalized two-weight evaluation. A certificate must save the
full relevant orbit accounting, rational inputs, candidate coverage and
actual-versus-required separation margins under scripts/finite-support/;
print only concise results and paths. The research turn may use a
symbolic proof of nonseparation if it covers the whole normalized domain.
Stop after this test. If its normalization or enumeration cannot be
certified within this scope, save the precise obstruction and return
inconclusive; do not enlarge support or restart ATTEMPTS/082.

Strict certified separation continues the fixed-pair exclusion route.
A complete nonseparation verdict parks this two-distance test only.
Neither gives RS safety/unsafety or changes 955–957. L105's independent
rows, L106's restricted primal, L107's sufficient theorem and L108's
uncapacitated cone are distinct stopped tests; their evidence is retained.
The exhausted translated-pole route remains 3/3.

Mathlib: full matching capacitated triangle and two-weight specialization
coverage is not checked; supporting LP duality and finite orbit counting
coverage is not checked. Unknown availability is not evidence of absence.
No theorem was reproved and no new lemma or mathematical script was
written or run during this literature-only step. The local argument and
finite verdict remain work for a separate research invocation.
