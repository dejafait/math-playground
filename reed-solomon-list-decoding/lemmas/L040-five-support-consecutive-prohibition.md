# L040 — Five prescribed consecutive-overlap supports are forbidden

## Hypotheses

Use C001a's E=F_65537, F=F_(65537^28), subgroup H of order 1024,
k=64 and any integer m>=1. As in L031, h=19139 generates H.
Order the edges ij, 1<=i<j<=5, lexicographically as
12,13,14,15,23,24,25,34,35,45, with indices r=0,...,9. Put

\[
 C=\{h^{20},\ldots,h^{78}\},\quad
 U_{ij}=\{h^{2r},h^{2r+1}\},\quad
 W_i=\{h^{78+i}\},\qquad
 S_i=C\cup W_i\cup\bigcup_{j\ne i}U_{\min(i,j),\max(i,j)}.
\]

Realizability means five pairwise distinct polynomial m-tuples P_i over F,
each row of degree strictly less than 64, and one center Y:H -> F^m
agreeing with P_i on every point of S_i. Extra agreements are allowed.
The messages and center are not assumed to descend to E.

For v in V=E[X]_<5^4, write its four quartics as g_1,...,g_4,
put g_5=0, and order coefficients by message, then ascending degree.
Let D_ij:V -> E^5 give the coefficients of g_i-g_j. Let M be the
20-by-20 matrix whose two rows for edge ij are
(1,x,x^2,x^3,x^4)D_ij for x=h^(2r),h^(2r+1), in that order.
Differences have signs +1 and -1 in E.

## Conclusion

The five supports are not realizable for any m>=1. More strongly,
any five tuples agreeing with one center on these supports are equal.
The exact signed matrix satisfies

\[
 \det_E M=52987\ne0,\qquad \operatorname{rank}_E M=20.
\]

The same full rank holds over F. This is one prescribed actual-label
restriction; no uniform support-family cap or boundary improvement is
established. The bracket 955<=t_star(m)<=957 remains unchanged.

## Proof

