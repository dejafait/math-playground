# L022 — Selected triple SDP batch cannot certify the threshold

## Hypotheses

Use L021's instance and notation: n=1024, w=68, v=956, minimum binary
support distance d=10, and T=65537^28/2^128. For the RS interpretation,
use C001a's field, domain, strict degree bound and any m>=1, with closed
simultaneous column-Hamming balls. Select 68 agreement columns per list
candidate, as in L001 and L021; extra agreements are allowed.

Use only the following relaxation of the imported Schrijver constant-weight
SDP, with the normalization and coefficients in
[the primary source note](../foundations/04-constant-weight-triple-sdp-source.md):
all 68 basic pair-LP inequalities; both PSD families at (k,l)=(33,33)
on {33,34,35} and at (34,34) on {34}; both (0,0) principal matrices on
{0,5,6,68}; and the source scalar inequalities, permutation equalities and
distance zeros on all touched orbits and their permutation closure.
All pair variables are retained. No omitted triple variable is fixed to zero.
Block indices k,l are unrelated to the RS dimension 64.

## Conclusion

This relaxation has an exactly feasible rational primal assignment of
objective

\[
 M=\frac{U+1}{2},\qquad
 U=\frac{\binom{1024}{64}}{\binom{68}{64}},\qquad
 \frac{1383}{1000}<\frac{M}{T}<\frac{1384}{1000}.
\]

It therefore cannot supply an upper certificate at or below T. Even the
integer-floor code bound cannot suffice: floor(M)>T. This stops only the
specified batch as a threshold certificate. It does not determine its
optimum, the full Schrijver SDP, an actual constant-weight packing, an RS
list, or safety at 956 errors. C001a's 955–957 bracket is unchanged.

## Proof

