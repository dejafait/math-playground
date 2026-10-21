# L059 — Complete supplied guarded proofs lifted through mixed contexts

## Hypotheses

Use L056's native NOT/implication calculus: ax-1 A→(B→A), ax-2 (A→(B→C))→((A→B)→(A→C)), ax-3 (NOT A→NOT B)→(B→A), and MP. Write, fully expanded at every occurrence,

    X(A,B)=((A→B)→NOT(B→A)), E(A,B)=NOT X(A,B),
    P(A,B)=NOT(A→NOT B).

Supply fully written native formula trees G,U,V and a complete assumption-free native proof pi with both declared endpoint and exact last formula G→E(U,V). Every formula, primitive rule tag, axiom substitution and strictly earlier MP reference is written. Retain unused records. Variable payloads are nonempty ASCII alphanumeric/underscore strings; other finite names require a charged injective encoding. Arbitrary depths, repeated terms and coincident names are permitted. No freshness condition is imposed.

Supply a finite binary context skeleton C with exactly one marked leaf. Its internal nodes are X or P; each unmarked leaf contains one fully written native formula. The mark is construction data, not a variable or assumption. Let s be its node count, h its height and k≤h the marked-leaf distance to the root. The identity context h=k=0 is allowed. For the polynomial claim require

    h ≤ a ceil(log₂(s+1))

for a fixed integer a≥1 independent of the input. Without that promise the explicit bounds below still hold, but no polynomial bound in s is asserted.

The literal image tau sends NOT A to NOT tau(A) and A→B to NOT tau(A) OR tau(B), retaining double negations. Only native proofs are supplied; the image calculus uses precisely the translated primitive schemas and MP. Arbitrary independently supplied NOT/OR proofs, arbitrary ordinary-input normalization and completeness for every ordinary Frege presentation are outside scope.

For each format j=native,image, let t_j≥1,d_j bound the nodes/depth of U,V and every unmarked term after literal translation. Let g_j,e_j be the nodes/depth of G. Let N count all supplied proof records, K_j sum all their formula and declared substitution nodes, and delta_j be their maximum formula/substitution depth. Let B≥1 bound every raw name payload, including the fixed one-character template names. Complete input includes the request, skeleton, terms, proof header and every record; all byte costs are uncompressed.

The fixed library below is part of the construction, not an arbitrary caller-provided proof cache. L055 section 6 is intended downstream use, not a premise. Guard-proof existence and any IPS certificate premises are not supplied by this result.

## Conclusion

There is a complete-record construction of a primitive native proof of

    G→E(C[U],C[V]),

and its line-by-line literal image. It validates pi in full against the external coordinate endpoint, retains every supplied record in fresh append-only state, relocates references explicitly and uses only fully copied primitive templates plus MP. No supplied-premise rule, formula DAG abbreviation, definition axiom or semantic inference is emitted.

The four fixed guarded templates have line counts 2165,2165,1471,1477 for X-left, X-right, P-left, P-right. Checked common constants are

    L=2165,
    (D_native,S_native,c_native)=(16,1260,3),
    (D_image,S_image,c_image)=(22,1776,6).

D bounds every fixed formula/substitution depth; S counts formula and substitution nodes together per record. Set

    R=k(L+1), J=N+R,
    Q_j=8·4^(h+1)(t_j+1), P_j=max(g_j,Q_j),
    F_J=256+64 ceil(log₂(J+2)).

Output lines are at most J, maximum complete-record nodes at most max(K_j,S_j P_j), and depth at most

    max(delta_j, D_j+max(e_j,c_j h+d_j)).                (1)

Output uncompressed bytes are at most

    (B+4)[K_j+(R+1)S_j P_j]+(J+2)F_J.                 (2)

Full binary length is eight times (2). For each fixed a, construction and checking admit polynomial bit time and output length in the full explicit input. Guard depth and supplied proof depth are retained by a maximum in (1), with only fixed/logarithmic context overhead; neither is multiplied by the number of ancestors. The separate step-182 critical audit below validates this conditional component after repairing an archive-path collision; no mathematical bound changes. This is an implementation reproduction of known logic, neither certified original mathematics nor a P-versus-NP advance beyond the sources checked.

## Proof

### Primary logical inputs and fixed primitive strings

