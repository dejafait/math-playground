# L103 — Pathwise logarithmic renaming does not bound the full-map cache

## Hypotheses

Retain L101's explicitly written assumption-free renaming-Frege syntax,
ground axioms, scheme-instantiation records, simultaneous variable maps,
and nonduplicating connective abbreviations. Every proof/map variable
belongs to V=Var(F), where F is an occurring-variable CNF of width at
most three. Supply exactly L087's occurrence pair, provenance, complete
Boolean/commutator dictionary B and pre-witness length M. Fix

    Q=2+M+|F|+|π|

before any normalization. Every backward source-reference path, starting
at any written line, must contain at most floor(log₂ Q) renaming lines.

Use the following specified modification of L101 §§1–2. Initialize
(i,id_V) for every source line i. Cache by the pair (i,σ), where σ is
the full function V→V. At MP request both parents with σ; at a renaming
line i with map ρ_i request its parent with σ∘ρ_i. Equal functions at
the same source line share a request, regardless of their descriptions
or paths. For each requested ordinary axiom/MP line write a separate
ordinary record; renaming requests only alias their parent's ordinary
index. Store maps, formulas, instantiation records and references
explicitly. No formula interning across unequal keys, proof replacement,
early contradiction shortcut or pruning precedes this procedure.

## Conclusion

There is an explicit admitted family indexed by h≥1 for which

    2^h ≤ Q_h ≤ C(h+2)^6 2^h,

with C fixed, and at least 2^(h²) distinct realized full-map requests at
one ordinary axiom line. Their requested formulas are pairwise distinct.
The procedure therefore writes at least 2^(h²) ordinary axiom records.
Its full output length and bit writing time have no uniform polynomial
bound in original Q. The procedure still produces a valid ordinary proof.

The separate step-404 all-size informal critical audit below finds no
substantive defect. This is an implementation obstruction, not certified
originality or a lower bound for best ordinary proofs, witnesses,
Frege/EF or SAT. No implementation or proof strings have been verified.
L101's global-count theorem is preserved. Short-proof availability,
bounds in M alone, unrestricted source normalization, arbitrary ER data
and SAT transfer remain open.

## Proof

**Coverage and relevance.** The pre-invocation EXPLORE assessment
`drafts/literature/2026-10-21-composed-map-pathwise-normalization.md`
approves exactly this cache test. Its primary-source comparisons do not
supply the requested bound. No external elimination or extraction theorem
is imported or reproved here. L101 supplies syntax and ordinary-record
materialization; L087 supplies the original occurrence package. The
standard propositional completeness theorem for the fixed Schoenfield
presentation is used only for one constant-size tautology template, with
the explicit variable/constant reception in L097 §3. It is not used to
assert short proofs for arbitrary growing tautologies. L102/Attempt 034
and L099/L100/Attempts 032–033 are contrasts, not counting premises.

The intermediate target is a polynomial original-Q normalization bound
that could precede L098's ordinary-proof receiver. An admitted
superpolynomial count of actual records, rather than possible contexts,
is the abandonment test for that bound. Independent short-proof and
unrestricted SAT gaps remain even if a different normalization succeeds.

**1. Source variables, maps and final CNF.** Fix h≥1 and b=2^h.
Use distinct source variables

    z, x_(l,t), x'_(l,t)                 (1≤l,t≤h).

Let X be the left-associated disjunction of the h² unprimed variables,
in lexicographic (l,t) order; for h=1 this is its single variable. Put

    T = X → (true → X).

This is an instance of the first scheme A→(B→A), with written
arguments A=X, B=true. For each layer l and subset S⊆{1,…,h}, let
ρ_(l,S) swap x_(l,t) and x'_(l,t) exactly for t∈S, and fix every
other member of V. These are explicitly written bijections; use a full
table if desired, including fixed entries. The empty subset gives the
identity. Maps supported on different layers commute, although the
request algorithm still composes in its prescribed order.

Let R be the left-associated conjunction, in lexicographic pair order,
of the clauses (x_(l,t)∨¬x_(l,t)) and (x'_(l,t)∨¬x'_(l,t)). Define
the actual clause tree of F by

    F=(z∧¬z)∧R,                 A=¬F.

