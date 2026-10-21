# Count-dependent length bound — completed source comparison

TARGET: Establish explicit functions A(r),B(r) with N<A(r)log(N)+B(r) for every actual closed concatenation of r>=3 postspell words with independent exact tails.
CHECKED: 2026-10-08
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Four focused general-cycle and exact-word searches; primary chaining and effective-bound passages compared with L031/L035/L037/L038, ready balance/total-length/odd-count assessments, history 069 and Attempt 019; queries and limits below.
SOURCE_EVIDENCE: Simons–de Weger, Acta Arith. 117 (2005), sections 1.1–1.3 pp. 51–53, Lemmas 6/7 with complete proofs pp. 58–59, Lemma 8 with proof p. 59 and Lemmas 12/14 with proofs p. 61; Theorem 3 cases and large-m proof coverage reused from the ready total-length assessment; Hercher Theorem 16 with full proof pp. 10–11 inspected; prior correction and odd-count coverage reused.
COMPARISON: General effective ceilings depend on the full minimum count, not designated word count r; no inspected theorem supplies this variable-r target. Local single-word mass, valuation and transfer calculations cover the required word hypotheses, while their uniform cyclic assembly and explicit functions remain to be proved.
GAP: Extend the existing wordwise calculations to all r occurrences, obtain and solve a count-dependent represented-length inequality, and test its r=3 ceiling against 225640000 without tail caps or global-minimum identification.
REASON: Essential changed-scope comparison is complete; approve one later REPRODUCTION proof attempt at the unchanged target using cited cycle inputs and justified extensions of the existing local calculations, without reproof of general cycle or transcendence theorems.
SCOPE: Integer r>=3; W_i=(OOEO)^{J_i}O^{H_i}E^{a_i}, J_i>=2,H_i>=3,a_i>=0 congruent to 2 modulo 18 for every i; actual positive closed concatenation from n_0>1, all r junction occurrences positive odd and 20 modulo 27, exact independent tails, represented shortcut length N; repetitions and coincident junctions admitted.
LITERATURE_REASON: The variable-r target changes the two-word scope; the essential missing comparison is whether general chaining/minimum-count bounds or the inspected single-word calculations support a uniform designated-junction assembly.

## Relevance and bounded test

The main gap is universal eventual descent. The intermediate target is
explicit finite positive A(r),B(r), uniform over the word parameters.
A fixed-r ceiling could support a later restricted-cycle exclusion by
comparison with the published primitive odd-count threshold. Entry into
this language, other cycles, divergence and eventual descent remain
independent unresolved gaps. No complete candidate is proposed.

Continue only if every junction can be controlled with explicit constants
and represented counts, with no uncontrolled tail or height assumption.
The first usefulness test is a rigorously justified r=3 ceiling below
225640000. If the obtained estimate misses this threshold, abandon that
estimate as an exclusion mechanism; do not infer existence of cycles.
Failure to obtain a uniform cyclic estimate also stops that calculation.
No multiword coefficient, inequality or ceiling is derived this turn.

## Primary inputs and stronger-result comparison

