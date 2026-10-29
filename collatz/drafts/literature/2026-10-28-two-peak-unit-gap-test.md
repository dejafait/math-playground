# Two-peak first-drop descent with a unit intervening even run

TARGET: Attempt a symbolic integer-junction proof of first-drop descent for actual parity words 1^a 0 1^c 0^d with a,c,d>=1, retaining all prefix guards and both possible non-descending endpoint cases.
CHECKED: 2026-10-28
DECISION: EXPLORE
SEARCH_EVIDENCE: Step538's three-mechanism review searched CST/two-local-maxima/two-peak/acyclic-paradoxical/run terminology, compared L002/L005/L109 and Attempts002/003/036, and found no inspected theorem settling this exact unbounded open-word family. This is a bounded source comparison, not a novelty finding.
SOURCE_EVIDENCE: Rozier–Terracol arXiv:2502.00948v5 (2026-05-17), Definition1.2/C1–C3, Remark5.5, AppendixA LemmaA.1 and entire acyclic proof with its separately cited circuit case; Simons–deWeger2005 section1.2, Theorem3(b), section3.3 cyclic chaining; Lagarias1985 pp.7–9/TheoremC and p.11/TheoremE proof sketch; reuse Rozier2019 Lemma1/affine proof pp.2–3 as assessed in the saved first-drop and L109-audit reviews.
COMPARISON: One-peak integer elimination is known; extending it to two chronological odd-run junctions with intervening even length1 is the proposed difference. Closed-cycle exclusions cannot discharge an open endpoint inequality. TheoremE leaves the smallest representative; harmonic-mean bounds lack a closing orbitwise estimate. None is a complete citation for this target.
GAP: No proof or counterexample for this exact target is supplied here. The unresolved task is strict endpoint descent under actual integrality and first-drop guards; success leaves longer intervening even runs, further peaks, and finite coefficient-drop existence unresolved.
REASON: A single symbolic test of a source-suggested structural family could give a partial coefficient-to-actual bridge or expose the exact limit of the two-junction elimination, without restarting sorting, finite sieving or fixed-block descent. This newly written assessment requires separate next-turn approval before research.
SCOPE: Only the stated unit-intervening-run two-peak family and one symbolic elimination attempt; no arbitrary two-peak extension, finite census, extra cycle premise or universal claim.

## Hypotheses of the proposed test

Use T(n)=n/2 for even positive integers and (3n+1)/2 for odd positive
integers. Let n>1 be an actual positive integer with finite parity word

    w = 1^a 0 1^c 0^d,       a,c,d integers >=1,
    j = a+1+c+d.

The word describes states before each application of T. Put
q_k=sum_{i<k} w_i. Require explicitly

    3^(q_k) >= 2^k  for every 0<=k<j,
    3^(a+c) < 2^j.

Thus j is an assumed finite first coefficient drop. The sought conclusion
is T^j(n)<n, with strictness essential. Examine both alternatives
T^j(n)=n and T^j(n)>n when attempting contradiction. Do not replace them
by a single strictly increasing endpoint premise.

The first odd run and intervening even run are exact because the word
contains the next odd state; the second odd run is also exact. The final
zero run is only the observed prefix and may stop before its maximal
length. No parity is imposed on the endpoint T^j(n). No minimum rotation,
seed, closure, primitive period or distinct-junction premise is added.
No universal bound on coefficient stopping time is assumed.

## Inputs and what can be imported

Essential local mathematical input: L002, for the exact first maximal
odd/even block and its integer domain. Use the source finite affine
identity for the truncated second block, rather than assuming that its
final even run is maximal. L005 and L109 and Attempts002/003/036 are
failure/scope comparisons only, not mathematical premises.

The inspected finite input is
[Olivier Rozier, *Parity Sequences of the 3x+1 Map on the 2-adic Integers
and Euclidean Embedding*, INTEGERS19(2019),A8, Lemma1, equation(4) and
proof, printed pp.2–3](https://math.colgate.edu/~integers/t8/t8.pdf#page=2).
Reuse its ready assessment in `2026-10-28-first-drop-swap-margin.md` and
`2026-10-28-l109-critical-audit.md`. It covers every finite parity word,
its integer congruence class and affine endpoint. It asserts no positive
realization of an infinite word. There is no reason to reprove finite
coding; the new work would be the joint integer elimination under the
extra first-drop guards.

[Rozier–Terracol, *Paradoxical behavior in Collatz sequences*,
arXiv:2502.00948v5, 2026-05-17](https://arxiv.org/html/2502.00948v5),
Remark5.5/AppendixA is the structural motivation, not a two-peak theorem.
Its acyclic one-peak proof uses the initial congruence and an integer
endpoint increment. Its equality case invokes circuit exclusion; do not
claim that the acyclic proof covers equality or transplant that conclusion
to two peaks. No circuit theorem is needed as an assumed premise of this
test: equality remains among the cases to examine.

[Simons–deWeger, Acta Arithmetica117(2005),51–70,
section1.2/Theorem3(b)/section3.3](https://www.impan.pl/shop/en/publication/transaction/download/product/82263)
was inspected only to distinguish closed cycles and cyclic chaining.
No theorem from it is imported. Likewise
[Lagarias1985, American Mathematical Monthly92,3–23,
TheoremE, printed p.11](https://web.williams.edu/Mathematics/sjmiller/public_html/372Fa15/addcomments/Lagarias_3x%2B1AndItsGeneralizations.pdf)
is a localization comparison, not a premise eliminating small starts.

## One bounded symbolic attempt and decision rule

Keep the two chronological odd-run starts n and x=T^(a+1)(n).
Use their actual integer/run domains, the finite endpoint identity and
every proper-prefix coefficient guard. Try to eliminate the junction
parameters in the non-descent cases and force a contradiction or a
strictly positive descent margin. This is a proposed proof method, not
a derived formula or an already justified inequality.

Bound this turn by one symbolic elimination pass on this family. Do not
replace it with enumeration of starts, parity lengths or run exponents.
A complete positive result must cover all a,c,d>=1 satisfying the guards,
all compatible positive integer starts, equality and growth alternatives,
and partial final even runs. A valid restricted parameter result can be
useful only with its exact domain and remaining boundary recorded.

Continue on such a proof or a material refined mechanism supported by a
new discriminating inequality. An explicit feasible counterexample to a
named relaxation rejects that relaxation only; verify actual parity before
calling anything a CST counterexample. If elimination leaves an unsigned
expression, save it and label the outcome EXPLORATION, not NEGATIVE or
ADVANCE. Do not repeat the same elimination, extend a census, or enlarge
the family without materially new input. A second unproductive turn must
reassess the mechanism under the shared stopping rule.

Even success supplies no theorem for arbitrary intervening even runs,
arbitrarily many peaks, or existence of finite coefficient drop. The
plausible downstream use is a first non-sorting, orbitwise partial transfer
beyond the sourced one-peak case. A fixed number of blocks is a structural
hypothesis here, never a claimed universal stopping horizon.

## Coverage and approval qualification

The source comparison is recorded in
`2026-10-28-orbitwise-mechanism-discovery.md`. All primitive inputs needed
for this bounded attempt have inspected coverage; no inaccessible Garner,
Terras or Simons source is made an essential dependency. New hypotheses or
techniques outside this scope require their own review.

This nomination contains no new mathematical conclusion and was not
invoked for research in step538. It awaits separate approval next turn.
Full matching Mathlib coverage for the proposed restricted CST statement
is not checked; supporting integer arithmetic is not a matching theorem,
and unknown availability does not imply absence. No cross-notebook input
is proposed.
