# Proposed one-letter redistribution table test

TARGET: Assess coverage for certifying C077a's data tests at r=25, B=9250245 and tau=2 for L055's table with H_0=39 and H_24=32670622, all other entries unchanged.
CHECKED: 2026-10-18
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 302 compared the complete C077a data hypotheses and L075–L077 criterion statements/proof mechanisms, L055's explicit table, reusable variable-table assessments and Attempts 026–031; two focused web queries found no inspected certificate for this changed table.
SOURCE_EVIDENCE: Reused the recorded primary inspection of Halbeisen–Hungerbuehler (1997), section 2 equations (2)–(4), Lemma 2 pp. 228–229 and printed induction cases, and DLMF 4.5.1/4.6.4/4.2.19; reopened MathPrize's exact statement dated 2021-07-07. No new primary theorem is imported.
COMPARISON: Audited L075–L077 and C077a cover explicit finite tests for variable tables; primary affine and analytic results cover the machinery, not the new certificate operands. C074b and the two rational witnesses concern different fixed data.
GAP: Source coverage is adequate for one certificate attempt; every changed-table order/support/cutoff inequality still needs rigorous evidence, and survivor nondivisibility and all universal gaps remain unresolved.
REASON: Permit one later RESEARCH/REPRODUCTION calculation using the existing criteria, with no generalized theorem reproof, table search or transfer of old numerical margins.
SCOPE: One table only: L055's indexed pairs with H_0=39 and H_24=32670622, r=25, B=9250245, tau=2; certify all C077a tests or rigorously fail a required sufficient test, without survivor arithmetic or realization claims.
COVERED_TARGET: Certify C077a's data tests at r=25, B=9250245 and tau=2 for L055's table with H_0=39 and H_24=32670622, all other entries unchanged, or record a rigorous strict failure.
LITERATURE_REASON: The saved changed-table target was REVIEW_REQUIRED; existing assessments approved general criteria and the original benchmark, but no attempt on these changed operands. This separate scope comparison closes that essential coverage gap.

## Original proposal

The pending-review wording below is preserved as step-301 provenance;
the separate step-302 comparison following it supersedes that wording.

Main gap: universal eventual descent. Proposed intermediate target:
certify, or find a rigorous failed sufficient test in, all three
independent C077a data-test sets for this one table. The table is
specified by L055's 25 indexed J,H pairs, changing only H_0 from
40 to 39 and H_24 from 32670621 to 32670622. Keep the full integer
allocation simplex of total B=9250245 and cutoff tau=2. This is a
new pair table, not another order or allocation of the old table.
No calculation on it has been performed in step 301.

Essential inputs for assessment are L055's explicit table, L075,
L076, L077 and C077a. Compare their full hypotheses and analytic
certificate requirements, particularly the independent constants,
support residual denominator, every early offset, both eta bounds,
uniform lower domain, every cutoff incoming product and boundary
margin. Reuse the known primary affine coverage where adequate:
Halbeisen–Hungerbuehler, *Optimal bounds for the length of rational
Collatz cycles*, Acta Arithmetica 78 (1997), 227–239,
DOI 10.4064/aa-78-3-227-239, section 2 equations (2)–(4),
Lemma 2 pp. 228–229, with nonempty-word/nonzero-denominator guards.
The existing record contains the inspected primary proof cases.
Search this exact proposed scope and known obstructions; do not
infer novelty or transfer the original numerical margins merely
from the small parameter change. Matching Mathlib coverage is unchecked.

Plausible downstream use: if all data tests can be certified, C077a
would give its stated order/support/cutoff reduction for this new
table. Applying L078 and audited C078a would still require separate
nondivisibility certificates for every surviving parameter. No such
certificate, actual cycle exclusion or feasibility assertion is part
of the proposed data-test task. Both original-table rational witnesses
and Attempts 026–031 remain valid; their prime residues cannot be
carried over to changed numerators.

Continuation test for the later mathematical step: report complete
rigorous certificates for all C077a tests, or an explicit strict
failure and its actual versus required bound. An inconclusive interval
is not a failed mathematical inequality. A failed sufficient test
stops that use of C077a, without proving feasibility or infeasibility.
Do not expand to more tables, new moduli or survivor arithmetic in
that step. This proposal grants no readiness and derives no result;
the next turn is solely its source/scope comparison.

## Step 302 source and scope comparison — 2026-10-18

The main gap is universal eventual descent. The intermediate target is
the finite sufficient-test package for this one changed table. Its
downstream use is C077a's necessary order/support/cutoff reduction,
conditional on passing every test. L078/C078a would additionally need
nondivisibility for every survivor; neither certificate production there
nor actual-word realization is covered by this assessment.

### Inspected coverage and applicability

Read C077a's complete data hypotheses, normalization and composition
passages, L075–L077 statements and their relevant affine/product,
first-recipient and boundary mechanisms, and L055's explicit 25-row
table. The changed entries specify integer H values in the stated
variable-table domain; all J entries remain the same. The calculation
must explicitly check the full domain and recompute totals and prefixes.
This review certifies no numerical inequality, even where old data might
ultimately be reusable after an exact equality check.

