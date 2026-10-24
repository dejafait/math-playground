# Subscription loop, Cloudflare AI Gateway and caching

Reviewed October 24, 2026. This is an operational assessment, not a mathematical research turn. No authentication, model routing, scheduling, prompt construction or notebook proof content was changed by this review. Existing notebook work was committed separately as `Add progress on all 10 open problems`.

## Recommendation

Keep the current ChatGPT-authenticated Codex loop. Cloudflare AI Gateway becomes useful if the project deliberately adds separately billed provider APIs or several providers; it is not a way to route the existing subscription allowance through a cheaper API. Improve startup size and avoidable process failures before introducing another network service. Do not globally downgrade mathematical reasoning just to increase turn count.

The launcher in `../codex.py` explicitly requires ChatGPT sign-in and rejects provider API keys, custom base URLs and custom model-provider configuration. Each invocation is a fresh session in one notebook. The round-robin distributes turns, not tokens, money or theorem-solving probability. Ten independent notebooks do not imply concurrent model calls.

## What we already implemented

- Round-robin scheduling across ten independent Markdown notebooks, with one canonical lemma DAG per notebook, compact checkpoint conventions and persistent retry/recovery state.
- Subscription-only authentication, account-wide quota cooldowns, transport backoff, invocation timeouts and process/workspace locks.
- Reusable literature assessments tied to exact targets, explicit import/reproduction classifications, stopping rules and changed-direction recovery rather than endless repetition.
- Explicit model/effort routing, mechanical-task and deep-research roles, bounded Astra/max shares, availability checks and fallback reporting. Current defaults are medium for comparison and high for ready calculations; they are not generally low.
- Passive per-request/per-turn accounting, cached/fresh input, output/reasoning subsets, observed settings, tool-output sizes, compactions and heuristic read-scope signals. The collector makes no model calls.
- Active-notebook scope, selective certificate inspection, shared instructions before variable content, and one verbatim startup copy instead of repeated orientation reads.
- Deferred approval of changed continuation coverage, preserving completed mathematics instead of rejecting it for its next proposed direction; the RH external-result update prevents rediscovery of the screened fixed-half-plane results.

These are documented in `../README.md` and commits `b69f4221`, `4a892b2d`, `c1a88c73`, `117a5d25`, `162f94f0`, `60babfa2`, `6b601f4f`, `9be17ec8`. They are mechanisms and safeguards; their existence is not evidence of a quantified increase in the probability of solving a prize problem.

## Observations from local logs

Snapshot window: invocation `started_at` from October 22 00:00 UTC through October 24 17:44:13 UTC. There were 645 recorded invocations: 626 complete accounting observations, 17 partial and two without accounting. The totals below exclude the 19 incomplete/unavailable observations. The [sanitized snapshot](2026-10-24-usage-snapshot.json) contains aggregate counts only, not session IDs, prompts, arguments, quota/account records or proof passages.

| Measure | Observation |
| --- | ---: |
| Model requests within the 626 accounted invocations | 7,324 |
| Total input tokens, including cached input | 627,438,147 |
| Cached input tokens | 573,391,744 |
| Fresh input tokens | 54,046,403 |
| Cached share of input | 91.39% |
| Output tokens, including reported reasoning | 6,261,997 |
| Reasoning tokens already within output | 1,187,884 |
| First-request fresh input across matching 626 sessions | 25,669,122 |
| First-request share of all fresh input | 47.49% |
| Median literal initial prompt size | 166,467.5 bytes |
| Tool outputs reported by the collector | 86,083,405 bytes |

Token totals sum repeated input across model requests; 627 million is not 627 million unique tokens or an API invoice. Cached input is not added to input again. Reasoning is not added to output again. Collection status is a parser-completeness observation, not a guarantee that every provider billing field was exposed. First requests were matched by thread ID in the local logs and deduplicated by thread/response/request index; no IDs are published.

The complete sample used Sol for 476 turns, Astra for 149 and Luna for one. Observed effort was high for 396 turns and medium for 230; no low, xhigh or max was recorded in this sample. Thus the assumption that most work already runs at low effort does not match these observations. Requested defaults, model fallback, task mix and accepted recommendations need separate investigation before blaming the router.

The 645 invocations contain 588 accepted reports. Thirty-one validation messages concern a missing direct source URL (22) or a target/assessment mismatch (nine). Other messages include research stopping rules, literature stalls and unaccepted invocations. Acceptance validates reporting/process conditions, not mathematical correctness. Likewise ADVANCE labels include known-source imports and reproductions, not necessarily progress beyond established mathematics.

Literal PROOF.md sizes at review time ranged from 122,010 to 260,045 bytes despite a 100-line compactness convention. The rule admits enormous single-line paragraphs. The whole initial prompt already embeds that file, then tools often return more content. There were 1,188 heuristic PROOF.md read mentions across the sample, but these can include legitimate changed-passage checks; they are not 1,188 proven redundant complete reads.

## Cost distribution: illustrative weights, not subscription charges

