# Fixed odd-model, field and support certificate

2026-10-25. Work under the prior SPECIALIZE assessment
`literature/2026-10-25-pair-genus-two-odd-model-support.md`, unchanged target.
Main gap: residual positive primitive Beal signatures. Intermediate target:
certify the saved genus-two quintic, its actual quartic descent factor,
and sufficient Jacobian two-descent support compatible with L137.
This can prepare a later rank-upper-bound calculation; units, full descent,
local images, ranks, points, marked lifts, degree-nine/integer recovery,
both L095 systems and other signatures remain independent gaps.

Inputs: audited L110; saved complete `/model` in
`scripts/pair-genus-two/rank-lower-certificate.json`; L133; audited L134
and L137. The approved source assessment and localization assessment
are reused. ATTEMPTS/050 and 059–060 stop different finite searches;
their stops and unfinished L108 are preserved. No cross-notebook input.

Before calculation: reuse c=-36300, X=c/(T-2), Y=c²W/(T-2)³.
Check all coefficients, squarefreeness, inverse compositions and exceptional
proper points. Divide by the known factor X-9075, then certify both field
maps and complete degree-four basis matrices, including the transported
maximal-order basis. Compute discriminants by exact Sylvester determinants
and replay by a separate resultant algorithm and Taylor expansion.
Only this fixed model is tested; no point/relation enumeration or backend
probe. Sympy is unavailable; use Python standard-library exact rationals.

Finite bounds: degree <=12, matrix size <=12, rational numerator/denominator
bit length <=4096, rational prime trial bound <=100000. Try division by
2,3,5,11 first and retain the complete cofactor; if nonunit, use bounded
trial division, recording every trial. Save full certificates and failures.
These are finite-domain/size bounds, not an elementary-operation count.
Continue dependent descent only if every model, twist, inverse-field and
outside-support check succeeds. Any unresolved cofactor or map discrepancy
withholds that interface rather than silently altering the curve.

## Completed fixed calculation

Canonical result: L138. The saved quintic is independently certified,
including the inverse proper-curve maps and exact twist/functions.
Its factor H gives the actual field map eta=-907500/(alpha-50), with
inverse alpha=50-907500/eta, full inverse basis matrices and the complete
transported maximal order. The exact polynomial discriminant is
2^32*3^21*5^27*11^35, so sufficient Jacobian support is exactly
infinity,2,3,5,11. No enlargement of L137's localization is necessary.

The complete artifacts are
`scripts/pair-genus-two/odd-model-support-certificate.json` and
`scripts/pair-genus-two/odd-model-support-verification.json`, produced by
`odd_model_support.py` and `verify_odd_model_support.py` in that directory.
The producer passes 22 checks and the independent replay 82; no mathematical
failure or cap stop. Degree/matrix size actual/caps are 6/12 and 9/12;
observed rational bit sizes are 417/4096 and 250/4096; factor trials end
at 11/100000 with final cofactor one. These are observed size/domain
bounds, not full operation counts. The replay uses sparse polynomial
arithmetic, Taylor expansion, Gaussian determinants and Euclidean
resultants and imports no producer mathematics. Complete matrix and
factorization evidence is consumed, not merely previewed.

The initially checked environment lacks Sympy; no installation or renewed
backend probe was needed. A patch-format error while writing the new
lemma changed no mathematical file and was corrected before its creation.
The final documentation check caught six omitted trailing zeros in the
displayed decimal disc(G); its prime powers and both certificates were
already correct. The decimal was corrected to the complete certificate
value and all three printed decimal values were compared exactly.
The prescribed point/divisor and relation searches were not rerun.
No source refresh was needed for this unchanged ready target.

This is relevant local preparation using known theory, not a novel general
result, a Selmer computation or a rank bound. The continuation test passes
for this fixed interface; a separate critical proof audit is proposed
under a new REVIEW_REQUIRED assessment, without approving that audit here.
All independent main-target gaps and historical stops remain as above.
