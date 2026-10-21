# L095 — Occurrence pairs need not have logarithmically many oriented blocks

## Hypotheses

Use L087's exact occurrence-splitting construction for explicitly written
width-at-most-three CNFs: append `(u OR v),(NOT u OR NOT v)`; give each
literal occurrence its own distinct name; let D read clause/literal order
and let E group occurrences by their old variable, preserving D's order
within each group. Old variables precede u then v in E. Use L087's dense
width-at-most-three testers, ordered representatives f,g, and full original
Boolean/commutator dictionary B. Its parameter M is 2 plus the actual full
binary length of these two diagrams, orders and complete dictionaries,
before any partition annotation, witness or witness-degree parameter.

An oriented common contiguous partition means a partition of D's order
into b nonempty intervals whose lists, independently reversed or retained,
can be permuted to give E's order. These are unsigned lists of distinct
occurrence names; literal signs are not signs on this alphabet. There are
no added endpoint symbols. This is the partition promise in L094; its
witness construction is not used in this proof.

For each integer t>=6 put n=2^t. Give distinct old variables x_1,...,x_n,z
ordinary explicit indexed names, and take the following ordered CNF F_n:

    (x_1),...,(x_n), (x_1),...,(x_n), (z),(NOT z).

Apply the unchanged L087 construction. Fix the concrete complete encoding
specified below; the statement uses its actual M_n, without padding it.

## Conclusion

F_n is unsatisfiable, and its resulting two dense width-at-most-three
diagrams have different orders and Boolean-zero original product fg.
Every oriented common contiguous partition of these exact orders has

    b >= 2n-1 > floor(log₂ M_n),

where the complete original encoding satisfies

    M_n < 2^16 (n+2)^3.

Thus L094's logarithmic partition promise is not universally available
on L087's unsatisfiable occurrence pairs. This is an elementary
specialization of the known unsigned breakpoint obstruction, not a new
general partition theorem or a certified originality claim. It does not
refute L094, W₂, any alternative witness bound, or either answer to P
versus NP. The separate step-372 critical audit below finds no substantive
defect in the all-size proof or encoding ledger. No implementation or
finite computation is claimed.

## Proof

