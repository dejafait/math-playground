# L026 — Reduced original-axiom data from common-order OBDDs

## Hypotheses

Use L025's original width-at-most-three CNF F, valid fresh acyclic AND-extension ER refutation pi, binary length T=2+|F|+|pi|, and original axiom list A(x). There are n distinct original variables in F, so n<=T. Work in the free noncommutative ring over F₂ with independent original x and axiom placeholders t. Write b_j for the placeholder of x_j²+x_j and c_ij for the pair-once placeholder of x_i x_j+x_j x_i (i<j). Original clause placeholders will be unused in the reduced relations. All arithmetic circuits have division-free fan-in-two gates with sharing.

For every positive extension value supply an explicitly layered deterministic OBDD, with one common order y_1,...,y_n of the original variables. A level-k state queries y_k and has two successors at level k+1; level n+1 has terminals 0,1. Each nonterminal level has at most w states, w>=1. Diagrams have dense explicit level/state identifiers and roots, and include redundant tests if needed to fill skipped levels. No reduction/canonicity assumption is imposed. Terminal labels and the common order are explicitly encoded.

The diagrams are promised to compute the extension functions on every Boolean assignment to the original variables. These functions are evaluated recursively through the ER definitions, with signed literals complemented and with every nonextension proof variable absent from F set to 0, as in L025. Thus the output diagram of each definition agrees on all Boolean assignments with the AND of its two signed operand functions. The promise is not inferred from arbitrary circuit identity testing. No bound w=T^{O(1)} is assumed for arbitrary ER extensions.

## Conclusion

There is a polynomial-time construction of L025's abstract reduced DAG and supplied representative/relation data. Original variables have representative x_j, constants have 0,1, every signed node is exactly 1+r_a, and each reduced AND node i has an x-only representative r_i and a witness H_i using only the original Boolean and commutator placeholders, such that formally

H_i(x,0)=0,                    H_i(x,A(x))=r_i+r_a r_b.             (1)

The constructed data satisfy

S=O(T+n+2),     d=max(1,n),     h=max(1,2n-1).                     (2)

In fact d and h bound syntactic degrees of the written representative and relation circuits, and every monomial of H_i contains exactly one placeholder unless H_i is zero. There are no new free variables or placeholders.

For a full encoding bound put B=T+n+2, v=w+2, and

M=B(n+1)²v+T(n+1)v²+n²+1.

A common arithmetic DAG for the construction has O(M) gates. Even writing every supplied representative and relation as a separate rooted DAG, retaining their labels and abstract-node/root associations and writing the original axiom list, gives

E=O(B M (T+log(M+2))+T³).                                        (3)

The same allowance covers the explicit input diagram descriptions. The constants are independent of extension depth, w, n and T. These are fixed polynomial bounds in T,n,w, not bounds in path-unfolding size.

Consequently these data meet L025's hypotheses. Its existing construction has complete pre-substitution formal degree at most h+(4S+T²+2T+2)d and full binary size polynomial in T,n,w. If w is polynomial in T, both are polynomial in T. This is a restricted structural consequence. Small common-order OBDDs for arbitrary extensions, tree conversion, hardness of every admissible certificate, unrestricted proof lower bounds and SAT decision transfer remain unproved. This is not a P-versus-NP candidate or a claim of certified originality.

## Proof

**Ordered representatives and exact signs.** For a state u at level k let u_0,u_1 be its successors. Set e_(k,0)=1+y_k and e_(k,1)=y_k. Define bottom-up

r_0=0, r_1=1,             r_u=e_(k,0) r_(u_0)+e_(k,1) r_(u_1).    (4)

Every monomial in r_u is an increasing word in the suffix variables y_k,...,y_n, with no repetitions. This follows by induction because y_k precedes every variable in each child. Its syntactic degree is at most s=n-k+1. Evaluating (4) at a Boolean assignment selects the indicated successor, so it computes exactly the diagram's Boolean function. Each state needs only constantly many arithmetic gates, with child roots shared.

We will use the following precise bridge from Boolean agreement to a free-ring identity. Evaluation on {0,1}^s is injective on the vector space of increasing multilinear suffix words. For completeness, this specialization follows by induction on s: split a polynomial uniquely as A+y_k B, where A,B are increasing multilinear polynomials on the remaining suffix. If all Boolean evaluations vanish, setting y_k=0 gives A=0 by induction; setting y_k=1 then gives B=0. The scalar case s=0 starts the induction. This proves equality in the free ring for two polynomials in this subspace. It does not assert injectivity for arbitrary free polynomials or supply a general efficient multilinearization algorithm. The short argument is needed specifically for this free-ring bridge; it is not a reproof of an OBDD reduction or Apply algorithm.

