# Joint full-grid polynomial dual — completed source comparison

TARGET: Test the joint full-grid space D_(u,M)={P_+(b_u J s): deg s<M} for mean_u ||Proj_D F_u||^2>=c exp(-n/16)D_single,n in L649's unchanged integer-mass family.
CHECKED: 2026-11-02
DECISION: EXPLORE
SEARCH_EVIDENCE: Reused the full-grid-polynomial-dual, full-grid-markov-remainder and rotation-averaged-anchor-line-hankel assessments; searched finite Blaschke/Hankel polynomial subspaces, model-space angles, smallest singular values and positive-residue logarithmic derivatives. Inspected the primary results below, including the September 2026 Blaschke-approximation sequel. No matching uniform joint-projection theorem was identified; bounded coverage is not a novelty claim.
SOURCE_EVIDENCE: Direct PDFs inspected 2026-11-02: https://arxiv.org/pdf/1501.01161v2 Theorem 4 and proof p.9, Section 5.2/(24)--(27) pp.10--11, Theorem 7 and proof/(57)--(61) pp.18--19; https://arxiv.org/pdf/1104.5358v1 (C1)--(C2), Theorem 3.1 pp.7--8, Lemma 6.2 and proof of Theorem 3.1 pp.18--21; https://arxiv.org/pdf/2603.16295v2 Theorem 3/(35),(37),(43)--(51) pp.13--17 and Proposition 1/(52)--(55) with proof pp.21--22. Page numbers are printed. Prior inspected projection, Parseval, residue and Markov comparisons are reused, not newly audited.
COMPARISON: Finite rational model-space formulas and lower approximation bounds do not evaluate this prescribed joint range on F_u. Fixed-symbol Nehari convergence has extra maximizing-vector hypotheses and problem-dependent constants. The 2026 degree-explicit theorem concerns approximation of a Blaschke product; no identification with this weighted projection is supplied. L650's close-pair sum survives, so its separate-column stop does not settle the joint target.
GAP: Bound mean_u ||Proj_D F_u||^2 relative to the exact D_single,n at squared rate 1/16, with a positive constant and onset uniform over n-dependent integer families, or give a full admissible obstruction. The joint Gram cost and its relation to the correlated response remain unevaluated.
REASON: Essential source comparison for the unchanged joint target is complete enough for one bounded finite-algebra attempt. Known results supply tools but no matching estimate; a joint combination can retain cancellation discarded by separate normalization. This is source readiness only, not proof or mathematical approval in this literature turn; the newly changed assessment receives separate approval next turn.
LITERATURE_REASON: The invocation-start REVIEW_REQUIRED target replaces a single normalized column by its whole polynomial image; prior coverage did not assess that quantitative subspace claim. The new 2603.16295v2 lead was checked because it gives degree-explicit Blaschke bounds.
SCOPE: Exactly the saved joint-projection target below, retaining its full Gram form, complete grid, angular mean and integer family. One proof attempt, full admissible countersequence, or quantitatively bounded remaining cost using finite Hardy/projection/residue/polynomial algebra is covered. No new general approximation theorem, grid prefix, separate-column replacement, fractional-mass relaxation, separation assumption or Xi conclusion is approved.

## Exact proposed calculation

Retain n>=5, x=-5/4, R=11/8, eta=1/100, t_j=j/n, common distinct
Re(a)=x poles with |a|<=R-eta and x in Z, positive integer original
simple-pole residues r_a, and M=sum r_a<=n/3. Keep the multiplicity
polynomial P of degree M, every rotated grid factor with its conjugated
denominator angle, all spatial modes and normalized angular means.
No separation, symmetry or coefficient-integrality assumption is allowed.

C645y supplies F and the complete identity (10); L649 supplies kappa
and D_single,n. L650 identifies their norms and gives the response and
cost for d=P_+(b_u J s), with J s=zeta^(-1)conj(s) on the boundary.
The proposed D_(u,M) uses every analytic polynomial of degree <M.
Its optimizing combination may depend on the complete family P and u;
one must retain the full Gram form of these vectors. This is not the
initial M grid coefficients. No conclusion about its adequate rate is
inferred from its dimension or from exact interpolation.

The precise target is the displayed relative inequality, with c>0 and
onset independent of every admissible family. It is a sufficient
constant-input comparison, not the full Hankel operator or an Xi claim.
All Xi realization, matching upper bounds and all-degree signs remain
independent. C645y, L649 and L650 have separate audit limitations.

## Review and bounded test

Compare the exact statement and stronger known results, reusing the
primary background rather than rereading unchanged sources without a
reason. Inspect any essential new theorem hypotheses and proof cases.
Check the distinction between polynomial spatial tests and grid prefixes,
and between family-dependent joint combinations and C645x's universal
fractional-mixture dual. L650's close pair is a required normalization
test: the joint span must retain its unit-norm sum. Preserve C645y's
prefix stop and L646/L649's exact-recovery stops.

After a separate ready assessment, a bounded mathematical test could
either prove the displayed uniform relative rate, supply a complete
admissible countersequence for this joint projection, or isolate one
quantitatively bounded remaining cost. Repeating an unevaluated Gram
minimization or separately normalizing its columns would not qualify.
Failure of this joint sufficient projection would still not refute the
full energy or detector. Full matching Mathlib coverage is not checked.

## Source comparison completed — 2 November 2026

### Local overlap and recorded failures

