# L034 critical audit — 2026-10-07

Completed target: Critically audit L034's cyclic minimum count and repeated-period application of Hercher's Theorem 23 under its exact actual positive closure hypotheses.

The pre-invocation SPECIALIZE assessment is
`literature/2026-10-07-two-postspell-minimum-cutoff-audit.md`.
Its TARGET matches this completed action literally; the supervisor's
reported gate mismatch requires no change to that already ready scope.
This is a mathematical proof audit, not a fresh literature assessment
or retroactive approval. Complete L034 and the relevant histories
065/066 and Attempt 019 were inspected. Unfinished work is preserved.

## Scope and discriminating test

Universal eventual descent is the main gap. The intermediate target is
reliability of L034's conditional parameter exclusion; its downstream
use is removing a bounded region of one unresolved cycle language.
The test is whether every cyclic boundary, nontriviality condition and
primitive-period inference matches the imported cutoff. An unmatched
hypothesis or counting error would invalidate or qualify that exclusion.
No existence, least-root, first-return, distinct-junction or primitive
representation assumption may be introduced.

## Complete load-bearing checks

L034's hypotheses provide actual positive integer states throughout
the closed word. At every odd input the next state is strictly larger,
and at every even input it is strictly smaller. Thus a strict minimum
occurrence is precisely an E-to-O input transition, including time zero
across the closing boundary. No intermediate flat step is possible.

Each OOEO copy has just one E-to-O transition. The seams between copies
and the appended odd run are O-to-O, and the final odd-to-even seam is
O-to-E. Since a_i is a nonnegative integer congruent to 2 modulo 18,
both tails are nonempty. Each tail-to-next-word seam contributes one
minimum. These exhaust the possible transitions and establish the
existing exact count M=J_1+J_2+2, counting occurrences rather than
distinct values. The two named junctions may coincide; they are still
different time indices in the represented period. No exact-tail guard
or maximal-run condition is missing: the actual next input is odd.

The initial integer is odd and greater than 1, hence greater than 2.
Neither member of the invariant shortcut cycle {1,2} is this state.
An actual closed orbit containing it cannot be a repetition of that
trivial cycle. Positivity and the map convention match the cited source.

For the least positive return time p, determinism supplies p-periodicity
from the initial state, not just an eventually periodic suffix. Dividing
the known return time N by p gives remainder s with T^s(n)=n; minimality
forces s=0. The input parities and minimum indicator therefore repeat
in every p-step block. At each block boundary the preceding state is
the same as the primitive closing predecessor, so no boundary exception
is lost. Hence M=r m_0 for N=rp, with integral r>=1 and primitive
minimum count m_0. The primitive orbit remains positive and nontrivial.
Hercher gives m_0>=92; consequently M>=92 and J_1+J_2>=90. The excluded
integer region is exactly J_1+J_2<=89 for this necessary bound.

## Primary input and qualifications

Reopened the already assessed primary PDFs on 2026-10-07 to check
applicability, without a new discovery search or expanded source scope:
Christian Hercher, [*There are no Collatz m-Cycles with m <= 91*](https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/hercher5.pdf),
JIS 26 (2023), Article 23.3.5, Definitions 1/5/6, pp. 2–4,
and Theorem 23 with its complete proof, pp. 15–16. The cited theorem's
verification height and numerical proof inputs remain imported;
this audit does not independently certify its computations.

John Simons and Benne de Weger,
[*Theoretical and computational bounds for m-cycles of the 3n+1 problem*](https://deweger.net/papers/%5B35a%5DSidW-3n%2B1-v1.44%5B2010%5D.pdf),
v1.44, 31 August 2010, complete section 1.2, p. 2,
was checked for occurrence counting and permitted nonminimal periods.
It supports the convention; its older numerical cutoff is not used.
The primitive-period reduction independently avoids needing a broader
interpretation of Hercher's represented-period scope.

L034 has no local lemma inputs. L020/L021 name conventions only, which
L034 states explicitly. Neither L031 nor its unresolved divisibility
condition is used to infer existence. The existing DAG row remains
correct. Full matching and supporting Mathlib coverage remains not
checked; no availability or absence is inferred.

## Result and route decision

No defect was identified in the stated specialization. The full proof
and citations remain canonical in L034. This is REPRODUCTION of a local
application of known mathematics, with no stronger bound or advance
beyond the inspected published theorem. Report EXPLORATION: a completed
critical review, not a new mathematical input or a budget-reset claim.
No mathematical script or finite parameter screen was needed.

Attempt 019's automatic-boundary-guard stop remains in force for that
mechanism. Larger closure parameters, positive integer closure, other
cycles, divergent orbits and universal eventual descent remain open.
The argument in PROOF.md and the DAG are unchanged; current review status
is recorded in PROGRESS.md. A separate pending source assessment proposes
testing coverage based on the number of non-unit even runs, rather than
repeating the generic minimum cutoff or automatic-guard audit. No result
for that changed scope is derived or approved here.
