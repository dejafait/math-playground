# Two-postspell ceiling versus general cycle-length lower bounds

TARGET: Compare L039's N<4500 ceiling with a primary published lower bound for the length of a positive nontrivial shortcut cycle, checking primitive and represented counts.
CHECKED: 2026-10-08
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Four focused queries on general cycle-length bounds, Eliahou/Crandall and Simons–de Weger Corollary 2; inspected the primary passages below and Hercher's current corrigendum; reused L039, L035's count/period proof, prior total-length assessment, Attempt 019 and history 069.
SOURCE_EVIDENCE: Simons–de Weger, Acta Arith. 117 (2005), sections 1.1–1.3 pp. 51–53, Lemma 1, Corollary 2 and its complete proof; Hercher's complete two-page corrigendum linked June 14 2026; exact version and access qualifications below.
COMPARISON: Published Corollary 2 supplies a general odd-count threshold far above L039's represented-length ceiling, with matching shortcut map and period convention; the later local application must combine these inputs rather than reprove the source theorem.
GAP: Write the conditional contradiction using L039, L035's represented counts/primitive scaling and Corollary 2, preserving the imported computational qualification; no cycle exclusion is established this literature turn.
REASON: Essential coverage is adequate for one REPRODUCTION theorem-application step at the unchanged target; the two-postspell specialization is local, without a novelty claim.
SCOPE: L039's actual positive closed two-word language with J_i>=2,H_i>=3,a_i>=0 congruent to 2 modulo 18, positive odd residue-20 n,x,n>1, exact independent tails and represented N; retain repetitions and x=n.
LITERATURE_REASON: The saved target was REVIEW_REQUIRED; general length lower-bound coverage was missing from the prior audit, and a newly observed source correction required a narrow relevance check.

The main gap remains universal eventual descent. This intermediate
source comparison could enable a later conditional exclusion of this
specific cycle language. It cannot settle universal entry, other cycle
languages or divergence. No theorem application or new inequality is
derived here; the later applicability specialization is now approved.

Reuse L039 for the audited ceiling, L035 for odd/even occurrence counts
and its primitive-period scaling, and L031 for the closed language.
If a source bounds a primitive period, justify its relation to represented
N; distinguish shortcut steps, odd steps and unshortened steps. Preserve
every source height/computational qualification and cite the exact
version, theorem and pages. First inspect primary statements and essential
proof cases; do not infer a usable lower bound from a search snippet.
Reuse earlier assessments where their actual source coverage suffices.

Continuation test: approve a later specialization only if a precise
inspected theorem supplies a compatible threshold that can conflict with
the ceiling, with all count conversions justified. Otherwise record the
exact mismatch or source blocker and choose an independently testable
target. The full-minimum count cannot be replaced by two (history 069),
and boundary guards alone add no contradiction (Attempt 019). No feasible
exhaustive enumeration, primitive-word hypothesis, global-minimum
identification or least-root assumption is permitted implicitly.

## Inspected primary theorem and qualifications

John Simons and Benne de Weger, *Theoretical and computational bounds
for m-cycles of the 3n+1-problem*,
[Acta Arithmetica 117 (2005), 51–70](https://www.impan.pl/shop/en/publication/transaction/download/product/82263),
published version, not the revised 2010 manuscript. Sections 1.1–1.2,
pp. 51–52, use the shortcut map, K odd inputs and L even inputs;
the chosen period need not be minimal. Section 1.3, pp. 52–53, imports
xmin>301*2^50 from distributed computations [Ro], with a footnote
attributing personal communication to Roosendaal. For a nontrivial
positive m-cycle and a convergent p_j/q_j to log(3)/log(2), j>=4,
Lemma 1 gives

    K > min{q_j, 2*xmin/(q_j+q_(j+1))}.

Corollary 2, p. 53, states K>2.2564*10^8. Its complete one-sentence
proof uses Lemma 1, the stated height bound, q_18=225644606 and
q_19=397573379. This chosen bound is independent of a fixed minimum
count. The computational and continued-fraction inputs are imported,
not independently certified here.

Crandall's original, *On the 3x+1 problem*, Math. Comp. 32 (1978),
1281–1292, was sought at its
[publisher PDF](https://www.ams.org/journals/mcom/1978-32-144/S0025-5718-1978-0480321-3/S0025-5718-1978-0480321-3.pdf);
the request returned HTTP 403. That original proof remains unread.
This does not block importing the precisely stated published Corollary 2
with its complete proof inspected. No independent reproof is needed.
Eliahou's 1993 publisher abstract was a search lead, not an inspected
theorem or accepted additional input; stronger modern bounds are
unnecessary for this comparison.

## Applicability to be written next

L039's audited hypotheses are those in SCOPE. Its ceiling concerns total
represented shortcut inputs. L035 already identifies K,L,N and proves
primitive-to-represented count scaling. Those established facts supply
the intended bridge; neither K nor N may be identified with the number
of local minima or unshortened steps. L039 already checks nontriviality
against the invariant shortcut cycle {1,2}.

The source threshold 225640000 and L039's threshold 4500 pass the
source-comparison test. The next proof must cite Corollary 2, either
using its nonminimal-period scope or passing through the primitive
period using L035. It must preserve the global computational qualification
without identifying a designated junction with the global minimum.
This approves writing a conditional language exclusion, not that exclusion
itself. Entry into the language, other cycles, divergence and universal
eventual descent remain unresolved. No exhaustive enumeration is needed.

## Current correction, duplicates and retained failures

The [Hercher publication page](https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/hercher5.html)
links a corrigendum dated June 14 2026. Both pages of the
[corrigendum](https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/corrigendum.pdf)
were inspected. It repairs an erroneous estimate in Theorem 21's proof
on original p. 14 by a convexity/polytope argument; it does not amend
Theorem 16. L039's load-bearing estimates use Theorem 16 and Simons–de
Weger Lemma 12, not Theorem 21 or Theorem 23. L035's use of L034's
return/count argument does not use its minimum-cutoff theorem. The
replacement proof has not been independently audited here. This narrow
inspection warrants a source note, without a canonical mathematical repair.

Attempt 019's guard-only failure and history 069's two-long-tail count
mismatch remain intact. This comparison uses the full odd count and
does not revive either mechanism. No duplicate local exclusion was
found in the scoped overview, L039/L035 and relevant source/history
records. No novelty inference follows from this search.

Queries: `Collatz nontrivial cycle length lower bound Eliahou 1993 Simons
de Weger 2005 theorem 1`; `Hercher There are no Collatz m cycles 91 2023
cycle length lower bound`; `Crandall 1978 On the 3x+1 problem lemma 1
cycle length pdf`; `Simons de Weger Corollary 2 225644606 cycle lower
bound corrigendum`. Only the explicitly inspected primary passages are
accepted coverage; third-party snippets are unread leads.

This LITERATURE/NOVELTY_UNCHECKED step is EXPLORATION: new coverage
is saved, without a theorem application, lemma, calculation certificate
or mathematical advance beyond the known sources. It spends no mathematical
exploration turn and claims no counter reset. The unchanged TARGET is
ready for a later RESEARCH/REPRODUCTION specialization. Mathlib coverage
of the general lower bound and full specialization is not checked;
there is no cross-notebook input or complete Collatz candidate.
