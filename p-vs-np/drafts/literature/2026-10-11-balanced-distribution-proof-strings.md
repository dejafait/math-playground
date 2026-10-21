# Balanced distribution proof strings — completed source comparison

TARGET: Construct and independently check native and literal NOT/OR Frege proof strings for distributing one supplied shallow left factor over a balanced XOR slot tree, with logarithmic depth and polynomial full-bit bounds.
CHECKED: 2026-10-11
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused step-167/169 coverage; searched Metamath for conjunction distributing over XOR and scoped L055/L056, compiler/checker/suite interfaces, histories 167–170 and Attempt 018 for overlap/failures.
SOURCE_EVIDENCE: Inspected complete xordi/anbi2/anbi2d statements and displayed proofs, followed xordi's annim/pm5.32/xchbinx proof cases, and read df-an/df-bi definition elimination; primitive basis, completeness, XOR congruence and literal translation reuse saved assessments.
COMPARISON: Known fixed distributivity/product-congruence laws cover arbitrary substituted Boolean formulas; they do not verify the balanced compiler, its full-bit ledger or completeness for arbitrary ordinary inputs.
GAP: Emit/check primitive fixed templates, implement balanced contextual composition, and establish all-size depth/record/byte bounds with actual formula copying.
REASON: Essential logical coverage is accessible; remaining work is implementation/reproduction of known fixed laws, not an unread theorem or new mechanism.
SCOPE: Exactly TARGET for M=2^h, h>=1, one fully written shallow native NOT/implication factor, M such slots, ASCII-encoded names and literal NOT/OR images; perfect balanced input/output order. No arbitrary ordinary-input normalization or whole receiver.
LITERATURE_REASON: The saved continuation lacked the specific distribution/product interface comparison; new xordi/anbi2 coverage fills it while unchanged primitive coverage is reused.

## Relevance, overlap and evidence boundary

The main gap remains unrestricted SAT decision/separation. This single-factor component could discharge L055 §§4–5/8's distribution/factoring in backward coordinate comparisons. Other coordinate/zero-identity/guard strings, certificate existence, general ER representation, W/V/U and SAT transfer remain independent gaps.

Read L055's row-transition/rewrite/audit passages and L056's hypotheses, primitive library and audited cache qualification; inspected compiler.py's formula definitions, schemas and instance handling, checker.py's pattern/matching/serialized format, and run_suite.py's contextual lifting. L056 implements XOR exchange/cancellation and XOR congruence, but its fixed library contains no product/distribution entry. Its constants cannot be inherited for an enlarged library. Histories 167–170 confirm this distinct pending component. Attempt 018 preserves the stop against repeated approval with no new evidence; this review fills a specific missing law once and routes to implementation. No cross-notebook input is used.

## Precise primary coverage

New sources are live public-domain Metamath Proof Explorer pages inspected 2026-10-11, identified by stable labels rather than numerical ordinals, which differ across retrieved versions. No raw HTML or set.mm revision is pinned. The exact statements/proof cases below are the source evidence, not a locally verified source database. Reused version/hash qualifications remain in step-167/169 assessments and scripts/balanced-slot/sources/provenance.json.

