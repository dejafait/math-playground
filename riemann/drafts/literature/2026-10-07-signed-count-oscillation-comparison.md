# Source coverage: signed count oscillation comparison

TARGET: Assess whether unconditional negative oscillations of the total zeta zero-count remainder, together with L372, obstruct L374's eventual count inequality for the actual pair.
CHECKED: 2026-10-07
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched unconditional signed Omega results for S(t) and Tsang's 1986 paper; retrieved Dobner arXiv:2101.01747v2 and Brent–Platt–Trudgian's published author offprint; scoped local count/disjointness assessments, failures and histories, and checked literature/foundations for these exact source identifiers.
SOURCE_EVIDENCE: Read Dobner v2 (25 March 2024), definitions/(1), Theorem 1 and complete Section 6 (PDF pp. 1–2, 18–20), including its negative-sign final paragraph; read Brent–Platt–Trudgian, Math. Comp. 90 (2021), 2923–2935, DOI 10.1090/mcom/3652, multiplicity convention p. 2923 and Section 2/(5)–(8), Lemma 2 with proof pp. 2926–2927; read L366 (1), L018 and L372, and L374's hypotheses/conclusion/proof. Direct primary sources: https://arxiv.org/html/2101.01747v2 and https://maths-people.anu.edu.au/brent/pd/rpb276-MC-preprint.pdf (published DOI landing page: https://doi.org/10.1090/mcom/3652).
COMPARISON: Dobner supplies unconditional negative deviations of S(t) on positive-measure sets and the total-count normalization; L372 has a bounded response-count remainder on each fixed ray. Source coverage suffices for a separate actual-pair count specialization; the count comparison and contradiction with L374 are not derived here.
GAP: A later research step must transfer the total strip count to the critical-line F_0 count in the correct inequality direction, retain analytic multiplicities and fixed-H corrections, select upper endpoints away from all zero ordinates, and compare with L374 without assuming RH or disjointness.
REASON: An inspected primary theorem closes the formerly missing unconditional sign/height coverage; only the elementary family-specific count assembly remains. Reproving the oscillation theorem would duplicate known mathematics.
SCOPE: Only literature comparison for the actual zero-regulator pair, with full multiplicity and one fixed eventual ray; no actual disjointness, D≤0, simplicity of F_0 zeros or RH is assumed.

This completes source review of the saved target. It establishes source
availability and applicability scope, not a new count consequence. The
separate proposed mathematical continuation is recorded in
`drafts/literature/2026-10-07-signed-count-deficit-specialization.md`;
its newly ready coverage receives supervisor approval next turn.

The main gap remains actual-theta mixed positivity and the total signed
margin. The intermediate source target asks whether a known signed
oscillation theorem can discharge the separate arithmetic count
comparison left by the physical-discriminant route. A successful
comparison could clarify which combination of physical inequalities
and noncoincidence is impossible; it would not independently prove
noncoincidence, a favorable total margin or RH.

Essential local inputs for review are L372's exact eventual response
count, L374's closed-endpoint conditional inequality, and L366's
definitions identifying the unshifted transform with completed zeta.
Use L018 only if the completion convention needs checking. Read their
relevant statements and proof ranges, and reuse their saved assessments
and critical audits. L376 is contrast/route evidence, not a mathematical
premise. No cross-notebook input is proposed.

## Inspected primary theorem and proof cases

