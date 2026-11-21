# Pointwise source audit1188 — working checkpoint

Approved target: assessment1186 as separately approved1187; reproduce
only Polson v24 Lemma6.1's m(r)>=-6 and m(r)>1 for |r|>=20,
including its series and Binet constants. No audit verdict yet.

Main gap remains L030-L032/C032a actual-Xi all-polynomial positivity.
Use: remove one imported input in C030e. Explicit formula, heat-series
convergence, far-time estimates, theta signing and realization stay open.

The complete series subtraction must give a summable nonnegative
increment over m(0). Gauss p=1,q=4 gives the exact value at zero.
For z=1/4+ir/2, use principal log and split Binet at u=r/4.
Check the head denominator via its real part and the tail via its
nonzero imaginary part; check all four error budgets uniformly in r>=20.
Extend to negative r by the series' evenness. Include both endpoints.

L744(8)'s stronger 2/r^2 asymptotic bound is existing overlap, not
the requested independent audit of Polson's Binet constants. Reuse
C030e's elementary pi enclosures where necessary, without a dependency
cycle. Preserve all existing work and stops1117/1181.

Continue only with a complete analytic proof and strict scalar margins;
otherwise name the exact failed constant/hypothesis and C030e effect.
No numerical sample can establish the universal bounds.

Completed: C030f contains the full independent reproduction. Both
source bounds and all four Binet budgets pass, with m(20)>3241/3000.
All13 rational checks passed; every complete check object was inspected.
The source's stronger preexisting L744 tail estimate was not needed
as a premise. C030e now uses C030f and retains only its explicit-formula
and heat-series external imports. The initial notes above are preserved
as unfinished-work evidence, not a continuing uncertainty about the
completed two pointwise estimates.
