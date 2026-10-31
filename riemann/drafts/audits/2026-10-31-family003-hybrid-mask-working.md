# Hybrid-mask conditional audit working record

2026-10-31. Approved target: the implication specified by
`drafts/literature/2026-10-31-family003-hybrid-mask-reduction-audit.md`.
Task: RESEARCH / proof_audit / REPRODUCTION. This record preserves the
attempt before the detailed bookkeeping is finalized.

Main gap: actual-Xi all-degree positivity. Intermediate target: reproduce
old-eq:4.6b from the weighted completed quadratic reduction and the pinned
cubic-sieve formulation. Downstream use: reduce L541 Hypothesis 2 to these
primitives; their independent proofs and Xi transfer remain unresolved.
No L541 or canonical closure conclusion is an input.

The primary statement and full hybrid proof have been retrieved at commit
1581d4cbdd69a0faf34b2089614fe2a814316a6a, build/paper.tex, 7036–7194;
the quadratic input statement and relevant support cases are 2518–2626.
The shell download failed DNS; primary retrieval through the web tool
succeeded. Prior overlap/source assessments are reused, with no new
literature search or novelty claim. The scoped ATTEMPTS search found no
matching hybrid/completed-quadratic/moving-mask failure record.

Completed result: L542, `lemmas/L542-conditional-hybrid-moving-mask-audit.md`.
The full D expansion retains q_D^(-1); its quadratic coefficient is
row-independent and legitimately arbitrary complex. The zero identity
retains r,c',m zeros, and fixing ht before the cubic sieve leaves no moving
coefficient mask. The full T/r/C/D charges yield the required bound
(KNBL)^epsilon (K+NB)B{N+L+(NL)^(2/3)}, with no extra power.

The bounded-range qualification matters: a positive center below one can
still contain a unit because of fixed upper support constants. Normalize
such nonempty quotients by max(1,x); only an actual upper norm bound below
one forces emptiness. This repairs the source's loose sentence at 7191
without weakening its norm conclusion. No numerical or mathematical
script was needed. The result is conditional reproduction, not an
independent verification of the two primitives or progress beyond their
source claim. Canonical proof, hypotheses and Mathlib qualification are
in L542. Primitive coverage is the concrete continuation; no justified
creative sign mechanism emerged from this absolute-norm implication.
