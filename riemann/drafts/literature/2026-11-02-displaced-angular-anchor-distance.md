# Displaced angular anchor distance: completed source comparison

TARGET: Test whether delta_e=dist_(L2(T),normalized)(1,span_C{W_a:a in Z_e and a!=x}) satisfies delta_e>=exp(-n/100)*n^(-C) with absolute C and onset for every L666 displacement vector, or give an admissible sequence for which (-log delta_e-n/100)/log n is unbounded above.
CHECKED: 2026-11-02
DECISION: EXPLORE
SEARCH_EVIDENCE: On 2026-11-02 searched rational-span distances, uniform minimality, reproducing-kernel Riesz bounds and two-sided prescribed-pole spaces; exact queries and inspected sources appear below. Reused the two nominated assessments and narrowly checked L646/L647/L650, C645p and L666. No matching evaluated bound for this prescribed span was identified; this bounded comparison does not certify novelty.
SOURCE_EVIDENCE: Bultheel--Cruz-Barroso--Lasarow, arXiv:1707.09748v2 (3 December 2017), Sections 2--3, Lemmas 3.1--3.2 and complete proofs, printed pp.5--8 (https://arxiv.org/pdf/1707.09748v2); Fricain, Bases of reproducing kernels in model spaces, J. Operator Theory 46 (2001), 517--543, author PDF Theorem 2.1, Lemma 2.2 and both proof directions, internal pp.10--11 (https://pro.univ-lille.fr/fileadmin/user_upload/pages_pros/emmanuel_fricain/JOT-2001.pdf). Prior inspected finite observation/Hardy comparisons are reused within their recorded qualifications.
COMPARISON: The rational-space lemma changes an ambient prescribed-pole representation; it does not identify the span of these W_a with a kernel system or bound its anchor distance. Fricain requires kernel identification, Carleson/angle conditions and Toeplitz left invertibility, none verified here with uniform quantitative constants. Quadrature measures norms without coercivity. L646/L650 are spatial tests, and L647 supplies no positive exponential loss. No inspected source supplies the rate 1/100.
GAP: Evaluate the distance of 1 from exactly the nonanchor angular span, retaining arbitrary complex auxiliary coefficients and all rational factors, at the stated uniform rate or by the stated admissible countersequence. A kernel identification, favorable Gram spectrum and uniform inverse estimate remain unproved; neither they nor Xi realization may be assumed.
REASON: Essential selected source comparison for the unchanged TARGET is complete enough for one bounded family-specific attempt. The unresolved quantitative distance is outside the conclusions inspected; EXPLORE approves its investigation, not the inequality or a new general frame theorem. Separate approval of this newly changed assessment precedes research; no essential source is blocked.
LITERATURE_REASON: The new quantitative object is the distance of the constant angular function from a prescribed rational span, not a cleared-polynomial coefficient, general spatial interpolation input or signed-energy derivative. Existing assessments do not explicitly cover this changed target.
SCOPE: Exactly TARGET for the full L666 family defined below. One family-specific rational/Hilbert-space proof attempt or admissible asymptotic upper-distance witness is covered, including complete complex projection costs. Any application to c_0 and the existing Jensen/localization bridge must be justified. No replacement of original residues, exponential surrogate, assumed kernel identification, favorable spectrum or new general frame theorem is covered.

## Exact target and intended use

Retain q>=1, n=12q+3, M=4q+1, J=n-1, x=-5/4, R=11/8,
U=121/64, H_0=27/(10n), every t_j=j/n for 0<=j<n, and

    Z_e={x} union {x+i*H_0*(r+1/2+e_r): -2q<=r<2q},
    e_r real, |e_r|<=1/8,
    W_a(u)=B_u(x)/B_u(a),
    B_u(v)=product_(0<=j<n) R*(v-t_j*u)/(U-t_j*v/u).

The functions belong to normalized angular L2(T), with the same
displacement vector at every angle. The proposed object is exactly

    delta_e=inf_(lambda in C^(M-1))
       ||1-sum_(a!=x)lambda_a W_a||_(L2(T)).

The auxiliary coefficients lambda describe the comparison subspace;
they do not change any original unit residue in G or D. The prospective
application is to the actual c_0=R^(-1)(1+sum_(a!=x)W_a), then to
the existing full-spatial Jensen bridge and L658/L661 localization.
That applicability argument must be checked in the later mathematical
attempt. No projection identity or quantitative lower bound is proved
in this nomination. The other M-1 spatial moments remain present in
the target G; support, Xi realization and mixed signs remain open.

## Why this is a different test, and where it may fail

L670 and L671 stop specific coefficient certificates after clearing
all angular denominators. This proposal keeps the original rational
functions on the angular circle. It seeks signed separation of one
anchor from the entire remaining span, rather than an energy identity,
a positive-entry assertion or differentiation of the scalar energy.
It is a possible new input for the scalar route parked after L666;
renaming that old route or restating its unevaluated Gram form would
not count as progress.

L646 and L650's relevant stops use spatial interpolation and allow
exponentially close poles; the present target has L666's particular
separation and an angular norm. These differences justify comparison,
not a claim that the old obstructions disappear. L647 stops a constant
full/group energy comparison while its example has zero exponential
loss; it does not directly evaluate this distance. The prior
joint-full-grid-polynomial-dual assessment concerns a spatial image
at each angle, not this fixed angular span. These source-scope
distinctions must be checked before a mathematical attempt.

The proposed distance may be too small because it permits arbitrary
complex auxiliary coefficients. If an admissible sequence defeats its
rate, stop this sufficient mechanism; do not claim the actual
unit-residue c_0 or H is small. A finite positive Gram determinant,
unquantified linear independence, observation identity, numerical
condition estimate or unknown smallest eigenvalue does not decide
the rate. A singular case must be handled explicitly, not excluded by
assumption. Any use of a Gram inverse must justify invertibility or
the correct pseudoinverse/projection formulation.

## Completed primary comparison, 2 November 2026

**Two-sided rational spaces.** A. Bultheel, R. Cruz-Barroso and
A. Lasarow, *Orthogonal Rational Functions on the Unit Circle with
Prescribed Poles not on the Unit Circle*, SIGMA 13 (2017), 090,
[arXiv:1707.09748v2](https://arxiv.org/pdf/1707.09748v2),
Sections 2--3, printed pp.5--8. Their parameters alpha_j are in the
disk, beta_j=1/conjugate(alpha_j), and gamma_j chooses either;
L_N consists of numerators of degree at most N over the prescribed
product denominator. Lemma 3.1 states
L_N=dot(B)^beta_N L^alpha_N=dot(B)^alpha_N L^beta_N.
Read the complete cancellation proof, including N=0 and
alpha_j=0/beta_j=infinity, and Lemma 3.2's shifted-space proof.
The boundary multipliers have modulus one. This is a representation
of an entire rational space; it gives no distance estimate for a
prescribed collection within it. The L666 pole lists permit a later
membership comparison, but no identification of its W_a span with
a full space or kernel family is established here. After a change
of representation the anchor must also be transformed. Replacing
the comparison space by a larger ambient space cannot be asserted
to preserve the desired quantitative distance. No specialization is
proved in this literature turn; recurrence and quadrature sections
are not inputs.

**Kernel Riesz criterion.** E. Fricain, *Bases of reproducing kernels
in model spaces*, J. Operator Theory 46 (2001), 517--543,
[author PDF](https://pro.univ-lille.fr/fileadmin/user_upload/pages_pros/emmanuel_fricain/JOT-2001.pdf),
internal pp.10--11, Theorem 2.1. For finite-dimensional E, inner
Theta, unit e_lambda and sup ||Theta(lambda)^*e_lambda||<1,
the model kernels form a Riesz basis of their hull iff Lambda is
dim(E)-Carleson, the stated local vector angles have positive infimum,
and T_(B^*Theta) is left invertible; K_B is the hull of ordinary
kernels k_lambda e_lambda. Read both proof directions, through
Lemma 2.2's projection/isomorphism criterion. Lemma 2.2's proof and
the background properties are omitted by the author, not audited here.
The theorem concerns identified reproducing kernels and qualitative
invertibility, with geometric conditions to check. No such
identification, uniform constants or quantitative inverse bound for
these W_a is supplied. Ordinate separation alone verifies none of
those conditions. A finite Riesz property for each individual family
would still leave the required uniform n-dependent rate unresolved.
Theorem 2.8 and later perturbation theorems were screened only as
leads and are not inputs. No reproof is proposed.

**Reused inputs and local distinctions.** The nominated
`2026-11-02-displaced-signed-angular-sampling.md` already records
Danchenko--Semin v1 Theorem 2, its complete proof and its pole/order
conditions, and Moitra v4 Theorems 2.2--2.3 with finite alias cases.
Reuse those readings: exact signed rational observation is available,
whereas a coercive bound and a map to exponential columns are not.
L666 proof Sections 1--2 were checked for the family and angular pole
lists. Its common interior poles and a-dependent exterior poles
must remain in any representation; neither projection onto one
Hardy half nor dropping cross terms is justified as an equality
for delta_e. The prior joint-full-grid-polynomial-dual assessment's
finite Hardy/Nehari/Blaschke comparisons also give no identification
with this angular span; their separate spatial target is unchanged.

The inspected L646 and L650 hypotheses/conclusions use spatial
interpolation or spatial polynomial duals and permit exponentially
close poles. Their countersequences do not evaluate the L666 distance.
L647 stops a constant energy comparison in a broader family and
explicitly has zero exponential relative loss. C645p and its
zero-evaluation failure record retain the sharp ambient transfer
cost; they must not be presented as a family-specific anchor bound.
L670/L671's clearing-coefficient stops are preserved as recorded at
startup; no independent audit is claimed. None is a duplicate proof
of the present distance claim or its negation.

## Search record, readiness and continuation

Queries included `rational functions Hilbert space distance constant
span reproducing kernels Blaschke product Riesz basis uniform minimality`,
`rational functions unit circle prescribed poles least squares
approximation constant Gram matrix distance`, `"rational functions"
"uniform minimality" distance`, `"Blaschke" "ratio" "distance"
"span" rational functions Hilbert`, and `"rational functions"
"distance from 1" prescribed poles`. The exact rational-span query
and stronger kernel/space comparisons led to the two inspected primary
texts above, rather than a matching rate theorem. Shapiro--Shields,
optimal approximants, general discrete least squares and multipoint
Schur sources remained search leads, not inspected theorems or
essential inputs. No conclusion of novelty or global absence follows.
Text retrieval succeeded. Screenshot calls returned no usable image;
the complete selected proof ranges were read as text instead.

After separate approval, perform one bounded test of exactly TARGET.
The proposed new mechanism is joint angular separation of the anchor;
it may use full rational identities or a bounded auxiliary annihilator,
but must pay its entire norm. An upper-distance countersequence must
give admissible displacements and auxiliary coefficients with an
asymptotic error proof, rather than finite ill-conditioning evidence.
A lower-distance proof must cover every displacement with absolute
C and onset, including any singular span, without assuming an inverse.
Only achieving the stated rate, proving its failure on a full admissible
sequence, or isolating a quantitatively bounded remaining cost justifies
continuation. An unevaluated Gram minimum is insufficient. Failure
would stop this sufficient separation mechanism without refuting H.

Essential continuation inputs are L649/L666's exact family, L657/L658's
integrability/localization, and L661's diagonal comparison; the existing
full-spatial Jensen bridge remains to be applied with its hypotheses.
The target concerns a Hilbert distance, so its prospective use in the
angular maximum and H still requires the later applicability argument.
Other spatial moments, general support, Xi realization and all-degree
mixed signs remain independent. No new lemma or mathematical script
is written and no RH candidate is asserted. Full matching Mathlib
coverage is not checked; Hilbert projection support would not establish
the prescribed quantitative inequality.
