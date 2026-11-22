# Research storage policy — 22 November 2026

## 1. Preserved in GitHub

The code for the loop, routing and optimizations, mathematical programs, notebook text, source reviews, audits and compact evidence are committed and pushed to `main`. Commit `26c02dbc` records the final mathematical progress; `85e360d9` records the maintenance tools; `66572b5c` records the initial archive inventory and the externally verified RH announcement.

Levent Alpöge announced a Claude-assisted proof of RH on 20 November. The [joint statement of the Lean and Mathlib communities](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/), dated 21 November and endorsed by the Lean FRO and Mathlib Initiative, certifies the formal statement and proof after independent checks. [Andrew Sutherland's MIT record](https://math.mit.edu/~drew/grh/) documents the verification. Our notebook retains its original exploratory status; it did not prove RH.

## 2. Deliberately excluded bulky generated results

The owner subsequently chose to preserve code and mathematical reasoning without uploading all generated numerical results. The exact exclusions in [riemann/scripts/.gitignore](../../riemann/scripts/.gitignore) cover 2,415 previously untracked result files totaling 26,030,753,738 bytes. They comprise JSON results, compressed results, NumPy matrices and text outputs, all larger than 1 MiB. No Python source or Markdown mathematical text is excluded by that list. Existing tracked evidence and historical commits are preserved; this policy does not rewrite Git history.

The remaining numerical programs may refer to excluded files. A Git clone preserves the code, not a guarantee that every replay can run immediately: excluded data must be regenerated where possible. Regeneration may require substantial computation, original input sources or dependencies. The exact old result bytes will be lost if the entire local folder is deleted without another backup. This is the owner's chosen tradeoff.

## 3. The complete archive is LOCAL ONLY

Before this policy change, a complete workspace archive was prepared locally and read back successfully. Its 18,914 files occupy 29,389,453,341 original bytes; its 21 compressed parts total 21,814,417,847 bytes. Every file hash was verified, and the live research workspace matched the inventory at preparation time.

**The GitHub release upload was cancelled before publication. There are no release assets to download.** The archive parts remain under `.generated/research-archives/research-snapshot-2026-11-22/` inside this local project folder. Deleting the folder also deletes that local archive. The [versioned manifest](research-snapshot-manifest.json) records hashes and filenames; it does not contain the underlying data and cannot restore it by itself.

If exact results are ever worth retaining, copy the local archive parts and its manifest to separate storage before deleting the folder. This is optional under the new policy; GitHub does not contain a complete numerical workspace backup. No files were deleted during this policy update, and no large-result release upload will be resumed automatically.

## 4. Reusable commands

`make math-plan-progress` selects mathematical files of at most 1 MiB for a reviewed progress commit. Exact ignored large paths do not enter that plan. `make math-save-progress` commits the plan; `make math-push` sends existing commits. Existing tracked large archives remain in history.

`make math-archive` and `make math-archive-check` are optional local full-backup tools. Their upload targets require a separate deliberate invocation; they are not dependencies of commit, push, tests or the research loop. They were not run successfully for remote publication in this session. `make math-save-storage-policy` records this policy independently from mathematical progress. The loop is stopped.
