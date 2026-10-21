# Pool-index cached Python serializer — completed source comparison

TARGET: Implement and differentially check an iterative pool-index adaptation of the existing bounded-cache Python spelling writer on the preserved step-261 checkpoint, without emitting the full production coordinate pair.
CHECKED: 2026-10-16
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused step-262 primary JSON/gzip/time and logical coverage; inspected finish_exports.py Spelling/write, interned_255.py Syntax.spelling/Package.record/enc, copier_257.py owned/pool/restore, coordinate_261.py ByteCount/write_pair, inspect_261.py, watch_255.py/watch_261.py and rss_worker_255.py; compared ATTEMPTS/025 and 026. Fresh primary inspection: Python 3.15.0 collections OrderedDict, gzip GzipFile, zlib decompression state and resource getrusage, 2026-10-16.
SOURCE_EVIDENCE: Python 3.15.0 documentation: collections OrderedDict.popitem/move_to_end and LRU recipes; gzip GzipFile/close/decompress; zlib Decompress.unused_data/unconsumed_tail/eof/decompress; resource Resource Usage/getrusage/ru_maxrss/RUSAGE_SELF. Reuse RFC 8259 §§2,4,6–8 and Python json/time contracts precisely recorded in 2026-10-16-compiled-coordinate-serializer.md; logical statements remain unchanged.
COMPARISON: Known cache and traversal components cover supporting operations, not this combined consumer. Tuple-owner identity keys must become one retained pool plus literal integer indices and a fixed format; recursion must become iterative without an unbounded expanded-value memo. Existing full-field buffers and old per-worker timing cannot be assumed bounded by cache payload or one shared deadline.
GAP: Coverage ready for exactly TARGET under the binding implementation conditions below. No adapted serializer, byte equivalence, cap-compliant execution, useful speed or full coordinate reception is established.
REASON: Approve one later RESEARCH / implementation / REPRODUCTION attempt specializing existing engineering contracts, with exact-output, memory, deadline and factor-two discriminators. No new mathematical result, logical reproof or production pair is approved.

This is the sole proposed continuation, not another attempt in step 263. The
separate review should reuse adequate primary sources rather than repeat web
discovery. It must compare the exact existing tuple-cache implementation with
the proposed immutable owned pool-index interface, including eviction, owner
lifetime, repeated occurrences, substitution order, literal double negations,
and arbitrary admitted depth up to 4096. Cache payload is at most 33554432
bytes and entries at most 32768; metadata and all simultaneously live expanded
strings must count toward RSS. No cached abbreviation may enter an archive.

Essential inputs: L056; L065 with step-206 corrections; L066; L068 §§6–11;
step-253 unchanged source/envelope/twelve archives; step-255 pools; audited
step-257/259 copier; step-261 constructed checkpoint, exact counts, corrected
fixed-prefix ledger and failure evidence; finish_exports.Spelling/write;
step-263 build-admission failure. No cross-notebook input is proposed.
Trusted local pickle/external provenance, literal integer indices, fixed
ASCII string keys, immutable owned syntax, enabled assertions and parser
depth ≤4096 remain qualifications. Generated-tail validation must use
inspect_261's explicit prefix/tail contract rather than copier_257.restore.

Proposed discriminator for review: unchanged Python enc/Package.record byte
oracle; deterministic valid prefix plus beginning/middle/end windows covering
every rule/substitution/reference, repeated syntax/rows, q=x and both maximum
rows; ≤268435456 total differential expanded bytes. Replay the complete valid
prefix in both formats and label disconnected windows only as record tests.
Compare complete reinflated bytes and exact byte-counter values; reject all
schema/type/image/reference corruptions, truncation/checksum/extra gzip data
and sink/close failures. Use one absolute 600-second deadline from before
preparation through reporting, child-free heartbeat/terminal-peak accounting
and explicit deadline-gap, expired-start, stall/RSS/output failure tests.
Preserve RSS maximum 2147483648 (stop 1610612736), artifacts 17179869184 and
expanded 137438953472, with no production pair or raised cap. A single matched
render-plus-level-1-gzip/close comparison per selected window and format must
give aggregate factor ≥2 in each format, with ≤1073741824 total benchmark
expanded bytes and all other tests passing. These are proposed acceptance
conditions for separate review, not executed tests or established bounds.

