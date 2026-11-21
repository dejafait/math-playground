# Source coverage for the interior Cartan certificate audit

TARGET: Audit L755's conditional Cartan selection and certificate-only failure, checking the changed-width logarithm and strip bounds, universal-constant calibration, complete-circle comparison, and uniformity in height, displacement and central multiplicity.
CHECKED: 2026-11-04
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 341 compared the full L755 with the two ready assessments below, L018, L266, L461 and the scoped step-339/340 records and paid-certificate stop. Reopened the primary Cartan definition, statement and complete one-variable proof case for its exact normalization; reused the existing exact-statement/stronger-result search rather than repeating discovery. No new search-based originality claim.
SOURCE_EVIDENCE: Goldstein--Schlag (2011), Definition 2.1 and Lemma 2.4, printed pp.347--349, equation (2.2) and complete d=1 proof case rechecked in the journal PDF on 2026-11-04. Reuse Titchmarsh (1986), Theorem 14.2 proof, pp.336--337, DLMF 5.11.1/5.11.3, and Liu 2610.12234v2 Corollary 33.2/Section 14 as precisely assessed below, with the register's unaudited-proof qualifications unchanged.
COMPARISON: The sources cover the analytic tools, not L755's quantitative specialization or stop. No direct theorem import validates the changed-width envelope, universal-constant lower calibration, parameter uniformity or certificate comparison. These are existing local claims for a separate audit; no new estimate or reproof is made here.
GAP: Source coverage is adequate for the exact audit. Still unverified are L755's complete conditional construction, its claimed uniform certificate excess and the direction K_actual<=K_cert. The desired actual-Xi cutoff, initial signs, outer layer and full positivity remain open.
REASON: The new scope comparison clears the literature gate for one conceptual audit of the existing proof. The implementation remains parked; the completed attempt is preserved and its quantitative stop is not certified by this review.
SCOPE: Exactly TARGET for fixed w=14998281/40000000 and 0<delta<w, L018's undeformed Xi, all sufficiently large heights with fixed-parameter existential onsets, arbitrary central multiplicity, and the registered conditional external premise. No new Cartan geometry, effective onset, boundary nonvanishing, sign theorem or actual-ratio obstruction is covered.
LITERATURE_REASON: This REVIEW_REQUIRED audit target newly asks whether the source's exact universal-constant normalization and changed-domain analytic mechanisms cover L755; the earlier attempt's ready assessment did not separately approve its audit. Reopen only the load-bearing Cartan passage and reuse the other adequate source assessments.

## Nomination retained from step 340 (not the current gate decision)

The exact target is a later audit, not a second mathematical exploration.
The next invocation first compares its essential scope with the reused
coverage in `2026-11-04-adaptive-interior-anchor-minimum-modulus.md`
and `2026-10-24-fixed-half-plane-witness-cutoff-coverage.md`. Do not
repeat general browsing or rederive L755 during that literature-only
approval step. If these sources adequately cover the precise audit,
record that with the correct classification; any missing source must
be named specifically. This REVIEW_REQUIRED nomination approves no
newly derived mathematics in the turn that derived it.

Essential local inputs are L755, L018, L266 and L461. The changed
external premise is exactly the rational-width statement retained in
L755 and `foundations/2026-10-quasi-riemann-input.md`; no boundary
nonvanishing or independently verified manuscript is assumed. L462
is historical contrast only and is not an input to L755. No sibling
notebook input is involved.

The decisive later audit checks are whether a generic universal
constant in (GS) must satisfy C_G>=1/log7, whether the small-loss
parameters and fixed-margin onsets are uniform as claimed, and whether
the bound K_actual<=K_cert has been kept in the correct direction.
Check the full relevant proof and quantifiers; a numerical sample or
documentation checker cannot validate these analytic claims. The
implementation stays parked during the audit. Initial Xi signs,
all-degree positivity and the desired actual ratio remain unresolved.

Full matching Mathlib coverage is unchecked. A later proof audit, once
its gate is ready, calls for proof_audit/conceptual_audit because of
the analytic normalization, exceptional-set selection and distinction
between a sufficient certificate and a necessary bound.

## Completed source-scope comparison, step 341, 2026-11-04

### Purpose and reused coverage

The main gap is actual-Xi mixed positivity and the initial Laguerre
signs. The intermediate target is the exact audit in TARGET. A valid
certificate-specific diagnosis would justify parking this implementation
and constrain what new quantitative input could reopen it; it would not
exclude a zero. This is source review, not the conceptual audit itself.

