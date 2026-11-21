# Laplace prefix attempt1839 — working checkpoint

Completed: the full proof is now canonical in
[C034b](../lemmas/C034b-laplace-width-first-prefix-and-second-prefix-gap.md).
The unfinished notes below are preserved as the interruption checkpoint;
the canonical result supersedes their provisional wording.

Approved target: assessment1838's single analytic all-prefix test for
(1,k(1,sigma),k(2,sigma)) on [1,2]. No grid refinement, scalar evaluator,
new divisor, or odd-kernel sign transfer. Source comparison1838 is reused.

The full C032n proof through its normalized evolution was inspected,
along with C033w/l's exact hypotheses, C033k's second-width regularity
argument and stop1746. Local C032/C033/C034 searches found no existing
sign conclusion for these Laplace prefixes. C033m already contains
second-width Gaussian regularity; regularity alone is not a new sign
input. All source and divisor qualifications remain in force.

Unfinished reasoning saved before further estimates: C032n states C^1
width dependence of every fixed complex derivative. Its identity
dot b(w)=-b''(w)+b''(0) can therefore be differentiated once more:
ddot b(w)=b''''(w)-b''''(0). This gives C^2 width dependence without
differentiating a bound or repeating the spatial-integral proof.
For w_j=sqrt(j), set q_j=b''(w_j)-b''(0) and
r_j=-b''''(w_j)+b''''(0). Then dot k_j=k_j*q_j and
ddot k_j=k_j*(q_j^2+r_j). The candidate final prefix factor is
q_1*q_2*(q_2-q_1)+q_1*r_2-q_2*r_1. Signs remain unproved.

Next within this attempt: retain the origin subtraction explicitly in
the real spatial integral, test whether the available full-divisor
majorants separate either prefix from zero, and stop if they do not.
The candidate first-prefix estimate now has a full-divisor mechanism.
Writing h_rho(x)=Re((G_sigma(x-z_rho)+G_sigma(x+z_rho))/2), the exact
normalized first derivative has weight
Q_s(x)=4*s*(3*x^2+s)/(x^2*(x^2+s)^2) against h_rho(x)-h_rho(0).
For s=1,2 the positive core [gamma-1,gamma+1] contributes more than
(31/32)*s/gamma^4. Each translate's entire possible negative-phase
part on x>=1 costs less than (9/40)*s/gamma^4. The origin interval
costs less than (2/125)*s/gamma^4; the constant subtraction costs
less than s/(10000*gamma^4). Their net coefficient is
31/32-9/20-2/125-1/10000=10053/20000>1/2.

These are analytic candidate estimates, not a numerical certificate.
The exact weighted-Gaussian inequality and every exchange must be
written in the canonical result before accepting the partial bound.
The second prefix still has the unsigned correlation
d1*e2-d2*e1, where dj=dot b(sqrt(j)), ej=ddot b(sqrt(j)).
No sign for it follows from the candidate first-prefix margin.
