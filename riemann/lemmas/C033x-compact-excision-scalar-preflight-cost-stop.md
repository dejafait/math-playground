# Corollary C033x: compact-excision scalar preflight cost stop

## Hypotheses

Use C033m's exact residual transform m(s), its finite compact-excision
evaluator in Sections2-3, and its prescribed Section5 allocation at
scalar tolerance epsilon in {2^-8,2^-16,2^-32,2^-64}. Thus the compact
exponent tolerance is beta=epsilon/4. The prescribed sufficient
allowances are

    K_s/(192*n^2)<beta/3, d<beta/3=epsilon/12,
    K_s=42*s^2+326*s+1915/2, s in {1,2}.

Use precisely the D=0 profile approximation C033m(7): cutoffs
0<u<=1, A>=1, integer J>=1, all four nonnegative error allowances,
and the literal J-node midpoint evaluation. A total operational cap
of 10^6 scalar/node/prime-power terms is fixed for the eight-entry
C033w interpolation screen. Sharing nodes between profiles cannot
reduce the number below J for even one literal profile evaluation.
Compressed sums, new estimates, correlations, reallocated budgets,
and different evaluators are outside the statement.

Retain C033m's qualified actual divisor, conjugation and multiplicity,
excluded ordinate zero, strict strip/gamma>14, counting, verified
through100 and retained-real-zero, reciprocal-square-tail, heat
positivity and separate fixed-j errors, both fixed-v1 qualifications,
zero drift/killing and Gaussian half-variance wherever interpreting
the exact residual and laws. No source-wide preprint or zero-data
verification is supplied. The cost inequality below only uses the
displayed numerical allowances and elementary real inequalities.

## Conclusion

Every such prescribed compact evaluation necessarily has

    J>27*(1-4*epsilon/3)^2/(128*epsilon^3).             (1)

Already at epsilon=2^-8, (1) is J>3,502,176>10^6. Each finer
trial also exceeds the entire cap. Consequently the approved bounded
screen stops before computing the two residual entries, independently
of the six kernel entries, primitive evaluation, coefficient arithmetic,
conditioning or solving. No actual scalar, nonsingularity or TV bound
has been certified. The fixed-three-width interpolant remains undecided.

This is a local implementation-specific negative result under ready
SPECIALIZE assessment1796/approval1797, recorded19 November2026.
It is not a lower bound on actual quadrature error, actual entry cost
under other methods, d_S, d_2 or feasible total variation, and proves
neither singularity nor absence of interpolation. C033m's analytic
effectivity and the earlier C032x/common-disk stop remain intact.

## Proof

Reuse C033m(5)-(9) and its audit1755 without reproving their explicit
formula, differentiation or midpoint inputs. In particular the primary
quadrature source is Erik Talvila and Matthew Wiersma, *Simple derivation
of basic quadrature formulas*, arXiv:1202.0249v1, Section1(1.1) and
composite rule p2, Section4 p8,
https://arxiv.org/pdf/1202.0249v1 . C033m's evaluated profile interface
uses Alain Connes, *Heat Expansion and Zeta*, arXiv:2402.13082v1,
Section2(4)-(9), printed p4,
https://alainconnes.org/wp-content/uploads/heat-zeta.pdf . These known
inputs are imported through their already audited specializations;
only the instance-specific allowance comparison is performed here.
No verified linear-solve theorem is applied because its inputs are
unavailable. This is not a replay of C032x's common-disk argument.

C033m(7) gives, using pi<4,

    d>=d_small=(u^2+u/2)/(2*pi)>u/16.

Hence d<epsilon/12 requires u<c:=4*epsilon/3. Each trial has
0<c<=1/192<1. To bound the stated quadrature allowance, retain only
the positive 2*coth(u) term in its bracket:

    L=exp(A/2)/(2*u)*[4*A+1/2+2*(1/2+coth(u))]
      >coth(u)/u>1/u^2.

For completeness, u*cosh(u)-sinh(u) vanishes at zero and has
derivative u*sinh(u)>0 for u>0. Division by u*sinh(u)>0 proves
coth(u)>1/u. Also A-u>=1-u>1-c>0. Therefore

    d_quad=L*(A-u)^2/(8*pi*J)
      >(1-c)^2/(32*J*c^2)
       =9*(1-4*epsilon/3)^2/(512*J*epsilon^2).

All omitted error allowances are nonnegative. The necessary
d_quad<=d<epsilon/12 rearranges to (1), with positive denominators
throughout. This is deliberately weaker than C033m's additional
per-component quarter-budget choices; imposing those can only increase
the cost.

At epsilon=1/256 the exact right side is

    (27*2^24/128)*(191/192)^2=96*191^2=3,502,176.

For smaller positive epsilon<=1/256, both 1-4*epsilon/3 and
epsilon^-3 increase, so their positive product cannot decrease.
Thus even a single literal J-node profile needs at least3,502,177
nodes, exceeding the entire cap before its arithmetic or prime terms.
One need not allocate or execute that quadrature to reject its budget.
The complete four rational comparisons are saved by
`python3 scripts/smoothed-law/two_observation_compact_cost_1798.py` in
`scripts/smoothed-law/two_observation_compact_cost_1798.json`.

As a second comparison, the prescribed outer quadrature requires
n^2>K_s/(16*epsilon). At epsilon=2^-8 this gives n>=146 for s=1
and n>=169 for s=2 (K_1=2651/2, K_2=3555/2).
The script checks both minimal integers at all four radii using
exact rational comparisons and records n times the minimum J for
literal nested evaluation. This larger count is not needed for the
stop and is not imposed on a method sharing node work across widths.

No entries were evaluated. Consequently no condition estimate, exact
weights, residual or variation conclusion follows. In particular this
cost failure does not change C033w's minimax theorem or the possibility
of d_{ {1,2} }=0. RH, full interval control, cancellation, signed
height and actual-Xi realization remain open. A different evaluator
needs its own separate source-scope review before further research.

## Mathlib

Full matching coverage is unchecked and unknown. The proof uses the
already cited effective evaluator and elementary real inequalities;
the script verifies rational arithmetic only. No formal verification
or new general theorem beyond the checked source tools is claimed.
