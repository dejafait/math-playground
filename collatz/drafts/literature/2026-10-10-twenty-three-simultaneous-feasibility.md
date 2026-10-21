# Twenty-three-word simultaneous feasibility — completed source comparison

TARGET: Test whether L051's twenty-three-word real-height subsystem admits a simultaneous solution to all exact cyclic endpoints and own-index guards.
CHECKED: 2026-10-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Six focused exact-word, rational-coding and coupled-height queries; read relevant L051/L041/L046/L050 passages, ready rational-cycle and fixed-range assessments, Attempts 019/021–024 and history 135; no inspected result decides the exact twenty-three-word subsystem.
SOURCE_EVIDENCE: Reopened Halbeisen–Hungerbuehler, Acta Arith. 78 (1997), Lemmas 1/2 and denominator/induction proof cases pp. 228–229; reused inspected Simons–de Weger Corollary 2/Lemma 12 and Lemmas 6/7, Hercher Theorem 16, and the fixed-range assessment's stronger global-minimum comparisons.
COMPARISON: Prescribed-word affine closure is known; integer-cycle lower bounds and full-minimum chaining do not guarantee simultaneous satisfaction of the retained real-height guards. L051's fixed-test failure at twenty-three supplies neither feasibility nor infeasibility.
GAP: A later mathematical attempt must certify a complete simultaneous witness or obtain an all-parameter contradiction for L051 (1)–(4) at r=23; no such result is established by this source review.
REASON: Essential coverage is sufficient for one separate RESEARCH/REPRODUCTION attempt using existing wordwise inputs and cited affine coding; general cycle theorems need no reproof, and the new coupled-system assessment awaits separate supervisor approval.
SCOPE: Exactly L051 hypotheses (1)–(4) at r=23, including integer parameters/counts/scaling, the unchanged log23 seed and length inequality, real lower-height/minimum/own-index guards and every exact cyclic endpoint; no failed sufficient-test predicate is added.
LITERATURE_REASON: The target changes from auditing a fixed sufficient predicate to feasibility of the complete coupled twenty-three-word system; this essential scope comparison reuses adequate general sources rather than repeating their discovery.

## Assessed scope; no calculation performed

Essential input IDs: L051, L041, L046, L050. Fix r=23 and retain every
hypothesis (1)–(4) of L051: integer J_i>=2,H_i>=3, nonnegative a_i
congruent to 2 modulo 18, integer total counts, K=dK_0,L=dL_0 with
K_0>225640000, positive Lambda, the length inequality and log23 seed,
real s_i>=540/11, a smallest designated s_0, all own-index guards and
all exact cyclic endpoints. Independent tails, repetitions and ties
remain. The sufficient-test guard and T bound are conclusions of a
particular method, not additional assumptions of this system.

Main gap: universal eventual descent. Possible downstream use: an exact
simultaneous witness would delineate what the present relaxation can
exclude; an infeasibility proof would extend only the restricted word
exclusion. Neither would settle universal entry, arbitrary cycles or
divergence. The discriminating target is a certified simultaneous witness
or a rigorous contradiction using coupled individual endpoint information.
A scalar tuple or another failed fixed-pair comparison is insufficient.
No witness, new inequality or feasibility judgment is asserted here.
Preserve L049 and Attempts 019/021–024. The completed coverage is for a
separate mathematical invocation after supervisor approval; no larger-count
search or rational-pair optimization is proposed.

The constraints are recorded explicitly to prevent scope drift. Indices
are modulo 23. Set P_i=4J_i+H_i, K=sum_i(3J_i+H_i),
L=sum_i(J_i+a_i), N=K+L. Require positive integers d,K_0,L_0 with
K=dK_0, L=dL_0, K_0>225640000, and

    Lambda=N log2-K log3>0,
    N<(8/5)K+1587/1034.

