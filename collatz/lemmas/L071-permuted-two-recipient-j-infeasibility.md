# L071 — All-order two-recipient J-subsystem infeasibility

## Hypotheses

Use exactly the 25 indexed pairs J_i,H_i in L055. For an integer
1<=t<=9250244 attach tails

\[
a_i=2\ (i<22),\qquad a_{22}=20,\qquad
a_{23}=2+18t,\qquad a_{24}=166504394-18t.
\]

Let pi be any permutation of {0,...,24}, keeping each triple intact.
Suppose real s_0,...,s_25 satisfy s_25=s_0, s_k>=540/11 and,
for every 0<=k<=24, the exact endpoint and own-input non-strict J guard

\[
s_{k+1}=2^{-a_{\pi(k)}}\left((27/16)^{J_{\pi(k)}}
(3/2)^{H_{\pi(k)}}s_k-(12/11)(3/2)^{H_{\pi(k)}}-1\right)+23/11,
\tag{1}
\]
\[
4J_{\pi(k)}\log2\le\log s_k+\log(11/4).
\tag{2}
\]

Logarithms are natural. These are only L051's endpoint/domain/J
conditions. No minimum location, growing-row condition, H guard, seed,
integer/parity/residue/exact-valuation realization or primitive/count-ray
premise is imposed. Repeated periods and coincident junctions are allowed.

## Conclusion

There is no such tuple for any admitted integer t or cyclic order.
Conditionally on (1) and the domain, a smallest designated shifted
junction has logarithm below 27. From any rotation to such a minimum,
every nonliteral order strictly fails (2) at its first displaced row,
by more than 629441541677/50000000000>12.58. The remaining literal
order is excluded by audited L070.

This is local RESEARCH/REPRODUCTION under the prior SPECIALIZE assessment
`drafts/literature/2026-10-15-permuted-two-recipient-j-test.md`.
It adapts an existing affine/product/first-displacement method, with no
claim of originality beyond the sources checked. The separate critical
audit below found no defect within the stated scope. No actual-word
application is assembled here. Existing
rational witnesses have different allocations and remain valid; other
allocations, entry, unrestricted cycles, divergence and universal eventual
descent remain unresolved.

## Proof

### Full closure and minimum control

At chronological position k put n_k=s_k-23/11>=47 and

\[
c_k=\frac{3^{3J_{\pi(k)}+H_{\pi(k)}}}
 {2^{4J_{\pi(k)}+H_{\pi(k)}+a_{\pi(k)}}},\qquad
\eta_k=\frac{23}{11}-\frac{12}{11}(16/27)^{J_{\pi(k)}}
 -(16/27)^{J_{\pi(k)}}(2/3)^{H_{\pi(k)}}.
\]

Every J,H is positive, so both subtracted terms are positive and their
sum is strictly less than 12/11+1. Thus 0<eta_k<23/11.
Substitution into (1) gives, including the closing edge,

\[
n_{k+1}=c_k(n_k+\eta_k).                            \tag{3}
\]