Simons and de Weger, *Theoretical and computational bounds for m-cycles
of the 3n+1-problem*, [Acta Arithmetica 117 (2005), 51–70](https://www.impan.pl/shop/en/publication/transaction/download/product/82263),
uses shortcut counts K,L and permits nonminimal periods (section 1.2).
Its Lemma 6 chains consecutive local minima; Lemma 7 iterates that
estimate through all m minima. Both full proofs were read. Lemma 14
compares Lemmas 7 and 12 to bound K by an m-dependent root.
Theorem 3(a),(d) supplies fixed-m finiteness and effective ceilings;
its statement/proof-case coverage is reused from the ready total-length
assessment. These results retain the full minimum count, which is not
bounded merely by fixing r in the proposed language. Substituting r for
m would drop intervening minima and is not licensed by these theorems.

The precise effective input remains Lemma 12, p. 61:
Lambda > exp[-13.3(0.46057+log K)], where Lambda=N log2-K log3.
Its proof and the supporting Lemma 8 proof were inspected. Published
height computations and Rhin's Proposition remain imports, not locally
certified inputs. Corollary 2, p. 53, provides the comparison threshold;
reuse the ready odd-count assessment, including its computational and
continued-fraction qualifications. No reproof of those theorems is needed.

Hercher, *There are no Collatz m-Cycles with m <= 91*,
[JIS 26 (2023), Article 23.3.5](https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/hercher5.pdf),
Theorem 16 and its complete proof, printed pp. 10–11, bound the positive
cycle linear form by one third of the full odd-state reciprocal mass.
The proof partitions that mass into maximal odd runs; a different
partition must cover exactly the same occurrences. L035 already checks
primitive-to-represented scaling, so the later extension should justify
that applicability without assuming distinct junctions. Reuse the
June 14 2026 corrigendum inspection recorded in the odd-count assessment:
Theorem 16 was not amended; its Theorem 21 repair is not an input here.
The minimum-cutoff theorem does not supply this count-dependent target.

## Local scope comparison, duplicates and failures

Read L035 through its single-word mass calculation (equations (4)–(8))
and its complete period-scaling passage. The single-word calculation
uses positive actual inputs and disjoint half-open input intervals;
its constants are independent of the terminal run and exact tail lengths.
Its displayed two-word conclusion is not an r-word theorem. The later
attempt must write the r-word occurrence assembly and justify its counts.

Read L031's exact boundary-valuation section and L038's transfer and
own-word height sections in full, with L037's supporting boundary-size
calculation. L031's valuation calculation is at one actual word with
J>=2,H>=3 and an odd endpoint after a>=2 even steps. L038's transfer
calculation likewise follows one actual word to its endpoint and retains
both additive shifts; its own-word height calculation uses that word's
valuations. These portions do not assume a tail cap or a global minimum.
Thus their hypotheses match each proposed individual word. However,
L037's selected-boundary estimate and L038's final numerical constants
are conclusions for two words only: neither may be imported unchanged
for r words. A later proof must supply an r-dependent boundary seed and
iterate justified transfers around the represented cyclic ordering.
This is an identified specialization difference, not an established
uniform result or a fresh reproof of parity coding.

The ready assessments reused are
`2026-10-07-two-postspell-logarithmic-parameter-balance.md`,
`2026-10-08-two-postspell-total-length-bound.md`, and
`2026-10-08-two-postspell-cycle-length-comparison.md` in this directory.
L035/L031/L038 are potential inputs; L037/L036 contain effective
supporting estimates, and L039/L040 supply only the two-word comparator.
No duplicate variable-r bound appears in the supplied overview and
these scoped local reads. That finding is not a novelty claim.

History 069 preserves the mismatch between longer tails and full minima;
Brox's later proof remains unread and is not imported. Attempt 019
preserves the guard-only failure. The present proposal uses independent
linear-form estimates and actual height transfer, so neither historical
stop prohibits this distinct test. Keep exact independent tails, cyclic
index occurrences, repeated periods and coincident junctions. Do not
identify the smallest designated junction with the global cycle minimum,
replace represented K,N by primitive K_0,N_0 silently, or use least-root
minimality. Sodelin's source/version and unchecked Lean-build qualifications
remain as recorded in L031; no refreshed external declaration is assumed.
Mathlib coverage for the full variable-r statement remains not checked.

## Search and access record

Queries: `Collatz cycles fixed number local minima upper bound length
Simons de Weger Hercher`; `Collatz cycle postspell OOEO logarithmic
length bound junctions`; `Collatz "postspell" cycle bound`;
`Collatz "OOEO" cycles "bound"`. General results led to the primary
passages above. Exact-word searches returned guarded-descent and
public-ledger leads, without an inspected matching cycle-length theorem.
Those leads remain unread and supply no dependency; failed searches
do not establish novelty. There is no essential source blocker for the
proposed specialization of the inspected inputs. No broader repository
or sibling-notebook orientation was performed.

The [MathPrize target page](https://mathprize.net/posts/collatz-conjecture/),
dated 2021-07-07, was checked on 2026-10-08; its original positive-integer
3n+1/even-halving target agrees with GOAL.md and the recorded conventions.
Prize adjudication remains separate from mathematical correctness.

## Completed decision and continuation

Completed LITERATURE/NOVELTY_UNCHECKED, outcome EXPLORATION: this bounded
source comparison resolves readiness, not the mathematical target.
No source directly supplies the requested functions and no new theorem
or exclusion is claimed. No lemma, mathematical script or certificate
was written. PROOF.md and DAG.md require no changes.

The exact TARGET is now SPECIALIZE for a separate mathematical invocation.
Its first task is to justify the all-occurrence extension of the ready
single-word inputs, then attempt explicit r-dependent functions and the
r=3 usefulness comparison. All uniform assembly claims remain unresolved.
No mathematical exploration attempt was spent and no counter reset is
claimed. The next turn defaults to mathematics under this assessment.
