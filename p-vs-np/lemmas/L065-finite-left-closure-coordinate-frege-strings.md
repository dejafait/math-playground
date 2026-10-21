# L065 — Finite left-closure coordinate packages from exact local proofs

## Hypotheses

Use the assumption-free native ax-1/2/3 and MP calculus of L056, with fully expanded native trees

    X(A,B)=((A→B)→NOT(B→A)), E(A,B)=NOT X(A,B),
    P(A,B)=NOT(A→NOT B), Y=(q→q), Z=NOT Y.

The literal image τ sends NOT to NOT and A→B to NOT τ(A) OR τ(B), retaining double negations. Receive native proofs only; arbitrary independently supplied NOT/OR proofs are outside this interface. All variable payloads, including q, are nonempty ASCII alphanumeric/underscore strings. Names and suffix trees may coincide and have arbitrary supplied depth.

Receive N≥2 fully written suffixes S_v, n≥0 ordered letter-variable occurrences x_b, any designated 0≤t<N, and dimensioned literal-bit matrices E₀,E_b of size N×N, all strictly upper triangular. No last-index/sink condition on t is added. Let Bal([])=Z, Bal([A])=A; longer lists are right-padded by Z to the least power-of-two capacity and combined by the perfect ordered X tree. W(a;S) selects entries with bit 1 in increasing index order, using this exact Bal. There is no scalar gate or bit variable.

Receive all N complete assumption-free native proof occurrences with declared and actual last endpoint exactly

    E(S_v,R_v),
    R_v=X(B_v,X(W((E₀)_v;S),
                  Bal([P(x_b,W((E_b)_v;S)):0≤b<n]))),
    B_v=Y if v=t, and Z otherwise.                         (1)

Every supplied formula, axiom substitution, earlier MP reference, unused/deep record and header is explicit input. A semantic recurrence, a theorem label, an assumption, a shortened proof or an external cache does not supply (1). Identical written S_v are used throughout. No constructor for these local proofs or bridge from L054's outgoing-edge syntax is assumed.

Use precisely L063's checked fourteen-law library and the additional fixed law

    E(A,X(A,X(B,C))) → E(B,C).                            (2)

Complete checked native strings and their literal images are fixed library inputs; arbitrary caller libraries and prepopulated caches are excluded. The new checked files are `scripts/left-closure/output/close_cancel.<native|not-or>.jsonl.gz`. Fixed-library synthesis is confined to this three-variable schema, never a growing closure tautology.

For format j=native,image let I be the total received line count, K_j the total formula/substitution node count of those complete occurrences, and δ_j their maximum depth. Let t_j≥1,d_j bound nodes/depth of every supplied suffix, letter,Y,Z in that format. Let B≥1 bound every raw name, including fixed library auxiliaries. All syntax, dimensions, arrays, names, proof occurrences and framing count toward the original uncompressed explicit input Q. The fixed library has maxima

    L=3470, (D_native,S_native)=(19,2456),
            (D_image,S_image)=(27,3492),

where S_j counts a whole record, including its axiom substitution fields. The enlarged library's depth maxima differ from L063's old maxima and must be paid.

## Conclusion

Compute the finite bit tables

    K₀=I_N+E₀+...+E₀^(N−1), beta=K₀e_t, G_b=K₀E_b.

There is a deterministic complete-record construction of all N native coordinate packages ending exactly

    E(S_v,C_v),
    C_v=X(Β_v,Bal([P(x_b,W((G_b)_v;S)):0≤b<n])),
    Β_v=Y or Z according to beta_v.                      (3)

Every package contains every supplied local proof occurrence once with relocated references, including unused records, and a complete generated proof prefix. Every formula abbreviation is expanded in serialization. Each package has a line-by-line literal image and matches L064's supplied-coordinate interface. This conclusion supplies packages from the stated local packages, not the existence or smallness of the latter.

One original-input ledger pays the aggregate of all complete exports. Set

    D=2+N+n, h=ceil(log₂D), a=3h+4,
    V=2^(3h+6), H=9h+30,
    T=10000 N V²(H+1)², G=(L+1)T, J=I+G,
    P_j=8·4^(H+1)(t_j+1), F_J=256+64 ceil(log₂(J+2)).

Each coordinate package has at most J lines, depth at most max(δ_j,D_j+c_jH+d_j), record nodes at most max(K_j,S_jP_j), and bytes at most

    U_j=(B+4)[K_j+(G+1)S_jP_j]+(J+2)F_J,             (4)
    c_native=3, c_image=6.

The aggregate in format j has at most NJ lines and NU_j bytes (8NU_j full bits). Both formats together cost at most N(U_native+U_image) bytes. These are fixed polynomials in Q; no generated-package length or measured output enters them. Construction/checking admit polynomial abstract bit time. Particular Python recursion, memory and disk limits are practical qualifications, not an all-input execution claim.

This is a conditional construction argument and partial implementation/reproduction of known finite closure and logical operations, without certified novelty. Complete empty-case, two-vertex variable-edge and isolated three-vertex constant-cancellation exports are checked. Step 207 completely verifies the preserved star coordinate-0 pair, including nonpower selection and variable-after-constant closure; step 208 constructs and completely verifies coordinate 1 in a fresh store from the original local inputs. Step 209 constructs and completely verifies coordinate 2 in another fresh store, completing the three independent star pairs. Step 210 checks the aggregate full-bit cost and exact L064 receiving syntax of those independent pairs by composing their complete replay evidence. Actual receiver import and coordinate-0 historical cache-call instrumentation remain unverified. The separate step-206 all-size audit below repairs two intermediate counts within the unchanged ledger; it does not certify unfinished exports. The complete L055 candidate, ordinary-input completeness, coefficient/initial-output interfaces, both receivers, certificate existence, ER representation, W/V/U and unrestricted SAT transfer remain unresolved.

## Proof

### Known coverage and exact specialization

