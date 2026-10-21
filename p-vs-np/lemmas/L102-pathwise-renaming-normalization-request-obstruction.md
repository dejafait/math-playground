# L102 — Pathwise logarithmic renaming does not bound the exact subset cache

## Hypotheses

Use precisely L101's source presentation, request initialization and
closure in §1, and ordinary-record materialization in §2. In particular:
start every (i,∅), cache by the exact source-line/index-subset pair (i,S),
keep distinct subsets separate even if their maps agree, and write an
ordinary axiom/MP record for every requested axiom/MP pair. Only renaming
requests are resolved aliases. There is no formula-based interning,
identity-rule deletion, proof pruning or empty-clause shortcut before
this normalization. We are testing this specified normalization, not
every algorithm for L101's final witness task.

Retain L101's explicitly written assumption-free proof syntax, fixed
nonduplicating connective abbreviations, ground axioms true and ¬false,
and explicit variable-to-variable maps fixing unlisted variables. An empty
map denotes the identity, as permitted by that syntax. Every proof/map
variable must occur in the original width-at-most-three CNF F. Retain
L087's prescribed occurrence pair, provenance, dictionaries, B and M.
Fix Q=2+M+|F|+|π| before normalization. Replace only L101's global
renaming-count promise by this one: every backward source-reference path,
starting at any written line including unused lines, visits at most
floor(log₂ Q) renaming lines.

## Conclusion

There is an explicit family indexed by integers h≥1 satisfying these
conditions for which the specified normalization realizes at least
2^(h²) distinct requests at one ground-axiom line and writes at least
that many ordinary proof records, while

    2^h ≤ Q_h ≤ C (h+2)³ 2^h

for one fixed encoding constant C≥1. Thus neither its full output length
nor its bit construction time has a uniform polynomial bound in the
original Q under the pathwise promise.

This is an implementation obstruction, without certified originality.
The separate step-400 all-size informal critical audit below finds no
substantive defect in the stated construction or original-Q comparison.
It is not a lower bound on ordinary Frege proofs, affine ABPs, alternative normalization or witnesses. Indeed the
source formula below has a one-line ordinary proof and a constant-size
zero witness. The globally logarithmic theorem L101 is unchanged.

## Proof

**Coverage and the fixed object.** Reuse the pre-invocation EXPLORE
assessment `drafts/literature/2026-10-21-pathwise-renaming-normalization.md`,
whose COVERED_TARGET is exactly this normalization test. L101 supplies
the procedure being tested, not a bound under the changed promise.
L087 supplies the unchanged occurrence package, including its empty-clause
case. The proof below is direct finite combinatorics; no external
elimination theorem or algebraic extraction theorem is invoked or
reproved. The assessment's primary comparisons do not establish this
exact cache bound. L099/Attempt 032 and L100/Attempt 033 are historical
contrasts, not inputs to the counting argument.

**1. Actual legal source records.** Fix F to be the CNF consisting of
one empty clause, written as false. Then ¬F is exactly T=¬false, a
permitted ground axiom. The source variable set V=Var(F) is empty.
L087 still appends its fixed two-clause u/v gadget when constructing
the occurrence pair, so that pair has its required distinct orders and
a constant full pre-witness size M=M₀. Those occurrence names are not
source proof/map variables. All source formulas and all instantiation
arguments used here are variable-free. Every renaming map is explicitly
the empty list, hence the identity on V; this is a valid renaming
inference even on a variable-free formula.

For an arbitrary integer b≥2, write the following ordered proof with h
layers. Its first line, denoted T₀, is the ground axiom T. In layer
l=1,…,h first write b separate lines

    R_(l,j): T       by identity renaming from T_(l−1),  1≤j≤b.

All these lines have different original source indices. Starting with
C_(l,1) denoting the already written line R_(l,1), write these three
lines for each j=2,…,b, in increasing j:

    U_(l,j): T → (T → T)       first axiom scheme, arguments T,T;
    D_(l,j): T → T             MP from C_(l,j−1), U_(l,j);
    C_(l,j): T                 MP from R_(l,j), D_(l,j).

