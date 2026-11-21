# Fixed-grid full-cut calculation, step166 (working)

Approved target: determine L905's full four-demand cut at x=16,y=0,
M=128, total degree two, without refinement. Reuse the unchanged
SPECIALIZE assessment `literature/2026-11-09-hall-full-cut-taylor-enclosure.md`.
The main gap is actual-Xi all-degree mixed positivity. This cut can reject
nearest-neighbor allocation or remove one finite obstruction only.

Plan retained before implementation: use full K=4W, even and holomorphic
by L908/L910; evaluate full derivatives at lattice centers through order
two with finite theta heads plus complete derivative tails. On each
rectangle integrate the quadratic amplitude against 2t^2 cos(16q).
Use the full analytic kernel for the remainder, including seam cells.
Cauchy radius 1/4 and L910's envelope permit a uniform derivative bound;
all effective constants and weighted moments still require verification.
L905's complete spatial tail and positive A0 can be reused unchanged.

Stop after this one enclosure: negative upper endpoint rejects the rule;
nonnegative lower endpoint passes only this cut; zero-containing interval
ends the test. No grid/degree campaign. No sign has yet been certified.

Potential coefficient-tail bound being checked: differentiating
P0=8v^2-12v by P -> 2vP'+(1/2-2v)P gives
P2=32v^4-224v^3+330v^2-75v. For v>=3 its absolute value is <147v^4.
This yields a uniform n>=5 tail <=30000000000 exp(-75), subject to
the decreasing-exponent and geometric-ratio verification in the final
canonical calculation. Existing value/first-derivative tails remain
160000 exp(-75), 80000000 exp(-75). These are application estimates,
not a claim that the reflected finite head is smooth.

Inputs: L036/L037, L312, L898, L905, normalization part of L908,
analytic-even envelope of L910. Full certificate, proof and outcome
remain unfinished at this checkpoint. Other cuts, lobes/heights,
infinite allocation/residual and mixed positivity remain independent.

Completed: the one fixed-grid enclosure gives
0.0000159908498950 < A0 H(F) < 0.0000261476291328, strictly positive.
Full proof, effective constants and qualifications now live canonically
in L912. Full certificates are `scripts/theta-marginal/full-cut-taylor-166.json`
and `scripts/theta-marginal/full-cut-taylor-checks-166.json` (paths relative
to the notebook). The latter's 16949 checks have no failures; it checks
all stored moment arrays and exact aggregate scaling, not independent
center-jet recomputation or full cell replay. Separate critical audit
is the nominated continuation. No mesh or degree increase occurred.
