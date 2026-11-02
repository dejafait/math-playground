# Fixed reciprocal-quadratic Stein model: calculation checkpoint

2026-10-31. Research under the unchanged startup SPECIALIZE assessment
`drafts/literature/2026-10-31-fixed-reciprocal-quadratic-stein-test.md`.

Main gap: actual-Xi signs at unbounded heights. This diagnostic can only
decide whether the one prescribed model refutes the generic monotone-Stein
first-sign implication. Existing C233b and L604 stops are preserved.

Reconstruction in progress: put Q(u)=u^2/2+u^4/4. Solving
(tau p)'=-u p with tau=1/(1+u^2) gives
p(u)=C(1+u^2)exp(-Q(u)). Here C is the positive normalizing constant.
Directly, integral_u^infinity v p(v)dv=C exp(-Q(u)) at both signs of u,
so the required tail ratio is realized, rather than inferred from a
representation theorem alone. Every density derivative is polynomial
times exp(-Q), giving all original rapid-decay hypotheses.

Prospective Newman application: choose the finite-class measure
rho(du)=C(1+u^2)exp(-u^4/4+u^2/2)du and damping b=1. Parameters in
the reviewed convention are m=0, a=1/4, beta=-1/2, N=1, a_1=1.
Then exp(-b u^2)rho(du)=p(u)du. No zero-damping limit is needed.

Remaining check before canonical completion: obtain growth order at most
4/3 by a quartic Young bound; use named Hadamard factorization, real
zeros, evenness and F(0)=1 to obtain the paired genus-zero product in
z^2. Then the paired logarithmic derivative gives the nonnegative first
Laguerre form off the real zeros; continuity covers the zeros.
This is a specialization/reproduction of known mathematics, not a new
generic Stein theorem. If all checks pass, terminate the negative scan.

Completed 2026-11-01: canonical L606 contains the remaining checks,
including the explicit quartic maximum, Hadamard pairing and treatment
of zeros. The known-class match succeeds; the fixed negative search
is closed. This checkpoint is retained as reasoning saved during the
attempt; the completed proof is canonical in L606.
