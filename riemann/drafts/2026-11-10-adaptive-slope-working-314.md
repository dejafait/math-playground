# Adaptive slope separation — working record, step314

10 November2026. One RESEARCH proof attempt, completed as REPRODUCTION, under the
unchanged, pre-invocation EXPLORE assessment
[review312](literature/2026-11-10-adaptive-slope-spectral-separation-review-312.md).
Target: Assess whether degree-dependent signed slope measures of subexponential total variation can retain L997's selected quartet while uniformly suppressing the competing family 7/8+i*gamma for 7/4<=gamma<=9/4.

Main gap: L030-L032/C032a actual-Xi positivity and L966/L968 signed
forcing; L984(H) remains unpaid. The intermediate target is exactly
review312's finite assay, including its complete quartets, both closed
intervals, all short-interval endpoints and K_(n+2)'s constant subtraction.
Possible downstream use: norm-controlled spectral localization before
actual reconstruction and signs. These independent gaps stay open.

Threshold: selected value one for every sufficiently large n, one fixed
positive exponential suppression rate uniformly over the competing
ordinate interval, and TV bounded by every positive exponential allowance.
An obstruction must cover every finite complex Borel measure. A failed
construction, finite fitting, a pure exponential model or a finite
asymptotic truncation cannot decide the assay.

Startup overview/DAG and review312 were supplied verbatim. Narrow reads
checked L994(6)-(7), L995's exact contracts, the full relevant L997 proof
and its step294 audit, review291, and stop293. The fixed positive bump's
endpoint-jump argument does not apply to n-dependent complex measures.
Existing unfinished files are preserved. No cross-notebook input.

Initial possible mechanisms, not results: a degree-dependent Fourier
window may suppress separated frequencies but must overcome the factor
exp(c*n/8), retain the other Laguerre branch, and pay endpoint errors.
Alternatively, the exact quartet may admit an analytic response with a
common compact-support representation, allowing a norm-controlled dual
or propagation obstruction. The next work tests this second mechanism;
no scalar analytic identification or decisive growth bound is yet proved.

No new source assessment is being made, and no new theorem is assumed.
Known complex-analysis and Laguerre tools are reused on their recorded
hypotheses. If the calculation is incomplete, preserve its exact missing
estimate rather than claiming a universal stop.

## Saved reduction in progress

For real c the complete quartet response a_n(c;eta) is real. L997(7)
gives z_0(c)^n=exp(-cn/4)*exp(i*n*(phi(c)-c)). Multiplying nu_n by
this last unit phase preserves total variation. Taking the real part
afterwards preserves the selected value one and cannot enlarge any
competing modulus. Thus existence can be tested with a real signed
measure against the real kernels exp(-cn/4)*a_n(c;eta); this does not
restrict the complex-measure feasibility question. This exact reduction
still needs a complete write-up if it becomes a useful canonical result.

Summing the quartet before integrating gives
sum exp((omega-1)t)=4*exp(-t/2)*cosh((beta-1/2)*t)*cos(gamma*t).
This retains both conjugate and reflected pairs. Inserting this identity
in L997(5) suggests a real finite-measure operator amenable to exact
duality and bounded numerical diagnostics. Neither real-signed reduction
nor such diagnostics decides the large-n uniform assay by itself.

## Completed disposition

The full exact reductions and their qualifications are now canonical in
[C997a](../lemmas/C997a-real-slope-measure-duality.md). This preserves
the earlier working fragments as a record, not as an alternative proof.
Hahn–Banach and Riesz–Markov–Kakutani yield an attained real primal
maximum and an exact weighted dual norm; no closed-range or dual-minimum
attainment is assumed. C997a(7) identifies a sufficient all-measure
obstruction, but its quantitative estimates are unpaid. The elementary
analytic identification in C997a(8) retains an extra cosh(t/2) term.

The bounded floating-point dual experiment is saved in
scripts/adaptive-slope/dual-diagnostic-314.py and its same-stem JSON.
It keeps the exact quartet and both intervals in the integrand, but
quadrature, SVD, and validation at extra c points are uncertified.
The six runs n=8,16,24,32,48,64 produce no asymptotic certificate.
At n=64, the best tested cutoff gives grid residual about 0.001545
and coefficient l1 about 52379; the selected grid maximum is about
0.0038015. These observations cannot establish either (7) or its
failure. Increasing roundoff sensitivity makes extrapolation unsafe.
The complete arrays and explicitly listed failures are retained.

Disposition: EXPLORATION / REPRODUCTION. This is a useful exact
reformulation with an unpaid rate, not a universal obstruction or
successful filter. The next mathematical continuation can reuse the
unchanged review312 on this same assay. Its refined test is an analytic
dual construction paying C997a(7), including the closed-interval
residual and coefficient TV, rather than a larger sampled fit.
No all-measure stop, actual-Xi bound, candidate, or budget reset follows.
