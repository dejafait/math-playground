# Pool-aware full-record copying — completed scope comparison

TARGET: Implement and completely validate a pool-aware full-record copier from the six preserved step-253 interned packages into one fresh append-only store within the existing resource caps.
CHECKED: 2026-10-16
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused step-254 hash-consing/JSON discovery and fixed-calculus coverage; searched the named local copying/substitution implementations, L056/L065/L066/L068 and step-253/255 failure/result records; reinspected the primary ML 2006 paper §§1–2.3, PDF pp.1–4. No full cap-bounded multi-package copier match was established.
SOURCE_EVIDENCE: Filliâtre–Conchon, Type-Safe Modular Hash-Consing, ML 2006, §2.1 equation (1), §2.2 constructors and §2.3 equality-based lookup/lifetime; L056 primitive basis and all-size copying proof; L065 Hypotheses and step-207 strict reception; L066 exact local endpoints; L068 §7 standalone reception. Existing JSON coverage is unchanged.
COMPARISON: Known structural interning plus unchanged simultaneous substitution and append-only relocation cover the operations; current interned substitution and its differential probe use one pool, whereas the target requires six unrelated source pools and one destination. No cited source supplies this concrete implementation or its resource guarantee.
GAP: Implement source-to-destination structural translation, environment-scoped substitution, occurrence-preserving record append, exact provenance/checkpoint reception and complete production validation within caps; implementation success is unverified.
REASON: Essential source comparison is complete for the unchanged bounded target; specialize known operations and test the changed receiving interface, without a new mathematical theorem or reproof.
SCOPE: Exactly TARGET on the six unchanged step-253 local native/not-or pairs and their step-255 interned representation; full copying, bounded substitution discriminators and checkpoint/reload only; no Closure integration, coordinate generation, joined export or fixture regeneration.
LITERATURE_REASON: Separate required review of the changed cross-pool consumer contract after successful standalone reception; prior coverage did not approve production full-record copying into a fresh pool.

## Relevance and decision boundary

The main gap remains unrestricted SAT decision/separation. This intermediate
implementation could make L066 local packages usable by a later pool-aware
L065 receiver. It supplies neither coordinates nor the complete receiver,
ordinary-input completeness, certificate existence, ER representation, W/V/U
or a SAT consequence. No new lemma or mathematical script is produced here.

Continue to one bounded reproduction attempt if all requirements below can
be instrumented. Continue beyond that attempt only on complete passing
evidence. Any mismatch, lost occurrence, stale-cache result, unsupported
required depth, monitoring failure or cap breach leaves the target incomplete;
preserve its exact boundary and park that implementation without raising caps.

## Sources actually inspected and reused

