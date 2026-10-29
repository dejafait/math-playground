# Step 481 — L116 audit source-scope comparison

2026-10-25. Literature only; no new estimate, proof audit or certificate.

The main gap is rank versus arbitrary analytic order at least two for
all E/Q. The intermediate target is the exact L116 critical audit in the
matching assessment. Its plausible use is validation of a conditional
fixed-curve assembly contract; it cannot resolve the universal gap.

## Reused primary coverage and applicability

The complete step-479 coverage note was read, together with its ready
producing assessment. It records inspected primary theorem statements
and essential proof cases, not search snippets. No source change or new
curve, domain, normalization or integration method is proposed here.

Cremona, *Algorithms for Modular Elliptic Curves*, corrected second
edition (1997), Section 2.13, Proposition 2.13.1 and preceding proof,
printed pp.42–43 ([author chapter](https://johncremona.github.io/book/fulltext/chapter2.pdf#page=36)),
requires a normalized weight-two newform, Fricke eigenvalue
(-1)^(r-1), and analytic order at least r. The recorded proof cases
include the lower-vanishing transition from completed to uncompleted
L. L101's assessed r=2 application supplies the unnormalized derivative;
L116 explicitly retains that normalization and lower vanishing.
The later audit must check faithful use, rather than reprove the Mellin
identity or infer nonzero second derivative from lower vanishing.

Wuthrich, *Numerical modular symbols for elliptic curves*,
arXiv:1608.06423v2 (24 March 2017), Section 3.1, Lemma 4 and proof,
printed pp.6–7 ([primary version](https://arxiv.org/pdf/1608.06423v2#page=6)),
concerns the elliptic newform and modular-symbol truncation, with
Im(tau)>0, positive tolerance and sufficiently large truncation index.
Its proof supplies the assessed coefficient majorant and geometric-tail
method. Its modular-symbol theorem is not a second-derivative contract.
L116 uses the same majorant through L101/L115; no stronger coefficient
bound or changed normalization needs new source coverage.

Johansson, *Numerical integration in arbitrary-precision ball
arithmetic*, arXiv:1802.07942v1 (22 February 2018), Section 2, p.2
([primary paper](https://arxiv.org/pdf/1802.07942v1#page=2)),
provides the previously inspected whole-set/analyticity distinction and
failure/coarse-output cases. L116 assumes actual valid intervals rather
than tolerances or successful returns. No backend implementation is an
input to this proof-only audit; the mutable FLINT contract is not newly
certified. Existing integration coverage suffices for these conditional
premises. Full matching Mathlib coverage remains unchecked.

## Scope boundary, duplicates and failures

Read L116's complete producing proof to identify obligations, not to
certify their truth. Read L101's statement, imported theorem conditions,
both remainder proofs, parameter estimate and separate audit cases;
read L115's full proof and separate audit. Also read the two upstream
audit assessments. These local results encapsulate their upstream
arithmetic; no cross-notebook input or new upstream theorem is used.

The changed finite-output assumption is already assessed in step 479.
The audit must distinguish all n>128 full kernels, y>128 for n<=128,
and the n=43–128 block on [1,128]. The same full-sum parameter estimate
is to be used before discarding the midpoint block. A partial-sum
sensitivity estimate would be outside this coverage. Check signed
remainder notation against L101's nonnegative majorants, as well as
signed centers versus absolute error weights. This identifies an audit
question, not a finding of error or a mathematical repair.

The optional 624*2^-50 allowance and strict total radius are audit
obligations, not newly verified arithmetic in this review. A source
citation alone cannot certify this particular local composition. That
is why a REPRODUCTION audit is justified despite ready source coverage;
no reproof of any named imported theorem is needed.

Specific local searches for L116, conditional 42-kernel and 624 found the
producing assessment, pending assessment and producing history, without
an already completed L116 audit in the searched scope. Reuse the exact
and broader source searches and duplicate comparison in step 479's
coverage note. No claim of novelty follows. ATTEMPTS/054 preserves the
coordinator failures and unattempted standalone proposal; they concern
production/provenance, not this conditional analytic composition. They
do not justify resuming production, nor globally forbid it.

## Decision and continuation test

SPECIALIZE: no essential unread source was identified for the exact
saved audit. This step resolves source scope only; it makes no critical
correctness judgment and proves no new mathematical result. No new
external passage was retrieved because the recorded inspected coverage
is adequate and unchanged. Uninspected software leads are not inputs.

Continue with the separate critical audit only if L101 and L115 imply
the advertised enclosure without a missing region or uncovered estimate.
Check hypotheses, full-sum transfer, signed weights, strictness and all
optional width comparisons. If a necessary implication fails, preserve
it and record the precise correction or obstruction; do not silently
expand scope. Actual coefficients/kernel certificates, narrow c data,
assembly and zero exclusion remain unresolved application premises.
The stated allowance supplies no inherited 2^-40 guarantee. No complete
candidate, general rank comparison, full Sha or refined BSD follows.
