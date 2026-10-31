# Completed quadratic reduction — conditional audit scope

TARGET: Audit the conditional implication from eq:quadratic-large-sieve to eq:completed-quadratic-reduction in family 003 at commit 1581d4cbdd69a0faf34b2089614fe2a814316a6a, with fixed S containing all primes above 6, arbitrary row-independent coefficients, original S-parts, full collision expansion and bounded or empty quotient ranges.
CHECKED: 2026-10-31
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the completed primitive source gate and the terminal/hybrid comparisons; relevant local exact-claim searches found no matching completed primitive audit. No novelty claim.
SOURCE_EVIDENCE: https://raw.githubusercontent.com/openai/math/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex lines 519–588, 2480–2517 and 2518–2626; https://arxiv.org/pdf/1112.1642v2 Definition 1/Theorem 1.1/Corollary 1.2, PDF pp. 1–2; both retrieved 2026-10-31.
COMPARISON: The source claims the entire weighted reduction. The general squarefree-family theorem does not directly state it. Reproduction checks L542's retained contract; importing the final reduction would bypass the audit.
GAP: The weighted application remains unaudited. Retain the base display, source symbol conventions and ideal/divisor counts; exclude independent verification of the base Hecke-family specialization and broader S hypotheses.
REASON: Separate literature approval repairs the missing direct source URL; primary access and the retained scope are confirmed, without auditing the weighted implication.
LITERATURE_REASON: Supervisor recovery identified a missing direct source URL in this ready assessment; verify the exact primary endpoints and repair provenance rather than repeat mathematical research.
SCOPE: Fixed source arithmetic datum and comparison constants; S contains primes above 6 and fixed presentation/ray supports. No varying-S uniformity, bounded-beta corollary audit, independent base proof, reflection/global closure/Xi signs or cross-notebook input.

## Direct primary-source provenance and approval

The pinned [OpenAI primary TeX](https://raw.githubusercontent.com/openai/math/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex),
*The Quasi-Riemann Hypothesis*, 30 September 2026, was retrieved directly
on 2026-10-31. Rechecked the stated arithmetic conventions, base display,
weighted statement and support proof at the ranges in SOURCE_EVIDENCE.
The exact labels are `eq:quadratic-large-sieve`,
`lem:completed-quadratic-reduction` and `eq:completed-quadratic-reduction`.
The claim and its proof cases are accessible; correctness of the implication
is reserved for the conditional audit.

Goldmakher–Louvel, *A quadratic large sieve inequality over number fields*,
Math. Proc. Cambridge Philos. Soc. 154 (2013), 193–212,
[arXiv v2, 31 May 2012](https://arxiv.org/pdf/1112.1642v2),
Definition 1, Theorem 1.1 and Corollary 1.2 (PDF pp. 1–2), was also
retrieved directly. Its family hypotheses and squarefree-index bound
remain as assessed in the completed source gate; no independent family
specialization is approved here. The existing comparison is reused.

This separate source approval leaves DECISION SPECIALIZE and TARGET
unchanged. The edit repairs provenance only: no new bound, lemma or
mathematical audit result is established. Mathlib coverage is not checked.

Use the citations and qualifications in
[the completed source gate](2026-10-31-family003-completed-quadratic-primitive-scope.md).
Retain `eq:quadratic-large-sieve` for arbitrary complex coefficients,
squarefree good primary indices and cutoffs U,V>=1, with constants allowed
to depend on fixed S. Retain zero extension, multiplicativity and standard
ideal/divisor counts in Z[omega].

The target is precisely the weighted display at source lines 2544–2553,
including its original support D_r(t), not the bounded-beta corollary.
Preserve K,N,B>=1, squarefree primary n, unrestricted primary b and allowed
S-primes other than lambda. Write b=gt^2, c=(n,g), n=cm, g=ch, c=rc';
c,m,h are pairwise coprime squarefree while g,t may share primes.
In q_c asymp C, q_g asymp G, q_t asymp T, B asymp GT^2, the required
prefactor is (KNB)^epsilon T; each t,r summand has weight
(K/q_r+NG/C^2)C/q_r times the squared original coefficients reconstructed
by n=rc'm, b=rc'ht^2. Here r is squarefree good with
q_r bounded by a fixed multiple of min(K,C).

Check the zero identity, complete collision expansion, fixed row/column
restrictions, S-part separation and reconstruction, coefficient grouping,
divisor multiplicity and exact charges. Keep c' S-parts and shared g/t
primes. Treat empty ranges as zero and normalize both quotient lengths
by their maxima with one only with a proved nonempty-range comparison;
subunit centers can include units. Fixed sectors/bounded row scalars must
preserve coefficient independence and the constant. Do not use L542,
L541 or canonical conclusions as mathematical inputs.

Continue on the exact weighted implication with no extra power. Narrow or
stop on unsupported masks/support enlargement, coefficient dependence,
uncontrolled S dependence or a missing nonempty case. Success discharges
L542 Hypothesis 1 only under the source S hypotheses. Mathlib not checked.
