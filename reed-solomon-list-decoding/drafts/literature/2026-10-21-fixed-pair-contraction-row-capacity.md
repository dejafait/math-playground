# Fixed-pair independent contraction-row capacity — source assessment

TARGET: Test all 64 nonzero-distance exact-cardinality contractions separately against the original-orbit scalar bounds at L098's fixed exact-N pairs.
CHECKED: 2026-10-21
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the 2026-10-20 normalized-control, triple-marginal and free-cardinality assessments; searched constant weight code triple distribution linear programming marginal constraints fixed cardinality Schrijver and the exact A(1024,10,68) string on 2026-10-21; compared L098, L021–L023, ATTEMPTS/081–082 and step 362. No inspected matching row-capacity verdict was located; unread search leads are not imported.
SOURCE_EVIDENCE: Reused inspected primary statements in foundations/04,12,13: Schrijver author manuscript III.B (62)–(67), p.7, DOI 10.1109/TIT.2005.851748; Kim–Toan arXiv:1212.3467v1 (31)–(35), pp.8–9; Raghavendra–Tan arXiv:1110.1064v1 Section 3 pp.7–9; Polak arXiv:1703.05171v1 Proposition 1.1 and full indicator proof p.2, Section 1.2 p.3; Boyd–Vandenberghe Section 5.9.1 pp.264–266 for certificate sufficiency. L098 supplies the audited exact contraction conversion, including repetitions and zero pairs.
COMPARISON: Known scalar bounds and cardinality marginals supply the tools; L098 tests one complete triple assignment, whereas this target lets each original coordinate vary independently within its scalar interval for each contraction separately. The stopped free-variable numerical method included PSD and shared variables. Neither local result supplies this necessary row-capacity verdict.
GAP: Specialize the cited scalar rows at the fixed pairs, justify the independent-coordinate relaxation, and compute exact lower/upper contraction capacities on all admissible original entries. No joint feasibility or row-capacity result has yet been established.
REASON: A direct finite interval calculation is a bounded independently testable preliminary question, with no solver, source access dependency, hidden identification or PSD. Its applicability and original-coordinate certificates must be justified in research; literature approval alone proves no new mathematics.
SCOPE: Only this independent-row relaxation, fixed L098 pairs and exact N; no shared-triple joint solve, parameter search, altered pairs, new PSD blocks or translated-pole calculation.
LITERATURE_REASON: Changed target from the saved full fixed-pair feasibility problem to a necessary row-capacity diagnostic; existing tools cover it, but its precise scope and stopping rule needed comparison before calculation.

## Gap, use and limits

The main gap is arbitrary-center safety at 68 or 67 agreements in the
955–957 bracket. Use n=1024,w=68,v=956,d=10 and
N=floor(65537^28/2^128)+1. Freeze exactly L098's p_c coordinates from
its alpha mixture, not L022's unscaled pairs and not L098's triples.
L098 has already proved the support reduction and all 69 contractions;
its separate audit is recorded in step 362. Repeating that audit or
testing its same frozen y values is not the proposed work.

An exact row obstruction would exclude these fixed pairs even without
PSD; it would not prove safety uniformly over other pairs. If every row
passes, stop this independent-row diagnostic. Such a pass gives no
joint assignment: shared source equalities and simultaneous contractions
can still conflict. Neither outcome gives an RS list. Independent
67-agreement safety, other pair distributions, labeled restrictions,
L104's pending audit and the qualified ABF comparison remain unresolved.

## Imported hypotheses and qualifications

