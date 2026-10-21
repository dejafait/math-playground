# L026 — Alternating-coordinate obstruction for the cyclic 0125 family

## Hypotheses

Let F be any extension field of F_97. Let H be the order-sixteen
subgroup of F_97^*, let omega be any generator of H, and put
\[
 A_t=\{\omega^t,\omega^{t+1},\omega^{t+2},\omega^{t+5}\},
 \qquad 0\le t<16.
\]
Exponents are taken modulo sixteen. Use L010's moment map, with
zero-based syndrome indices in this proof:
\[
 \sigma(z)_j=\sum_{x\in H}z_xx^{j+1},\qquad 0\le j<8.
\]
All error weights and all parameters below are allowed to lie in F,
with no shifted-weight, scalar-orbit, or prime-field assumption.

## Conclusion

There do not exist u,v in F^8, parameters gamma_t in F, and words
e_t with support exactly A_t, such that
\[
 \sigma(e_t)=u+\gamma_t v\quad\text{for all }0\le t<16.
\]
In particular these sixteen supports cannot realize an L010 equality
pencil over F_(97^20), even with unrelated nonzero weights and sixteen
distinct finite parameters. The stronger nonexistence statement does
not require the parameters to be distinct or impose determinant or
nonpersistence assumptions: it already contradicts a necessary
syndrome condition, so no purported witness can pass all L010 gates.

This is a fixed cyclic labeling exclusion, for every generator omega.
It does not cover arbitrary bijective labelings of the abstract family
by H, other matching-number-two families, or arbitrary equality
supports. The global interval remains 11/q–16/q, and challenge-level
ABF26 correspondence is unresolved.

## Proof

Write m(x)=(x,x^2,...,x^8)^transpose and
U_t=span_F{m(x):x in A_t}. By L010's Vandermonde argument any eight
distinct moment columns are independent, and sigma has no nonzero
kernel word of weight at most eight. In particular sigma(e_t) is
nonzero for every full-weight e_t under consideration.

First suppose u,v were linearly dependent. Since every sigma(e_t)
is nonzero, span{u,v} would be a one-dimensional subspace contained
in every U_t. But A_0 and A_6 are disjoint, as in L025: their exponent
sets are {0,1,2,5} and {6,7,8,11}. Independence of the resulting eight
moment columns gives U_0 intersection U_6={0}, a contradiction. This
also rules out the zero-dimensional case. Consequently any proposed
realization would require linearly independent u,v.

We now exclude that possibility by linear equations in their alternating
coordinates. Set
\[
 p_{jk}=u_jv_k-u_kv_j\quad(0\le j<k<8).
\]
There are 28 such coordinates. All of them vanish if and only if u,v
are linearly dependent: if u is nonzero, choose u_j nonzero and the
relations give v_k=(v_j/u_j)u_k for every k; if u=0 dependence is
immediate.

