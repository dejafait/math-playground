# First rank-19 factor-filter residual — completed scope comparison

TARGET: Test L109's full extension-field gates on the rank-19 L116 residual (n,u)=(0,279), with A3={1,12,75,79} and A4={8,18,75,85}.
CHECKED: 2026-10-18
DECISION: EXPLORE
SEARCH_EVIDENCE: Reused step-288 thirteen-query seven-coordinate discovery and step-306 four-query algebraic-method comparison; searched exact index/support and rank-19 strings in October 18 assessments, histories 310–329 and ATTEMPTS/041–042; read L109's complete necessary gates, L112's projective-line proof, L115's whole-locus proof and L116's scope/overlap limitations. Only the proposal and step-321 audit history matched this exact target in that search.
SOURCE_EVIDENCE: Read saved primary extractions: Hall, Notes on Coding Theory, Theorem 5.1.1 and full proof pp. 63–64, https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf ; Marquez-Corbella–Pellikaan, accepted manuscript 2016-02-29, section 5 pp. 7–8, https://pure.tue.nl/ws/files/93073933/16_02_29_ECP_MDS.pdf ; Stacks Theorem 10.34.1(1), https://stacks.math.columbia.edu/tag/00FS ; Magma V2.29 exact-certificate and variety references below. Reused inspected stronger-result comparisons; no fresh external retrieval or source-freshness claim.
COMPARISON: L109 covers arbitrary selected rows and kernel dimensions with explicit extension-field, projection, weight and prescribed-chart gates. L112 resolves different two-dimensional kernels; its specific quadratic zero sets cannot be assumed here. L115/L116 exclude whole coordinate-factor kernels in their stated domains, while this occurrence is a recorded filter failure. No inspected source or local result settles its full gate locus.
GAP: Resolve the complete homogeneous decomposable locus of this one complete rank-19 kernel and all necessary row gates, including rank-zero branches and arbitrary original charts; exact feasibility or exclusion remains uncomputed.
REASON: Existing theorem and algebraic-method coverage is adequate for this changed exact locus. Approve one bounded diagnostic, with no claim of feasibility, exclusion, originality or a global count.
SCOPE: F_(97^20), fixed order-sixteen H, k=8, pinned event, S={1,8,12,18,22,27,33}, A1={1,8,47,50}, A2={12,18,64,70}, A3={1,12,75,79}, A4={8,18,75,85}; sixteen actual finite errors, nonzero D/locators and t=0, arbitrary extension weights and prescribed original chart; inherited L010/L103/L104 and L086/L109 computational qualifications.
LITERATURE_REASON: The newly proposed one-occurrence projective gate test is outside the exhausted whole-kernel factor filter and needs an exact-scope comparison; reuse adequate inspected sources rather than repeat discovery browsing.

## Completed comparison — step 322

The main gap is exclusion or realization of sixteen bad parameters,
with current interval 11/q–16/q. The intermediate target is exactly
TARGET. Removing one indexed occurrence could establish a whole-locus
mechanism for residual kernels; a checked survivor could instead locate
an obstruction that requires additional simultaneous rows. Neither
outcome alone excludes its third, fixed pair or arbitrary t=0 profile.
Universal representation, seven-set/pair extraction and challenge
qualifications remain independent gaps.

### Primary statements, hypotheses and reuse

Read the saved primary extraction in
`2026-10-05-two-block-moment-obstruction.md`, Primary theorem and
applicability. Hall's undated author-hosted GRS chapter, Theorem 5.1.1,
printed pp. 63–64, permits any field, distinct evaluation points,
nonzero multipliers and 0<k<=n. It gives dimension k and distance n-k+1;
the inspected proof covers the root bound and an attaining product
polynomial. The sixteen distinct H labels, unit multipliers and k=8
meet these hypotheses over the full extension. Import by citation
through L104/L109, without reproof.

