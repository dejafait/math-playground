# L083 — Used repeated self-ANDs obstruct the counted-path supplier

## Hypotheses

Use the fresh signed-AND ER and full-bit conventions of L027 and
foundations/05. In particular repeated operands are allowed, clauses
are sets with duplicates removed, and every resolution names its earlier
premises and signed pivot. Original variables are exactly those occurring
in the original CNF. Retain the full canonical signed value DAG, both
signs, original-root associations and every ordered operand occurrence.

Use precisely L080/L081's unsimplified original-input restrictions:
queried occurrences become scalar leaves; signs inherit support, ANDs
take the union of operand supports, and products by zero are retained.
With actual original length T=2+|F|+|pi|, keep
k=floor(log₂(T+2)). A counted AND has BOTH operand supports larger than
k; every ancestry path from every root must contain at most k counted
ANDs. For the tree assertion use L081's explicit finite full binary
original-input query trees, with no repeated query on a path.

## Conclusion

There is a polynomial-time constructible family, indexed by n=2^r for
integers r>=10, of width-one original CNFs F_n and width-at-most-three
ER refutations pi_n, with the following properties.

1. All n inputs occur originally. Every introduced extension has both
   a defining clause and a derived positive unit in the final inference
   ancestry. Its defining circuit is evaluated on every original-input
   assignment, including those violating F_n.
2. The actual full encoded length T_n satisfies

       T_n+2 <= 2^15 n² r,       k_n <= 15+3r,
       n > 2k_n,                n² > k_n.                 (1)

   In particular T_n=O(n² log(n+2)).
3. For every set D of originals and every assignment alpha on D, its
   residual satisfies the all-root counted-path promise if and only if

       |D| >= n-k_n.                                      (2)

   No cardinality assumption |D|<=k_n is used in this statement.
4. Every L081-admissible tree for this supplied proof has M leaves with

       M >= 2^(n-k_n).                                    (3)

   A full fixed-order tree querying any n-k_n originals attains this
   leaf count. Moreover (n-k_n)/log₂(T_n+2) tends to infinity along the
   family, so no fixed polynomial in T_n bounds these leaf counts.

Thus L080's allowed sets do not exist on this supplied family, and
L081 cannot receive it with polynomial-full-bit trees in T_n. These are
obstructions to the stated structural promises on supplied proofs,
not bounds against alternative data, proofs or certificates, ER proof
length, or unrestricted SAT. The original CNF has an immediate
alternative refutation. The separate step-323 informal critical audit
below finds no substantive defect and changes no hypothesis or bound.
The construction's POTENTIALLY_NEW records only the inspected-source comparison,
not certified originality or progress beyond all existing literature.

## Proof

**Scope, reuse and test.** The pre-invocation EXPLORE assessment is
`drafts/literature/2026-10-18-counted-path-repeated-square-obstruction.md`.
It compares the exact target with restricted-query CNF backdoor bounds,
arithmetic non-skew depth, the local repeated-square examples and prior
failed conversion routes. None of those results is imported as this
bound. We specialize L027's already written signed-unit/accumulator
host and gamma-code ledger, not its HWB circuit or OBDD theorem. The
new work is the conjunction/square instance, unchanged-cutoff ledger and
support/path threshold. Giving the particular inferences below verifies
that the reused host accepts repeated operands and the promised family;
it does not reprove any external theorem. L082's audited replacement is
imported for the arbitrary-tree assertion, with its unrestricted-M
qualification. The downstream purpose is to test universality of the
structural supplier. Continue this obstruction only if genuine use,
polynomial full bits, n²>k, n>2k and the unbounded ratio all hold.

**Originals and core.** Set

    F_n = (x_1) AND ... AND (x_n) AND (NOT x_1).

These n+1 unit clauses have exactly n originals. Introduce c_2 iff
(x_1 AND x_2), followed by c_j iff (c_(j-1) AND x_j), j=3,...,n.
Set s_0 to be the alias c_n and introduce n² fresh gates

    s_t iff (s_(t-1) AND s_(t-1)),   t=1,...,n².             (4)

Every operand is earlier and every defined variable fresh. List these
H=n²+n-1 core gates as g_1,...,g_H in that order. On the all-one original
assignment every core gate is one. Derive its positive unit from its
third defining clause and the two positive operand units: two resolutions
for each conjunction gate; just one for each square, since its third
clause is (s_t OR NOT s_(t-1)) after duplicate removal. No truth-table
enumeration or semantic restriction of the value DAG is used here.

**Genuine final ancestry.** Specialize L027's accumulator device with
all epsilon_i=g_i. Let a_0 be the alias x_1, and introduce fresh

    a_i iff (a_(i-1) AND g_i),   i=1,...,H.