Here a designation such as C_(l,1) is only a name for an existing line,
not an additional proof inference. Set T_l to designate C_(l,b).
All cited records precede their uses. The two MP pairs have exactly
the required antecedent and implication, including the fixed expansions
of →. The first scheme A→(B→A) with A=B=T gives the displayed U.
Each renaming's premise and conclusion are literally T. Consequently
every record is a legal assumption-free axiom, MP or renaming line.
There are no substitutions by formulas, assumptions or extensions.
The last written line T_h is exactly ¬F. The complete source line count is

    N=1+h[b+3(b−1)]=1+h(4b−3),

and its total renaming count is r=hb. Every layer and every R_(l,j)
lies in the backward ancestry of T_h: the MP chain visits all its
renamed premises and then the preceding layer. No count below depends
on a merely possible, unrequested context.

**2. Pathwise depth, including every starting line.** For a written line
i let d(i) be the largest number of renaming records on a backward
reference path starting at i. Axioms have d=0; at MP, d is the maximum
of its two premise depths; at a renaming, d=1+d(parent). Thus d(T₀)=0.
Inductively, each R_(l,j) has depth l, each U_(l,j) has depth zero,
and each D_(l,j) and C_(l,j) has depth at most l, with d(T_l)=l.
In particular no backward path starting anywhere in this proof contains
more than h renaming lines. Parallel R records are never ancestors of
one another. This proves the all-start assertion directly rather than
checking only final-output paths.

**3. Realized requests and emitted records.** Write r_(l,j) for the
original index of R_(l,j), and i₀ for the index of T₀. All indices from
layer l exceed those in earlier layers. Consider any request (T_l,S)
where every member of S comes from a later layer. The MP edges from
C_(l,b), through the D and preceding C records, reach every (R_(l,j),S).
These request edges encounter no renaming and therefore preserve S.
The renaming rule in the fixed closure then requests

    (T_(l−1), S ∪ {r_(l,j)})                  for every j=1,…,b.

This is an assertion about actual paths in the specified request
closure. For j=1, C_(l,1) is R_(l,1), so the same assertion holds at
the end of that MP chain. Every new subset has exactly the descending
index convention required by L101.

The request (T_h,∅) is one of the initialized requests. Repeatedly apply
the preceding observation for l=h,h−1,…,1. For every tuple
(j₁,…,j_h)∈{1,…,b}^h the closure therefore contains

    (i₀, {r_(1,j₁), …, r_(h,j_h)}).

These b^h keys are pairwise distinct: a different tuple selects a
different source index in at least one layer, and the layer index sets
are disjoint. It is irrelevant that every selected map is the identity
and every requested formula at i₀ is the same ground formula T.
L101's cache explicitly separates such subsets. Starting all other
empty-context requests can only add requests; it cannot identify these.

The source line i₀ is an axiom, not a renaming. Section 2 of the fixed
materialization writes the ground axiom T for each distinct request
at i₀. Thus these are b^h separately written ordinary proof records,
not just unresolved renaming aliases or an unused universe of subsets.
Resolving the aliases for R records does not merge axiom requests or
their output records. Source-index order processes i₀ before its uses,
and no cancellation rule exists in this ordinary-proof procedure. Any
optional last-line copy only increases the output count. Every explicit
record takes at least one bit, so both full output length and the bit
time to write it are at least b^h. The request store also contains at
least b^h entries, independently of how the alias indices are stored.

**4. Original full-bit bounds and the promised threshold.** Set b=2^h.
All written formulas and scheme argument trees are now fixed constant
strings; the original-name dictionary and map entry lists are empty.
Map and inference tags have constant size. Every source reference and
line/framing index uses O(log(N+2)) bits in the notebook's explicit
binary encoding. Consequently the complete proof, including its records,
empty maps, instantiation arguments and framing, has at most
c N log₂(N+2) bits for a fixed c. The fixed F and L087 package contribute
another constant independent of h. Since

    N=1+h(4·2^h−3) ≤ 1+4h2^h,

we obtain Q_h≤C(h+2)³2^h after increasing one fixed C≥1. This is an
upper bound for a particular fully written encoding, not an encoding
that omits repeated formulas, references or maps. Conversely there are
at least b explicit nonempty renaming records, so |π_h|≥b=2^h bits
and Q_h≥2^h. Therefore

    h ≤ floor(log₂ Q_h),

and §2 proves the required promise at the unchanged original Q_h.
No output size or expanded proof size contributes to this cutoff.

