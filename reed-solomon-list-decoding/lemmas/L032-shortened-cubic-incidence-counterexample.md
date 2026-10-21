# L032 — Shortened cubic packing contains the four-block incidence pattern

## Hypotheses

Let K=F_11[u]/(u²-2), T={0,1,...,7} in its prime subfield, and

\[
 \Omega=(T\times K)\setminus\{(0,0),(0,1),(0,2),(0,3)\}.
\]

Let \(\mathcal B\) consist of the graph blocks
\(B_p=\{(x,p(x)):x\in T\}\) for polynomials p in K[X] of degree at
most three with p(0) outside {0,1,2,3}.

The abstract forbidden incidence pattern means four distinct blocks,
every pair intersection having size two, the six pair intersections
mutually disjoint as sets of graph points, and exactly two private
points in each block. This is the whole-pattern avoidance diagnostic,
not L031's actual labeled rank restriction over F_65537.

## Conclusion

K is a field of order 121, |Omega|=964, and |B|=207272637.
Distinct blocks meet in at most three points. Nevertheless B contains
the stated four-block pattern: put

\[
 f=2X+9X^2,\qquad g=1+4X+4X^2+X^3,
\]

and take p_1=u, p_2=u+f, p_3=u+g, p_4=u+f+g.
Thus the proposed shortened cubic whole-pattern avoidance construction
fails. No finite labeled-cap bound, unsafe RS list, or improvement of
955<=t_star(m)<=957 follows.

## Proof

