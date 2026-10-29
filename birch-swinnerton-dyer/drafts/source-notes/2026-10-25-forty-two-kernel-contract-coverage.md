# Step 479 — reduced-output contract source coverage

2026-10-25. Literature only. No new inequality, enclosure formula, lemma,
mathematical script, numerical output or critical proof audit is supplied.

## Gap, target and downstream use

The main gap remains rational rank versus arbitrary complex analytic
order at least two for all E/Q. The exact target of this assessment is
the conditional 42-kernel derivative enclosure saved in the matching
literature assessment. Its plausible use is a later signed fixed-curve
assembly, retaining actual-parameter and all arithmetic errors. Such a
certificate would reproduce a known fixed-curve conclusion; it would
not close the universal BSD gap or prove refined BSD.

The supplied overview and DAG were used before detailed proofs. Read
the complete producing proof of L101, its separate audit's applicability,
tail, parameter and finite-error cases, and the whole L115 proof/audit.
The other inputs of L101 remain encapsulated in that audited result;
no upstream theorem is newly applied to a changed curve or normalization.
No computed kernel endpoint, L103 data or cross-notebook input was read.

## Primary sources and reused coverage

Reopened J. E. Cremona, *Algorithms for Modular Elliptic Curves*, corrected
second edition (1997), Section 2.13, printed pp.42–43 (PDF pages 36–37),
Proposition 2.13.1 and the preceding Mellin and integration-by-parts cases
([primary chapter](https://johncremona.github.io/book/fulltext/chapter2.pdf#page=36)).
The statement requires a weight-two newform, Fricke eigenvalue
epsilon=(-1)^(r-1), and analytic order at least r. Its derivative identity
uses the logarithm-weighted improper kernel. The preceding proof checks
the completed-to-uncompleted transition using lower vanishing. L101 has
already checked this at r=2 and N=389, obtaining the unnormalized L''
with factor four. Reuse that identity; a new derivation is unnecessary.
Changing the number of evaluated finite terms does not change these
source hypotheses. The source's numerical evaluation discussion supplies
neither outward endpoints nor this reduced-output error contract.

Reopened C. Wuthrich, *Numerical modular symbols for elliptic curves*,
arXiv:1608.06423v2, PDF dated 24 March 2017, Section 3.1, Lemma 4 and
its full proof, printed pp.6–7
([primary passage](https://arxiv.org/pdf/1608.06423v2#page=6)).
Its theorem concerns an upper-half-plane point, positive error tolerance
and sufficiently large truncation index. The proof uses |a_n|<=n for
the associated elliptic newform and a full geometric majorant. It does
not assert the weighted second-derivative or reduced-output contract.
That source input is already specialized and audited in L101/L115;
no new coefficient estimate or modular-symbol theorem is required.

Reopened F. Johansson, *Numerical integration in arbitrary-precision
ball arithmetic*, arXiv:1802.07942v1 (22 February 2018), Section 2,
printed p.2, including the callback cases and algorithm steps 1–4
([primary paper](https://arxiv.org/pdf/1802.07942v1#page=2)).
It distinguishes whole-set evaluation from analytic-domain certification,
rejects failed branch/analyticity tests with a nonfinite ball, and permits
a coarse enclosure when evaluation limits are exceeded. Thus tolerances
or successful return alone do not certify the widths sought here.
Only actual valid intervals are conditional inputs to the proposed
proof. No implementation, installed backend or mutable API is approved.

Reuse the inspected elementary logarithm comparison, exact interval
rules and the broader formula/integration comparison recorded in
`drafts/source-notes/2026-10-21-complex-derivative-sources.md`, together
with `drafts/literature/2026-10-25-unproduced-kernel-block-bound.md` and
its separate audit assessment. FLINT documentation is historical coverage
only; no present API behavior is newly asserted. A conditional composition
of supplied valid enclosures does not need a fresh backend investigation.

## Changed hypotheses and exact remaining specialization

The two original analytic omissions in L101 are n>128 with full kernels
and y>128 for n<=128. L115 instead covers n=43–128 only on [1,128],
uniformly for every real parameter in [3/10,1/2], including an admissible
midpoint. These scopes are compatible but must be composed explicitly in
research; no omission may be silently counted as already in another bound.

L101's parameter-transfer statement concerns the full 128-term sum.
Preserving that statement before discarding the midpoint block is within
the reviewed inputs. Reusing its signed derivative bound for a partial
sum without justification is outside them. A new smaller sensitivity
constant, alternative analytic partition or improved block threshold is
not part of the approved target.

Only the retained 42 coefficient values and kernel enclosures are to be
supplied as finite-output premises. Their identification with the same
newform, actual midpoint containment, nonnegative radii and certified
summation error remain mandatory. For omitted coefficients the all-n
majorant remains available without individual coefficient evaluation.
The later proof must retain signed weights in the center, absolute
weights for errors, L115's allowance and both original tails. L101's
old sufficient widths cannot be quoted as a total-radius guarantee under
the changed output assumptions. No combined radius is proved here.

## Duplicates, failures and search record

Searched 42-kernel, forty-two-kernel, partial-assembly, reduced-output,
S_42 and S42 in notebook literature/source notes, ATTEMPTS and histories
470–478. Matches propose this contract or distinguish it from L115;
no completed matching contract was located in that scope. Reuse the
broader exact-kernel and cutoff discovery recorded in the two source
assessments above; failure to locate a duplicate is not a novelty claim.

New web queries were: `"elliptic" "second derivative" "42" "enclosure"`;
`"Cremona" "2.13.1" derivatives truncation`;
`"Algorithms for Modular Elliptic Curves" "derivatives" "G"`;
and `"elliptic" "L-series" "rigorous" "derivative" truncation`.
The exact queries returned irrelevant material; broader results included
a secondary book mirror and general elliptic L-series documentation.
Neither was used as theorem evidence. The author's chapter and the two
primary papers above were opened directly. No inspected search result
supplied a stronger matching conditional 42-output theorem. Uninspected
software documentation remains a lead, not an imported result.

Read ATTEMPTS/052–054. The two stops concern source-statement selection
and AST context before production, not analytic impossibility. They remain
preserved, and no coordinator/standalone production is resumed. Historical
production and audit artifacts remain unchanged. This different target
is proof-only and conditional on future valid finite inputs.

## Decision and discriminating test

SPECIALIZE, for a later REPRODUCTION attempt at the exact saved target.
No essential unread theorem is required for this conditional composition;
the cited formulas and audited local estimates suffice as proposed inputs.
This is a scope assessment, not verification of the missing composition.

Continue only if the next proof supplies an explicit enclosure with every
region and error accounted for, preserving the source hypotheses and
leaving kernel evaluation out. If it needs an uncovered implication,
record it and stop rather than silently expanding this approval. The
future signed center and total verified radius must separately exclude
zero; source readiness proves no such fact. Full matching Mathlib
coverage is unchecked, with no claim of absence. No candidate solution
to the notebook's exact target exists.