Let
\[
 P_0(X)=\prod_{a\in\{0,1,2,5\}}(X-\omega^a)
       =\sum_{i=0}^4c_iX^i,
 \qquad c_i=0\text{ for }i\notin\{0,...,4\}.
\]
Then the support polynomial at t is
\[
 P_t(X)=\omega^{4t}P_0(\omega^{-t}X)
       =\sum_{i=0}^4c_i\omega^{(4-i)t}X^i.
\]
Define a four-by-eight matrix R_t: its row r, for 0<=r<4, is the
coefficient vector of X^r P_t(X), in degrees 0,...,7. Thus
\[
 (R_t)_{rj}=c_{j-r}\omega^{(4-j+r)t}.
\]
The zero-coefficient convention makes this formula valid for all j.
Its scalar product with m(x) equals x^(r+1) P_t(x), so R_t
annihilates every column from A_t. Hence a proposed realization gives
R_t u+gamma_t R_t v=0. For each row pair r<s its two coordinates
have zero alternating product. Expansion yields
\[
 0=\sum_{j<k}
 (c_{j-r}c_{k-s}-c_{k-r}c_{j-s})
 \omega^{(8+r+s-j-k)t}p_{jk}.                         \tag{1}
\]
Divide by the nonzero factor omega^((8+r+s)t). As t ranges from
0 to 15, the polynomial
\[
 \sum_{h=1}^{13}Z^h
 \sum_{\substack{j<k\\j+k=h}}
 (c_{j-r}c_{k-s}-c_{k-r}c_{j-s})p_{jk}                 \tag{2}
\]
vanishes at the sixteen distinct elements Z=omega^(-t). Its degree
is at most thirteen, so the polynomial root bound makes each
coefficient zero. Thus for each h we obtain a separate system
\[
 B_h(p_{jk})_{j+k=h}=0,
 \qquad (B_h)_{(r,s),(j,k)}
       =c_{j-r}c_{k-s}-c_{k-r}c_{j-s}.                 \tag{3}
\]
Rows are ordered (0,1),(0,2),(0,3),(1,2),(1,3),(2,3), numbered
0,...,5. Columns are the pairs j<k with j+k=h, in lexicographic
order. The column counts for h=1,...,13 are
1,1,2,2,3,3,4,3,3,2,2,1,1, summing to 28.

The following small exact minors prove that each B_h has full column
rank over F_97. All displayed integers are residues modulo 97. The
eight possible generators and the ascending coefficients of P_0 are:

| omega | c_0 | c_1 | c_2 | c_3 | c_4 |
| --- | --- | --- | --- | --- | --- |
| 8 | 96 | 9 | 46 | 42 | 1 |
| 12 | 96 | 75 | 12 | 10 | 1 |
| 18 | 96 | 66 | 91 | 37 | 1 |
| 27 | 96 | 60 | 6 | 31 | 1 |
| 70 | 96 | 8 | 28 | 61 | 1 |
| 79 | 96 | 36 | 69 | 89 | 1 |
| 85 | 96 | 55 | 51 | 88 | 1 |
| 89 | 96 | 87 | 85 | 22 | 1 |

Each listed omega satisfies omega^16=1 and omega^8=-1. They are
distinct and exhaust the roots of X^8+1, so exhaust the order-sixteen
elements of F_97. The coefficients are obtained by multiplying the
four displayed linear factors; thus this table does not assume a
choice of error weights.

In the next table, take exactly the indicated rows of B_h and all
its columns. Determinants use increasing row and column order.

| h | Rows | omega=8 | 12 | 18 | 27 | 70 | 79 | 85 | 89 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 2 | 0 | 88 | 22 | 31 | 37 | 89 | 61 | 42 | 10 |
| 3 | 0,1 | 5 | 76 | 69 | 22 | 87 | 20 | 4 | 16 |
| 4 | 0,1 | 17 | 66 | 62 | 65 | 2 | 16 | 71 | 73 |
| 5 | 0,1,2 | 52 | 66 | 89 | 5 | 25 | 29 | 87 | 92 |
| 6 | 0,1,2 | 80 | 58 | 75 | 12 | 62 | 73 | 40 | 52 |
| 7 | 0,1,2,3 | 10 | 5 | 92 | 8 | 68 | 72 | 45 | 31 |
| 8 | 0,1,2 | 72 | 21 | 5 | 92 | 13 | 84 | 25 | 76 |
| 9 | 0,1,2 | 8 | 74 | 28 | 8 | 38 | 67 | 71 | 70 |
| 10 | 1,2 | 55 | 87 | 60 | 66 | 36 | 8 | 9 | 75 |
| 11 | 2,3 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 12 | 4 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 13 | 5 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |

These are determinants of matrices of size at most four, with every
entry specified by (3) and the coefficient table. For example h=2
has the single column (0,2); row (0,1) gives c_0 c_1=-c_1,
which gives its displayed row. For h=7 the columns are
(0,7),(1,6),(2,5),(3,4), and the chosen four-by-four matrix is
\[
 \begin{pmatrix}
 0&0&c_2&c_3^2-c_2\\
 0&c_1&c_2c_3&c_3c_2-c_1\\
 c_0&c_1c_3&c_2^2&c_3c_1-c_0\\
 0&c_0&c_1c_3-c_0&c_2^2-c_3c_1
 \end{pmatrix}.
\]
This also specifies the largest minors without any large-matrix
rank oracle. Every determinant in the table is nonzero. It remains
nonzero in F, because the embedding F_97 into F is injective.
Consequently all the systems (3) have trivial kernel over F; they
force all 28 p_jk to be zero, contradicting independence of u,v.
Together with the first case, this proves the conclusion.

The exact arithmetic is reproducible by
`python3 scripts/cyclic-0125/alternating_obstruction.py`.
Its full certificate is
`scripts/cyclic-0125/alternating-obstruction-result.json`, with complete
B_h matrices, chosen minors, determinants, and original 96-by-28
necessary-condition matrices. The `/proof_certificate` field contains
the complete compact table data used above. Minors are evaluated by
the Leibniz formula. An independent Gaussian-elimination check on the
original matrices gives rank 28 for all eight generators; direct
multiplication at the sixteen support root sets also checks the
coefficient scaling in (1). No failures occurred. These checks cover
the finite coefficient identities; the extension-field conclusion
comes from invertibility and the algebra above, not from sampling
weights or parameters in F_97.

L010 supplies the established RS/moment input; L025 supplies the
specified incidence family and disjoint pair. No new distance theorem
or decoding algorithm is reproved. The saved SPECIALIZE assessment
found no inspected theorem deciding this fixed family with unrelated
weights. This is local progress beyond those inspected conclusions,
not a claim of certified originality. Generic GM-MDS results and the
shifted-weight obstruction of L009 are not used as premises.

### Separate critical audit, October 5, 2026

The independent audit found no error in the proof or the two printed
tables. It reconstructed coefficients by elementary symmetric sums and
all 104 displayed determinants by recursive cofactor expansion, without
importing the certificate generator. It compared every entry of all
thirteen blocks for every generator and of the eight original 96-by-28
matrices against the complete saved certificate. All comparisons passed.

For a second construction, it formed the four-by-eight matrix whose
rows are the actual moment columns m(x)^transpose for each A_t, computed
its nullspace, and used pairs of those nullspace vectors as annihilating
rows. The resulting alternating-condition matrices again have rank 28
for all eight generators. Each nullspace was checked to have dimension
four and to agree with the row space of R_t. This construction checks
the rank obstruction without using the cyclic block separation.

The conceptual audit retained the following qualifications. The scalar
product of a coefficient row with m(x) has the extra factor x, so the
one-index moment offset is correct. Equation (1) is necessary even when
R_t v=0; no division by a parameter or a weight occurs. The polynomial
in (2) has degree at most thirteen over F itself, and its sixteen roots
remain distinct in any extension. Every nonzero determinant over F_97
remains nonzero there. No decomposability condition is needed after
all alternating coordinates vanish. Finally, a nonzero word supported
on four distinct nonzero evaluation points has nonzero syndrome by
column independence. This excludes span{u,v}=0 and makes the
one-dimensional intersection argument valid even for repeated parameters
or v=0. Thus no genericity, parameter-distinctness, finite-extension, or
full-orbit assumption was introduced into the stronger conclusion.

Reproduce the audit with
`python3 scripts/cyclic-0125/audit_alternating_obstruction.py`.
The complete independent certificate is
`scripts/cyclic-0125/alternating-obstruction-audit.json`; its summary
reports 104 of 104 nonzero minors, ranks 28 of 28 for all eight
generators, 743 checks, and no failures. It stores all reconstructed
blocks, moment nullspaces, independent constraint matrices and their
reductions. This is verification of the existing fixed-family result,
not a new theorem or a stronger global bound. The audit changes no
mathematical premise or dependency of L026.

### Arbitrary-label matrix and bounded test, October 5, 2026

