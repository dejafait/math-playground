# Interior-anchor minimum-modulus source review

TARGET: Assess whether Cartan minimum-modulus selection can supply L266's complete circle-to-anchor bound at an interior anchor, uniformly for hypothetical Xi zeros a+ib with 0<b<=w-delta, yielding K<=ceil((w/2-delta/8)log(2+|a|)+B_delta), where w=14998281/40000000 and 0<delta<w is fixed.
CHECKED: 2026-11-04
DECISION: EXPLORE
SEARCH_EVIDENCE: Step 339 completed the bounded exact-statement/stronger-result search and reused the local Cartan/Remez assessment named below. Read the directly relevant witness/anchor proofs and fixed-anchor failure. Inspected primary analytic small-value theorems and their relevant proof cases; no matching selected-Xi cutoff was found in the sources checked. Queries, retrieved passages and uninspected leads are distinguished below; no originality claim.
SOURCE_EVIDENCE: Il'yashenko--Yakovenko, JDE 126 (1996), Sections 1.1, 1.3--1.4, Lemmas 1--3, printed pp.92--98, including the complete zero-factor/Harnack/Cartan proof; Goldstein--Schlag, Annals 173 (2011), Definition 2.1 and Lemma 2.4, pp.347--349, one-variable statement/proof case; Brudnyi math/9908105v1, Theorem 1.1 and Remark 2.2. Liu 2610.12234v2 Theorem 27.1, Corollary 33.2 and Section 14 transfer rechecked only for the stated domain; retain the register's external-proof qualifications. Reuse the existing Titchmarsh/Stirling assessment, without another audit.
COMPARISON: Known Cartan theorems allow zeros and exceptional disks at every fixed height, but charge a growth deficit or multiplicity count and require a nonzero normalization away from the hypothetical zero. Remez charges a function-dependent degree. None supplies the stated coefficient w/2-delta/8 or a full-circle Xi ratio. L461/L468 remain exterior-anchor results; L462's fixed exterior-anchor stop does not cover the proposed interior selection.
GAP: The uncovered mathematical task is to normalize actual Xi without dividing by Xi(a), quantify the local growth and all exceptional-disk losses, select s in the required interval, and compare the resulting complete-circle ratio with the exact cutoff uniformly in a,b and central multiplicity. Source access is adequate for one bounded attempt; the saving, or an obstruction to this implementation, remains to be established there.
REASON: The new mechanism tests actual-function adaptive selection rather than abstract backward positivity. A success could shorten the initial-sign workload for the specified inner zero layer, leaving initial signs and the outer layer unresolved. EXPLORE licenses a test of an uncovered inequality, not a theorem application with the desired conclusion assumed; step 339 itself is literature-only.
SCOPE: Exactly TARGET and its displayed test below, fixed 0<delta<w, L018's undeformed Xi and the registered external-input qualifications. One later bounded mathematical attempt, after the supervisor's separate approval of this changed assessment. No new result is derived in this review; no effective onset, interior reciprocal subpower bound, smaller global zero strip or coefficient sign is imported.

## Exact proposed test, not an asserted estimate

Use L018's Xi normalization and L266's notation
H_a(y)=Xi(a+iy)Xi(a-iy), T=2+|a|. Retain the external register's
trust qualifications. The proposed w is the Xi width corresponding
to Liu's registered rational boundary 34998281/40000000; the boundary
itself is not excluded. This choice prevents counting the already
known tiny global-width improvement as evidence for a new mechanism.

For each fixed delta in (0,w), consider hypothetical zeros a+ib
with 0<b<=w-delta. The proposed input is existence of an anchor
s in (b,w-delta/2), a radius s<R<1/2 and A>0 satisfying
H_a(s)>=A, with M=max_(|y|=R)|H_a(y)| and

    K=ceil(log(2M/[A(1-s^2/R^2)])/(2log(R/s)))
      <=ceil((w/2-delta/8)log T+B_delta).

B_delta must be finite and independent of a, b and coincident real
zero multiplicity; an existential height onset independent of those
variables is allowed if stated. Quantitative separation and support
of exceptional disks, the available anchor interval, all logarithmic
losses and the entire complex circle must be accounted for together.
Do not replace M by a real-axis maximum or divide by Xi(a).
No such anchor, A, R or bound has been constructed here.