The realized ground-axiom record count is b^h=2^(h²). For any fixed
K>0 and d≥0, the preceding upper bound gives

    log₂(K Q_h^d) ≤ log₂ K + d log₂ C + dh + 3d log₂(h+2).

For h≥1, h+2≤2^(h+1), so the right side is at most
log₂ K+d log₂ C+4dh+3d. Subtracting it from h² tends to +∞.
Hence 2^(h²)>KQ_h^d for every sufficiently large h. This defeats
every fixed original-input polynomial, for both written output length
and writing time, and proves the conclusion.

**5. Scope, downstream meaning and stopping decision.** The actual
normalization test is negative. Stop extending this unchanged exact
subset-cache implementation from the global cutoff to the pathwise
cutoff. The achieved lower bound is 2^(h²), versus the required KQ_h^d
for one fixed d; no finite-size computation is used to infer that
comparison. The original global theorem is not contradicted: r=h2^h,
so r>floor(log₂ Q_h) eventually under the displayed Q upper bound.

The ground-axiom and identity-map choices are admitted by the target,
but make the limitation especially explicit. Deleting identity rules,
interning equal requested formulas, changing the cache to map actions,
or detecting the empty clause first would avoid this family's growth.
Each changes the tested implementation. This proof does not analyze
the changed algorithms, and it does not claim that they work on the full
pathwise class. Here F already has the one-line proof T, L087's f is
formally zero, and the zero affine graph witnesses fg=0. In particular
there is no lower bound on the final witness or on the best ordinary
proof, and no claim that L098 must be expensive on this input. The
normalization's explicit work is what fails its proposed uniform bound.
The independent short-proof availability, M-only, universal W₂,
arbitrary-ER and SAT decision/separation gaps remain unresolved.

**Independent critical audit — 2026-10-21, step 400.** Reuse the
pre-invocation SPECIALIZE assessment
`drafts/literature/2026-10-21-pathwise-normalization-obstruction-critical-audit.md`.
The object is this full L102 proof, not a proposed stronger normalization.
The received definitions are L101's hypotheses, §§1–2 and step-396 audit
items 1–2, and L087's empty-clause occurrence construction and original M.
The saved primary-source comparisons remain adequate: no elimination,
extraction or proof-system simulation theorem is imported into this
finite counting argument. No new source search or reproof is needed.

1. **Admitted input and exact inference syntax.** The one-clause CNF
   whose clause is empty has source formula false and no source
   variables. Its negation T=¬false is an explicitly admitted ground
   axiom, so T₀ and the last line T_h have the required exact formulas.
   Ground instances of the first scheme are allowed: A=B=T yields
   T→(T→T), with both formula arguments explicitly recorded. For the
   first MP in a merge, C_(l,j−1) has formula T and U_(l,j) has formula
   T→(T→T), so the conclusion is exactly T→T. For the second MP,
   R_(l,j) has formula T and D_(l,j) has formula T→T, so the conclusion
   is exactly T. The fixed implication expansion preserves these exact
   strings. All references are earlier, including C_(l,1)=R_(l,1),
   which is a designation and not an extra rule. Empty simultaneous
   maps fix the ground formulas and are legal even when V is empty.
   Thus no extra variables, assumptions, tautology oracle or unlisted
   axiom scheme have entered the construction.

2. **All-start path bound.** Use depth zero at every axiom, maximum
   of the two premise depths at MP, and one plus the parent depth at
   renaming. In layer l the b renaming lines all reference T_(l−1),
   so their depths are l. U has depth zero; successively D and C have
   depth l, beginning with C_(l,1) of depth l. This proves depth l
   for T_l, by induction from T₀. It also covers a path starting at
   any auxiliary U, D or C, not merely at the final line. Traversing
   the merge chain can encounter many MP records but cannot visit two
   R records in a single layer: each R immediately returns to the
   previous layer. The ordinary reference graph and the request graph
   must not be conflated with the union of all their paths.

