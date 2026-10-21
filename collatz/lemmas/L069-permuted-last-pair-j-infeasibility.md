# L069 — Arbitrary-order last-pair J-subsystem infeasibility

## Hypotheses

Use exactly the 25 indexed pairs J_i,H_i of L055. For an integer
2<=t<=9250245 attach tails a_23=2+18t, a_24=166504412-18t and
a_i=2 for 0<=i<23. Let pi be any permutation of {0,...,24}, with
each triple (J_i,H_i,a_i) intact. Suppose real s_0,...,s_25 satisfy
s_25=s_0, s_k>=540/11, and, for every 0<=k<=24,

\[
s_{k+1}=2^{-a_{\pi(k)}}\left((27/16)^{J_{\pi(k)}}
(3/2)^{H_{\pi(k)}}s_k-(12/11)(3/2)^{H_{\pi(k)}}-1\right)+23/11,
\tag{1}
\]
\[
4J_{\pi(k)}\log2\le\log s_k+\log(11/4).
\tag{2}
\]

These are exactly the endpoint/domain/J part of L051. Logarithms are
natural. No minimum location, H guard, seed, integer junction, residue,
parity, exact valuation, primitive-orbit or count-ray premise is imposed.
Allowing every pi is equivalent to normalizing row 24 last by cyclic
rotation; the closing edge and each row's own input must be retained.

## Conclusion

There is no such tuple, for any permitted integer t and any cyclic
order. Conditional on (1) and the lower domain, the smallest designated
shifted junction is less than 500000000000, hence has logarithm below 27.
After rotation to any such minimum, every nonliteral order violates (2)
at its first displaced row, with left-minus-right margin strictly greater
than 629441541677/50000000000>12.58. The literal order is excluded by
L068 throughout 2<=t<=9250245.

This is local RESEARCH/REPRODUCTION under the prior SPECIALIZE assessment
`drafts/literature/2026-10-14-last-pair-permuted-j-feasibility.md`.
It extends the local restricted-family exclusion, without a claim of
originality beyond the sources checked. The separate critical audit below
found no defect within the stated necessary-subsystem scope.
No actual-word consequence is assembled here. Other allocations, entry,
unrestricted cycles, divergence and universal eventual descent remain
unresolved. The rational witnesses at t=0,1 are outside these hypotheses.

## Proof

### Full closure bounds the minimum independently of order

Write n_k=s_k-23/11>=47 and, at each chronological position k, put

\[
c_k=\frac{3^{3J_{\pi(k)}+H_{\pi(k)}}}
{2^{4J_{\pi(k)}+H_{\pi(k)}+a_{\pi(k)}}},\qquad
\eta_k=\frac{23}{11}-\frac{12}{11}(16/27)^{J_{\pi(k)}}
 -(16/27)^{J_{\pi(k)}}(2/3)^{H_{\pi(k)}}.
\]

Both subtracted factors are positive and below one. Therefore
0<eta_k<23/11. Subtracting 23/11 from (1), including its final edge,
gives exactly

\[
n_{k+1}=c_k(n_k+\eta_k).
\tag{3}
\]

