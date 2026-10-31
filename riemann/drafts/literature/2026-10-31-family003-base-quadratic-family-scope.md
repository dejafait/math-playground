# Base quadratic Hecke-family specialization — source comparison completed

TARGET: Assess the Goldmakher–Louvel family-hypothesis specialization underlying eq:quadratic-large-sieve in family 003 at commit 1581d4cbdd69a0faf34b2089614fe2a814316a6a, including primitive conductors, fixed square/ray classes and transpose duality for fixed S containing primes above 6.
CHECKED: 2026-10-31
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused completed quadratic/terminal comparisons; searched family003 assessments, relevant audit notes, dated history and ATTEMPTS for Goldmakher, base quadratic and reciprocity-four-class. No matching independent audit was found. Queries "quadratic large sieve" "Eisenstein" Goldmakher Louvel primary and "quadratic" "primary" "lambda" "Goldmakher" found no inspected stronger matching independent specialization; mirrors are not independent evidence and search failure implies no novelty.
SOURCE_EVIDENCE: https://raw.githubusercontent.com/openai/math/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex lines 519–588, 772–859, 860–927, 933–947 and 2480–2517; https://arxiv.org/pdf/1112.1642v2 Definition 1/Theorem 1.1/Corollary 1.2 (PDF pp. 1–2), Section 2 conductor/primitive-product discussion (pp. 3–5) and Lemma 4.5 with proof (pp. 8–9), retrieved 2026-10-31.
COMPARISON: Goldmakher–Louvel supplies the required arbitrary-coefficient squarefree bound for a verified quadratic Hecke family. The pinned source claims the entire specialization; its conductor correction, group identification and exact matrix orientation still require a separate applicability audit. Corollary 1.2 cannot bypass verification by merely naming the sextic symbol.
GAP: Essential source statements and relevant proof cases are accessible and now inspected. The family specialization has not been proved or audited this turn; L543 still assumes its base estimate. Wider S hypotheses, varying-S uniformity and independent Gaussian-proof verification remain outside the proposed applicability audit.
REASON: Approve a separate reproduction of the identified family application under fixed source hypotheses; importing the manuscript's final bound would bypass that audit. No new mathematical implication is established in this literature turn.
LITERATURE_REASON: The independent family specialization was explicitly excluded from the weighted audit; the previously unread reciprocity proof cases and Goldmakher–Louvel primitive-inducing and duality conventions were essential to its source gate.
SCOPE: Fixed S contains primes above 6 and fixed presentation/ray supports. Standard residue-field and CRT facts and the cited quadratic reciprocity formula are inputs; the Gaussian derivation is inspected, not independently certified. No cubic primitive, reflection, global closure, Xi signs or cross-notebook input.

## Reuse and completed source work

Reuse the inspected statements and comparisons in
[the completed source gate](2026-10-31-family003-completed-quadratic-primitive-scope.md)
and [the weighted audit assessment](2026-10-31-family003-completed-quadratic-primitive-audit.md).
Do not repeat the completed weighted proof or infer the base estimate
backwards from L543, L542 or L541.

The precise source lead is OpenAI, *The Quasi-Riemann Hypothesis*,
30 September 2026, pinned commit above, `eq:quadratic-large-sieve`
and its adjoining family-identification paragraph. The paragraph invokes
`eq:reciprocity-four-class`; its essential statement/proof cases were not
covered by the weighted audit and have now been retrieved narrowly.
Compare them to Goldmakher–Louvel, *A quadratic large sieve inequality
over number fields*, Math. Proc. Cambridge Philos. Soc. 154 (2013),
193–212, arXiv:1112.1642v2, Definition 1/Theorem 1.1/Corollary 1.2.
The abstract theorem comparison is reused; the new reads cover its
previously missing family and orientation interfaces. Applicability is
reserved for the separate research audit below.

The intermediate target would reduce L543's retained base assumption to
an independent cited theorem. Its decisive test is a complete match for
the primitive inducing characters, trivial infinite type, finite-group
reciprocity, same-class primitive product, and transpose orientation,
with every fixed-prime correction and coefficient partition accounted for.
The next audit is approved only at the stated source scope. No suspected
failure or new mathematical implication is asserted here.

L543 is a downstream audit result; its base estimate (1), the fixed
zero/multiplicative conventions and the standard ideal/divisor counts are
the relevant interfaces. L542/L541, reflection, the cubic estimate and
actual-Xi all-degree positivity remain independent open contracts.
No cross-notebook input is proposed. Mathlib coverage is not checked.

## Exact theorem interfaces and outstanding audit

Goldmakher–Louvel, *A quadratic large sieve inequality over number
fields*, Math. Proc. Cambridge Philos. Soc. 154 (2013), 193–212,
[v2, 31 May 2012](https://arxiv.org/pdf/1112.1642v2), Definition 1 and
Theorem 1.1, require primitive characters with trivial infinite type,
quadratic order, finite-group reciprocity, and exact primitive conductor
ab for coprime indices in one group class. Both index sets are squarefree
and avoid the fixed modulus; lengths are at least one and coefficients
are arbitrary complex numbers. The constant permits fixed field/modulus
dependence. Section 2, PDF pp. 4–5, explicitly passes to primitive
inducing characters and the primitive character inducing a product.
Its construction is noncanonical, so it cannot simply be identified with
the present primary-generator family. Lemma 4.5, PDF pp. 8–9, proves
orientation comparison through finite-group twists and Hilbert-space
duality. This supplies an inspected orientation precedent.

The pinned [primary TeX](https://raw.githubusercontent.com/openai/math/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex),
`eq:quadratic-large-sieve`, claims conductor a lambda^{e(a)} for the
primary-evaluated quadratic character, where e(a)=(q_a-1)/2 modulo 2.
It omits the lambda factor when e(a)=0 and asserts same-class cancellation
of that correction. `lem:quadratic-four-term` supplies Gamma modulo 4;
`eq:reciprocity-four-class` gives its four-class bicharacter. The relevant
proof cases were read: Gaussian limiting argument, square invariance,
four representative evaluations, CRT for distinct good primes, and
multiplicative extension. The quadratic kernel needs that quadratic
identity; auditing the full sextic/cubic reciprocity machinery is not
necessary for this application. These are inspected source claims,
not new local proofs or an independent certification of that Gaussian
argument.

The applicability audit must distinguish an ideal from its primary
generator, specify a homomorphism on all ideals avoiding the fixed
modulus, check primitivity also at each prime of a, and handle the unit
ideal and e(a)=0 without an artificial zero at lambda. It must compare
the primitive character values to Q_a(b) on all good squarefree pairs,
including noncoprime pairs. Same-class primitive products must have no
residual fixed-prime conductor. A restriction to a class alone is not a
new Hecke family indexed by all ideals: verify the global family first,
or justify any extension, then partition the matrix. Transpose duality
must preserve arbitrary coefficients and the U+V bound. Extra fixed
S-primes may be removed by support restrictions only after those checks.
No row-and-column-dependent mask is authorized by coefficient zeroing.

The ready continuation is
[the family audit](2026-10-31-family003-base-quadratic-family-audit.md).
It receives separate next-turn approval. The current result is source
coverage sufficient to attempt that audit, not discharge of L543 (1).
No new lemma, mathematical script, PROOF or DAG change was made.
