# Small-cluster cancellation — working record

Approved target: Test a three-pole unit-residue cluster for cancellation of the inverse-Blaschke residue sum on L645's unchanged logarithmic grid.

The supplied EXPLORE assessment is reused unchanged. Read L645 through
its exact complex-factor convention and the parent contour source review;
the scoped Pick/contour duplicate search found no earlier cluster proof.
C645a/C645b/C645c remain comparison stops, not inputs to a residue bound.
Existing notebook changes and unfinished work are preserved.

Main gap: actual-Xi signs/all-degree mixed positivity. Intermediate test:
an admissible cluster of at most three synthetic simple poles with unit
residues and exactly zero normalized inverse-Blaschke sum for unbounded
n, or a usable uniform positive lower bound. This tests only the proposed
derivative-free noncancellation shortcut. No actual zero realization,
contour identity, boundary norm, PSD or zero-separation premise is assumed.

Partial reasoning, not yet a result: at x=-d, the logarithmic derivative
of R(z-it)/(R^2+itz) is 1/(z-it)-it/(R^2+itz). Its real part is
-d(R^4-t^4)/((d^2+t^2)(R^4+d^2t^2))<0 for 0<=t<=1<R.
Thus the derivative of the product's local logarithm is of order n and
cannot vanish. A second pole at x+w/n could rotate the factor by pi.
The remaining check is exact solvability of that phase equation with a
uniform remainder estimate and every strict geometric condition retained.

Continue if this yields an exact root (not a floating-point near-zero)
for every sufficiently large n at fixed delta. Such a construction would
abandon the universal positive-residue noncancellation shortcut; it would
not refute a constrained actual-Xi detector or RH. Failure to control the
root and admissibility is EXPLORATION, not a theorem.

Completed disposition: the exact construction and full proof are now
canonical in C645d. The finite logarithmic derivative has a uniform
negative real part; an explicitly bounded contraction solves the phase
equation exactly for every n beyond the stated threshold. Every strict
cluster margin is retained. This is NEGATIVE for the universal
noncancellation shortcut and remains pending independent audit. No
numerical experiment or mathematical script was needed. The initial
partial reasoning above is preserved as such, not a second proof.
