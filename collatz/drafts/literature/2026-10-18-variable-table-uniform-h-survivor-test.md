# Variable-table uniform H-survivor test — source scope approved

TARGET: Develop a computable sufficient own-input H-guard test that uniformly rejects all C077a last-pair survivors for a variable indexed table.
CHECKED: 2026-10-18
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Five recorded queries on prescribed-parity affine roots, prefix bounds, normalized heights, last-pair H guards and a returned Christoffel lead; compared L077/C077a, L081/L082, C082a, L055/L065, ready variable-table assessments and Attempts 026–031. No inspected source supplies the exact uniform own-input H criterion; no novelty inference.
SOURCE_EVIDENCE: Reopened Halbeisen–Hungerbuehler (1997), section 2 equations (2)–(4), Lemmas 1/2 pp. 228–229 with printed proof cases and Lemma 4/exchange proof p. 230; reused assessed Lemma 5/Corollary 1 and DLMF coverage. Inspected Fernandez–Ibanez arXiv:2607.24844v1 sections 2–3, Propositions 5.1/5.2, Theorem 7.3 and Theorem 8.2 with relevant proofs; rechecked MathPrize's exact statement.
COMPARISON: Known finite-word affine algebra and L077's variable-table root/parameter formulas cover the mechanism; L081/L082 provide fixed-root normalized-cap benchmarks. Scalar prefix-order and rotation-minimum results do not give the required uniform bounds at each designated outgoing input. The sufficient data inequalities and their implication remain to be proved.
GAP: Establish explicit certified table-data bounds for every surviving integer t and needed incoming prefix, derive a sufficient own-input H rejection test and recover C082a without rejecting either original witness; no such generalized bound or test is established by this review.
REASON: Essential source coverage now permits one separate bounded specialization of existing affine/analytic machinery. Import those identities precisely and prove only the variable-table uniformity and sufficient-test applicability; no general coding or analytic reproof is needed.
SCOPE: Exactly TARGET under every independent C077a O/S/C test, integer r>=3,B>=0,tau>=0, strictly increasing integer J_i>=2, arbitrary integer H_i>=3 and integer survivors 0<=t<=B,t<tau; explicit additional sufficient data tests are permitted, not a claim that every table passes them.
LITERATURE_REASON: The saved REVIEW_REQUIRED target changes fixed-root estimates to variable tables and an entire survivor range; that uniformity lies outside the ready C082a audit coverage and requires this separate comparison before mathematics.

## Proposal retained from step 329

The following paragraphs preserve the original proposal. Their pending
source-review wording is superseded by the separate step-330 comparison
below; no proposed mathematical claim has been proved by this review.

The main gap remains universal eventual descent. The proposed intermediate
target would make real H-guard exclusion testable across tables without
constructing enormous exact rational roots separately. Its downstream
use would be a sufficient real-system exclusion after C077a's reduction;
it would supply neither universal table coverage nor eventual descent.

Proposed scope: C077a's integer r>=3, B>=0, tau>=0, increasing integer
J_i>=2, integer H_i>=3, and every independent O/S/C data test remain
explicit hypotheses. Only its literal last-pair allocations with integer
0<=t<=B and t<tau are considered. Seek explicit, certifiable table-data
bounds on s_i/C_i(t), sufficient to force one own-input H margin to
fail for each survivor. Do not replace this target by the tautological
assumption that all survivor roots fail. Whether a single uniform bound
is adequate is unresolved; no such bound is asserted here.

Essential comparison inputs: C077a, L077's last-pair root formulas,
L081/L082's normalized input caps, and audited C082a. L055 and L065
are positive original-table benchmarks, not inputs authorizing a new
exclusion. Reuse recorded Halbeisen–Hungerbuehler/DLMF primary readings
where their exact hypotheses match; inspect any essential uncovered
source before approval. No cross-notebook theorem is proposed.

