# L124 — Full N=4 residual relation: minimum-support basis and direct DAG realization

## Hypotheses

Work over F₂. Use L110 §4's right closure and scalar-arrow equations,
and L122's original independent endpoints A=Prod(F₄,G₄),
B=Prod(G₄,F₄), including all fresh roots, constant connectors and
zero-residual coordinates. Both stored coordinate orders are

    s,f0,f1,f2,f3,f4,h0,h1,h2,h3,h4,t.

The topological order of B instead puts its h block before its f block.
F₄ has parallel 1/x edges at each of its four layers; G₄ is the four-edge
x path. No coordinate quotient or endpoint replacement is permitted.
Write R_J(z)=Σ_(ell>=0) M_J^ell beta_J z^ell. Let

    E₄={(u,v) in F₂^12 × F₂^12 : u R_A=v R_B}.

Scalar support means the number of expanded nonzero entries. Occurrence
size is g(J)=|V(J)|+2|E(J)|, including parallel occurrences. In particular
S=g(A)+g(B)=84. A scalar arrow X:U->V obeys

    alpha_U X=alpha_V, M_U X=X M_V, X beta_V=beta_U.

## Conclusion

E₄ has dimension 15. The basis below has total scalar support 37, the
minimum among all bases of this finite E₄. In these coordinates its
induced shift (u,v)->(uM_A,vM_B) has 24 nonzero entries and an acyclic
literal digraph. Both initial boundaries and the common final functional
are received exactly. An explicit singleton 1/x graph Q has 17 vertices,
29 occurrences and g(Q)=75; the scalar arrows A<-Q->B have respective
supports 24 and 13. Their paired row images span the whole E₄, including
the six independent zero-residual directions and the final direction.

This is a finite discriminant. It establishes neither a uniform O(N)
bound, a recursive construction for N=2^k, an optimal occurrence bound,
nor an obstruction to other bases or realizations. It does not resolve
the unary fourth comparison, general operands, actual reception, total
resource bounds, certificate availability or P versus NP.

## Proof

### 1. Source scope, exact residuals and full dimension

