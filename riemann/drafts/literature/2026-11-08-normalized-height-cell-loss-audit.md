# Degree-uniform height-cell loss — approved audit scope

TARGET: Audit L903's weighted-reference stability, recovery of A_0 normalization and degree-uniform parity bound on closed height cells, retaining L902's L309/L037 contracts.
CHECKED: 2026-11-08
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse step129's exact-statement, weighted-normalization, stronger-result and scoped duplicate comparison in 2026-11-08-normalized-shrinking-height-cell-loss.md and its separately saved specialization nomination. Step130 adds the nominated application as L903; no changed kernel, observable or height range and no new search or originality claim.
SOURCE_EVIDENCE: Sprungk arXiv:1906.07120v3 Theorem8 printed p10, probability setup p3, half-L1 convention p7, normalization cases pp7-9 and AppendixA before (13) p24; DLMF4.36.1/4.33.1/25.6.1 as applied in audited L899; L898 domination and audited L902 coefficient order under retained L309/L037 contracts. Primary hypotheses and proof cases were inspected in step129; this nomination reuses them.
COMPARISON: The general stability theorem is imported. L903's changed cosh-weighted reference, mass recovery and finite parity observers are the proposed specialization to audit; L899's unweighted TV bound alone is insufficient. Van Hemert Section11 gives fixed-degree refinement and does not supply this quantitative uniform-degree application.
GAP: L903 has not received a separate audit; check its explicit constant, the original versus weighted normalizers, the two complementary squared-height increments and every endpoint. Independent signs, growing-frequency coverage and higher mixed positivity remain open.
REASON: A first audit of the completed specialization is a concrete bounded continuation. This is a new nomination for separate next-turn approval, not an audit or approval performed during step130 and not a repeat discovery search.
SCOPE: Exactly L903 for R>0, eta>0, integers m>=0, real |x|<=R and 0<=a<=y<=b<=1/2. Retain L902's inherited arithmetic contracts without replay, and allow explicit finite theta-integral constants. No optimization, new sign premise, numerical certificate, unbounded-frequency width or curvature reproof.
COVERED_TARGET: Audit L903's weighted-reference stability, recovery of A_0 normalization and degree-uniform parity bound on closed height cells, retaining L902's L309/L037 contracts.

The main gap is L030–L032/C032a actual-Xi all-degree mixed positivity.
The intermediate assertion is a fixed-window absolute cell-error budget;
it could support adaptive coefficient refinement once independent margins
are proved. No such margin is selected or assumed.

Read L903's full proof and the precise scalar/stability interface of
L899. L898 supplies theta domination and normalization; L902 supplies
only coefficient order and carries L309/L037's retained contracts.
Check the changed reference's finite positive mass, potential L1
membership and essential infima; the exact posterior normalizers; the
half-L1/full-L1 factor; raw mass differences; return to the original
A_0 normalizers; and the nonnegative finite parity observers with their
single integrable cosh-series majorant. Reconcile the constant in (1)
with (7)–(10), and verify that the two height increments add to the
whole cell width without an extra factor or a hidden sign. Include
m=0, x=0, a=0, b=1/2 and coincident heights.

Pass only if the stated absolute estimate and positive width follow
with exactly these hypotheses. Correct or withdraw any failed factor,
normalizer, domination or endpoint claim. The weighted-density estimate
itself does not use L902's curvature contract; the lower inequality for
the minorant does. Do not promote either estimate to Fourier positivity.
No new general stability or curvature proof is requested.

Primary citations, version qualifications and source reuse are canonical
in L903 and the preceding assessment. Sprungk's reference is
[Theorem8 in v3](https://arxiv.org/pdf/1906.07120v3#page=10).
Van Hemert's inspected raw source and fixed-degree scope are recorded
in the step129 review; its mutable-version qualification remains.
Full and supporting Mathlib coverage remains unchecked, not absent.
L898's fixed cross-endpoint stop and L312's cosine-order failure remain
comparisons, not mathematical premises. No cross-notebook input.

No independently justified signed compensation mechanism is identified
by this bounded specialization. That missing input presently blocks a
justified central creative nomination; this ordinary normalization and
hypothesis audit is not labeled creative. After the audit, select further
work for its relevance to signs rather than repeating width calculations.

## Separate scope approval — 8 November 2026, step131

LITERATURE_REASON: The supervisor requires separate approval of the newly
saved L903 audit nomination; reuse the ready step129 source assessment
rather than repeating its searches. This step checks coverage of the
completed application's audit, not the mathematical validity of L903.

The complete L903 text was read to identify its source interfaces, with
L899's scalar/stability interface, L898's normalization/domination range,
L902's hypotheses and ordering interface, and the recorded fixed-cell
failure. The preceding assessment's primary theorem extraction and
essential proof cases are reused unchanged. No new external theorem,
source version or broader search is needed for this exact target.
No mathematical audit verdict is issued in this literature-only turn.

Coverage comparison for the later audit:

- L903 (3) imports Sprungk v3 Theorem 8, with the probability setting,
  L1-potential hypotheses, essential infimum, finite normalizers and
  half-L1 convention already extracted in step129. Its arbitrary
  reference probability covers the type of changed reference proposed
  here; verifying this particular reference remains the audit's work.
- L903 (4) uses L899's already assessed scalar comparison on the closed
  height interval, including zero. No new scalar theorem is proposed.
- L903 (5)–(6) calls for fixed-R polynomial-exponential domination and
  essential-infimum checks. L898 supplies the relevant domination
  interface; neither a uniform-in-R statement nor a new decay theorem
  is required by the nominated scope.
- L903 (7)–(10) and its final parity application are the local application
  to be audited, not conclusions imported verbatim from Sprungk.
  In particular weighted posterior normalization is distinct from A_0,
  and both raw mass corrections must be checked. The assessment covers
  these application obligations; it does not certify their factors.
- L902 supplies only the coefficient order under retained L309/L037
  contracts. Its curvature certificate replay and an oscillatory-order
  theorem are outside scope. The final nonnegative lower inequality
  must remain qualified by those contracts.

The scoped duplicate comparison in step129 remains applicable: L899's
unweighted estimate and L900's transform estimate do not supply the
stated all-degree unbounded-observer application. Van Hemert's inspected
Section 11 covers fixed-degree refinement. L898's fixed cross-endpoint
stop and L312's cosine-order failure remain comparison evidence, not
premises or a ban on this different estimate. No newly discovered result,
stronger source conclusion or new mathematical obstruction is claimed.

DECISION remains SPECIALIZE, now separately approved for the exact TARGET
and COVERED_TARGET above. The next invocation should perform one audit,
classified REPRODUCTION, with the stated endpoint/factor/normalizer test.
Pass only with the stated hypotheses; correct or withdraw an invalid
claim. No further literature is needed unless an essential hypothesis or
source interface changes. The finite-window absolute loss can price
refinement, but independent signed margins, growing-R coverage and
higher mixed positivity remain open. Mathlib coverage remains unchecked.
No justified new central signed-compensation mechanism was identified;
this scope approval does not manufacture a creative nomination.
