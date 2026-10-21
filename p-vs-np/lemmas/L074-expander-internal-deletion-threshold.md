# L074 — Linear internal-deletion threshold for the supplied expander family

## Hypotheses

Use either of L031's supplied proofs, with sigma in {0,1}, for a finite
simple graph G=(V,E), n=|V|>=2, m=|E|, maximum degree at most a fixed
integer Delta>=3, and fixed 0<epsilon<1 such that

    |N_G(U) \ U| >= epsilon |U|       whenever |U|<=n/2.

Keep L031's exact definitions and binary encoding, with T=2+|F|+|pi|.
Let H be the underlying undirected simple graph of L071's full signed
Boolean value DAG for that proof. All original inputs are shared; every
positive extension AND vertex, required NOT vertex, unused root and actual
signed operand is retained. Only repeated wires are merged as adjacencies.
Let D be any set of positive internal extension vertices. Original inputs
and NOT vertices are not in D. Write P={p_1,...,p_m} for L031's edge gates
and k_p=|D intersect P|. Deletion means vertex deletion with all incident
wires removed, not Boolean simplification or identification of inputs.

## Conclusion

If tw(H-D)<=2, then

    k_p >= epsilon*n/4-3,             |D| >= epsilon*n/4-3.       (1)

Put

    U(n,m)=128(22m+2n+5) ceil(log_2(22m+n+4)).

If

    epsilon*n/4-3 > floor(log_2(U(n,m)+2)),                     (2)

then no D satisfies both tw(H-D)<=2 and
|D|<=floor(log_2(T+2)). A simpler sufficient finite-size test is

    epsilon*n/4-3 > log_2(C_Delta)+2 log_2(n),                  (3)
    B=11Delta+5,       C_Delta=128B log_2(2B)+1.

For fixed epsilon and Delta, (3) holds for all sufficiently large n.
Thus along any supplied unbounded family with these fixed parameters,
L073's logarithmic positive-internal deletion promise fails eventually
for both sigma choices. This specializes known treewidth machinery;
no new general expander theorem or certified originality is claimed.
It stops this application of L073 only, giving no affine-ABP, unrestricted
ER or SAT lower bound. Small instances failing these tests are not
decided, and alternative data, certificates and proofs remain possible.
The separate step-286 informal critical audit below found no substantive
defect in this restricted conclusion. No formal verification is claimed.

## Proof

