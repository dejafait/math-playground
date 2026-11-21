# Full Mellin remainder: reproduction nomination1652

TARGET: Reproduce Kawano v1's full relative Mellin bound |I(p)/S(p)-1|<=(17/10)L^(9/2)/r on L>=12, Re(p)>=-|p|/(4L), from C048a-i with an exact contour partition, principal normalization and uniform total error allocation.
CHECKED: 2026-11-19
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse step1652's exact-bound primary queries, scoped full-remainder duplicate search and preserved global-import/endpoint-loop stops, recorded in 2026-11-19-mellin-full-remainder-source-notes-1652.md; no matching canonical assembly theorem found in that bounded scope and no novelty claim.
SOURCE_EVIDENCE: Kawano Preprints.org202611.0383v1, posted4November2026, DOI10.20944/preprints202611.0383.v1, https://www.preprints.org/manuscript/202611.0383/v1 , Section5.1(25), Section5.2(28)-(29)/Lemma5.1(i) contour and both phase cases, AppendixB full-mode/origin paragraphs and (A4), AppendixC domain through the final budget before C.1, directly inspected19November2026; reuse source-notes1627/1648. Exact statement, applicability and source version in source-notes1652.
COMPARISON: The full inequality and its allocation are already claimed in the source. C048a/b provide the continued I and combined origin; C048c-i supply matching finite components and tails with S(p). This is a known-source assembly specialization, not a creative sign mechanism or a general saddle-theorem application.
GAP: Prove the complete oriented identity, Gaussian subtraction/completion and finite mode split; verify C048f's 112sqrt(L)exp(-5r/L^2) is below10^(-4)L^(9/2)/r uniformly, convert C048e's scale, and certify one total coefficient below17/10. All boundary/reflection/zero-height cases and convergence qualifications must be retained.
REASON: Verification is justified because a quantitative unreviewed source statement and individually proved components do not by themselves constitute the assembled proof. Reuse every canonical component conclusion; no reproof of general integration or saddle theorems is needed. Essential source coverage is complete for this bounded REPRODUCTION target.
SCOPE: Newly ready continuation requiring separate approval next turn. Only the displayed full relative remainder is covered; the source's additional less-than-one claim, finite-band estimates, derivative bounds, zero counts, inversion and sufficient actual-Xi signs are excluded.

Use C048a's meromorphic I, C048b's combined E_o, and exactly C048c's
sector, d=1/(3L), principal w=W_0(2p/pi), u_0=w/2, h_p, g, K,
A_0 and S(p). Reuse the component definitions without changing their
modulus placement. Source-notes1652 contains the source-to-obligation
comparison; source-notes1648 supplies the preserved failure context.

The bounded test is an exact identity and one uniform triangle-inequality
budget below17/10 on the whole closed sector, not sample evaluation.
Write all contour pieces and normalizations explicitly, use the
fixed-height identity pointwise, and retain real p, conjugation and
both angular boundaries. The combined origin is charged once. Local
leading error, Gaussian completion, lower-power first mode, higher
local modes and complete horizontal tails must each appear exactly
once. Only the scalar conversion still unpaid in C048f is to be
verified, not a stronger theta-mode theorem. Any scalar certificate
must be exact and its complete load-bearing evidence inspected.

The printed source bound1.606651 is unnecessary: any rigorously
verified total <=17/10 at the same normalization meets the target.
Do not assume that sum or the higher-mode allocation as premises.
If assembly fails, identify the incompatible hypothesis, missing
integral or failed sufficient budget and preserve the partial reasoning;
a failed majorant is not a counterexample to the remainder or RH.

Keep ATTEMPTS/2026-11-05-mellin-global-remainder-import-unpaid.md and
ATTEMPTS/2026-11-05-mellin-endpoint-review-loop-closed.md. No supplement
retry, rotated L798-L804 bound transfer or full-sector expansion of
AppendixB's finite-band constants is authorized. The general
strip-series identity from L799 may be reused with its actual scope.
Any resulting full proof belongs in a single canonical corollary with
all direct mathematical uses reflected only in DAG.md. Mathlib matching
coverage is unchecked, not asserted absent.

The main goal remains actual-Xi all-degree algebraic-square positivity
in L030-L032/C032a. This analytic input could support later control of
I, but C028b's H_d=o(d), C028g's S_F=0, zero counts, inversion and a
sufficient Mellin-to-sign bridge remain independent. There is no RH
candidate and no specified new signed mechanism for a creative route.
