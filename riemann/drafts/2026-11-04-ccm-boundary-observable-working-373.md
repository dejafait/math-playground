# Step373 working record — approved finite observable

The prior SPECIALIZE assessment is
`drafts/literature/2026-11-04-ccm-boundary-observable-test.md`.
Exact target: enclose b(P_120 k) away from zero, then compare the normalized
observable with the L760 ground interval at lambda=sqrt(13), z=i/4.
Main gap: actual-Xi positivity. Downstream purpose: discriminate this
trial for quantitative ground/trial comparison. Upper discrepancy<=1/10
passes this observable; lower discrepancy>1/10 supplies negative evidence;
an unresolved denominator or straddling interval is inconclusive.

Inputs inspected: L759 basis; full L760 including normalization and error
propagation; L761 hypotheses, coefficient transport and complete-audit
description. The audited ground observable interval has been read in full
and is approximately2.3233310939e28. All241 trial coefficient rectangles
will be read and checked by the finite evaluation, without even-part
replacement. Their error already includes infinite prolate mode error and
finite transport; those errors must not be removed or paid twice.

Plan: integer interval arithmetic on the grid10^-340; reuse the audited
L and pi intervals, enclose the positive sinh series with an explicit
tail, form both complex rows and all contributions, certify nonzero
complex boundary modulus before division, and retain complete evidence.
No ratio or outcome has yet been computed. Python integer semantics and
the upstream Decimal arithmetic remain trust assumptions. Neither limit,
family control, full-vector agreement nor Xi sign is covered. Existing
96-mode failures and112-mode success remain unchanged.

Completed: the initial pending state above is preserved. C761a records
the certified nonzero denominator and discrepancy0.48616229937498...,
strictly above1/10. Both complete certificates pass all arithmetic and
input-inflation checks; the miss is the mathematical outcome. Canonical
proof and qualifications are in C761a, not this working note. The next
boundary-trace nomination has REVIEW_REQUIRED source coverage; no
variable-N estimate has been derived or approved.
