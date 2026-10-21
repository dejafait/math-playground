# L020 — Exact triple-support criterion and subgroup degeneracy

## Hypotheses

Use C001a's instance E=F_65537, F=F_(65537^28), H<=E^* of order
1024, message dimension k=64, and any integer m>=1. A message is an
m-tuple of polynomials in F[X] of degree less than 64. Let S_1,S_2,S_3
be subsets of H of size 68, with common intersection T of size 61 and
pair-only overlaps

\[
 U_{12}=(S_1\cap S_2)\setminus T,\quad
 U_{23}=(S_2\cap S_3)\setminus T,\quad
 U_{31}=(S_3\cap S_1)\setminus T
\]

of size two each. These three pairs are disjoint. Each support has three
points belonging to neither other support. Write

\[
 G(X)=\prod_{t\in T}(X-t),\qquad
 q_{ij}(X)=\prod_{u\in U_{ij}}(X-u)=X^2-s_{ij}X+p_{ij}.
\]

The supports are **selected** agreement supports: realizability means
that there is one received array Y on H and three pairwise distinct
message tuples P_1,P_2,P_3 with P_i(x)=Y(x) for every x in S_i. Additional
agreements are allowed. Neither Y nor the original message coefficients
are assumed to lie in E.

## Conclusion

The supports are realizable, for any and hence every m>=1, if and only if

\[
 \det M=0,\qquad
 M=\begin{pmatrix}
 p_{12}&p_{23}&p_{31}\\
 -s_{12}&-s_{23}&-s_{31}\\
 1&1&1
 \end{pmatrix}.                                      \tag{1}
\]

Equivalently, their three (sum,product) points are collinear:

\[
 (s_{23}-s_{12})(p_{31}-p_{12})
 -(s_{31}-s_{12})(p_{23}-p_{12})=0.                    \tag{2}
\]

Rank is the same over E and F. When singular, M has rank exactly two,
and every nonzero scalar kernel vector has all three entries nonzero.
Every simultaneous realization has its row-wise reduced differences in
this one-dimensional kernel; realizability does not require an assumption
of descent for arbitrary messages.

On the prescribed subgroup, both cases occur. Three disjoint antipodal
pairs give realizable supports of the stated sizes; three consecutive
pairs of powers of a generator give nonrealizable supports. Thus universal
exclusion of this overlap pattern is false. This is a local support
restriction and a counterexample to universal nonvanishing, not a list
maximum, an unsafe-threshold witness or an improvement of
955<=t_star(m)<=957.

## Proof

