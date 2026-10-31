# Hybrid norm moving-mask reductions — completed source gate

TARGET: Review source coverage for a conditional audit of the two moving-mask reductions in family 003 lem:hybrid-energy at commit 1581d4cbdd69a0faf34b2089614fe2a814316a6a, retaining lem:completed-quadratic-reduction and eq:cubic-large-sieve and checking their exact coefficient, source-support and divisor-charge interfaces.
CHECKED: 2026-10-31
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the terminal assessment's primary Goldmakher–Louvel and Xu–Sang comparisons; scoped searches of family003 assessments/notes, ATTEMPTS, L541 and immediate history found no completed matching audit. No new generic external search was needed; the missing primary theorem was retrieved directly. Search failures establish no novelty.
SOURCE_EVIDENCE: Read pinned build/paper.tex completed-quadratic-reduction statement 2518–2566 and essential support/normalization proof 2567–2626; cubic-large-sieve and scope 7036–7053; entire hybrid statement/proof 7054–7194. Arbitrary row-independent complex coefficients, weighted r/c' factors, S-parts, shared primes and bounded/empty cases are explicit. Heath-Brown's original Theorem 2 remains unread; only the pinned cubic formulation is retained.
COMPARISON: L541 treats the complete hybrid norm as a contract. A later bounded audit would test its two mask reductions from the explicitly retained quadratic reduction and cubic sieve; generic quadratic or sextic bounds do not automatically validate those coefficient interfaces. The target reproduces a source claim and has no novelty presumption.
GAP: Essential source coverage for the scoped conditional implication is now complete. Mathematical verification of its zero identities, independence, allowed positive enlargements, divisor charges and quotient cases remains a separate audit; primitive arithmetic and Xi signs remain unresolved.
REASON: The missing theorem interface has been inspected without deriving the hybrid implication. The distinct audit target is recorded in drafts/literature/2026-10-31-family003-hybrid-mask-reduction-audit.md for separate next-turn approval; this source review establishes no norm bound.
SCOPE: Review only the implication from the retained completed quadratic reduction and the displayed cubic-sieve estimate to old-eq:4.6b, including both explicit masks, coefficients independent of the remaining sieve row, original n/b support, squarefree restrictions, divisor Cauchy and bounded/empty quotient ranges. Exclude proving the primitive sieve/reduction theorems, structural reflection, global manuscript closure and Xi signs.
LITERATURE_REASON: The interior proof of lem:hybrid-energy was excluded from the terminal application assessment; its essential completed-quadratic-reduction statement and hypotheses were unread for this application at nomination. This review supplies that coverage.

Primary source: OpenAI, *The Quasi-Riemann Hypothesis: A Zero-Free
Half-Plane Re(s)>7/8*, 30 September 2026, commit
`1581d4cbdd69a0faf34b2089614fe2a814316a6a`,
[pinned build/paper.tex](https://raw.githubusercontent.com/openai/math/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex).

Completed the exact theorem and support-case reading before comparing
the hybrid proof. Evidence and limitations are recorded in
`drafts/audits/2026-10-31-family003-hybrid-mask-source-notes.md`.
The future application retains both primitive estimates explicitly, so
the blocked original cubic paper is not silently imported as audited.
Neither the hybrid conclusion nor L541/L538–L540 is an input to that audit.

The discriminating source test is whether the D-mask and completed
quadratic output have exactly the restrictions and factors the hybrid
proof needs, including its original S-parts and shared primes. Approve
only a precisely scoped later application audit; otherwise identify the
missing assumption or narrow the target. The later mathematical test
would be the claimed (K+NB)B{N+L+(NL)^(2/3)} norm with adjustable small
loss and no new pair-dependent mask. This is a target, not a derivation.

No independently justified creative sign-producing mechanism emerged
from the terminal audit: its output is an absolute energy bound, while
the main missing statement is actual-Xi all-degree positivity. This
scope review follows a concrete retained contract and is not labelled
creative to satisfy a scheduling preference. Mathlib coverage is not
checked. No cross-notebook input is proposed.