A signed copy of any diagram is obtained by complementing its terminal labels and retaining all states/transitions. Its state representative r_u^- satisfies r_u^-=1+r_u as a formal identity: the terminal case is exact, and induction in (4) gives

e_(k,0)(1+r_(u_0))+e_(k,1)(1+r_(u_1))
 =1+e_(k,0)r_(u_0)+e_(k,1)r_(u_1),

using e_(k,0)+e_(k,1)=1. For the abstract signed node we write the actual circuit 1+r_u; the signed diagram is an auxiliary representation of this identical polynomial. No extra sign-correction witness is needed.

Add trivial diagrams for original variables and constants. A variable diagram has width at most two: it queries that variable once and thereafter follows the appropriate constant state; preceding and other redundant tests have identical successors. Its root is formally x_j, by (4) and the bridge above (or direct cancellation). Constant diagrams have width one. They are auxiliary only; the actual original and constant representatives retain their prescribed input/constant gates. Nonextension variables absent from F use the constant-0 diagram. Every signed operand in a definition is therefore represented by an available signed diagram, even if it is a constant, an original variable or a repeated operand. Each individual diagram has width at most v; counting positive and signed diagrams separately still gives O(B) diagrams.

**Commuting a suffix with one earlier variable.** If y_k precedes a state u at level j>k, construct K_(u,k) satisfying

K_(u,k)(x,0)=0,       K_(u,k)(x,A)=r_u y_k+y_k r_u.                (5)

Let c(k,j) be the original pair placeholder for the distinct original variables y_k,y_j, indexed in whichever original identifier order is increasing. Over F₂ its axiom value is y_j y_k+y_k y_j in either order. Put K=0 at terminals and at level j use

K_(u,k)=e_(j,0)K_(u_0,k)+e_(j,1)K_(u_1,k)
          +c(k,j)(r_(u_0)+r_(u_1)).                              (6)

This is L020's ordered product/addition commutator recurrence specialized to (4). Indeed [e_(j,a),y_k]=y_j y_k+y_k y_j for both a=0,1, while

[e r,y_k]=e[r,y_k]+[e,y_k]r.

Here brackets mean pq+qp and all product orders are as written. Substituting the child identities proves (5), and every summand in (6) contains a zero-at-zero witness or placeholder. The recurrence applies separately to signed copies with the same proof.

If u has s suffix levels remaining, (6) has syntactic degree at most s: each inherited K gains at most one from e, and the last term has degree at most 1+(s-1). Terminals have degree zero. At most n choices of earlier k are needed per state, and memoization by (u,k) shares every suffix result. No pair of extension-depth histories is stored, and (6) uses only earlier-variable/suffix-state entries.

**The corrected product recurrence.** Fix one extension definition and its two signed operand diagrams U,V. For every same-level state pair (u,v) reachable in their synchronous product, or conservatively for every same-level pair, define the ordered product representative P_(u,v) and witness W_(u,v). Terminal values are field elements, and there set

P_(u,v)=r_u r_v in F₂,                   W_(u,v)=0.               (7)

At a nonterminal level k write e_a=e_(k,a), u_a=r_(successor_a(u)), v_a=r_(successor_a(v)). This notation denotes actual x-only child roots, including the sign convention. Put

P_(u,v)=e_0 P_(u_0,v_0)+e_1 P_(u_1,v_1),

W_(u,v)=(e_0 K_(u_0,k)+e_1 K_(u_1,k))(v_0+v_1)
          +b_(y_k)(u_0+u_1)(v_0+v_1)
          +e_0 W_(u_0,v_0)+e_1 W_(u_1,v_1).                     (8)

Here b_(y_k) is the original Boolean placeholder for that variable. Every product remains in its displayed order. In particular the Boolean placeholder stays to the left of the two suffix sums. Only two same-level successor pairs are needed per recurrence; no width product over all extension definitions is taken.

We prove the exact invariants

W_(u,v)(x,0)=0,           W_(u,v)(x,A)=r_u r_v+P_(u,v).            (9)

The terminal case is (7). For the induction, abbreviate beta=y_k²+y_k and let K values after substitution be u_a y_k+y_k u_a. Since e_b is either y_k or 1+y_k, the identity

