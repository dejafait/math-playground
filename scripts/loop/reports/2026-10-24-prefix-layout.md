# Stable-prefix layout: controlled offline probe

After the separate overview compaction, this change reorders existing startup
material without shortening or summarizing any supplied file. Shared policy and
static routing instructions precede notebook identity. Local GOAL/PROOF/DAG
precede PROGRESS and its assessment. Dynamic gate/balance/recovery instructions
and the observed current model/effort follow the snapshots.

The exact gate, checkpoint and selected route still control work; no model,
effort, scheduling, authentication, retry or quota rule changed. The post-turn
validator still compares against the original checkpoint and assessment. The
optional-assessment byte limit and containment/symlink checks remain in place.

Probe: for each current notebook, compare two copies of its literal notebook
context differing only by inserting ` changed-` after `STEP_ID:`. Compare the
original context function's GOAL/PROGRESS/PROOF/DAG ordering with the new
GOAL/PROOF/DAG/PROGRESS ordering, using the same now-compact files, snapshot
headers/digests and absent optional assessment. Count identical leading UTF-8
bytes before the first mismatch. Do not edit the actual checkpoint.

| Notebook | Old identical notebook prefix (bytes) | New prefix (bytes) |
| --- | ---: | ---: |
| Riemann | 2,265 | 14,786 |
| P versus NP | 795 | 5,853 |
| Hodge | 854 | 7,182 |
| BSD | 895 | 6,480 |
| Yang–Mills | 881 | 14,320 |
| Beal | 861 | 6,395 |
| Collatz | 814 | 6,474 |
| IUT challenge | 953 | 5,940 |
| RS MCA | 1,231 | 7,311 |
| RS list decoding | 1,101 | 7,305 |

The median increases from 888 to 6,831 bytes for this controlled change.
Unchanged shared policy, static routing, notebook identity, tools and CLI context
are not counted in these notebook-only figures. A changed PROOF or DAG can
still shorten the prefix, as can earlier changes to policy or hidden CLI input.
Different models/settings, cache lifetime and routing can also prevent reuse.
These byte counts are neither tokens nor observed cache hits, and the probe
does not establish savings in the subscription allowance or mathematical quality.

Regression checks verify full verbatim snapshot retention, checkpoint ordering,
stability when an assessment changes, one copy of the routing instructions,
gate placement and preservation of the explicitly selected model/effort. The
entire offline supervisor suite passes with fake processes; no inference or
paid before/after experiment was run. Compare real first-request fresh input,
total fresh input/output, elapsed time and later proof review after restart.
