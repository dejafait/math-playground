# Lemma 838: Prescribed finite PF order does not force adjacent eventual positivity

## Hypotheses

Fix any integer m>=2. Put u=m+1, t=1/u, q=1+t^2, and define
\[
 P_m(z)=(1+4z)(1+3z)(1+2z)(1+2z+qz^2)
       =\sum_{n=0}^5 a_nz^n.
\]
Extend a_n by zero outside 0<=n<=5. For integers r>=1 and k>=0 let
\[
 D_{(r,k)}(P_m)=\det[a_{k+j-i}]_{0\le i,j<r}.
\]
PF_m means every ordered minor of size at most m in the infinite
Toeplitz matrix (a_(j-i))_(i,j>=0) is nonnegative. Coefficients are
ordinary coefficients; no factorials or Xi identification are assumed.

## Conclusion

For each prescribed m the six coefficients are strictly positive
rational numbers, a_0=1, all five polynomial roots are distinct, and
the zero-extended coefficient sequence is PF_m. Moreover, with
R(m)=1000(m+1),
\[
 24^{-r}D_{(r,3)}(P_m)>\frac{72}{125}>0
       \qquad(r\ge R(m)).                                      \tag{1}
\]
The set of positive integers r with D_(r,4)(P_m)<0 has positive
natural density, in particular is infinite. No effective negative
onset or specified arithmetic progression is claimed.

Thus no prescribed finite PF order, together with eventual positive
shift3 minors, forces eventual nonnegative shift4 minors in this
rational degree-five class. The polynomial and its positive onset may
depend on m. This does not assert one polynomial is PF_m for all m,
nor supply strict overlap or actual-Xi structure. It is a known-method
specialization, not a proof or disproof of RH. The separate bounded
critical audit below validates precisely this prescribed-finite-order scope.

## Proof

### Imported results and scope

