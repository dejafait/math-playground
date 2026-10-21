# L079 — One redistributed-H table passes the C077a data tests

## Hypotheses

Take L055's complete indexed 25-row pair table, replacing only
H_0=40 by 39 and H_24=32670621 by 32670622. Every J and every other H
is unchanged. Set r=25, B=9250245 and tau=2. Use the definitions and
the three independent sufficient-test sets of C077a, with natural
logarithms and kappa=23/11. This specifies data, without assuming
any feasible junction tuple, integer realization or actual Collatz word.

## Conclusion

This changed table satisfies **every** O, S and C data test of C077a.
For the certificate choices below, the exact minimum O and S rational
margins and the C boundary margin are respectively

\[
\min M_k^O=\frac{629441541677}{50000000000}>12.58,
\quad \min M_j^S=\frac{2431999810929}{250000000000}>9.72,
\quad F^C=-\frac{2102267684691}{500000000000}<-4.20.
\tag{1}
\]

Consequently, C077a applies to this table over the full nonnegative
integer allocation simplex of budget B and every cyclic order. Any
tuple satisfying its endpoint/domain/non-strict own-input J subsystem
has literal cyclic order; after normalization at indexed row 0 it has
b_0=...=b_22=0, b_23=t, b_24=B-t and t in {0,1}.

This is a necessary reduction only. Neither survivor is asserted
feasible or infeasible. No survivor nondivisibility, integer-cycle
exclusion, actual-word application or universal eventual descent follows
from these data tests alone. The fixed-table witnesses and Attempts
026–031 remain valid. This is local REPRODUCTION under the prior
SPECIALIZE assessment
`drafts/literature/2026-10-18-redistributed-h-table-data-tests.md`,
without an originality claim beyond the sources checked. The separate
critical audit below found no defect in this certificate and specialization.

## Proof

### Machinery and exact arithmetic conventions

