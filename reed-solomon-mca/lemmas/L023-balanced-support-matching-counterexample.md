# L023 — Balanced sixteen-support incidence does not force a disjoint triple

## Hypotheses

Let G=Z/8Z, A={0,1,2,4}, and V={0,1}×G. For i in {0,1}
and t in G define E_(i,t)={i}×(A+t), and let F be the family
of these subsets of V. Addition and subtraction in G are modulo eight.
The matching number is the largest size of a pairwise disjoint subfamily.

## Conclusion

F is a simple four-uniform family on sixteen vertices with exactly
sixteen edges. Each vertex belongs to exactly four edges, but F has
matching number exactly two. Thus sixteen distinct four-element
supports on sixteen coordinates, each coordinate used four times,
need not contain three pairwise disjoint supports.

This is an exact specialization of a known cyclic construction, not a
claim of a new construction. It rejects only the incidence-only
implication suggested by L010's equality conclusion. It supplies no
affine syndrome pencil, coordinate locators, error weights, nonzero
Hankel determinants, or moment-compatible equality witness. L022's
restriction to its prescribed supports and parameters is unaffected.

## Proof

We import the following known result: for a subset S of a finite Abelian
group G, S-S=G if and only if its family of translates is intersecting.
The forward translate construction works for composite group order;
the prime-order restriction in the reverse comparison of minimum-size
quantities is not used. Precise source: Ellis, Kalai and Narayanan,
*On symmetric intersecting families*, arXiv:1702.02607v8 (9 June 2022),
Section 4, printed p. 12, observation immediately preceding Lemma 4.1
and the forward construction in its proof
([versioned primary PDF](https://arxiv.org/pdf/1702.02607v8)).

Every residue has an explicit witness as a difference of elements of A:

| Residue | Difference modulo eight |
| --- | --- |
| 0 | 0-0 |
| 1 | 1-0 |
| 2 | 2-0 |
| 3 | 4-1 |
| 4 | 4-0 |
| 5 | 1-4 |
| 6 | 0-2 |
| 7 | 0-1 |

Consequently A-A=G, so the cited result makes its translate family
intersecting. The complete orbit is:

| t | A+t, written in increasing residue order |
| --- | --- |
| 0 | {0,1,2,4} |
| 1 | {1,2,3,5} |
| 2 | {2,3,4,6} |
| 3 | {3,4,5,7} |
| 4 | {0,4,5,6} |
| 5 | {1,5,6,7} |
| 6 | {0,2,6,7} |
| 7 | {0,1,3,7} |

These eight sets are pairwise distinct by their displayed elements.
They are all the translates because G has eight elements; in particular
the translation stabilizer of A is {0}. For each fixed v in G,
v belongs to A+t exactly when t=v-a for some a in A. The four distinct
a give four distinct t. Thus each vertex has degree four in one copy.

The two copies have disjoint vertex sets, so their eight-edge orbits
give sixteen distinct edges in total and preserve degree four on V.
Each edge has four vertices. Within either copy every pair of edges
intersects by the imported result. A matching therefore contains at
most one edge from each copy, hence at most two edges. The edges
E_(0,0) and E_(1,0) are disjoint and attain two. This proves the stated
matching number and the failure of the universal incidence implication.

All finite checks needed for this specialization are displayed above;
the proof does not depend on a numerical search or an uninspected
certificate. Relabeling V by any sixteen coordinate labels preserves
these incidence facts, but does not establish RS moment equations.
No such realization is asserted.

## Mathlib

The exact doubled cyclic family and the imported translate/intersection
equivalence have **not been checked** in Mathlib. No matching theorem
name or absence claim is made. The versioned primary citation supplies
the only imported mathematical result; the remaining checks are the
explicit finite specialization above.
