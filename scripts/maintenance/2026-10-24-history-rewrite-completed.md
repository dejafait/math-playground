# History rewrite completed on 2026-10-24

The user authorized rewriting and publishing `main`. The original tip was
`4aa1581c4a1e02c91a783ce583b72991c7e5d577`. An isolated import replayed all
50 original commits into 53 commits. Root commit
`726051bfdbd2519735f0f6c4fd6f4145104e377f` installs the revised ignore policy.
The [commit map](history-rewrite-map.json) records every original commit and
its replacements. Three mixed commits (`cb4ddb7d`, `f7beac40`, `c6c11321`)
were split into feature changes followed by mathematical progress. Existing
ignore changes were reconciled into the root policy.

All 50 corresponding historical snapshots were compared by path, mode and
blob identity: every non-ignore tracked file is unchanged. The replay tip
before new maintenance work is `ceef4136d6cba9fdeef98591b9bbb49568c4c90d`.
Author identities and timestamps were preserved. No existing lemma, DAG,
certificate or mathematical claim was changed by this rewrite.

## Previously missing evidence

A clean checkout exposed broken links to certificates that existed only in
the original working directory under the old ignore rules. A separate commit
now versions 333 certificates, inputs and source bindings, totalling
904,935,760 original bytes and 336,052,431 stored bytes. Fifteen large files
are losslessly compressed, with original and archive SHA-256 identities in
[the manifest](compressed-evidence.json). `make -f scripts/maintenance/Makefile
evidence` restores exact original bytes without regeneration or overwriting
changed files. Structural checks restore missing files automatically, without
rehashing existing large files on every loop iteration.

The [inventory](recovered-evidence-inventory.json) separately lists 559
previously unversioned generated execution streams that remain local. They
were not deleted. Full replay of computations relying on these streams still
requires regeneration or the local streams; structural validation is not a
mathematical certificate audit. This inventory does not claim that every
untracked output in the working directory is a proof certificate.

The tracked tree after evidence recovery is approximately 465 MB, excluding
this small completion record and map. Preserving evidence increases the
published tree; the rewrite is not presented as a storage reduction. The
largest stored blob is 38,875,808 bytes, below GitHub's per-file limit. Actual
Git transfer/storage size depends on packing and remote retention.

## Validation and recovery

All ten notebook structure, link, DAG and overview-budget checks pass.
The offline suite passes 5 restoration, 7 documentation and 84 loop tests.
The imported object database passed `git fsck --full --no-reflogs`.
Original local certificate SHA-256 identities were checked before publication.

Original history is retained locally in
`.history-backups/2026-10-24-before-rewrite/original.bundle`, together with
the original export and detailed mapping. A verified rewritten bundle is
retained alongside it. Neither backup is published. Existing generated files
are preserved; exact paths previously ignored remain excluded locally in
`.git/info/exclude`, without broad JSON exclusions in the shared policy.

Publication uses an exact lease against the original remote tip, so a
concurrent remote update aborts the push. Existing clones must reconcile
their branches with rewritten `origin/main` before continuing work; preserve
any local work first. Local old objects are deliberately not garbage-collected.
