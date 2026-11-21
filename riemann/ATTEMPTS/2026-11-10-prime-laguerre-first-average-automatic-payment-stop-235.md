# Automatic first-order degree-average payment — stop, step235

10 November2026. The approved test is settled by the quantitative
application in [L982](../lemmas/L982-fixed-index-prime-laguerre-identification.md),
using L981 and Ross arXiv2210.08091v1 Proposition3.4 p7. This is
REPRODUCTION, not a new estimate beyond the inspected sources.

WHY IT FAILS: At X_n=exp(10000*(n+1)^4), the average of P_k(X_n)
differs from the average of P_k(X_k) by at most T/(n-1), where
T<=2*exp(-630). The exact moving-cutoff inverse has error at most
2T and costs only a linear factor in n. Both directions preserve
the every-epsilon two-sided subexponential threshold. None of the
imported results supplies an independent bound for the average,
so first-order smoothing alone has not paid the arithmetic head.
This stops only automatic payment for this average and threshold;
it is not an obstruction to independently established average bounds,
other orders or one-sided hypotheses. L983's different lobe-sign
stop remains unchanged. The new application awaits separate audit.
