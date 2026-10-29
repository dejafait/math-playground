# L125 — Balanced Pascal-product residual bases: valid graphs, superlinear support

## Hypotheses

Work over F₂ with L110 §4's right closure and scalar arrows. Keep the
entire original endpoints A=Prod(F_N,G_N), B=Prod(G_N,F_N) of L122 §2,
where N=2^k, k>=0, F_N has parallel 1/x layers and G_N is the N-edge
x path. Both stored coordinate orders are

    s,f0,...,fN,h0,...,hN,t.

All original coordinates, including output-dead vertices, are retained.
Write R_J(z)=sum_(ell>=0) z^ell M_J^ell beta_J and

    E_N={(u,v):u R_A=v R_B}.

Scalar support counts expanded nonzero entries; occurrence size is
g(J)=|V(J)|+2|E(J)|, including parallel occurrences. Thus S=16N+20.
An arrow X:U->V means alpha_U X=alpha_V, M_U X=X M_V and
X beta_V=beta_U. No polynomial-labelled edge, compressed XOR program or
uncharged closure oracle is allowed.

The construction below chooses **one specified balanced product basis**.
It does not restrict the arbitrary bases quantified in the larger target.

## Conclusion

For every k the construction gives a full basis of E_N of dimension
2N+7. Its induced shift has an acyclic adjacency, and the explicit
singleton 1/x graph below receives both original accepting boundaries.
Its total basis support, also the combined support of its two realized
endpoint maps, is

    W_k=8+H_k,
    H_0=5, H_1=12, H_(k+2)=2H_(k+1)+H_k.                (1)

In particular W_k/S is unbounded: it grows on the scale
((1+sqrt(2))/2)^k. This rejects a uniformly linear support bound for
this balanced Pascal-product extension, even though every algebraic
equation and the literal realization are valid. It does not reject
every basis, every common source, or arbitrary scalar chains.

At N=4 the basis is exactly L124's basis, up to row order. At N=8 the
full 23-row basis has support 78, shift support 41, initial support 5
and final support 1. Its graph has 25 vertices and 47 occurrences,
g(Q)=119, with map supports 53 and 25; S=148. Exhaustive finite
enumeration proves that 78 is the minimum support of any basis of E_8.
No minimum-occurrence claim or all-N optimality follows from that finite
enumeration. In particular, this result does not resolve the unary
fourth comparison, the independent reception/resource gaps, or P versus NP.

## Proof

### 1. Known input and the exact scope of this attempt

