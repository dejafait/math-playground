# L067 — Exact-length coefficient tables from an actual zero tree

## Hypotheses

Supply exactly the source syntax of `scripts/actual-tree/build.py:validate_input`: an explicit ordered F₂ arithmetic occurrence tree with `add`, `mul`, `zero`, `one` and indexed `var` leaves, an ordered ASCII letter-name dictionary, one ASCII q, and a Boolean zero-edge deletion convention. All letter names must be pairwise distinct. Repeated occurrences of the same indexed letter and unused dictionary entries are allowed. q may coincide with a letter: q is only a logical template parameter, not an additional formal generator. Fix a positive integer depth factor a, default 4, and require the implementation's admission d ≤ a·bit_length(U+1), where U is the occurrence-node count. This implies L066's d ≤ a ceil(log₂(U+2)).

The polynomial computed by the tree is promised zero in the **free noncommutative F₂ algebra** on its dictionary letters. Boolean vanishing or commutative vanishing is insufficient. No separately supplied graph, suffix, bit matrix, proof occurrence, identity oracle or proof-string cache is input. In particular this statement does not retain optional L066 proof occurrences: they are outside this constructor's input syntax.

Let Q be the byte length of the complete original compact ASCII JSON source, excluding generated tables. All encodings and a are fixed for the polynomial bound.

## Conclusion

`scripts/coefficient-chain/construct.py:construct` constructs L066's actual graph, N=2U written native suffixes and L065's finite left-closure tables beta, G_b. It returns N+1 dimensioned levels R_i with k_i≤N, R_0=[e_source] (source index 0), and exactly R_N=[] with k_N=0 and T_N=[]. Every R_i is a row basis of the exact-length space

    V_i = span{e_source G_(b1)...G_(bi) : b1,...,bi are dictionary positions}.

For every nonterminal indexed row j and letter b it returns T_(i,j,b) as a literal 1-by-k_(i+1) matrix, satisfying

    (R_i)_j beta=0,   (R_i)_j G_b=T_(i,j,b)R_(i+1).

These are L064's table and fixed-term fields in its exact receiving syntax; complete coordinate proof packages are **not** returned. Earlier empty spaces stay empty, even for n=0. No zero-row padding replaces an empty space.

Basis bits total at most (N+1)N²; transition bits total at most nN³. A deliberately loose full compact certificate bound is 2³⁰(Q+2)^(4a+12) bytes, including source, graph, adjacency, closure, fixed suffixes, chain tables, dimensions and ledger. Abstract construction and complete finite checking take polynomial bit time for fixed a. Python recursion/resource limits remain implementation qualifications. This is an implementation/reproduction of the existing L055 section 3 adaptation, without certified novelty. The separate step-230 critical audit below found no defect in this mathematical contract; it repaired incomplete diagnostic-ledger validation in the checker.

## Proof

### Imported scope and source reconstruction

