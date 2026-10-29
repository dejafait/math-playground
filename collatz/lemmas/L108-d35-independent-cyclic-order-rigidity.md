# L108 — Independent cyclic-order rigidity for d35

## Hypotheses

Take the 25 indexed pairs of L055's table, changing only H_0 to 5
and H_24 to 32670656; every J_i and every other H_i is unchanged.
Put r=25, B=9250245 and kappa=23/11. Let b_i be arbitrary
nonnegative integers with sum_i b_i=B, and set a_i=2+18b_i.
Let pi be any permutation of {0,...,24}. Suppose real junctions
s_0,...,s_25 satisfy s_25=s_0, s_k>=540/11 for 0<=k<25,
and all 25 equations and own-input inequalities

\[
s_{k+1}=2^{-a_{\pi(k)}}(G_{\pi(k)}s_k-Q_{\pi(k)})+\kappa,
\quad G_i=(27/16)^{J_i}(3/2)^{H_i},\quad
Q_i=(12/11)(3/2)^{H_i}+1,
\tag{1}
\]
\[
4J_{\pi(k)}\log2\le\log s_k+\log(11/4).
\tag{2}
\]

All logarithms are natural. Each outgoing indexed row keeps its pair,
tail allocation and own input under permutation or rotation. No H guard,
seed, prescribed minimum location, integer junction, actual-word, parity,
residue, exact-valuation or primitive-period hypothesis is imposed.

## Conclusion

Every feasible cyclic order is a rotation of 0,...,24 over the full
integer allocation simplex. More precisely, for any q at which the
smallest designated junction occurs,

\[
\pi((q+k)\bmod25)=k\qquad(0\le k<25).
\tag{3}
\]

Zero budgets, including a closing tail equal to 2, are allowed. There
is no distinct-junction or primitive-period assumption. This is a local
RESEARCH/REPRODUCTION application of audited L075 and L084, not a new
ordering criterion or a result beyond their machinery. The separate
critical applicability audit below found no defect in this scope. No feasibility verdict,
assembly with C107a, actual-word transfer or universal descent follows
from this application alone.

## Proof

Use the prior SPECIALIZE assessment
`drafts/literature/2026-10-26-d35-independent-cyclic-order.md`.
Apply L075's independently audited sufficient implication, matching its
numbered hypotheses below. L055 is used only for its literal pair table;
none of its witness, minimum, seed or primitive-count assumptions is
imported. L097 is a d34 template, not a mathematical input for d35.

**Table and totals, L075 (1).** This is precisely L084's member d=35,
since 40-35=5 and 32670621+35=32670656. Its integers J_i are strictly
increasing from J_0=8. Here H_0=5 and all other H_i>=72, so every
H_i>=3. The opposite changes preserve sum J_i=66061058 and
sum H_i=199390205. L084's completed step337 reconstruction certifies

\[
K=\sum_i(3J_i+H_i)=397573379,\qquad
N=\sum_i(4J_i+H_i)+2r+18B=630138897.
\tag{4}
\]

Every allowed allocation has sum_i a_i=2r+18B=166504460.
Thus these are exactly L075's totals for every allocation and order,
not totals inferred from a minimum or a primitive orbit.

**Analytic tests, L075 (2).** Use L084's independent O constants

\[
\lambda=1323/12500000000000,\quad T=27,\quad
\ell=693147180559/10^{12},\quad
u=1098612288669/10^{12},\quad v=2.
\tag{5}
\]

The completed analytic audit in L084 proves
0<lambda<Lambda=N log2-K log3, 0<ell<log2, log3<u and
log(11/4)<2, with the amplified enclosure errors retained. Its O cap is

\[
U=\frac{23r}{11\lambda}+\frac{23}{11}
=\frac{7187500000030429}{14553}
<500000000000<P(27)<e^{27},\qquad
P(27)=\sum_{j=0}^{40}\frac{27^j}{j!}.
\tag{6}
\]

These certify every inequality in L075 (2). The coarse grid ell,u is
used for the margins, not to infer the tiny positive Lambda; that sign
is supplied by L084's separate outward analytic enclosures. Neither the
failed fixed C/H cap nor the failed S test is used.

**All offsets, L075 (3).** The complete d35 O records certified in
L084 include all 25 tail-2 offset bounds. At row0 the exact value is

\[
d_0=\frac{81}{44}-\frac3{11}(3/2)^5=-\frac{81}{352}<0.
\tag{7}
\]

For every i=1,...,24, H_i>=72 gives the certified upper bound

\[
d_i=\frac{81}{44}-\frac3{11}(3/2)^{H_i}
\le-\frac{67585198634721895314242333308740579}
           {51946031311566097350656}<0.
\tag{8}
\]

