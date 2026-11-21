# Independent audit of the existing shifted specialization

TARGET: Critically audit C999g's shifted centered-derivative identity, full complex tail bound and first-exponential error comparison on [1,3/2] x [40,45], retaining the moving center, logarithm branch, both tails and normalization; verify the stated inequalities or record a precise repair without attempting another sign estimate.
CHECKED: 2026-11-11
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse completed exact-family, branch and contour searches in reviews425/427/428 and event comparison429 completed in step430. Targeted November11 history/assessment searches found the two derivations and source review, with no completed C999g audit in those records. No new sign claim or originality claim.
SOURCE_EVIDENCE: Lagarias–Rains math/0104176v5 (7July2002), Theorem2.1/(2.9), Proposition3.2/(3.7), Theorem4.4 complete proof(4.6)-(4.9), Lemmas4.5-4.7, printed pp8-9,12,21-24, https://arxiv.org/pdf/math/0104176v5 ; DLMF20.5.3 https://dlmf.nist.gov/20.5.E3 . Exact primary cases already inspected in step428; reuse its normalization and branch assessment unchanged.
COMPARISON: Source (4.8)-(4.9) supplies the full shifted identity and compact-strip decay, not C999g's explicit constants. The audit checks the already written specialization, mirrored half-line reduction and quantitative error allowance; it does not reprove the entire-family or contour theorem.
GAP: C999g's compact domination, even/conjugate symmetry, derivative formula, full complex tail constants and first-exponential allowance have not had a later independent audit. C999f remains separately unaudited and is not a premise for those estimates.
REASON: After parking citation-only determinant signing, validate or repair a retained analytic input independently of the unknown sign. This has an exact pass/fail claim and cannot be substituted for a collision certificate.
SCOPE: Newly ready nomination for separate approval; one conceptual proof audit of C999g only, with source imports reused. No new sign mechanism, contour optimization, numerical event search, implementation or audit chain is authorized.

Main gap: L030-L032/C032a actual-Xi all-degree positivity; L966/L968
forcing, L984(H) and C997s's capped E_n bridge stay separate.
The intermediate target is correctness of C999g's existing claims.
A verified centered representation and error budget could support a
future signed method; it pays no sign by itself.

Essential local inputs: C999g, L018/L019 for normalization and theta
convention, and the precise primary statements named above. Read the
complete C999g proof before the audit; today's review read only its
setup and conclusions. C999f may supply notation but no unverified
lemma claim. No cross-notebook input. Full matching Mathlib coverage
is unknown; distinguish source theorems from auxiliary support.

Check the exp(s*(x+i*y)) factor from source proof (4.8), the total
w derivative at fixed t with s=w/2+i*t, the continued theta logarithm,
reflection/conjugation on opposite horizontal lines, and the 1/2
normalization when reducing the full integral to a real half-line.
Check all domination needed before differentiation and all quantitative
bounds (including whether the <10^(-40) tail claim follows uniformly).
Check the first-exponential error comparison exactly as stated: an
upper allowance exceeding the core bound does not lower-bound the
actual error. Inspect complete load-bearing reasoning, not a preview.

Continuation/abandonment test: every retained equation and numerical
inequality must follow from the cited inputs under the entire original
rectangle; otherwise give a concrete countercalculation or correction
and trace its effect. Confirming the claims verifies an inconclusive
comparison, not G_w positivity. A successful audit does not authorize
repetition of the exhausted sign diagnostic. Any further mechanism
needs a separately assessed, materially different bounded target.

Keep G=G_t=0, G_w*G_tt!=0 prospective; no event, nondegeneracy,
curvature sign, all-height extension, initialization, multiplicity
control, global transport or RH conclusion is assumed. An audit is
mathematics and should default to REPRODUCTION under SPECIALIZE.
Route proof_audit/conceptual_audit, deep_research/xhigh: branch,
reflection, moving-center differentiation and full-tail control are
analytic logic questions rather than only arithmetic replay.
