# L064 — Single-tail redistribution J-guard classification

## Hypotheses

Keep the literal J_i,H_i table of L055, in that order, with 25 rows
indexed 0,...,24. For one j in {0,...,23}, replace its tails by
a_j=20, a_24=166504394, and a_i=2 at every other row. Consider real
cyclic junctions s_25=s_0 satisfying every exact endpoint L051 (4).
Test the domain s_i>=540/11 and the own-input necessary guards

\[
4J_i\log2\le\log s_i+\log(11/4),\qquad 0\le i\le24.
\tag{1}
\]

All logarithms are natural. H guards, the seed, integrality, parity,
residue membership, exact valuations and primitive realization are not
assumptions or conclusions. No permutations or other redistributions
are included. The fixed counts are K=397573379 and N=630138897.

## Conclusion

Every one of the 24 allocations has a unique real cyclic endpoint
tuple. Each has n_i=s_i-23/11>18*10^9 for 0<=i<=24, so its entire
tuple lies in the required domain. Exactly j=23 satisfies all 25 guards
(1), in fact strictly. Its smallest certified right-minus-left margin
is greater than 402427610954/10^12, at i=19.

For each 0<=j<=22, guard i=j+1 is strictly violated: its left-minus-right
margin exceeds 9.32. Thus those 23 literal allocations cannot satisfy
the necessary subsystem. The remaining allocation is a witness only to
cyclic endpoints, the lower domain and J guards; no full real-system or
integer-cycle witness is asserted. The restricted actual-cycle exclusion
through 24 and the universal eventual-descent gap are unchanged.

This is local REPRODUCTION under the pre-existing SPECIALIZE assessment
`drafts/literature/2026-10-12-single-tail-redistribution-j-guards.md`.
It is not a claim of originality beyond inspected sources. The separate
critical audit below found no defect within this necessary-subsystem scope.

## Proof

### Exact root and changed-tail applicability

For each allocation put

\[
c_i=3^{3J_i+H_i}/2^{4J_i+H_i+a_i},\quad
\eta_i=23/11-(12/11)(16/27)^{J_i}-(16/27)^{J_i}(2/3)^{H_i},
\]
\[
C_i=\prod_{t<i}c_t,\quad C_0=1,\quad
B=\sum_{i=0}^{24}\eta_i/C_i.
\]

All eta_i lie strictly between 0 and 23/11. The changed tails still
sum to 166504460, and the unchanged table gives sum J_i=66061058
and sum H_i=199390205. Therefore sum(3J_i+H_i)=K and
sum(4J_i+H_i+a_i)=N. In particular
C_25=3^K/2^N=exp(-Lambda). L055's audited count-dependent bound is

\[
\lambda_-=10584/10^{14}<\Lambda=N\log2-K\log3
 <10585/10^{14}=\lambda_+<1.
\tag{2}
\]

