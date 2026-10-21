# Constant-weight triple SDP — primary source input

Alexander Schrijver, [New code upper bounds from the Terwilliger algebra
and semidefinite programming](https://homepages.cwi.nl/~lex/files/codes.pdf),
IEEE Transactions on Information Theory 51 (2005), 2859–2866,
DOI 10.1109/TIT.2005.851748. Inspected the eight-page author manuscript
on 2026-10-05: equation (7), Theorem 1/equation (51), Section III.A,
equations (52)–(59), and Section III.B, equations (60)–(67).

Cross-check: Hyun Kwang Kim and Phan Thanh Toan,
[Improved Semidefinite Programming Bound on Sizes of Codes](https://arxiv.org/pdf/1212.3467v1),
arXiv:1212.3467v1, 14 December 2012, Section III.B, pp. 8–9,
equations (31)–(35); Section III.C.2, p. 10, equation (40).
The later strengthened constraints are not imported.

## Hypotheses

Let C be a nonempty binary length-n, constant-weight-w code of minimum
Hamming distance at least d, and v=n-w. For the proposed application,
d is even and 0<d<2w<=n. No linearity, design, field or RS hypothesis is
part of the cited coding bound. A singleton causes no difficulty; the
application has d>2 and cannot be the whole weight layer.

Write multinomial(N;a,b,c)=N!/(a!b!c!(N-a-b-c)!), zero if a part or
the remainder is negative. The nonzero triple-orbit indices are

\[
0\le i,j\le\min(w,v),\quad
\max(0,i+j-w)\le t\le\min(i,j),\quad
\max(0,i+j-v)\le s\le\min(i,j).
\]

For ordered triples (X,Y,Z) in C^3, let mu_(i,j)^(t,s) count those with
|X\\Y|=i, |X\\Z|=j, |(X\\Y) intersection (X\\Z)|=t,
and |(Y\\X) intersection (Z\\X)|=s. Set

\[
y_{ij}^{ts}=\frac{\mu_{ij}^{ts}}
 {|C|\,\operatorname{multinomial}(w;i-t,j-t,t)
       \operatorname{multinomial}(v;i-s,j-s,s)},\qquad p_i=y_{i0}^{00}.
\]

Zero-orbit coefficients are zero, not variables with a zero denominator.
Distance-zero cases represent repeated codewords and must be retained.

## Conclusion

The following is the cited constant-weight SDP, not a newly proved bound.
Define, using ordinary binomials,

\[
\beta_{ij,k}^{t,N}=\sum_{u=k}^{N-k}(-1)^{u-t}
 \binom ut\binom{N-2k}{u-k}
 \binom{N-k-u}{i-u}\binom{N-k-u}{j-u}.
\]

Let W_k={k,...,w-k}, V_l={l,...,v-l}. For every
0<=k<=floor(w/2), 0<=l<=floor(v/2), both matrices

\[
\left(\sum_{t,s}\beta_{ij,k}^{t,w}\beta_{ij,l}^{s,v}y_{ij}^{ts}\right)_{i,j\in W_k\cap V_l},
\quad
\left(\sum_{t,s}\beta_{ij,k}^{t,w}\beta_{ij,l}^{s,v}
 (p_{i+j-t-s}-y_{ij}^{ts})\right)_{i,j\in W_k\cap V_l}
\]

are positive semidefinite. Sums use admissible orbit indices; empty blocks
impose no condition. The scalar conditions are

\[
p_0=1,\qquad 0\le y_{ij}^{ts}\le p_i,\qquad
p_i+p_j\le1+y_{ij}^{ts}.
\]

Use the scalar orbit inequalities only on nonzero orbit matrices.
Coefficients are equal when t-s is unchanged and the ordered triples
(i,j,i+j-t-s) are permutations. They vanish if any of
2i, 2j, 2(i+j-t-s) belongs to {1,...,d-1}. No equality based only on
the three distances is licensed: t-s must also be preserved.

The maximization objective is

\[
\sum_{i=0}^{\min(w,v)}\binom wi\binom vi p_i.
\]

Its optimum upper-bounds A(n,d,w). Equation (40) of Kim–Toan identifies
binom(w,i)binom(v,i)p_i with the average distance count B_(2i),
including B_0=1. Thus this objective includes the diagonal contribution,
unlike L021's objective sum a_i.

## Proof

Import Schrijver's Section III.B, (64)–(67), cross-checked against
Kim–Toan (32)–(35). Schrijver's Theorem 1 and Section III.A (53)–(58)
give the tensor block diagonalization, deletion of zero rows, and the
positive diagonal rescaling yielding the displayed integer coefficients.
Section III.B (60) averages incidence-vector outer products separately
over permutations whose image code contains or excludes an anchor of
weight w. Equations (62)–(63) give the triple normalization; (65) retains
repeated words, permutation symmetry and forbidden nonzero distances.
These essential source cases were read; no local reproof is needed.

Two source qualifications must survive implementation. The printed
all-index wording of the scalar inequalities is used only on actual
orbits; arbitrary impossible indices are not added as contradictory
constraints. Schrijver's (61) prints a complement prefactor with 2^n,
although (60) uses an anchor in the weight layer. This normalization
identity is not imported or repaired here. The needed PSD statement is
explicitly (64), independently restated as Kim–Toan (32)–(33); a program
must use those affine matrices, not reconstruct (61)'s prefactor.

## Mathlib

Full matching constant-weight triple SDP theorem and finite exact SDP
certificate machinery: **not checked** in Mathlib. No library theorem
is assumed from an uninspected search result.

## Strengthened four-block constraint source review (2026-10-06)

Kim–Toan arXiv:1212.3467v1, III.C.1, Theorem 12, equation (36),
printed pp. 9–10, is an additional necessary constraint. For every
nonzero orbit in the above normalization, let

\[
 D=\binom it\binom{w-i}{j-t}\binom is\binom{v-i}{j-s},\qquad
 K=T(t,i,j-t,w-i,s,i,j-s,v-i,d).
\]

Here T denotes the maximum size of a binary code of minimum distance d
with prescribed weights in four disjoint coordinate blocks, in the
alternating weight/length order displayed. The imported conclusion is
D y_{ij}^{ts} <= K p_i. Any certified upper bound on K gives a weaker
necessary inequality with that bound on the right. D is strictly positive
for the admissible orbits; no division through p_i is necessary.

The entire source proof (37)–(39) was inspected: fix an ordered pair
(X,Y), count eligible Z in the four coordinate regions, bound this count
by K, sum over pairs, and convert their count to p_i using (31).
Complementing the first two regions explains the source's weights
(t,j-t,s,j-s), rather than the uncomplemented weights in (37).
Repeated words are included; the proof does not require three distinct
words. Its only code hypotheses are binary constant weight and minimum
distance. No RS, linearity or field restriction is added. L022's support
application remains justified by its existing L001 argument.

For explicit coefficients, the appendix, printed pp. 18–19, defines
multiply constant-weight T and provides Proposition 22(ii),(iii),(v),(vi)
and Proposition 25 (99). Zero-weight blocks may be removed; any block
may be complemented. If the total weight is below d/2, the maximum is 1;
at d twice the total weight, it is min floor(n_a/w_a), taken over
positive-weight blocks. Proposition 25 bounds T by floor((n_a/w_a) T')
for w_a>0, where that block loses one coordinate and one unit of weight.
The appendix explicitly omits proofs of these elementary properties;
that qualification is retained. Their precise statements were read,
rather than claiming an inspected source proof. A future implementation
must justify induction and base cases locally. No such derivation or
coefficient computation was performed in this literature turn.

These constraints are additional to the ordinary scalar rows previously
imported. The prior sentence excluding strengthened constraints describes
the original 2026-10-05 scope. This supplement supplies source coverage,
not a feasibility claim for the fixed extension. Full matching Mathlib
coverage was not checked.

## Weak-duality certificate input (source review, 2026-10-20)

### Hypotheses

Use finite real affine scalar inequalities g_r(x)>=0, affine symmetric
matrix inequalities A_b(x)>=0 in the PSD order, and affine equalities
e_j(x)=0. The objective M(x) is affine. No constraint qualification,
strict feasibility, dual attainment or rational optimizer is assumed.

### Conclusion

The standard conic weak-duality certificate for an upper bound U is
the coefficient identity

    U-M(x) = sum_r lambda_r g_r(x) + sum_b trace(Z_b A_b(x))
             + sum_j nu_j e_j(x),

with lambda_r>=0, Z_b PSD and unrestricted nu_j. Rational coefficients
and exact PSD congruences give a finite checkable certificate. The
identity must include constants and every free coefficient; its trace
uses both symmetric off-diagonal entries. It asserts sufficiency of a
given certificate, not existence of one or equality of primal/dual optima.

### Proof

Import S. Boyd and L. Vandenberghe, *Convex Optimization*, Cambridge
University Press (2004), author PDF seventh printing with corrections
(2009), [§5.9.1, pp. 264–266](https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf),
the generalized-inequality weak-duality proof and Example 5.11.
Those passages were inspected on 2026-10-20, including the dual-cone
sign argument, PSD self-duality and affine coefficient cancellations.
Apply its minimization convention to -M; include scalar nonnegativity
cones and the retained PSD blocks. This is a sign specialization of the
cited standard rule, without reproving conic duality. The Schrijver
complement prefactor qualification above remains unchanged.

### Mathlib

Full matching finite conic certificate theorem: not checked. No presumed
Mathlib result or strong-duality theorem is required for this import.
