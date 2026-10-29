# L113 — Raw simulations obstruct even commuting unary products

## Hypotheses

Work over F₂. The normalized operands F,G are finite explicit acyclic
graphs with singleton edge labels scalar one or the single original letter
x, with the path and root conventions of L035. The allowed family includes
constants, parallel occurrences, cancellation, empty paths, unequal path
lengths, disconnected graphs and arbitrary designated roots. No restriction
to any particular fixed job's operands is asserted here.

Let A=Prod(F,G) and B=Prod(G,F) be independently built by the exact L110
§21 recipe: two fresh roots, two disjoint complete operand copies, and
three scalar-one connectors in serial order. Their initial rows eta and
final columns theta are the units at the fresh source and sink. Write E_0
for the scalar-one adjacency and E_x for the x adjacency, with entries
equal to the parity of edge occurrences. Set g(H)=number of vertices plus
edges plus singleton-label entries, before constant closure; the fixed
denominator is S=g(A)+g(B).

The tested **raw-first** proposal requires each arrow U -> V in a finite
zigzag to have a scalar matrix X, with rows indexed by U and columns by V,
satisfying all four equations

    eta_U X = eta_V,           theta_U = X theta_V,
    E_(U,0) X = X E_(V,0),     E_(U,x) X = X E_(V,x).       (1)

Intermediates may have arbitrary finite dimensions and boundary vectors.
The obstruction below does not need them to be acyclic, functional
quotients, sparse, or graphs. Extra unused original letters would impose
additional equations and do not weaken (1).

For comparison, the actual right-closed equations for an acyclic U -> V
are only

    alpha_U X = alpha_V,       beta_U = X beta_V,
    M_(U,x) X = X M_(V,x),                                  (2)

where K_H=sum_(j=0)^(n_H-1) E_(H,0)^j, alpha_H=eta_H K_H,
M_(H,x)=E_(H,x)K_H and beta_H=theta_H, exactly as in L110 §4.
There is no separate constant-letter equation in (2).

## Conclusion

The permitted pair consisting of a one-edge x graph F and a one-edge
scalar-one graph G has S=32. There is **no finite zigzag satisfying (1)**
between its independent products A,B, irrespective of support or size.
Nevertheless both right-closed representations recognize precisely x.

The same raw obstruction occurs with constant-free operands: for simple
paths F=x^r and G=x^s, r,s>=1 and r!=s, no such raw zigzag exists, while
both right-closed products recognize x^(r+s). Thus merely excluding
constant edges inside operands does not repair this raw-first proposal;
the required product connectors remain relevant.

This rejects a universal raw-first quotient or raw-first simulation chain,
before any proposed bound C*S is considered. It does **not** reject chains
satisfying only (2), provide a lower bound for those chains, or establish
the desired linear support/intermediate-graph ledger. It changes a local
certificate strategy, not P versus NP. The concrete obstruction is a
REPRODUCTION/application of known simulation soundness, not a claim of a
new equivalence theorem or certified originality.

## Proof

### 1. Source import and the preserved quantity