The bound is exact at row1 and an upper enclosure at rows2–24,
including the changed row24. These are the required tail-2 offsets;
no sign is asserted for an actual large-tail offset.

**All prefixes and margins, L075 (4)–(5).** With this same table put
A_k=sum_(i<k)(3J_i+H_i), D_k=sum_(i<k)(4J_i+H_i+2), for
0<=k<=23. L084's completed all-member O reconstruction certifies
all 24 indexed tests with their own outgoing row k+1:

\[
M_k=4J_{k+1}\ell-27-2-A_k u+D_k\ell>0,
\qquad
\min_{0\le k\le23}M_k=\frac{629441541677}{50000000000}>12.58.
\tag{9}
\]

The records include A_0=D_0=0, A_1=29,D_1=39 and
A_23=144318677,D_23=162928754. For every nonempty tested prefix,
both exponents are the d1 exponents minus34: row0 is included and
row24 is excluded. This is L084's audited general prefix formula at
d=35; its margin shift is +34(u-ell)>0 and the empty-prefix test
is unchanged. The all-member reconstruction, not just L084's displayed
d<=4 minimum, supplies (9). Strict increase of J and ell>0 are exactly
L075's conditions covering every larger displaced row j>k. The empty
prefix and the last eligible displacement k=23 are both retained.

For the complete relevant finite evidence see `/tables/34/O` in
`scripts/postspell-word-count/h-transfer-family-certificate.json` and
`/reconstructed_tables/34/O` in
`scripts/postspell-word-count/h-transfer-family-audit-certificate.json`.
The prior source gate inspected both complete objects. This application
also inspected the complete audit O object, its explicit member d=35,
all 25 rows and its counts, matching the changed table rather than an
array index alone. The mathematical input is L084's completed analytic
and all-member O audit. A stored PASS flag or a preview is not a proof;
no certificate was regenerated or independently recertified in this step.

**Same-tuple application, L075 (6)–(7).** The indexed b_i are
nonnegative integers of total B and have precisely L075's tails. The
arbitrary pi permutes intact outgoing rows. Equations (1), (2), the
lower domains and s_25=s_0 are literally L075's tuple hypotheses for
this same allocation and coordinates. They assert no existence of a
feasible tuple. All data tests having matched, L075 gives (3).

For clarity about the cuts in this application, rotation at q replaces
the position-k input by s_((q+k) mod25), and its outgoing row by
pi((q+k) mod25), keeping that row's b_i and a_i. The old edge24 to0
remains among the edges; the new closing edge is the old edge q-1 to q,
read modulo25. Thus both cuts, all exact endpoints and the non-strict
guard at each actual input are preserved. Repeated junction values stay
as separate occurrences. L075 chooses any minimum occurrence; none is
prescribed in these hypotheses. Its audited proof retains every actual
tail in the cyclic product and makes tail-2 comparisons at actual
lower-domain inputs only. No criterion reproof is needed here.

