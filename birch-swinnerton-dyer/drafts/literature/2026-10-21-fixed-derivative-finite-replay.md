# Fixed derivative finite replay — concrete backend blocked

TARGET: Construct and independently replay L101's finite second-derivative enclosure at M=Y=128, with certified parameter and kernel radii at most 2^-50 and exact signed summation, and test the final interval for zero exclusion.
CHECKED: 2026-10-21
DECISION: SOURCE_BLOCKED
SEARCH_EVIDENCE: Reused analytic discovery/overlap coverage; searched the python-flint integral/endpoint and FLINT order-one interfaces, inspected release-specific sources, and checked functioning PATH interpreters and usual C installation paths; full evidence and retrieval failures are in drafts/source-notes/2026-10-21-fixed-derivative-backend-review.md.
SOURCE_EVIDENCE: Reuse Cremona (1997) Proposition 2.13.1 https://johncremona.github.io/book/fulltext/chapter2.pdf#page=37 and Johansson arXiv:1802.07942v1 Section 2 https://arxiv.org/pdf/1802.07942v1#page=2; newly inspected python-flint 0.8.0 callback/integral/log https://raw.githubusercontent.com/flintlib/python-flint/0.8.0/src/flint/types/acb.pyx and outward exact export https://raw.githubusercontent.com/flintlib/python-flint/0.8.0/src/flint/types/arb.pyx; matching FLINT v3.3.1 contract https://raw.githubusercontent.com/flintlib/flint/v3.3.1/doc/source/acb_calc.rst and directed bounds https://raw.githubusercontent.com/flintlib/flint/v3.3.1/doc/source/arb.rst; official release metadata https://pypi.org/pypi/python-flint/json reports bundled FLINT 3.3.1 but no local binary is identified.
COMPARISON: Known release-specific machinery covers branch checking, rigorous finite integration and rational outward export; the Python wrapper discards the C status, making actual returned containment and width checks essential. These contracts supply neither an available local backend nor the fixed certificate.
GAP: Every functioning checked PATH Python lacks flint, usual FLINT/Arb installations are absent, and local PyPI metadata retrieval fails at DNS resolution; actual backend/linkage, callback, narrow c endpoints, 128 kernel intervals, replay and zero exclusion remain absent. This is an essential concrete-executable input blocker, not an inaccessible primary theorem.
REASON: New interface and environment evidence prevents approval of this exact finite replay; park the library implementation instead of assuming installation or repeating availability checks without changed evidence. A proposed backend-free mechanism needs its own separate source review.
LITERATURE_REASON: The new implementation target requires essential version-matched callback, outward-export and concrete-backend coverage outside the ready proof-only audit; this is its separately required review, not repeated analytic-formula browsing.
SCOPE: Preserve the original TARGET and M=Y=128, without execution approval. No installation, fallback, cutoff change or replacement integration construction is approved by this record.

The main gap remains the arbitrary-curve rank/order comparison. This
fixed replay could supply independent complex upper-bound evidence
alongside L099's finite-witness lower bound. L035 already supplies this
known fixed order by citation; success changes evidence provenance,
not the list of known BSD cases. Preserve ATTEMPTS/043 and /045.

Essential inputs are audited L101, L030's actual model and conductor,
L031's independent coefficient/sign and parameter rules only, audited
L099 and foundations/02. No L035 published complex order, L100 p-adic
squeeze, published basis or Sha premise may replace these inputs.
Reuse the existing primary formula, tail and logarithm coverage. The
new essential review concerns an actually available, identified finite
integrator interface and its rigorous coefficient/callback, branch,
endpoint-export and replay obligations. The earlier absence of the
Python flint module does not certify another executable or library.

The proposed certificate must identify every a_n through 128, give
a rational c enclosure inside [3/10,1/2] with half-width <=2^-50,
and give all 128 finite-kernel enclosures at its exact midpoint,
each with half-width <=2^-50. Retain signed weights and exact rational
summation (eta=0), then use L101's complete error radius. Independent
replay must check complete evidence, not a preview or a tolerance flag.
Backend version, finite callback behavior and actual intervals must
be explicit; the mutable documentation is insufficient provenance
for an unspecified installed binary. No additional mathematical
integration construction is derived or approved here.

Continue only with a source-covered available method and a bounded
execution/replay plan fixed before invocation. A nonfinite result,
an unmet width, or missing evidence fails that certificate; a final
interval containing zero is inconclusive about L''. Preserve the
failure without silently increasing cutoffs or changing the method.
A successful zero-excluding interval would still require separate
critical review before its complex-order conclusion is accepted.
Persistent backend blockage requires parking dependent work for an
independently testable target. Mathlib coverage remains not checked.

## Step 397 decision

The [completed review](../source-notes/2026-10-21-fixed-derivative-backend-review.md)
pins the candidate API and records new availability and retrieval
evidence. Source comparison is complete for that candidate; no matching
available executable is established. SOURCE_BLOCKED concerns the
essential concrete implementation input, not access to the primary
mathematical sources. Preserve the original target for a changed
environment. Park this library implementation; the proposed rational
integration source comparison is uncovered and receives no mathematical
approval in this turn.
