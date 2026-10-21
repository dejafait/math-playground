# Two-block five-point fiber: completed source comparison

TARGET: Assess whether L013's size-five ratio fiber can occur for a (5,5,6) partition of the fixed order-sixteen subgroup H, and whether this gives a certified fifteen-count lower-bound test.
CHECKED: 2026-10-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Read L013/C013a completely; inspected the two named programs, their selected certificate fields, history/021 and history/162, ATTEMPTS/006 and the original five-coordinate draft; searched active histories/drafts/attempts for five-point attainment and read L015 and L069's reduction, universal census and separate audit. External queries and inspected statements are below.
SOURCE_EVIDENCE: L015 gives the five-coordinate bound for arbitrary extension-field pencils; L069 Conclusion and complete-census proof give M(A)<=6 for every five-set independently of its triangle application, separately audited October 11. Liu–Mesnager–Tang–Zheng arXiv:2605.11465v1, Definition 3.1 and Proposition 4.1 with proof, supplies rational-fiber terminology, not the fixed-H decision. Mathlib Polynomial.abc supplies only a general radical bound.
COMPARISON: The 256 old two-block partitions were sampled, but the later audited five-coordinate configuration census is complete and stronger in scope than a new partition search. L013 already supplies the conditional fifteen count. Applying L015 and the universal part of L069 to L013 is the missing local specialization to check, not a new census or new split-polynomial theorem.
GAP: Verify all L015 hypotheses for every L013 partition, import only L069's universal configuration conclusion, and compare the resulting full-B bound with L013's size-five case; no such deduction is completed in this literature turn.
REASON: Documented overlap changes the route from a proposed attainment search to a short application of existing results. Coverage suffices for the precise COVERED_TARGET, pending separate next-turn approval; no mathematical script or lemma was changed.
LITERATURE_REASON: Invocation began REVIEW_REQUIRED for five-point attainment and prior-search completeness; the older two-block assessment concerns a different eight-coordinate support obstruction.
SCOPE: F=F_(97^20), fixed H of order sixteen in F_97^*, frozen event on 1/4<=delta<5/16; all disjoint (5,5,6) partitions and exactly L013's inputs. The universal configuration statement in L069 is usable independently of its triangle hypotheses; the triangle bound itself must not be imported outside scope.
COVERED_TARGET: Check whether L015 and L069's audited universal configuration bound exclude every size-five ratio fiber in L013's fixed-H two-block family, retaining the original same-support event and all nonpersistence hypotheses.

## Gap, intended use and discriminating test

The main gap remains sixteen-count feasibility and uniform triangle twelve,
with independent challenge-definition qualifications. The intermediate
question is whether the already proved five-coordinate bound settles
five-point attainment. An explicit five-point fiber would improve the
model-only lower count to fifteen through L013; an exclusion would close
that attainment branch. Neither result would settle arbitrary pencils.
Continue with a short hypothesis-by-hypothesis application if the exact
five-coordinate hypotheses match. Abandon a fresh partition census if
that existing theorem covers the family. If a real hypothesis mismatch
appears, record it rather than assuming the proposed exclusion. No new
mathematical derivation is asserted here.

## Local source comparison and completeness

L013 Hypotheses define a,b supported on A of size five. Its Conclusion
states that D and all locators are nonzero polynomials and gives counts
10, 11 or 15; its proof covers singular parameters, residual repeated
roots, the full extension and same-support failure. C013a displays only
a size-four fiber, ratio 55, with residual root 77.

`scripts/resultant-pencil/check.py`, supplied_pencils, generates 256
random distinct unordered block pairs, followed by two other sampled
families. audit_two_block checks fibers of those inputs only. Selected
complete fields in its result.json give tested=256 and largest-fiber
histogram {1:216,2:40}; these are sample diagnostics. The specialization
routine in `scripts/coefficient-feasibility/five_coordinate.py` checks
only C013a's displayed partition. Its six saved ratios were inspected
in full and match C013a. Neither routine is a complete partition census.
ATTEMPTS/006 stops seeking sixteen from this family, not seeking fifteen.
The October 5 two-block assessment is about L023's two eight-block family
and cannot approve this target merely because of its similar name.

