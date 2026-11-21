# Coupled compact-core attempt1289 — reasoning checkpoint

Ready target: unchanged review1288. No new literature or global domain theorem.
Let v(t)=Psi(t)(exp(-t/8),exp(t/8))^T. Linear combinations of the
unchanged column kernels give 2v=(1+c)a+b and 2tv=(1-c)a-b.
Compact-input Green calculus gives D k''+E k'+F k=0, where
D=p(y)I-P(x), E=p'(y)I-P'(x), F=Q(x)-q(y)I, t=x+y.
Subtracting t times the v equation from the tv equation gives
2D v'+E v=0. With p(y)=a y^2+b y, P(x)=M x^2+N x,
the x^2 coefficient is 2(aI-M)v'=0. Integrate and use v->0
to infer (aI-M)v=0; distinct exponential tilts span R^2, hence M=aI.
The x coefficient then reads ((2at+b)I+N)v'+2a v=0.
Thus (((2at+b)I+N)v)'=0; the full-theta value tail makes the
constant zero. Positivity p>0 gives a,b>=0, not both zero, so
2at+b>0 for t>0. Positivity P(x)>0 gives N positive semidefinite
by x->0+. Taking the inner product with nonzero v contradicts
(((2at+b)I+N)v)=0.

To finish: write the componentwise rectangular Green adaptation with
compact cutoffs, actions and brackets; check all polynomial coefficients
and degeneracies. No derivative-tail or spectral-domain input is used.
A completed proof will be canonical in C032i if the checks hold.

Completed1289: the action, cutoff, coefficient and degeneracy checks
are written in canonical C032i. The contradiction holds in the stated
class. Preserve this initial reasoning checkpoint as historical work;
the canonical proof supersedes its unfinished obligations. No separate
independent audit has been performed.
