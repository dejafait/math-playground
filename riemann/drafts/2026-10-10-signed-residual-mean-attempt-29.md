# Signed residual mean — bounded working record

Approved target: compute the sharp dyadic mean of L370's
−4wk/(T^4L^4) at log H scale, under the unchanged SPECIALIZE assessment
`drafts/literature/2026-10-10-signed-residual-mean-calculation.md`.
Main gap: global actual-theta positivity and the total L367 margin.
Downstream use: one signed term in L370; the separate w'-square mean
and total comparison remain independent. Stop on logarithmic cancellation
or any uncontrolled error of that scale; no lower-order expansion.

Unfinished calculation checkpoint: write r=e^{iφ}U, h=e^{iφ}V,
V=bZ, f=−r, g=Re h. Then w=−Re X and k=−Re Y, where
X=e^{2iφ}(UV'−U'V) and
Y=e^{2iφ}[U'V''−U''V'+iω(UV''−U''V)
−(ω²+iω')(UV'−U'V)]. Leading terms are
X_0=−b e^{2iφ}U'Z and
Y_0=b e^{2iφ}Z(ω²U'−iωU'').
The proposed coefficient is −S/(192π²), S=ζ(5)ζ(3)²/ζ(6).
This is not yet a proved assertion at this checkpoint: complete
order-two Cauchy moments, signed unsmoothing, full tails, reflection
and all height-rectangle edges must be checked before canonical recording.

Inputs read: L366 (1), L368 carrier and ordinary right-line jets,
L370 in full, L380 carrier/reflection, audited L381 in full,
and the completed exact-target source/duplicate/failure comparison.
Prior source coverage is reused; Young is imported, not reproved.
No RH, simplicity, noncoincidence, physical D≤0 or common-count bound.

## Completed bounded attempt

The checkpoint above is superseded by the full proof in
`lemmas/L386-signed-residual-negative-dyadic-mean.md`.
The coefficient survives: both leading opposite-height terms are
required, while the complete same-height projection is O(1).
The proof records full order-two tails and signed endpoint control.
No lower-order calculation, w'-square mean or total-sign inference was
attempted. Classification: RESEARCH / REPRODUCTION / ADVANCE, local
specialization only; a separate critical audit remains pending.