**Known input and reason for specialization.** Import the three-way
difference-kernel dictionary from Chong Shangguan and Itzhak Tamo,
[Combinatorial list-decoding of Reed–Solomon codes beyond the Johnson
radius, arXiv:1911.01502v1](https://arxiv.org/pdf/1911.01502v1),
November 4, 2019 version, Definition 4.1, printed pp. 10–11, and the
common-root division in the proof of Lemma 4.3, pp. 11–12. Their matrix
has a first block row [I_s I_s I_s] and diagonal Vandermonde constraints
on the three pair intersections. Its kernel describes three
degree-less-than-s polynomials summing to zero and vanishing on the
respective pairs. Here common-root division gives s=64-61=3.
Lemma 4.2 proves symbolic nonvanishing under the empty triple-intersection,
pair-size-at-most-s and total-pair-size-2s hypotheses, which the reduced
pairs satisfy. We do not reprove that theorem or infer nonsingularity at
our fixed points from symbolic nonvanishing. The prior
[SPECIALIZE assessment](../drafts/literature/2026-10-05-triple-support-rank-diagnostic.md)
requires the tuple/extension, nonzero-difference, converse-center and
specialized-rank checks below. These are needed to use the known scalar
dictionary for this exact definition of realizability.

**Necessity and simultaneous tuples.** Suppose a realization exists. For
each row r, define cyclic differences

\[
 D_{12,r}=P_{1,r}-P_{2,r},\quad
 D_{23,r}=P_{2,r}-P_{3,r},\quad
 D_{31,r}=P_{3,r}-P_{1,r}.
\]

They sum to zero. Each vanishes on T, so division by the monic G gives
polynomials of degree at most 63-61=2 (including the zero polynomial).
For x in U_ij, G(x)!=0 and D_ij,r(x)=0, since both tuples equal the same
center there. By the factor theorem the quotient is a scalar multiple
of q_ij. Thus, for a_r,b_r,c_r in F,

\[
 D_{12,r}=G a_r q_{12},\quad D_{23,r}=G b_r q_{23},\quad
 D_{31,r}=G c_r q_{31},\qquad
 M(a_r,b_r,c_r)^t=0.                                 \tag{3}
\]

If M is invertible over F, every difference is zero in every row, contrary
to pairwise distinctness. Consequently a realization forces det M=0.
This does not use a scalar projection that might identify two tuples.

**Rank, nonzero entries and ambient extension.** Any two of the q_ij are
linearly independent over F. Indeed, a scalar relation between two monic
quadratics would make them equal; their distinct, disjoint root pairs
rule this out. Hence rank M>=2. If det M=0, its rank is exactly two.
A nonzero vector in its kernel cannot have a zero entry, because that
would give a dependence between the other two columns (or a zero
multiple of one nonzero column). Rank over a field is the largest size
of a nonzero minor; all minors lie in E, and E embeds injectively in F.
Thus both fields give the same rank. In the singular case an E-valued
nonzero kernel vector z=(a,b,c) exists by row reduction over E. Its span
over F is the entire F-kernel. Equation (3) therefore also describes
every row of an arbitrary F-valued tuple realization.

**Sufficiency and center.** Fix this z with a,b,c all nonzero. In the first
row set

\[
 f_1=0,\qquad f_2=-aGq_{12},\qquad f_3=cGq_{31}.
\]

Then f_1-f_2=aGq_12, f_2-f_3=bGq_23 (by Mz=0), and
f_3-f_1=cGq_31. The latter three are nonzero degree-63 polynomials.
All f_i have degree less than 64. Their evaluations are pairwise
distinct by L001's injectivity/root-bound argument on the 1024 distinct
points. For m>1 put zero in every remaining row. On each S_i prescribe
Y(x)=P_i(x). Whenever two prescriptions overlap, their difference
vanishes on T union U_ij, precisely the corresponding pair intersection,
so the prescriptions are compatible. Set Y(x)=0 off the union. This
constructs a single center and proves sufficiency for every m>=1.
The argument permits additional agreements. The size-three portions
unique to each S_i impose no further compatibility constraint.

**Determinant formula.** Reversing the first and third rows of M and
negating its sum row changes determinant by two signs. Its determinant
is therefore that of the rows (1,1,1), (s_12,s_23,s_31),
(p_12,p_23,p_31). Subtract the first column from the other two and expand
to obtain (2). This also shows explicitly that the test depends only
on the six pair-only points, not on the choice of T or unique portions.

**Realizable antipodal configuration.** Let h have order 1024 in H. Choose

\[
 U_{12}=\{1,-1\},\quad U_{23}=\{h,-h\},\quad
 U_{31}=\{h^2,-h^2\}.
\]

These are six distinct points: the exponents 0,512,1,513,2,514 are distinct
modulo 1024. All sums vanish, and products -1,-h^2,-h^4 are distinct,
so M has rank two. More explicitly, putting p_1=p_12, p_2=p_23,
p_3=p_31, the vector

\[
 (p_2-p_3,\ p_3-p_1,\ p_1-p_2)
\]

is nonzero in each coordinate, its coordinates sum to zero, and their
product-weighted sum is zero by expansion. It is a valid kernel vector.
Choose any 61 of the remaining 1018 points as T, then nine more points
split into three size-three unique portions. The supports obtained by
adjoining to T the two incident pairs and the respective unique portion
have exactly the required intersections. The center construction above
is therefore a genuine realization for every m, not merely a singular
matrix without distinct messages.

**Forbidden consecutive-power configuration.** Choose instead

\[
 U_{12}=\{1,h\},\quad U_{23}=\{h^2,h^3\},\quad
 U_{31}=\{h^4,h^5\}.
\]

All six points are distinct. Set x_0=1, x_1=h^2, x_2=h^4. The sum/product
coordinates of the three pairs are ((1+h)x_i,h x_i^2). Formula (2)
factors as

\[
 h(1+h)(x_1-x_0)(x_2-x_0)(x_2-x_1),
\]

which is nonzero: h!=0,-1 and x_0,x_1,x_2 are distinct by its order.
After any admissible core/unique-portion choice these supports are not
realizable for any m. This is a fixed-domain obstruction; it invokes
neither a generic-domain hypothesis nor a numerical universal test.

**Exact finite diagnostic.** Run
`python3 scripts/finite-support/triple_support_rank.py` from this notebook.
It saves `scripts/finite-support/triple-support-rank-results.json` with the
entire domain, both sets of supports, matrices, row reductions,
antipodal kernels, polynomial coefficients, all message and center
evaluations, full agreement sets and pairwise equality sets. All arithmetic
is modulo 65537. The choice h=3^64=19139 satisfies h^1024=1 and
h^512=-1. As the divisors of 1024 are powers of two, this proves its
order is exactly 1024; its cyclic group is H, since a field's polynomial
X^1024-1 has at most 1024 roots and H already supplies that many.

The fully inspected pair data and matrices are

```text
antipodal pairs: (1,65536), (19139,46398), (15028,50509)
M = [[65536,50509,65255],[0,0,0],[1,1,1]]
kernel normalized with c=1: (15028,50508,1)
rank=2, det=0
consecutive pairs: (1,19139), (15028,44536), (282,23164)
M = [[19139,23164,44085],[46397,5973,42091],[1,1,1]]
rank=3, det=34940
```

The determinant expansion and independent sum/product formula agree.
Row reduction and the explicit antipodal product-difference kernel agree.
All prescribed agreements and all center-overlap equalities are checked,
as are degree bounds and equality on exactly 63 columns for each pair of
messages. For the saved antipodal center the full agreement counts are
1016,68,68: the first message has allowed extra agreements. This count
also follows without enumeration. Outside the support union all 948
points match the zero first message; it matches its own 68 points. At
every remaining point some prescribed nonzero message is used and its
pairwise difference from the first message has no root there. Each other
message matches its 68 points and cannot acquire an extra agreement:
outside the union its roots are already in its prescribed support, and
on another support its difference roots are precisely the corresponding
63-point intersection. There are no reported failures. These diagnostics
check the explicit examples; the argument above supplies the criterion
for all admissible supports and tuple widths on this instance.

The realized list has at least three messages. C001a's threshold exceeds
2^320, so this is far below what would establish unsafety. A quantitative
bound on entire realizable support families, sufficient to save a factor
greater than 2.763 against C001b, is independent and unproved. Safety at
67 agreements, exact maxima and ABF equivalence also remain unresolved.

## Mathlib

Full matching triple-support criterion and the fixed-subgroup examples:
**not checked** in Mathlib. Supporting polynomial factor/root and
field-extension rank results: **not checked**. The canonical source is
the precise Shangguan–Tamo citation above; L001 supplies evaluation
injectivity locally. This is REPRODUCTION of the assessed scalar
difference-kernel method with tuple/converse and explicit fixed-domain
checks. It establishes a useful local restriction and its limitation;
no novelty beyond the sources checked is claimed.
