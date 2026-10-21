# Order-three pole at 67 agreements — source comparison

TARGET: Review the 67-agreement rational-center family r_{a,b,c}(x)=(x^67+a*x^2+b*x+c)/x^3 on H for a list exceeding 65537^28/2^128.
CHECKED: 2026-10-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Compared the existing pole-at-zero, two-leading-coefficient and degree-67 assessments and ATTEMPTS/007,008; searched rational received words, ending coefficients, restricted-root counts and sum/product constraints; followed the Hayes-class zero-distribution lead to Gao arXiv:2203.06729v5.
SOURCE_EVIDENCE: Read Gao arXiv:2203.06729v5 definitions (1)-(2), (5)-(6), Proposition 2 and its factorization proof, definition (17), Theorem 3 and proof (18)-(19), and Theorem 2/Section 4 Proposition 3 hypotheses; rechecked Gao-Kuttner-Wang arXiv:2109.02000v1 Type I, Proposition 1 and Theorem 1, and Gao arXiv:2105.12845v3 Proposition 2 and Theorem 1.
COMPARISON: A known exact Hayes-class identity permits arbitrary root domains, zero leading constraints and residues modulo X^3; it does not evaluate the requisite subgroup fiber. Older irreducible and rational-distance results do not certify the required list size. Approve only the bounded applicability-and-averaging specialization below.
GAP: Verify the RS/root-product correspondence, three ending coefficients, strict degree, ambient-extension completeness and simultaneous rows; determine the valid class space and compare its averaging certificate with the exact ambient threshold. Maximum fibers remain uncomputed.
REASON: The changed pole and agreement level required fresh comparison; the newly inspected arbitrary-domain identity removes the essential source gap for an elementary test without importing inapplicable full-domain estimates.
SCOPE: E=F_65537, H<=E^* of order 1024, F=F_(65537^28), degree<64, 67 agreements, a,b,c in E with c nonzero, any m>=1 and zero remaining center rows; only the exact dictionary and finite class-averaging certificate. Excludes new character estimates, fixed-fiber evaluation, safety, other rational families and optimization.
COVERED_TARGET: Verify the entire 67-agreement list dictionary for r_{a,b,c}(x)=(x^67+a*x^2+b*x+c)/x^3 on H and compare its proved class-averaging lower certificate with 65537^28/2^128.
LITERATURE_REASON: Denominator X^3 and agreement level 67 are outside L019's ready denominator-X/66-agreement assessment; this turn supplies the missing theorem-level comparison.

## Relevance and intermediate target

The bracket remains 955<=t_star(m)<=957. A common-center list strictly
above threshold at 67 agreements would make error index 957 unsafe.
Arbitrary-center safety at 68 agreements, the exact boundary and the ABF
definition comparison would remain independent gaps. This review proves
no new list bound. The intermediate target is a complete dictionary and
one exact averaging comparison, not an assumption of a large fiber.
Inputs: L001, C012a, L019 and foundations/01-target-and-source-audit.md
and 02-pinned-list-model.md. L019 supplies a comparison, not its new-pole
conclusion. No cross-notebook input is used.

## Closest primary result

