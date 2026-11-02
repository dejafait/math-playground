# 2 November 2026 — full angular response and microscopic grouping

Invocation target: test the uniform rotation-averaged Hankel lower bound
at exponent 1/32 for the saved common-pole anchor-line family. The
unchanged EXPLORE assessment is
`drafts/literature/2026-11-02-rotation-averaged-anchor-line-hankel.md`.
This is one mathematical attempt, not a new source assessment.

Main gap: actual-Xi all-degree mixed positivity at unbounded heights.
Intermediate test: group ordinates at scale 1/n and control the complete
constant-input energy at c^2 exp(-n/16), or find an admissible obstruction
to a precise grouping inequality. A successful bound could supply the
synthetic detector; Xi layer isolation, remaining poles, census/clearance,
simultaneous realization, matching upper bounds and signs stay open.

Inputs read: C645g's normalization and symbol; C645n's pointwise anchor
rate; C645o's full signed energy and negative-entry warning; C645q's full
energy/rank comparison; L646's actual clustered-symbol lower bound and
exact-recovery stop. Scoped associated failure records were checked.
No repeated literature search is needed within the ready Fourier/residue
scope. The supplied overview and DAG were used without rereading them.

Keep n>=5, x=-5/4, R=11/8, eta=1/100, distinct common poles a=x+i*y,
|a|<=R-eta, x in Z, positive integer simple-pole residues, M<=n/3,
and the conjugated denominator angle. No separation or symmetry is
available. With u=i exp(i theta), retain

    W_a(u)=B_u(x)/B_u(a),
    q_u(zeta)=sum_a r_a W_a(u)/(R*zeta-a).

Initial unfinished test: before approximating a group by its center,
bound the phase change of W_a(u) along a segment of length 1/n.
The variation is of order n times the diameter, so simply asserting
that it tends to zero at this scale is invalid. Every within-group
and cross-group term must remain in the final comparison. Local
coherence alone is not a global lower bound. Continue only with a
uniform estimate, a proved obstruction, or a quantitative refinement;
an unevaluated block matrix or finite angular screen is insufficient.

## Preserved developing mechanism

The precise proposed shortcut is E_n >= c D_n, where E_n is the full
angular constant-input energy and D_n is the sum of the angular energies
of the 1/n ordinate groups, with a uniform c>0. Negative individual cross
entries alone do not refute this stronger inequality. The following
concentration construction is being checked; it is not yet a theorem.

Take a0=x+i/10000 and define the continuum logarithmic derivative

    L(a,u)=integral_0^1 [1/(a-t*u)+(t/u)/(R^2-t*a/u)] dt,
    F(u)=integral_0^1 log|b_(u,t)(x)/b_(u,t)(a0)| dt,
    z(u)=-i L(a0,u).

On the relevant vertical strip, the derivative in a of the integrand
has modulus <20. At a=x its real part is negative at every t and u;
the portion t<=1/4 supplies Re L(x,u)<=-1/16. Thus Im z(u)>1/32.
At u=i an explicit positive integral gives F(i)>1/10000000, while
F(1)<0. Real analyticity therefore gives a nonempty finite maximizer
set. These assertions and constants still need complete verification.

At each maximizer u_j choose an odd phase increment
h_j*Im z(u_j)=(2k_j+1)*pi, with h_j greater than the sum of earlier
h's plus 2. Then the positive-coefficient exponential product

    P(z)=product_j [1+exp(-h_j Re z(u_j))*exp(h_j z)]

vanishes at every angular maximizer. Its subset-sum offsets are more
than 2 apart, hence the associated poles a0+i*s/n occupy different
1/n bins. Rounding a common growing multiple of its positive
coefficients to positive integer residues can preserve M<=n/3.

Uniform logarithmic-derivative convergence should make the full
cluster response divided by its base response converge to P(z(u)).
The normalized angular mass of that base response concentrates on the
maximizers of F. This would give E_n/D_n -> 0, retaining every cross
term and treating the anchor separately. It would refute constant
block coercivity only; no upper bound at exp(-n/16) follows. Essential
remaining checks: uniform finite-product convergence, integer rounding,
pole admissibility, concentration, and the separate anchor term.

## Completed bounded test

The construction and every listed check are now proved in
[L647](../lemmas/L647-angular-cluster-block-coercivity-stop.md). In
particular the maximizer set is finite without a uniqueness assumption,
the integerized families obey the common-pole and census hypotheses,
and the separate anchor is bounded in the full Hilbert-space norm.
No signed term is deleted. The complete arithmetic record is
`scripts/one-sided-hankel/angular-cluster-coercivity-check.json`;
all 24 rational comparisons passed.

Outcome NEGATIVE: no uniform positive constant compares the full energy
from below with the summed 1/n-bin energies. The canonical proof also
shows both energies have the same positive exponential rate. Thus this
sequence cannot refute the detector; its relative loss is subexponential.
This is a method obstruction, author-checked but separately unaudited,
with no novelty claim beyond the scope of the saved source comparison.

The continuation retains the exact approved target and asks for an
exponential-loss comparison against the singleton diagonal, keeping
the full signed left side. That is a quantitative refinement justified
by this obstruction, not a repeat of constant block coercivity. Its
bound, effective constants and uniform onset are all unproved; no new
assessment was written and no continuation estimate was derived here.