3. **Actual closure, not a possible-context count.** Starting with
   the initialized (T_h,∅), fix any desired index j in layer l. From
   (C_(l,b),S), repeatedly take the D premise and its preceding C
   premise until reaching C_(l,j); take its R premise when j≥2,
   or use C_(l,1)=R_(l,1). Every traversed edge before R is an MP
   edge and retains exactly S. The renaming edge then reaches
   (T_(l−1),S∪{r_(l,j)}). All old elements of S belong to later
   layers and exceed r_(l,j), while r_(l,j) exceeds T_(l−1)'s index.
   Hence the full path is legal under L101's descending-index rule.
   Concatenating these choices realizes the key at T₀ for every
   tuple (j₁,…,j_h). If two tuples differ in layer l, intersecting
   their context subsets with that layer's renaming indices gives
   different singletons. Their keys are therefore different. The
   argument uses only closure from the final initialized request;
   initialization at every other line cannot remove these keys.

4. **Written records and alias resolution.** The keys just counted
   have first coordinate i₀, the ground-axiom line. L101 §2 instructs
   the materializer to write the ground axiom at each such request;
   it does not search for another record with the same formula or
   composed map. These are b^h non-alias records. Increasing source
   index processes them before their uses, and aliases at R simply
   store the corresponding earlier ordinary indices. Neither alias
   resolution nor sharing identical (i,S) keys identifies distinct
   T₀ keys. Consequently both the request store and written proof
   contain at least b^h respective entries/records. In the specified
   explicit binary output model every record consumes at least one
   bit and writing those bits takes at least b^h bit operations. This
   is a lower bound on this materialization, not on an implementation
   returning a compressed description or choosing different proofs.

5. **Original-Q ledger and comparison for all h.** There are exactly
   1+h(4b−3) records, each with a constant-size formula, tag and
   instantiation data, zero map entries, and at most two binary source
   references. With b=2^h and h≥1, N≤5h2^h and N+2≤7h2^h, so
   log₂(N+2)≤h+log₂ h+3≤2h+3. Thus the fully written proof has
   at most a fixed constant times h(2h+3)2^h bits; the weaker bound
   C(h+2)³2^h in §4 follows after absorbing the constant package.
   L087 appends exactly four occurrence names even for this empty
   source variable set. Its two orders are u₁,v₁,u₂,v₂ and
   u₁,u₂,v₁,v₂, so they are different and both dense diagrams and
   the full B/placeholder/provenance dictionaries have constant size.
   These are occurrence names, not illegal source proof variables.
   F and M are consequently constant independently of h. The b
   distinct nonempty source renaming records alone give Q_h≥2^h,
   establishing the required cutoff at the original input length.

   The output bound is at least b^h=2^(h²). For every fixed K>0 and
   d≥0, log₂(KQ_h^d) is at most
   log₂ K+d log₂ C+4dh+3d, using h+2≤2^(h+1). Subtracting this
   upper bound from h² tends to positive infinity. This is the required eventual
   comparison with every polynomial, not a comparison only with one
   chosen exponent or with expanded-output Q. The global count r=h2^h
   exceeds log₂ Q_h eventually, so the example violates L101's global
   promise and does not contradict that theorem.

6. **Easy alternative and exact scope of the stop.** In L087's D,
   an empty clause places the root in the failure chain. Both children
   of each failure state are failure states; from terminal value zero,
   recurrence (1) gives zero formally at each preceding failure state.
   Hence f=0 in the free ring, not just on Boolean assignments, and
   fg=0. A graph with distinct endpoints and no accepting path gives
   the zero witness with the complete constant dictionaries retained.
   The one-line source proof T is also legal. Thus the audit confirms
   only the failure of the specified exact-subset normalization under
   the pathwise promise. Identity deletion, equal-map/formula interning
   and an early empty-clause shortcut change that procedure and are
   not excluded; their behavior on the full pathwise class is unproved.
   Attempts 020/032/033 concern different objects and cannot strengthen
   this count to optimal-proof, final-witness or SAT hardness.

The separate audit finds no substantive defect. It validates the local
implementation-specific stop with unchanged hypotheses, bounds and
mathematical inputs; it proves no stronger theorem and certifies no
originality, implementation or formal proof. Alternative normalization,
short-proof availability, M-only bounds, universal W₂, arbitrary ER data
and the unrestricted SAT gap remain unresolved.

## Mathlib

Full matching coverage and supporting finite-DAG/counting coverage have
not been checked. The exact source-proof/cache statement is proved here
informally. Unknown Mathlib availability is not evidence of absence.
The separate informal critical audit is recorded above. No implementation,
exhaustive finite certificate or formal verification is claimed.
