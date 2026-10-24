# L116 — Maximal order and field discriminant of the marked octic

## Hypotheses

Work in the entire field K=Q[theta]=Q[t]/(F) identified in audited L115,
where

    F(t)=275t^8−2860t^6+6930t^4−3564t^2+243.

Thus F is primitive and irreducible of degree eight over Q. The generator
theta is not assumed integral. No class group, unit group, local point
image or rational-point completeness is assumed. This is the marked
octic of L113–L115, not L095's different octic.

## Conclusion

Let B be the following matrix, whose column j is the coefficient vector
of b_j in the ordered Q-basis (1,theta,...,theta^7), indexed from zero:

```text
 1  1/2  -571/4  -2859/8  -14815/32  -14783/64  -6273/128  -6145/256
 0 55/2       0  -2035/8          0    2475/64          0    341/256
 0    0    55/4    275/8    1045/48    1045/96    385/384    385/768
 0    0       0    275/8          0   1045/288          0   385/2304
 0    0       0        0     275/96    275/192  -385/3456  -385/6912
 0    0       0        0          0    275/576          0 -385/20736
 0    0       0        0          0          0   275/3456   275/6912
 0    0       0        0          0          0          0  275/20736
```

Then O_K has Z-basis b_0,...,b_7, and its signed field discriminant is

    disc(K)=6818950876320000=2^8 * 3^7 * 5^4 * 11^7.

For the nonmonic equation order R_F described below,

    [O_K:R_F]=6340338096537600=2^32 * 3^10 * 5^2.

This certifies only the maximal ring and its discriminant. It computes
neither supported square classes nor rational points or integer solutions.

## Proof

### Imported general results and applicability