If source comparison supports this test, the later mathematical task
would have one falsifiable inequality rather than another general
sign conjecture. Its downstream use is a shorter sign segment needed
to exclude this specified class of hypothetical zeros. Initial signs,
the remaining outer-edge layer, all-degree mixed positivity, bounded
heights and source correctness remain unresolved. An upper bound on
a negative witness does not conflict with positivity of a higher-order
tail, and must never be presented as such a contradiction.

## Recovery comparison: three mechanisms (nomination retained)

1. **Abstract Gaussian backward comparison: park.** L754's step-338
   audit verifies the complete realized crossing. The preserved record
   is ATTEMPTS/2026-11-04-neutral-gaussian-abstract-backward-comparison-stop.md.
   More abstract anchors or finite spectral models do not supply the
   missing arithmetic derivative inequality.
2. **Short arithmetic multiplier realization: do not repeat.** The
   scoped step-261 audit history and
   ATTEMPTS/2026-11-04-short-arithmetic-bump-projection-stop.md record
   L737's checked vanishing projection in its stated range. L639's
   growing-jet audit is also complete despite the overview's older
   annotation. No changed length regime or Gram estimate has been
   supplied to reopen either dictionary. L727's tail-only signing
   limitation likewise remains recorded, rather than queued for audit again.
3. **Selected actual-function interior anchor: nominate source review.**
   This changes the mathematical input to a minimum-modulus existence
   bound on a same-height segment, with its exceptional sets paid.
   L462 stops a fixed-anchor small-tail comparison at its stated
   threshold; it does not prove this selected-anchor estimate or rule
   it out under changed parameters. L468 approaches the global strip
   edge from outside and supplies no such interior lower bound.
   Those stops are evidence to compare, not a global prohibition.

The nomination required inspecting a primary Cartan theorem and relevant proof cases before
attempting any selection or power comparison. Check exact-statement
and stronger-result duplicates and countermodels, including whether
arbitrary close zeros on the same horizontal segment make the loss
too large. A result only outside exceptional heights is inadequate
for the stated every-hypothetical-zero target. If the required loss
exceeds the displayed cutoff, record that obstruction and park this
implementation; neither rename it nor repeat retrieval without a new lead.

At nomination, the creative attempt was not ready: primary minimum-modulus
coverage and an actual-Xi quantitative saving had not been established.
Step 339 below supplies technique coverage for testing the saving, without
establishing it. The earlier nomination approved no mathematics in the
completed L754 audit turn. Full matching Mathlib coverage remains unchecked.

## Step 339: completed literature-only comparison, 2026-11-04

### Main gap, use and the boundary of this review

Actual-Xi all-degree mixed positivity and the required initial Laguerre
signs remain open. The exact proposed cutoff is an intermediate target,
not a sign theorem: with L266 it would reduce the finite list of signs
sufficient to exclude a hypothetical zero in the specified inner layer.
No source inspected proves those signs. This step derives neither an
anchor nor a new Xi estimate. The mathematical application, including
any quantitative obstruction, belongs to a later turn.

### Primary sources and essential cases read

