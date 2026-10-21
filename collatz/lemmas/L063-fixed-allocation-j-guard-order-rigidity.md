# L063 — Fixed allocation J-guard order rigidity

## Hypotheses

Use exactly the 25 indexed triples in L055: J_i,H_i are its literal
table, a_i=2 for 0<=i<24 and a_24=166504412. Let pi be a permutation
of {0,...,23}, extended by pi(24)=24. At chronological position k use
the intact triple (J_pi(k),H_pi(k),a_pi(k)). Require real junctions
s_k>=540/11, s_25=s_0, all 25 exact endpoints L051 (4), and all own-index
non-strict J guards

\[
4J_{\pi(k)}\log2\le\log s_k+\log(11/4),\qquad 0\le k\le24.
\tag{1}
\]

All logarithms are natural. No H guard, seed, integer, residue, actual
parity, exact valuation, or primitive-orbit realization is assumed.
The fixed totals are K=397573379 and N=630138897. These hypotheses
are a necessary subsystem of the complete L055 real system, with the
large-tail row fixed last. No different allocation is considered.

## Conclusion

Such junctions exist if and only if pi is the identity. They are uniquely
determined by the cyclic endpoints. For every allowed order those endpoints
alone give a positive tuple with

\[
18\cdot10^9<n_0<s_0<20\cdot10^9,\qquad n_k=s_k-23/11,
\]

and s_0 is its unique smallest designated junction. Every nonidentity
order violates (1) at its first displaced row. The certified lower bound
on that guard's left side minus right side is at least
779441541677/50000000000>15.58, strictly.

This is a local REPRODUCTION/specialization under the prior assessment
`drafts/literature/2026-10-12-fixed-allocation-j-guard-order-rigidity.md`.
No originality beyond the checked sources is claimed. The separate critical
audit below found no defect. L055's real witness and the earlier modular stops remain
valid. This proves neither integer exclusion for the allocation nor a
Collatz resolution; L056 is potential downstream use, not an input here.

## Proof

### Unique cyclic endpoints and a bound uniform in the order

For each chronological position k put

\[
c_k=3^{3J_{\pi(k)}+H_{\pi(k)}}/
       2^{4J_{\pi(k)}+H_{\pi(k)}+a_{\pi(k)}},
\]
\[
\eta_k=23/11-(12/11)(16/27)^{J_{\pi(k)}}
                    -(16/27)^{J_{\pi(k)}}(2/3)^{H_{\pi(k)}},
\quad C_k=\prod_{t<k}c_t,\quad C_0=1.
\]

