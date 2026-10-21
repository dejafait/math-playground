# Proposed phase-sensitive proper-subgroup fiber review

TARGET: Review phase-sensitive Hayes-character estimates for L099's 67-subset fibers on H as a route to a single-center list strictly exceeding 65537^28/2^128.
CHECKED: 2026-10-20
DECISION: EXPLORE
SEARCH_EVIDENCE: Searched Hayes characters with prescribed coefficients and multiplicative-subgroup subsets; prescribed subset sums/products; and distinct-coordinate character sieves. Compared Gao v5 Section 4 with Li-Wan 1806.00152v3 Section 4 and 1507.06329v1 Sections 2-3; exact queries and inspected cases are recorded below.
SOURCE_EVIDENCE: Read Gao 2203.06729v5 Proposition 3 and proof (26)-(28), Theorem 2 hypotheses; Li-Wan 1806.00152v3 Lemma 4.1 and complete proof (4.1), including arbitrary monic moduli and the even-character branch; Li-Wan 1507.06329v1 Theorem 2.1, Corollary 2.2, cycle generating function in Lemma 2.6 proof, and Lemma 3.1 factorization.
COMPARISON: Exact orthogonality retains coefficient phases, but the inspected quantitative arguments take absolute values and do not certify a phase-aligned large fiber on H. A separately scoped quotient-ring/subgroup upper-certificate test has source coverage; no fiber bound is established here.
GAP: No applicable phase-sensitive finite lower estimate was located in the inspected sources. Park the large-fiber phase proposal pending a specific new estimate; propose a uniform family upper-certificate test, with subgroup restriction and exceptional constant-term characters still to be verified.
REASON: The changed phase mechanism required source comparison; this bounded review distinguishes an exact identity from a lower estimate and supplies a different falsifiable family test without claiming a mathematical advance.
SCOPE: E=F_65537, H of order 1024, F=F_(65537^28), L099's existing 67-subset residue labels (a,b,c) in E² times H, degree<64 and every m>=1; source review only, with no new lemma, script, maximum search or fiber estimate authorized here.

## Original proposal (preserved; disposition below)

The main gap remains arbitrary-center safety at 67/68 agreements, with
955<=t_star(m)<=957. L099's audited dictionary would turn any one fiber
strictly larger than the ambient threshold into an unsafe index 957.
The proposed mechanism must distinguish coefficient classes through
their character phases. Repeating a uniform average or renaming an
old absolute-norm allowance is not a new test. No phase alignment or
large fiber is presently asserted.

The next turn is literature-only. Reuse the exact-class framework and
recorded exclusions; assess finite proper-subgroup character-counting
results with their actual constants and hypotheses. Approve a later
mathematical test only if the source comparison identifies a concrete
phase-sensitive expression or estimate and its exact unresolved step
toward a strict >65537^28/2^128 witness. If only the already insufficient
average, full-domain asymptotics, or the old absolute-norm failures remain,
record that obstruction and select a different independently testable gap.
Do not infer novelty from a failed search or assume the quantitative
estimate merely because an exact character identity exists.

Essential local inputs: L001, C012a and L099, foundations/01–02,
the order-three-pole assessments, and ATTEMPTS/083. L015–L018 and
ATTEMPTS/007–008 are contrasts for failed residual/absolute estimates,
not premises or permission to restart them. Exact source leads for
phase-dependent bounds remain unassessed. Maximum fibers, source-model
comparison with ABF and independent 68-agreement safety remain open.
No cross-notebook input is proposed. Mathlib coverage for this changed
quantitative target is not checked. This file proposes work only and
does not approve mathematics; its target receives separate assessment.

## Completed source review, 2026-10-20

This was one literature-only comparison. No new mathematical formula,
fiber estimate, lemma or program was derived. Outcome EXPLORATION;
classification NOVELTY_UNCHECKED. A failed bounded search is not evidence
of novelty or nonexistence of a stronger theorem. The original proposal
above is retained as motivation, not a current authorization.

Queries included `Hayes characters prescribed coefficients subset
multiplicative subgroup character sum Gao 2203.06729`, `subset prescribed
first coefficients product multiplicative subgroup finite field character
sums`, `"prescribed" "sum and product" "subsets" finite fields`,
`"subset" "Hayes characters" polynomial`, and `Li Wan distinct coordinate
sieve character sum prescribed coefficients multiplicative subgroup`.
Search snippets were discovery leads only. The mathematical comparison
uses these primary texts:

