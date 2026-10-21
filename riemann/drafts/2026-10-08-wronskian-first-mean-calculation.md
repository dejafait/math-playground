# 2026-10-08 — approved Wronskian first-mean calculation

The unchanged SPECIALIZE assessment is
`drafts/literature/2026-10-08-actual-wronskian-first-mean.md`.
The calculation addresses feasibility of a signed-mean input to a later
local Wronskian test, not the still-open actual-theta positivity assertion.
Existing unfinished work is preserved.

Checkpoint before completing bounds: in L369's notation, writing
`V=bZ` to avoid confusing its response amplitude with the Wronskian,
the requested convention is

    W = F_0'G-F_0G'
    W/A² = Re[e^(2i phi)(U V'-U' V)]
         = Re[b(bar U Z'-bar U' Z+2i omega bar U Z)+b' bar U Z].

These are zero-safe identities; the A' and the initial i omega terms
cancel exactly before critical-line reflection restores 2i omega.
The diagonal predicted by L369 (16) is

    t/(pi T² L) [mu_0 omega + mu_0/2-mu_1],

where mu_0=zeta(3) and mu_1=sum(log n)/n³. All b and b' terms
remain present. The diagonal is O(1/H), while the presently available
mixed-mean error appears larger. Verify every weight's bounded variation
and the final error before promoting this scratch computation. A mean
alone cannot exclude common-zero resets (L373). Higher moments and
localization are outside the approved scope.

Completed calculation: canonical L380 contains the exact identity,
complex weight derivatives, applicability of L369 (16), complete
diagonal and uniform error. The diagonal equals
`zeta(3) log(2)/(2 pi H)+O(1/(H log H))`, while the covered error
is `O(H^(-1/2) (log H)^2)`. The real t² carrier diagonal cancels;
the imaginary linear term in b and real b' give the residual diagonal.
The mean tends to zero, but the available error envelope dominates
the diagonal. This is an informative negative for this signing
certificate, not a lower bound for the actual error or a proof that
sharper first moments cannot work. No mathematical script was needed.
The original scratch checkpoint above is retained as unfinished-work
provenance; all completed reasoning is in L380.