The unchanged step-201 SPECIALIZE assessment `drafts/literature/2026-10-13-left-closure-coordinate-primitive-strings.md` covers precisely this target. The semantic comparison is Mohri, *Generic Epsilon-Removal and Input Epsilon-Normalization Algorithms for Weighted Transducers*, IJFCS 13(1):129–143 (2002), [author manuscript](https://www.cs.nyu.edu/~mohri/pub/ijfcs.pdf), Definitions 4–5, Theorem 1 and complete proof, §§3.1–3.3, manuscript pp.3–6/10–11; and *Weighted Automata Algorithms*, [author Handbook manuscript](https://cs.nyu.edu/~mohri/pub/hwa.pdf), §6.1, Theorem 4/(28)–(31), pp.21–23. The general complete-semiring theorem is not applied to F₂. The separately stated acyclic any-semiring case applies: all edges increase index, so no cycle/infinite sum occurs. Its empty remaining-path case supplies the terminal injection, and its first non-epsilon-edge case uses the left-closure orientation. L055 already writes this identity; no semantic closure discovery or theorem-level reproof is claimed.

Reuse the checked primitive basis/substitution of L056, single-factor distribution of L057, complete imports/combinations of L058, L062's successive-cut geometry and L063's paid normalizer. Primary logical coverage in the assessment includes the Church P2/Lukasiewicz system, [biluk](https://us.metamath.org/mpeuni/biluk.html), [xor3](https://us.metamath.org/mpeuni/xor3.html), [xorbi12i](https://us.metamath.org/mpeuni/xorbi12i.html), [xorass](https://us.metamath.org/mpeuni/xorass.html) and [xordi](https://us.metamath.org/mpeuni/xordi.html). Their inspected live pages are not a pinned/recursively checked set.mm revision, and source XOR requires the paid double-negation bridge. No source label is emitted as a rule.

The required specialization is the exact recurrence-to-package interface and changed aggregate ledger. Law (2) is a fixed common-expression cancellation schema, semantically true for the eight assignments to A,B,C: if A equals A XOR (B XOR C), then B XOR C is false, hence B=C. Semantic evaluation is not a proof rule. The emitter uses L056's finite synthesis/deduction construction only on this fixed schema, and the independent primitive checker verifies all 1937 records in each format. Archive replay also checks their literal correspondence. Thus it is an actual fixed primitive proof before any growing substitution; completeness is not invoked for growing terms.

### Reception, finite tables and one coordinate

`scripts/left-closure/endpoints.py:request` checks dimensions, literal integer bits, strict triangularity and all fixed syntax/names. Nilpotence follows because a length-N nonzero matrix-product term would require N strict increases among only N indices. Finite multiplication constructs all powers and checks E₀^N=0 and K₀E₀=K₀+I_N. It constructs beta and G_b directly. All G_b are strictly upper triangular: a nonzero term has u≤v<w. These are explicit finite arithmetic construction checks, never Frege premises or a formal-zero oracle.

`Closure` checks every complete package against its independently reconstructed exact endpoint (1) before starting a fresh store. L058's importer reparses all substitutions and earlier MP references, rejects assumptions/invalid records/duplicate fields, and retains every occurrence. Each supplied record is reconstructed at offset s+i with exactly the relocated references s+j; field-by-field comparison checks full retention, including unused records. Repeated paths supplied as different occurrences are copied independently. The local template cache starts empty and references only records already copied in this same store. Simultaneous substitution, including q, does not recurse into replacement trees, so coincident names do not cause capture or further substitution.

Fix v, write k for row v of K₀, and A_v=W(k;S). Balanced combination of the imported (1) conclusions selected by k gives a genuine earlier primitive record

    E(A_v,D_v), D_v=Bal([R_u:k_u=1]).                  (5)

The implementation then compares D_v with

    T_v=X(A_v,X(S_v,C_v)).                            (6)

Here all S_u retain their literal input trees. To justify the comparison, use L063's occurrence tags: Y has tag (0), S_w has (1,w), P(x_b,S_w) has (2,b,w), and Z is the deletable zero. These tags refine literal formula equality, even if distinct indices/names spell identical formulas. They are not propositional variables. Single-left-letter distribution expands actual P(x_b,W(...)) occurrences without commuting their factors. Reassociation, occurrence sorting, pair cancellation and padding are all paid primitive operations from the fixed library.

In D_v the parity of Y is k_t=beta_v. The parity of each suffix tag (1,w) is (kE₀)_w=k_w+[v=w]. The parity of each product tag (2,b,w) is (kE_b)_w=(G_b)_(v,w). In T_v these parities are respectively beta_v, k_w+[v=w], and (G_b)_(v,w). Other leaves are explicit Z. Thus the two normalizations have literally identical sorted odd-tag outputs with the exact Bal padding convention. This equality remains valid for n=0, empty selections, cancelled constant paths, repeated suffix spellings and arbitrary t. Product-on-Z is contracted by its paid law. Finite parity checks only justify choosing these transformations; they never replace their proof records.

L063's comparison procedure therefore produces E(D_v,T_v). Transitivity with (5) yields E(A_v,T_v), and simultaneous substitution A↦A_v,B↦S_v,C↦C_v in the checked (2), followed by MP, yields exactly E(S_v,C_v). Earlier equivalence proofs are used only as MP premises; none is inserted inside a growing term. This proves (3) for each coordinate by explicit primitive assembly, without receiving the conclusion or assuming the whole L055 receiver.

### New all-size argument and copying ledger

Above unchanged suffix/letter/Y/Z trees, every selection/padded Bal adds at most h X levels. A local right side has height at most 2h+3; the selected combination D_v has height at most 3h+3. C_v has height at most 2h+2 and T_v height at most 2h+4. All are at most a. Congruence uses actual corresponding child terms, never equivalence formulas as leaf terms. The common-expression detachment substitutes A_v,S_v,C_v directly, also within this bound.

Expansion distributes a single atomic letter through its right X tree, retaining the original branch height; a product atom is later measured by restoring its one P node. There are at most 2^a expanded atomic leaves. Padding to capacity M adds an unpadded near-balanced zero tree when necessary: M≤2^a<V and its source height is at most a+1. L062's interval-restriction invariant bounds the successive match intermediates by 2a+2, independent of the number of cuts. The target is perfect of height at most a.

Each adjacent slot operation starts/finishes in that perfect shape; L056 bounds temporary height by 3a+2. Thus the two sorting passes and the cancellation pass do not compound heights. Erasing zero children only reduces height. The final compact-shape comparison has height at most 2a+1 by the same successive-cut theorem; empty outputs are one Z. Restoring a product annotation adds at most one level. All arguments throughout, including cumulative transitivity's initial/previous/final terms, consequently have height at most 3a+3<H. The supplied depth d_j is additive; an unused deep proof affects only δ_j/K_j and is never placed inside a new term. No depth exponent depends on received proof depth.

Count one elementary operation per fixed-law instance or external MP. As in L062's operation-by-operation proof, each normalize call costs less than 1000 V²(H+1)²: expansion has fewer than 4V visits, each with at most 12 operations; the at most three zero-erasure traversals have fewer than 2V visits each; padding/final composition use at most 50 more; the two shape comparisons have at most 2V(H+1) rotations, each costing at most 2H+8; the two insertion sorts and cancellation have at most 2V² slot operations, each with at most 4H+3 events of cost at most 2H+8. These estimates apply to the present admitted X/Y/Z/suffix/single-letter-product expressions; the old transition's numerical ledger is not substituted for this new call count.

There are two normalizations per coordinate, hence 2N total. A row of K₀ selects m≥1 entries because its diagonal is 1. Its least-power-of-two capacity M satisfies M<2m≤2N, so combination visits 2M−1 nodes, not necessarily at most 2N−1. Its exact elementary cost without cache savings is 7(M−1)+(M−m): seven per internal congruence and one per padding reflexivity. This is less than 15m and hence at most 16N. After the normalizations, comparison-return symmetry/transitivity cost five operations; the row's final transitivity and detachment cost another five. The total is at most

    2000 N V²(H+1)² + N(16N+10) < T.

Here V≥64D³ and N≤D, so the final inequality holds with ample fixed slack. No favorable cache reuse is assumed. A fixed instance copies at most L records and an external MP one, giving G generated records across the entire fresh store and J after the I full imports. Every export is a prefix of this store, not a recursively imported generated package.

For native X the node recurrence is p_(i+1)≤8+4p_i; its image and P obey the same bound. Starting at t_j yields at most P_j nodes for every substituted argument of height ≤H. A fixed record with S_j total nodes, including axiom substitution fields, then has at most S_jP_j nodes and depth at most D_j+c_jH+d_j. MP conclusions outside templates are subformulas of those copied implication records. Imported records have total K_j nodes and maximum depth δ_j. ASCII formula/name text costs at most B+4 bytes per node, and rule/reference/JSON framing is bounded by F_J. The repeated endpoint header is covered by the extra generated-record allowance and J+2. This proves (4), including every substitution occurrence and global reference.

After row v, export the entire store prefix through its actual final coordinate record, with no pruning. It contains all received occurrences and all earlier generated records. That prefix fits (4); summing over N such complete packages gives NU_j, including N copies of every input occurrence. Internal shared roots alone would not satisfy the external L064 interface. The literal writer translates every header/formula/substitution and leaves references unchanged. Native primitive induction and the translated axiom/MP induction prove both streams. Row indices, tables and paths can be encoded in O((n+1)N³+N log(J+2)+Q) additional bytes; their inclusion preserves a fixed polynomial aggregate bound.

Finally 2^h<2D, so V=O(D³) and 4^H=O(D^18); all fixed constants, dimensions, t_j,K_j,I and name lengths are bounded polynomially by Q (literal translation has constant node overhead). Thus the displayed ledger is one fixed polynomial in the original input. Matrix construction, parsing, full-template copying, reference relocation, finite comparisons, serialization and primitive replay each have polynomially many operations on strings of these bounded lengths. This proves polynomial abstract bit time, without claiming that a finite test or a particular interpreter verifies all resource limits.

### Bounded evidence and limitations

The initial bounded run is `python3 scripts/left-closure/run.py`; full certificates/logs are under `scripts/left-closure/output/`. The fixed 15-law constants and checked (2) are established. `certificate-202.json` records the complete N=2,n=0,E₀=0,t=0 case. Both received local packages, including an unused 35-negation record, are retained in each exported prefix. Every native/image record and relocated input field was independently replayed by the archive checker, both exact final endpoints and all earlier coordinate roots were matched, and writer/checker full-byte hashes agree. The four actual complete streams are:

| Coordinate | Lines per format | Native/image uncompressed bytes | Native/image depth, actual / required |
| --- | ---: | ---: | --- |
| 0 | 240652 | 649827368 / 994890311 | 37 / 165; 37 / 318 |
| 1 | 302608 | 884456585 / 1344436964 | 37 / 165; 37 / 318 |

The original-input line threshold is 2796383077662831152 for each export. Native/image aggregate actual bytes are 1534283953 and 2339327275. Exact uniform node/byte/aggregate thresholds from (4) are in the full certificate, and every measured inequality passes. All generated law arguments have measured structural height ≤3, below H=48; native/image argument nodes are 116/159 and depths 11/15, each below its independently input-derived threshold. These very loose majorants establish a polynomial form, not practical efficiency or an optimal exponent. Reproduction is not a mathematical discovery beyond the checked sources.

`python3 scripts/left-closure/check_rejections.py` records five rejected complete corruptions in `rejections-202.json`: wrong adjacency dimension, a nonzero diagonal triangularity bit, wrong local endpoint, wrong exported header and a forward MP reference. These use the fully checked empty case as a valid base; each file corruption retains the complete other records. All five reject for their designated reception/primitive check, with no failures. No corrupted stream supplies a proof.

The initial N=4 constant-path/variable fixture produced an unnecessarily large local input and was interrupted during input processing. Its artifact `diamond-local-0.native.jsonl.gz`, initial log and `certificate-202-interrupted.json` remain preserved and are not counted as checked complete input evidence. `python3 scripts/left-closure/run_fast.py` replaces only test-input construction by short paid associativity/congruence/cancellation strings. All four new complete local packages pass primitive checks. Their graph has two cancelling constant 0-to-3 paths, beta=(0,1,1,1), a surviving G₀(0,3)=1 reached through constant edge 0-to-1 followed by variable edge 1-to-3, a three-entry selected K₀ row, empty selections, repeated name x=q=A and an unused deep record. Their suffixes are exactly P(A,Y), X(Y,P(A,Y)), Y, Y; the test decompositions are literally identical to the received suffix syntax, and assert no general suffix/proof finder.

The unchanged compiler constructed the first nontrivial root and matched its exact endpoint in memory (1241691 generated-plus-imported records), but the bounded run was interrupted during native serialization. `certificate-202-fast.json` records `KeyboardInterrupt`, a false overall completion flag and no completed nontrivial export; `run-202-fast.log` and the partial archive are retained. There is no completed image/replay/aggregate measurement for this case, and no claim that any of its closed-coordinate streams passed. The remaining complete exports are necessary implementation evidence for continuation. The all-size ledger above is written, not inferred from an interrupted stream or a certificate preview; its independent critical audit is still pending.

#### Step 203: complete variable-edge exports; preserved diamond replay interruption

`python3 scripts/left-closure/finish_exports.py` receives the same four complete smaller diamond local proofs in a fresh store. The writer uses bounded identity-based spelling caches and gzip level 1 only. For a variable it returns the identical payload, for native `n` it emits the identical negation parentheses, and for native `i` it emits the original implication or its literal NOT/OR image. Structural induction proves equality with the old serializer; a cache hit requires the identical retained tree object and emits its full spelling. Cache/compression policy therefore changes no inference, formula occurrence, substitution, reference or uncompressed copying bound. Every fixed-library formula/substitution in both formats was also compared with the old serializer. The initial descriptive-tag mismatch was caught before export, corrected, and preserved in `certificate-203-initial.json`/`run-203-initial.log`; it was an implementation failure, not a mathematical counterexample.

The diamond's coordinate-0 native and image writers both returned after serializing all 1241691 records. Full archive replay was subsequently manually interrupted during gzip reading. `certificate-203.json` records KeyboardInterrupt, a false overall flag and **zero completed verified diamond exports**. Both new archives and the old step-202 artifacts are preserved. Their uncompressed writer measurements had not been checkpointed before replay; no size/depth/retention or endpoint-replay check is claimed for them. The coordinate-1 output reservation is an unused directory containing `STOP.md`, not an archive. Future writes now save writer sidecars before long replay; a writer sidecar alone is not proof verification.

The smaller discriminator `python3 scripts/left-closure/run_variable.py` completes the unchanged compiler on N=2,n=1,t=1,E₀=0, one variable edge 0→1, identical q=x=A, and written suffixes P(A,Y),Y. Its finite tables are K₀=I₂, beta=(0,1), G₀=[[0,1],[0,0]]. Complete genuine local proofs use only already checked zero/product/congruence/transitivity strings, with an unused 35-negation record retained. This is test-input construction on these literal formulas, not a general local-recurrence finder or L054 syntax bridge.

`certificate-203-variable.json` is complete with no failures. The archive checker reconstructs every primitive record, compares every literal-image field, checks every retained/relocated local input, both exact endpoints and all earlier coordinate roots. All writer full-byte hashes/counts agree with replay. Both complete exports satisfy (4), and their aggregate/argument checks pass:

| Coordinate | Lines per format | Native/image uncompressed bytes | Native/image depth, actual / required |
| --- | ---: | ---: | --- |
| 0 | 160294 | 635440425 / 938128185 | 37 / 194; 37 / 374 |
| 1 | 291723 | 1042363653 / 1564209276 | 37 / 194; 38 / 374 |

The original-input bound is J=250749725567877135011 lines per export. Native/image per-export byte bounds are respectively 32743741258938733749564741537420543237254290059718189013277194 and 58194800730972138769075772317117537145117757744608821682515744. Aggregate actual bytes are 1677804078 and 2502337461, each below its respective 2U_j bound. The 15011 imported records include both entire local proof occurrences in every export. Maximum measured structural argument height is 4≤H=57; native/image argument nodes are 158/215 and depths 14/18, below the input-derived thresholds. All record-node/depth bounds pass. `certificate-203-summary.json` records exact actual/required bounds and distinguishes these four checked streams from every interrupted or unverified artifact.

This is local verification/reproduction of the conditional interface. It tests a surviving variable coordinate and terminal beta, but E₀=0 means it does **not** check nonzero constant closure, two constant paths cancelling, a variable edge following a constant edge, or nonpower selection. Those discriminators remain pending; finite checks do not validate the general all-size proof. Avoid rebuilding the large diamond automatically: isolate a smaller constant-only cancellation case next, under the unchanged ready compiler assessment. No new mathematical lemma or bound is asserted here.

#### Step 204: complete isolated constant-cancellation exports

`python3 scripts/left-closure/run_constant.py` completes the unchanged compiler on N=3,n=0,t=2,q=A, E₀=[[0,1,1],[0,0,1],[0,0,0]], and the identical written suffixes S=(Z,Y,Y). The graph has exactly a direct and a length-two constant path from 0 to 2, so their F₂ contributions cancel. The complete finite tables are

    K₀=[[1,1,0],[0,1,1],[0,0,1]], beta=(0,1,1), G=[].

All matrices satisfy the original strict-triangular hypotheses; the empty letter list has its exact Z syntax. This is a test specialization, with no changed all-size argument, fixed library, source coverage or receiving contract.

The three assumption-free local test proofs are constructed from paid fixed cancellation, congruence, zero, symmetry and transitivity strings. Their exact right sides reduce as follows, where every arrow is an equivalence proved through those fixed laws and MP:

    R₀=X(Z,X(X(Y,Y),Z)) -> X(Z,X(Z,Z)) -> X(Z,Z) -> Z,
    R₁=X(Z,X(Y,Z)) -> X(Z,Y) -> Y,
    R₂=X(Y,X(Z,Z)) -> X(Y,Z) -> Y.

The first step for R₀ substitutes Y into the paid cancellation law and lifts it through the marked two-level XOR context; the remaining steps use zeroR/zeroL, each lifted by congruence where needed. Transitivity and symmetry give exactly E(S_v,R_v), with no recurrence supplied as an axiom. All three complete local packages pass primitive/endpoint checks. Input 0 additionally retains the unused 35-negation axiom. These test-only literal constructions are not a general local recurrence finder or L054's actual-tree syntax bridge.

`certificate-204-constant.json` is complete with no failures. The separate archive checker reconstructs every native axiom/MP record, compares every image formula and substitution field, retains and compares all three complete input occurrences with relocated references, and matches every earlier/final coordinate root. The exact final endpoints are E(Z,X(Z,Z)), E(Y,X(Y,Z)), E(Y,X(Y,Z)). Writer full-byte hashes/counts agree with replay for all six streams; all original-input per-prefix record-node/depth/line/byte checks and aggregate/argument checks pass:

| Coordinate | Lines per format | Native/image uncompressed bytes | Native/image depth, actual / required |
| --- | ---: | ---: | --- |
| 0 | 442406 | 3804577906 / 5869200529 | 37 / 192; 43 / 372 |
| 1 | 677804 | 6092030697 / 9427483056 | 37 / 192; 43 / 372 |
| 2 | 734672 | 6355741967 / 9839819723 | 37 / 192; 43 / 372 |

Each export retains all 24177 imported records: input counts 10987,6570,6620 at offsets 0,10987,17557. The original-input ledger has h=3,V=32768,H=57 and J=376124588351815704177 lines per export. The native/image per-export byte bounds U_j are 30697257430255062890176137891861162368301765316561649427625128 and 52375320657874924892098570122986569537900625371235038073672148. Aggregate actual bytes are 16252350570 and 25136503308, each below its respective 3U_j threshold. Maximum record nodes are 158976 native and 226364 image, below the respective input-only max(K_j,S_jP_j) bounds recorded completely in the certificate. Maximum measured argument height is 5≤57; argument nodes/depth are 612/17 native and 871/23 image, below the original-input P_j and depth thresholds 173/345. `certificate-204-summary.json` preserves exact actual/required bounds, all export evidence and the remaining discriminators. Every complete relevant export, input-retention/argument field and ledger was inspected, rather than treating a preview or writer sidecar as verification.

This supplies local verification/reproduction for nonzero constant closure and two cancelling constant paths, with surviving beta, empty selections and repeated suffix syntax. Selected K₀ row lengths are 2,2,1, so nonpower selection is not tested; n=0 leaves variable-after-constant closure untested. The all-size ledger remains unaudited. Every prior interrupted diamond artifact and the complete empty/variable/rejection evidence is preserved. No new lemma, novelty claim, complete receiver or SAT consequence is asserted.

#### Step 205: three-entry selection and variable-after-constant closure

`python3 scripts/left-closure/run_star.py` constructs one literal test input for the unchanged compiler: N=3,n=1,t=2,q=x=A, E₀=[[0,1,1],[0,0,0],[0,0,0]], E₁=[[0,0,0],[0,0,1],[0,0,0]], and S=(X(a,Y),a,Y), a=P(A,Y). Both adjacency matrices are strictly upper triangular. E₀²=0, so the finite tables, independently rebuilt by the receiving contract, are

    K₀=[[1,1,1],[0,1,0],[0,0,1]], beta=(1,0,1),
    G₁=[[0,0,1],[0,0,1],[0,0,0]].

The first K₀ row selects three entries, forcing least-power-of-two right padding to four. G₁(0,2)=1 is supplied by the constant edge 0→1 followed by the variable edge 1→2, whereas E₁(0,2)=0. This tests nonpower selection and variable-after-constant closure within the existing receiving hypotheses, without changing the compiler, fixed library, all-size ledger or source comparison. Two cancelling constant paths remain covered by step 204, rather than this star.

The three exact local right sides reduce by the following paid equivalences:

    R₀=X(Z,X(X(a,Y),P(A,Z)))
       -> X(Z,X(X(a,Y),Z)) -> X(Z,X(a,Y)) -> X(a,Y),
    R₁=X(Z,X(Z,a)) -> X(Z,a) -> a,
    R₂=X(Y,X(Z,P(A,Z)))
       -> X(Y,X(Z,Z)) -> X(Y,Z) -> Y.

For R₀ and R₂, prod_zero first proves E(P(A,Z),Z); congR lifts this through the inner X. zeroR gives E(X(C,Z),C) for the actual constant selection C, and transitivity combines those inner steps. A second congR lifts the inner equivalence through the terminal X. The final law is zeroL for R₀ and zeroR for R₂. For R₁, zeroL proves E(X(Z,a),a); congR lifts it through the outer X, followed by zeroL. Transitivity and symmetry yield precisely E(S_v,R_v) in all cases. All law substitutions use the identical written q=A, suffixes and letter; no semantic recurrence is emitted as an axiom. The complete local packages have 10653,5503,10702 records and pass native primitive/endpoint checks. Input 0 additionally retains the unused 35-negation axiom. These are test-only literal constructions, not a general local-proof finder or L054 actual-tree bridge.

Coordinate 0 reached its exact in-memory root with 1217747 imported-plus-generated records. Both complete prefix writers returned and saved sidecars: native 30027917995 uncompressed bytes (SHA-256 e05c99b420ca1f07d76eceb5a71076035448258bbb66f1a4e6d8cefa0ee9e8ec), image 45525924076 bytes (SHA-256 7778a78c759ff19228c3948328b84dca78664e53cd7e5c28175ec7367ee9244e). These are **unverified writer measurements**, not independently replayed proof or copying evidence. The original-input ledger has I=26858,J=376124588351815706858,H=57; its complete per-format thresholds are retained in the certificate. No measured record-node/depth, import-retention, hash-correspondence or aggregate/argument comparison is claimed for these star exports.

Full coordinate-0 replay was intentionally interrupted at this bounded attempt's practical boundary while the checker was rebuilding syntax trees. The process exited 130 and saved `KeyboardInterrupt` in `scripts/left-closure/output/certificate-205-star.json`, with complete=false and exports=[]. Thus **zero star exports are certified**; coordinates 1/2 were not constructed. The archives, writer sidecars and `run-205-star.log` are preserved. The interruption is neither an invalid primitive inference nor a mathematical counterexample or lower bound.

`python3 scripts/left-closure/summarize_star.py` independently rechecks only the three complete small local inputs to retain their full primitive/endpoint measurements in `scripts/left-closure/output/certificate-205-summary.json`; it does not rebuild or replay either large archive. The summary keeps the complete original-input ledger, finite tables, writer measurements explicitly marked replay_verified=false, actual/required writer line/byte thresholds, the interruption and all pending checks. The initial driver had recorded the input paths and check results in its log but omitted these per-input machine measurements; this additional bounded check fills that evidence omission, rather than widening the mathematical attempt.

This step is EXPLORATION / REPRODUCTION: it constructs and checks the exact local test inputs and writes one complete prefix pair, without completing the intended discriminators at the export level. All earlier completed and interrupted evidence remains untouched. Before further large stream work, the next bounded test should independently audit the all-size argument and original-input ledger under this unchanged compiler scope. Do not automatically rebuild/replay the preserved archives during that audit; the all-size proof remains unaudited, and the missing star export checks remain recorded.

At the end of step 205, this new assembly had not received a critical audit; step 206 below addresses its all-size argument only. It does not produce (1) from L054, coefficient spaces, initial/output identification, a whole receiver, ordinary-input normalization or a formula-only certificate bound. L055 remains an UNVERIFIED CANDIDATE at proof-string level, with no main-problem candidate or SAT conclusion.

### Independent all-size audit, 2026-10-14 (step 206)

This RESEARCH / REPRODUCTION audit reuses the unchanged step-201 SPECIALIZE assessment. It checks the complete closure emitter and receiving contract, inherited `Store`, `Rewrite`, `expand`, `erase_zeros`, `normalize`, `compare` and `combine`, complete-import and prefix writers, and L056/L057/L058/L062's applicable proofs. It uses the precise source imports already stated above; no new theorem-level source claim, source reproof or cross-notebook result is introduced. The target is the original-input all-size construction and copying bound, not the unfinished large archive replay.

**Endpoint and hypotheses.** For a row k of K₀, selecting the exact supplied recurrence proofs gives E(W(k;S),Bal(R_u:k_u=1)). The matching target is X(W(k;S),X(S_v,C_v)). After single-left-letter distribution, their respective tagged coefficients are k_t=beta_v, (kE₀)_w=k_w+[v=w], and (kE_b)_w=(G_b)_(v,w). Tags are tied to positions, so equal written suffixes or letters at different indices need not be identified. Within a tag all occurrences have identical native syntax, allowing literal cancellation. Sorting each normal form by tag leaves one occurrence precisely for an odd count, with Z removed and identical right padding restored. Thus both normal forms agree literally. The two normalization proofs, symmetry and transitivity yield the comparison; another transitivity and the checked fixed common-expression law yield exactly (3). No established equivalence is substituted as a term. The finite triangular identity includes the diagonal of K₀ and all empty constant paths; it requires no last-index or sink condition on t. Empty letter sums and empty selected successor rows are exactly Z. No suffix equality or recurrence is inferred from semantic evaluation.

**All substituted arguments.** Each received suffix, letter, Y or Z is an opaque base tree for the structural-height argument, with its complete size/depth retained. The initial bounds 2h+3 for R_u, 3h+3 for the selected right side, 2h+2 for C_v and 2h+4 for the comparison target follow by adding the displayed X/P levels and at most h per balanced range. The mixed old/new trees within combination use the same range split and have these bounds. Distribution moves a single atomic left factor down its right X tree; it preserves that branch's height and creates no nested product. Treating P(x_b,S_w) as one tagged atom changes no serialized formula; undoing that annotation adds at most one structural level.

The expanded X tree has at most 2^a leaves. Appended zero padding has at most that capacity and height at most a; its addition increases source height to at most a+1. L062's restriction invariant applies to this precise ordered tree, giving height at most 2a+2 throughout first matching, regardless of the number of cuts. Each slot operation starts and ends in the same perfect shape; L056's exposure/reversal bound gives at most 3a+2 during it. Bottom-up zero erasure only replaces children by no-taller children. Both compact trees have height at most a, so their final matching has height at most 2a+1, including the zero-survivor case of one Z. The actual arguments of rotation, symmetry, congruence and cumulative transitivity are subtrees or initial/previous/final whole trees from these phases. Restoring product annotations gives at most 3a+3=9h+15<H. An unused deep supplied proof record never enters this structural recursion: its depth contributes to δ_j, while deep suffixes contribute additively through d_j.

**Operation-count corrections.** The previous 2N−1 visit assertion is false for nonpower selected lengths: m=N=3 has capacity four and seven visits. The corrected exact count above still gives at most 16N elementary operations. The previous displayed subtotal also omitted `compare`'s final symmetry (two operations) and transitivity (three); the corrected subtotal explicitly pays these in addition to the five final row operations. Neither correction changes T, G, J, H, P_j or U_j, or any previously saved threshold.

For clarity, the per-normalization estimate follows from the actual helper costs refl=1, symm=2, trans=3 and two-child congruence=7. Expansion costs at most 48V operations; three zero-erasure traversals cost at most 72V. Padding, two rewrite initializations and final composition fit the allowance 50. A rotation or slot event, including context lifts and cumulative transitivity, costs at most 2H+8. L062 gives at most 2V(H+1) rotations across both shape matches; the two insertion sorts and cancellations give at most 2V² slot operations, each at most 4H+3 events. Thus a normalization costs at most

    120V+50+2V(H+1)(2H+8)+2V²(4H+3)(2H+8)
    ≤250V²(H+1)² <1000V²(H+1)².

For the inequality use V≥1, 2H+8≤8(H+1), and 4H+3≤4(H+1). This pays even cache misses. Since 16N+10≤16D and D≤V, the corrected row subtotal is at most 2016NV²(H+1)²<T. Each law call emits at most L complete primitive records and an external MP one; using (L+1)T therefore safely bounds every generated record across the entire fresh store.

**Substitution, imports, references and every complete prefix.** Simultaneous template substitution is single-pass on schematic leaves, including q; it does not recurse into replacements even when their names coincide with schematic or auxiliary names. For a fixed record containing s operator nodes and v variable occurrences, including all declared substitution fields, the resulting count is at most s+vP_j≤S_jP_j. Native X has 4+2|A|+2|B| nodes and its literal image has 7+2|A|+2|B|; native/image P have respectively 3+|A|+|B| and 4+|A|+|B|. Hence the stated recurrence 8+4p and depth increments 3/6 cover both constructors. External MP conclusions are subformulas of instantiated implication records. The complete imported occurrences cost K_j nodes with maximum depth δ_j and I records; no supplied proof is shortened, deduplicated or iterated as a new input-size parameter.

`AppendProof` appends every record. Import at offset s maps every earlier reference r to s+r; fixed-template copying uses the explicit already-copied reference map. The law cache starts empty and can return only earlier records in this same store, so it cannot introduce uncharged premises or forward references. Each row finishes with a new MP, and export occurs immediately through that root. The writer includes every preceding record; the separate endpoint header repeats the already charged final formula. ASCII payloads need no JSON escapes and cost at most B+4 per syntax node. Fixed keys/rule names and at most two decimal references below J fit F_J. Consequently (4) bounds each full prefix and summing over N exports pays N copies of all supplied records and up to N copies of every generated record. Literal translation changes neither reference indices nor prefix membership. Writer caches return full identical spellings, not references or abbreviations.

The implementation's `(1+N+n).bit_length()` equals ceil(log₂(2+N+n)); `(J+1).bit_length()` equals ceil(log₂(J+2)). All ledger arguments are supplied dimensions, full received measurements or fixed-library constants; output measurements do not enter them. Since 2^h<2D, V=O(D³) and 4^H=O(D^18), while supplied counts, names and base-tree sizes are bounded by the explicit Q, the aggregate bounds are fixed polynomials in Q. Tables and root metadata have the separately stated polynomial cost. Direct copying, finite bit arithmetic and comparisons of these bounded strings admit polynomial abstract bit time, even with deep supplied trees implemented using explicit stacks. This does not claim freedom from Python, disk or memory limits.

**Meaningful bounded checks and verdict.** `python3 scripts/left-closure/audit_all_size.py` completely replays all fifteen fixed native laws and their literal images, checking every primitive/substitution/reference field and exact endpoint. `scripts/left-closure/output/audit-206.json` records all thirty complete stream measurements, with unchanged maxima L=3470, (D_native,S_native)=(19,2456), (D_image,S_image)=(27,3492), and no failures. A counting adapter also executes the actual `combine` traversal for all selected lengths 1 through 129: its two trees match the exact padded Bal endpoints and all exact operation counts equal 7(M−1)+(M−m). The first old-visit-bound failure is m=3: seven visits versus five, with 22 elementary operations versus the valid 48 allowance. The adapter emits no proofs, and these finite diagnostics do not establish the all-size inequalities; the proof above does.

The audit repairs two intermediate accounting errors within the unchanged polynomial bound and finds no further defect in the conditional all-size construction. This is local verification/reproduction, not certified novelty or progress beyond the checked sources toward SAT separation. It does not replay or certify any star/diamond coordinate export: zero star exports remain certified, and later prefixes, aggregate implementation checks, the actual-tree local recurrence bridge, coefficient/initial-output interfaces, whole receivers and all main-problem gaps remain open. Every interrupted artifact and prior complete test is preserved.

### Complete preserved star coordinate-0 replay, 2026-10-14 (step 207)

This bounded RESEARCH / implementation / REPRODUCTION attempt reuses the unchanged step-201 SPECIALIZE assessment. It replays only the existing step-205 coordinate-0 pair: no local input, compiler root or archive is regenerated. The all-size argument audited at step 206 and its precise Mohri/Metamath/LTW source qualifications are reused, not reproved or claimed novel. The downstream use is one completely checked coordinate input for L064, conditional on the supplied local recurrences. No other receiver premise follows.

**Practical parser and receiving repair.** `scripts/left-closure/native_parser.cpp` and `fast_syntax.py` replace only the native parser's intermediate Python tuple-tree construction. Recursive descent accepts precisely a nonempty ASCII alphanumeric/underscore variable, (~T), or (T>T), consuming each connective and closing parenthesis and requiring complete input consumption. Induction on the recursion gives the exact parsed syntax. A node is interned by its full tagged tuple: variable payload, negated child identifier, or ordered implication child identifiers. The unordered map resolves hash collisions by full tuple equality. Thus identifier equality is exact structural equality, not a hash assumption. Newly interned nodes are synchronized through the original Python node constructor, including its full expanded native/image node, depth and payload recurrences; matching indices are required. The original axiom reconstruction, exact MP, native formula/image field reconstruction, duplicate-field rejection and import/root comparisons in `audit_archives.scan` are retained. Proof membership therefore follows by the same primitive induction as above. The C parser explicitly rejects depth over 4096 as a practical resource limit; no all-input execution guarantee is inferred from this prototype.

A review found a real receiving defect in the legacy image comparison: Python dictionary/list equality identifies False and 0.0 with 0. Two complete malformed image streams are accepted by that legacy comparison. The strict adapter rejects every reference field in either format unless it is a two-element list of literal nonnegative integers, before reconstructing/comparing its record. Native MP still checks strictly earlier references; exact image comparison transfers those same integer references. Thus all image references also have the intended syntax and positions. This repairs a checker defect, not a mathematical proof rule or the receiver's hypotheses. The baseline diagnostic, repaired corruptions and complete validation are preserved.

`parser-validation-207-strict.json` records complete differential replay of all fifteen native/image fixed-law pairs, all three star local inputs and the entire empty coordinate-0 pair: all measurements and references agree with the original scanner. There are 485 accepted native syntax cases, fourteen rejected syntax cases and seventeen record/header rejection tests. Fifteen are rejected by both backends; the other two are the explicitly preserved legacy image-reference acceptances rejected by the repaired adapter. No fixed law is synthesized or inferred from these tests. The parser/primitive justification above, rather than finite testing alone, explains applicability.

Reproduction commands, relative to this notebook:

    clang++ -std=c++17 -O3 -shared -fPIC scripts/left-closure/native_parser.cpp -o scripts/left-closure/output/native_parser-207.so
    PYTHONDONTWRITEBYTECODE=1 python3 scripts/left-closure/replay_star.py validate
    PYTHONDONTWRITEBYTECODE=1 python3 scripts/left-closure/replay_star.py replay

The drivers refuse to overwrite their certificates; reproduction must use fresh output names or retain the existing evidence. The first pre-repair validation and interrupted replay remain at `parser-validation-207.json` and `replay-207-star-coordinate-0.json`. That first replay saved a progress checkpoint at 174999 paired records and KeyboardInterrupt, with no certified export. The repaired replay starts from the preserved archives' headers, covers every record and reaches EOF in both streams; it does not resume from an uncertified sample or trust the earlier progress count.

**Complete result.** `scripts/left-closure/output/replay-207-strict-star-coordinate-0.json` is complete with no failures and exactly one verified export pair. The scanner reconstructs every native axiom/MP and every literal-image formula/substitution/reference field, compares all 26858 retained local records against their exact source occurrences with relocated references, checks the externally reconstructed header and last coordinate endpoint, and requires equal native/image stream lengths. The final zero-based root is 1217746. With Y=(A→A) and a=P(A,Y), the exact endpoint is E(X(a,Y),X(Y,a)); the serialized endpoint is independently constructed from the original request, not accepted from a writer label.

| Format | Complete records | Uncompressed bytes | Maximum full-record nodes | Maximum full-field depth |
|---|---:|---:|---:|---:|
| Native | 1217747 | 30027917995 | 745120 | 39 |
| Literal image | 1217747 | 45525924076 | 1029660 | 53 |

The checker independently recomputes the original-input ledger using the complete local inputs and the fully validated fixed library. It agrees exactly with the saved ledger: I=26858, J=376124588351815706858 and H=57; full-field depths 39/53 are below 197/378. Every per-prefix line, full-record-node and byte inequality in (4) passes. The complete exact actual/required integers, full expanded formula/substitution node sums and goal sizes/depths are in the certificate. Both full-byte checker hashes equal the preserved writer sidecars: native e05c99b420ca1f07d76eceb5a71076035448258bbb66f1a4e6d8cefa0ee9e8ec and image 7778a78c759ff19228c3948328b84dca78664e53cd7e5c28175ec7367ee9244e. Hash agreement is an integrity check after primitive replay, not its replacement.

This establishes local complete-string evidence for coordinate 0 with three selected closure entries and a variable edge after constant closure, plus surviving beta, empty selections, coincident q/letter names and the retained unused deep input. It does not construct/replay coordinates 1/2, certify the whole-star aggregate/argument implementation tests or the preserved diamond. The actual-tree recurrence bridge, coefficient/initial-output interfaces, ordinary-input completeness, both complete receivers, the whole L055 candidate, certificate existence, ER/W/V/U and unrestricted SAT remain unresolved. No progress beyond the checked sources or main-problem candidate is claimed. PROOF.md and DAG.md are unchanged because the mathematical argument and direct inputs are unchanged.

### Complete fresh star coordinate-1 construction and replay, 2026-10-14 (step 208)

This bounded RESEARCH / implementation / REPRODUCTION attempt reuses the unchanged step-201 SPECIALIZE assessment, the step-206 all-size audit and step-207 strict parser validation. The precise Mohri/Metamath/LTW imports and their hypotheses/qualifications above remain unchanged. No semantic closure theorem is reproved and no novelty is claimed. The independently testable target is one additional closed-coordinate input for L064, conditional on the three supplied local recurrence proofs.

`python3 scripts/left-closure/run_star_coordinate_one.py` loads the original `star-205.request.json` and all three complete `star-205-local-v.native.jsonl.gz` occurrences. It checks their original exact endpoints, uses the existing fixed library, starts an empty append-only store/cache and compiles only `row(1)`. It never regenerates coordinate 0 or treats a generated coordinate package as input to its bound. The row is K₀(1,*)=(0,1,0), beta₁=0 and G₀(1,*)=(0,0,1). With Y=(A→A), Z=NOT Y and a=P(A,Y), the exact endpoint is therefore E(a,X(Z,a)). The fresh-store final zero-based root is 172140; different record indices from a sequential whole-star run are allowed because L064 imports complete independent packages and relocates each occurrence.

`replay_star.py:replay` now accepts an explicit coordinate, fresh destination and two archive paths; its default coordinate-0 invocation remains available. Only these selectors and completion labels change. The original source request, complete local inputs, independent finite-table/endpoint reconstruction, strict primitive/image scanner and independent original-input ledger calculation remain identical. Replay starts at both headers, processes every record and requires both EOFs; progress checkpoints never certify a prefix. Writer sidecars are used only for count/byte/hash agreement after primitive verification, not as a proof premise.

`construction-208-star-coordinate-1.json` and `replay-208-star-coordinate-1.json` are complete, with failures=[] and exactly one newly verified pair. All 26858 original local records, including the unused deep record, are retained and independently compared field by field at offsets 0,10653,16156, with all earlier references relocated. Every native axiom/MP and literal-image formula/substitution/reference field passes, and the independently reconstructed exact final endpoint matches.

| Format | Complete records | Uncompressed bytes | Maximum full-record nodes | Maximum full-field depth |
|---|---:|---:|---:|---:|
| Native | 172141 | 671347196 | 49776 | 37 |
| Literal image | 172141 | 991916441 | 67868 | 37 |

The independently reconstructed ledger agrees with both the original star-205 ledger and the fresh construction ledger: I=26858, J=376124588351815706858 and H=57. All line/record-node/byte bounds in (4) pass; the complete-field depths 37/37 are below 197/378. Every generated fixed-law argument was measured, with native/image maxima 158/215 nodes and 13/17 depth below the original-input thresholds P_j and 178/351. Every law invocation's structural argument height, including cache hits, is at most 4≤57; both complete normalization traces also stay at height ≤4. Full actual/required integers are saved in the two certificates. These finite checks supplement the audited all-size proof; the measured outputs do not define the thresholds.

Both checker full-byte hashes equal the writer sidecars: native e3a89f216e2716591415faa30c35d1913527f0724072f37338303117434cbbbb; image 806d6bbf3ce1263966f5d0e385a8ea49a8be8e592e59efa7fe3e12fdc9779436. Reproduction command, relative to this notebook, is `PYTHONDONTWRITEBYTECODE=1 python3 scripts/left-closure/run_star_coordinate_one.py`; fresh names are required because existing certificates/archives are preserved. The driver prints actual/required bounds and artifact paths; its complete log is `scripts/left-closure/output/run-208-star-coordinate-1.log`.

This establishes local implementation evidence for another conditional coordinate package, reproducing the already assessed operations. Together with step 207, two star coordinate pairs are certified in independent complete stores. It does not certify coordinate 2, a sequential whole-star aggregate or all-coordinate implementation check. The actual-tree local recurrence bridge, coefficient/initial-output interfaces, ordinary-input completeness, both whole receivers, whole L055, certificate existence, ER/W/V/U and unrestricted SAT transfer remain unresolved. PROOF.md and DAG.md are unchanged because neither the mathematical construction nor its direct inputs changed. Mathlib coverage remains as qualified below.

### Complete fresh star coordinate-2 construction and replay, 2026-10-14 (step 209)

This RESEARCH / implementation / REPRODUCTION attempt reuses the unchanged step-201 SPECIALIZE coverage, step-206 all-size audit and step-207 strict parser validation. The precise source citations, hypotheses and qualifications above remain applicable; neither a new semantic theorem nor certified novelty is claimed. The downstream use is the last independently certified star coordinate input for L064, conditional on the supplied exact local recurrence strings.

`run_star_coordinate_two.py` changes only step/coordinate/artifact selectors from the step-208 driver. It receives all three complete original `star-205-local-v.native.jsonl.gz` proofs and the original request, starts a fresh append-only store/cache and compiles only `row(2)`. Certified pairs 0/1 and all earlier interrupted artifacts remain untouched. The original finite tables give K₀(2,*)=(0,0,1), beta₂=1 and G₀(2,*)=(0,0,0). With Y=(A→A), Z=NOT Y and z=P(A,Z), the exact endpoint is E(Y,X(Y,z)); the nonempty one-letter list retains P(A,Z), rather than silently deleting it. The independently reconstructed endpoint matches both the header and last record at zero-based root 168368.

`construction-209-star-coordinate-2.json` and `replay-209-star-coordinate-2.json` are complete with failures=[] and one newly verified export pair. The strict scanner processes both streams from headers through EOF, checking every primitive axiom/MP and literal-image formula/substitution/reference field. All 26858 original local records, including the unused deep record, are retained and compared field by field at offsets 0,10653,16156 with relocated earlier references. No sampled prefix or sidecar substitutes for proof replay.

| Format | Complete records | Uncompressed bytes | Maximum full-record nodes | Maximum full-field depth |
|---|---:|---:|---:|---:|
| Native | 168369 | 473743050 | 38960 | 37 |
| Literal image | 168369 | 725003772 | 54348 | 38 |

The independent replay ledger equals the original star-205 and construction ledgers, with I=26858, J=376124588351815706858 and H=57. All per-prefix line/record-node/byte checks pass, and full-field depths are below 197/378. Every generated law argument, including cache hits, has structural height at most 4≤57. Both normalization traces stay at height ≤4. Native/image argument maxima are 134/185 nodes and 14/18 depth, below P_j and 178/351. Full actual/required integers are recorded in the certificates; thresholds use only original inputs and fixed-library constants, never generated-package lengths. These finite checks supplement the audited all-size proof.

Full-byte checker/writer hashes agree: native f44615c38794f9df12bc04b8caaa6a58976dd52ff11ceb647ed66ba09357b760; image bd9d6582a757f3978200c33c9c52ddd1ed37b784c614465bf153ee8b5963b1d4. Reproduction command: `PYTHONDONTWRITEBYTECODE=1 python3 scripts/left-closure/run_star_coordinate_two.py`, with fresh artifact selectors required to preserve existing evidence. The log is `scripts/left-closure/output/run-209-star-coordinate-2.log`; both certificates and archives are in that directory. All complete load-bearing certificate fields were inspected after completion.

All three star pairs now have separate complete replay certificates in independent stores. This step does not perform a whole-star aggregate/integration check or certify the preserved diamond. Actual-tree local recurrence construction, coefficient/initial-output interfaces, ordinary-input completeness, both whole receivers, whole L055, certificate existence, ER/W/V/U and unrestricted SAT transfer remain unresolved. This is local conditional implementation progress, not progress beyond the inspected sources toward SAT separation. PROOF.md and DAG.md remain unchanged because the argument and direct mathematical inputs did not change. Mathlib coverage remains as qualified below.

### Step 210: aggregate certified-package interface

The unchanged SPECIALIZE assessment authorizes this bounded RESEARCH / implementation / REPRODUCTION check. `scripts/left-closure/check_star_aggregate.py` composes the complete strict replay certificates from steps 207/208/209; it neither regenerates proof strings nor performs another primitive replay. This is additional local conditional implementation evidence, with no novelty or SAT consequence. The primary citations, qualifications, all-size proof and direct mathematical inputs above remain unchanged.

The checker consumes all three replay certificates in full, requires complete=true and failures=[], exactly one correctly indexed export per certificate, exact last-record roots, full input retention, literal correspondence and writer agreement. All three original local-input measurements (including complete-record hashes) and original-input ledgers must agree exactly with the original star-205 ledger. It independently reconstructs K₀, beta and G, and passes the fixed data to `chain.validate` with an explicitly empty terminal level solely to obtain L064's coordinate endpoint strings. These match all three L065 closed endpoints literally; the six current archive headers also match. Empty terminal data does not prove any zero row or execute a chain.

The certified measurement sums are:

| Format | Aggregate records | Aggregate uncompressed bytes | Aggregate full bits |
|---|---:|---:|---:|
| Native | 1558257 | 31173008241 | 249384065928 |
| Literal image | 1558257 | 47242844289 | 377942754312 |

These are compared to the unchanged original-input bounds NJ=1128373765055447120574 and NU_native=460458861453825943352642068377917435503439430827068544340768930, NU_image=890380451183873723165675692090771682119709074236080083195623270 bytes. Bits are checked against eight times those same bounds. The aggregate threshold is not recalculated in generated-package lengths. Each package retains 26858 original local records, hence 80574 retained local-record occurrences across the three packages in each format. Independent stores are permissible: no package uses a reference into another, and L064's importer relocates each complete occurrence.

The 6049-byte manifest `scripts/left-closure/output/interface-210-star.json` records exact endpoints, archives, replay-certificate hashes and the complete certified measurements. Its planned receiver starts are 0,1217747,1389888 and roots 1217746,1389887,1558256. These arithmetic locations describe the already proved L064 relocation interface, not an executed receiver import. Five corrupted manifests—missing coordinate, swapped coordinates, wrong endpoint, wrong root and absent image—are rejected. This does not substitute for earlier primitive rejection/replay tests.

The full replay record-node and full-field-depth maxima also bound every serialized substitution field below the original-input argument thresholds. For coordinates 1/2, the separately checked construction call/cache traces remain as recorded above. Coordinate 0's interrupted construction did not save those traces, so no retrospective structural-height/cache-call check is claimed. The audited all-size proof still covers that construction mathematically. Current archive headers and writer measurements are compared, but archive contents are not rehashed this turn: complete primitive verification is reused from the precise unchanged prior replay certificates, whose hashes are bound into the new manifest. A preview or a writer sidecar is not newly treated as proof.

The complete result is `scripts/left-closure/output/aggregate-210-star.json`, with failures=[]; it records actual/required bounds, receiving endpoints, retained input counts, five rejections and the foregoing limitations. Reproduction: `PYTHONDONTWRITEBYTECODE=1 python3 scripts/left-closure/check_star_aggregate.py`, using fresh destination/manifest selectors to preserve existing evidence. Actual receiver import/full-chain execution, actual-tree local recurrence construction, coefficient/initial-output interfaces, ordinary-input completeness, whole L055 and certificate existence/ER/W/V/U/SAT transfer remain unresolved. PROOF.md and DAG.md are unchanged because the mathematical argument and dependencies did not change. Mathlib coverage remains qualified below.

## Mathlib

Full matching native closure-coordinate/compiler coverage has not been checked. Metamath fixed logical laws and Mohri's semantic closure are source inputs, not Mathlib coverage. Unknown coverage is not absence or novelty.