- Gao, *Asymptotic distributions of the number of zeros of random
  polynomials in Hayes equivalence class over a finite field*,
  [arXiv:2203.06729v5](https://arxiv.org/html/2203.06729v5), 2024-01-07,
  Section 4 Proposition 3, (25)-(28), and Theorem 2. Equation (26)
  retains the class-character factor; (28) instead bounds the absolute
  distinct-root character sum. The proof explicitly uses the full
  complement domain when replacing restricted root sums by complete
  sums. Its character-power argument invokes the leading-coefficient
  p-group, not arbitrary trailing-only unit characters. Thus neither
  the theorem nor its quantitative proof can be imported wholesale for
  ell=0 and D=H. The earlier arbitrary-domain dictionary coverage is
  reused, not reproved. An exact phase factor supplies no positive
  lower estimate on the whole nonprincipal contribution.
- Li and Wan, *Distance Distribution in Reed-Solomon Codes*,
  [arXiv:1806.00152v3](https://arxiv.org/html/1806.00152v3#S4), 2019-07-30,
  Section 4 Lemma 4.1, printed pp. 9-10. For any monic modulus of
  positive degree d and a nontrivial character of its unit group,
  extended by zero off the units, its degree-j monic character sum
  has absolute value at most binomial(d-1,j) q^(j/2).
  The proof uses its Dirichlet L-polynomial, including imprimitive
  characters; squarefreeness of the modulus is not assumed. The
  additional even-character conclusion requires triviality on field
  units and concerns a cumulative monic sum. These are complete-domain
  upper estimates, not a proper-subgroup phase-sensitive lower theorem.
  Modulus X^3 is within the statement, but restriction to H requires
  a separate applicability argument. Theorem 5.1 still uses full-field
  roots and is not imported.
- Li and Wan, *Counting polynomial subset sums*,
  [arXiv:1507.06329v1](https://arxiv.org/html/1507.06329v1#S2), 2015-07-22,
  Theorem 2.1 and Corollary 2.2 (printed p. 5) apply to arbitrary finite
  domains and complex weights; symmetry permits conjugacy-class
  grouping. Lemma 3.1 (pp. 8-9) displays the target-character phase
  before the cycle products. Its additive-ring statement is not itself
  a theorem about multiplicative residue constraints; the general
  weighted theorem is the appropriate input for those constraints.
  The Lemma 2.6 proof gives the exponential generating function for
  cycle weights. Import the sieve and its normalization, rather than
  reproving it. No source theorem here forces favorable phase alignment.

The degree-d bound and the arbitrary-domain sieve suggest a different,
independently testable question: can a uniform upper certificate rule
out every L099 fiber as a threshold-sized witness? It needs character
extension to the full unit group, restriction to H through the constant
term, and a separate treatment of characters factoring through that
constant term. Taking powers in cycles can trivialize some such
characters. None of those checks, nor their numerical consequence, is
proved in this literature turn. They are the explicit future test.

## Duplicates, blockers and route decision

L099 and ATTEMPTS/083 cover the exact dictionary and insufficient
average; neither covers a uniform fiber upper bound. ATTEMPTS/007-008
concern a degree-67 polynomial center at 66 agreements, a residual
factor and signed collision energy. The new proposed upper test concerns
67-root products with no residual factor and quotient-ring characters;
it does not retune those norms or restart their stopped elimination.
No cross-notebook input is used. The full Mathlib result and supporting
character/sieve coverage are not checked; unknown coverage is not absence.

Author-hosted h-version.pdf and sieve.pdf returned web-reader 502; the
PMC moment-paper page returned a browser challenge. Those accesses are
not inspected theorem evidence. Versioned arXiv primary texts above
suffice for the proposed general tools, so there is no essential source
blocker for their bounded specialization. Broader mixed-character-sum
search hits were not needed and are not imported. No blocked source was
used to justify a conclusion. The old ABF-model qualification persists.

Park the phase-dependent large-fiber search: the inspected sources do
not supply its decisive estimate. Reopen only with a specific effective
phase-sensitive lead. The separate proposed assessment is
[uniform fiber upper certificate](2026-10-20-order-three-pole-uniform-fiber-upper.md).
Its newly written ready continuation must receive separate approval.
This review changes no mathematical argument: PROOF.md and DAG.md stay
unchanged, the bracket stays 955–957, and mathematical exploration usage
stays 0/3. A future passing family upper bound would stop this witness
family only; it would not establish arbitrary-center 67/68 safety.