Read L649's exact component and diagonal definitions and L650's hypotheses,
conclusions and full-dual construction through its nonvanishing argument.
Read C645y's hypotheses, complete-energy and inverse-Gram statements and
prefix stop; reused their prior detailed source comparisons. Read the
L650 failure record and its session history. No certificate was replayed
or mathematical input critically audited in this turn.

The exact unit-norm two-column sum is already L650 (7), not a new result.
It must be retained when assessing the joint space. C645y's first-M and
half-grid stops concern grid coordinates; the proposed space uses images
of spatial polynomials under the entire b_u. L649's stop concerns the
recovered inner-input component, whereas this target concerns F_u.
C645x's universal fractional-mixture restriction remains a contrast,
reused from the previous assessment; it is not a negative result for
P-dependent joint choices with positive integer original residues.

### Primary theorem comparison

1. L. Baratchart, S. Chevillard and T. Qian, *Minimax principle and lower
bounds in H2-rational approximation*, J. Approx. Theory 206 (2016),
17--47, [v2, 24 March 2015](https://arxiv.org/pdf/1501.01161v2).
Theorem 4 assumes continuous strictly negative Hardy f and orthonormal
Hankel singular vectors; its lower error bound uses their sup norms.
Section 5.2 gives finite rational model-space and Bezout computations.
Theorem 7 assumes strictly negative Hardy f and a degree-at-most-k weight
polynomial pi without unit-circle zeros. It bounds best degree-k rational
error below by a minimum linearized error, normalized by ||q/pi||_infty=1.
Its proof handles interior weight zeros by reflection, then Hardy
projection and a genus argument. These are approximation-error bounds,
not the requested norm of a prescribed joint projection of F_u.
Theorem 4's complete proof and Theorem 7's two weight cases were inspected;
no identification or uniform rate for the present family follows merely
from these statements. No reproof is proposed.

2. A. E. Frazho, S. ter Horst and M. A. Kaashoek, *Optimal solutions to
matrix-valued Nehari problems and related limit theorems*,
[v1, 28 April 2011](https://arxiv.org/pdf/1104.5358v1).
Theorem 3.1 assumes a bounded matrix symbol, finite-rank Hankel operator,
no maximizing vector in zH2, maximizing-vector space of dimension equal
to the input dimension, and a fixed finite backward-shift-invariant
initial space. For its recursive enlargements, central restricted Nehari
solutions converge geometrically for fixed data. In the scalar case the
maximizing singular value must be simple. Lemma 6.2 and the four proof
parts use a fixed defect inverse and state resolvents; their bounds are
uniform in enlargement index, not asserted uniform in the symbol.
Those extra hypotheses and uniform constants are unverified here.
Moreover our output projection is not identified with that recursive
input restriction. Proposition 2.1's previously inspected restricted
distance identity is reused; it does not supply the missing comparison.

3. L. Baratchart, A. Borichev, S. Chevillard, C. Coiffard and R. Zarouf,
*Lower bounds in H2-rational approximation to Blaschke products*,
[v2, 29 September 2026](https://arxiv.org/pdf/2603.16295v2).
Theorem 3: a degree-N Blaschke product with zeros of modulus <=lambda<1,
0<=k<N, 0<alpha<(1-lambda)/(1+lambda), beta in [0,1] satisfies
d2(f,R_(k,k))>=sqrt(max(0,Psi(N,k,lambda;alpha,beta))), with Psi in (43),
s* in (35), K in (37). The proof uses winding number, a signed Fourier
moment, and coefficient tails. Proposition 1 gives geometric upper
coefficient and tail bounds only at indices >=N/alpha; its proof handles
inner/outer contour radii and optimizes the latter. These hypotheses
and the complete indicated proofs were inspected. The target is a
weighted rational response, not approximation of b_u by lower degree.
No conversion controls its D_single,n normalization or joint response.
Coefficient upper bounds alone are not the requested lower bound.

These comparisons do not establish a nonexistence theorem for an import
or certify novelty. Mathlib coverage of the full target was not checked;
the previously inspected Hardy/Fourier support remains background only.

### Search record and bounded continuation

Web queries included `finite Blaschke product Hankel range polynomial
subspace smallest singular value model space angle`, `finite rank Hankel
logarithmic derivative positive integer residues rational approximation
lower bound projection`, `"model spaces" "angle" "polynomials" Hardy`,
`"Hankel" "polynomial subspace" lower bounds`, `"finite Blaschke"
"Hankel" "smallest"`, and `"logarithmic derivatives" "L2" "rational"
approximation`. Results led to the three primary texts above. General
truncated-Toeplitz norm and simple-partial-fraction density papers were
search leads only; their theorems were not inspected or used.
The prior five-source Markov/Pade comparison and Biro assessment are
reused within their saved scopes. No source access blocker remains
essential to this bounded finite-algebra target.

The main gap remains actual-Xi all-degree mixed positivity. A uniform
joint bound could supply the sufficient constant-input detector
comparison, leaving actual-Xi realization, matching upper bounds and
signs independent. Continue only upon the stated rate with uniform
constants/onset, a rigorous full admissible countersequence, or one
quantitatively bounded remaining cost. An unevaluated Gram minimum,
finite screen or a separately normalized column is not decisive.
Preserve partial reasoning before further lengthy work and require
new input or a refined mechanism before repeating an unsuccessful test.

This turn completes the previously uncovered source review and changes
the gate to EXPLORE. It derives no new result and changes no lemma or
mathematical script. Separate approval of this newly ready assessment
precedes the nominated research attempt.