Continuation/abandonment test: the later mathematical test should recover
C082a's two exclusions with explicit sufficient data, while remaining
consistent with both original-table rational witnesses. Retain all tails
in closure, every incoming prefix, and each row's own input. A method
requiring unsupported prefix growth, a minimum/seed at indexed zero,
or an unevaluated root-failure premise should be rejected or narrowed.
Integer/parity/exact-valuation/primitive realization and universal entry
remain unresolved and cannot be assumed. Empty survivor ranges require
no H test. This proposal approves no new mathematics in step 329.

## Separate source comparison — step 330, 2026-10-18

The main gap remains universal eventual descent. The intermediate target
is a sufficient table-data H test after C077a, with plausible downstream
use in rejecting an entire table's endpoint/domain/J/H real subsystem.
Coverage of arbitrary tables, unrestricted cycles, entry and divergence
remain independent gaps. Source readiness is not mathematical progress
beyond the inspected results, nor a complete Collatz candidate.

### Precise primary inputs and scope

Halbeisen–Hungerbuehler, *Optimal bounds for the length of rational
Collatz cycles*, Acta Arithmetica 78 (1997), 227–239, DOI
10.4064/aa-78-3-227-239, [section 2, equations (2)–(4), Lemma 2,
pp. 228–229](https://www.math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf),
gives a finite nonempty binary word's affine map and fixed point
Phi/(2^N-3^K). Read the numerator recursion, concatenation identity,
length-one and appended-zero proof cases; appended one is printed as
analogous. Integer rows define finite formal words; C077a's positive
Lambda supplies the denominator sign. Import formal real affine algebra
only, not rational parity Lemma 1 as an integer-realization premise.
Lemma 4, p. 230, requires distinct words of equal length/one count and
domination at every prefix; its exchange proof compares scalar numerators.
Equal totals do not establish that premise. Previously assessed Lemma 5/
Corollary 1, pp. 230–231, optimizes a minimum over rotations, not a
specified outgoing input. No general coding reproof is justified.

Reuse positive-real analytic coverage from
`2026-10-17-variable-table-last-pair-cutoff.md` and
`2026-10-18-redistributed-h-t1-failure-critical-audit.md`:
[DLMF 4.5.1](https://dlmf.nist.gov/4.5.E1) for real x>-1,x!=0,
[4.5.8](https://dlmf.nist.gov/4.5.E8) for real nonzero x,
[4.6.4](https://dlmf.nist.gov/4.6.E4) for Re(z)>=0,z!=0, and
[4.2.19](https://dlmf.nist.gov/4.2.E19) for the exponential series.
The ready audit records version 1.2.8, released 2026-09-15; this turn
does not assert an independently checked current release. Their domains
include positive Lambda and the positive arguments used locally. Reuse
the existing certified remainder method, without rederiving a logarithm
theorem. New constants still require outward enclosures with their
amplified errors; fixed-table values cannot become universal constants.

A returned stronger-result lead was inspected at theorem level:
Fernandez–Ibanez, *Christoffel Words as Extremal Structures in Collatz
Dynamics*, [arXiv:2607.24844v1](https://arxiv.org/html/2607.24844v1),
24 July 2026. Sections 2–3 define binary words of length N with r ones,
the scalar numerator C and C_min as its minimum over all rotations.
Their r denotes the notebook's total odd count K, not its row count.
Propositions 5.1/5.2 and their displayed proofs concern concatenation
and adjacent 10-to-01 exchanges. Theorem 7.3 claims the Christoffel
maximizer of C_min for N>=1,0<=r<=N; its proof was read. Theorem 8.2
assumes a positive integer periodic orbit and N/r>log_2(3), and bounds
some orbit element by 1/(2^(N/r)-3); its geometric-sum proof was read.
These scalar/minimum statements do not bound every indexed input.
No result from this preprint is imported or independently certified.
Its cited Rajab/Rozier/Knight leads remain unread and nonessential.

Rechecked [MathPrize's page](https://mathprize.net/posts/collatz-conjecture/),
dated 2021-07-07: every positive integer reaches 1 under n/2 when even
and 3n+1 when odd. This is the unchanged universal target; prize
adjudication is separate. Full matching Mathlib coverage for the proposed
criterion has not been checked; unknown availability is not absence.

### Local comparison, duplicates and failures

Read C077a's complete simultaneous test statements and normalized
conclusion, L077 through its uniform-domain and boundary-cap proof,
L081/L082 through their complete normalized-cap and failed-H passages,
C082a's hypotheses/reduction, and L051 (1)–(4). Read L055's full indexed
table and witness scope and L065's positive H conclusions. Scoped
searches of variable-table assessments and the latest relevant history
found no duplicate uniform H test. This is a bounded comparison, not
evidence of originality or a claim to have searched every local file.

L077 (9) already states the variable-table endpoint formulas, including
the full inverse-prefix sum and closing product. Its (10) proves parameter
directions: inputs through r-2 increase and the final input decreases.
Its (11) bounds one normalized input at the rejection boundary. None is
already a uniform H test on the survivor interval. L081 (5)–(8) and
L082 (5)–(6) instead bound all normalized inputs for their individual
allocations. They certify the changed row18 upper margin below
-457745289/50000000000. The second proof separately handles its tail-20
row; its growth floor is not licensed for arbitrary redistributed tails.
All-input assertions there stop at C_24, never C_25. This distinction is
essential when table data, budget and cutoff vary.

C082a assembles these two failures, using C077a and L079, but supplies
no new uniform estimate. L055 and L065 are positive benchmarks for the
original H table, with the same two tail allocations. L065's smallest
certified H-margin lower bound is 0.006289114252 at row18. These are
imported canonical conclusions, not fresh calculations or recertification.
The proposed sufficient criterion must be compatible with their real
feasibility; failed sufficient tests will imply no feasibility verdict.

Read Attempts 026–031. The unchanged-table witness defeats universal
exclusion of that real subsystem; the prime-cancellation stops concern
specific arithmetic diagnostics, and Attempt 031 rejects one permuted
candidate by its own J guard. They neither ban this different sufficient
test nor supply its premises. No stopped prime route is reopened, and
no cross-notebook input is used. All unfinished work remains preserved.

### Discovery record and approved bounded continuation

Queries actually run:

- `Collatz rational cycles prescribed parity intermediate bounds affine fixed point redistribution even steps`
- `Collatz rational cycles prefix sums ordering Halbeisen Hungerbuhler uniform bounds`
- `"Collatz" "normalized" "prefix" "Hungerbühler"`
- `"Collatz" "H-guard" "last-pair"`
- `"Christoffel words as extremal structures in Collatz dynamics"`

Results included the primary affine paper, the inspected Christoffel
preprint, a 3n+c generalization, repositories, discussions and speculative
claims. Only the primary passages identified above support this review;
other hits remain unread leads. A failed exact-phrase search establishes
neither absence nor novelty. No essential source is blocked.

SPECIALIZE approves one later proof attempt at exactly TARGET. Seek
explicit positive rational lower bounds on every needed incoming prefix
over the survivor range, a certified reciprocal-prefix sum/root cap, and
own-input H upper-margin tests depending solely on table data. A common
bound may be sufficient without being sharp or passing every table.
The proof must establish uniformity, including the final varying input;
it may not assume C_i>=1, growth of a varying-tail map, a normalized
minimum/seed, or any unevaluated root-failure verdict. Existing L077
formulas and monotonicity are inputs, not new theorems to reprove.

Retain all independent O/S/C tests and the exact closed integer ranges,
including r=3, B=0, tau=0, tau>B and final tail 2. Empty survivor sets
need no H tests. Transport each strict H guard with its own outgoing
row through both cuts if stating a downstream all-order implication.
No minimum/seed invariance, survivor feasibility, integer/parity/exact-
valuation or primitive realization is an available premise.

Continue only if explicit certified data recover C082a's changed-table
t=0,1 rejection while remaining consistent with both original witnesses.
Abandon or narrow the uniform-cap mechanism if that test fails, the
required bounds lack proof, or the criterion simply restates unknown
root failure. All generalized inequalities, any canonical lemma and any
certificate implementation belong to the separate mathematical turn.
This literature turn derives no new result and changes no lemma or
mathematical script; source readiness alone is EXPLORATION.
