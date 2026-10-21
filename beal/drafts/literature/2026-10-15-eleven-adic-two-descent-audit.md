# L073 eleven-adic two-descent audit — source coverage approved

TARGET: Critically audit L073's full eleven-adic cubic factorizations, exceptional Kummer evaluations and complete valuation images.
CHECKED: 2026-10-15
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the exact-curve and odd-prime descent searches in drafts/literature/2026-10-15-eleven-adic-even-valuation-containment.md; compared the complete L073 proof with its source scope, ATTEMPTS/033 and history/231. Reopened the three primary sources below for the audit-specific hypothesis comparison; no repeated broad search or novelty claim.
SOURCE_EVIDENCE: Barrera Salazar–Pacetti–Tornaría, arXiv:2001.02263v3 (17 September 2020), Section 1 p.3 and Lemma 1.3/Remark 1.4 p.4, https://arxiv.org/pdf/2001.02263v3; Bruin–Stoll, 14 March 2008 author manuscript, Section 2/Remark 2.1 p.3 and Section 9 p.15, https://mathe2.uni-bayreuth.de/stoll/papers/twocoverdescent.pdf; Clark, accessible 161-page author notes, Theorem 1.79 p.58 and Proposition 2.9/Corollary 2.10 p.65, https://plclark.github.io/PeteLClark/Expositions/8410FULLL.pdf. These passages were inspected this turn; Theorem 1.75 p.57 coverage is reused from the prior assessment.
COMPARISON: The general results cover the exact audit with split and partially split local cubic algebras, exceptional root evaluations and arbitrary finite extensions of Q11. No containment or global no-two-torsion hypothesis is needed for the local size formula. The remaining work is independent verification of L073 arithmetic and exhaustive-image certification, rather than reproof of these general theorems.
GAP: Source coverage is adequate; independent mathematical audit remains outstanding. Global realization of the odd class, global all-finite-even containment, class-norm data, rank and primitive integer lifting remain unresolved.
REASON: Separate audit-scope comparison now completed: approve the unchanged target for one REPRODUCTION proof_audit next turn. This source approval does not verify L073.

## Concrete continuation and bounded test

Essential inputs: L033's exact K and E0; L041's ENTIRE base algebra
Q11 x Q11 x Q11[r]/(r^10+55); L069's SAME θ and g with its
origin-preserving coordinate change and discriminant; L073's full proof.
No cross-notebook theorem is used. Import general source inputs through
precise citations rather than reprove their statements.

After separate coverage approval, check the following load-bearing points:
α's simple lift, the complementary quadratic and discriminant identity;
its full splitting field and maximal valuations; sqrt(5) and sqrt(-11)
in the actual degree-ten completion; all three CRT factors and dimension
36; exceptional class formulas including their nonzero entries; the
nonsquare residues and independence of the displayed classes; and BPT's
full-image size formula without additional containment assumptions.

Continue if every statement, valuation normalization and exhaustive-image
argument is justified. If any fails, identify and repair the exact error,
then reassess whether the odd local point still certifies the route stop.
Do not infer global point realization from the local two-torsion point,
a global counterexample to L072 containment, or a rank/branch exclusion.
Full Mathlib matching and supporting coverage remain not checked.

## Approval record — 2026-10-15

LITERATURE_REASON: The prior turn proposed this audit with REVIEW_REQUIRED; this separate turn compares the essential source hypotheses for that exact target. The already ready containment assessment is reused rather than refreshing its broad literature search.
SCOPE: Exactly TARGET, using L033, L041, L069 and the full L073 proof; both rational places, the actual degree-ten completion, full cubic algebras, exceptional evaluations and image-size exhaustiveness. No global containment, rank calculation or new descent-support target is approved.

The supplied overview and DAG were used before loading L073. The
recorded failure in ATTEMPTS/033 is the result to audit, not an independent
proof or a global ban. History/231 records the same pending audit, with
no duplicate completed audit found in this targeted check.

**BPT comparison.** Section 1 starts with a monic square-free cubic over
a field of characteristic different from two, not necessarily irreducible.
Lemma 1.3 then assumes a finite extension of Qp and gives the full image
order as [O:2O] times the rational two-torsion order. Remark 1.4 explicitly
allows products of local fields. These local statements precede the
additional containment hypotheses and do not inherit the introduction's
global no-two-torsion assumption. Thus neither split roots nor bad
reduction at eleven is a source-scope blocker. The audit must still
certify the actual two-torsion orders and enough independent classes;
size alone does not establish their valuations or independence.

**Bruin–Stoll comparison.** Section 2 assumes characteristic zero and a
square-free polynomial. Its root-point prescription applies after
factoring off a rational root. Remark 2.1 explicitly replaces the even
degree scalar quotient by the full algebra modulo squares for odd degree;
the monic infinity value is one. Section 9 provides the genus-one descent
interface. Hence L073's exceptional formula is within the cited scope at
both types of completion. Component values, nonvanishing and model
compatibility must still be checked; no finite disk enumeration is used
or required by the proposed proof.

**Clark comparison.** Theorem 1.79 requires a complete field, integral
polynomial and the strict Hensel–Newton inequality. Proposition 2.9
requires a DVR, monic polynomial, all lower coefficients in the maximal
ideal and constant coefficient outside its square; it identifies the
root uniformizer and residue field. Corollary 2.10 identifies the integral
closure. These match the proposed lifting and Eisenstein uses; the audit
must verify each concrete hypothesis. No theorem about polynomial-order
maximality from repeated residue factors is being imported.

No essential unread source remains for this bounded audit. The prior
Simon lead is unnecessary: its irreducibility restrictions are avoided
by the inspected full-algebra inputs. Mathlib matching and supporting
coverage remain not checked. No lemma, mathematical script, PROOF or DAG
was changed. Continue only after independently checking the full proof
and every claim in the bounded test above; repair a failed claim before
relying on the route stop. This is source-coverage progress, not a new
mathematical result or a completed critical audit.
