# Prescribed finite PF order — bounded degree-five test

TARGET: Test a degree-five rational-quadratic deformation of L837 for every prescribed PF_m order, eventual shift3 positivity and infinitely many negative shift4 minors.
CHECKED: 2026-11-06
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Completed exact/stronger-result and local-overlap comparison is recorded in 2026-11-06-prescribed-finite-pf-adjacency-scope.md; no matching full rational family was identified. The known-method inputs cover the proposed distinct-root test; no originality claim is made.
SOURCE_EVIDENCE: Alexandersson https://arxiv.org/html/1208.5607v1 Theorem6 p.5/Section3.2 pp.11–12; Katkova https://arxiv.org/pdf/math/0505174v1 Definition2 p.4/TheoremB p.5; Bell–Gerhold https://fam.tuwien.ac.at/~sgerhold/pub_files/papers/2007_osc_rec.pdf DOI10.1007/s11856-006-0015-1 Theorem2 p.335/Section3 pp.339–341. Exact hypotheses, inspected cases, primary links and qualifications are in the completed scope assessment.
COMPARISON: Known sector sufficiency supplies an all-ordered-minors PF_m test, Widom supplies the exact fixed-band expansion, and Bell–Gerhold supplies negative-density signs under its actual dominant-root hypotheses. Rational parameters, both ray applications and the positive-ray bound remain specialization obligations.
GAP: For every prescribed integer m>=2, choose a rational quadratic in the single degree-five deformation class and verify positive coefficients, PF_m, distinctness, eventual positive shift3 and infinitely negative shift4. No such choice or verification has been performed here.
REASON: This strengthens audited L837's PF2 limitation without repeating its audit or assuming a signed Xi bridge. Missing parameter and sign verifications are mathematical work under ready methods, not a reason for repeated general literature review. This newly written continuation requires separate supervisor approval next turn.
SCOPE: Only the ordinary-coefficient, zero-extended rational degree-five class retaining L837's three real linear factors and varying its real quadratic. The intended quantifier is one polynomial for each prescribed m>=2, not one polynomial for all m. Shifts remain3/4; parameters and onset R may depend on m.

Main gap: actual-Xi all-degree mixed positivity L030–L032/C032a.
The downstream use is to decide whether an arbitrarily large prescribed
finite-PF band repairs the abstract adjacent-ray inference refuted at
PF2. Actual-Xi realization, all-degree signs and effective overlap
remain unresolved even upon success.

Essential local input is audited L837 and the preserved stop
`ATTEMPTS/2026-11-06-pf2-adjacent-ray-propagation-stop.md`.
The complete method comparison and source evidence are in
`2026-11-06-prescribed-finite-pf-adjacency-scope.md`; reuse them.
L772 is a nonmatching contrast, not a premise. C832a/L834 motivate
the question only. No cross-notebook input or new mathematical
script is needed to obtain source coverage. Mathlib matching coverage
has not been checked.

One bounded test is nominated by this assessment once separately
approved: choose parameters within the stated deformation class,
then check the following mathematical obligations as one coherent
specialization. No coefficient choice or parameter interval is
asserted by this nomination.

- Check normalization, rationality and positivity of every coefficient;
  exclude repeated roots and verify the precise sector for each m.
- Use Theorem6 with the source's shift/rank convention. Retain every
  maximal-modulus term, verify its coefficient and provide a complete
  smaller-term bound giving a finite positive shift3 onset R(m).
- For shift4, combine equal bases, delete only coefficients proved zero,
  verify a real nonzero constant-coefficient recurrence and show its
  actual maximal-modulus characteristic roots contain no positive real
  root before importing Bell–Gerhold Theorem2. An arbitrary annihilating
  polynomial with extraneous roots is not sufficient evidence.

Import the cited theorems; do not reprove the sector criterion, Widom's
formula or general recurrence oscillation. The intended contribution
is a known-method specialization, classified REPRODUCTION. Bell–Gerhold
does not require roots of unity or an irrational-phase proof, and does
not provide an effective negative onset. Do not transfer L837's period6
to the deformation without proof. A finite determinant sample alone
cannot establish either required infinite-rank statement.

Continue upon a complete all-m certificate in this single ansatz, or
record an informative obstruction. Stop this ansatz if rationality,
sector membership, distinctness, strict positive dominance or the
negative-ray theorem hypotheses fail without a specified repair.
Do not replace the all-m statement by PF2 or a list of finite m values.
Do not require uniformity in m or in a coalescing-root limit: the exact
question permits R and P to depend on m. Preserve unfinished reasoning
and require a refined mechanism before repeating a failed test.

This is routine known-method development, not a central creative Xi
mechanism. Supervisor approval of the new ready assessment is a
separate next-turn gate; no mathematical construction occurred in the
literature turn that wrote it.

### Direct-source recovery check, 6 November 2026

The three direct URLs in SOURCE_EVIDENCE resolved in this recovery turn.
The retrieved Alexandersson v1 Theorem6 states the distinct-variable
formula for every positive rank; Katkova v1 TheoremB states the open-sector
sufficient condition with f(0)>0; Bell–Gerhold Theorem2 requires a nonzero
real recurrence with no positive dominating characteristic root. Its
Section3 separates irrational, rational and mixed frequencies. These
checks agree with the existing scope assessment, whose detailed proof-case
review is reused rather than repeated. No theorem comparison changed,
no new search-based novelty claim was made, and no parameter or sign
specialization was performed. The literal URLs repair the reported
ready-assessment defect; SPECIALIZE and the exact TARGET remain unchanged.
The mathematical obligations and Mathlib-unchecked qualification above
remain in force.
