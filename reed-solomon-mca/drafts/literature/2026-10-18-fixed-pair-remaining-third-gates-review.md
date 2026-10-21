# Remaining-third gate census: completed source comparison

TARGET: Assess a complete gated four-row compatibility census for the remaining pairwise-linear third supports extending L112's fixed pair at t=0 equality.
CHECKED: 2026-10-18
DECISION: EXPLORE
SEARCH_EVIDENCE: Reused the thirteen-query seven-coordinate comparison and inspected Hall/shortening extracts; compared L109/L111/L112 and ATTEMPTS/041; four new targeted algorithm/theorem queries located the primary Stacks and Magma passages identified below, without a matching fixed-pair count.
SOURCE_EVIDENCE: Reused Hall Theorem 5.1.1 pp. 63–64, https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf , and Marquez-Corbella–Pellikaan accepted manuscript 2016-02-29 section 5 pp. 7–8, https://pure.tue.nl/ws/files/93073933/16_02_29_ECP_MDS.pdf ; read Stacks Theorem 10.34.1(1), tag 00FS, https://stacks.math.columbia.edu/tag/00FS , and Magma V2.29 2026-08-03 exact ideal-coordinate and variety documentation, https://magma.maths.usyd.edu.au/magma/handbook/text/1314 and https://magma.maths.usyd.edu.au/magma/handbook/text/1325 .
COMPARISON: L109 already retains all kernel dimensions and exact necessary gates; L112 solves only its specific points/lines. Standard ideal certificates cover arbitrary-dimensional algebraic exclusions, but neither they nor the reused coding sources give a fixed-pair bound or a practical complete remaining-third solver.
GAP: Test one explicit nondisjoint-third profile, retaining complete kernels, all Plucker equations and every gate over extensions; any unsolved locus remains unresolved rather than excluded or counted as a recovery.
REASON: Source scope is adequate for the bounded diagnostic COVERED_TARGET below; the full remaining-third feasibility census is deferred because no bounded all-locus solver has been demonstrated. This approves a later attempt, not a new mathematical conclusion or its novelty.
SCOPE: F_(97^20), fixed H and S={1,8,12,18,22,27,33}, k=8, pinned event, actual D/locators nonzero, arbitrary extension weights and prescribed original chart, t=0 equality, A1={1,8,47,50}, A2={12,18,64,70}; no universal fixed-pair occurrence is assumed.
COVERED_TARGET: Test all pairwise-linear fourth supports extending A1={1,8,47,50}, A2={12,18,64,70}, A3={1,22,75,79} by L109's full gates, preserving every unresolved extension-field kernel locus.

LITERATURE_REASON: The proposed continuation changes from the disjoint-third audit to a complete remaining-third compatibility census; compare this expanded support-profile hypothesis with the saved source coverage before approving dependent work.

## Completed comparison, 2026-10-18, step 306

The main gap is still sixteen versus fifteen, with global interval
11/q–16/q. The intermediate target is now one complete fourth-row
diagnostic for the explicitly named third support in COVERED_TARGET.
Its plausible downstream use is to exclude this conditional equality
profile if every possible fourth row fails, or identify an exact residual
locus requiring simultaneous fifth-row constraints. No universal
occurrence of this fixed pair or third support is asserted. The broader
remaining-third question in TARGET is preserved as the question reviewed;
only the stated slice is authorized for the next mathematical attempt.

This is LITERATURE / NOVELTY_UNCHECKED / EXPLORATION: a changed-scope
comparison and a bounded continuation, with no rank calculation, new
lemma, bound, mathematical script or claim beyond inspected sources.
Mathematical exploration usage remains zero. Separate supervisor
approval of this newly written ready continuation precedes calculation.

### Reused inputs, duplicates and failure evidence

Read the completed seven-coordinate assessment
`2026-10-17-seven-coordinate-syndrome-bound-review.md`, the primary
extractions in `2026-10-05-two-block-moment-obstruction.md` and
`2026-10-07-six-coordinate-triple-equality-obstruction.md`, and the
direct-source recovery in `2026-10-18-residual-kernel-gate-audit-review.md`.
Hall's field, distinct-label, nonzero-multiplier and dimension hypotheses
remain unchanged. The existing shortening application deletes precisely
J minus K, seven labels, leaving dimension one and nonzero retained
multipliers. Changing intersections among selected supports does not
change that row-wise source application. These standard inputs are
imported by the precise citations above; no reproof is justified.

