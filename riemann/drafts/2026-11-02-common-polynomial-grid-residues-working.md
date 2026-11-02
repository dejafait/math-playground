# Common multiplicity polynomial and retained grid residues — bounded attempt

Prepared STEP_ID: 2026-11-02-common-polynomial-grid-residues-01.
One proof_attempt/creative under the unchanged ready EXPLORE assessment
`drafts/literature/2026-11-02-rotation-averaged-anchor-line-hankel.md`.
No new source gate or changed family is being introduced.

Main gap: actual-Xi all-degree mixed positivity at unbounded heights.
The intermediate target is the saved common-pole angular bound; the
bounded sufficient test is mean ||q_u||_2^2 >= c^2 exp(-n/16).
It could supply a synthetic detector, but Xi layer isolation, other
poles, census/clearance, simultaneous realization, a matching upper
bound and signs remain independent gaps.

Retain n>=5, x=-5/4, R=11/8, eta=1/100, t_j=j/n, common distinct
poles on Re(a)=x, |a|<=R-eta, the anchor x, positive integer simple
residues r_a and M=sum r_a<=n/3. Let P(z)=product (z-a)^(r_a).
Its coefficients need not be integers. Repeated polynomial zeros
still give simple poles in P'/P. No separation or symmetry is added.

Read C645g's exact spaces/scaling, C645o's angular product and residue
identities, C645n's stated rate bounds, C645x's qualified dual stop,
the prior audit's nominated polynomial test, and the corresponding
angular failure records. A scoped search in C645 corollaries and the
angular working records found no general retained-grid polynomial
estimate. This is not a novelty claim. The existing source assessment
and its named Fourier/residue imports are reused.

The calculation starts with T_u(z)=B_u(x) P'(z)/(P(z) B_u(z)).
Its Z-pole part is Q_u(z)=q_u(z/R). The other finite poles are the
rotated grid b_j=t_j u, with candidate residue
B_u(x)*(P'/P)(b_j)/B'_u(b_j). All of them, including b_0=0, must
remain. The behavior at infinity and any polynomial part must be
checked before using a partial-fraction identity.

Continue only with the required uniform bound, an informative
obstruction to this mechanism, or a quantitatively refined test.
A rational identity alone is not an advance. A small constant-input
energy alone would not refute the largest-operator-norm target.
Do not replace the degree constraint by coefficient integrality,
drop grid residues, or assume entrywise positivity.

This checkpoint saves the setup before extended calculation; no
unproved expression above is asserted as a completed result.

## Completed bounded attempt

The exact decomposition, polynomial identity and full orthogonal grid
energy are now canonical in C645y. The coefficient for grid index j
depends on the prefix through j, not on the later grid factors. This
permits a quantitative test of the natural degree-M simplification:
could the first M grid coefficients already suffice? C645t and the
exact nesting identity answer no, even if every coefficient through
ceil(n/2) is retained and the chosen prefix depends on angle.
The bound is 22000*m*exp(-7*n/200) on its admissible n=3m family,
with rate deficit 3/800 relative to exp(-n/32).

This is an informative local restriction obtained by specialization
of an existing audited bound, not a new angular lower bound or a
claim of progress beyond the sources checked. Raw grid sample norms
also keep C645n's insufficient rate lambda>47/1000; the exact inverse
Gram amplification remains essential. The polynomial's degree M has
not yet controlled that amplification or the later coefficients.
Do not count the polynomial identity alone as progress.

The exact finite certificate passes 35 aggregate checks and 41
prefix equalities in five rational cases, including oblique rotations
and repeated polynomial zeros. Its complete check fields were
inspected. These check normalization only; the uniform restriction
comes from the proof and the imported C645t bound. No external
source was added, and no angular quadrature was used.

## Refined continuation within the unchanged target

Let K_*=ceil(n/2) and use the R_j and v_j of C645y. Test the sufficient
tail bound

    mean_u |B_u(x)|^2 sum_(K_*<=j<n) v_j |R_j(u)|^2
        >= c^2 exp(-n/16)

uniformly in the original common-pole family, retaining the same
degree-M polynomial in identity (10). This is a proposal, not a
proved bound or an approval of new mathematics. It uses precisely
the coefficients that the initial-prefix restriction leaves open.
A family-dependent nonlinear use of the common polynomial is needed;
the fractional unit-pole dual and entrywise positivity are still
unavailable. An initial-prefix estimate or the unevaluated inverse
Gram formula would not pass the test. A small tail would refute this
sufficient test only, not the full constant-input or operator target.

The essential continuation inputs are C645g's spaces, C645n's anchor
rate and projection, C645t's admissible stop, and the new, separately
unaudited C645y identities. The latter must be used with their exact
prefix ordering and all signed sums. The unchanged ready assessment
covers Fourier/coefficient tests of the same family and threshold;
no new assessment is written. All actual-Xi bridges named above
remain unresolved. The sole current Next action is in PROGRESS.md.
