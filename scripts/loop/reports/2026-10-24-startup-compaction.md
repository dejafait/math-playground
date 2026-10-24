# Startup overview compaction

This maintenance change replaces the ten accumulated PROOF.md catalogs with
concise argument/gap/partial-result/trap overviews. Before editing, both loop
locks were free; the edits held the supervisor's workspace lock. No checkpoint,
lemma proof, source qualification, DAG, routing, auth or retry state was changed.

Every original PROOF.md is retained byte-for-byte as
`history/2026-10-24-proof-overview-before-compaction.txt` in its notebook.
The raw text format preserves the original bytes, including historical relative
Markdown destinations, without reinterpreting those links from the new directory.
The source location for those historical links was the notebook root. Canonical
proofs and the current checkpoint remain authoritative; historical audit-status
recaps can be stale and must not override them.

The archive bytes were compared with a Git archive of pre-edit HEAD, not just
with an in-memory intermediate copy. All ten matched exactly. This preserves
historical exposition; it is not a new mathematical verification or permission
to skip a needed canonical hypothesis or proof.

Combined PROOF.md size fell from 1,499,196 to 27,960 UTF-8 bytes, a 98.14%
reduction in that component. Individual overviews are 2,679–2,973 bytes. This is
not a 98% reduction in the full prompt, model tokens, runtime or allowance use.
The full startup still includes shared policy, local goal, checkpoint, DAG,
optional assessment and CLI context. Additional targeted proof reads remain
necessary and may offset part of the initial-context reduction.

The documentation checker now enforces 8,192 UTF-8 bytes for each PROOF.md and
PROGRESS.md in addition to their existing 100/40-line limits. It does not
truncate either file. A failure reports how to preserve detailed evidence in
canonical proofs or tracked history. The global policy tells the loop to revise
the overview's existing paragraphs, not append a growing per-lemma catalog.

Offline maintenance commands are available without model calls:

```bash
make -f scripts/maintenance/Makefile check
```

```bash
make -f scripts/maintenance/Makefile test
```

The new regression cases cover a giant single line, exact byte boundaries,
multibyte UTF-8 text and the independent line limits. All ten current notebooks
pass structural checks. Existing proof-success criteria and literature gates
are unchanged. Fresh-session consumption and downstream reviewed quality must
be measured after resuming the loop; no paid A/B experiment was run here.
