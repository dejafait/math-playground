# Full-pole Hardy-space boundary mechanism — completed source comparison

TARGET: Assess a Hardy-space Hankel replacement for C645f's three-pole census, with explicit dependence on n, total pole multiplicity and boundary clearance.
CHECKED: 2026-11-01
DECISION: EXPLORE
SEARCH_EVIDENCE: Completed bounded Nehari/AAK, rational-symbol, positive-residue and simple-partial-fraction searches; inspected the primary statements and proof cases listed below. Reused the scoped Pick/contour comparison and September stops; checked C645f's exact hypotheses, C645d's cancellation statement and C645c's rate statement. No inspected theorem gives the required phase-weighted n/M/eta bound; no exhaustive absence or novelty claim.
SOURCE_EVIDENCE: Adamjan–Arov–Krein (1971), Theorems 0.1/0.2, pp.31–33, and relevant finite-rank eigenvalue cases of Theorem 1.1, pp.41–43, https://www.mathnet.ru/php/getFT.phtml?jrnid=sm&option_lang=eng&paperid=3284&what=fullteng ; Baratchart–Chevillard–Qian (2016), Sections 2–4, Theorems 2/4, Corollary 1, complete Section 5.2 and finite-Blaschke proof case of Lemma 1/Theorem 5, pp.18–30, https://www.must.edu.mo/images/SCSE/qiantao/QianTao_P147.pdf ; Chunaev–Danchenko 1907.07437v1, Theorem 1/(8), pp.1–3, and relevant symmetry/removal steps in Sections 2.1/2.4, https://arxiv.org/pdf/1907.07437v1 .
COMPARISON: Nehari/AAK supplies exact distance/singular-value identities for complex bounded symbols, and rational-symbol theory supplies a finite model-space calculation. Neither supplies an evaluated n/M/eta lower bound. The explicit inner-symbol and unweighted logarithmic-derivative estimates have different hypotheses; positive original residues do not make the proposed weighted symbol inner or its amplitudes positive. C645f remains a small-cluster result.
GAP: A separation-free quantitative spectral lower bound for the exact weighted positive-residue family remains unproved; a useful rate, full principal-part reduction, actual census/clearance, interpolation realization and an independent boundary upper bound remain open.
REASON: The source comparison stops the identity-only shortcut and makes the missing spectral estimate precise. Nominate one bounded positive-residue, growing-census test separately; do not spend another turn rederiving Nehari/AAK or claim a full-pole certificate from finite rank alone.
LITERATURE_REASON: Essential operator theorems lay outside the ready finite-moment coverage. This turn completes that comparison, including the newly located simple-partial-fraction terminology; unchanged browsing is unnecessary.
SCOPE: Completed comparison for the saved full-boundary mechanism. Standard identities may be cited with their exact hypotheses; no quantitative full-census estimate or mathematical attempt was established in this literature-only turn.

## Exact comparison problem, not an asserted theorem

Retain C645f's fixed delta, d, R, x, n>=5, grid, exact complex B_n,
neighborhood regularity and exact interpolation. For this proposed
comparison only, replace its small one-to-three-pole cluster by a finite
set Z in |z|<=R-eta, containing x and avoiding the grid, where
0<eta<R-d. Allow arbitrary other locations and arbitrarily close
distinct poles. Require F to have exactly these poles in the closed disk,
each simple with positive integer residue r_a, and total multiplicity
M=sum r_a; r_x>=1. This models logarithmic-derivative multiplicities as
residues of simple poles, not higher-order poles of F. Keep P holomorphic
near the closed disk with every grid value matched. No actual-Xi
realization or positive-real P is supplied by these synthetic data.

The object proposed for comparison is the boundary function
G_n(z)=B_n(x)(F(z)-P(z))/B_n(z) on |z|=R. Ask whether a Hardy-space
Hankel norm or a meromorphic approximation theorem controls its full
boundary norm from its pole data, with a bound explicit in n, M, eta
and delta. Its residue amplitudes have the exact complex phase
r_a B_n(x)/B_n(a); replacing them by positive numbers is forbidden.
No formula for that operator, norm identity or quantitative lower
bound is established in this nomination.

## Relevance and discriminating test

Main gap: actual-Xi signs at unbounded heights/all-degree mixed
positivity. C645f's complete three-pole census is unavailable for Xi.
A full-pole boundary test could supply a detector without requiring an
isolated small cluster, if its quantitative costs were small enough.
The independent upper bound, actual pole census/counts and clearance,
interpolant realization, and final signs would remain open.

Retrieve primary theorem hypotheses and relevant proof cases before
large extracts. Compare Nehari/AAK or a genuinely matching meromorphic
interpolation result with this exact object, including analyticity,
norm, finite-rank, pole and multiplicity conventions. Give the strongest
inspected conclusion and its n/M/eta dependence; do not merely name a
standard theorem. Assess whether it could improve on a growing-degree
polynomial-moment cost when n and M are of logarithmic height size.
This is a proposed usefulness threshold, not an available Xi estimate.