For this paragraph only, let lambda: Z/16Z -> H be any bijection,
and put E_t={lambda(t+a): a in {0,1,2,5}}. No assertion that all such
labelings have rank 28 is made. For any four-element E subset H,
write P_E(X)=prod_(x in E)(X-x), and take the four coefficient rows
of X^r P_E(X), 0<=r<4, in degrees 0,...,7. Their dot products with
m(x) are x^(r+1)P_E(x). Their highest nonzero degrees are successively
4,5,6,7, with leading coefficient one, so they are independent. L010's
four independent moment columns have a four-dimensional annihilator;
these rows therefore form a basis of that annihilator. Their six pairwise
alternating rows have entries a_j b_k-a_k b_j, in lexicographic j<k
order, and annihilate (p_jk) whenever u+gamma_t v lies in span{m(x):x in E_t}.
This necessary equation does not divide by a parameter or error weight.

This rank question is basis independent. Each new annihilator basis is
obtained by an invertible four-by-four matrix S. Bilinear expansion
expresses its six alternating rows as the second compound matrix of S
times the original six rows. Applying the compound matrix of S^(-1)
reverses this transformation; hence the block row space, and therefore
the full stacked row space, is unchanged. The same reasoning holds over
every extension. The disjoint pair E_0,E_6 is preserved by every bijection,
so the dependent-direction exclusion in the proof above also applies.
No symmetry reduction of the labeling list is assumed.

A bounded exact falsification test checked 4096 explicitly recorded,
distinct bijections. All have rank 28, certified by a nonzero determinant
of 28 selected rows of their 96-by-28 matrices. The complete list consists
of eight cyclic generator controls, 960 single transpositions of those
controls, 120 additional affine exponent orders, 380 additional bit orders,
28 additional block orders, 32 numerical orders, and 2568 seeded shuffles.
Duplicates were removed in the stated order; the seed is 20261005042 and
the exact permutations, origins and ordering are in the certificate.
No listed transformation is used as a rank-preserving symmetry.

Reproduce the search with
`python3 scripts/cyclic-0125/arbitrary_label_rank.py` and its independent
complete check with `python3 scripts/cyclic-0125/audit_arbitrary_label_rank.py`.
The certificates are `scripts/cyclic-0125/arbitrary-label-rank-result.json`
and `scripts/cyclic-0125/arbitrary-label-rank-audit.json`. For each labeling
the first stores all sixteen support keys, the selected row indices and
nonzero minor determinant; it stores the complete six-by-28 block for every
used support, so every full matrix is specified. All 1820 possible
four-element subsets of H occur among those blocks. The audit independently
reconstructs each polynomial by elementary symmetric sums, checks every
block entry and agreement with the nullspace of the actual moment columns,
and checks every selected maximal minor by column pivoting and Schur
complements, independently of the search's row elimination. It also
reconstructs full nullspace-basis matrices for the eight controls. All
4096 minor checks and 1820 moment-nullspace checks pass; its 27784 checks
report no failures.

For each listed labeling these exact nonzero minors survive extension,
and thus supply the same obstruction as in the proof. The list is not
exhaustive over all bijections; seeing every individual support block does
not exhaust their simultaneous arrangements. No deficient labeling was
found, no decomposability or locator existence was established, and no
universal arbitrary-label exclusion or improvement of the global
11/q–16/q interval follows. This is EXPLORATION using the saved EXPLORE
assessment, not certified novelty or a complete solution. The full
target remains open after this bounded test.

## Mathlib

Coverage of this exact fixed-family exclusion, its alternating-coordinate
systems, and the displayed finite minors in Mathlib is **not checked**.
Coverage of the arbitrary-label matrix construction and bounded certificates
is also **not checked**.
No full matching theorem, absence claim, or Lean verification is
asserted. L010's existing Mathlib qualifications still apply to its
supporting algebra; the elementary linear algebra and polynomial
root argument needed here are given explicitly above.
