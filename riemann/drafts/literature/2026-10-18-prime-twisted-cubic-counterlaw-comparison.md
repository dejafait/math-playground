# Proposed coverage review: one prime-twisted signed cubic

TARGET: Assess source coverage for comparing the sharp cos(t log 2)-weighted signed cubic of the actual critical jets with L429's complete counterlaw.
CHECKED: 2026-10-18
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 213 reused the inspected cubic assessments from steps 103/112/116/118, searched the specific October-14--18 literature/history/failure paths for the changed observable, and made the focused external queries recorded below. No completed comparison or matching full-statistic theorem was established; no novelty inference follows.
SOURCE_EVIDENCE: Reinspected Milinovich--Ng, author-hosted 19-page Lower_Bounds.pdf, Lemma 6.1 p. 9; Gonek (1984), section 3, Lemma 2 p. 130 and its saddle/endpoint/exterior proof; Sourmelidis--Steuding--Suriajaya 2007.14008v2, section 3 between (35)--(36), both branches; Fazzari 2306.15553v1, (1.3), Theorem 1.1 and (3.5); DLMF 25.11(i), 25.11.5. Reuse audited L406's absolute transfer and L407--L409's ordinary-jet and full-response coverage, and audited L429's complete-law bounds.
COMPARISON: The inspected tools permit a fixed rational-frequency specialization, including both cosine frequencies, rather than importing a theorem for the complete weighted statistic. The exact coefficient, denominator-two zero-carrier bookkeeping, full-tail passage and complete-law comparison remain separate mathematical obligations. Neither the unweighted cubic nor fixed-prime seconds decides them.
GAP: Evaluate or obstruct the actual-versus-unchanged-law coefficient difference with total error o((log H)^2), retaining both cosine frequencies, sharp endpoints, complete response tails, all three law components and the full corrections. No essential source is inaccessible for this bounded test; no coefficient, sign or separation is established here.
REASON: Approve source scope for one later SPECIALIZE proof attempt using the cited kernels and finite Hurwitz representation, with the explicit obligations below. This literature-only turn performs no coefficient evaluation or new lemma derivation; the newly written mathematical continuation receives separate supervisor approval.
LITERATURE_REASON: New sign-sensitive observable cos(t log 2) Delta Bcal, rather than a covariance weight or a fixed-prime second moment; its actual arithmetic coefficient and full-tail scope have not been assessed.
SCOPE: One fixed prime p=2, real cosine weight, sharp [H,2H] averages, complete actual response and the unchanged complete L429 law, with all sufficiently large real H; no increasing twist, conditional actual distribution or law redesign.

The main gap remains global mixed positivity. The intermediate target
for this review is a source-backed, independently testable comparison of

    H^(-1) integral_[H,2H] Delta(t) Bcal(t) cos(t log 2) dt

with the same observable integrated against L429's complete law, at
scale (log H)^2. No value, sign, existence of a limit or mismatch is
asserted here for either expression. No calculation for this target was
performed in step 212.

A separation could identify actual arithmetic information absent from
this particular counterlaw even after its fixed-prime second tests.
Equality or a vanishing separation would reject this diagnostic. Neither
outcome would establish actual clipping or repair the regulator margin;
rejecting one law would not rule out other moment-compatible laws.

Reuse existing primary coverage before searching further: L406's
absolute physical replacement and L407--L409's rational-frequency
and full-response arguments are the precise local leads. The review
must compare the actual cosine-weighted target to the imported signed
mean-value theorem, its frequency error and both carrier orientations.
It must not infer a weighted cubic coefficient from an unweighted one
or from Young's quadratic moment. Retrieve only the necessary primary
hypotheses and proof cases; inspect the relevant previous assessments
for both completeness and recorded failures.

Continuation test: approve a later bounded mathematical comparison only
if the necessary source coverage and a concrete full-tail/error route
at o((log H)^2) are documented, or an independently testable obstruction
to that route is specified. A coefficient separation must exceed the
proved remainder and include all three law components, the bounded
mean and full covariance correction. If essential coverage is missing,
record it; do not derive and approve the changed target in the review.

Essential local inputs for the prospective comparison are L406, L407,
L408, L409, L419, L421 and audited L429. L423 and L428 retain their
original scopes. Actual realization, actual clipping, capped
nondegeneracy, L413's full-error margin and global mixed positivity
remain unresolved. Mathlib coverage for this new observable has not
been checked, without an absence claim. No cross-notebook input is
proposed.

