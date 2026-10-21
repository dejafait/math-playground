# Twenty-four-word simultaneous feasibility — completed source comparison

TARGET: Test whether L051's twenty-four-word real-height subsystem admits a simultaneous solution to all exact cyclic endpoints and own-index guards.
CHECKED: 2026-10-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Three focused searches on postspell/24 cycles, prescribed-parity rational cycles and the exact real-height terminology; read L051 hypotheses/proof, L052 own-count/transfer/ceiling/product passages, L041 all-r seed/own-index identities, L046 real-domain estimates, L050 separation/product passages, Attempts 023/024 and history 139; no inspected result decides the exact system at twenty-four.
SOURCE_EVIDENCE: Reopened Halbeisen–Hungerbuehler Lemmas 1/2 and relevant proof cases in the author PDF pp. 2–3 (published Acta Arith. 78 (1997), pp. 228–229); reused complete inspected Simons–de Weger Corollary 2/Lemma 12 and Hercher Theorem 16 coverage from the ready twenty-three assessments, with fixed-range global-minimum comparisons.
COMPARISON: Known affine coding and integer-cycle bounds remain applicable in their original domains; L041 has all-r necessary-condition coverage, while L052's conclusion and numerical ceiling are specific to twenty-three. None of the inspected results certifies a solution or contradiction at twenty-four.
GAP: A separate mathematical turn must prove an all-parameter contradiction or verify a complete simultaneous witness for exactly L051 (1)–(4) at r=24; neither scalar survival nor a failed separation guard settles feasibility.
REASON: Essential source coverage is sufficient for one RESEARCH/REPRODUCTION attempt using the retained own-count, logarithmic-transfer and endpoint information; no general coding or published cycle-bound reproof is needed. The newly ready assessment receives separate supervisor approval.
SCOPE: Exactly L051 (1)–(4) at r=24, with log24 seed, length term 69*24/1034, integer parameters/counts/scaling, real minimum/lower-height guards, every own-index guard and all exact cyclic endpoints; retain L050's p,q if separation is used.
LITERATURE_REASON: The saved target changes the full simultaneous system from twenty-three to twenty-four; this count-specific comparison reuses adequate general coverage and checks the local conclusion limits, without repeating the stopped fixed predicate.

## Relevance and exact bounded scope

Main gap: universal eventual descent of every positive integer greater than
one. Intermediate target: decide simultaneous feasibility of the stated
necessary-condition system at exactly twenty-four words. A contradiction
would extend the restricted cycle exclusion; a complete witness would
identify limitations of the retained conditions. Neither closes universal
entry, arbitrary-cycle, divergence or eventual-descent gaps.

Essential input IDs: L051, L052, L041, L046, L050. Retain precisely L051
(1)–(4) at r=24: integer J_i>=2,H_i>=3, nonnegative integer a_i congruent
to 2 modulo 18; K=sum(3J_i+H_i), L=sum(J_i+a_i), N=K+L; positive integer
d,K_0,L_0 with K=dK_0,L=dL_0,K_0>225640000; positive Lambda; unchanged
log24 seed and length term 69*24/1034. Keep real s_i>=540/11,
s_0=min_i s_i, all own-index guards, and all 24 exact endpoints including
closure. Independent tails, repeated occurrences and ties remain allowed.
No real junction is assumed to realize an integer parity, residue or
valuation; formal scaling alone does not realize a primitive orbit.

L052's audited per-occurrence estimates are available as existing tools;
its r=23 ceiling and final contradiction are not imported at r=24.
L050's unchanged p=9809721694,q=6189245291 may be used only with a
newly justified admissible bound satisfying the needed separation signs.
No pair optimization, stronger source threshold, tail cap, replacement of
the seed, full-minimum identification, or larger-count search is covered.
This review performs no calculation or specialization proof at r=24.

## Primary sources and reusable coverage