Qualitative common-source existence is already known: Ésik–Maletti,
*Simulation vs. Equivalence*, 2010 author manuscript, Definition 3.1 and
Theorem 4.2, pp.2–3
([primary manuscript](https://www.informatik.uni-leipzig.de/~maletti/pub/esimal10.pdf)).
The ready assessment `drafts/literature/2026-10-28-residual-relation-generators.md`
distinguishes that result from a full-relation basis with joint expanded
support/shift/occurrence/boundary costs. We do not reprove the general
theorem or claim novelty for qualitative existence. This calculation is
needed for the specific original-coordinate finite data not supplied by
that source. L122/L123's restricted lift failures are contrasts, not
premises asserting that arbitrary bases fail.

For reproducible finite polynomial notation encode Σ a_j z^j by
Σ a_j 2^j, and encode a row by bits in the stored coordinate order.
From L122 §2's complete endpoint transitions, the residual columns are

    R_A bits: [0,480,160,96,32,0,16,8,4,2,0,1],
    R_B bits: [0,30,10,6,2,0,272,136,68,34,0,1].       (1)

For example, A's f_i residual is z^5(1+z)^(3-i), i<4,
and its h_j residual is z^(4-j), j<4. B's f_i residual is
z(1+z)^(3-i), i<4, while its h_j residual is
z^(4-j)(1+z)^4=z^(4-j)+z^(8-j), j<4.
In both columns s,f4,h4 vanish and t has residual 1. These formulas
also follow by the finite backwards recurrence R=beta+zMR; they include
every coordinate and use no leading constant closure on R.

All these polynomials have degree at most eight. A's nine nonzero
residuals are monic with distinct degrees 0,...,8 and therefore
independent. Thus the map (u,v)->uR_A+vR_B has rank 9 in a
24-dimensional domain, proving dim(E₄)=15.

### 2. The complete basis, every shift equation and both boundaries

Every set in the following table denotes the sum of its named unit
rows in the specified endpoint block; '-' means zero. Let g_i=(a_i,b_i).
The last column gives the entire shift image as a sum of g_j; absent
indices have coefficient zero.

| i | A block a_i | B block b_i | shift targets j |
|---|---|---|---|
| 0 | s | - | - |
| 1 | f4 | - | - |
| 2 | h4 | - | - |
| 3 | - | s | - |
| 4 | - | f4 | - |
| 5 | - | h4 | - |
| 6 | h3 | f3 | 2,4,7 |
| 7 | t | t | - |
| 8 | h1,h3 | f1 | 2,4,6,7,9 |
| 9 | h2,h3 | f2 | 2,4,6,7 |
| 10 | f3,h3 | h3 | 1,2,4,5,6,7,9,11 |
| 11 | h0,h2 | f0,f1 | 8 |
| 12 | f1,f3,h1 | h1 | 13 |
| 13 | f2,f3,h2 | h2 | 10 |
| 14 | f0,f1,f2,f3,h0 | h0 | 12 |

Substitution in (1) verifies all fifteen residual equalities. The first
six rows are independent unit vectors on distinct zero-residual
coordinates. The remaining nine rows have independent projections onto
B's nine nonzero-residual coordinates: the four f projections are
f3,f1,f2,f0+f1; the four h projections are h3,h1,h2,h0; and the last
projection is t. None uses a zero-residual B coordinate. Therefore all
fifteen rows are independent, and the dimension calculation proves they
span the full E₄. This is more than the paired reachable space.

Let X_A,X_B be the two blocks of the table and T its shift matrix.
L122 §2's transition rows give, entry for entry,

    T X_A=X_A M_A, T X_B=X_B M_B.                    (2)

The shift-target column is a full specification of (2), not a sample.
For instance, row 11 uses (f0+f1)M_B=f1 and
(h0+h2)M_A=h1+h3, giving g_8. In row 10 the extra output-dead
rows 1,2,4,5 and row 7 are retained; omitting them would fail (2).
The complete products in (2) are also saved in the certificate below.
There are 3+5+4+8+1+1+1+1=24 transition entries.

The initial coordinate row is c=e_0+e_1+e_3+e_14. Directly,

    c X_A=s+f0+f1+f2+f3+f4+h0=alpha_A,
    c X_B=s+h0=alpha_B.                             (3)

The two final products agree and are d=e_7^T:

    X_A beta_A=X_B beta_B=d, c d=0.                (4)

The order

    0,3,14,12,13,10,1,5,11,8,9,6,2,4,7

puts every transition target strictly after its source. This directly
establishes acyclicity; nilpotence alone would not establish it in fixed
coordinates.

### 3. Finite minimum support, with complete exhaustive evidence

The basis weights are

    1,1,1,1,1,1,2,2,3,3,3,4,4,4,6,

of sum 37. For w>=0 let r_w be the rank of the span of ALL vectors of
E₄ of scalar weight at most w. Exact enumeration gives

    w:    0  1  2  3  4  5  6,...,24
    r_w:  0  6  8 11 14 14 15,...,15.               (5)

Here is a finite verification procedure for the upper bounds in (5),
independent of a heuristic basis search. Enumerate every mask
m=0,...,32767, form v=⊕_(i:bit_i(m)=1) g_i in the table's full
24-coordinate order, and compute w=popcount(v). Check

    m < 2^(r_w).                                   (6)

Since the table is an independent basis, this enumeration is bijective
onto E₄. Test (6) says every vector of weight w lies in the first r_w
table rows. The rank sequence in (5) is nondecreasing, so it gives the
upper bound also for every weight-at-most-w vector. The first r_w rows
themselves have weight at most w and are independent, giving the lower
bound. The supplied diagnostic independently computes the threshold
ranks by elimination; the separate audit executes (6) for ALL masks.
Both use integer XOR/popcount only, without floating-point tolerances,
randomness, a solver's success flag, or a truncated search. The full
enumeration and rank evidence are retained on disk.

For any basis H of E₄, at most r_w of its members can have weight at
most w. Using wt(h)=Σ_(w=0)^23 [wt(h)>w] gives

    Σ_(h in H) wt(h) >= Σ_(w=0)^23 (15-r_w)
       =15+9+7+4+1+1=37.

The table attains this lower bound. This proves finite optimality of
generator support only, without optimizing T or any occurrence graph.

### 4. Literal acyclic realization and all added map rows

Q's vertices in stored order are s,q0,...,q14,t. For each target j in
the table put ONE x occurrence qi->qj. Put constant occurrences

    s->q0, s->q1, s->q3, s->q14, q7->t,

and no others. Extend the displayed transition order by s first and t
last. This proves the complete raw occurrence graph acyclic. Its raw
roots are s,t. All edge labels are the singleton 1 or x, and no dense
closure or compressed XOR program is supplied as an uncharged object.

Let Y_J:Q->J, J=A,B, have entire rows

    Y_J(s)=0,
    Y_J(qi)=X_J(i)+d_i e_(t_J),
    Y_J(t)=e_(t_J).                                (7)

Only i=7 has d_i=1, so (7) removes its t entry and adds one fresh final
row. No other original endpoint entry changes. All scalar entries are
listed by (7) and the complete table. In particular the qi=q7 row is
zero in BOTH maps; t still carries the full original final direction.

To check the right-closure convention explicitly, Q's closed initial row
is e_s+Σ c_i e_qi, because cd=0. Its closed transition from qi is
Σ T_ij e_qj+(Td)_i e_t, and its s,t transition rows vanish. Applying
Y_J to a qi transition gives

    Σ T_ij (X_J(j)+d_j e_(t_J))+(Td)_i e_(t_J)
      = (T X_J)(i) = X_J(i) M_J = Y_J(qi) M_J.

The last equality uses e_(t_J) M_J=0, valid for these literal sinks.
The s,t transition equations hold because both sides are zero.
The initial equation follows from (3), (4), and (7). Each internal
map row has final coordinate d_i+d_i=0, the s row also has final zero,
and the t row has final one. This proves all three arrow equations.

The paired rows of (7) retain all table generators except g7, which is
replaced by the t row g7. Thus their span remains the whole E₄. No
auxiliary map or accepting state has been omitted.

### 5. Exact ledger, replay and limitations

There are 15+2=17 vertices and 24+4+1=29 charged occurrences, so g(Q)=75
and the two-arrow graph charge is 2g(Q)=150. X_A has support 24, X_B
support 13. Removing q7's two endpoint entries and adding the two final
entries leaves the realized combined map support 37. If the basis table,
T,c,d and realized arrows are all separately stored, their scalar-entry
charges are respectively 37,24,4,1,37, of sum 103. This does not replace
wire/index/work/live accounting. All finite counts are compared with
S=84 only at N=4; no bound on their ratios as N grows is asserted.

Reproduce in a fresh output directory:

```bash
python3 scripts/batched-incidence/check_residual_relation.py \
  --output /tmp/p-vs-np-residual-relation-542
python3 scripts/batched-incidence/audit_residual_relation.py \
  scripts/batched-incidence/output-542-direct/residual-relation.json \
  --output /tmp/p-vs-np-residual-relation-audit-542.json
```

The complete certificate is
`scripts/batched-incidence/output-542-direct/residual-relation.json`;
the separate audit is `scripts/batched-incidence/output-542-direct/audit.json`.
They retain the literal endpoints, closures, every basis row, all 32768
relation vectors, every shift-coordinate equation, both boundary products,
all Q occurrences and all arrow-product coordinates. The earlier
`output-542/residual-relation.json` retains an unnecessarily larger
orbit-unrolled realization (137 vertices, 140 occurrences, map support
163); the direct acyclicity test justifies the smaller realization here.
It is preserved as exploratory evidence, not used for the smaller ledger.

No uniform recursion has been constructed. The exhaustive search space
and its optimality statement concern ONLY E₄. In particular, finite
optimality does not imply an all-N lower bound, finite success does not
imply linear asymptotic costs, and rank alone does not control support.
The earlier template-specific stops remain intact.

## Mathlib

Full matching quantitative/finite-enumeration coverage was not checked.
Finite-dimensional kernel/rank and F₂ matrix operations are supporting
subjects, not a matching theorem supplying this full basis, minimum
support or occurrence ledger. No Mathlib theorem is imported, and unknown
coverage is not evidence of absence.
