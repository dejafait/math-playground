# Coverage: critical audit of the deeper-band arithmetic input

TARGET: Critically audit L459's conditional arithmetic moving-saddle margin on 13/16≤m/r≤7/8, including its enlarged logarithm disk, factorial normalization and complete relative contour budget.
CHECKED: 2026-10-24
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused exact-band queries, duplicate and failure comparisons in 2026-10-24-deeper-band-moving-saddle-coverage.md and L457 audit coverage; compared the complete L459 proof and the inherited L456 disk construction. No fresh broad search or claim of exhaustive coverage.
SOURCE_EVIDENCE: Reinspected DLMF 2.4.10–2.4.16 hypotheses and both half-path cases, and Temme 1308.1547v1 Sections 2.2–2.3 and 4.1, equations (2.9)–(2.13), (4.1)–(4.5). Reused inspected Titchmarsh–Heath-Brown (1986) Theorem 14.2/proof and Section 14.3, pp. 336–339, and DLMF 1.14.20, 25.2(i)/25.2.4, 5.11.3 via the named prior assessments.
COMPARISON: The enlarged 282/256 logarithm disk uses the same assessed interpolation mechanism on L456’s larger domain; the new power and all application estimates require audit. The saddle sources cover the method but do not assert uniformity for the varying paired-zeta exponent. No essential new theorem is needed for this critical verification.
GAP: Independently verify L459’s inherited logarithm domain, new interpolation and reserves, real saddle, factorial scale, inversion, both residues, every contour region and one uniform onset on the exact closed band; source approval is not mathematical validation.
REASON: Separate literature-only scope comparison supplies adequate coverage for the written proof’s critical audit, preserving the completed construction and all external trust qualifications; no source blocker remains for this exact audit.
SCOPE: Critical audit of L459 and its load-bearing L452/L456/L457 inputs on the stated real-r/even-m coupled domain only; no theta extension, every-height transfer, stronger sign theorem or external manuscript/import-closure audit.

## Original nomination, preserved

The paragraphs below record the nomination before this review. Their
REVIEW_REQUIRED condition is discharged by the completed comparison
below; they do not describe a second pending literature gate.

## Exact continuation and discriminating test

The main gap remains initial low-index signs and global mixed positivity.
The intermediate audit target is L459's full conditional arithmetic input;
its possible downstream use is a separately assessed matching theta
reduction, followed by an every-height transfer. Neither independent
step is established on this new band. The next invocation first compares
this audit's scope with the existing inspected primary mechanisms; it is
literature-only while DECISION remains REVIEW_REQUIRED. This nomination
does not approve or perform that audit in the construction turn.