**Imported tools and scope.** The prior
[SPECIALIZE assessment](../drafts/literature/2026-10-08-five-support-consecutive-realizability.md)
covers exactly this configuration. Import the signed intersection
framework of Alrabiah–Guruswami–Li, *Randomly punctured Reed–Solomon
codes achieve list-decoding capacity over linear-sized fields*,
[arXiv:2304.09445v3](https://arxiv.org/pdf/2304.09445v3), 26 July 2023,
Definition 2.5 and Lemma 2.7, printed pp. 7–8. The common-root division
is the factor-theorem proof step in Shangguan–Tamo, *Combinatorial
list-decoding of Reed–Solomon codes beyond the Johnson radius*,
[arXiv:1911.01502v1](https://arxiv.org/pdf/1911.01502v1),
Lemma 4.3, printed pp. 11–12. Their list-radius conclusion is not used;
the characteristic-two assumption of their Section 5 forbids importing
its unsigned matrix here. L031 supplies the checked methodology and
generator, not a theorem for five messages. The changed core size,
all ten distinctions, fixed specialization and tuple qualifications are
justified below. No generic-rank result is applied to fixed subgroup points.

**Incidences.** Exact exponentiation gives h^1024=1 and h^512=65536=-1.
The divisors of 1024 are powers of two, so h has exact order 1024.
Its powers with exponents 0,...,83 are distinct. The twenty overlap
points use exponents 0,...,19; the core uses 20,...,78 (59 points);
the five private points use 79,...,83. These pieces are mutually
disjoint. Each support has 59+1+4*2=68 points. A noncore point belongs
either to its single private support or to exactly the two endpoints
of its edge. Consequently S_i intersect S_j=C union U_ij, and every
intersection of at least three distinct supports is exactly C. This
also exhausts all possible conflicts in prescribing one center.

**Tuple necessity and extension fields.** Let G=product_(c in C)(X-c).
It is monic of degree 59. In a realization, for every row a and every
i<=4, P_i,a-P_5,a vanishes at all core points. The factor theorem gives
P_i,a-P_5,a=G g_i,a with deg g_i,a<=4, including the zero case;
put g_5,a=0. On U_ij the two messages agree with Y, and G has no zero
there. Hence g_i,a-g_j,a vanishes at both points, so the row's
coefficient vector v_a lies in ker_F M. These are selected equality
constraints even if there are extra agreements; omitting the latter
never invalidates necessity.

The matrix and its inverse certificate below have entries in E.
The identity TM=I remains an identity over F; therefore ker_F M=0.
Thus every v_a=0, every P_i,a=P_5,a, and all five tuples are equal.
This contradicts pairwise distinctness. There is no descent assumption
on the given messages, and no projection of a tuple to a purported
scalar witness.

**All distinctions and center sufficiency.** To check explicitly what
the signed-system test means, put K=ker_E M. For a hypothetical
realization, each distinct pair ij must have D_ij v_a!=0 for at least
one row a, possibly a different row for every pair. If D_ij vanished
on K, then ker_E [M;D_ij]=K and the two ranks would be equal. Ranks
are unchanged in F because all minors lie in E; equal dimensions
and kernel inclusion would force D_ij to vanish on ker_F M as well.
Thus necessity requires D_ij|K!=0 for each of the ten pairs.

Conversely, if those ten conditions held for this system, let d=dim K.
Then d>=1, since a nonzero restriction cannot have zero-dimensional domain.
Each N_ij=K intersect ker D_ij would be a proper E-subspace, of size
at most 65537^(d-1). Their union has size at most
10*65537^(d-1)<65537^d. A vector outside the union would give five
pairwise distinct reduced polynomials, including g_5=0. Set f_i=Gg_i.
Their degrees are at most 59+4=63, and all differences remain nonzero
in E[X]. A nonzero polynomial of degree at most 63 cannot vanish on
all 1024 domain points, so the evaluation messages also remain distinct.
On S_i prescribe Y=f_i: all values are zero on C, and on U_ij the
prescriptions agree because Mv=0. There are no further intersections.
Set Y=0 outside the union. This would construct a scalar realization
over E, extended to every m by appending zero rows over F. This checks
sufficiency without assuming singularity alone suffices. For the actual
system K=0, all ten restrictions are zero and each augmented rank is
20 (it contains a rank-20 matrix with 20 columns). Thus no distinction
is possible; no scalar or tuple center witness has been asserted.

**Exact rank evidence.** The ten ordered overlap pairs are

```text
(1,19139), (15028,44536), (282,23164), (43528,41585),
(13987,44085), (19477,61384), (12114,45477), (52943,8520),
(8224,44799), (53027,43308).
```

Run `python3 scripts/finite-support/five_support_rank.py` from this
notebook. It writes the complete certificate to
`scripts/finite-support/five-support-rank-results.json`: the domain,
all pieces and supports, every pair and higher intersection, every
coefficient map, all twenty signed rows, all invertible elementary row
operations, their transformation T, the complete RREF and pivots,
determinant evidence, and each of the ten distinction conclusions.
The RREF is I_20, with pivot columns 0,...,19. There are three swaps;
the unnormalized pivot values, in order, are

```text
1,19138,25394,32960,57485,53426,38792,34828,26505,57017,
53426,64799,58736,11228,42637,15419,22893,19644,29749,1840.
```

Their product times (-1)^3 is 52987 modulo 65537. Every scale uses
a nonzero field element; every row addition uses distinct rows.
Replaying all operations on M and I gives respectively the saved
RREF and T. Separately multiplying the full matrices verifies TM=I
and MT=I. A different forward elimination, selecting the last
available pivot, leaving pivots unnormalized and clearing only below,
also computes determinant 52987. The inverse identity alone already
certifies the rank needed in the mathematical argument.

All 41 named checks pass, including all 26 pair/higher intersections,
all support sizes, both inverse identities and the independent
determinant. The complete matrix, transformation, overlap pairs,
pivot factors, all checks and ten distinction entries were inspected
in full using the bounded JSON inspector with `--full` at selected
pointers. The verifier checks every entry and every operation, without
sampling; no floating-point rank or preview is used as evidence.
The distinction ranks are logical consequences of full rank, not
separately computed augmented reductions.

**Independent critical audit (2026-10-08).** The separate audit retains
the prohibition and conditional converse, with no substantive correction.
The strict degree bound is 63-59=4 after common-root division, including
zero differences. Every original tuple row separately lies in ker_F M;
the identity TM=I proves this kernel is zero over the extension. For the
conditional converse, d>=1 follows from the nonzero-restriction hypothesis,
and 10<65537 makes the union bound strict. Multiplication by G preserves
all nonzero differences. The complete incidence description exhausts
conflicting center prescriptions, while private points and extra
agreements cause no additional constraints. No tuple descent or common
distinguishing row is assumed.

Run `python3 scripts/finite-support/audit_five_support.py`. It reads the
original certificate without modifying it or importing the generating
script, and writes `scripts/finite-support/five-support-audit-results.json`.
The audit reconstructs h=3^64 and the entire domain by repeated
multiplication, assigns owners to all 84 used points, and checks all
five supports and all 26 pair/higher intersections. Each signed row is
reconstructed by evaluating each elementary message monomial; all twenty
rows and all ten coefficient maps agree exactly with the original.

All 275 saved operations are checked for invertibility and replayed on
[M | I]. The complete resulting left and right blocks are I and T;
both products TM and MT are independently checked in all 400 entries.
Every raw pivot, normalization, swap, pivot column and determinant factor
is checked. For each of the ten maps D, the audit also saves the complete
5-by-20 matrix DT and verifies (DT)M=D entry by entry. Thus all its rows
are in the row space of M, directly certifying the augmented rank 20
and zero restriction without relying on a saved distinction label.

As a separate determinant check, exact integer fraction-free (Bareiss)
elimination on the displayed residue matrix, with last-available-row
pivots, gives

```text
3428318394171485247353829459767439037379410237770150198071735712171331339789894739905391
```

which reduces to 52987 modulo 65537. Each trailing entry is updated as
(pivot*entry-column_entry*row_entry)/previous_pivot, starting with previous
pivot 1; all exact divisions and row-swap signs are retained. This is the
standard fraction-free determinant elimination identity over the integers;
the terminal entry times the total swap sign is the determinant. This
independent arithmetic check is redundant for rank: the two complete
inverse identities already supply the required certificate.

All 417 named audit checks pass. The audit artifact retains source and
script hashes, complete reconstructed data, every replay state, every
integer elimination division and all ten row-space identities. The full
original matrix and inverse and the full integer determinant were also
inspected using selected `--full` JSON pointers. No sampling, floating-point
rank or preview is treated as verification. This establishes reliability
of the existing local input, not a new support-family or list bound.

**Relevance and limitations.** A selected-support list containing this
exact configuration cannot share a center, so this prohibition could
be used as one additional necessary support constraint. No estimate
on families avoiding it is supplied. Its 59-core is outside L031's
60-core incidence hypotheses; it is not an application of L034's
184665717 cap criterion. Quantitative exploitation, cross-core
consistency, large common-center lists, 67/68-agreement safety and
ABF equivalence remain unresolved. The old stops in ATTEMPTS/019–021
and 023–025 are retained. This is a local REPRODUCTION/specialization
of the assessed equality tools, without a novelty claim beyond the
sources checked or a candidate resolution of the challenge.

## Mathlib

Full matching five-support prohibition, tuple criterion, fixed signed
matrix certificate and supporting finite-union/extension-rank results:
**not checked** in Mathlib. Unknown availability is not evidence of
absence. Precise primary mathematical inputs and the reason for the
finite specialization are recorded above.
