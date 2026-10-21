# Proposed uniform upper-certificate specialization

TARGET: Test a uniform upper certificate for all of L099's 67-subset fibers using quotient-ring character bounds and the weighted distinct-coordinate sieve against 65537^28/2^128.
CHECKED: 2026-10-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the phase-sensitive review's completed bounded searches and exact theorem comparison; the new test uses the inspected arbitrary-modulus character bound and arbitrary-domain weighted sieve, not an unassessed phase lower theorem.
SOURCE_EVIDENCE: Li-Wan arXiv:1806.00152v3 Section 4 Lemma 4.1 with complete proof; Li-Wan arXiv:1507.06329v1 Theorem 2.1, Corollary 2.2, Lemma 2.6 cycle generating function and Lemma 3.1 factorization; Gao arXiv:2203.06729v5 Proposition 3 proof (26)-(28) as a scope comparison only.
COMPARISON: Known complete-domain character bounds and weighted distinct-coordinate identities cover the tools; no inspected theorem states the uniform proper-subgroup trailing-coefficient fiber cap. Only the restriction, exceptional characters, normalization and exact finite threshold specialization remain for the proposed test.
GAP: Verify character extension and subgroup restriction, distinguish principal and constant-term-only characters from other unit characters under every cycle power, and compute one valid uniform upper certificate with all multiplicities and 67! normalization retained. No passing cap is assumed.
REASON: This is an independently testable upper diagnostic for the audited 67-root dictionary after the phase-sensitive lower-source search found no adequate estimate; it uses no residual-energy norm retuning.
SCOPE: E=F_65537, H of order 1024, modulus X^3, L099's fibers with labels in E² times H, ambient F=F_(65537^28), degree<64, every m>=1; one uniform upper-certificate applicability and arithmetic test only. Excludes a phase-dependent lower bound, exact maximization, other poles, new character estimates and arbitrary-center safety.
COVERED_TARGET: Test a uniform upper certificate for all of L099's 67-subset fibers using quotient-ring character bounds and the weighted distinct-coordinate sieve against 65537^28/2^128.
LITERATURE_REASON: The phase-sensitive review identified a different finite quotient-ring upper test, outside the old averaging and residual-factor assessments; this assessment records its inspected tools for separate approval before any mathematical invocation.

## Approval status and precise sources

This is a newly written ready assessment. It has not authorized a
mathematical attempt in the current literature-only turn. The supervisor
must separately approve this continuation next turn. It records source
coverage, not a new specialized inequality or its proof.

The [completed comparison](2026-10-20-order-three-pole-phase-sensitive-fibers.md)
records exact queries, versions, inspected hypotheses, failed accesses
and route comparisons. Import these named general results:

1. Li and Wan, *Distance Distribution in Reed-Solomon Codes*,
   [arXiv:1806.00152v3](https://arxiv.org/html/1806.00152v3#S4),
   2019-07-30, Lemma 4.1, printed pp. 9-10. For monic modulus f of
   degree d>0, a nontrivial character of (E[X]/f)^*, extended by zero
   on nonunits, and monic polynomials g of degree j, the absolute sum
   is at most binomial(d-1,j) |E|^(j/2). No squarefree-modulus assumption
   is imposed. The separate cumulative estimate requires the character
   to be trivial on E^*. Use the degree-one estimate only after checking
   nontriviality of each twisted/powered character. Its proof, including
   the zero coefficient branch and imprimitive L-polynomial bound, was
   inspected. No full-field RS list theorem is imported.
2. Li and Wan, *Counting polynomial subset sums*,
   [arXiv:1507.06329v1](https://arxiv.org/html/1507.06329v1#S2),
   2015-07-22, Theorem 2.1 and Corollary 2.2, printed p. 5: the weighted
   distinct-coordinate sieve for arbitrary finite domains, with symmetric
   weights grouped by permutation conjugacy classes. The Lemma 2.6 proof
   supplies its cycle exponential generating function. Lemma 3.1,
   pp. 8-9, is supporting evidence for Fourier phase and cycle
   factorization; its additive-ring conclusion is not directly asserted
   for multiplicative unit residues. Apply the general weighted theorem.

Gao v5 Proposition 3 cannot be substituted for this specialization:
ell>=1 and the full zero-complement domain are its hypotheses. Its
proof's character-power and complete-root-sum steps require fresh checks
here, especially for characters of the constant-term group. Neither
source supplies the subgroup specialization or its threshold outcome by
citation alone. No generating-function or Weil-bound reproof is needed.

## Bounded mathematical continuation

Main gap: arbitrary-center safety at 67 or 68 agreements, with the
955–957 bracket unchanged. Intermediate target: a valid uniform upper
certificate for this one 67-agreement rational-center family. Downstream
use: a below-threshold certificate would park every L099 fiber as an
unsafe-index-957 witness, avoiding an unjustified phase-alignment search;
an inconclusive upper estimate would identify the precise remaining
quantitative gap. It would not imply arbitrary-center safety.

Essential inputs are L001, C012a, audited L099 and foundations/01–02.
Use L099's actual restricted label container rather than assume all
full unit classes are occupied. Any Fourier normalization must specify
its group and retain characters trivial on the restricted subgroup.
Check extension/restriction of finite abelian-group characters and the
index-64 subgroup indicator; a full-field character bound cannot be
applied to a restricted root sum without that step. Verify the behavior
of powers of every character for cycle lengths 1 through 67. Characters
factoring through the constant term can become principal on some cycles;
they require a separate exact treatment, not the generic nontrivial
bound. Verify all unit-group structure used in that treatment. Include
empty fibers, c outside H, the odd constant sign and unordered subsets.

Continuation/abandonment test: construct and compare one rigorously
justified cap to T=65537^28/2^128 by exact arithmetic. If it is <=T for
every admissible label, retain only a family exclusion. If the cap
exceeds T, preserve its actual/required values and park this particular
certificate; that does not prove a large fiber or a lower obstruction
on all better estimates. If a needed character remains uncovered, save
the exact missing hypothesis and return to source review, without
assuming it or broadening into a new character-sum theorem. One bounded
test is authorized after separate approval, not successive norm tuning.

Independent gaps: other centers, arbitrary-center 67/68 safety, exact
boundary and ABF-model comparison. ATTEMPTS/083 and ATTEMPTS/007-008
remain preserved. No cross-notebook use is proposed. Mathlib coverage
for this full specialization and the supporting character/sieve facts
is not checked; the primary citations provide the intended inputs.
