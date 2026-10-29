# Simple-zero two-level masking — duplicate and source assessment

TARGET: Determine whether a real even polynomial with only simple zeros and a nonreal quartet can satisfy D_1(F;x)>=0 and D_2(F;x)>=0 for every real x.
CHECKED: 2026-10-25
DECISION: IMPORT
SEARCH_EVIDENCE: Notebook-local filename search found L260 and its September 23 simple-root masking attempt, omitted by the nomination; checked L251/L257, L260 in full, L261 for stronger recorded scope and L354 for contrast. External queries and primary-source reads are recorded below.
SOURCE_EVIDENCE: L260, entire canonical statement/proof; ATTEMPTS/2026-09-23-simple-root-masking-test.md; Cardon, arXiv:0911.1122v1 (5 November 2009), Theorems 1.1/2.1, Corollary 2.2 and proof of Theorem 2.1, pp. 1–4; Csordas, arXiv:1309.0055v2 (21 February 2014), Theorem 2.4 and Remarks 2.5, p. 4. Prior first-sign assessment reused for its stated limitations.
COMPARISON: L260 already answers the exact question affirmatively, with strict signs and simple zeros over C; its even translated product has the required distinct quartet. The inspected external all-order criterion does not reduce to two levels. L257's multiplicity qualification does not describe the notebook's strongest available two-level example.
GAP: No new construction is needed for this target. A separate critical audit of the existing L260 certificate is a concrete verification task; actual-Xi signs, effective height overlap and all-degree positivity remain unresolved.
REASON: Import the exact existing local result and preserve its historical stop rather than reproduce it or call it new mathematics. The nomination missed a duplicate, not an essential inaccessible source.
SCOPE: Real even polynomials, all zeros simple over C, a distinct nonreal quartet and both inequalities at every real center including roots; no actual-Xi, Fourier-kernel or zeta-simplicity premise.
LITERATURE_REASON: The invocation-start assessment was REVIEW_REQUIRED; this single review completes its missing exact-target comparison and discovers canonical coverage.

## Main gap, intermediate target and decision

The main gap remains initial signs at unbounded heights and global
mixed positivity for actual Xi. The intermediate target is TARGET:
its downstream use is to determine whether adding simplicity repairs
finite-level sufficiency. Continue to construction only if neither
existing sources nor local certificates settle that question. Abandon
that construction if a matching certificate already exists, or if a
primary obstruction theorem forbids it.

The duplicate test succeeds: L260 is an exact existing certificate.
Its recorded polynomial is P(z)=z(z²−ε²)(z²+b²), 0<ε<b, and the even
example is E(z)=P(z−10)P(z+10), b=1/4. This is quotation of its
construction, not a new derivation or a completed critical audit.
Its canonical proof gives explicit global coefficient formulas and
uses L257's finite coefficient convolution. It addresses real roots
and the full real axis; no compact-continuity extrapolation is needed.
The September attempt already stops simplicity as a repair of
second-level sufficiency. L261 even records a three-level extension;
that too must not be nominated as new construction work.

The earlier nomination correctly described L257 but overlooked L260.
Its proposed split-root test is therefore superseded by existing work.
This turn is an informative routing correction, not mathematical
progress beyond the notebook or the external sources. No lemma,
script, DAG edge or assembled argument is changed. The single next
task is a bounded audit of L260, with fresh coverage recorded separately
for next-turn approval. Do not infer a theorem for arbitrary finite K.

## Bounded external comparison

Queries actually issued:

- `generalized Laguerre inequalities polynomial simple zeros counterexample first second inequalities Csordas Varga`
- `"Laguerre inequalities" "simple" "polynomial" counterexample`

Primary texts inspected:

1. David A. Cardon, *Extended Laguerre inequalities and a criterion for
   real zeros*, [arXiv:0911.1122v1](https://arxiv.org/pdf/0911.1122v1),
   submitted 5 November 2009, pp. 1–4, as specified above. Theorem 1.1
   treats nonzero f=e^(−bz²)f_1, b>=0, with f_1 real entire of genus
   zero or one; membership in the Laguerre–Polya class is equivalent
   to nonnegativity at every real x and every index. Theorem 2.1 uses
   an even auxiliary polynomial with nonnegative coefficients and a
   nonreal root, again requiring every coefficient. Its converse proof
   uses the whole expansion at a nonreal zero; the polynomial forward
   case uses real linear factors, followed by compact limits. This
   is no two-index converse. Polynomials fit the hypotheses, but the
   all-index requirement remains. The arXiv text was accessible; a
   CiteSeer PDF mirror returned 403 and is unnecessary.
2. George Csordas, *Fourier transforms of positive definite kernels and
   the Riemann ξ-Function*, [arXiv:1309.0055v2](https://arxiv.org/pdf/1309.0055v2),
   Theorem 2.4 and Remarks 2.5, p. 4. Its coefficient identity (2.11)
   matches the notebook D_n normalization exactly. Its converse likewise
   requires every n and every x. This comparison reuses the
   [first-sign assessment](2026-09-27-first-laguerre-zero-compensation.md)
   for Propositions 2.2–2.3 and its actual-Xi limitations.

The searches also returned Hawaiian-conjecture material and discrete
partition-sequence inequalities; these do not supply the exact
simultaneous two-level polynomial example. They were discovery leads,
not imported theorems. No exhaustive search or originality claim is
made. External all-order criteria are contextual inputs; L260 itself
supplies the exact local answer. A new reproof is unnecessary.

## Mathlib and continuation qualifications

L260 records Mathlib coverage as unchecked. This review does not
upgrade that statement. The complete polynomial certificate remains
canonical in lemmas/L260-simple-root-strict-second-level-masking.md;
its mathematical input L257 remains canonical in its own lemma file.
The next audit must check the two formulas, parameter signs, all ten
root distinctions, evenness and convolution including real roots and
infinity. A failed identity, root collision or sign violation would
require a documented correction; success merely validates reuse of
the old counterexample. Neither outcome establishes signs for Xi,
a positive Fourier representation, RH or a counterexample to RH.
