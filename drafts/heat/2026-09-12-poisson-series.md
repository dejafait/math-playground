# Poisson representation checkpoint — 2026-09-12

Earlier L138–L139 work is complete and preserved. Set N=sqrt(t/(2π)), τ=t−π/2, and extend f(x)=x^(−2+iτ)exp(−log²(x/N)) by zero for x≤0. Then S=e^(π²/16+iπ log(N)/2) Σ f(n). The extension should be Schwartz, so periodization gives exact Poisson summation. Two integrations by parts bound the omitted Fourier modes by ||f''||_1/(2π²K). Candidate explicit derivative bound: ||f''||_1 ≤ N^(−3)sqrt(π)e^(9/4)[2(|τ|+3)²+24]. Taking K=ceil(t²) should make the error O(t^(−3/2)), below L138's remainder.

These claims are draft and unproved at this checkpoint. Resume by auditing derivatives, the Schwartz extension, periodization, the zero mode and the tail constants. Positive Fourier modes have stationary points x=τ/(2πk) for t>π/2; estimating their combined cancellation is a separate unresolved task.

Completed: L140 proves the exact identity, zero mode, and explicit tail bound, including the derivative audit. The canonical proof supersedes the draft claims. No stationary-phase expansion or lower bound was proved. PROGRESS.md records the next scoped calculation.
