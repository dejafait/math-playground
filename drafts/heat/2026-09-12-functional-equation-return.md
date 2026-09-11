# Functional-equation return checkpoint — 2026-09-12

Draft claims, initially unproved. Put g(v)=exp(-v²/4)/(2sqrt(pi)),
chi(z)=2(2pi)^(z-1)sin(pi z/2)Gamma(1-z), Q=tau/(2pi).
Functional equation in L145 should give an absolutely convergent sum of
integrals with nth factor n^(-2+i tau) and integrand
 g(v) chi(-1+i(tau+v)) exp(iv log(An)).
The candidate local multiplier is
 chi(-1+i(tau+v)) = X(tau) exp(-iv log Q)
 (1+O((1+v²)/tau)), |v|<=tau^(1/4),
 X(tau)=Q^(3/2)exp(i[tau(1-log Q)+pi/4]).
Gaussian integration should return X(tau) times
 sum n^(-2+i tau)exp(-log²(nA/Q)) with O(sqrt(tau)) error.
On the L144 scale A=Q/N this sum is exactly S/C, and X=1/B.
Resume by checking the Stirling phase, all tails, absolute Fubini majorant,
and the error after multiplying by CB. No draft claim is a DAG input.

Completed in L146: exact interchange, local phase and amplitude, tail bounds,
and return to S/C are proved. The resulting error is coarser than L144's
existing comparison. No lower bound was proved or promoted.
