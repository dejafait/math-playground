# Immutable-byte literal checker — proposed implementation scope

TARGET: Implement a bounded immutable-byte literal-checker interface and verify exact primitive-rule and caller-byte retention.
CHECKED: 2026-10-24
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 465 inspected checker.check and the complete parameterized_input.py request boundary, generic emit/receive callers, occurrence bind_K, the complete step-459 race harness and L108 §11/L097 §9 provenance limits; reused steps 456/460/462 coverage and checked parked Attempts 037/038. Scoped call-site search found no existing byte checker. Read official Python io binary-stream/BytesIO/readline documentation and bytes.splitlines documentation on 2026-10-24.
SOURCE_EVIDENCE: Reuse Shoenfield (1967) §2.6 pp.21–22 and inspected step-460 primary coverage at https://w2.cs.uni-saarland.de/op/fullpaper/logics/SHOENFIELD_Mathematical_logic.pdf ; audited local L108 §§10–11 and L097 §§8–9 govern reception. Python documentation, rendered version 3.15.1: https://docs.python.org/3/library/io.html (Binary I/O, IOBase.readline, BytesIO) and https://docs.python.org/3/builtins/stdtypes.html#bytes.splitlines . No new mathematical theorem is imported.
COMPARISON: A snapshot-only replacement loses the existing changed-second-read rejection. Approve a byte checker plus a bounded second-read equality guard in the parameterized caller; preserve the old path API. Binary LF framing must survive the refactor, rather than substituting splitlines semantics for checker iteration.
GAP: Implementation and regression evidence remain absent. Byte-count caps do not establish total interpreter work/memory, filesystem latency, full positive occurrence reception or proof availability.
REASON: Essential changed-interface review is complete; ready rule coverage is reused. The restricted contract below removes the uncapped parsing boundary without authorizing snapshot-only path semantics, new algebra, endpoint synthesis or library preparation.
SCOPE: Immutable exact bytes with an explicit byte cap; unchanged primitive rule engine and evidence schema; unchanged strict caller preflight and dictionary/source retention; bounded second-read equality guard preserving the existing race-rejection fixture; legacy check(path, expected) retained.

The main gap remains unrestricted SAT. The intermediate target removes one
specific obstacle to reliable finite supplied-proof reception. Its downstream
use is checking caller-pinned proof bytes without an unbounded reopening of the
source path; it supplies no proof or witness existence premise.

Essential inputs: L108 §§10–11 and L097 §§8–9; the exact primitive rules,
`scripts/parity-four-rule/checker.py`,
`scripts/four-rule-extraction/parameterized_input.py`, existing generic
emitter/receiver call sites, output-459 authorization checks and output-464
audit evidence. Mathematical correction inputs remain audited L035/L036/L108.
Preserve the path-based interface where needed and all prior race-test evidence;
determine explicitly whether snapshot semantics changes any caller contract.

The next literature/scope turn should review only that interface difference
using ready exact-rule coverage. No broad source search or library preparation
is needed. Continue if bounded bytes retain all exact rule/header/endpoint and
original-caller checks. Test intercepted path replacement after the initial
bounded read: the checker must consume precisely those retained bytes and bind
its digest to the original caller. Malformed, oversized and changed endpoint
inputs must still reject. A semantic change requires an explicit assessed
contract or abandonment of that implementation.

Total interpreter work/memory bounds, full positive occurrence acceptance,
short proofs, M-only bounds, universal W₂, arbitrary ER data and SAT remain
outside scope. Trusted paths/SHA remain assumptions where hashes are used.
Mathlib coverage remains unchecked; Attempts 036/037/038 stay parked.
The preceding text records the initial proposal. Step 465 below approves only
the narrowed contract; no implementation has been performed.

## Step 465 — completed interface comparison

LITERATURE_REASON: The proposed byte interface changes an essential source-read
and authorization boundary outside the prior executable assessment. Existing
mathematical coverage remains adequate; this review resolves that difference.

### Evidence and source applicability

The exact-rule engine in `scripts/parity-four-rule/checker.py`, `check`, checks
the header, original-name membership, backward integer references, all seven
tag/arity cases, literal ordered premise trees and final endpoint. It computes
counts, node totals, raw-byte length and SHA while iterating a binary file.
`parameterized_input.request` already reads at most `input_bytes+1`, rejects
overflow, checks the caller SHA, strictly parses every line and checks the
caller header/goal before reopening that file through `checker.check`.
The second digest comparison occurs too late to cap the checker's parsing.
This is precisely the previously recorded limitation, not a newly found
mathematical defect.

The complete `audit_parameterized_input.py` interception replaces only the
second binary open by legal whitespace-changed bytes. It requires rejection
as `source changed during checking` after two opens. A byte checker alone
would never observe that replacement. Thus a snapshot-only substitution is
incompatible with the recorded rejection contract. This source-level
comparison is new evidence for narrowing the proposal; no executable test
was run in this literature turn. The old evidence is not regenerated.