u_a e_b=e_b u_a+K_(u_a,k)(A)

holds for both b. Expanding the product of the two representatives, with a,b ranging independently over 0,1, gives

r_u r_v = sum_(a,b) e_a u_a e_b v_b
        = sum_(a,b) e_a e_b u_a v_b
          +(e_0 K_(u_0,k)(A)+e_1 K_(u_1,k)(A))(v_0+v_1).         (10)

For each of the four ordered choices a,b, direct multiplication of 1+y_k and y_k gives the formal identity

e_a e_b = delta_(a,b) e_a+beta.                                  (11)

This uses no Boolean quotient and does not move beta across a suffix. Consequently the first sum in (10) equals

e_0 u_0 v_0+e_1 u_1 v_1+beta(u_0+u_1)(v_0+v_1).                 (12)

Substituting the two child instances of (9) into the last two terms of (8), and combining (10)–(12), proves the second identity in (9). The child product terms cancel in characteristic two, leaving r_u r_v+P_(u,v). The first identity follows independently by induction from (8): every summand contains either K, a Boolean placeholder or W. This also proves that every surviving monomial contains exactly one original placeholder. No quotient identity, nonlinear correction sector or path expansion is suppressed.

If there are s>=1 remaining levels, the first correction term in (8) has syntactic degree at most 1+(s-1)+(s-1)=2s-1 by the bound for K. The Boolean correction has degree at most 1+2(s-1)=2s-1. For s=1 the two inherited W terms have degree at most one, since the children are zero constants; for s>=2 their degree is at most 1+(2(s-1)-1)=2s-2. Thus W has syntactic degree at most 2s-1. The terminal case n=0 needs only W=0; using h>=1 in (2) covers it. P is an ordered multilinear representative of degree at most s by its recurrence. Every suffix and relation bound is independent of extension depth.

**Identifying the supplied output.** The synchronous pair representative P at the operand roots computes the pointwise AND of their Boolean functions, by (7)–(8). By the hypothesis on the output diagram, it agrees with that output's representative r_i on all Boolean assignments. Both belong to the increasing multilinear subspace for the same common order, so the injectivity argument following (4) gives P=r_i formally in the free ring. The operand-root representatives equal the prescribed signed roots r_a,r_b formally as already proved. Therefore setting H_i to the corresponding W root gives exactly (1). No witness identifying arbitrary Boolean-equivalent free polynomials is assumed; the ordered multilinear restriction is essential here.

Coincident successors do not change any step: (10) sums all four terms before cancellation, (11) holds in every case, and memoization can simply reuse an identical child pair. Repeated operands, complementary operands and constant roots satisfy the same identities. With n=0 all functions and products are constants, the promised agreement is a scalar equality, and every H_i is zero. These cover the degeneracies without introducing extra axioms.

**All data and complete costs.** Topologically list constants, original variables, every extension and all required exact signed nodes to form L025's abstract DAG. There are O(T+n+2)=O(B) nodes. At a reduced AND node, reference the independently supplied output representative, its signed operand nodes and the newly constructed H_i. The arithmetic gates inside representatives are not abstract nodes. This gives the required acyclic associations, with S and degree bounds (2).

All O(B) positive/signed/base diagrams have O(B(n+1)v) states including terminals and roots, and their representative circuits use that many gates up to an absolute factor. The earlier-variable/suffix table (6) has at most O(B(n+1)²v) entries, with constant gates per entry. Each of at most T extension definitions has at most O((n+1)v²) paired states, including terminals. Recurrences (7)–(8) use a constant number of gates per pair beyond shared child, representative and K roots. This allowance includes the entire P network even though P is not required as a supplied data output. The original Boolean/commutator placeholder nodes and other constant/root framing contribute O(n²+B) more. The total is O(M). The construction is bottom-up in suffix level within each independent definition; an earlier extension's entire product network is never multiplied into a later state space.

There are O(B) supplied representative and H roots. To avoid assuming free sharing between separately written outputs, write each root as its reachable sub-DAG, charging at most O(M) nodes each. Dense arithmetic references need O(log(M+2)) bits. Original variable/definition identifiers and associations cost at most O(T) bits per occurrence; coefficients in F₂ cost constant bits. Densely renumbering each output is polynomial-time and preserves sharing within it. The original axiom list has O(T²) constant-width entries and O(T³) full bits, as in L020/L025. These estimates give (3), including all separate roots and the source associations needed by L025.

