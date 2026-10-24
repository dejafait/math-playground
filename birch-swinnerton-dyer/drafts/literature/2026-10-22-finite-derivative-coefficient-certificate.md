# Exact finite derivative coefficients — source and duplicate review

TARGET: Certify all exact coefficients a_n for 1<=n<=128 on L030's conductor-389 curve by complete replay of L031's fixed prime-count evidence and exact Euler-factor recurrences, without evaluating another kernel.
CHECKED: 2026-10-23
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Targeted searches of L030/L031/L101, twist-five verify.py/audit.py/certify.py coefficient sections, history/076 and /078, the 2026-10-07 twist-five assessments and 2026-10-21 derivative assessments locate an already certified table through 256; primary-book searches for traces of Frobenius, multiplicativity and Euler products locate the exact recurrences.
SOURCE_EVIDENCE: Cremona, Algorithms for Modular Elliptic Curves, corrected second edition (1997), Chapter 2 Section 2.6 equations (2.6.1)--(2.6.2) printed p.25 and Section 2.8 equation (2.8.3) printed p.29; Chapter 3 Section 3.9 printed p.102, Traces of Frobenius, freshly inspected at https://johncremona.github.io/book/fulltext/chapter2.pdf and https://johncremona.github.io/book/fulltext/chapter3.pdf; reuse audited L031 and its saved primary-source assessments.
COMPARISON: Known normalized elliptic Euler coefficients and L031's existing exact 256-table cover all requested mathematical values; only a bounded derivative-facing replay and explicit provenance extraction remain, not a new coefficient-production theorem or BSD case.
GAP: No fresh complete coefficient replay was performed in this literature turn; the existing full certificate is sufficient upstream evidence, but its derivative-facing restriction and preservation report remain the approved implementation obligation.
REASON: Changed evidence scope requires checking normalization and duplication; reuse the certified table rather than rebuild it, keeping kernel and derivative obligations separate.
SCOPE: Only E=[0,1,1,-2,0], conductor 389, full unnormalized coefficients through 128; replay may check the existing 256-table and all its prime counts as stronger fixed evidence. No additional kernel or derivative evaluation is covered.

## Primary statements and applicability

[Cremona Chapter 2, printed p.25](https://johncremona.github.io/book/fulltext/chapter2.pdf#page=19)
normalizes a_1=1. Equation (2.6.2) gives
 a_(p^(r+1))=a_p*a_(p^r)-delta_N(p)*p*a_(p^(r-1)), r>=1,
with delta_N(p)=1 away from N and zero at its primes;
coprime multiplicativity follows in the same paragraph. Equation
(2.6.1) distinguishes single and repeated conductor factors.
[Equation (2.8.3), printed p.29](https://johncremona.github.io/book/fulltext/chapter2.pdf#page=23)
gives both Euler-product cases. These are imported identities, not a
proposed reproof. [Chapter 3, printed p.102](https://johncremona.github.io/book/fulltext/chapter3.pdf#page=41)
identifies a_p with p+1 minus the projective count on the minimal
equation, addresses bad reduction, and treats two separately from the
odd-prime quadratic counting algorithm.

L030's inspected arithmetic paragraph establishes Delta=N=389 and good
reduction elsewhere on the exact model. Thus only the good-prime
recurrence is needed for either table. The nodal count at 389 belongs
to the separate sign input, not to any coefficient at index <=256.
No bad-prime power or additive-reduction extension is needed.
L030's modularity identification and L031's coefficient paragraph
identify these integers with L101's normalized newform coefficients.
They are not twist coefficients chi_5(n)*a_n, a_n/n, or period-normalized
symbols; L101 retains the factor four separately.

## Duplicate and failure comparison

Canonical mathematics remains in L031's exact-coefficient, complete-replay
and separate-critical-audit paragraphs. History/076 and history/078 record
production and audit. Existing `scripts/twist-five/certificate.json` has
SHA256 `7547b371d675441190256195270c9282213e888cdb666451ae21a062896e4415`.
Selected attempt zero has T=256. The saved verification report has that
hash, seven passing grouped checks and no failures; these selected fields
were read in full. Inspector array previews locate 54 prime-count rows
and 255 factorization records; previews do not verify their entries.

The complete coefficient/count block of `scripts/twist-five/verify.py`
was read. It generates the full prime list independently, exhausts y for
every x, checks all odd-prime characters and pairs at two, includes
infinity, and compares every factorization, prime-power value and
coefficient through T. Its recurrence guard alone would not justify
general bad-prime powers; fixing T=256<389 excludes them entirely.
The inspected input/power section of `audit.py` explicitly does not
replace this count/recurrence replay. That complementary audit alone
would therefore be insufficient.

Reuse source scope in
`drafts/literature/2026-10-07-twist-five-certificate-critical-audit.md`
and L101's inspected finite-contract paragraph. ATTEMPTS/043's
complex-to-p-adic obstruction concerns a different coefficient.
History/397's backend stop and history/404's first-kernel limitation
concern integration, not this finite integer input. No stop is erased
or reopened. No novelty is inferred from local or primary-book searches.

## Approved bounded replay contract

One research invocation may add a separate exact replay/extraction
certificate under `scripts/finite-derivative-coefficients/` and document
applicability, preferably as a supplement to L031 rather than a duplicate
lemma. Preserve original certificate, programs and reports byte-for-byte;
bind fresh outputs to hashes and retain all unfinished first-kernel work.
Original producers and original report-writing entrypoints need not run.

1. Fix model, N=Delta=389, selected attempt zero and T=256 before arithmetic.
   Reconstruct the complete prime list through 256 and exhaust all pairs
   for every saved count, including two and the separate nodal row at
   389. Check every character, affine/projective total and trace. No
   selected-prime sampling substitutes for this full fixed evidence.
2. Replay a_1=1, all 255 factorizations and all associated prime-power
   recurrences through 256, requiring complete residual factorization
   and exact equality in every table slot including zeros. Export the
   restriction indexed 1 through 128 with full upstream binding. Retain
   powers of two and the p multiplier in every good-prime recurrence.
3. Save complete fixed records/checks on disk; print coverage, failures,
   actual/required bounds and paths. No period recovery, analytic series,
   published order/rank/Sha, kernel or derivative is needed. L031's
   optimality and period premises are not inputs to this subset.
4. Use one combined setup/replay/final-preservation execution of at most
   180 seconds and 134217728 new artifact bytes. Reserve finalization
   time and include final writes in measurement. Stop at the first
   mismatch or bound failure without retry or enlarged scope. This is
   an execution contract, not an established runtime theorem.

Continue on complete agreement and preservation under those bounds;
otherwise save the first missing/conflicting obligation and park dependent
coefficient work. No new arithmetic or mathematical script ran in this
review. Full matching Mathlib coverage is not checked; no absence claim
is made. Remaining 127 kernels, L101's complete signed assembly/error
radius and strict zero exclusion remain unresolved, as do arbitrary-curve
rank equality and the refined BSD formula.
