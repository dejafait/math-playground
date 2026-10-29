# Coefficient-supercritical prefix escape — completed bounded discovery

TARGET: Compare at most three primary arithmetic mechanisms for escape from coefficient-supercritical parity prefixes and nominate at most one bounded pointwise test.
CHECKED: 2026-10-28
DECISION: EXPLORE
SEARCH_EVIDENCE: Step536 compared exactly three mechanisms: finite residue sieving, 2-adic coding/rationality, and Diophantine lattice separation. Targeted local comparison used L001/L003/L109, Attempt020/036 and step534; primary queries, inspected passages and access failures are recorded below. No bounded pointwise test is nominated.
SOURCE_EVIDENCE: Read Rozier2019 Lemma1/affine proof pp.2–3, Theorem1/proof p.4, Corollary2 and Example3 p.6, and section3.3/Conjecture1 pp.7–8; Nashida r7 author repository's displayed Theorem1.1 and definitions, plus S13B.lean hgt_thm1 statement and essential proof branches; reused the saved Rozier–Terracol v2 assessment. Terras1976 primary PDF access failed; no theorem from it or Bugeaud2002 is imported.
COMPARISON: Finite coding does not control escape of a fixed integer; 2-adic coding does not supply positive realization or the conjectured rationality implication; the inspected lattice source bounds survivor counts under an explicit external hypothesis and does not supply the needed single-orbit bridge. These are scope findings, not new obstructions or novelty claims.
GAP: Finite coefficient drop for every fixed n>=2 remains open, independently of coefficient-to-actual descent. None of the three inspected mechanisms supplies a justified bounded pointwise test with its missing arithmetic premises discharged.
REASON: Complete the saved discovery target without manufacturing a lemma or repeating failed swap/digit forcing. Park direct applications of these mechanisms; prepare a separate audit of the existing negative L109, whose finite inputs are covered, while preserving the central escape gap.
SCOPE: Completed literature comparison only; no new result, lemma/program write, theorem import or mathematical calculation. EXPLORE here records the completed discovery and does not approve an unspecified escape mechanism.
LITERATURE_REASON: The separate pre-drop existence gap was outside the ready swap-margin assessment; primary coverage for a pointwise escape mechanism was missing.

## Completed comparison — step536, 2026-10-28