Continue to a separately gated mathematical test only if the source
comparison exposes a specific unproved quantitative claim with a
plausible useful scale. Stop or refine this mechanism if standard
theory already settles it, if it merely restates a norm identity with
an uncontrolled singular value, or if its cost cannot address the
logarithmic-grid bottleneck. Retain an informative obstruction if
one is found. No uniform-in-n positive bound is presumed, and no
finite test is promoted to all-degree positivity.

The local duplicate check read the parent assessment's distinction
from the squared-pole high-real-axis Hankel family, not its proof.
The older stops are
`ATTEMPTS/2026-09-09-finite-hankel-extrapolation.md` and
`ATTEMPTS/2026-09-09-strip-to-hankel-positivity.md`.
Their finite-to-infinite and algebraic-square obstructions remain;
this proposed test concerns a full boundary operator and quantitative
pole costs, and must still be compared with the relevant Pick sources.
No historical stop is treated as a global ban. No cross-notebook input
is used. Full matching Mathlib coverage is unchecked.

The preceding paragraphs preserve the nomination and its original
tests. The completed comparison below replaces its former unread-source
status. No protected mathematical attempt was performed here.

## Completed comparison — 1 November 2026

### Primary operator statements and relevant cases

V. M. Adamjan, D. Z. Arov and M. G. Krein, *Analytic properties of
Schmidt pairs for a Hankel operator and the generalized Schur–Takagi
problem*, Math. USSR-Sb. **15** (1971), 31–73,
[DOI 10.1070/SM1971v015n01ABEH001531](https://doi.org/10.1070/SM1971v015n01ABEH001531).
Read the English publisher scan linked in SOURCE_EVIDENCE: Section 0
definitions and Theorems 0.1/0.2, and the finite-rank-relevant cases of
Theorem 1.1. The approximation class is H-infinity plus a proper
rational function with at most k interior poles counted by order.
For a bounded circle symbol phi, the best uniform error in that class
equals s_k(H_phi), with indexing from zero. Theorem 0.1 retains the
Hankel restriction on rank-k approximants. The proof connection uses
Nehari's norm/distance theorem and Kronecker's finite-rank theorem.
The inspected eigenvalue cases handle multiplicity via invariant
subspaces; they do not evaluate singular values from a pole count.
No reproof is needed. Some scan display extraction is damaged; the
clear operator convention/formula is also stated in BCQ Theorem 2.
The entire original AAK proof was not audited or claimed audited.

L. Baratchart, S. Chevillard and T. Qian, *Minimax principle and lower
bounds in H2-rational approximation*, J. Approx. Theory **206** (2016),
17–47, [DOI 10.1016/j.jat.2015.03.004](https://doi.org/10.1016/j.jat.2015.03.004).
The author-hosted journal PDF above is the citation version;
[arXiv:1501.01161v2](https://arxiv.org/pdf/1501.01161v2),
24 March 2015, was a readable comparison copy. Read the normalized
circle norms, Riesz projections and meromorphic classes, (17)–(19),
Theorem 4 and proof, Corollary 1 and proof, and all of Section 5.2.
For phi in L-infinity,

    H_phi: H2 -> H2_minus,  h |-> P_minus(phi h),
    s_k(H_phi) = dist_L-infinity(phi, H-infinity_k).

For continuous phi the operator is compact. Its norm is the k=0
distance, not the boundary norm of an arbitrary chosen representative.
The H-infinity-to-H2 operator A_f in (11) has a different domain;
its approximation numbers must not be substituted for s_k(H_phi).
For continuous strictly anti-analytic f, Theorem 4 gives

    dist_L2(f, R_(k-1,k)) >=
      min_(0<=j<=k) [s_j(H_f)/||v_j||_infinity] / sqrt(k+1),

for orthonormal singular vectors v_j; its stated bound is zero if a
required vector is unbounded. The proof uses orthogonality and a
finite-dimensional norm comparison. Section 5.2 reduces a coprime
proper rational p/q of degree m, with all poles inside the disk, to
a finite model space and a Hermitian matrix; it computes singular
values rather than bounding them uniformly from m and clearance.
The quoted statements are source inputs, not new local lemmas.

### Applicability, quantitative costs and limits

The nominated boundary function is continuous, since the closed-circle
regularity and nonvanishing boundary factors are explicit hypotheses.
Thus the bounded-symbol scope is available after scaling z=R*zeta.
There is no source-access blocker for Nehari/AAK. A future application
must still verify the full principal-part reduction and grid removals;
this source turn does not establish that new reduction.

Pole order and residue multiplicity are different parameters. The
proposed F has m=|Z| distinct simple poles, with residue sum M. The
standard rational degree/rank parameter counts m, not M. Enlarging a
positive integer residue does not create a higher-order pole. The
relevant amplitudes after division remain exactly
r_a B_n(x)/B_n(a), with complex phase; disk scaling also needs its
factor 1/R in simple-pole coordinates. Neither m nor eta bounds away
all other pole distances, and no separation assumption is available.

For the source identity itself the evaluation costs are:

| Parameter | What the inspected theorem actually supplies |
| --- | --- |
| Grid size n | No explicit bound; its effect is inside the symbol/amplitudes. |
| Distinct pole count m | A finite rational/model-space calculation of dimension m, if its proposed reduction is verified. |
| Total residue M | No positive-residue improvement in AAK or BCQ Section 5.2. |
| Boundary clearance eta | Interior poles are permitted; no evaluated eta-only lower bound on the required spectral norm. |
| L2 versus boundary norm | Different distances/operators; Theorem 4 retains spectral/vector-norm factors. |

These are limits of the inspected statements, not a theorem that a
useful uniform estimate is impossible. At n,M of logarithmic-height
size, an unevaluated matrix or singular value supplies no comparison
against a boundary upper bound. The nominal degree k in AAK is an
approximant pole budget; it is neither our grid size n nor the total
residue M. Taking a budget large enough to reproduce a rational symbol
cannot give a nonzero approximation-error lower bound.

The stronger explicit comparison in BCQ Section 5.3, Lemma 1 and
Theorem 5 (pp.28–30), concerns a Blaschke symbol. Read the finite-degree
proof: its decisive step is that H_conjugate(b) is an isometry on the
finite model space, giving unit nonzero singular values. No such inner
symbol or isometry is a hypothesis of our weighted family. Its printed
constants are not imported or used here. Section 5.4/(35), H1–H2,
requires an arclength density on a hyperbolic geodesic segment; read
those hypotheses only. Arbitrary moving discrete complex poles do not
meet them. Its Theorem 6 proof and resulting function-dependent
constants are not assessed for application here.

P. Chunaev and V. Danchenko, *Gorin's problem for individual simple
partial fractions*, [1907.07437v1](https://arxiv.org/pdf/1907.07437v1),
17 July 2019, defines rho_N=sum r_a/(z-a) with positive integer residues
and N=sum r_a. Theorem 1, (8), pp.2–3, has no real-axis pole, N>=4,
and gives, for every pole a and one absolute c>0,

    |Im a| ||rho_N||_L-infinity(real line)
      >= c [(log N)^(1/r_a)+1]/[(log N)^(1/r_a)-1]
             * log(log N)/log N.

This primary theorem was inspected, including the temporary symmetry
assumptions in Section 2.1 and their removal in Section 2.4. It concerns
the unweighted fraction and its full real-line norm. It does not
permit arbitrary holomorphic subtraction or inverse-grid complex
residues. No circle transformation or weighted generalization is
asserted. This useful terminology prevents a novelty inference from
searching only operator language. The 2015 SPF survey, Danchenko's
1995/2006 papers and Borodin's approximation papers remain leads,
not inspected matching theorems or necessary inputs for the nominated
weighted test.

### Search evidence, decision and continuation

Queries included `Nehari theorem Adamjan Arov Krein meromorphic
approximation Hankel operator rational symbol finite rank theorem pdf`,
`Hankel operator rational function poles residues norm lower bound
Blaschke product separation`, `Baratchart lower bounds L2 rational
approximation singular vectors Hankel Theorem 4 pdf`, `"Hankel"
"positive residues" norm`, `"logarithmic derivative" "Blaschke"
"approximation" lower bound`, `simple partial fractions lower bound
norm poles unit disk approximation positive integer residues Hankel`,
and `Danchenko simple partial fractions norm lower estimate circle
poles logarithmic derivative interpolation`. Search snippets located
sources only; mathematical comparisons above use the primary texts.

PDF screenshots timed out for the publisher/author URLs and shell
downloads failed DNS. Web text retrieved the actual primary papers;
BCQ's readable restatement fixed the essential AAK convention. No
unread formula is claimed inspected, and those access failures do not
block the bounded comparison. No mathematical script was run.

Reuse the derivative-free parent assessment and the named September
stops. The new comparison preserves C645d's exact scalar cancellation,
C645f's small-cluster restriction, and C645c's exact-product rate;
none gives the missing full spectral estimate. No other notebook was
read. Matching Mathlib coverage is unchecked; no homepage or search
failure is evidence of absence.

Outcome: informative source-scope negative for the identity-only
shortcut, not a negative theorem about every Hankel mechanism. The
main actual-Xi/all-degree-sign gap is unchanged. A possible useful
quantitative question survives and is posed, without a derivation, in
`drafts/literature/2026-11-01-positive-residue-hankel-exponent-test.md`.
It asks whether a sufficiently sparse growing pole census retains
half the exact grid exponent. This is different from scalar residue
noncancellation or a fixed three-moment bound. Essential source
coverage is now available; the new nomination still receives the
supervisor's separate approval before mathematics. No RH candidate,
full-pole estimate or verified novelty is claimed.