## Completed source comparison — 2026-10-18, step 213

The preceding proposal is preserved; this section supersedes its pending
coverage language. Outcome EXPLORATION records new bounded source-scope
work, not a mathematical advance or a coefficient determination.
No lemma, mathematical script, PROOF.md or DAG.md is changed. The main
gap remains global mixed positivity. This one intermediate diagnostic
could separate the actual cubic from this particular law, but cannot
by itself supply clipping, a regulator margin or an RH consequence.

### Discovery, reuse and recorded stops

Scoped searches used the literal cosine observable and the terms
`prime.twisted.cubic` and `weighted.signed.cubic` in the October-14--18
literature, histories and ATTEMPTS. Only the step-212 proposal matched.
Read the step-103 signed-cubic exclusions, step-112 finite-Hurwitz
assessment, step-116 full-response comparison and step-118 kernel audit
coverage. Read L406's hypotheses and absolute-transfer statement;
L407's exact ordinary-jet/carrier and analytic-weight sections;
L408's arbitrary fixed-rational pole interface; L409's kernel,
connectors, full-tail and resonance estimates; L421's unchanged rare
components; and L429's hypotheses, cutoff, full covariance/mean and
signed-bulk estimates. The full step-212 audit is reused, not repeated.

External locator queries were `"zeta" "cubic moment" "rational" twist
Gonek`, `"Hardy" "cubic" "twisted" cosine moment`, `"Milinovich"
"Ng" "Lower bounds" "6.1" chi`, `"zeta" "twisted third moment" fixed
twist`, `"Hardy" "cubic moment" "Ivic" twist`, and `"shifted triple
divisor" "Fazzari" correction`. These did not establish a matching
full-statistic theorem or a usable correction. Irrelevant search hits
and search snippets are not theorem evidence. No novelty or global
absence conclusion is drawn. Reuse the inspected exclusions rather
than importing Bui's explicitly unproved Theorem 5.1, an absolute
third-moment bound as a signed asymptotic, or a four-factor theorem.

L427's canonical failure record concerns W^3 f^2 for the unchanged
fixed mixture; L428 concerns uniformly bounded second densities.
They neither settle this cubic nor prohibit testing it. Preserve those
stops, L423's selected-list validity, L429's audited scope, and the
parked core/tail calculation. No cross-notebook source is used.

### Primary hypotheses and relevant proof cases

