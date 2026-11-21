# Inverse theta averaging: one exact quadratic test

TARGET: Test B_3 on f(x)=(1-x)^2 using L019/L021/L795: verify the finite inverse identity and exact positive sign-change counts, and reject the universal inverse premise if the count increases.
CHECKED: 2026-11-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse step615's completed inverse-averaging review, its finite-multiplier/positivity-preserver searches and scoped duplicate checks; no new search or novelty claim is needed for this single quadratic specialization.
SOURCE_EVIDENCE: Guterman–Shapiro https://staff.math.su.se/shapiro/Articles/FinalPosit.pdf Lemma3.2 pp7–8, full i=1 proof, Definition1.1 p1 and Proposition3.10 p10; Branden https://arxiv.org/pdf/math/0403364v2 (29 September2004), definition and Theorem3.14 p8; primary passages rechecked 2026-11-05. Reuse step615 and step502; use the named Cauchy–Schwarz inequality with its linear-dependence equality case and the quadratic formula.
COMPARISON: Known quadratic positivity machinery covers the diagnostic; the remaining work is only its actual-law specialization and the half-line sign analysis. Finite real-rootedness preservation is not the proposed variation-diminution premise, and no infinite multiplier or moment characterization is required.
GAP: Verify all finite monomial identities, actual-law nondegeneracy for strict Cauchy–Schwarz, the image's degree and endpoint signs, locations/multiplicities of any roots and the resulting positive-half-line crossing counts; none has been computed by step615.
REASON: One exact low-degree necessary test can decisively park the universal inverse mechanism without a cubic search, numerical moments or an RH-equivalent input. Any negative result concerns this premise alone, not RH or restricted inverse constructions.
LITERATURE_REASON: Supervisor recovery identified missing direct source URLs in this ready assessment; this turn verifies and inserts those URLs without repeating discovery or performing the saved calculation.
SCOPE: Actual untruncated L795 law; real polynomials of degree at most three for the inverse identity, then only f(x)=(1-x)^2 for oscillation. Known-method reproduction/specialization; no new general preserver theorem or creative central bridge. Newly saved readiness is subject to separate next-turn supervisor approval.

## Hypotheses and retained obligations

Use exactly L019's K and L021's finite positive moments, with the L795
normalization m_j=M_(2j), dmu=K(u)du/m_0. Proposed operators are
A_3 f(x)=integral f(u^2 x)dmu(u) and B_3(x^j)=(m_0/m_j)x^j for
0<=j<=3. Verify rather than assume their inverse relation, using only
finite polynomial sums and the stated moments. The positive full
support of the actual law must justify strictness if used; retain
the equality case, not merely L021's nonstrict inequality.

The count v_+(g) is the supremum of alternations of nonzero values
g(x_1),...,g(x_r) with 0<x_1<...<x_r<infinity. For a nonzero real
polynomial it counts precisely the interior zeros of odd multiplicity.
The future proof must justify that interpretation where used. Even
roots and endpoint zeros do not count; define v_+(0)=0 if needed.
Check that a nonzero input has nonzero image before using its signs.

## Bounded reproduction and acceptance test

Use only the fixed square above. Compute its image from the operator
definition, use the named inequality/equality case on the actual law,
and determine the discriminant, root locations, multiplicities and
crossings exactly. No numerical certificate or script is necessary.
State how the real-line positivity diagnostic in the source is being
specialized to this positive-half-line test; do not import the changed
domain without justification. The source's quadratic argument is
being specialized because that domain and the actual theta law were
not its stated application, not because it needs a new proof.

If v_+(B_3 f)>v_+(f), reject the universal inverse variation-diminution
premise and stop this test. If no increase is proved, record precisely
the inconclusive or contrary result; do not infer all-cubic validity
or expand the calculation. The proposition asks for every nonzero
real polynomial, so even-multiplicity inputs cannot be silently
excluded. A restricted alternative would be a different target
requiring its own source assessment.

Main gap: actual-Xi all-degree mixed positivity. The intermediate
premise could only support lower oscillation after a valid reference
application. All-degree extension, reference geometry and mixed-sign
transfer remain open. L821, L795's common-interlacing obstruction,
step502 and step565 are context/contrasts; L821 is not a mathematical
input to this test. No cross-notebook result is used. Matching full
Mathlib coverage is unchecked. If a canonical result is written next
turn, include its hypotheses, full finite specialization, qualifications,
precise source citation and Mathlib status; claim no beyond-source
mathematical discovery.

## Direct-source recovery check — step616

The unversioned [Guterman–Shapiro author manuscript](https://staff.math.su.se/shapiro/Articles/FinalPosit.pdf)
was accessible on 2026-11-05. Rechecked Definition1.1 (p1), Lemma3.2
and its complete i=1 discriminant argument (pp7–8), and Proposition3.10
with its counterexamples (p10). The necessary diagonal condition is
lambda_1^2<=lambda_0 lambda_2 for positivity preservation when degree
two is available. Positivity here means strictly positive at every real
argument. This is source evidence, not a theorem about B_3 on (0,infinity).
Its square input and half-line crossing interpretation still require the
specialization already specified above. No source conclusion is applied
to the theta moments in this recovery turn.

Rechecked the definition immediately before Theorem3.14 and that theorem
in [Branden v2](https://arxiv.org/pdf/math/0403364v2), printed p8.
It characterizes degree-at-most-n real-rootedness preservation through
the image of (1+x)^n having real zeros of one sign. It supplies no
crossing-count conclusion for arbitrary input polynomials. The source
versions and scope agree with step615; no changed hypothesis or new
mathematical evidence was found. Earlier duplicate/failure comparisons
are reused, not repeated. This repair leaves DECISION: SPECIALIZE and
the exact TARGET unchanged. Full Mathlib coverage remains unchecked.
