# Common-height assembly — completed source-scope review

TARGET: Audit the common-height overlap of L465 and L464 for the unconditional Xi tail 2p>=c_0 log(t/(2pi)), for each fixed c_0>1/2, including integer endpoints.
CHECKED: 2026-10-25
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the completed growing-radius and finite-local-factor assessments; searched those files, canonical L464/L465 statements and the October 25 audit histories for overlap, Theorem 1a and recorded failures. No earlier completed local assembly audit was found in this bounded search; the exact conclusion is already stated in the inspected primary source.
SOURCE_EVIDENCE: bramble_trace, Generalized Laguerre positivity at growing orders, paper 41, displayed v4, 24 October 2026 07:18 UTC, definitions (1)-(2), Theorem 1a (4a), Section 4.2 opening hypotheses, Section 4.3 (18h) and the full first paragraph of Section 4.4, accessed 25 October 2026; existing component assessments reused for their underlying classical source coverage.
COMPARISON: Theorem 1a states the exact unconditional all-large-order Xi conclusion, and Section 4.4 expressly assembles its analytic window and product tail. L465 and L464 separately reproduce those components with the same actual-Xi coefficient convention; neither canonical statement claims the common-height assembly. L463's stronger conditional tail has a separate external premise and is not an input here.
GAP: No essential source coverage is missing for the saved audit. The common existential onset, p versus 2p conversion and integer endpoints still require a separate mathematical check; this review neither performs that check nor establishes the assembled theorem.
REASON: Approve one bounded REPRODUCTION audit of the exact saved target. Reproof is justified to make the source's short overlap assertion checkable from locally audited components, not to claim new mathematics or redo the analytic and product estimates.
SCOPE: Fixed c_0>1/2, positive real heights tending to infinity, integer p with 2p>=c_0 log(t/(2pi)), actual entire Xi; central zeros and multiplicities allowed. No numerical onset, endpoint c_0=1/2, arbitrary-order Hardy conclusion or external fixed-half-plane premise is covered.
LITERATURE_REASON: The invocation-start REVIEW_REQUIRED assessment nominated a distinct assembly that the two ready component assessments expressly excluded. This separate source-scope review resolves that changed-target gate without repeating broad discovery or deriving the assembly.

## Gap, use and discriminating test

The main gap remains initial actual-Xi signs at unbounded heights,
effective bounded-height coverage and global mixed positivity. The
intermediate target is exactly TARGET above. Its plausible downstream
use is a separately checked unconditional tail component of the sign
picture; it cannot supply the surviving initial signs.

Continue with the saved audit if the same coefficient and height
variables, uniform constants and quantifiers are available in both
components. That source-access and scope test passes. The later
mathematical test is whether a single height onset covers every allowed
integer order after combining the two domains. Record a failed domain,
normalization or endpoint check if one occurs, and do not assert an
all-order conclusion from two disjoint ranges. No such assembly proof
or endpoint calculation is performed in this literature-only turn.

## Inspected source and reused coverage

The [primary manuscript](https://rstation.ai/problems/riemann_hypothesis/papers/41)
still displays the v4 author, date and version above. Definition (1)
uses the coefficient of y^(2p) in f(t+iy)f(t-iy), matching D_p in both
local statements; definition (2) identifies the same completion.
Theorem 1a is the exact claimed tail theorem. Section 4.4's first
paragraph invokes A=2, the analytic window ending at ell cubed and
(18h), and explicitly restricts arbitrary orders to Xi. Its next
paragraph concerns Corollary 4a and Theorem 4 and is outside this audit.
The source is an online manuscript; publication or full-manuscript
correctness is not inferred from its platform or its participant notes.

Reused [growing-radius coverage](2026-10-25-growing-radius-audit-coverage.md)
and [product coverage](2026-10-25-local-factor-coefficient-audit-coverage.md),
including their primary classical theorem statements and proof cases.
Read the canonical hypotheses and conclusions of L464 and L465, not
all their detailed proofs: the assembly audit may take the separately
audited component results as inputs. L465 has constants and onset
uniform in its allowed order range for each fixed c_0; L464 has one
absolute existential constant and applies at every t>=2. The audit
must retain these qualifications rather than turn them into numerical
certificates. L018 identifies actual Xi in both; no cross-notebook
input or new analytic estimate is proposed.

## Duplicates, failures and bounded continuation

Targeted October 25 histories show the product and analytic audits
completed separately, with assembly expressly deferred. The two reused
assessments already checked the finite-level masking/count failures;
those countermodels and L462's fixed-anchor small-tail stop remain
unchanged. They concern sufficiency for missing signs, not this
source-stated tail assembly. No historical stop is reopened and no
novelty is inferred from the bounded local search. No new broad query
was needed: the exact stronger source statement and its essential
assembly paragraph were accessible directly.

The next invocation should use L464 and L465 with L018's shared
completion, retain their positive coefficient normalization at central
zeros, choose a common existential onset with fixed c_0, and check
integer endpoints explicitly. It should not re-audit either whole
component, import L463, or extend the Hardy conclusion. A successful
assembly belongs in a canonical result with full hypotheses and proof
in that later research turn. Full matching Mathlib coverage remains
unchecked; this is not an absence claim.

Outcome: EXPLORATION, LITERATURE, REPRODUCTION. The separate review
changes the nomination from REVIEW_REQUIRED to SPECIALIZE and leaves
the exact Next action unchanged. No new lemma, mathematical script,
assembly derivation or proof verdict is produced.
