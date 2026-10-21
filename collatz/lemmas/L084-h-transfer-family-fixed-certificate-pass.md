# L084 — Fixed sufficient-test pass over the H-transfer family

## Hypotheses

For an integer 1<=d<=37, take all 25 indexed pairs of L055, changing
only H_0 to 40-d and H_24 to 32670621+d. Every J is unchanged.
Set r=25, B=9250245 and tau=2. Use C077a's definitions of the
endpoint/domain/non-strict own-input J subsystem, arbitrary cyclic
orders and nonnegative integer allocation simplex sum b_i=B.
The additional own-input H guards are

\[
0<\log s_i+J_i\log(27/16)-H_i\log2
\]

at each outgoing indexed row, in its chronological position. All
logarithms are natural. There is no minimum, seed, integrality,
parity, residue, exact-valuation or primitive-orbit premise.

For the certificate calculation use exactly the constants and finite
rule in the prior SPECIALIZE assessment
`drafts/literature/2026-10-19-h-transfer-family-sufficient-tests.md`.
In particular put kappa=23/11, lambda_-=10584/10^14,
lambda_+=10585/10^14, ell=693147180559/10^12,
u=1098612288669/10^12, v=1011600911679/10^12. The independent
O/S/C choices have T^O=27, v^O=2 and T^S=T^C=24,
U^S=U^C=20000000000, e^C=2; their other constants are the
corresponding ell,u,v,lambda values. For H choose lambda_H=lambda_-,
U_H=20000000000, T_H=24, ell_H=ell and u_H=u.

Independently for C at t=2 and H at m=1 set

\[
w_d=10^8(2/3)^{d-1},\quad L_0=1,\quad
L_i=w_d2^{i-1}\ (1\le i\le24),\quad
Q_d=\kappa\sum_{i=0}^{24}1/L_i.
\tag{1}
\]

Use the complete finite sum in (1), the actual L_* for H, 100-term
outward logarithm bounds and degree-40 exponential lower sums. No
certificate optimization or precision escalation is included.

## Conclusion

For d=1,2,3,4 every independent C077a O/S/C test and every additional
L083 cap test passes. Row18's rational H upper bound is negative:

| d | F_18, required <=0 |
|---:|---:|
|1|-457745289/50000000000|
|2|-41462001389/100000000000|
|3|-410042561/500000000|
|4|-122555023011/100000000000|

Thus for each of these four tables the endpoint/domain/J/H real
subsystem is infeasible over every cyclic order and the full integer
allocation simplex. Consequently any full L051 system containing that
subsystem is infeasible. The d=1 conclusion duplicates C082a/L083;
d=2,3,4 are additional finite table specializations.

The fixed comparison stops for d=5,...,37. Every such table fails
the S row0 tail-20 offset test. In addition d=34,...,37 fail both
fixed normalized cap tests and d=36,37 fail the O row0 offset test.
No other tested data inequality fails, and no enclosure is inconclusive.
These failures give **no feasibility verdict**, and negative F values
without all prerequisites are not exclusions.

This is local RESEARCH/REPRODUCTION: new local finite certificates by
specializing existing criteria, not a new general theorem beyond the
inspected affine/analytic machinery. The separate critical audit below found
no defect in this fixed finite scope.
Both original d=0 rational witnesses, Attempts 026–031 and every
universal eventual-descent gap remain unchanged. There is no claim of
arbitrary-table coverage or integer/parity/exact-valuation/primitive
realization, and this is not a complete Collatz candidate.

## Proof

### Imported mechanism and analytic coverage

