# Reflected complete-kernel test — work in progress

Approved target: drafts/literature/2026-10-31-associated-theta-reflected-majorant-test.md.
Main gap: actual-Xi all-degree signs at unbounded heights. This test concerns
only a stronger sufficient condition for the first sign.

The sufficiency link survives: for h=pi/x, absolute half-wave rearrangement
of I(x)=integral_0^infinity G(t)sin(xt)dt gives
I(x)=integral_0^(h/2) [S_h(r)+S_h(h-r)]sin(pi r/h)dr.
Thus D_h>=0 on this half interval implies I(x)<=G(0)/x. This
requires all h for the all-frequency conclusion, not the bounded box.
Full proof and hypotheses will be saved canonically after the attempt.

Planned diagnostic: evaluate A using its full positive theta series with
explicit omitted-mode and improper-tail envelopes, and numerical Gauss
quadrature/Chebyshev integration. Search the approved box only. Quadrature
and interpolation errors are NOT certified; no positive grid or replay
establishes any uniform sign. If a negative candidate appears, it requires
an independent rigorous enclosure before being reported as a counterexample.
No mathematical conclusion is claimed in this unfinished note.

## Completed attempt

The full sufficiency proof and analytic improper-tail estimates are in
L598, `lemmas/L598-reflected-cumulative-sufficient-condition.md`.
The diagnostic used 129 equally spaced h in [1/8,4] and 97 equally
spaced q=r/h in [1/8,1/2]: 12,513 pairs. Runs used (Chebyshev nodes,
s Gauss nodes)=(128,192),(256,384),(384,512), eight theta modes,
|s|<=6 and cumulative cutoff 3. All sampled previews were positive.
At the finest resolution the minimum was 2.7979503671947924e-6,
D/G(0)=0.0004900160795299805 at h=1/8, r=1/64. The successive maximum
grid differences were 3.04444e-16 and 3.62558e-16. These differences
are empirical replay evidence, NOT rigorous error bounds.

The full evidence is `scripts/reflected-majorant/scan-certificate.json`.
The complete cumulative/alternating tail contributes <10^-500;
omitted theta and s tails contribute <10^-92 by L598. Gauss,
interpolation and rounding errors remain unenclosed. There is no
negative candidate to certify, no certified positive pair, and no
uniform sign conclusion. Parameters outside the grid, outside the
box, and the all-degree main gap remain unresolved.

Outcome EXPLORATION: the bounded search was unsuccessful. Do not repeat
it without a materially new estimate or mechanism. A distinct proposed
strength test asks whether even a positive kernel with Laguerre–Pólya
Fourier transform must satisfy this stronger reflected majorant. It
needs separate literature coverage and no answer is assumed here.