The two units and all width-two clauses are retained. Every source/map
variable occurs in F. No occurrence variable from L087 is a source
proof variable. Construct exactly that lemma's two diagrams and its
complete dictionaries for this F, including the four u/v gadget
occurrences and their distinct orderings.

**2. Every source record and the final attachment.** Begin the proof
with the axiom T₀=T. In layer l, first write b separate renaming lines,
one for each subset S in binary order:

    R_(l,S): ρ_(l,S)(T)    by renaming from T_(l−1).

Enumerate these subsets S₁,…,S_b. Designate C_(l,0)=T_(l−1), which
is an existing line, not an additional inference. For j=1,…,b append
the following three records, in this order:

    U_(l,j): T → (ρ_(l,S_j)(T) → T)    first scheme;
    D_(l,j): ρ_(l,S_j)(T) → T         MP from C_(l,j−1), U_(l,j);
    C_(l,j): T                        MP from R_(l,S_j), D_(l,j).

The scheme arguments in U are A=T and B=ρ_(l,S_j)(T), both fully
written. Set T_l=C_(l,b). Each C has exactly formula T, so every MP
pair is syntactically correct. All references are earlier; the b
renamings in one layer have a common earlier parent and are not
ancestors of one another. The prefix has exactly 1+4hb records and
hb renaming records. Every R is in T_h's backward ancestry.

To finish, use one fixed ordinary proof of the tautology template
¬((z∧¬z)∧r), then substitute R for r in every line and instantiation
argument. The template is true for both values of z, independently of
r. Standard propositional completeness gives a fixed proof in the
specified calculus. As in L097 §3, its constants, if any, have the
stated ground axioms. Any additional proof variables can first be
uniformly replaced by z, leaving the template conclusion unchanged.
Thus after instantiation all variables are in V. This finite proof has
a fixed number of records and O(|R|+|z|+1) formula/argument bits; it is
an ordinary proof of A, with no renamings. This is the only use of
completeness, and the template is fixed independently of h.

Append that proof of A, then the first-scheme instance A→(T→A),
then T→A by MP with A, and finally A by MP with T_h. The final
formula is exactly ¬F with its chosen tree. The resulting π_h is an
assumption-free source proof under the stipulated rules. T₀ and all
layers are in its final inference ancestry. The earlier short proof
of A is intentional: replacing the supplied derivation by it would
be a different normalization procedure.

**3. The pathwise promise covers every starting line.** Define d(i)
as the maximum number of renaming lines on a backward path from i.
An axiom has depth zero, MP takes the maximum of its premise depths,
and renaming adds one to its parent's depth. Starting from d(T₀)=0,
every R_(l,S) has depth l. Every U has depth zero; the successive D
and C records have depth at most l, and d(T_l)=l. In particular the
first D in a layer has depth l−1, while its C has depth l. The
independent ordinary proof of A has depth zero; the final attachment
has depth at most h and its last MP has depth h. These recurrences
cover all written lines, including auxiliary records and unused lines
inside the fixed template proof. Hence every required path has at most
h renamings. Section 6 proves h≤floor(log₂ Q_h) using original input.

**4. Realized functions, not merely paths or map descriptions.** Start
from the initialized final request with identity context. Its last MP
requests (T_h,id_V). For any request (T_l,σ), the MP chain through
the C and D records reaches (R_(l,S),σ) for every S⊆{1,…,h}:
from C_(l,j) take its R premise, or take its D premise and then
C_(l,j−1) to reach an earlier j. No renaming is traversed before
the selected R, so the context remains σ. Its renaming edge then
requests

    (T_(l−1), σ∘ρ_(l,S)).

Repeatedly choosing S_h,…,S₁ therefore realizes at T₀ every context

    σ_(S₁,…,S_h)=ρ_(h,S_h)∘…∘ρ_(1,S₁).

