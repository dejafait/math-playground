# Source comparison: real scalar residue signs

TARGET: Assess whether some fixed reflection-symmetric centered-gap profile selected by L699 has nonzero scalar residues rho_(j,n) of one common sign for every 1<=j<n on an unbounded sequence n=12q+3.
CHECKED: 2026-11-03
DECISION: EXPLORE
SEARCH_EVIDENCE: Step 130 made nine bounded queries on real-rational interlacing, positive residues, nonreal poles, generalized Nevanlinna functions and perturbed-lattice spectral gaps; exact queries and inspected sources are recorded below. Scoped duplicate/failure checks retain the step-115/127/129 stops. No failed search is evidence of novelty.
SOURCE_EVIDENCE: McKee--Smyth arXiv:math/0308213v2, Lemma 4 and complete proof p.3; Reiffenstein arXiv:2108.10746v3, Definition 2.1 and Theorem 2.2 pp.2--3, Theorem 2.3 p.3; Baker (17 March 2020), Theorem 3 and strict-case proof. Reuse step-128 rational Jensen and Lev coverage; reinspected Lev v3 Theorem 4.8 and complete proof, Section 4.10.
COMPARISON: The inspected residue/interlacing characterizations require prescribed real interlacing or a Herglotz representation with nonnegative coefficients; neither is verified for L699's whole rational function or its interior-pole part. L666 retains possible nonreal exterior poles and cancellations. Lev prescribes a distributional transform, not these finite angular signs. No inspected theorem decides TARGET.
GAP: Prove strict common signs for every 1<=j<n on an unbounded sequence for one fixed allowed Picard profile, or supply an eventual obstruction with correctly quantified profile scope. L699's alternating real sums, cancellations and large-n quantifier remain unresolved; scalar compensation, H/support and Xi transfer remain independent.
REASON: The new theorem-level comparison supplies adequate coverage for one bounded analytic test of the actual L699 (7) residues, subject to separate next-turn approval of this newly ready assessment. No essential source blocker remains, no residue inequality is proved, and no new mathematics is derived or imported into lemmas this literature-only turn.
LITERATURE_REASON: The target changed from scalar logarithmic compensation to strict signs of the actual finite angular residues; the necessary positive-residue and interlacing hypotheses had not been inspected. Reuse the ready Jensen/gap assessments for their unchanged scope.
SCOPE: Exactly TARGET for L699's reflected L694/L696 prescribed-center Picard construction. One analytic actual-residue test is covered, beginning with j=1,2 as a possible eventual obstruction and retaining all j as the positive success obligation. Fix all choices and g>0 before n; preserve cap 1/8, real l1 shifts, unit masses, anchor, j=0, angle 1/u, n=12q+3, exact -2q<=m<2q and every downstream M moment. No sampled finite-profile surrogate, assumed Herglotz membership, or generic divisor reaccounting is covered.

The nomination below is preserved as historical scope. Its pending-review
language describes the nomination stage; the completed comparison below
resolves source coverage, with separate next-turn approval still required.

The main gap remains actual-Xi all-degree mixed positivity. This target
tests a sufficient finite charge mechanism for the approved scalar
counterprofile question, with realization and H/support still independent.
Its precise implication, endpoint charge and integrated spatial comparison
are already proved conditionally in L699. Review that canonical result
as an unaudited local input, not an unconditional lower bound.

Fix all cutoffs, the sufficiently small positive gap width and the exact
Picard solution before varying n. L699's choice is the L696 prescribed
center omega_* with L694's even Phi and eta, and has real l1 shifts,
cap 1/8 and e_(-m-1)=-e_m. Existential choices may remain explicit;
the step-127 finite Fourier array is inadmissible. Use the original
unit masses, fixed anchor, j=0, angle 1/u and exactly -2q<=m<2q.
No changes to the downstream full M spatial moments are allowed.

The actual interior candidate poles are p_j=-d*j/(U*n). At every
selected n the proposed condition requires every residue in L699 (7)
to be strictly positive or every residue to be strictly negative;
the common sign may vary with n. A zero residue is a cancellation and
fails this particular sufficient condition. It does not refute the
desired scalar logarithmic rate. A finite exceptional n likewise does
not refute a condition sought only on an unbounded subsequence.

Search for exact or stronger known real-rational interlacing results,
positive-residue characterizations, and obstructions for these products
or the spectral prescription. Retrieve the actual hypotheses before
importing a theorem. Do not substitute positivity of the spatial masses
for positivity of angular residues, or assume this rational sum belongs
to a Stieltjes/Pick class without verifying it. The elementary conditional
interlacing argument is already in L699 and need not be reproved merely
to call the literature review useful. What matters is comparison with
the family-specific sign obligation.

