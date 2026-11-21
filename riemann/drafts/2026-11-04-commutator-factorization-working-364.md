# Step364 — bounded commutator attempt, working checkpoint

Approved target: the exact target in
`literature/2026-11-04-commutator-dual-factorization-test.md` (EXPLORE,
saved before invocation). Main gap: actual-Xi mixed positivity; intermediate
purpose: controlled finite Fourier observable sensitivity for a later
ground-state/trial comparison. No trial residual or limiting transfer assumed.

Inputs read: complete L759 including its independent audit; step362's primary
source comparison and recorded failures. Reuse the audited entry enclosures,
not a new arithmetic matrix or source hypothesis. Prior floating and first
interval failures are retained. No new source discovery is required here.

Let x=xi/sqrt(L), eta^T x=1, T=A-epsilon I, D=diag(j),
F=(w-D)^(-1), w=zL/(2pi). With f=x^T F eta and a=x^T F beta,
the imported commutator formally yields

    x^T F T = a eta^T F - f beta^T F.

This identity alone still has beta^T F instead of the desired eta^T
boundary row. It is a working algebraic reduction, not a controlled
preimage. Check signs and normalization in the final write-up. Defining
the missing row through T's inverse is not an explanation of a gain.

Bounded test: lambda=sqrt(13), N=120, z=i/4, all 241 directions/both
parities. Need two-sided actual gap bounds, nonzero row norm, and rigorous
ratio rho=g||qRP||/||q||<=1/10 plus a non-tautological explanation to continue.
A point-arithmetic screen is only diagnostic. A generic commutator model,
if used, must be distinguished from this arithmetic cell. Stop a mechanism
that only reinstates the inverse or assumes the missing overlap estimate;
ambiguous enclosures are inconclusive. General parity, boundary overlap,
trial residuals, both limits and Xi transfer remain open.

The full interval test has now enclosed the actual gap in
(3.0555e-55,3.0556e-55) and rho in (5.25e-30,5.26e-30). The direct
frequency-resolvent ansatz h0=(k/a)x^T F leaves a residual larger than q:
its norm ratio is 1+2.2592481...e-29. Complete enclosures and all parity
pivots are saved in `scripts/spectral-triples/commutator-certificate-364.json`.
This is a finite diagnostic certificate, not yet a controlled preimage.

Remaining algebra within this same attempt: the imported identity T D x=-beta
and parity give T D^2 x=c eta-D beta, c=beta^T D x<0. Thus the dominant
boundary term may admit an explicit partial preimage, leaving a smaller
arithmetic row. Check its full norm and cost; retain any inverse needed
for the remainder openly. This cannot be described as an inverse-free
exact preimage unless that remainder is actually paid without such a solve.

## Completed step

The second commutator certifies ||r||/||q||<0.02197 and
g||H||/||q||<7e-31, hence rho<0.022. The exact inverse is still retained
on r. Full proof, source qualifications and error bounds are canonical in
`lemmas/L760-finite-commutator-fourier-row-saving.md`; this note preserves
the attempted reduction and its failure rather than a competing proof.
The finite partial result is ADVANCE, with independent audit pending.
