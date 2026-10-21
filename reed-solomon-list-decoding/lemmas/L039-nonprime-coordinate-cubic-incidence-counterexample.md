# L039 — Changed-coordinate cubic family contains the four-block pattern

## Hypotheses

Let K=F_11[u]/(u²-2), with the field presentation verified in L032,
and let T={0,1,2,3,4,5,6,u}. Define

\[
 \Omega=(T\times K)\setminus\{(0,0),(0,1),(0,2),(0,3)\}.
\]

Retain every graph B_p={(x,p(x)):x in T}, where p in K[X] has degree
at most three and p(0) is outside {0,1,2,3}. The whole-pattern diagnostic
asks for four distinct retained blocks whose six complete pair
intersections have size two, are mutually disjoint as graph-point sets,
and leave two private points in each block. Opposite edges may reuse a
coordinate when their graph values differ. This is auxiliary incidence,
not the actual-label restriction of L031 or an RS-list construction.

## Conclusion

Whole-pattern avoidance fails for this exact changed family. Put

\[
 f=X^3-X,\qquad g=X^3-X^2+8X+2,
\]

and take p_1=4, p_2=4+f, p_3=4+g, p_4=4+f+g. Their graph blocks
satisfy every diagnostic requirement and avoid every deleted point.
This stops the changed-coordinate avoidance construction. It supplies
no actual labeled cap, common-center RS realization or improvement of
955<=t_star(m)<=957.

## Proof