Essential local inputs are L452's growth/logarithm mechanism, L456's
larger normalized-log domains and inversion, L457's bare factorial-scale
identity and audited contour method, and L459's complete new proof.
Retain the exact coupled a(r,m), positive real r, positive even m,
full S including zero cutoff equality, N=m+1, upward contour and
both original residues. The unchanged external premise is September 30
Theorem 1.1 at commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a`,
strict Re(s)>7/8 with the allowed pole at one and unaudited manuscript
and formal import closure. No boundary assertion or stronger premise
may enter silently. Full matching Mathlib coverage remains unchecked.

The critical audit, once separately approved, should continue only if
the normalized full complex logarithm really has the claimed larger
domain, all Cauchy/Taylor reserves survive, the real saddle is unique
on its stated interval, the factorial scale is positive with sublinear
logarithm, and the complete relative error tends uniformly to zero.
In particular inspect the shrinking annulus, fixed middle region,
both shifted-height-zero neighborhoods, both unbounded rays and both
residues, as well as fixed-parameter connector limits and one common
onset. A failed constant, missing hypothesis or incomplete contour
budget requires a precise correction or qualification of L459.
The exact-constant certificate is supporting evidence, not this audit.

Preserve the L323/L327, fixed-real-center, shrinking-domain and
fixed-r/unit-phase stops with their actual scopes. No matching full-band
arithmetic result was identified in the prior bounded comparison, but
this does not establish originality. Initial indices, bounded exterior
heights, mixed positivity and selected-law/regulator realization remain
independent unresolved assumptions for any larger route.

## Completed source-scope comparison — 2026-10-24

This step is LITERATURE / NOVELTY_UNCHECKED / EXPLORATION. It approves
coverage for the exact TARGET, not the correctness of L459. The next
mathematical audit is REPRODUCTION. No new theorem, lemma or mathematical
script was produced, and no main argument or DAG change is warranted.
LITERATURE_REASON: The new audit nomination required separate scope approval for L459’s enlarged logarithm disk and changed power, beyond L457’s old-band audit; unchanged primary assessments were reused.

### Inspected primary cases and reused evidence

Reinspected [DLMF 2.4(iii)–(iv)](https://dlmf.nist.gov/2.4#iii),
equations 2.4.10–2.4.16, on 2026-10-24. Hypotheses (a)–(c) require
analyticity near the contour, convergent endpoint expansions with
Re(lambda)>0 and mu>0, absolute uniform far-end convergence, and a
strict real-phase gap. The interior argument splits into two half-paths:
the nonstationary expansions cancel; the simple saddle retains the
Gaussian term with the direction-selected branch. The initially fixed
saddle does not certify this proof’s changing exponent or uniformity.

Reinspected [Temme, arXiv:1308.1547v1, 7 August 2013](https://arxiv.org/html/1308.1547v1),
Sections 2.2–2.3, (2.9)–(2.13), and Section 4.1, (4.1)–(4.5).
Gaussian reduction requires an analytic domain containing the path and
suitable growth/convergence at infinity; contour changes must avoid
singularities and branches. Section 4 warns that extra parameters can
change validity, convergence rates and contours. Section 4.1 separates
a nearby pole before expansion. These are method inputs, not a theorem
about L459’s arithmetic sum. The audit must retain both crossed residues.

Reuse the actual book inspection in
[the Littlewood assessment](2026-10-21-fixed-half-plane-endpoint-derivative-review.md):
Titchmarsh–Heath-Brown, second edition (1986), Theorem 14.2 and proof,
printed pp. 336–337, and Section 14.3, pp. 338–339. Its RH hypothesis
is not imported. Only the analytic-logarithm, Borel–Caratheodory,
three-circles and Cauchy mechanisms apply. L456’s proof supplies the
larger domain to be checked; L452’s narrower derivative theorem is
not a substitute. This turn did not reread the book or external manuscript.

Reuse the [inversion assessment](2026-10-23-subendpoint-relative-mellin-coverage.md)
and [L457 audit comparison](2026-10-23-lower-band-moving-saddle-critical-audit-coverage.md)
for DLMF 1.14.20 (continuity, piecewise continuous derivative,
exponential order and a rightward inversion line), 25.2(i)/25.2.4
(absolute Dirichlet convergence right of one and the unit-residue pole),
and 5.11.3/5.11(ii) (positive-ray Stirling with remainder). Their
hypotheses are unchanged. No general new uniform saddle theorem is
needed: checking the explicitly written estimates is the audit’s task.
Olver/de Bruijn and Flajolet–Sedgewick remain nonessential unread leads.

### Changed obligations, duplication and decision

Compared L459’s complete proof, including Mathlib and limitations,
with its construction assessment, L456’s normalized full-domain proof
and the prior L457 audit record. L459 is already the canonical local
statement; the next turn must audit it, not manufacture a duplicate.
The radius 282/256 and power 15/16 are the new claims, not imported
conclusions of the old radius-273/256 statement. Audit the Euler
normalization on the inner disk, the radius-284/256 logarithm bound,
outer zero-free/pole-free neighborhood, all new inclusion reserves,
reflected holomorphic logarithm and reserved Cauchy circles.

Then verify the unique real saddle and displacement, N=m+1 and the
bare factorial identity, positive orientation/root and |log M*|=o(r).
L459 Sections 3–6 require independent checking of full inversion and
cutoff equality, fixed-parameter connector limits, the central Taylor
error, quadratic shrinking-annulus decay, fixed middle region,
both shifted-height-zero neighborhoods, both infinite rays and both
original residues. Compare their sum with M*, with one common onset
on the closed band. The finite 17-check certificate was not rerun or
used as analytic evidence in this source review.

The construction assessment’s exact-sum searches and scoped failure
screen remain adequate for this unchanged mathematical statement.
L456 stops fixed-center freezing, L331’s models concern older regional
bounds, L323 concerns a theta-strip modulus certificate, L327 an AFE/Gram
replacement, and L335 fixed-r/unit-phase uniformity. None is a theorem
refuting the stated coupled moving-saddle target. Preserve their evidence;
this audit does not reopen those implementations. No matching external
arithmetic-margin theorem was inspected, and no novelty is inferred.

SPECIALIZE approves precisely this critical audit. Continue if every
load-bearing estimate is justified uniformly; otherwise record the exact
failed inequality, missing hypothesis or normalization and qualify or
repair L459 within the assessed scope. Do not approve a local Gaussian
term with an uncontrolled complement. No mathematical verdict is issued
here. Full matching Mathlib coverage is unchecked; absence is not claimed.
The pinned external premise and its unaudited proof/import closure remain
assumptions. Matching theta reduction and every-height transfer on this
band, initial indices, bounded heights, mixed positivity and selected-law
realization remain independent gaps. A successful audit supplies only a
validated conditional arithmetic input toward those separate tasks.