For precise upstream coverage, L075 specializes Halbeisen–Hungerbuehler,
*Optimal bounds for the length of rational Collatz cycles*, Acta Arith.
78 (1997), 227–239, DOI 10.4064/aa-78-3-227-239,
[section2, equations(2)–(4), Lemma2, pp.228–229](https://www.math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
The nonnegative integer exponents specify finite formal affine words;
(4)–(6) supply the positive Lambda and nonzero denominator. No integer
itinerary realization is imported. The positive-real analytic inputs
and certified remainders are reused through L075/L084 from NIST DLMF
[4.5.1](https://dlmf.nist.gov/4.5.E1),
[4.2.19](https://dlmf.nist.gov/4.2.E19) and
[4.6.4](https://dlmf.nist.gov/4.6.E4). Their relevant arguments2,3,11/4
and exponential argument27 are positive. No new source retrieval,
current-release claim or reproof of those identities is made.

Attempt032's failed S/C/H package and the original-H witnesses remain
valid. This independent order application neither repairs that package
nor invokes C107a's full-guard exclusion. A later same-tuple rotation
and assembly must retain its H assumptions explicitly. Actual-word
transfer, entry, other tables, unrestricted cycles, divergence and
universal eventual descent remain unresolved.

### Independent critical applicability audit — 2026-10-27, step525

This RESEARCH/REPRODUCTION audit uses the invocation-start SPECIALIZE
assessment `drafts/literature/2026-10-27-l108-d35-independent-order-critical-audit.md`.
Its verdict is no defect in the exact application (1)–(9) and conclusion
(3). This validates a local use of established machinery, not a stronger
ordering theorem, a feasibility verdict or progress beyond the inspected
sources. No new analytic criterion or certificate program is introduced.

**Exact input scope.** Read L075's full sufficient implication and its
completed step281 audit, L084's analytic/O construction and completed
step337 audit, and L055's complete pair table only. L055's witness,
minimum, seed, H guards and primitive-count conditions are not premises
of this application. L097 is not an input. The scoped duplicate check
found the pending application rather than a completed L108 audit.
Attempts027,032,035 and the original-H witnesses retain their scope.

**Member, totals and analytic directions.** Inspected the complete
`/reconstructed_tables/34/rows`, `/counts`, `/Lambda_interval` and `/O`
within the audit certificate named above, and confirmed its member
identity d=35. Every row matches L055 except precisely H_0=5 and
H_24=32670656. The J list is strictly increasing, and H_i>=5.
The opposite changes preserve both pair sums; hence K=397573379 and
N=630138897 for every allowed allocation, since sum a_i=166504460.
The rational lambda in (5) equals L084's 10584/10^14 exactly.
L084's completed analytic audit supplies lambda<Lambda from outward
logarithm endpoints with the large coefficients retained, not from
ell and u. Its separately verified positive exponential sum and cap
give (6), with the same r, lambda and T. The lower bound ell and
upper bounds u,v have precisely the directions required in L075 (2).
Changing the allocation or order changes none of these operands.
The complete Lambda interval was inspected without truncation; its
analytic validity is imported from L084, not recertified from its digits.

**All offsets and displacement cases.** The complete O object contains
exactly rows0–24 and exactly displacement indices0–23, with no omission
or duplicate. Row0's offset is -81/352. At row1 the displayed H=72
offset in (8) is exact; at each row2–24 it is an upper bound, because
H_i>=72 and H -> (3/2)^H is increasing. Therefore each actual tail-2
offset is negative, including changed row24. This says nothing about
the sign of an actual large-tail offset.

For all24 records, the recorded A_k,D_k match the literal sums in
L075 (4): A_0=D_0=0 and the increments are 3J_k+H_k and
4J_k+H_k+2, respectively. In particular the first nonempty pair is
(29,39) and the final tested pair is (144318677,162928754).
Relative to d=1 every nonempty prefix decreases by34 in both
coordinates, since it includes row0 and excludes row24. Substitution
in the margin formula changes its value by +34(u-ell)>0. The empty
margin is unchanged, equals 60ell-29=629441541677/50000000000,
and remains the minimum; all23 other complete records exceed it.
L084's audited d=1 minimum and this exact prefix shift also verify
positivity without extrapolating its displayed d<=4 scope. Increasing
J_j and ell>0 cover every larger displaced row j>k. Thus the empty
prefix and k=23, whose displaced row can only be24, are both covered.

**One tuple and both cuts.** L108's indexed integer b_i>=0 of total
B give exactly L075's tails, and pi permutes the same intact indexed
rows. Equations (1),(2), s_k>=540/11 and closure are literally its
remaining hypotheses, on the original coordinates and allocation.
In particular n_k=s_k-23/11>=47; no junction integrality is needed.
At any minimum occurrence q, rotating positions modulo25 carries
each outgoing pair, b_i, a_i and own-input non-strict J guard together.
The old closing edge is retained; the new closing edge is the old
q-1 to q edge. This includes q=0 and q=24, and neither edge's tail
is replaced by a tail-2 comparison in the full cyclic product.

L075 then applies to this same rotated tuple. Its strict minimum cap
handles k=0; its tail-2 upper comparisons apply only at actual
lower-domain inputs. The nonnegative prefix coefficients give an
upper logarithmic bound using u and ell, whereas ell and v give a
lower bound for the displaced row's guard difference. The positive
M_k therefore contradicts that very row's non-strict guard, including
an equality guard. Every nonidentity permutation has a first
displacement k<=23. This proves exactly (3), for any chosen minimum
occurrence. Ties and repeated values are retained as occurrences;
zero budgets, closing tail2 and repeated periods are never excluded
by an added hypothesis. No H guard or realization premise is used.

The completed L084 audit supplies the arithmetic input; no certificate
was regenerated, and no stored PASS flag or bounded preview substitutes
for its proof. No unresolved arithmetic defect requiring replay was
found. The existing DAG row L055,L075,L084 remains accurate. Neither
the mathematical argument nor its dependencies changed, so PROOF.md
and DAG.md are unchanged by this audit. A later C107a assembly still
needs separate coverage and must retain its own H assumptions; no
such assembly or actual-word transfer was attempted here. Full matching
Mathlib coverage remains unchecked, and universal descent remains open.

## Mathlib

Full matching coverage for this d35 cyclic endpoint/own-input guard
application has not been checked. Supporting positive-real logarithm,
exponential and finite-sum results are not a matching theorem. Unknown
coverage is not evidence of absence; no Lean verification is claimed.