Require real s_i>=540/11, h_i=log s_i, s_0=min_i s_i, s_23=s_0,
and

    0<h_0<(133/10)log N+8+log23,
    4J_i log2<=h_i+log(11/4),
    H_i log2<h_i+J_i log(27/16).

For G_i=(27/16)^J_i(3/2)^H_i, require each exact equation

    s_(i+1)=2^(-a_i)[G_i s_i-(12/11)(3/2)^H_i-1]+23/11.

This is a transcription of the canonical system, not a newly derived
result. J_i>=2,H_i>=3,a_i>=0 are integers and a_i=2 modulo 18.
No integer parity, valuation, residue, least-root or global-minimum
realization of the real junctions is assumed. The scaling variables
remain required arithmetic constraints; a rational witness would not
thereby establish that K_0 is its primitive odd count.

## Primary coding theorem and specialization limits

Lorenz Halbeisen and Norbert Hungerbuehler, *Optimal bounds for the length
of rational Collatz cycles*, Acta Arithmetica 78 (1997), 227–239,
DOI 10.4064/aa-78-3-227-239,
[published Lemmas 1/2, pp. 228–229](https://math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
For g_0(x)=x/2 and g_1(x)=(3x+1)/2, Lemma 2 gives the nonempty
binary-word affine map (3^k x+phi(w))/2^ell and unique fixed point
phi(w)/(2^ell-3^k). Lemma 1 identifies pseudo-cycles with cycles in
odd-denominator rationals, with parity determined by the numerator in
lowest terms. Read the preceding denominator argument, Lemma 1, phi's
recursion/decomposition, and Lemma 2's length-one base and last-bit-zero
induction; the paper states the last-bit-one case is analogous.

For a prescribed admissible parameter list the corresponding word is
(OOEO)^J_i O^H_i E^a_i concatenated over the 23 occurrences. Its length
and odd count are N and K, both positive. L041 already records its exact
shifted word map, so the cited coding theorem supplies prescribed-word
closure without a new general coding proof. It does not certify the
extra guards or scaling conditions. In particular, rational numerator
parity is not positive-integer residue-20 realization. A witness must
still check every retained constraint together; a closing height cannot
be chosen independently of the word parameters. No specialization or
feasibility calculation is performed in this literature turn.

Reuse the stronger-source comparison in
`2026-10-10-fixed-pair-cyclic-product-range.md`: its inspected Lemma 5/
Corollary 1, pp. 230–231, and Theorems 1–4, pp. 235–236, optimize or
bound the global cycle minimum over parity rotations. That minimum is
not the selected designated junction s_0-23/11. Those statements do not
provide an assignment satisfying this system or an inspected matching
infeasibility theorem. Their entire analytic proof chain was not
critically audited, and no additional theorem is imported here.

## Reused integer-cycle inputs and local applicability

John Simons and Benne de Weger, *Theoretical and computational bounds
for m-cycles of the 3n+1-problem*, Acta Arithmetica 117 (2005), 51–70,
[published paper](https://www.impan.pl/shop/en/publication/transaction/download/product/82263):
period conventions p. 52 allow nonminimal representations; Corollary 2
and its proof p. 53 supply primitive odd count K_0>225640000 for
nontrivial positive integer cycles. Lemma 12 and its proof p. 61 supply
Lambda>exp[-13.3(0.46057+log K)]. Reuse the complete proof coverage and
supporting Lemma 8 recorded in the ready L051 audit assessment. Lemmas
6/7 and their complete proofs pp. 58–59, inspected in the ready
`2026-10-10-cyclic-individual-height-feasibility.md`, chain consecutive
local minima using integer height guards and all odd runs. Neither
permits replacing the full minimum count by 23 designated junctions.

Christian Hercher, *There are no Collatz m-Cycles with m <= 91*,
JIS 26 (2023), Article 23.3.5,
[Theorem 16 and full proof pp. 10–11](https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/hercher5.pdf),
bounds the positive linear form by one third of the full odd-input
reciprocal mass. Reuse its complete product/mass proof coverage in the
ready audit assessment. The previously inspected June 2026 correction
leaves Theorem 16 unchanged; amended Theorem 21 is not used.

Read L041's hypotheses, smallest-designated-junction seed, own-index
identities, exact endpoint and length conversion; L046's real-domain
transfer/prefix and applicability passages; L050's separation/product
passages; and L051's hypotheses, proof through its sufficient-test stop.
L041 permits every r>=3. Actual closed words provide the necessary
system with the count-dependent constants transcribed above. The
junction lower bound, nontriviality, represented-period scaling and
cyclic relabeling retain exact independent tails, repetitions and ties.
L046's per-occurrence estimates apply to the real domain using its
explicit guards, not by asserting integer-cycle theorems for reals.
Its eighteen-word exclusion and L050's twenty-word exclusion cannot
be relabeled as twenty-three-word exclusions.

The computational height 301*2^50, distributed [Ro] computation,
Roosendaal communication, continued-fraction denominators 225644606/
397573379 and Rhin/Crandall originals retain their existing qualified
import status. Original certificates, external Lean and full matching
Mathlib coverage remain not checked; no absence claim is made. No
integer computation bound applies to a rational witness merely because
its counts satisfy the retained scaling relations.

## Discovery, duplicates and bounded continuation

Queries on 2026-10-10:

- `Collatz "postspell" "23" cycle real heights`
- `Collatz rational cycle prescribed parity vector affine fixed point Halbeisen Hungerbuhler`
- `Collatz cyclic endpoint simultaneous real height logarithmic guards cycle relaxation`
- `Collatz "postspell" "twenty-three"`
- `Collatz "cyclic endpoints" "real" system feasibility`
- `Collatz "simultaneous" "rational cycles" logarithmic height`

These supplied rational-cycle sources, general cycle material, forums,
repositories and irrelevant endpoint matches. No inspected theorem
matched all the constraints. Search snippets and repository claims are
not mathematical inputs, and unsuccessful searches establish no novelty.
The new m<=95 preprint search lead is unread and unused; no strengthened
full-minimum threshold is needed or substituted. Reuse the fixed-range
assessment's qualified comparison with Fernandez–Ibanez,
arXiv:2607.24844v1, Theorems 7.3/8.1/8.2, without importing that
preprint; its extrema and global-minimum statements are not a supplied
solution of this subsystem. Knight's extremal integer high-cycle lead
remains preview-only and unused. Neither extremality nor integer
realization is a hypothesis here; these are not essential access blockers.

The narrowly checked local records contain no completed simultaneous
test at 23. Attempt 019/L031 concerns positive integer closure and cannot
be used as a rational-real feasibility verdict. Attempts 021–023 retain
their weaker scalar stops, and Attempt 024/L051 retains the fixed-pair
stop at 23. History 135 validates that sufficient predicate only. This
target asks about the individual coupled constraints that those failed
predicates do not decide; another scalar survivor is not useful evidence
for simultaneous feasibility.

Continue with one bounded mathematical attempt after separate approval.
Accept a full exact simultaneous witness or an all-parameter contradiction
from the retained constraints; certify strict logarithmic signs when
load-bearing. If neither is achieved, save the precise unresolved coupled
constraint and honest evidence. Do not renew the failed half-log/T test,
add its conclusions as assumptions, silently change the seed or tails,
or search larger counts. No rational-pair optimization is approved.
An infeasibility proof would extend only the restricted word exclusion,
with the existing integer-source qualifications; a feasible relaxation
would delimit this method without realizing an integer cycle. Universal
entry, unrestricted cycles, divergence and eventual descent remain open.

This is a literature EXPLORATION and completed scope comparison, not a
new mathematical input, negative feasibility result or originality claim.
No lemmas or mathematical scripts were written or run. The existing
mathematical exploration count remains one. SPECIALIZE licenses a later
REPRODUCTION attempt; the newly completed assessment receives separate
supervisor approval before that attempt.
