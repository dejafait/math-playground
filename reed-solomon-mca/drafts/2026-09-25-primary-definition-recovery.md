# Primary-definition recovery — 2026-09-25

Working notes saved before further retrieval. The existing September 24 files
and all other notebooks' work are preserved. The local DAG is empty; there is
no mathematical result or failed technical mechanism to duplicate.

Gap: the current primary MCA definition, smooth-domain scope, and radius
endpoints remain unread. Intermediate target: a version-specific primary
statement, with one discriminating check of the codeword/support quantifiers.
Downstream use: decide whether a support-counting or affine-line argument
actually controls the required MCA error. A full upper/lower threshold theorem
would remain a separate unresolved task. Continue into mathematics only if the
definitions can be certified; otherwise record the retrieval limits honestly.

Retrieval approaches compared: the ePrint PDF and version archive (previously
unsuccessful), an author-hosted copy, and a primary project mirror linked by the
official companion challenge. The first retry still failed; the current
ePrint metadata continues to report the July 6 revision and its MCA lower-bound
addition. Fenzi's publications page still points to ePrint. A newer third-party
formalization surfaced in search but is not a replacement for ABF26's text.

The exact target remains the largest radius with MCA error at most the given
epsilon, illustratively 2^-128. No achieved bound is claimed in these working
notes. The previous exploration count is one; this step has not been assessed.

## Discriminating endpoint check

A successful new lead is the upstream ArkLib revision pinned in the official
companion project's lake manifest:
`e65197892890b8fd9b0dc05b8980273cf1d595cc`. Its `GrandChallenges.lean`
explicitly formulates an adjacent-grid boundary, not a largest safe real radius.
`GrandMcaResolution.sublevel_iff` states that the safe real radii below such a
boundary form a right-open interval.

The source-audit target is now concrete: unpack the pinned support event and
check this endpoint statement independently. Continue using the grid source as
a definition-audit aid only if its support condition matches the primary WHIR
quantifiers. If the safe set is right-open, reject an automatic identification
with the prize page's real maximum. This is a review of the source bridge,
not a proposed resolution or a change to the local target. The July paper's
actual text still has not been recovered.

The pinned `CoreDefinitions.IsMCA` uses a support of size at least
`n * (1 - delta)`, code agreement of the combination on that support, and
failure of one input to agree with the code on the same support. The generator
is `(1, gamma)`. These are the WHIR support quantifiers. Smoothness in the
pinned code is a nonzero multiplicative coset of power-of-two size.

An informative endpoint test is possible without identifying this frozen model
with the unread July paper: exhibit a smooth RS code at an official rate and
the actual error target 2^-128 whose model error is safe at radius zero and
unsafe at another radius. Integer support sizes then make the safe set
right-open, so the pinned grid answer is not a real maximum.

Candidate arithmetic: F = F_(5^56), n = 16, k = 1. The inequalities
2^128 < 5^56 < 6 * 2^128 would place six distinct bad challenges above the
budget while a single bad challenge remains below it. The length-16 constant
code has rate 1/16; a subgroup of order 16 exists since 16 divides 5^56 - 1.
For four coordinates set b_i = x_i and a_i = x_i^2 with
x_i = 0, 1, theta, theta^2. The six pair sums are distinct if theta has no
nonzero degree-at-most-two relation over F_5. At gamma = -(x_i + x_j), the
combination is constant on that pair and b is not. Such a pair is an allowed
support at radius 7/8. Remaining coordinates can be zero.

This is saved unfinished reasoning. The source bridge, exact inequalities,
and complete endpoint proof require checking before this can be assessed.

## Completed assessment

The event, sampler, smooth-domain declaration, and grid convention were read
at the immutable upstream revision. The primary WHIR excerpt independently
supports the event's quantifier order. The July ABF26 paper remains unread.
The canonical definition and provenance are now in
[the frozen-model foundation](../foundations/02-pinned-affine-line-model.md).

The mathematical endpoint check succeeded: the full arguments are stored in
[L001](../lemmas/L001-affine-support-radius-cells.md) and
[C001a](../lemmas/C001a-smooth-endpoint-witness.md), superseding the unfinished
derivation above. Exact integer and polynomial-coefficient checks passed.
There is a positive safe interval and an unsafe radius at the prescribed
2^-128 budget, so the maximum/supremum/grid distinction is substantive for
this model. The safe boundary index itself is not determined.

Outcome: NEGATIVE for the proposed unqualified source bridge. The conditional
application to the grand challenge is recorded as an UNVERIFIED CANDIDATE,
with the paper correspondence and possible parameter restrictions left for
critical review. This does not claim that an endpoint issue settles the
intended sharp-threshold research problem. Current status and the single
continuation action are recorded only in PROGRESS.md.
