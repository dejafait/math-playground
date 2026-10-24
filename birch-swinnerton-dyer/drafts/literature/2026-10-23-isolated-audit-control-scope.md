# Function-scoped audit controls: primary-source review

TARGET: Review the Python scope and metadata contract for function-scoped signed controls and an immutable kernel index in a fresh L105 audit, reusing step-419's static collision evidence without executing kernels.
CHECKED: 2026-10-23
DECISION: IMPORT
SEARCH_EVIDENCE: Targeted histories 418/419, named local audit assessments, complete retained worker/control sources, ATTEMPTS/047 and static diagnosis; no completed corrected audit found in those paths. Reused unchanged ready analytical discovery.
SOURCE_EVIDENCE: Inspected official Python 3.15.1 execution model sections 4.2.1–2 and 4.2.6, complete exec namespace cases and simple-statements sections 7.12–13; precise URLs, source comparison and finite preflight contract in drafts/source-notes/2026-10-23-isolated-audit-control-scope.md.
COMPARISON: Standard scope semantics explain the recorded module-level binding collision and support an explicit lexical installer; separate exec mappings and implicit function locals do not supply that contract. This imports known language behavior, not new mathematics or program verification.
GAP: Future implementation, identity preflight and full arithmetic audit remain unexecuted; no complete L105 audit PASS or runtime guarantee follows.
REASON: The essential previously unread namespace cases are now covered; the changed interface has a finite independently checkable preflight and explicit first-failure test.
LITERATURE_REASON: Step 419 exposed worker/control binding behavior absent from prior coverage; unchanged analytical coverage was reused.

Full applicability, qualifications, essential inputs, allowed mutations and
continuation/abandonment tests are in the source note. No lemma, mathematical
script, control execution or kernel execution was performed. Step 419 remains
stopped; this review does not repair or resume its evidence.
