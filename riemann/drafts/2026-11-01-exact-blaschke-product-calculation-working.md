# Exact-product calculation — working checkpoint

Invocation-start target: determine whether retaining L645 (6)'s exact product changes C645b's envelope stop at N=floor(log gamma). The saved SPECIALIZE assessment covers this calculation; reuse its source review. Main gap: actual-Xi signs/all-degree positivity. This step tests only an elementary factor loss; no sign claim follows from removal of the obstruction.

Inputs read: L645 hypotheses and finite-Blaschke bound (6), full audited C645b, C645a's supplied conclusion/source assessment, L018 completion, named attempt stop and audit history. Existing unfinished changes preserved. No external search or cross-notebook input.

Let f_delta(t)=-log b_delta(t) and Lambda_delta=integral_0^1 f_delta(t) dt. The exact negative log product is sum_{j=0}^{N-1} f_delta(j/N). Need rigorous finite-grid error, both floor inequalities and full fixed-delta comparison Lambda_delta versus delta/4; equality needs separate treatment. f is smooth and decreasing on [0,1]. Source-backed Euler–Maclaurin may supply endpoint/error control. An elementary antiderivative is a possible means of comparison; no verdict yet.

Continue if the comparison changes whether this explicit envelope necessarily fails. Park the refined certificate if divergence persists. A favorable comparison removes only the proved rate obstruction; actual derivative lower bounds and signed residual control remain open. Do not reuse q_delta^N as the purported exact test.

## Analytic comparison found (pending canonical write-up)

For fixed R, write f(t) as integral from d to R of
k(x,t)=x/(x^2+t^2)-xt^2/(R^4+x^2t^2). On 1<d<=x<=R and 0<=t<=1,
partial_x k=(t^2-x^2)/(x^2+t^2)^2-t^2(R^4-x^2t^2)/(R^4+x^2t^2)^2<0.
Thus Lambda>(R-d)[2 arctan(1/R)-1/R]>delta[arctan(2/3)-1/3]>delta/4.
The last strict bound follows by integrating the exact geometric remainder:
arctan(2/3)>2/3-(2/3)^3/3+(2/3)^5/5-(2/3)^7/7>7/12.

DLMF 2.10.1 with m=1 and F(x)=f(x/N), subtracting endpoint f(1), gives
S_N=N Lambda+(f(0)-f(1))/2+r_N, |r_N|<=K_delta/(8N),
K_delta=d^2/R^4+1/d^2. The finite correction and floor therefore give
B_N=Theta_delta(gamma^(-Lambda)), with explicit constants to be recorded.
The benchmark U B_N/(D gamma^(v+epsilon)) tends to zero; actual envelope
ratio is only bounded BELOW by this benchmark. No success or sign follows.

## Diagnostic evidence (not used in proof)

A direct binary64 antiderivative diagnostic evaluated Lambda=f(1)+(R^2/d)atan(d/R^2)-d atan(1/d).
All six runs completed with no runtime failures; required rate/delta threshold was 0.25.
The (delta, rate/delta) outputs were (0.0001,0.2546777884693263),
(0.01,0.2555237014962408), (0.1,0.26345683474722215),
(0.25,0.27771783949926077), (0.49,0.3035859688569707),
(0.5,0.30475329366292425). The final delta is an excluded endpoint diagnostic.
These floating-point values were reconnaissance only, not a certificate of an inequality,
not verification across parameters, and not evidence about zeta zeros.
Exact rational check of the arctangent lower polynomial: 44846/76545; its excess over 7/12 is 779/306180.
