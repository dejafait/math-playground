# Compiled bounded-buffer serializer — completed source comparison

TARGET: Implement and differentially check a compiled bounded-buffer native/literal-image serializer on the preserved step-261 vertex-0 checkpoint, without emitting the full production coordinate pair.
CHECKED: 2026-10-16
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the step-260 logical/interner assessment; searched the exact existing exporter, parser, checkpoint and watchdog paths and step-261 failure records. Fresh primary discovery queries were site:zlib.net manual deflate Z_FINISH gzwrite gzclose; site:rfc-editor.org rfc 8259 strings escaping json; site:docs.python.org time monotonic subprocess timeout. Inspected the primary contracts listed below, including the ctypes native-call boundary; no matching compiled exporter exists in the inspected local interfaces.
SOURCE_EVIDENCE: zlib 1.3.1 Manual, gzip File Access Functions (gzopen/gzbuffer/gzwrite/gzclose) and Basic Functions (deflate/inflate/deflateEnd); Adler's zlib Usage Example, complete compression loop and error/finish branches; RFC 8259 §§2,4,6–8; Python 3.11.17 json Basic Usage, ctypes Loading shared libraries/function prototypes/Surprises, and time monotonic/monotonic_ns, retrieved 2026-10-16. Logical inputs remain L056, audited L065, L066 and L068 §§6–10.
COMPARISON: Known interfaces support a bounded in-process compiled exporter and exact Python-byte comparison; they neither implement this consumer nor guarantee throughput, cap compliance or a complete coordinate. The old parser only parses/interns syntax, and the old Python writer expands whole strings. The previous active-duration timing rule omits phase gaps.
GAP: Essential source coverage is ready for the exact bounded implementation test below. Native ownership/ABI validation, exact full-field output, gzip completion/error rejection, absolute-deadline enforcement and useful measured speed remain implementation obligations; the full production coordinate pair is outside this approval.
REASON: Approve one later RESEARCH / implementation / REPRODUCTION attempt applying known contracts to the preserved checkpoint, with no logical reproof or new lemma. Approval rests on the concrete differential, resource and performance discriminators below, not on expected compression or unique-node counts.
SCOPE: Exactly TARGET; an in-process C-compatible compiled serializer using bounded chunks and zlib level-1 gzip, accessed through ctypes.CDLL, on the unchanged step-261 checkpoint. Bounded saved-record outputs only; no full production pair, fixture regeneration, closure reconstruction, other coordinate, chain or bridge.
LITERATURE_REASON: Changed compiled serialization consumer with essential unread streaming/compression interface contracts; the ready step-260 target covered the existing pool-aware consumer, not this implementation.

The main gap remains unrestricted SAT. The proposed intermediate target is
independently testable without another production coordinate run. It could
support later complete serialization/reception of the saved vertex-0 state;
it would not certify that coordinate by itself. The original proposal supplied
no implementation, throughput claim or approval. Step 262 below completes its
source review; no implementation or new lemma is supplied in this turn.

Essential inputs are L056, L065 including step-206 corrections, L066, L068
§§6–9 and the step-261 evidence section; the unchanged step-253 source,
envelope and twelve local archives; step-255 source pools; the audited
step-257/259 copier; and step-261's constructed checkpoint, exact byte counts,
executed-source snapshot, corrected fixed-prefix ledger and time-stop evidence.
The checkpoint remains trusted local pickle. Fixed string-key provenance,
ownership, assertion-enabled runtime, parser depth ≤4096 and full literal
field conventions remain qualifications. No fixture regeneration or second
production pair is proposed in this target. No cross-notebook input is used.

The review must distinguish structural sharing from expanded output and cover
ordered references/substitutions, literal double negations, exact JSON/header
bytes, bounded output buffers, full gzip termination, error handling, cache
ownership and fail-closed monitoring. It must specify a concrete differential
and performance discriminator before approving implementation. Retain RSS
2147483648 (stop 1610612736), 600 seconds, artifacts 17179869184 and expanded
output 137438953472; do not infer feasibility merely from compressed size or
unique syntax-node counts. Compare the 88420711187-byte complete proposed pair
with the observed Python writing stop; a benchmark estimate is not a checked
production coordinate or a guarantee of later full replay.

