# Shrinking height-cell specialization — working record, step130

Approved scope: the pre-existing SPECIALIZE assessment
`drafts/literature/2026-11-08-normalized-shrinking-height-cell-specialization.md`.
Main gap: L030–L032/C032a actual-Xi all-degree mixed positivity.
One target: fixed-R absolute error of L902's own-normalized parity
minorant, uniformly in degree and the closed height cell. Possible use:
price adaptive refinement before any independent positive margin is paid.
Pass test: a finite explicit constant and positive squared-height width,
including height zero and no sign assumption. Stop/narrow on a failed
normalizer hypothesis, exact duplicate or hidden sign assumption.

Inputs read: L898 domination/normalization, audited L899 scalar potential
bound and Sprungk Theorem8 application, audited L902 with its unreplayed
L309/L037 contracts. Reuse step129's primary-source comparison; no new
source or mechanism is needed. The fixed cross-endpoint stop remains.

Plan saved before completion: write c=cosh(Rq), D_y=integral c W_y,
D_*=D_(1/2), a_*=A_0(0), Q_R=integral c p^2 W_(1/2),
Q=integral p^2 W_(1/2). Apply Sprungk to reference c W_(1/2)/D_*.
Recover c W_y/A_0(y) from its newly normalized probability, keeping
both weighted-mass and original-mass errors. Then bound both finite
parity observers by c; use L902 only for the lower inequality.
All constants/claims at this point are pending verification.
No Fourier sign, numerical optimization, global coverage or RH candidate.

Completed: canonical proof and exact constant are in L903. Applying the
known stability theorem to the changed reference gives the weighted
probability bound; two raw mass estimates recover the original A_0
normalization. All-degree finite parity observers have one integrable
cosh majorant. The cell increments telescope in squared height.
Result: the target absolute bound and positive width are established
locally by specialization, conditional on L902 only for the lower
inequality. No failure or numerical calculation was needed. The new
proof awaits a separate audit; this is not progress beyond the known
general stability theorem or an RH candidate. See the audit nomination
for the sole continuation, with unchanged source scope and no sign input.
