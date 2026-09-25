# L012 — Polynomial extended-resolution refutations by certified parity row addition

## Hypotheses

Fix an integer Δ≥2. Let G=(V,E) be a simple connected graph on n≥3 vertices, with m edges and 2≤deg(v)≤Δ. Index its edge variables consecutively by x₁,…,x_m. Let χ:V→F₂ have odd total charge. The CNF T(G,χ) contains, at every vertex v, all clauses forbidding the assignments to its incident edges whose parity differs from χ(v). Its binary length is N, with variable identifiers, signs, and separators charged.

Use [the notebook's ER convention](../foundations/05-refutation-systems-and-simulation.md): resolution, weakening, clause reuse, and fresh definitions z↔(ℓ₁∧ℓ₂), each contributing its three defining clauses. All operands of a definition are previously available literals. Charge all written literals, binary variable identifiers, and inference references. No semantic-consequence or XOR rule is added to ER.

## Conclusion

There is a uniform polynomial-time procedure that constructs an ER refutation of T(G,χ), with

- O_Δ(n(m+1)) clauses and fresh variables;
- maximum clause width at most max(Δ+1,6);
- total binary proof length O_Δ(n(m+1) log(n+m+2)).

The procedure can obtain the equations from the CNF alone by grouping equal clause supports as in L010; it does not need a supplied graph or an expansion certificate. For L010's degree-at-most-26 family this is O(n² log(n+2)) bits, hence O(N²) bits, whereas ordinary resolution requires 2^{Ω(N/log N)} lines on the same odd-charge formulas.

This supplies an explicit simulation of the parity row additions used here. It neither makes ER polynomially bounded on all UNSAT formulas nor simulates arbitrary rejecting SAT computations.

## Proof

**A finite consequence compiled into actual resolution.** Suppose a set H of available clauses involves at most k variables and entails a non-tautological clause C on those variables. Fix the variables of C to their unique values falsifying C. For each assignment to the other variables, some clause of H is false. Weaken that clause to the full clause D containing exactly the literals falsified by this complete assignment. In particular, D contains C. Resolve pairs that differ only on the last free variable, then on the preceding free variable, until C remains. There are at most 2^k leaves and fewer than 2^k resolutions, and every clause has width at most k. If there are no free variables, the falsified premise is already a subset of C and one weakening suffices.

This is an explicit construction using only resolution and weakening; semantic entailment is used to justify which finite construction succeeds, not as a proof rule. For each use below k≤6. Tautological target clauses can be omitted, repeated literals are identified, and identifying input wires can only reduce the number of distinct variables. If an already available clause is the target, reuse it.

**False and two-input XOR from legal extensions.** Pick the existing edge variable x₁. Introduce f↔(x₁∧¬x₁). Resolving its first two clauses (¬f∨x₁) and (¬f∨¬x₁) gives ¬f. Its third defining clause is included even though it is tautological.

To define c=a⊕b for any two available wires a,b, introduce in order

u↔(a∧b),  v↔(¬a∧¬b),  c↔(¬u∧¬v).

These are three permitted fresh AND definitions. Their nine clauses involve at most five distinct variables and imply the following four clauses, denoted Q(a,b,c):

(a∨b∨¬c), (a∨¬b∨c), (¬a∨b∨c), (¬a∨¬b∨¬c).

They forbid exactly the assignments with c≠a⊕b. The finite construction above derives each non-tautological clause in constant size from the nine definitions. Thus every XOR occurrence costs a fixed number of legal ER lines and three fresh variables, including when its operands coincide. Subsequent local derivations use these four derived clauses; they need not mention the internal u,v wires.

**Canonical prefix chains for a coefficient row.** For s=(s₁,…,s_m)∈F₂^m, set p₀(s)=f. If s_j=0, let p_j(s) denote the very same wire as p_{j−1}(s), with no new definition. If s_j=1, introduce the XOR gate

p_j(s)=p_{j−1}(s)⊕x_j.

A newly constructed row uses fresh gates at its nonzero coordinates. Different occurrences of the same coefficient vector may use different fresh chains; p_j(s) always refers to the chosen row occurrence. Its output is p_m(s). A zero row has every prefix equal to the existing wire f; it introduces no gates. Omitting zero coefficients therefore does not require a separate equivalence proof between sparse and dense circuits.

Write ℓ(y,b) for y when b=1 and ¬y when b=0. A certified row (s,b) consists of its prefix-chain definitions and the derived unit ℓ(p_m(s),b).

**Certifying an initial vertex row without enumerating extension assignments.** Let its d incident edge variables, in order, be x_{i₁},…,x_{i_d}, and let its prescribed charge be b. Construct its prefix chain, with final output p. For each assignment a∈{0,1}^d, let D_a be its full blocking clause on these original variables. We derive D_a∨ℓ(p,b).

If a has parity different from b, D_a is an initial clause of T(G,χ), so one weakening suffices. If a has parity b, first weaken ¬f to D_a∨¬f. Inductively suppose the current prefix wire q has value ε under a, and D_a∨ℓ(q,ε) has been derived. If the next active variable x has assigned value α and the next wire is r=q⊕x, its derived XOR clauses include

¬ℓ(q,ε) ∨ ¬ℓ(x,α) ∨ ℓ(r,ε⊕α).

Resolve this with the conditional prefix clause on q. The literal ¬ℓ(x,α) already belongs to D_a, leaving D_a∨ℓ(r,ε⊕α). The prefix wires are fresh extensions and do not occur in D_a, so this pivot is legitimate. After the d active coordinates the resulting clause is D_a∨ℓ(p,b).

Now resolve these clauses over all 2^d assignments in a complete binary tree on the original d variables. The common literal ℓ(p,b) remains as a unit. This construction uses O((d+1)2^d) lines and width at most max(d+1,5), including the XOR macro derivations. It enumerates only the original local assignments, never all assignments to the whole graph or its extension circuit. Since d≤Δ is fixed, the cost is O_Δ(1) per vertex. The initial clauses themselves are also charged.

**Certifying one row addition coordinate by coordinate.** Suppose certified rows (s,b_s) and (t,b_t) are available. Construct a fresh prefix chain for r=s+t over F₂. At every j derive Q(p_j(s),p_j(t),p_j(r)). At j=0 all three wires are f, and the only non-tautological member of Q(f,f,f) is ¬f, already derived.

For the induction step write a=p_{j−1}(s), b=p_{j−1}(t), c=p_{j−1}(r), x=x_j, α=s_j, and β=t_j. The previously derived Q(a,b,c) asserts c=a⊕b. The next prefixes have values

a′=a⊕αx,  b′=b⊕βx,  c′=c⊕(α⊕β)x,

where a zero coefficient means an alias, not a gate. Therefore

a′⊕b′ = a⊕b⊕(α⊕β)x = c′.

This calculation has only four coefficient cases. If (α,β)=(0,0), the old invariant is reused. In each of the other three cases exactly two of the three prefix chains take an XOR step. The old invariant and these two gates' already derived Q clauses involve at most six distinct wires: a,b,c,x and the two new prefix wires. They entail each clause of Q(a′,b′,c′). Apply the explicit finite consequence construction to obtain these clauses in a fixed number of resolution/weakening lines. All identifications or repeated operands are covered by the same construction.

At j=m the invariant states p_m(r)=p_m(s)⊕p_m(t). Resolve its appropriate clause with the two available row units to obtain ℓ(p_m(r),b_s⊕b_t); alternatively the same finite consequence construction uses at most three variables. This completes a certified row addition in O(m+1) lines and fresh variables, with a constant independent of the rows and graph. No semantic correctness assertion about a general algorithm has been assumed.

**Summing the vertex rows.** Start with the certified zero row of charge 0, whose output unit is ¬f. Certify each vertex row from its own initial parity block, then add it to the current accumulated row by the preceding construction. After all n rows, each edge coefficient has been added twice, because the graph is loopless and each edge has two endpoints. The final coefficient vector is therefore zero. Its charge is the assumed odd total, so its certified output unit is f. Resolve this with ¬f to obtain the empty clause.

**Uniformity and size.** There are 2m nonzero entries among the initial vertex rows, and at most nm gates among the n newly constructed accumulated rows. The initial-unit derivations use at most O(n(Δ+1)2^Δ) lines. The n certified additions use O(n(m+1)) further lines. The false definition and final inference have constant cost. Thus the number of clauses and fresh variables is O_Δ(n(m+1)), with width bounded by max(Δ+1,6).

For fixed Δ, the largest variable identifier and line reference are O_Δ(n(m+1)). Every one therefore has O_Δ(log(n+m+2)) bits. Including all clauses, definitions, rule tags, and references gives the asserted binary proof length. Since n≤m≤Δn/2, it is O_Δ(n² log(n+2)). Every finite enumeration in the producer concerns at most Δ original vertex bits or six local wires, so writing the whole proof is uniform polynomial time. Constants depend on the fixed Δ, not on n or χ.

To produce it from the CNF alone, normalize clauses and group their supports using L010's polynomial-time parity-block recognizer. In these graphs different vertices have different supports: two vertices share at most one edge, while every vertex has at least two incident edges. Hence the recovered rows are exactly the vertex rows, in some order. Each edge column occurs in two recovered rows and their charges sum to 1, so the construction applies without recognizing the graph construction or its expansion. Behavior on other inputs can be bounded by parsing, checking this fixed-width form, and returning failure if those tests do not pass; no promise is needed for the producer's running time.

For L010's graphs, its binary-length estimate is N=Θ(n log n). Our bound O(n² log(n+2)) is in particular O(N²), while L010 supplies a lower bound of 2^{Ω(N/log N)} for resolution without extensions. The difference is possible because the current proof uses fresh prefix variables and their defining clauses. The resolution width theorem does not apply to ER by ignoring those added variables.

**Required versus achieved.** The achieved bound is a polynomial upper bound on ER refutations of the existing parity family, together with an explicit local row-addition compiler. Thus this particular family cannot furnish superpolynomial ER lower bounds. The main target still requires a polynomial-time SAT algorithm or an exclusion of all such algorithms. An ER lower-bound route still lacks both a suitable hard family and a justified implication from SAT∈P to polynomial boundedness of ER. The construction does not supply short ER proofs of the rejection-soundness CNFs from L011 or a general theorem certifying arbitrary computation traces.

**Supplementary verification.** `PYTHONDONTWRITEBYTECODE=1 python3 scripts/tseitin-er/check_proofs.py` constructs proof records and checks them using a separate syntax-only verifier. It checks all four row-addition coefficient cases, then 116 odd-charge refutations on 13 small connected graphs, including every connected minimum-degree-two graph on three or four vertices, the five-cycle, and the complete graph on five vertices. All 185076 generated clauses passed; the largest proof had 3425 clauses and the largest width was 6. A deliberately corrupted final resolution inference was rejected. The output is saved in `scripts/tseitin-er/small-proofs.txt`. These checks test the macro compilation and legal inference bookkeeping; the uniform bounds and asymptotic comparison follow from the proof above.

## Mathlib

Coverage: **not checked** for the full ER refutation bound, row-addition compiler, or supporting Boolean/proof-system formalizations. No absence claim or unverified Mathlib identifier is asserted. The full informal proof is supplied above. The external Ben-Sasson–Wigderson theorems preserved in the resolution-width foundation support L010's contrasting resolution lower bound, not a matching statement for the ER upper bound proved here.