Continue only with approved exact-output tests and a defensible performance
discriminator; abandon a mismatch, buffer/cap failure or no useful improvement.
Other coordinates, indexed chain/bridge, nested retention, combined original
source ledger, ordinary-input completeness, certificate existence, ER/W/V/U
and unrestricted SAT remain unresolved. Full Mathlib coverage is not checked.

## Step 262: primary contracts and exact applicability

This is a literature-only comparison, not a serializer test or a renewed
production attempt. Reuse the unchanged mathematical coverage in
`2026-10-16-interned-first-closed-coordinate.md`: L056's syntactic translation,
L065's audited construction/step-206 count repairs and L066's local packages
remain conditional inputs. Their mathematical statements need no reproof.
The changed boundary is writing already stored rows, not constructing or
approving new mathematics. No cross-notebook input is used.

Primary sources actually inspected, with version and limits:

- [zlib 1.3.1 Manual](https://www.zlib.net/manual.html), January 22, 2024,
  gzip File Access Functions: `gzbuffer` must precede I/O; its stated buffer
  allocation is three times the chosen size. `gzwrite` reports uncompressed
  bytes written, or zero on error. `gzclose` flushes/closes and returns an
  error code; query `gzerror` before freeing its handle. Basic Functions:
  `Z_FINISH` needs repeated output space until `Z_STREAM_END`; `deflateEnd`
  discards pending input/output rather than completing it. `inflate` gzip
  mode stops at one member, whereas `gzread` accepts concatenation and even
  transparent non-gzip input. These distinctions matter to strict reception.
  They supply neither a total memory ceiling nor a speed guarantee.
- Mark Adler, [zlib Usage Example](https://zlib.net/zlib_how.html), live
  unversioned page, retrieved 2026-10-16: inspected `def()` from initialization
  through cleanup, especially the inner output loop, short-write/error
  branch and final `Z_STREAM_END` assertion. Its fixed chunks demonstrate
  streaming without a whole-file buffer. Its ordinary example is zlib
  framing, so it cannot simply replace a gzip writer. The `inf()` completion
  discussion distinguishes stream completion from input exhaustion. This
  is an implementation pattern, not a proof of correctness of our exporter.
- T. Bray, [RFC 8259](https://www.rfc-editor.org/rfc/rfc8259.html), STD 90,
  December 2017, §§2,4,6–8, pp.5–10: JSON whitespace and object member order
  do not specify one byte encoding; strings require escaping quotes,
  backslashes and controls. Names should be unique; duplicate-name receiving
  behavior varies. Number grammar does not enforce this notebook's literal
  integer reference types. Therefore JSON validity alone is insufficient.
  JSONL framing, key order and byte identity are our narrower local contract.
- [Python 3.11.17 json](https://docs.python.org/3.11/library/json.html),
  Basic Usage and encoder notes: compact separators and `ensure_ascii`
  control spelling; default encoding preserves input order. JSON is not
  framed. `interned_255.enc`, with its explicit final newline, remains the
  byte oracle. Reuse the prior strict duplicate/type receiver, rather than
  adopting permissive default decoding as proof validation.
- [Python 3.11.17 ctypes](https://docs.python.org/3.11/library/ctypes.html),
  Loading shared libraries, function prototypes and Surprises: `CDLL` uses
  the C calling convention, defaults to integer returns and releases the
  GIL during foreign calls; `PyDLL` does not release it. Explicit
  `argtypes`/`restype` and retained owner objects are necessary; structure
  subobjects may alias their original buffer. This supports a heartbeat
  during native work, but does not validate pointer lifetimes, native code
  or resource accounting.
- [Python 3.11.17 time](https://docs.python.org/3.11/library/time.html),
  `monotonic`/`monotonic_ns`: the clock does not go backwards or follow
  system-clock updates; its origin is unspecified, and differences are
  meaningful. On macOS it is system-wide starting with Python 3.10.
  Keep one parent's absolute deadline in that clock domain throughout this
  run, instead of summing worker lifetimes. This is an engineering
  application of the contract, not an enforcement theorem.

The installed compiler, header/runtime zlib versions and newly built binary
are not verified by reading these documents. Record and check them during
implementation; a missing/incompatible interface stops the attempt without
installing dependencies or silently changing mechanisms. No essential source
is blocked. No unread lead supports an assertion. Matching Mathlib coverage
of this concrete exporter remains not checked, not asserted absent.

## Local overlap and preserved failure comparison

Read `coordinate_261.py`'s ByteCount, checkpoint and write_pair;
`interned_255.py`'s enc/Syntax.spelling/Package.record/load;
`copier_257.py`'s pool/restore contracts; the complete
`left-closure/native_parser.cpp` and `fast_syntax.py` adapter; and
`watch_255.py`, `rss_worker_255.py`, `watch_261.py` and
`watch_inspect_261.py`. Also inspected L068 §§7,10, L056's translation/basis,
L065's step-206 correction and L066's source hypotheses, history/261 and
ATTEMPTS/025. Searches were restricted to these consumers and dated local
assessments/history. This is not a claim of a global duplicate search.

The native parser exports structural constructors/info and a depth-limited
parser, not a serializer. Its `Info.name` is borrowed from pool storage;
the exporter must not retain such a pointer across mutation/free. Use an
immutable owned snapshot and explicit lifetime, with no concurrent pool
mutation. Do not alter the old parser ABI or overwrite its binary. Native
exceptions must become checked C-boundary errors, never cross ctypes.
The Python Package emits every formula and substitution in row order and
preserves substitution insertion order. `Syntax.spelling` is iterative but
still builds the whole expanded string. `finish_exports.Spelling` is an
older bounded-cache tuple writer, not this owned-pool exporter. These are
oracles/patterns, not a ready implementation of TARGET.

L056's image is literal: native implication `(A>B)` becomes `((~A)|B)`;
NOT remains `(~A)`. Double negations stay. Native names are admitted only
as nonempty ASCII alphanumeric/underscore payloads; fixed string keys and
rules are separately whitelisted. Under precisely this checked alphabet,
the local formula strings need no JSON escaping. Reject anything outside
the alphabet/schema instead of claiming a general Unicode JSON exporter.
Headers are ordered format then goal; records are f then rule then refs
or subs. Decimal reference order, every substitution field and final newline
must equal `enc(Package.record(...))` literally. No row pruning, output
simplification, reference renumbering or occurrence merging is approved.

The step-261 complete report's selected `/actual_required` and
`/complete_proposed_bytes` values were read in full with the JSON inspector.
They retain 35536722766/52883988421 proposed expanded bytes, the failed
629.8588169754948/600-second interval and the truncated native output. These
are existing evidence, not fresh calculations or new reception. The old
watchdog has a local start for each monitor and the inspection launcher
subtracts only active durations. Native work also changes the monitoring
boundary: Python audit hooks alone cannot prohibit a native fork, and a
held GIL can starve the heartbeat. Inspect the new native code for process
creation, use CDLL, and explicitly account for any compiler subprocesses.
No historical stop prohibits this different bounded test; the failed
full-field writer and gap-omitting launcher stay parked.

## Approved bounded implementation and discriminating tests

All items below are tests to perform later, not results of this review.
Save an incomplete certificate before build/loading, and report failures,
actual/required bounds and complete artifact paths. Preserve original files.

1. Reload the trusted local constructed checkpoint without regenerating
   fixtures or running Closure. Check its source identities, complete owned
   topological nodes, exact four-field rows and stored endpoint against the
   preserved step-261 evidence. `copier_257.restore`'s imported-only
   `start==len(rows)` assertion does not admit the generated tail: reuse the
   step-261 inspector's explicit prefix/generated-tail validation rather
   than weakening the old copier contract. Preserve external provenance,
   strict literal integer indices and parser depth qualification ≤4096.
2. Implement a separate in-process compiled serializer through a typed C
   interface/CDLL. Permit at most a 65536-byte staging chunk and a separately
   recorded bounded spelling cache (at most 33554432 payload bytes, with its
   allocation/metadata included in RSS); a cache is optional. Traversal must
   expand every child occurrence in order without recursively allocating
   whole parent strings. Validate lengths/indices before native access;
   use checked wide counters, with no overflow or pointer-lifetime reliance.
   Keep buffers, traversal stacks, node/row transfers and compressor state
   in the resource account; a chunk limit alone is not an RSS bound.
3. For both formats compare complete uncompressed bytes, not selected
   fields or hashes alone, against the unchanged Python oracle. Select
   deterministically from the saved checkpoint: a complete valid proof
   prefix with goal equal to its actual last row, and contiguous beginning,
   middle and end record windows bounded by the existing byte counter.
   Include each rule, both reference positions, every ordered substitution,
   repeated syntax/rows, q=x, the first/last rows and a maximum-size row in
   each format. Cap the total selected differential output at 268435456
   expanded bytes across both formats; record exact selected indices and
   coverage. A disconnected window is only an exact-record test. Completely
   replay the valid prefix in both formats and retain its explicit endpoint;
   never describe windows as a complete coordinate. The byte counter must
   agree on every tested complete record and header.
4. Use level-1 gzip, bounded writes and checked completion/error results.
   Reinflate every bounded output completely, require one complete gzip
   member with no trailing/concatenated data and compare all output bytes
   with the oracle. Compressed bytes need not match the Python archive's
   gzip metadata. Deliberately reject invalid node/row indices, non-ASCII
   payloads, wrong rule/substitution schema, Boolean/float reference values,
   changed image/header/reference fields, truncated trailer, bad checksum,
   extra member/trailing bytes and injected sink/close failure. Test chunk
   boundaries at tiny buffer settings as well as the chosen production
   buffer. Preserve failure artifacts; do not accept an unfinished gzip.
5. One parent deadline covers build, self-tests, checkpoint transfer,
   differential work, benchmark, verification, reporting and phase gaps.
   Set it once before experimental preparation; stop useful work early
   enough to save the report before 600 seconds. No relative timer reset or
   gap subtraction is allowed. Test an inserted inter-phase delay and an
   already expired deadline: subsequent work must not launch. Test a
   missing heartbeat/native stall and RSS/output-budget failure as well.
   Include compiler children and their peak memory in build accounting;
   the old child-free worker report cannot certify an unmonitored build.
   If such accounting is unavailable, stop at that boundary. For native
   execution retain the parent/worker heartbeat and terminal-peak checks,
   with their sampling limitation; do not call this a continuous hard cap.
6. On the same deterministic saved-row windows, time Python and compiled
   render-plus-level-1-gzip through successful close, with identical
   uncompressed content. Record cold setup separately, then one matched
   comparison per selected window/format, without a tuning loop. Cap all
   benchmark emissions combined at 1073741824 expanded bytes, including
   oracle and repeated output; all other new payloads remain counted too.
   The prespecified useful-improvement test is at least a factor of two
   reduction in aggregate timed serialization duration in each format,
   with all correctness/resource tests passing. This is an engineering
   continuation threshold, not a theorem or evidence of full-run feasibility.

Unchanged maxima remain RSS 2147483648 bytes (stop 1610612736), total
elapsed 600 seconds, new artifacts 17179869184 bytes and aggregate expanded
payload 137438953472 bytes; the smaller test budgets above do not raise them.
The existing 88420711187-byte proposed production pair is a comparison scale
only. Report measured rates and any projection as estimates, separately from
actual expanded bytes and complete replay. Neither passing the factor-two
test nor fitting a writer-only projection certifies a future full-pair
writer/replay pipeline. That larger target would require separate coverage.

Continue this mechanism only if the exact bounded test passes and supplies
the prespecified useful improvement. A mismatch, unsafe ownership/ABI,
unsupported monitoring, cap breach or speed failure parks the exporter with
its evidence; do not repeat a production run or raise limits. Passing provides
local implementation evidence for one output boundary. All remaining
coordinates, complete vertex-0 serialization/reception, indexed chain/bridge,
nested retention, combined original-source ledger, ordinary-input completeness,
certificate existence, ER/W/V/U and unrestricted SAT remain unresolved.
