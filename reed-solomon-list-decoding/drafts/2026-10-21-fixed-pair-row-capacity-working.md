# Independent contraction-row capacity — work record

Approved target: Test all 64 nonzero-distance exact-cardinality contractions separately against the original-orbit scalar bounds at L098's fixed exact-N pairs.

Assessment: `literature/2026-10-21-fixed-pair-contraction-row-capacity.md`
(prior SPECIALIZE). This is a RESEARCH / REPRODUCTION calculation.
The main gap is arbitrary-center safety at 68/67 agreements. The target
can reject only L098's fixed pairs; a pass ends this diagnostic and does
not establish shared-triple, PSD, packing or RS feasibility.

Inputs read: canonical L098 (including its separate audit), L021's pair
definition, L022's normalization, L023's scalar specification,
foundations/04,12,13, ATTEMPTS/081,082 and history/362. No matching local
row-capacity verdict was found in the assessment or these records.
The prior literature assessment is reused without browsing.

Construction plan: recover the pairs from L021's complete rational
vector, then apply exactly L098's alpha mixture. With common denominator
q and numerators P_i, intersect every presentation's scalar rows to get
q*y in [max(0,P_a+P_b-q over all pairs), min(P_i,P_j,P_h)].
Repeated words fix y=p_b; forbidden distances fix y=0. Check these
additional equalities against the interval, rather than discarding them.
Every D is positive, so independent-coordinate row endpoints are sums
of D times the entry endpoints. Dropping source equalities and cross-row
coupling enlarges the original feasible set. Original t,s entries stay
distinct; factored endpoint evaluation does not equate their variables.

All six presentations will be checked at every actual orbit; a second
implementation will reconstruct the eight Boolean regions and D from
factorial multinomials. Bounds cover construction plus verification:
18,007,500 planned presentation/coefficient visits <20,000,000 (each
orbit's coefficient is computed during its first presentation visit),
1,500,625 entries <1,501,000, 69 rows, 1 GiB live memory, 256 MiB output,
262144-bit rational components and 900 seconds total. Check caps and
save an incomplete result if one is reached. No solve or retuning.

Completed in step 392: all 69 rows pass, strictly at i=5,...,68. The
canonical proof and complete evidence paths are in L105. Independent
eight-region reconstruction verifies every original entry, every
presentation and every endpoint sum; there are no verification failures.
The scalar row-capacity mechanism is stopped at these fixed pairs.
Shared-triple joint feasibility is unresolved and requires its separate
REVIEW_REQUIRED assessment; no further solve was attempted.

One initial JSON-inspector command used an unsupported `--max-items`
option and returned its usage without loading a selected value. The
command was corrected to the supported pointer interface. No mathematical
artifact or result was changed by that inspection error.
