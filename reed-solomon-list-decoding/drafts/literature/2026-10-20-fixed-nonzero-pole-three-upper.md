# Fixed nonzero-pole dictionary and upper-test assessment

TARGET: Test the entire 67-agreement dictionary and one uniform upper certificate for Y(x)=(((x-3)^67+a(x-3)^2+b(x-3)+c)/(x-3)^3,0,...,0), with a,b in F_65537 and c nonzero, against T=65537^28/2^128.
CHECKED: 2026-10-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Completed bounded searches for rational-center RS lists, prescribed-coefficient subgroup fibers, Hayes classes and subset products; inspected the primary statements below and checked local L099–L101, pole assessments, ATTEMPTS/083–084 and relevant histories for overlap. No matching finite cap was located; search failure is not a novelty claim.
SOURCE_EVIDENCE: Gao 2203.06729v5 definitions (1)–(2), (5)–(6), Proposition 2 (15)–(16), Theorem 3 (17)–(19), and Theorem 2/Section 4 domain restriction; Li–Wan 1806.00152v3 Section 4 Lemma 4.1 with its complete proof; Li–Wan 1507.06329v1 Theorem 2.1, Corollary 2.2 and the general cycle generating identity in Lemma 2.6's proof, reopened 2026-10-20.
COMPARISON: Gao supplies exact identities for arbitrary monic moduli and arbitrary domains avoiding their zeros, but its quantitative full-complement theorem does not apply here. Li–Wan supplies arbitrary-modulus nonprincipal character estimates and an arbitrary-domain weighted sieve; these cover one upper-test mechanism, not the translated RS dictionary, class occupancy or a passing finite cap.
GAP: Prove the entire translated-pole RS dictionary; choose and count a valid Fourier class group; verify each cycle power, joint-modulus twist and excluded evaluation; then evaluate one uniform upper certificate exactly against T. No specialized character bound, cancellation, cap or threshold outcome is established in this review.
REASON: Essential general-source coverage is now adequate for this changed-pole specialization, including a conservative arbitrary-modulus treatment of twists; its remaining elementary applicability and finite-arithmetic obligations belong to a separate mathematical turn.
SCOPE: Q=65537, E=F_Q, H=<19139> of order 1024, F=F_(Q^28), degree<64, all m>=1, closed simultaneous agreement; only the displayed family with a,b in E and c in E^*. No variable pole search, new character theorem, exact maximum, or arbitrary-center claim.
LITERATURE_REASON: The nonzero pole changes the modulus/domain relationship and removes the previously assessed constant-H setup; the old ready target does not cover these essential hypotheses.

The source review is complete. This newly ready SPECIALIZE assessment
requires the supervisor's separate continuation approval before invocation;
no mathematical attempt was made in this literature-only turn. No new
dictionary, bound, character case, arithmetic comparison or admissibility
proof for this family has been derived here.
In particular, do not carry over K, its character counts, or the
constant-character cancellation from L100 without justification.

The main gap is arbitrary-center safety at 67 or 68 agreements, with
the fixed-instance bracket 955–957. The intermediate target is one
complete family dictionary and one rigorously normalized upper test.
A passing cap would exclude another possible witness family; an
insufficient cap would identify the quantitative limitation of this
one test, without proving a large list. These are plausible local uses,
not an asserted route to the full boundary.

Essential local inputs for assessment are C012a's field/domain and
primitive generator, foundations/01–02's list convention, and L099–L100
as comparisons of the dictionary and character method. L101 and
ATTEMPTS/084 are contrasts to prevent restarting the fourth-order
absolute-sieve test; ATTEMPTS/083 preserves the old averaging shortfall.
No cross-notebook input is proposed.

