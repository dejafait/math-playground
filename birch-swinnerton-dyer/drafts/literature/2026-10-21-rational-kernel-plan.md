# Capped rational-kernel plan — proposed known-method specialization

TARGET: Prove or refute a bounded rational Taylor enclosure plan for all 128 L101 kernels at M=Y=128, using the fixed 1016 panels of length 1/8, Taylor degree at most 256 and 256-bit outward dyadic arithmetic, with kernel radius at most 2^-50 and no derivative evaluation.
CHECKED: 2026-10-21
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the completed rational-kernel source comparison in drafts/literature/2026-10-21-backend-free-finite-kernel-review.md and its primary-source/query/failure record drafts/source-notes/2026-10-21-rational-kernel-source-review.md; this is a known numerical-analysis mechanism, not a novelty claim.
SOURCE_EVIDENCE: NIST DLMF v1.2.8 (2026-09-15), https://dlmf.nist.gov/1.4.vi equations 1.4.35--37 with C^(d+1) hypothesis and both finite remainders; 1.4.26/28/29 integration cases; 4.2.19, 4.6.1/4, 4.7.3/7/8/10, 4.8.2 and 1.2.11 elementary identities/derivatives. L031 supplies existing exact interval arithmetic and small-argument constant rules; audited L101 supplies the kernel and eventual total-error contract.
COMPARISON: Sources supply finite Taylor and integration containment principles on the entire positive path, with no unavailable binary. Only the capped numerical specialization, constant/rounding/product error propagation and replay-cost proof remain to derive; the full curve-specific radius conclusion is not imported.
GAP: No cap-feasibility inequality, complete rational integration construction, operation bound, actual c endpoints, coefficients, kernel outputs or derivative exists. This assessment does not authorize implementation or claim radius attainment.
REASON: Essential mathematical coverage is sufficient for this proof-only test; a new ready continuation receives separate next-turn approval before research. The unavailable library and unread optional Taylor-model implementation are not inputs.
SCOPE: Rational c_* in [3/10,1/2], n=1,...,128, y in [1,128]; fixed endpoints 1+j/8, j=0,...,1016; panel polynomial degree <=256, scalar series <=256 terms, exponential squarings <=16, outward grid 2^-256. One complete error/cost proof attempt, no parameter or kernel evaluation and no program.

The exact target concerns J_n(c_*)=integral_1^128 exp(-c_* n y)
log(y)/y dy. Uniformity in the supplied rational parameter avoids
assuming uncomputed narrow c endpoints. The main BSD gap and downstream
fixed-case provenance use are unchanged from the completed review.

The proposed panel scheme may use Taylor factor polynomials with
separate enclosures of constant exp/log values; positive argument
reduction and all its errors must be explicit. No polynomial factors,
degrees within the caps or numerical error allocations are prescribed
as already sufficient. Do not assume an alternating-series bound for
large exponential arguments or log increments outside their hypotheses.
Retain or bound all discarded products; include all directed rounding,
then integrate errors on every panel and sum them over the full path.
Identify finite independent replay obligations and a conservative
arithmetic-operation bound. Do not import a software tolerance as error.

Essential retained inputs are audited L101, L030's exact model/conductor,
L031's independent coefficient/sign and elementary parameter/arithmetic
rules only, audited L099, and foundations/02 for the eventual analytic
application. L035, L100 and published basis/Sha premises are excluded.
The proof of this numerical plan may leave actual parameter/coefficient
production and all BSD arithmetic comparisons unresolved.

Continue to an independently reviewed implementation target only if
the full error bound gives radius <=2^-50 for every permitted n,c_*
within the stated caps. Otherwise preserve the actual failed bound or
cost and park this plan, with no enlarged partition, degree or precision
in the same attempt. Even success gives no kernel value or nonvanishing.
Future exact signed summation keeps eta=0 in L101's
B=2^-43+200*delta+4*sum(|a_n|/n)e_n; zero containment is inconclusive.
Mathlib is not checked. No new mathematics beyond sources is claimed.
