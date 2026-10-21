# Fixed-pair cyclic-product range — completed source comparison

TARGET: Determine the maximal initial word-count range excluded by L050's fixed rational pair and cyclic-product method, retaining L041's seed, L046's 48/25 transfer and all exact endpoints.
CHECKED: 2026-10-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Five focused queries on the exact pair, rational-cycle/minimum bounds and cyclic-product/postspell terminology; read L050, relevant L041/L046 proof ranges, ready assessments and Attempts 019/021–023; no inspected theorem supplies this fixed-method postspell-count cutoff.
SOURCE_EVIDENCE: Reopened Halbeisen–Hungerbühler Acta Arith. 78 (1997), Lemmas 1/2 and their relevant cases pp. 228–229, Lemma 5/Corollary 1 pp. 230–231 and Theorems 1–4 pp. 235–236; reused inspected Simons–de Weger Corollary 2/Lemma 12 and Hercher Theorem 16 coverage; inspected Fernández–Ibáñez arXiv:2607.24844v1 Theorems 7.3/8.1/8.2 and displayed proofs, without importing them.
COMPARISON: Known coding and global-minimum bounds provide background and the unchanged published inputs, but do not identify designated junctions with the global minimum or determine this pair's range; the proposed test specializes L050's audited mechanism rather than reproofs of general cycle results.
GAP: In a later mathematical turn justify the variable-count substitutions and certify the initial successful range and first failure of the explicit sufficient predicate below; no cutoff, new exclusion or simultaneous feasibility is established here.
REASON: Changed-range source comparison is complete and permits one separate RESEARCH/REPRODUCTION attempt; retain the exact pair, seed, transfer, endpoints and qualified published threshold, stopping at the first failure of this specified comparison.
SCOPE: Integer r>=3; L050's subsystem with indices modulo r, log r in its seed and 69r/1034 in its length conversion; all other own-index, real-height, integer-count, primitive-scaling and exact-endpoint hypotheses retained; only the half-log separation and explicit test below are covered.
LITERATURE_REASON: The saved REVIEW_REQUIRED target changes fixed twenty-word scope to a variable-count range and leaves the finite-ceiling selection unspecified; this review resolves that essential comparison while reusing adequate primary inputs.

Main gap: universal eventual descent. Intermediate target: identify the
reach and first obstruction of the specific cyclic-product comparison,
rather than generate individual exclusions one count at a time. A useful
range result would make its limitation explicit and inform whether a
different mechanism is needed. This is not a proposed optimal cutoff for
actual cycles and cannot close the independent entry/divergence gaps.

Essential input IDs: L050, L041, L046. Keep p=9809721694 and
q=6189245291 fixed, integer own-index parameters, primitive scaling
K_0>225640000, smallest designated junction, the r-dependent seed and
length constant, and every exact cyclic endpoint. The later comparison
must specify how its finite ceiling M is chosen and certified, keeping
the residual guard 2M(q log3-p log2)<log2 for L050's half-log separation.
No bound uniform in r, optimal rational approximation, actual feasibility
or stronger source theorem has been established or assumed.

The source review below supplies coverage for a separate calculation,
not a mathematical derivation or originality claim. The exact TARGET
is unchanged. Previously inspected inputs remain adequate as specified
below; no missing source is essential to the fixed-input test.

## Sources actually compared

Read the source-evidence passages of the ready assessments
`2026-10-10-twenty-cyclic-height-feasibility.md`,
`2026-10-10-twenty-cyclic-height-infeasibility-audit.md` and
`2026-10-09-retained-transfer-word-count-range.md` in this directory.
Their inspected proof cases are reused, not claimed freshly retrieved.
The last assessment records the unchanged MathPrize original-map target,
page dated 2021-07-07 and checked 2026-10-10. Prize terms are not inputs.

