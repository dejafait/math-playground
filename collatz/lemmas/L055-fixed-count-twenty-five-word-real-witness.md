# L055 — Fixed-count twenty-five-word real-system witness

## Hypotheses

Consider exactly L051 (1)–(4) with r=25 and fixed integer counts
K=397573379, L=232565518 and N=630138897. In particular the required
parameters are integers J_i>=2, H_i>=3 and a_i>=0 with a_i=2 modulo 18,
and K=sum(3J_i+H_i), L=sum(J_i+a_i), N=K+L. Positive integers
d,K_0,L_0 must satisfy K=dK_0, L=dL_0 and K_0>225640000. Require
Lambda=N log2-K log3>0 and N<(8/5)K+1725/1034.

The junctions are real numbers s_i>=540/11, with h_i=log s_i,
s_0=min_i s_i and s_25=s_0. The seed and own-index guards are

\[
0<h_0<(133/10)\log N+8+\log25,
\quad 4J_i\log2\le h_i+\log(11/4),
\quad H_i\log2<h_i+J_i\log(27/16).
\]

Writing G_i=(27/16)^{J_i}(3/2)^{H_i}, all 25 endpoints must obey

\[
s_{i+1}=2^{-a_i}\{G_i s_i-(12/11)(3/2)^{H_i}-1\}+23/11.
\]

No integer, residue, parity or valuation realization is required of
the junctions. Independent tails, repeated periods and ties are allowed.
These are the constraints to be witnessed, not an assumed solution.
All logarithms are natural.

## Conclusion

This complete fixed-count real system is feasible. The parameters below
and the exact positive rational junctions defined in (3) satisfy every
constraint, including the closing endpoint and exact total-tail budget.
They have d=1, K_0=K, L_0=L and

\[
18000000000<n_0<s_0<20000000000,\qquad n_i=s_i-23/11.
\tag{1}
\]

Thus no valid consequence of this unchanged real system can exclude
this branch. This is stronger negative evidence about the exclusion
method than L054's failed upper envelope. It is not an integer Collatz
cycle or a counterexample to Collatz: integer/parity/valuation realization
is not established. The restricted actual-cycle exclusion remains through
24, and entry, unrestricted cycles, divergence and universal descent
remain open. The separate critical audit below found no defect within
this exact real-system scope and the stated qualifications.

This is local REPRODUCTION under the prior SPECIALIZE assessment,
not a claim of a new general rational-cycle theorem or of originality
beyond the inspected sources.

## Proof

### Explicit allocation and exact counts

For 0<=i<24 set a_i=2; set a_24=166504412=2+18*9250245.
Choose the following integers.

| i | J_i | H_i |
|---:|---:|---:|
|0|8|40|
|1|15|72|
|2|28|134|
|3|52|249|
|4|98|467|
|5|184|877|
|6|347|1650|
|7|653|3106|
|8|1230|5849|
|9|2317|11018|
|10|4365|20756|
|11|8224|39104|
|12|15494|73672|
|13|29191|138802|
|14|54998|261511|
|15|103621|492705|
|16|195229|928293|
|17|367827|1748976|
|18|693015|3295208|
|19|1305695|6208431|
|20|2460032|11697176|
|21|4634896|22038409|
|22|8732512|41522114|
|23|16452748|78230965|
|24|30998279|32670621|

Their sums are

\[
\sum J_i=66061058,\quad \sum H_i=199390205,
\quad \sum a_i=166504460.
\]

Consequently sum(3J_i+H_i)=K and sum(J_i+a_i)=L, exactly.
In particular sum a_i=N-K-sum J_i is enforced by actual individual
tails with their required congruences. Each J_i>=2, H_i>=3 and a_i>=2.
Take d=1, K_0=397573379>225640000 and L_0=232565518>0.
Direct rational comparison verifies N<(8/5)K+1725/1034.
The certified logarithms below give

\[
\lambda_-:=10584/10^{14}<\Lambda<10585/10^{14}=: \lambda_+<1.
\tag{2}
\]

### Exact cyclic root, with no numerical closure approximation

Use L051's shifted endpoint coordinates. Put

\[
c_i=\frac{3^{3J_i+H_i}}{2^{4J_i+H_i+a_i}},\quad
\eta_i=\frac{23}{11}-\frac{12}{11}(16/27)^{J_i}
                       -(16/27)^{J_i}(2/3)^{H_i},
\quad C_i=\prod_{j<i}c_j,
\]