Alexander Dobner, *Large deviations of the argument of the Riemann zeta
function*, [arXiv:2101.01747v2](https://arxiv.org/html/2101.01747v2),
25 March 2024, Theorem 1 (PDF p. 2): there are constants kappa,D>0
such that, for every sufficiently large T and every

\[
 \sqrt{\log\log T}\le V\le
 \kappa\left(\frac{\log T}{\log\log T}\right)^{1/3},
\]

\[
 \operatorname{meas}\{t\in[T,2T]:-S(t)\ge V\}
 \ge T\exp\left[-\frac{DV^2}
 {\log(\log T/(V^3\log V))}\right]>0.
\]

Here S uses the logarithm with horizontal cuts to the left of zeros/pole,
real at 2, and averaged limits at jumps. Equation (1), p. 1, is the
total-strip count with half weight at the upper endpoint:

\[
 N(t)=\frac{t}{2\pi}\log\frac{t}{2\pi}
       -\frac{t}{2\pi}+\frac78+S(t)+O(t^{-1}).
\]

Section 6, pp. 18–20, was read completely: both parameter cases retain
the exceptional off-line-zero term; (25)–(26) pass from smoothing to
positive measure for S itself; the final paragraph uses angle pi/2 for
the negative sign. Section 7's RH-dependent Theorem 2 is excluded.
The logarithmic denominator was checked against HTML, since PDF text
extraction loses its nested logarithm. No proof of the theorem is repeated.

Richard P. Brent, David J. Platt and Timothy S. Trudgian, *Accurate
estimation of sums over zeros of the Riemann zeta-function*,
Math. Comp. **90**, no. 332 (2021), 2923–2935,
[published author offprint](https://maths-people.anu.edu.au/brent/pd/rpb276-MC-preprint.pdf),
DOI 10.1090/mcom/3652. The first-page convention explicitly retains
multiplicities and half endpoint weights. Section 2, (5)–(8) and Lemma 2
with its complete proof, pp. 2926–2927, confirms the standard path branch,
the total count and its normalization. For t≥2pi it bounds the difference
between the count remainder (including 7/8) and S(t) by 1/(150t), including
zero heights by continuity of that difference. It cites Titchmarsh,
second edition (1986), Theorem 9.3. This is a precise source for the
count conventions, not a theorem about G or critical-line completeness.

## Scope comparison and prospective application

L366 (1) identifies F_0(t)=2xi_c(1/2+it). L018 identifies exactly which
zeta zeros this restriction can count and preserves their multiplicities.
It does not identify its real-zero count with the total strip count
without RH. L372 (1)/(12) has the same two main terms as the sources
and a bounded error for each fixed H, with full closed endpoints. L374
requires no common real zeros, physical D≤0 and strict response Laguerre
positivity on one ray. Its conditional count inequality is already
canonical and separately audited; no premise for the actual pair is
provided by this source review.

The covered continuation should use the theorem's positive-measure
negative set to address upper-endpoint conventions, rather than assert
a uniformly bounded correction for zero-height multiplicities. It must
justify excluding all strip-zero ordinates, not just critical-line zeros,
and retain the finite correction at the fixed lower endpoint even when
H is a zero. A diverging negative threshold, rather than an effective
onset or the sharp Omega exponent, is sufficient for the proposed test.
These are prospective applicability obligations; no deficit theorem or
actual-pair incompatibility is proved in this literature-only turn.

## Searches, reuse and retained failures

Queries: `Selberg S(t) Omega plus minus sqrt log t log log t unconditional
theorem`; `unconditional S(t) negative omega Riemann von Mangoldt remainder
theorem Tsang`; `"S(t)" "unconditional" "Omega" Selberg Tsang negative`;
`"Tsang" "Some" "theorems" "1986" zeta`. Search snippets and secondary
summaries were used only to find primary leads. Exact-source-identifier
searches in local literature/foundations found no ready Dobner or
Brent–Platt–Trudgian assessment to duplicate.

The parent `2026-10-06-discriminant-zero-interlacing.md` had SOURCE_BLOCKED
for unconditional S(t), after inspecting conditional n=0 results and
unconditional higher iterates. This review supplies a different accessible
primary source for that exact missing input; it does not override the
common-zero failures L371/L373. Reuse
`2026-10-06-response-zero-count-audit.md` and
`2026-10-07-disjoint-zero-count-audit.md` for the unchanged local inputs.
L375/L376 address geometric noncoincidence only and are not count inputs.

Tsang, *Some Omega-theorems for the Riemann zeta-function*, Acta Arith.
46(4) (1986), 369–395, DOI 10.4064/aa-46-4-369-395, remains an unread
original-theorem lead: the IMPAN full-text link failed. Dobner's directly
inspected stronger measure theorem suffices, so this access failure is
not an essential blocker. Selberg's original papers, Titchmarsh's book
proof and the related RH-conditional improvements are not imported by
pretending their proofs were retrieved. The attempt to download Dobner
through shell curl failed DNS, and PDF screenshot outputs had no readable
images; its readable primary HTML/PDF text supplies the necessary evidence.

The source acceptance test passes: unconditional negative sign, an
unbounded allowed threshold, positive-measure height sets, total-count
normalization and multiplicity conventions have inspected primary
coverage. Continue to the separate specialization after supervisor
approval. Abandon that application if its critical-line/total inequality
direction or an endpoint correction cannot be justified without an
additional hypothesis. Actual disjointness, physical D≤0, the total L367
margin and RH remain unresolved. Full matching Mathlib coverage for the
oscillation theorem and actual-pair count comparison is **not checked**;
this means neither absence nor novelty. No lemma, mathematical script,
DAG or PROOF change is made. This is local source progress using known
mathematics, not progress beyond the inspected sources.