The underlying operand variables are distinct. Resolve the third defining
clause with units (a_(i-1)) and (g_i) to derive (a_i), in two steps.
Separately resolve (NOT a_i OR a_(i-1)) against (NOT a_(i-1)) to derive
(NOT a_i), starting with original (NOT x_1). Finish by resolving (a_H)
against (NOT a_H). These are all legal ordered earlier references; all
clauses have width at most three.

Recursing backwards from (a_H), every (a_i) and (g_i) is a premise
ancestor. Each core unit derivation uses that core gate's third defining
clause. Each accumulator positive unit uses its own third clause, while
the negative chain uses its first projection. Thus every one of the 2H
introduced extensions has a defining clause and a derived positive unit
in final ancestry. In particular s_(n²) is an actual accumulator operand
whose unit is used, not an unused circuit appended to a refutation.
Unused individual projection clauses are allowed. No nonextension
variable absent from F_n is introduced.

The all-assignment recursive value of c_j is the conjunction of the
first j inputs and every s_t has the same Boolean value as c_n. This
semantic equality does not contract (4) in the canonical syntactic DAG.
Every such value and every accumulator still has its own retained root.

**Full binary ledger and unchanged actual cutoff.** Use the explicit
encoding of L027: gamma-code a nonnegative integer u by the Elias gamma
code of u+1, of length 2 floor(log₂(u+1))+1. Encode F by n, clause count
and its clauses. Prefix each clause by its size; a literal has a sign
bit and variable identifier. Encode pi by record count, and per record
a two-bit kind, written clause, and either initial-clause index, extension
variable plus two-bit definition slot, or two premise references and a
signed pivot. Operands are recovered from the three defining clauses.
Repeated-operand blocks remain unambiguous after clause deduplication.

There are 6H definition records, at most 2H core-unit resolutions, 2H
positive accumulator resolutions, H negative accumulator resolutions,
one final resolution and n+1 initial records. Hence the actual record
count R is at most

    R_* = 11H+n+2 = 11n²+12n-9.

Variable identifiers are at most n+2H<=R_*, as are reference indices,
clause indices and all other encoded integers. Put
L=ceil(log₂(R_*+2)). Each integer code costs at most 2L+1<=3L bits.
A clause costs at most 3L+3(1+3L)<=15L bits. Record kind costs at most
2L; the largest additional field list is two references and a signed
pivot, costing at most 10L. Thus 64L safely bounds each record,
including each independently repeated clause. Headers and F's n+1
written units fit the conservative complete bound from the same host:

    T_n <= 128(R_*+n+3)L.                                  (5)

For completeness, F costs at most (7n+13)L, pi's count header at most
3L, and all pi records at most 64R_*L; these plus T's constant 2 are
bounded by (5). This charges both original and proof copies of the
initial clauses, all identifiers, metadata and references, rather than
only the number of gates. Enumeration, all-one unit derivations and
record production take polynomial bit time.

For n=2^r, r>=10 (indeed for n>=2), direct inequalities give

    R_*+n+3 = 11n²+13n-6 <= 18n²,
    R_*+2 <= 18n²,
    L <= 6+2r <= 8r.

Consequently T_n+2 <= 18432 n²r+2 <= 2^15 n²r, and

    log₂(T_n+2) <= 15+2r+log₂ r <= 15+3r.                  (6)

Here k_n is still computed from the actual encoded T_n, not from the
upper bound (5). Inequality (6) merely bounds that unchanged cutoff.
For r=10, 2^r>30+6r. If this holds at r, then
2^(r+1)>60+12r>30+6(r+1), so it holds for every r>=10.
It follows that n>2(15+3r)>=2k_n, and then n²>k_n. This proves (1).
No padding parameter chosen after k_n is needed: the fixed n² chain
already exceeds it.

**Exact deletion threshold, including zero products.** Fix any D among
the n originals, with no logarithmic size restriction, and any assignment
alpha on D. Each undeleted original has its singleton support, each
replaced occurrence empty support, and retained signs inherit support.
By induction, c_j has support {x_1,...,x_j} minus D. Each operand of
every s_t has support {x_1,...,x_n} minus D: union with the same set
preserves it at every square. This holds even when a queried bit is zero
and every square has Boolean value zero. Zero multiplication is not a
support simplification. Repeated operands stay two actual operand
occurrences with identical supports.

If n-|D|>k_n, both operands of each of the n² square gates have support
larger than k_n. Starting at retained root s_(n²), a source-ancestry path
can choose either operand at each successive square and then continue
to c_n. This one path contains all n² counted squares. Since n²>k_n,
the all-root promise fails, independently of alpha. Thus any successful
set must have |D|>=n-k_n, before any appeal to |D|<=k_n.