Reuse L056's primitive-basis, fixed completeness and simultaneous-substitution coverage and L058's complete package import/copying contract, with their native/literal-image and fresh-state qualifications. Primary schemas are precisely [ax-1](https://us.metamath.org/mpeuni/ax-1.html), [ax-2](https://us.metamath.org/mpeuni/ax-2.html), [ax-3](https://us.metamath.org/mpeuni/ax-3.html), [ax-mp](https://us.metamath.org/mpeuni/ax-mp.html). The named Church P2/Lukasiewicz propositional completeness metatheorem is [Metamath Proof Explorer §§1.2–1.2.2](https://us.metamath.org/mpeuni/mmtheorems1.html), inspected in the saved step-167 assessment. Completeness is used only to synthesize fixed three-variable laws, never to bound proofs of growing tautologies. L056's source snapshots pin retrieved statement extracts, not a set.mm revision or recursively checked database.

The unchanged SPECIALIZE start assessment is `drafts/literature/2026-10-12-guarded-context-proof-strings.md`. It records inspection on 2026-10-12 of the complete primary statements and essential deduction cases: [xorbi12d](https://us.metamath.org/mpeuni/xorbi12d.html) takes G→(A↔B) and G→(C↔D) to G→((A XOR C)↔(B XOR D)); [biidd](https://us.metamath.org/mpeuni/biidd.html) gives G→(S↔S); [anbi1d](https://us.metamath.org/mpeuni/anbi1d.html) and [anbi2d](https://us.metamath.org/mpeuni/anbi2d.html) lift G→(A↔B) under conjunction in either argument. Parameters are arbitrary wffs, with no depth or freshness restrictions. The guarded XOR page was contributed 4-Sep-2016; the two AND pages 11-May-1993, shortened 16-Nov-2013. The source XOR expands to NOT NOT X here, so its theorem label cannot be used as a literal native rule. All definition labels must be paid or eliminated. The construction instead implements the native laws directly in the checked primitive basis.

Reuse the complete native congL/congR streams of L056, whose endpoints are H→K with H=E(A,B) and K=E(X(A,C),X(B,C)) or E(X(C,A),X(C,B)). Synthesize only the two analogous fixed P laws, under the inspected completeness input, using L056's fixed truth-table emitter. Their complete assumption-free native strings have 1467 and 1473 lines; independent primitive checking, rather than trust in the synthesis tactic or a truth table, establishes them. The implementation need is concrete fully paid strings, not a reproof of the known conjunction law as a discovery. L057's distribution theorem is not used.

Given any of these four complete H→K strings, copy it once and append precisely four primitive records:

    (H→K)→(G→(H→K))                       ax-1,
    G→(H→K)                               MP,
    (G→(H→K))→((G→H)→(G→K))              ax-2,
    (G→H)→(G→K)                           MP.

Thus each fixed guarded template has the exact endpoint needed to lift one earlier guarded equivalence. This elementary specialization merely instantiates the inspected primitive schemas. The complete eight native/image guarded streams were checked against these literal endpoints, and every image record was compared with the corresponding native record's literal translation. No new checking rule is introduced. `scripts/guarded-context/output/certificate-180.json` records the measured constants above; each maximum is over all records of the four fixed strings. All substitution depths are no larger than their axiom formula depths because the substitutions occur within the instantiated axiom. Their nodes are counted separately in S_j.

### Validation, complete import and induction on the context

`context_endpoints.py` independently validates the request and constructs C[U],C[V] by literal recursive substitution at the sole mark. It imports no emitter/planner. `lift.py` invokes L058's complete native package loader against G→E(U,V). Every line is checked by the unchanged primitive checker, all declared substitutions/names/references and the native header are validated, duplicate JSON fields are rejected, and the copied final formula is required to match. Hash comparison records stability across reads; proof membership comes from primitive checking and reconstruction, not hashes.

Start with a fresh `AppendProof`, whose addition retains each record without deduplication. Copy all N supplied records, reconstructing each axiom from its declared substitution and each MP from its relocated earlier references. Require the reconstructed formula to equal the supplied one. Here the input copy starts at offset zero; its references are numerically unchanged. Each subsequent template copy maps its local references to its fresh appended positions. The same explicit relocation method applies in both cases. No synthesizer helper/cache supplies a growing-input premise, and unused deep records are retained. Induction on the copied records establishes every inference in the output.

At the marked leaf the exact earlier conclusion is G→E(U,V). Suppose the marked child of an ancestor has literal terms A,B and earlier conclusion G→E(A,B). Reconstruct its unmarked sibling S, including the whole sibling skeleton and all its terms. Copy the fixed guarded template for that ancestor's operator and marked side with simultaneous substitution A↦A, B↦B, C↦S, G↦G. Apply MP to the earlier guarded conclusion. For a left marked child the new conclusion is G→E(op(A,S),op(B,S)); for a right marked child it is G→E(op(S,A),op(S,B)). These are exactly the terms of the enlarged supplied context.

Induction up the marked path gives G→E(C[U],C[V]) after k lifts. The final MP is the actual last record. For k=0 the imported endpoint is already the last record, and no additional proof is inserted. All premise references are earlier. Every replacement is simultaneous: a schematic variable returns its replacement without traversing that replacement again. Thus coincident input and template names, even names appearing in G or S, cause no capture or recursive substitution. Earlier guarded equivalences are used by proof reference; they never become context-term arguments. Terms may themselves contain text identical to G, which is part of their explicit paid input; the construction inserts no new guards inside them.

The image writer translates every formula and every substitution field, preserves rule tags/references, and writes fully parenthesized text. Induction on records establishes a proof in precisely the translated axiom/MP calculus. Its MP requires NOT antecedent OR consequent literally, retaining all double negations. This does not establish the excluded arbitrary ordinary-input interface.

### All-size line, depth and copying ledger

Import costs N lines. Each marked ancestor appends at most L fixed lines and one external MP, proving J. More exactly, the implementation uses N plus the sum over its ancestors of the selected template line count plus one. Templates are copied even if arguments coincide; the theorem requires the particular fixed library, not arbitrary mutable caller entries.

Every actual non-guard argument is a U/V subtree on the marked path or a fully reconstructed unmarked sibling. Its skeleton height is at most h above supplied terms. Native X contributes at most three depth levels per skeleton level; native P at most three. Their images contribute at most six and four respectively. A substituted record has depth at most its original fixed depth plus the maximum substituted-argument depth. Its guard argument has depth e_j, independently of h; its context arguments have depth at most c_j h+d_j. Hence all generated records have depth at most D_j+max(e_j,c_j h+d_j). External MP conclusions are subformulas of those instantiated implications, so obey the same bound. Retained supplied records have depth at most delta_j, proving (1). The header repeats the final formula and obeys that bound too. In particular, increasing k does not recursively nest G-bearing proofs beneath X or P.

Expanded native X has 4+2|A|+2|B| nodes and its image 7+2|tau(A)|+2|tau(B)|. Native P has 3+|A|+|B| and its image 4+|tau(A)|+|tau(B)|. Consequently every height-i context argument obeys

    p_0=t_j, p_(i+1)≤8+4p_i,
    p_i≤4^i t_j+8(4^i−1)/3≤Q_j  for i≤h.

G has g_j nodes and is substituted separately, so P_j=max(g_j,Q_j) bounds every actual argument. For a fixed record with u operator nodes and v variable occurrences, including its declared substitution fields, the substituted node count is at most u+vP_j≤S_j P_j. This pays every occurrence of G, rather than treating the guard as a free abbreviation. Every external MP conclusion is a subformula of the copied template's final implication, so needs no larger record bound. Generated records contribute at most R S_j P_j nodes, imported records exactly K_j, and the final endpoint header at most S_j P_j: for h=0 this endpoint is the instantiated antecedent G→E(A,B) of any guarded template, which gives the same header estimate. This proves the complete node allowance K_j+(R+1)S_j P_j and the per-record bound.

Each ASCII payload occurrence costs at most B bytes, and a fully parenthesized operator at most three punctuation bytes; B+4 per node is sufficient. Fixed JSON keys/tags/quotes/newlines, at most three substitution keys or two decimal references below J, cost at most F_J per record. Decimal digit lengths are bounded by the binary logarithmic allowance. J+2 copies cover all records, header and framing. Equation (2) therefore pays full formulas, repeated guards/terms/names, substitutions, rules, references and their relocated growth. No dictionary is used: each name is written at each occurrence. Gzip archives preserve strings losslessly; costs remain uncompressed bytes/bits.

Let I≥2 be the full written native input length. Then s,N,K_native,t_native,g_native,B≤O(I); the image doubles nodes at most. For fixed a, 4^(h+1)≤4^(a+1)(s+1)^(2a), R=O_a(log(I+1)), and P_j=O_a(I^(2a+1)). Equation (2) is bounded by C_a I^(2a+3) for a fixed C_a, using log(I+1)=O(I). No exponent depends on G, pi or their depths. Finite parsing, schema matching, literal copying, reconstruction, reference relocation and checking have polynomial bit time in this input/output bound; an iterative tree traversal can replace recursive calls. The bounded Python implementation is not asserted to support every depth on every interpreter. Interpreter recursion/resource limits do not justify removing the arbitrary-depth mathematical input obligation.

### Complete bounded evidence and limitations

Reproduce construction with `python3 scripts/guarded-context/run_suite.py`. The original full certificate is `scripts/guarded-context/output/certificate-180.json`; the supplied and output strings remain in the same directory. Step 182 found that the suite had overwritten its four fixed-template archive names in each format with later growing test outputs. The original library measurements describe the streams checked before that overwrite, not those paths' final contents. The audit below recovers the exact fixed streams under `fixed-<operator>-<side>.<format>.jsonl.gz`, and the corrected suite now uses those distinct paths. The original certificate and growing streams are preserved. Eight cases comprise the identity context, both marked positions of each connective, mixed perfect skeletons of heights two and three, and a height-three mixed case with depth-80 guard, depth-22 marked term and depth-34 unmarked term. Other cases retain unused supplied axioms of depths up to 50, truth/falsehood terms, repeated names and nontrivial commutation/double-negation endpoints. All native/image streams are checked in full against independently reconstructed endpoints; every retained input record/reference is compared, all actual arguments are measured, and native/image correspondence is compared for every output record. Output archive measurements match writer hashes/bytes. This is implementation evidence plus the separate all-size argument above, not a finite-test proof of that argument.

For mixed height three with shallow guard, native/image actual/required lines are 6193/6881, depths 50/50 in each format, and bytes 9429706/419271131454 and 13509592/709161925899. For the deep-payload case, lines are 5498/6880, depths 83/96 and 85/102, and bytes 34800930/3018705725511 and 37833420/4254934107146. The identity case retains all 383 supplied records and depth 42 with no generated records. All line/depth/record/byte/argument bounds pass. The full certificate is complete with an empty failure list.

Ten malformed receptions are rejected: changed endpoint, declared substitution, forward reference, wrong MP antecedent, assumption rule, image input, changed external guard, missing proof, missing mark and two marks. Six complete corrupted packages are preserved; four malformed requests are recorded in the certificate. Image-input rejection here does not by itself test every well-formed independent image proof; the loader's native-header restriction supplies that scope condition. No failed mathematical test is suppressed.

This supplies one conditional L055 section 6 interface, not the guard premises, zero-proof strings, complete receiver or ordinary-input completeness. Certificate existence, arbitrary ER representation, W/V/U and unrestricted SAT decision/separation remain unproved. Existing component proofs and failures are preserved. The component audit below is complete; full receiver verification remains pending and L055 remains an UNVERIFIED CANDIDATE for the conditional receiver only.

### Independent critical audit, 2026-10-12 (step 182)

The unchanged SPECIALIZE assessment `drafts/literature/2026-10-12-guarded-context-critical-audit.md` covers this audit. The primary statements and proof cases above, including their native/database-XOR and source-version qualifications, are reused. No new theorem or source reproof is needed. L056 supplies primitive schemas/substitution and the unguarded XOR strings; L058 supplies the complete import contract. Its balanced-list conclusion is not used here. No L057 theorem, L055 receiver conclusion or cross-notebook result is an input.

**Archive defect and exact recovery.** The original suite checked and loaded the four guarded templates into memory before overwriting each template's native/image path with the correspondingly named growing case. This falsified the claim that those paths still held the fixed proofs, although it did not change the already loaded library or invalidate a primitive inference. The independent auditor `scripts/guarded-context/audit_archives.py` checks the complete surviving L056 congL/congR strings and the two local unguarded AND strings against separately written endpoints. It copies each whole unguarded proof and appends the four ax-1/MP/ax-2/MP records displayed above, using its own schema and record constructors. For each of the eight streams, all uncompressed measurements and the SHA256 digest agree with the original step-180 library entry. Primitive checking against the reconstructed guarded endpoint establishes membership; digest agreement establishes exact recorded-byte recovery, not mathematical validity. The new `fixed-` archives preserve the recovered evidence without replacing any old archive. The suite's fixed output filenames are repaired to prevent recurrence. All eight overwritten paths are separately checked to contain exactly their recorded growing output.

**Complete import and endpoint induction.** Inspection of `load`, `AppendProof.add`, `copy`, the primitive `ax`/`mp`/`sub` methods, the checker, and `Lift.run` confirms the following induction. Reception checks every axiom substitution and strictly earlier MP, both the requested header and last formula, ASCII payloads and duplicate fields. Fresh append-only copying gives the k-th imported record position k and a template record position offset+k; no inherited cache or helper adds a premise. An axiom is reconstructed with its declared substituted fields, and an MP with the relocated earlier antecedent/implication; each result must equal the substituted original formula. Thus unused supplied records are retained and each copied inference is valid. Substitution returns a replacement directly at a schematic variable, so colliding names never cause a second substitution inside a replacement.

At the mark the last imported formula is precisely G→E(U,V). A validated context has exactly one marked child at every ancestor, and its sibling has no mark. If the current terms are A,B and sibling is S, the selected fixed endpoint is (G→E(A,B))→(G→E(op(A,S),op(B,S))) on the left, or its ordered right-position counterpart. The added MP therefore proves the exact enclosing-context endpoint. The earlier guarded theorem is a proof reference, never a term substituted for A, B or S. G is the separate fixed-template argument at every ancestor. Identity context emits nothing beyond the entire supplied proof. This verifies all four orientations, mixed contexts, arbitrary supplied term/guard/proof depths and the actual last record. Literal translation of every formula and substitution preserves the stated translated axiom/MP interface, not arbitrary ordinary-input completeness.

**All-size ledger.** Each ancestor appends exactly its selected library count plus one MP, so the count is N+sum(L_selected+1)≤J. Direct complete checking reproduces L=2165, (D_native,S_native)=(16,1260) and (D_image,S_image)=(22,1776). Every context argument uses a subtree of the original height-h skeleton with U/V or an original unmarked term at its leaves. Native X/P add at most three depth levels; image X/P at most six/four. Thus its depth is at most c_j h+d_j; G retains e_j independently. Substitution into a fixed formula or declared field adds at most max(e_j,c_j h+d_j) to D_j. External MP conclusions are subformulas of the instantiated fixed endpoint. Imported fields retain delta_j, yielding (1), with no dependence on guard depth hidden in h.

The exact X/P node recurrences above imply p_(i+1)≤8+4p_i and hence p_i≤Q_j. Taking P_j=max(g_j,Q_j) therefore bounds every substituted variable, including each separate occurrence of G. For u operator nodes and v variable nodes in a complete fixed record, u+vP_j≤S_jP_j. Generated records contribute at most R S_jP_j, supplied records exactly K_j, and the header at most S_jP_j. In the identity case its formula is the instantiated antecedent of any guarded template, so that header bound still applies. ASCII names and punctuation cost at most B+4 per node; fixed JSON fields and at most three substitution keys or two references below J fit F_J. The J+2 framing allowance gives (2), including all repeated substitutions, names, guard copies and relocated references. Since h≤a ceil(log₂(s+1)) with fixed a, 4^(h+1)≤4^(a+1)(s+1)^(2a), proving the stated fixed polynomial bound in full input length. This argument admits iterative traversals for arbitrary input depth; the finite Python interpreter is not asserted to implement an unbounded recursion stack.

**Full evidence.** Run `python3 scripts/guarded-context/audit_archives.py`; the complete certificate is `scripts/guarded-context/output/audit-182.json`. After recovering/checking the fixed strings, it checks all eight supplied packages and reconstructs every output record independently of the emitter: all formula/substitution fields, every relocated reference, each external MP and the complete event/argument trace. All sixteen native/image output streams match that reconstruction and its literal translation record by record, and pass the primitive checker against independently built context endpoints. Complete input node/depth sums, all canonical parameters and bounds, and every growing argument are recomputed. The actual/required values are those above: in the deepest case 5498/6880 lines, native/image depths 83/96 and 85/102, and bytes 34800930/3018705725511 and 37833420/4254934107146. The identity case retains all 383 records and depth 42. Every saved output measurement agrees.

All six corrupted packages are read in full and differ from the good supplied package in precisely their recorded one header or record; the other four malformed requests are reproduced. The actual receiver rejects all ten with the recorded reasons. Only those final rejection tests import the emitter; output reconstruction does not. The certificate has `complete=true`, eight explicitly recorded repaired archive collisions and no unresolved verification failures. The conditional mathematical argument and bounds survive without a dependency change. This is local verification and evidence repair for known logical operations, not a main-problem advance beyond the checked sources. Guard-premise existence/strings, zero strings, the complete receiver and ordinary-input completeness remain outside the verdict; the stated Mathlib and interpreter qualifications are unchanged.

## Mathlib

Full matching Mathlib coverage for this complete supplied guarded-context compiler and ledger is **not checked**; no absence claim follows. Primary named logical inputs and their native/database/image qualifications are above. Metamath page inspection and Python primitive checks are not Lean verification. This is an implementation/accounting specialization of known laws without certified originality.