Gao, [Asymptotic distributions of the number of zeros of random polynomials
in Hayes equivalence class over a finite field, arXiv:2203.06729v5](https://arxiv.org/html/2203.06729v5),
2024-01-07, permits ell>=0, monic modulus Q, and polynomials coprime to Q.
D is any subset avoiding zeros of Q. Equations (5)-(6) give class sizes.
Section 3 Proposition 2, (15)-(16), and Theorem 3, (17)-(19), give an
exact factorial-moment identity using root-subset/residual-polynomial
counts. Read their factorization and coefficient-extraction proofs,
including the high-j case. Proposed applicability: q=65537, Q=X^3,
ell=0, D=H, k=64, j=67; c nonzero supplies coprimality. The RS and
extension-field interpretations still require verification.

Theorem 1 is asymptotic as k-r grows, not a finite extreme-agreement
estimate. Theorem 2 and Section 4 Proposition 3 require ell>=1 and D
equal to the entire complement of the zeros of Q. Those quantitative
conclusions are not imported. The exact framework, not a threshold-sized
fiber, is covered. No general generating-function theorem needs reproof.

## Reused sources and exclusions

Gao, Kuttner and Wang, [Counting irreducible polynomials with prescribed
coefficients over a finite field, arXiv:2109.02000v1](https://arxiv.org/html/2109.02000v1#S2),
2021-09-05, Section 2 Type I, Proposition 1, (1)-(7), track leading and
ending coefficients with nonzero constant term. Their statement fixes
positive ell and t; a trailing-only specialization is not silently
imported. Theorem 1, (26)-(30), is for irreducible enumeration, not
squarefree root products on H. The newer source explicitly permits
ell=0 and is preferred. The old assessment used an inexact descriptive
title for this paper; the title here matches the inspected version.

Gao, [Counting polynomials over finite fields with prescribed leading
coefficients and linear factors, arXiv:2105.12845v3](https://arxiv.org/html/2105.12845v3#S2),
2022-11-10, Section 2 Proposition 2, (5)-(6), and Theorem 1, (7)-(8),
give the earlier arbitrary-D leading-coefficient/root-factor mechanism.
Read its unique-factorization proof and distinct-tuple case; its
X+alpha convention needs sign checks. It does not prescribe ending
coefficients. Its Section 4 subfield formulas are inapplicable to H,
as already assessed. Use the newer generalization instead.

Reuse the [2026-10-04 assessment](2026-10-04-pole-at-zero-sum-product.md)
for inspected Wu-Hong arXiv:1108.3524 Theorem 1.2 and Keti-Wan-Zhu
errordistance.pdf Theorem 9, pp. 6 and 11-14. Reciprocal deep holes use
the full nonzero field and a different polynomial part. The latter
theorem requires its denominator nonvanishing also at zero and concludes
nearest-distance existence. X^3 still violates that hypothesis, and
existence is weaker than a large-list count. Neither quantitative route
is a dependency; blocked mirrors were not retried.

Reuse the two-leading-coefficient assessment for Lai-Marino-Robinson-Wan
[arXiv:1910.05894v2](https://arxiv.org/html/1910.05894v2).
Freshly checked Theorem 9: additive moments on polynomial images,
a character-bound hypothesis, size inequalities and a positivity
conclusion. It imposes neither the additional product/residue data nor
a threshold-sized list. No moment theorem is imported. The later
second-moment publisher lead remains unread as recorded in that
assessment; it is nonessential to the elementary test.

## Duplicates, failures and version check

L019 concerns denominator X and 66 agreements. L013-L014 concern two
leading coefficients of polynomial centers; L015-L018 count 66-agreement
subsets with a residual factor. These do not evaluate this family.
ATTEMPTS/007 and 008 stop tested norm and quadratic-root allowances;
neither is reopened. Earlier recovery screening in history/137 and
drafts/literature/2026-10-10-embedded-quadratic-common-center.md listed
67-agreement rational witnesses as uncovered without a quantitative
mechanism. No local proof of the proposed dictionary was found.
ATTEMPTS/082's numerical prescription remains parked.

The [prize page](https://proximityprize.org/) was checked on 2026-10-20:
constant m and epsilon* times ambient field size remain the list target.
This does not recover the unavailable ABF PDF. The pinned closed-ball
and simultaneous-column qualifications remain in force.

## Bounded continuation and decision test

After separate supervisor approval, verify the cited identity's
applicability and the elementary RS interpretation, retaining all three
ending coefficients and their signs. Prove division by X^3, strict
degree, injectivity, exact versus extra agreements, extension-field
candidates and every zero remaining row. Determine the actual parameter
space from root products before pigeonhole counting. Do not assume
uniformity, surjectivity or that the denominator-X proof suffices.

Compute one exact integer averaging certificate and compare it with
65537^28/2^128. No large-subset enumeration, maximum-fiber search,
new character estimate, old-energy retuning or optimization is covered.
Continue an unsafe-radius conclusion only for a strictly larger
single-center list. Failed correspondence stops this construction;
an insufficient average parks this averaging certificate without
inferring family safety. Stronger fiber estimates need a different
explicit mechanism and assessment.

No dictionary, specialized count, lemma or mathematical script was
produced this turn. Outcome EXPLORATION supplies actionable source
coverage, not mathematical progress beyond the sources checked.
Mathematical exploration usage remains 1/3. The newly covered
continuation receives separate approval next turn. PROOF.md and DAG.md
are unchanged because the assembled argument did not change.

## Search record and Mathlib

Queries included `Reed Solomon rational received words prescribed ending
coefficients subset product inverse moments`; `finite field subset sum
product two prescribed`; `prescribed leading and ending coefficients
linear factors`; `Reed-Solomon x^3 rational`; `polynomials prescribed
ending coefficients roots`; and `Asymptotic distribution zeros equivalence
class Gao polynomials`. Sum-product expansion search results are not
counting inputs. The primary passages above, not snippets, support the
comparison. No novelty conclusion follows from this bounded search.

Full order-three rational-center list result and supporting Mathlib
coverage: **not checked**. The pinned ArkLib definitions in foundations/02
are model inputs, not a proof of the proposed list bound.