If two tuples differ at membership of t in S_l, their functions send
x_(l,t) to different members of the pair {x_(l,t),x'_(l,t)}. All
other layer maps fix that pair. Thus their full functions differ, not
just their path descriptions. There are b^h=2^(h²) such tuples and
distinct cache keys at the same source line. Sharing an intermediate
request with another path cannot remove these keys: closure still
follows every premise edge from that request. Initialization at the
other source lines can only add requests.

The distinction also appears in the requested formulas σ(T). At each
fixed leaf position (l,t) in the first X occurrence, the leaf is primed
if and only if t∈S_l. Renaming preserves the exact connective tree.
Different tuples therefore give different formula strings. The count
does not exploit actions only on variables absent from T. No assertion
about Boolean inequivalence is made: all these formulas are axioms.

**5. Ordinary validity and actual materialization.** For completeness,
the full-map cache preserves L101's syntactic invariant without its
global-count bound. Request (i,σ) asks for σ(A_i). At an axiom scheme,
apply σ to every formula argument in its original instantiation record;
this is an ordinary instance of the same scheme. Ground axioms are fixed.
At MP the requested premises are σ(B) and σ(B)→σ(A_i), yielding
the required formula by MP. At renaming, A_i=ρ_i(A_p), and the parent
request has formula (σ∘ρ_i)(A_p)=σ(A_i), so its existing ordinary
index is a sound alias. Equal full functions give identical requested
formulas and transformed instantiation records at the same source line.
This justification permits even noninjective maps, though the family
uses only bijections.

Source indices strictly decrease along every request edge. The finite
closure can consequently be processed in increasing source index, with
every referenced ordinary line already present and aliases resolved.
As in L101, append a copy of the conclusion's ordinary axiom/MP record
if necessary to put exactly ¬F last. This proves validity without
asserting a polynomial closure bound.

T₀ is an ordinary axiom, not a renaming. Every one of its 2^(h²)
distinct requests therefore emits its own ordinary axiom record with
the corresponding fully transformed arguments X,true. These are not
aliases, and in fact their formula strings differ. Each record takes
at least one output bit. Consequently both explicit output length and
bit writing time are at least 2^(h²), independently of map-lookup
efficiency or sharing elsewhere. No arithmetic cancellation or semantic
proof simplification is a rule of this procedure.

**6. Complete original-input ledger and comparison.** Choose dense
binary source names for the 2h²+1 variables, with O(log(h+2)) bits
per name. Source formula F has O(h²) literal/connective occurrences
and |F|=O((h+2)² log(h+2)). The occurrence construction has
q=4h²+6 names: 4h² from the tautological clauses, two from the units,
and four from its fixed gadget. Its two dense diagrams have O(q)
records, and its two permutations and provenance lists are explicit.
Choose tagged dense occurrence and placeholder names of O(log(h+2))
bits; the fresh u/v source names also have that bound. There are O(q²)
Boolean/commutator dictionary entries, each containing a bounded number
of explicitly written symbols. All orders, transitions, terminal values,
roots, axiom words and name dictionaries therefore satisfy

    M_h ≤ c (h+2)^4 log₂(h+2).

This is a direct ledger for L087's specified construction; no witness
or expanded proof contributes to it.

In each source prefix record, every formula and scheme argument has
O(h²) nodes, including all independently written copies of T and ρ(T).
A full map table has 2h²+1 entries, each with a source name and image
of O(log(h+2)) bits. Thus O((h+2)² log(h+2)) bits pay all formula,
argument and map occurrences per record. The source has 1+4h2^h+O(1)
records including the fixed-template attachment. Every source reference
uses O(log(h2^h+2))=O(h+log(h+2)) bits. Fixed scheme tags, full
dictionary records and ordinary binary length/framing fields fit these
charges after increasing a fixed constant. The template proof has a
constant number of records, each with O(|R|+1) expanded content and
the same reference charge. Consequently one may use the loose bound

    |π_h| ≤ c' (h+2)^5 2^h,
    Q_h=2+M_h+|F_h|+|π_h| ≤ C(h+2)^6 2^h.

All constants are independent of h. This bound includes full maps even
for fixed entries and includes all original occurrences, not implicit
trees or uncharged sources. Conversely at least b=2^h distinct source
renaming records are explicitly written, each occupying at least one
bit. Hence Q_h≥2^h and the promised original cutoff admits depth h.

For arbitrary fixed K>0 and d≥0,

    log₂(K Q_h^d) ≤ log₂ K + d log₂ C + dh + 6d log₂(h+2).

Since h+2≤2^(h+1) for h≥1, this is at most
log₂ K+d log₂ C+7dh+6d. Subtracting from h² tends to +∞. Thus
2^(h²)>KQ_h^d for every sufficiently large h. The required threshold
was one polynomial in original Q; the actual record count exceeds
every such polynomial. No finite experiment is used for this conclusion.

**7. Route decision and limits.** Abandon the universal polynomial
bound for this specified full-map normalization under the pathwise
cutoff. Unlike L102, the counted maps act differently even on the
requested formula; merging equal map actions or deleting identity
renamings alone does not identify the distinct nonidentity choices.
The result does not analyze a different normalization that avoids
materializing these requests or selects the independent ordinary proof
of A. It is not a lower bound on L098's optimal input proof, a final
affine-ABP witness, a proof system, or SAT decision. The global renaming
count here is h2^h, which exceeds floor(log₂ Q_h) eventually, so the
family does not contradict L101. The downstream and main gaps remain.

**Independent critical audit — 2026-10-21, step 404.** The prior EXPLORE
assessment `drafts/literature/2026-10-21-full-map-obstruction-critical-audit.md`
authorizes this exact audit. Its inspected component coverage is reused;
no external elimination bound, stronger-system simulation or new
extraction theorem is assumed. The mathematical inputs remain L101's
syntax/materialization, L087's occurrence package and L097 §3's reception
of standard classical propositional completeness for a fixed template.
Attempts 032–035 are checked for scope and duplication, not used as
proofs of the present count. The following checks establish the existing
claim without changing its family, procedure or bound.

1. **Source legality and the exact conclusion.** There are 2h²+1 source
   variables. Both members of every swapped pair occur in tautological
   clauses of F, and z occurs in both unit clauses. The fresh u/v names
   used by L087 are provenance for occurrence variables, not variables
   in the source proof or its renamings. Thus they do not enlarge the
   domain V of the cache maps. Each table is a total permutation of V.
   Renaming T_(l−1)=T gives exactly the displayed R_(l,S), with no
   simplification. In U the first-scheme arguments are T and ρ(T).
   Its MP with C_(l,j−1)=T gives D, whose MP with R gives C=T.
   Every premise is earlier, including all b parallel renamings.
   These statements remain literal syntactic identities when implication
   is expanded as ¬A∨B and conjunction as ¬(¬A∨¬B).

   For the attachment, ¬((z∧¬z)∧r) is one constant-size tautology,
   in the same nonduplicating presentation. Classical propositional
   completeness supplies one fixed ordinary proof. Replacing any other
   object variables by z fixes its conclusion, and substituting the
   written R for r throughout that finite proof and all instantiation
   arguments preserves axioms and MP. This is construction of ordinary
   scheme instances, not a formula-substitution inference in π_h.
   The two ground constant axioms, if present, are unchanged, as required
   by L097 §3. A fixed number of occurrences of r gives only a fixed
   multiple of |R| copied bits. The result is exactly the chosen ¬F
   tree. The last two MPs through A→(T→A) and T_h are legal, and
   retain the entire layer prefix in the final ancestry. No assumption
   or fresh extension variable is being discharged implicitly.

2. **All-start depth, including the long MP chains.** Use maximum
   renaming count over all backward paths, not shortest-path depth.
   Each U has depth zero. The first D in layer l has depth l−1;
   its C has depth l because its R premise has depth l. Thereafter
   both D and C have depth l. Every R has one renaming above a
   depth-(l−1) parent. Following a chain back through D and C adds
   no renaming until one chooses an R premise, which immediately enters
   the preceding layer. It cannot visit a second R in the same layer.
   Ordinary lines of the fixed proof of A have depth zero, and the
   final attachment has maximum h. This accounts for every source
   record, so initializing requests at unused or auxiliary lines cannot
   violate the same bound. The lower input bound in item 5 makes
   h≤floor(log₂ Q_h); no expanded length enters that inequality.

3. **Closure and distinctions on actual formulas.** For each realized
   (T_l,σ), following both MP premises of C and D visits every
   (R_(l,S),σ) and hence every (T_(l−1),σ∘ρ_(l,S)). This is a
   closure implication for an already realized request, not a count of
   abstract paths that might never be requested. Induction down from
   (T_h,id) realizes every displayed h-tuple at T₀. Merging requests
   with equal full maps cannot invalidate that implication: both parent
   positions of the merged request still have to be processed.
   For any differing tuple coordinate (l,t), all other layers fix its
   pair. The two composites therefore send x_(l,t) to different names.
   At the fixed leaf position in the first X of T, those two names
   appear in the respective requested strings. Renaming preserves all
   positions, even at h=1 when X is a single leaf. Thus the b^h maps
   and requested formulas really are pairwise distinct at one axiom;
   tautologicity and equal truth functions do not merge their strings.

4. **Ordinary records and validity are separate obligations.** T₀ is
   an ordinary first-scheme instance, so each of its distinct requests
   emits a record with the arguments σ(X),true. None is a renaming
   alias. The specified output therefore has at least b^h records and
   bits, independent of cache search or map representation costs.
   Separately, for every admitted source proof the invariant requested
   formula σ(A_i) is preserved by scheme instantiation, MP and the
   exact composition σ∘ρ_i at a renaming. This does not require
   injectivity. Finitely many maps on finite V and strictly decreasing
   source indices ensure a finite acyclic request closure. Processing
   by increasing source index resolves every alias to an earlier
   ordinary record. Copying that record, with its original earlier
   premises, puts the identity-context conclusion last if necessary.
   Validity supplies no polynomial bound on the number of requests.

5. **Original encoding, not normalized output.** F has two units and
   2h² tautological two-literal clauses, so its 4h²+2 occurrences plus
   the four gadget occurrences give q=4h²+6 exactly. L087's diagrams
   have O(q) states/transitions and distinct orders on the gadget.
   Provenance, permutations and schedules have O(q) entries. Dense
   tagged names and all their positions use O(log(h+2)) bits. The
   q(q+1)/2 complete Boolean/commutator entries dominate the resulting
   O((h+2)^4 log(h+2)) input ledger. This tighter family-specific count
   uses L087's actual records, rather than substituting a favorable
   value into its more conservative general |F|-based estimate.
   Every prefix formula/instantiation has O(h²) nodes; each total map
   has 2h²+1 entries. There are exactly 1+4h2^h prefix records,
   O(1) attachment records and O(h+log(h+2)) bits per source reference.
   All names, copied arguments, map entries, length fields and source
   dictionaries fit |π_h|≤c'(h+2)^5 2^h. The attachment's fixed
   number of copies does not depend on h. Combining these counts gives
   Q_h≤C(h+2)^6 2^h with one constant C. At least 2^h renaming
   records are present even for h=1, proving the lower bound on Q_h.

   For every fixed K>0 and d≥0 the logarithm of KQ_h^d is at most
   log₂ K+d log₂ C+7dh+6d, using the inequality in §6. Its difference
   from h² tends to −∞. Hence the materialized-record lower bound
   exceeds KQ_h^d eventually. This is an all-size comparison, not an
   extrapolation from a finite run or an inflated parameter convention.

These checks find no substantive defect. Keep the procedure-specific
stop: full-map equality and even equality of the counted axiom strings
cannot reduce these distinct requests. This does not test a procedure
that avoids requesting them or selects the already supplied short proof
of A. In particular no lower bound on a best ordinary proof, an ABP
witness, a proof system or SAT follows. L101's global renaming promise
is not met eventually, since its count is h2^h while log₂ Q_h is
O(h+log(h+2)). The audit is local verification of an existing informal
result, not a stronger theorem, verified implementation or novelty claim.

## Mathlib

Full matching coverage has not been checked. No Mathlib theorem is
claimed present or absent. The proof uses finite functions, composition,
explicit proof-reference DAGs and an elementary asymptotic comparison;
these general supporting topics are not a formalization of this
specified normalization or its encoding ledger.
