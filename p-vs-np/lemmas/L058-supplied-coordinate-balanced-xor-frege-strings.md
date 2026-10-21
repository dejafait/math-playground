# L058 — Complete supplied-coordinate proofs combined along a balanced XOR tree

## Hypotheses

Supply two ordered lists U_i,V_i, 0≤i<M=2^h, h≥1, of fully written NOT/implication formula trees. Variable payloads are nonempty ASCII alphanumeric/underscore strings; arbitrary finite identifiers require a paid injective encoding first. Let

    X(A,B)=((A→B)→NOT(B→A)), E(A,B)=NOT X(A,B).

Every occurrence of these abbreviations is literally expanded. B_M is the perfect ordered binary X tree. For each i supply a **complete assumption-free native proof** pi_i whose exact last formula and declared endpoint are E(U_i,V_i). Only ax-1/2/3 and MP, with the schemas specified in L056, are allowed. Every formula, axiom substitution field and strictly earlier MP reference is written. A semantic equivalence, theorem label, supplied premise, omitted derivation or externally populated proof cache is not a proof package. Coincident names and repeated terms are allowed.

The literal image tau sends NOT A to NOT tau(A), and A→B to NOT tau(A) OR tau(B), retaining all double negations. Native proofs are supplied; arbitrary independently supplied NOT/OR proofs are outside this interface. All costs below concern **uncompressed** complete records, including unused supplied lines. The input is the complete package of terms and proof strings, not just the number of coordinates or endpoint lengths.

Let N be the sum of all supplied proof line counts. For each format j=native,image, let t_j≥1,d_j bound nodes/depth of every written U_i,V_i; let K_j be the sum of nodes of all supplied proof records after literal translation to format j, including every declared substitution field; and let delta_j be their maximum formula/substitution depth. Let B≥1 bound every raw variable payload, including fixed template auxiliary names. These are actual full-input measurements, not semantic or endpoint-only estimates. The supplied proof headers, term/name data and framing also count toward the complete input length.

No claim that such pi_i exist with small length is assumed beyond the explicitly supplied inputs. L055 is downstream motivation, not a premise; no IPS identities, formal-zero promise, fixed-a premise or certificate-existence assumption is needed here.

## Conclusion

There is a deterministic complete-record construction of a native primitive proof of

    E(B_M(U),B_M(V)),

and its line-by-line literal NOT/OR image in the translated axiom/MP calculus. The importer checks every complete native pi_i against the externally reconstructed exact coordinate endpoint. It uses fresh append-only state, explicitly relocates every reference and retains every supplied line, including unused deep lines. It uses no proof supplied through a cache. The output contains no formula DAG abbreviation, extension variable, semantic checking rule or unpaid logical law.

Use L056's already checked conservative library constants

    L=3470,
    (D_native,S_native,c_native)=(18,2456,3),
    (D_image,S_image,c_image)=(25,3492,6).

Here S_j counts all formula and axiom-substitution nodes per fixed record. Set

    G=(M−1)(3L+4), J=N+G,
    P_j=8·4^(h+1)(t_j+1)=32 M²(t_j+1),
    F_J=256+64 ceil(log₂(J+2)).

The output has at most J primitive lines, depth at most

    max(delta_j, D_j+c_j h+d_j),                         (1)

and at most max(K_j,S_j P_j) nodes in any complete record. Its uncompressed bytes are at most

    (B+4)[K_j+(G+1)S_j P_j]+(J+2)F_J.                  (2)

Full binary length is eight times (2). Construction and checking admit polynomial bit time in the complete supplied input. In particular, the depth retains the maximum supplied proof depth; it does not multiply that depth by M. With shallow terms/proofs, the added list-context depth is O(log M). These informal all-size bounds and the complete archived evidence passed the separate step-178 critical audit below. This is reproduction/accounting of known logical operations, without certified originality, a whole-receiver certification or a P-versus-NP conclusion.

## Proof

### Imported logical laws and justified specialization