**Coverage and precise source use.** The prior SPECIALIZE assessment is
`drafts/literature/2026-10-20-occurrence-pair-oriented-block-availability.md`.
Kolman and Waleń, *Reversal Distance for Strings with Duplicates: Linear
Time Approximation using Hitting Set*, Electronic Journal of Combinatorics
14 (2007), R50, §1.1 pp.3–4
([primary PDF](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v14i1r50/pdf)),
defines common contiguous partitions with equality/reversal congruence.
Alexandrino, Oliveira, Dias and Dias, *On the Complexity of Some Variations
of Sorting by Transpositions*, JUCS 26(9) (2020), 1076–1094, §2.1
pp.1080–1082, Definitions 8–13 (Definitions 11–13 on p.1082)
([primary PDF](https://www.jucs.org/jucs_26_9/on_the_complexity_of/jucs_26_09_1076_1094_alexandrino.pdf)),
defines unsigned reversal breakpoints by absolute successive difference
unequal to one, and the corresponding strips. We use that elementary
internal-adjacency necessity, proved below to receive the present
occurrence naming and sentinel-free endpoints. No approximation,
sorting-hardness or exact-optimum theorem is needed or reproved. L087
supplies the occurrence testers, their scalar correctness and B/M model.
The local specialization must additionally establish unsatisfiability,
realizability and the complete encoding comparison; the sources alone
do not supply those conclusions.

**The exact realizable orders.** The old CNF has 2n+2 clauses, all units.
The opposing z units make it unsatisfiable. L087 appends its two binary
clauses, producing 2n+4 clauses and exactly

    q=2n+6

distinct occurrence variables. Write a_i for the occurrence y_(i,1),
b_i for y_(n+i,1), c for y_(2n+1,1), d for y_(2n+2,1), and write
u_1,v_1,u_2,v_2 for the four distinct appended occurrences. These are
aliases for the actual (clause,literal-position) names, not replacements
by unsplit names. D's exact order is

    a_1,...,a_n, b_1,...,b_n, c,d, u_1,v_1,u_2,v_2.       (1)

Every old variable occurs exactly twice. Consequently E's old-variable
prefix is a permutation of the n blocks (a_i,b_i) and the block (c,d),
followed by u_1,u_2,v_1,v_2. The pairs retain the order displayed within
each block. This description holds for every deterministic ordering of
old variables allowed in L087, including the increasing indexed order.
It does not change either supplied order or group copies by literal sign.

In particular the gadget retains L087's strict order distinction. Each
diagram has q nonterminal levels, at most three states per such level,
and only final Boolean terminals. Redundant/unreachable states may all be
retained. The exact L087 tester construction applies to these nonempty
unit/binary clauses without any new reception case. Its scalar
characterization says joint acceptance is equivalent to satisfiability
of F_n; hence f(a)g(a)=0 for every occurrence-bit assignment a. No equality
of the two free-ring representatives or witness existence is inferred.

**Forced internal cuts, allowing either orientation.** For any adjacent
names s,s' in D's order, if a single partition block contains both, they
are adjacent in that block. Its placement in E makes them adjacent in E,
in one order or the other. Distinct names cannot be rematched elsewhere.
Thus nonadjacency of s,s' in E forces a cut between them in D. This is
only a necessary condition, which suffices; no exact optimum formula is
asserted. It also applies to blocks of any length, including singletons.

Number the old-variable groups in E by r=1,...,n+1. If x_i has group
number r_i, then the positions of a_i and b_i in the complete E order are
2r_i-1 and 2r_i, respectively. The r_i are distinct. Therefore for every
1<=i<n the absolute E-position differences are

    |pos_E(a_(i+1))-pos_E(a_i)| = 2|r_(i+1)-r_i| >= 2,
    |pos_E(b_(i+1))-pos_E(b_i)| = 2|r_(i+1)-r_i| >= 2.

All these 2(n-1) pairs are adjacent in (1). They force distinct cuts.
A partition into b nonempty D intervals has exactly b-1 internal cuts,
so b>=2n-1. Reversal cannot remove an unsigned nonadjacency. All counted
pairs lie inside the two x-runs, away from endpoints and the gadget;
joining other names to a block cannot remove a forced cut. No sentinel
contribution or unproved realizability of an arbitrary permutation is used.

**A concrete full original encoding.** The following ordinary record
format fixes M_n, rather than adding an adjustable padding parameter.
Put h=q(q+1)/2, the exact number of B entries, and

    w=ceil(log₂(16(q+2)^2)).

Start with the self-delimiting prefix 1^w0. Every subsequent numerical
field has exactly w bits, every record has an 8-bit type tag, and Boolean
flags use one bit. Record types determine their arity. No alignment
padding or unused records beyond the retained three diagram states are
inserted. The fixed header gives q,h,n and the section counts. All IDs,
levels, counts, clause positions and indices below are smaller than
16(q+2)^2 and fit in w bits.

* Store the n+3 old names x_i,z,u,v by their distinct kind/index codes
  and dense IDs. Store q occurrence-name records with their dense ID,
  actual clause index, literal position, old-name ID and literal sign.
  These records retain the old-name map and the full named alphabet;
  their order is the fixed original dictionary order. Names are encoded
  by these explicit tagged indices, rather than long decimal strings.
* Store each diagram's counts, root and designated terminal IDs in its
  metadata record. Retain all three nonterminal state slots at every
  query level, and the two final terminals. Each vertex record gives its
  ID, level and state/terminal type (including a terminal scalar). Each
  transition record gives its source, queried bit and destination. The
  query name at a level is explicitly supplied by that diagram's order.
  Thus there are 6q+4 vertex records and 12q transition records in total.
  All successors, including coincident successors, are written separately.
* Store both orders as 2q position/occurrence-ID records.
* Store h separate placeholder-name records: a kind flag and the
  original index i for σ_i, or indices i,j for τ_ij, with a dense ID.
  Store all h B records, each giving its axiom/placeholder association
  and both word lengths and complete word token lists. Boolean words
  are (i,i) and (i); commutator words are (i,j) and (j,i). Original
  tokens are explicit dense references to the complete name dictionary.
  Store a coefficient bit 1 for each word. Every axiom word is written, not
  represented by a rule standing for the dictionary.

The header and two metadata records each fit 16(w+1) bits; a vertex or
transition or order record does too. Name records have at most four
numerical fields and one sign bit; placeholder records at most three
numerical fields and a kind bit. An axiom record has at most nine
numerical fields (association, word count/lengths and four tokens),
one kind bit and two coefficient bits. Thus 16(w+1) is a uniform bound for every complete record,
including tags and framing. Terminal types need at most two flag bits.

There are at most

    1 + q + q + 2 + (6q+4) + 12q + 2q + 2h
      <= q²+23q+9 <= 8(q+2)^2

records: old names number n+3<=q; all other terms are the records just
listed; the displayed polynomial bound has two records of slack. Root
designations occupy their metadata as specified. Section counts require
no further framing. No length of F_n
or derived ABP G is silently used as M: only the complete two-diagram
input and its dictionaries just specified are counted.

Including the prefix and the defining extra 2, the actual length obeys

    M_n <= 2+(w+1)+128(w+1)(q+2)^2
         <= 130(w+1)(q+2)^2
         <= 390(q+2)^3
         < 2^16(n+2)^3.                                  (2)

For the penultimate inequality, put s=q+2>=3. The elementary integer
inequality ceil(log₂ s)<=s-1 gives
w+1<=5+2ceil(log₂ s)<=2s+3<=3s. The last inequality uses
q+2=2n+8<=4(n+2) and 390*4^3=24960<65536. This is an upper bound on
the actual encoding, not an inference from its lower bound. All diagrams
and dictionary words are explicit; there is no succinct encoding or
post-witness enlargement of M. They can be produced in polynomial bit
time in the explicitly written F_n length.

**Cutoff comparison.** For n=2^t, t>=6, one has n+2<2^(t+1), so (2)
implies floor(log₂ M_n)<=19+3t. At t=6,

    2^(t+1)-1=127 > 37=19+3t.

When t increases by one, the left-minus-right difference increases by
2^(t+1)-3>0. Therefore 2n-1>floor(log₂ M_n) for every t>=6, proving
the claimed infinite-family obstruction. Fixed constant-factor variants
of the encoding also fail eventually, since b is linear and their
logarithmic cutoffs remain O(log n); the displayed threshold is claimed
only for the concrete format above.

The original CNFs already have an immediate opposing-unit refutation.
This is a syntactic failure of one sufficient representation promise,
not hardness of these formulas, of their best witnesses, or of SAT.

**Separate critical audit — 2026-10-20, step 372.** The prior SPECIALIZE
assessment is
`drafts/literature/2026-10-20-occurrence-partition-obstruction-critical-audit.md`.
This audit receives L087's construction and original B/M definition and
L094's partition hypotheses only. It reuses the inspected primary
definitions cited above; neither an external optimum theorem nor L094's
witness proof is needed. The source page locator is corrected to include
p.1082, as already verified in that assessment. This is a citation repair,
not a change in any mathematical bound.

The following checks independently validate the claimed obstruction.

1. **Occurrence identity and scalar reception.** There are 2n+2 old unit
   occurrences and four appended occurrences, hence q=2n+6. All old
   variable groups, including z, have exactly two members. Stable grouping
   puts the first/second x_i copies at 2r_i-1 and 2r_i for distinct r_i,
   even if z is interspersed among the x-groups. These are positions in
   the complete E order, since u and v follow the old variables. The
   negative sign on d changes D's literal test, not the raw equality test
   or the occurrence alphabet. Joint acceptance would force c=d while
   the two unit tests require c=1,d=0, an impossibility. This also checks
   the needed specialization of L087's scalar characterization directly.
   The appended u/v pair remains unchanged and enforces distinct orders.
   L087 permits all three state slots, with failure propagated through
   every remaining level and two final terminals; unit clauses reset the
   live clause state exactly at their sole occurrence. No early terminal,
   additional original variable or formal-zero inference is introduced.

2. **Internal cuts and orientation.** The position differences within
   each run are nonzero even integers. Therefore none is 1 in absolute
   value. Each of the 2(n-1) adjacent pairs occupies a different internal
   D boundary. If such a pair belonged to one block, preserving or
   reversing that whole block would make the pair adjacent in E. Moving
   the block among other blocks cannot change this fact. Thus all these
   boundaries are cuts, and b-1>=2(n-1). The argument does not count the
   boundary between runs, any endpoint, or a gadget boundary. It neither
   assumes sufficiency of adjacency nor a minimum-partition formula.

3. **Complete record and field audit.** The format can use a fixed section
   order: old names, occurrence names, D metadata/vertices/transitions/order,
   E metadata/vertices/transitions/order, placeholders, axioms. These are
   twelve sections; their counts together with q,h,n are fifteen numerical
   header fields. Thus the header, including its tag, fits 16(w+1).
   Metadata can give vertex/transition/order counts, root and two terminal
   IDs in six fields. Old-name records need at most three fields;
   occurrence records use four fields and a sign bit. Vertices need ID,
   level and at most two type/scalar flags; transitions need source,
   destination and the queried bit. Orders use two fields. Placeholder
   records use a dense ID, at most two original indices and a kind flag.
   An axiom record can use axiom ID, placeholder ID, word count, two word
   lengths and four tokens: at most nine fields, a kind flag and two
   coefficient bits. With an eight-bit tag this is at most 9w+11, below
   16(w+1). Tags determine arity; no omitted string or variable-length
   reference is required. The level order supplies the query name on
   every transition; coincident successors remain separate records.

   The exact record count with all retained slots is

       R = 1+(n+3)+q+2+(6q+4)+12q+2q+2h
         = q²+22q+n+10
         <= q²+23q+7 <= q²+23q+9.

   This confirms the stated two-record slack rather than using it to
   hide a missing section. All section counts are bounded by this R;
   R<16(q+2)². Local or globally numbered diagram vertices, terminal IDs,
   placeholder/axiom IDs, order positions, original indices and clause
   positions also lie below 16(q+2)². Therefore every numerical field
   fits w bits. The largest tags need far fewer than 256 values.
   Full B has h=q(q+1)/2 independently written axioms and placeholders;
   no coefficient, token or old-name map is omitted. The unary width
   prefix and extra 2 in M are charged separately. The old CNF, derived
   ABP, partition annotation and nonexistent witness are not silently
   included in or used to enlarge this parameter.

4. **All-size comparison.** For s=q+2>=3,
   q²+23q+9<=8(q+2)² follows since the difference is
   7q²+9q+23>0. Also
   w+1<=5+2ceil(log₂ s)<=2s+3<=3s.
   Substituting into the full-record bound gives exactly the bound
   390(q+2)³ in (2); the prefix and extra 2 fit its preceding factor 130.
   Since q+2=2n+8<=4(n+2), the strict comparison with 2^16(n+2)³
   follows from 24960<65536. For n=2^t, t>=6, this gives
   log₂ M_n<19+3t, so the weaker stated floor bound is valid.
   The initial margin is 127-37=90, and its increment is
   2^(t+1)-3>0 at every subsequent integer t. This proves the whole
   infinite range; no numerical preview or asymptotic-only estimate
   substitutes for the finite starting threshold.

The audit therefore confirms L095 and the local stop in Attempt 031,
without changing its conclusion, encoding bound or stated threshold.
The only edit to the original proof is the source page locator. There is
no new lower bound beyond this reproduction of unsigned adjacency
reasoning, and no certified originality. The DAG input remains L087;
L094 is the promise being limited, not a mathematical premise of the
obstruction. The full general W₂ witness question, alternative suppliers,
general ER data and unrestricted SAT remain unresolved.

## Mathlib

Full matching coverage for this occurrence-family and full-bit cutoff
statement has not been checked. The cited primary sources provide the
partition/breakpoint definitions; this proof explicitly supplies the
finite adjacency/counting specialization. Unknown Mathlib coverage is
not evidence of absence. No Lean verification is claimed.
