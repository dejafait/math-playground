# Restricted Ramanujan positive-inverse obstruction — audit coverage

TARGET: Independently audit C034q's normalized inverse multiplier, gamma recurrence factors, t=1 bound and two-point positive-measure contradiction, retaining its restricted scope.
CHECKED: 2026-11-21
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse assessment2075 and discovery2075's completed exact multiplier/Fourier-positivity comparisons; the mathematical target and hypotheses of C034q are unchanged. No repeated discovery search is needed for verification of this fixed application.
SOURCE_EVIDENCE: Assessment2075 records Dixit2011 Theorem1.1/(1.6), manuscript pp1-2; NIST DLMF5.5.1/5.6.6; Fasshauer Chapter2 Theorem2.2.1 and full forward proof pp10-11. Review2077 additionally inspected DLMF5.2(i), Euler integral domain, Gamma poles and nonvanishing. Exact citations below.
COMPARISON: This is an audit of a written specialization of known Gamma and Fourier-positivity tools, not a new inverse theorem, coefficient calculation or frequency test. Existing source coverage is adequate for every input in the canonical proof.
GAP: Independent verification of the source variable, normalization direction, recurrence arithmetic, modulus-bound domain and restricted conclusion remains to be performed. This assessment supplies no audit verdict or actual-Xi sign.
REASON: C034q is the recent unaudited restricted stop and can be checked independently of the parked coefficient route. A successful audit consolidates obstruction evidence without repeating the source search or pretending to close L030-L032/C032a.
SCOPE: Only the complete C034q proof and its essential standard inputs; no new frequencies, asymptotic strengthening, second coefficient, signed inverse, actual-data-only inverse, numerical script or all-degree transfer. This newly written ready assessment needs separate supervisor approval before research invocation.

The canonical proof is
`lemmas/C034q-ramanujan-positive-convolution-inverse-obstruction.md`.
The main gap L030-L032/C032a is relevance context, not a premise.
C034q has no direct local mathematical lemma inputs; do not add
those context IDs as DAG edges.

Reuse `2026-11-21-ramanujan-positive-deconvolution-test-2075.md` for:

- Atul Dixit, *Transformation formulas associated with integrals
  involving the Riemann Xi-function*, Monatsh.Math.164(2)(2011),133-156,
  [Theorem1.1/(1.6), author pp1-2](https://adixit.people.iitgn.ac.in/wp/wp-content/uploads/2025/11/transformation_formulas.pdf).
  Its t is the source integration variable; Xi has argument t/2.
  The global constant cancels on normalization. The retained weight
  includes the denominator1+t^2 and exactly two conjugate gamma factors.
- [NIST DLMF5.5.1](https://dlmf.nist.gov/5.5.E1), Gamma recurrence,
  and [DLMF5.6.6](https://dlmf.nist.gov/5.6.E6), the modulus inequality
  at positive real part. The recurrence is essential to reaching
  that domain. No Euler integral at negative real part is licensed.
- Gregory Fasshauer, [Chapter2, Theorem2.2.1, pp10-11](https://www.math.iit.edu/~fass/603_ch2.pdf),
  full measure-to-positive-definite proof previously read. Only that
  direction is needed, with the stated Fourier convention after
  absorbing its scalar normalization.

Additionally [NIST DLMF5.2(i)](https://dlmf.nist.gov/5.2#i), inspected
in2077, states that Gamma is meromorphic, has no zeros, and has simple
poles at the nonpositive integers. Euler's integral(5.2.1) assumes
positive real part. These facts cover the domain and positivity checks;
no changed hypothesis or new literature search is necessary.

The bounded audit must independently check every step in C034q, the
actual claimed lower bound v(1)>=4 against the necessary upper bound1,
and the determinant bound<=-15. These are the canonical claims to
verify, not verified results of this source assessment. Confirm that
convolution by a finite positive Borel measure is the exact contract;
failure of that contract does not exclude another operation. An error
requires a precise local correction and reassessment of the conclusion.
If the proof checks, report reproduction/audit of known mathematics,
with no implication of an RH sign or new mathematical discovery.

No new general theorem or parameter expansion is proposed. No
cross-notebook input. Full matching Mathlib coverage remains unchecked;
the audit need not browse it without a concrete verification benefit.
The supplied goal's proof_audit/routine_audit route applies: this is
ordinary arithmetic, domain and normalization checking, without a
delicate analytic interchange or candidate resolution to review.
