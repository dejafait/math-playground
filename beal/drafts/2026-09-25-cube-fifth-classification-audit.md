# Repeated-cube fifth-power classification audit — 2026-09-25

## Starting state and relevance

Read the shared GOAL.md and PROMPT.md, local goal and checkpoint, the whole proof overview and DAG, and the existing local changes. No applicable AGENTS.md was found. Existing unfinished work is preserved. Mauldin's accessible primary statement was rechecked and agrees with the recorded target; the nominated AMS page again returned HTTP 403.

The main gap is zero positive primitive solutions for every residual reduced signature. The bounded intermediate target is a primary theorem proving nonexistence of nonzero primitive integer solutions of X^3+Y^3=Z^5, with enough sign coverage to exclude each placement of (3,3,5). Its plausible downstream use is to remove that signature and the original signatures reducing to it through exponent divisors. Other small repeated-cube exponents, complementary large primes, and other mixed families would still remain.

The existing Freitas application explicitly excludes p=5 from its hypotheses. The local-solubility, isolated-factor, exceptional-prime, and primitive-divisor multiplicity failures do not establish this fixed-signature result. A repository search found no already imported classification of (3,3,5). This is a different global input from the stopped multiplicity inference, not a rerun of that inference.

Continue the import only if a precise primary statement gives zero nonzero primitive integer solutions, or a complete classification whose exceptions fail the target hypotheses. Check signs, gcd conventions, zero coordinates, bases equal to one, and every exponent bound. If only fixed-signature finiteness, a bounded search, or a conditional result is available, record that shortfall and do not claim an exclusion. The required and sought threshold is zero solutions, not a lower height bound or finitely many unidentified solutions.

## Unfinished reasoning saved before source work

No classification has yet been imported. If a signed nonexistence theorem is found, the placements map to (X,Y,Z)=(a,b,c), (c,-b,a), and (c,-a,b). These transformations preserve absolute-value gcd and nonzero coordinates. Their exact compatibility with the source's hypotheses remains to be audited.

## Completed source audit and assessment

The [publisher's preview](https://page-one.springer.com/pdf/preview/10.1007/10722028_9#page=2) supplies Bruin's Theorem 2 at n=5 and the adjacent Theorem 1 at n=4, both on printed p. 170. They require integer coordinates and nonzero product and conclude gcd greater than one. Definitions on p. 169 allow signed integers and define triviality by a zero coordinate. Neither statement is conditional. The same bounded source audit therefore includes the adjacent n=4 case; no second mechanism or separate source classification was pursued.

The [foundation](../foundations/06-bruin-small-exponent-theorems.md) records the exact citation, direct links, and access limits. The full proof and associated computations were not reproduced; the numbered published theorems are cited mathematical inputs. The paper's abstract mentions reductions at 7,11,13 but does not claim completion at those exponents. They are not imported here.

[L009](../lemmas/L009-bruin-small-repeated-cube-exclusions.md) applies the signed theorems, lists and proves the zero-coordinate exceptions, and checks all three placements. In particular, moving a cube works when the singleton exponent is even; no fourth power absorbs a sign. The exponent-divisor consequence uses L002, and the complete-system consequence uses L003's converse, whose domain n>=2 includes 4 and 5. Those are the two genuine local mathematical inputs. Earlier failed methods and the other cited exclusions supply context, not premises of this lemma.

The achieved threshold is exactly zero primitive positive solutions for all six ordered reduced signatures, for all original exponent triples reducing to them, and for both complete systems at n=4,5. This fills the intended (3,3,5) gap in the assembly and the adjacent (3,3,4) gap. The factor-only witnesses remain valid and do not meet the simultaneous conditions. No bound has been mistaken for emptiness, and no computation is offered as a proof of the imported theorem.

Outcome: ADVANCE as a relevant cited input, with exploration turns used 0/3. There is no complete Beal candidate. Repeated-cube primes 7,11,13 and the remaining complementary primes are still unexcluded by the assembled results, as are independent mixed signatures. The reason for the next direction is that a primary classification of the remaining small cube exponents could remove further explicit residual signatures with a checkable range. A source lead is Chen–Siksek, *Perfect powers expressible as sums of two cubes*, cited by the literature search; its theorem and qualifications were not audited in this step. The sole concrete next action is in PROGRESS.md.
