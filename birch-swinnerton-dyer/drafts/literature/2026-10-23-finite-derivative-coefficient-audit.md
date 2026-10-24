# Finite coefficient extraction — proposed critical review

TARGET: Critically audit L031's derivative-facing coefficient extraction by complete fresh replay, independent exact recurrence comparison and full input-preservation checks under one 180-second/134217728-new-byte cap, without evaluating a kernel.
CHECKED: 2026-10-23
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused ready coefficient assessment; inspected L030 arithmetic, L031 coefficient proof and fresh supplement, L101 coefficient contract, full fresh replay.py, report and inventory interface, histories 407/408 and earlier twist-five audit scope; exact extraction is duplicate mathematics with a new persisted-evidence interface.
SOURCE_EVIDENCE: Cremona, Algorithms for Modular Elliptic Curves, corrected second edition (1997), Chapter 2 Section 2.6 equations (2.6.1)--(2.6.2), p.25, Section 2.8 equation (2.8.3), p.29, and Chapter 3 Section 3.9, p.102; primary statements already inspected in drafts/literature/2026-10-22-finite-derivative-coefficient-certificate.md, reused unchanged without additional browsing.
COMPARISON: Sources identify the normalized untwisted integers, not correctness of the fresh files; approve one full independent audit of that finite specialization, with no reproof of Euler rules or new coefficient theorem.
GAP: Complete fresh replay, independent exact recurrence comparison, export equality and preservation remain unexecuted; historical post-write timing cannot be recovered merely from the saved pre-final-write timer.
REASON: Separate review now matches the newly persisted extraction interface to ready source coverage and specifies its historical-document transition; this approves audit execution, not its mathematical verdict.
SCOPE: Only L031 extraction for E=[0,1,1,-2,0], N=389, full table through 256 and indexed restriction 1..128, including the separate nodal evidence; no period, kernel or derivative calculation.

Essential inputs are L030's model/conductor/modularity, L031's original
fixed coefficient certificate and fresh supplement, and L101's full
untwisted convention. The new certificate binds the original SHA256 and
all 128 exported index/value rows. An audit must inspect complete
relevant records rather than inspector previews, retain all prime counts
including two and the separate nodal row, and compare all recurrences
including zeros and powers of two. Original twist-five and unfinished
first-kernel evidence must remain intact. This target supplies no kernel,
derivative nonvanishing, uniform BSD input or period premise.

## Separate source/interface review, step 409

The ready assessment imports the normalized Euler identities from
[Cremona Chapter 2](https://johncremona.github.io/book/fulltext/chapter2.pdf#page=19)
and the minimal-model point-count identification from
[Chapter 3](https://johncremona.github.io/book/fulltext/chapter3.pdf#page=41).
Its primary-page inspection and exact recurrence comparison are reused;
no new essential source or changed theorem hypothesis calls for browsing.
L030's arithmetic proof establishes minimality and Delta=N=389; hence
every prime in indices <=256 is good. The nodal row at 389 supports the
separate sign input and must not be used as a good-prime recurrence.
L031 and L101 use a_1=1 and full untwisted coefficients: neither chi_5,
division by n, period normalization nor the derivative factor four is
part of the exported integer. This is source applicability review, not
a fresh derivation or acceptance of stored numerical entries.

The earlier twist-five audit covers stronger analytic/period evidence,
but does not alone audit this new restriction file. Histories 407/408
identify production followed by pending audit, not an already completed
independent audit. The recorded integration/backend stops and
ATTEMPTS/043's complex-to-p-adic comparison obstruction are different
targets; they are preserved and no exhausted mechanism is reopened.
The benefit here is provenance for L101's finite signed sum, conditional
on all still-missing kernels and its full error contract. It supplies no
arbitrary-curve rank comparison or progress beyond the known formulas.

## Approved single-invocation audit contract

1. Treat both original and extracted certificates and reports as fixed
   untrusted inputs. Do not rerun a producer or an entrypoint that
   overwrites original reports. Read complete relevant records, not
   inspector previews. Independently check all 54 good-prime rows and
   the separate nodal row, all fibers including two and infinity, all
   255 complete factorizations/prime-power records and all 256 slots.
2. In addition to complete replay, independently reconstruct coefficients
   from the verified prime traces using a different recurrence traversal
   (for example least-prime decomposition of every index, retaining
   coprime multiplicativity and the p multiplier). Compare every slot,
   including zeros and powers of two, against both fixed tables and
   every indexed export row. Require exactly the indices 1..128, with
   no gaps, duplicates or extra rows, and verify all source/hash/model
   bindings. Merely rerunning replay.py is insufficient.
3. Inventory and preserve all current coefficient and first-kernel files
   and canonical inputs before/after execution. Also check the old
   48-entry preservation inventory. Its L031 digest predates the step-408
   supplement: bind the old bytes to the retained copy at
   scripts/first-rational-kernel/step-404/originals/lemmas/L031-independent-twist-five-ratio-certificate.md,
   require its recorded old hash, and check that the complete current
   document differs only by the exact derivative-facing supplement
   before Mathlib. Persist this exact transition and both hashes; no
   pathname exemption is allowed. All other old entries must match.
   Preserve the current supplemented L031 bytes during the audit;
   any later audit annotation is a separately identified transition.
4. Use one aggregate setup/replay/comparison/preservation/final-writing
   execution, <=180 seconds and <=134217728 new artifact bytes, with
   finalization reserve. Save full records and print coverage, failures,
   actual/required bounds and paths. Preserve original printed timing
   as historical evidence only: the report saves 0.07647291710600257
   seconds before final write and a byte upper bound, not an independently
   persisted post-write duration. Fresh measured success does not
   retroactively prove historical timing. No retry or enlarged cap.

Continue only on complete equality and preservation within both caps;
the first mismatch, missing transition or cap failure parks dependent
work with its exact obligation saved. This review performs no replay or
mathematical calculation and accepts no certificate verdict. Full
matching Mathlib coverage remains not checked, not absent. The 127
remaining kernels, signed assembly, strict zero exclusion, uniform rank
comparison and refined formula remain unresolved. No lemma, mathematical
script, PROOF.md or DAG.md changes are needed for this source review.