The formal affine-word input is Halbeisen–Hungerbuehler,
*Optimal bounds for the length of rational Collatz cycles*, Acta Arith.
78 (1997), 227–239, DOI 10.4064/aa-78-3-227-239,
[section 2 equations (2)–(4), Lemma 2, pp. 228–229](https://math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
The saved assessment inspected its hypotheses and essential induction
cases. Here the nonempty formal word has L055's fixed counts
K=397573379 and N=630138897. Its denominator is nonzero by the audited
L055 bound below. Only the real affine identity is used, with the displayed
coordinate specialization; no parity or integer-realization converse and
no scalar-order extremizer theorem is imported. General affine coding
does not need reproof. The following product estimate is the required
changed-family comparison.

Both variable tails remain in the total:
sum a_i=23*2+(2+18t)+(166504412-18t)=166504460.
Thus the complete table gives

\[
\prod_{k=0}^{24}c_k=3^K/2^N=e^{-\Lambda},\qquad
\Lambda=N\log2-K\log3>\lambda_-:=10584/10^{14}>0.
\tag{4}
\]

Multiplying (3) and using n_25=n_0>0 cancels all 25 n_k factors:

\[
1=e^{-\Lambda}\prod_{k=0}^{24}(1+\eta_k/n_k),\qquad
\Lambda=\sum_{k=0}^{24}\log(1+\eta_k/n_k).
\tag{5}
\]

Let m=min_(0<=k<25) n_k>=47. For x>0,
log(1+x)=integral_0^x (1+u)^(-1) du<x. Consequently

\[
\Lambda<\sum_k\frac{\eta_k}{n_k}<\frac{575}{11m},\qquad
s_{\min}=m+23/11<\frac{575}{11\lambda_-}+\frac{23}{11}
=\frac{7187500000030429}{14553}<500000000000.
\tag{6}
\]

An exact positive partial sum certifies

\[
e^{27}>\sum_{q=0}^{40}\frac{27^q}{q!}
=\frac{1112436109266660239093546627471481746956608769015849}
{2106019961293006716393905717248000000000}>500000000000.
\tag{7}
\]

Hence log(s_min)<27. This estimate neither identifies the minimum in
advance nor requires any growing multiplier. In particular it remains
valid when either changed-tail row contracts. It uses only the designated
junctions, with repetitions counted as separate occurrences.

### Rotation and strict first-displacement comparisons

Choose any index attaining the finite minimum and rotate the entire
cyclic tuple to put it at position zero. Rotate each outgoing row with
its own input. Equations (1)–(2) still hold at every edge, including
both the old cut and the new closing edge; ties cause no difficulty.
Write pi again for the rotated order. By (6)–(7), log s_0<27.

If pi is not the identity, let k be the first position with pi(k)!=k.
Then k<=23: once positions 0,...,23 agree, the last row is forced.
All smaller indices have been used, so j=pi(k)>k. Every preceding
row has index i<k<=23, hence i<=22 and its tail is exactly 2. On
these edges, (1) becomes

\[
s_{i+1}=c_i s_i+81/44-(3/11)(3/2)^{H_i}<c_i s_i.
\tag{8}
\]

The strict sign follows from H_i>=40>=5 and
(3/11)(3/2)^5=729/352>648/352=81/44. All s_i are positive by
hypothesis, so logarithms preserve (8). Define literal prefix totals

\[
A_k=\sum_{i<k}(3J_i+H_i),\qquad
D_k=\sum_{i<k}(4J_i+H_i+2),\qquad 0\le k\le23.
\]

Induction gives log s_k<27+A_k log3-D_k log2. No changed-tail
edge appears in this prefix. Also log(11/4)<2, since e^2>1+2+2=5.

Use L055's audited strict rational bounds with
S=10^12, ell=693147180559, u=1098612288669:
log2>ell/S and log3<u/S. For 0<=k<j<=24 set

\[
M_{k,j}=4J_j\ell-29S-A_k u+D_k\ell.
\tag{9}
\]

The J_i increase strictly. Thus the least M_(k,j) for fixed k is
M_(k,k+1). Here are all 24 such integers, directly from (9):

| k | M_(k,k+1) |
|---:|---:|
|0|12588830833540|
|1|29614189109158|
|2|60500402863455|
|3|120442505935101|
|4|232101715013033|
|5|444789447521691|
|6|842717332620691|
|7|1593302785441944|
|8|3007437357201471|
|9|5671924720528197|
|10|10692950383724652|
|11|20151244757249915|
|12|37970278458171381|
|13|71545229723009157|
|14|134804692957947822|
|15|253986199620832760|
|16|478536672198650665|
|17|901607006436467362|
|18|1698704513169729983|
|19|3200496967003432188|
|20|6029997120405317955|
|21|11360998507314510417|
|22|21405032543880209425|
|23|40328770003284970567|

For k<=22 these are L063's audited weakest margins minus 3S;
this imports only those finite expressions, not its fixed-tail root bound
or its all-order conclusion. The new k=23 entry uses
A_23=144318712, D_23=162928789 and J_24=30998279. The certificate
also recomputes every expression directly from L055. All 300 eligible
pairs are positive, with minimum M_(0,1)=12588830833540.

At the first displaced row its own guard therefore obeys

\[
\log s_k+\log(11/4)
<29+(A_k u-D_k\ell)/S
<4J_j\ell/S<4J_j\log2.
\tag{10}
\]

More precisely, left-minus-right in (2) is strictly greater than
M_(k,j)/S>=629441541677/50000000000>12.58. This contradicts (2).
The first-displacement partition covers every nonidentity permutation,
not merely the 300 pairs individually screened. Since the minimum
rotation is arbitrary, any hypothetical feasible cyclic order must be
literal from that minimum. No assumption that row 24 was largest-tailed
or preceded a minimum has entered the argument.

### Literal rejection finishes the interval

In the remaining order pi(k)=k, both attached tails are precisely L068's
tails at the same integer t. All 25 endpoints, the domain and the own-input
guards match its hypotheses, including closure. L068's audited exact
cyclic-root classification states that row 24 fails its J guard for every
2<=t<=9250245. Its t=2 right-minus-left upper margin is
-474883782659/125000000000<-3.79 and decreases thereafter. This is a
contradiction. The argument establishes no assertion about H/seed guards
or integer realizability and needs none for this necessary-subsystem
exclusion. The t=0,1 witnesses and Attempts 027–031 retain their scopes.

### Verification and qualifications

Run `python3 scripts/postspell-word-count/certify_permuted_last_pair.py`.
The complete certificate is
`scripts/postspell-word-count/permuted-last-pair-certificate.json`.
It stores the indexed table, imported intervals, all 300 pairs with
complete operands, every prefix and weakest case, exact rational bounds,
41 exponential terms and the symbolic coverage statement. All five
rational and eight table checks pass; all margins are positive. The
complete weakest-case operands and margins and all supporting checks
were inspected. Monotonicity in J_j then covers every pair. The symbolic
product, minimum rotation and first-displacement proof above, rather than
a pass flag or numerical preview, provide full order/parameter coverage.

This is a changed finite applicability argument within the saved affine/log
assessment, not an import of a theorem asserting simultaneous guard
feasibility. L067's growing-prefix premise is deliberately not assumed.
No new external theorem or cross-notebook input is used. The separate
critical review below verifies (5)–(10), rotation, the expanded 300-pair
coverage and the L068 application. This restricted result is not a
candidate solution to Collatz.

### Independent critical audit — 2026-10-14

The audit used the prior SPECIALIZE assessment
`drafts/literature/2026-10-14-permuted-last-pair-critical-audit.md`.
It found no defect. This verifies the existing local reproduction;
it adds neither a stronger theorem nor a claim beyond the sources checked.
The affine/logarithm citations and their inspected hypotheses are reused.
The precise analytic imports are NIST DLMF, version 1.2.8 (2026-09-15),
[4.5.1](https://dlmf.nist.gov/4.5.E1) for log(1+x)<x at x>0,
[4.2.19](https://dlmf.nist.gov/4.2.E19) for the exponential series at
27>0, and [4.6.4](https://dlmf.nist.gov/4.6.E4) for the logarithm
expansion at positive arguments 2 and 3. The finite remainder checks
below verify the already assessed specialization and error bounds;
they are not a replacement reproof of those general analytic results.

**Full product and minimum.** The domain gives
n_k=s_k-23/11>=540/11-23/11=47. For every row, J>0 and H>0, so
0<(16/27)^J<1 and 0<(2/3)^H<1. Their weighted contributions to
eta have sum strictly below 12/11+1=23/11, proving both signs required
in (3). Multiplying c by eta gives exactly
(23/11)c-2^(-a)((12/11)(3/2)^H+1); hence (3) is (1) in the
unshifted coordinate, for every actual attached tail. Both changed tails
are at least 2 throughout the stated interval; their sum is independent
of t. The complete sums give K=397573379 and N=630138897.
Multiplication includes the final endpoint, so the positive products
of outgoing and incoming n cancel even with ties or repeated values.
This yields (5) without any H/seed, integer-cycle or count-ray premise.

For m=min n, every n_k>=m>0 and 0<eta_k<23/11. Thus each
log(1+eta_k/n_k)<eta_k/n_k<23/(11m), in the correct upper direction.
Together with Lambda>lambda_->0 this gives m<575/(11 lambda_-),
and adding the common shift gives exactly (6). The independent rational
calculation verifies both the displayed fraction and its strict threshold.
Every term of the 41-term positive sum in (7), its exact total and its
strict lower comparison with 500000000000 are verified. The positive
remaining exponential series makes exp(27) strictly larger still.
Consequently log s_min<27. No contraction/growth or minimum-location
claim about either changed row is used.

**Rotation and all orders.** Choose any minimum occurrence q and set
the new input at position k to the old s_((q+k) mod 25), with the
outgoing row pi((q+k) mod 25). The old final edge becomes one of these
edges and the new final edge is the old edge from q-1 to q. Both retain
their own rows and inputs. This verifies closure and every non-strict
J guard after rotation. The argument works for any tied minimum.
For a nonidentity permutation the first displaced k is <=23 and its
row j is >k, because all rows <k are already used. Every preceding row
is therefore literal with index <=22 and has tail 2 throughout the
parameter interval. Its exact additive shifted offset is negative by
H>=40 and the checked inequality 81/44<729/352. This proves (8)
on the positive domain. At k=0 the prefix is empty and strictness
already follows from log s_0<27; induction handles every later k.

The nonnegative prefix exponents give an upper bound by replacing
log3 with u/S and subtracting D_k ell/S. The positive J coefficient
gives a lower bound by replacing log2 with ell/S. Thus (9) has exactly
the required rounding directions for left-minus-right in (2). For fixed
k the difference M_(k,j)-M_(k,k+1) is
4(J_j-J_(k+1))ell>=0, since the full J table is strictly increasing.
All 24 weakest cases and, independently, all 300 complete pairs verify
(10). The new final pair uses A_23=144318712, D_23=162928789;
its two scaled operands are 85945478764125031844 and
45616708760840061277, giving margin 40328770003284970567.
The global minimum remains 12588830833540/S>12.58 at (0,1).
This finite partition covers every nonidentity permutation, regardless
of the suffix or whether row 24 was originally last.

**Literal specialization.** The only remaining order after minimum
rotation has every row i in position i, with a_23=2+18t and
a_24=166504412-18t. It therefore meets precisely L068's endpoint,
domain and own-input J hypotheses at the same integer t. L068 needs
neither a minimum at row 0 nor H/seed assumptions. Its independently
audited all-interval monotonicity and literal rejection apply for every
2<=t<=9250245, including the endpoint where a_24=2. Its t=2 upper
margin -474883782659/125000000000<-3.79 was also arithmetically
cross-checked here. No inference is made from its preserved failed
optional margin<-4 probe. The t=0,1 rational witnesses are untouched.

**Independent finite evidence.** Run
`python3 scripts/postspell-word-count/audit_permuted_last_pair.py`.
The program does not import or run the construction program. It compares
a separately transcribed complete table with L055, recomputes all prefix
sums by direct summation, and compares all original pair operands,
weakest entries, five rational checks, eight table checks and 41
exponential terms with independent values. All 24 written weakest
margins and all 23 reused L063 expressions minus 3S agree.

As an additional check on the eligible audited log inputs, for z=2,3
set x=(z-1)/(z+1), so 0<x<=1/2. The assessed logarithm expansion gives
P<log z<P+R, where P=2 sum_(k=0)^159 x^(2k+1)/(2k+1) and
R=2x^321/[321(1-x^2)]. The remainder is the positive integral
2 integral_0^x u^320/(1-u^2) du, strictly below R by comparison with
1/(1-x^2). No terms are rounded. Opposite interval endpoints bound
N log2-K log3 and independently verify both L055 Lambda bounds and
the two grid logarithm bounds used here. This is verification of
already assessed analytic inputs, not a new analytic theorem.

The full evidence is
`scripts/postspell-word-count/permuted-last-pair-audit-certificate.json`:
387 exact checks pass, zero failures. Complete independent operands,
all 300 pairs, all logarithm terms/remainders, boundary tails and the
original certificate's SHA-256 are saved. The complete selected summary,
24 weakest records, Lambda endpoints and exponential total were inspected.
The original construction certificate is unchanged. These arithmetic
checks supplement the symbolic full-order/full-interval proof above.

No mathematical premise, conclusion or direct dependency changed.
The audit assumes no integer/parity/residue/exact-valuation realization,
primitive counts or actual-word bridge. Attempts 027–031 retain their
recorded stops, and all independent universal gaps remain unresolved.

## Mathlib

Full matching theorem coverage has not been checked. Basic real logarithm,
exponential and finite-product facts would support a formalization, but no
Mathlib theorem is asserted to cover this table, arbitrary-order exclusion
or the Collatz target. Unknown availability is not evidence of absence.
