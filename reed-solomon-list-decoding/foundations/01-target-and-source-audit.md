# Target and source audit

Access date: 2026-09-24. This is a **partial source freeze**, not a completed audit of the companion paper's definitions.

Follow-up on 2026-09-25: the [pinned list model](02-pinned-list-model.md) supplies
readable, commit-specific ArkLib conventions and preserves the unresolved
comparison with ABF26. The access limitations below describe this initial audit.

## Primary statement and version

The [Proximity Prize challenge page](https://proximityprize.org/) specifies an RS code over a finite field F, on a smooth evaluation domain L contained in F. Write q = |F|, n = |L|, and R = k/n. The designated rates are 1/2, 1/4, 1/8, and 1/16. For a given epsilon* (example: 2^-128) and a constant interleaving order m, the requested radius is the largest delta in [0,1] satisfying

\[
 |\Lambda(C^{\equiv m},\delta)|\leq\varepsilon^*q.
\]

The page assumes the field is large enough for an admissible radius to exist. It supplies no explicit growth law relating q to n, and does not restrict F to prime fields. The bound uses q, not the interleaved alphabet size q^m. A field-size condition sufficient for a particular bound must therefore be stated, rather than inferred from the phrase about existence.

The companion is Gal Arnon, Dan Boneh, and Giacomo Fenzi, [Open Problems in List Decoding and Correlated Agreement, ePrint 2026/680](https://eprint.iacr.org/2026/680). Its metadata records receipt on 2026-04-07 and a latest revision on 2026-07-06, with three revisions. The current PDF returned HTTP 403 and the version archive was inaccessible through the web reader. Local HTTP retrieval failed at DNS resolution. No PDF snapshot, exact revision URL, or hash was obtained.

In particular, the companion's precise definition of smooth domains, list boundary convention, and any additional concrete field instances have **not been checked**. No definition number is being guessed. The website statement above is frozen as read; the local GOAL.md requirement to audit the full source remains incomplete.

## Explicit provisional notation

For comparing sources only, use

\[
 C=\{(f(x))_{x\in L}: f\in F[X],\ \deg f<k\}.
\]

An interleaved codeword is an m-tuple of codewords, regarded as a length-n word over F^m. For arrays Y and P, set

\[
 d_{\rm col}(Y,P)=\frac{1}{n}|\{x\in L:Y(x)\ne P(x)\}|,
 \qquad B_m(C,\delta)=\max_Y|\{P\in C^{\equiv m}:d_{\rm col}(Y,P)\leq\delta\}|.
\]

Thus a column agrees only when every row agrees there. This follows the convention in [TR26-169, Section 8.2](https://eccc.weizmann.ac.il/report/2026/169/download#page=31); it has not been cross-checked against the unavailable ABF text. The closed-ball convention and the distinction between a real-radius maximum, supremum, and integer-error threshold must remain explicit. None is silently substituted for the challenge's wording.

## Current bounds located, with qualifications

Brakensiek, Chen, Putterman, Zhang, and Zheng, [ECCC TR26-164, revision 1, 2026-09-05](https://eccc.weizmann.ac.il/report/2026/164/), **Corollary 5.1**, printed pp. 22–23, states: for fixed R and slack gamma, some C permits decoding on arbitrary distinct evaluation points over prime F_q when q >= Cn and k/n <= R, at agreement at least (R+gamma)n, with list size q^{O_{R,gamma}(1)}. See the [formal statement and proof](https://eccc.weizmann.ac.il/report/2026/164/revision/1/download#page=22). Its informal **Corollary 1.2**, printed p. 3, instead writes n^{O_{R,gamma}(1)}. The audited proof ends with the q-dependent bound; it does not justify replacing q by n when q/n is unrestricted. This is a limitation of the proposed transfer, not a disproof of the paper's decoding result.

Fernando Granha Jeronimo, [ECCC TR26-169, 2026-09-05](https://eccc.weizmann.ac.il/report/2026/169/), **Theorem 1.1** and **Corollary 8.2**, separately claim, for fixed gamma > 0, sufficiently large n, prime q >= n, and k <= (1-gamma)n,

\[
 B_m(C,1-k/n-\gamma)\leq n^{mC_{\rm list}(\gamma,1)}.
\]

This would meet the list threshold if q >= n^{mC_list(gamma,1)}/epsilon*. This comparison is conditional on that preprint's theorem; its geometric cover construction has not been verified here. **Sections 8.3–8.5** explicitly leave the largest safe radius and concrete constants unresolved. Section 8.4 additionally claims a large-characteristic extension with p > max{k-1,B_{gamma,1}}, which still does not cover all finite fields. See [theorem](https://eccc.weizmann.ac.il/report/2026/169/download#page=3) and [scope discussion](https://eccc.weizmann.ac.il/report/2026/169/download#page=31).

Review qualification, 2026-09-25: the [component-cover audit](../drafts/2026-09-25-component-cover-audit.md) checks the singleton-list support-isolation and counting passage in Lemma 6.2 and Theorem 6.3. It does not establish the cover required by Corollary 6.1 or the full list-size theorem.

Further local review, 2026-09-25: the [lifted-jet audit](../drafts/2026-09-25-lifted-jet-degree-audit.md) checks the recurrence in Lemmas 5.6–5.7 and proves linear, rather than quadratic, numerator and residual degree bounds in L003. The result is restricted to a nonsingular Taylor chart. Graph-closure degree control, singular branches, and the complete cover remain unverified. The prize page was rechecked on this date; the frozen base-field threshold and existence proviso remain unchanged.

Subsequent review, 2026-09-25: the [open-graph audit](../drafts/2026-09-25-open-jet-graph-degree.md) checks the local intersection/graph passage in Lemmas 5.3–5.4 and the nonsingular construction on printed p. 25. L004 now gives explicit cumulative-degree bounds for one chart closure, including a separately constructed fixed-parameter chart. The preceding graph-closure gap is removed for these charts; singular coverage and the full theorem remain unverified. The prize statement was rechecked and the source qualifications are unchanged.

Fixed scalar cover review, 2026-09-25: the [singular-cover audit](../drafts/2026-09-25-singular-solution-cover.md) completes the scalar coverage step with L005, using a finite chain of highest-variable partials and anchors over the algebraic closure. Its explicit bound includes singular solutions under characteristic zero or p>max(d,B). This removes the preceding scalar cover qualification, but does not establish the parametric theorem, the fixed-slack interpolation input, or the full list-decoding theorem. The prize statement was rechecked; its field-existence proviso and the unresolved ABF comparison remain unchanged.

Fixed-slack interpolation review, 2026-09-25: the [interpolation audit](../drafts/2026-09-25-fixed-slack-interpolation.md) checks the needed scalar input using the fixed-shape construction underlying Proposition 3.7, Corollary 3.9, and Lemma 4.1. L006 gives a full local proof with explicit parameters, over any field; C006a assembles the large-characteristic fixed-slack list certificate. This removes the preceding interpolation qualification for that certificate. The optimized derivative-order estimate, parametric theorem, all-field sharp boundary, and ABF comparison are not established. The prize threshold and field-existence proviso were rechecked and are unchanged.

These citations record current claims and prevent redundant work. The local partial proofs above do not establish the exact target.

## Mathlib

Full challenge: **not checked**. Full statements of the cited September results: **not checked**. Supporting polynomial and finite-field results: **not checked**. No matching Mathlib theorem is asserted, and unknown availability is not evidence of absence.