Reuse the pre-invocation EXPLORE assessment
`drafts/literature/2026-10-26-unary-product-sparse-quotient.md` and its
inspected source: Ésik–Maletti, *Simulation vs. Equivalence*,
[2010 author manuscript, Definition 3.1 and soundness, p.2](https://www.informatik.uni-leipzig.de/~maletti/pub/esimal10.pdf).
Every scalar simulation in its stated orientation preserves the recognized
series. F₂ is an allowed semiring; finite dimensions and arbitrary boundary
vectors are allowed. No positivity, determinism, acyclicity or
characteristic-zero assumption is needed for this soundness assertion.
The qualitative existence theorem is not used to infer any size bound.

Apply soundness to the auxiliary alphabet {c,x}, interpreting E_0 as the
transition matrix for c and E_x as the transition matrix for x. This is
legitimate because (1) is precisely the source's two-letter simulation
condition. The auxiliary c only records the positions of scalar edges for
testing (1); it is **not** an original letter, an alteration of the input
dictionary, or a claim that scalar one is noncentral in the target algebra.
Consequently every arrow preserves, for each word w in {c,x}*, the scalar
eta_H E_(H,w) theta_H. Equality of this scalar is symmetric, so it is also
preserved by a zigzag with any orientations. We import soundness rather
than reprove the general theorem.

### 2. An exact six-state counterexample

Give each operand vertices 0,1 and its indicated single edge 0 -> 1.
For each product use the literal recipe numbering: fresh source 0 and sink
1, first operand copy 2,3 and second copy 4,5. The complete edge lists are

    A: (0,2,1), (2,3,x), (3,4,1), (4,5,1), (5,1,1),
    B: (0,2,1), (2,3,1), (3,4,1), (4,5,x), (5,1,1).       (3)

They are acyclic in order 0,2,3,4,5,1. All copies, roots and connectors
are present, with no padding, deletion or semantic replacement. Each has
6 vertices, 5 edges and 5 singleton entries, so g(A)=g(B)=16 and S=32.

Write Q_ij for a 6-by-6 matrix unit and e_i for a unit row. Then eta=e_0,
theta=e_1^T, and the complete nonzero adjacency entries are

    E_A0 = Q_02+Q_34+Q_45+Q_51,       E_Ax = Q_23,
    E_B0 = Q_02+Q_23+Q_34+Q_51,       E_Bx = Q_45.          (4)

For the diagnostic word w=c x c c c, successive rows on A are

    e_0 -> e_2 -> e_3 -> e_4 -> e_5 -> e_1.

On B they are e_0 -> e_2 -> 0 -> 0 -> 0 -> 0, since row 2 of
E_Bx is zero. Thus the exact necessary equality fails:

    eta_A E_A0 E_Ax E_A0^3 theta_A = 1,
    eta_B E_B0 E_Bx E_B0^3 theta_B = 0.                    (5)

By §1 this rules out any zigzag of (1), including one through a common
quotient or arbitrary scalar representations. It is stronger than a
failure of a particular guessed matrix, but only for the raw contract.
An arrow or intermediate violating (1) cannot be silently included in
such a chain.

### 3. The right-closed obligations remain different

From the full matrices (4), the finite closures give

    alpha_A = e_0+e_2,          alpha_B = e_0+e_2+e_3+e_4,
    beta_A = beta_B = e_1^T,
    M_Ax = Q_23+Q_24+Q_25+Q_21,
    M_Bx = Q_45+Q_41.                                     (6)

For example, the only x edge of A ends at 3, whose constant-reachable
vertices are 3,4,5,1; the only x edge of B ends at 5, whose
constant-reachable vertices are 5,1. The initial rows include all
constant paths from source 0. These enumerate every nonzero term in (6),
including the identity terms of K, without any infinite closure.

Both empty-word coefficients alpha beta are zero. Also

    alpha_A M_Ax = e_3+e_4+e_5+e_1,
    alpha_B M_Bx = e_5+e_1,

so both x coefficients are one. Each M_x squared is the zero matrix:
M_Ax has only row 2 nonzero and no nonzero column-2 entry; M_Bx has
only row 4 nonzero and no nonzero column-4 entry. Every higher coefficient
is therefore zero. This checks all words in the original unary alphabet,
not just a finite prefix standing in for an unbounded assertion. By
L110 §4's finite right-closure semantics, both products are exactly x.

L111 §§4,7 already proves that a raw intertwiner between acyclic graphs
survives right closure; no converse was asserted there. Here (5) precludes
the raw chain although the closed series agree. We neither infer a
closed scalar map from this equality nor present the dense notation K
as an uncharged sparse occurrence graph. The two products and their
denominator remain exactly (3).

### 4. Constant-free operands and precise stopping scope

For simple operand paths of lengths r,s>=1, every product has exactly
one accepting path. Marking its three connectors by c gives respectively

    c x^r c x^s c,                c x^s c x^r c.            (7)

If r!=s, the positions of the second c differ. The coefficient of the
first word is one in A and zero in B. Section 1 again rules out (1).
The actual scalar connectors erase these marks in the original algebra,
and each product's polynomial is x^(r+s), as also follows from L110's
ordered composition semantics. No commutation of distinct original
letters is used. Each product has r+s+4 vertices, r+s+3 edges and the
same number of singleton entries, so S=6(r+s)+20. For r=1,s=2 it is 38.
There is no growth threshold to compare: the raw equations are already
inconsistent, for every proposed universal C.

A counterexample within the allowed family suffices to refute its
universal raw-first claim; no omitted case involving cancellations,
coincident roots or disconnected graphs can restore that claim. Those
cases remain mandatory for any future positive closed-only construction.
This obstruction does not depend on the cut table rejected by L112,
and it does not invalidate L111's checked copy-ancestry maps. It receives
no fixed-job bytes or occurrences and changes no previous cap, format or
production recipe. Mixed-letter Dcomm, closed-only quantitative bounds,
full reception/work/live costs, certificate availability and unrestricted
ER/Frege/SAT conclusions all remain unresolved.

## Mathlib

Full matching coverage for this raw/closed product obstruction and the
quantitative continuation is **not checked**. No absence claim is made.
The external input used is the precise simulation-soundness citation
above; the finite graph recipe, closure conventions and their local
qualifications are L035, L110 and L111. Equations (3)–(7) supply the
complete specialization and verification here, without a numerical
experiment, path-enumeration algorithm or new general soundness proof.
