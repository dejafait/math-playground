# Immutable-byte checker — separate critical-audit scope approved

TARGET: Critically audit the bounded immutable-byte checker, equality guard, and retained caller authorization evidence.
CHECKED: 2026-10-24
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 467 compared the saved step-465 interface assessment, L108 §§1,11–12, L097 §9, steps 465/466 histories and Attempts 036/037/038; scoped searches located the two checker wrappers, request read boundary and AST/race harness. Existing coverage is adequate for this unchanged-rule finite audit; no external rediscovery or executable audit was performed.
SOURCE_EVIDENCE: Reuse inspected Shoenfield, Mathematical Logic (1967), §2.6 pp.21–22 at https://w2.cs.uni-saarland.de/op/fullpaper/logics/SHOENFIELD_Mathematical_logic.pdf ; official Python io Binary I/O, IOBase.readline and BytesIO at https://docs.python.org/3/library/io.html and bytes.splitlines at https://docs.python.org/3/builtins/stdtypes.html#bytes.splitlines as recorded in step 465 (rendered 3.15.1; implementation 3.15.0). Audited L035/L036, L108 and L097 supply the qualified local interfaces; primary mathematical comparison is retained in the unchanged step-460 assessment.
COMPARISON: Exact-rule mathematics is unchanged; binary-stream specifications cover the private BytesIO wrapper and LF framing, while the prior implementation assessment covers the bounded second-read equality contract. Neither source specifications nor the existing harness independently certify code or caller authorization. Approve only independent finite review of this delta and its retained evidence.
GAP: Independent correctness review of wrappers, normalization, bounded reads, AST baseline selection, full receipts and original-caller bindings remains undone. Full positive occurrence reception, total interpreter bounds and unrestricted SAT remain unresolved.
REASON: Separate scope comparison is complete using adequate retained source coverage; next turn defaults to the exact finite critical audit, without new mathematics, library preparation or changed acceptance contracts.

The main gap remains unrestricted SAT. The intended intermediate target is a
separate critical review of the small implementation delta and its finite
evidence, for reliable supplied-proof reception. No lemma, proof synthesis,
new cap, new algebra or all-size resource theorem is proposed.

Essential inputs: L108 §§10–12, L097 §§8–9, audited L035/L036;
`scripts/parity-four-rule/checker.py`,
`scripts/four-rule-extraction/parameterized_input.py`, unchanged generic
emit/receive and occurrence `bind_K`; the complete
`scripts/four-rule-extraction/test_immutable_bytes.py`; baseline code and
`scripts/four-rule-extraction/output-466/` certificates/receipts, step-459
authorization evidence and step-464 caller-binding audit. Read selected complete
receipt fields and all load-bearing evidence, not whole unrelated archives.

Suggested discriminating review after approval: independently compare the full
old engine and new helper, verify normalization and binary framing, trace capped
second reads and ensure replacement bytes cannot enter either parser, check exact
original-caller receipt/source/dictionary retention, and review/replay the saved
framing, type/cap, race and generic regression evidence without overwriting prior
outputs. Continue on exact agreement within the assessed scope; a weakened
authorization or unbounded fallback requires a concrete repair or stop.

Trusted caller paths, remaining SHA bindings, filesystem latency, changes after
the second read, total interpreter resources and full positive occurrence proof
reception remain unresolved. Legacy path checking is deliberately still uncapped.
No proof existence, M-only bound, universal W₂, arbitrary ER or SAT consequence
follows. Mathlib coverage remains unchecked; Attempts 036/037/038 stay parked.

## Completed scope comparison — step 467, 2026-10-24

LITERATURE_REASON: The new critical-audit target required separate scope approval
for the changed immutable-byte and equality boundary; existing mathematics and
API coverage are reused rather than searched again.

The preceding pending proposal is now approved within the boundary below.
This approval does not supply the audit verdict. The main gap is unrestricted
SAT decision/separation. The intermediate target is independent finite reception
review; downstream use is trustworthy reception of a future supplied proof.
There is no new lemma, reproof or progress beyond the mathematical sources.

### Applicability and duplicate/failure comparison

Step 465 already inspected the exact stream specifications: binary I/O performs
no newline translation, binary readline terminates at LF, and BytesIO provides
an in-memory binary stream. bytes.splitlines has different boundary semantics.
These retained specifications apply to the same wrappers and caller preflight;
no changed API hypothesis requires fresh browsing. The implementation's 3.15.0
versus recorded documentation 3.15.1 distinction must remain explicit; neither
version label certifies runtime equivalence. The audit must inspect behavior.

Shoenfield §2.6 supplies the literal directed rules, with the local constant
axioms separately specified in L108. Completeness is not required to check an
already supplied proof. L108 §§1,11–12 and the unchanged step-460 assessment
retain the precise limits of the LTW formula/tree comparison; it is not a
source theorem about Python, proof-DAG reuse or provenance. Audited L035/L036
supply the actual original-only correction contracts. No change to those
inputs justifies reproof or another extraction lemma. Full matching Mathlib
coverage remains not checked.

The scoped source read located check/check_bytes/_check_stream, read_bytes,
request, and equivalent_engine/guarded_reads. The old and byte wrappers both
normalize the expected tree; the byte wrapper uses a private BytesIO. The
request retains strict first-byte preflight, then invokes the bounded reader
for an equality check before passing the first bytes to the checker. These
observations identify a covered audit boundary, not an independently verified
all-input correctness conclusion. Review the entire engine and its baseline,
not merely the AST equality flag or the inspected wrapper ranges.

L108 §11 already records the whitespace replacement and original-caller
rejection contract; L097 §9 already separates checked generic receipt binding
from occurrence bind_K. Step 466 is the implementation evidence to audit,
not an independent certification of itself. Attempts 036/037/038 concern the
old opaque-OR presentation or failed library preparation; this supplied-proof
audit requires neither route and does not reopen them.

### Exact approved test and stopping boundary

Next turn inspect the complete changed modules and harness, the retained
baseline, and complete load-bearing output-466 receipt/race/regression fields.
Independently verify the AST extraction boundaries and wrapper normalization,
all seven exact tags, binary framing, first-byte identity and original-caller
source/dictionary checks. Use output-459 authorization and output-464 provenance
only for their retained contracts; their old code hashes cannot automatically
certify changed dependencies. Review/replay evidence in a fresh output location,
without rerunning archive-writing drivers over old outputs. No proof synthesis,
new cap, new algebra or broad resource theorem belongs to this audit.

Continue if exact receipt/framing and caller bindings agree, replacement reads
are bounded and never parsed, and complete finite evidence survives review.
A weakened binding, incorrect baseline comparison or unlimited fallback requires
a specific repair or a stop with preserved evidence. Persistent unrelated
proof-preparation blockers do not justify repeating preparation here. Legacy
uncapped callers, trusted paths/remaining SHA assumptions, filesystem latency,
post-second-read changes and absent positive occurrence reception remain explicit.
