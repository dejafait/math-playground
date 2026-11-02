# Full-action mass specialization — working checkpoint, step 59

Approved scope: the exact TARGET of the unchanged SPECIALIZE assessment
`drafts/literature/2026-11-02-full-action-positive-arc-mass.md`.
Main gap: actual-Xi all-degree mixed positivity. Intermediate target:
polynomial central-arc mass for the full norm-budgeted L666 action;
later attenuation comparisons, cone/H/support/Xi transfer remain open.

Use z=y/(9/20) on [-1,1] and Bernstein ellipse rho=3/2.
On its closure |z|<=13/12 and |Im z|<=5/12, so for
a=x+i*(9/20)*z, |a|>=17/16 and |a|<=139/80.
L666 (6), including j=0, then gives |W_a(u)|<=400^n:
each j>=1 factor is bounded by
36*(1161/105)=13932/35<400 and |x/a|<=20/17<400.
The full action is holomorphic on this fixed ellipse and bounded
by exp(7n)*n^C from normalized Cauchy--Schwarz.

Prospective completion: Trefethen 8.2 gives complex approximation
error epsilon=4*exp(-n) at degree
m=ceil((20+4*max(C,0))*n), using log(3/2)>2/5 and log n<=n.
Take the real trace polynomial p, then g=p+epsilon>=0,
g(0)>=1. Markov at its maximum gives integral g>=1/(4m^2).
If epsilon<=1/(32m^2), integral h>=1/(8m^2), where
h(z)=Re A(x+i*(9/20)*z). Angular density theta'(z)>1/2
then yields M_n>=1/(128m^2).
With D=21+4*max(C,0), m<=Dn; n>=ceil(128D^2)
should imply both the error condition and M_n>=n^(-3).

Before treating this as established: check holomorphy across all
removable quotient singularities, constants, complex-to-real transfer,
endpoint maximum, scaled Markov interval, and exact normalized mass.
No symmetry, exact degree, zero or stronger-domain sign is assumed.
Continue only if these checks pass; a failed estimate stops this
mechanism, not the full mass target. No mathematical script is needed.

Completed in `lemmas/L679-full-action-positive-central-arc-mass.md`.
The stated checks passed within this attempt; a separate independent
audit is pending. The final proof uses the slightly larger linear
degree displayed above to simplify all fixed-C constants. No action
existence or downstream attenuation comparison has been proved.