The prior SPECIALIZE assessment, saved before this calculation, is
`drafts/literature/2026-10-22-marked-octic-maximal-order.md`.
Import H. W. Lenstra, Jr., *Algorithms in algebraic number theory*,
Bull. Amer. Math. Soc. (N.S.) **26** (1992), 211–244,
[DOI 10.1090/S0273-0979-1992-00284-7](https://doi.org/10.1090/S0273-0979-1992-00284-7),
the inspected [arXiv:math/9204234v1](https://arxiv.org/pdf/math/9204234v1),
1 April 1992, Sections 2.4–2.5, 2.7, 2.10 and Theorem 4.5 with its
algorithmic proof on manuscript pp.17–18. This supplies exact order and
lattice arithmetic, discriminant-index control, and the all-prime
radical/multiplier algorithm, including small primes.

Also import I. Del Corso, R. Dvornicich and D. Simon, *Decomposition of
primes in non-maximal orders*, Acta Arith. **120.3** (2005), 231–244,
[published primary PDF](https://www.impan.pl/shop/en/publication/transaction/download/product/82018),
Section 2 pp.232–234 (nonmonic order and Proposition 4's discriminant)
and Section 4, Proposition 9 p.238 (radical/multiplier maximality).
The following are the exact imported statements used here.

For primitive irreducible F=a_0 t^n+...+a_n over Z, the lattice with
basis 1,T_1(theta),...,T_(n−1)(theta), where
T_i=a_0 theta^i+...+a_i, is an order R_F of discriminant disc(F).
For any order A in K and rational prime p, let I be the inverse image
of the nilpotents of A/pA. Its multiplier ring

    M={b in K : bI subset I}

is an overorder of A. It equals A exactly when A is p-maximal, meaning
p does not divide [O_K:A]. Otherwise [M:A] is a positive power of p.
The nilpotents are the kernel of x -> x^(p^k) for p^k>=n. Lenstra's
distinct second kernel computes pM/pA as the kernel of

    A/pA -> End_Fp(I/pI),  a -> (multiplication by a).

Repeated strict enlargements terminate within
floor(v_p(disc(A_initial))/2) steps. Finally
disc(A)=disc(K)[O_K:A]^2, so a complete factorization of an initial
order discriminant bounds all possible index primes.

These are imported algorithms and theorems, not new general results.
Their hypotheses hold: Z is Dedekind, L115 establishes the unchanged
primitive irreducible F, and the quotient has degree eight in
characteristic zero. Neither normality nor a restriction p>8 is needed.
The only work beyond citing them is the exact instance evidence below;
no unreviewed alternative maximality criterion or field identification
is used. R_F, rather than Z[theta], handles the nonmonic polynomial.

### Starting order and complete index-prime coverage

Write the descending coefficient list as
(a_0,...,a_8)=(275,0,−2860,0,6930,0,−3564,0,243).
The starting basis consists of 1 and T_i for 1<=i<=7 exactly as above.
In monomial coordinates its column i has coefficient a_(i−j) in row j
for 0<=j<=i and zero below; column zero is 1. Its determinant is 275^7,
so it is full rank. The certificate records this complete matrix and its
inverse, the coordinates of one, all 64 products, all eight traces and
the complete trace Gram matrix. The product coordinates and one are
integers; this checks order closure directly as well as applying the
nonmonic-order theorem. A finite full-rank unital Z-subring is integral,
by the monic characteristic polynomial of multiplication by each element.

The determinant of its computed trace Gram matrix is the positive integer

    D_0=274121055903156976389282167681421882163200000000
       =2^72 * 3^27 * 5^8 * 11^7.

Successive exact division by 2,3,5,11 leaves remainder one, with the
displayed exponents; trial division through each square root proves
these four numbers prime. This factorization therefore covers every
possible index prime, including the leading-coefficient primes 5 and 11.
As a redundant independent cross-check, L114's disc(11F) equals
11^14 D_0, as required by the degree-eight polynomial discriminant
scaling. That polynomial discriminant is never used as the field
discriminant. The computed order trace determinant and its complete
factorization suffice for coverage.

### Exact radical and multiplier certificates

All order bases stay inside the original monomial-coordinate field.
For each current order A use its certified integral multiplication table.
At p=2,3,5,11 respectively, the chosen p^k are 8,9,25,11.
The columns of the complete 8-by-8 Frobenius matrix are the powers of
the eight order-basis vectors, reduced modulo p. The power map is
F_p-linear. Its complete kernel V is obtained by invertible row
operations; the certificate retains every operation, reduced matrix,
pivot and free column, and every normalized kernel vector.

Let J express an integral basis of I in the current A-basis. For each
free column j of the Frobenius matrix, column j of J is its normalized
kernel vector; for every pivot column j it is p e_j. Hence J reduces
into V, contains p Z^8 and has determinant of absolute value
p^(8−dim V). These facts establish both inclusions in the inverse-image
lattice, not just a subset of the radical. J and its rational inverse
are stored and independently checked.

If C_i is multiplication by the i-th A-basis vector, then

    H_i=J^(-1) C_i J

is integral. Its reduction is the action on I/pI. Stack all entries of
H_i into column i of a 64-by-8 matrix H over F_p. The complete kernel
U of H is computed with the same full certificates. Form its normalized
inverse-image lattice P just as for J, and put E=P/p. The imported
kernel formula gives M with basis transform E. Explicitly,
pM subset A since p belongs to I; a/p belongs to M precisely when
aI subset pI. Thus the complete second kernel, with the codomain
I/pI rather than A/pA, recovers the whole multiplier ring.

The certificate checks E^(-1) integral (A subset M), pE integral,
the inverse-image determinant and both lattice inclusions. It checks
that every E-basis vector acts integrally on I. Each strict new basis
B_new=B_old E is independently certified closed under all products and
containing one. Both reverse coordinate matrices and

    disc(A)=[M:A]^2 disc(M)

are checked exactly. The basis, full multiplication table, trace Gram
matrix and discriminant are retained at every one of the sixteen orders.
No floating-point reduction, guessed prime decomposition, trace-radical
approximation or assumed polynomial-order maximality enters these steps.

The complete sequential index data are:

| p | Strict indices [M:A], in order | Terminal Frobenius rank | Terminal multiplier rank | Strict steps / cap |
| --- | --- | --- | --- | --- |
| 2 | 2,4,8,16,32,64,128,4,4 | 2 | 8 | 9 / 36 |
| 3 | 3,9,27,81 | 3 | 8 | 4 / 13 |
| 5 | 5,5 | 4 | 8 | 2 / 4 |
| 11 | none | 1 | 8 | 0 / 3 |

There are nineteen sequential radical/multiplier checks, fifteen strict
steps and four terminal checks. Every cap follows from D_0's valuation;
none is enlarged. The full chain and order identities are linked in the
certificate, with no skipped order or unused order record.

### Final maximality, basis and signed discriminant

After the sequential computation, repeat the complete radical/multiplier
calculation at all four primes on the same final basis B displayed in
the conclusion. Their Frobenius ranks are (2,3,4,1), and all four
64-by-8 action matrices have rank eight. In each case their reduced
matrix has I_8 as its first eight rows and zeros thereafter. Their
kernels are zero, so all four multiplier rings equal the final order.
The imported criterion makes this order p-maximal at every possible
index prime. Every other prime is excluded by the complete initial
discriminant factorization and containment R_F subset A_final.
Consequently A_final=O_K.

The complete final trace Gram matrix is

```text
    8      4    -856   -2144   -2920   -1456    -324   -158
    4  15732    -428  -37372   -1460   42832    -162   2726
 -856   -428  103208  258448  348740  173942   38364  18754
-2144 -37372  258448  864992  873310  365788   96072  43994
-2920  -1460  348740  873310 1180640  588860  130140  63610
-1456  42832  173942  365788  588860  421412   64908  40306
 -324   -162   38364   96072  130140   64908   14376   7026
 -158   2726   18754   43994   63610   40306    7026   4028
```

Its exact determinant is the signed discriminant in the conclusion.
The initial-in-final matrix is integral and its determinant has absolute
value 2^32 * 3^10 * 5^2, agreeing with the product of all strict indices.
The identity D_0=(2^32 * 3^10 * 5^2)^2 disc(K) is checked independently.
Successive division of the final determinant has exponents (8,7,4,7)
at (2,3,5,11) and residual cofactor one. This preserves the entire field
and sign; no selected local factor or altered generator is substituted.

### Reproduction and independent arithmetic replay

Run from the notebook directory:

    python3 scripts/pair-genus-two/marked_octic_maximal_order.py
    python3 scripts/pair-genus-two/replay_marked_octic_maximal_order.py

The producer saves all evidence to
`scripts/pair-genus-two/marked-octic-maximal-order-certificate.json`.
It saves intermediate orders as it proceeds and preserves exact failures
if an exception occurs. This completed run has no arithmetic failures.
All relevant prime bounds and actual iteration counts are displayed in
the table above; no backend number-field package is used.

The separate replay imports no producer implementation. Its full evidence
is `scripts/pair-genus-two/marked-octic-maximal-order-replay.json`.
It identifies the source certificate by SHA-256 and rebuilds all order
products by Horner multiplication and companion shift/reduction, instead
of the producer's monomial-product convolution. It recomputes every trace
Gram determinant by a subset Laplace expansion, rather than the
producer's fraction-free elimination. It reconstructs every Frobenius
matrix by repeated multiplication, rather than binary powering; verifies
every saved invertible row operation; and independently computes ranks
by incremental column-space elimination. Nullspace equations, normalized
free-coordinate independence and rank/nullity prove kernel completeness.

For both kinds of inverse-image lattice, the replay checks inverse
identities, integrality, reduction into the kernel, containment of pA
and the exact determinant. These certify equality with the full inverse
image. It recomputes every conjugated action matrix, the entire joint
map, multiplier-basis actions, linked forward/reverse transforms,
strict indices, discriminant identities and source caps. It checks the
complete initial and final prime-division chains and every final check
on the same basis. All 1,331 comparisons pass, with zero failures;
actual/required final multiplier ranks are (8,8,8,8)/(8,8,8,8).
The full multiplication tables and matrix data are consumed by replay,
not inferred from producer flags or bounded previews.

This is a REPRODUCTION specialization of known algorithms and local
progress on a ring prerequisite, without claiming a new general theorem
or progress beyond those sources. The calculation's arithmetic replay
was followed by the separate critical audit below. Supported units/classes, class-group
two-torsion, complete local images, points on surviving covers,
degree-nine distinguished-root recovery, compatible remaining factors,
both L095 integer systems and the minus-eleven route remain unresolved.
The known rational infinity points continue to preclude an empty
fake-Selmer-set shortcut. Beal remains IN_PROGRESS with no complete
candidate argument.

### Separate critical audit, 2026-10-23

The separately approved audit assessment is
`drafts/literature/2026-10-23-marked-octic-maximal-order-critical-audit.md`.
The audit passes without changing the basis, discriminant or argument.
It uses audited L115's entire field, not an assumed irreducible factor
of a different polynomial. The only direct lemma input remains L115:
the L114 discriminant comparison is redundant, and the original marked
geometry is not a premise of the maximal-ring assertion.

The nonmonic order matches the cited T_i construction coefficient by
coefficient; no integrality of theta is assumed. Every stored inverse,
unit coordinate and all 64 basis products in each of the sixteen orders
were reconstructed exactly by the reviewed independent replay. Closure
and the unit show that these full-rank lattices are orders, so the
maximality and discriminant-index theorems apply at every step.

Both kernel computations were checked in full in all nineteen sequential
records and four final records. The Frobenius exponents 8,9,25,11 meet
the degree-eight threshold, including the small primes. Replayed invertible
row operations, independently computed column ranks, nullspace equations
and independent normalized free coordinates prove completeness, not just
that the proposed vectors lie in the respective kernels. For each radical
lattice J, reduction lands in the entire nilpotent kernel and pZ^8 is
contained in JZ^8. Its index p^rank(Frobenius) is the index of the full
inverse image; hence the inclusion is an equality. The identical
index-and-inclusion argument is checked separately for pE and the second
kernel, rather than reusing the radical kernel.

Crucially, the integral matrices J^(-1) C_i J act on I in its J-basis,
so reducing them computes the action on I/pI. The domain of their joint
map is A/pA: multiplication by pA is zero on I/pI. Since p is in I,
bI subset I implies pb in I subset A; conversely a/p preserves I exactly
when aI subset pI. Thus the full second kernel indeed gives pM/pA.
All eight multiplier generators preserve I, and the verified reverse
coordinate transforms and indices identify the full multiplier lattice.
This checks applicability of the imported criterion, without replacing it
by a trace-radical test or merely integral-looking candidate basis.

Every strict step and terminal case is used, with the stated index
sequences and caps. Complete exact prime-division chains leave cofactor
one for the initial discriminant, so 2,3,5,11 exhaust the possible index
primes. In particular neither leading-coefficient prime is omitted.
All four final records use order 15, with nilpotent dimensions 6,5,4,7
but zero multiplier kernels. Their full 64-by-8 reduced joint matrices
have the first eight rows I_8 and the remaining rows zero. The criterion
therefore proves maximality on this one final basis. Discriminant-index
control excludes every other prime, irrespective of uncomputed prime
decompositions or class data.

The full producer and replay implementations were inspected. The replay
imports no producer code; its Horner products, subset determinants,
successive-power computations and column-rank computations are independent
of the producer's corresponding implementations. The audit reruns that
reviewed replay, rather than claiming a third independent field engine.
It consumes all multiplication, action, kernel, lattice, trace and chain
data; all 1,331 comparisons pass with no failures. A separate Newton
power-sum check verifies every entry of all sixteen trace Gram matrices
directly from F/275, without using their multiplication tables: with
F/275=t^8+c_1 t^7+...+c_8 and s_k=Tr(theta^k), it uses s_0=8,
s_k+sum_(j=1)^(k−1)c_j s_(k−j)+k c_k=0 for 1<=k<=8, and
s_k+sum_(j=1)^8 c_j s_(k−j)=0 for 8<k<=14. Then
Tr(b_a b_d)=sum_(k,l=0)^7 B_(k,a) B_(l,d) s_(k+l).
The printed basis and Gram matrix match their complete stored values.
The signed determinant and total index agree with the conclusion;
all 35 additional audit comparisons pass with no failures.

Reproduce this audit from the notebook directory with
`python3 scripts/pair-genus-two/audit_marked_octic_maximal_order.py`.
Its full evidence is
`scripts/pair-genus-two/marked-octic-maximal-order-audit-certificate.json`
and `scripts/pair-genus-two/marked-octic-maximal-order-audit-replay.json`.
The original certificate and original replay are preserved; the fresh
replay binds the source bytes by SHA-256. Complete kernel vectors for all
23 records are also retained together in the audit certificate. This
critical audit confirms the ring prerequisite only, with all previously
stated class, local-image, rational-point and integer-lifting limitations.

## Mathlib

Full matching Mathlib coverage of this maximal-order instance or the
complete radical/multiplier certificate was not checked. General ring,
linear-algebra and discriminant support is not asserted to be a matching
formal theorem. No availability or absence claim is made.
