# L012 — Identically singular pencils have at most five bad parameters

## Hypotheses

Let F=F_(97^20), let H be the order-sixteen subgroup of F_97^*, and let
\[
 C=\{(p(x))_{x\in H}:p\in F[X],\ \deg p<8\}.
\]
Fix arbitrary a,b in F^H. Use the event in
[the pinned affine-line model](../foundations/02-pinned-affine-line-model.md)
at 1/4<=delta<5/16, whose agreement supports have size at least twelve.
Write B_4(a,b) for this original bad-parameter set and B_3(a,b) for the
same pair's bad set at radius 3/16, with supports of size at least thirteen.

Use the moments and determinant defined in L010:
\[
 s_j(T)=\sum_{x\in H}(a_x+Tb_x)x^j\quad(1\le j\le8),
 \qquad D(T)=\det(s_{i+j+1}(T))_{0\le i,j\le3}.
\]
Assume D(T)=0 identically as a polynomial in F[T]. No hypothesis on
coordinate locators or the direction b is imposed.

## Conclusion

Every parameter having an error representative of weight at most four
has a representative of weight at most three. Moreover,
\[
 B_4(a,b)=B_3(a,b),\qquad |B_4(a,b)|\le5<15,
 \qquad |B_4(a,b)|/97^{20}\le2^{-128}.
\]
The five count is an upper bound; attainment on this H is not asserted.
This does not count all close parameters as bad, assert that every
singular syndrome is sparse, or identify the pinned event with July ABF26.

## Proof

### Applicability of the covered syndrome-rank identity

The kernel and pointwise moment identities in L010's proof precede and
do not require its polynomial nonvanishing assumptions. In particular,
the moment map annihilates C, and a witnessed error e of weight four
and support A satisfies its identity (4):
\[
 D(t)=\det(V_A)^2\prod_{x\in A}e_xx\ne0,
 \qquad (V_A)_{i,x}=x^i\quad(0\le i\le3).
\]
All factors are nonzero: the four locators are distinct, lie in H and
are nonzero, and e_x is nonzero by the definition of its support.
This is a use of that pointwise identity, not of L010's full theorem
under a violated determinant hypothesis.

The supporting syndrome-rank result is known: Farré, Sayols and
Xambó-Descamps,
[*On PGZ decoding of alternant codes*, arXiv:1704.05259v2](https://arxiv.org/pdf/1704.05259v2#page=7),
May 7, 2018, Theorem 3.1 and Corollary 3.2, printed p. 7.
To reconcile the zero-indexed syndrome convention with the displayed
moments, take locator alpha_x=x and check multiplier h_x=x. Its
syndrome of index m is then sum_x e_x*x*x^m, our moment of index
m+1. The leading four-by-four Hankel block is precisely D(t).
The coefficient field is the whole F, with eight check moments and
decoding capacity four; there is no prime-subfield restriction on e.
No new decoder or rank theorem is being reproved.

At any t with a+tb-c=e, c in C and weight(e)<=4, the annihilation of
C makes the pencil's evaluated moments those of e. If weight(e)=4,
the displayed identity contradicts D(t)=0. Consequently weight(e)<=3.
The minimum distance nine, also checked in L010's proof, makes such
a weight-at-most-four representative unique, although uniqueness is
not needed for the support transfer.

### Transfer of the complete original bad set

Fix t in B_4(a,b). Choose its original witnessing support S and a
codeword c agreeing with a+tb there. The word e=a+tb-c has weight
at most four and vanishes on S. The preceding argument gives weight
at most three. Its full agreement set
\[
 S^+=H\setminus\operatorname{supp}(e)
\]
therefore contains S and has size at least thirteen.

On any witnessing support, membership of a+tb in C|_S makes the
input-failure disjunction equivalent to b|_S not belonging to C|_S:
if b were a code restriction, subtraction would make a one too.
Thus b fails on the chosen S. This failure persists on S^+, since
a codeword agreeing with b on S^+ would also agree with it on S.
The combination agrees with c on S^+. Hence this same enlarged support
witnesses t in B_3(a,b). No puncturing, loss of input failure, or fixed
common codeword is assumed.

This is the applicability passage for the known agreement-support
bridge in Chojecki's July 17, 2026-dated
[*Shortening Bounds for Reed–Solomon MCA*, v9.2 author TeX](https://raw.githubusercontent.com/przchojecki/rs-mca/main/RS_MCA_Paving_v9.2.tex),
`lem:mca-definition-bridge` (MDB), read October 3. That mutable source
is a supporting result, not a certified copy of July ABF26 or a match
for the full singular-pencil statement.

We have proved B_4(a,b) is contained in B_3(a,b). Conversely, every
support of size at least thirteen is allowed in the original cell,
so its same membership and failure conditions imply the reverse
inclusion without a determinant assumption. This proves equality.
Weights zero, one and two are included, as are b=0 and b in C.
In the latter cases the combination-membership condition would itself
force a to be a code restriction, so the bad set is empty.

### Application of the existing boundary count

Apply the uniform upper theorem of L007 with n=16, k=8, r=3 and
radius 3/16. Its hypotheses hold over F and on these distinct points:
\[
 n-k+1=9=3r,\qquad 3/16\le3/16<4/16.
\]
It gives, for every pair including the present one,
\[
 |B_3(a,b)|\le\max\{r+1,\lfloor n/r\rfloor\}
 =\max\{4,5\}=5.
\]
Only this upper theorem is used; L007's five-count attainment on
F_17^* is not transferred to H in F_97^*. Its packing ingredient
overlaps the inspected `prop:general-overlap-packing-upper` (OP5–OP6)
in the same Chojecki source; no new general boundary theorem is claimed.
Finally 15*2^128<=97^20<16*2^128 compares the achieved count five
with the actual allowed count fifteen, proving the budget assertion.

Singularity was used only after a sparse representative had been
witnessed. In particular, a residual family on three fixed coordinates
can be close for all q parameters while having only three bad ones.
The claimed bound is for the original same-support event throughout.

The auxiliary command `python3 scripts/singular-distance/check.py`
compares both support events over F_97 by interpolation on every
admissible support, without using the determinant as a decoding test.
It checks identically zero D for degenerate, fixed-support, confluent
and translated pencils, and verifies the weight reduction for every
close parameter found. These examples do not enumerate all pairs or
the extension field; the proof and L007 cover arbitrary inputs in F.

## Mathlib

Full singular-pencil transfer and count: **not checked**. Supporting
finite-field syndrome-rank, Vandermonde, support-enlargement and packing
coverage in Mathlib: **not checked**. The precise PGZ, MDB and OP5–OP6
citations are supporting results; none is claimed to match the full
statement or to supply formal verification.

The pinned ArkLib declarations
[`CoreDefinitions.IsMCA` and `CoreDefinitions.mcaError`](https://github.com/Verified-zkEVM/ArkLib/blob/e65197892890b8fd9b0dc05b8980273cf1d595cc/ArkLib/Data/CodingTheory/ProximityGap/ProximityGenerators.lean#L98)
support only the event definition. ArkLib is separate from Mathlib,
and this argument does not certify correspondence with July ABF26.
This step reproduces a local application of covered rank, support and
boundary ingredients; originality of the full specialization is not claimed.
