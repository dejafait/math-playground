# L031 — Four-support realizability and two fixed subgroup tests

## Hypotheses

Use C001a's E=F_65537, F=F_(65537^28), order-1024 subgroup H of E^*,
k=64 and integer m>=1. Let C, the six sets U_ij (1<=i<j<=4), and
four sets W_i be mutually disjoint subsets of H, with |C|=60 and
|U_ij|=|W_i|=2. Define

\[
 S_i=C\cup W_i\cup\bigcup_{j\ne i}U_{\min(i,j),\max(i,j)}.
\]

Thus |S_i|=68 and S_i intersect S_j=C union U_ij. Realizability means
four pairwise distinct m-tuples P_i of polynomials over F of degree
strictly less than 64, and one center Y:H -> F^m, with P_i=Y on S_i.
Additional agreements are allowed. The original messages and center
need not descend to E.

Let V=E[X]_<4^3, with coordinates the coefficients of g_1,g_2,g_3 in
ascending degree order, and put g_4=0. For each edge ij, D_ij is the
4-by-12 coefficient matrix of g_i-g_j. Let M be the 12-by-12 matrix
whose rows, in edge order 12,13,14,23,24,34 and then point order within
each U_ij, are

\[
 (1,x,x^2,x^3)D_{ij},\qquad x\in U_{ij}.
\]

All signs are in E; in particular a difference block has +1 and -1,
not two +1 entries. Put K=ker_E M and r=rank_E M.

## Conclusion

For any, and hence every, m>=1, the supports are realizable if and only if
all six of the following equivalent conditions hold:

\[
 D_{ij}|_K\ne0
 \quad\Longleftrightarrow\quad
 \operatorname{rank}_E\begin{pmatrix}M\\D_{ij}\end{pmatrix}>r.
 \tag{1}
\]

When (1) holds there is already a scalar realization over E. Every rank
in (1) is unchanged on extending E to F. Mere singularity of M is not
the criterion.

For h=3^64 mod 65537=19139, assign U_ij, in the stated edge order, by
r=0,...,5. Consecutive pairs {h^(2r),h^(2r+1)} give rank M=12, so are
not realizable. Antipodal pairs {h^r,-h^r} give rank M=10 and all six
augmented ranks 12, so are realizable. Both conclusions hold for any
admissible C,W_i and for every m. The criterion supplies a labeled local
restriction; no list-size bound or improvement of 955<=t_star(m)<=957
follows here.

## Proof

