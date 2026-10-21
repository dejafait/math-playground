# L032 — Exact digit reduction of the small CRT target

## Hypotheses

For each integer L>=6 let M_L=2^(L+1)*3^(L+4)=162*6^L and let
r_L be the unique representative in [0,M_L) satisfying

\[
r_L\equiv47\pmod{3^{L+4}},\qquad
81r_L+97\equiv0\pmod{2^{L+1}}.                         \tag{1}
\]

The standard input is the named Chinese Remainder Theorem for coprime
positive moduli; 81 is invertible modulo 2^(L+1). No distribution,
equidistribution, convergence or least-nonconvergent-root hypothesis
is imposed. All occurrences of B below mean real B>=0.

## Conclusion

There are unique digits d_L in {0,1,2,3,4,5} such that

\[
r_{L+1}=r_L+d_L M_L.                                   \tag{2}
\]

Writing a_L=(r_L-47)/3^(L+4) and c_L=(81r_L+97)/2^(L+1),
the digit is specified exactly by

\[
a_L+2^{L+1}d_L\equiv0\pmod3,\qquad
c_L+3^{L+8}d_L\equiv0\pmod2.                           \tag{3}
\]

The following two assertions are equivalent:

1. For every B there are infinitely many integers L>=6 and integers n
   satisfying (1) with r_L replaced by n and
   4^L<n<=6^(L-B).
2. The digit sequence (d_L)_(L>=6) contains finite consecutive runs
   of zeros of arbitrarily large length.

Neither assertion is established here. This is an exact reformulation
and a bounded diagnostic, not a small-height theorem, a new clock
obstruction or a Collatz resolution.

## Proof

### Standard input and purpose of the specialization

Use [Ben Lynn, *The Chinese Remainder Theorem*, named theorem and
proof](https://crypto.stanford.edu/pbc/notes/numbertheory/crt.html),
as inspected in the prior assessment
`drafts/literature/2026-10-06-small-crt-coalescence-roots.md`.
Its coprime-modulus hypotheses hold for the powers of 2 and 3 in (1).
CRT is imported, not reproved. The specialization below is needed
because the moduli change with L and the target imposes two height
bounds; existence of a CRT class alone does not address those bounds.
The target's intended coalescence use is through L028, which is
motivation rather than a mathematical input to this arithmetic proof.

### Exact representative and digit recurrence

An explicit independent description is

\[
u_L=\bigl[-3904(3^{L+8})^{-1}\bigr]_{2^{L+1}},\qquad
r_L=47+3^{L+4}u_L,                                    \tag{4}
\]

where [x]_m is the least nonnegative representative modulo m.
Indeed 81*47+97=3904, so (4) satisfies both congruences.
It is in [0,M_L) because 0<=u_L<2^(L+1) and
0<47<3^(L+4). Uniqueness follows from CRT.

The class at L+1 is contained in the class at L and M_(L+1)=6M_L.
Consequently its least representative is one of
r_L+dM_L for 0<=d<=5, proving (2). Dividing its ternary
congruence by 3^(L+4) and its binary congruence by 2^(L+1)
gives (3). The coefficients 2^(L+1) modulo 3 and 3^(L+8)
modulo 2 are units. Thus (3) specifies exactly one residue modulo
6, hence exactly one permitted digit. The two carry updates are

\[
a_{L+1}=(a_L+2^{L+1}d_L)/3,\qquad
c_{L+1}=(c_L+3^{L+8}d_L)/2.                             \tag{5}
\]

These formulas retain unbounded carries; a bounded alphabet for d_L
does not by itself supply a finite-state recurrence or any distribution
law. With x_L=r_L/M_L, (2) gives

\[
x_{L+1}=(x_L+d_L)/6,\qquad 0<x_L<1.                    \tag{6}
\]

The digits are not eventually all zero. If they were, r_L would
eventually equal a fixed nonnegative integer r. Divisibility of r-47
by arbitrarily high powers of 3 would force r=47, while divisibility
of 81r+97=3904 by arbitrarily high powers of 2 is impossible.
Every maximal zero run is therefore finite.

### The infinite selection assertion implies long zero runs

Assume assertion 1. Since 6^(L-B)<=6^L<M_L, every admitted n is
the least representative r_L. Thus x_L<=6^(-B)/162.
Fix a positive integer k and use assertion 1 with B=k. Infinitely
many of its horizons have L>=6+k. Iterating (6) backwards k times
gives the exact identity

\[
x_L=6^{-k}x_{L-k}+\sum_{j=1}^k 6^{-j}d_{L-j}.           \tag{7}
\]

All terms are nonnegative. If any of those k digits were positive,
then x_L>=6^(-k), contrary to x_L<=6^(-k)/162.
Hence the k digits immediately preceding each such L are zero.
Since k was arbitrary, assertion 2 follows. This direction does
not discard the strict lower guard; it simply does not need it.

### Long zero runs supply both height guards

Assume assertion 2. Fix B and choose a positive integer k such that
162*6^(-k)<=6^(-B). Because every maximal run is finite and their
lengths are unbounded, infinitely many distinct maximal runs have
length at least k. Exclude the possible initial run starting at 6.
The remaining starting indices m are unbounded and satisfy
d_(m-1)>=1 and d_m=...=d_(m+k-1)=0. From (2),

\[
27\cdot6^m=M_{m-1}\le r_m=r_{m+k}<M_m=162\cdot6^m.     \tag{8}
\]

Set L=m+k. The upper bound in (8) gives
r_L<162*6^(L-k)<=6^(L-B). For the lower bound,

\[
\frac{27\cdot6^m}{4^{m+k}}
=\frac{27}{4^k}(3/2)^m\longrightarrow\infty.
\]

Therefore for all sufficiently large selected m one has
r_L>=27*6^m>4^L. There are infinitely many such m, proving
assertion 1 with n=r_L. This establishes the lower guard without
assuming it holds at the end of an arbitrarily long entire run:
we use only its first fixed k zeros, after a nonzero digit.

### Bounded diagnostic and stopping decision

`python3 scripts/small-crt/check.py` generates the roots by (3),
independently checks (4), and checks both original congruences and
the strict guarded representative

\[
n_L=r_L+M_L\left(\left\lfloor(4^L-r_L)/M_L\right\rfloor+1\right)
\]

at every integer 6<=L<=256. The complete exact records, all required
bounds and failures are in `scripts/small-crt/certificate.json`.
All 251 least representatives already satisfy r_L>4^L; no check
failed. At integer B=0, exactly L=56,86,255 meet the upper bound.
At B=1,2,3 none do in this range. The minimum r_L/6^L occurs at
L=255 and is approximately 0.22564938383939653, above the B=1
threshold 1/6; the certificate records its exact rational value.
The longest observed zero run has length 3, ending at L=56 and 255.
The digits before L=6 and after the tested interval are not sampled.

These finite checks verify the recorded finite statements only.
In particular they neither establish nor refute either infinite
assertion. The recurrence identifies a necessary and sufficient
digit question but supplies no mechanism forcing long runs and no
uniform obstruction to them. The tested elementary digit-lifting
route is therefore parked under its predeclared stopping test.
Reopening needs a specific infinite-run mechanism or a rigorous
bound on these particular digits, not more sampling or an assumption
of equidistribution. This stopping decision is not a proof that the
small-root target is false. Universal eventual descent remains open.

## Mathlib

The full small-CRT infinite-selection assertion and this exact digit
equivalence: **not checked**. Supporting CRT, modular inverses, finite
digit expansions and geometric growth: **not checked**. The named
CRT source is sufficient for the imported input. No Mathlib absence,
formal verification or novelty claim is made.
