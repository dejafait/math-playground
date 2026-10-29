# L103 — Conditional literal d35 earlier-support exclusion

## Hypotheses

Take all 25 indexed pairs from L055, changing only H_0=5 and
H_24=32670656. Use literal indexed order. Let b_0,...,b_24 be
nonnegative integers with sum b_i=B=9250245, and assume b_0=0.
Put a_i=2+18b_i and define

\[
\kappa=23/11,\qquad G_i=(27/16)^{J_i}(3/2)^{H_i},\qquad
Q_i=(12/11)(3/2)^{H_i}+1.
\]

Suppose real s_0,...,s_25 satisfy s_25=s_0, s_i>=540/11 for
0<=i<25, and every endpoint and non-strict own-input J guard

\[
s_{i+1}=2^{-a_i}(G_i s_i-Q_i)+\kappa,\qquad
4J_i\log2\le\log s_i+\log(11/4)\quad(0\le i<25).
\tag{1}
\]

All logarithms are natural. The closing endpoint remains required
when a_24=2. No H guard, minimum, seed, integer junction, parity,
valuation, realization or primitive-period premise is assumed.

## Conclusion

Every such tuple has b_1=...=b_21=0. More precisely, a hypothetical
least positive recipient j in 1,...,21 would satisfy

\[
4J_{j+1}\log2-\log s_{j+1}-\log(11/4)>M_j,
\qquad
M_j\ge\frac{734806653733}{31250000000}>47/2>0,
\tag{2}
\]

contrary to its own-input J guard.

This is local RESEARCH/REPRODUCTION under the prior SPECIALIZE
assessment `drafts/literature/2026-10-25-d35-earlier-nonzero-recipients.md`.
It is a finite specialization of inspected affine/analytic machinery,
with no originality claim beyond the checked sources. Construction
and exact data checks are complete; the separate step474 critical audit
below found no defect within these hypotheses.
b_0=0 remains an assumption. No assembly with L102 or the last-pair
exclusion, actual-word transfer or Collatz resolution is asserted.

## Proof

### Imported machinery and changed-table scope

Import only L055's indexed table, not its witness, minimum or seed.
The two opposite H changes preserve sum H=199390205 and sum J=66061058.
For every allocation in the hypotheses the full tail sum is
50+18B=166504460. Consequently

\[
K=\sum_i(3J_i+H_i)=397573379,\qquad
N=\sum_i(4J_i+H_i+a_i)=630138897.
\tag{3}
\]

L084 (2) and its independent all-member audit supply at d=35

\[
0<\lambda:=10584/10^{14}<\Lambda:=N\log2-K\log3,
\qquad \ell:=693147180559/10^{12}<\log2,
\]
\[
\log3<q:=1098612288669/10^{12},\qquad
\log(11/4)<w:=1011600911679/10^{12}.
\tag{4}
\]

These are independent analytic inputs, not applications of L084's
failed full O/S/C conjunction. Use the guard-conditioned cap argument
L076 proof(6)-(7) separately from its full sufficient criterion.
The changed-prefix specialization of its first-recipient proof(8)
is justified below with distinct prefix and recipient offset tests.
L099's d34 conclusion and L102's fixed-row22 conclusion are not inputs.
Attempt032 and the original witnesses are unchanged.

