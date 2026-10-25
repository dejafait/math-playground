# Overnight review: October 24–25, 2026

Read-only runtime snapshot taken around 10:02 UTC October 25. Window: completed
invocations starting at or after 20:13 UTC October 24, through 09:57 UTC October
25. Sources: local per-notebook `routing.jsonl` and `requests.jsonl`, current
checkpoints and canonical evidence references. Runtime logs are not copied into
Git. The running invocation is excluded. No runtime configuration was changed.

## Activity and validation

188 completed invocations, all with accounting; 18–19 per notebook. Supervisor
accepted 176 (93.6%): 80 ADVANCE, 65 EXPLORATION, 20 NEGATIVE, 11 STALLED.
These are checkpoint classifications, not independently established novel
theorems. ADVANCE includes source readiness and audits. All ten notebooks remain
IN_PROGRESS; no complete candidate was established. All ten pass the current
structure/link/DAG/overview checks. Active-invocation elapsed times sum to
13.21 hours within the approximately 13.72-hour window.

Representative recorded results and qualifications:

| Notebook | Recorded overnight work |
| --- | --- |
| Riemann | Conditional logarithmic upper-tail import L463 audited; C463a range intersection leaves the leading threshold obstruction; L260 finite masking certificate audited. Initial signs/global positivity remain open. |
| P versus NP | L097 finite integration independently audited (529 events); new opposing-units endpoint has 212 records, audit pending. Uniform worst-case problem remains open. |
| Hodge | Conditional trace/operator and section-pairing results L161–L164; a mixed-cup route fails. Actual bundle existence and primitive realization remain open. |
| BSD | Four further kernel certificates (39–42) audited; L116 gives a conditional 42-kernel error composition. Actual signed assembly and zero exclusion remain open. |
| Yang–Mills | Fixed-mesh coefficient assemblies and exact reflected coefficient L279; latter audit pending. Uniform mesh/continuum/mass-gap obligations remain open. |
| Beal | Several shortcut routes excluded; L134 certifies a quartic integral basis and discriminant 2,874,960 with 967 replay checks, dedicated critical audit pending. Rank/point control remains open. |
| Collatz | Audited restricted d35 allocation exclusion C103a; C103b transfers it conditionally to actual words, audit pending. Row-zero support, language exhaustion and universal descent remain open. |
| IUT challenge | Pointed-model L115 audited; L116 identifies a conditional pole-cost budget obstruction. Averaging route under review; full challenge obligations remain open. |
| RS MCA | Audited incidence/disjoint-pair extraction; L153 census covers 79,380 pairs, uniformly rank 12. Uniform compatibility/exterior bridge remains open. |
| RS list decoding | L124 survivor bound 1,597,620,964,591 audited; proposed 1,532,495 local cap refuted by existing 2,571,353-block families. Cross-core compatibility remains open. |

## Optimization measurements

Baseline: invocations starting in the preceding 24 hours, ending before the
restart cutoff (290 attempts, 288 accounted). This is an observational
comparison with changed tasks/model mix, not a randomized A/B experiment.

| Metric | Before restart | Overnight |
| --- | ---: | ---: |
| Median initial prompt bytes | 169,862 | 44,478.5 |
| Median first-request input tokens | 50,024.5 | 25,189.5 |
| Median first-request uncached input tokens | 37,759 | 12,887 |
| First-request cached-input share, weighted by input | 22.85% | 48.04% |
| Median uncached input tokens per invocation | 82,918.5 | 54,109.5 |
| Aggregate cached-input share | 91.79% | 92.55% |
| Median invocation seconds | 230.07 | 225.23 |

Startup bytes fell 73.8%, first-request uncached input 65.9%, and median
invocation uncached input 34.7%. First requests were identified by request_index
zero and joined by thread ID, covering all accounted samples. Total overnight
input was 151,507,056 tokens, including 140,219,392 cached and 11,287,664 fresh;
output was 2,015,344 tokens. These input totals count repeated context across
model requests, not unique notebook content.

Within Sol/high alone (110 baseline, 78 overnight), first-request fresh median
fell from 37,450.5 to 13,014.5 and invocation fresh median from 97,606 to 71,159.
Model mix therefore does not explain the whole improvement, but task mix and
other context changes still confound causal estimates. Runtime did not show a
large overall improvement; Sol/high median rose from 305.33 to 314.93 seconds.

This supports retaining the combined overview compaction and stable prefix
ordering. It does not isolate the incremental effect of reordering from smaller
context, measure the exact server cache boundary/lifetime, establish subscription
allowance savings, or demonstrate improved mathematical correctness. A high
aggregate cache share alone is insufficient evidence because it also reflects
within-invocation reuse. No paid controlled experiment was run.

All current PROOF.md files remain 3,163–4,943 bytes and PROGRESS.md files
2,268–3,123 bytes, below the 8,192-byte caps. Overviews have grown since initial
compaction but remain bounded. No compaction-induced loss is established by
structural checks; proof correctness needs the separate mathematical audits.

## Quota observations and remaining waste

Records report plan_type=pro overnight, versus prolite in the baseline. They
report one non-null primary window, 10,080 minutes (seven days). Usage rose from
0% to 15%, then fell to 0% around 06:08 UTC October 25 with a reset timestamp
change; latest snapshot is 5%. The cause of that discontinuity is not exposed.
Therefore the latest 5% cannot be described as total overnight consumption,
and adding segments is only an approximate 20 percentage points across changed
counters, not a stable-denominator billing measurement. No projection of spare
weekly allowance is justified by that single current reading.

Twelve invocations were rejected: eight missing a direct source URL, one
literature-only turn editing mathematical files, and three exploration/stall
gates. IUT currently has queued recovery for a missing source URL. Repairs
elsewhere allowed scheduling to continue. No history-rewrite failure was found.

95/188 invocations were classified as literature comparisons. Model/effort mix:
39 Astra/high, 78 Sol/high, 71 Sol/medium; no low-effort invocation in this window.
There is further opportunity to reduce repeated source-scope approval and
metadata failures while retaining explicit mathematical audit obligations.
Any gate or routing change needs its own implementation/review; this report
does not alter the running loop or certify that source-review turns were useless.
