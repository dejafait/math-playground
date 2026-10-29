# Step 502 — actual-map two-dimensional pencil obstruction

Invocation-start target and ready EXPLORE assessment are unchanged:
`drafts/literature/2026-10-25-four-row-finiteness-review.md`.
Main gap: uniform twelve-row exclusion. Intermediate target: universal
four-row finiteness under two designated disjoint pairs, or an explicit
infinite family. A finite locus could feed later-row gates; extraction of
a second disjoint pair and coding identification remain independent.

Unfinished reasoning saved before further work: use L160's normalized
K_t, t!=0,1. Divide coordinate r by P(r)=product over J of (r-y).
Then V_j=E^{I_j}+E(1/d_j(r))_r, d_j monic quadratic with roots K_j.
Write the four vectors x,y,x+y,x+t*y with generator coefficients
alpha,beta,gamma,delta. These coefficients are linear forms on K_t.
Each coordinate occurs in at most two I_j; overlaps occur only across
the two designated pairs. Total I-incidences=8 on seven coordinates.
If m is the number of overlapping coordinates, there are m-1 uncovered
coordinates and 8-2m singly covered coordinates, with 1<=m<=4.

Proposed contradiction to dim K_t=2: its coefficient projection to
(alpha,beta) is injective, so both are free coordinates. If all four
coefficients vanish then coordinate-wise two independent remaining
zero equations force x=y=0 (t!=0,1). If alpha=beta=0, x+y is coordinate
supported on I_a union I_b, while its nonzero gamma term would be
nonzero at a coordinate outside I_a union I_b union I_c (at most six
coordinates); hence gamma=0. Likewise delta=0. This proves injection
without discarding any zero coefficient vector.

For m>=2 choose uncovered r0. Its two equations determine gamma and
delta in terms of alpha,beta. At every other uncovered coordinate all
four normalized d_j values must agree. At a singly covered coordinate
of row j, all three other normalized d_i values must agree; this uses
t!=0,1. If m=4, three uncovered coordinates force all d_j equal.
If m=3, two uncovered coordinates put all four quadratics in one
2D evaluation pencil, and any singleton adds an independent evaluation
constraint forcing dimension<=1. If m=2, one uncovered coordinate:
a row with two singleton coordinates forces its other three d_i
proportional at three points, impossible. Otherwise overlap graph is a
matching; every row has one singleton. Each triple d_i is linearly
dependent, hence all four span a 2D pencil. Two singleton coordinates
then impose three-point evaluation proportionality, impossible.

For m=1 there is no uncovered coordinate. Relabel across the designated
pairs so the sole overlap is I_a intersect I_c. Then rows b,d each
have two singleton coordinates, rows a,c one each. Let
 gamma=u*alpha+v*beta, delta=w*alpha+z*beta.
At singleton d coordinates, u=d_c/d_a and v=d_c/d_b are nonzero.
Thus d_a,d_b,d_c span a common 2D evaluation pencil. At singleton b
coordinates, z/d_d=t*v/d_c, and
 w/d_d=t*u/d_c+(1-t)/d_a.
The first makes d_d/d_c=z/(t*v) a nonzero constant; the second makes
d_a/d_c a nonzero constant there. Hence d_a,d_c,d_d span another 2D
pencil, necessarily the same one. Its two independent quadratics would
have proportional evaluations on at least three distinct singleton
coordinates (two from b, two from d), impossible.

Still to check fully: overlapping-coordinate cardinalities and permissible
relabeling; every coefficient comparison at singleton types; independence
of distinct monic d_i; independence of two evaluation-ratio functionals
at three distinct coordinates; the m=2 triple-span argument; inherited
L160/L159 qualifications. No all-label census, fourth sample, mathematical
script or external retrieval is planned. Continue only if the full
contradiction survives; otherwise preserve the precise residual case.

Correction during the attempt: in the m=1 case the two singleton pairs
can be DIFFERENT fibers of a quadratic rational function. Proportional
evaluations within each pair do not make all four evaluations
proportional. Thus the proposed last contradiction was invalid and is
not a theorem. What does follow is that the common 2D polynomial pencil
contains the monic root polynomials of I_b and I_d: a nonzero pencil
element vanishing at the first point also vanishes at the second.
It also contains the four distinct d_j. Test the finitely many pencils
spanned by two disjoint S-pair polynomials (105 unordered choices),
retaining the full J-pair membership lists and exact cross products.
Threshold: every such pencil has fewer than four J-pair polynomials.
If met, m=1 is impossible. If not met, inspect only the surviving
pencils and retain this unresolved structural branch. This is not an
all-original-quadruple census or an additional sampled quadruple; it
checks an exact necessary obstruction produced by the structural proof.
No previous finite ranks or samples decide this certificate.

Completed bounded attempt: L161 proves dim K_t=2 impossible for m>=2
by comparing independent coefficient variables at uncovered and singleton
coordinates. For m=1 it proves all four d_j lie in the pencil generated
by the two singleton-pair root polynomials. The complete exact certificate
checks all 105 such S-pair pencils and all 3780 J-pair memberships, with
independent four-set coverage and affine-coefficient membership checks.
Maximum four J pairs meets, rather than misses, the necessary threshold.
Nine choices survive, representing exactly three constant-product
pencils h=8,12,22. All other eligible quadruples have at most five planes
using L159/L160, with their existing audit/input qualifications.

No surviving m=1 configuration was solved and no infinite family was
constructed. This is a partial structural ADVANCE, with the failed
stronger exclusion recorded separately in ATTEMPTS/051. Stop this turn
before further residual tests. Continue the same ready target by testing
the remaining equations on these three derived pencils, keeping all
assignments, possible shared-coordinate locations, zero coefficients,
exact ranks and distinctness. Do not promote the necessary pencil table
to realization or add arbitrary samples. No complete challenge candidate,
new source retrieval, source-level novelty or separate critical audit.
