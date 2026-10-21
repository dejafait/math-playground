# Variable-table last-pair cutoff — source assessment

TARGET: Assess a variable-table sufficient last-pair cutoff under literal endpoint/domain/J guards, with L068's rejection of t>=2 as the benchmark.
CHECKED: 2026-10-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Two focused adjacent-tail/prescribed-parity searches; compared complete L068 and its ready assessment, L051's endpoint/shift passages, L055's table/root and L064's changed-tail/domain passages, scoped variable-table assessments, histories 210/211/213 and Attempts 026–031; no inspected theorem supplies the variable-table cutoff.
SOURCE_EVIDENCE: Reopened Halbeisen–Hungerbuehler (1997), section 2 equations (2)–(4), Lemma 2 and printed induction pp. 228–229, and Lemma 4 with complete exchange proof p. 230; reused ready positive-real DLMF and exact-remainder coverage from step 282; rechecked MathPrize's exact statement.
COMPARISON: Known finite affine composition covers the construction; audited L068 supplies only the fixed-table full-interval argument. Scalar numerator ordering and L075/L076 do not supply variable-table last-row guard thresholds or uniform lower-domain estimates.
GAP: Formulate and prove independently certifiable table/budget/sign/domain/boundary tests sufficient for a last-pair cutoff, recovering all L068 t>=2 rejections without transferring fixed-table estimates to arbitrary tables.
REASON: Essential source coverage is adequate for one later specialization of L068's mechanism; changed coefficient signs, parameter dependence, domain bounds and cutoff sufficiency remain proof obligations, not results of this review.
SCOPE: Exactly TARGET with the proposed parameters and endpoint/domain/J subsystem below; only the exact affine last-pair and last-row boundary mechanism of L068 is covered. No new-table search, modular test, integer exclusion, order assembly or actual-word application.
LITERATURE_REASON: The new variable-table last-pair target was REVIEW_REQUIRED; existing early-support coverage did not compare its coefficient, domain and boundary hypotheses. This turn completes that essential comparison before mathematics resumes.

## Proposal retained from step 285

The pending-review wording below records the original proposal. The separate
step-286 comparison completes source approval, without proving a new criterion.

The main gap remains universal eventual descent. A portable last-pair
cutoff could reduce the allocation parameters left after L076 on qualifying
tables. Later combination with L075 and arithmetic exclusion of surviving
parameters remain independent work; no such assembly is asserted here.

Proposed objects are integer r>=3, B>=0, increasing integer J_i>=2,
integer H_i>=3, literal indexed rows, b_i=0 for i<r-2,
b_(r-2)=t and b_(r-1)=B-t for integer 0<=t<=B, and
a_i=2+18b_i. Retain all L051 shifted endpoints including closure,
s_i>=540/11 and every non-strict own-input J guard. No H/seed,
minimum location, arbitrary-tail growth, integer-junction, realization
or primitive/count-ray premise is available. Any positive-Lambda,
coefficient-sign, root-domain or boundary-comparison condition must be
identified as a proved consequence or explicit data test, not inherited
from the fixed table. B=0 and both endpoint parameters must be retained.

Essential prospective input IDs are L051 for definitions, L068 for the
existing fixed-table last-pair argument, L055/L064 for its benchmark,
and L076 only for the downstream motivation that early support can
already be excluded conditionally. Read L068 and its saved assessment
first, then only the necessary input ranges. Reuse existing affine and
analytic source assessments where their exact hypotheses match. Inspect
relevant recorded failures before approving research. No cross-notebook
input is proposed. Full matching Mathlib coverage remains unchecked.

The source-review test is whether exact known affine machinery and the
fixed-table analysis cover a separate sufficient-cutoff specialization,
with a precise remaining difference. A later mathematical test would
seek a data-only criterion recovering the full L068 rejection t>=2
for B=9250245, including the final tail-2 endpoint. Passing t=0,1
and arithmetic exclusion of them are separate benchmark facts, not a
universal claim for other tables. No monotonicity formula or new theorem
is derived in this proposal. If essential sign or domain hypotheses are
uncovered, narrow or retain REVIEW_REQUIRED; do not import fixed-table
properties as general facts. Failed sufficient tests imply no feasibility.