Halbeisen and Hungerbuehler, *Optimal bounds for the length of rational
Collatz cycles*, Acta Arith. 78 (1997), 227–239, DOI
10.4064/aa-78-3-227-239, [author PDF](https://people.math.ethz.ch/~halorenz/publications/pdf/collatz.pdf).
Read PDF pp. 2–3: denominator argument, Lemma 1, phi recursion/decomposition,
Lemma 2, length-one base and last-bit-zero induction; the last-bit-one
case is stated analogous. Lemmas 1/2 (published pp. 228–229) supply
odd-denominator rational parity coding and the fixed point
phi(w)/(2^N-3^K) for a nonempty prescribed binary word. The current
parameter domain makes the word nonempty and Lambda positive. This
provides closure coding, not satisfaction of the retained extra guards
or positive-integer residue realization. Use this citation for any coding
input; no general reproof is justified.

Reuse the primary passages actually inspected in
`2026-10-10-twenty-three-simultaneous-feasibility.md` and
`2026-10-10-twenty-three-infeasibility-audit.md`:

- Simons–de Weger, *Theoretical and computational bounds for m-cycles
  of the 3n+1-problem*, Acta Arith. 117 (2005), 51–70,
  [published paper](https://www.impan.pl/shop/en/publication/transaction/download/product/82263):
  period conventions p. 52, Corollary 2 and complete proof p. 53,
  Lemma 12 and complete proof p. 61. These provide the nontrivial
  positive integer cycle odd-count threshold K_0>225640000 and
  Lambda>exp[-13.3(0.46057+log K)]. Supporting Lemma 8 coverage is
  reused from the fixed-pair audit. They are not theorems about arbitrary
  real junctions. L041's all-r bridge supplies the actual-word application.
- Hercher, *There are no Collatz m-Cycles with m <= 91*, JIS 26 (2023),
  Article 23.3.5, [Theorem 16 and proof pp. 10–11](https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/hercher5.pdf):
  positive cycle linear form less than one third of full odd-input
  reciprocal mass. Reuse the complete product, mean-comparison,
  logarithm and occurrence-partition proof coverage. The previously
  inspected correction leaves Theorem 16 unchanged; Theorem 21 is unused.

L041's seed, own-index identities, shifted endpoint and count conversion
are stated for every r>=3. L046's per-occurrence argument uses the
explicit real-domain guards and endpoint, not its eighteen-word
infeasibility conclusion. L052's tighter own-count and transfer estimates
use those same local guards; its geometric assembly, whole-ray ceiling,
integer separation and final K comparison require count-specific work.
Reusing these estimates addresses stronger retained information than the
stopped L051 predicate; it does not establish their success at twenty-four.

Reuse the inspected stronger comparisons in
`2026-10-10-fixed-pair-cyclic-product-range.md`: Halbeisen–Hungerbuehler
Lemma 5/Corollary 1 and Theorems 1–4 concern global minima over parity
rotations; Simons–de Weger Lemmas 6/7 use full consecutive local minima.
Neither identifies the smallest designated junction with the global
minimum or supplies this exact simultaneous verdict. The previously
compared Fernandez–Ibanez preprint is not imported. Stronger-cycle and
extremal high-cycle leads remain unread/preview-only, unused and
nonessential to this fixed-input attempt.

The published computational height 301*2^50, distributed computation,
Roosendaal communication, continued-fraction and Rhin/Crandall inputs
retain their recorded qualified import status. Original certificates,
external Lean builds and full matching Mathlib coverage remain unchecked.
Unknown coverage is not evidence of absence. No independent verification
of these external inputs is claimed.

## Search evidence, failures and decision test

Queries run on 2026-10-10:

- `Collatz "postspell" "24" cycles`
- `Collatz rational cycles prescribed parity vector simultaneous height bounds Halbeisen Hungerbuhler`
- `Collatz "real-height" "twenty-four"`

Results supplied rational-cycle sources, general cycle material,
repositories and forums; no inspected theorem matched every retained
constraint. Only the primary author PDF was newly read as a mathematical
source. Snippets and repository assertions are not evidence of correctness;
a failed search establishes no novelty. General source assessments are
reused without refreshing unchanged proof coverage.

The narrowly inspected canonical records contain no completed r=24 test.
L051/Attempt 024 stops its specified fixed predicate at twenty-three;
L052 separately excludes the full twenty-three-word system, and history
139 records its completed audit. L049/Attempt 023 retains a weaker scalar
survivor at twenty words. These failures remain valid within their scope;
none supplies simultaneous feasibility or bans stronger endpoint work.
The inherited Attempt 019 closure comparison and fixed-transfer stops
remain as recorded in the reused assessment, without reopening them.

Continue with one bounded mathematical attempt after separate approval.
The acceptance test is a rigorous implication excluding every admissible
parameter list, or a complete verified witness satisfying all retained
constraints together. Load-bearing strict logarithm signs need certified
bounds. A failed ceiling or half-log comparison alone is not feasibility.
If neither outcome is obtained, save the precise failed implication or
unresolved coupled constraint and reassess rather than repeat the old
fixed predicate or increase the word count. Independent universal-descent
gaps remain unresolved even if this target succeeds.

This completes a LITERATURE/NOVELTY_UNCHECKED EXPLORATION: coverage is
ready, but no new mathematical input or feasibility result is established.
No lemma or mathematical script was modified or executed. Mathematical
exploration usage remains one since L052's advance. SPECIALIZE licenses
a separate REPRODUCTION attempt following supervisor approval.
