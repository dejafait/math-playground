# Fixed nonunitary recovery — separate critical-audit coverage

TARGET: Critically audit L052's fixed nonunitary-cusp exact recovery, including degree-one differential normalization, split-prime counts, total-period orientation and complete rational isolation.
CHECKED: 2026-10-12
DECISION: SPECIALIZE
SEARCH_EVIDENCE: BSD-173 searched the exact L052 proof, production assessment, L048 torsion/period passages, L051 audit entry, histories 171/172 and ATTEMPTS/025; reopened the three primary sources at their load-bearing statements/proof cases. Reused BSD-171's recorded discovery queries; no novelty inference or broad repeated search.
SOURCE_EVIDENCE: Cai--Chen--Liu, Trans. AMS 370 (2018), Section 3 p.3732; Cesnavicius--Neururer--Saha author version 2022-01-28, Theorems 1.2/7.2 pp.3,45--46 and complete final proof; Wuthrich arXiv:1608.06423v2, Proposition 1 and full proof pp.3--4. Direct links and inspected passages below; L048's audited Cremona/Silverman coverage is reused.
COMPARISON: The known statements cover the proposed audit's exact CM/additive, degree-one and arbitrary-cusp hypotheses. The audit may check their applicability and the finite specialization; no new normalization or torsion theorem is needed. Production replay remains distinct from separate critical validation.
GAP: Mathematical audit remains undone: verify L052's assembly, both complete counts, connected total-period factor, reversed path, rational existence and all isolation evidence; inspect complete certificates rather than report previews. Source coverage is adequate, but it does not certify the claimed value or software.
REASON: Separate literature-only approval of BSD-172's saved audit target; the first comparison of this audit scope with L052 and primary hypotheses changes REVIEW_REQUIRED to SPECIALIZE without conducting the mathematical audit.
LITERATURE_REASON: The newly saved audit scope was REVIEW_REQUIRED; review the new L052 applicability and evidence obligations using ready production coverage before invoking a separate research audit.
SCOPE: Exact minimal CM E=[0,0,0,0,1], N=36, Delta=-432, oriented {1/6,infinity}, audited L051 interval, claimed clearing integer 24 and value -1/12; source applicability and complete finite audit only, no new analytic production or non-CM application.

## Source comparison

Read L052 in full before comparing sources. The unchanged production
assessment `drafts/literature/2026-10-12-nonunitary-exact-value-recovery.md`
is ready for its original target; this approval covers the distinct
critical-audit target above, with future classification REPRODUCTION.

Cai, Chen and Liu, *Heegner points on modular curves*, DOI
10.1090/tran/7053, [Section 3, p.3732](https://archive.ymsc.tsinghua.edu.cn/pacm_download/632/12220-Heegner_points_on_modular_curves.pdf#page=12),
explicitly present the genus-one modular curve with rational infinity
origin and minimal equation y^2=x^3+1. Reopened the Section 3 opening
paragraph. This covers the model/origin input. Its rank, Tamagawa and
L-value assertions are outside the audit inputs. The audit must check
L052's passage from this identification to its optimal-quotient and
associated-differential usage; no database label substitutes for that check.

Cesnavicius, Neururer and Saha, *The Manin constant and the modular degree*,
[28 January 2022 version, Theorems 1.2/7.2](https://maths.qmul.ac.uk/~asaha/research/manin-paper.pdf#page=3),
cover an elliptic curve at its exact conductor and every surjection from
the specified intermediate modular level. The differential multiplier is
a nonzero integer; its divisibility by the degree holds when 8 and 27 do
not divide the conductor. Read Theorem 1.2's hypotheses, Theorem 7.2's
complete statement and final proof pp.45--46, including both its
rational-singularity branch and unrestricted exceptional-prime bound.
There is no CM or semistability exclusion in these statements. This is
sufficient coverage for testing L052's proposed degree-one normalization;
the audit must retain exact conductor, minimal differential and sign choice.
Import the theorem rather than reprove its geometric inputs.

Wuthrich, *Numerical modular symbols for elliptic curves*,
[arXiv:1608.06423v2, Proposition 1 and proof pp.3--4](https://arxiv.org/pdf/1608.06423v2#page=3),
assumes optimal Manin constant one and uses selected good primes greater
than two congruent to one modulo the square-part parameter. Its first
conclusion covers arbitrary rational cusps; only its stronger second
conclusion requires unitary cusps. Read the period-ratio definitions,
statement and entire proof through the unitary case and final remark.
The proof puts cusp images over the cyclotomic field, invokes
Manin--Drinfeld, and cites Silverman VII.3.4 for torsion injection at
unramified places. It explicitly retains the half-lattice factor for a
nonrectangular real lattice. These are the needed proof cases, not an
assumption that a prime-to-residue-characteristic injection suffices.
The audit must check how L052 discharges the Manin premise and converts
this convention to the total minimal real period and reversed path.

L048's already audited passages supply the full torsion-injection
qualification e < ell-1 and Cremona's total-period convention, corrected
second edition, Section 2.8 following (2.8.9), p.30. Their coverage is
reused without broad source re-extraction. No new theorem or reproof is
needed for exact rational enumeration: this is finite evidence to audit.
Full matching Mathlib coverage remains not checked; no absence claim.

## Overlap, failures and bounded audit plan

Histories 171/172 establish source approval then production recovery,
not a completed independent audit. L048/L049 already supply the general
mechanism; L051's separately audited interval is the analytic input.
ATTEMPTS/025 stops the complex-rectangle representation and does not
bar this distinct finite recovery audit. Preserve all prior evidence.
No sibling notebook or cross-notebook input was read.

Essential inputs: L052 in full; audited L048 torsion/period conventions;
L050 exact minimal model/conductor and real-component input; audited
L051 analytic interval. Inspect the complete new certificate and report
`scripts/nonunitary-cusp/exact_value_certificate.json` and
`scripts/nonunitary-cusp/exact_value_verification.json`, plus the full
producer/verifier code needed for their claimed coverage. This source
review inspected only the verifier's invocation/output interface, not
its complete implementation or evidence, and performed no replay.
The verifier currently writes its production report; a fresh audit must
preserve original bytes and write distinct evidence. An independent
containing interval can supplement isolation but cannot replace L051.

The main gap remains arbitrary analytic-order-at-least-two rank equality.
The intermediate target is validation of one exact nonunitary symbol,
plausibly useful as a normalization test. Continue only after every source
hypothesis and the complete finite evidence pass independently. A
load-bearing mismatch, incomplete enumeration or replay failure requires
repair or qualification before dependent use. Independent rational
directions, Sha, uniform coefficients, complex-order comparison and a
full generator table remain missing. This approval is not audit success,
a new mathematical input beyond L052, or a BSD candidate.

The REVIEW_REQUIRED proposal from BSD-172 is superseded here only as a
coverage decision. Its completed recovery is preserved and the separate
mathematical critical audit is deferred to the next invocation.
