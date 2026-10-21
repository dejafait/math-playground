# Triangle three-row compatibility attempt

STEP_ID: 2026-10-11-mca-145-triangle-three-row-test

The approved target remains the exact twelve-additional-recovery action
in `literature/2026-10-10-triangle-twelve-recovery-bound.md`; its supplied
EXPLORE assessment is reused without new literature. The main local gap
is excluding seven distinct scalars in L059's disjoint-P table, or
controlling full M for survivors. Other patterns, extraction and the
challenge definitions remain independent gaps.

Intermediate test: couple three complete L059 rows at one gated weight
point, with distinct scalars. A uniform incompatibility would strengthen
L064; an exact surviving triple would delimit that possible strengthening
and supply an independently checkable input for larger-fiber tests.
Stop if the calculation supplies only a formal resultant or repeats
the fixed-pair bound. A survivor is not a thirteen-recovery counterexample.

Scoped inspection found no previous three-row test in the triangle
attempts. ATTEMPTS/022–024 retain the individual-capacity, support-only,
and unqualified singleton-triple failures. L060–L063's selected maxima
two are not assumed. L064 remains unaudited: its needed identities are
checked directly from audited L059 (4), rather than using its count.
Equating r gives u_c mu-u'_c nu=v_c-v'_c; equating q after
multiplication by mu nu and equating p after multiplication by
(1+mu)(1+nu) gives L064 (1). All multipliers are nonzero. Two such
systems sharing mu impose a common root but alone give no exclusion.

Bounded discriminating calculation: test at most 256 explicitly saved
nine-label assignments, first sign-paired singleton choices and then
deterministically seeded mixed assignments. Enumerate complete
disjoint-P rows for each tested assignment, retaining all 95 both-zero
scalars and zero fourth weights. Stop at the first gated fiber with at
least three distinct scalars, and independently recover all eight moments
of that fiber and an admissible original finite chart. If none occurs,
record only bounded exploration, with no uniform at-most-two claim.
Full support M is required only if the seven-scalar filter is reached.

## Completed attempt and limits

For three rows indexed 0,1,2, compare row 0 with rows i=1,2 using
L064 (1), verified directly above. If u_c^(0) and both u_c^(i) are
nonzero, the r equations give mu_i=A_i mu_0+B_i, with
A_i=u_c^(0)/u_c^(i) and B_i=(v_c^(i)-v_c^(0))/u_c^(i).
Each remaining q and p equation is exactly the corresponding quadratic
Q_2 and P_2 in L064 (6), with prime coefficients replaced by row i.
Thus all four polynomials must vanish at the same mu_0; each row's
projected test, gates and distinct-scalar conditions remain necessary.
When a denominator is zero, retain the original three pair equations;
do not apply this substitution. Isolated rows retain their fixed scalar.
This is a reversible restatement of the three complete rows, not a
new obstruction. No resultant alone was interpreted as an exclusion.

The bounded search and independent replay are saved at
`scripts/triangle-recovery/three-row-search.json` and
`scripts/triangle-recovery/three-row-search-verification.json`.
Reproduction, from the notebook directory:

```sh
python3 scripts/triangle-recovery/three_row_search.py
python3 scripts/triangle-recovery/verify_three_row_search.py
```

The 256 saved assignments comprise all 56 choices of three antipodal
singleton pairs, each with one seeded shared-label triple, followed by
200 seeded mixed assignments. They are distinct, but do not exhaust
arbitrary labelings. Each has all 715 disjoint-P supports, giving 183,040
rows. Independent seven-column moment inversion reconstructs every
projected case, every eligible scalar test, every rejected gate and
every retained weight point without importing the row producer. It
checks all eight moment residuals of the 190,922 gated rows. It replays
272,619 scalar tests, including 133,570 both-zero tests, and retains
10,820 rows with a zero fourth weight. Scalar unions are deduplicated.
All residual failures are zero. The maximum across these assignments is
two; each assignment has maximum below three. Required thresholds are
three for this exploratory survivor test and seven for L059's necessary
violation filter. No full M test or original-chart witness was needed:
no triple or seven-scalar survivor exists in the tested rows. Omitting E
only enlarges the tested set, as proved in audited L059.

The first verifier run stopped on an incorrectly hard-coded assertion
that every individual maximum was exactly two. The producer had claimed
only a global maximum of two; some individual maxima are smaller. The
assertion was corrected to equality with the saved individual maximum
and strict inequality with three. The complete corrected replay passed.
This was a verifier expectation error, not a changed mathematical count.

Outcome: EXPLORATION / RESEARCH / POTENTIALLY_NEW, actual task type
calculation. There is no new canonical lemma: the formal common-root
condition adds no restriction, and the verified finite search neither
excludes arbitrary triples nor exhibits a survivor. It does not prove
twelve, improve 11/q–16/q, or certify novelty. L064's separate critical
audit and the previous computational audits remain unfinished.

One mathematical exploration turn has been used since the preceding
advance. Do not repeat more assignment sampling as the default next
step. Within the unchanged ready target, next test whether interpolation
on the six singleton labels classifies the both-zero support polynomials
uniformly, including all gated lifts. A usable label-independent
restriction, or an exact exceptional family requiring explicit testing,
would justify continuation; merely rephrasing the projected zero tests
would not. This is a proposed test, not an established classification.
It leaves isolated rows, simultaneous seven-scalar fibers, full M for
survivors, other patterns, extraction and challenge definitions open.
