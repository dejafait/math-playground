# Lossless interned native-package reception — completed scope comparison

TARGET: Implement and completely validate a lossless interned native-package loader on the six preserved step-253 local pairs, retaining every record/reference and exact expanded statistics within 2 GiB RSS.
CHECKED: 2026-10-16
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 254 searched hash-consing/maximal-sharing terminology and primary Python JSON documentation; inspected the primary ML 2006 paper §§1–2.3, local strict parser/scanner, aggregate.load/copy, Store.retain, Closure initialization, L056/L065/L066 receiving contracts, L068 §6 and the recorded step-207/253 failures. No full matching cap-bounded package loader was established by these sources.
SOURCE_EVIDENCE: Filliâtre–Conchon, Type-Safe Modular Hash-Consing, ML 2006, §§1–2.3, PDF pp.1–4, especially §2.1 equation (1) and §2.3 lookup-or-insert; Python 3.11.17 json documentation decoder conversion table, object_pairs_hook and Repeated Names; reused L056 fixed-calculus/substitution coverage and L065 step-207 exact native-parser/strict-replay justification.
COMPARISON: Known structural hash-consing and the existing strict interned scanner cover syntax equality and primitive replay; aggregate.load instead retains recursively materialized tuple trees. The implementation difference is a complete ordered package of formula/substitution IDs and literal references with exact expanded accounting and monitored lifetime, not a new logical theorem or a smaller serialized proof.
GAP: Implement and test the retained package interface, all-record round trips, simultaneous substitution/relocation probes, exact expanded statistics and RSS envelope; neither source citations nor previous scanner success establish the six-package loader or its resource contract.
REASON: The changed receiving representation has adequate source coverage for one bounded reproduction attempt. Separate scope review is complete; implementation and its success remain unverified.
SCOPE: Exactly TARGET on preserved local-0 through local-5 native/not-or pairs under scripts/output-zero/output/nonempty-253/; standalone lossless reception and bounded copy/checkpoint probes, with no coordinate generation, joined output or fixture regeneration.
LITERATURE_REASON: Changed implementation hypothesis after step 253: retain structurally interned syntax instead of expanded tuple trees, and monitor reception operations rather than only stage boundaries.

## Relevance and decision boundary

The main gap remains ordinary uniform worst-case P versus NP. The intermediate
target is exactly TARGET. A checked receiving layer could later expose the
preserved L066 local packages to L065 without the failed materialization cost.
It does not supply coordinate construction, a joined L068 output, ordinary-input
completeness, certificate existence, arbitrary ER representation, W/V/U or SAT
transfer. Full expanded-output feasibility and the combined original-source
ledger remain independent obligations. No mathematical claim is derived here.

This assessment replaces the step-253 REVIEW_REQUIRED proposal, preserving
its target, six complete pairs, strict full-field tests and 2 GiB threshold.
The prior proposal did not approve an implementation. This separate turn now
approves only a bounded implementation/reproduction attempt. SPECIALIZE is
appropriate because the operation is known but the concrete complete-record
interface and measured resource contract require implementation evidence.

## Primary sources actually inspected

Queries were `hash consing maximal sharing Filliatre Conchon 2006 paper hash
consing` and `site.docs.python.org 3 library json boolean integer
object_pairs_hook`. Primary-reference following reached the author PDF and
versioned Python documentation; search snippets were not used as coverage.

