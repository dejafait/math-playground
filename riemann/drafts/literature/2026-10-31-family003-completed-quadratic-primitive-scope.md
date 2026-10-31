# Completed quadratic primitive — source gate completed

TARGET: Assess the conditional implication from eq:quadratic-large-sieve to lem:completed-quadratic-reduction in family 003 at commit 1581d4cbdd69a0faf34b2089614fe2a814316a6a, checking arbitrary coefficients, fixed S-parts, full collision expansion and bounded quotient ranges.
CHECKED: 2026-10-31
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the terminal/hybrid Goldmakher–Louvel comparisons; searched relevant family003 notes/history and ATTEMPTS for completed-quadratic, quadratic-large-sieve and Goldmakher. No completed matching primitive audit or matching counterexample was found; this establishes no novelty.
SOURCE_EVIDENCE: Newly inspected pinned build/paper.tex 2480–2517 (base estimate and claimed family specialization), 519–588 (primary/S/zero conventions); consulted the previously inspected 2518–2626 for the weighted interface and essential proof cases. Goldmakher–Louvel arXiv:1112.1642v2 Definition 1, Theorem 1.1 and Corollary 1.2, PDF pp. 1–2, were checked against the earlier assessment.
COMPARISON: The base estimate allows arbitrary complex coefficients on squarefree good indices; it does not itself state the weighted completed-index reduction. The source already claims that reduction. Its fixed S contains all primes above 6, stronger than the explicit minimal S condition in L542. A conditional reproduction should retain the displayed base estimate rather than silently verify its Hecke-family identification.
GAP: Essential coverage is complete for the narrowed conditional application audit; the implication remains unverified. The independent base specialization, applicability beyond source S hypotheses, varying-S uniformity, reflection, global closure and actual-Xi signs remain open.
REASON: Retrieve the missing source interface and approve only a separate reproduction under its exact setting; no new implication is established here and L542 cannot be used backwards.
LITERATURE_REASON: Essential unread base-interface coverage was requested by the pending gate and excluded from the completed hybrid audit.
SCOPE: Literature comparison only. Fixed S contains primes above 6 and fixed presentation/ray supports; retain the base estimate, source symbol conventions and standard ideal/divisor counts. No cross-notebook input.

## Precise citations and comparison

OpenAI, *The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane Re(s)>7/8*,
30 September 2026, commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a`,
[primary TeX](https://raw.githubusercontent.com/openai/math/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex),
`eq:quadratic-large-sieve`, `lem:completed-quadratic-reduction` and
`eq:completed-quadratic-reduction`. Stable labels specify the claims;
line ranges above locate this version. Web retrieval succeeded; shell
curl failed DNS resolution and supplied no evidence.

Goldmakher–Louvel, *A quadratic large sieve inequality over number fields*,
Math. Proc. Cambridge Philos. Soc. 154 (2013), 193–212,
[arXiv:1112.1642v2](https://arxiv.org/pdf/1112.1642v2), 31 May 2012,
Definition 1 and Theorem 1.1 (PDF pp. 1–2): primitive Hecke characters of
trivial infinite type, order dividing two, finite-group reciprocity on
coprime indices, and a primitive product of conductor ab for coprime
same-class a,b. Both sums are squarefree and avoid the fixed modulus.
For M,N>=1 and arbitrary complex coefficients the squared operator norm
is O((MN)^epsilon(M+N)); constants depend on field, modulus and epsilon.
Corollary 1.2 applies to quadratic powers of even-order Hecke families
satisfying those family conditions. Naming a residue symbol alone does
not verify them.

The pinned source asserts the primitive inducing-character identification,
its possible lambda conductor factor, same-primary-class cancellation,
finite ray partition and transpose orientation. These are retained
provenance for the displayed base estimate, not independently established
by this review. Conditional work from that display does not silently
approve those assertions. The stronger completed-index conclusion needs
its own application audit; a citation to Theorem 1.1 alone bypasses it.

Reuse [the terminal comparison](2026-10-31-family003-reflected-energy-terminal-audit.md)
and [the hybrid notes](../audits/2026-10-31-family003-hybrid-mask-source-notes.md).
Their cubic/sextic comparisons do not replace this weighted quadratic
application. The recorded Heath-Brown access failure belongs to another
retained primitive and does not block this gate. No fresh generic search
was necessary. Searches and source statements do not establish novelty.

## Continuation and limits

Actual-Xi all-degree positivity is the main gap. The intermediate target
is the weighted reduction used in L542 Hypothesis 1. Its audit could
reduce that contract to the base sieve in the source setting. Independent
primitive verification, reflection and all global/sign gaps would remain.

Audit obligations are arbitrary row-independent beta, full original
support, S-part reconstruction, shared g/t primes, complete collision
expansion, grouping multiplicities and the exact weighted charges. These
are identified source proof cases, not newly proved claims. Bounded and
empty quotient cases must be checked, including positive subunit centers
that can contain units under fixed comparisons.

The source fixes S to include primes above 2 and 3. L542 explicitly names
only lambda in its abstract conditional hypotheses. Its conditional proof
is preserved; a reproduction here cannot discharge its retained input
at that broader generality. Enlarging S changes row support and cannot
silently prove missing cases. No lemma modification occurs this turn.

Continue only if the exact weighted output follows with no extra power,
unsupported residual mask or coefficient dependence. Narrow or stop on a
missing fixed-prime hypothesis, nonempty quotient failure or uncontrolled
S dependence; varying-S uniformity is excluded. Mathlib was not checked.
The [new audit assessment](2026-10-31-family003-completed-quadratic-primitive-audit.md)
receives separate next-turn approval. No mathematical audit was run here.
