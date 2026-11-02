# Nonuniform phase census — bounded attempt

Prepared STEP_ID: 2026-11-02-localized-logarithmic-research-05.
Reuse the unchanged invocation-start EXPLORE assessment
`literature/2026-11-02-localized-logarithmic-joint-moment.md`; its exact
paid-arc criterion is the only target of this turn.

Main gap: actual-Xi all-degree mixed positivity and unbounded-height
signs. Intermediate target: test an admissible nonuniform unit-residue
countersequence for the H-versus-D comparison. Downstream use of a
positive criterion would be L651's first-M moment/joint-projection bound.
Xi realization, matching upper bounds, signs and inherited audits remain.

Keep L649's n>=5, x=-5/4, R=11/8, eta=1/100, every t_j=j/n,
common distinct vertical poles within R-eta including x, positive integer
residues of total mass M<=n/3, conjugated denominator angle and normalized
means. Symmetric unit-residue support is a proposed construction, not a
consequence for the general family.

Test: construct a sequence for which 2H-log D+n/16 tends to minus
infinity, which would rule out every permitted arc by L658; otherwise
quantify the specific unpaid endpoint, sampling or spatial-mode cost and
stop this construction. A finite screen, another favorable special family,
or an unbounded remainder is not a counterexample.

Inspected L649's full definitions and exact deweighting stop, L658's full
localization proof, L659's envelope and resonant lattice proof, L660's
phase calculation, L651's hypotheses and response conclusions, and the
scoped logarithmic/monomial failure records. Reused the ready primary
source comparison. No new literature claim or source blocker is involved.

Unfinished construction saved before further reasoning: put
phi_n(y)=sum_j [atan(y/(d-t_j))+atan(t_j*y/(U-d*t_j))], d=5/4,
so W_(x+iy)(-1) has phase phi_n(y) continuous from zero. Consider
phi_n(y_l)=h*l with a fixed phase mesh h, symmetric integer l, and
all residues one. A mesh below the resonant 2*pi could avoid the
previous aligned phase, but the mass ceiling, analytic inverse-coordinate
range, both endpoints and all first-M spatial modes must still be paid.
No quadrature, suppression exponent or admissibility conclusion is yet
established. The candidate should first be tested for a deterministic
endpoint obstruction before attempting a growing-degree contour argument.

All inherited work is preserved. Initial notebook-scoped git status was
larger than the output budget; it showed extensive existing untracked work
and modified supplied overviews, which are not reset or discarded.

## Refined test saved before exact certification

Specialize the proposed census to n=6q+3 and phi_n(y_l)=pi*l,
-q<=l<=q, with all residues one. Place the contour endpoint at
phi_n(Y_n)=pi*n/6, halfway between adjacent phase nodes. The diagnostic
suggests Y_n tends to about .266; it has no error enclosure and is used
only to choose the rational test Y_n<27/100.

Use the exact rational phase function S_n(y)=exp(2i phi_n(y)) and
the residue-one kernel K_n(y)=2i phi_n'(y)/(S_n(y)-1). On the rectangle
Re(y)=+/-Y_n, Im(y)=+/-1/8 it should represent the entire spatial
polynomial, with no quadrature or omitted alias. On the endpoint segment
y=Y_n+i*s, |s|<=1/(100n), test |K_n|>=n/3 and
|W_(x+i*y)(1)|>=exp(-81n/6250-2). This would lower-bound the absolute
contour cost, not the signed response.

For comparison with the actual D, refine L659's single-factor envelope
using its exact quartic/Bernstein argument on a 128-piece radial grid.
The intended bound is |W_a(u)|<=exp(9n/500+3). Together with the
endpoint estimate, it would force the absolute-contour cost divided by
exp(-n/32)*sqrt(D) to grow at least c*n^(-1/2)*exp(29n/100000).
That would stop this absolute contour certificate for the half-turn
census, while leaving cancellation in its exact contour integral open.
No lower bound for H or counterexample is inferred from a contour norm.

The diagnostic is `scripts/one-sided-hankel/phase-census-diagnostic.json`.
It explicitly records missing error enclosures and computes neither the
finite-family response nor D. An optional mpmath availability check failed;
the diagnostic uses only Python's standard library. No source access or
mathematical conclusion depends on that missing package.

## Completed attempt and continuation

The complete result and proof are now canonical in
[L661](../lemmas/L661-phase-census-absolute-contour-endpoint-cost.md).
The initial .018 envelope target failed: its exact certificate rate was
about .01812066. That certificate is preserved. The final .0182 envelope
passes and leaves the strict normalized cost growth 9/100000. The separate
replay checks every quartic, cover cell, Bernstein coefficient and phase
row, not just the certificate's success flags. All final failures lists
are empty. Complete relevant comparison and replay-summary fields were
inspected with the shared JSON inspector.

Outcome: NEGATIVE for estimating this fixed contour by absolute values.
The lower bound is for a positive contour cost, not for the signed
response. It cannot be promoted to an H lower bound, a census
counterexample or a proof of the paid criterion. The full spatial
polynomial remains in the exact integral; no mode or alias is discarded.

Materially different continuation within the unchanged target: estimate
the signed contributions of both endpoints and the rest of the exact
contour. The first two spatial coefficients might avoid cancellation of
the two endpoint phases. To exclude this census as a countersequence,
a useful test is max(|c_0(1)|,|c_1(1)|)>=exp(-(81/6250+epsilon)n)
up to a polynomial factor, for one fixed 0<epsilon<9/100000, with all
remaining contour terms rigorously controlled. This bound is unproved;
the absolute-cost inequality does not imply it. Its passage to the full
spatial Mahler mean must retain coefficient/root costs using the ready
assessment's polynomial comparisons. A failure requires a quantitatively
different mechanism or support, not repetition of this absolute bound.

Essential inputs for that continuation are L649 and L657--L659/L661;
L651 with C645y/L650 remains downstream. Keep all original geometric,
integer-mass, full-grid and angular conventions. No signed endpoint
asymptotic, negligible interior remainder, all-angle suppression or Xi
realization has been assumed or established.
