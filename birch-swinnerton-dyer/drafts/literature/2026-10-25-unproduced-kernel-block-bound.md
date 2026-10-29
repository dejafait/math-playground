# Unproduced kernel block — proof-only source comparison

TARGET: Prove or refute the uniform bound 4*sum_(n=43)^128 (|a_n|/n)*J_n(t)<2^-14 for every t in [3/10,1/2], using L101's kernel and coefficient majorant, without evaluating kernels or assembling the derivative.
CHECKED: 2026-10-25
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Queried Cremona Algorithms Modular Elliptic Curves Proposition 2.13.1 derivatives G r truncation exponential error and elliptic curve 389 second derivative L series rigorous truncation 42; searched partial assembly, n=42/43 and tail terminology in notebook literature/source notes, ATTEMPTS and histories 390–474; no matching completed block-bound certificate located in that scope. Reused the broader comparison in drafts/source-notes/2026-10-21-complex-derivative-sources.md via its inspected audit-coverage record.
SOURCE_EVIDENCE: Reopened Cremona corrected second edition (1997), Section 2.13 printed pp.42–43, Proposition 2.13.1 and preceding Mellin/integration-by-parts passage, https://johncremona.github.io/book/fulltext/chapter2.pdf#page=37; reopened NIST DLMF 4.5.4 with x>0, https://dlmf.nist.gov/4.5.E4; reused Wuthrich arXiv:1608.06423v2 Lemma 4 and full geometric-remainder proof printed pp.6–7 as recorded in drafts/source-notes/2026-10-21-fixed-derivative-audit-coverage.md; read L101's hypotheses, identity, full remainders, parameter propagation and corresponding audit cases, and L103's complete parameter statement/containment proof.
COMPARISON: Known exponential/geometric-tail methods and audited L101 supply the majorant mechanism, positivity domain and coefficient input; L101 bounds a different omitted range, n>128, and does not assert this n=43–128 threshold. Only the explicit finite-block specialization remains to be proved. No new integration theorem or claim of novelty is needed.
GAP: The displayed 2^-14 threshold has not been derived, computed or verified. Its utility requires later signed assembly of the first 42 kernels with all coefficient, parameter and analytic errors; no final interval or zero exclusion follows from source readiness.
REASON: Replace repeatedly stalled source adaptation by an independently testable analytic bound that needs neither an executable backend nor a new runner. A source citation supplies the method but not the requested cutoff-specific inequality.
LITERATURE_REASON: The changed target omits an unevaluated finite block rather than producing each kernel; this error-budget change is outside the original fixed 128-kernel output contract and requires its own comparison.
SCOPE: One proof-only attempt at exactly the stated threshold, uniform on the closed positive parameter interval; no mathematical script, kernel production, modified historical contract, derivative evaluation or BSD conclusion.

## Gap, competing mechanisms and choice

The main gap remains rational-rank equality for arbitrary E/Q of analytic
order at least two. This fixed-curve target addresses only the cost of
constructing independent complex evidence. L035 already imports the
known fixed analytic order; this route would change provenance, not
establish a new BSD case.

Three mechanisms were compared. Coordinator adaptation has two stopped
constructions, with exact failures preserved in ATTEMPTS/052–053.
Standalone n=43 production avoids that coordinator but its runner/edit/
inventory coverage remains REVIEW_REQUIRED; the n=1 assessment cannot
be inherited wholesale. A positive analytic majorant for the unproduced
block requires neither source adaptation nor kernel evaluation. Select
this third mechanism. The library route's separate availability failure
in the finite-replay assessment is also retained, not retried.

## Sources, applicability and precise remaining difference

Cremona's proposition concerns a normalized weight-two newform with
Fricke sign (-1)^(r-1) and vanishing of order at least r. Its preceding
proof explains the lower-vanishing and integration-by-parts steps.
L101 already checks these hypotheses at r=2 for the conductor-389 model;
import that local result rather than repeating the Mellin proof. This
turn does not verify any new cutoff inequality.

Reuse the coefficient majorant |a_n|<=n from Wuthrich's cited proof,
already specialized and audited in L101. It applies to this elliptic
newform, not to arbitrary unnormalized cusp forms. DLMF 4.5.4 applies
on y in [1,128]; the integrand's logarithm and all exponential arguments
are real with positive t. The existing L101 proof provides a full-kernel
positive majorant and geometric-tail method, including rational bounds
for its geometric factor and exponential decay. Those are supporting
inputs, not a certificate of the new threshold. L103 places both the
actual c and its certified midpoint in the required closed interval;
no midpoint endpoint need be read from a computed kernel report.

The research task is to give the complete rational comparison for this
finite block, retaining the factor four and absolute coefficient weights.
An infinite positive majorant may enlarge it if justified; positivity of
the majorant must never change signs in a later retained sum. No claim
of a sharp bound is required. The stronger numerical-evaluation leads
returned by search (PARI ellL1 and Sage L-series documentation) do not
provide this rational block certificate and are not imported. An exact
local duplicate was not located; that is not evidence of originality.

## Continuation and abandonment test

Essential mathematical inputs are L101's kernel definition, coefficient
majorant and audited elementary tail estimates. L030/L031/L099 and
foundations/02 remain encapsulated in L101's already checked derivative
interpretation; no new rational-rank or published-order premise enters
the bound. L103 supplies only parameter-domain context. L102 and the
produced kernel endpoints are not arithmetic inputs to this proof task.

Continue this mechanism only if one complete proof establishes the
stated strict bound uniformly, with every exponential and geometric
comparison justified. If it fails, record the actual unmet inequality
or missing hypothesis and abandon this fixed threshold in this attempt;
do not silently weaken it or produce another kernel. A success would
permit proposing a separate partial-assembly contract, adding the block
error to L101's original tails and actual parameter/retained-kernel errors.
It does not alter L101's existing 128-output contract or assert that
zero can be excluded. Signed finite assembly, coefficient/source replay,
exact-parameter transfer, nonvanishing, general rank comparison, full Sha
and refined BSD remain unresolved. Matching Mathlib coverage is not
checked; no absence claim is made.

This is source readiness for REPRODUCTION, not a new estimate or an
independent approval of a derived result. The newly written continuation
is subject to the supervisor's separate next-turn approval.
