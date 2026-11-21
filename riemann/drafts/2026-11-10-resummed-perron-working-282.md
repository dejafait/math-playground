# Resummed Perron-Cauchy construction — working record, step282

10 November 2026. One RESEARCH attempt under unchanged approved
`literature/2026-11-10-resummed-perron-cauchy-construction-review-280.md`.
Expected classification REPRODUCTION. No external search or new source
is needed: reuse review279's inspected Montgomery–Vaughan and DLMF
contracts and L985/L989's exact normalization. Preserve stop244 and
working271. No cross-notebook input.

Main gap: L030-L032/C032a actual-Xi positivity and L966/L968 signed
forcing. Target: the exact G_1,G_2 in review280, with an explicit
degree-resummed kernel, all four endpoint jumps, continuum compensators
and a locally uniform symmetric Perron-height limit. A later signed
singularity test is a plausible use; it is not authorized in this step.
Continue if these requirements hold on a nonzero disk. Otherwise save
the specific failed estimate, without a general impossibility claim.

## Saved partial reasoning before the uniform-limit proof

Try rho=1/4, |w|=rho, a(w)=1/(1-w), b(w)=a(w)-1 and Perron
Re(s)=1. Then 4/5<=Re(a(w))<=4/3. The absolute Dirichlet majorant
is sum_(q>=2) log(q)/q^(9/5), finite and independent of w. Retain
the -1 in K_m by the second Cauchy factor (1-w)^(-1).

Set S_1(v)=-log(1-v)-v and
S_2(v)=(-log(1-v)-v-v^2/2)/v, with removable value at zero.
Candidate summed endpoint kernel:

    H_r(w,s,z)=w^(-r)*[(exp(2*r*s)-1)*S_r(z*exp(2*s)/w)
                       -(exp(r*s)-1)*S_r(z*exp(s)/w)].

This sums 1/(n+r-1), n>=2, and all four affine endpoints. Candidate
arithmetic integrand is H_r/s times

    (1-w)^(-3)*(-zeta'/zeta)(s+a(w))
                  -(1-w)^(-1)*(-zeta'/zeta)(s+1).

The proposed disk is |z|<rho*exp(-2). Work first at finite degree
and finite height. For fixed endpoint x, the imported near error is a
finite sum over x/2<q<2*x, q!=x, weighted by
log(q)*q^(-4/5)*min(1,x/(H*|x-q|)); its supremum in w tends to zero.
Its height-independent bound is at most
2^(9/5)*x^(1/5)*log(2*x). The far error is at most
(4+x)*sum log(q)/q^(9/5)/H. These are candidate summable bounds on
the proposed disk after coefficient extraction; the proof and constants
still need checking. No assertion of absolute infinite-height convergence.

Remaining work within this attempt: check these bounds and Cauchy factors;
write the exact full-jump correction and an explicitly summed continuum
term; prove local uniform convergence and holomorphy; audit all signs and
small-degree normalizations. No spectral deformation or zero-sum exchange.

## Completed attempt

The construction and full proof are now canonical in
[L994](../lemmas/L994-resummed-perron-cauchy-moving-band-germs.md).
The proposed disk and logarithmic kernel pass. The near endpoint sum
has a finite head tending to zero; the degree tail has a common geometric
majorant independent of height. The exact continuum term includes
-r*S_r(z), and all four half-jump corrections are retained. No mathematical
script or numerical preview is used as proof. This is local ADVANCE by
REPRODUCTION, with independent conceptual audit pending; it supplies
neither a signed bound nor zero-sensitive continuation. All originally
listed independent gaps and prior stop evidence remain unchanged.
