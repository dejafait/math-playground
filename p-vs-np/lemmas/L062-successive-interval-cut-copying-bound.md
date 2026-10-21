# L062 — Successive interval cuts and the backward-zero copying bound

## Hypotheses

An ordered full binary X tree has explicitly distinguished leaf occurrences, even when their supplied native formulas coincide. Its structural height counts X vertices above those formulas; a leaf has height zero. Let T and U have the same m≥1 ordered occurrences, with heights h₀ and g. `split(T,k)`, for 0<k<m, is exactly `Rewrite.split` in `scripts/backward-zero/build.py`: recurse into the child containing the cut, then rotate once at the root; do nothing when the cut is already the root cut. `match(T,U)` splits at U's root cut and recursively matches its two children, left first. `rebalance` is this procedure with the perfect target and power-of-two m.

Use L056's native X,E, primitive ax-1/2/3/MP basis, simultaneous substitution and checked associativity, symmetry, reflexivity, congruence and transitivity strings. All leaves are fully copied, without a formula DAG abbreviation. The image τ is the literal NOT/OR translation, including double negations. The rewriter starts with fresh proof state and may cache only already copied fixed instances.

For the application to one backward-zero transition, receive the exact native-input contract in `drafts/literature/2026-10-12-backward-zero-transition-primitive-strings.md`: N≥2, n≥0, 0≤k≤N, all suffix/letter/name strings, dimensioned bit tables, every complete coordinate and next-row package including unused lines, and identical suffixes at both levels. The checks rβ=0 and rG_b=T_bR_next are explicit finite checks. They do not supply a missing coordinate proof. The template library is fixed and consists of the fourteen exact laws in `scripts/backward-zero/endpoints.py:fixed`; each is received with a checked complete native proof and its literal image. In particular the three zero laws have their own checked strings. An arbitrary unchecked caller library is excluded.

Let L≥1 be the maximum template line count. For format j, let D_j and S_j bound the depth and total nodes of one complete library record, counting its axiom substitution fields. These constants must be measured on the entire enlarged library; they are not inferred from an older sublibrary. Let I be the total number of supplied proof records, K_j their total formula/substitution nodes, and δ_j their maximum depth. Let t_j≥1,d_j bound the nodes/depth of every supplied suffix, letter, Y and Z in format j. Let B≥1 bound every ASCII alphanumeric/underscore variable payload, including library auxiliaries. All input syntax, tables and proof records contribute to the uncompressed input length Q.

## Conclusion

At every point of `match`, the current tree has structural height at most

    H₀=h₀+g+1,

and at most R₀=(m−1)h₀ rotations occur. At entry to a recursive target interval J, the current subtree is exactly the original T restricted to J, deleting absent leaves and suppressing unary vertices. Every rotation has a paid primitive equality, including its context lifts and cumulative transitivity. This gives complete native and literal-image proofs of E(T,U). With arbitrary h₀,g the following bounds are exponential in their sum, not claimed polynomial in m alone:

    J₀={1+R₀(2H₀+8)}(L+2),
    P₀,j=8·4^(H₀+1)(t_j+1).

There are at most J₀ records, depth at most D_j+c_jH₀+d_j, and bytes at most

    (J₀+2)[(B+4)S_jP₀,j+256+64 ceil(log₂(J₀+2))],

where c_native=3 and c_image=6. In particular logarithmic source and target heights give one fixed polynomial full-bit/time bound.

For the exact backward-zero prototype, set

    D=2+N+n+k,  h=ceil(log₂D),  a=3h+2,
    V=2^(3h+4),  H=9h+20,
    E₀=10000 V²(H+1)²,  G=(L+1)E₀,  J=I+G,
    P_j=8·4^(H+1)(t_j+1),
    F_J=256+64 ceil(log₂(J+2)).

Every generated record in one `compile_one` run, and any complete output it produces, obeys the uniform bounds

    lines ≤ J,
    depth ≤ max(δ_j,D_j+c_jH+d_j),
    record nodes ≤ max(K_j,S_jP_j),
    bytes ≤ (B+4)[K_j+(G+1)S_jP_j]+(J+2)F_J.       (1)

Full bits are eight times these byte bounds. Parsing, copying, checking and serialization admit polynomial bit time in Q, including deep supplied proofs and unused records. Formula depth is not multiplied by I or by the number of induction steps. These are abstract algorithm bounds; Python recursion/resource limits are not all-input execution guarantees.

