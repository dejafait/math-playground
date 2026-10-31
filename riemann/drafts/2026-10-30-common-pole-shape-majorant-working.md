# Fixed-symbol shape attempt: saved reasoning

The approved target is the real-even smooth unit class on (-1,1),
with K=(e exp(2it)-1)/(1+2it) and dm=dt/(2pi).
No trace extension is assumed. L526/L527 are motivation only.

Put a+ib=(e exp(2it)-1)/|e exp(2it)-1|. Then the symbol is
(a+2tb)/sqrt(1+4t^2). A periodic majorant is m=1 where a>=0,
and m=|b| elsewhere: Cauchy--Schwarz proves the first case;
dropping the negative a term proves the second.

Fourier-series Parseval on (-1,1), applied to h(x)exp(-itx),
gives sum_k |H(t+k pi)|^2=2. Thus the expectation of any bounded
nonnegative pi-periodic multiplier is its period mean. No finite
section, spectral isolation or discarded sector is needed.

Writing theta_0=arccos(1/e), the mean is
(theta_0+e+1-sqrt(e^2-1))/pi. Candidate exact upper certificate:
theta_0<5/4, e+1-sqrt(e^2-1)<6/5, pi>47/15. Hence the mean
is <147/188<47/60<pi/4, with rational gap 1/705.

The pi bound follows from atan(1/2)+atan(1/3)=pi/4 and alternating
lower polynomials: their sum is 284663/362880, exceeding 47/60
by 407/362880. The cosine upper polynomial at 5/4 is
1969/6144<1/3<1/e. Use 8/3<e<3 from its series.

This is a uniform obstruction for this fixed functional, not an
evaluation of its supremum and not an obstruction for variable
symbols/supports, collective forms or RH. Canonical proof and a
separate later audit are required before treating the stop as audited.

Non-load-bearing numerical discovery record: a NumPy midpoint scan
used 100000 s-nodes in (0,pi/2), with the limiting b(s) baseline and
the 50 positive translates s+k pi, k=0,...,49. Its sampled envelope
mean was 0.7498815960518146. The looser continuous-direction envelope
1 where a>0 and b otherwise had sampled mean 0.7590711737210128.
These floating-point diagnostics had no error certification and do
not establish any threshold. They motivated the exact periodic
majorant now proved in L528; all load-bearing rational checks are
saved in its certificate. No numerical optimization or finite-space
spectral conclusion is used.