**Sources, scope and reason for the finite calculation.** The pre-existing
[EXPLORE assessment](../drafts/literature/2026-10-07-shortened-cubic-four-pattern-test.md)
covers exactly this prescribed finite diagnostic. The signed equality
search uses the framework of Alrabiah, Guruswami and Li, *Randomly
punctured Reed–Solomon codes achieve list-decoding capacity over
linear-sized fields*, [arXiv:2304.09445v3](https://arxiv.org/pdf/2304.09445v3),
26 July 2023, Definition 2.5 and Lemma 2.7, printed pp. 7–8, previously
inspected for L031. No random-puncturing or generic-rank conclusion is
used. The root argument is L001's factor-theorem proof. Neither those
inputs nor the inspected high-girth existence theorems supply this
finite witness; direct substitution is needed. The proof below does
not rely on the search, a singular matrix alone, or an asymptotic theorem.
It is a local finite specialization not identified in the sources checked;
POTENTIALLY_NEW records only that comparison, with no originality claim.

**Field, shortening and ordinary packing.** The squares modulo 11 are
{0,1,3,4,5,9}. Thus 2 is a nonsquare and the quadratic u²-2 is
irreducible. Its quotient is a field with the 121 unique elements a+bu,
a,b in F_11. Multiplication is

\[
 (a+bu)(c+du)=(ac+2bd)+(ad+bc)u.
\]

For a nonzero a+bu the norm a²-2b² is nonzero: if b=0 this follows
from a nonzero, and if b is nonzero a zero norm would make (a/b)²=2.
The inverse is (a-bu)/(a²-2b²). This verifies the actual field
presentation, rather than treating arithmetic modulo 121 as a field.

There are 8*121-4=964 ground points. An ascending coefficient tuple
(c_0,c_1,c_2,c_3) has 117 choices for c_0 and 121 choices for each
other coefficient. All produce permitted graphs on Omega. If distinct
tuples gave the same graph, their nonzero degree-at-most-three
difference would vanish at eight distinct points, contradicting L001's
root argument. Therefore |B|=117*121³=207272637, with no quotient by
scalars or graph multiplicities. The same root argument bounds each
intersection of distinct blocks by three. This ordinary packing
property does not imply whole-pattern avoidance.

**The explicit witness.** All four p_i have u-coordinate one in their
constant term and zero in their other coefficients. Hence every value
on T has the form u+a, with a in F_11, and every block avoids all four
deleted points. Their degrees are respectively 0,2,3,3. They are distinct:
the differences, up to sign, are f, g, f+g and f-g, all nonzero.

The full table below gives p_i(x)-u in F_11. Every entry follows by
substitution in the displayed polynomials; all eight positions are shown.

| x | p_1-u | p_2-u | p_3-u | p_4-u |
|---|---:|---:|---:|---:|
| 0 | 0 | 0 | 1 | 1 |
| 1 | 0 | 0 | 10 | 10 |
| 2 | 0 | 7 | 0 | 7 |
| 3 | 0 | 10 | 10 | 9 |
| 4 | 0 | 9 | 2 | 0 |
| 5 | 0 | 4 | 4 | 8 |
| 6 | 0 | 6 | 0 | 6 |
| 7 | 0 | 4 | 7 | 0 |

As an independent way to exhaust the root sets, factor in F_11[X]:

\[
\begin{aligned}
 f&=9X(X-1),\\
 g&=(X-2)(X-6)(X-10),\\
 f-g&=10(X-3)(X-5)(X-8),\\
 f+g&=(X-4)(X-7)(X-9).
\end{aligned}
\]

The additional roots 10,8,9 are outside T. Thus the zeros on T of
f,g,f-g,f+g are exactly {0,1},{2,6},{3,5},{4,7}. The following are
the complete graph-point intersections, not merely coordinate sets:

| Edge | Its two graph points |
|---|---|
| 12 | (0,u), (1,u) |
| 13 | (2,u), (6,u) |
| 14 | (4,u), (7,u) |
| 23 | (3,u+10), (5,u+4) |
| 24 | (2,u+7), (6,u+6) |
| 34 | (0,u+1), (1,u+10) |

Only the opposite edges 12/34 and 13/24 reuse coordinates. At those
coordinates their values differ, so all six point sets are disjoint.
The incident edge sets occupy six different points in each block,
and their complete private parts are

| Block | Its two private graph points |
|---|---|
| 1 | (3,u), (5,u) |
| 2 | (4,u+9), (7,u+4) |
| 3 | (4,u+2), (7,u+7) |
| 4 | (3,u+9), (5,u+8) |

The full table shows these points occur in no other block. Consequently
there is no triple intersection and no unintended pair equality.
The union has 6*2+4*2=20 graph points. This proves every requirement
of the pattern inside the shortened family.

**Finite certificate and bounded search.** Run
`python3 scripts/finite-support/shortened_cubic.py`. It writes
`scripts/finite-support/shortened-cubic-results.json`, including all
120 nonzero field elements' norms and inverses, all tested coordinate
partitions, the selected signed matrix and its complete reduction,
kernel basis, all polynomial coefficients, 32 evaluations, six full
intersections, four full private parts and 287 named verification checks.
There are no failures. The entire witness object was inspected, and
the displayed table and factorizations give a proof independently
checkable without trusting the matrix search.

The search stopped at its twentieth coordinate partition. It tests
only the parallelogram subset h,h+f,h+g,h+f+g of the prescribed family;
it is not exhaustive exclusion. Its chosen partition assigns the
zeros of f,g,f-g,f+g to the four pairs stated above. The signed system
has kernel vector (0,2,9,0,1,4,4,1) in ascending coefficient order.
The certificate verifies the entire transformation times matrix
identity and all actual graph requirements. The conclusion rests on
the exhibited polynomials, so no search miss, completeness assertion
or inference from singularity is needed.

**Qualification and downstream decision.** One valid witness suffices
to refute whole-pattern avoidance for this entire prescribed family.
The assessment allows size/cap comparison only after complete avoidance;
that prerequisite fails, so no 60-core cap comparison is made. The field
K is auxiliary, not a subfield of the RS instance. The graph labels have
not been mapped into H\C or tested against L031's actual signed matrices.
This result refutes neither the existence of other large independent
families nor the actual labeled-cap target. Cross-core consistency,
common-center realization, 67/68-agreement safety and the ABF comparison
remain unresolved. It stops this fixed construction's proposed mechanism,
not the challenge or all cubic constructions.

## Mathlib

Full matching finite witness, shortened-family count and graph-incidence
counterexample: **not checked**. Supporting finite-field, quotient,
factorization and polynomial-root results: **not checked** in Mathlib.
Unknown coverage is not evidence of absence. The primary algebraic
framework is cited above; the complete finite proof is given locally.
