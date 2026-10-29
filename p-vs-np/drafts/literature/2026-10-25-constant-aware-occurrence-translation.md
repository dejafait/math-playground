# Constant-aware occurrence translation — bounded specialization reviewed

TARGET: Implement a bounded constant-aware original-only translation for the retained 31-record occurrence proof, preserving exact ordered polynomials, caller data and existing caps.
CHECKED: 2026-10-25
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 472 searched noncommutative formula constant elimination/folding and ABP conversion; inspected Raz–Shpilka Lemma 2 Step 1 and LTW Definition 1.3/Lemma 4.8 proof, plus scoped prior assessments, L035/L036 contracts, L108 extraction, L097 endpoint/stop and Attempts 036–039. No matching finite receiver optimization was established.
SOURCE_EVIDENCE: Raz–Shpilka author-hosted 16-page manuscript §2.1 pp.4–5, Lemma 2 statement and complete Step 1; LTW 40-page author manuscript Definition 1.3 p.6 and Lemma 4.8 statement/proof p.26, retrieved 2026-10-25. Reuse audited L035/L036 and L108 with prior source qualifications; precise applicability below.
COMPARISON: Ordered scalar arithmetic and formula-to-graph composition cover the component operations; LTW's constant-free zero-formula/Frege conclusion does not certify this arbitrary-operand translator. The specialization is bounded integration with unchanged correction constructors and independent formal reception, not a new normalization theorem.
GAP: Implementation preservation, benefit on the exact 31-record input, all-root checks and complete K/H reception remain unverified. No reduction past record 7 or all-size optimized interpreter bound is asserted.
REASON: Essential source coverage is sufficient for the restricted implementation test below; this review closes a source-scope gap without deriving a lemma or executing mathematics. Success remains conditional on the saved resource and formal-identity tests.
LITERATURE_REASON: Step 471 changed representation outside ready step-460 coverage; this separate review supplies the missing comparison and reuses correction/reception coverage.
SCOPE: Only scalar cases in original-only arithmetic translation of the unchanged retained proof; preserve every caller tree, source root, block role, multiplicity, ordered dictionary and cap. No correction-constructor optimization, general identity testing or Boolean normalization.

Step 471 required this separate literature-only review. Its proposal is retained
below; the completed comparison and bounded scope follow it. Reuse component
citations only where their hypotheses match. Do not synthesize a different endpoint
proof, increase caps, drop unused source records, alter dictionary positions,
commute factors, or replace the exact translation by Boolean equivalence.

Main gap: unrestricted deterministic polynomial-time SAT decision/separation.
Intermediate purpose: test whether a different original-only representation
can make the existing supplied-proof extraction usable on this fixed input.
Potential downstream use is complete independent reception of L097 §6.5,
not proof availability or an M-only bound. Essential existing inputs are
L108's literal translation/extraction, L035/L036 original-only contracts,
L097 §§1–2,6.5,10–11 and L087's unchanged occurrence pair.

Preserved discriminating proposal from step 471: require exact formal ordered
translation agreement on every affected formula/operand, complete retained
caller data and source roots, and a predicted or measured reduction past the
record-7 stop within the unchanged cap. Full success still requires complete
K and H reception, not merely a smaller first seed. Reject or park the mechanism
if its required source coverage fails, it changes those identities, or it has
no concrete reduction of the recorded bottleneck. No such calculation has
been performed this turn. Empty-clause f=0, nonzero-correction coverage, trusted
paths/SHA, all-size resources and general proof availability remain unresolved.

## Completed source comparison — step 472

### Primary passages and applicability

