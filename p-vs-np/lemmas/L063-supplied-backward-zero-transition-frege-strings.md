# L063 — Complete supplied backward-zero transition strings

## Hypotheses

Use L056's assumption-free native ax-1/2/3 and MP calculus, simultaneous substitution, and fully expanded formulas

    X(A,B)=((A→B)→NOT(B→A)), E(A,B)=NOT X(A,B),
    P(A,B)=NOT(A→NOT B), Y=(q→q), Z=NOT(q→q).

q is a paid ordinary free variable. All names are nonempty ASCII alphanumeric/underscore payloads. Receive native proofs only. The image τ preserves NOT and sends A→B to NOT τ(A) OR τ(B), including every double negation. No assertion about arbitrary independently supplied NOT/OR proofs is made.

For an ordered explicit list, Bal([])=Z and Bal([A])=A. A list of length at least two is right-padded with Z to the least power-of-two capacity and combined by the perfect ordered X tree. W(a;T) is Bal of the terms T_v with bit a_v=1, in increasing index order. No bit variable or scalar gate is introduced.

Receive N≥2 identical fully written suffix trees S_v at both levels; an ordered alphabet of n≥0 variable occurrences x_b; 0≤k≤N; and actual dimensioned bit arrays

    β:N×1, G_b:N×N, r:1×N, R_next:k×N, T_b:1×k.

All entries are literal bits. Empty arrays keep their dimensions. Check rβ=0 and rG_b=T_bR_next for every b by explicit F₂ arithmetic. Neither a basis, formal-zero/PIT answer nor an UNSAT assertion is a proof premise.

Receive all N complete assumption-free coordinate packages, including unused/deep records, with exact declared and actual final endpoint

    E(S_v, X(Β_v, Bal([P(x_b,W((G_b)_v;S)):0≤b<n]))),

where Β_v=Y or Z according to β_v. All n letter slots occur. Receive all k complete next-row packages ending exactly E(L_j,Z), where L_j=W((R_next)_j;S), including unused rows. No proofs of the three intermediate goals below are received. No coordinate existence or closure/basis construction is asserted.

Use precisely the fourteen fixed laws specified by `scripts/backward-zero/endpoints.py:fixed`, with checked complete native strings and checked literal images: refl, symm, trans, congL, congR, assoc, comm, cancel, zero_slots, dist, prod_cong, zeroR, zeroL, prod_zero. This is a fixed-library hypothesis; arbitrary caller libraries or prepopulated proof caches are excluded. L056–L058 establish the relevant copying operations; the three extra fixed zero laws have their own full checked streams. All term/name data, proof records, tables and their framing are explicit input.

## Conclusion

The fresh append-only construction in `scripts/backward-zero/build.py:compile_one` produces checked earlier records for

    E(L(r),Q7), E(Q7,Q8), E(Q8,Z),

and an actual final record E(L(r),Z), where

    L(r)=W(r;S),
    Q7=Bal([P(x_b,W(rG_b;S)):0≤b<n]),
    Q8=Bal([P(x_b,W(T_b;[L_j:0≤j<k])):0≤b<n]).

All abbreviations are expanded in every serialized occurrence. Every supplied record is retained exactly once with relocated earlier references. The entire output has a line-by-line literal NOT/OR image in the translated axiom/MP calculus.

L062 equation (1), with its complete fixed-library and supplied-input constants, bounds lines, depths, record nodes, full uncompressed bytes and abstract bit time by one fixed polynomial in the full explicit input. No measured output size is an input to that bound. The separate step-196 critical audit below verifies this conditional construction and ledger without a substantive defect. This is a conditional local receiver component reproducing known logic, without certified originality, coordinate/certificate existence, ordinary-input completeness, iteration, a complete L055 receiver or a SAT consequence. L055 remains an UNVERIFIED CANDIDATE.

## Proof

### Known inputs and why this specialization is needed