Read `2026-10-07-six-coordinate-triple-equality-obstruction.md`, Primary
shortening input. I. Marquez-Corbella and R. Pellikaan, *A characterization
of MDS codes that have an error correcting pair*, FFAA 40 (2016),
224–245, DOI https://doi.org/10.1016/j.ffa.2016.04.004, accepted
manuscript February 29, 2016, section 5, Definitions 5.1–5.2, Lemma 5.3
and the following unnumbered GRS formula, printed pp. 7–8: shortening
at a_n gives GRS_(k-1)(a',b'*(a'-a_n)). The formula has no separate
detailed proof in that passage; the general MDS parameter lemma is
not substituted for it. Each L109 row shortens exactly J minus K_j,
seven distinct labels, leaving dimension one. Successive shortenings
retain positive dimension and nonzero products of label differences.
Changing A3/A4 changes none of these hypotheses. No new shortening
proof or new recovery criterion is needed.

Reuse `2026-10-17-seven-coordinate-syndrome-bound-review.md`: thirteen
recorded queries, the inspected BCHKS November 11, 2025 author version,
Theorems 1.3 and 4.6, printed pp. 8 and 28–29, and Chojecki author TeX
v9.2 dated July 17, 2026, statements and proof cases lines 1244–1460.
The saved BCHKS sharp endpoint is below this cell and its wider bound
exceeds sixteen. The inspected ray/circuit results confine all selected
error supports to a fixed union; coefficient-syndrome membership in U_S
does not supply that premise. No matching residual exclusion is imported.
Unread ABF26/ePrint leads remain unimported and are not essential to
this restricted test. Source versions are reused, not freshly verified.

Read step-306's saved primary extraction in
`2026-10-18-fixed-pair-remaining-third-gates-review.md`, New primary
algorithm coverage and limitations. Stacks Project, Commutative Algebra,
Theorem 10.34.1(1), tag 00FS, allows any field and finite-type algebra;
its inspected induction includes both contraction cases. It supplies
no prescribed-degree descent or practical cost bound. A proper ideal
over F_97 does not establish a point in F_(97^20).

Magma Handbook V2.29, August 3, 2026, Gröbner bases,
https://magma.maths.usyd.edu.au/magma/handbook/text/1314 ,
`Coordinates`, `CoordinateMatrix`, `NormalForm`, H115E9 and the
truncation warning; Computation of Varieties,
https://magma.maths.usyd.edu.au/magma/handbook/text/1325 ,
`Variety(I,L)` and H116E3; First Operations on Ideals,
https://docs.magma-maths.org/CommutativeAlgebra/PolynomialRingIdealOperations/ideal-operation.html ,
`ColonIdeal`, `Saturation`, `IsProper`: reuse those inspected passages.
They distinguish exact identities, specified extension points and
saturation from incomplete reductions or a single quotient. They do
not certify a local installation, license or a result for this kernel.
No particular solver is required. L109 already proves the needed
characteristic-97 Plucker reconstruction; no unread geometric source
is essential. Full matching Mathlib coverage is not checked.

### Exact local comparison and bounded continuation

Essential inputs are audited L109 necessary gates, audited L116's
partition, audited L114's complete kernel provenance and audited L086
eligibility; retain L010/L103/L104 qualifications. L112 and L115 are
mechanism comparisons. The selected full record was read with the
JSON inspector at `scripts/seven-coordinate/residual-coordinate-factors/third-000.json`,
`/cases/3`, historical (n,u)=(0,279). It records rank 19, free columns
2 and 6 and the two complete basis vectors stated in the proposal.
All eight tested factor choices are recorded failures; the fourth is
in the historical-residual class, not one of L112's exchanged-row
exceptions. This is input identification, not a fresh verification of
rank, basis, Plucker equations or gates.

L112's two-point conclusion depends on its actual homogeneous quadratic
coefficients. It cannot be transferred merely from equal kernel dimension.
L115 uses a complete common coordinate factor; L116 tests eight
selected row/overlap-label choices. Their failure does not imply absence
of other factors, absence of decomposable points or feasibility. Preserve
ATTEMPTS/041–042: rank-only and label-1-only exhaustion remain valid.
This one-locus gate test is a different, independently testable mechanism.
The scoped duplicate search found no completed exact-target gate test;
that is not a novelty claim.

First independently reconstruct the original four exterior blocks,
rank witness, kernel residuals and basis independence for this occurrence.
Then retain all 35 homogeneous Plucker equations on its complete
projective line. Cover infinity, zero-coordinate, identically vanishing
and extension-valued branches; do not assume L112's s*t pattern.
For every resulting plane retain every necessary L109 projection,
nonzero lambda, both overlap-weight and prescribed finite-direction gate.
Rank-zero projection is explicitly rejected only by the actual
nonpersistence hypotheses. Keep zero recovered weights visible and check
the original shifted eight-moment identities. Arbitrary omitted original
points remain allowed, including nonrational ones.

Continue if one bounded attempt gives an exact whole-locus exclusion,
a fully checked selected-row survivor, or explicit unsolved equations
with a discriminating next test. Exclusion needs complete algebraic case
coverage or exact identities against the original generators and nonzero
gates. A survivor must specify its field and embedding in F_(97^20);
a point only over another extension is enlarged-domain evidence. Four
rows do not invoke L109's r>=6 converse or prove actual nonpersistence,
t=0 or sixteen events. A freely chosen chart cannot silently replace the
prescribed chart. Base-field sampling, truncated reduction, a nonunit
ideal or resource exhaustion is unresolved. Save complete unfinished
branches and stop if exact resolution is impractical; do not expand to
all 599 cases or recursively import the 174 third exclusions.

This is LITERATURE / NOVELTY_UNCHECKED / EXPLORATION: a completed new
scope comparison, no mathematical result or discovery beyond checked
sources. No lemma, mathematical script, DAG or proof argument changes.
Mathematical exploration usage stays zero. The exact ready continuation
receives separate supervisor approval next turn.

## Original proposal (preserved; superseded above)

The main gap is still sixteen versus fifteen; the global interval is
11/q–16/q. This proposed one-occurrence test could validate an exact
whole-locus mechanism for kernels left by L116, useful before considering
any larger residual family. Removing one occurrence alone need not
exclude its third, fixed pair or arbitrary t=0 profile.

Essential inputs are L109's complete necessary gates, L116's audited
partition, L114's audited historical kernel provenance and L086's
eligibility scope. L112/L115 are mechanism comparisons. The exact input
is `scripts/seven-coordinate/residual-coordinate-factors/third-000.json`,
`cases[3]`, historical fourth index 279; it is in the historical-residual
fourth class, not a disjoint L112 fourth. Its rank is 19 and its two
complete basis vectors have a single 1 in zero-based alternating columns
2 and 6 respectively, with all other entries zero. This merely records
the fully replayed input; no new decomposability or gate assertion has
been derived here.

After approval, retain the full homogeneous projective locus, every
rank-zero branch, original shifted moments, zero recovered weights and
the prescribed finite-direction gate. A complete exclusion would require
every decomposable point to fail a necessary gate; otherwise preserve
an exact admissible selected-row recovery or an explicitly unresolved
branch. Four-row feasibility would not supply sixteen events. Do not
assume a common coordinate factor for the entire kernel, sample only
prime-field points, expand to all 599 cases, or recursively use the 174
third exclusions. ATTEMPTS/041–042 and all L116 filter failures remain.

No literature approval, new mathematical attempt or expanded solver is
performed in the proposing audit turn. The next invocation must first
complete this scope comparison, reusing adequate inspected sources.