The standard formal affine input is Halbeisen–Hungerbuehler,
*Optimal bounds for the length of rational Collatz cycles*, Acta Arith.
78 (1997), 227–239, DOI 10.4064/aa-78-3-227-239,
[section 2 equations (2)–(4), Lemma 2, pp. 228–229](https://math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
The saved assessment covers its statement and essential induction cases.
Only formal chronological affine composition is used, with the coordinate
specialization (3), not an integer/parity realization converse. The word
is nonempty with the fixed counts below and nonzero denominator because
Lambda>0. No general coding theorem is reproved here.

The changed tails retain the sum

\[
44+20+(2+18t)+(166504394-18t)=166504460.
\]

L055's full table gives sum J_i=66061058 and sum H_i=199390205,
so K=397573379 and N=630138897 in every order. The audited L055
logarithm enclosure therefore gives

\[
\prod_k c_k=3^K/2^N=e^{-\Lambda},\qquad
\Lambda=N\log2-K\log3>\lambda_-:=10584/10^{14}>0.
\tag{4}
\]

Multiplication of (3) cancels every positive n_k, since n_25=n_0.
Taking logarithms yields

\[
\Lambda=\sum_{k=0}^{24}\log(1+\eta_k/n_k).
\tag{5}
\]

Let m=min_(0<=k<25) n_k. For positive x, log(1+x)<x.
Consequently Lambda<sum eta_k/n_k<575/(11m), giving

\[
s_{\min}=m+23/11<\frac{575}{11\lambda_-}+\frac{23}{11}
=\frac{7187500000030429}{14553}<500000000000.
\tag{6}
\]

The same exact positive exponential partial sum as in audited L069 gives

\[
e^{27}>\sum_{q=0}^{40}\frac{27^q}{q!}
=\frac{1112436109266660239093546627471481746956608769015849}
 {2106019961293006716393905717248000000000}>500000000000.
\tag{7}
\]

Thus log s_min<27. This repeats L069's minimum comparison with the
actual changed tail sum checked; its different-allocation conclusion is
not invoked. The analytic inputs, already inspected under that method,
are NIST DLMF [4.5.1](https://dlmf.nist.gov/4.5.E1) for log(1+x)<x
at x>0 and [4.2.19](https://dlmf.nist.gov/4.2.E19) for the exponential
series. No growth or prior minimum location is used. Both varying tails
remain in full closure, even when their rows contract.

### Rotation and the changed literal prefix

Choose any minimum occurrence and rotate the cyclic inputs and their
outgoing rows together to make it position zero. Every equation and
own-input guard is preserved: the old closing edge remains present,
and the new closing edge is the old edge just before the chosen minimum.
Ties and repeated values cause no loss. Write pi for the rotated order;
now log s_0<27.

If pi is not the identity, let k be its first displaced position.
Then k<=23, since after positions 0,...,23 agree the last is forced.
All rows below k have already been used, so j=pi(k)>k. Each preceding
row has its literal index i<k and hence i<=22. Those rows have a_i<=20
and H_i>=40. Their shifted affine offsets are strictly negative:

\[
2^{-a_i}\left((12/11)(3/2)^{H_i}+1\right)
>\frac{12}{11}\frac{(3/2)^{40}}{2^{20}}
=\frac{36472996377170786403}{3170534137668829184}
>\frac{23}{11}.                                    \tag{8}
\]

For the last comparison the exact positive difference is
2713063429607401481/288230376151711744. Hence the shifted endpoint
on each preceding literal edge satisfies s_(i+1)<c_i s_i.
This checks precisely the new obligation: row 22 has tail 20, rather
than 2, when k=23. It assumes neither that row 22 grows nor anything
about the signs of the offsets at varying-tail rows 23 and 24.

For 0<=k<=23 define literal prefix totals using the actual fixed tails
on rows below 23:

\[
A_k=\sum_{i<k}(3J_i+H_i),\qquad
D_k=\sum_{i<k}(4J_i+H_i+2)+18\,\mathbf1_{k=23}.
\]

Induction on these positive endpoints gives

\[
\log s_k<27+A_k\log3-D_k\log2.                    \tag{9}
\]

At k=0 strictness follows from the minimum bound and the prefix is
empty. All later steps use (8). In particular
A_23=144318712 and D_23=162928807; both varying-tail rows are absent
from every load-bearing prefix.

### Complete first-displacement comparison

Reuse audited L055's outward bounds, obtained from the positive-real
logarithm expansion [DLMF 4.6.4](https://dlmf.nist.gov/4.6.E4) with
its recorded rational remainder:

\[
\log2>\ell/S,\qquad \log3<u/S,\qquad
S=10^{12},\quad \ell=693147180559,\quad u=1098612288669.
\]

Also log(11/4)<2 because e^2>1+2+2=5>11/4. For each
0<=k<j<=24 put

\[
M_{k,j}=4J_j\ell-29S-A_k u+D_k\ell.               \tag{10}
\]

For fixed k, J_j strictly increases, so M_(k,j) is least at j=k+1.
All 24 least scaled margins are as follows; the first 23 expressions
agree with L069, while the final one incorporates the extra 18 halvings.
Every expression is also recomputed directly from L055's full table.

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
|23|40328782479934220629|

The last case has lower scaled operand 85945478764125031844 and
upper scaled operand 45616696284190811215. Every margin is positive;
the least over all 300 eligible pairs is M_(0,1)=12588830833540.
The full-order coverage is the first-displacement partition, not an
enumeration of 300 permutations.

At the displaced row j, (9), A_k,D_k>=0 and the indicated outward
rounding directions give

\[
\log s_k+\log(11/4)
<29+(A_k u-D_k\ell)/S
<4J_j\ell/S<4J_j\log2.                            \tag{11}
\]

Its own guard (2) fails, with left-minus-right strictly greater than
M_(k,j)/S>=629441541677/50000000000>12.58. This covers every
nonidentity order after any minimum rotation, with no suffix or
parameter restriction beyond the hypotheses.

### Literal rejection and qualifications

The only remaining order has row i at position i, with tails exactly
a_22=20, a_23=2+18t and a_24=166504394-18t. Every endpoint,
the lower domain and every own-input J guard, including closure,
match L070 at the same integer 1<=t<=9250244. L070's audited literal
exclusion applies without a minimum, growth, H/seed or integrality
premise. Its row-24 right-minus-left guard margin is at most its t=1
value, strictly below -474883782659/125000000000<-3.79. Thus this
last order is impossible as well. At the upper endpoint the final
tail is 2; it has never been omitted from (4)–(5).

Reproduce the finite arithmetic with
`python3 scripts/postspell-word-count/certify_permuted_two_recipient.py`.
The complete certificate is
`scripts/postspell-word-count/permuted-two-recipient-certificate.json`.
It stores the full indexed table, both parameter-boundary tail tables,
every prefix and all 300 pair operands, all 24 least cases, six rational
checks, twelve table checks and all 41 exponential terms. Zero checks
fail. All 24 least-case operands and margins, every rational check and
the table checks were inspected in full. Monotonicity in J_j covers
all other pairs mathematically; the symbolic product, rotation and
prefix argument gives coverage of every order and every admitted t.
The certificate supports that proof and is not a substitute for it.

L070 alone did not exclude other orders, and L069's old prefix claim
could not be reused without (8). No general scalar composition ordering
theorem asserts these simultaneous guards. Attempts 026 and 031 and
the earlier modular stops retain their scopes. This fixed-family
necessary-subsystem exclusion is not a candidate Collatz resolution.
The independent audit below verifies this scope without strengthening it.

### Independent critical audit — 2026-10-15

Under the prior SPECIALIZE assessment
`drafts/literature/2026-10-15-permuted-two-recipient-critical-audit.md`,
the independent audit found no defect. The affine and analytic source
coverage cited above is reused; no further general theorem is assumed
or reproved. This is verification of a local reproduction, not a new
allocation exclusion or an originality claim.

**Product and strict minimum.** In (1), subtracting 23/11 and writing
s_k=n_k+23/11 gives
c_k n_k+(23/11)c_k-2^(-a)((12/11)(3/2)^H+1).
Multiplication of the stated eta_k by c_k gives exactly the last two
terms. This proves (3) for every attached tail, including closure.
Since J,H>0, the two subtracted contributions to eta have sum strictly
less than 23/11, and both are positive. Thus 0<eta<23/11.
The domain gives n_k>=47. The separately transcribed table gives
the stated J,H sums; the tails sum to 166504460 for every t. Hence
the full product is exactly 3^397573379/2^630138897.

Multiplying all 25 equations cancels positive incoming and outgoing
n factors, with repetitions counted as occurrences. For m=min n_k,
each log(1+eta_k/n_k)<eta_k/n_k<23/(11m). This yields (6),
using Lambda>lambda_->0 in the correct direction. The independent
arithmetic verifies the exact fraction in (6), all 41 exponential
terms and the total in (7), and both strict comparisons with
500000000000. The exponential series has a positive omitted tail.
Therefore log(s_min)<27, without a growth or minimum-location premise.

**Rotation and changed support.** At a minimum occurrence q, relabel
input k as the old input (q+k) modulo 25 and give it that old input's
outgoing row. Each endpoint and its own-input guard is retained. The
old closing edge is still present; the new closing edge was the edge
from q-1 to q. Ties and coincident junctions cause no loss. For any
nonidentity order after rotation, its first displaced k is at most 23,
and its row j is greater than k because all smaller rows have been used.
The preceding literal rows are therefore precisely 0,...,k-1<=22.

These preceding rows have a<=20 and H>=40. Their subtracted offset
term exceeds (12/11)(3/2)^40/2^20: the omitted positive 2^(-a)
makes the comparison strict even at both parameter boundaries. The
independent calculation verifies the fraction and positive difference
in (8). Hence every preceding shifted offset is negative, including
row 22 when k=23. Positive inputs and multipliers justify the logarithms
and induction in (9); the empty prefix at k=0 is covered by the strict
minimum bound. Neither varying-tail row is used in a prefix. The extra
18 halvings occur precisely in D_23, whose recomputed value is 162928807;
the corresponding A_23 is 144318712.

**Complete comparisons and rounding.** The independent program uses
the already assessed positive-real logarithm expansion, with
x=(z-1)/(z+1) for z=2,3,11/4 and the exact enclosure

\[
P_z=2\sum_{v=0}^{159}\frac{x^{2v+1}}{2v+1}
 <\log z<P_z+\frac{2x^{321}}{321(1-x^2)}.
\]

Here 0<x<=1/2. The positive remainder is
2 integral_0^x u^320/(1-u^2) du, strictly below the displayed
upper bound. This checks the previously assessed finite-remainder
method with no rounded terms. The two endpoints independently confirm
the log2/log3 grid bounds and, with opposite signed endpoints, both
ends of the cancellation-sensitive L055 Lambda enclosure.

All A_k,D_k are nonnegative. Increasing log3 and decreasing the
subtracted log2 therefore bounds the right side of (9) upward, whereas
decreasing log2 bounds the positive 4J_j log2 downward. The inequality
log(11/4)<2 follows from the strict exponential comparison recorded
above. This proves the rounding directions in (11). For fixed k,
M_(k,j)-M_(k,k+1)=4(J_j-J_(k+1))ell>=0. Strictly increasing J
therefore makes the 24 listed adjacent cases sufficient for all 300
pairs. Their complete operands, all 300 comparisons and every printed
margin are independently reconstructed and agree. In the changed final
case the operands are 85945478764125031844 and 45616696284190811215,
with difference 40328782479934220629. The least margin remains
629441541677/50000000000>12.58. The first-displacement argument,
rather than finite permutation sampling, covers every nonidentity order.

**Exact literal match.** The surviving order has exactly L070's indexed
pairs and tails at the same integer t. Rotation has preserved the real
lower domain, every non-strict own-input J guard, and all endpoints.
L070 requires no minimum, H/seed, integrality or primitive-count premise.
Its audited monotonicity and boundary rejection thus apply throughout
1<=t<=9250244. The extreme tails are (20,20,166504376) and
(20,166504394,2) on rows 22--24. The fixed row 22 and both varying
rows match, including the closing tail 2 at the upper endpoint.
Independently summing the first 24 boundary rows gives
(p,q)=(271907921,306970784); recomputing L070's signed logarithm
comparison gives exactly -474883782659/125000000000<-3.79.
No inference about the other guards or actual-word realization is needed.

**Finite evidence and verdict.** Run
`python3 scripts/postspell-word-count/audit_permuted_two_recipient.py`.
It imports or executes no construction program. It separately transcribes
all 25 pairs, compares them with L055, reconstructs prefixes by direct
summation and compares the original certificate's complete arithmetic
records: all pairs, weakest cases, rational/table checks and exponential
terms. It also checks every written weakest margin and cited rational
fraction. All 355 exact checks pass, with zero failures. The full evidence,
including logarithm terms/remainders and original-certificate SHA256, is
`scripts/postspell-word-count/permuted-two-recipient-audit-certificate.json`.
The full summary, all 24 weakest operands, both boundary tables, complete
Lambda endpoints and exponential total were inspected. The original
certificate is preserved. The symbolic reasoning above supplies the
full-order and full-interval coverage; pass flags alone do not.

No hypothesis, conclusion or direct mathematical dependency changed.
L051 supplies the conventions, L055 the table/count/log inputs, L069
the audited product/comparison method and L070 the literal exclusion.
Other allocations, entry, unrestricted cycles, divergence and universal
eventual descent remain unresolved. Actual-word application has not
been assembled; full matching Mathlib coverage remains unchecked.

## Mathlib

Full matching theorem coverage is unchecked. Standard logarithm,
exponential, finite-product and affine facts support the argument, but
no matching Mathlib theorem for this table or all-order guard exclusion
has been identified. Unknown coverage is not evidence of absence; no
Lean build or formalization is claimed.