**Scope and known inputs.** The preexisting EXPLORE assessment
`drafts/literature/2026-10-08-nonprime-coordinate-cubic-pattern.md`
covers this exact finite diagnostic. Its inspected signed-equality
framework is Alrabiah, Guruswami and Li, *Randomly punctured
Reed–Solomon codes achieve list-decoding capacity over linear-sized
fields*, [arXiv:2304.09445v3](https://arxiv.org/pdf/2304.09445v3),
26 July 2023, Definition 2.5 and Lemma 2.7 including proof, printed
pp. 7–8. This motivates the search; the proof below uses direct
substitution rather than a generic-rank or random-puncturing theorem.
No inspected source supplies the displayed finite witness, so direct
verification is necessary. POTENTIALLY_NEW describes only this recorded
comparison and is not an originality claim. No GRS equivalence or
reproof of a known rank theorem is used.

L032 verifies that 2 is a nonsquare modulo 11, so K is a field and
u is outside its prime subfield. In particular the eight points of T
are distinct and -u is not in T: it is neither a prime-subfield element
nor u, since characteristic 11 is odd and u is nonzero. All arithmetic
below is in K. L032's old witness is not imported as a witness on T;
its direct evaluation loses one intersection point on edge 14.

**Polynomials, shortening and all evaluations.** The displayed four
polynomials have degrees 0,3,3,3. Their values at zero are 4,4,6,6,
which all avoid the four deleted values. Thus all four entire graphs
lie in Omega. Their complete evaluations are:

| x | p_1(x) | p_2(x) | p_3(x) | p_4(x) |
|---|---:|---:|---:|---:|
| 0 | 4 | 4 | 6 | 6 |
| 1 | 4 | 4 | 3 | 3 |
| 2 | 4 | 10 | 4 | 10 |
| 3 | 4 | 6 | 4 | 6 |
| 4 | 4 | 9 | 9 | 3 |
| 5 | 4 | 3 | 3 | 2 |
| 6 | 4 | 5 | 3 | 4 |
| u | 4 | 4+u | 4+10u | 4 |

For the last row, u²=2 and u³=2u give f(u)=u and g(u)=10u.
Their sum is zero. The prime-subfield rows follow by substitution
modulo 11. In particular 4+u and 4+10u are distinct from 4 and from
each other: equality between the latter two would force 9u=0.

Independent factorizations exhaust the coordinate equalities:

\[
\begin{aligned}
 f&=X(X-1)(X+1),\\
 g&=(X-2)(X-3)(X-7),\\
 f-g&=(X-4)(X-5),\\
 f+g&=2(X-6)(X^2-2).
\end{aligned}
\]

These identities hold by multiplication modulo 11. The roots 10,7
and -u are outside T. Therefore the zeros on T of f,g,f-g,f+g are
exactly {0,1},{2,3},{4,5},{6,u}. Each difference between distinct
p_i is, up to sign, one of these four nonzero polynomials. The table
also directly shows that the four graphs are distinct.

**Complete graph-point intersections and private parts.** The full
pair intersections are:

| Edge | Its complete intersection |
|---|---|
| 12 | {(0,4),(1,4)} |
| 13 | {(2,4),(3,4)} |
| 14 | {(6,4),(u,4)} |
| 23 | {(4,9),(5,3)} |
| 24 | {(2,10),(3,6)} |
| 34 | {(0,6),(1,3)} |

The only repeated coordinates across these edge sets are 0,1 on
opposite edges 12/34 and 2,3 on opposite edges 13/24. Their values
differ at each repeated coordinate. All six graph-point sets are
therefore mutually disjoint; no point belongs to three blocks.
Their complete private parts, read from the eight-point table, are:

| Block | Its complete private part |
|---|---|
| 1 | {(4,4),(5,4)} |
| 2 | {(6,5),(u,4+u)} |
| 3 | {(6,3),(u,4+10u)} |
| 4 | {(4,3),(5,2)} |

Each private point is absent from every other block by that table.
Thus every pair has exactly two common points, every block has exactly
two private points, and the union has 6*2+4*2=20 points. This proves
the entire required pattern, including shortening, without inferring
it merely from a singular equality matrix.

**Exact certificate and bounded search.** The command
`python3 scripts/finite-support/nonprime_cubic.py` writes
`scripts/finite-support/nonprime-cubic-results.json`. Field elements
are encoded there as the integer a+11b for a+bu; this is not arithmetic
modulo 121. The file contains all 32 values, every complete block,
intersection and private part, deletion checks, factorization
coefficients, field inverses and the selected signed matrix, reduction,
transformation and kernel. The first tested parallelogram partition
was {0,1},{2,3},{4,5},{6,u}; its rank is seven and its selected kernel
is (0,10,0,1,2,8,10,1). Adding the common constant 4 gives this witness.
The general K4 search was not reached. All 192 named checks pass,
including the complete transformation identity, kernel identities and
independent Horner/direct evaluations. The complete witness and linear
certificate were inspected. The explicit table and factorizations
above are the load-bearing proof; no search completeness is asserted.

**Separate critical audit (2026-10-08).** The preexisting SPECIALIZE
assessment `drafts/literature/2026-10-08-nonprime-cubic-critical-audit.md`
authorizes this REPRODUCTION audit. It retains the witness without any
correction or new bound. The field input from L032 was checked directly:
the square set is {0,1,3,4,5,9}, excluding 2, and all 120 nonzero
elements have nonzero norm a²-2b². Thus reduction by u²=2 is field
arithmetic, not integer arithmetic modulo 121. The eight positions are
distinct; -u is excluded for the reasons above.

Independent multiplication gives the ascending coefficient vectors
(0,10,0,1), (2,8,10,1), (9,2,1), (2,7,10,2) for the four displayed
factorizations. For example, the last product is
2X³-12X²-4X+24=2X³+10X²+7X+2 in characteristic 11; the third is
X²-9X+20=X²+2X+9. These equal f,g,f-g,f+g respectively. Their
complete roots in K are {0,1,10}, {2,3,7}, {4,5}, {6,u,-u};
the factorizations and nonzero leading coefficients rule out additional
roots. Intersecting with T gives exactly the four coordinate pairs
claimed above. In particular f(u)=u, g(u)=10u, while 4,4+u,4+10u
are pairwise distinct, so the nonprime row has no hidden equality.

The command `python3 scripts/finite-support/audit_nonprime_cubic.py`
writes `scripts/finite-support/nonprime-cubic-audit-results.json`.
It imports no producer routines. It represents elements as residue
pairs, multiplies by convolution followed by quadratic reduction,
constructs the four polynomials from their definitions, and evaluates
by direct power sums. It reconstructs every field of the complete
saved witness and compares all 32 values, all four eight-point blocks,
all six complete intersections and all four complete private parts.
All 70 named checks pass. The full reconstructed witness was inspected,
not merely its summary or the producer's pass flags. The certificate
records the input file's SHA-256 and all actual/required check values.

Set operations independently give pair sizes (2,2,2,2,2,2), private
sizes (2,2,2,2), four empty triple intersections and union size 20.
On opposite edges 12/34 the repeated x-values 0,1 have respective
y-values (4,6) and (4,3); on 13/24 the repeated x-values 2,3 have
(4,10) and (4,6). These inequalities verify the disjointness at every
repeated coordinate. Every other edge pair uses different coordinates.
The four private sets displayed above are the full set differences,
so every block has precisely six shared and two private points.
Degrees (0,3,3,3) satisfy the family bound; zero values (4,4,6,6)
exclude all deletions. This verifies both membership and the complete
incidence conclusion without using an equality-matrix rank.

The search matrix, kernel selection and search completeness are not
inputs to this audit and were not recertified. Their role remains
auxiliary discovery evidence. The direct witness is sufficient even
without those fields. This audit reproduces the existing proof; it
does not import an unverified converse from AGL Lemma 2.7 or establish
a new restriction on actual subgroup labels.

**Limits and decision.** One permitted witness refutes whole-pattern
avoidance. It does not refute the existence of other avoidance families
or establish a violation of L031's actual-label rank test. Auxiliary K
is not the subgroup-label field. No cap conversion is performed;
L033's independent triple condition, actual-label ranks, cross-core
consistency, common-center realization, 67/68 safety and ABF equivalence
remain unresolved. The separate critical audit retains this local
counterexample and its family-specific stop; the main challenge remains
IN_PROGRESS.

## Mathlib

Full matching finite witness and changed-family incidence theorem:
**not checked**. Supporting quotient-field, finite-field and polynomial
factorization results: **not checked** in Mathlib. Unknown coverage is
not evidence of absence. The field presentation is the retained local
input L032, and the finite incidence proof is written out above.