Main gap: eventual descent for every positive integer. The intermediate
target is arithmetic escape from prefixes with 3^q_k>=2^k for every
prefix k, where q_k counts ones before step k. Its plausible downstream
use is finite coefficient drop; converting that to actual descent is
still independent. The [MathPrize statement](https://mathprize.net/posts/collatz-conjecture/)
was rechecked today: the July7,2021 ordinary-map positive-integer target
is unchanged. No prize-adjudication conclusion is involved.

### Three mechanisms and their missing premises

1. **Finite residue sieve.** [Rozier, INTEGERS19(2019), A8,
   Lemma1 pp.2–3 and Theorem1 p.4](https://math.colgate.edu/~integers/t8/t8.pdf#page=2)
   give finite parity classes and inverse formulas. Both affine and
   conjugate-map proofs were read. This is arithmetic information at
   each finite depth, without a bound forcing escape for a fixed start.
   A new test would need a separate quantitative integer-height input.
   Merely extending a finite census is not such an input. Terras,
   *A stopping time problem on the positive integers*, Acta Arith.30
   (1976),241–252 remains an unread primary lead in this step: the
   indexed theorem text was not substituted for the inaccessible PDF.
   No new density theorem is imported or relied upon.

2. **2-adic coding and rationality.** Rozier's Corollary2 and Example3,
   p.6, concern all infinite binary words and their unique 2-adic
   preimages; the all-ones example represents -1. Section3.3,
   pp.7–8, labels rational x implying rational Q(x) as Conjecture1.
   Neither positive realization nor this implication is an established
   escape input. In particular a real series sign cannot replace
   equality with its 2-adic limit. No such transfer is proved here.
   Any future restricted symbolic-language test needs a new, explicit
   arithmetic restriction; no language is selected merely to produce
   another finite negative-cycle example. L003 is the existing local
   warning about compatible finite prefixes versus one positive orbit.

3. **Diophantine lattice separation.** The inspected primary is
   [Hiroyuki Nashida, *A strict improvement of the Terras-type bound
   for integers with long Collatz stopping times*, author repository,
   revision r7, September28,2026](https://github.com/harappa/collatz-terras-bound-improvement),
   displayed Theorem1.1 and NKcount/SurvW definitions. Conditional on
   Thm1G1(8), it bounds coefficient survivors up to 2^(alpha K),
   1/2<alpha<=0.659, by 2^((alpha(1-c)-epsilon)K) for sufficiently
   large K, some epsilon>0, c=1-H(1/log2(3)). This is a count bound.
   Its [S13B.lean hgt_thm1](https://raw.githubusercontent.com/harappa/collatz-terras-bound-improvement/master/CollatzProof/M1/S13B.lean)
   gives max(|a|,|b|)>=q*2^D*(q*2^h+1) for integer (a,b)!=0,
   a=3^L b modulo 2^(q+D), with D=floor(cD q), 0<cD<=0.009,
   1<s/q<=1.94 and 0<=h<=10^-8 q, h=L log2(3)-s, for all sufficiently
   large natural q, uniformly in natural s,L, conditional on Thm1G1(8).
   Inspected gcd, zero-difference, oddness, exceptional-ratio and
   logarithm-application cases; not the full numerical/counting assembly.
   No theorem or Lean certification is imported. A bridge
   from an individual affine parity prefix to the requisite short
   homogeneous vector remains missing. The count conclusion alone
   does not discharge that premise or establish pointwise escape.

The third source remains an unaudited preprint. Version r7 was kept
separate from the discovery index's r6 description. The Zenodo redirect
failed; author text/code were readable. Bugeaud2002's printed statement
was not read, so its transcription and applicability remain unverified.

### Duplicates, stops and decision test

Read the full local L001, L003 and L109 statements/proofs and
Attempt020; compare Attempt036 and step534's saved assessment. L001's
witnesses depend on the horizon; L003 already disposes of its repeated
growing block as a positive infinite-word construction. Attempt020's
missing zero runs remain missing. L109 rejects the tested margin order
only. None is a global ban, and none becomes a premise for escape.
Targeted duplicate searches in the October28 assessments and ATTEMPTS
found no assessed single-orbit lattice bridge; failure to find one is
not a novelty claim. Broader matches concerning cyclic-table survivor
roots were unrelated and were not loaded as mathematical inputs.

The continuation criterion was a primary input plus an explicit
pointwise specialization whose missing part admits a decisive bounded
test. None passed. **No pointwise test is nominated.** Abandon direct
finite-coding, rationality-conjecture and count-to-pointwise upgrades
without a materially new bridge. This is a completed bounded discovery
with outcome EXPLORATION, not a mathematical negative or advance.

The separately proposed continuation audits the already recorded L109
negative; it does not solve or relabel the escape gap. Its assessment
is `2026-10-28-l109-critical-audit.md` and requires separate approval.
Essential local inputs for that audit are L109's own statement and
certificate plus its two finite primary imports; L001/L003/Attempt020
are contrasts only. No cross-notebook input is used. Unknown Mathlib
coverage is not absence; no matching pointwise theorem was checked.

### Search and access record

- `Collatz finite stopping time positive integers infinite stopping time parity vectors Terras theorem arithmetic constraints`
- `Collatz "Terras" "Bugeaud" lattice stopping time 2026`
- `"A stopping time problem on the positive integers" Terras 1976 pdf`
- `Collatz coefficient stopping time least residue growth non periodic parity positive integer Rozier`
- `"Collatz" "Bugeaud" "lattices"`
- `"Terras" "stopping" "height" lattice bound`

Local searches were restricted to this notebook's assessments, ATTEMPTS,
foundations and the named canonical proofs. Terras's matwbn PDF returned
403 (also through HTTP); its download variant and EuDML205476 were
inaccessible. A publisher download attempt did not resolve a readable
file. These are access failures, not theorem evidence. Discovery-site
abstracts, other repositories, informal discussions and search snippets
were leads only. No additional mechanism from them was assessed.

## Preserved startup nomination (historical, not new approval)

## Named gap and intended comparison

For a finite parity prefix of length j, write q_k for the number of
ones before step k. The language to be examined has
3^q_k>=2^k for every 0<=k<=j: coefficient contraction has not yet
occurred. The independent unresolved claim is that a fixed positive
integer n>=2 cannot remain in this language forever. This is an
unproved claim, not an imported premise or a disguised new lemma.
Even a useful result here must account separately for the gap between
coefficient contraction and actual descent.

Read primary hypotheses and essential proof cases for at most three
concrete arithmetic mechanisms. In particular, distinguish information
from congruences on integer endpoints from assertions about typical
parity vectors or positive realizations of infinite words. A finite
coding bijection alone is not a pointwise escape estimate. No candidate
or theorem comparison is claimed to have been completed in this file.

Use L109 only for the failed directed margin comparison and use L001,
L003 and Attempt020 as obstruction-scope contrasts. Read the exact
needed canonical statements if a candidate overlaps them; the prior
stops are not global bans. Do not revive bounded-window/block descent,
presumed zero-run forcing, or an altered swap order without a materially
new input and its own assessment. No cross-notebook input is proposed.

The prospective downstream use is a pointwise finite-drop input or an
intermediate restriction that could help establish it. Do not count
an equivalent reformulation of this missing claim as progress.

## Continuation and abandonment test for the future review

For each candidate actually examined, record its primary theorem and
hypotheses, strongest usable conclusion, overlap with the named failures,
and the precise missing specialization. Nominate at most one later
bounded calculation or proof test with a decisive outcome; give exact
input IDs and all unresolved assumptions in its assessment. An
uninspected lead remains a lead. If none supplies a justified test,
record that discovery outcome without inventing a claim or beginning
mathematical work. This file is REVIEW_REQUIRED, not approval.

## Existing finite references and Mathlib qualification

- [Rozier, INTEGERS19(2019), A8, Lemma1 and affine proof, pp.2–3](https://math.colgate.edu/~integers/t8/t8.pdf#page=2): finite parity classes only, reused in the completed step535.
- [Rozier–Terracol, arXiv:2502.00948v2, Definition1.2](https://arxiv.org/html/2502.00948v2#S1): the finite or infinite coefficient stopping time definition; no pointwise finiteness theorem is assumed.

Full matching Mathlib coverage for the unselected future target is not
checked. Unknown availability does not establish absence.
