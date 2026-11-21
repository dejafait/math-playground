# Original angular mean: completed bounded source comparison

TARGET: Test whether |mu_n|>=exp(-n/100) holds along an unbounded subsequence for mu_n=mean_(|u|=1)c_0(u) of the fixed L703 family, retaining the complete signed constant-mode residue sum and anchor.
CHECKED: 2026-11-03
DECISION: EXPLORE
SEARCH_EVIDENCE: Step 213 searched rational angular means, Blaschke quotient constant coefficients, averages of ratios and contour noncancellation; inspected Borichev--Fouchet--Zarouf 2107.00405v1 Theorem 1(1), its complete fixed-k proof and Theorem 2(2), and reused the previously inspected Fourier/residue and analytic-saddle assessments. Checked C645o/C645p, working steps 86/87 and 212 and their stops. No matching theorem was found in this bounded search; no novelty or exhaustive absence claim.
SOURCE_EVIDENCE: Borichev--Fouchet--Zarouf arXiv:2107.00405v1, 1 July 2021, pp.1--2,9,12,18, Theorem 1(1), Theorem 2(2), Section 3.1 fixed-k proof; https://arxiv.org/pdf/2107.00405v1 . Reuse Levitt Theorem 1.3/Exercise 1.2 and Theorem 1.11/Corollary 1.12, Howell--Mathews Theorems 8.1.5/8.1.7, and Pemantle--Wilson 0903.3585v1 Theorem 2.3/Corollary 2.4 as qualified below. DLMF 2.4 was consulted as a contour-hypothesis cross-check, not a lower-bound input.
COMPARISON: The inspected fixed-factor theorem concerns analytic powers of one Blaschke factor, not a spatial sum of n-dependent meromorphic quotients with correlated inverse angles. Residue/Fourier identities describe the scalar mean but supply no lower magnitude; analytic saddle expansions require verified contours, uniform errors and noncancellation. The continued-origin stop and negative-mode coordinates do not decide this constant coefficient.
GAP: Bound the complete actual angular mean at the stated subsequence rate with fixed L703 selections and all original endpoints and unit masses; anchor cancellation, any reflection, contour dominance and triangular-array uniformity remain unproved.
REASON: Essential bounded comparison is complete for one direct constant-mode noncancellation attempt using ready residue/Fourier tools; no matching quantitative theorem can be imported. This is coverage for the preserved research target, not a derived estimate or mathematics in this turn. Newly ready scope receives separate next-turn approval.
LITERATURE_REASON: The observable changes to the original zero angular Fourier coefficient, for which the anchor survives; its noncancellation is not covered by the ready negative-mode assessment or the origin-evaluation stop.
SCOPE: Exactly TARGET with one actual L703/L708 profile fixed before n=12q+3 varies, M=n/3, unit spatial masses, normalized angular measure and L666's unmodified c_0 and D. Covers one bounded complete signed residue/contour test; assumes no symmetry, sign, saddle dominance, profile-uniform constants or realization.

## Intended relevance and review boundary

The main gap is actual-Xi all-degree mixed positivity. The proposed
mean bound is a sufficient scalar route to the same E_0/D comparison
using the standard constant-mode projection and L661's recorded
diagonal envelope. Step 212 records the sufficient squared-energy
threshold C*n^3*exp(-261*n/10000); the remaining polynomial margin
must be checked if the mean estimate is established. Global charge,
H/support, realization and signs would
remain independent gaps even after such an estimate.

Keep precisely L666's c_0 and D and fix the actual L703/L708 profile
before n=12q+3 varies. Preserve M=n/3, the anchor, unit masses, inverse
angle, j=0 factor and both endpoints. The target is existential on an
unbounded subsequence, not eventual positivity or nonvanishing.
Do not replace mu_n by c_0(0), c_0(infinity), a magnitude envelope or
a differently weighted mean. Any reflection property must be justified.

Essential inputs are L666 and L703/L708; L661 supplies only its audited
original-D envelope. C645o/C645p are unaudited leads: justify any scalar
mean formula used directly. Actual mean noncancellation is unresolved.
L725's interior limsup supplies no constant angular coefficient. No
cross-notebook result is proposed.

The invocation-start TARGET asked to assess known coverage for this
same bound. TARGET now states its mathematical continuation; the mean,
threshold and subsequence quantifier have not changed. No identity,
inequality or asymptotic is derived in this literature-only step.

## Scoped duplicate and failure check

Read L666's exact hypotheses/scalar interface, L703/L708's fixed-profile
hypotheses/conclusions, L661's recorded envelope, C645p Section 1 and
C645o Section 2 including pole/cancellation cases. The latter two
corollaries remain unaudited leads; verify any scalar specialization
directly from L666 and the standard cited tools before using it.

The origin stop is preserved in
`ATTEMPTS/2026-11-03-low-moment-origin-closure-overlap.md` and working
step 87. Its costly pole-clearing transfer is not a result about this
mean. Working step 86's bounded-coefficient propagation stop does not
assert an actual-profile extremizer. Working step 212's negative-mode
coordinates retain the unpaid actual-vector problem and annihilate
the anchor. Merely changing their basis repeats that attempt. These
stops retain their scopes; none bans the present constant-mode test.
No duplicate estimate was found in these specific paths; no global
absence claim is made.

## Primary statements and reading limits