John Simons and Benne de Weger, *Theoretical and computational bounds
for m-cycles of the 3n+1-problem*, Acta Arithmetica 117 (2005), 51–70,
[published period conventions p. 52, Corollary 2 and proof p. 53,
Lemma 12 and proof p. 61](https://www.impan.pl/shop/en/publication/transaction/download/product/82263):
Corollary 2 supplies K_0>225640000 for a nontrivial positive integer
cycle; Lemma 12 supplies Lambda>exp[-13.3(0.46057+log K)]. Their
full-minimum parameter is not the number r of designated word boundaries.
The prior assessments inspected the relevant complete proofs and Lemma 8
support. Keep the published computational height 301*2^50, distributed
[Ro] computations, Roosendaal communication, continued-fraction inputs
225644606/397573379 and Rhin/Crandall originals as qualified imports;
original certificates and external Lean builds remain unchecked.

Christian Hercher, *There are no Collatz m-Cycles with m <= 91*,
JIS 26 (2023), Article 23.3.5,
[Theorem 16 and complete proof pp. 10–11](https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/hercher5.pdf),
supplies 0<Lambda<S/3 at primitive counts, where S sums every odd-input
reciprocal occurrence. L041 already partitions those occurrences and
scales repeated periods. Its all-r seed and length conversion are the
relevant inputs. The previously inspected June 2026 correction leaves
Theorem 16 unchanged; amended Theorem 21 is unused. These integer-cycle
theorems are not assertions about arbitrary real assignments.

Lorenz Halbeisen and Norbert Hungerbühler, *Optimal bounds for the length
of rational Collatz cycles*, Acta Arithmetica 78 (1997), 227–239,
DOI 10.4064/aa-78-3-227-239,
[published paper](https://math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf):
Lemma 1 and Lemma 2 pp. 228–229 give odd-denominator rational parity
coding and the nonempty-word fixed point phi/(2^N-3^K). Read the
denominator argument and both induction cases (the last-bit-1 case is
stated analogous). Lemma 5 and Corollary 1 pp. 230–231 optimize the
minimum rotation numerator over all parity words of fixed length/odd
count. Theorems 1–4 pp. 235–236 give continued-fraction and optimal
global-minimum/length criteria; Theorem 3's complete displayed proof was
read, while all supporting analytic estimates were not critically audited.
These stronger general criteria do not determine this restricted test or
its smallest designated junction. No new theorem from these passages is
imported, and no rational-coding reproof is needed. The particular offset
product in L050 still requires its own variable-count algebra check.

Carlos Fernández and Santiago Ibáñez, *Christoffel words as extremal
structures in Collatz dynamics*,
[arXiv:2607.24844v1, submitted 2026-07-24](https://arxiv.org/html/2607.24844v1),
Theorem 7.3 optimizes the rotation-minimum functional for binary words
of length N with a fixed number of ones; Theorems 8.1/8.2 give integer
cycle ratio/global-minimum consequences. Read these theorem statements
and displayed proofs, but not all supporting sections or a critical
verification. Their r denotes odd inputs, corresponding to our K, not
postspell words. They contain no fixed-pair postspell range theorem and
are not imported. Knight's qualified publisher-preview lead remains
parked: extremal integer high cycles are not assumed here. The new
preprint and other unread search leads are not essential sources for
the existing audited mechanism. No stronger threshold is substituted.

## Applicability, duplicates and failures

Read L050's proof, source applicability and audit; L041's hypotheses,
count/period scaling, seed (6), own-index prefix (7), endpoints and length
conversion (11); and L046's hypotheses and real-domain transfer/prefix
proof. L041 already permits every integer r>=3 and preserves repeated
periods and coincident junctions. Its actual positive closed words give
s_i>=540/11 and a nontrivial primitive cycle. The general-r real system
is a necessary-condition relaxation of those words, not a theorem that
every real solution realizes a parity word. L046's numerical transfer
and prefix estimates are per-occurrence statements; its eighteen-word
conclusion and L050's twenty-word conclusion cannot just be relabeled.

Attempt 019/L031 stop boundary guards as an independent exclusion.
Attempts 021–023 and L045/L047/L049 stop their specified scalar systems.
Their witnesses supply no simultaneous heights or closing equation, so
they do not settle the fixed-pair product test. L050's audit already
checks closure and integer logarithm separation at twenty words; it
does not supply a variable-count cutoff. The scoped records contain
no completed cutoff for this precise mechanism. No novelty follows.

Queries on 2026-10-10: `Collatz cycles "9809721694" "6189245291"`;
`Collatz rational cycles cyclic product minimum continued fractions
Halbeisen Hungerbuhler`; `Collatz postspell words twenty cyclic height
bound`; `Collatz "fixed" "rational approximation" "cycle" minimum bound`;
`Collatz "cyclic" "product" "postspell"`. These located the primary
papers, forum material, ledgers and recent preprints. Nonprimary claims
and snippets are not theorem evidence. No exhaustive novelty search is
claimed. Full matching Mathlib/Lean coverage remains not checked.

## Exact sufficient comparison to test next — unproved specification

The following definitions fix the intended calculation, not its result.
Prove the variable-count implications separately before using them.
Keep rho=48/25, p=9809721694, q=6189245291, ell=log2 and
epsilon=q log3-p log2. L050 certifies epsilon>0. For integer r>=3
define the test quantities by the corresponding audited expressions:

    R_r = sum_(j=0)^(r-1) rho^j
    A_r = (399/5) R_r
    B_r = (54+6 log r) R_r + 69r/1034
    F_r(t) = t - A_r log t - B_r
    D_r = (69 r q+23)/11
    T_r = (15/4) R_r (1+log D_r).

These are prospective comparison functions. This literature turn has
not derived N<A_r log N+B_r, h_0<log D_r or K<T_r for the
general-r subsystem, or evaluated any new r.

Define an admissible integer ceiling M by the three strict tests

    M>A_r,    F_r(M)>0,    2 M epsilon<ell.

Use the least integer M satisfying the first two tests; the later proof
must justify whole-ray monotonicity, existence of this least ceiling and
why failure of its third test excludes any larger admissible ceiling.
Certify minimality using the immediately preceding integer when it is
above A_r, with exact comparisons rather than rounded root estimates.
If the preceding integer is at or below A_r, record that boundary instead.
An exact equality in a ceiling test is a failure of that strict test.

The specified success predicate is: such an admissible ceiling exists
and T_r<=225640000. The non-strict final comparison is intentional:
the proposed contradiction requires a strictly smaller K than T_r
against the strict published primitive threshold. The later proof must
verify every strict sign and this use of primitive scaling.

This fixes L050's half-log separation and its weakened Lambda>1/(3q)
step; it does not optimize the residual loss with K, use a different
rational pair, sharpen eta_i, alter the transfer, or add a stronger seed.
Retain all r endpoint equations to justify the proposed D_r expression;
integer total counts, rather than integrality of real junctions, must
justify the logarithm separation. The use of log D_r avoids an arbitrary
integer rounding of the final height bound. Its general-r applicability
is an explicit proof obligation, not an established result of this review.

Test integer counts from r=3 and stop at the first certified failure of
this predicate. Certify every count in the claimed initial range, or
prove the required monotonicity reducing those checks. At the first
failure, certify either that no integer ceiling can satisfy the three
tests or that T_r>225640000; numerical enclosure uncertainty is not a
failure certificate. No simultaneous feasibility witness is needed for
maximality of this specified sufficient test, and none follows from it.
Do not claim maximality among all uses of exact endpoints or this pair.

Continue only if the next mathematical step proves the substitutions
and supplies an exact initial range or informative first-failure bound.
If a strict comparison remains unresolved, save it as unfinished. Stop
this unchanged sufficient comparison once its first failure is proved;
different retained constraints or a new rational pair require separate
coverage. Universal entry, unrestricted cycles, divergence and eventual
descent remain independent gaps. Newly completed ready coverage is
subject to the supervisor's separate next-turn approval; no calculation
has been performed during this literature-only step.