The unchanged step-191 SPECIALIZE assessment `drafts/literature/2026-10-12-backward-zero-transition-primitive-strings.md` covers precisely these hypotheses and syntax. Reuse L056's primitive copying and slot operations, L057's single-left-factor distribution/product congruence, L058's full import/balanced combination, and L062's successive-cut/resource proof. L055 motivates the target; its receiver conclusion is not a premise. L059's guarded endpoint is not used.

The precise primary logical inputs are the classical Church P2/Lukasiewicz system in [Proof Explorer §§1.2–1.2.2](https://us.metamath.org/mpeuni/mmtheorems1.html), [xorbi12i](https://us.metamath.org/mpeuni/xorbi12i.html) with both equivalence hypotheses, closed [xordi](https://us.metamath.org/mpeuni/xordi.html), and closed [anbi2](https://us.metamath.org/mpeuni/anbi2.html) with its equivalence antecedent. Retain the component assessments' inspected 2026-10-11/12 live-page qualifications: no pinned or recursively checked set.mm revision is claimed. Source XOR has a double-negation difference; the checked native strings implement the laws rather than emitting source labels or definition axioms. Completeness is used only for the fourteen fixed finite laws, never a growing row tautology.

The coefficient mechanism is motivated by Li–Tzameret–Wang, *Characterizing Propositional Proofs as Non-Commutative Formulas*, arXiv:1412.8746v4, Definition 4.13/Lemma 4.15, printed pp.32–35, and Kiefer, *Notes on Equivalence and Minimization of Weighted Automata*, arXiv:2009.01217v1, Algorithms 1–2 and Propositions 2.1–2.2/3.1, pp.1–5. Their inspected hypotheses and empty cases are recorded in the assessment. No coefficient-space existence theorem is invoked here: the tables and all coordinate proofs are received. The specialization is the paid literal syntax/complete-record assembly those statements do not provide; no theorem-level reproof is needed.

### Reception and paid logical operations

`endpoints.py:request` independently reconstructs all endpoints and verifies the bit identities/dimensions. `aggregate.load` checks each complete native package, then parses every record and substitution, requires native headers and exact endpoint, rejects duplicate fields/assumptions/invalid references, and compares stability between reads. Import reconstructs each schema instance and MP with earlier relocated references. A package beginning at s maps its i-th record to s+i; the subsequent field-by-field comparison proves full retention, including unused records. Hashes record integrity; induction on each actual inference establishes proof membership. These are exactly L058's complete-import conditions.

The proof state starts empty. A fixed instance simultaneously substitutes native argument trees into every template formula and declared axiom substitution, reconstructing all MPs with explicit relocated references. An already copied instance can be referenced from a cache local to this state; no external proof is supplied by that cache. Simultaneous substitution does not recurse into replacements, so coincident names cause no capture. Unsubstituted library auxiliaries are paid ordinary free variables.

`combine` proves E(Bal(U),Bal(V)) from explicit earlier E(U_i,V_i). Empty lists use refl(Z); singletons use the supplied reference. For longer lists, append paired Z slots with refl(Z) and recursively use congL, congR and trans at each binary node as in L058. No child equivalence becomes a substituted term. The result preserves the exact selected order and padding in both lists.

### A literal normal form with paid zero and permutation operations

Tags distinguish occurrences independently of formula spelling. Y has key (0); suffix S_v has (1,v); P(x_b,S_v) has (2,b,v); letters used as left factors have (3,b); Z has (9). A key determines its exact underlying native tree. Different suffix or letter indices may spell identical formulas and are still retained separately; this deliberate refinement suffices for the checked coefficient comparison. Tags introduce no propositional name or definition. Erasing a product annotation is permitted only when its underlying native tree is literally unchanged.

Consider a coordinate/row expression admitted here: X trees over Y,Z, tagged suffixes and products with one atomic left letter and an X tree of suffixes/Z on the right. `expand` proves equivalence to an X tree of atoms. At each product with an X right child use dist, recursively expand both resulting products, combine their proofs by XOR congruence, then compose by trans. At a right Z use prod_zero. At a suffix leaf tag the identical fully expanded product and use refl. Original X nodes use the two child equivalences. Induction gives the exact expanded tree with an actual primitive proof; no semantic equality of distinct suffixes is tested.

Each `erase_zeros` traversal first combines the two child proofs, then contracts an actual Z child with zeroR or zeroL and trans. If both children are Z, either law gives Z. Thus it produces the tree obtained by deleting Z occurrences and suppressing unary X vertices, or the single Z if no occurrence survives, with a paid equivalence.

After expansion, let m≥1 be its number of atomic occurrences and M the least power of two ≥m. If m<M, append an unpadded near-balanced X tree of exactly M−m Z occurrences. Prove that added tree equals Z by `erase_zeros`, use the symmetry of zeroR to introduce X(old,Z), then congruence and trans to replace the right Z with the actual padding tree. L062's `split`/reassociation proves equivalence to the perfect M-slot tree in the same occurrence order. No parenthesization is assumed equal for free.

Insertion sort compares the finite occurrence keys. Each adjacent exchange uses L056's paid exposure, commutativity, context lifting, cumulative transitivity and inverse rotations; it restores the perfect M-slot shape. Thus equal non-Z atoms form contiguous groups. Scan each such group left to right, replacing each consecutive equal pair by Z,Z with cancel followed by zero_slots. The scan retains one atom exactly when the original multiplicity is odd; this is immediate for a group of length 2a or 2a+1 after its a pair operations. Z's own multiplicity is irrelevant. The second insertion sort puts surviving atoms in increasing key order followed by all Z slots.

Erase zero slots with paid laws. The result `slim` has exactly the sorted odd-multiplicity atoms and some induced bracketing. Independently construct their requested Bal and erase its explicit right padding to obtain `compact` with the same ordered atoms. If there are none, both are the single Z. Otherwise L062's target-boundary `match` gives E(slim,compact), including nonperfect target shapes. Symmetrize the paid erasure of the requested Bal and compose all equivalences. Hence `normalize` proves equivalence to exactly Bal of sorted odd-multiplicity non-Z atoms, with the empty convention Z. Every operation is one of the assessed fixed laws or its paid context/MP composition.

In particular `compare(A,B)` is valid whenever these parity data agree: both normalizations have literally identical output tags/native trees, so symmetry and trans give E(A,B). This is an arithmetic/syntactic precondition checked using supplied bits; it is never a Frege axiom or an external identity oracle.

### First endpoint, including constant parity and empty r

Select coordinate packages with r_v=1 and apply `combine`. Its left endpoint is exactly L(r), and its right endpoint C is Bal of the corresponding complete coordinate right sides; an empty selection gives Z,Z. In C, the multiplicity parity of Y is Σ_v r_vβ_v=0. For every (b,w), the parity of P(x_b,S_w) is Σ_v r_v(G_b)_(v,w)=(rG_b)_w. All other expanded occurrences are Z. In Q7 the same product atom occurs once exactly when (rG_b)_w=1, and any other occurrence is explicit padding/product-zero. Its Y multiplicity is zero. Thus the two normal forms agree, even if n=0, a row selects nothing, or distinct suffixes spell the same formula. `compare(C,Q7)` gives an earlier E(C,Q7); trans with the coordinate-combination record gives E(L(r),Q7).

### Second endpoint and actual next-row use

In Q8, expansion of the selected L_j trees gives, for each (b,w), product multiplicity parity Σ_j(T_b)_j(R_next)_(j,w). The checked equality rG_b=T_bR_next makes this the same as in Q7. Neither side has a Y atom at this tagged level: even a suffix that literally spells Y remains the unchanged tagged S_w on both sides. Thus `compare(Q7,Q8)` gives exactly E(Q7,Q8), with all nested selection padding/distribution/flattening paid as above. Empty k and n are included.

For each b, `combine` the actual earlier next-row records selected by T_b. It gives E(W(T_b;[L_j]), Bal of the corresponding Z slots). Erase that zero list to Z and compose. Apply prod_cong with left factor x_b and then prod_zero to get E(P(x_b,W(T_b;[L_j])),Z). These MPs reference the received next-row conclusions; no guard is dropped and no (7)/(8) premise is received. Empty selection uses refl(Z), with the same subsequent operations. Combining all n resulting product proofs and erasing the outer zero list gives E(Q8,Z). For n=0 all these terms are exactly Z and the proof uses its paid reflexivity/composition.

Finally trans combines E(Q7,Q8) with E(Q8,Z), then E(L(r),Q7) with that result. The last appended MP has endpoint E(L(r),Z). `compile_one` checks each of the four recorded roots against the independently reconstructed expanded strings and checks that the final root is the actual last record. All references are earlier by append-only induction.

### Uniform copying bound and literal image

All operations, terms and inputs above satisfy L062's prototype hypotheses. In its notation D=2+N+n+k, h=ceil(log₂D), V=2^(3h+4), H=9h+20, E₀=10000V²(H+1)², G=(L+1)E₀, J=I+G, and P_j=8·4^(H+1)(t_j+1). Its successive-cut invariant bounds temporary reassociation heights rather than accumulating one height increase per split. It separately charges the restored perfect slot operations, all four normalizations, coordinate/next-row combinations and final MPs. Equation (1) therefore applies to this whole output, not just one component:

    lines ≤ J,
    depth ≤ max(δ_j,D_j+c_jH+d_j),
    record nodes ≤ max(K_j,S_jP_j),
    bytes ≤ (B+4)[K_j+(G+1)S_jP_j]+(J+2)[256+64 ceil(log₂(J+2))].

I,K_j,δ_j describe all imported records; t_j,d_j describe written suffixes, letters,Y,Z; B includes supplied and library names. D_j,S_j,L are maxima from the entire checked fourteen-law library. No old sublibrary maximum is substituted for a newly enlarged library. `scripts/backward-zero/ledger.py` implements these formulas with integer bit lengths for exact ceilings, using input/library statistics only. The finite actual-event bound is kept separately and does not justify this uniform bound. Depth of an unused supplied line remains in δ_j, never in the added structural-height exponent.

The full native serialized output copies every formula/substitution occurrence even when Python tuples share storage. Translating every native record, substitution and header by τ preserves each translated axiom instance and exact MP antecedent/consequent; reference indices are unchanged. This gives the entire literal image, with nodes/depth/names charged in its own j-format bound. The output has polynomial abstract bit time by L062's full copying/checking argument; particular interpreter recursion/resource limits remain a practical qualification, not an all-input execution claim.

### Bounded evidence and review status

Reproduce the new discriminator streams with `python3 scripts/backward-zero/run_remaining.py`, then check fixed-library correspondence with `python3 scripts/backward-zero/check_library_images.py`. The complete certificates are `scripts/backward-zero/output/certificate-194.json` and `library-images-194.json`; actual/required thresholds and paths are also in `certificate-194-summary.json` and `run-194.log`. Every new output record is checked by the independent primitive checker, including declared axiom substitutions and earlier MP references. The three earlier requested roots and actual last record are compared with independent endpoint reconstruction in both formats. Writer/checker uncompressed bytes and hashes agree; hashes alone are not proof checks.

All three new cases and six complete streams pass, with no failures:

| Case | Lines in each format | Native/image depth (actual / uniform required) | Native/image uncompressed bytes |
| --- | ---: | --- | --- |
| Three-term selection, N=3,n=0,k=1 | 134440 | 28/161; 39/310 | 718287741; 1072294119 |
| r=0 with retained unused deep inputs | 60647 | 37/161; 37/310 | 55359593; 79329974 |
| T=[1], R_next=[1,0], rG=[1,0] | 65389 | 22/161; 30/310 | 65270588; 91535858 |

The complete certificates contain each exact uniform line/node/byte threshold from the displayed formula; every inequality passes, as do argument-size/depth and skeleton-height checks. The very loose polynomial majorants are mathematical upper bounds, not practical efficiency or optimality claims. The fourteen fixed laws are checked in both formats, and `library-images-194.json` compares every header, formula, substitution, rule and reference with the literal image of its native record. Their newly measured full-library constants are L=3470, (D_native,S_native)=(18,2456), (D_image,S_image)=(25,3492). Equality with older component constants is a measured result, not an inherited assumption.

Step 192's three completed cases/six full streams already cover empty alphabet, k=0 and a genuine coefficient cancellation with repeated suffixes, coincident names and deep unused records; its thirteen malformed receptions are recorded in `certificate-192-summary.json`. This step reuses that complete evidence rather than reporting new rejection tests or rechecking those large outputs. Historical certificates and the interrupted larger k=2/nonzero-T fixture are unchanged. The new used-next-row case has a singleton nonzero selected row; the old larger fixture remains interrupted and is not counted as passed. Nonzero-β cancellation is covered by the general parity argument, without a new completed fixture claim.

No finite test alone establishes the general construction or L062's bound. The separate critical review required at step 194 is recorded next. Full iteration, whole-receiver/ordinary-input completeness, coordinate/certificate existence and all main-problem gaps remain unresolved.

### Independent critical audit, 2026-10-13 (step 196)

This audit uses the unchanged joint SPECIALIZE assessment `drafts/literature/2026-10-12-backward-zero-transition-critical-audit.md` and its reused primary citations. It checks the complete canonical arguments of L062/L063 against the actual endpoint constructor, emitter, complete importer, primitive operations, serializer and ledger. The relevant L056/L057/L058 proofs and prior audit qualifications were inspected. There is no new theorem-level source claim or certified novelty.

**Reception and normalization.** `request` requires literal integer bits with all row/column dimensions, enforces 0≤k≤N, and checks both finite identities. Suffixes are parsed native formulas; letters and q are ASCII variable names. The importer separately checks all exact native endpoints, every axiom substitution and strictly earlier MP, including unused lines, before copying. Fresh append-only state prevents an external cache from supplying an unpaid proof. Substitution is simultaneous, including q: replacement trees are not recursively resubstituted when names coincide. Local cache hits refer only to already copied records.

The ordered tags refine formula spelling: equal suffix formulas with different indices stay distinct, whereas every occurrence of one (b,w) product has the identical full native tree. `expand` distributes only through actual right X nodes, contracts right Z by prod_zero, and changes a product to an atom only after literal native-tree equality. Sorting orders these keys; cancelling disjoint consecutive equal pairs removes exactly an even multiplicity. Padding introduces an explicitly proved zero tree, with exactly the missing number of leaves even when that number is not a power of two. The second sort and paid zero deletion leave the ordered odd-multiplicity atoms. Matching the compact requested tree and reversing its paid padding removal therefore returns exactly the specified Bal, not just an equivalent bracketing. L062's audited cut invariant covers this nonperfect match.

For the first comparison the only Y occurrences have parity rβ, and each tagged product has parity (rG_b)_w. Thus rβ=0 removes Y and the normal forms of C and Q7 agree. In particular a nonzero β with an even selected parity is covered by this argument without requiring every selected β_v=0. For the second comparison, the corresponding Q8 parity is Σ_j(T_b)_j(R_next)_(j,w), so the checked matrix identity supplies precisely the same ordered atoms. A suffix spelling Y or Z remains an opaque suffix tag at both endpoints; its internal shape does not invalidate this parity reasoning. These two comparisons require neither a formal-zero oracle nor semantic identification of different suffixes.

**Actual next-row inference and boundary cases.** The b-th combination receives exactly the earlier records `inputs[N+j]` for selected j. It first proves equality of the selected L_j sum with the equally padded zero sum; paid erasure, product congruence and prod_zero then give the b-th product zero. Outer combination and erasure give E(Q8,Z). Both MPs of every transitivity use explicit earlier premises. Empty r, n or k use the literal Bal([])=Z branch; k=0 also forces rG_b=0 by the checked identity. No received Q7/Q8 proof or L059 guarded premise is substituted for this inference. The final two compositions end in the required E(L(r),Z), and the implementation enforces that its last MP is the actual last record. L062's audited uniform estimate covers this whole procedure, including all imports and four normalizations.

**Independent complete record checks.** The archive-only auditor is `scripts/backward-zero/audit_archives.py`; its complete result is `scripts/backward-zero/output/audit-196.json`. It imports the endpoint constructor, not the emitter, for positive primitive replay. Its second primitive checker parses the declared native substitutions and reconstructs exactly ax-1/2/3. Interned syntax nodes are merely a checker representation: each native formula must equal the fully expanded reconstructed string, and MP must use the exact earlier antecedent and implication before returning its consequent. For each row, the entire image formula, all substitution fields, rule and references must equal its literal translation. Induction on records proves membership; hashes are compared only after these checks. Node/depth recurrences count repeated child occurrences, so internal interning provides no proof-size credit.

All fourteen laws in both formats pass both this reconstruction and the original independently written primitive checker, with identical complete measurements. The maxima are again L=3470, native D/S=18/2456 and image D/S=25/3492. Every supplied coordinate/next-row package for the six completed fixtures is checked in full. Every imported output-prefix record equals its complete source record with the precise offset added to references. All twelve transition streams match every saved measurement, all four independently rebuilt endpoints and their literal images; final roots are actual last records. For nonzero T, backward traversal of actual MP references places every selected next-row root in the Q8-zero ancestry; the used-next-row fixture includes received root 31693. This is an ancestry check on full records, not an interpretation of trace labels.

All six cases pass independently recomputed input-only line/depth/node/byte thresholds. For the nonpower case the actual/required line count is 134440/5366819334389812066; depths are 28/161 and 39/310. Its native/image bytes are 718287741/208859828742058328017197470162980324181233089720873254 and 1072294119/356354326694104730343348647789459624119839678072676539. These loose majorants are not practical-efficiency claims. Exact bounds for every case are in the complete certificate. All thirteen recorded malformed requests/packages are rejected again by the actual receiver with their recorded reasons; the full geometry replay is documented in L062.

The initial auditor occupied the generic Python module name `endpoints`, causing an AttributeError when its later rejection checks loaded the receiver. This was an audit-harness integration failure, after all positive archive replays had completed, not a proof failure. The auditor now loads that module under a private name. The original partial certificate/log are retained as `audit-196-initial.json` and `audit-196-initial.log`; `audit-196.json` retains the harness failure and the completed same-step replay, and `audit-196-finish.log` records resumed reception/geometry checks. The final mathematical-check failures list is empty. The ordinary reproduction command runs the corrected audit from the beginning without emitting proofs.

**Verdict and limitations.** No substantive endpoint, reference, hypothesis or uniform-bound defect was found. The conditional single-transition component survives independent informal review, with complete finite evidence and the audited all-size argument kept distinct. This is local verification/reproduction, not progress beyond the checked sources on P versus NP. The interrupted larger k=2 fixture remains unpassed; no new nonzero-β fixture is claimed. No planner-call-trace reconstruction, independently supplied ordinary-input completeness, coordinate construction, iteration bound, full L055 receiver, certificate existence or SAT consequence is certified. Mathlib coverage and source-version qualifications remain as stated.

## Mathlib

Full matching Mathlib coverage for this exact supplied-transition compiler, primitive strings and binary ledger is **not checked**; no absence claim is made. Supporting field/linear-algebra theorems do not certify the emitted primitive records. The primary logical/coefficient citations, native receiving restriction and literal-image qualifications above remain essential. Python primitive checks and this informal proof are not Lean verification.
