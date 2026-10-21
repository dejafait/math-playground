# L025 — Matching two does not force six edges on eight vertices

## Hypotheses

Let V=Z/16Z and A={0,1,2,5}. For t in V let E_t=A+t,
with addition modulo sixteen, and let F={E_t:t in V}.
The matching number is the largest size of a pairwise disjoint subfamily.

## Conclusion

F has sixteen distinct four-element edges on sixteen vertices, every
vertex has degree four, and its matching number is exactly two.
For every six distinct edges their union has at least nine vertices.
Consequently the proposed universal six-edge/eight-vertex criterion is
false, including under every stated simplicity and regularity hypothesis.

The auxiliary independent exhaustive check finds the stronger minimum
eleven for this example; the proof below needs only the lower bound nine
and does not depend on that computation. This is an abstract incidence
counterexample. No assignment of RS coordinate labels, affine moments,
error weights or distinct bad parameters is supplied. It does not refute
the MCA challenge or alter its current 11/q–16/q interval.

## Proof

The edges, indexed by their translates, are:

| t | E_t |
| --- | --- |
| 0 | {0,1,2,5} |
| 1 | {1,2,3,6} |
| 2 | {2,3,4,7} |
| 3 | {3,4,5,8} |
| 4 | {4,5,6,9} |
| 5 | {5,6,7,10} |
| 6 | {6,7,8,11} |
| 7 | {7,8,9,12} |
| 8 | {8,9,10,13} |
| 9 | {9,10,11,14} |
| 10 | {10,11,12,15} |
| 11 | {0,11,12,13} |
| 12 | {1,12,13,14} |
| 13 | {2,13,14,15} |
| 14 | {0,3,14,15} |
| 15 | {0,1,4,15} |

Each has four elements. They are distinct: the successive clockwise
gaps in A have lengths 1,1,3,11. Its unique gap of length eleven
would have to be preserved by any stabilizing translation, including
its endpoints, which forces the translation to be zero. For each v,
the translations containing v are exactly t=v-a for a in A; these
four translations are distinct. This proves degree four and also that
every vertex is used.

Direct subtraction gives
\[
 A-A=\{0,1,2,3,4,5,11,12,13,14,15\}.
\]
Indeed all differences lie between -5 and 5 as integers, and each
of 1,2,3,4,5 occurs as 1-0,2-0,5-2,5-1,5-0, respectively;
the negatives and zero also occur. Two translates E_s,E_t intersect
exactly when t-s belongs to this difference set: equality
a+s=b+t is equivalent to t-s=a-b. Thus they are disjoint exactly
when t-s is in {6,7,8,9,10}. In particular E_0 and E_6 are disjoint.
If three translates were pairwise disjoint, order their translation
indices clockwise around the sixteen-cycle. Each of the three positive
cyclic gaps would be in {6,7,8,9,10}, since it is the forward difference
of a pair of these indices. Their sum is sixteen, whereas each is at
least six, a contradiction. Therefore the matching number is two.

Now choose any six distinct translation indices S. Their edge union is
S+A, which contains S+{0,1,2}. Decompose S into its maximal nonempty
clockwise runs of consecutive vertices. If there are r such runs,
there are r intervening nonempty complement gaps, with lengths
g_1,...,g_r. They sum to ten, and r<=6. Adding 1 and 2 fills exactly
the first min{2,g_i} positions of the gap following each run. Thus
\[
 |S+\{0,1,2\}|=6+\sum_{i=1}^r\min\{2,g_i\}.             \tag{1}
\]
This counts all new positions: a complement vertex is reached by
adding 1 or 2 precisely if it is within two forward steps of the last
S vertex preceding its gap. Different gaps are disjoint.

If r>=2, at least one gap has length at least two, since the lengths
sum to ten and r<=6. Hence the sum in (1) is at least
2+(r-1)>=3, and the edge union has size at least nine.
If r=1, S is one interval of length six. Rotate it to {0,...,5};
rotation preserves the union size. Then
\[
 S+\{0,1,2\}=\{0,...,7\},\qquad S+5=\{5,...,10\},
\]
so S+A has size eleven. These cases cover every six-edge choice
and prove the stated lower bound without a certificate assumption.

The exact test is reproducible from the notebook root by
`python3 scripts/small-union/cyclic_orbits.py` and
`python3 scripts/small-union/verify_counterexample.py`.
The first certificate, `scripts/small-union/cyclic-orbits-result.json`,
records all 116 translation orbits of the 1820 four-element seeds.
Among its 112 full orbits, 62 have matching number two, and 56 of
those are candidate counterexamples to the proposed criterion.
These search counts are auxiliary, not a classification of arbitrary
regular families. The second certificate,
`scripts/small-union/selected-counterexample-verification.json`,
reconstructs the displayed family using set operations without importing
the generator, checks all 560 triples and all 8008 six-edge subsets,
and compares its full edge set and histogram with the first certificate.
It reports forty disjoint pairs, zero disjoint triples, and the complete
six-edge union histogram
\[
 11:64,\quad12:288,\quad13:1408,\quad14:3264,
 \quad15:2560,\quad16:424.
\]
The six indices 0,...,5 attain eleven. No verification failure was
reported; the complete selected edge list, checks, histogram and
minimum witness were inspected. The elementary proof above, rather
than the search, establishes the universal criterion's refutation.

No external theorem is required for this finite proof. The translate
mechanism is familiar, and the approved EXPLORE assessment did not
establish whether this exact counterexample was previously recorded.
No originality claim is made. L023 and L024 are contrasts and motivation,
not mathematical inputs to this proof.

## Mathlib

Coverage of this exact counterexample and its cyclic-gap bound is
**not checked** in Mathlib. No matching theorem name, absence claim
or Lean verification is asserted.