Conversely, if n-|D|<=k_n, every support at every node of the entire
canonical DAG is a subset of the remaining originals, by the same
base/sign/union induction. This includes all accumulators, both signed
wrappers and associated scalar roots. No AND has either operand support
larger than k_n, so every path has zero counted ANDs. This proves (2),
for all assignments on each D. Combining (2) with n>2k_n excludes all
sets permitted by L080. Constants, both signs and all retained roots
have been accounted for; no restricted ER proof is assumed.

**All explicit adaptive trees and the required asymptotic threshold.**
Take any L081-admissible tree with M leaves, without assuming M<=T_n+2.
L082 gives the queried set D on a shortest leaf path, satisfying the
residual promise for every assignment, and 2^|D|<=M. Its proof requires
only the unsimplified residual convention and full binary branching,
which are precisely the present hypotheses. By the unrestricted-set
necessity in (2), |D|>=n-k_n, proving (3). This does not invoke the whole
L080 theorem outside its cardinality range. Conversely, query any n-k_n
originals in a fixed order in a full binary tree. Every leaf satisfies
(2), so that tree is L081-admissible and has exactly 2^(n-k_n) leaves.

From (6), using the positive numerator ensured by (1),

    (n-k_n)/log₂(T_n+2)
      >= (2^r-15-3r)/(15+3r) -> infinity.                  (7)

For example 2^r/r tends to infinity: its ratio at successive r is
2r/(r+1)>=3/2 for r>=3. This proves the limit in (7) without a finite
preview or numerical extrapolation. Thus for every fixed C>0 and e>=0,
(3) eventually exceeds C(T_n+2)^e. L081's explicit encoding has
M<=B+1, so B also cannot have a fixed polynomial bound in T_n.

**Limit of the obstruction.** F_n is immediately refuted by original
(x_1) and (NOT x_1). Its original-axiom tree certificate
C=t_(x_1)+t_(NOT x_1) satisfies C(x,0)=0 and
C(x,A)=(1+x_1)+x_1=1 over F₂. Therefore these supplied-proof structural
bounds imply no optimal-proof or alternative-certificate hardness.
They stop universality of the particular L080/L081 promises, not the
conditional correctness of their suppliers. Other ABP data, semantic
simplification, compressed query DAGs and changed promises remain
outside this conclusion. Attempts 016–017 and 019–020 are preserved;
none of their stopped conversion premises is assumed here. All-size
legality, ancestry, encoding and threshold proofs are given above; no
mathematical script or finite experiment is needed for this attempt.

**Separate critical audit — step 323, 2026-10-18.** The pre-invocation
EXPLORE assessment is
`drafts/literature/2026-10-18-repeated-square-obstruction-critical-audit.md`.
This is REPRODUCTION: an independent informal check of the existing
argument, not another construction or a claim of originality. The
step-319 primary comparison and duplicate/failure checks are reused;
neither the external CNF-backdoor nor arithmetic-depth comparison is
a mathematical premise. The checks below receive only L027's host and
encoding, foundations/05's ER rule, L080/L081's structural hypotheses
and L082's audited arbitrary-M replacement.

For legality, write u=s_(t-1) and z=s_t. The three definition records
have clauses (NOT z OR u), (NOT z OR u), and (z OR NOT u).
Duplicate literal removal changes the third clause's width, but does
not prohibit two records with identical clauses. Resolving that third
record with the earlier (u), on pivot u, gives exactly (z) in one step.
The first two slots still recover the two identical ordered operands;
no operand metadata is lost. Freshness holds because z is new and u is
earlier, even for t=1 where u is the alias c_n. For a conjunction gate
with distinct operands p,q, its third clause resolves with (p) to
(z OR NOT q), then with (q) to (z). All units needed here are available
from the original positive units and the topological core order.

Each accumulator's operands a_(i-1),g_i are distinct: for i=1 one is
the original x_1 and the other the fresh first core gate, and thereafter
one is an accumulator variable and the other a core variable. Its two
positive resolutions therefore have the same legal distinct-operand
form. Its negative inference resolves (NOT a_i OR a_(i-1)) with
(NOT a_(i-1)), giving exactly (NOT a_i). One legal total proof order is
all original records, the core blocks and their units, then the
accumulator blocks with their positive and negative units in increasing
i, then the final resolution. Every reference in this order is earlier.
Backward ancestry through the final positive accumulator unit reaches
every g_i unit and every positive accumulator unit; their third clauses
are ancestors as well. The negative final unit traces through every
first accumulator projection to (NOT x_1). This verifies use of all
2H definitions, including the last square, without requiring every
projection clause to be an ancestor. All n original variables occur
in F, so none is subject to the absent-original-to-zero convention.