The primary coding input is Schrijver,
[author manuscript](https://homepages.cwi.nl/~lex/files/codes.pdf),
III.B (62)–(67), printed p.7, cross-checked by Kim–Toan,
[arXiv:1212.3467v1](https://arxiv.org/pdf/1212.3467v1), (31)–(35),
pp.8–9. It applies to nonempty binary constant-weight codes of minimum
distance d; here 0<10<136<=1024. Retain both multinomial denominators,
all admissible original (i,j,t,s) and the h=i+j-t-s third distance.
Use scalar rows only on actual orbits. Repetitions are Boolean pairs;
forbidden-distance entries are zero. Schrijver (61)'s qualified
complement prefactor is unused. No block diagonalization reproof is
needed because this test omits every PSD constraint.

Raghavendra–Tan,
[arXiv:1110.1064v1](https://arxiv.org/pdf/1110.1064v1), Section 3,
Definitions 3.1,3.3 p.7 and conditional-cardinality display pp.8–9,
supplies conditioned cardinality with consistent local distributions,
not a global representing measure. Polak,
[arXiv:1703.05171v1](https://arxiv.org/pdf/1703.05171v1), Proposition
1.1 and its full indicator proof p.2, Section 1.2 p.3, supplies the
ordinary constant-weight moment framework and constraint-preserving
averaging. Retain the printed A(n,d) versus proved constant-weight
qualification. L098 already specializes these inputs homogeneously;
no division by zero pair probabilities or new hierarchy is needed.

For any proposed contradiction use the exact scalar/equality weak-duality
identity, a special case of Boyd–Vandenberghe,
[*Convex Optimization*, Section 5.9.1](https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf),
pp.264–266, as recorded in foundations/04. Sufficiency of a checked
identity requires neither strict feasibility nor dual attainment.
The local interval calculation is necessary because no inspected source
evaluates these specific rational p_c values. This is a known-method
specialization, to be classified REPRODUCTION, without novelty claim.
Full matching Mathlib coverage and supporting interval-LP coverage:
not checked. Unknown availability is not evidence of absence.

## One bounded future attempt

First save the exact contract and input paths. Recover p_c,N and L098's
positive integer D coefficients from its canonical definitions or full
selected certificate values. Check the exact objective, p0, forbidden
pairs and all repeated-word entries. Use the canonical formulas rather
than a copied inherited-feasibility flag. No old numerical proposal is
an input. Preserve every unfinished artifact.

For each actual orbit obtain its scalar interval using every source
scalar inequality applicable at its presentations, including all three
pair distances. Keep repeated or forbidden entries fixed as required.
Do not assume lower bounds vanish: check them exactly. In research,
explain why dropping equality couplings between different entries and
between different rows enlarges the original feasible set. This is a
necessary relaxation, not an asserted exact projection. Derive the
interval endpoint rule explicitly there; it is not derived by this
literature assessment. No equality of different t-s entries is imposed.

Evaluate each i=5,...,68 contraction's exact attainable scalar lower
and upper endpoints in this independent-coordinate relaxation and
compare N*p_c,i with both. Include i=0 and i=1,...,4 as controls, retaining
both repeated third words. Do not aggregate solely by three distances.
Lossless factored sums are permitted only with their complete original
entry lift and multiplicities. An empty scalar interval is itself a
failure requiring an original-row certificate, not an entry to skip.

Save all 69 endpoint sums and comparisons, actual versus permitted
counts, exact input hashes and lossless full coefficient/interval data
under `scripts/finite-support/fixed-pair-row-capacity-`. Independently
regenerate every admissible orbit, its presentation bounds, repeated
entries and D from four-region counts. A failing row must yield an exact
signed contraction/scalar combination with every original coefficient
and constant checked. A pass requires all endpoints and all comparisons,
not samples or numerical approximations. No lemma is required merely
to document a passing necessary test.

Hard bounds: 1,501,000 original entries, 69 contractions, 20,000,000
coefficient/presentation visits over construction plus independent
verification, 1 GiB declared live arrays, 256 MiB certificate output,
262,144 bits per rational numerator/denominator and 900 seconds total.
Use streaming and exact arithmetic, with no numerical or rational Phase I,
parameter scan, rounding, optimization or full joint solve. Stop at the
first work bound and preserve the incomplete record. Limits are caps,
not promises of tractability. Print only counts, actual/required bounds,
first failures and paths; inspect selected complete load-bearing values
with the shared JSON inspector when necessary.

Continue only to complete this one row-capacity verdict within these
bounds. If all rows pass, abandon row-wise scalar capacity as an exclusion
mechanism at these pairs; do not call it joint feasibility. If a row
fails, record precisely that fixed-pair obstruction for a later separate
critical review. A cap or verification failure leaves even this smaller
question undecided and does not authorize retuning. Essential inputs
are L098, its L021–L023 pair definitions, L001's already imported support
selection and foundations/04,12,13. No cross-notebook input is used.