The generic emitter and receiver both consume `request`'s raw bytes, records
and checker receipt. The receiver compares full source text, caller digest,
typed receipt, dictionary and symbol table. Occurrence `bind_K` separately
compares the K source text/digest and typed dictionary with the ORIGINAL
occurrence context. Retain these comparisons; byte-checker success alone
cannot replace cross-read caller authorization. Legacy fixture receivers and
audits also call `check(path, expected)`, so that interface must survive.

Reuse the precise mathematical coverage in the unchanged step-460 assessment,
“Ready source coverage and precise limitations,” and step-456 parameterized
assessment. Shoenfield's literal rules support the same engine; L108 supplies
the actual local extraction, rather than an attributed theorem about Python
or arbitrary proof-DAG code. Audited L035/L036 are unchanged downstream
correction inputs and require neither rereading their proofs nor reproof here.
No completeness or uniform short-proof premise is used. Attempts 036/037/038
remain relevant stops for other interfaces/preparation and are not restarted.

The official [Python binary-stream documentation](https://docs.python.org/3/library/io.html)
states that binary I/O performs no newline translation. IOBase.readline uses
LF as its binary line terminator; BytesIO provides an in-memory binary buffer.
The [bytes.splitlines documentation](https://docs.python.org/3/builtins/stdtypes.html#bytes.splitlines)
describes ASCII line boundaries, including its CRLF example. Consequently,
do not replace the checker's binary iteration by the caller's splitlines
preflight. Retain both stages and their existing framing behavior. These are
API specifications, not a proof of implementation equivalence or resource
complexity; record the actual interpreter version when implementing.

### Approved implementation and discriminating tests

1. Factor only the existing rule engine into a shared binary-stream helper.
   Keep `check(path, expected)` as a compatible wrapper. Add a byte-oriented
   entry accepting exactly immutable `bytes` and an explicit nonnegative
   integer byte limit, rejecting overflow before parsing. It must create its
   own private binary stream, not accept a caller-mutated stream or bytearray.
   Preserve exact rule comparisons, exceptions for invalid streams and the
   successful receipt schema; hash original bytes without reserialization.
   This entry's byte cap alone is not a general depth/work bound.
2. In `parameterized_input.request`, keep ALL existing strict source/request
   parsing, caps, header, endpoint, alphabet and dictionary checks. After that
   preflight, perform a second bounded source read using the existing bounded
   reader and compare its complete bytes with retained `raw`. An in-cap
   difference rejects as `source changed during checking`; oversize may reject
   at the byte cap. Do not parse second-read bytes. Then run the byte checker
   on the FIRST retained bytes with `CAPS['input_bytes']` and bind its receipt
   digest to the caller SHA as before. Direct equality strengthens cross-read
   byte comparison without changing accepted stable inputs. No unlimited
   fallback read is permitted.
3. Preserve generic raw source text, all records including unused lines, receipt
   types, ordered dictionaries and occurrence `bind_K`. Do not change old
   archives or hashes; write new evidence separately. No new caps dictionary
   entry or certificate format is needed merely for this read refactor.
4. Verify stable-input path/byte receipt equality on retained complete fixtures
   covering every primitive tag, constants, parallel premise occurrences and
   legal unusual names. Check LF, CRLF, missing final LF, blank lines and lone
   CR behavior against the old path engine; no normalization is allowed.
   Retain malformed-rule, duplicate-key, strict-reference, header/endpoint,
   oversized, foreign-caller and typed-dictionary rejection checks.
5. Replay the second-open whitespace interception: it must still reject with
   its recorded message. Intercept replacement by an oversized or deep payload:
   cap/equality rejection must occur before any checker parsing of replacement
   bytes. Instrument the byte checker to confirm it consumes precisely the
   retained original bytes and never opens the source path. Record actual
   bytes/limits, full receipts, failures and artifact paths. Tests must leave
   original fixtures unchanged. A bounded read does not bound blocking latency
   or certify atomic filesystem snapshots or changes after that read.

Continue if these exact-input and race tests pass. A receipt/framing difference,
weakened caller binding or unbounded fallback stops the affected change; save
its evidence and require separate assessment for a different contract. The
new byte entry and bounded guard are the only implementation delta approved.
No positive occurrence endpoint proof is available here; do not synthesize one
to fill coverage or promote rejection/component tests into full acceptance.

This is a specialization of ready mathematics and standard stream APIs, not
a new lemma or a claim of novelty. Full matching Mathlib coverage remains not
checked. Trusted caller paths and SHA assumptions for other bindings persist.
Unrestricted SAT, universal witness availability and total executable resources
remain unresolved. PROOF.md and DAG.md need no change because the mathematical
argument has not changed.