The assessed formal-affine source is Halbeisen–Hungerbuehler,
*Optimal bounds for the length of rational Collatz cycles*, Acta
Arithmetica 78 (1997), 227–239, DOI 10.4064/aa-78-3-227-239,
[section2 equations(2)-(4), Lemma2 pp.228-229](https://www.math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
Only finite real affine algebra is used; no integer-realization converse
is needed. The analytic inputs are [NIST DLMF4.5.1](https://dlmf.nist.gov/4.5.E1),
log(1+x)<x at x>0, and the audited positive-real applications of
[4.6.4](https://dlmf.nist.gov/4.6.E4) and
[4.2.19](https://dlmf.nist.gov/4.2.E19) at 2,3,11/4 and24.
Primary hypotheses and needed proof cases are recorded in the reused
assessment. No general coding or series theorem is reproved here;
the following algebra verifies this conditional support specialization.

### Cyclic cap with arbitrary later allocations

Put n_i=s_i-kappa>=47 and

\[
\eta_i=\kappa-(16/27)^{J_i}\bigl(12/11+(2/3)^{H_i}\bigr),
\qquad c_i=2^{-a_i}G_i.
\]

All J_i>=2,H_i>=3, so the positive subtracted sum is strictly
less than 12/11+1=kappa. Thus 0<eta_i<kappa. Substitution in (1)
gives n_(i+1)=c_i(n_i+eta_i)>0. The full product is
prod c_i=3^K/2^N by (3). Closure therefore gives exactly

\[
\Lambda=\sum_{i=0}^{24}\log(1+\eta_i/n_i).
\tag{5}
\]

For i>=1 the own-input J guard implies
n_i>=(4*2^{4J_i}-23)/11. The indexed J are strictly increasing
with J_1=15. Hence, by log(1+x)<x and eta_i<kappa, their 24
summands total strictly less than

\[
E=\frac{552}{4\cdot2^{60}-23}
=\frac{552}{4611686018427387881}.
\]

The remaining summand is strictly below kappa/n_0. Thus
lambda<Lambda<kappa/n_0+E. The exact comparisons lambda-E>0 and

\[
s_0<R:=\frac{\kappa}{\lambda-E}+\kappa
=\frac{1325859730438202850942226985830949}{67113790726173775832193}
<U:=20000000000
\tag{6}
\]

are checked in the certificate. All inversions use positive quantities.
The imported exponential partial-sum application, recomputed exactly,
gives

\[
U<\sum_{k=0}^{40}\frac{24^k}{k!}
=\frac{202750314819830504045671593478515759301}
       {7661655986496068058455078125}<e^{24}.
\tag{7}
\]

In particular log s_0<24. This cap uses all 25 actual endpoints
and every allocated tail through (3)-(5). It needs no support
assumption or minimum. H_0=5 satisfies its positivity hypotheses.

### Separate prefix and recipient offsets

Suppose some b_j>0 for j in 1,...,21, and choose the least such j.
Since b_0=0 is assumed, all preceding b_i=0, so a_i=2 for i<j.
Integrality gives b_j>=1 and a_j>=20. Every possible preceding
row 0,...,20 has H_i>=5. Its tail2 offset obeys

\[
\kappa-Q_i/4=81/44-(3/11)(3/2)^{H_i}
\le81/44-(3/11)(3/2)^5=-81/352<0.
\tag{8}
\]

Every possible recipient row 1,...,21 instead has H_j>=72, so

\[
Q_j\ge\frac{12}{11}(3/2)^{72}+1
=\frac{67585198634830509743348335148655587}{12986507827891524337664}
>\frac{24117248}{11}=\kappa2^{20}.
\tag{9}
\]

These signs use disjoint roles. At row0, Q_0=817/88<kappa*2^20
still fails the old tail20 sufficient test. It is never required here.

At each actual input, the positivity already proved above gives
G_i s_i-Q_i=G_i(n_i+eta_i)>0. Increasing the tail therefore
decreases the endpoint at that input. Equations (8)-(9) imply

\[
s_{i+1}<(G_i/4)s_i\quad(i<j),\qquad
s_{j+1}\le2^{-20}(G_j s_j-Q_j)+\kappa
<2^{-20}G_j s_j.
\tag{10}
\]

Both the subtracted Q_i inside the tail division and kappa outside
are retained until their offset signs are justified. Every multiplied
factor and actual junction is positive. No auxiliary trajectory or
monotonicity of later heights is assumed.

### Complete prefixes and all 21 own-input margins

Define A_k=sum_(i<k)(3J_i+H_i) and
D_k=sum_(i<k)(4J_i+H_i+2). Multiplying (10) and using (6)-(7) yields

\[
\log s_{j+1}<24+A_{j+1}\log3-(D_{j+1}+18)\log2.
\tag{11}
\]

The extra 18 belongs only to the recipient; a larger b_j strengthens
the comparison. All these prefixes contain row0 but omit row24, so
both A and D decrease by exactly 35 relative to L055's original table.
Set C_j=D_(j+1)+18+4J_(j+1) and

\[
M_j=C_j\ell-24-w-A_{j+1}q.
\tag{12}
\]

Here A_(j+1)>0 and C_j>0. Equations (4) and (11) give

\[
4J_{j+1}\log2-\log s_{j+1}-\log(11/4)
>C_j\log2-24-\log(11/4)-A_{j+1}\log3>M_j.
\tag{13}
\]

All amplified analytic errors have their outward sign: the exact
middle expression minus M_j equals
C_j(log2-ell)+A_(j+1)(q-log3)+(w-log(11/4))>0.
Complete exact data are as follows.

| j | A_(j+1) | D_(j+1) | 10^12 M_j |
|---:|---:|---:|---:|
|1|146|173|24614600652024|
|2|364|421|23559751834478|
|3|769|880|24315412022970|
|4|1530|1741|23513812919456|
|5|2959|3356|24961510738708|
|6|5650|6396|24175419834005|
|7|10715|12116|24289743253172|
|8|20254|22887|24319344511102|
|9|38223|43175|24186831738161|
|10|72074|81393|25181073716428|
|11|135850|153395|24787056827122|
|12|256004|289045|23688895386938|
|13|482379|544613|23767843789027|
|14|908884|1026118|25548281359505|
|15|1712452|1933309|24060245283770|
|16|3226432|3642520|25081357109227|
|17|6078889|6862806|25511157299736|
|18|11453142|12930076|25875470816889|
|19|21578658|24361289|24377935364284|
|20|40655930|45898595|25253987843274|
|21|76599027|86476590|23933606963962|

The minimum occurs at j=4 and equals the bound in (2), strictly
greater than 47/2. Each case contradicts precisely input j+1's
non-strict guard in (1). The first case includes row0 in its prefix;
the last rejects at input22. Thus no least positive j exists in
1,...,21, proving the stated implication.

Later allocations are arbitrary throughout: only their full budget
and their endpoints enter the cap. In particular b_24=0 (closing
tail2), zero intermediate later allocations, and allocation of every
unit to a single recipient are covered by the same proof. No endpoint
is dropped or allocated twice. No conclusion about the possible
support on rows22-24 is assembled here. Adding H guards would retain
the implication, but is unnecessary for this approved target.

### Finite evidence and limitations

Run `python3 scripts/postspell-word-count/certify_d35_earlier_recipients.py`.
The full certificate is
`scripts/postspell-word-count/d35-earlier-recipients-certificate.json`.
It records the canonical table/hash, changed table, cap operands,
all 41 exponential terms, separated offset operands, all incoming
prefixes, all 21 exact margin operands and 502 comparison records.
There are zero failed comparisons and zero parameter samples.
The load-bearing constants, uniform offsets and complete margin array
were inspected in full. Finite data match the independently audited
subsets of L084; that match does not apply its failed full package.

The quantified argument, rather than sampling or a stored pass flag,
provides full-simplex coverage. The construction evidence is independently
checked in the audit below. The conditional premise b_0=0
has not been established at d35. Both d0 witnesses, Attempt032 and
unfinished work are preserved. Other support, order exhaustion, entry,
realization, actual-word transfer, unrestricted cycles, divergence
and universal eventual descent remain unresolved.

### Independent critical audit — 2026-10-25, step474

This RESEARCH/REPRODUCTION audit uses the prior SPECIALIZE assessment
`drafts/literature/2026-10-25-l103-conditional-support-critical-audit.md`.
It found no defect in the conditional implication, its quantified
coverage or its exact evidence. This verifies an existing local input;
it adds no support exclusion beyond the statement above and makes no
originality claim. The following checks supersede pending-audit wording.

Run `python3 scripts/postspell-word-count/audit_d35_earlier_recipients.py`.
Complete evidence is saved in
`scripts/postspell-word-count/d35-earlier-recipients-audit-certificate.json`.
The audit neither executes nor imports the constructor. It independently
transcribes all 25 L055 pairs and compares them with the canonical table,
changes only H_0,H_24, and reconstructs all incoming prefix sums by direct
summation. It recomputes the complete changed table, invariant totals,
cap, 41 exponential terms, 22 offset records and all 21 margin records.
Every printed margin row agrees. All 502 construction comparisons are
checked against freshly reconstructed operands, relation, difference and
verdict, with exact key sets and unique names. The source hashes match.
There are 3668 matching leaf comparisons and 672 successful proof or
container checks, with zero failures. These counts include repeated data
and schema checks; they are not counts of distinct mathematical claims.
No allocation is sampled and the construction certificate is unchanged.

For an independent check of the analytic imports, the audit applies the
already assessed positive-real remainder formula to 120 terms at 2,3/2
and 11/4, retaining every rational term and remainder. With
z=(x-1)/(x+1), the lower sum is
2 sum_(k=0)^119 z^(2k+1)/(2k+1) and the upper remainder is
2z^241/[241(1-z^2)]. Each z lies strictly between zero and one.
The resulting bounds verify ell<log2, log3<q using log3=log2+log(3/2),
and log(11/4)<w. For intervals [a,b] at 2 and [c,d] at 3/2,
the Lambda interval is
[(N-K)a-Kd,(N-K)b-Kc], where N-K=232565518>0.
Its complete rational endpoints lie strictly inside
(10584/10^14,10585/10^14). Thus the tiny positive lower bound survives
all amplified errors; it is not inferred from rounded log constants.
The exponential recurrence t_0=1,t_k=24t_(k-1)/k reconstructs (7),
whose positive omitted terms give the strict exp24 lower comparison.
These are applications of the cited analytic inputs, not new series proofs.

For the quantified cap, n_i>=47 and 0<eta_i<kappa make every ratio
and logarithm in (5) legitimate. Multiplying all 25 endpoint ratios
telescopes exactly because n_25=n_0. The tail contribution is the full
50+18B for every integer allocation, so neither a later support choice
nor closing tail2 changes Lambda. All 24 nonzero-index guards yield the
same valid E upper bound because J_i>=J_1=15. Direct arithmetic verifies
lambda-E>0 and the printed R<U<exp24 sum. No auxiliary root or minimum
condition enters this cap. It remains usable independently of L084's
failed full certificate conjunction.

For each least positive j in 1,...,21, the conditional b_0=0 and
minimality force exactly the preceding tails to equal 2; integrality
forces a_j>=20. The tail2 offsets are bounded by -81/352 for rows0--20.
Only rows1--21 need the tail20 offset, and their H>=72 bound proves
the required sign. The failed row0 tail20 value Q_0=817/88 is retained
and never invoked as a passing test. Positivity of G_i s_i-Q_i follows
from n_i+eta_i>0 at the actual input, justifying tail monotonicity before
dropping the negative offsets. Thus (10) concerns the actual coordinates,
and its product has precisely A_(j+1),D_(j+1)+18. No later coordinate
is compared with a fictitious trajectory.

At j=1 the prefix includes row0 and the rejection is at input2, with
(A,D)=(146,173); at j=21 it includes rows0--20 before the recipient
and rejects at input22, with (A,D)=(76599027,86476590). These cases
are included in the complete exact margin array. Positivity of A and C
validates every outward sign in (13). The unique minimum remains at j=4,
734806653733/31250000000>47/2, so strict rejection contradicts each
non-strict own-input J guard. Arbitrary later budgets, zero later
allocations and b_24=0 remain covered by the same cyclic identity.

No repair, narrowing or dependency change was needed. b_0=0 is still
assumed; no H guard, minimum, seed, integrality of junctions, realization
or primitive period was introduced. Row0 elimination, assembly, transfer
and universal descent remain outside this audit. Attempt032, both d0
witnesses and prior unfinished work are preserved.

## Mathlib

Full matching coverage is unchecked, not known absent. Supporting affine,
logarithm, exponential and rational arithmetic results are not themselves
a matching theorem for this conditional table statement. No Lean
verification is claimed.
