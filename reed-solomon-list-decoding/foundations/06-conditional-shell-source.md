# Conditional shell bounds — primary source coverage

Inspected 2026-10-06. Erik Agrell, Alexander Vardy and Kenneth Zeger,
*Upper bounds for constant-weight codes*, IEEE Trans. Inform. Theory
46(7) (2000), 2373–2395, DOI 10.1109/18.887851.
The directly inspected [institutional manuscript](https://publications.lib.chalmers.se/records/fulltext/local_14986.pdf)
is dated **June 24, 2000**, has 25 numbered manuscript pages after a
repository cover, and is not the journal pagination. Section IV.C,
printed pp. 9–11, contains Proposition 17 (57)–(64), Lemma 18 and its
complete proof (65)–(66), and the complete proposition proof (67)–(72)
and Figure 3 discussion. The theorem formulas are corroborated by
Kim–Toan, [arXiv:1212.3467v1](https://arxiv.org/pdf/1212.3467v1),
14 December 2012, printed pp. 16–17, Theorem 21 (91)–(95).
This note imports source coverage; it contains no computed exclusion test.

## Hypotheses

C is a nonempty binary length-n, weight-w code, with minimum distance
at least 2δ, where δ is a positive integer and w<=n/2. Its average shell
occupancies are A_(2i)=|C|^(-1) sum_(c in C)|S_(2i)(c)|. Take distinct
i,j in {δ,...,w}, and put Δ=w-δ. Choose positive integer bounds
P_i>=T(i,w,i,n-w,2δ) and P_j>=T(j,w,j,n-w,2δ).

For i+j<=n-δ choose nonnegative integers P_ij,P_ji satisfying

\[
P_{ij}\ge\min\{P_i,T'(\Delta,j,i-\Delta,n-w-j,2i-2\Delta)\},
\quad
P_{ji}\ge\min\{P_j,T'(\Delta,i,j-\Delta,n-w-i,2j-2\Delta)\}.
\]

Here T'(w1,n1,w2,n2,d) is the maximum size of a length n1+n2,
constant total weight w1+w2 binary code with distance >=d and **at most**
w1 ones in its first n1 positions, equivalently at least w2 ones in
its last n2 positions. It does not fix both block weights. Definition
(3), printed p. 3, supplies the original convention. For the proposed
test restrict to 0<=P_ij<=P_i and 0<=P_ji<=P_j by clipping certified
upper coefficients; this keeps the source proof's multiplying factors
nonnegative. No unrestricted replacement theorem is needed.

## Conclusion

If i+j>n-δ, Proposition 17 gives P_j A_(2i)+P_i A_(2j)<=P_i P_j.
In the other case put r=P_ij/P_i+P_ji/P_j. If r>1, its two rows are

\[
P_{ji}A_{2i}+(P_i-P_{ij})A_{2j}\le P_iP_{ji},
\qquad
(P_j-P_{ji})A_{2i}+P_{ij}A_{2j}\le P_jP_{ij}.
\]

If r<=1, its row is P_j A_(2i)+P_i A_(2j)<=P_i P_j.
Equality belongs to the latter case in both sources. The source's
geometric discussion says that P_ij=P_i and P_ji=P_j reduces the
constraint to the individual shell bounds (Proposition 15).

The coefficient tools inspected in the same manuscript are:

- Theorem 26 and its entire proof, printed p. 13: for
  p=min(w1,n2-w2) and 0<=e<p,
  T'(w1,n1,w2,n2,d)<=T'(w1-e-1,n1,w2+e+1,n2,d)
  +T(w1,n1+e,w2+e,n2+e,d). The proof partitions by head weight and
  appends bits to the second part; extension cannot reduce distance.
- Theorem 22, printed pp. 12–13: T'(0,n1,w2,n2,d)=A(n2,d,w2).
  Its elementary proofs are omitted, not reported as inspected proofs.
- Theorems 32 and 36 (142)–(145), printed pp. 16–17: block reflection,
  deletion of zero weights, disjoint-support and distance-too-large
  base cases, and integer shortening bounds for either block. These
  statements have no full proof there. Theorems 8–9, printed pp. 6–7,
  provide the corresponding one-block rules.
- Theorem 27 (110)–(111) and complete proof, printed pp. 13–14:
  T'<=A(n1+n2,d,w1+w2), and for d=2δ,
  T'<=A(n1+n2,2min(δ,n1-w1,w2),w1+w2)-1, in its positive-distance
  use. These are alternative bounds, not evaluated coefficients here.

The author [T' table introduction](https://codes.se/bounds/dbw.html)
only promises tables at total length <=28 and even distance <=14
(with stated trivial exceptions). It supplies no tabulated coefficient
for the proposed length-956 inputs. The 2018 paper *Improved linear
programming bound on sizes of doubly constant-weight codes*,
DOI 10.1016/j.ffa.2018.08.009, is a search lead, not an inspected
theorem or a necessary input to this fixed elementary diagnostic.

## Proof

Import Proposition 17 and Lemma 18, rather than reprove the shell theorem.
Lemma 18 fixes c and x in shell i, orders c as (1^w,0^(n-w)), and
orders x with i exchanged positions in each block. For y in shell j,
the first-block distance to x is at most (w-i)+(w-j). The last block
therefore forces at most Δ ones in its distinguished i positions and
at least j-Δ in the remainder. For two words in shell j, their first
blocks differ in at most 2w-2j, so puncturing leaves distance at least
2j-2Δ. This is the T' coefficient for **P_ji**, bounding shell j when
shell i is occupied. Swapping i and j yields P_ij. The proof includes
the empty-shell case and the impossible i+j>n-δ case.

The proposition proof first records individual and conditional shell
caps (67)–(70). It splits anchors by occupancy of the two shells in
(71)–(72), then takes two different nonnegative linear combinations.
The sign of P_iP_ji+P_jP_ij-P_iP_j chooses the two ratio cases;
the i+j>n-δ case has no anchor with both shells occupied. These are
average constraints, not a claim that average occupancies are integers.
The convex hull discussion and the equality/redundancy case were read.

For the proposed later specialization use n=1024,w=68,δ=5,v=956,
Δ=63,i=67,j=68 and verify all displayed hypotheses before evaluation.
The conditional inputs are T'(63,68,4,888,8) for P_67,68 and
T'(63,67,5,889,10) for P_68,67. The source's remark confines useful
indices to above Δ; these selected indices are within that regime.
In foundations/04's normalization A_(2i)=B_(2i)=binom(68,i)binom(956,i)p_i;
L022 specifies p_i using half of L021's primal values. No original
pair value, triple assignment or objective is to be changed.

Only a prescribed upper-coefficient test is supported, not the exact
T' values. Repeated Theorem 26 with e=0, terminating at Theorem 22,
is an assessed way to bound T' by fixed-head-weight subcode bounds.
The later implementation must justify its shortening induction and
zero-block cases because the cited elementary statements omit proofs.
L025 already justifies the distance-10 version; a distance-8 instance
must explicitly use δ=4, rather than its hard-coded cutoff 5.
This justification serves an exact implementation of known bounds;
there is no reason to reprove the imported shell theorem.

An exclusion would remove the unchanged pair witness and all its triple
extensions; it would not optimize the strengthened program or prove
RS safety. A pass would park only these fixed upper coefficients, not
establish exact-coefficient or full-SDP feasibility. L023's scalar stop,
L024's block stop, L025's cap-10 stop and ATTEMPTS/017 remain independent.

## Mathlib

Full matching conditional-shell theorem, doubly-bounded-weight bounds
and this finite specialization: **not checked**. No absence or novelty
claim is inferred.