The needed standard input is Halbeisen–Hungerbuehler, *Optimal bounds
for the length of rational Collatz cycles*, Acta Arithmetica 78 (1997),
227–239, DOI 10.4064/aa-78-3-227-239,
[section 2, equations (2)–(4), Lemma 2, pp. 228–229](https://math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
The approved assessment inspected its hypotheses and essential proof
cases. The word is nonempty, with N letters and K odd letters; the
denominator 2^N-3^K is nonzero by (2). We import formal affine
composition and its fixed-point formula only, without integer realization.

The local coordinate specialization of L051 (4) is exactly
n_(i+1)=c_i(n_i+eta_i), after n_i=s_i-23/11. Its composition gives
n_25=C_25(n_0+B). Since 0<C_25<1 there is precisely one cyclic root,

\[
n_0=\frac{B}{2^N/3^K-1},\qquad
n_i=C_i\left(n_0+\sum_{t<i}\eta_t/C_t\right),\quad s_i=n_i+23/11.
\tag{3}
\]

These are finite exact factored rational expressions. They satisfy each
endpoint and n_25=n_0 algebraically. Every root and prefix is positive.
The changed final tail enters C_25; it is not omitted or treated as growing.
This checks the changed-word specialization without redoing general coding.

### Uniform root and domain bounds

For row 0, the worst allowed tail is 20. Direct integer comparison gives

\[
c_0\ge3^{64}/2^{92}>10^8/2^{18}>2,
\quad \eta_0=
\frac{7122556955297586891012225981605}{3433683820292512484657849089281}>2.
\]

For every 1<=i<24, J_i>=15, H_i>=72 and a_i<=20. Because
27/16>1 and 3/2>1, the multiplier is bounded below by
3^117/2^152>2. Thus all first 24 actual multipliers exceed 2,
including the modified one, and n_0<n_1<...<n_24. The minimum is
proved to occur at row 0, rather than assumed. Also
C_i>(10^8/2^18)2^(i-1) for 1<=i<=24. The finite geometric sum gives

\[
2<B<B_+=(23/11)(1+2\cdot2^{18}/10^8)=9031479/4296875.
\]

For 0<x<1, the exponential series gives x<exp(x)-1<x/(1-x), as
in L055. From (2)–(3),

\[
n_0>2(1-\lambda_+)/\lambda_+
 =39999999995766/2117>18\cdot10^9,
\quad n_0<B_+/\lambda_-=96335776000000/4851.
\tag{4}
\]

All s_i>18*10^9>540/11. In particular the domain precedes any guard
test. For i<=24, C_i>=1 and sum_(t<i)eta_t/C_t<B_+. Consequently

\[
18\cdot10^9<\frac{s_i}{C_i}
=n_0+\sum_{t<i}\eta_t/C_t+\frac{23}{11C_i}
<\frac{B_+}{\lambda_-}+B_++23/11
=\frac{37631162507944991614}{1894921875}<20\cdot10^9.
\]

The logarithm enclosure below gives log(18*10^9)>23.61, and the
positive 41-term exponential sum sum_(k=0)^40 24^k/k!>20*10^9
gives log(20*10^9)<24. Therefore at every tested input,

\[
23.61+\log C_i<\log s_i<24+\log C_i.                 \tag{5}
\]

The old tail-2 prefix bound has been replaced by this argument using
the actual tails. L063's fixed-allocation rigidity is not an input.

### Complete finite guard comparisons

Set S=10^12. Exact outward enclosures give

\[
E_-/S<\log2<E_+/S,\quad T_-/S<\log3<T_+/S,
\quad D_-/S<\log(11/4)<D_+/S,
\]

where (E_-,E_+)=(693147180559,693147180560),
(T_-,T_+)=(1098612288668,1098612288669), and
(D_-,D_+)=(1011600911678,1011600911679).
Define A_-=3T_--4E_+=523248143764,
A_+=3T_+-4E_-=523248143771,
F_-=T_--E_+=405465108108, F_+=T_+-E_-=405465108110.
These enclose alpha=log(27/16) and beta=log(3/2).

For each allocation independently start v_0=23610000000000 and
w_0=24000000000000. For 0<=i<24 compute

\[
v_{i+1}=v_i+J_i A_-+H_i F_--a_iE_+,
\quad w_{i+1}=w_i+J_i A_++H_i F_+-a_iE_-.
\tag{6}
\]

Since log C_i=sum_(t<i)(J_t alpha+H_t beta-a_t log2), (5) proves
v_i/S<log s_i<w_i/S. The guard margin
M_i=log s_i+log(11/4)-4J_i log2 therefore obeys

\[
(v_i+D_--4J_iE_+)/S<M_i<(w_i+D_+-4J_iE_-)/S.
\tag{7}
\]

For j=0,...,22, the upper numerator in (7) at i=j+1 is as follows.
Every value is negative, and its negative is greater than 9.32*S.

| j | i | Upper margin numerator |
|---:|---:|---:|
|0|1|-10035584058473|
|1|2|-10423321868174|
|2|3|-9368473050628|
|3|4|-10124133239120|
|4|5|-9322534135606|
|5|6|-10770231954858|
|6|7|-9984141050155|
|7|8|-10098464469322|
|8|9|-10128065727252|
|9|10|-9995552954311|
|10|11|-10989794932578|
|11|12|-10595778043272|
|12|13|-9497616603088|
|13|14|-9576565005177|
|14|15|-11357002575655|
|15|16|-9868966499920|
|16|17|-10890078325377|
|17|18|-11319878515886|
|18|19|-11684192033039|
|19|20|-10186656580434|
|20|21|-11062709059424|
|21|22|-9742328180112|
|22|23|-11258799181634|

For j=23 the lower numerators in (7), for i=0,...,24 respectively,
are the following 25 positive integers:

```text
2440891133758 2051065191390 1663327381386 2718176198370
1962516008830 2764115110378 1316417287430 2102508185178
1988184752918 1958583470330 2091096196822 1096854131050
1490870855498 2589031985090 2510082997830 729644324850
2217678323394 1196562584354 766755020350 402427610954
1899936889482 1023835096458 2344123064214 827477009934
8286876116986
```

Each value is obtained from the literal table by (6)–(7), with the
changed tail 20 included at i=23. Their minimum is 402427610954
at i=19, proving all 25 strict guards for that allocation. One strict
failure suffices for each rejected allocation; no omitted guard is
assumed valid. The displayed finite comparisons exhaust the target.

### Certification and qualifications

Reproduce with
`python3 scripts/postspell-word-count/certify_single_tail_redistribution.py`.
The complete certificate is
`scripts/postspell-word-count/single-tail-redistribution-certificate.json`.
It stores all 24 parameter tables, all prefixes and closing exponents,
600 guard intervals, 20 rational checks, 168 allocation integer checks,
every logarithm term and rounding/remainder budget, and the 41 exponential
terms. No check failed and no guard interval straddled zero. The complete
23 decisive failing records, all 25 survivor records and their operands,
all domain/root comparisons and allocation count checks were inspected.

For logarithms use L055's exact integrated geometric remainder method,
supported by [NIST DLMF 4.6.4](https://dlmf.nist.gov/4.6.E4), version 1.2.8
(2026-09-15), whose positive-real domain applies. For t>=1 write
t=2^k u with 1<=u<2 and x=(u-1)/(u+1). Then

\[
\log u=2\sum_{m=0}^{95}\frac{x^{2m+1}}{2m+1}
 +2\int_0^x\frac{z^{192}}{1-z^2}\,dz.
\]

Since 0<=x<=1/3, the remainder is less than
9/(4*193*3^193). Round each term down to a multiple of 2^-192;
add 96*2^-192 and that remainder for an upper bound. Bound log2
the same way and add k times its outward interval. This proves the
displayed logarithm bounds; the certificate also reproduces (2) using
N(log2)_lower-K(log3)_upper and the reverse endpoints. All comparisons
are rational, including the cancellation in Lambda. No floating-point
root or sampled orbit establishes closure or a guard.

The standard rational fixed-point input does not establish integer
realization. No integer-cycle theorem is applied to these reals. Existing
published cycle-bound qualifications in L051's background remain unchanged;
this classification uses only its endpoints and necessary J guard.
Earlier fixed-allocation modular failures, L055's witness and L063/C063a
are preserved. The j=23 survivor ends the bounded exclusion attempt for
this entire family; other guard and realization tests remain separate gaps.

### Independent critical audit — 2026-10-13

The approved audit compared the statement with L051 (3)–(4) and the literal
L055 table, retaining all 24 changed allocations and every outgoing row's
own input. It found no defect. This verifies the existing classification;
it does not strengthen its conclusion or assess additional realization
conditions. The prior SPECIALIZE assessment is
`drafts/literature/2026-10-12-single-tail-redistribution-critical-audit.md`.
The affine and logarithm source imports above are reused with their stated
domains; no new source theorem or general coding reproof is introduced.

For the symbolic check, substitute s_i=n_i+23/11 into L051 (4).
The coefficient of n_i is c_i and the remaining unshifted term is
c_i eta_i, since G_i(16/27)^{J_i}=(3/2)^{H_i} and
G_i(16/27)^{J_i}(2/3)^{H_i}=1. Dividing each recurrence by
C_(i+1)=c_i C_i gives (3). The complete exponent sums include
a_24=166504394, so the closing multiplier remains exp(-Lambda).
Its strict location in (0,1) proves uniqueness and positivity of the
cyclic root; neither property is inferred from approximate iteration.

For every row 1 through 23, the literal J_i>=15 and H_i>=72 and the
actual a_i<=20 justify the baseline 3^117/2^152>2. Row 0 separately
uses 3^64/2^92>10^8/2^18>2. Thus growth and C_i>=1 apply to all
25 designated inputs, without applying a growth bound to the closing
edge. The complete finite bound used in place of B is
(23/11)(1+(2^18/10^8) sum_(k=0)^23 2^-k)<B_+.
Together with eta_0>2, the verified Lambda interval and the exponential
inequality in the proof, this gives exactly (4) and the displayed upper
bound on s_i/C_i. The strict lower and upper root/domain comparisons
are verified by rational arithmetic, including all 41 positive terms
used to prove exp(24)>20*10^9. No seed or H guard enters these steps.

The independent program
`python3 scripts/postspell-word-count/audit_single_tail_redistribution.py`
does not import or run the original certifier. Its separately transcribed
25-row table is compared with L055. For the independent logarithms it
uses 128 **unrounded** rational terms. With x=(t-1)/(t+1), set

\[
P_{128}(x)=2\sum_{m=0}^{127}\frac{x^{2m+1}}{2m+1},\qquad
R_{128}(x)=\frac{2x^{257}}{257(1-x^2)}.
\]

For 0<x<=1/2, integrating the remaining geometric series gives
P_128(x)<log t<P_128(x)+R_128(x): on 0<=z<=x the denominator
1-z^2 is at least 1-x^2, with strict inequality except at the endpoint.
At x=0 the logarithm and both bounds equal zero. The program evaluates
t=2,3,11/4 directly, so log3 uses x=1/2 rather than the original
binary reduction. For 18*10^9 it evaluates t=18*10^9/2^34 and adds
34 times the independent log2 interval. All these arguments satisfy
1<t<=3. These enclosures independently verify the decimal-grid bounds,
log(18*10^9)>23.61 and the full cancellation in Lambda.

For each allocation and each i, let
p_i=sum_(t<i)(3J_t+H_t), q_i=sum_(t<i)(4J_t+H_t+a_t).
The audit directly sums these prefixes rather than propagating (6).
It verifies the stored height endpoints as
2361*S/100+p_i*T_--q_i*E_+ and 24*S+p_i*T_+-q_i*E_-.
Using the independent log intervals [ell_-,ell_+], [tau_-,tau_+]
and [d_-,d_+] gives a second pair of strict guard bounds

\[
23.61+p_i\tau_--(q_i+4J_i)\ell_++d_-
 < M_i <
24+p_i\tau_+-(q_i+4J_i)\ell_-+d_+.
\]

All 600 independently computed verdicts agree with the original records.
All 23 published negative numerators and all 25 published positive
numerators match direct summation. The weakest rejection bound is
9322534135606/S>9.32 at j=4, i=5; the smallest survivor lower
bound is exactly 402427610954/S at i=19, as claimed. These are
strict bounds on the true margins, not approximate margin values.

The audit also checks every stored rounded logarithm term (480 terms
over five base-series records), each floor inequality, the 96*2^-192
rounding budgets, the complete remainder envelopes, reduced arguments
and full reconstructed intervals. It reconstructs all 20 original rational
check operands and all 168 allocation integer checks, all prefix and
closing exponents, and every guard record. The full audit certificate is
`scripts/postspell-word-count/single-tail-redistribution-audit-certificate.json`:
1,535 checks pass, with no failures. It retains all exact independent
series terms, intervals, guard operands and comparisons, plus the original
certificate's hash. The 48 decisive scaled values and root/domain bounds
were also inspected in its complete selected summary. The original
certificate is preserved unchanged.

No dependency changes are needed. In particular, L063/C063a do not
apply to changed tails, and the earlier modular diagnostics say nothing
about this survivor. The audit proves no H guards, seed, integrality,
parity, exact valuations, primitive realization or universal descent.

## Mathlib

Full matching coverage for this changed-allocation classification is
**not checked**. Supporting exact rational arithmetic and logarithm facts
are used informally; no Mathlib theorem or Lean build is claimed. Unknown
coverage is not evidence of absence.
