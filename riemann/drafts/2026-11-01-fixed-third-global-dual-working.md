# Fixed one-third census: global dual working record

Started 2026-11-01 under the unchanged invocation-start EXPLORE
assessment `drafts/literature/2026-11-01-fixed-third-census-hankel.md`.
One mathematical attempt; this file initially checkpoints unfinished
reasoning, not a theorem or a successful lower bound.

The main gap is actual-Xi all-degree mixed positivity. The exact
intermediate target is the uniform lower bound c exp(-n/32) for
C645g's symbol at delta=1/4, eta=1/100, R=11/8, x=-5/4,
n>=5, M=sum r_a<=n/3. Poles are distinct, grid-avoiding, in
|a|<=R-eta and contain x; residues r_a are positive integers.
No separation, simplicity of the underlying zero, one-sided support,
or actual-Xi realization is assumed. Spaces and circle measure are
exactly C645g's. A positive result could bridge C645j's coefficient
at this displacement to the C645h residual mechanism; clearance,
realization, a useful independent upper bound, other displacements,
and signs would remain open.

Read C645g's complete proof through (21), the C645i full-boundary
quadrature and product estimates (9)--(23), C645h's assumptions and
conclusion, and C645j's count-envelope statement. Reused the ready
primary operator/residue coverage. The local duplicate/failure check
included the sparse proof history and the one-sided C=10 stop.
The audited small-census theorem and C=10 counterfamily are comparisons;
neither establishes this target.

Bounded test: seek a global Hardy dual coupling the full positive
residue census to the exact grid product. Keep complex inverse-grid
weights throughout. A uniform position-independent c and onset proves
the target; an admissible sequence with exp(n/32)||H_q|| tending to
zero refutes it. A failed dual, scalar cancellation, finite experiment,
or small least singular value is inconclusive. Preserve partial
reasoning and require a refined mechanism before repeating an
unsuccessful attempt. No additional literature search is needed for
the covered elementary residue/Hardy tools.

## Saved refinement during the attempt

The global-dual target must survive a full-boundary circle census.
C645i's separate numerator/denominator estimates are too costly at
n/3, but the exact logarithmic derivative combines them:

    b_t'(v)/b_t(v)=(R^2-t^2)/[(v-it)(R^2+itv)].

Candidate parameters, still unchecked at this checkpoint:
u=523/400, c=-u, r=23/400, s=67/1000, n=3m, m>=8,
a_k=c+r exp(2 pi i k/m), all original residues one. Then a_0=x
and u+r=R-eta. The auxiliary disk |v-c|<=s has negative real
part and lies strictly inside the physical disk.

For this disk, the combined derivative may bound the full reciprocal
grid cost by

    log |B_n(c)/B_n(c+w)|
      <= s/[(u-s)(R^2-s)] * sum_j (R^2-t_j^2)
      <= gamma n + K,
    gamma=s(R^2-1/3)/[(u-s)(R^2-s)],
    K=s/[2(u-s)(R^2-s)].

The intended rational thresholds are gamma<7/150 and K<1/50.
For m=n/3, (r/s)^m=(115/134)^m<=exp(-19n/402), leaving
19/402-7/150=1/1675. The separate product gain is to be bounded
using C645i's real derivative formula at the new u,R; an average
greater than 11/20 would give |B_n(x)/B_n(c)|<=exp(-253n/8000),
strictly faster than exp(-n/32). These arithmetic and uniformity
claims are not yet certified here. If they hold, the exact residue
quadrature controls the whole boundary and defeats any universal
dual at the approved census; this remains the same target/test.

## Completed outcome

The refined full-boundary test succeeds as a counterfamily. The full
proof, hypotheses, exact constants, source qualifications and Mathlib
status are canonical in C645k. All intended rational thresholds above
passed; the resulting operator upper bound is
2700 n exp(-253 n/8000) along n=3m, m>=8. Its rate exceeds the
target 1/32 by 3/8000. The exact-rational certificate is
`scripts/one-sided-hankel/fixed-third-counterfamily-check.json`.

This provides an informative NEGATIVE for the approved universal
lower-bound target and hence prevents any uniform global dual from
proving it under just those hypotheses. It is a sharper application
of the circle mechanism, not a new general Hardy theorem or a
certified originality claim. No scalar cancellation or finite
spectral observation is used as a substitute for the norm bound.
A separate conceptual audit of C645k is the sole next action, using
the unchanged assessment and exact target. Actual-Xi realization and
signs remain unresolved. Earlier partial checkpoints above are kept
as unfinished-at-the-time reasoning, not separate results.