This closes the prototype's missing height/copying estimate. It is **not** a correctness audit of every transition endpoint or a report that the pending discriminator streams have passed. It does not assert ordinary-input completeness, iteration, a complete L055 receiver, coordinate/certificate existence, or a SAT consequence. L055 remains an unverified candidate. No originality beyond the sources checked is certified.

## Proof

### Known inputs and specialization

The unchanged step-191 SPECIALIZE assessment covers this construction/accounting difference. L056 supplies the actual associative/congruence primitive strings and the restored-slot exchange/cancellation bound; L057 supplies distribution and product congruence; L058 supplies the complete-import/reference argument and balanced coordinate combination. Their primary logical references are the named Church P2/Lukasiewicz classical system in [Metamath Proof Explorer §§1.2–1.2.2](https://us.metamath.org/mpeuni/mmtheorems1.html), [xorbi12i](https://us.metamath.org/mpeuni/xorbi12i.html) with both equivalence hypotheses, closed [xordi](https://us.metamath.org/mpeuni/xordi.html), and closed [anbi2](https://us.metamath.org/mpeuni/anbi2.html) with its equivalence antecedent. Reuse their inspected 2026-10-11/12 live-page qualifications: these are not a pinned or recursively verified set.mm database. Source XOR differs by double negation; the paid native strings, not source theorem labels, implement the operations.

There is no new source theorem reproof or invocation of completeness for growing formulas here. The additional proof is required to bound the *sequence* of cuts in this concrete implementation. A single-cut or single-slot estimate alone does not imply it. LTW's coefficient-space results motivate the receiver but are not premises of this syntactic resource argument. No L055 conclusion, L059 guard premise or cross-notebook input is used.

### Restrictions and a single cut

For a nonempty set J of consecutive occurrence indices, define T|J recursively: discard a leaf outside J; retain a leaf inside J; at an internal node retain both nonempty child restrictions with their X parent, or retain the sole nonempty child without that parent. Restriction never increases height or reorders leaves. If J'⊆J, then (T|J)|J'=T|J'. To prove composition, induct on T. At a leaf both sides make the same retain/discard decision. At an internal node each child agrees by induction. If both remain nonempty both sides keep the parent; if one or both disappear both sides perform the same suppression. This also proves the claim when an entire original child was discarded in the first restriction. Occurrence indices prevent equal formulas from being identified.

For any nontrivial cut k, `split` returns

    X(T|[0,k),T|[k,m)),                              (2)

with indices understood in T's order. Prove simultaneously (2), a bound of h(T) rotations, and a bound of h(T)+1 on every intermediate height, by induction on T. Write T=X(A,C) with ℓ leaves in A. For k=ℓ no change is made, and (2) already holds. For k<ℓ, the recursive call splits A into X(A₁,A₂), its prefix/suffix restrictions. Its intermediates have height ≤h(A)+1 by induction, so after adjoining the unchanged C their heights are ≤h(T)+1. The final right rotation gives X(A₁,X(A₂,C)). Its two children are exactly the two restrictions in (2); each has height ≤h(T), so the result again has height ≤h(T)+1. The number of rotations is at most h(A)+1≤h(T). For k>ℓ, split C into X(C₁,C₂), then rotate left to X(X(A,C₁),C₂). The same restrictions, count and height statements follow with the children interchanged. In both cases the recursion descends into a strictly smaller nonempty tree and both output intervals are nonempty.

### Successive cuts, including partially processed siblings

At the initial call the subtree is T=T|[0,m). Suppose the recursive target interval is J and its unprocessed subtree equals T|J. Apply (2) at the target's split. Its children are restrictions of T|J, hence the original restrictions T|J_left and T|J_right by composition. Recursing into the left child cannot modify the right sibling, and vice versa. Thus the stated entry invariant holds for every call, independent of how many cuts have already occurred. At a target leaf it gives that exact original occurrence. Induction over target nodes proves the final tree is U. No repeated height-increase estimate is accumulated across target levels.

Every unprocessed interval restriction has height ≤h₀. During its active single split the height is ≤h₀+1. Its already fixed target ancestors have depth ≤g. Completed sibling subtrees have their target shape and global depth ≤g; pending sibling subtrees are original restrictions beneath target ancestors and have global depth ≤g+h₀. Consequently **all** current whole trees, including those between the recursive cut and the rotation at its parent, have height ≤g+h₀+1. There are m−1 target internal nodes. Each invokes one split on a restriction of height ≤h₀, proving the total bound R₀. Perfectness is unnecessary; nonpower compacted target shapes satisfy the same proof.

### Primitive strings for reassociation

Start with paid reflexivity E(T,T). A rotation uses the associativity instance with its actual three subtrees; the reverse direction additionally uses symmetry and MP. Lift its local equality through the actual X ancestors with congL or congR and one MP each. Use transitivity with arguments initial whole tree, previous whole tree and next whole tree, followed by two MPs. All premises are explicit earlier records. Every argument is an actual subtree or a whole tree of height ≤H₀. Earlier equality formulas and proofs never become new leaf terms. This proves primitive membership and the endpoint by induction over events, including zero events and m=1.

A rotation uses at most three template/MP operations locally, at most 2H₀ in lifting and three in transitivity. Allow 2H₀+8, plus initial reflexivity. Each template operation copies at most L records and each external MP contributes one, giving J₀. Caching an instance already copied in this same append-only proof only reduces these costs. There is no uncharged external cache.

Native X has 4+2|A|+2|C| nodes and adds at most three depth levels; its image has 7+2|τA|+2|τC| nodes and adds at most six. Thus the structural recurrence p_(i+1)≤8+4p_i, p_0≤t_j, gives the displayed P₀,j bound. Substituting actual arguments into a library record with at most S_j nodes, including all its substitution fields, costs at most S_jP₀,j nodes and depth D_j+c_jH₀+d_j. MP conclusions are subformulas of the copied implication record. Variable occurrences cost at most B bytes and punctuation at most three per node; B+4 suffices. Reference/rule/framing fields fit 256+64 ceil(log₂(J₀+2)). The header repeats the endpoint and is covered by J₀+2. This proves the first ledger and its literal-image counterpart. The construction explicitly pays every copy rather than invoking associativity as a new proof rule.

### Application: a global argument-height bound for the prototype

Each selected/padded range over suffixes, coordinates, letters or next rows adds at most h X levels, including empty and singleton ranges. The largest initial tagged skeleton is the selected sum of coordinate right sides: outer selection, X with β, letter sum, one P and inner selected suffix sum give height at most 3h+2=a. Q7 has height ≤2h+1 and Q8 ≤3h+1. The same bound covers intermediate old/new combinations: congruence combines actual children at the same node, not a child equivalence as a term.

`expand` distributes only a single atomic left letter over its right X tree. Along a branch it retains the original X path with at most one P. Thus height remains ≤a; after each P(letter,suffix) is tagged as one atom, the X tree has height ≤a and at most 2^a leaves. Products with the distinguished Z are paid contractions. The annotation does not change any native formula. When measuring formula size/depth, undo each product annotation by restoring its one P, so it contributes at most one further structural level above the original supplied terms.

Let M be the least power of two above the expanded leaf count. Then M≤2^a<V. The appended zero tree is constructed with exactly M−m leaves and height ≤ceil(log₂(M−m))≤a; the entire padded source has height ≤a+1. Padding uses the explicit zero law, its symmetry, congruence and transitivity. The first reassociation has target height log₂M≤a. The result just proved bounds all its intermediates by 2a+2.

Each subsequent adjacent exchange/cancellation starts and finishes in the perfect M-slot shape. L056 bounds its temporary height by 3 log₂M+2≤3a+2. It applies equally when a tagged atom spells a compound native formula: that full formula remains a paid leaf. Reversing the saved rotations restores the shape after replacing equal slots by Z,Z. The two insertion-sort passes and cancellation pass therefore do not accumulate height.

`erase_zeros` is bottom-up suppression of zero children by the paid laws. Each new child has height no larger than its old child; its congruence and transitivity arguments consequently have height no larger than the input tree. After the final sort, `slim` has height ≤log₂M≤a. The separately constructed requested Bal of survivors has height ≤a, and its compacted target also has height ≤a. Their `match` phase therefore has height ≤2a+1, including the zero-survivor case of one Z atom. Restoring the requested padding uses only these already bounded trees.

All initial/previous/final arguments passed to transitivity are among the bounded mixed trees just listed. Coordinate combination, next-row combination, product congruence and the final three transitivity calls have height ≤a+1. Allowing one level for each product annotation and slack gives the uniform H=9h+20>3a+3. Native/image depth therefore has the stated bound. In particular an unused deep supplied line only affects δ_j and K_j; it is not inserted as a new term into this recursion.

### Application: number of copies, full bytes and time

Count one elementary operation for a call to a fixed library instance or one external MP; internal library records are charged later. The helper costs are refl 1, symm 2, trans 3, two-child congruence 7 and product congruence 2. These counts include every external MP. A local rotation/cancellation plus lifting and cumulative transitivity costs at most 2H+8 such operations.

For completeness the following deliberately generous estimates cover one `normalize` call, with every size bounded by V and every structural depth by H:

* Expansion has fewer than 4V recursive visits, each with at most 12 elementary operations: distributing a product over X costs one law, one two-child congruence and one transitivity, or 11 operations outside its two recursive calls. Original X and leaf cases cost less.
* Each zero-erasure traversal has fewer than 2V visits, each costing at most 12 operations. There are at most three such traversals: extra padding, `slim`, and the compact target. Padding, initialization and the final composition use at most 50 further operations.
* The two reassociations together have at most 2V(H+1) rotations, each costing at most 2H+8 operations. This includes matching the possibly nonperfect compact target.
* Each insertion-sort pass exchanges at most M(M−1)/2 adjacent pairs. There are two passes and at most M/2 cancellations, so at most 2V² slot operations. Each uses at most 4 log₂M+3≤4H+3 events by L056, each of cost at most 2H+8. No pairwise cache credit is taken.

The sum is less than 1000 V²(H+1)². The compiler calls `normalize` four times, twice for each `compare`. Outside these normalizations, the coordinate combination and the n next-row combinations use fewer than 2N+2nk padded slots in total. Their zero sums, the outer n-slot combination and its erasure, product congruences and concluding transitivity calls require fewer than 1000V(H+1)² further operations: N,k,n≤D, 2N+2nk+2n≤6D², V=16·2^(3h)≥16D³, and each visited binary node costs at most 12 operations as above. This justifies E₀ with slack. Dimension checking and endpoint construction do not call proof templates; their explicit loops are polynomial in the supplied dimensions.

Every library invocation copies at most L records; external MPs cost one. Thus G=(L+1)E₀ bounds generated lines without assuming a favorable cache. All I received records are copied exactly once, with relocated earlier references, by the complete-import construction of L058. Their full node sum is K_j. All generated template records have at most S_jP_j nodes by the height argument and the recurrence already proved. External MP conclusions lie inside a copied generated implication, hence satisfy the same bound. This yields max(K_j,S_jP_j) per record, and K_j+(G+1)S_jP_j for all formula/substitution data and the final header.

There are at most J records and every reference is below J. The framing/reference allowance F_J and the name/punctuation estimate above prove (1). This accounts for unused imported lines, all declared substitutions, library auxiliaries, repeated literal suffixes, temporary normalization trees, reference relocation and literal translation. The library's fourteen proofs are fixed overhead. Their maxima remain symbolic here; no uninspected numeric constant is used in this proof.

Finally D≤O(Q+1), h=O(log(Q+2)), V=O((Q+1)³) and 4^H=O((Q+1)^18) with fixed constants. I,K_native,t_native,B≤O(Q+1); the literal image increases node counts by at most a factor of two. Thus (1) is a fixed polynomial in Q. Every shape traversal, explicit bit-table operation, name/tree comparison, simultaneous substitution, earlier-reference check and serialization is polynomial in these bounded lengths and event counts. Parsing or handling a deep supplied tree can use an explicit stack of size at most its written length; no depth-dependent exponent or assignment enumeration is required. This is also a polynomial bound if endpoint comparison ultimately rejects: resource accounting alone does not establish that every intended valid request is accepted.

### Bounded geometry evidence and remaining verification

`python3 scripts/backward-zero/check_geometry.py` executes the actual inherited `Rewrite.split` recursion with a geometry-only rotation recorder. A separate leaf-filter restriction checks (2), restriction composition and the recursive entry invariant. It preserves every before/after tree and rotation in `scripts/backward-zero/output/geometry-193.json`, with summary `scripts/backward-zero/output/geometry-193-summary.json`.

All 6112 cases and 16414 rotations pass: all source shapes and single cuts through eight leaves, all source/target pairs through six leaves, and shallow/compacted-prefix cases through 128 leaves. The largest measured height case has actual/required height 10/16 and rotations 112/1008. There are no failures. The test emits no native proof and performs no new primitive-stream check; the all-size argument is the proof above, not the finite certificate. At step 193, nonpower selection, r=0, used nonzero-T streams and separate critical review were pending. L063 records the later transition completion; the joint step-196 audit below addresses this resource proof. The interrupted larger fixture remains unpassed. Full iteration and all main-problem gaps remain unresolved.

### Independent critical audit, 2026-10-13 (step 196)

The unchanged SPECIALIZE assessment `drafts/literature/2026-10-12-backward-zero-transition-critical-audit.md` covers this joint audit. The complete resource argument, actual `Rewrite.split`, `normalize`, `compile_one`, importer, primitive operations and `ledger.py` were inspected. L056's restored-slot proof, L057's factor-path qualification and L058's complete-import proof apply with the stated hypotheses. No new source theorem or existence premise is used.

**Successive cuts.** Inspection confirms that a recursive cut changes only the child containing its boundary before performing its one parent rotation. Both resulting children are original interval restrictions. Restriction composition remains valid when either original child disappears: both orders suppress precisely the same unary parent. Left-first processing cannot change an unprocessed right sibling. Thus an active subtree at target depth d starts with height at most h₀, temporarily has height at most h₀+1, and has at most g fixed ancestors. Completed siblings have the target shape; pending siblings remain restrictions. This verifies H₀=h₀+g+1 for the whole evolving tree, including the period before the parent rotation, and R₀=(m−1)h₀. The m=1 and nonperfect-target cases need no extra hypothesis. This is an all-size argument, not an extrapolation from balanced examples.

**Mixed normalization and operation count.** Products in `expand` have exactly one atomic left letter and no nested product on the right; their right children are X trees over supplied suffixes/Z. Distribution retains a branch's X ancestry with one product. The maximum starting height 3h+2 covers coordinate selection and both nested next-row selections. The first reassociation has height at most 2a+2; restored slot operations have height at most 3a+2; bottom-up zero deletion cannot increase height, and compact-target matching has height at most 2a+1. Undoing product tags adds one level. Consequently H=9h+20 covers every law argument, including all three complete terms supplied to transitivity; a proved equivalence is never itself installed as a new leaf term.

An exchange needs one local law; cancellation needs cancel, zero_slots and trans with two external MPs, hence five elementary operations. Context lifting contributes at most 2H and cumulative transitivity three. Thus 2H+8 also covers cancellation. Single-factor distribution needs eleven operations outside its recursive children. Each normalization has at most two insertion sorts, M/2 cancellations, two reassociations and three zero-erasure traversals. Their bounds in the proof give fewer than 1000V²(H+1)² operations. Four normalizations and the separately charged coordinate/next-row/outer combinations fit E₀. Empty lists add only the already budgeted reflexivity/composition calls. No favorable cache or observed output length is needed.

**Full input-only ledger.** Literal native/image X and P constructors obey p_(i+1)≤8+4p_i, while their depth increments are at most 3/6. A copied record with s operator nodes and v variable occurrences has at most s+vP_j≤S_jP_j nodes, including declared substitutions. External MP conclusions are subformulas of their copied implications. All imports retain total K_j and depth δ_j; the output header costs one further generated-formula allowance. ASCII payloads and explicit references then give exactly (1). In `ledger.py`, `(D−1).bit_length()` equals ceil(log₂D), and `(J+1).bit_length()` equals ceil(log₂(J+2)); both are exact for the positive integers here. L,D_j,S_j are measured on all fourteen laws. Finite measured argument/event bounds are separate and are not fed into (1). Since dimensions and all supplied records are written input, the polynomial-in-Q conclusion and abstract-stack qualification survive.

**Complete evidence.** `python3 scripts/backward-zero/audit_archives.py` preserves the earlier archives and writes `scripts/backward-zero/output/audit-196.json`. It replays all 6112 complete geometry cases/16414 rotations against the actual splitter and independent interval filtering, comparing every saved entry and before/after tree. It independently recomputes (1) from all supplied records and the full library, agrees exactly with `ledger.thresholds` and all saved step-194 thresholds, and checks complete actual line/depth/node/byte measurements for all twelve transition streams. The full resource audit found no substantive defect or required threshold change. L063 records the primitive/archive details. This verifies a conditional local input, not an iteration bound or a whole-receiver theorem; Mathlib and interpreter limitations remain unchanged.

## Mathlib

Full matching coverage for the interval-cut algorithm, its primitive Frege strings and the complete copying bound has not been checked. Supporting tree/linear-algebra facts would not certify this compiler. This is an informal resource proof and bounded geometry test, not Lean verification or a new complexity separation.