L109's hypotheses, complete necessary gate argument and converse
qualifications were read, together with L111's classification and
equality-transfer passages, and L112's complete projective and weight-gate
argument. L109 applies to arbitrary selected two-overlap supports; it
does not require a disjoint third row. L111/L112 require that disjointness
for their finite coverage. Consequently their certificates do not decide
the COVERED_TARGET. The saved seven-coordinate comparison already checks
stronger MCA ray/circuit results: their all-error support-confinement
hypothesis is still absent. No unchanged general MCA search is repeated.

ATTEMPTS/041 preserves actual deficient, pairwise-linear stacks and
invalidates uniform rank-only extrapolation. L112 subsequently excludes
those particular loci by weight gates, without converting rank deficiency
into sufficient compatibility. This diagnostic changes the tested support
profile and keeps the same exact gate mechanism; it does not reopen the
false rank-only claim. No local duplicate of the named nondisjoint slice
was found in this focused comparison. Search absence is not novelty.

### New primary algorithm coverage and limitations

The Stacks Project, *Commutative Algebra*, Theorem 10.34.1(1),
[tag 00FS](https://stacks.math.columbia.edu/tag/00FS), inspected online
2026-10-18, allows any field and any finite-type algebra. Its maximal
residue fields are finite extensions. Read its statement and induction
proof, including both contraction cases. This supplies the usual weak
Nullstellensatz over an algebraic closure. It imposes neither
zero-dimensionality nor characteristic zero. It provides no bound on
computational cost and no rational-point descent. A proper ideal over
F_97 alone does not assert a point over F_(97^20).

University of Sydney Computational Algebra Group, *Magma Handbook*,
V2.29, 3 August 2026, [Gröbner bases](https://magma.maths.usyd.edu.au/magma/handbook/text/1314):
read `Coordinates`, `CoordinateMatrix`, `NormalForm`, example H115E9
and the degree-truncation warning. Fixed original generators permit
exporting an identity for 1; checking it requires exact polynomial
multiplication. A truncated computation on an inhomogeneous ideal has
no advertised completeness guarantee. These are implementation references,
not a theorem about the present support matrices or evidence that Magma
is locally installed or licensed.

The same handbook's [Computation of Varieties](https://magma.maths.usyd.edu.au/magma/handbook/text/1325),
introductory hypotheses, `Variety(I,L)` and example H116E3, distinguishes
solutions over the coefficient field from solutions over an explicitly
specified extension. The example has more geometric solutions than
base-field solutions. Finite-field higher-dimensional ideals are allowed;
this asserts no feasible cost at the present field size. Do not use a
base-field variety call as an extension-field exclusion.

Also inspected the official [First Operations on Ideals](https://docs.magma-maths.org/CommutativeAlgebra/PolynomialRingIdealOperations/ideal-operation.html),
`ColonIdeal(I,f)`, `Saturation(I,f)` and `IsProper` descriptions, online
2026-10-18. They specify saturation by powers of f and its computation
using an auxiliary inverse equation, rather than a single ideal quotient.
This is standard coverage for nonzero gates. No specialized saturated
ideal or new gate polynomial is derived in this source review.

Four new queries were executed: `site.magma.maths.usyd.edu.au handbook
Groebner basis saturation ideal variety finite field`;
`site.math.uchicago.edu Plucker relations Grassmannian decomposable
coordinates notes`; `site.stacks.math.columbia.edu Hilbert Nullstellensatz
finite type field algebraically closed maximal ideal`;
`site.magma.maths.usyd.edu.au "GroebnerBasis" "Representation"
"coordinates" ideal`. General Grassmannian and unrelated algebra leads
were not imported. L109 already proves the exact characteristic-97
Plucker reconstruction needed here; an unread complex-geometric lead is
unnecessary. No matching fixed-pair theorem was inspected.

### One bounded diagnostic and its test

Fix the A3 in COVERED_TARGET; enumerate the existing 756 two-overlap
support choices for A4 and retain precisely distinct pairwise-linear
choices against A1,A2,A3. Prove exact case-set coverage and keep excluded
incidence cases separate. Reuse the audited block construction, but
certify each rank and each complete kernel independently. Import prior
audited coverage only when the actual support family matches it; do not
assume an H-label symmetry.

For every deficient kernel retain all 35 homogeneous Plucker equations
in all kernel coordinates. L109's reconstruction and row gates, rather
than a new four-row converse, are the mathematical specification. Use
complete affine chart coverage for nonzero projective coordinates, keep
all row-projection pivot branches and their nonzero conditions, and
retain lambda, both overlap weights and prescribed finite directions.
Any polynomial encoding of those gates must be justified and checked in
the later research step; no such encoding is certified here. Rank-zero
projection is a rejected branch under L109's actual nonpersistence
hypothesis, not a silently inverted pivot.

A point/line may be solved exactly only with complete homogeneous root
coverage, including infinity, identically zero equations and nonprime
roots. L112's s*t pattern must not be assumed for new kernels. For any
dimension, an exact identity expressing 1 in the appropriate chart/gate
ideal is an admissible exclusion certificate; verify it against original
generators. An identity excludes over every extension. A nonunit ideal,
incomplete reduction or resource cap is unresolved. Any explicit survivor
needs an actual field representation and all original gates checked;
geometric existence alone is not existence in the prescribed field or
chart. Save full unsolved equations and complete bases for all such cases,
including positive-dimensional loci. Do not sample F_97 and declare
completeness. The bounded diagnostic may legitimately finish with an
unresolved bucket instead of a feasibility classification.

Continue if this yields complete conditional exclusion, a checked local
survivor, or an exact smaller unresolved locus with a discriminating next
test. If a larger locus defeats the bounded algebraic method, stop that
solver path and preserve the first explicit unresolved support family;
do not launch an unrestricted all-third sweep or repeat rank-only tests.
Only if every eligible actual fourth is excluded can this A3 profile be
excluded using L109's 12–14 rows and audited L086. Four local compatible
rows do not give sixteen events, t=0, actual nonpersistence, or L109's
r>=6 converse.

Essential inputs: audited L086/L109/L111/L112 and inherited L010/L103/L104
finite-certificate qualifications. The named fixed S, pair, A3 and t=0
equality are conditional assumptions. Arbitrary extension weights,
original chart, all full-weight gates and lower-rank loci remain in
scope. Arbitrary pairs and seven-sets, universal representation, other
t profiles and challenge-definition qualifications remain open. Full
matching Mathlib coverage is not checked; no absence is inferred.

## Original proposal from step 305 (preserved, superseded above)

This is a proposed assessment, not a ready authorization. No previously
uncovered mathematics is derived or approved in step 305. Reuse adequate
primary-source extractions and comparisons; do not repeat browsing without
an essential unread theorem case or specific new relevant lead.

The main gap remains sixteen versus fifteen. The prospective intermediate
target is a complete necessary four-row gate census conditional on the
fixed pair. Its downstream use is to decide whether that fixed-pair class
can survive 12–14 simultaneous two-overlap rows. Four compatible rows
alone imply neither equality nor L109's r>=6 converse. A complete fixed-pair
exclusion would still leave arbitrary fixed pairs, seven-sets, t=1,2,
universal representation and challenge qualifications unresolved.

Essential local inputs are audited L086, L109, L111 and L112, with inherited
L010/L103/L104 qualifications. ATTEMPTS/041 forbids uniform rank-only
extrapolation. Preserve every deficient kernel; kernels larger than the
ones in L112 must retain their full algebraic Plucker locus, rather than
base-field sampling. L112's lambda-zero rejection is chart invariant,
but a surviving new plane must retain all full-weight and original finite
direction gates. No assumption of rational extension-field weights is allowed.

Continue to a bounded mathematical census only after the literature turn
has verified that the source scope covers this exact mechanism and has
specified a case-complete handling or bounded diagnostic for larger
kernels. If no defensible extension-field coverage method is available,
narrow to one explicitly named support profile before approval. Repeating
a rank-only test or inferring a global bound from a fixed seed is not a
continuation. This turn does not test or decide feasibility of the proposed
remaining-third families. Full matching Mathlib coverage is not checked.