M. B. Milinovich and N. Ng, *Lower bounds for moments of zeta'(rho)*,
[author-hosted 19-page manuscript, Lemma 6.1, p. 9](https://home.olemiss.edu/~mbmilino/Lower_Bounds.pdf#page=9),
retrieved 2026-10-18, has no reliable printed version date. Read its
whole displayed remainder and proof attribution. For x>0 and fixed
kappa_0>0, uniformly for kappa_0<=kappa<=2, its chi(1-s)x^(-s)
primitive on [kappa+i,kappa+iV], divided by 2pi i, is

    indicator_{0<=x<=V/(2pi)} exp(-2pi i x)
      + O(x^(-kappa)[V^(kappa-1/2)
             + V^(kappa+1/2)/(|V-2pi x|+sqrt(V))]).

This analytic lemma is unconditional. Its subsequent GRH-dependent
character application is excluded. It supplies a single-frequency
kernel, not the response-summed cubic or its coefficient.

S. M. Gonek, *Mean values of the Riemann zeta-function and its
derivatives*, Invent. Math. 75 (1984), 123--141,
[section 3, Lemma 2, p. 130](https://www.sas.rochester.edu/mth/people/faculty/gonek-steve/assets/pdf/5-mvzdrvs.pdf#page=8):
read the statement and proof for large A, A<B<=2A, positive saddle
parameter and fixed exponent. The proof distinguishes interior saddles,
square-root-width endpoint neighborhoods and exterior saddles; its
complementary estimates use integration by parts. These cases justify
retaining transition denominators rather than asserting a fixed-twist
error uniform in all response indices. The correct section is 3.

A. Sourmelidis, J. Steuding and A. I. Suriajaya,
*Dirichlet Series with Periodic Coefficients and their Value-Distribution
Near the Critical Line*,
[2007.14008v2, section 3 between (35)--(36)](https://arxiv.org/html/2007.14008v2#S3):
read both gamma-exponential branches. The primitive assumes an absolutely
convergent series on Re s>1 with coefficients O_eta(n^eta) for every
eta>0, fixed q and a=1+epsilon. One branch has an additive-phase sum
and O(V^(1/2+epsilon)) error; the other is O(1). L407's fixed rational
support encoding is reused. This is no growing-q uniform theorem.

A. Fazzari, *A Voronoi summation formula for the shifted triple divisor
function*,
[2306.15553v1, 27 June 2023, (1.3), Theorem 1.1 and (3.5)](https://arxiv.org/html/2306.15553v1#S3):
reinspected the three independent shifts and full finite residue-class
decomposition, including nonunits and the zero class. The reduced
additive numerator and modulus must be coprime. Theorem 1.1 is a
Schwartz-weight formula, so is not imported for a sharp indicator.
Use (3.5) with L408's assessed smooth-first absolute endpoint transfer;
the previously flagged expanded polar display remains excluded.
No source supplies the complete signed jet coefficient.

[DLMF 25.11(i)](https://dlmf.nist.gov/25.11#i) gives the sole Hurwitz
pole, residue one; [25.11.5](https://dlmf.nist.gov/25.11.E5), Apostol
(1976), (25), p. 269, has Re s>0, s!=1, a>0 and nonnegative integer
cutoff. These are the fixed-progression analytic inputs already used
in L408. L406's Curran--Heycock power-three specialization and L391's
Bourgain/Cauchy connector coverage are reused without another broad
search or reproof. Full matching Mathlib coverage is unchecked.

### Bounded application scope, without a coefficient calculation

The real cosine has two fixed character frequencies. In the prospective
L407 expansion, their rational parameters are 2mn/k and mn/(2k)
for the single carrier, and 2mnk and mnk/2 for the zero carrier.
This identifies source parameters only; no weighted asymptotic is
proved here. Keep both signs even after taking the real projection.
The finite Hurwitz input covers each reduced fixed rational parameter.
Ordinary critical derivatives remain of order at most two, and the
complete chi kernel retains both exponential branches.

Do not put the oscillating cosine into L407's slowly varying analytic
weight: its derivative does not have the required 1/H size. Encode its
two characters in the rational frequency, retaining the original
analytic coefficients. Similarly, a signed-tail estimate does not
follow by multiplying L409's already integrated signed remainder by a
bounded cosine. The later proof must return to its frequency-level
estimates. The fixed factor two is within the cited positive-frequency
kernel's scope; summability and endpoint transfer still require an
explicit specialization. For the changed zero carrier, mnk/2 can be
half-integral. Retain its integer resonances and bound its nonresonant
near-integer terms on the denominator-two grid instead of quoting the
integer-only resonance proof verbatim. No new source theorem is needed
to test these bounded changes.

For the actual side use L406's absolute physical replacement with the
bounded test, then L407's exact zero/single-carrier algebra. At fixed
response head use L408's arbitrary-rational Hurwitz mechanism, retaining
all jet monomials and sharp boundary mass. For the complete response,
check L409's summable connector and frequency-error majorants for each
of the two parameters before taking H first and then the fixed head
to infinity. This is a concrete error route, not a claim that the
new coefficient or its sign follows from beta or from second moments.

For the law side retain L421's unchanged high and intermediate kernels
and L429's complete translated six-state bulk. The available interfaces
are L421 (4)'s high cubic bound, its (5)'s exact intermediate calibration,
and L429's exact conditional signed-bulk identity and integrated norm
bound in its remaining-moments section. They are stronger information
than the selected unweighted cubic alone. The later attempt must check
their weighted use, including the exact bounded mean, every entry of
A_H, normalization and the all-real-height cutoff. No law value or
limit is asserted in this source review, and no law redesign is covered.

Continue only if the actual and complete-law normalized coefficients
can be compared with rigorously vanishing errors, or if a specific
failure of this frequency-level route is established. A nonzero
coefficient difference rejects only adding this observable to this
unchanged law. Equality rejects this leading-scale diagnostic. Stop
the claimed comparison if a tail, endpoint, resonance or correction
is uncontrolled; do not infer equality from overlapping numerical
enclosures. Actual realization, actual clipping, capped nondegeneracy,
L413's full-error regulator margin and global mixed positivity remain
independent gaps. A separate ready continuation is saved in
`2026-10-18-prime-twisted-cubic-coefficient-test.md` for supervisor
approval before mathematics. No exploration calculation budget was used.