The exact main target remains ordinary uniform worst-case P versus NP.
Reconfirmed the Clay page and its linked Stephen Cook, *The P versus NP
Problem*, §1 pp.1–2, 12-page official PDF, on 2026-10-25:
[official statement](https://www.claymath.org/wp-content/uploads/2022/06/pvsnp.pdf).
Its deterministic polynomial-time languages and checking relation with
polynomial witness length match foundations/01-model-and-target.md.
This finite representation test supplies no decision algorithm or
unrestricted lower bound. Historical algorithmic claims are not imported.

**Conversion.** Ran Raz and Amir Shpilka, *Deterministic Polynomial Identity
Testing in Non Commutative Models*, author-hosted 16-page manuscript,
revision date unestablished, §2.1 pp.4–5, Lemma 2 and complete Step 1:
[primary PDF](https://www.cs.tau.ac.il/~shpilka/publications/RazShpilka_PIT.pdf).
Scalar/variable leaves and ordered parallel/serial composition give the
nonleveled intermediate graph. Its field is arbitrary, permitting F₂.
The full homogeneous-component lemma assumes zero free term; only Step 1
is reused here. Later constant-edge elimination and homogeneous
normalization are unnecessary. The formula-input conversion does not
bound repeated correction construction on the supplied proof DAG.

**Constant comparison.** Fu Li, Iddo Tzameret and Zhengyu Wang,
*Characterizing Propositional Proofs as Non-Commutative Formulas*, SIAM J.
Comput. 47(4), 1424–1462 (2018), DOI 10.1137/16M1107632, inspected via the
40-page [author manuscript](https://www.doc.ic.ac.uk/~itzamere/Ideal_non-commutative.pdf),
revision date unestablished: Definition 1.3 p.6 and complete Lemma 4.8
proof p.26. The definition matches L108 over F₂. The lemma assumes a
formula containing a variable and computing zero, and seeks a constant-free
formula with a Frege derivation. Its proof lists scalar addition/product
replacements, representing addition of one by Boolean negation. We import
neither that Boolean representation as an arithmetic leaf nor the terminal
constant-free conclusion or assertion excluding terminal zero. Arbitrary
operands here may be nonzero or scalar, and output constants are allowed.
This is a comparison, not a matching translator theorem. Standard ring/field
scalar laws suffice for the limited arithmetic cases below; no reproof of
this lemma is needed.

Search queries: `noncommutative arithmetic formula constant elimination
zero one algebraic branching program Raz Shpilka` and `arithmetic formula
simplification constant folding noncommutative zero one`. Results included
these primary texts and broader PIT/ABP minimization leads. Bogdanov–Wee,
*More on Noncommutative Polynomial Identity Testing*, was seen only as a
search lead; its minimization theorem/proof were not inspected or imported.
No completeness or novelty inference follows from this bounded search.
No essential source blocker remains for the restricted scalar operations;
arbitrary ABP minimization is outside scope.

### Existing results, failures and implementation difference

Reuse `2026-10-24-parameterized-four-rule-extraction.md` and
`2026-10-24-supplied-four-rule-occurrence-composition.md` in this directory.
L035 permits zero/constant x-only affine graphs with its exact ordered
commutator contract. L036 has the same input allowances and supplies
Booleanity. These audited local extensions remain the correction inputs.
L108 §2 formulates its rule identities for arbitrary original-only
argument polynomials, including constants; §§10–13 retain the serialized
interface and separately audited byte boundary. Its independent receiver
reconstructs source translations arithmetically rather than requiring the
unoptimized internal operand shape. Concrete inspection covered
emit_parameterized.py's translation/copy preflights and
receive_parameterized.py's expected block roles, original-only checks,
block arithmetic and per-line identities. This is contract comparison,
not an audit of future code.

The 2026-10-17 signed-and-syntactic-degree assessment mentions constant-aware
presentation but concerns an all-root T+D bound for a different DAG input.
It supplies neither this implementation nor its resource improvement.
L108's direct zero-graph ground axiom is not a whole-tree optimizer.
The scoped search established no completed matching optimization and no
originality claim. Full matching Mathlib coverage was not checked.

Attempt 039/L097 §11 stops the unoptimized input at zero-based record 7:
2,008,364 required records versus 2,000,000 allowed. This review uses its
canonical complete-graph/count evidence, without replay or any partial-K
arithmetic claim. Attempts 036–038 concern missing source reception or
preparation; this target consumes the supplied legal proof and leaves those
routes parked. It changes operand representation, preserving proof and stop
evidence. Source synthesis and cap changes are outside the assessed scope.

### Obligations for the later bounded attempt

1. Retain literal proof checking, every supplied tree and all 31 source
   roots, exact endpoint, caller manifest/request, original alphabet and
   complete ordered dictionary. Optimize only derived original-only
   arithmetic operands after literal checking. Keep scalar tags disjoint
   from original names and placeholders.
2. Restrict arithmetic folding to syntactically certified scalar cases:
   scalar-only operations in F₂, additive zero, multiplicative zero and
   multiplicative unit on either side. A nonconstant complement remains
   the arithmetic sum with one. No semantic scalar recognition, Boolean
   idempotence, factor commutation, source rewriting or nonconstant
   cancellation search is covered. Document the future implementation's
   structural preservation argument using these standard laws; this review
   derives no new induction, lemma or size estimate.
3. Output explicit acyclic affine graphs with the existing endpoint/framing
   contracts, independent copies and ordered factors. Pass original-only
   graphs to unchanged L035/L036 constructors. Preserve required block roles
   even when a substituted value is zero. Equality of old/new free
   placeholder witnesses is not required: original-operand equality and
   zero/substituted witness contracts are separate obligations.
4. Independently check formal ordered translation agreement for every
   affected operand, including nested correction-call operands, retaining
   complete evidence or a separately checkable structural trace. Reconstruct
   targets from unchanged source trees using receiver arithmetic independent
   of the emitter. Keep all zero/substituted block and source-root checks,
   then require complete K and L097 §6.5 H reception. A trace or smaller
   first graph alone is insufficient. Retain unused dictionary entries.
5. Keep all input, graph, label, arithmetic and output caps. Use fresh output
   paths for the exact retained input and report actual/required counts,
   failures and full load-bearing evidence. The first discriminator is
   construction beyond the previous record-7 stop within the unchanged cap;
   this is a future measured test, not a predicted reduction. Stop this
   mechanism/input combination if it fails. If it passes, continue only in
   the same bounded attempt toward complete independent K/H reception;
   preserve any later failure rather than equating prefix progress with
   acceptance.

SPECIALIZE covers known component operations with unverified bounded
integration and benefit. No mathematical result, executable calculation or
resource improvement was established here. This newly completed assessment
receives separate supervisor approval before research invocation.

Essential continuation inputs are L035/L036, L108 §2 and §§10–13,
L097 §§1–2,6.5,10–11 and L087's retained provenance/interface. Reuse
output-470 proof/request, output-461/final/empty-clause source/annotations/pair
and output-471 failure frames/count receipt, reading actual data narrowly
when needed. Trusted caller paths and remaining SHA bindings persist.
Empty-clause f=0 cannot test nonzero fJ. All-size interpreter resources,
general proof availability, M-only/W₂/ER transfer and SAT remain unresolved.