The supplied diagrams use O(B(n+1)v) records, each with a constant number of dense successor references, terminal data and at most T bits for restored original labels, plus the common variable-order list. Their encoding is also covered by (3). There are no sparse uncharged state identifiers, implicit diagrams, free sharing across files or unfolded paths. Scanning the input, building all tables, writing the rooted data and restoring labels take polynomial time in T,n,w. The construction uses the semantic diagram promise only to justify root equality; it need not decide a general promise or general circuit identity.

Applying L025 with these S,d,h,E is now legitimate. L025 supplies the direct reduced clause invariant and full certificate propagation; it is not a source for the missing local identities proved here. L023's stopped exact-lift mechanism is avoided: no witness compares r_i with an unreduced high-degree extension polynomial. This constructs only relations among separately supplied ordered representatives.

**Source comparison and finite verification.** The ready assessment is `drafts/literature/2026-10-05-obdd-reduced-data.md`. Bryant's fixed-order Boolean product/equivalence algorithms are supporting known results, not a free-ring correction theorem. Forbes–Shpilka–Tzameret–Wigderson's commutative correction theorem likewise does not authorize the factor moves in (10). L020 imports the ordered commutator identities; the new work here is their suffix specialization together with (8), the ordered-output bridge and the full size/degree bounds. No known OBDD algorithm or general multilinearization theorem is reproved as a purported discovery.

Run `PYTHONDONTWRITEBYTECODE=1 python3 scripts/obdd-reduced-data/check_suffix_witness.py`. It independently expands noncommutative words, using no Boolean quotient simplification. The generic local identity (8) is tested with free child-value symbols, explicit commutator/Boolean substitutions and independent child-product representative symbols. The 308 diagram tests include every pair of Boolean functions on n=0,1,2 variables, plus signed cases through n=3, reversed common orders, constants and both merged and duplicate-state diagrams. All substituted H identities, zero identities, exact complements, ordered-output equalities and 3,960 suffix commutator checks pass. The maximum tested syntactic degrees are 3 for values and 5 for H, within the respective max(1,n) and max(1,2n-1) bounds. Root mutations omitting the commutator term, omitting the Boolean term and reversing the commutator coefficient order are detected in 164, 172 and 112 cases respectively.

The complete finite circuits, diagrams, axioms and relevant expanded polynomials are in `scripts/obdd-reduced-data/suffix-witness-results.json`. Its tests are diagnostics; the all-size identities, degree estimates and complete encoding bound are established by the preceding inductions/counts. No ER proof strings or arbitrary-width existence claim were tested. The separate critical audit recorded in `drafts/2026-10-05-obdd-reduced-data-critical-audit.md` checked the full inductions, signed/base and terminal cases, pre-substitution degrees, independent per-definition state counts and separately written root encodings against L025. It found no load-bearing defect and reproduced the diagnostic results. This is informal verification of the existing restricted statement, not a strengthened theorem or a main-problem candidate.

## Mathlib

Coverage: **not checked** for the full reduced-data construction, ordered free-ring bridge or complete encoding bound. No matching Mathlib theorem or absence claim is asserted.

The inspected primary supporting sources are Randal E. Bryant, [*Graph-Based Algorithms for Boolean Function Manipulation*, IEEE Transactions on Computers 35(8), 677–691 (1986), Theorem 1 and §§4.2–4.3, author-restored pp. 5–6 and 10–14](https://www.cs.cmu.edu/~bryant/pubdir/ieeetc86.pdf); Michael A. Forbes, Amir Shpilka, Iddo Tzameret and Avi Wigderson, [*Proof Complexity Lower Bounds from Algebraic Circuit Complexity*, Theory of Computing 17(10), 2021, Propositions 4.5–4.6, pp. 30–32](https://toc.cs.uchicago.edu/articles/v017a010/v017a010.pdf); and Fu Li, Iddo Tzameret and Zhengyu Wang, [*Characterizing Propositional Proofs as Non-Commutative Formulas*, arXiv:1412.8746v4, 11 September 2015, Lemmas 3.6–3.7, pp. 17–18](https://arxiv.org/pdf/1412.8746v4). Their supporting scope and the missing full-statement match are recorded in the unchanged prior assessment. L020's shared implementation is used explicitly in (6), and L025 only for the concluding propagation application. The record is POTENTIALLY_NEW under that EXPLORE coverage, meaning that no inspected full match was established, not certified novelty.