Reuse the unchanged ready EXPLORE assessment
`drafts/literature/2026-10-28-residual-relation-generators.md`.
Qualitative common-source existence and the scalar simulation convention
are known: Ésik–Maletti, *Simulation vs. Equivalence*, 2010 author
manuscript, Definition 3.1 and Theorem 4.2, pp.2–3
([primary manuscript](https://www.informatik.uni-leipzig.de/~maletti/pub/esimal10.pdf)).
F₂ is an allowed semiring and its arbitrary finite boundary vectors
include these right-closed representations. That theorem neither chooses
the full original-coordinate relation basis used here nor gives the
expanded-support/occurrence bound sought. We import its convention and
qualitative comparison, not a quantitative conclusion or a new existence
theorem. The specialization here is necessary to test the explicit
dyadic basis and its exact support recurrence. L124's graph realization
calculation is reused with the verified hypotheses below.

L122/L123 and Attempts 056/057 are earlier restrictions on other lifts;
their support obstructions are not premises about the present basis.
No uninspected circuit lower bound, cancellation-free restriction or
cross-notebook input is assumed. The classification POTENTIALLY_NEW
does not certify originality beyond the documented comparison.

### 2. Full residual relation in original coordinates

Put y=1+z. L122 §2's complete closed transition rows give

    R_A(f_i)=z^(N+1)y^(N-1-i), R_A(h_i)=z^(N-i),
    R_B(f_i)=z y^(N-1-i),      R_B(h_i)=z^(N-i)y^N,
                                                        (0<=i<N). (2)

In both endpoints s,f_N,h_N have residual zero, and t has residual one.
For completeness, these formulas follow from the finite recursion
R=beta+zMR. The f rows use
`1+z sum_(j=0)^(m-1) y^j=y^m`; the h rows then follow along their
path, retaining the last constant connector in M. In characteristic two,
successive squaring gives y^N=1+z^N. These observations check the dyadic
specialization of all residuals, not just the accepted polynomial.

A's 2N+1 nonzero residuals have distinct degrees 0,...,2N. They are
monic, hence linearly independent and span all polynomials of degree at
most 2N. Every residual of B also has degree at most 2N. Consequently
the map (u,v)->uR_A+vR_B has rank 2N+1, and

    dim(E_N)=2(2N+4)-(2N+1)=2N+7.                         (3)

Here is also a useful exact core description, with no quotient of the
endpoints. Let P_N have row j the coefficients of (1+z)^j, in increasing
degree order, 0<=j<N. Translation by 1 twice is the identity over F₂,
so P_N^2=I. Relabel the nonzero f/h blocks in reverse order. If r,b are
the A_f and B_f coefficient rows, equality of high and low degrees in
(2) gives all core rows, respectively,

    (A_f,A_h; B_f,B_h)=(r,(b+r)P_N; b,rP_N).             (4)

The remaining direct factors are six independent original-coordinate
unit rows and the paired t row. This is a description of the full
relation, not merely its reachable subspace. Equation (4) supplies no
sparsity theorem for arbitrary parameters r,b.

### 3. Balanced factors and the full basis

For an index j<N let w be its binary popcount, and list its set bits
in increasing order. In the low family choose a to be the sum of the
first floor(w/2) such bits; in the high family choose the first
min(w,floor(w/2)+1) bits. In either family put b=j-a. Thus a&b=0.
Define, separately for the two choices,

    q_j(z)=z^a(1+z)^b,
    q_j^z = its coefficient row in powers of z,
    q_j^y = its coefficient row in powers of y=1+z.

Both coordinate polynomials have degree j and leading coefficient one:
in y coordinates q_j=(1+y)^a y^b. For a coefficient row p=(p_0,...,p_(N-1))
write f(p)=sum_j p_j e_(f_(N-1-j)) and likewise h(p). Define

    L_j=(h(q_j^z),                 f(q_j^y)),
    H_j=(f(q_j^y)+h(q_j^z),        h(q_j^z)),              (5)

where L uses the low split and H the high split. Add the six unit rows
Z_As,Z_Af,Z_Ah,Z_Bs,Z_Bf,Z_Bh on s,f_N,h_N in their respective endpoint,
and F=(e_t,e_t). These are all 2N+7 rows of the proposed basis.

The common residual of L_j is z q_j and that of H_j is
z q_j(1+z^N), by (2); hence every row belongs to E_N. The 2N core
residuals have distinct leading degrees 1,...,2N, so they are
independent. Together with F they form a basis of the residual polynomial
space. The six Z rows are independent on disjoint zero-residual
coordinates. Therefore all rows in (5), F and the Z rows are independent;
(3) proves that they span the entire relation. The low tie choice makes
the N=4 row set agree exactly with L124's table.

### 4. Shift, boundaries and a literal graph for every k

Let X_A,X_B be the two blocks of this basis. The relation is invariant
under (u,v)->(uM_A,vM_B): subtract the equal constant coefficients in
uR_A=vR_B, then use R=beta+zMR and divide by z. Thus there is a unique
matrix T satisfying

    T X_A=X_A M_A, T X_B=X_B M_B.                        (6)

All six Z rows and F have shift zero, because the corresponding endpoint
transition rows vanish. Every other basis row has final value zero; its
shifted common residual is its original common residual divided by z.
In the degree-triangular residual basis, a polynomial of degree at most
d-1 has zero coordinates on every row of leading degree >=d: descending
elimination of distinct monic leading terms proves this assertion.
It follows that any shift edge from a core row goes either to a smaller
residual degree or to a Z row. Therefore the literal adjacency of T is
acyclic in the order

    H_(N-1),...,H_0,L_(N-1),...,L_0, all Z rows, F.      (7)

This is a proof of acyclicity in the specified coordinates, not an
inference from nilpotence alone. No linear bound on the number of entries
of T is asserted here; the trivial degree-order bound is quadratic.

Expand z^(N-1) uniquely as sum_j eta_j q_j in the high polynomial basis.
Summing eta_j H_j gives B's h0 and A's h0+sum_(i=0)^(N-1) f_i:
in y coordinates z^(N-1)=(1+y)^(N-1), whose N coefficients are all one.
Thus the full initial coordinate row is

    c=Z_As+Z_Af+Z_Bs+sum_j eta_j H_j,
    cX_A=alpha_A, cX_B=alpha_B.                         (8)

The final functional is d=e_F^T, since only F uses a t coordinate;
X_A beta_A=X_B beta_B=d and cd=0. In particular no boundary coordinate
has been discarded. The initial support is at most N+3.

Construct Q with fresh source/sink s_Q,t_Q and one vertex q_i for each
basis row. For each T_ij=1 put one x occurrence q_i->q_j. For each
c_i=1 put one constant occurrence s_Q->q_i, and put the one constant
q_F->t_Q. There are no other occurrences. Order the graph by (7), with
s_Q first and t_Q last, proving literal acyclicity. Every edge label is
one singleton 1 or x.

The complete arrow rows for J=A,B are

    Y_J(s_Q)=0, Y_J(q_i)=X_J(i)+d_i e_(t_J),
    Y_J(t_Q)=e_(t_J).                                  (9)

The hypotheses of L124 §4's right-closure realization computation all
hold: cd=0, e_(t_J)M_J=0, (6), (8), and the common final equation.
Explicitly alpha_Q=e_(s_Q)+sum_i c_i e_(q_i), and a q_i closed transition
is sum_j T_ij e_(q_j)+(Td)_i e_(t_Q). Applying (9) cancels the two
copies of (Td)_i e_(t_J), leaving X_J(i)M_J=Y_J(q_i)M_J.
The initial products are (8); every internal final product is d_i+d_i=0,
and the new sink's final product is one. The source/sink transition
products are zero. These verify all three arrow equations.

The paired Q rows replace F by the fresh sink row F, leaving all other
basis rows present. Hence their span is still the full E_N. Removing
F's two internal entries and adding the two new sink entries preserves
the combined map support exactly. This realization needs no uncounted
auxiliary maps. Its occurrence count is |supp(T)|+|supp(c)|+1.

### 5. Exact support recurrence and its failure of the linear threshold

For any nonnegative integer m, repeated squaring gives

    (1+z)^m=product_(ell:bit_ell(m)=1) (1+z^(2^ell)).

Different subsets give different exponents, so its coefficient support
has exactly 2^popcount(m) entries. This elementary identity establishes
the exact scalar count here; no cancellation-free circuit bound is used.
The shifts by z^a and y^b do not change these counts. If w=2m or 2m+1,
the row weights from (5) are respectively

    w=2m:   wt(L_j)=2^(m+1), wt(H_j)=3*2^m;
    w=2m+1: wt(L_j)=3*2^m,   wt(H_j)=4*2^m.             (10)

For w=0 the high split has a=b=0 and the same formula gives 3.
The two endpoint blocks and the f/h subblocks are disjoint, so all
these sums count expanded nonzero entries without any hidden cancellation.
Let f_(2m)=5*2^m and f_(2m+1)=7*2^m. Exactly binom(k,w) indices have
popcount w. The six unit rows and F cost eight, hence

    H_k=sum_(w=0)^k binom(k,w) f_w, W_k=8+H_k.           (11)

Since f_(w+2)=2f_w, Pascal's identity applied twice yields

    H_(k+2)=sum_w binom(k,w)(f_w+2f_(w+1)+f_(w+2))
            =2H_(k+1)+H_k.

The initial values are 5 and 12, proving (1). Furthermore
f_w>=(7/sqrt(2))*(sqrt(2))^w for either parity, so

    W_k/S >= [7/(36sqrt(2))]*[(1+sqrt(2))/2]^k,          (12)

using S=16*2^k+20<=36*2^k. The base on the right is strictly greater
than one. Therefore no constant C bounds this construction's expanded
support by C*S for all k. It fails before any possible charge for
shift entries, graph occurrences, wire indices, work or live memory
could help it. An economical recursive description of (5) does not
change (11). This is a stop for this construction only.

### 6. Complete N=8 specialization and finite minimum

Write Z=Z_Ah+Z_Bf+F and
U=Z_Af+Z_Ah+Z_Bf+Z_Bh+F in the shift column below; these abbreviations
stand for the displayed independent rows, with no cancellations omitted.
The six Z rows are the unit rows already specified and shift to zero;
F=(t,t) also shifts to zero. The remaining sixteen rows and every
shift entry are:

| Row | A block | B block | Shift |
|---|---|---|---|
| L0 | h7 | f7 | Z |
| L1 | h6,h7 | f6 | Z+L0 |
| L2 | h5,h7 | f5 | Z+L0+L1 |
| L3 | h4,h6 | f4,f5 | L2 |
| L4 | h3,h7 | f3 | Z+L0+L1+L3 |
| L5 | h2,h6 | f2,f3 | L4 |
| L6 | h1,h5 | f1,f3 | L5 |
| L7 | h0,h2,h4,h6 | f0,f1 | L4+L6 |
| H0 | f7,h7 | h7 | U+L0+L1+L3+L5+L7 |
| H1 | f6,f7,h6 | h6 | H0 |
| H2 | f5,f7,h5 | h5 | H1 |
| H3 | f4,f5,f6,f7,h4 | h4 | H2 |
| H4 | f3,f7,h3 | h3 | H3 |
| H5 | f2,f3,f6,f7,h2 | h2 | H4 |
| H6 | f1,f3,f5,f7,h1 | h1 | H5 |
| H7 | f0,f1,f2,f3,h0,h4 | h0,h4 | H2+H6 |

Here c=Z_As+Z_Af+Z_Bs+H3+H7 and d=e_F^T. Thus the graph has 41
x occurrences, five initial constants and one final constant; its
25 vertices give g(Q)=25+2*47=119. The two maps (9) have support 53
and 25, with sum 78. If X_A,X_B,T,c,d and both realized maps are all
stored separately, their scalar entries total 78+41+5+1+78=203;
this is not a wire/work/live bound. The two-arrow graph charge is
2g(Q)=238. The required uniform threshold is still O(S), and (12)
disproves that threshold for this construction despite these finite counts.

Here is the exhaustive finite optimality test, including its scope.
Let C_8 be the 16-dimensional core generated by the L/H rows. Enumerate
every mask 0<=m<65536 and form the XOR of the indicated rows. Independence
proved above makes this enumeration bijective. Group all vectors by
their expanded weight, and insert every vector into binary elimination
pivots in increasing-weight order. If r_w denotes the rank of the span
of ALL vectors of weight at most w, the complete result is

    w:   0 1 2 3  4  5  6  7  8,...,32
    r_w: 0 0 1 5 11 11 15 15 16,...,16.                (13)

Elimination replaces a row by XORs with rows already in the span;
it adds a pivot exactly when the row is outside that span. Induction
over every inserted vector proves these are the threshold ranks, not
the ranks of a sample. The audit retains all 65536 vectors, the chosen
pivots' basis rows and the full threshold sequence. Only integer bit
operations are used; the executable procedure is reproducible below.

For any core basis at most r_w of its elements can have weight <=w.
Summing the identity wt(v)=sum_(w=0)^31 [wt(v)>w] gives total support
at least sum_(w=0)^31 (16-r_w)=70. The displayed core basis attains 70.
To pass from the core to the full relation, use its disjoint-coordinate
direct factors: six unit directions and the paired t direction. A
weight-<=w full vector projects to weight-<=w vectors in every factor;
conversely every low-weight pure factor vector is a full relation vector.
Hence the full threshold-span ranks are

    r_w+6*[w>=1]+[w>=2].                               (14)

The same rank-sum lower bound adds 6+2 to 70, and the displayed full
basis attains 78. This proves finite minimum support without assuming
any basis has the special product form (5). It does not prove (13)'s
analogue for any other N, and proves no shift/occurrence optimum.

### 7. Complete artifacts, replay and qualifications

The certificate `scripts/batched-incidence/output-543-matched/residual-dyadic.json`
contains the complete original graphs/closures/residuals, every basis row,
every shift product, both boundary products, the literal Q graphs and
all realized arrow entries for N=1,2,4,8. Its companion `audit.json`
reconstructs endpoints and constant closures independently of the new
constructor, checks every equation and graph occurrence, and retains the
full N=8 enumeration supporting (13). All finite checks pass; the
uniform linear requirement fails by the symbolic proof (12).

```bash
python3 scripts/batched-incidence/check_residual_dyadic.py \
  --output /tmp/p-vs-np-residual-dyadic-543 --max-k 3
python3 scripts/batched-incidence/audit_residual_dyadic.py \
  /tmp/p-vs-np-residual-dyadic-543/residual-dyadic.json \
  --output /tmp/p-vs-np-residual-dyadic-543/audit.json --enumerate-core
```

The preserved earlier `scripts/batched-incidence/output-543/residual-dyadic.json`
uses the opposite low-family odd-popcount tie. It also has basis support
78 at N=8, with shift 29 and 35 occurrences, but does not reproduce
L124's N=4 rows. It is not the input to the final audit or table above;
the final matched construction is fixed by §3. The exploratory variant
does not change (10)–(12), and no claim of optimal shift is made.

The proof uses original-coordinate residuals, true full-relation rank,
explicit shift acyclicity and both boundary equations. It does not infer
linear size from finite success, replace expanded maps by programs, or
convert a failed construction into a lower bound on all certificates.
General operands, mixed letters, actual reception, total resource bounds,
certificate availability and unrestricted P versus NP remain unresolved.

## Mathlib

Full matching quantitative coverage was not checked. Supporting binary
linear algebra, polynomial translation and finite DAG operations are not
an imported theorem for this basis, its support recurrence or the finite
threshold ranks. No Mathlib theorem is used to certify these calculations;
unknown coverage is not evidence of absence.
