# Double-gap endpoint bound — completed source comparison

TARGET: Assess known results and obstructions for the bound T^j(n)<=n+1 on actual first-drop words 1^a0^2 1^c0^d with a,c,d>=1.
CHECKED: 2026-10-29
DECISION: EXPLORE
SEARCH_EVIDENCE: On 2026-10-29 searched Collatz with two peaks/stopping time, coefficient stopping time/two runs, paradoxical sequences/two local maxima, two blocks/paradoxical, and 1^a/stopping/two; inspected the primary passages below and reused the exact finite-word, localization and cycle assessments. No inspected theorem supplies this unbounded b=2 open-endpoint bound; this is not a novelty finding.
SOURCE_EVIDENCE: Rozier2019 Lemma1/equation(4)/affine proof paragraph, printed pp.2–3; Rozier–Terracol arXiv:2502.00948v5 (2026-05-17), Definition1.1–1.2/C1–C3, Remark5.5 and AppendixA LemmaA.1/complete proof; Niu arXiv:2605.13886v1, Theorem2 statement and section3 proof paragraph (not its deferred AppendixA), Theorems4,7 statements/displayed proofs and section7 scope; reused saved Simons–deWeger2005 and Lagarias1985 comparisons without rereading their unchanged sources.
COMPARISON: Finite parity coding covers the changed word but supplies no uniform endpoint cap. The inspected structural exclusion has one peak; published m-cycle exclusion assumes closure. Fixed-length counting and bounded-length density conclusions do not cover unbounded a,c,d or every compatible start. L110's b=1 proof is a method reference, not a b=2 theorem.
GAP: The b=2 bound remains unproved and unrefuted here. A separate symbolic integer-junction attempt must preserve every first-drop guard, exact internal runs and a potentially partial terminal run; finite-drop existence and other shapes remain independent gaps.
REASON: Essential primitive coverage is available for one established-route extension of L110; no new finite-coding proof, cycle premise, census or enlarged family is needed. The separately saved mathematical assessment is a nomination for supervisor approval, not mathematical execution in this turn.
SCOPE: Literature-only review of the stated bound; no lemma, mathematical script, b=2 endpoint identity, parameter reduction or counterexample was derived.
LITERATURE_REASON: The exact middle even-run hypothesis changes from1 to2, leaving essential open-endpoint source coverage missing.

## Proposed scope and discriminating test

Retain the shortcut T, n>1, actual finite parity word and all first-drop
guards of L110, with only the middle run changed to exactly two even
steps. Thus j=a+2+c+d, q_k counts actual odd steps, every proper prefix
satisfies 3^{q_k}>=2^k, and 3^{a+c}<2^j. Both odd runs and the middle
even run are exact; the terminal d even steps may be partial. These
are proposed hypotheses, not facts about every orbit.

The proposed endpoint bound would be useful because an integer endpoint
at most n+1 reduces non-descent to equality or unit growth, as in C110a.
Any reuse of that argument would still require checking its changed
word hypotheses; no such application is approved here. Longer middle
runs, additional peaks and finite coefficient-drop existence remain
independent gaps.

The main gap remains universal eventual descent; the cap would narrow
non-descent in this one family to equality or unit growth. It would not
itself eliminate equality or establish finite coefficient-drop existence.

## Inspected primary coverage and its boundary

[Rozier, INTEGERS19(2019),A8, Lemma1, equation(4), printed pp.2–3](https://math.colgate.edu/~integers/t8/t8.pdf#page=2)
gives the congruence class for every finite binary word; its proof gives
the affine iterate identity. The changed finite word lies in that scope,
including a truncated final run. Import this input; reproof is unnecessary.

[Rozier–Terracol v5](https://arxiv.org/html/2502.00948v5), Definition1.2
separates stopping and coefficient stopping. Remark5.5 motivates fixed
numbers of maxima; AppendixA LemmaA.1 excludes one peak, handling equality
by a separate circuit result and growth by integer/congruence algebra.
Its proof does not state a two-peak result. The abstract page confirms v5
as the latest posted revision. No heuristic in section6 is imported.

[Tong Niu, arXiv:2605.13886v1](https://arxiv.org/html/2605.13886v1),
Theorem2 covers finite residue classes; Theorem4(i)–(ii) and their proof
express paradoxicality through an affine threshold for each fixed word.
Theorem7 and its proof concern bounded lengths. These are comparisons,
not imported counting formulas or certificates. Section7 expressly leaves
CST open. None supplies the proposed cap over unbounded run lengths.
The displayed v1 metadata and internal manuscript date differ; this
review identifies the retrieved version and makes no chronology claim.

Reused `2026-10-28-orbitwise-mechanism-discovery.md` for
[Lagarias1985 TheoremE, printed p.11](https://web.williams.edu/Mathematics/sjmiller/public_html/372Fa15/addcomments/Lagarias_3x%2B1AndItsGeneralizations.pdf):
its least-representative exception remains. Reused
`2026-10-28-l110-equality-cycle-exclusion.md` for
[Simons–deWeger2005 Theorem3(b), printed p.55](https://www.impan.pl/shop/en/publication/transaction/download/product/82263):
closure is essential; it cannot bound an open endpoint. Neither theorem
is an input to the proposed cap proof. No inaccessible source is essential.

## Local overlap, failures and decision

Read L002 in full through its mathematical proof, L110's hypotheses,
conclusion and endpoint-cap proof, the saved unit-gap assessment and
step538 source comparison, and Attempt036. L002 allows arbitrary exact
internal even length; L110 and C110a restrict their conclusions to length1.
No b=2 result is imported from them. The failed swap-margin ordering in
L109/Attempt036 remains stopped; direct junction elimination does not
assume that ordering or fixed-block descent. Unfinished work is preserved.

The exact mathematical nomination is in
`2026-10-29-two-peak-double-gap-symbolic-test.md`. Continue only after its
separate approval. One symbolic pass may establish the cap or a precisely
stated useful subcase; an actual counterexample rejects the cap, while an
unsigned expression is EXPLORATION and must be saved rather than hidden.
No finite census or new family is authorized. Matching Mathlib coverage
is not checked; unknown availability is not absence. This review makes no
claim of original mathematics or progress beyond the inspected sources.

The [MathPrize page](https://mathprize.net/posts/collatz-conjecture/), dated
2021-07-07 and retrieved 2026-10-29, explicitly states iteration of n/2
when even and 3n+1 when odd reaches1 for every positive integer. This
matches GOAL.md; prize adjudication remains separate. No argument overview
or DAG change is warranted by this source-only step.
