# Signed real-zero allocation: completed source comparison

TARGET: Review source coverage for a displacement-scale signed-block compensation test using one nonreal pair and two neighboring real zeros with finite allocation budgets.
CHECKED: 2026-10-30
DECISION: EXPLORE
SEARCH_EVIDENCE: On 2026-10-30, searched the exact one-pair/two-real-zero Laguerre block, fractional weights, positive residues, quartic criteria and the Hawaii conjecture; scoped local searches found no duplicate criterion. Primary theorem statements and relevant proof cases below were read; no exact fractional-budget feasibility theorem was found in this bounded search.
SOURCE_EVIDENCE: Reused Csordas arXiv:1309.0055v2 Proposition 2.2 (2.3) and Proposition 2.3 via L471; inspected Tyaglov arXiv:0902.0413v3 Definition 1.4, Notation 1.6, equation (1.6), Theorem 4.1 and its proof; Cardon arXiv:0911.1122v1 Theorems 1.1/2.1, Corollary 2.2 and Theorem 2.1 proof; Katkova–Tyaglov–Vishnyakova arXiv:2406.00686v1 Notation 1.1, Theorem 2.2 and Section 6 Lemma 6.1 proof opening; Tyaglov–Atia arXiv:1912.04951v2 Section 2 hypotheses and Theorem 2.2.
COMPARISON: Known identities cover the integer-multiplicity polynomial block. The Hawaii theorem bounds critical-point counts, and newer differential-polynomial counts require additional derivative-root hypotheses; their real parameter kappa does not allocate fractional real-zero masses. All-order Laguerre characterizations do not supply the proposed first-sign criterion. No displacement/budget threshold is imported.
GAP: The exact fractional-budget feasibility region remains unestablished. A symmetric m=d=1 slice with equal allocations w in [0,1] is a bounded rational-positivity discriminator; actual-Xi matching, conserved budgets, residual mass and higher signs remain independent gaps.
REASON: Essential theorem-level comparison is now complete for one bounded elementary test; direct citation does not supply its fractional feasibility region. EXPLORE authorizes the listed test after separate next-turn approval, without a novelty claim or an actual-Xi inference.
SCOPE: Finite rational block G as stated below, with p,q,d>0, integer m>=1 and nonnegative real allocation coefficients; only the listed symmetric slice is nominated for the immediate calculation. No Xi allocation/transfer, density estimate or higher sign is covered.
LITERATURE_REASON: New displacement-scale geometry and conserved fractional allocation budgets were outside the ready detector assessments and the older coarse-count comparison; this turn completes that missing source comparison.

COVERED_TARGET: Determine the exact feasibility region in (r,w) for G with m=d=1, p=q=r>0 and alpha=beta=w in [0,1], including equality cases and x=+/-r exclusions.

## Retained nomination and proposed discriminator

The nomination below records the pre-review proposal. The completed comparison
and sole proposed continuation are recorded after it; no algebra was performed.

The main gap remains actual-Xi all-degree positivity and initial signs
at unbounded height. L471's signed identity retains real-zero terms
that its negative-mass majorant drops. A quantitative local compensation
rule could use some of that positive mass. This is a possible use, not
an assertion that such a rule applies to actual Xi.

For a pair centered at gamma with displacement d>0 and multiplicity m,
place candidate real zeros at gamma-p and gamma+q, with p,q>0.
Allocate nonnegative masses alpha and beta to this pair. The proposed
finite block, for real x away from -p and q, is

    G(x)=2m (x^2-d^2)/(x^2+d^2)^2
                     +alpha/(x+p)^2+beta/(x-q)^2.

Given budgets A_-,A_+>=0, ask whether some 0<=alpha<=A_- and
0<=beta<=A_+ make G(x)>=0 for every such x, and what exact conditions
on p/d, q/d and these budgets are needed. This is a proposed subblock
of the cited identity, not a claimed sufficient parameter range.
Compare stronger known polynomial first-Laguerre criteria and
fractional-weight versions before nominating calculation. Coverage
only for integer multiplicities must not silently cover fractional ones.

In a prospective Xi application, allocations to different pairs must
sum to at most the multiplicity of each real zero. The same positive
term cannot be spent repeatedly. No such allocation, neighboring-zero
geometry, or estimate for unallocated pairs is assumed. Real zeros
require L471's zero-safe D_1 formulation, not division by Xi there.
Full-sum convergence, the retained remainder and endpoint windows
would need a separate application. Even first-sign control leaves
higher signs and RH unresolved. Essential prospective inputs are
L471's identity and its L018/L024 normalization; no cross-notebook input.

## Comparison of three continuations

1. More vertical measures: stopped by audited L508, including larger
   masses and new atoms. General rectangle measures remain outside
   that theorem, but no new input justifies another measure search.