Primary source: [Filliâtre and Conchon, Type-Safe Modular Hash-Consing,
ML 2006 author PDF](https://usr.lmf.cnrs.fr/~jcf/publis/hash-consing2.pdf),
§§1–2.3, PDF pp.1–4, reinspected 2026-10-16. Section 1 requires systematic
smart-constructor use. Section 2.1 equation (1) explicitly conditions tag-based
equality on use of a single table. Section 2.2 constructs terms through that
table. Section 2.3 compares full equality in bucket lookup, and discusses
weak references/lifetime. These support structural sharing, not comparison of
unrelated integer tags, semantic simplification or a Python/C++ RSS theorem.
No full copier theorem is imported from the paper. The local adaptation must
be tested; a new mathematical reproof is unnecessary.

Reuse `drafts/literature/2026-10-16-interned-native-package-loader.md` for its
recorded discovery queries, primary Python 3.11.17 JSON decoder/duplicate-name
sections and strict parser comparison. No changed JSON hypothesis requires a
new search. L056's precise ax-1/2/3 and MP citations and uniform substitution
coverage remain applicable to literal trees and their literal images. No
additional Frege/PIT or algebraic simulation theorem is needed for copying.
Mathlib full-result coverage is not checked; this is a concrete programming
interface rather than a newly stated mathematical theorem.

## Local comparison, duplicates and failures

Inspected `scripts/balanced-slot/compiler.py:sub,Proof.add,ax,mp`,
`balanced-coordinate/aggregate.py:AppendProof,Combination.copy`,
`backward-zero/build.py:Store.copy,retain` (all under `scripts/`).
The recursive tree substitution returns a replacement without substituting
inside it. AppendProof overrides the base formula-deduplicating add method;
full occurrence retention requires that append-only behavior. Store.retain
compares every imported field and relocates references, including unused rows.
These are reusable contracts, not evidence that a new implementation passes.

Inspected `scripts/output-zero/interned_255.py:Syntax,Package,check_row,small_tests`
and `scripts/left-closure/fast_syntax.py` pool construction/cache methods.
Syntax.substitute reads and constructs in one Syntax and its memo is indexed
by source node ID. Its five-row differential test substitutes in that same
pool. Package.record also interprets IDs through Package.syntax. Neither can
be used unchanged as a cross-pool identity operation. Fresh-pool translation
must preserve ordered constructors and payloads; no bare source ID may be
accepted as a destination ID. Caches must distinguish live source pool,
destination and substitution environment, or have one-call lifetimes. Test
repeated calls with different environments and deliberately conflicting IDs.
Replacement roots belong to the destination and must not be recursively
resubstituted. Pool ownership and cache release must be explicit, with C++
and Python allocations both included in monitored RSS.

L065's complete-record/deep-input hypotheses and L066's exact occurrence/
letter-position endpoints are unchanged. Reuse step-255 reconstructed endpoints
and full reception evidence, not a new assumption of coordinate correctness.
L068 §7 and the complete selected verification-final.json values establish the
prior boundary: six counts 37000,16288,28654,16288,28654,28704; 155588 records
per format; native/image expanded bytes 256056258/376605480; monitored peak
346079232/2147483648 bytes. This turn inspected the saved measurements and
code; it did not rerun archive verification. Prior corruption checks are reused.

The recorded step-253 recursive-materialization peak 4339793920 bytes exceeded
2147483648 before coordinates. That implementation stays parked. Step 255's
failed ps preflight and successful replacement heartbeat watchdog remain
preserved. The bounded loader result neither removes the parser depth-4096
limit nor certifies cross-pool copying, Closure compatibility or later output
feasibility. No duplicate production copier was found in the named paths.

## Required validation for the approved attempt

Save an incomplete certificate before production; use fresh artifact names.
Translate all six packages into one fresh live pool/store with a valid prefix
so every package starts at a nonzero offset. Retain each row, duplicate and
unused occurrence, rule, ordered reference, substitution key/value, declared
goal and exact source path/local-row/global-row map. Verify every relocated
reference and both actual/declared endpoints. Sharing syntax must never merge
proof rows. Derive expected endpoints from preserved source/envelope inputs.

Under identity substitution compare every copied native/image record against
the complete original archives through EOF, allowing only declared relocation.
Compare exact expanded formula/substitution node sums, depths, payloads and
bytes with the prior statistics, accounting explicitly for prefix/header and
reference-digit changes; do not require unchanged serialized byte counts after
relocation. Checkpoint/reload the joined store and source-location map with
complete field comparisons and primitive replay, not just hashes or samples.

On bounded cases compare every field against the append-only tree copier under
q/A/B/C simultaneous substitutions containing those schematic names. Deliberately
change pool construction order, collide bare IDs, repeat identical rows, retain
unused deep rows, use nonzero offsets, and repeat environments to test memo
isolation. Reject wrong-pool operands or require explicit translation; document
the contract. Reuse strict malformed-field/reference/literal-image tests and
include invalid relocation/provenance/checkpoint discriminators. Do not run the
materializing loader on all six production packages as an oracle.

Reuse the tested fail-closed heartbeat watchdog, including preflight, with
1.5 GiB conservative stop threshold, 2 GiB RSS ceiling, 600 s elapsed ceiling,
16 GiB new artifacts and 128 GiB expanded output. Cover parse/translation,
substitution, serialization and reload, counting all live pools, row arrays,
caches and buffers; sampling is not a continuous hard-cap theorem. No full
joined proof export is required: complete record streaming comparisons and a
lossless internal checkpoint can certify this copying boundary. Retain parser
4096/4097 qualification. Report actual/required values and every failure.

This separate review approves the saved target for a later REPRODUCTION
attempt. It proves no new result and does not claim implementation completion
or progress beyond the checked sources. PROOF.md, DAG.md, lemmas and scripts
remain unchanged this turn.
