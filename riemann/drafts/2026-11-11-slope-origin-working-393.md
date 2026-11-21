# Slope-origin attempt — step393, work in progress

Approved target: Test slope-origin moment extraction from C997s's complete capped residual, using analytic propagation to c=0 and growing centered frequency moments, against the exp(-n/64) threshold.

Pre-invocation EXPLORE assessment: `drafts/literature/2026-11-11-slope-origin-moment-test-review-391.md`; the supplied complete text has been read. Source scope and comparison in review390 are reused. C997c's kernel and C997s's original objective were read; C997w/x remain respectively an uncapped construction and a prescribed-family cap stop. No cross-notebook input.

Main gap: L030-L032/C032a actual-Xi positivity, L966/L968 forcing and unpaid L984(H). Intermediate target: an all-admissible-coefficient lower bound for this fixed grid. A rate strictly below 1/64 would stop this capped bridge, not general band measures or RH. One fixed-domain test only; retain a weaker proved rate or precise blocker and park if it misses.

## Partial reasoning saved before the quantitative propagation work

Write h(t)=exp(i z_star t)-sum A_j exp(i gamma_j t), q(t)=g_n(t)h(t), and

    F(c)=c integral_n^(n+2) q(cu)du,
    D(c)=-exp(nc/4)R(c)/2=F(c)-F(1).

The fixed-parameter integral gives an entire F. If q(t)=sum q_k t^k, then

    [c^(k+1)]D=b_k q_k,
    b_k=((n+2)^(k+1)-n^(k+1))/(k+1)>=2 n^k.

Thus the c-independent lower window vanishes from every positive-order coefficient, exactly. The full kernel has not been replaced by pointwise spectral data. K_(n+2)(0)=g_n(0)=(n+4)/2 is nonzero. The desired centered moment is

    M=m! [t^m]{exp(-2it)q(t)/g_n(t)}/(i^m(z_star-2)^m),
    m=ceil(sqrt(n)).

Since |gamma_j-2|<=1/8 and |z_star-2|=sqrt(65)/8,

    |M|>=1-exp(sqrt(n))*65^(-m/2)>1/2.

Proposed local inversion estimate to check: on |t|<=1/(8(n+3)), the finite Laguerre expansion bounds K/K(0)-1 by 10/63; exp(-2it)/g_n(t) is then bounded by 16/(n+4). Together with Cauchy on |c|=1/n this should give

    |M|<=T_n sup_(|c|=1/n)|R(c)|,
    T_n=4 exp(1/4)(m+1)m! [8(n+3)]^m,
    log T_n=o(n).

The local estimate is now derived; its full proof is being placed in C997y. No division outside the small t disk is needed.

## Quantitative propagation and discriminating evidence

An explicit elementary propagation chain in the prescribed Omega gives alpha=2^(-17): first use the slit-disk Green function at center 2, radius 1/2, to reach |c-2|<=1/8 with exponent 1/2; then sixteen steps of length 1/8 use radii (1/8,1/4,1/2), losing a factor 1/2 each. For n>=8 this covers the entire |c|=1/n contour. The original-cap upper envelope is

    U_n=448 exp(20)/(n+1) * exp((81/8+log(2))*n+sqrt(n)).

Together these give the weak lower bound

    E_n >= (2 T_n)^(-131072) U_n^(-131071).

This has exponential cost 131071*(81/8+log(2)), far above 1/64. The propagation chain is not asserted optimal.

There is also a sharper *scope test* for using only a scalar global bound in this fixed disk. At A=0 the complete target response on the boundary point c=-1/2 has modulus >=7(n+4)exp(5n/8)/32 for n>=20. Its negative-t amplitude is positive after removing a phase lying in an arc of width 1; C997c's real-t bound controls the retained lower window. Continuity from inside Omega makes this an unavoidable floor for any uniform scalar prior. Separately, the analytic test polynomials ((c-2)/(5/2))^N force every generic power-propagation exponent to be <=log(5/4)/log(10). These are tests of the general analytic estimate, not residuals.

Consequently even a sharp scalar prior and generic power exponent have rate cost at least (5/8)*(log(10)/log(5/4)-1)>45/8, still above 1/64, when combined with the constructed subexponential extraction estimate. This does not rule out residual-specific, data-conditioned estimates or a different geometry. Both the explicit weaker bound and this precise scoped stop need independent conceptual audit. The fixed-domain scalar-prior certificate is parked after this one attempt; no claimed bound on the optimal E_n in the opposite direction, no general-band obstruction and no RH candidate.

Completed proof and qualifications are canonical in [C997y](../lemmas/C997y-slope-origin-extraction-and-scalar-propagation-stop.md). Ten exact rational germ diagnostics and all selected scalar checks passed; the full certificate is `scripts/adaptive-slope/slope-origin-check-393.json`. The original provisional reasoning above is retained as a work checkpoint, not a second full proof. The new audit scope is prepared for separate approval; no independent conceptual audit has yet occurred.