2. Actual-height closure from finite shifted moments: the paired-jet
   assessment and L472/L473 overview leave the clipped actual-Xi
   statistic and realization uncontrolled. No new correlation input
   was identified here; repeating that test supplies no fresh mechanism.
3. Explicit signed zero-block allocation: selected for source review.
   This keeps individual displacement-scale positions and conserved
   multiplicity budgets. It neither infers them from counts/gap averages
   nor optimizes a positive detector measure.

The local comparison used
`drafts/literature/2026-09-27-first-laguerre-zero-compensation.md`,
`ATTEMPTS/2026-09-27-count-and-gap-first-sign-test.md`,
`ATTEMPTS/2026-10-27-displacement-weighted-negative-mass-test.md`, and
`drafts/literature/2026-10-28-two-height-hardy-jet-moment-coverage.md`.
L354 is a failure contrast, not an imported theorem for a new result.
Its coarse-count stop remains; no full L354 proof was needed here.

## One review and its continuation test

Reuse Csordas's inspected identity coverage. Search the exact finite
block, generalized Laguerre inequalities for polynomials with a
conjugate pair, and local compensation or fractional-charge criteria.
Retrieve primary hypotheses and necessary proof cases, checking local
duplicates first. Do not repeat the broad density/spacing search.

Continue only if a known theorem supplies the criterion or a precise
uncovered finite feasibility problem remains with a useful allocation
threshold. State the extra actual-Xi geometry its eventual use needs.
Import any matching known criterion rather than reprove it. Abandon
if this only renames the coarse-count claim or gives no displacement-
sensitive discriminator. No algebraic solution is derived or approved
in this nomination; source review must precede dependent mathematics.

No justified creative proof attempt is ready: actual-Xi geometric
matching or signed-cancellation input is missing. A finite algebraic
test may be routine specialization and must not be labeled creative
to meet a scheduling aim. A genuinely new actual-Xi mechanism needs
its own coverage, bounded test and escalation. Mathlib coverage is
unchecked, not absent.

## Completed review, 30 October 2026

### Local overlap and retained failures

Read L471's hypotheses, signed identity (6), convergence argument and
zero-safe cancellation in Sections 1–2. Its summation obstruction and
L354's coarse-count obstruction are retained through the two ATTEMPTS
files named above. No complete proof of L354 was needed for this comparison.

A final targeted duplicate check also read L251 and L257. L251 already
compensates a nonreal pair by a real zero **at its center**; L257 masks
any prescribed finite number of signs using real-root multiplicity at
that center. These are existing masking results, not new evidence for
the distinct-neighbor problem p,q>0 with fractional budgets. Any future
calculation must compare with them and must not claim that real-root
compensation itself is a new mechanism. The scoped searches found no
exact fractional-budget criterion. This is a bounded duplicate check,
not a claim that the full notebook or literature contains none.

### Primary statements actually inspected