This is a new uncovered continuation, not a ready assessment. The next
turn is literature-only and may approve a later bounded mathematical
attempt if coverage is adequate. The completed L076 audit is independent
of that approval. Both rational witnesses and prior failure evidence remain.

## Separate source comparison — step 286, 2026-10-17

The main gap remains universal eventual descent. The intermediate target
is a sufficient, table-dependent cutoff for the literal last-pair family.
For tables meeting the tests it could reduce the parameters left after
L076; combination with L075 and integer exclusion of the survivors are
independent, unproved downstream steps. This review supplies source scope,
not a cutoff formula, new-table verdict or mathematical advance.

### Primary statements and applicability

Halbeisen–Hungerbuehler, *Optimal bounds for the length of rational
Collatz cycles*, Acta Arithmetica 78 (1997), 227–239,
DOI 10.4064/aa-78-3-227-239,
[primary PDF](https://www.math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf),
section 2, equations (2)–(4), Lemma 2, pp. 228–229, states for a
finite binary word of length ell and k ones the affine map
(3^k x+phi)/2^ell and fixed point phi/(2^ell-3^k).
Read the length-one and appended-zero induction cases; the appended-one
case is printed as analogous. Import its formal real affine identity
only. The rational parity and pseudo-cycle discussion is not an integer
realization premise here.

The proposed integer rows give finite words with totals defined in L051.
A certified positive Lambda must be part of this sufficient mechanism;
it checks a positive, nonzero fixed-point denominator. L055's numerical
Lambda enclosure applies only to its unchanged benchmark totals.
Coordinate specialization and changed-tail comparisons still require proof;
no general parity-coding reproof is needed.

Lemma 4, p. 230, requires distinct binary words with equal length and
one count and prefix domination at every cut. Its complete finite
exchange proof orders scalar numerators. It supplies neither all
intermediate lower-domain conditions nor the last row's own-input guard.
Equal total tail budget alone is not its prefix hypothesis. Reuse the
ready rotation-extremum and scalar-ordering comparisons in the
[variable-order assessment](2026-10-17-variable-table-cyclic-order-criterion.md);
no ordering optimizer is imported or newly inspected here.

Reuse the inspected positive-real analytic coverage in the
[early-support assessment, step 282](2026-10-17-variable-table-early-support-criterion.md):
NIST DLMF [4.5.1](https://dlmf.nist.gov/4.5.E1),
[4.6.4](https://dlmf.nist.gov/4.6.E4) and
[4.2.19](https://dlmf.nist.gov/4.2.E19), with the exact integrated
logarithm remainder and outward bounds in L055/L064. Their real domains
cover the positive logarithm/exponential arguments in this mechanism.
No analytic theorem is reproved or new numerical enclosure certified.
The reused assessment retrieved these equations on 2026-10-17 and did
not independently verify a current release number; none is inferred here.
Full matching Mathlib coverage is unchecked, not absent.

Rechecked [MathPrize's statement](https://mathprize.net/posts/collatz-conjecture/),
dated 2021-07-07: every positive integer eventually reaches 1 under
the ordinary map n/2 for even n and 3n+1 for odd n. This precise version
is unchanged. Prize adjudication supplies no mathematical premise.

### Local proof comparison, duplicates and failures

Read L068 completely, including its independent audit, before its needed
inputs. Its ready October 14 assessment covers the entire fixed-table
interval, and its existing exact parameter formulas, positivity argument,
domain proof and single-boundary comparison are reusable proof architecture.
This is substantially more than isolated endpoint sampling, but is not
already a theorem for every increasing J table and H>=3.

L051's hypotheses (3)–(4) give the non-strict J guard and shifted endpoints;
its shift/eta passage gives the pointwise unshifted identity and positive
offsets for the stated parameter range. Its minimum-dependent bounds,
seed, H guards and primitive-count hypotheses are not available inputs.
L055's complete 25-row table, exact totals, positive Lambda and root
passages, and L064's changed-tail root/domain passages were inspected.
L068 imports L055 at t=0 and audited L064 at t=1. Those are the same
two benchmark survivors, not universal existence statements.

L068's coefficient signs use its positive denominator and positive
affine terms. Its quantitative all-input domain proof also uses its
particular eta lower bounds and unchanged-prefix growth. Its boundary
height cap uses prefix growth at t=2 only. None of the numerical
eta>2, n>18*10^9, prefix-growth or normalized-height estimates may be
silently transferred to other tables. A later sufficient test must expose
any needed sign/domain/boundary conditions as verifiable data tests or
prove them from existing hypotheses. An unknown feasible tuple is not data.
No general parameter-dependence formula or monotonicity is derived here.

The benchmark boundary includes both changed tails, and its symbolic
argument reaches the final tail-2 endpoint. Its optional margin<-4 probe
failed; the load-bearing certified upper bound is
-474883782659/125000000000<-3.79. Preserve that failure. No certificate
was rerun or independently recertified during this source review.

Scoped searches of the supplied overview/DAG, the variable-table
assessments and histories found no duplicate general last-pair criterion.
L075 restricts order and L076 restricts early support under their own
tests; neither supplies this missing cutoff or arithmetic exclusion.
Attempts 026–031 were read: the real-system witness, prime cancellations
and one permuted-guard failure stop their specific mechanisms. Both
known rational witnesses are compatible with a cutoff rejecting t>=2.
None of those stops bans this distinct target or proves its generalization.
All evidence and unfinished work are preserved; no cross-notebook input.

### Discovery and bounded continuation

Queries actually run:

- `Collatz rational cycles prescribed parity sequence redistribution two adjacent even exponents intermediate values monotonicity`
- `"Collatz" "last pair" affine cutoff guards`

Results included the primary affine paper, other rational-cycle papers,
repositories, discussions and speculative claims. No inspected matching
variable-table sufficient-cutoff theorem was found. *Collatz high cycles
do not exist* (publisher result S0012365X25004200), arXiv:1909.13218
and other returned papers remain unread leads; no theorem or hypothesis
from them is imported. They are not essential dependencies of this scoped
formal-affine specialization. Failed discovery searches establish neither
novelty nor absence of a stronger theorem. No essential source is blocked.

SPECIALIZE approves one separate mathematical attempt at the unchanged
TARGET, using L068's mechanism and known affine/analytic inputs by precise
citation. Formulate finite table/budget tests, prove their sufficient
implication and recover the full L068 t>=2 rejection for B=9250245.
The target is a sufficient cutoff, not a necessary-and-sufficient
classification or a claim that every arbitrary table has two survivors.
Any full-domain claim beyond the premise needs its own uniform proof.

Retain integer r>=3, strictly increasing integer J_i>=2, integer H_i>=3,
B>=0, early b_i=0, b_(r-2)=t, b_(r-1)=B-t and every integer 0<=t<=B.
Keep all endpoints, s_i>=540/11 and every own-input non-strict J guard.
Retain B=0, small budgets with no t=2, both parameter endpoints and the
closing edge even at final tail 2. Do not assume a minimum location,
growth of varying-tail rows, H/seed guards, integer/parity/valuation or
primitive/count-ray realization. L076 is motivation only; no support or
order assembly belongs to this attempt.

Essential input IDs are L051 for definitions and the pointwise shift,
L068 for the complete fixed-table mechanism, and L055/L064 for its
benchmark. Continue if explicit data-only tests with proved sufficiency
recover every L068 rejection from t=2 through 9250245 without assuming
the cutoff itself. Preserve the known t=0,1 facts separately. If a required
coefficient sign, domain bound or boundary comparison cannot be justified,
record the exact obstruction and stop or narrow; a failed sufficient test
implies no feasibility. New tables and arithmetic tests require new scope.

Completed LITERATURE/NOVELTY_UNCHECKED, outcome EXPLORATION: source
comparison is complete, but no new lemma, script, cutoff, guard verdict
or mathematical derivation was made. Mathematical exploration usage
remains zero. The same saved TARGET is ready for a later research turn;
this turn does not perform that attempt.