Olga M. Katkova, *Multiple positivity and the Riemann zeta-function*,
[arXiv:math/0505174v1](https://arxiv.org/pdf/math/0505174v1),
Definition2/(8), printed p.4, and **Theorem B**, printed p.5:
a real polynomial f with f(0)>0 and no roots in the open sector
|arg z|<pi*m/(m+1) has a PF_m coefficient sequence. This is the
all-ordered-minor sufficient criterion, with boundary roots allowed.

Per Alexandersson, *Schur polynomials, banded Toeplitz matrices and
Widom's formula*, Electronic Journal of Combinatorics19(4) (2012), P22,
[arXiv:1208.5607v1](https://arxiv.org/html/1208.5607v1),
**Theorem6**, printed p.5, for distinct complex variables x_1,...,x_5
and elementary coefficients a_j with a_0=1, gives at shifts k=3,4
and every positive integer r
\[
 D_{(r,k)}=\sum_{|S|=k}C_SB_S^r,\quad
 B_S=\prod_{i\in S}x_i,\quad
 d_S=\prod_{i\in S,j\notin S}(x_i-x_j),\quad
 C_S=B_S^{5-k}/d_S.                                      \tag{2}
\]
Deleting the source's first k columns and taking its leading r-square
gives a_(k+j-i), exactly the determinant here. No transpose,
reciprocal-root convention or extra sign is introduced.

Jason P. Bell and Stefan Gerhold, *On the positivity set of a linear
recurrence sequence*, Israel Journal of Mathematics157, 333–345,
DOI10.1007/s11856-006-0015-1,
[published author PDF](https://fam.tuwien.ac.at/~sgerhold/pub_files/papers/2007_osc_rec.pdf),
**Theorem2**, printed p.335, with dominating-root convention on p.334
and proof in Section3, pp.339–341: a nonzero real constant-coefficient
linear recurrence sequence with no positive dominating characteristic
root has both positivity and negativity sets of positive natural
density. Dominating roots are the maximal-modulus roots in the actual
nonzero power-sum representation. No irrational-angle assumption is
required. We verify the actual roots below, rather than use an
annihilator with possible extraneous roots.

These three results are imported. Their already assessed source proof
cases are reused; no reproof is needed. The parameter choice, bounds
and recurrence applicability below are the specialization obligations
not supplied by their statements. L837 supplies historical motivation
only; no local lemma is a mathematical premise of this proof.

### Rational coefficients, distinct roots and prescribed sector

Write w=1+it and v=1-it, so wv=q. Then
\[
 P_m(z)=\prod_{x\in\{4,3,2,w,v\}}(1+xz),
\]
and direct multiplication gives
\[
 (a_0,\ldots,a_5)=
 (1,11,45+t^2,85+9t^2,74+26t^2,24+24t^2).                 \tag{3}
\]
Since 0<t<=1/3 is rational these are strictly positive rational
numbers. The five variables are nonzero and distinct: the three real
ones differ by at least1, w and v are nonreal, and |w-v|=2t>0.
Consequently the polynomial roots -1/x are distinct as well.

Let theta=arctan(t). The two nonreal polynomial roots have absolute
principal argument pi-theta. Since
\[
 0<\theta<t=1/(m+1)<\pi/(m+1),
\]
their arguments exceed pi*m/(m+1). The other roots are negative real
and have absolute argument pi. Thus none lies in the excluded open
sector. With P_m(0)=1, Theorem B proves PF_m for all ordered minors
through the prescribed order, including the zero extension.

### Complete positive-ray bound

Set rho=|w|=|v|=sqrt(q). Here
\[
 1<\rho\le\sqrt{10}/3<4/3<2.                              \tag{4}
\]
In (2) with k=3 the subset S_*={4,3,2} has base24 and coefficient
\[
 C_* =\frac{576}{(9+t^2)(4+t^2)(1+t^2)}
       >\frac{576}{10\cdot5\cdot2}=\frac{144}{25}.        \tag{5}
\]
Its denominator pairs each real variable with w and v, so each
paired product is (x-1)^2+t^2>0. There is no other factor or sign.

There are exactly nine other triples. Six contain two real variables
and one of w,v; their base moduli are at most12rho<16. Three contain
one real variable and both w,v; their base moduli are at most4q<=40/9<16.
This exhausts all binomial(5,3)=10 triples and proves that24 is the
unique maximal-modulus base. In particular each other |B_S|/24<=2/3.

Every pairwise difference other than w-v or v-w has modulus at least1:
real differences have modulus at least1, and for x=2,3,4,
|x-w|=|x-v|=sqrt((x-1)^2+t^2)>=1. A cross denominator d_S contains
at most one factor w-v or v-w. If it contains this factor its other
factors have modulus at least1, so |d_S|>=2t. If it does not, then
|d_S|>=1>=2t. All ten denominators are nonzero, and, since |B_S|<=24,
\[
 |C_S|=|B_S|^2/|d_S|\le288/t.
\]
Thus the entire remainder, including every tied subleading term,
satisfies for every positive r
\[
 \left|24^{-r}D_{(r,3)}-C_*\right|
 \le \frac{2592}{t}(2/3)^r=2592u(2/3)^r.                 \tag{6}
\]
For r>=1000u, the binomial inequality
(3/2)^r>r/2 (indeed >=1+r/2) gives
\[
 2592u(2/3)^r<\frac{5184u}{r}
                  \le\frac{648}{125}.
\]
Combining (5) and (6) yields (1), since
144/25-648/125=72/125. The determinant is real because its entries
are real; alternatively every nonreal term in (2) is paired with its
conjugate. This proves the full infinite positive ray, not a finite
sample or continuity argument. The onset is deliberately coarse.

### Actual shift-four recurrence and negative signs

For k=4 the five subsets in (2), listed by their omitted variable,
give precisely the following bases:
\[
 \begin{array}{c|ccccc}
 \text{omitted variable}&v&w&2&3&4\\\hline
 B_S&24w&24v&12q&8q&6q.
 \end{array}                                             \tag{7}
\]
They are pairwise distinct: the first two are a nonreal conjugate
pair, and the remaining three are different positive real numbers.
Each coefficient C_S=B_S/d_S is nonzero, since all variables and all
cross differences are nonzero. Thus there are no equal bases to
combine and no zero coefficients to remove. Reality follows either
from the determinant or from conjugation of the complete expansion.

The sequence therefore satisfies the real rational-coefficient
recurrence whose characteristic polynomial is
\[
 H(X)=(X^2-48X+576q)(X-12q)(X-8q)(X-6q).                 \tag{8}
\]
These are its actual characteristic roots, not just extraneous
annihilating roots. To see this directly, distinct nonzero bases B_j
have invertible matrix (B_j^r)_(1<=r,j<=5): its determinant is a
nonzero Vandermonde determinant times prod_j B_j. Consequently a
power sum with all five nonzero coefficients cannot vanish
identically. If another polynomial A in the forward shift annihilates
the sequence, applying it to (2) gives sum_j C_j A(B_j)B_j^r=0 for
all r>=1. The same invertibility forces A(B_j)=0 for all j.
Hence every base in (7) occurs in the minimal characteristic
polynomial, which is exactly (8). This also verifies the required
nonzero-sequence hypothesis without extrapolating from samples.

The first two roots have modulus24rho; the remaining roots have
modulus at most12q=12rho^2<24rho by (4). The only dominating roots
are therefore24w and24v, and neither is positive real. Bell–Gerhold
Theorem2 applies to this nonzero real recurrence and yields positive
natural density of negative terms. Shifting its index from r>=1 to
r>=0, if required by the source convention, multiplies its nonzero
power-sum coefficients by B_j and leaves all these hypotheses and
the natural densities unchanged. In particular negative shift4
minors occur beyond every finite rank cutoff.

No period-six property is transferred from L837; no phase irrationality
or effective negative onset is needed or asserted. The all-m
construction is proved separately for each prescribed m. Constants
need not be uniform as t tends to zero; (1) nevertheless supplies an
explicit allowed onset for each m. PF_m constrains ranks at most m,
so later negative minors do not contradict it. Actual-Xi realization,
additional overlap assumptions, growing-shift comparison and the main
all-degree mixed-positivity gap L030–L032/C032a remain unresolved.

### Separate bounded critical audit, 6 November 2026

The invocation-start SPECIALIZE scope covers this audit. It passes
without a correction to the mathematical argument. The imported
Katkova Definition2/TheoremB, Alexandersson Theorem6 and Bell–Gerhold
Theorem2 are used at the precise versions and locations above, with
their previously inspected proof cases. This audit checks the full
local specialization, not independent proofs of those theorems.

First multiply the real cubic, whose coefficients are (1,9,26,24),
by (1,2,q). This gives (3), with positive rational coefficients for
every prescribed integer m>=2. In particular the entries are ordinary
coefficients, not factorial-scaled moments. The five factors have
nonzero distinct variables. For a variable w=1+it in the upper half
plane, -1/w lies in the upper left quadrant and has argument
pi-arctan(t); the conjugate root has the opposite argument. Thus the
excluded-sector comparison has the correct direction. Negative real
roots avoid the open sector too. Applying TheoremB with constant
term1 proves every ordered minor through size m, rather than just the
consecutive minors used later. The zero extension agrees with its
Toeplitz convention.

For a separate exhaustive denominator check, write
A_x=sqrt((x-1)^2+t^2) for x=2,3,4. The ten shift3 terms have the
following moduli; each row containing a choice of w or v means two
terms, giving 1+2+2+2+1+1+1=10 in total:

| Selected triple S | Base modulus | Denominator modulus |
| --- | --- | --- |
| {4,3,2} | 24 | A_4^2 A_3^2 A_2^2 |
| {4,3,w} or {4,3,v} | 12 rho | 4t A_4 A_3 A_2 |
| {4,2,w} or {4,2,v} | 8 rho | 2t A_4 A_3 A_2 |
| {3,2,w} or {3,2,v} | 6 rho | 4t A_4 A_3 A_2 |
| {4,w,v} | 4q | 2 A_3^2 A_2^2 |
| {3,w,v} | 3q | A_4^2 A_2^2 |
| {2,w,v} | 2q | 2 A_4^2 A_3^2 |

Here A_x>=1 and 2t<=2/3<1. The table confirms all denominators
are >=2t, without overlooking a second small conjugate difference.
For the real triple the signed denominator is positive: the factors
pair as (x-w)(x-v)=A_x^2. Its coefficient is therefore exactly
576/(A_4^2 A_3^2 A_2^2)>144/25. All nine other bases have modulus
strictly less than16, and at most24 overall, giving the coefficient
bound288/t and the complete remainder2592(m+1)(2/3)^r.

For integer r>=1000(m+1), the strict inequality
(3/2)^r>=1+r/2>r/2 yields a remainder strictly less than
5184(m+1)/r<=5184/1000=648/125. Subtracting this from the strict
dominant lower bound gives >720/125-648/125=72/125. This covers
every allowed r and m; it does not pass to a coalescing-root limit.
There is no reliance on small determinants or numerical samples.

For shift4, the product of all five variables is24q. Dividing it
by the omitted variable gives (7), using q/v=w and q/w=v.
The coefficients B_S/d_S are all nonzero; no product collision is
possible between a nonreal base and the three distinct real bases.
The quadratic factor of (8) has sum48 and product576q, so (8) is
real with rational coefficients. If a forward-shift polynomial A
annihilates the sequence, its values at all five bases vanish by the
Vandermonde argument already given, since each C_S and each B_S is
nonzero. This proves minimality even for the tail indexed by r>=1,
and excludes an identically zero sequence. Thus all five roots, with
their actual nonzero coefficients, occur in the recurrence.

Finally 12q/(24rho)=rho/2<1, so only24w and24v dominate. They
are nonreal for every m in the hypotheses. This verifies all the
nonzero/reality/actual-dominant-root hypotheses of Bell–Gerhold
Theorem2. Its natural-density conclusion, not just a finite sign
sample or an unproved irrational-phase argument, gives the asserted
positive density of negative shift4 minors. Reindexing changes no
density. No periodic subsequence or effective negative onset is added.

The empty local DAG row is correct: the three cited external results
and elementary finite algebra suffice, with L837 used only as
motivation. The audit validates local known-method reproduction; it
establishes no new general theorem beyond the cited methods, no
single PF-infinity example and no Xi realization, overlap or signs.

## Mathlib

Full matching coverage for this family, the sector criterion, Widom's
formula and Bell–Gerhold's oscillation theorem has not been checked.
Supporting polynomial, determinant and recurrence machinery is not
being claimed as a matching formal proof. No absence claim is made.