1. Mikhail Tyaglov, *On the number of real critical points of logarithmic
   derivatives and the Hawaii conjecture*,
   [arXiv:0902.0413v3, 23 January 2011](https://arxiv.org/html/0902.0413v3),
   Definition 1.4, Notation 1.6, equation (1.6), Theorem 4.1 and its proof.
   For a non-exponential function phi in LP*, Q=(phi'/phi)' satisfies
   2m-2m_1 <= Z_R(Q) <= 2m, counting multiplicities; 2m and 2m_1
   count nonreal zeros of phi and phi'. LP* means a real polynomial
   without real zeros times an LP function; all real polynomials qualify.
   Read both proof branches: Z_R(Q)=0 and the finite reduction using
   property A. No independent audit of its earlier supporting theorems
   is claimed. This is a count theorem, not a displacement/budget
   positivity criterion. Its hypotheses do not state a fractional-residue
   extension or apply to actual Xi with an unbounded nonreal zero set.

2. David A. Cardon, *Extended Laguerre inequalities and a criterion for
   real zeros*,
   [arXiv:0911.1122v1, 5 November 2009](https://arxiv.org/html/0911.1122),
   Theorems 1.1/2.1, Corollary 2.2 and the proof of Theorem 2.1.
   For nonzero f=exp(-bz^2)f_1, b>=0 and real entire f_1 of genus
   zero or one, all real Laguerre signs at every order characterize LP.
   Theorem 2.1 uses an even auxiliary polynomial with nonnegative
   coefficients and a nonreal root. Read the nonreal-root contradiction
   and the real-rooted-polynomial approximation argument. Both require
   all coefficient signs, not only the first. Neither statement supplies
   the two-neighbor allocation region or arbitrary real root weights.

3. Olga Katkova, Mikhail Tyaglov and Anna Vishnyakova, *On the number of
   real zeroes of a homogeneous differential polynomial and a
   generalization of the Hawaii conjecture*,
   [arXiv:2406.00686v1, 2 June 2024](https://arxiv.org/html/2406.00686v1),
   Notation 1.1, Theorem 2.2 and Section 6, Lemma 6.1 with its proof
   opening (6.55)–(6.63). For a real degree-n polynomial whose real
   roots are simple and whose derivative has only real simple roots,
   kappa>=(n-1)/n implies
   Z_R(kappa(p')^2-pp'')=Z_C(p), with multiplicities.
   The proof opening studies p/p' on intervals between derivative roots.
   These derivative hypotheses are additional conditions to check,
   not consequences of having two real roots and one nonreal pair.
   The parameter kappa multiplies (p')^2; it is not a fractional
   allocation to particular real zeros. Thus even this exact-count
   result is not the sought criterion. No application is proved here.

4. Mikhail Tyaglov and Mohamed J. Atia, *On the number of non-real
   zeroes of a homogeneous differential polynomial and a generalization
   of the Laguerre inequalities*,
   [arXiv:1912.04951v2, 12 December 2019](https://arxiv.org/html/1912.04951v2),
   Section 2 setup and Theorem 2.2. Its polynomial in (2.1) has only
   real zeros with integer multiplicities; its parameter kappa again
   changes the differential expression. These hypotheses exclude the
   proposed nonreal pair. Only this comparison was used; its later
   proofs and the latest v5 were not inspected or imported.

The Csordas identity and fixed-factor small-displacement obstruction
are reused from the older assessment and L471, not reproved. Inspection
of Proposition 2.3 also confirms the fixed remaining factor is essential;
it is not a uniform statement for real zeros moving with the pair.
For integer alpha,beta, equation (2.3) applies to the polynomial
(z^2+d^2)^m (z+p)^alpha (z-q)^beta. Noninteger allocations do not
satisfy the stated polynomial multiplicity hypotheses. No extension
from integers, nor a positivity threshold, is inferred here.

### Search and access record

Queries actually issued included:

- `Laguerre inequality polynomial one conjugate pair two real zeros weighted logarithmic derivative`
- `Laguerre inequalities nonreal zeros real zeros compensation fractional weights`
- `"Laguerre inequality" "quartic"`
- `"Laguerre inequality" "fractional"`
- `"Laguerre inequality" "positive residues"`
- `"Laguerre inequality" "fractional weights"`
- `"Hawaii conjecture" "residues"`
- `"Laguerre inequality" "two real" "zeros"`

Local searches used allocation, fractional multiplicity/weight,
one conjugate pair, two real zeros/roots and quartic Laguerre terms
in lemmas/, drafts/literature/ and ATTEMPTS/, followed by the specific
L251/L255/L257 comparison. No sibling notebook was read.

An arXiv v2 URL for 2406.00686 returned 404; the v1 primary text and
version page were accessible, so the comparison has no essential
access blocker. Search also surfaced Brandon Muranaka's *The Laguerre
inequality and the distribution of zeros of entire functions*, a
rendering dated 16 October 2008, Section 7.2/Proposition 7.8, at
[CiteSeer](https://citeseerx.ist.psu.edu/document?doi=6cbd60abd134d8b004a35225a042ee90d36d3829&repid=rep1&type=pdf).
Opening that file returned 403. Its indexed extracts are **unread
leads**, not theorem evidence. They advertise the one-pair critical-point
count already covered more generally by the inspected Tyaglov theorem;
no exact fractional criterion is attributed to Muranaka. This optional
lead is not used as an essential input. Search did not establish
novelty or rule out a matching result elsewhere.

### Decision and sole bounded continuation

EXPLORE: the inspected sources give important overlapping identities
and count results but no directly importable fractional-budget region.
It is reasonable to test the symmetric slice of the nominated block:
m=d=1, p=q=r>0, alpha=beta=w in [0,1]. This is a proposed finite
parameter problem, not an assertion that feasible parameters exist.
The inequality remains required for every real x except +/-r,
including all equality cases. No numerator, stationary point,
parameter threshold, scaling theorem or sample feasibility is derived
in this literature turn.

The one calculation would determine that region by elementary rational
positivity, with a negative witness for excluded parameters. Its
discriminator is a nonempty displacement-sensitive feasible range
with a strict margin and a finite per-zero charge, or an informative
obstruction showing this restricted local certificate cannot work.
Do not replace that calculation by another count/gap comparison.
Even success leaves asymmetric blocks, actual-Xi geometry, a conserved
global matching, unmatched-pair mass and all higher signs unresolved.

The covered target above is ready **as a source assessment**, subject
to the supervisor's separate next-turn approval of this newly written
continuation. Recommend calculation / standard / high: this is routine
finite algebra, not a creative central-gap proof attempt. The blocker
to a justified creative actual-Xi step is the absence of a new
geometric matching or signed-cancellation input, not a scheduling quota.
No additional literature is needed after approval unless the target
or hypotheses change. Mathlib coverage remains unchecked; no full
matching theorem or absence assertion is made. No lemma, mathematical
script, DAG entry or PROOF.md change was made.