Import the audited implications of C077a and L083; no general criterion
is reproved. Their upstream formal-affine input is Halbeisen–Hungerbuehler,
*Optimal bounds for the length of rational Collatz cycles*, Acta Arith.
78 (1997), 227–239, DOI 10.4064/aa-78-3-227-239,
[section 2, equations (2)–(4), Lemma 2, pp. 228–229](https://www.math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
Use only formal real affine algebra; the positive Lambda below supplies
its nonzero denominator. Integer rows specify finite nonempty words,
without asserting integer itinerary realization.

Reuse exactly L079 (2)'s rational remainder scheme for x=2,3,11/4:
with z=(x-1)/(x+1), retain
2 sum_(k=0)^99 z^(2k+1)/(2k+1) and upper remainder
2z^201/[201(1-z^2)]. Its assessed inputs are
[DLMF 4.6.4](https://dlmf.nist.gov/4.6.E4) and
[4.2.19](https://dlmf.nist.gov/4.2.E19); positive arguments satisfy
their hypotheses. Positive exponential partial sums through degree 40
are lower bounds at 24 and 27. No analytic input is reproved.
All series terms and amplified interval endpoints are saved in the
certificate specified below, with exact rational arithmetic.

For every d, the opposite H changes preserve sum H=199390205,
sum J=66061058, K=397573379 and N=630138897. The actual tails
sum to 2r+18B=166504460. Both varying outgoing tails remain in
the closing product. The freshly computed intervals certify

\[
0<\lambda_-<\Lambda<\lambda_+<1,\quad
0<\ell<\log2,\quad \log3<u,\quad\log(11/4)<v<2.
\tag{2}
\]

These are also the matching L079 enclosures. Only the incoming
prefixes change; invariant totals alone do not certify them.

### Every O/S prerequisite for the successful members

For d=1,...,4 all H_i>=36. Thus every negative O offset is certified by

\[
81/44-(3/11)(3/2)^{36}<0.
\]

Every early S offset passes because

\[
Q_i\ge(12/11)(3/2)^{36}+1
=450284094869558387/188978561024
>24117248/11=\kappa2^{20}.
\tag{3}
\]

The O cap, support residual E=552/(4*2^60-23), and support root
cap are identical to L079, with the same independent constants:
23r/(11lambda_-)+kappa<500000000000<P(27),
E<lambda_-, and kappa/(lambda_--E)+kappa<20000000000<P(24).
Here P(T)=sum_(k=0)^40 T^k/k!<exp(T). The constructor also checks
these exact inequalities separately for every member.

Write A_i(d),D_i(d) for the literal incoming tail-2 exponents.
For 1<=i<=24, only row0's H change occurs in that prefix, so
A_i(d)=A_i(1)-(d-1) and D_i(d)=D_i(1)-(d-1).
The empty prefix is unchanged. Hence every O displacement margin
with k>=1 and every S next-input margin equals its L079 d=1 value
plus (d-1)(u-ell). The O k=0 margin is unchanged. Since u>ell,
all required margins are strictly positive. Exact finite evaluation gives

\[
\min_{1\le d\le4,k}M_k^O=629441541677/50000000000>12.58,
\quad
\min_{1\le d\le4,j}M_j^S=2431999810929/250000000000>9.72.
\tag{4}
\]

This retains all 24 displacement tests and all 23 recipient tests;
it does not assume growth of any arbitrarily allocated later row.

### Independent cutoff and H incoming certificates

For every tested d, eta_0>=eta(J=8,H=3)>2. Since
J_24>=J_0 and H_24>=H_0, monotonicity of both subtracted powers
in C077a's eta formula gives eta_24>=eta_0>2. These comparisons
are exact rational bounds; they do not require expanding the final
row's powers. The uniform domain lower bound is unchanged:
2(1-lambda_+)/lambda_+=39999999995766/2117>47.

At either package's specified t, row0's multiplier is exactly

\[
c_0(d)=\frac{3^{63}}{2^{73}}(2/3)^{d-1}>w_d.
\tag{5}
\]

Rows1,...,23 have unchanged pairs with J>=15,H>=72 and actual
tails at most 38 (38 in C, 20 in H at row23). Each therefore has
c_i>=3^117/2^170>2, the matching L079 comparison. Independently
the certificate encloses log(c_i/2) using the full A and D exponents
for every one of these factors in both packages; every lower endpoint
is positive. Induction from C_0=L_0=1 proves every incoming
C_i(t)>=L_i, including i=24. Row24's compensating tail belongs
to closure, not to these incoming products.

The actual minimum L_* is 1 for all 37 members: the exact rational
w_37>1 is the smallest w_d, and L_i>=w_d for i>=1. In particular,
with the complete finite reciprocal sum, the two required caps are

\[
R_C(d)=Q_d/\lambda_-+Q_d+\kappa/L_{24},\qquad
R_H(d)=Q_d/\lambda_-+Q_d+\kappa.
\tag{6}
\]

For d=1,...,4 the maximum R_H is at d=4 (Q_d increases as w_d
decreases), and exact substitution gives

\[
R_C(d)\le R_H(d)\le
385875994128308515163014926269/19532705955840000000
<19800000000<20000000000<P(24).
\tag{7}
\]

Thus each independent C/H cap passes with its fixed U and T.
No C cap is substituted for H's different denominator L_*.

At C's t=2 the actual tails are a_23=38,a_24=166504376.
Both incoming exponents at row24 decrease by d-1 from L079's
values 271907920 and 306970783. Therefore the cutoff margin is

\[
F^C(d)=-2102267684691/500000000000-(d-1)(u-\ell)<-4.20.
\tag{8}
\]

Equations (2)–(8), the table domains and the strictly increasing J
values verify every C077a test for d=1,...,4. Its implication leaves
only literal cyclic order, no early support, and t=0 or 1 after
normalization at indexed row0. No existence assertion is used.

### H rejection and exact matching

H's incoming lower bound uses t=m=1, with a_23=20 and
a_24=166504394. Its H upper expression uses the smaller denominator
exponent at t=0, exactly as L083 requires. For row18 the unchanged
parameters are J_18=693015,H_18=3295208. At d=1 its incoming
exponents are A_18=6078923,D_18^0=6862840; both decrease by d-1.
Thus direct substitution in L083 (4) gives

\[
F_{18}(d)=-457745289/50000000000-(d-1)(u-\ell),
\tag{9}
\]

which yields the four negative values in the conclusion. The complete
certificate also evaluates all 25 F_i for all 37 members, without
allowing an H rejection to override a failed prerequisite.

Now apply L083 with all independent C077a and additional H tests
just verified, for each d=1,...,4. Every endpoint/domain/J/H tuple
would normalize at indexed row0 to one of the two unique cyclic roots.
Its own row18 H margin is strictly below F_18(d)<0, contradicting
that row's strict H guard. L083 transports each outgoing row, tail
and input through both cyclic cuts; no minimum or seed invariance is
assumed here. This proves precisely the asserted real-subsystem exclusion.

### Failures and the limit of this pass

For d=5,...,37 the actual row0 offset datum decreases with d and
already at d=5 equals

\[
Q_0=(12/11)(3/2)^{35}+1
=150094729786279633/94489280512<24117248/11.
\tag{10}
\]

Thus the required S test Q_0>kappa2^20 fails throughout that range.
This is an exact failed table-data hypothesis, not a log-enclosure issue.
The other failed tests in this fixed pass are exhaustively recorded below.
The integer intervals are outward bounds obtained by exact integer division;
the certificate retains the full rational operands and differences.

| d | R_C, required <=20000000000 | R_H, same requirement |
|---:|---:|---:|
|34|[20011074610,20011074611)|[20011074612,20011074613)|
|35|[20138923465,20138923466)|[20138923467,20138923468)|
|36|[20330696747,20330696748)|[20330696749,20330696750)|
|37|[20618356671,20618356672)|[20618356673,20618356674)|

The O row0 offset is 81/176 at d=36 and 81/88 at d=37,
both positive instead of negative. All remaining data tests pass under
the fixed rule; all members have F_18<0, but (10) prevents invoking
the sufficient mechanism for d>=5. No alternative constants, new
arithmetic diagnostic or larger family is tested.

### Reproduction and verification scope

Run `python3 scripts/postspell-word-count/certify_h_transfer_family.py`.
The complete certificate is
`scripts/postspell-word-count/h-transfer-family-certificate.json`.
It includes the source table/hash, all 37 complete changed tables,
all analytic terms and remainders, independent O/S/C/H operands,
prefix factor intervals, every incoming bound and reciprocal, every
F_i, and 21238 exact comparisons (574 per member), retaining all
failed and inconclusive verdicts. There are 43 failed comparisons:
33 S offsets, 8 caps and 2 O offsets; these are the informative method
failures above, not defects to be silently removed. No interval is
inconclusive. Separate report bounds check the numerical bounds (4),
(7), (8), positivity of every incoming-factor interval and L_*=1.
The construction alone is not an independent critical audit. The audit
below separately verifies its complete evidence; a preview or stored
success flag alone is not verification.

### Independent critical audit — 2026-10-19, step 337

This RESEARCH/REPRODUCTION proof audit uses the unchanged SPECIALIZE
assessment `drafts/literature/2026-10-19-h-transfer-family-critical-audit.md`.
It found no defect in the four exclusions, the complete fixed-rule pass
or its 43 failed comparisons. This verifies an existing local input;
it adds no table exclusion or theorem beyond the source machinery cited
above. The d=1 result remains a duplicate, and d=2,3,4 remain finite
specializations. Attempt 032's stop for d>=5 is unchanged.

**Independent reconstruction.** Run
`python3 scripts/postspell-word-count/audit_h_transfer_family.py`.
The audit reads the construction certificate but neither imports nor
executes its constructor. Its separate transcription of all 25 L055
pairs matches the canonical table and source hash. For each d it changes
exactly H_0,H_24, then independently sums the row exponents and rebuilds
all mathematical certificate fields. Its complete evidence is
`scripts/postspell-word-count/h-transfer-family-audit-certificate.json`.
All 354310 recursive leaf comparisons and 2086 further proof/report
checks pass, with zero mismatches. These include repeated comparisons
of stored checks within their containing tables; they are not counts
of distinct mathematical claims. Every one of the 21238 construction
comparisons is checked with freshly computed operands, relation,
difference and verdict. Unique comparison names and exact key sets
prevent omitted or duplicated tests. The stored order is used only to
present the verified comparisons. All 37 tables, all 925 H bounds,
and all 43 mathematical failures are retained, with no inconclusive
interval. The construction certificate is unchanged.

**Analytic errors and domains.** Successive rational powers independently
regenerate all 300 logarithm terms, their three remainders and both
endpoints. Their z values are 1/3,1/2,7/15, within the assessed
positive-real series domain. The already justified L079 (2) remainder
starts at exponent 201; positivity gives a strict lower bound and the
geometric remainder gives the strict upper bound. The exponential
recurrence t_0=1, t_k=T*t_(k-1)/k regenerates all 82 terms through
degree 40 at T=24,27. Positive omitted terms justify the strict lower
sums. These are applications of the cited series, not new analytic
inputs. Every ell,u,v comparison and both intermediate exponential
thresholds in the written proof pass exactly.

The totals freshly give K=397573379,N=630138897 for every member.
Since both coefficients are positive, the lower Lambda endpoint uses
N times the lower log2 endpoint minus K times the upper log3 endpoint;
the upper endpoint uses the opposite choices. All amplified errors
are retained. As a second evaluation, 120-term intervals [a,b] for
log2 and [c,e] for log(3/2) give

\[
232565518a-397573379e<\Lambda
<232565518b-397573379c.
\]

Both new endpoints lie strictly inside the original interval and
between lambda_- and lambda_+. This uses N-K=232565518>0 and
log3=log2+log(3/2), with the same assessed positive-real analytic
coverage. The audit also stores complete rational outward-error bounds
for every F_i: for coefficients P=A_i+3J_i and R=D_i^0+4J_i+H_i,
its excess over the logarithmic expression is
P(u-log3)+R(log2-ell)>0. Both coefficients and both error signs
are checked at all 925 rows. No rounded decimal certifies a sign.

**All O/S hypotheses.** Each table has integer r=25, B=9250245,
tau=2, strictly increasing J_i>=8 and H_i>=3. All 25 order offsets
and 23 support offsets use the correct monotone enclosure at
min(H_i,72); every failing enclosure occurs at row0, where it is
the exact offset. No failed lower bound is misreported as an actual
offset failure elsewhere. All 24 displacement margins and all 23
next-input margins are reconstructed with their own indexed J and
the complete incoming prefixes, including the empty prefix.
The prefix shift is exactly -(d-1) in both exponents for 1<=i<=24,
and zero at i=0. Thus the stated O/S margin shifts have the claimed
sign. The residual E uses J_1=15, not J_0; its positive residual and
root cap are separately checked. The quoted minima (4) match exactly.
No other O or S test is omitted for this positive budget.

For d<=4 every H_i>=36, and (3) is a verified lower bound for
every early Q_i. For d>=5, the exact row0 Q already falls below
the required 24117248/11 at d=5 and decreases thereafter. Thus
all 33 S failures are actual prerequisite failures. The O offsets
are strictly negative through d=35; their two exact positive values
at d=36,37 match the displayed 81/176 and 81/88. These are data
failures, with no conclusion about feasibility of the corresponding
endpoint systems.

**Separate C/H packages and closure.** For each d the fresh factorization
eta_0=kappa-(16/27)^8(12/11+(2/3)^(40-d)) proves eta_0>2;
the independently checked minimum at H=3 suffices as well. Both
subtracted factors are nonincreasing in J,H, so the verified
J_24>=J_0,H_24>=H_0 give eta_24>=eta_0. This is a valid endpoint
bound without expanding the enormous final-row powers. The positive
e=2 and the exact lower domain 39999999995766/2117>47 match
C077a's unconditional cutoff tests.

C's actual row23/row24 tails are 38/166504376 and H's are
20/166504394. Both lists have total tail 166504460 and complete
denominator exponent N. Every tail is at least 2 and is 2 modulo 18.
The exact row0 multiplier exceeds w_d for all 37 members. For every
row1 through row23, in each package, the full rational interval for
log(c_i/2) is strictly positive, with all amplified exponents retained.
The common lower comparison 3^117/2^170>2 is also checked. This
uses the actual tail 38 or 20 at row23, not a tail-2 surrogate.
Multiplying these positive bounds proves C_i>=L_i at every incoming
index 0 through 24. No bound is imposed on C_25=exp(-Lambda)<1;
that full product remains in the fixed-point denominator.

The finite reciprocal sum is exactly
1+(2/w_d)(1-2^(-24)), independently of any infinite-sum estimate.
Every w_d>1, so the actual L_*=1 is checked before use. C uses
L_24 in its last cap term, while H uses L_*=1. The independently
reconstructed caps reproduce (7) and all eight failed cap intervals
for d=34,...,37. All other cap comparisons pass. The boundary margin
at t=2 is precisely (8), strictly negative for all 37 members;
its incoming exponent includes the extra 36 halvings. This successful
boundary test never cancels a failed O, S or cap prerequisite.

**Uniform H and application matching.** Every F_i is rebuilt using
the t=0 incoming denominator exponent and that row's own J,H.
The incoming lower bounds instead use the largest survivor m=1,
including its extra 18 halvings at row23. L083 proves the relevant
directions: C_24(t) decreases with t, while replacing D_24(t) by
D_24(0) increases the H upper bound. Other incoming prefixes do
not vary with t. Both varying outgoing tails remain in the full
product. Fresh row18 summation at d=1 gives A=6078923,D^0=6862840
and coefficients 8157968,12930108; (9) and all four quoted F_18
values match exactly. All members have F_18<0, but only d=1,2,3,4
pass the full prerequisite conjunction. Those are exactly the four
licensed L083 invocations; d>=5 obtains no exclusion from this pass.

For any alleged tuple at a licensed table, C077a applies first to
its endpoint/domain/non-strict J subsystem. It gives literal cyclic
order, zero early support and the integer range t=0,1. Only then
normalize at the position z of indexed row0, moving the complete
outgoing row, its tail and its own input together. The old closing
edge becomes edge 24-z; the new closing edge starts at old z-1
modulo 25. This preserves both cuts, also at z=0 or z=24, and
preserves each strict H guard at exactly its own input. L077's
nonzero-denominator uniqueness identifies the normalized endpoints
with the survivor root used by L083. Its strict upper H estimate
then contradicts row18's strictly positive required margin. No
minimum, seed, survivor existence or integer-realization premise is
introduced by this matching.

L055/L065's d=0 witness scopes are different and remain unaffected;
they are imported controls, not recertified by this audit. Attempts
026–032 retain their conclusions. The DAG's direct inputs remain
accurate, and the mathematical argument has not changed, so neither
the DAG nor PROOF.md is edited for audit status alone. The canonical
audit here supersedes their older pending-audit prose for L084.
Arbitrary tables, other cycles, entry, divergence and universal eventual
descent remain unresolved. There is no complete Collatz candidate.

## Mathlib

Full matching coverage for this finite family certificate has not been
checked. Supporting logarithm, exponential and finite rational-sum facts
do not constitute a matching table theorem; unknown coverage is not
absence. No Lean verification is claimed.