Reuse the inspected primary evidence in
`2026-10-17-variable-table-survivor-divisibility.md` and the cyclic-order,
early-support, last-pair and order/support/cutoff assembly assessments
of 2026-10-17. Halbeisen–Hungerbuehler, *Optimal bounds for the length
of rational Collatz cycles*, Acta Arith. 78 (1997), 227–239,
DOI 10.4064/aa-78-3-227-239,
[section 2, equations (2)–(4), Lemma 2, pp. 228–229](https://www.math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf),
provides finite formal affine composition and its fixed point for a
nonempty word with nonzero denominator. The recorded inspection includes
the length-one and appended-zero cases; appended one is printed as
analogous. The proposed integer exponents give finite words; a positive
Lambda certificate is still required before using the fixed point.
No parity/integer realization or new general composition proof is needed.

Reuse the primary positive-real inequalities and series recorded in the
early-support assessment: [DLMF 4.5.1](https://dlmf.nist.gov/4.5.E1),
[4.6.4](https://dlmf.nist.gov/4.6.E4), and
[4.2.19](https://dlmf.nist.gov/4.2.E19). The earlier record retrieved
them on 2026-10-17; a current release number is unverified. Logarithm
arguments must remain positive, and new bounds require rigorous
remainders and outward rounding. Existing local criteria already prove
how such certificates imply the conditional reduction. A second proof
of those implications would add nothing to this task.

The reused scalar-order comparisons distinguish a scalar numerator
optimizer from simultaneous intermediate guards. In particular the
primary paper's Lemma 4 requires equal length/one count and domination
at every prefix, and supplies no replacement for C077a's tests. No
optimizer, primitive-cycle cutoff or density theorem is an input here.
Matching Mathlib coverage remains unchecked; supporting real/rational
facts are not a matching table-certificate theorem.

### Complete later certificate obligations

Use separate O, S and C constants as in C077a; no shared cap is forced.
For order, certify positive Lambda, the minimum-height exponential cap,
all three logarithm enclosures, all 25 negative tail-2 offsets, and all
24 rational first-displacement margins, including the empty prefix.
For support, B>0 makes every test mandatory: certify E<lambda^S,
the positive residual denominator and root cap, all 23 negative tail-20
offset inequalities, and every next-input margin for j=0 through 22.
For cutoff, certify both Lambda bounds below 1, both eta lower bounds
and the uniform-domain inequality. Since tau=2<=B, also certify every
incoming prefix lower bound L_i at t=2, Q, U, the exponential/logarithm
bounds, and the strict final boundary margin. The changed final row
must stay in eta and total closure; the changed initial row must stay
in every relevant prefix. Sampling t is not a substitute for these
data tests or the existing theorem's full-interval implication.

These are exactly the existing criterion tests, not newly derived
inequalities. Exact factored powers or certified bounds avoid requiring
huge expanded rationals. Save the complete certificate and failures to
disk, with actual/required bounds and a concise printed verdict. An
interval straddling a threshold is inconclusive, not a strict failure.
Failure for one proposed choice of auxiliary constants must be identified
as such; it does not establish that no other certificate choice can work.

### Duplicates, known failures and search record

Scoped search for `H_0=39`, `32670622` and redistribution wording in
local assessments, histories and ATTEMPTS found the step-301 proposal,
not a completed changed-table result. Read Attempts 026–031 in full.
The unchanged real-system witness, prime cancellation stops and rejected
permuted candidate retain their exact scopes. No uniform-prime test is
reopened, and no old numerator residue or order/support margin transfers.
This is an independently testable finite data target, not a renaming of
one of those stopped diagnostics. Both rational witnesses remain valid.

Queries run on 2026-10-18:

- `Collatz rational cycles prescribed table intermediate guards tail allocation Halbeisen Hungerbuhler`
- `Collatz "9250245" "39" "32670622"`

Results included the primary 1997 paper and general rational-cycle papers;
no inspected result supplies this table's certificates. Other search hits,
including general cycle papers and claimed resolutions, remain unread,
nonessential leads and are not theorem evidence. Failed search does not
establish novelty. Reopened the [MathPrize statement](https://mathprize.net/posts/collatz-conjecture/),
dated 2021-07-07: the target remains every positive integer reaching 1
under even halving and odd 3n+1; prize rules supply no proof premise.

### Decision and bounded test

SPECIALIZE covers exactly the COVERED_TARGET for a later REPRODUCTION
calculation. Continue this application only with all required certified
tests; stop the attempted certificate on an explicit strict failed test
and report its scope. Inconclusive bounds require honest unfinished
status. Do not enlarge the table family, search moduli, infer feasibility
from failed sufficient tests, or claim an unconditional exclusion. The
remaining inputs for any downstream exclusion are all simultaneous data
certificates and every survivor's nondivisibility certificate.

Outcome: LITERATURE / EXPLORATION / NOVELTY_UNCHECKED. This is new scope
coverage using known machinery, not mathematical progress beyond the
checked sources. No lemma, mathematical script or numerical certificate
was written or run. Mathematical exploration usage remains zero. This
newly completed ready assessment receives separate approval next turn.