The original five-coordinate draft explicitly includes L013's prescribed
weights as a subfamily. L015 Hypotheses and full analytic proof cover
sigma(a),sigma(b) in U_A with nonzero D and locators, arbitrary F weights
and the original finite chart; its conclusion is |B|<=5+M(A), including
dependent syndromes and cancellations. L069 Conclusion separately states
M(A')<=6 for every five-set. Its census and October 11 audit cover all
4,368 five-sets via 273 disjoint orbits, every 330-point configuration,
14,819,805 point pairs and 29,639,610 directed differences. The full
written verification and separate audit were read; existing computations
were not rerun. Selected full certificate fields confirm actual_maximum=6,
orbit histogram {5:265,6:8}, failures=[]. These fields corroborate the
canonical audited proof; previews alone are not verification. Reuse the
established input with its explicit shared-compiler/residue-field and
finite-computation qualifications. No certificate correctness is newly
audited here. History/162 records that audit, so repeating it is unnecessary.

## External comparison, precise sources and limits

Queries: `finite field completely split polynomial pencil three disjoint
fibers multiplicative subgroup`; `"97" "sixteen" "Reed" "fiber"`;
`finite fields rational functions completely split fibres polynomial abc
Mason Stothers theorem`; `"split polynomials" "pencil" "finite field"`;
`"rational functions" "totally split" "fibers" finite fields`;
`"polynomials" "subgroup" "three" "split" finite field pencil`;
`"Beyond Polynomials" "Good Rational Functions" arxiv`.

Liu, Mesnager, Tang and Zheng, *Beyond Polynomials: Optimal Locally
Recoverable Codes from Good Rational Functions*,
[arXiv:2605.11465v1, 12 May 2026](https://arxiv.org/html/2605.11465v1),
Definition 3.1 defines full disjoint constant fibers on P^1(F_q).
Proposition 4.1, statement and proof, identifies finite rational fibers
with places above a finite value and full fibers with total splitting.
This is useful terminology; it does not force a third prescribed fiber
inside H after two fixed five-root blocks. Its later quantitative theorems
and cited polynomial classifications were not inspected or used as premises.
No Galois hypothesis or distribution estimate is assumed for U/V.

[Mathlib Polynomial.abc](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/FLT/MasonStothers.html#Polynomial.abc),
[source commit 2f3c7c8a8949b04a32f9303f59163acffb766996](https://github.com/leanprover-community/mathlib4/blob/2f3c7c8a8949b04a32f9303f59163acffb766996/Mathlib/NumberTheory/FLT/MasonStothers.lean),
was inspected for its exact field, nonzero, coprimality and sum-zero
hypotheses and derivative-zero alternative. It supplies degree-plus-one
radical bounds, without a fixed subgroup fiber classification. No new
specialization of that inequality is needed or proved. O'Sullivan's
182-page algebra PDF was opened but a theorem-number find failed; it is
not a checked theorem input. No exact external attainment theorem was
found in this bounded search; this is not evidence of novelty. Full
Mathlib coverage of the fiber exclusion is not checked. L013/L015/L069
remain the load-bearing local inputs; their checked computational scope
is more relevant than general rational-fiber sources.

## Continuation and unresolved assumptions

Essential inputs: L013, L015 and only L069's universal configuration
bound; L008/L010 remain inherited moment/event inputs. Keep r!=0,1,
disjoint (5,5,6) blocks, fixed field/domain and original same-support
failure. The application must check support-image membership,
nonpersistence and every degeneracy rather than import L069's conditional
triangle count. A matching bound would eliminate the proposed fifteen
attainment test without a new search. No unconditional fiber exclusion
or new challenge bound is recorded until that application is written in
a research turn. The newly ready COVERED_TARGET requires separate approval
next turn under the shared rule. Existing unfinished work is preserved.
