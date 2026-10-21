# First rank-18 residual — completed scope comparison

TARGET: Test L109's full extension-field gates on the rank-18 residual A3={1,12,75,79}, A4={8,12,85,89} for L113's fixed pair.
CHECKED: 2026-10-18
DECISION: EXPLORE
SEARCH_EVIDENCE: Reused step-288 seven-coordinate theorem searches and step-306 algorithm comparison; searched exact A3 and rank-18 residual strings in local assessments, histories and ATTEMPTS; read L109 complete gates, L112 projective cases, L113 whole-locus argument and L114 exact residual passage. Only the proposal and originating partition/failure record match this residual.
SOURCE_EVIDENCE: Reused inspected primary extractions: Hall, Notes on Coding Theory, Theorem 5.1.1 and proof pp. 63–64, https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf ; Marquez-Corbella–Pellikaan accepted manuscript 2016-02-29 section 5 pp. 7–8, https://pure.tue.nl/ws/files/93073933/16_02_29_ECP_MDS.pdf ; Stacks Theorem 10.34.1(1), https://stacks.math.columbia.edu/tag/00FS ; Magma V2.29 exact ideal-coordinate/saturation references identified below. No fresh external retrieval is claimed.
COMPARISON: L109 already specifies every necessary gate for arbitrary selected two-overlap supports. L112 only solves its point/line kernels; L113 excludes whole kernels with the label-1 factor. L114 preserves this different complete three-dimensional residual without further gates. Standard ideal certificates permit whole-locus exclusions but give neither this exclusion nor a practical solver guarantee.
GAP: One bounded exact test of this projective kernel, using all Plucker equations, rank-zero/rank-one projection cases, full weights and prescribed original-chart conditions; no base-field-only exclusion, assumed rational descent or four-row realization theorem.
REASON: The exact support locus changes beyond the completed factor filter, but existing source coverage applies to its row-wise gates and algebraic certificate method. Approve a bounded diagnostic only; its outcome remains unknown and no new mathematics is derived here.
SCOPE: F_(97^20), fixed H, k=8, pinned event, S={1,8,12,18,22,27,33}, A1={1,8,47,50}, A2={12,18,64,70}, A3={1,12,75,79}, A4={8,12,85,89}; sixteen original finite bad parameters, actual nonzero D/locators and t=0; arbitrary extension weights and prescribed original chart; inherited finite-certificate qualifications.

LITERATURE_REASON: The selected three-dimensional residual is outside the completed label-1 filter; compare its exact whole-locus gates and certificate scope before mathematics, reusing unchanged source coverage.

## Completed comparison — step 312

The main gap is sixteen versus fifteen, with global interval 11/q–16/q.
The intermediate target is exactly TARGET. An intrinsic exclusion would
remove this indexed fourth occurrence; a checked local survivor would
identify a locus requiring further simultaneous rows. Neither outcome
excludes the third support without its other fourth cases, nor supplies
universal pair/seven-set occurrence, representation or challenge qualifications.

### Reused primary results and limits

Read the saved primary extractions in
`2026-10-05-two-block-moment-obstruction.md`, Primary theorem and
applicability, and `2026-10-07-six-coordinate-triple-equality-obstruction.md`,
Primary shortening input. Hall's undated author-hosted chapter, Theorem
5.1.1 and full proof, printed pp. 63–64, allows any field, distinct labels,
nonzero multipliers and 0<k<=n. Here n=16, k=8 and unit multipliers satisfy
the hypotheses. The inspected proof includes both the root bound and an
attaining polynomial. Import that distance result without reproof.

Marquez-Corbella–Pellikaan, *A characterization of MDS codes that have an
error correcting pair*, FFAA 40 (2016), 224–245, DOI
https://doi.org/10.1016/j.ffa.2016.04.004, accepted manuscript dated
2016-02-29, section 5, Definitions 5.1–5.2, Lemma 5.3 and the following
unnumbered GRS shortening formula, printed pp. 7–8: use the formula,
not an enlarged interpretation of the MDS parameter lemma. Through
L104/L109, shortening exactly J minus K deletes seven distinct labels,
leaves dimension one, and retains nonzero products of label differences.
Changing A3/A4 does not change those row-wise hypotheses. No general
shortening reproof is needed or approved.

Reuse `2026-10-17-seven-coordinate-syndrome-bound-review.md` for the
thirteen-query discovery record and stronger-result comparison. Its
inspected Chojecki v9.2 (2026-07-17) ray/circuit statements and proof cases
confine all selected error supports to a fixed union; membership of the
coefficient syndromes in U_S is insufficient. The saved BCHKS theorem
comparison likewise supplies no bound for this locus. No mutable source
is freshly verified and no unread ABF26 assertion is imported.

Read step-306's primary algorithm extraction in
`2026-10-18-fixed-pair-remaining-third-gates-review.md`. Stacks Project,
Commutative Algebra, Theorem 10.34.1(1), tag 00FS, has arbitrary field
and finite-type algebra hypotheses; its saved full induction proof
includes both contraction cases. It gives no prescribed-degree descent
or computational cost bound. A proper ideal over F_97 alone does not
give a point over F_(97^20).