[xordi](https://us.metamath.org/mpeuni/xordi.html), contributed 3-Oct-2008, has arbitrary wff A,B,C and no logical premises:

    (A AND NOT(B IFF C)) IFF NOT((A AND B) IFF (A AND C)).

Read its complete three-line proof: annim identifies the left expression with NOT(A IMPLIES (B IFF C)); pm5.32 identifies the inner implication with the product biconditional; xchbinx combines the equivalences under negation. Its listed axioms are ax-1/2/3 and MP, with df-an/df-bi definitions. It covers fixed classical Boolean distribution, not a free-ring identity or a growing-proof size bound.

Followed [annim](https://us.metamath.org/mpeuni/annim.html): no premises, (A AND NOT B) IFF NOT(A IMPLIES B); its two displayed steps use iman/con2bii. [pm5.32](https://us.metamath.org/mpeuni/pm5.32.html), Whitehead–Russell *5.32 p.125, has no premises and states (A IMPLIES (B IFF C)) IFF ((A AND B) IFF (A AND C)). Read all nine displayed steps, using negation equivalence, implication congruence/distribution, conjunction definitions and equivalence composition. [xchbinx](https://us.metamath.org/mpeuni/xchbinx.html) requires D IFF NOT E and E IFF F, concluding D IFF NOT F; its four steps retain both premises, negate the second equivalence and compose. Earlier references were not recursively expanded or locally verified here.

[anbi2](https://us.metamath.org/mpeuni/anbi2.html) is the closed law (A IFF B) IMPLIES ((C AND A) IFF (C AND B)); its two steps use identity and anbi2d. [anbi2d](https://us.metamath.org/mpeuni/anbi2d.html) requires H IMPLIES (A IFF B), concluding H IMPLIES ((C AND A) IFF (C AND B)); read its three steps using the hypothesis, a1d and pm5.32d. The equivalence premise cannot be omitted. Closed product congruence can receive an earlier equality by MP. XOR ancestor congruence, symmetry/transitivity, double-negation bridges and fixed-law substitution reuse step-167 and L056 with their actual hypotheses.

[df-an](https://us.metamath.org/mpeuni/df-an.html) defines A AND B as NOT(A IMPLIES NOT B) and explains elimination via biid. [df-bi](https://us.metamath.org/mpeuni/df-bi.html) defines equivalence as NOT((A IMPLIES B) IMPLIES NOT(B IMPLIES A)), and explains replacing definition instances by bijust. Definitions cannot remain extra checker rules. No general source theorem needs reproving; implementation needs concrete primitive strings instead of unpaid law names.

## Approved native/image interface

Retain L056's literal X(A,B)=((A→B)→NOT(B→A)), E(A,B)=NOT X(A,B), Z=NOT(q→q), with q free. Select P(A,B)=NOT(A→NOT B), the df-an expansion. The requested endpoint is

    E(P(A,B_M(T)), B_M(P(A,T_0),...,P(A,T_(M−1)))).

Both B_M trees have the same perfect balanced order. This specifies the test, not a newly proved theorem. Fixed templates to emit are E(P(A,X(B,C)), X(P(A,B),P(A,C))) and E(B,C)→E(P(A,B),P(A,C)). Source NOT(B IFF C) expands literally to NOT NOT X(B,C), so it cannot be identified syntactically with native X. Expand the source proof with paid bridges, or synthesize the selected constant-size native templates under the reused completeness theorem and check their primitive lines before growing substitution. Completeness supplies fixed finite proofs only, not an efficient arbitrary-tautology proof finder. No template was synthesized/checked here.

Use literal τ(NOT U)=NOT τ(U), τ(U→V)=NOT τ(U) OR τ(V). The product image is NOT(NOT τ(A) OR NOT τ(B)); other double negations remain written. Translate every line/substitution field and accept only translated ax-1/2/3 and MP. Native completeness is the anchor; the image calculus is not separately established complete for arbitrary NOT/OR inputs or every ordinary Frege presentation.

## Continuation/abandonment test

Implement one bounded suite at M=2,4,8, with variable/composite shallow factors, repeated slots, Z/truth and composite terms. Independently reconstruct endpoints without the emitter planner. Check complete native/image streams and new fixed proofs; reject corrupt axiom substitution, MP antecedent/reference and endpoint. Save full certificates.

Required all-size threshold: in each format j, depth at most D_j+c_j log₂ M+d_j for input-independent constants established from the actual enlarged library/procedure, and one fixed polynomial in M, maximum fully written factor/slot size t_j and name payload B bounding lines, complete records and full binary length. These are thresholds sought, not bounds proved here. Establish explicit constants before measurement; charge formula and axiom-substitution copies, framing, names and references. Old L056 constants cover only its unchanged library. No arbitrary prepopulated mutable cache is allowed in the charged construction.

Continue if the implementation supplies all-size accounting and independently checked bounded evidence within it. Preserve and narrow/park on wrong endpoints, unmatched rules, superlogarithmic intermediate depth, unpaid copied terms/factors or an unproved receiving claim. Finite success alone is not an all-size proof; failure is not a Frege lower bound. Factoring needs the actual equality endpoint and paid symmetry, not reversed MP.

Essential inputs: L056 and complete step-170 library/audit certificates/code; L055 §§4–5/8; step-167/169 assessments; primary labels above. Fixed a and both formal IPS identities remain eventual-receiver premises, not component axioms. Ordinary-input normalization/image completeness, remaining receiver strings, certificate existence, ER representation, W/V/U and SAT transfer remain unresolved. Full matching Mathlib coverage is not checked; Metamath/Python checks are not Mathlib verification.

Step 171: EXPLORATION / LITERATURE / NOVELTY_UNCHECKED / literature_comparison. The unchanged TARGET is now SPECIALIZE; no new lemma, derivation, script, proof string, bound, audit verdict or originality claim. Mathematical exploration usage stays zero. Next is one RESEARCH implementation/reproduction step under this assessment.
