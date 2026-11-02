# L618 independent audit: preserved reasoning

Approved target: Audit L618's full-multiplier constants, weighted Fourier inversion and causal support compression, including the fixed-window quantifier limitation.
Prior gate: literature/2026-11-01-l618-compact-norm-audit.md (SPECIALIZE).
Inputs: L001/L005/L018; Suzuki 1907.07302v2, (1.1)/(1.10), Theorem 1.2 (K-ii)/(K-iii); DLMF 5.9.13; L1 Fourier inversion; Hilbert--Schmidt inequality.

Independent replay so far: the derivative majorant is summable on each Re(s)>=1+delta. At Re(s)=16, the arithmetic loss is <=1/14. DLMF's h lies strictly between 0 and 1, so the digamma loss in Re(xi'/xi) is 1/16. Both rational real parts are positive. Twice the total loss is 15/56; therefore q=(pi/8)exp(15/56)<28/41. For theta>=2, the complete transform has L1 norm <=16*pi*(28/41)^theta. The Fourier weight c=31/2 gives s=16-iu and weighted tail O_theta(exp(-15x)); inversion gives 8*exp(cx)*(28/41)^theta at every x by continuity. Causality restricts both input and output to [-t,t], producing HS norm <=16*t*exp(31t)*(28/41)^theta on the original space. t=0 is the zero operator; theta=2 has integrable quadratic decay. No missing factor or quantifier exchange found.

Source theorem statement was directly reopened to verify parameter/domain and normalization, without importing its (K-v) argument or implicit uniform constants. Remaining before final checkpoint: confirm DLMF domain/equation in the retrieved source, place complete audit record in the canonical lemma, select one uncovered continuation without expanding this mathematical attempt, and run scoped structure validation. No new theorem or stronger scaling claim is intended.

Completed: DLMF domain and equation confirmed; full audit is canonical in L618. All replay checks pass without changing the inequality. The new screw-function continuation remains REVIEW_REQUIRED and unproved. Scoped documentation validation passed.