The standard affine fixed-point formula is Halbeisen–Hungerbuehler,
*Optimal bounds for the length of rational Collatz cycles*, Acta Arith.
78 (1997), 227–239, DOI 10.4064/aa-78-3-227-239,
[section 2 equations (2)–(4), Lemma 2, pp. 228–229](https://math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
The prior assessment inspected its statement and essential proof cases.
The word here is nonempty, with fixed length N and K odd letters.
Only formal affine composition is imported, without integer realization.
Checking the coordinate specialization, L051 (4) becomes exactly
n_{k+1}=c_k(n_k+eta_k). Consequently, with

\[
B=\sum_{k=0}^{24}\eta_k/C_k,\qquad
P=C_{25}=3^K/2^N=\exp(-\Lambda),
\]

its 25-fold composition is n_25=P(n_0+B). L055's audited input gives

\[
\lambda_-:=10584/10^{14}<\Lambda=N\log2-K\log3
 <10585/10^{14}=: \lambda_+<1.
\tag{2}
\]

The totals do not change under an intact permutation, so 0<P<1.
The unique real cyclic tuple is therefore

\[
n_0=B/(\exp\Lambda-1),\qquad
n_k=C_k\left(n_0+\sum_{t<k}\eta_t/C_t\right).
\tag{3}
\]

These are finite exact rational expressions: exp Lambda=2^N/3^K.
Every eta_k is strictly between 0 and 23/11, since the two positive
subtractions have sum below 12/11+1. Thus B, n_0 and all n_k are positive.
This proves uniqueness among all real endpoint solutions before imposing
the J guards, and includes the full large tail in P and in closure.

Every eligible first row has J>=8 and H>=40. Its c_0 is at least
3^64/2^74>10^8; its eta_0 is at least
7122556955297586891012225981605/3433683820292512484657849089281>2.
Both facts follow by monotonicity in J,H and the exact baseline (8,40,2)
comparisons in L055/L062. For 0<=k<24, the actual tail is 2 and
c_k>2, using (27/16)^2(3/2)^3/4=19683/8192>2.
Hence C_k>10^8*2^(k-1) for 1<=k<=24, uniformly over every pi. Although
eta_24 appears in B, c_24 does not appear in these prefixes; it is never
assumed growing. Summing the finite geometric majorant gives

\[
2<B<B_+:=\frac{23}{11}(1+2/10^8)=1150000023/550000000.
\]

The positive exponential series gives x<exp(x)-1<x/(1-x) for 0<x<1.
Using (2), (3) yields the exact order-uniform bounds

\[
n_0>2(1-\lambda_+)/\lambda_+
 =39999999995766/2117>18\cdot10^9,
\]
\[
s_0<B_+/\lambda_-+23/11
 =95833335260143/4851<20\cdot10^9.
\tag{4}
\]

The positive recurrence and c_k>2 for k<24 show n_0<...<n_24.
Thus all junctions meet the stated lower bound and s_0 is their unique
minimum, with no assertion about intermediate parity phases. L062's exact
41-term lower sum for exp(24) exceeds 20*10^9, so (4) gives log s_0<24.
Also exp(2)>1+2+2=5>11/4, giving log(11/4)<2.
No order-dependent B value has been reused as though it were constant.

### Upper bound along an unchanged literal prefix

For a tail-2 row the exact shifted endpoint is

\[
s_{k+1}=c_k s_k+81/44-(3/11)(3/2)^{H_{\pi(k)}}<c_k s_k.
\tag{5}
\]

Indeed every such H>=40>=5 and
(3/11)(3/2)^5=729/352>648/352=81/44. Since s_k and s_{k+1}
are positive, logarithms preserve (5). Suppose positions 0,...,k-1
are literal. Define the integer prefix totals

\[
A_k=\sum_{i<k}(3J_i+H_i),\qquad
D_k=\sum_{i<k}(4J_i+H_i+2).
\]

For k=0 the empty sums are zero. Induction from log s_0<24 gives

\[
\log s_k<24+A_k\log3-D_k\log2.
\tag{6}
\]

Only edges in the unchanged prefix enter (6). The suffix may be any
permutation because the initial bound (4) is uniform in that suffix.

### Complete first-displacement comparison

Let S=10^12, ell=693147180559 and u=1098612288669.
L055 (6), with its audited rational logarithm remainder bounds, supplies
log2>ell/S and log3<u/S. For 0<=k<j<=23 put

\[
m_{k,j}=4J_j\ell-26S-A_k u+D_k\ell.
\tag{7}
\]

The J values in the literal table are strictly increasing. For each k,
m_{k,j} is therefore smallest at j=k+1. Here are all 23 exact smallest
scaled margins, calculated by the displayed integer sums and (7):

| k | m_(k,k+1) |
|---:|---:|
|0|15588830833540|
|1|32614189109158|
|2|63500402863455|
|3|123442505935101|
|4|235101715013033|
|5|447789447521691|
|6|845717332620691|
|7|1596302785441944|
|8|3010437357201471|
|9|5674924720528197|
|10|10695950383724652|
|11|20154244757249915|
|12|37973278458171381|
|13|71548229723009157|
|14|134807692957947822|
|15|253989199620832760|
|16|478539672198650665|
|17|901610006436467362|
|18|1698707513169729983|
|19|3200499967003432188|
|20|6030000120405317955|
|21|11361001507314510417|
|22|21405035543880209425|

All are strictly positive. For any nonidentity pi, let k be its first
displaced position. Then 0<=k<=22: after fixing positions 0,...,22,
the only remaining row is 23. All rows below k have already been used,
so j=pi(k)>k. The guard is paired with this row j at its own input s_k.
Using (6), nonnegative A_k,D_k, the outward log bounds and log(11/4)<2,

\[
\log s_k+\log(11/4)
 <26+(A_k u-D_k\ell)/S
 <4J_j\ell/S<4J_j\log2.
\tag{8}
\]

The middle strict inequality is precisely m_{k,j}>0. The difference
between the actual left side of (1) and its right side exceeds
m_{k,j}/S, whose minimum is the k=0,j=1 value stated in the conclusion.
Thus every nonidentity order fails a necessary non-strict guard.
There are 276 eligible pairs, not 276 permutations; the first-displacement
argument covers all 24! permutations, independently of their suffixes.

For the identity permutation L055's audited literal witness satisfies
all endpoints and every J guard (as well as its additional constraints).
This supplies existence, completing the claimed equivalence. Row 24's
own guard is included in that imported existence; for nonidentity orders
an earlier failure suffices. Cyclic relabeling cannot change the verdict
if the outgoing row remains attached to its input: the unique minimum
is just after row 24 and the rotated endpoint tuple is uniquely determined.

### Certificate, source comparison and qualifications

Run `python3 scripts/postspell-word-count/certify_fixed_allocation_order_rigidity.py`.
The full certificate is
`scripts/postspell-word-count/fixed-allocation-order-rigidity-certificate.json`.
It stores all intact rows, every literal prefix exponent, all 276 guard
operands and exact margins, the 23 weakest cases above, root fractions,
41 exponential terms, 12 rational supporting checks and 7 integer checks.
There are zero failures. The complete 23 weakest-case operands/margins
and all supporting comparisons were inspected. Their strict positivity
and monotonicity in J_j establish full pair coverage; no preview, pass
flag or floating-point estimate supplies the proof. The logarithm and
Lambda bounds are audited inputs from L055, not fresh source claims.

Known affine composition and scalar ordering theorems do not directly
give the simultaneous own-index guard verdict, as recorded in the prior
assessment. The necessary specialization here is the uniform root bound,
negative shifted offset, and complete first-displacement comparison.
No general affine/parity coding theorem is reproved. Attempts 027–030
remain valid modular stops and Attempt 031 remains a valid single-order
failure; none is used as an all-order premise. The published computational,
continued-fraction and Rhin/Crandall qualifications of L051 remain where
relevant to actual-cycle motivation. No integer-cycle theorem is applied
to these real junctions. Different allocations, unrestricted cycles,
divergence and universal eventual descent remain unresolved.

### Independent critical audit — 2026-10-12

The separate approved RESEARCH/REPRODUCTION audit found no defect in the
full statement, including the subsidiary uniform bounds, positivity,
unique minimum and cyclic relabeling. Coverage was reused from
`drafts/literature/2026-10-12-fixed-allocation-order-rigidity-audit.md`;
no broader allocation or downstream integer exclusion was attempted.

The coordinate check, for every chronological row and its actual tail,
is

\[
c_k\eta_k=\frac{23}{11}c_k-
 2^{-a_{\pi(k)}}\left(\frac{12}{11}(3/2)^{H_{\pi(k)}}+1\right).
\]

Thus subtracting 23/11 from L051 (4) gives exactly the recurrence used
above. Dividing it by C_{k+1}=c_k C_k gives
n_{k+1}/C_{k+1}=n_k/C_k+eta_k/C_k; the telescoped identity is (3).
Recomputed total exponents are K=397573379 and N=630138897, retaining
the full last tail. Consequently 0<C_25=exp(-Lambda)<1 and the cyclic
equation has exactly one real root. Every eta_k is positive, so B and
that root and all its prefixes are positive. This argument establishes
exact closure without expanding huge powers or using a tolerance.

For any allowed permutation, its first row has J>=8,H>=40,a=2.
The multiplier increases with either J or H. Both subtractions in eta
decrease with J, and the second decreases with H while the first stays
constant. Hence the same exact baseline c_0>10^8 and eta_0>2 holds
for every first row. The first 24 multipliers exceed 2. Every denominator
C_k appearing in B, including C_24, contains only those multipliers;
the closing multiplier is not among them. Therefore the same geometric
majorant gives 2<B<B_+ for every possible suffix. The closing tail still
enters C_25 and thus the root denominator. This distinction is essential
to the uniformity, and was checked explicitly.

For 0<x<1, x<exp(x)-1<x/(1-x), with strictness from the positive
series and its terms of degree at least two. The lower root estimate uses
2(1-lambda_+)/lambda_+; the upper shifted estimate uses
B_+/lambda_-+23/11. Their exact fractions in (4) check out.
Strictly increasing n_0,...,n_24 gives the unique minimum among the
25 designated inputs; n_25 is the repeated closing input. All s_k exceed
540/11. The independently summed 41 positive exp(24) terms exceed
20 billion, proving log s_0<24. Also exp(2)>5>11/4. No claim about
the minimum over intermediate parity phases is needed.

For each tail-2 edge the additive term in the shifted coordinate is
81/44-(3/11)(3/2)^H. It is negative for H>=5, since its latter
term is at least 729/352>648/352=81/44; every eligible H>=40.
Positivity of both endpoints therefore permits the logarithmic inequality
in (5). The unchanged prefix yields (6), even though its initial cyclic
root depends on the suffix, because the initial upper bound is uniform.
The prefix exponents A_k,D_k are nonnegative, so the outward logarithm
substitutions in (7)–(8) have the stated directions.

At the first displacement k, rows 0,...,k-1 have already been consumed.
Thus pi(k)>k, and k cannot equal 23. These are exactly the 276 pairs
0<=k<j<=23. The strictly increasing J sequence makes j=k+1 weakest
for each k. Every one of those 23 margins, and independently all 276
complete pairs, was recomputed. The global minimum is
779441541677/50000000000>15.58 at (k,j)=(0,1). The actual guard's
left side minus right side is strictly larger than its certified margin,
so it contradicts even the permitted non-strict <= sign. The outgoing
row j is paired with input s_k throughout. A later guard need not be
evaluated after this necessary one fails.

For literal existence the audit reused L055's audited exact construction
and checked its hypotheses against this subsystem. As an additional
finite check it recomputed all 25 literal J margins from the canonical
table, including row 24; all are positive. The lower-height induction
uses only the first 24 tail-2 edges. L055's stronger H/seed assertions
are not required for uniqueness. Rotating a cyclic solution and its
outgoing rows gives a solution for the rotated endpoints; their product
multiplier stays exp(-Lambda)<1, so uniqueness forces that same rotated
tuple. Its minimum and outgoing row remain paired. Moving row 24 back
to the final position restores the normalization used in this theorem.

The independent verifier is
`python3 scripts/postspell-word-count/audit_fixed_allocation_order_rigidity.py`.
It neither imports nor executes the original generator. It parses L055's
canonical table, independently sums every prefix, and recomputes all
saved pair operands and margins, all 23 written weakest margins, all
12 supporting rational comparisons, all 7 integer assertions, the root
fractions, and all 41 exponential terms using factorials. Complete saved
records are compared with recomputed records, not just their flags.

As an independent check of the imported enclosures, it uses 120 unrounded
rational terms of the already assessed logarithm expansion. For
0<x<1 and t=(1+x)/(1-x), its lower sum is
2 sum_{i=0}^{119} x^(2i+1)/(2i+1). The remainder is positive and at
most 2x^241/[241(1-x^2)], by bounding the denominator in the integrated
remainder. Direct x=1/3 and x=1/2 enclose log2 and log3; opposite
endpoints give N log2-K log3. The resulting interval lies strictly
inside (10584/10^14,10585/10^14). The same method at x=7/15
checks log(11/4), and binary reduction checks log(18 billion)>23.61
for the literal existence margins. The series terms, remainders and
full endpoints are saved; no floating-point logarithm is used.

The full certificate is
`scripts/postspell-word-count/fixed-allocation-order-rigidity-audit-certificate.json`:
348 exact audit checks, zero failures, all comparison operands, and the
original certificate's SHA-256. The complete root and Lambda fractions
and minimum operands were also inspected. The written all-order argument,
rather than finite enumeration of permutations, supplies the quantifiers.

The direct mathematical inputs remain exactly L051, L055 and L062:
the subsystem, allocation/existence/logarithm bounds, and exponential
bound respectively. L056 is only a proposed later use. No DAG edge or
main argument changed, so PROOF.md's historical pending label is
superseded by this canonical audit. Published source qualifications and
unchecked Mathlib/build status remain; no integer-cycle theorem is
applied to reals, and no Collatz candidate has been produced.

## Mathlib

Full matching coverage and external Lean builds were not checked. Existing
supporting logarithm/exponential results do not certify this finite
all-order statement. Unknown coverage is not evidence of absence. The
exact rational certificate supplements the written proof; it is not a
Lean theorem or an integer-cycle certificate.
