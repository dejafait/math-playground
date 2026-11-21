# Compact-width signed mixing: uncovered continuation1527

TARGET: Review compact-width signed mixing of C032j's laws over sigma in [1,2], checking measurability, uniform entire-lift hypotheses and whether a mass-one finite signed mixing measure can cancel the full odd transform.
CHECKED: 2026-11-18
DECISION: REVIEW_REQUIRED
SEARCH_EVIDENCE: Review1528 searched exact signed smoothed-Xi mixtures, continuous-mixture identifiability, integral independence of exponentials of entire functions, holomorphic parameter integrals and measurable probability kernels; read C032j/k/l, review1301 and stop1302. The bounded search found no matching signed odd-transform uniqueness theorem; queries and actual reads are recorded in source-notes1528 below.
SOURCE_EVIDENCE: Reuse fixed-v1 source interfaces from reviews1299/1301. Newly inspect Sra2611.00345v1 LemmaA.4 and complete proof/p13 and Proposition3.1 proof/p21; Haslinger Complex Analysis notes Theorem2.39 and full proof/pp67-68; Powers-Xu2025 Definition1 and Theorem1/full proof/pp520-522. Exact links and qualifications are in source-notes1528. The large MIT probability-kernel source was not retrieved in full.
COMPARISON: The analytic integration theorem is conditional on measurable sections and uniform integrable domination; an individual-width estimate does not verify those premises. Powers-Xu requires a transform reparameterization and treats probability mixing densities; neither its applicability nor an arbitrary signed reflected-family extension has been verified. C032l excludes only finite mixtures.
GAP: The full mass-one signed cancellation question and probability-kernel source comparison remain uncovered. A separate, narrower specialization can test compact-width analytic bounds without asserting a measurable probability kernel or uniqueness; its new assessment is drafts/literature/2026-11-18-compact-width-entire-lift-uniformity-1528.md.
REASON: Complete one literature-only source comparison after nomination1527. Keep REVIEW_REQUIRED for the broad target rather than approving uncovered measure or uniqueness claims; nominate an independently testable analytic prerequisite with inspected sources. No new mathematics is derived in this review.

## Proposed class, not an established construction

Retain C032j's probability laws nu_sigma and all fixed-v1 preprint,
actual-divisor, counting and heat-positivity qualifications. C032k
defines the individual entire lifts b_sigma=E_sigma+O_sigma. C032l,
including audit1340, excludes finite signed width combinations and
explicitly leaves infinite mixtures outside its conclusion. None of
these source qualifications is independently discharged here.

The new proposed class is a real finite signed Borel measure eta on
the fixed compact interval [1,2], with eta([1,2])=1, allowing infinite
support. It excludes distributional weights, width zero, unbounded
width and weights depending on the transform variable. Fixing this
interval avoids a singular zero-width limit or unbounded-width escape.

First determine whether the sources justify that sigma -> nu_sigma is
a measurable probability kernel. Only then may one use the proposed
mixture nu_eta(A)=integral_[1,2] nu_sigma(A) d eta(sigma).
Next check joint measurability and compact-width uniform bounds
sufficient for the proposed holomorphic integrals

    F_eta(w)=integral_[1,2] exp(-b_sigma(w)) d eta(sigma),
    J_eta(w)=integral_[1,2]
               exp(-E_sigma(w))*sinh(O_sigma(w)) d eta(sigma).

These formulas specify objects to assess, not proved existence,
holomorphy, identities or a continuum extension of C032k. Do not
interchange width integration with a series or divergent moment by
citing only an individual-width theorem.

## Bounded source test and downstream use

The discriminator is whether J_eta identically zero can hold with
eta([1,2])=1 in this compact class. Inspect primary integral-transform
uniqueness/completeness statements and essential proof cases. Reuse
the individual-width source reads; check only new uniformity or
uniqueness hypotheses. Narasimhan's finite independence theorem,
pairwise separation and finitely many cancelled odd coefficients
do not themselves settle this question. Import a matching theorem
with its applicability argument if one exists.

The main gap remains L030-L032/C032a actual-Xi all-degree positivity.
A probability representation with a positive exponential moment is a
possible input to that route. Individual smoothing and finite signed
compensation fail this necessary feature; the different operation
above tests the boundary of that failure. Even full odd cancellation
would leave mixed-measure nonnegativity, moment implications and
identification with the unsmoothed actual-Xi law unpaid. No such
representation, sign or RH consequence is asserted here.

Continue only with a matching theorem or a concrete integral-uniqueness
test whose essential estimates are covered. Exclusion stops this
compact class only; a candidate eta needs full-transform verification
and separate positivity/transfer work. If only finite independence,
coefficient truncations or unpaid source hypotheses are available,
park this implementation with the exact obstruction. Do not repeat
the stopped diagonal companion, degree-increment or finite-sum proof.

No new mathematical assertion is derived or approved here. The next
turn is literature-only. Essential inputs are C032j/C032k/C032l and
their qualified source interfaces; C028h and review1515 are contrasts,
not mathematical premises. No cross-notebook input is proposed. Full
Mathlib coverage is unchecked. No source-covered actual-theta sign or
continuum uniqueness mechanism yet justifies creative proof routing;
if review identifies one, nominate its bounded test on a later turn.


## Source comparison1528 — 18 November 2026

The initial nomination above is preserved as the proposed class and test,
not a proved construction. The completed source ledger is
[source-notes1528](2026-11-18-compact-width-source-notes-1528.md).
The original broad TARGET remains unchanged and REVIEW_REQUIRED.
The bounded search did not decide whether J_eta can vanish with mass one.
In particular an absence of a matching theorem is not an exclusion theorem,
a claim of novelty, or evidence that infinite mixtures exist.

The narrower analytic target has a plausible downstream role: it would
make the odd-transform integral a legitimate entire function before a
uniqueness/completeness test. It would not alone define a measurable
probability kernel, prove mixed nonnegativity, supply exponential moments,
or realize unsmoothed actual Xi. The original main gap is unchanged.
The new assessment awaits separate approval; this literature turn invokes
neither that mathematical attempt nor the full signed-cancellation test.