1. Yu. Il'yashenko and S. Yakovenko, *Counting Real Zeros of Analytic
   Functions Satisfying Linear Ordinary Differential Equations*,
   J. Differential Equations **126** (1996), 87--105,
   [author PDF, Sections 1.1, 1.3--1.4, pp.92--98](https://www.wisdom.weizmann.ac.il/~yakov/jde-95.pdf#page=7).
   For a simply connected Green domain U, compact K inside U, nonzero
   f analytic in U and continuous on its closure, write M=max_cl(U)|f|
   and m=max_K|f|>0. Lemma 3 provides geometry-dependent positive
   alpha,tau: for 0<h<1, outside finitely many disks of total diameter
   <h, on K one has |f|>=m(m/M)^(alpha-tau log h).
   The entire proofs of Lemmas 1--3 were read: Jensen counts zeros
   with multiplicity, Harnack treats the zero-free quotient, and Cartan
   treats its monic zero polynomial. No ODE hypothesis is used here.
   Constants depend on the domain/compact pair, not just h. The proof's
   displayed polynomial constant and its final logarithmic constant
   should not be used as a sharp numerical normalization without replay;
   this review relies on the stated existential constants only.

2. M. Goldstein and W. Schlag, *On resonances and the formation of gaps
   in the spectrum of quasi-periodic Schrödinger equations*,
   Annals of Mathematics **173** (2011), 337--475,
   [Definition 2.1 and Lemma 2.4, pp.347--349](https://annals.math.princeton.edu/wp-content/uploads/annals-v173-n1-p09-p.pdf#page=11),
   DOI 10.4007/annals.2011.173.1.9. In the one-variable unit disk
   centered at z0, let U0>=sup log|phi| and l0<=log|phi(z0)| be finite.
   For H sufficiently large the lemma gives log|phi|>U0-CH(U0-l0)
   on the concentric radius-1/6 disk outside disks of total radii
   <exp(-H). Its stated complexity is CH(U0-l0); the one-variable
   proof gives the stronger count C(U0-l0), with multiplicities
   retained. Read the normalization and one-variable proof through
   p.349. It cites Levin, *Lectures on Entire Functions* (1996),
   Theorem 4, p.79, and the proofs of Theorems 3--4 for disk overlap.
   Levin itself was not separately retrieved. The later multidimensional
   induction and spectral applications are not used. The center must
   be nonzero; this is not a normalization at Xi(a)=0.

3. A. Brudnyi, *On Local Behavior of Analytic Functions*,
   [arXiv:math/9908105v1, 19 August 1999](https://arxiv.org/pdf/math/9908105v1),
   Theorem 1.1, p.2; Definition 1.5 and Remark 2.2, pp.3,6.
   For f holomorphic on the complex ball of radius r>1 and a real
   interval I in the unit ball, positive-measure E within I satisfies
   sup_I|f|<=(4|I|/|E|)^d sup_E|f|, with finite d=d(f,r).
   Remark 2.2 relates d to a Bernstein index with geometry-dependent
   constants. This is comparison coverage, reused from step 204, not
   a family-uniform Xi degree bound. Its earlier [Br2] input remains
   uninspected and is not essential to the Cartan test. Corollary 1.10
   is not used; retain the earlier normalization qualification.

4. B. Liu, *Improved zero-free half-planes for the quasi-Riemann
   hypothesis*, [arXiv:2610.12234v2](https://arxiv.org/html/2610.12234v2),
   12 October 2026, Theorem 27.1, Section 14's factorization/pole
   case and Corollary 33.2 with its proof were inspected for domain
   matching. Corollary 33.2 states strict Re(s)>34998281/40000000;
   Theorem 27.1 has a slightly stronger algebraic boundary. Use the
   rational boundary already fixed in TARGET, not a new smaller width.
   The section-14 transfer includes zeta; no boundary nonvanishing or
   selected-point lower bound follows from this statement. The full
   analytic proof/formal import closure remains unaudited, exactly as
   in `foundations/2026-10-quasi-riemann-input.md`.

### Changed-scope applicability and what a citation cannot do

These Cartan estimates concern the bad set in the function's complex
variable, rather than a discarded set of heights. Their statements
therefore do not inherently impose an exceptional-height restriction.
For a later Xi application, disk support, scaling and the intersection
with the allowed real-y interval must still be checked explicitly.
No such selection is performed in this source review.

The source quantity m=max_K|f| is not an available anchor lower bound
when K is only the desired segment. Treating it as one would be
circular. A later argument must place a separately controlled exterior
point in its compact geometry or use a controlled nonzero disk center,
and then pay for propagation into the interior. It must specify a
holomorphic normalization preserving the relevant zeros. Ordinary
nonvanishing at some point supplies no uniform quantitative l0.

The sources count repeated zeros and permit arbitrarily close distinct
zeros. Thus they do not need a simplicity/separation assumption, but
their loss can depend on the full multiplicity count or growth deficit.
They supply no cancellation of that loss at central zeros. If the
later application uses only a bound O(log T) for the deficit, its
unspecified coefficient cannot certify the requested strict saving.
The geometry constants must be quantified or eliminated for that use.

Neither Cartan nor Remez bounds the full circle required by L266.
Reuse the complex Stirling and strip-growth mechanisms already covered
in `2026-10-24-fixed-half-plane-witness-cutoff-coverage.md`, but verify
their changed domains. In particular, L461's circle conclusion has
an exterior radius and cannot simply be invoked for a smaller radius
inside the new width; L468's conclusion uses the old 3/8 premise.
No interior reciprocal subpower estimate follows from the zero-free
register. Preserve the exponential decay at both shifted heights,
and do not replace a circle by its two real endpoints.

The necessary mathematics is a changed-domain application with exact
loss accounting. Merely reproving the generic Cartan theorem or
substituting the rational width into an exterior-anchor theorem would
not address TARGET. A future reproof is justified only for constants,
geometry or uniformity that the printed theorem does not supply.

### Duplicate/failure comparison and bounded search record

The scoped search used local witness/anchor assessments and ATTEMPTS,
then the relevant proofs: L018 and L266 in full; L461's logarithm,
circle and anchor sections; L468's statement/setup; L462's statement
and two-radius mechanism. Its retained stop is
`ATTEMPTS/2026-10-25-interior-anchor-small-tail-comparison.md`.
The earlier primary Cartan/Remez coverage is
`2026-11-03-complete-response-angular-log-propagation.md`, Sections
"New primary readings and their limits" and search record. That target
was a rational-family angular trace, not the actual Xi interior-anchor
cutoff. Reusing techniques does not transfer its conclusion. No sibling
notebook or additional lemma catalog was read.

New web queries included:

- `Cartan minimum modulus theorem analytic function disk log M f 0 exceptional disks proof`
- `Cartan minimum modulus theorem Levin holomorphic functions H polynomial disks total radii`
- `Cartan estimate analytic function log M m Lemma Goldstein Schlag H proof pdf`
- `"Xi" "Laguerre" "minimum modulus" zeros`
- `"Riemann" "Cartan" "minimum modulus"`
- `"Laguerre" "negative" "witness" "Cartan"`
- `"Riemann xi" "anchor" "minimum modulus"`
- `"zeta" "Cartan" "horizontal segment"`

A retrieved [rStation discussion, author halasz_resonator,
16 October 2026, "Chosen-Circle Derivative Bound"](https://rstation.ai/r/riemann_hypothesis/posts/6)
was screened at its local-count/Cartan/derivative passage. It concerns
a Blaschke product of selected near-Re(s)=1 zeros and a derivative
of a divided zeta function. It states neither this Xi anchor estimate
nor this cutoff and is not imported as a theorem. Its source chain
and proof are unverified here. Other search leads, including Levin's
book and minimum-modulus results for disk-order classes, were not
read and are not represented as inspected coverage. Failed TIFR URLs
and one screenshot timeout are nonessential: the two primary PDFs'
relevant theorem/proof text was accessible through the web tool.
Direct shell download failed DNS; no source-access obstruction to the
stated test remains. No inference of novelty from these searches.

### One bounded continuation and its stop test

The unchanged TARGET is now covered for one exploratory mathematical
attempt, subject to the supervisor's separate approval of this changed
assessment. Its new mechanism is adaptive selection for the actual
function at the same height, not another abstract positive-kernel
comparison. The attempt must preserve L266's exact logarithmic ratio
and the specified rational w, uniformly for b<=w-delta and central
multiplicity, with all parameters fixed before a varies except the
explicitly selected anchor/radius. First quantify the source loss;
do not assume it is subpower or below the threshold.

Continue only if that complete ratio yields the displayed cutoff with
a finite B_delta independent of a,b and central multiplicity, or if a
sharply identified partial estimate provides a different falsifiable
target for separate review. Park this implementation if the paid loss
cannot meet the cutoff, if the allowed segment can remain entirely
exceptional under the available quantitative data, or if the bound
works only outside exceptional heights. Failure to certify the bound
is not a disproof of its truth for Xi. Repeating Cartan with renamed
parameters after such a failure needs a materially new input.

No new lemma or mathematical script was written. Full matching Mathlib
coverage for this selected-anchor assertion and the Cartan versions
above is unchecked; supporting analyticity/Cauchy results are not a
full match. RH, initial signs, bounded heights and the outer-edge
layer remain open. Outcome: bounded source EXPLORATION, not a new
mathematical result, imported cutoff or quantitative route rejection.