[Filliâtre and Conchon, ML 2006 author PDF](https://usr.lmf.cnrs.fr/~jcf/publis/hash-consing2.pdf),
*Type-Safe Modular Hash-Consing*, §§1–2.3, PDF pp.1–4, inspected 2026-10-16.
Section 1 requires systematic smart-constructor use. Section 2.1 equation (1)
relates structural equality, physical equality and tags under a single table
and enforced construction discipline. Its hash must respect the chosen equality.
Section 2.3's bucket lookup compares equality, rather than accepting hash
agreement; it also discusses table lifetime and weak pointers. Only structural
syntax equality is relevant here. The paper supplies neither this proof-record
format nor a 2 GiB bound. Its OCaml implementation is not imported as a verified
Python/C++ loader. Its later SAT-specific simplifications are outside this
reception contract. No source result needs a new mathematical reproof.

[Python 3.11.17 JSON documentation](https://docs.python.org/3.11/library/json.html),
JSONDecoder conversion table, object_pairs_hook, Standard Compliance and
Repeated Names Within an Object, inspected 2026-10-16. Integer, real and Boolean
JSON values decode to different Python types; the default decoder accepts
repeated object names, retaining the last value. object_pairs_hook permits
checking the full ordered field list before dictionary construction. The local
strict scanner additionally requires literal integer references in both formats.
These documents do not certify that scanner or imply a memory bound.

No exact full-result Mathlib coverage was checked; the sources are programming
and proof-format inputs, not a new Mathlib theorem. Further hash-consing papers
returned by search were unread leads and are not essential dependencies.

## Local comparison, duplicates and failed routes

L056's Hypotheses and primitive/copying proof require fully expanded serialized
formulas and literal simultaneous substitution; internal sharing must not
change that contract. The fixed-calculus source assessment is reused, without
refreshing unrelated Frege or algebraic sources. L065 Hypotheses require all
local occurrences, arbitrary supplied depth, exact endpoints and all unused
records. L066 Hypotheses and its actual-tree/local-seed and retention proof
retain repeated positions/names and q collisions, including replacement terms
containing schematic names. Their ready source coverage is unchanged.

`scripts/backward-zero/audit_archives.py:Syntax/scan` interns native syntax,
reconstructs axioms and MPs, compares all native/image fields, and computes
expanded formula/substitution counts and depths. Its statistics count repeated
children at each occurrence, not just unique pool entries. The step-207 scanner
uses `replay_star.strict_read`, `fast_syntax.py` and `native_parser.cpp`; the full
tag/ordered-child/payload equality resolves collisions. L065 step 207 and
`drafts/2026-10-14-left-closure-star-replay-work.md` already document its complete
validation and the legacy image False/0 and 0.0/0 defect. Reuse this strict path;
ordinary dictionary equality alone is insufficient. This scanner discards its
pool after scanning and does not return the retained package needed here.

`scripts/balanced-coordinate/aggregate.py:load` separately validates, reparses
and retains expanded native tuples and measures expanded image trees. Its
`Combination.copy` and `scripts/backward-zero/build.py:Store.copy/retain`
reconstruct and compare each imported record with reference relocation.
`Closure.__init__` loads all packages before retaining them. Replacing only
load with integer IDs cannot be assumed compatible with these tuple consumers.
The present deliverable must expose an explicit interned package interface;
whole-Closure migration and a low-memory coordinate constructor are outside it.

The compiled parser has an explicit depth-4096 resource rejection; text output
and current substitutions also use recursion/caches. Thus arbitrary mathematical
input depth in L065 is not an all-input execution guarantee for this backend.
For a bounded loader, report/reject unsupported depth honestly, or use iterative
operations; test the declared boundary. Never silently truncate a deep record.
Pools must remain alive for their packages; unrelated pools' integer tags cannot
be compared as formulas without checked translation. Cache lifetime, strings,
Python/C++ duplicate storage, row arrays and checkpoint buffers all count in RSS.

L068 §6, the step-253 work/history, and selected complete `/cap_checks/rss` and
`/preserved` values in `verification.json` were inspected. The reported peak is
4339793920 bytes versus 2147483648, before any coordinate. This is evidence
against that materializing implementation, not impossibility of interning.
No replay, emitter or mathematical calculation was run this literature turn.
Attempt 018's warning against repeated unchanged approval applies: this review
fills a changed representation gap once; the next turn defaults to implementation.

## Acceptance and abandonment test for the next attempt

1. Save a fresh incomplete certificate before production. Preserve all step-253
   files. Independently reconstruct the six expected L066 local endpoints from
   the preserved source/envelope. Validate small fixed-law/package cases first,
   including repeated formulas at different record positions, unused/deep lines,
   names q/A/B/C, and replacement terms containing schematic names.
2. Retain every row in order, exact rule, formula, axiom-substitution key/value,
   references, header/goal and source identity. Share syntax only; never deduplicate
   proof occurrences or substitute semantic equality. Use full structural keys.
   Check native primitives and complete literal images, both actual final records
   and simultaneous EOF. Reject duplicate/extra/missing fields, malformed syntax,
   wrong endpoints, forward/Boolean/float references in either format and changed
   image formula/substitution. Reuse preserved corruptions where applicable.
3. Compare every decoded retained record with the corresponding complete archive
   record, not samples. Round-trip every formula and substitution in both formats;
   record serialization must retain every occurrence. Original byte counts/hashes
   are integrity checks, not substitutes for record equality. Compute exact
   expanded node sums, formula/substitution maxima, full-field depths, payloads,
   line counts and uncompressed bytes, and compare all saved scanner measurements.
   No unique-node or compressed-byte statistic replaces these quantities.
4. On bounded small packages test full retained copying at nonzero offsets and
   simultaneous substitution against the existing tree copier, checking every
   row/field and endpoint. Do not run the old materializing loader on all six
   production pairs as a differential oracle. Hold all six interned packages
   together, and exercise lossless checkpoint/reload with all-record comparison.
   This checks the receiving boundary, not any later zero chain.
5. Instrument peak worker/process-tree RSS during parse/load, retained-copy probes,
   serialization and checkpoint/reload, including native allocations and caches.
   Establish a working self-stop/watchdog before large loading; stage-boundary
   measurements alone are disallowed. Use a conservative 1.5 GiB stop threshold
   with headroom and retain actual peak data; sampling does not prove a hard cap.
   Any observed peak over 2147483648 bytes fails, even if recovered afterward.
   If monitoring/stopping cannot be enforced, stop before production. Inherit
   the prior bounded-attempt ceilings of 600 seconds, 16 GiB new compressed
   artifacts and 128 GiB expanded outputs; no joined export is authorized.

Continue only on complete exact reception/round-trip/statistics evidence within
all caps. A missing field/reference, incorrect statistic, pool-lifetime mismatch,
unmonitored large operation, unsupported required depth or resource breach leaves
the target incomplete and requires preserving its exact failure boundary. Do not
regenerate the fixture, resume blind generation or retry with a higher cap.
A successful loader would still leave the tuple-consuming closure copier,
coordinate/output-size feasibility, indexed chain/bridge composition and combined
original-source accounting unverified. No all-size memory theorem is claimed.