A. Borichev, K. Fouchet and R. Zarouf, *On the Fourier coefficients
of powers of a Blaschke factor and strongly annular functions*,
[arXiv:2107.00405v1](https://arxiv.org/pdf/2107.00405v1), 1 July 2021:
read definitions pp.1--2, Theorem 1(1), p.9, Theorem 2(2), p.12,
and the complete fixed-k induction in Section 3.1, p.18. For fixed
0<lambda<1 and fixed integer k>=0, Theorem 1(1) states

    hat(b_lambda^n)(k) ~ (-lambda)^(n-k)
                            *[n*(1-lambda^2)]^k/k!,
    b_lambda(z)=(z-lambda)/(1-lambda*z).

These are analytic Taylor coefficients. Theorem 2(2) covers the central
range alpha_0*n+omega<=k<=alpha_0^(-1)*n-omega, with
alpha_0=(1-lambda)/(1+lambda), omega/n^(1/3)->infinity, omega=o(n),
and has an oscillatory cosine; its full proof was not audited. Neither
statement treats our meromorphic quotient sum. The fixed-k proof uses
derivatives at zero of an analytic power. It cannot justify identifying
our mean with continued evaluation. No lower bound for mu_n is imported
from this paper.

Reuse the inspected primary inputs in
`2026-11-02-rotation-averaged-anchor-line-hankel.md` and
`2026-11-03-exact-pole-residue-angular-gram.md`:

- A. Levitt, *Analyse de Fourier et applications*,
  [author PDF](https://www.imo.universite-paris-saclay.fr/~antoine.levitt/blog/fourier/article.pdf),
  version retrieved 2 November 2026, Theorem 1.3/Exercise 1.2 and
  Theorem 1.11/Corollary 1.12, printed pp.6,8 (PDF pp.12,14), with
  completeness proof previously inspected. These cover normalized
  scalar L2 constant-mode projection, not a lower bound for its value.
- R. W. Howell and J. H. Mathews, *Complex Analysis*, online edition,
  front matter updated 22 August 2025,
  [Section 8.1, Theorems 8.1.5 and 8.1.7](https://complexanalysis.org/web/sec_residue-thm.html).
  The residue theorem/simple-pole rule give exact integrals after
  verifying every pole, including the origin and cancellations.
  They supply no positivity or lower magnitude of the signed sum.

No general-tool reproof is justified. The application difference is
quantitative noncancellation of the prescribed scalar sum.

Reuse the inspected saddle comparison in
`2026-11-03-signed-bump-remainder-rate.md`, primary-source item 1:
R. Pemantle and M. C. Wilson, *Asymptotic expansions of oscillatory
integrals with complex phase*,
[arXiv:0903.3585v1](https://arxiv.org/pdf/0903.3585v1), 20 March 2009,
Theorem 2.3/Corollary 2.4, PDF pp.4--5, with deformation/localization
and boundary cases previously read on pp.10--14. Hypotheses: compact
oriented real-analytic stratified d-space in C^d, analytic amplitude
and phase, Re(phi)>=0, finitely many stationary points in the zero-real-
part locus, interior with nonsingular complex Hessians; the corollary
allows its specified halfspace boundary case. Contributions add and
can cancel. No uniform conclusion for our growing product and spatial
sum is supplied. The Gaussian normalization remains unaudited as
recorded; no prefactor is imported here.

[NIST DLMF Section 2.4](https://dlmf.nist.gov/2.4), especially
2.4(iii)--(vi), was consulted for analytic-contour, complementary-gap
and coalescence qualifications already recorded in that assessment.
It supplies no legal deformation or dominance for our mean. Its
coalescing-pole book references remain unread leads, not essential
blockers or accepted target theorems.

## Search record

Queries actually issued:

- `rational function constant Fourier coefficient angular mean positive residues Blaschke quotient cancellation asymptotics`
- `"angular mean" "rational" "residue" constant coefficient`
- `rational functions contour integral noncancellation asymptotic saddle point coalescing poles`
- `"Blaschke" "quotient" "constant" "Fourier coefficients"`
- `"average" "ratio" "Blaschke products"`
- `"2107.00405"`

Search snippets, secondary discussions and generic integral tutorials
were not theorem evidence. General analytic-combinatorics and other
asymptotics hits were not inspected as new inputs: adequate general
saddle coverage was already available. No essential source-access
blocker remains for the proposed residue/Fourier test. Not finding
an exact match does not establish novelty.

## One bounded continuation, after separate approval

Test the complete signed constant-mode residue sum at TARGET's scale.
First justify the scalar mean formula directly from L666 and the
standard residue theorem, including the anchor, origin and cancelled
pole cases; do not accept C645o/C645p wholesale. The substantive test
is whether this complete sum, using the fixed actual e_m rather than
unrelated coefficients, has lower magnitude exp(-n/100) on an unbounded
allowed subsequence. A contour treatment must include every crossed
residue and make its error smaller than its retained signed main term.
No dominant saddle, reflection law or common sign is assumed.

Continue with that bound or a paid intermediate estimate specifying
the remaining exponential loss. An obstruction for the actual mean
would stop this sufficient scalar test, not RH. Stop and reassess if
one attempt only restates the residue identity, substitutes c_0(0),
returns to the old pole-clearing origin cost, or uses ambient propagation
without actual-profile control. Finite samples, reality or identity-
theorem nonvanishing are insufficient. Independent global charge,
H/support, realization and signs remain unresolved after success.

Mathlib: full matching coverage for this subsequence noncancellation
target was not checked; general Fourier/integral support is not a
matching theorem. No lemma, mathematical script, PROOF or DAG change
is made in this literature-only step.