The exact core-unit count is 2(n-1)+n², which is at most 2H. Counting
the original records, 6H definition records, these core resolutions,
the 3H accumulator resolutions and the final resolution gives at most
R_*=11H+n+2. No separate definition description is required by the
stated encoding: the extension name and the three numbered slots retain
the operand order, including repetitions. Every encoded integer is
bounded by R_*: this includes n, n+1, R, clause sizes, variable and
pivot names, original-clause indices and earlier references. A
definition slot and each literal/pivot sign are charged separately.
With L=ceil(log₂(R_*+2)), each integer code is at most 3L; a width-three
clause uses at most 12L+3<=15L; a resolution's extra fields use at most
9L+1<=10L. Definition and initial-record fields are smaller. Adding
the two kind bits leaves a record at most 27L<=64L. F's two headers and
n+1 units use at most (7n+13)L, the proof count uses at most 3L, and
T includes its constant 2. These quantities fit (5), including all
repeated copies of clauses. This verifies an explicit full encoding,
not a gate-count surrogate. No generated proof stream is certified here.

For the numerical range, 11n²+13n-6<=18n² for n>=2, and
R_*+2=11n²+12n-7<=18n². At n=2^r this gives
L<=ceil(log₂ 18)+2r=5+2r<=6+2r<=8r. Thus the stated looser
18432n²r+2 bound and its comparison with 32768n²r hold throughout
r>=10. Taking logarithms bounds the actual k; no equality with this
upper bound or recalculation after restriction is used. The base
2^10>30+6·10 and the displayed doubling induction establish n>2k
for every family member, hence n²>k. Polynomial construction time is
consistent with the full output: there are O(n²) constant-width records
with O(log n)-bit names, and topological enumeration does not unfold
the repeated-square circuit.

For arbitrary D, the conjunction support induction starts with the
remaining original singleton supports. A square preserves their full
union, so both its operands have size n-|D|. If that exceeds k, the
path through s_(n²),s_(n²-1),...,s_1 counts n² distinct AND nodes;
the two repeated operand positions provide alternatives, not two
successive visits to the same node. This path alone violates the
promise. Conversely n-|D|<=k bounds every operand support, including
accumulator operands and negative wrappers, by k. Every counted
indicator then vanishes. Assigned zero bits cannot shorten the former
path or remove a support under the stated unsimplified restriction.
Associated scalar roots have empty support and add no counted paths.
This checks both directions for all D and all assignments without
invoking L080's additional |D|<=k assumption.

L082 receives exactly these retained paths and supports and applies
for every finite M, including M>T+2. Its shortest-path set satisfies
the unrestricted necessity just checked, so 2^(n-k)<=2^|D|<=M.
Since 0<=k<n, a fixed-order tree on n-k distinct originals exists;
all its leaves satisfy the sufficiency direction, attaining the bound.
For the limit, both n-k and log₂(T+2) are positive. Their respective
lower and upper estimates justify (7) with the inequality in the
stated direction. The geometric lower bound on successive 2^r/r
proves divergence, so log₂ M-e log₂(T+2)-log₂ C tends to infinity
for every fixed C>0,e>=0. The explicit-tree inequality B>=M-1 then
rules out a polynomial B as well. No polynomial-leaf assumption was
used to obtain the lower bound.

Finally, the two opposing original units have falsity polynomials
1+x_1 and x_1. Their placeholder sum has both stated formal identities,
and resolving the two original units is an alternative refutation.
The three-node certificate expression may still require binary names
and an input dictionary; the claim here is constant expression size,
not a constant complete package for growing F_n. This qualification
does not alter any theorem bound. The obstruction concerns only the
specified structural promises on the supplied proof. It supplies no
lower bound for alternative representatives, witnesses, proofs or
certificates, and no unrestricted SAT consequence. No substantive
defect or missing mathematical input was found; all four direct DAG
inputs retain their existing roles. The argument and DAG are unchanged.

## Mathlib

Full matching ER-ancestry, unchanged-cutoff support obstruction and
adaptive-tree bound: **not checked**. No absence is inferred. The host
and finite-tree replacement are local informal inputs L027 and L082;
no external arithmetic-depth or CNF backdoor lower bound is imported.
The source assessment records precise primary comparisons and their
qualifications. Step 323 checks the construction and (5)–(7) informally;
no formalization, verified proof strings or certified originality is
claimed.