The ready assessments reused are
`2026-11-04-adaptive-interior-anchor-minimum-modulus.md` (EXPLORE) and
`2026-10-24-fixed-half-plane-witness-cutoff-coverage.md` (SPECIALIZE).
Their relevant primary passages and inspected proof cases are precisely
identified there. Both predate this invocation. L755 is within their
analytic technique scope, but its conclusions remain local assertions.
Reading its full proof here identifies source obligations, not a proof
verdict. L018 and L266 were read in full; L461's logarithm, strip,
circle and anchor sections were read for applicability comparison.

### Exact primary check and source boundaries

Goldstein--Schlag, *On resonances and the formation of gaps in the
spectrum of quasi-periodic Schrödinger equations*, Annals **173** (2011),
337--475, DOI 10.4007/annals.2011.173.1.9,
[Definition 2.1/Lemma 2.4, pp.347--349](https://annals.math.princeton.edu/wp-content/uploads/annals-v173-n1-p09-p.pdf#page=11):
the statement gives the radius-1/6 observation disk, center logarithm
normalization, and exceptional covering with total radii <exp(-H).
The complete d=1 proof case was inspected through its end on p.349;
it absorbs the additive growth-deficit term into an unspecified constant.
There is no printed value or lower calibration for C_G. L755's linear
test is a local claim for audit, not a quoted source conclusion.
The stronger disk-count refinement is unused; Levin (1996), Theorem 4,
p.79, remains an unread cited antecedent, not a new essential source.

Reuse [Titchmarsh, second edition (1986), Theorem 14.2 and proof,
pp.336--337](https://sites.math.rutgers.edu/~zeilberg/EM18/TitchmarshZeta.pdf#page=173)
only as the already inspected analytic-logarithm mechanism. Its theorem
assumes RH. It cannot directly establish a logarithm bound under Liu's
different half-plane. L755 supplies a changed-domain argument; the audit
must check its disk margins, logarithm branch, growth input and uniform
onset rather than treat the printed theorem as the asserted bound.
Reproof of that specialization is justified by changed hypotheses;
reproof of the generic source theorems is unnecessary.

Reuse [DLMF 5.11.1/5.11.3](https://dlmf.nist.gov/5.11)'s inspected
closed-sector/remainder coverage and L461's damping mechanism. These
cover tools for L755's strip argument, not its stated envelope on the
new disk. The audit must check reflection, compact real-part ranges,
both shifted heights, and the full complex circle, including the order
of rectangle and damping limits. Neither L461's old-width conclusion
nor a real-axis maximum substitutes for this check.

Liu [2610.12234v2, Corollary 33.2 and Section 14](https://arxiv.org/html/2610.12234v2)
is reused exactly as inspected in step 339 and retained in
`foundations/2026-10-quasi-riemann-input.md`. No new analytic or formal
verification of that manuscript is claimed. The changed rational width
is a conditional premise; its boundary is not excluded. No selected
anchor or reciprocal estimate follows just from nonvanishing.

### Later audit obligations and discriminating test

Check the full existing L755, not numerical samples, against these
obligations in one later mathematical audit:

1. The changed-width logarithm and strip envelopes must support its
   exact stated domains and fixed-parameter onsets. Distinguish constants
   depending on delta or nu from quantities allowed to vary with a,b.
2. The normalization must use the controlled exterior value, and the
   interval must lie in the observation disk after scaling. Check the
   exceptional-cover projection, strict noncoverage and multiplicity
   scope without assuming Xi(a) nonzero.
3. Test the existing universal-constant calibration in the exact (GS)
   form and quantifiers. The printed theorem supplies no numerical
   calibration; its availability does not validate this local test.
4. Check L266's actual maximum versus the chosen lower/upper models,
   the uniform coefficient comparison, ceilings and additive constants.
   A large sufficient upper certificate must not become a lower bound
   on an actual ratio or a least negative index.

Accept L755's conditional certificate-specific stop only if every
load-bearing claim survives those checks. Otherwise repair or qualify
the precise failure while retaining the original attempt and evidence.
No parameter tuning or second creative attempt is authorized here.
The stopped record `ATTEMPTS/2026-11-04-interior-cartan-paid-certificate-stop.md`
and step-339/340 histories were compared; L462 remains a contrast under
different fixed-anchor hypotheses, not an extra mathematical input.
No additional duplicate theorem was found or claimed in this review.

Essential continuation input IDs: L755, L018, L266 and L461. The
external-input qualification, possible boundary zeros, ineffective
fixed-margin onsets, initial signs and outer layer remain unresolved
or explicitly assumed as stated above. Full matching Mathlib coverage
remains unchecked; supporting analytic tools are not a matching theorem.
No cross-notebook input, new lemma, mathematical script, inequality
derivation or DAG/PROOF change was made. This is local coverage approval,
not a mathematical advance beyond the checked sources. Later routing:
proof_audit/conceptual_audit, with REPRODUCTION classification.
