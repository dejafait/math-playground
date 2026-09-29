# Counting-compatible first-sign model — construction note, 2026-09-27

This preliminary reasoning is retained after completion. The full
proof is [L354](../lemmas/L354-count-and-gap-data-do-not-force-first-laguerre-sign.md);
the prospective checks below have all been discharged there.

The exact target has the saved SPECIALIZE assessment in
[the source review](literature/2026-09-27-count-preserving-laguerre-model.md).
The known canonical-product and reciprocal-square theorems will be
cited; this step checks their simultaneous application only.

Candidate construction: let M(t)=t log(t/(2π))/(2π)−t/(2π) on
t≥2πe, and define t_n by M(t_n)=n for n≥1. Use the paired product
H(z)=∏_n(1−z²/t_n²). Choose consecutive t_m,t_(m+1)>40 and their
midpoint A, so H(A)≠0. The real-zero reciprocal-square sum S_A
is finite. Insert the even normalized quartet factor
[((z−A)²+b²)((z+A)²+b²)]/(A²+b²)² with
b=(S_A+16)^(-1/2).

Checks still to finish in the canonical proof: counting with positive
real part, eventual gap bound from M', exponent of convergence and
canonical genus, exact zeros, and the uniform reflected-pair bound.
The anticipated normalized first sign is S_A−2/b²+R_b, with
0<R_b<1/(2A²). That bound must be checked without freezing R_b
while changing b. No actual-zeta assertion follows from the model.

The discriminating test is a model satisfying every saved requirement.
Success stops only count/gap data as a sufficient first-sign argument;
failure must identify a genuine incompatibility, rather than infer
positivity for Ξ. This is the third turn in the inherited exploration
budget, which must end with a construction or a completed stop decision.

Completion: the count is floor(M(T))+2 times the indicator of T≥A,
so its remainder is O(1). The gap bound and genus-one hypotheses
hold, and the reflected contribution is uniformly below 1/(2A²).
The chosen b yields D_1(F;A)/F(A)²<−31. This is an informative
negative result for the proposed coarse-data certificate, obtained
by a classical specialization, with no actual-zeta sign conclusion.