Continue only if source comparison supplies an import or a concrete
bounded test of the actual signs. An informative obstruction must address
this fixed exact profile and its large-n quantifiers; an unrelated
positive-residue example, sampled finite approximation, generic Mahler
degree loss or restated Jensen identity does not suffice. If the
condition is unsuitable, park it and preserve the broader scalar target.
The compensation exploration count is two and is not renewed here.

Mathlib coverage of the new sign target is not checked. No essential
source blocker has been demonstrated, no mathematical sign attempt is
authorized by this REVIEW_REQUIRED nomination, and no novelty claim is
made. The next turn is literature-only until this exact comparison is
completed under the shared gate.

## Completed comparison — 3 November 2026, step 130

### Exact local obligation and previous failures

Read the complete L699 proof, L666's hypotheses and angular continuation
Section 2, and L696's hypotheses and prescribed-center construction.
Reuse the step-128 Jensen/gap assessment. L699 remains unaudited; this
review does not certify its reflection or conditional charge proof.
Its equation (7), including the already recorded alternating prefactor,
is the actual sign obligation. Reality of its inner sum is established
locally; its required strict alternating pattern is not.

The scoped checks found the earlier Pick-cluster test in
`2026-11-01-pick-cluster-residue-cancellation.md` and the signed-kernel
review in `2026-11-03-nonuniform-lattice-unit-residue-kernel.md`.
Those concern different residue normalizations/contours and supply no
sign estimate for L699 (7). The step-129 unpaid-charge note records the
present missing inequality. The step-127 inconclusive-screen note
retains its exact-profile/asymptotic qualification. The step-115
absolute-tail stop is retained through the reused step-128 assessment;
its historical proof was not reopened. No duplicate sign result was
found in these scoped inputs; that is not a global novelty claim.

### Inspected primary statements and comparison