The [official Codex Standard credit rate card](https://learn.chatgpt.com/docs/pricing#token-rates), inspected October 24, lists the following rates per million fresh input / cached input / output tokens: Sol 50 / 2.5 / 250; Astra 250 / 25 / 1,250; Luna 2.5 / 0.25 / 12.5. Codex credit billing has no separate cache-write charge. These rates are used only to construct a relative sensitivity proxy, not to price the included Pro allowance, infer euros, or estimate remaining tasks. Service speed and the actual subscription allowance calculation are not established by these logs.

For each model compute `(input-cached)*fresh_rate + cached*cached_rate + output*output_rate`, divided by one million. Weight the actual observed models separately before aggregating. This yields relative category weights of fresh input 39.76%, cached input 35.44% and output 24.80%. Astra represents about 68.07% of this proxy despite 23.80% of complete turns; Sol about 31.93%; Luna below 0.01%. These figures do not establish the true included-allowance cost share or that Astra's harder tasks would work on Sol.

The accompanying [interactive sensitivity view](2026-10-24-cache-sensitivity.html) starts at the observations. Its slider hypothetically moves a proportion of existing fresh input to cache at the same model's cached-input rate, holding total input, output and model mix fixed. It does not claim that this cache improvement is achievable or that reducing prompt size has the same effects as recaching tokens. Provider API cache-write prices are not part of this subscription credit-rate proxy.

## Two very different caches

| Mechanism | Reused work | Fit for this project |
| --- | --- | --- |
| Provider prompt cache | Computation for an identical eligible prompt prefix; the model still generates a new answer | Useful for stable instructions and repeated conversation history, with model/settings/lifetime compatibility |
| Cloudflare response cache | The completed provider response for a matching whole request, without another inference | Little expected reuse for changed checkpoints and tool transcripts; an auditor must get a fresh model response rather than a replay of a prior answer |
| Local source/validation cache | Immutable source extracts or deterministic tool results keyed by exact content and relevant tool version | Potentially useful without any gateway; live source freshness and invalidation remain explicit obligations |

Cloudflare's [caching documentation](https://developers.cloudflare.com/ai-gateway/features/caching/) says the default key includes provider, endpoint, model, authentication and the full request body. Its custom key can group different bodies, so never key proof work only by problem name: that could return a response for an obsolete checkpoint. Cached tool-call responses must not be replayed as fresh mutations. An independent proof audit should bypass response caching.

Cloudflare's [overview](https://developers.cloudflare.com/ai-gateway/) and [analytics documentation](https://developers.cloudflare.com/ai-gateway/observability/analytics/) describe a proxy providing request/token/error/cost visibility, response caching, limits and retry/fallback controls. For a production API application with repeated requests and multiple providers, this can centralize controls and observability. It does not certify proof quality or make identical failed mathematics a productive new attempt.

Core analytics, caching and rate limiting are currently free. [Pricing](https://developers.cloudflare.com/ai-gateway/reference/pricing/) also lists log-storage/export conditions and a 5% fee on Unified Billing credit purchases; optional model-based guardrails consume inference. BYOK still incurs provider API charges. A paid API gateway path therefore needs a separately authorized API budget. [OpenAI authentication guidance](https://learn.chatgpt.com/docs/auth) distinguishes API-key billing from included ChatGPT plan usage. No supported subscription-token proxy integration was established by the reviewed documentation; do not repurpose the stored ChatGPT access token as a provider API key.

## Prompt-prefix opportunity and limits

The current `context.py` already puts PROMPT.md and shared GOAL.md first. Within notebook context it orders GOAL, PROGRESS, PROOF, DAG, then the selected literature assessment. The variable gate/balance/recovery instructions precede notebook context in `runner.py`; the static routing instructions follow all notebook content. An early change in PROGRESS or gate instructions can prevent cross-session reuse of later otherwise-identical text. That is a real layout opportunity, not a measured cache improvement.

A candidate layout is stable shared policy and static routing instructions first, then stable local goal and necessary unchanged references, then checkpoint/target, assessment and variable gate/recovery details. Preserve authority, current checkpoint accuracy and all mathematical context required for rigor. Model/tool schemas, CLI-added hidden context, working-directory instructions and model/effort compatibility can still limit cache matches. Different models do not share a reusable model-computation cache simply because their visible text agrees. Do not assume Codex subscription calls expose the Responses API's cache keys, breakpoints or TTL controls.

[OpenAI prompt-cache guidance](https://developers.openai.com/api/docs/guides/prompt-caching) calls for exact reusable prefixes and stable instructions/tool definitions, placing changing material later. The current API offers model-dependent cache controls and read/write prices; these are not documented controls of this project's ChatGPT-authenticated CLI calls. Ten round-robin turns and quota waits may outlast a usable cache entry. Do not change scheduling fairness or keep appending stale history solely to maximize the cache-hit percentage.

## Prioritized follow-up

1. Restore an actually concise PROOF.md overview, preserving detailed arguments and historical narrative in canonical lemmas/attempts/history. Add a byte/word-budget warning so long lines cannot bypass compactness checks. This needs careful mathematical editing and was not performed in this review.
2. Run a bounded before/after prompt-layout experiment: identical content and task/model/effort mix, no removal of proof obligations, measure first-request fresh input, total fresh input, output, elapsed time and reviewed quality. Do not judge it by cache percentage alone. API-only cache settings should not be added to the subscription launcher.
3. Prevent missing-URL/target-mismatch repair turns with better deterministic feedback and template validation; separate those from legitimate new literature review. Do not weaken the source gate to make acceptance rates look better.
4. Compare model/effort by actual task and subsequently audited usefulness. Route mechanical reporting/extraction to the routine role when suitable; retain deep models for hard mathematical reasoning. Avoid another model call just to route a turn.
5. Track reviewed relevant advances and informative negatives per resource unit, rejected-report overhead and repeated stopped routes. Lemma count and self-reported ADVANCE are poor stand-alone quality measures. Nothing here estimates a calibrated theorem-solving probability.
6. Reconsider Cloudflare only when there is a deliberate multi-provider/API plan. Start with observability and a hard paid budget, keep response caching disabled for research and independent audits, and avoid gateway retries duplicating the supervisor's work or silently changing model/effort.

This review does not change the loop or require a restart. All sources describe capabilities as inspected on the review date; prices, auth support and cache policies can change.