**Imported graph inputs.** Use Frank Gurski and Robin Weishaupt,
*The Behavior of Tree-Width and Path-Width under Graph Operations and
Graph Transformations*, [arXiv:2406.08985v1](https://arxiv.org/pdf/2406.08985v1),
13 June 2024, Theorems 17–18 (pp.8–9), Corollary 22 (p.10), Theorem 25
(pp.11–12) and Corollary 26 (p.13). For finite simple graphs these give
vertex-deletion loss at most one per vertex, subgraph monotonicity and
invariance under subdividing every edge once. Use also Dániel Marx,
*Can You Beat Treewidth?*, Theory of Computing **6** (2010), 85–112,
[journal PDF](https://www.theoryofcomputing.org/articles/v006a005/v006a005.pdf),
Lemma 3.2(b), pp.92–93: if tw(J)<=t and W is any vertex subset, some
S subset V(J), |S|<=t+1, leaves every component C of J-S with
|C intersect W|<=|W|/2. S is permitted to meet W.
The primary statements and relevant graph-operation proofs were inspected
in the prior SPECIALIZE assessment
`drafts/literature/2026-10-17-expander-internal-deletion-threshold.md`.
They are imported, not reproved. The necessary specializations below
are the exact signed-gadget subgraph, expansion count and encoded
threshold; none of these sources states the complete ER specialization.

**Identify the subgraph before deletion.** L031 defines
p_i iff (x_(u_i) AND x_(v_i)) for edge e_i={u_i,v_i}.
Both operands are positive original inputs. Hence H contains wires
x_(u_i)--p_i and p_i--x_(v_i). The n original vertices are distinct and
shared across gates; the p_i are fresh and distinct. Choose the subgraph
J on {x_v:v in V} union P with just these 2m adjacencies. Since G is
simple and loopless, J is exactly its once-subdivided graph I(G).
No sign wrapper, q gate, h gate or accumulator is used in J. Taking a
subgraph permits omission of their adjacencies; all these vertices and
wires remain present in H.

Changing sigma changes unit signs and accumulator operands, but not the
p_i definitions. The alias r_1=NOT p_1 neither identifies p_1 with a sign
vertex nor removes it. The identification therefore holds for both
proofs, including m=1, without substituting any original unit clause.
No original input belongs to D, so

    J-D = J-(D intersect P)

is a subgraph of H-D. Deleting other positive gates cannot remove the
retained original--edge-gate adjacencies.

**Finite-size expansion count.** Put t=tw(G). Apply Marx's lemma with
W=V to obtain S of size at most t+1, with every component of G-S of
size at most n/2. We show |S|>=epsilon*n/4. If |S|>=n/4 this follows
from epsilon<1. Otherwise G-S has more than 3n/4 vertices. If a component
has size at least n/4, choose it as U; its size is also at most n/2.
If none does, accumulate whole components until their total first reaches
n/4. Enough vertices remain to do so, and both the previous total and
the last component have size less than n/4. The union U then has
n/4<=|U|<n/2. These real thresholds require no divisibility or rounding
assumption, including at n=2.

In either case U is a union of components of G-S with
n/4<=|U|<=n/2. Every external neighbor of U lies in S, since distinct
components of G-S have no edge between them. Expansion gives

    |S| >= |N_G(U) \ U| >= epsilon |U| >= epsilon*n/4.

Since |S|<=t+1, we obtain

    tw(G) >= epsilon*n/4-1.                                   (4)

Only this component-union specialization is derived here; no stronger
uninspected expander/treewidth theorem is assumed.

**Deletion specialization.** The imported subdivision result gives
tw(J)=tw(G). Iterating the imported one-vertex deletion inequality over
the k_p distinct vertices in D intersect P gives

    tw(J-(D intersect P)) >= tw(J)-k_p.

If tw(H-D)<=2, subgraph monotonicity gives
tw(J-(D intersect P))<=2. With (4) this yields

    2 >= epsilon*n/4-1-k_p,

which proves (1). It forces deletions of edge gates alone, regardless of
other deleted positive gates. It uses neither a minor model after
deletion nor a claim about an isolated output cone. L073's sufficiency
theorem is not an input: its named promise is the condition being tested.

**Actual binary-length comparison.** L031's displayed encoding has

    R_*=22m+n+2,       L=ceil(log_2(R_*+2)),
    T<=128(R_*+n+3)L=U(n,m).

This is the supplied proof's full length, including original clauses,
all definitions and reference framing, not a choice to pad T. Thus (2)
implies epsilon*n/4-3>floor(log_2(T+2)), contradicting (1) whenever
|D| is within the promised allowance.

For (3), use 2m<=Delta*n and n>=2 to obtain

    R_*+n+3<= (11Delta+2)n+5 <= Bn,
    R_*+2<= (11Delta+1)n+4 <= Bn,
    T<=128 Bn log_2(2Bn).

Here ceil(a)<=a+1 pays L's ceiling. For integer n>=2,
log_2(n)<=n-1, since 2^(n-1)>=n by induction. As log_2(2B)>=1,
log_2(2Bn)<=n log_2(2B). Also 2<=n^2. Consequently

    T+2 <= (128B log_2(2B)+1)n^2=C_Delta n^2,
    floor(log_2(T+2)) <= log_2(C_Delta)+2log_2(n).

This proves sufficiency of (3). Its left side has positive fixed linear
coefficient epsilon/4, while its right side is a fixed constant plus
2log_2(n), and log_2(n)/n tends to zero. Thus (3) holds eventually,
uniformly in edge ordering and sigma. No expander-selection algorithm is
required. A finite instance may use (2), retaining its actual m.
No numerical calculation is needed for these all-size inequalities.

**Scope and prior failures.** Attempts 019–021 stop different universal
OBDD and identical-output conversion proposals; their conclusions are
not used as graph lower bounds. L031's immediate opposing-unit refutation
remains available, as do L032's existing circuit data. Failure of a
sufficient promise supplies no necessity theorem for alternative ABP
data or certificates. Arbitrary ER representation, formula-only bounds,
W/V/U and unrestricted SAT decision/separation remain unresolved.

**Separate critical audit — step 286, 2026-10-17.** Reuse the unchanged
SPECIALIZE assessment
`drafts/literature/2026-10-17-expander-internal-deletion-critical-audit.md`.
This REPRODUCTION audit leaves the hypotheses, constants and direct inputs
unchanged. It does not assert a new graph theorem or broader obstruction.

L031's singleton expansion applies for every n>=2. Every original has a
neighbor, so m>=1 and the imported subdivision theorem's edge hypothesis
holds. In L071's full signed graph, p_i has the two positive original
operands x_(u_i), x_(v_i), whatever sign its derived unit has. Freshness
makes the p_i distinct from each other and all originals; simplicity of
G makes their endpoints distinct. Selecting exactly these vertices and
operand adjacencies gives I(G). Wrappers, q gates, h and accumulators are
outside this subgraph; they are not simplified away in the host. At
sigma=0 the accumulator consumes NOT p_i, and at sigma=1 it consumes p_i.
Neither changes the selected edges. The signed original anchor changes
only an accumulator operand. For m=1 there is no q gate, r_1=NOT p_1,
and h has that repeated operand; the selected path through p_1 remains.
Singleton expansion then forces n=2, requiring no extra exception.

Since D contains only positive extensions, its intersection with the
selected vertex set is exactly D intersect P. Deleting a different gate
cannot remove an edge x_u--p_i whose endpoints both remain. This checks
the subgraph inclusion after deletion without assumptions about the
other wires or unused roots. Original-variable deletion would require a
different statement. L073 remains only the promise being tested.

Marx's Lemma 3.2(b) balances components against half the original |W|,
even if S meets W. With W=V(G) their sizes are at most n/2. If |S|>=n/4,
epsilon<1 supplies the desired bound immediately. Otherwise more than
3n/4 vertices remain. A component of size at least n/4 is an admissible U.
If none exists, the first prefix of components reaching n/4 exists, and
both its previous total and final summand are strictly below n/4. Its
total is therefore below n/2. This argument uses real thresholds without
rounding and covers every n>=2. All external neighbors of the resulting
union U lie in S, so expansion gives |S|>=epsilon*n/4. Together with
|S|<=tw(G)+1 this is exactly (4).

The imported deletion inequality has the needed direction
tw(J-v)>=tw(J)-1. Iterating over the distinct deleted p_i and using
subdivision invariance yields tw(J-(D intersect P))>=tw(G)-k_p.
Subgraph monotonicity gives tw(J-(D intersect P))<=tw(H-D)<=2.
Thus k_p>=epsilon*n/4-3, and |D|>=k_p. Both counts are integers, but
retaining this real lower bound is valid. It may be vacuous at small n;
no exclusion is asserted there unless a stated sufficient test holds.

L031 has K=2m circuit gates and K accumulator gates, with record count
at most 11K+n+2=R_*. Its audited gamma-code ledger includes F, headers,
definition slots, signs and references and gives
T<=128(R_*+n+3)ceil(log_2(R_*+2)). Substitution gives exactly U(n,m),
including its +5 and +4. Hence T<=U, and monotonicity of the logarithm
and floor proves (2)'s strict comparison with the actual integer
allowance. Equality is not claimed to suffice.

For (3), 2m<=Delta*n bounds the two arguments by
(11Delta+2)n+5 and (11Delta+1)n+4. Their slacks below Bn are
3n-5>=1 and 4n-4>=4. The ceiling obeys
ceil(log_2(R_*+2))<=log_2(R_*+2)+1<=log_2(2Bn).
Writing a=log_2(2B)>=1, the existing elementary bound gives
log_2(2Bn)=a+log_2(n)<=a+n-1<=an. Consequently
U<=128Ba*n^2 and T+2<=U+2<=C_Delta*n^2, since 2<=n^2.
This confirms C_Delta and (3); in fact (3) implies (2) as well.
The limit log_2(n)/n=0 supplies an eventual threshold depending only
on fixed epsilon>0 and fixed Delta, uniform in ordering and sigma.
No such uniformity is claimed if epsilon decays or Delta grows with n.
These checks use neither padding nor numerical evidence.

No substantive defect was found and no argument or DAG change is needed.
Attempt 028's family stop remains. It excludes one sufficient structural
promise, not alternative data, certificates, other refutations or SAT
algorithms. The immediate opposing-unit refutation and unfinished work
remain available. No mathematical script was needed; Mathlib remains
not checked.

## Mathlib

Full matching coverage and supporting subdivision, vertex-deletion and
balanced-separator theorem names in Mathlib are **not checked**; no
absence claim is made. The precise primary inputs are cited above;
the signed-ER and finite-size specialization is proved here under the
ready assessment, classified REPRODUCTION.