The initial source-review plan (now completed) was to check whether known
equivalences, exact formulas, or a stronger theorem settle the displayed
target, and to inspect changed hypotheses before any specialization.
The original source leads, now inspected, are Li–Wan,
[*Distance Distribution in Reed-Solomon Codes*, 1806.00152v3,
Section 4 Lemma 4.1](https://arxiv.org/html/1806.00152v3#S4), and
[*Counting polynomial subset sums*, 1507.06329v1, Section 2
Theorem 2.1 and Corollary 2.2](https://arxiv.org/html/1507.06329v1#S2).
Their general statements cover the proposed tools; their application to
every new cycle and twist remains a mathematical verification obligation,
not an established specialized result or evidence of novelty.

Continuation test for the source review: approve only a precise
dictionary and one upper test whose every imported character estimate
and exceptional case has adequate coverage, or import a matching known
result directly. If an essential case remains uncovered, identify it
and keep dependent mathematics unapproved. Do not replace missing
coverage with a new character lemma in the review turn.

For a later separately approved mathematical attempt, compare the one
valid cap with T by exact arithmetic. Retain a family exclusion only
if the entire-list argument and uniform bound pass the required
threshold; otherwise park that estimate without inferring unsafety.
Whether all labels occur, whether any fiber is large, and how this
family relates to arbitrary centers remain unresolved. The ABF-model
comparison also remains open. Full or supporting Mathlib coverage for
this changed target has not been checked; no absence is inferred.

## Completed source comparison: step 379

One literature-only turn; outcome EXPLORATION, classification
NOVELTY_UNCHECKED. This fills source coverage for a bounded test, without
claiming a new mathematical input, a finite bound or originality.

The local duplicate/failure check reused the supplied overview and DAG,
read L099's full dictionary and L100's character construction, C012a's
field/generator proof, the pinned list definition, the ready zero-pole
upper assessment and phase review, ATTEMPTS/083–084 and history/378.
Targeted searches of the pole assessments, working notes and histories
365,370,372,373,375,377–378 located only the proposed fixed-pole target.
L099's averaging shortfall and L101's insufficient fourth-order estimate
remain method comparisons. L100 is already audited; its pending-audit
wording in PROOF.md does not schedule another audit.

External queries included `"Reed Solomon" "rational" "pole"
"multiplicative subgroup" list decoding character`, `"Reed-Solomon"
"rational" "subset" "Hayes"`, `"Reed-Solomon" "translated"
"subgroup" deep holes rational`, `"subset" "rational functions"
"finite fields" Wan`, `"prescribed" "coefficients" "multiplicative
subgroup" polynomials Hayes`, and `"subset products" "finite fields"
character sums`. Search results were used for discovery only. No located
result was verified to give the displayed finite family bound. General
rational-interpolation and energy-decomposition leads were not inspected
as theorem inputs; they supply no coverage here. This was a bounded
search, not a claim to exhaust the literature.

### Inspected primary inputs

1. Gao, *Asymptotic distributions of the number of zeros of random
   polynomials in Hayes equivalence class over a finite field*,
   [arXiv:2203.06729v5](https://arxiv.org/html/2203.06729v5),
   2024-01-07. Definitions (1)–(2) allow a monic modulus of arbitrary
   shape; the domain must avoid its zeros. Equations (5)–(6) describe
   the class group and class sizes. Proposition 2 (15)–(16) and
   Theorem 3 (17)–(19), including the coefficient-extraction proof,
   give exact arbitrary-domain subset/residual identities. For the
   proposed application, the parameters to verify are source modulus
   (X-3)^3, t=3, ell=0, k=64, D=H and j=67. The source residual degree
   is zero. This does not by itself prove the entire ambient-field
   interleaved RS dictionary. Theorem 2 requires ell>=1 and the full
   complement of the modulus's zeros; Section 4 explicitly fixes that
   domain in (21). Its asymptotic estimate is not a finite subgroup cap.
2. Li and Wan, *Distance Distribution to Received Words in Reed-Solomon
   Codes*, [arXiv:1806.00152v3, Section 4](https://arxiv.org/html/1806.00152v3#S4),
   2019-07-30, Lemma 4.1, printed pp. 9–10. For a monic modulus f of
   degree d>0 and a nonprincipal character of (E[X]/f)^*, extended by
   zero on nonunits, the degree-j monic sum is bounded by
   binomial(d-1,j)|E|^(j/2). No squarefree or primitive-character
   hypothesis appears. The complete proof truncates the L-polynomial
   by character orthogonality, bounds its inverse roots by sqrt(|E|),
   and bounds its coefficients. Its separate cumulative bound requires
   triviality on E^*; it is unnecessary for the proposed test. This
   arbitrary-modulus statement covers a joint modulus after its
   character and nonprincipality hypotheses are verified. It does not
   estimate a principal character by the nonprincipal formula.
3. Li and Wan, *Counting polynomial subset sums*,
   [arXiv:1507.06329v1, Section 2](https://arxiv.org/html/1507.06329v1#S2),
   2015-07-22, Theorem 2.1 and Corollary 2.2, printed p. 5. The former
   is the signed distinct-coordinate identity for any complex weight
   on a subset of a finite Cartesian power; the latter groups
   permutation classes when domain and weight are symmetric. The
   general cycle exponential generating identity at the start of
   Lemma 2.6's proof was inspected. Use these identities directly,
   retaining 67!; the lemma's specialized gcd-based bound is not an
   automatic bound for a different principal-power schedule. This
   imports the sieve without reproving it or invoking the paper's
   additive polynomial-sum theorems for a multiplicative residue group.

### Exact scope of the later specialization

The named Chinese remainder theorem for coprime polynomial ideals and
finite abelian character orthogonality are standard algebraic inputs.
L100 already gives the latter construction and an index-64 subgroup
indicator. The following are obligations for the mathematical attempt,
not new results proved in this assessment:

- Verify 3 is outside H using C012a's order certificate before defining
  the center. Prove divisibility at the pole, monic leading cancellation,
  strict degree, exact agreement, injectivity and the entire converse
  over F, including zero other rows for every m. A translated root
  product must use its coefficients at 3 with correct signs. No label
  surjectivity, smaller container or extra extension-field rows may be
  presumed.
- Use the full unit group modulo (X-3)^3 as a permissible starting
  Fourier group. Count it and all character types explicitly. Any
  smaller group needs a new justification within the same attempt;
  the old constant-H container is not an input for this target.
- Assess the subgroup indicator in the original X coordinate. The
  proposed way to fit its twists into the inspected general theorem is
  the joint modulus X(X-3)^3, using the Chinese remainder theorem.
  Verify the actual product character, the evaluation at X-x, the
  constant/minus signs and the 1/64 factor. Account individually for
  x=0 and x=3 when passing to complete monic linear sums. A character
  extended by zero remains zero on a nonunit even at a principal power.
  Alternatively use separate lower-conductor sums only with their
  omitted-point corrections justified. No sharper conductor estimate
  is needed to make the general joint-modulus test well defined.
- Inspect every j=1,...,67 and every subgroup-indicator twist. Establish
  nonprincipality before using Lemma 4.1; handle principal powers with
  their exact domain contribution. In particular, retain all
  constant-term-only characters and possible principal powers rather
  than import L100's vanishing 67-subset sum. If using logarithmic
  coordinates for the nilpotent unit part, justify the coordinate
  isomorphism and power behavior in characteristic 65537.
- Apply the weighted sieve to the actual symmetric product weight.
  Keep all exceptional cycles, their character multiplicities, the
  Fourier denominator and unordered normalization. Produce one uniform
  upper certificate; compare it with T by exact integer arithmetic.
  This scope does not authorize a sweep of poles, a new character-sum
  theorem, phase lower estimates or repeated retuning of a failed cap.

These obligations are applications of the inspected arbitrary-modulus
and arbitrary-domain results, not an essential unread theorem. No
matching finite family result was found to import instead; the RS
interpretation and finite threshold comparison therefore require a
specialization. No character-bound, sieve or class-identity reproof is
justified. If the attempted translation cannot be justified from these
inputs, preserve the exact failure and return to assessment rather than
assert an uncovered estimate.

Retain a family exclusion only when its entire-list proof and valid
integer upper bound meet the threshold. An upper allowance above T
parks that estimate without establishing a large fiber; do not restart
the old fourth-order estimate. Independent gaps remain arbitrary-center
67/68 safety, the 955–957 boundary and the ABF-model comparison. Mathlib
coverage for the full specialization and supporting imported theorems is
not checked. No cross-notebook mathematical input is used.