Passing could support a later full-coordinate output/reception assessment;
mismatch, failed accounting/cap or insufficient speed parks this mechanism.
Complete vertex-0 serialization/replay, other coordinates, chain/bridge,
nested retention, combined original-source ledger, ordinary-input completeness,
certificate existence, ER/W/V/U and unrestricted SAT remain open. Full
Mathlib coverage of this concrete consumer is not checked.

## Step 264: completed interface and source comparison

This section supersedes the proposal-only approval language above; it preserves
the exact target and its proposed discriminators. LITERATURE_REASON: the changed
pool-index/cache interface had essential uncovered ownership, temporary-memory
and compiler-free monitoring obligations after step 263. Existing logical and
JSON/time coverage is reused rather than rediscovered. No lemmas or mathematical
scripts are changed. No theorem is reproved and no novelty claim is made.

Primary sources actually read (Python 3.15.0 documentation, retrieved
2026-10-16; record the actual execution runtime separately):

- [collections, OrderedDict](https://docs.python.org/3.15/library/collections.html#ordereddict-objects):
  `popitem(last=False)` evicts the oldest item; `move_to_end` updates recency.
  The LRU recipes provide a pattern, not a payload or total-memory guarantee.
- [gzip, GzipFile and decompress](https://docs.python.org/3.15/library/gzip.html):
  level 1 is supported; context management closes the gzip stream. A supplied
  file object has its own close responsibility. Convenience decompression
  accepts multiple members, so it does not enforce our single-member contract.
- [zlib, decompression objects](https://docs.python.org/3.15/library/zlib.html#decompression-objects):
  `eof` distinguishes completion from truncation; `unused_data` exposes bytes
  after the member; `unconsumed_tail` needs further processing when bounded
  output fills. Require EOF, no residual/trailing input and successful close.
- [resource, Resource Usage](https://docs.python.org/3.15/library/resource.html#resource-usage):
  `getrusage(RUSAGE_SELF)` includes process usage and `ru_maxrss` reports its
  maximum resident size. Platform units must be checked; it is not a continuous
  enforcement or a sum of descendant peaks.

These are API contracts, not mathematical source theorems. The existing exact
logical inputs L056, audited L065/step-206, L066 and L068 §§6–11 are reused with
unchanged hypotheses. Mathlib coverage of this concrete consumer is not checked.
No unread lead supports approval. No cross-notebook result is used.

### Binding specialization and test boundary

1. Retain exactly one live immutable validated pool per cache instance and a
   fixed native/image mode. Validate `type(index) is int`, range and owner at
   entry; reject wrong pool, closed owner, Boolean/float/bare foreign indices.
   Never reuse a cache across pools, formats or mutation. Pool nodes are
   canonical topological tuples under `copier_257.pool`; use its validation,
   not arbitrary trusted indices without checking. Keep the pool alive through
   all cache use. Cached values are complete literal strings, never archive
   abbreviations. All repeated proof rows remain separate.
2. Adapt traversal with explicit frames and local child values. No recursion
   or unbounded all-node expanded-text memo is admitted. Cache eviction must
   not invalidate child values needed by an active frame: hold those values
   locally or recompute, and count them as live memory. Never assume a child
   remains in the cache until its parent returns. Retain exact operand order,
   negations including double negations, variable names and literal-image
   spelling. Substitution has already occurred in the saved rows; do not
   apply another recursive substitution or rename schematic collisions.
3. Cache limits are simultaneously 33554432 ASCII payload bytes and 32768
   entries. Before insertion evict enough entries; skip oversized strings.
   Replacement must remove its old byte charge, and clearing must zero it.
   Payload excludes Python headers, dictionary entries, active frames, child
   strings and temporaries. Count all of those in monitored RSS. Use the
   existing exact length tables to admit each field/row before rendering;
   explicitly account for simultaneous rendered formula/substitution strings,
   concatenation/join temporaries, JSON text, encoded bytes, comparison oracle
   and gzip buffers. A twelve-line heuristic alone does not bound an explicit
   frame stack retaining expanded values at depth 4096. Supply conservative
   workspace admission from the selected traversal, or fail closed before
   allocation. Test cache eviction/recomputation, cold/warm mode separation,
   oversized values, repeated children and depth-4096 admitted syntax without
   imposing Python recursion limits. No total-memory theorem follows here.
4. Restore the generated checkpoint by `inspect_261`'s prefix/import/tail
   contract, including external expected provenance, exact typed schema,
   all primitive rows, corrected fixed-prefix ledger and final endpoint.
   `copier_257.restore` requires imports ending at the last row and therefore
   cannot restore this generated tail unchanged. Preserve trusted-local pickle,
   fixed ASCII keys, enabled assertions and parser depth qualifications.
5. Use the unchanged `interned_255.enc` and `Package.record` as byte oracle.
   Preselect deterministic valid prefix and beginning/middle/end windows with
   every rule, substitution/reference form, repeated syntax/rows, q=x and both
   maximum rows. Include header/goal bytes. Save selected indices and coverage;
   a missing discriminator fails admission. Compare complete reinflated bytes,
   every record field and independent exact byte-counter totals, not hashes
   alone. Differential expanded bytes ≤268435456. Replay the complete valid
   prefix in both formats. Disconnected windows are record tests only; do not
   renumber them and call them complete proofs. Run schema/type/image/reference
   corruptions and truncation, checksum, extra-member/trailing-data, write and
   close failures. The strict decoder must inspect all compressed input, even
   bytes arriving after EOF in a later read. Sink errors never yield success.
6. No compiler/build or worker children are admitted. Reuse the inspected
   child-denying worker and existing parser binary; do not silently trigger a
   parser rebuild. Check binary availability before loading the checkpoint.
   Fix monitoring to pass one absolute monotonic deadline from before all
   preparation through final reporting, including phase gaps and validation;
   never reset it or sum active durations. Check before each launch and stop
   expired starts. Recheck terminal parent-plus-worker peaks against the stop
   threshold, not merely after adding a final heartbeat to the report. Test
   missing heartbeat/stall, allocation/RSS, output limits, phase-gap expiry and
   expired starts. A stalled GIL heartbeat is a stop, not permission to disable
   monitoring. Include every live cache/oracle/buffer and report partial data
   on failure. Monitoring remains sampled, with no continuous hard-cap claim.
7. Keep RSS maximum 2147483648, stop 1610612736; one 600-second absolute
   deadline; new artifacts ≤17179869184 and expanded bytes ≤137438953472.
   Charge all actually produced/reinflated experimental data consistently and
   reserve room/time for certificates and reporting. Differential and benchmark
   subcaps are additional, not replacements. Do not load production checkpoints
   merely to perform this literature review (none was loaded).
8. For each preselected window and format, one matched original-writer versus
   adapted-writer render-plus-level-1-gzip/close comparison, same records and
   sink type; include fresh cache setup and all serialization work, exclude
   neither close nor warm-up work from the adapted timing. Sum timings per
   format and require baseline/adapted ≥2 separately in native and image.
   Total benchmark expanded bytes ≤1073741824, including both writers.
   Save timings, bytes, runtime, selection and cache/peak statistics. No retries
   or selective windows to improve the ratio. Byte/count correctness, rejection
   tests and all caps must pass as well. Insufficient speed, mismatch or failed
   accounting parks this mechanism without a production pair or raised caps.

The historical full-field time stop and compiler-admission failure remain
intact. This is a different cache-reuse mechanism with a falsifiable local
performance test, not a claim that cache hits reduce expanded archive length.
Passing could support a separate full-coordinate output/reception assessment;
it would not certify the missing production pair. Complete vertex-0 replay,
other coordinates, chain/bridge, nested retention, combined original-source
ledger, ordinary-input completeness, certificate existence, ER/W/V/U and
unrestricted SAT remain open. PROOF and DAG do not change.