J. McKee and C. Smyth, *There are Salem numbers of every trace*,
[arXiv:math/0308213v2](https://arxiv.org/pdf/math/0308213v2),
31 March 2004, Lemma 4 and complete proof, PDF/printed p.3.
For gamma>0 and strictly interlacing real numbers
alpha_1<beta_1<alpha_2<...<beta_(D-1)<alpha_D<=A, the quotient

    gamma product_(k=1)^(D-1)(v-beta_k)
          /product_(k=1)^D(v-alpha_k)

has partial fractions sum lambda_k/(v-alpha_k), lambda_k>0.
Conversely every such positive-residue sum has this interlacing form.
The lemma also locates the roots of f(v)=1, including the last root
relative to A; that extra conclusion is not needed here. Its proof uses
the sign of the simple-pole coefficients and the intermediate value
theorem. This characterizes an already controlled real-pole quotient;
it does not determine L699's coefficients. Neither a real-rooted
numerator of the required degree nor this strictly proper real-pole
form has been established for the whole c_(0,n).

J. Reiffenstein, *Higher-order interlacing for matrix-valued meromorphic
Herglotz functions*,
[arXiv:2108.10746v3](https://arxiv.org/pdf/2108.10746v3),
29 April 2022, Definition 2.1 and Theorem 2.2, pp.2--3.
In scalar notation the characterization is

    q(v)=C+D*v+sum_k A_k[1/(z_k-v)-z_k/(1+z_k^2)],

where C is real, D>=0, A_k>=0, the real z_k have no finite accumulation,
and sum A_k/(1+z_k^2)<infinity. This is equivalent to real-symmetric
holomorphy off the real axis with nonnegative upper-half-plane imaginary
part; finite sums are included. Actual pole residues are -A_k, with
strict negativity requiring A_k>0. Read the full statement, including
its additional clauses. Theorem 2.3, p.3, states an infinite product
criterion assuming poles unbounded in both directions; that version is
not a finite-family import. These representation statements are cited
as known results; their upstream general representation proofs were not
audited. No half-plane mapping property is proved in this review.

M. Baker, [*Interlacing via rational functions and spectral decomposition*](https://mattbaker.blog/2020/03/17/interlacing-via-rational-functions-and-spectral-decomposition/),
17 March 2020, Theorem 3 and its complete strict-case proof, was read
as an author exposition and reference trail to McKee--Smyth. It makes
explicit the real-rooted numerator/denominator and degree-difference-one
hypotheses. Its nonstrict case is a continuity sketch; no cancellation
argument here relies on that sketch. The original Lemma 4 above is the
primary finite statement used for comparison, with no reproof.

N. Lev, *An example concerning Fourier analytic criteria for translational
tiling*, [arXiv:2007.09930v3, Section 4.10](https://arxiv.org/html/2007.09930v3#S4.SS10),
Theorem 4.8 and its complete proof were reinspected for the new sign
obligation. For 0<a<b<1/2 and sufficiently small integer Fourier
coefficients of a Hermitian distribution supported in the two annuli,
it constructs real bounded shifts with the specified local counting
transform. No finite angular residue signs are asserted. Reuse the
ready construction comparison: summability/anchor, the center choice
and the selected reflection are local L694/L696/L699 conclusions,
respectively. None should be silently attributed to this theorem.

### Why these results are insufficient, and the permitted test

The comparison with L666 is about missing hypotheses, not a new
impossibility result. Its exact continuation lists possible nonreal
exterior poles a/t_k as well as the real interior p_j. Cancellations
have to be checked. L699 proves real coefficients, not holomorphy on
the whole nonreal plane or a half-plane mapping property. No inspected
result upgrades positive original spatial masses to angular residues.
Applying a Herglotz theorem to the whole scalar sum would therefore
skip an essential obligation. Conversely, possible exterior poles do
not invalidate L699's local conditional intermediate-value argument.
That argument does not need global Herglotz membership.

One could instead consider only the real-interior-pole principal part.
Its coefficients would be precisely the unknown rho_(j,n); positivity
of that representation is the requested inequality, not a supplied
premise. The cited characterizations cannot certify it without a
family-specific estimate. The known conditional interlacing/Jensen
reduction is already canonical in L699 and need not be reproduced.

Coverage is sufficient for one analytic attempt using the actual
expression (7). A concrete initial falsification test is to resolve
the signs at j=1 and j=2 for all sufficiently large n=12q+3 for a
fixed allowed profile, with a justified error bound from the exact
profile rather than a numerical Picard truncation. Opposite nonzero
signs eventually would exclude that profile's unbounded common-sign
subsequence. A positive result at these two poles alone would not
settle the target: all 1<=j<n must still be covered on one unbounded
sequence. If the endpoint test supplies no estimate, preserve its
partial reasoning and stop this bounded attempt rather than repeat
Jensen accounting or the old screen.

The existential profile quantifier matters. A failure for one allowed
choice only rejects that choice. To refute TARGET one needs eventual
failure for every allowed fixed choice, or another obstruction with the
same quantified scope. The onset may depend on the fixed profile;
claim no uniformity without proving it. An arbitrary finite exception,
a zero residue at finitely many n, or generic failure of Herglotz
membership is not such a refutation. No endpoint asymptotic, residue
sign, failure theorem or new profile is derived in this review.

Continuation succeeds with either a strict all-j certificate for one
fixed profile on an unbounded subsequence, or an informative rigorous
obstruction with its exact profile/large-n scope. A qualified partial
sign estimate is to be recorded honestly. Any negative result concerns
this sufficient interlacing mechanism; it leaves scalar/full-spatial
compensation, H/support, realization and the RH gap open. The two
previous mathematical EXPLORATION turns remain counted. Literature
does not reset them; a third mathematical EXPLORATION requires the
shared reassessment. This new actual-sign mechanism is not a reopening
of the absolute-tail or finite-screen closures.

### Search record and reading limits

The nine query strings were:

- `rational functions real poles residues same sign interlacing Herglotz theorem`
- `"rational" "interlacing" "residues" "Borcea"`
- `"spectral gap" "perturbed lattice" "Stieltjes"`
- `"rational functions" "residues" "nonreal poles" interlacing`
- `"perturbed lattice" "residues" "sign"`
- `"Higher-order interlacing" "Theorem 2.2"`
- `"rational function" "positive residues" "complex" "products"`
- `"generalized Nevanlinna" "residues" "real poles" sign`
- `"spectral gap" "lattice" "interlacing" residues`

Secondary interlacing indexes and Reiffenstein's thesis were discovery
leads only; the paper statements above replace them as evidence.
Search results also exposed generalized Nevanlinna/sign-indefinite
operator work, orthogonal-rational interpolation, real-rootedness
preservers and rational Gabor windows. Their theorems were not read
or imported. No representation, negative-square bound, recurrence or
orthogonality meeting those hypotheses is supplied by the local inputs,
so they are not essential missing coverage for the direct residue test.
Unrelated RH-claim and graph-spectral results were not used. No exact
or stronger family-specific sign theorem was found among the inspected
results; this bounded search neither proves absence nor certifies novelty.

Mathlib coverage of TARGET and the matching strict-residue criterion
remains unchecked. No formal verification is claimed. The result of
this source review is EXPLORATION / NOVELTY_UNCHECKED, not a mathematical
advance beyond the sources. EXPLORE makes this assessment ready for
separate next-turn approval; it does not certify a favorable sign or
perform the newly covered mathematical attempt.