Reuse L056's checked fixed primitive strings for congL, congR and trans, and its primitive-basis/substitution argument, with the step-170 cache qualification. The precise classical schemas are [Metamath ax-1](https://us.metamath.org/mpeuni/ax-1.html), A→(B→A); [ax-2](https://us.metamath.org/mpeuni/ax-2.html), (A→(B→C))→((A→B)→(A→C)); [ax-3](https://us.metamath.org/mpeuni/ax-3.html), (NOT A→NOT B)→(B→A); and [ax-mp](https://us.metamath.org/mpeuni/ax-mp.html), from A and A→B infer B. L056 preserves the retrieved 2026-10-11 source statements/snapshots and the qualification that these are not a pinned set.mm revision. No completeness theorem for growing inputs or theorem-level reproof is needed here.

The exact two-premise semantic interface is [Metamath xorbi12i](https://us.metamath.org/mpeuni/xorbi12i.html): from A IFF B and C IFF D infer (A XOR C) IFF (B XOR D), for arbitrary wffs. Its complete seven-step displayed proof and both hypotheses were inspected in the unchanged SPECIALIZE start assessment `drafts/literature/2026-10-11-balanced-coordinate-combination.md`, on 2026-10-12; the page records contribution 4-Sep-2016 and shortening 21-Apr-2024. Its database XOR expansion differs from native X by double negation. Therefore its label and definition axioms are not emitted as primitive rules. The paid native congL/congR/trans strings implement the interface literally. No new fixed proof is synthesized, and no source theorem is reproved as a new mathematical result. The justified specialization is complete package validation/copying and its ledger, which the inspected theorem does not supply.

The unchanged `scripts/balanced-slot/checker.py` reparses every serialized formula, matches precisely these three schemas with consistent repeated substitutions, compares every declared substitution and requires MP's exact antecedent/consequent with strictly earlier integer references. Its final comparison checks a requested literal endpoint. Induction on records gives native proof membership. The same induction in the literal image gives membership in the translated calculus, since implication has the same Boolean interpretation as NOT(left) OR right. This does not establish an arbitrary ordinary-input normalization interface or completeness in every ordinary Frege presentation.

### Complete import and reference relocation

`scripts/balanced-coordinate/aggregate.py` first reconstructs each exact E(U_i,V_i), independently checks the entire supplied package against it and parses all records, retaining unused lines. It enforces the native header, primitive record fields, nonempty ASCII payloads and strictly earlier references; duplicate JSON fields are rejected. The second read explicitly checks endpoint/reference structure and last formula as well. A full-byte SHA256 comparison records stability across the reads; hash agreement is an integrity measurement, not a mathematical proof rule. Every copied axiom/MP is reconstructed below, so primitive membership is not inferred merely from a hash.

Start with an empty append-only proof store, without synthesizer helpers or earlier requests. Copy pi_i's axiom records by their declared native substitutions. If its k-th record is MP from p,q<k, relocate those references to their copied earlier positions. With append-only copying, a package beginning at offset s maps k to s+k; there is no deduplication or pruning. Reconstruct each inference and require that its conclusion is literally the supplied formula. Axioms are actual schema instances and MPs use exact earlier formulas; induction proves every copied record. The copied final coordinate conclusion is exact. Thus reception cannot obtain an equality from an unpaid supplied assumption. Every input proof is copied once and all N lines, arbitrary depths and names are charged.

Uniform simultaneous substitution into a checked fixed template preserves each axiom instance and MP. Its replacement formulas are not recursively resubstituted, so collisions among input names and schematic/auxiliary names create no binding or freshness issue. Copy every template record with an explicit map of its earlier references. Fixed auxiliary variables left unreplaced remain paid ordinary free variables. The aggregation state has no external cache; the L057 step-174 fresh-state qualification motivates this choice but its distribution theorem is not a mathematical input.

### Bottom-up balanced combination and exact endpoint

At a leaf, use its already imported E(U_i,V_i). At a binary node suppose the two child endpoints are E(A,B) and E(C,D), where A,C are the actual left/right U subtrees and B,D are the corresponding V subtrees. Copy the fixed congL instance and apply MP to obtain

    E(X(A,C),X(B,C)).

Copy congR with its first/second arguments C,D and fixed left operand B; apply the second child equivalence by MP to obtain

    E(X(B,C),X(B,D)).

Copy trans with its three term arguments X(A,C), X(B,C), X(B,D), and use two MPs with these two established equivalences. Its conclusion is exactly E(X(A,C),X(B,D)). This pays three whole fixed proofs and four external MPs. The child proofs are referenced as earlier lines; neither their proof text nor their equivalence formula becomes a substituted term argument.

Induction on perfect subtree height preserves both contiguous order and the paired list split. Processing children before their parent gives exactly M−1 internal nodes and final endpoint E(B_M(U),B_M(V)). All references are earlier. A fresh append-only final MP makes that endpoint the actual last output record. Terms that themselves spell XOR, constants written as q→q or NOT(q→q), repeated terms and coincident names are opaque input trees for this structural induction; their complete expansions still count below. No permutation, padding, variable renaming or semantic normalization is performed.

### All-size copying, depth and binary ledger

Import costs N lines. Each of M−1 internal nodes costs at most 3L+4, proving J. The actual reused fixed counts are 2161,2161,1449, so the present unpruned implementation uses precisely N+5775(M−1) lines; L056's full-library L is a conservative common majorant, not a fitted test constant.

Every growing template argument is a U/V subtree or one mixed tree X(B,C), alongside X(A,C) and X(B,D). All have balanced skeleton height at most h above supplied terms. No argument contains an earlier E proof. Native X adds at most three depth levels per skeleton level; its image adds at most six. A fixed line/substitution of depth at most D_j therefore has instantiated depth at most D_j+c_j h+d_j. Added MP conclusions are subformulas of these copied implications and obey the same bound. Imported records retain precisely their actual depth, at most delta_j, proving (1) even with arbitrarily deep unused input lines. Header depth is the final formula's depth and is already covered.

Expanded native X has 4+2|A|+2|B| nodes; its image has 7+2|tau(A)|+2|tau(B)|. Thus a height-i argument has nodes bounded by p_0=t_j and p_(i+1)≤8+4p_i. Explicitly

    p_i≤4^i t_j+8(4^i−1)/3≤8·4^(h+1)(t_j+1)=P_j,

for i≤h. If a fixed record has s operator nodes and v variable occurrences, counting its declared substitution fields too, its copied nodes are at most s+vP_j≤S_j P_j. Additional MP records are subformulas of the copied laws and need no larger majorant. The G generated records therefore have total nodes at most G S_j P_j. Imported records have total exactly K_j, so each has at most K_j; the overall endpoint header needs at most S_j P_j. This proves the per-record bound and total formula/substitution-node allowance K_j+(G+1)S_j P_j.

ASCII payloads cost at most B bytes per occurrence and fully parenthesized operators at most three punctuation bytes per node; B+4 per node suffices. Each serialized record has a fixed rule tag, either at most three substitution keys or two decimal reference fields, and fixed JSON framing/newline. With every reference less than J, F_J pays this framing and relocation growth; decimal digit length is bounded by the binary logarithmic allowance. J+2 records cover all lines and the endpoint header with slack. This proves (2), including all retained unused records, axiom substitutions, repeated term/name copies and reference growth. Original input headers and request data contribute to input size even though output uses a new header; none is treated as a free oracle or implicit dictionary. No separate symbol dictionary is required because every name occurrence is literal and paid.

Let C be the total uncompressed supplied native proof bytes and W the bytes of all written U_i,V_i and request framing. Then N,K_native,B≤C+W+O(1), t_native≤C+W+O(1); literal translation adds just one NOT node per implication, so K_image≤2K_native and t_image≤2t_native. G=O(M) and P_j=O(M²(t_j+1)); references cost O(log(N+M+2)). Thus (2) is one fixed polynomial in M+C+W, with no hidden exponent depending on pi_i or its depth. The fixed library has constant cost. Complete parsing, validation, reference relocation, tree copying, serialization and the exact recursive traversal take polynomial bit time in that input/output majorant. This is an abstract finite algorithm; the Python implementation is not asserted to support every depth on every interpreter. Its recursion/resource limitations are not an omitted mathematical hypothesis of the copying construction.

### Bounded complete evidence and remaining limits

Reproduce with `python3 scripts/balanced-coordinate/run_suite.py`. The full certificate is `scripts/balanced-coordinate/output/certificate-176.json`. Every supplied package and every generated native/image proof is checked in full, against endpoints rebuilt by `endpoints.py`, which imports no emitter/planner. Complete input retention and offset relocation are compared record by record. All actual growing arguments are measured, not sampled. Lossless gzip archives retain complete strings; every reported Frege cost is uncompressed bytes, and output writer/checker hashes and byte counts match.

Cases M=2,4,8 include nontrivial commutation/double-negation coordinate proofs, repeated and coincident A/B/C/q names, truth/falsehood formulas, unequal supplied proof lengths and unused deep axiom records. Those coordinate proofs are bounded test inputs constructed from already checked fixed strings; this is no arbitrary-coordinate proof finder. Actual/required line counts are 7442/12081, 19632/33549 and 43046/75519 in both formats. Native depths are 26/26, 23/27, 32/32; image depths are 28/35, 32/41, 34/45. Native actual/required bytes are 6469854/147351250496, 32384683/1767968176250, 67905086/7333578511124. Image bytes are 9781395/279330466951, 49566646/3351613857625, 103075694/10427015805044. These deliberately loose fixed majorants are polynomial thresholds, not practical performance or optimality claims.

Eight reception tests reject changed coordinate endpoint, declared axiom substitution, forward reference, wrong MP antecedent, an assumption rule, image-format input, a missing coordinate proof and a mismatched external requested coordinate. Six corrupted complete package archives are retained; the remaining two are malformed requests recorded in the certificate. All six generated proof streams pass, as do their node/depth/line/byte and actual argument bounds; full results, input measurements, reference offsets and failure fields are in the certificate. Finite success tests the implementation; the separate all-size argument above supplies the bound. The step-178 independent audit is recorded next.

This supplies only L055's coordinate-combination interface. Zero/guard strings, ordinary-input normalization/completeness, the complete receiver audit, certificate existence, arbitrary ER representation, W/V/U and unrestricted SAT decision/separation remain open. No progress beyond the checked logical laws on the main problem and no certified originality is claimed.

### Independent critical audit, 2026-10-12 (step 178)

The unchanged SPECIALIZE assessment `drafts/literature/2026-10-12-balanced-coordinate-critical-audit.md` covers this audit. It reuses the precise primary logical inputs above and L056's primitive strings. No additional source theorem or theorem-level reproof is needed. The complete importer, endpoint builder and suite, the complete primitive checker and the used `Proof.ax`, `Proof.mp`, `sub` and append-only methods were inspected. L057's prior cache qualification is a comparison only; L056 remains the sole local mathematical input.

**Import and inference induction.** The first pass checks every native axiom and MP against the requested coordinate endpoint. The second pass rejects duplicate JSON fields, nonnative headers, invalid record keys, non-ASCII variable payloads and references that are not strictly earlier integers. `AppendProof.add` bypasses inherited deduplication, and copying uses only `ax` and `mp`, not the inherited synthesizer or instance caches. Starting at s, the k-th copied record is therefore exactly s+k. Reconstructed axioms have the supplied schema substitutions; reconstructed MPs use the relocated earlier antecedent and implication. The explicit comparison with the supplied formula closes this induction record by record, including unused records. Hashes detect file changes between reads; proof membership comes from checking/reconstructing each inference, not a digest. The fixed-library hypothesis is essential: arbitrary caller-provided library dictionaries are not covered.

For a fixed-template copy, `sub` returns the replacement tree at a variable and does not recurse into that replacement. Thus substitution is simultaneous even when replacement names include A, B, C or q. Each original axiom instance remains an instance with the correspondingly substituted fields; each MP retains literal antecedent and consequent equality. Unreplaced auxiliary names are paid free variables, with no freshness requirement in propositional syntax. At an internal node the two child proofs give precisely E(A,B), E(C,D). CongL gives E(X(A,C),X(B,C)), congR with arguments C,D,B gives E(X(B,C),X(B,D)), and trans with arguments X(A,C),X(B,C),X(B,D) yields the parent. Both premises are actual earlier lines. This checks orientation, coordinate order and the final endpoint, without substituting a child equivalence into a term. The last of the four MPs is the actual final record; it is already included in the count, not an additional fifth MP.

**All-size ledger.** Each internal node appends 2161+2161+1449+4=5775 lines, so the exact count N+5775(M−1) is below J=N+(3L+4)(M−1). All seven recorded arguments at a node are either child trees or one-level combinations of them; their balanced skeleton heights are at most h. Native X contributes at most three levels and its literal image at most six, while its node recurrences are respectively 4+2p+2q and 7+2p+2q. Hence p_(i+1)≤8+4p_i gives the claimed P_j. Fixed-template substitution adds at most c_j h+d_j to D_j and multiplies its complete record-node bound by at most P_j. Every external MP conclusion is a subformula of an instantiated implication. All declared substitution fields occur within their axiom conclusion, so the checker's maximum formula depth also bounds these fields; their nodes are separately counted in S_j and K_j. Imported records retain depth delta_j independently of M, proving (1). The final header repeats an already bounded conclusion.

There are at most G generated records, plus that header. Imported records contribute exactly K_j nodes, regardless of whether they are used. Thus their total formula/substitution allowance is K_j+(G+1)S_jP_j. The serializer writes every ASCII name occurrence and at most three punctuation bytes per operator; B+4 per node suffices without string escapes under the payload hypothesis. Apart from those formula strings, each record has fixed keys/tags and at most three substitution keys or two decimal references below J. The stated F_J exceeds their framing plus reference lengths, and J+2 copies cover all records/header. This proves (2), including offset growth, and a per-record bound follows by taking max(K_j,S_jP_j). Since all supplied terms, proof records, identifiers and coordinate entries are explicit input, M,N,K_native,t_native,B are bounded by the full input length up to fixed constants. Literal translation at most doubles node counts; G is linear and P_j quadratic in M times t_j+1. Consequently the bit-length and copying/checking-time bounds have one fixed polynomial exponent. Particular Python recursion/resource limits remain outside the abstract all-size algorithm's guarantee.

**Complete independent archive evidence.** Run `python3 scripts/balanced-coordinate/audit_archives.py`; the full certificate is `scripts/balanced-coordinate/output/audit-178.json`. It checks all six native/image congL/congR/trans streams against independently written endpoints, verifies their literal-image correspondence and bounds, and rechecks all fourteen complete supplied coordinate packages. It independently reconstructs every native output record from these archives, including each substituted formula/field, relocated reference and external MP, without importing the emitter. Both format streams are compared record by record with this reconstruction and its literal image, then fully checked by the primitive checker against independently reconstructed list endpoints. All import offsets, complete event traces and actual growing arguments agree. Only the final malformed-reception tests import `aggregate`; no emitted evidence depends on trusting that emitter.

Every saved measurement and uncompressed hash matches. The six line/depth/byte thresholds are those in the bounded-evidence section above. In particular M=8 has 43046/75519 lines in each format, native/image depths 32/32 and 34/45, and bytes 67905086/7333578511124 and 103075694/10427015805044 (actual/required). Complete reconstruction also confirms the retained unused deep record rather than sampling it. All six malformed archives differ from their accepted source in exactly the intended one record or header; the assumption-rule corruption changes both the rule and removal of its substitution field. The actual importer rejects all six again with the saved reasons, as well as both malformed requests. The image-input corruption is rejected for native syntax under its changed header; this test alone is not a test of every well-formed image input, whereas the importer's explicit native-header condition supplies that interface restriction.

The full audit certificate is complete with no failures. No substantive mathematical error was found and no bound or dependency changes are required. This verifies a conditional local component reproducing known logical laws; it neither supplies arbitrary short coordinate proofs nor establishes ordinary NOT/OR-input completeness, full receiver strings, certificate existence or any unrestricted SAT conclusion. Mathlib and interpreter qualifications remain unchanged.

## Mathlib

Full matching Mathlib coverage for this exact complete-package compiler and binary ledger is **not checked**; no absence claim is made. Precise primary logical citations and the native/literal-image qualifications are above. Metamath page inspection, Python primitive checks and this informal argument are not Lean verification. The local result is an implementation/reproduction of known equivalence congruence and composition, with a supplied-input accounting specialization.
