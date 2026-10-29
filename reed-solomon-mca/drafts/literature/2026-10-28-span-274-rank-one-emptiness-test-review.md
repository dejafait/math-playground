# Span 274 — bounded exact geometric test

TARGET: Test whether saved span 274 admits a nonzero decomposable wedge whose plane has exact rank one for all rows in history (0,51,98,177,318) over the algebraic closure of F_97, without new block-rank tests.
CHECKED: 2026-10-28
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse step 541's exact-history duplicate search, five external queries and local failure comparison in drafts/literature/2026-10-28-span-274-rank-one-obstruction-review.md; no expanded target or fresh calculation is asserted here.
SOURCE_EVIDENCE: L109/L154's all-pivot reconstruction and nonzero-gate template; Stacks Lemma 27.22.1 Tag 089T https://stacks.math.columbia.edu/tag/089T , Lemmas 15.8.4(3)/15.8.7 Tags 07ZA/07ZC https://stacks.math.columbia.edu/tag/07ZA and https://stacks.math.columbia.edu/tag/07ZC , Theorem 10.34.1 Tag 00FV https://stacks.math.columbia.edu/tag/00FV ; reused Gao–Platzer–Clarke CAI 2011 Theorem 4.1/Lemmas 4.1–4.2 https://symbolaris.com/pub/QEfin.pdf . Hypotheses, inspected cases and limitations are in the completed comparison.
COMPARISON: Standard chart/minor/nonzero-atom and algebraic-closure ideal methods supply the tools, not this locus's disposition; instantiate them on the saved complete kernel. No general theorem, four-row finiteness, prescribed-field point or new rank census is sought.
GAP: Bind node 1006/history to saved span 274, then certify emptiness of every normalized chart/open branch or exhibit an exact surviving point/proven nonempty component satisfying all five exact-rank-one gates.
REASON: This tests a necessary geometric gate omitted by the exhausted rank/incidence cover; one history is independently testable without extending that cover. Newly written ready continuation requires separate approval next turn before mathematics.
SCOPE: One saved history only; original 756-label ordering, S=(1,8,12,18,22,27,33), J=(47,50,64,70,75,79,85,89,96), L109 maps and E algebraic closure of F_97. At most the 21 normalized exterior charts and their complete row-nonzero open covers; no candidate-row sweep, new block-rank tests, traversal or cover mutation.

## Inputs and applicability

Use `scripts/pair-free-envelope/cover.json` and `verification.json` for
the complete selected node/span record and previously verified kernel
provenance; `scripts/residual-domination/verification.json` records the
named occurrence. Inspect complete selected values with the shared JSON
inspector, rather than inferring a basis or dimension from a summary.
The pair-free result record and its existing independent verifier bind
the original blocks, complete kernels and nonzero minors. Reuse those
rank results. Checking identities of the emitted geometric certificate
against saved inputs is required; computing new stack/extension ranks
or rerunning the exhausted rank traversal is outside scope.

Use L109 directly for exterior equations, reconstruction and the
necessary exact-rank-one gate; L154 only for the chart/nonzero-witness
template. L170, L159–L161 and a C155a pair parametrization are not inputs.
L169 supplies a previously audited verification method, not a theorem
covering this numerical history. L158 and L162–L165 are comparisons,
not replacements for this seed's equations.

For a coding implication retain F=F_(97^20), the order-sixteen H,
k=8, unit multipliers, 1/4<=delta<5/16, both syndromes in U_S,
sixteen original finite events, t=0, actual nonzero D and locators,
arbitrary original weights/chart, and L104/L086/L010 with inherited
finite-certificate qualifications. The geometric test omits full-weight,
lambda and original-chart gates: its emptiness would suffice to exclude
this history, while its nonemptiness would not give an actual event.
Other histories, arbitrary representation and challenge equivalence
remain open. No symmetry transfer or uniform twelve-row claim is allowed.

## One bounded attempt and decisive evidence

Apply the known template to the complete saved kernel, without assuming
any kernel dimension, common factor, finiteness or generic position.
Retain all nonzero exterior pivots, all 35 Plücker equations and all five
rank-one requirements. Rank at most one and rank zero must be distinguished.
Use the complete principal-open/inverse-witness covers described in the
source comparison, with no finite-field equations or selected-entry
shortcut. Prove coverage of the instantiated branches before claiming
an exhaustive result. Do not silently replace the open locus by an
unverified saturation or its boundary closure.

Try this one kernel by exact elimination or explicit algebraic reduction;
there is no requirement to run a solver if a short complete case argument
suffices. Save unfinished equations/case splits before lengthy work.
An incomplete run returns its exact unresolved branches without expanding
to another history, raising the prior rank cap or launching an unrestricted
solver sweep. No certificate degree or tractability bound is promised.

An emptiness result requires a complete chart/open cover and exact
identities 1=sum H_i f_i against the full instantiated generators, or
an equally complete explicit algebraic case proof. Independently verify
every load-bearing identity and boundary case. A surviving point must
specify exact extension-field arithmetic with an irreducibility check
when a finite-field presentation is used, nonzero wedge, all Plücker
residuals and all five exact ranks. Alternatively certify a genuinely
nonempty component meeting every required open condition; an unchecked
proper-ideal flag is insufficient. No F_(97^20) descent is required for
this algebraic-closure negative test, or inferred from it.

Continue the exclusion route only with the complete emptiness proof.
Any certified survivor/component stops this history's empty-locus route
and must be preserved; it is not a twelve-row or coding counterexample.
Incomplete charts, samples, partial Gröbner bases and timeouts are only
exploration. Scripts must retain full certificates on disk and report
actual versus required branch coverage, failures and paths concisely.
No saved cover is pruned and all 1665 frontier obligations remain.

Classification for the proposed attempt is REPRODUCTION, using known
methods for a new concrete instance, with no source-level novelty claim.
Full matching Mathlib coverage is not checked. Route as calculation,
standard/high; this template specialization does not justify creative
proof routing. The supervisor separately approves this new assessment.