where C_0=1. For all these parameters 0<eta_i<23/11: the
subtracted terms are positive and their sum is strictly less than
12/11+1=23/11. Define the finite positive rational numbers

\[
B=\sum_{i=0}^{24}\frac{\eta_i}{C_i},\qquad
n_0=\frac{B}{2^N/3^K-1},\qquad
n_i=C_i\left(n_0+\sum_{j<i}\frac{\eta_j}{C_j}\right)
\quad(0\le i\le25),\qquad s_i=n_i+23/11.
\tag{3}
\]

The denominator is positive by (2). The expression for n_i at i=0
agrees with the separately defined n_0. All quantities are finite,
though some integer powers are large; (3) is an exact factored rational
definition, not a numerical approximation.

These are the fixed-word affine rational-cycle formulas. A standard
source is Halbeisen–Hungerbuehler, *Optimal bounds for the length of
rational Collatz cycles*, Acta Arithmetica 78 (1997), 227–239,
DOI 10.4064/aa-78-3-227-239,
[Lemma 2, pp. 228–229](https://math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
The prior assessment inspected the lemma and relevant proof cases.
Here the word has length N and K odd letters. We need only its affine
fixed-point construction, specialized to the shifted blocks; we do not
import integer realization, or reprove the general parity-coding theorem.
The following algebra checks precisely the local specialization.

For each i, (3) gives n_{i+1}=c_i(n_i+eta_i). Substitution of eta_i
and s_i=n_i+23/11 makes this exactly the required endpoint equation.
The integer totals give C_25=3^K/2^N=exp(-Lambda), and (3) implies
B=n_0(C_25^{-1}-1). Hence
n_25=C_25(n_0+B)=n_0, proving exact closure including the last tail.
This does not infer closure from an approximate product or a truncated
orbit calculation.

### Root bounds, the minimum, and the seed

For i<24, a_i=2, so

\[
c_i\ge(27/16)^2(3/2)^3/4=19683/8192>2.
\]

Thus n_1>n_0,...,n_24>n_23>0. It follows that s_0 is the
smallest designated junction and all the lower-height guards follow
once (1) is established. We have made no global-orbit-minimum claim.

The first row gives c_0=3^64/2^74>10^8 by integer comparison and

\[
\eta_0=\frac{7122556955297586891012225981605}
                 {3433683820292512484657849089281}>2.
\]

For 1<=i<=24, C_i>10^8*2^{i-1}. Therefore

\[
2<B<\frac{23}{11}\left(1+\frac{2}{10^8}\right)
  =\frac{1150000023}{550000000}=:B_+.
\tag{4}
\]

The finite geometric sum is strictly less than the infinite sum 2;
all its terms are positive. For 0<x<1, the exponential series yields
x<exp(x)-1<x/(1-x): the upper bound follows by comparing 1/k!<=1
termwise and using strict inequality at k=2. By (2)–(4),

\[
n_0>\frac{2(1-\lambda_+)}{\lambda_+}
 =\frac{39999999995766}{2117}>18000000000,
\]
\[
s_0<\frac{B_+}{\lambda_-}+\frac{23}{11}
 =\frac{95833335250000}{4851}+\frac{23}{11}<20000000000.
\]

This proves (1). In particular all s_i>18*10^9>540/11.
The same rational logarithm procedure used for (2) proves

\[
\log(18*10^9)>23.61,\qquad \log(20*10^9)<24,
\quad (133/10)\log N+8+\log25>24.
\tag{5}
\]

Thus the seed holds, with 0<h_0<24. No part of this argument assumes
that the conditional L054 bounds are attained.

### Every own-index guard

Let S=10^12 and use the following certified strict enclosures:

\[
693147180559/S<\log2<693147180560/S,
\quad 1098612288668/S<\log3<1098612288669/S,
\quad 1011600911678/S<\log(11/4).
\tag{6}
\]

Set E=693147180560, C=1011600911678,
A=523248143764 and T=405465108108. These satisfy
A/S<alpha=log(27/16) and T/S<beta=log(3/2), with A,T>0.
Set v_0=23610000000000 and, for 0<=i<24, define the integers

\[
v_{i+1}=v_i+J_i A+H_i T-2E.
\tag{7}
\]

By (1), (5), log n_0>v_0/S. The exact recurrence, eta_i>0 and
a_i=2 for i<24 give

\[
\log n_{i+1}>\log n_i+J_i\alpha+H_i\beta-2\log2
 >\frac{v_i+J_i A+H_i T-2E}{S}.
\]

Induction proves h_i>log n_i>v_i/S for every i=0,...,24. Notice
that (7) is applied only to the first 24 tails, all actually equal to 2;
the large closing tail is retained in the exact closure proof.

For the displayed parameter table, integer arithmetic verifies, at
every one of the 25 indices,

\[
v_i+C-4J_i E>0,\qquad v_i+J_i A-H_i E>0.           \tag{8}
\]

The minimum first margin is 402427610954 (i=19); the minimum second
margin is 6289114252 (i=18). The last row has
v_24=85945498516173480348, first margin 20763525367066 and second
margin 79519741629507734744. Every v_i and both margins are stored
in the full certificate. Combining (6)–(8) with h_i>v_i/S gives

\[
4J_i\log2<4J_i E/S<(v_i+C)/S<h_i+\log(11/4),
\]
\[
H_i\log2<H_i E/S<(v_i+J_i A)/S<h_i+J_i\alpha.
\]

These are stronger than the required non-strict first guard and give
the required strict second guard. All 25 occurrences, including the
closing word, have now been checked against their own junctions.

### Exact certificate, source qualifications, and scope

Reproduce with
`python3 scripts/postspell-word-count/certify_fixed_count_tail_witness.py`.
The full certificate is
`scripts/postspell-word-count/fixed-count-tail-witness-certificate.json`.
It records the parameter table, prefix product exponents, exact factored
root definition, log enclosures with all rounded terms and remainders,
70 strict rational comparisons and 34 integer/count/recurrence checks.
There are no failed checks. All 25 guard records, every strict margin,
integer checks, exact totals and full root-bound fractions were inspected.

For completeness the logarithm enclosures use L051's integrated
geometric-series certificate, with 96 terms rounded down to multiples
of 2^-192. For t>=1, binary-reduce t=2^k v with 1<=v<2 and set
x=(v-1)/(v+1). The exact identity is

\[
\log v=2\sum_{j=0}^{95}\frac{x^{2j+1}}{2j+1}
       +2\int_0^x\frac{u^{192}}{1-u^2}\,du.
\]

Each positive integral remainder is bounded above by
9/(4*193*3^193), using 0<=x<=1/3; at x=0 the zero remainder
also lies below this positive bound. Adding 96*2^-192 covers the
term-rounding errors. Treat log2 the same way and add k times its
outward interval. For Lambda use N(log2)_lower-K(log3)_upper
and N(log2)_upper-K(log3)_lower. Thus the large cancellation in
(2) is enclosed exactly, not computed with floating-point logarithms.
The displayed constants and strict comparisons are rational. The
certificate's compact margin values are downward roundings of exact
positive margins; full operands remain stored.

The pre-existing assessment is
`drafts/literature/2026-10-11-twenty-five-fixed-count-tail-budget.md`.
The new work is the explicitly identified allocation specialization of
known affine endpoint machinery: placing the complete budget in the
last tail, matching integer totals/congruences, and checking the fixed
root against all individual guards. Merely citing existence of a
rational fixed point would not establish those guards or the seed.
L051 is the mathematical input for the system and shifted coordinates;
L052 and L054 supplied context, not unproved feasibility premises.

For the motivating actual-cycle restrictions, the existing published
qualifications remain: Hercher, *There are no Collatz m-Cycles with
m <= 91*, JIS 26 (2023), Article 23.3.5,
[Theorem 16, pp. 10–11](https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/hercher5.pdf),
and Simons–de Weger, *Theoretical and computational bounds for m-cycles
of the 3n+1-problem*, Acta Arith. 117 (2005), 51–70,
[period conventions p. 52, Corollary 2 p. 53, Lemma 12 p. 61](https://www.impan.pl/shop/en/publication/transaction/download/product/82263).
Their computational height, continued-fraction, Rhin/Crandall and other
published inputs are not reverified here. This witness does not apply
those integer-cycle theorems to arbitrary reals: it directly satisfies
the explicit K_0 threshold in the real subsystem. Its existence does
not certify any actual primitive integer orbit or its repetition count.

### Independent critical audit — 2026-10-11

The audit compared the full statement against L051 (1)–(4), including
log25 in the seed, 69r/1034=1725/1034, the strict/non-strict guard signs,
the lower junction bound and d=1 scaling. It read the previously approved
source comparison and retained its fixed-word affine-coding qualification.
No source theorem about integer cycles was applied to arbitrary reals.
No defect was found. This confirms the negative method verdict, without
adding a new theorem or establishing integer realization.

The symbolic check can be made directly for every index: c_i=2^(-a_i)G_i
and

\[
c_i\eta_i=\frac{23}{11}c_i-
 2^{-a_i}\left(\frac{12}{11}(3/2)^{H_i}+1\right).
\]

Consequently n_{i+1}=c_i(n_i+eta_i) is exactly (not approximately) the
required endpoint after s_i=n_i+23/11. If
T_i=sum_{j<i}eta_j/C_j, then T_{i+1}-T_i=eta_i/C_i and
C_{i+1}=c_i C_i, proving all 25 recurrences in (3). The total exponents
are sum(3J_i+H_i)=K and sum(4J_i+H_i+a_i)=N, so
C_25=3^K/2^N. Thus the positive denominator C_25^(-1)-1 gives
n_25=C_25(n_0+B)=n_0, including the large final tail.
All eta_i are positive because both (16/27)^J_i and (2/3)^H_i lie
strictly between zero and one. The root and every prefix are positive.

For i<24 the bound c_i>=19683/8192>2 is valid, and c_0>10^8
and eta_0>2 were checked as exact rational inequalities. These yield
2<B<(23/11)(1+2/10^8), since every C_i with 1<=i<=24 has
C_i>10^8*2^(i-1). The exponential-series comparison in the proof is
valid for 0<Lambda<1 and yields the displayed root bounds. Strict growth
through n_24 identifies the minimum among the 25 designated inputs;
closure identifies n_25 with n_0, not another input. No bound on all
intermediate parity phases is assumed. The certified root logs give
log n_0>23.61 and h_0<24, while the seed upper bound exceeds 24.

The independent verifier
`python3 scripts/postspell-word-count/audit_fixed_count_tail_witness.py`
reads the literal parameter table in this lemma, not the generator's
greedy choices, and never imports or runs that generator. It recomputes
every count, congruence, prefix exponent, v_i and guard margin. It checks
all 70 original strict comparisons with their full operands/margins,
all 34 original integer checks, all root fractions, all 768 rounded
series terms and each rounding/remainder budget, and all seven complete
log intervals. Thus it does not merely accept saved success flags.

As an independent second enclosure it uses 120 unrounded rational
terms. For x=(v-1)/(v+1) in [0,1/3], the lower sum is
2 sum_{j=0}^{119} x^(2j+1)/(2j+1); the integrated geometric remainder
lies between zero and
2x^241/[241(1-x^2)]. This upper bound follows by replacing
1/(1-u^2) by 1/(1-x^2) in the integral; at x=0 both are zero.
Binary reduction and nonnegative multiples of the log2 interval give
outward intervals for every needed argument. These unrounded intervals
are contained in the stored intervals, and independently give
10584/10^14<Lambda<10585/10^14. Both signs in the large cancellation
N log2-K log3 use opposite endpoints as required.

All 25 guard pairs have strictly positive recomputed margins. The
smallest scaled J-margin is 402427610954 at i=19, and the smallest
scaled H-margin is 6289114252 at i=18. Induction using only a_i=2
for i<24 proves log n_i>v_i/10^12; hence these margins prove the
own-index inequalities at every input, including i=24. The closing
tail is not used as if it were 2 in this induction. Positive h_0 and
all s_i>=540/11 follow from the root and minimum just checked.

The separate full evidence is
`scripts/postspell-word-count/fixed-count-tail-witness-audit-certificate.json`:
317 audit checks, no failures, complete independent log bounds and
comparisons, and the original certificate's SHA-256. Exact symbolic
closure is justified above, not by expanding the enormous rational root
or by a numerical tolerance. The audit changes no direct mathematical
input: L051 supplies the tested system and coordinates; L054 remains
historical comparison only. It supplies no integer/parity/valuation/residue
or primitive-orbit realization, other-count result or universal descent.

## Mathlib

Full matching coverage was not checked. The existing external Lean builds
and source computations remain unverified locally; unknown coverage is
not evidence of absence. The Python certificate proves finite rational
inequalities accompanying the written argument, not a Lean theorem or
an integer Collatz cycle.