The implication from the certified tests to the reduction is imported
from C077a, rather than reproved. Its elementary affine machinery is
Halbeisen–Hungerbuehler, *Optimal bounds for the length of rational
Collatz cycles*, Acta Arithmetica 78 (1997), 227–239,
DOI 10.4064/aa-78-3-227-239,
[section 2, equations (2)–(4), Lemma 2, pp. 228–229](https://www.math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
The prior assessment inspected its finite-word hypotheses and essential
induction cases. Our integer exponents define finite nonempty formal
words. Positive Lambda is certified below before any fixed-point use;
no integer/parity realization converse is imported.

For the analytic certificates reuse the assessed positive-real identities
and series [DLMF 4.5.1](https://dlmf.nist.gov/4.5.E1),
[4.6.4](https://dlmf.nist.gov/4.6.E4) and
[4.2.19](https://dlmf.nist.gov/4.2.E19). To make all numerical bounds
reproducible without source-dependent decimal rounding, for each
x in {2,3,11/4} put z=(x-1)/(x+1), m=100 and

\[
L(x)=2\sum_{k=0}^{99}\frac{z^{2k+1}}{2k+1},\qquad
R(x)=\frac{2z^{201}}{201(1-z^2)},\qquad U(x)=L(x)+R(x).
\tag{2}
\]

Here 0<z<=1/2. The logarithm series has positive omitted terms;
bounding each omitted denominator below by 201 and summing the
geometric series gives L(x)<log(x)<U(x). This is a remainder
justification for the existing series, not a new logarithm theorem.
All terms in (2) are exact rationals.

Recomputed table totals give sum J=66061058, sum H=199390205,
K=397573379, N=630138897 and total tails 2r+18B=166504460.
In particular the H changes cancel in the totals, but not the prefixes.
Put S=10^12 and choose

\[
\lambda_-=10584/10^{14},\quad \lambda_+=10585/10^{14},
\quad\ell=693147180559/S,\quad
u=1098612288669/S,\quad v=1011600911679/S.
\tag{3}
\]

Exact substitution into (2), retaining the cancellation-sensitive
products with N and K, gives

\[
0<\lambda_-<NL(2)-KU(3)<\Lambda
<NU(2)-KL(3)<\lambda_+<1,
\]
\[
0<\ell<L(2),\qquad U(3)<u,\qquad U(11/4)<v<2.
\tag{4}
\]

These are freshly checked series bounds, not transferred old margins.
For T=24 and 27 let P(T)=sum_(k=0)^40 T^k/k!. The positive
exponential series gives P(T)<exp(T). Direct rational comparisons give

\[
20000000000<P(24),\qquad
500000000000<P(27).
\tag{5}
\]

The complete terms, remainder bounds, exact rational operands and
sign checks for (2)–(5) are retained in
`scripts/postspell-word-count/redistributed-h-table-certificate.json`.
They can be regenerated with
`python3 scripts/postspell-word-count/certify_redistributed_h_table.py`.
No floating-point arithmetic is used anywhere in this certificate.

### O: minimum cap, all offsets, all first displacements

Choose lambda^O=lambda_-, T^O=27, ell^O=ell, u^O=u, v^O=2.
The cap is exactly

\[
\frac{23r}{11\lambda_-}+\kappa
=\frac{7187500000030429}{14553}
<500000000000<P(27)<e^{27}.
\tag{6}
\]

Every H_i>=39. Since 3/2>1, every required offset satisfies

\[
d_i\le\frac{81}{44}-\frac3{11}(3/2)^{39}<0.
\tag{7}
\]

Compute A_k=sum_(i<k)(3J_i+H_i) and
D_k=sum_(i<k)(4J_i+H_i+2) from the **changed** table. Then
M_k^O=4J_(k+1)ell-27-2-A_k u+D_k ell.
All 24 margins, including the empty and final displacement prefixes,
appear in the exact table below. Their minimum is (1).

### S: residual cap, every early offset and every next input

Here B>0, so none of the support tests is optional. Choose
lambda^S=lambda_-, U^S=20000000000, T^S=24,
ell^S=ell, u^S=u and v^S=v. The unchanged J_1=15 gives

\[
E=\frac{552}{4\cdot2^{60}-23}<\lambda_-,
\]
\[
\frac{23}{11(\lambda_--E)}+\kappa
=\frac{1325859730438202850942226985830949}
       {67113790726173775832193}
<20000000000<P(24)<e^{24}.
\tag{8}
\]

Every early H_j>=39 (j=0,...,22), so each of the 23 offset tests
follows from the exact common lower bound

\[
Q_j\ge(12/11)(3/2)^{39}+1>\kappa 2^{20}.
\tag{9}
\]

For every j=0,...,22 compute
M_j^S=(D_(j+1)+18+4J_(j+1))ell-24-v-A_(j+1)u.
All 23 margins are tabulated below. The minimum occurs at j=4
and equals (1). Thus all early recipients, including zero and r-3,
are covered, without a premise about later tail growth.

The following entries are **integers** S*M_k^O and S*M_k^S.
The dash is the absent support index 23, not an omitted test.

| k or j | S*M^O | S*M^S |
|---:|---:|---:|
|0|12588830833540|10441049166583|
|1|30019654217268|10828786976284|
|2|60905867971565|9773938158738|
|3|120847971043211|10529598347230|
|4|232507180121143|9727999243716|
|5|445194912629801|11175697062968|
|6|843122797728801|10389606158265|
|7|1593708250550054|10503929577432|
|8|3007842822309581|10533530835362|
|9|5672330185636307|10401018062421|
|10|10693355848832762|11395260040688|
|11|20151650222358025|11001243151382|
|12|37970683923279491|9903081711198|
|13|71545635188117267|9982030113287|
|14|134805098423055932|11762467683765|
|15|253986605085940870|10274431608030|
|16|478537077663758775|11295543433487|
|17|901607411901575472|11725343623996|
|18|1698704918634838093|12089657141149|
|19|3200497372468540298|10592121688544|
|20|6029997525870426065|11468174167534|
|21|11360998912779618527|10147793288222|
|22|21405032949345317535|11664264289744|
|23|40328770408750078677|—|

### C: both eta bounds, all incoming prefixes and the cutoff boundary

Choose lambda_-^C=lambda_-, lambda_+^C=lambda_+ and e^C=2.
The changed first row gives exactly

\[
\eta_0=\frac{2374185650978801216525801124919}
                    {1144561273430837494885949696427}>2.
\]

Both subtracted bases in eta_i are in (0,1). Since J_q>=J_0
and H_q>=H_0, eta_q>=eta_0>2. Thus this is a lower certificate
for both required rows, including the changed final H. Moreover

\[
\frac{2(1-\lambda_+)}{\lambda_+}
=\frac{39999999995766}{2117}>47.
\tag{10}
\]

At tau=2 the two final tails are a_23=38 and a_24=166504376;
all preceding tails are 2. Their sum is the full budget tail sum.
The changed row 0 multiplier is **3^63/2^73**, not the old
3^64/2^74, and exact integer comparison gives c_0>10^8.
For 1<=i<=23, J_i>=15, H_i>=72 and a_i<=38. Hence

\[
c_i=(27/16)^{J_i}(3/2)^{H_i}2^{-a_i}
\ge3^{117}/2^{170}>2.
\tag{11}
\]

Define L_0^C=1 and L_i^C=10^8*2^(i-1) for 1<=i<=24.
Starting from C_0=1, multiplication of (11) and the row-0 lower
bound proves 0<L_i^C<=C_i(tau) at all 25 incoming inputs.
This proof uses the actual tail 38 at row 23; row 24's large tail
is retained in the total Lambda and closing endpoint and does not
belong to an incoming prefix C_i with i<=24.

Choose

\[
Q^C=\kappa(1+2/10^8),\qquad
U^C=Q^C/\lambda_-+Q^C+\kappa
=\frac{435606069410390910013}{22050000000},\quad T^C=24,
\]

and ell^C=ell, u^C=u, v^C=v. The finite geometric sum gives
sum_(i=0)^24 1/L_i^C<1+2/10^8, so Q^C bounds the full required
inverse-prefix sum times kappa. Since L_24^C>=1,

\[
Q^C/\lambda_-+Q^C+\kappa/L_{24}^C
\le U^C<20000000000<P(24)<e^{24}.
\tag{12}
\]

The recomputed incoming exponents at q=24 are
A_q=271907920 and d_q(tau)=306970783. In particular both
are one less than the old benchmark values. The required last-row
boundary margin is exactly

\[
24+271907920u-(306970783+4\cdot30998279)\ell+v
=-\frac{2102267684691}{500000000000}<0.
\tag{13}
\]

All cutoff tests are therefore certified. This is a boundary-data test;
the full-interval implication for 2<=t<=B comes from C077a's audited
L077 input, not from sampling t or assuming the two varying rows grow.

### Assemble only the stated necessary reduction

The indexed table has strictly increasing J_i>=2 and H_i>=3,
r>=3 and nonnegative integer B,tau. Equations (3)–(13) certify all
three sets on precisely this table and budget, with independently
chosen O/S/C constants. Thus the exact hypotheses of C077a match.
Its conclusion gives cyclic literal order, permits normalization at
indexed row 0 with each outgoing row and its input carried together,
and gives b_0=...=b_22=0 and 0<=t<=B, t<2. Integrality of the
allocation makes the survivor list {0,1}. All closing edges and
non-strict own-input guards remain part of this conditional conclusion.

The reproduction program checks 272 rational comparisons and 13
integer/domain/index conditions with no failures. The full certificate
contains all 25 rows, all 24/23 margin operands, all 25 incoming
prefixes, and the complete analytic evidence. These calculations verify
finite data only; the quantified implication is C077a. No denominator
nondivisibility at either survivor has been tested, and no integer
or actual-word conclusion is assembled. The separate audit below verifies
this local result without strengthening its conclusion.

### Independent critical audit — 2026-10-18, step 305

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-18-redistributed-h-table-critical-audit.md`.
This RESEARCH/REPRODUCTION audit found no defect. It verifies a local
input, not a new general theorem or a complete Collatz candidate. The
approved scope is precisely the changed table, every O/S/C data test,
and the necessary reduction stated above. Survivor arithmetic was not
performed. The primary affine and positive-real analytic coverage cited
above is reused; the existing audits of C077a and its criteria are
imported rather than reproved.

**Independent evidence.** Run
`python3 scripts/postspell-word-count/audit_redistributed_h_table.py`.
It reads but neither imports nor executes the constructor and leaves the
construction certificate unchanged. A separately transcribed L055 table
is compared with all 25 source rows, then only the two stated H changes
are made. It independently reconstructs every mathematical certificate
field, every term and remainder, all 272 named rational comparisons and
13 integer/domain/index conditions, and all printed margin entries and
displayed cap/domain constants. The full output is
`scripts/postspell-word-count/redistributed-h-table-audit-certificate.json`:
3905 checks pass with no failures. It contains the exact actual/required
operands, source-certificate hash and separate analytic evidence; its
summary alone is not the verification. All evidence arrays are traversed
in full, including 300 stored logarithm terms, 82 exponential terms,
25 incoming prefixes, 24 O margins and 23 S margins.

**Analytic justification.** The three arguments in (2) give respectively
z=1/3,1/2,7/15, all strictly between zero and one. The omitted terms
start at exponent 201 with denominator 201. Replacing every later
denominator by 201 gives R; some replacements are strictly larger, so
the upper enclosure is strict. Positive omitted terms give the strict
lower enclosure. The audit regenerates terms through a recurrence for
the numerator powers, then checks every stored sum and remainder. With
N,K positive the lower Lambda bound must use the lower log2 and upper
log3, and the upper bound the opposite choices, exactly as in (4).
This sign-sensitive substitution and all rational comparisons pass.

As an independent cancellation check, the audit also computes 120-term
intervals [a,b] for log2 with z=1/3 and [c,d] for log(3/2) with z=1/5,
using the same justified remainder formula with exponent 241. The
positive-real identity log3=log2+log(3/2) gives

\[
(N-K)a-Kd<\Lambda<(N-K)b-Kc,
\]

since N-K=232565518>0 and K>0. Both endpoints lie strictly inside
the construction's exact interval in (4), and hence strictly between
lambda_- and lambda_+. The complete rational endpoints, terms and
remainders are saved in the audit certificate. No floating-point value
or rounded difference certifies Lambda. For the exponential lower
bounds the recurrence t_0=1, t_(k+1)=T t_k/(k+1) independently recovers
every term through 40. Positivity of the infinite remaining terms at
T=24,27 justifies both strict inequalities (5); no upper remainder is
needed. The ell,u,v enclosures and v<2 also pass exactly.

**Order and support.** Every J is increasing with J_0=8, and every
H>=39. Since 3/2>1, (7) is an upper bound for each of the 25 offsets,
and (9) is a lower bound for each of the 23 early Q values. Both common
rational comparisons have the required strict sign. All A_k,D_k are
recomputed from the changed entries, including the empty prefix and
the final first-displacement prefix. All 24 O margins equal the printed
values and are positive; their minimum is exactly (1). Increasing J
and ell>0 make these the weakest tests among all later displaced rows,
as required by the imported L075 criterion. This covers every eligible
first displacement, not a sample of permutations.

Here B>0, so all support tests are mandatory. E uses J_1=15, not the
changed first J; the residual lambda_--E is positive and the exact
root cap is the displayed (8). It is below U^S=20*10^9<exp(24).
The 23 independently recomputed S margins use A_(j+1),D_(j+1), with
the extra 18 in the denominator and the guard of row j+1. They include
j=0 and j=22. Their minimum is the stated value at j=4, strictly
greater than 9.72. There is no support comparison at j=23 to omit.
Every cap and enclosure is matched to its own O or S constants.

**Cutoff and closing edge.** Factoring eta_0 as
kappa-(16/27)^8(12/11+(2/3)^39) reproduces the displayed exact rational
and proves eta_0>2. For eta_q, both factors subtracted from kappa are
positive and nonincreasing in J and H. The actual J_q>=8 and
H_q>=39 therefore give eta_q>=eta_0>2 without expanding huge powers.
The positive e=2 and the domain inequality (10) match all of C077a (4),
with 0<lambda_-<Lambda<lambda_+<1.

At tau=2 the full tail list is 23 copies of 2 followed by 38 and
166504376. Its total is 166504460. Independent sums give K,N as above,
the first multiplier 3^63/2^73>10^8, and incoming exponents
(A_q,d_q)=(271907920,306970783). The final row is absent only from
the incoming prefix; adding its odd exponent gives K and adding its
denominator exponent with its actual tail gives N. Thus closure has
not dropped either changed row or a tail contribution.

For each of rows 1,...,23 the bases 27/16 and 3/2 exceed one,
J_i>=15, H_i>=72 and a_i<=38. These inequalities justify the factored
lower bound (11), checked independently as
(27/16)^15(3/2)^72/2^38>2. Beginning with C_0=L_0=1 and multiplying
positive bounds proves each of the 25 incoming inequalities
L_i<=C_i(tau). In particular the row-23 tail is 38 in the step to
input 24. The complete inverse-prefix sum is exactly

\[
\sum_{i=0}^{24}1/L_i
=1+\frac{2}{10^8}(1-2^{-24})
=\frac{167772163355443}{167772160000000}
<1+2/10^8.
\]

Multiplying by kappa proves the required Q^C bound. All L_i are
positive and L_24>=1, so the required normalized cap is no larger
than the chosen U^C. Its exact value is
80390828282991765264571312031/4069313740800000000; both it and U^C
are verified in the audit. The latter is below 20*10^9<exp(24).
Finally the independently recomputed boundary margin is exactly (13),
strictly below -4.20. All signs and the non-strict own-input guard
convention match C077a; no growth assumption on the varying rows or
sampling of the remaining parameters is used.

**Quantified specialization.** The same table has r=25>=3, integer
B>=0, tau=2<=B and the required pair domains. The preceding checks
exhaust C077a's three data sets, using its permitted independent
constants. For an arbitrary tuple in that corollary's endpoint/domain/J
subsystem, the audited order implication is applied first. Rotation at
the unique occurrence of indexed row 0 then carries each outgoing row,
its allocation and its input together. The old closing edge becomes
edge 24-z and the new closing edge is the old edge z-1 modulo 25;
both exact endpoints and every own-input guard survive. C077a next
removes precisely b_0,...,b_22, and its last-pair implication gives
the integer t=b_23 with 0<=t<=B and t<2. Hence only {0,1} remain
possible. The normalized unshifted input is s_z-kappa, not an assumed
chronological first input or a shifted integer.

Neither possibility is asserted to satisfy the J guards, H guards,
seed, integrality or actual-word requirements. No old numerator residue
is transferred. Both original rational witnesses and Attempts 026–031
remain valid. No new mathematical input was introduced beyond L055's
table and C077a's audited implication, so the DAG is unchanged. The
main argument is unchanged by this no-defect audit; PROOF.md is not
rewritten merely to propagate audit status. The unresolved survivor
nondivisibility and universal eventual-descent gaps remain explicit.

## Mathlib

A full matching theorem for this changed table and certificate has not
been checked in Mathlib. Supporting rational arithmetic and real
logarithm/exponential facts are not a matching C077a instance. No
absence or formal verification claim is made.