Magma Handbook V2.29 (2026-08-03), Gröbner bases, `Coordinates`,
`CoordinateMatrix`, `NormalForm`, example H115E9 and truncation warning,
https://magma.maths.usyd.edu.au/magma/handbook/text/1314 ; Computation
of Varieties, `Variety(I,L)` and example H116E3,
https://magma.maths.usyd.edu.au/magma/handbook/text/1325 ; and First
Operations on Ideals, `ColonIdeal`, `Saturation`, `IsProper`,
https://docs.magma-maths.org/CommutativeAlgebra/PolynomialRingIdealOperations/ideal-operation.html
are reused from that inspected extraction. They distinguish specified
extension points from base-field points, saturation from one quotient,
and exact identities from truncated calculations. They certify no local
installation, license, feasible run time or result for this residual.
No particular software package is required by this assessment.

### Duplicates and retained failures

L109's complete necessary gates apply to arbitrary selected rows and
all kernel dimensions. L112's s*t projective-line classification does
not transfer to a three-dimensional kernel. L113's whole P^2 exclusion
requires complete containment in its label-1 factor space, which L114
explicitly does not establish for this residual. Do not assume either
prior Plucker pattern. ATTEMPTS/041 and ATTEMPTS/042 remain valid:
rank-only and the completed label-1 filter cannot exclude the fixed pair.
The changed mechanism is full algebraic gate testing of one saved locus,
not repetition or enlargement of either stopped filter.

The focused local search located the proposal and originating records,
not a completed gate test of these exact supports. This is not a novelty
claim. L114's independent replay is recorded, but its separate critical
audit remains pending; the later test must check this exact input rather
than silently mark L114 audited. Full matching Mathlib coverage and
supporting algebraic API coverage are not checked; unknown is not absent.

### Approved bounded test and stopping criterion

Use only the complete basis in L114, increasing S-pair order, and
`scripts/seven-coordinate/remaining-third-factor-filter/third-000.json`
at `/cases/249`. First independently check the exact four supports,
original matrix, rank and basis completeness. This is input validation
for one locus, not a replay or approval of the enlarged L114 partition.
Retain the inherited L010/L103/L104 finite-certificate qualifications.

In the research attempt retain all 35 homogeneous Plucker equations in
all three kernel coordinates. Cover the whole nonzero projective locus,
including infinity, zero-coordinate and identically vanishing branches.
L109's nonzero p_ab charts and complete projection-pivot alternatives
supply the specification; L113 is an implementation comparison only.
Keep rank-zero projections as explicit rejected branches under actual
nonpersistence, and separately test lambda, both overlap weights and the
original finite direction at every row. An encoding must be justified
against L109 in the later mathematical step; none is derived here.
A prescribed chart stays arbitrary, including a nonrational omitted point.

An exclusion needs exact whole-locus identities or complete algebraic
case coverage over extensions, checked against original equations and
nonzero conditions. Unit-ideal certificates must be verified by exact
polynomial arithmetic with the original generators. Saturation/nonzero
gates and every projective branch must be explicit. Base-field sampling,
a nonunit ideal, a truncated reduction or a resource cap is unresolved.
A survivor must have a specified field embedding in F_(97^20) and pass
all original gates; existence over some other extension is only evidence
for an enlarged-domain locus. Four selected recoveries do not invoke
L109's r>=6 converse or establish actual nonpersistence, t=0 or sixteen
original finite events. A freely chosen chart cannot replace the prescribed
chart without explicitly qualifying the result.

Continue if one bounded attempt gives an intrinsic exclusion, a fully
checked local survivor, or an exact residual with a discriminating further
test. If exact solving becomes impractical, save the complete unsolved
equations, gate branches and input basis and stop this attempt; do not
launch an all-residual census. No outcome is predicted. Independent
universal representation, arbitrary t=0 profiles and challenge-definition
gaps remain even if this occurrence is excluded.

This is LITERATURE / NOVELTY_UNCHECKED / EXPLORATION. It completes the
changed-scope comparison, establishes no mathematical result and spends
zero mathematical EXPLORATION turns. The exact ready continuation is
left for separate supervisor approval next turn.

## Original proposal from step 311 (preserved; superseded above)

This is a newly written continuation proposal, not a ready approval and
not a second mathematical attempt. The next turn should compare the exact
locus with canonical L109/L113 and recorded failures, reusing adequate
source extractions. No new solver, factor exclusion or kernel analysis is
performed in this assessment.

Essential inputs are L086/L109/L113/L114, with inherited L010/L103/L104
qualifications. The complete basis and all 72 original residuals are in
L114 and in `scripts/seven-coordinate/remaining-third-factor-filter/third-000.json`
at `/cases/249`; the master and replay also preserve this first residual.
L111/L112 are only prior removed-domain comparisons. ATTEMPTS/041 and
ATTEMPTS/042 remain route evidence; rank deficiency is not sufficiency.

The main gap is still sixteen versus fifteen. The intermediate target is
the whole exact kernel locus, not its base-field points. An intrinsic
failure valid for the entire locus would remove this indexed residual;
a survivor would still need all other actual rows, coordinate balance,
nonpersistence and original-chart conditions before any equality claim.
Universal pair/seven-set occurrence, representation and challenge
qualifications remain independent gaps.

Continuation test: approve a specific bounded whole-locus test only when
the source/local comparison covers it. Retain all Plucker and projection
branches and full recovered weights. An exact intrinsic exclusion or
verified local survivor would be informative; incomplete coverage stays
unresolved. Do not enlarge to a new all-residual solver in this review.