**Imported framework and specialization.** Use Alrabiah, Guruswami and
Li, *Randomly punctured Reed–Solomon codes achieve list-decoding capacity
over linear-sized fields*, [arXiv:2304.09445v3](https://arxiv.org/pdf/2304.09445v3),
26 July 2023, Definition 2.5 and Lemma 2.7, printed pp. 7–8: the signed
reduced intersection matrix and the necessary kernel obtained by
subtracting the last message. This framework works over arbitrary finite
fields. Common-root division is the same factor-theorem step used in
L020, sourced there to Shangguan–Tamo,
[arXiv:1911.01502v1](https://arxiv.org/pdf/1911.01502v1),
Lemma 4.3, printed pp. 11–12. Their Section 5 unsigned four-way matrix
assumes characteristic two and is not used.

The prior [SPECIALIZE assessment](../drafts/literature/2026-10-07-four-support-realizability.md)
requires the fixed-domain converse and all distinctness and tuple
qualifications. Those are the differences justified below. We do not
reprove or apply generic or random-domain full-rank theorems to H.

**Necessity, including tuple width.** Put G=product_(c in C)(X-c),
a monic polynomial of degree 60. In any realization, for each row a,
P_i,a-P_4,a vanishes on all 60 distinct core points, so it equals G g_i,a
with deg g_i,a<=3 (allowing zero). Put g_4,a=0. On U_ij, G is nonzero,
and P_i,a-P_j,a vanishes; hence g_i,a-g_j,a vanishes there. Thus the
12-vector v_a of reduced coefficients belongs to ker_F M. Distinctness
of P_i and P_j says that at least one row has D_ij v_a nonzero. No single
coordinate projection is presumed to preserve all pairwise distinctions.

Rank is the largest order of a nonzero minor; every minor of M and each
augmented matrix lies in E, and its vanishing is unchanged in F. If
D_ij vanished identically on K, adding its equations would leave the
kernel dimension, hence rank, unchanged over E, and therefore over F.
The inclusion ker_F [M;D_ij] subset ker_F M together with equal
dimensions would force D_ij to vanish on the latter, contradicting the
row just found. This proves all six conditions. More generally this
dimension argument proves the equivalence in (1): a nonzero restriction
strictly reduces kernel dimension. It also justifies extension descent
of the test without assuming that given messages descend.

**One scalar witness for six distinctions.** Suppose (1). Then d=dim_E K
is at least one. Each N_ij=K intersect ker D_ij is a proper E-subspace
of K, so has size at most 65537^(d-1). Their union has size at most
6*65537^(d-1)<65537^d=|K|. Choose v outside this union. Its reduced
polynomials g_1,g_2,g_3,g_4=0 are pairwise distinct. Define f_i=G g_i.
Every f_i has degree at most 63, and every difference f_i-f_j is nonzero
because G is nonzero and E[X] has no zero divisors. L001's root bound
ensures their evaluation vectors on 1024 points are distinct.

On S_i prescribe Y=f_i. Multiple prescriptions agree: on C all f_i
vanish, and on U_ij their difference is G times a polynomial vanishing
there, by Mv=0. There are no other intersections. Set Y=0 off the union.
This constructs one scalar center over E. Append zero rows to obtain a
realization over F for each m>=1. This proves sufficiency, including
private points and extra agreements. Necessity and sufficiency together
establish the asserted independence from m and the choices of C,W_i.

**The two prescribed tests.** The domain in the certificate is
(h^a)_(a=0)^1023. Exact exponentiation gives h^1024=1 and h^512=-1.
Since every divisor of 1024 is a power of two, h has exact order 1024.
As in L020, its powers comprise H. The consecutive point exponents are
0,...,11, and the antipodal exponents are r,r+512 for r=0,...,5; in both
cases the twelve points are distinct. The certificate chooses the first
60 unused domain points for C, then the next eight in pairs for W_i.
There are 1012 unused points, so all choices exist and are disjoint.

For antipodal pairs, the inspected ordered pairs are

```text
(1,65536), (19139,46398), (15028,50509),
(44536,21001), (282,65255), (23164,42373).
```

The exact kernel has basis

```text
b0=(53800,0,58839,0, 32073,0,15029,0, 46060,0,1,0),
b1=(0,53800,0,58839, 0,32073,0,15029, 0,46060,0,1).
```

The scalar witness b0 yields reduced messages

\[
 g_1=53800+58839X^2,\quad
 g_2=32073+15029X^2,\quad
 g_3=46060+X^2,\quad g_4=0.                 \tag{2}
\]

For the six edges, their (constant,quadratic) difference coefficients are

```text
(21727,43810), (7740,58838), (53800,58839),
(51550,15028), (32073,15029), (46060,1).
```

Each is nonzero. Substitution at both points of its prescribed pair gives
zero modulo 65537. Consequently the difference is a nonzero scalar
multiple of that pair's monic quadratic, and the message difference has
exactly the 62 roots C union U_ij in H. The certificate verifies these
equalities at every domain point. In this scalar witness every nonzero
message has degree 62. The selected-center rule above, with value zero
off the support union, gives agreement counts 68,68,68,1012. To see the
last count, the support union has 60+12+8=80 points; message 4 agrees
at its 68 selected points and the 944 outside points. For the other
messages, roots relative to zero and each pairwise equality set have
already been exhausted by the prescribed intersections, so they gain
no other agreements.

For consecutive pairs the signed matrix row reduction is the 12-by-12
identity. All six augmented ranks are 12, and K={0}. Thus no nontrivial
reduced messages exist even over F, and necessity rules out any tuple
realization. This calculation makes no universal assertion about other
choices of six pairs. In particular the antipodal witness disproves
universal exclusion of the incidence pattern.

**Full finite certificate.** Run
`python3 scripts/finite-support/four_support_rank.py`. It writes
`scripts/finite-support/four-support-rank-results.json`. This contains
the full domain, both sets of core/private/pair points and supports,
both signed matrices, all six coefficient maps and augmented matrices'
reductions, every elementary row operation, transformation matrices,
RREFs, pivots, full kernel bases, and all scalar witness polynomials,
message/center evaluations, agreement sets and pair equality sets.
Arithmetic is exact modulo 65537; no floating-point rank is used.

For every reduction the verifier replays the invertible elementary
operations and separately multiplies the saved transformation by the
original matrix; both equal the entire saved RREF. Pivot columns and
zero tails certify its rank. Kernel vectors are checked against every
row, and their free-coordinate identity and rank-nullity certify a basis.
Thus the rank claims have complete finite evidence, including rank ten's
zero rows. Every intersection, center prescription, strict degree and
pairwise distinction is checked. The complete consecutive matrix,
antipodal basis, six restricted maps and reduced witness were inspected;
the verifier checks the full remaining identities, not sampled entries.
No failures were reported.

The script's witness search is also bounded rigorously: for a basis
b_0,...,b_(d-1), try v(t)=sum t^a b_a. For each nonzero D_ij|K, at least
one coefficient coordinate of D_ij v(t) is a nonzero polynomial of degree
at most d-1. At most 6(d-1)<=66 parameters are excluded across all edges,
so testing 6(d-1)+1 distinct base-field values suffices. In the only
realizable prescribed case, d=2 and t=0 already succeeds. This algorithm
is only a way to exhibit the scalar witness; the union proof gives (1).

**Independent critical audit (2026-10-07).** The audit retains the proof
and both conclusions without correction. In necessity, distinct tuples
give a possibly different witnessing row for each pair; rank invariance
descends each noncontainment separately. It never presumes a common row
or projects a tuple to a scalar. In sufficiency, the strict inequality
6*65537^(d-1)<65537^d applies because each of the six kernels is proper;
if K were zero, (1) would already fail. Multiplication by the degree-60
core factor preserves every nonzero difference and leaves degree at most
63. The mutual disjointness assumptions ensure that the core and six
pair sets exhaust every possible conflicting center prescription. These
arguments hold for every admissible core/private choice, whereas the
saved full evaluations use the stated deterministic choices.

Run `python3 scripts/finite-support/audit_four_support.py` for the independent
finite audit. It reads the original certificate without changing it or
importing its generator. It writes
`scripts/finite-support/four-support-audit-results.json`, retaining the
original certificate's SHA-256, the reconstructed domain, both entire
configurations and signed matrices, independently computed echelon forms,
all reconstructed witness data, and all 208 named check outcomes.
Independent forward elimination chooses the last available pivot, does not
normalize it, and clears only below it. This confirms ranks 12 and 10
and all twelve augmented ranks 12. Separately, all 14 saved reductions
are checked by replaying every invertible operation on both the original
matrix and the identity, comparing the full saved transformation and
RREF, and multiplying the transformation by the original matrix. Exact
pivot columns, leading positions, zero tails, all kernel equations and
the complete free-coordinate identity certify every saved kernel basis.

The audit reconstructs every coefficient of the four antipodal messages,
all 4096 message evaluations, all 1024 center values and owner sets,
every agreement set and all six equality sets. The exact message degrees
are 62,62,62 and the zero polynomial, below the required 64; all six
differences are nonzero multiples of the prescribed pair quadratics.
The full six restricted maps, each with two kernel-basis columns, agree
with the saved evidence. The 208 checks report no failures. This verifies
the existing local input; it adds no new configuration, counting bound,
unsafe list or claim beyond the assessed source specialization.

**Limitations and downstream use.** A list with selected supports
containing the forbidden consecutive pattern is impossible, providing
a potential additional labeled support constraint. The allowed antipodal
case prevents replacing (1) by universal incidence exclusion. No bound
on the number of supports avoiding these forbidden configurations has
been proved, and no effect on L030's independent families or cross-core
compatibility has been established. The witness gives only four known
list members, far below C001a's threshold >2^320. Arbitrary-center safety
at 68 or 67 agreements, quantitative extremal transfer, the full SDP and
ABF equivalence remain unresolved. This is a local REPRODUCTION of an
assessed framework with its required finite specialization, not a claim
of mathematical novelty beyond the sources checked.

## Mathlib

Full matching four-support criterion, tuple-to-scalar implication and
fixed-subgroup certificates: **not checked**. Supporting finite-union,
polynomial factor/root and extension-rank results: **not checked**.
Unknown availability is not evidence of absence. The precise primary
inputs and the reason for this specialization are given above.
