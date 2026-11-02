# Fixed uncorrected Jacobi mixed term — 2026-10-31

The approved target tested ordinary finite-shift convergence and
temperedness of M(t)=integral k(s+t)Q(s-t) ds with exactly L600's Q.
[L601](../lemmas/L601-jacobi-mixed-correlation-not-tempered.md)
contains the full proof, hypotheses, citations and independent critical
audit completed on 2026-10-31. Every finite shift converges absolutely
and M is continuous, but its regular distribution is not tempered.
The audit required no repair and accepts only this local stop.

**WHY IT FAILS.** The positive actual theta kernel makes the surviving
negative zero mode of Q contribute a nonzero exponentially growing
signed translation limit. A fixed nonnegative translated smooth bump
detects exponential averaged mass, contradicting every polynomial
Schwartz-seminorm bound. Thus decay of k repairs finite-shift
integrability but does not make this mixed term an ordinary tempered
Fourier component. This is a different test from L600's L2 obstruction;
neither stops corrected profiles or specified complete combinations
with compensating terms. No such identity or independent signed
residual estimate is established, and no Xi sign follows. Reopening
this implementation requires a materially changed, explicitly defined
profile or combination and its own discriminating test and coverage.