The prior SPECIALIZE assessment is `drafts/literature/2026-10-14-actual-tree-coefficient-chain-tables.md`. The standard basis/coordinate mechanism is inspected in Stefan Kiefer, *Notes on Equivalence and Minimization of Weighted Automata*, [arXiv:2009.01217v1](https://arxiv.org/pdf/2009.01217v1), Algorithms 1–2, Propositions 2.1–2.2 and 3.1, printed pp.1–5; the layerwise analogue is Li–Tzameret–Wang, *Characterizing Propositional Proofs as Non-Commutative Formulas*, [arXiv:1412.8746v4](https://arxiv.org/pdf/1412.8746v4), Definition 4.13 and Lemma 4.15, printed pp.32–35. Kiefer's cumulative spaces and LTW's homogeneous linear-edge graph are not imported verbatim for this mixed-degree graph. L055 section 3 already supplies the exact-length adaptation and word-coefficient argument; this proof verifies its implementation and receiving specialization rather than reproving PIT.

L066 supplies the occurrence graph and fixed suffix construction, including zero leaves, constant connectors and the distinct root entry/exit. Its source validation is invoked before construction; aliases are explicitly rejected. The returned adjacency is reconstructed from that source, never supplied as independent trusted data. L065 supplies the left orientation

    K=I+E0+...+E0^(N-1),  beta=K e_terminal,  G_b=K E_b.

The implementation calls the existing finite closure request. All graph matrices are strictly upper triangular, so each G_b is strictly upper triangular. The independent checker reconstructs the graph/suffix endpoints using `scripts/actual-tree/verify.py:contract` and recomputes K instead by descending rows K_v=e_v+Σ_(j>v)(E0)_(v,j)K_j. This acyclic recurrence has a unique solution and equals the finite power sum. It then compares all entries of K, beta and G to the certificate.

### Exact-length elimination and coordinates

Start with the single nonzero source unit row. At stage i list every rG_b for the current basis rows r and dictionary positions b, in row-then-letter order, without retaining earlier-length rows. The routine `basis` reduces each candidate by the existing pivot rows in increasing pivot order. Each pivot row is nonzero, has first 1 at its pivot and zeros in all earlier columns. Reduction preserves the span of the candidates together with selected rows; a zero residue adds nothing, and a nonzero residue has a new pivot and is added. Adding a new earlier pivot preserves the echelon property of existing rows because they already vanish before their own later pivots. Thus the final sorted pivot rows are independent and span exactly the candidate rows. There are at most N such rows. They may be linear combinations of word rows; they need no individual word label.

Inductively their span is V_(i+1): every length-(i+1) word row is a length-i word row times one G_b and hence in the candidate span; conversely every candidate is a linear combination of such rows by distributivity. There is no cumulative-basis assertion.

`coordinates` reduces each candidate against that sorted next basis, recording the residue's pivot bit at each step. The invariant is original row = current residue + sum of recorded bits times the already visited basis rows. Later rows have zero earlier pivot columns, so elimination cannot undo a cleared pivot. Since the candidate is in the basis span, the final residue is zero; otherwise construction rejects. The recorded vector, wrapped as one matrix row even when empty, is exactly the required T_(i,j,b).

L055 equation (4) identifies e_source G_w beta with the coefficient of w, by the unique splitting of a path at its letter edges, including constant-only and empty-word paths. Distinct dictionary names ensure positional words are precisely free-algebra words; aliases would invalidate this step. Formal zero therefore implies all V_i annihilate beta. The constructor checks each basis row before exporting the level and rejects any failed check. A product of N strict upper triangular N-by-N matrices is zero, since a nonzero contribution would require N strict index increases. Hence V_N=0 and the computed terminal basis must be empty. An earlier empty basis produces no candidates, no T rows and an empty next basis; n=0 therefore gives empty spaces from level 1 onward. Source index 0 follows from the graph construction, independently compared by the checker.

The checker performs a separate column-pivot rank calculation on every full candidate list, comparing rank(candidates)=k_next=rank(candidates concatenated with R_next). Together with the next rows' independence this checks both span containments without trusting `basis` or `coordinates`. It checks each literal transition matrix equality and annihilation entry, and invokes `scripts/backward-zero/chain.py:validate` on the entire returned chain, including all term, level, row and bit fields. No Frege proof is inferred from a bit calculation: L064 still needs its actual coordinate proof packages.

### Original-source ledger

The source JSON has Q≥4(U+1), Q≥n, and maximum payload length B≤Q, by literal syntax and dictionary framing. Also N=2U≤2Q. The admission gives

    4^(2d) ≤ (2(U+1))^(4a) ≤ (Q+2)^(4a).

L066's continuation geometry bounds each arithmetic suffix height by 2d+1. Its native X/P expansion satisfies p_(h+1)≤8+4p_h with leaf node count at most 5, so 48·4^(2d+2) is a sufficient node bound for one written suffix. Allowing B+4 bytes per node and summing N suffixes bounds all suffix bytes by 2¹⁴(Q+2)^(4a+2). No recursively generated coefficient proof is used to define this bound.

There are at most (n+1)N² adjacency bits, N² closure bits, nN² G bits and N beta bits. There are N+1 levels with at most N rows each, giving at most (N+1)N² basis bits and N stages with at most nN² transition bits apiece, giving nN³. Each literal bit is a one-digit JSON integer; commas, brackets, row/level/letter fields and decimal dimensions contribute at most a polynomial of degree six in Q+2. The graph has at most 4U edges, with indices costing O(log(Q+2)) bytes, and the full source is retained once. Framing the finite fixed set of ledger fields, including the bound's decimal integer with O(a log(Q+2)) digits, is also polynomial. For positive integer a its linear factor is absorbed by (Q+2)^(4a). These quantities fit the generous uniform 2³⁰(Q+2)^(4a+12) bound; even duplicating all table metadata once fits its slack. The implementation computes the actual compact certificate byte count to a fixed point after inserting that count and checks it against the bound. The trailing newline in an archived file is outside this compact count and fits the same bound with its large slack.

Closure by N dense multiplications costs O((n+1)N⁴) bit operations. Each stage has at most nN candidates; reduction and coordinate extraction use O(N²) bit operations per candidate, so N stages cost O((n+1)N⁴). Storing these lists is polynomial; no word enumeration occurs in the all-size algorithm. The independent rank and literal matrix checks have polynomially many bit operations. Repeated exact endpoint construction, parsing and serialization in the reused receiving routines involve balanced lists over polynomially many terms and the fixed written suffixes; their explicit X expansion adds only a polynomial list-size factor. Therefore even these unsimplified checks and decimal/framing operations have polynomial bit time. This is an abstract finite algorithm claim, not an all-input Python runtime guarantee.

### Complete bounded evidence and limits

Reproduction command: `python3 scripts/coefficient-chain/check.py`. Full certificates and full finite checks, also reread from disk, are in `scripts/coefficient-chain/output/{empty,constants,variable,mixed}.json`; complete measurements/rejections are in `scripts/coefficient-chain/output/results.json`. Every fixture additionally uses independent explicit free-word tree expansion and compares every exact-length word-row span to R_i, through all N+1 levels. That bounded enumeration is excluded from the constructor and from the all-size algorithmic claim.

The fixtures are 0 over an empty alphabet, 1+1 over an empty alphabet, xy+xy with an unused listed letter, and (1+x)+(x+1) with unused letters. Their initial dimensions respectively are (1,0), (1,0), (1,1,1,0) and (1,1,0), followed by zeros through level N. Their complete compact sizes are 753, 1366, 5660 and 5728 bytes. The variable case has 42 basis bits and 6 T bits, against maxima 2940 and 8232. The checker rejects nonzero 1 and x, Boolean-only x²+x, commutative-only xy+yx, and aliased positional x+x, as well as five certificates corrupted at the source row, terminal dimension, transition, closure or graph. No failed mathematical check remains. An initial Python module-name collision was repaired by naming the new constructor `construct.py`; it supplies no mathematical evidence.

The fixtures do not replace the all-size argument. This result fills only the coefficient-table input. It creates no coordinate or chain strings, initial-output identification, ordinary-input normalization, complete L055 receiver, certificate existence, ER representation, W/V/U premise or SAT conclusion. L055 remains an UNVERIFIED CANDIDATE at its separate conditional-receiver level; P versus NP remains unresolved.

### Independent critical audit, 2026-10-14 (step 230)

The unchanged SPECIALIZE assessment `drafts/literature/2026-10-14-coefficient-table-critical-audit.md` covers this REPRODUCTION proof audit. The precise Kiefer/LTW imports above and L065's Mohri acyclic specialization are reused; no new external theorem or PIT reproof is claimed. The complete constructor/checker, actual-source reconstruction, finite closure and L064 table validator were inspected against L055 section 3 and the relevant L064–L066 hypotheses. No additional mathematical input or DAG edge is required.

**Elimination and exact lengths.** A later candidate can have a pivot earlier than an existing pivot. Reducing by sorted old pivots still clears all their pivot positions: a row whose pivot is p is zero in every column below p, so later eliminations cannot change an already cleared earlier position. The new nonzero residue has a pivot outside the old set. Every older row with a larger pivot is already zero at the new earlier pivot. Sorting the updated rows therefore preserves the echelon invariant; backward reduction to reduced echelon form is unnecessary. Their leading positions prove independence, and adjoining a residue preserves the span of all processed candidates. The coordinate routine's residual invariant then gives the exact represented row, including the unique empty coordinate vector for a zero row in a zero-dimensional next space. At each level the candidate list consists only of the present basis times each G_b. Right multiplication is linear, so the span is exactly the next length, without mixing earlier lengths. This checks the all-size induction rather than inferring it from fixtures.

**Source and reception.** The actual graph has source 0, terminal N−1, N=2U≥2 and strictly increasing edges, including all addition/product connectors. Zero edges contribute no adjacency bit for either retention convention. The independent source contract reconstructs all edges, suffix strings and adjacency entries, not merely an output value. The downward recurrence for K and the producer's power sum agree by the unique triangular equation K=I+E₀K. Consequently G_b=KE_b and beta=Ke_t have the same left orientation as L055 equation (4). Splitting paths before each variable edge retains both the final constant segment and the empty word. Distinct names identify positional words with the formal alphabet; q coinciding with a letter changes neither the formal alphabet nor the tautology Y. Formal zero, not Boolean or commutative zero, supplies annihilation. Products of N strictly triangular matrices vanish, giving exactly zero rows at level N; an earlier empty space remains empty. The checker checks both span inclusions by rank, every annihilation entry and every transition product. L064 additionally checks literal bit types and every dimension. A nonempty current level with empty next space has T entries `[[]]`; an empty current level has no T entries. The terminal is exactly `{k:0,R:[],T:[]}`. This is table reception only: no coordinate proof or chain is inferred.

**Original-source accounting.** Put z=Q+2. Explicit source syntax gives Q≥4(U+1), n≤Q, B≤Q and N≤2Q. The admission and bit-length inequality imply 4^(2d)≤(2(U+1))^(4a)≤z^(4a). The actual continuation follows at most d ancestors and then one subtree of depth at most d, so suffix skeleton height is at most 2d+1. Native expansion obeys p_(h+1)≤8+4p_h, p_0≤5; hence the stated 48·4^(2d+2) bound is conservative. Each written node costs at most B+4 ASCII bytes. Both copies of the suffix list, in adjacency and chain, fit 2¹⁵z^(4a+2), with string/array delimiters paid separately. No names require JSON escaping under the admitted payload syntax.

The adjacency/K/G/beta/R/T scalar-bit counts are respectively at most (n+1)N², N², nN², N, (N+1)N² and nN³. Their nested arrays have bounded nesting depth and polynomially many containers even when their innermost rows are empty; in particular each of the at most nN² empty T wrappers is still counted. A coarse 2¹⁰z⁴ bound pays all finite table entries, containers, graph records, level records and fixed ledger fields. Excluding suffix strings and the special large integers below, allowing 2⁶z² bytes per such record/entry more than pays its punctuation, fixed keys and decimal indices. Thus 2¹⁶z⁶ suffices for this ordinary metadata, source/name copies included. The bound integer has at most 11+(4a+12)log₁₀z decimal digits, bounded by 32(a+1)z; the two copies of a cost at most 2(a+1) further digits. Since a is positive and fixed, a+1≤2z^(4a); these charges fit the unused slack in the stated bound. They do not make a part of the original source length or claim a uniform polynomial for varying a.

There is no circular byte estimate. Let A be the length of the entire compact certificate with the `certificate_bytes` field present but its decimal digits removed. All preceding charges bound A by 2¹⁹z^(4a+6), independently of that field's value. Its fixed-point equation is s=A+digits(s). The initial counter is at most A; the iteration is monotone and bounded by 2A because A≥2 and digits(2A)≤A. It therefore stabilizes in at most 2A integer increases, with s≤2²⁰z^(4a+6)<2³⁰z^(4a+12). The one archived newline also fits this strict slack. This supplies the termination and encoding justification separately from the measured sizes. Finite F₂ arithmetic, elimination and rank have polynomially many scalar operations; integer implementations and decimal serialization add at most polynomial bit overhead. Balanced-list expansions in the reused endpoint validators multiply written-suffix size by a polynomial in N,n,k, not by the number of levels in an exponent. Python recursion/memory limits and running assertion-based checkers without optimization remain implementation qualifications.

**Found defect and scoped repair.** Before repair, changing `ledger.U` from 7 to 8 in the full variable fixture retained its byte length and passed `check`. The complete accepted malformed certificate and the original checker's SHA-256 are preserved in `scripts/coefficient-chain/output/audit-230/accepted-wrong-U-before-repair.json` and `before-repair.json`. The omitted equalities concerned diagnostic ledger fields, not the constructor's R/T values or the bound's use of actual source Q. `check.py` now reconstructs and compares every ledger field, requires integer types, checks the exact top-level/ledger field sets, and checks all stored maxima against their formulas. The malformed certificate now fails at `ledger mismatch: U`. No constructor, theorem hypothesis, exponent or historical fixture was changed. This repairs the completeness of the diagnostic checker, not an error in the mathematical table construction.

**Complete evidence.** Run `python3 scripts/coefficient-chain/audit.py`; its full result is `scripts/coefficient-chain/output/audit-230/results.json`. It reads and checks every field of all four original certificates, compares each full object with fresh reconstruction, runs the independent bounded free-word span checks through all N+1 levels, and compares all original reports and all ten rejection results. Historical fixture files are not rewritten. Four explicit row cases include descending newly inserted pivots, a pivot exposed by reduction, duplicate/zero rows and an empty candidate list; full bases, coordinates and explicit spans are saved. Every ordered list of at most four vectors over F₂^N for N=1,2,3 is also tested: 31+341+4681=5053 lists. These finite tests discriminate implementation cases and are not the all-size proof.

Three additional complete source certificates use a=1: duplicated xy+yx with q=x yields dimensions (1,2,2,0,…,0), and retained/deleted zero with an unused letter q gives (1,0,0). Their compact sizes are 15863, 799 and 771 bytes. The rank-two case has 150 basis bits≤27900 and 12 transition bits≤54000; the zero cases each have 2≤12 basis bits and 0≤8 transition bits. Full byte thresholds and all source/graph/suffix/closure/chain fields are saved and checked. The audit also rejects the preserved wrong-U certificate and a separate mutation of each of the fourteen ledger fields, for 25 total rejection checks including the ten original cases. All checks pass with no unresolved failed case. No new primitive proof strings were generated.

The audit is complete at this conditional table-only scope. It supplies no new mathematical theorem or certified originality. L055's proof-string candidate, actual coordinate/chain composition, source-output identification, ordinary-input completeness, certificate existence, ER/W/V/U and unrestricted SAT remain unresolved. The repaired checker and finite evidence do not establish any of those independent claims.

### Preserved empty-zero source-to-chain execution, 2026-10-15 (step 232)

**Hypotheses and imported scope.** This RESEARCH / implementation / REPRODUCTION uses the unchanged SPECIALIZE assessment `drafts/literature/2026-10-14-actual-zero-source-chain-composition.md`. It applies this lemma's checked table construction, L066 steps 216/218, L065 (4) and L064 (1)/(2). The source is exactly `scripts/actual-tree/output/empty-zero-repaired.input.json`: the sole tree `['zero']`, no letters, q=`q`, deleted zero edge, fixed admission a=4, U=1,d=0,N=2,n=0,t=1. The dictionary-distinctness and depth conditions hold. All original optional native occurrences, local pairs and both complete coordinate prefixes are explicit, paid inputs to the appropriate stage. No coordinate is replaced by a theorem label or shortened ancestor subset. The two original optional packages have no separately supplied literal-image files; their images are checked at every occurrence in the complete local/coordinate/chain pairs. Arbitrary independently supplied NOT/OR inputs are not received.

The primary mechanisms remain Kiefer, *Notes on Equivalence and Minimization of Weighted Automata*, arXiv:2009.01217v1, Algorithms 1–2 and Propositions 2.1–2.2/3.1, pp.1–5; Li–Tzameret–Wang, *Characterizing Propositional Proofs as Non-Commutative Formulas*, arXiv:1412.8746v4, Definition 2.3 p.12, Theorem 4.11 proof (15)–(16) pp.30–32, Definition 4.13/Lemma 4.15 pp.32–35 and qualified Lemma 4.17/(22) pp.36–39; and Mohri's acyclic any-semiring closure, *Weighted Automata Algorithms*, author manuscript §6.1, Theorem 4/(28)–(31), pp.21–23, with the IJFCS 13(1):129–143 (2002) Definitions 4–5/Theorem 1 comparison. Direct source links and exact applicability qualifications are in the assessment and the earlier canonical proofs. Their general theorems do not themselves assert this primitive mixed-degree compiler. No semantic closure, PIT, completeness or coefficient-space theorem is reproved here; this is the existing conditional machinery's first joined execution on the preserved source, without a novelty claim.

**Exact table and endpoint application.** Write Y=(q→q), Z=NOT Y. Independent literal reconstruction and the complete table checker give unchanged S₀=P(Z,Y), S₁=Y, K=I₂, beta=(0,1)ᵀ, G=[], and the three levels

    R₀=[[1,0]], T₀=[[]]; R₁=[],T₁=[]; R₂=[],T₂=[].

The dimensions are respectively 1,0,0; no dummy empty-only receiving level replaces these actual source levels. The sole row r=(1,0) has r beta=0 and no letter-transition obligations. Both complete coordinate endpoints are exactly E(P(Z,Y),X(Z,Z)) and E(Y,X(Y,Z)), as in L066 step 216. Thus every L064 hypothesis holds, and its sole requested final endpoint is E(W(r;S),Z)=E(P(Z,Y),Z). This statement identifies the exact written source-row suffix, not the original arithmetic output by an additional theorem.

The fresh append-only store imports coordinate 0 at offset 0 with 122742 records/root 122741, and coordinate 1 at offset 122742 with 238690 records/root 361431. All 361432 records remain, including coordinate 0's entire generated prefix inside coordinate 1; that nested coordinate root is now 245483. The sole generated row occupies indices 361432 through 377086. Its four exact L064 roots are 375610,375631,375633,377086. Every root is checked against independently rebuilt endpoints; the final root is also the registered (level 0,row 0) handle and the actual last record. Backward MP ancestry contains coordinate 0's root 122741. Coordinate 1 is retained and charged even though this row selects only suffix 0. There is no next-row premise at either empty level.

**Complete native/image verification and import implementation.** Run

    PYTHONDONTWRITEBYTECODE=1 python3 scripts/backward-zero/actual_zero_232.py
    PYTHONDONTWRITEBYTECODE=1 python3 scripts/backward-zero/actual_zero_232.py --source-interface-ledger-only

The first command refuses existing destinations. The second is an accounting-only supplement to the completed same-attempt replay, preserving its certificate and proof streams. Full evidence is `scripts/backward-zero/output/actual-zero-232-r1/certificate.json` and `source-interface-ledger.json`; the log is `scripts/backward-zero/output/actual-zero-232-r1.log`. Both certificates have complete=true and failures=[]. Existing source/table/reception archives are untouched.

All thirteen source-law pairs and fifteen closure-law pairs are replayed completely. Both original five-record optional native proofs are reconstructed against their independently written endpoints, including the unused depth-39 record. Both complete local pairs are reconstructed with every optional record and relocated reference compared. Each complete coordinate pair is then reconstructed with all 41143 local records compared after relocation; both actual coordinate EOF roots and the earlier root inside coordinate 1 are checked. A separate full comparison checks all 122742 earlier-prefix record bytes in both formats. No hash or old success flag substitutes for these checks.

The driver represents formulas internally by immutable shared native subtrees, but never deduplicates proof records. `fast_package` checks every header, schema/substitution and strictly earlier MP; its nodes are interned in child-before-parent order. Induction on that order proves that its tuple for each node spells exactly the parsed native tree. Its depth and size statistics count recursively expanded occurrences, including every substitution, rather than distinct interned nodes. Every converted package's full native hash/count/bytes, node sums, depths and payload maximum agree with the independent full paired replay. The bounded immutable representation therefore changes neither received formulas nor their ledger.

`ExactImportChain.copy` specializes only empty-map substitution. Since substitution by the empty map is the identity on every tree (structural induction), it can retain the immutable terms while reconstructing each axiom or MP occurrence and relocating every reference. `AppendProof.add` appends each occurrence; the unchanged `Store.retain` compares every formula, rule, substitution and relocated reference. Nonempty simultaneous substitution, row construction, owned handles and cache discipline use the existing implementation. The paid writer expands every shared subtree into the full formula/substitution string. This avoids redundant allocation, not any mathematical input or copying charge.

The final strict scanner reconstructs every native axiom from its complete declared substitutions and every MP from exact earlier antecedent/implication records. It compares every full literal-image field, both headers, both complete relocated coordinate occurrences and every requested root, reaching EOF in both streams together. Thus transitive comparison retains four occurrences of each original optional package: once in each of two local packages, inside each of two coordinate occurrences. The supplemental location map explicitly records all eight five-record blocks, totalling 40 optional records. Complete earlier generated coordinate records are also retained twice. Writer/scanner full uncompressed measurements agree.

| Format | Complete records | Uncompressed proof bytes | Full formula/substitution depth | Maximum record nodes |
| --- | ---: | ---: | ---: | ---: |
| Native | 377087 | 1072025822 | 39 | 47904 |
| Literal NOT/OR image | 377087 | 1614404612 | 42 | 65372 |

The 15655 generated records prove the exact stated endpoint. Every copied-law argument is measured: maxima are native/image 20/27 nodes and 5/7 depth, and structural height 1≤H=47. The full proofs, imported unused records, substitutions and headers are expanded; compression and interning receive no size credit. Finite success supplements, rather than replaces, L064–L066's existing all-size arguments.

**One original-input ledger.** Keep source, closure and chain library constants separate. Complete replay recovers source L=2567, native/image (D,S)=(18,2040)/(24,2712); closure L=3470, (19,2456)/(27,3492); and chain L=3470, (18,2456)/(25,3492). The original optional/source/library payload majorant is B*=6. Original suffix/Y/Z statistics are t_native=10,d_native=4 and t_image=13,d_image=6. Step 234 corrects the previous prose values 14/5; both preserved executable ledgers already used 13/6. No generated coordinate measurement chooses these parameters.

First recompute L066 (1) from the ten original optional records: J₆₆=5136010 and U₆₆,native/U₆₆,image=5273469255851860176/7010612066620695136. Substitute I≤2J₆₆, K_j≤2U₆₆,j and the source depth limits into L065 (4), exactly as audited in L066 step 218. This gives each complete coordinate at most J₆₅=2796383077672992020 records and source-derived depth limits 167/321; per-coordinate byte bounds U₆₅,j are recorded in the certificate's `closure_source_bound`. Each field's occurrence contributes at least one uncompressed ASCII byte, so receiving both complete prefixes in L064 gives

    I₆₄ ≤ 2J₆₅,
    K₆₄,j ≤ 2U₆₅,j,
    delta₆₄,j ≤ (167 or 321), B ≤ B*.

This counts both complete coordinate occurrences, including all duplicated nested ancestry. There is no prefix discount. Substitute these values into L064 (1)/(2), with the original written suffix statistics and exact supplied table dimensions. Every term is monotone in I,K,delta,B: J and its logarithmic framing increase, as do the maximum/header term and nonnegative byte sum. The independently implemented equations in `audit_chain.bounds` agree with the chain threshold implementation, both for the directly received inputs and these source majorants. Earlier row output sizes never enter the bound.

For m=1,D=5,h=3,V=8192,H=47, G₆₄=5366819334389760000. The source-based complete record bound is 10959585489735744040. Native/image byte bounds are respectively

    77532829592388702507090369634823510260378218973725461504,
    140302967615957169387275466046314788927189819326406127104.

Depth limits are 167/321. L064 (2) pays 69632 location bytes, versus 279 actual bytes; the direct-input location bound is 68608. Every per-format actual line/node/depth/byte inequality passes. These are deliberately loose original-source bounds, not efficiency claims.

The original source file plus optional uncompressed native streams costs 4979 bytes; original optional-path framing adds 158. This differs from L067's source-only Q=57. Fixed source, closure and chain native/image library bytes are separately charged, conservatively paying common laws again. The complete L067 archive is 754 bytes including its newline, below its source-derived bound 2³⁰(57+2)²⁸. The assembled interface is 1203 bytes. Its independent a-priori bound is the sum of original source-file bytes (395), optional-path framing (158), that entire L067 certificate bound, the original coordinate-path list bytes (319), source-bounded locations (69632), and 1024 bytes for fixed outer field names/punctuation. Each interface component is one of these paid objects or a subobject; no measured generated interface size defines this bound. The full proof/location/table/interface/library actual charge is 2735016756 bytes, below the source-derived total

    82591083966083754586895605479257935903677687517503704368615.

For fixed admission a, L066's original-source bounds are fixed polynomials; L065 then applies one fixed polynomial to their explicit majorants, and L064 applies one fixed polynomial to both complete coordinate majorants and L067's polynomially bounded tables. Source suffixes/names, optional depth and all fixed libraries retain the hypotheses of those bounds. The displayed interface bound adds only the L067 polynomial, L064 location polynomial and original strings/constants. Composition and addition of these finitely many fixed polynomials give one polynomial in the original explicit source/optional/library input, with full paths, headers, substitutions, occurrence multiplicity and reference fields paid. This is an application of the existing bounds, not a new unproved output-size estimate. The main certificate's much looser 2¹⁰⁰(Q+2)¹⁰⁰⁰ numerical envelope is only a finite-case diagnostic; the uniform polynomial claim uses this monotone source-based composition and the supplemental a-priori interface bound.

**Preserved failure and verdict.** The first driver stopped after complete coordinate replay, before chain construction, because its name maximum covered fixed libraries but omitted the original optional name `unused`. Its failed certificate and exact pre-repair driver are preserved in `scripts/backward-zero/output/actual-zero-232/`. The repaired bound uses B*=6 from the original optional/source and all libraries, as the reviewed contract already required. The rerun uses fresh destinations; no mathematical hypothesis or previous archive changes. There is no unresolved failed check in the completed integration.

This establishes the approved finite source-row interface by reproduction of existing machinery, without progress beyond the checked sources or a novelty claim. The separate step-234 audit below verifies the new importer, complete streams and composed ledger, correcting one numerical prose error without changing their values. No initial-output identification, nonzero chain, ordinary-input completeness, whole-L055 critical verdict, certificate existence, arbitrary ER representation, W/V/U premise or SAT consequence follows. L055 remains an UNVERIFIED CANDIDATE only at its conditional receiver level. Existing direct DAG inputs already include L064–L066; no dependency changes.

### Independent joined-interface audit, 2026-10-15 (step 234)

**Scope and sources.** This RESEARCH / proof_audit / REPRODUCTION uses the unchanged SPECIALIZE assessment `drafts/literature/2026-10-15-actual-zero-chain-critical-audit.md`. The hypotheses are exactly the step-232 preserved zero source, a=4, N=2,n=0, distinct dictionary names, both complete coordinate prefixes and the original optional packages. Reuse the Kiefer v1 Algorithms 1–2/Propositions 2.1–2.2/3.1, LTW v4 Definition 2.3/Theorem 4.11 (15)–(16)/Definition 4.13/Lemma 4.15/qualified Lemma 4.17, and Mohri acyclic closure citations given above. They support the existing component contracts; none directly certifies this joined primitive implementation. This audit neither reproves nor extends those semantic theorems. L064 step 200 checks supplied chains, L066 step 218 checks source-to-coordinate reception, and step 230 checks tables; none previously checked the changed joined importer and complete output together.

**Immutable conversion and import proof.** The native parser allocates a node only after its children have been parsed or validated as existing nodes. Interning uses full tag/child/name equality. In `fast_package.tree`, induction on the allocation index therefore identifies each variable with its original ASCII name, each negation tuple with the negation of the already identified child, and each implication tuple with its two already identified children. A repeated child is referenced twice in that tuple: its expanded spelling and occurrence count are not contracted. All declared substitution terms receive the same conversion. The `Syntax.node` size recurrence adds both child counts (even for equal children); depth takes their maximum with the proper connective increment. Thus these statistics concern expanded fields, not distinct interned nodes.

For each native axiom, the loader reconstructs the exact ax-1/2/3 instance from its complete substitution dictionary. For MP it requires two literal integer indices strictly less than the current index, an implication whose antecedent is exactly the first referenced formula, and its exact consequent. It rejects extra fields and checks the final formula and header against the supplied goal. Consequently conversion preserves the complete validated package, including unused records. The independent audit additionally spells every converted formula and substitution back to the entire original native record and checks every rule/reference through EOF for both coordinates; it compares full byte hashes/counts and both-format expanded statistics with fresh paired replay.

Empty-map simultaneous substitution is the identity by induction on the native tree. `ExactImportChain.copy` therefore legitimately reuses these immutable terms while reconstructing every axiom/MP occurrence. `AppendProof.add` always appends, so induction on package index i gives actual global index s+i, where s is the store length before retention; MP references become s+r. `Store.retain` compares the entire resulting formula/rule/substitution/shifted-reference tuple and empty assumption set. The fresh audit exercises this branch on both complete packages in an import-only store, obtaining exactly 361432 records at the original offsets. Nonempty environments use the unchanged inherited simultaneous-substitution implementation; no claimed optimization applies there. The writer recursively spells every child occurrence and every substitution into the full JSON strings. Its cache saves computation only: no pointer, abbreviation or compression receives proof-size credit.

**Exact chain application and complete evidence.** Independent reconstruction gives S₀=P(Z,Y), S₁=Y, K=I₂, beta=(0,1)ᵀ, no letters, and dimensions 1,0,0 with R₀=[(1,0)]. The table checker checks the full preserved certificate; the audit also compares these complete tables directly with the source and chain request. The sole row annihilates beta, there are no letter obligations or next-row premises, and both empty successor levels retain their original dimensions. L064's exact four endpoints are, in order,

    E(P(Z,Y),Z), E(Z,Z), E(Z,Z), E(P(Z,Y),Z).

They occur at indices 375610,375631,375633,377086. The row begins at 361432 and ends exclusively at 377087; its last root is the actual final record and the (0,0) indexed location. Fresh counts reconstruct imports (start,count,root)=(0,122742,122741) and (122742,238690,361431), with the earlier coordinate root also checked at 245483 inside the second occurrence. Backward MP ancestry of the final root contains 122741. Coordinate 1 remains fully present and paid despite being unselected by this row. No whole-graph initial-output identification follows from this exact suffix endpoint.

Reproduction commands, which refuse existing certificate destinations, are:

    PYTHONDONTWRITEBYTECODE=1 python3 scripts/backward-zero/audit_actual_234.py --source
    PYTHONDONTWRITEBYTECODE=1 python3 scripts/backward-zero/audit_actual_234.py
    PYTHONDONTWRITEBYTECODE=1 python3 scripts/backward-zero/audit_actual_234.py --term-statistics

The first runs the inspected archive-only step-218 auditor with a fresh destination; it replays all thirteen source-law and fifteen closure-law pairs, both original native optional packages, both local pairs, and both complete coordinate pairs. The second independently reconstructs joined endpoints/locations and source bounds, scans both complete joined streams, exercises the changed importer, checks full earlier-prefix equality in both formats, and audits each interface charge. The third checks the numerical discrepancy below against literal syntax. Full evidence is `scripts/backward-zero/output/audit-234/{source-replay,certificate,term-statistics}.json`; all three are complete with empty failure lists. No historical archive is regenerated or changed. These are fresh executions, not acceptance of old flags or hashes as proof.

The strict scanner reconstructs every native axiom/MP and compares every literal-image formula, substitution, rule, reference and header, reaching simultaneous EOF. Every complete import is compared field by field with its original native package after relocation; paired-image equality then proves the corresponding image retention. Transitive source-to-local-to-coordinate-to-chain comparisons preserve eight five-record optional blocks, starting at 0,5,16508,16513,122742,122747,139250,139255. They total 40 records, including unused depth-39 native records and all their image occurrences. Optional native inputs have no separately supplied image archives; their images are checked within the complete paired outputs. Both copies of the earlier generated coordinate prefix are retained. The fresh full output measurements are 377087 records in each format, 1072025822 native bytes and 1614404612 image bytes, full-field depths 39/42, and maximum record-node counts 47904/65372. All exact original measurements agree.

**Numerical correction.** The old prose incorrectly gave (t_image,d_image)=(14,5). Literal translation of P(Z,Y) is NOT(NOT τ(Z) OR NOT τ(Y)). Here τ(Y) has four nodes and depth two, τ(Z) five nodes and depth three, so this displayed suffix has thirteen nodes and depth six. Native P(Z,Y) has ten nodes and depth four; both suffixes and Y/Z are bounded by these maxima. Independent literal parsing confirms them. The preserved closure ledger already has `input_term_nodes=13,input_term_depth=6`; the chain ledger already has image argument depth 6·47+6=288 and argument-node bound 8·4^48·14. Thus the prior 14/5 prose was an incorrect numerical description, not a failed executable depth bound. Correcting it leaves every preserved threshold, certificate and proof unchanged. The full evidence retains the former prose values explicitly.

**Uniform original-source accounting.** The fresh source replay independently evaluates L066 (1) on the ten original optional records, obtaining J₆₆=5136010 and U₆₆,native/U₆₆,image=5273469255851860176/7010612066620695136. It applies L065 (4) to I≤2J₆₆, K_j≤2U₆₆,j, the source depth limits, and original suffix statistics. The source, closure and chain library maxima remain separate, with B*=6 including `unused`. This reproduces J₆₅=2796383077672992020, depth limits 167/321, and per-coordinate byte bounds

    U₆₅,native = 1915346158648091146599648375229631990556816562954664768,
    U₆₅,image  = 3465999518951283682816242588400428969342894941527841408.

Receiving two complete prefixes gives I₆₄≤2J₆₅ and K₆₄,j≤2U₆₅,j, because each formula/substitution node occupies at least one byte in its separate full field. Repeated optional/local/generated-prefix records contribute separately. The L064 record, maximum-node/depth, nonnegative byte-sum and logarithmic reference terms are monotone in these majorants and B*. Its own library and original suffix constants are retained. Independently evaluated L064 (1)/(2) agree exactly with the preserved source-based bounds: 10959585489735744040 records, native/image byte limits 77532829592388702507090369634823510260378218973725461504 / 140302967615957169387275466046314788927189819326406127104, depths 167/321 and 69632 location bytes. All measured inequalities pass. No measured generated length chooses a threshold and no earlier row proof becomes a new suffix argument.

The complete interface is independently equal to the five objects charged in the supplement: the original source object, original optional path/count list, the exact `chain` subobject of the fully checked L067 table certificate, the original coordinate-path list, and the reconstructed L064 locations. Compact source serialization is no longer than its 395-byte original file; optional framing costs at most 158 bytes. The chain subobject fits the full table bound 2³⁰(57+2)²⁸; original coordinate paths cost 319 bytes; locations fit 69632 bytes. The five outer keys and punctuation cost less than the fixed 1024 allowance. This proves the stated a-priori interface bound; comparison with its actual 1203 bytes is only verification. Original external paths count as explicit inputs; constructor-owned paths have the fixed-prefix/index framing already charged in L066 step 218. Arbitrarily long path strings are not silently free.

All three libraries are conservatively charged separately in both formats. Summing both proof-and-location bounds, the complete table bound, the interface bound and these library bytes reproduces the total required 82591083966083754586895605479257935903677687517503704368615 bytes versus 2735016756 actual bytes. The uniform conclusion uses composition of the existing fixed polynomials under their original hypotheses: fixed a bounds source suffix expansion; L066 bounds full local inputs; L065 bounds each complete coordinate prefix; L067 bounds the explicit tables; L064 bounds the joined stream and locations. Addition of original strings and fixed framing preserves polynomial dependence. The giant monomial diagnostic in the old certificate is not used to establish this argument. This verifies the displayed composition; finite empty-zero replay does not certify a new nonzero implementation.

**Verdict and limitations.** The exact conditional empty-zero interface survives independent informal audit after the numerical prose correction. No stream, immutable-import, indexed-root, occurrence or source-bound defect was found. Historical constructor call traces and their reported maxima are not independently reconstructed; full emitted fields and the applicable mathematical copying arguments are checked instead. The first missing-name payload failure, all previous archives and unfinished work remain preserved. This is a reviewed local input and correction by reproduction, not certified novelty or progress beyond the checked sources toward unrestricted SAT. Initial-output identification, nonzero reception, ordinary-input completeness, complete L055 review, certificate existence, ER/W/V/U and P versus NP remain unresolved. L055 stays an UNVERIFIED CANDIDATE only at its conditional receiver level; no new DAG input is introduced.

### Retained initial-output/source-row composition, 2026-10-15 (step 241)

**Hypotheses and scope.** This implementation/REPRODUCTION applies the prior
SPECIALIZE assessment `drafts/literature/2026-10-15-output-zero-composition.md`.
Receive exactly L066 steps 236/239's complete initial-output bridge pair for
`scripts/actual-tree/output/initial-236/zero-deleted/` and this lemma's steps
232/234 complete source-row chain pair, with the preserved original
`scripts/actual-tree/output/empty-zero-repaired.input.json`.
The source is the sole zero tree, q=`q`, no letters, deleted zero edge,
U=1,d=0,N=2,n=0, with fixed admission a=4. Retain all source/closure/table
and chain hypotheses already checked above. The bridge receives no optional
proofs and needs no formal-zero premise. The chain separately receives all
its original optional/local/coordinate occurrences. Its original payload
bound remains B*=6, including `unused`; source-only table Q=57 is not the
full original joined input. No independently supplied ordinary-input proofs
or other source fixtures enter this claim.

**Conclusion and proof of the exact composition.** With the unchanged native
abbreviations Y=(q→q), Z=NOT Y and S₀=P(Z,Y), the bridge proves E(Z,S₀)
and the chain proves E(S₀,Z). This step exports a complete native proof of
E(Z,Z), together with its full literal NOT/OR image, retaining both entire
input streams and the entire substituted L056 transitivity string.
The new output is conditional receiver integration, not a new zero-leaf
tautology, a general receiver or certified original mathematics.

Copy the bridge's 1634 records at offset 0, retaining its root 1633. Copy
all 377087 chain records at offset 1634, relocating each MP reference by
that offset. The chain's indexed (level 0,row 0) root 377086 becomes
378720. The resulting coordinate roots are 124375 and 363065; the earlier
coordinate root retained inside coordinate 1 becomes 247117. The source
row range becomes [363066,378721), with exact required roots
377244,377265,377267,378720. These are transported handles, never replaced
by another proof of an equivalent endpoint.

Copy all 1449 records of L056's checked `trans` proof at offset 378721,
simultaneously substituting A↦Z,B↦S₀,C↦Z,q↦q. Substitute every formula
and every axiom substitution field once, without recursing into replacements;
relocate each MP reference. Its root 380169 is literally

    E(Z,S₀) → (E(S₀,Z) → E(Z,Z)).

MP with references [1633,380169] gives the implication at record 380170;
MP with [378720,380170] gives E(Z,Z) at the actual final record 380171.
There are exactly 380172 records. Each imported axiom is unchanged or a
simultaneous instance of the same primitive axiom; each imported MP still
has strictly earlier, literally matching premises after relocation.
Induction on records therefore proves primitive membership, using only
L056's ax-1/2/3/MP strings. Translation commutes with this substitution and
preserves every reference and field; no simplification or new rule is used.
In particular, a direct reflexivity proof is not the exported construction.

Known logical scope is precisely [Metamath bitri](https://us.metamath.org/mpeuni/bitri.html)
(contributed 1993-01-03, proof shortened 2012-10-13) and
[ax-mp](https://us.metamath.org/mpeuni/ax-mp.html), live statements and bitri's
complete five-step proof inspected 2026-10-15 in the assessment. Their
biconditional notation is not identified with the local E syntax: the
implementation copies the already checked L056 string instead. Its
primitive-basis citations and the qualified LTW/Kiefer/Mohri inputs in
steps 232/234 are reused; no semantic closure or coefficient theorem is
reproved. This specialization is necessary to export complete strings and
account for every occurrence rather than use transitivity as an unpaid rule.

**Full retention.** Every bridge and chain record, including unused records,
is copied with its full formula/substitutions and relocated references.
The chain's audited two coordinate, four local and eight optional-block
occurrences remain distinct. The optional starts become
1634,1639,18142,18147,124376,124381,140884,140889; each has five records.
All original source/request/manifest/interface data and the transported
coordinate/local/optional/row locations are written in
`scripts/output-zero/output/composition-241/retained-inputs.json` and its
`locations.json` companion. Induction through the previously audited occurrence
maps, followed by complete equality with the imported chain, preserves
every nested field and reference. Direct checks of all forty original
optional records in both formats supplement that argument. No overlapping
ancestry or unused premise receives a retention discount. Both input roots
occur in the final MP ancestry.

**Original-input ledger application.** Use L066(2)–(4), not the measured
bridge length: J_b=1634, H=1, P*=768, B=1, R=17280000 and

    V_b,native=3670398720, V_b,image=4951975680,
    M_b=10000(R+J_b+2)²+5(584+788)P*.

Use the audited step-234 source composition for J_c=10959585489735744040
and the per-format U_c,j displayed above, with depth limits 167/321.
These already come from the original optional inputs through L066(1),
L065(4) and L064(1)/(2); their parameters are not generated proof lengths.
Keep the full L067 table bound 2³⁰(57+2)²⁸, the step-234 original-source
interface bound and the 69632-byte source location bound.

Complete fixed-trans replay gives L_t=1449 and full-record
(D_t,S_t)=(14,792) native and (20,1100) image. Original source terms
Z,S₀,q have node/depth maxima (10,4) and (13,6), respectively. Write
t_j=10 or 13 and d_j=4 or 6. A substituted fixed record has at most
S_t,j t_j nodes over all its fields: for s connective and v variable
occurrences, s+v t_j≤(s+v)t_j. Its field depth is at most D_t,j+d_j.
The two new MP conclusions and final header are subformulas of the copied
trans conclusion, so obey the same bounds. This also covers literal images
because translation commutes with simultaneous substitution.

Let J*=J_b+J_c+L_t+2=10959585489735747125 and let δ be the binary
bit length of J*+2, here 64. Every relocated decimal reference has at most
δ characters. Each imported record has at most two references; adding
2(J_b+J_c)δ to the old byte bounds pays their new widths without subtracting
the old numeral lengths. Thus each complete joined stream is bounded by

    W_j = V_b,j + U_c,j + 2(J_b+J_c)δ
          + (L_t+4)[(B*+4)S_t,j t_j + 256 + 64δ].       (3)

The last term pays every substituted trans record, both MPs, the final
header and framing, including references. Native/image values are

    W_native = 77532829592388702507090369634823511663205161663692707552,
    W_image  = 140302967615957169387275466046314790330016762017747651512.

To pay every ancillary object explicitly, let A be the already source-bounded
step-234 interface, T the full table bound, F the separately paid uncompressed
fixed-library total (source, closure and chain, plus unitR/symm/trans), and
O the original source-plus-optional native bytes. The libraries are charged
conservatively again when shared. Define

    E*=R+M_b+T+A+F+O+J*+W_native+W_image+10000,
    M*=10000(E*)²,   total*=W_native+W_image+M*+F.       (4)

This is an a-priori framing bound, not a fitted monomial. In this fixed
interface the source/request/original manifests/interface/locations are paid
subobjects of the displayed original bounds; new indexed locations add only
a fixed number of numerals of at most δ characters. There are fewer than
1000 ordinary metadata leaves. Ancillary proof artifacts are the one
substituted-trans pair and three malformed prefix pairs of at most J_b+22
records each. Each record has at most five scalar values and at most 32 separately
counted key/value/punctuation groups (the step-243 clarification below),
so all ancillary fields and groups number less than 1000E*.
Each expanded field costs less than 10E* bytes: imported fields fit their
original whole-stream bounds, substituted fields fit (3), paths fit the
original path framing plus fixed prefixes, and every new numeral, including
the digits of (4), fits this allowance. The original variable/path payloads
are retained. Hence M* pays all these objects, the certificate, retention
supplement and final accounting report, with full JSON framing. The actual
report's small number of fixed fields lies within the same allowance.
Compression is never substituted for expanded proof size.

For fixed a, the reused bounds are fixed polynomials in original explicit
source/optional/path inputs and fixed libraries. Addition and composition
preserve this property. Moreover δ≤J*+2, so (3) and (4) remain fixed
polynomials in those original inputs. No bridge/chain measurement, compressed
size, interned-node count or old giant diagnostic envelope defines a
parameter. This applies the existing copying machinery to the stated
retained interface; it does not assert reception of arbitrary new sources.

**Complete evidence.** Reproduce in order with fresh destinations (the
scripts refuse existing certificates):

    PYTHONDONTWRITEBYTECODE=1 python3 scripts/output-zero/compose_241.py
    PYTHONDONTWRITEBYTECODE=1 python3 scripts/output-zero/verify_retention_241.py
    PYTHONDONTWRITEBYTECODE=1 python3 scripts/output-zero/final_accounting_241.py

The canonical full evidence is in
`scripts/output-zero/output/composition-241/{certificate,retention-check,final-accounting}.json`.
All three certificates have complete=true and failures=[]. Both complete
input pairs and the fixed trans pair receive full primitive/literal-image
replay; the full joined pair is checked to simultaneous EOF against both
entire imported native streams and the entire substituted trans occurrence.
Every native axiom is reconstructed from its declared substitutions and
every MP from strictly earlier literal premises. Every image field/reference
is compared. The separate supplement compares all 1449 original trans
records under an independently implemented simultaneous substitution, the
entire transported map, and all forty original optional records per format.
It does not repeat the full primitive scan or claim an independent critical
audit of the new composition.

| Format | Complete records | Uncompressed proof bytes | Full-field depth | Maximum record nodes |
| --- | ---: | ---: | ---: | ---: |
| Native | 380172 | 1073836801 | 39≤167 | 47904 |
| Literal NOT/OR | 380172 | 1616964652 | 42≤321 | 65372 |

Every line/node/depth/byte bound passes. Final accounting includes every
ancillary artifact and itself (serialized to a stable byte-count fixed
point), all rejection witnesses uncompressed and the separately paid fixed
libraries: 2749679919 bytes, below (4)'s exact total in the certificate.
Seven malformed receptions reject: changed source, suffix, q, wrong indexed
root, corrupted imported reference, corrupted image substitution, and an
omitted retained optional record. The last rejects specifically on full
import mismatch; the image rejects on literal record/image mismatch. The
small corrupted prefixes are rejection witnesses and are not described as
complete positive exports. There is no unresolved failed check. Prior
archives, the first payload failure and all unfinished work are preserved.

**Limitations.** The exact retained output-zero interface now has complete
finite execution evidence and the displayed original-source ledger. Its
separate critical audit remains pending. This is local integration of known
logical operations; it supplies no nonzero integration, arbitrary ordinary-input
completeness, whole-L055 audit, certificate existence, ER/W/V/U premise or
SAT decision/separation. L055 remains only its existing conditional
UNVERIFIED CANDIDATE; there is no main-problem candidate.

### Independent retained-composition audit, 2026-10-15 (step 243)

**Hypotheses, scope and verdict.** The separate RESEARCH / proof_audit /
REPRODUCTION applies exactly the prior SPECIALIZE assessment
`drafts/literature/2026-10-15-output-zero-composition-critical-audit.md`.
Keep step 241's sole-zero source, distinct empty dictionary, q=q, deleted zero
edge, N=2,n=0,a=4, S₀=P(Z,Y), and original source-row root 377086. The bridge
has no optional premises; the chain retains its full source/closure/table
hypotheses and B*=6. No load-bearing composition or bound defect was found.
The small ancillary grouping claim is made precise below without changing
(3), (4), any numerical threshold or an old archive. This supersedes step
241's pending-audit qualification for this interface only. It does not
validate nonempty-letter integration or the whole L055 receiver.

Reuse L056's already audited simultaneous substitution and primitive strings,
L066 steps 236/239 and this lemma's steps 232/234. The exact known logic is
[Metamath bitri](https://us.metamath.org/mpeuni/bitri.html) and
[ax-mp](https://us.metamath.org/mpeuni/ax-mp.html), with the versions and
inspected proof recorded in step 241. Their biconditional notation is not a
new primitive E rule. The qualified LTW v4 Lemma 4.17/(22), pp.36–39, and
Theorem 4.11/(15)–(16), pp.30–32, and the Kiefer/Mohri inputs recorded in
step 234 remain unchanged. No semantic source theorem is reproved or new
source retrieval claimed. The specialization being checked is literal proof
retention and full accounting, not transitivity as a new mathematical fact.

**Complete copying and inference proof.** In `substituted_library`, a variable
node returns its replacement directly. The recursion visits only the original
node's children; it never recursively substitutes within that returned term.
Caching by the original node is therefore valid even if replacement names
coincide with schematic names. The same operation is applied separately to
f and every subs value. For an original axiom schema F(σ), simultaneous
substitution θ gives F(θσ), the very same axiom with its transformed declared
fields. For an MP with earlier r,s, θ preserves the literal implication and
antecedent, so copying to offset o gives MP with references o+r,o+s. Induction
over each complete occurrence proves its primitive membership, including
unused records. The notation has no binders. Literal translation commutes
with substitution by induction on NOT and implication; it never simplifies.

A separately implemented tuple recursion compares every one of the 1449
original trans records against the substituted native stream. The strict
scanner checks all primitive records and every image field to simultaneous
EOF. It reconstructs ax-1/2/3 from declared substitutions, requires two
literal integer earlier indices for MP, checks exact premises/conclusion,
and rejects extra record keys. Its structural parser uses complete key
equality, allocates children first and counts repeated child occurrences
separately. Thus internal interning is no proof-size discount. The reused
parser's finite resource limit is not claimed as all-input completeness.

Fresh full comparison copies all 1634 bridge records, all 377087 chain
records and all 1449 substituted trans records in **both formats**, relocating
only MP references. Each original input reaches its own EOF; exactly two
MPs follow, then the joined streams end. They have references
[1633,380169] and [378720,380170]. The expected intermediate implication
and actual final E(Z,Z) are checked literally, and both imported roots
1633 and 378720 lie in final ancestry. This checks the actual construction,
not a shorter reflexivity proof of the same endpoint.

Every retained source/request/manifest/interface object equals its original.
Fresh map reconstruction shifts both coordinates, all four local occurrences,
eight optional occurrences and the full row interval by 1634. It obtains
coordinate roots 124375/363065, nested earlier root 247117, and row roots
377244/377265/377267/378720 in [363066,378721). Full chain equality transports
the previously audited nested retention; all forty original optional records
are also compared directly. No unused occurrence is removed or discounted.
The bridge, trans and output manifests, actual final roots, complete byte
counts and uncompressed digests agree with their archived inputs.

**Original-source and ancillary ledger.** Independent integer arithmetic
re-evaluates L066(1), L065(4), L064(1)/(2), L066's bridge bound and (3)/(4),
without calling the composition's bound function. Original optional inputs
supply ten records, K=1224/1264 and B*=6. Source and closure library maxima
remain separate from the chain's maxima. This reproduces J₆₆=5136010,
J₆₅=2796383077672992020, J_c=10959585489735744040 and all native/image byte
bounds displayed above. Generated-coordinate bytes enter only through their
**proved source majorants**, not as measured input parameters. Source-only
Q=57 pays the coefficient table, not the original optional proof inputs.

For each fixed trans record, write its expanded nodes as s connective plus
v variable occurrences. The entire transformed record, including subs, has
s+v t_j≤S_t,j t_j nodes and field depth at most D_t,j+d_j. The two MP
conclusions and header are subformulas of its final formula. All imported
references remain below J*. Paying two new δ-digit references per imported
record without removing their old charge proves the relocation term in (3).
Decimal digits are bounded by binary length, and δ≤J*+2. These facts justify
(3), rather than merely observing that its enormous thresholds pass.

The ancillary inventory contains 651 scalar metadata leaves and 3276
separately counted keys/values/braces/colons/commas in the ten JSON files,
including the final report. The earlier work note's 751 was only locating
evidence; the fresh exact count is 651. For proof records, the fully separate
key/value/punctuation convention gives a maximum of 25 groups, so we use 32
instead of the earlier unspecified “less than 20” grouping convention. There
are two trans streams of 1449 records and six malformed-prefix streams of
at most J_b+22=1656 records. Thus fewer than

    10000 + 32[2L_t+6(J_b+22)] + 10000 < 1000E*

items pay these records, metadata and header/whitespace framing (E*≥10000).
The malformed prefixes are paid artifacts, not positive proofs. An imported
formula field fits its original whole-stream bound; a substituted field fits
(3); original paths are paid in the prior interface or fixed prefixes. Fixed
keys/punctuation have constant size. Newly written counters measure at most
polynomial products of J*, W_j and the source quantities, so their decimal
lengths are O(log(E*+2)) and below 10E* here. In particular the digits of
10000(E*)² are at most 5+2 digits(E*), avoiding circular self-accounting.
The complete fixed schemas and this conservative item count therefore give
10000(E*)² for the ancillary artifacts with their actual indentation. The
bound remains a fixed polynomial in the original explicit inputs under the
inherited fixed-a hypotheses; it is not extended to other sources by this
finite execution.

Every ancillary gzip stream is read to EOF at its **uncompressed** size, and
every other artifact is charged in full. The final report's exact reserialized
bytes equal its stored bytes, including its stable own-length contribution.
The fresh total is 2690801453 proof bytes + 8507905 ancillary bytes + 50370561
separately charged fixed-library bytes = 2749679919, below (4). All record,
full-field depth/node and byte inequalities pass. The fresh ledger records
actual and required integers; compression supplies no proof-size credit.

**Evidence and limitations.** `scripts/output-zero/audit_243.py` runs with no
argument, then `--supplement`, then `--metadata`, using fresh destinations
and refusing existing evidence. Its full reports are
`scripts/output-zero/output/audit-243/{certificate,retention-accounting,metadata-framing}.json`.
All are complete with failures=[]. The first report checks the full joined
primitive/image pair, original trans substitution, source arithmetic,
provenance and self-accounting. The second directly compares every original
input record in both formats and inventories every ancillary proof record;
the third counts all ordinary metadata groups. Prior primitive scanner and
component audits are reused and explicitly inspected, not independently
reimplemented in full. The seven historical rejection witnesses are retained
and paid; their rejection tests are not claimed as rerun in this audit.

This is successful local verification by reproduction, with no new theorem
or substantive bound repair, hence recorded conservatively as EXPLORATION.
It supplies neither nonzero-source execution, arbitrary ordinary-input
completeness, the complete two-identity/original-CNF receiver, certificate
existence, ER/W/V/U, nor unrestricted SAT decision/separation. L055 retains
its conditional UNVERIFIED CANDIDATE status; the main problem has no candidate.

## Mathlib

Full matching coverage was not checked. General finite-dimensional F₂ linear algebra would support elimination/span facts, but no specific Mathlib theorem or formalization of these actual-source/L064 encodings, complete joined primitive streams or original-source composition is asserted. Unknown coverage is not absence.
