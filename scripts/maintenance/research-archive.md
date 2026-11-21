# Final research workspace snapshot — 22 November 2026

## 1. Why the autonomous run was stopped

On 20 November 2026 Levent Alpöge announced a proof of the Riemann hypothesis developed with Claude. The [joint statement by the Lean and Mathlib communities](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/), dated 21 November 2026 and endorsed by the Lean FRO and Mathlib Initiative, certifies both the mathematical statement and the formal proof. It reports statement comparisons against Mathlib and checks of the inert proof export by multiple kernels. [Andrew Sutherland's MIT verification record](https://math.mit.edu/~drew/grh/) provides detailed results and logs; its timestamp can precede the community statement, and it distinguishes completed checks from still-running additional checks.

This is an external result. Our local `IN_PROGRESS` notebooks do not constitute a proof of RH, and were preserved without relabeling their unresolved gaps. Prize administration and a conventional exposition are distinct from the formal checks reported above. The author of this snapshot has read the primary verification reports, not independently rerun the full external proof.

## 2. What is preserved

The versioned [snapshot manifest](research-snapshot-manifest.json) records every archived file's exact byte count and SHA-256 (or a symlink's target), every archive part's SHA-256, the Git base commit, exclusions and the release tag. Ordinary Git contains the notebook changes, reviews, audits, mathematical programs and new evidence files up to 1 MiB. Larger files remain preserved without regeneration inside the tagged snapshot, rather than becoming enormous Git blobs.

The tar archive additionally preserves the complete research workspace, including ignored runtime logs, expanded certificates and `.history-backups/`. Its `.archive-history.bundle` contains all current Git references. That bundle also lets the current history be recovered without depending on a live Git hosting account. The older pre-rewrite bundle is retained separately in `.history-backups/` within the snapshot. Empty directories and disposable file-system metadata are not research evidence.

The manifest lists exclusions explicitly: live `.git/` internals (replaced by the verified Git bundle), `.generated/` output (including the archive itself), credentials/local environment configuration, Python bytecode, workstation metadata, dependencies and build caches. No mathematical evidence is excluded merely because it is large or reproducible. The manifest itself and this closure commit are kept in Git and also uploaded alongside the archive parts; the tar snapshot was taken before that final inventory commit.

## 3. Where to find the backup

Release: <https://github.com/dejafait/math-playground/releases/tag/research-snapshot-2026-11-22>

Each `research.tar.gz.part-NNNN` is at most 1 GiB. Concatenating parts in numeric filename order produces one gzip-compressed tar. The release also contains `research-snapshot-manifest.json`. GitHub's automatically generated source ZIP does **not** include the attached archive parts; use the release assets explicitly.

Publication is performed in two steps: upload to a draft release, then download each asset from GitHub and check its SHA-256 against the versioned manifest. Only after all readbacks match is the release made public. Preparation and upload alone are not confirmation of a complete remote backup.

## 4. Restore on another machine

Download all assets from the release into an empty download directory. With GitHub CLI, from that directory:

```bash
gh release download research-snapshot-2026-11-22 \
  --repo dejafait/math-playground
```

Verify the manifest against the copy tracked in Git, and verify every part's SHA-256 and byte count listed in it before extracting. Do not treat an incomplete download or the source ZIP as a full backup. Create an empty destination, then concatenate and extract:

```bash
mkdir restored-workspace
cat research.tar.gz.part-* | gzip -dc | tar -xf - -C restored-workspace
```

The extracted files are the original workspace bytes, not recomputed numerical output. Recover a separate full Git checkout from the embedded bundle:

```bash
git clone restored-workspace/.archive-history.bundle restored-history
```

The final closure/inventory commit can also be retrieved from the GitHub repository. The tar contains notebook files already; the separate history clone is useful for inspecting commits. Reinstall dependencies if execution is desired. Research does not resume automatically.

## 5. Reusable maintenance commands

`make math-stop` stops only this repository's supervisor using its existing graceful SIGINT handling. `make math-plan-progress` inventories the compact mathematical files; `make math-save-progress` commits that explicit list. Infrastructure is committed separately with `make math-save-diagnostics`.

`make math-archive` holds both loop locks, creates and verifies a Git bundle, streams an exact tar/gzip snapshot into bounded parts, and writes the manifest. `make math-archive-check` reads the complete archive and verifies every file and the gzip trailer. `make math-save-archive` records the closure documentation and inventory. `make math-push` must succeed before `make math-archive-upload`; the upload command checks that local and remote `main` agree. `make math-archive-remote-check` downloads every asset, verifies hashes and then publishes the release. None of these targets deletes the original research folder.