**Imported bound and relaxation.** Schrijver, *New code upper bounds from
the Terwilliger algebra and semidefinite programming*, IEEE Trans. Inform.
Theory 51 (2005), 2859–2866,
[author manuscript](https://homepages.cwi.nl/~lex/files/codes.pdf),
Section III.B (64)–(67), gives both PSD families, scalar constraints and
objective. Kim–Toan, [arXiv:1212.3467v1](https://arxiv.org/pdf/1212.3467v1),
III.B (32)–(35) and III.C.2 (40), corroborates the formulas and the
pair-distribution normalization. These are imported known inputs; no
reproof is required. Here d is even, 0<10<136<=1024 and v=956. L001's
common-64-column uniqueness gives binary support distance at least 10
for the entire tuple list, uniformly in m. The objective includes its
diagonal 1, with no m exponent.

Every full feasible assignment satisfies the selected principal PSD and
scalar constraints. Dropping other constraints enlarges the feasible
region, so optimizing this relaxation would remain a valid upper-bound
method. A feasible point above T precludes a sufficient upper bound from
this relaxation alone, regardless of feasibility for the omitted blocks.
No triple count or actual code interpretation is required of that point.

**Exact assignment.** Let a_i^* (5<=i<=68) be L021's exactly specified
positive primal witness, and set

\[
 p_0=1,\quad p_1=\cdots=p_4=0,\quad
 p_i=\frac{a_i^*}{2\binom{68}{i}\binom{956}{i}}\ (i\ge5),
 \qquad \lambda=p_{68}>0.
\]

For each admissible touched orbit (i,j,t,s), put h=i+j-t-s. If any of
{i,j,h} lies in {1,2,3,4}, set y=0. If a distance is zero, set y=p_b,
where the sorted distances are (0,b,b); admissibility forces t-s=0 in
this repeated-word case. Otherwise put

\[
 y_{ij}^{ts}=p_i p_j p_h/\lambda.
\]

The assignment depends only on the distance multiset and t-s (indeed its
value in the distinct case does not depend on t-s). Thus it respects all
required equalities, without identifying different t-s variables in the
relaxation. It has y_(i,0)^(0,0)=p_i, correct distance zeros and y_00^00=1.
Only touched variables are used; the formula makes no extension-feasibility
claim. The retained variable count is 6978: 64 pair variables and 6914
unfixed distinct-triple variables, below the construction cap 20000.

**Complete exact finite verification.** The canonical rational values,
all 7093 orbit classes (including fixed classes), their 30856 actual
permuted orbit indices, all scalar rows, the 68 pair rows, every affine
block coefficient and every PSD congruence are saved in
`scripts/finite-support/selected-triple-sdp-results.json`.
The following identities and signs were exhaustively checked, rather
than inferred from a sampled orbit or approximate spectrum:

1. All 68805 orbit scalar slacks are nonnegative: y, p_i-y and
   1+y-p_i-p_j, for every ordered pair appearing in each class's
   permutation closure. The 68 pair slacks are nonnegative with minimum
   1/2. The total scalar/pair row count 68873 is below the cap 200000.
   Pair feasibility also follows directly by scaling L021: each original
   slack s becomes (1+s)/2.
2. The full coefficient dictionaries for the 17 upper-triangular entries
   in the three selected blocks contain 9101 nonzero aggregate entries.
   Each is the sum of the source integer products
   beta_(ij,k)^(t,68) beta_(ij,l)^(s,956) over its actual admissible orbits.
   The second-family coefficients use p_(i+j-t-s)-y, with all pair
   distances retained. Impossible multinomial orbits are absent.
3. For each rational matrix A, the saved rational, invertible matrix E
   satisfies E^T A E=D, with D diagonal and nonnegative. In index order,
   E is obtained by eliminating a positive pivot d=A_kk using
   column operations e_j -> e_j-(A_kj/d)e_k and the same row operations.
   A zero pivot is accepted only when every remaining entry in its row
   is zero. This provides a complete exact PSD certificate, including
   the singular case. The independent audit verifies every entry of
   E^T A E and det(E)=1; it does not trust the elimination's PSD flag.

The inspected certificates have the following pivot counts:

| Block | Family y: positive / zero | Family p_h-y: positive / zero |
|---|---:|---:|
| (33,33), {33,34,35} | 3 / 0 | 3 / 0 |
| (34,34), {34} | 1 / 0 | 1 / 0 |
| (0,0), {0,5,6,68} | 4 / 0 | 3 / 1 |

All positive diagonal entries are full rational numbers in the certificate
and the audit; their signs and identities were inspected in full. The
last matrix's zero pivot is the index-0 row: p_j-y_(0,j)^(0,0)=0 for
all its columns, so its whole residual row is exactly zero. Positive
pivots and invertible congruence give x^T A x>=0 for every real vector x:
write x=E z, then x^T A x=z^T D z. Hence these finite certificates establish
all six PSD constraints, including the zero-row obligation.

`audit_selected_triple_sdp.py` independently reconstructs admissibility
from nonnegative multinomial parts, every permutation, and every scalar
row. It uses factorial binomials and the literal full-u source summation
to rebuild beta coefficients, unlike the generator's restricted-u sums.
It reconstructs pair numerators by polynomial convolution, checks every
stored affine coefficient, evaluates all matrices afresh, and verifies
all congruence identities and signs. The independent output is
`scripts/finite-support/selected-triple-sdp-audit-results.json`.
Both generation and audit report no failures. These are finite rational
arithmetic proofs of feasibility, not evidence of a realizable packing.

**Objective and threshold.** L021 gives sum a_i^*=U-1. Thus the new
objective, including p_0, is M=1+(U-1)/2=(U+1)/2. Independent binomial
arithmetic and exact cross-multiplication give

```text
2^128*M-65537^28 = 278623344535004185563774417633448491259524856948687283912464936072396859308983357073255491132778488018151478995510523335052648532672511 > 0.
```

The ratio comparisons in the conclusion are also exact. U is even by
L021's displayed integer, so floor(M)=U/2. Subtracting 2^127 from the
positive displayed excess still leaves a positive integer. Consequently
2^128 floor(M)>65537^28, and integer rounding cannot repair the failed
threshold. Any correct upper certificate for every feasible point of
this relaxation must bound this particular M; hence none can certify
index 956. No conclusion on unretained constraints follows.

Reproduce from the notebook with
`python3 scripts/finite-support/selected_triple_sdp.py`, then
`python3 scripts/finite-support/audit_selected_triple_sdp.py`.
The prior SPECIALIZE assessment approved this exact batch. This is a
REPRODUCTION of a known SDP method and a local negative certificate,
without a claim of novelty beyond the sources checked.

## Mathlib

Full matching Schrijver constant-weight SDP and this finite rational
feasibility certificate: **not checked** in Mathlib. The primary theorem
is imported by the precise citation above. Exact congruence arithmetic,
rather than a presumed library theorem or numerical eigenvalues,
certifies the selected matrices.
