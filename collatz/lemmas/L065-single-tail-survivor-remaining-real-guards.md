# L065 — Single-tail survivor remaining real guards

## Hypotheses

Use the literal 25-row J_i,H_i table of L055, indexed 0,...,24,
with a_23=20, a_24=166504394 and a_i=2 at every other index.
Set K=397573379, L=232565518, N=630138897 and r=25.
Take exactly L064's unique cyclic endpoint tuple. Explicitly, put

\[
c_i=3^{3J_i+H_i}/2^{4J_i+H_i+a_i},\quad
\eta_i=23/11-(12/11)(16/27)^{J_i}-(16/27)^{J_i}(2/3)^{H_i},
\]
\[
C_i=\prod_{t<i}c_t,\quad C_0=1,\quad
B=\sum_{i=0}^{24}\eta_i/C_i,\quad
n_0=B/(2^N/3^K-1),
\]
\[
n_i=C_i\left(n_0+\sum_{t<i}\eta_t/C_t\right),\qquad
s_i=n_i+23/11,\qquad h_i=\log s_i.
\]

All logarithms are natural. No remaining H guard or seed inequality,
integer junction, parity, residue, exact valuation or primitive-orbit
realization is assumed. No other order or allocation is considered.

## Conclusion

Every one of the 25 own-input strict H guards and the seed holds:

\[
H_i\log2<h_i+J_i\log(27/16)\quad(0\le i\le24),\qquad
0<h_0<(133/10)\log N+8+\log25.
\]

The smallest certified H-margin lower bound is
6289114252/10^12=0.006289114252, at i=18. Explicitly checking the
aggregate premises below and combining these comparisons with L064's
closure, domain, minimum and J guards yields a complete positive rational
witness to L051 (1)–(4), with d=1, K_0=K and L_0=L. Thus this
changed-tail tuple also survives the full specified real system.

This is local REPRODUCTION under the pre-existing SPECIALIZE assessment
`drafts/literature/2026-10-13-single-tail-survivor-remaining-real-guards.md`,
not a general rational-cycle theorem or a claim of originality beyond
inspected sources. The separate critical audit below found no defect
within this exact real-system scope. No integer
Collatz cycle or counterexample is established; the restricted actual-cycle
exclusion remains through 24. Entry, other cycles, divergence and universal
eventual descent remain unresolved.

## Proof

### Exact tuple and eligible height bounds

L064 proves for exactly these changed tails that the factored expressions
in the hypotheses define the unique cyclic tuple satisfying every L051 (4)
endpoint. In particular C_25=3^K/2^N and the large closing tail is
included. It proves n_0<n_1<...<n_24, s_25=s_0 and s_i>18*10^9,
so s_0 is the designated minimum and every s_i>=540/11. Its audited
normalized height bounds give, for every 0<=i<=24,

\[
23.61+\log C_i<h_i<24+\log C_i.                 \tag{1}
\]

These are the changed-tail bounds, rather than a transfer of L055's
tail-2 comparisons. L064 also proves all 25 J guards strictly for
this tuple; they remain eligible without another permutation or allocation.

The standard affine input underlying L064 is Halbeisen–Hungerbuehler,
*Optimal bounds for the length of rational Collatz cycles*, Acta Arithmetica
78 (1997), 227–239, DOI 10.4064/aa-78-3-227-239,
[section 2, equations (2)–(4), Lemma 2, pp. 228–229](https://math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
The word is nonempty with N letters and K odd letters, and its denominator
is positive by the Lambda bounds below. Only formal composition and its
fixed point are used. L064 already checks the shifted-coordinate
specialization; no coding reproof or integer-realization assertion is needed.

### Complete own-input H comparisons

Set S=10^12. Use the strict logarithm enclosures

\[
E_-/S<\log2<E_+/S,\qquad T_-/S<\log3<T_+/S,
\]

where (E_-,E_+)=(693147180559,693147180560) and
(T_-,T_+)=(1098612288668,1098612288669). Put
A_-=3T_--4E_+=523248143764 and
F_-=T_--E_+=405465108108. Then
A_-/S<alpha=log(27/16) and F_-/S<beta=log(3/2).
Start v_0=23610000000000 and set, for 0<=i<24,

\[
v_{i+1}=v_i+J_i A_-+H_i F_--a_iE_+.             \tag{2}
\]

Since log C_i=sum_(t<i)(J_t alpha+H_t beta-a_t log2),
(1) implies h_i>v_i/S. This uses the actual a_23=20 in the
transition from row 23 to row 24. The closing tail is in exact closure,
and no increasing-height bound is applied across the closing edge.

Consequently the true H margin obeys

\[
h_i+J_i alpha-H_i\log2>
(v_i+J_i A_--H_i E_+)/S.                        \tag{3}
\]

For the literal table and these tails, the 25 integer lower numerators
in (3), in index order, are

```text
70097927712 570420269452 53436522780 496444359460
243194644024 296420192316 267360955140 357237954752
638069930720 305365679840 444535689244 220290618028
636585593476 136430507056 322103147984 548337798856
465906922552 188606219424 6289114252 664232490696
480571431372 56750531324 64953570744 399111636848
79519729152858484664
```

Every numerator is positive; the minimum is 6289114252 at i=18.
For example the decisive own-input comparison is exactly
H_18 E_+=2284064134558756480 <
v_18+J_18 A_-=2284064140847870732. For row 24,
v_24=85945486039524230268, including the eighteen additional
halvings at row 23. This certifies every strict H guard separately;
no interval meets zero.

### Seed and explicit aggregate premises

At i=0, C_0=1 and (1) gives 0<23.61<h_0<24.
The certified logarithm procedure below yields

\[
24<
\frac{8809792135310463031399506046653464402068626298388305227378587}
{31385508676933403819178947116038332080511777222320172564480}
<(133/10)\log N+8+\log25.                       \tag{4}
\]

Thus both seed inequalities hold, retaining the exact log25 term.

The table gives sum J_i=66061058 and sum H_i=199390205.
The new tails sum to 23*2+20+166504394=166504460.
Each J_i>=2, H_i>=3 and a_i>=2 with a_i=2 modulo 18;
in particular 166504394=2+18*9250244. Hence

\[
\sum(3J_i+H_i)=397573379=K,\quad
\sum(J_i+a_i)=232565518=L,\quad K+L=N=630138897.
\]

Choose positive integers d=1, K_0=397573379>225640000 and
L_0=232565518. Then K=dK_0 and L=dL_0. The remaining aggregate
length comparison has exact positive right-minus-left margin

\[
(8/5)K+1725/1034-N=30908902223/5170>0.
\]

Finally the unchanged count-dependent interval, independently reproduced
by outward logarithms in the new certificate, is

\[
10584/10^{14}<N\log2-K\log3<10585/10^{14}<1.
\]

This verifies all L051 (1) premises. The threshold K_0 is directly
satisfied by the chosen integers, without invoking an integer-cycle
theorem on real junctions. L064 supplies the exact endpoints, minimum,
domain and J comparisons; (3)–(4) supply the remaining guards and seed.
Together they satisfy every clause of the stated real system.

### Certificate and qualifications

Reproduce with
`python3 scripts/postspell-word-count/certify_survivor_remaining_real_guards.py`.
The complete evidence is
`scripts/postspell-word-count/survivor-remaining-real-guards-certificate.json`.
It stores the literal changed-tail table, all factored prefix exponents,
all 25 H-margin operands and intervals, the complete seed bounds,
42 strict rational comparisons and 63 integer/count/prefix checks.
Every check passes; no guard interval is unresolved. The complete H records,
all rational actual/required operands, all integer checks and the exact
seed margin were inspected. Closure and the J verdict are imported from
the audited L064 proof, not independently audited again in this turn.

For the logarithms reuse L055's finite certification method, supported by
[NIST DLMF 4.6.4](https://dlmf.nist.gov/4.6.E4), version 1.2.8
(2026-09-15). Its positive-real domain includes all arguments used.
For t>=1 binary-reduce t=2^k u, 1<=u<2, and let x=(u-1)/(u+1).
The exact identity is

\[
\log u=2\sum_{m=0}^{95}\frac{x^{2m+1}}{2m+1}
 +2\int_0^x\frac{z^{192}}{1-z^2}\,dz.
\]

For 0<=x<=1/3 the remainder is bounded above by
9/(4*193*3^193). Round each summand down to a multiple of 2^-192;
add 96*2^-192 and the remainder bound for an upper enclosure. Treat
log2 by the same procedure and add k times its interval. The certificate
retains all rounded terms, arguments, rounding budgets, remainder bounds
and final exact rational endpoints. For Lambda multiply the log2 and
log3 intervals by the full N,K with the proper opposing endpoints;
for (4) multiply by positive 133/10 and add the log25 lower endpoint.
All errors, including large multiplier amplification, are retained.
This is application of the inspected method, not a new logarithm theorem.

Attempt 026/L055's original witness and L064's J-only family stop remain
valid; this result completes only the approved survivor test. Fixed-allocation
order and prime diagnostics do not apply to these changed tails. No integer,
parity, residue, exact-valuation or primitive-orbit realization is supplied.
Published computational qualifications motivating L051's necessary system
remain as recorded there; none is used to assert an actual orbit here.
The separate critical review below assesses this finite specialization
and its essential inherited inputs without extending the conclusion.

### Independent critical audit — 2026-10-13

The audit under the prior SPECIALIZE assessment
`drafts/literature/2026-10-13-survivor-real-system-critical-audit.md`
found no defect in the full witness to L051 (1)–(4). It retains exactly
the displayed tuple, including a_23=20 and a_24=166504394. The cited
affine identity and finite logarithm method above are reused with their
stated hypotheses. This verifies an existing finite specialization; it
neither strengthens the theorem nor claims an advance beyond those sources.

For the inherited algebra, substitution of s_i=n_i+23/11 in L051 (4)
gives n_(i+1)=c_i(n_i+eta_i): the identities
G_i(16/27)^{J_i}=(3/2)^{H_i} and
G_i(16/27)^{J_i}(2/3)^{H_i}=1 account for both negative offsets.
Dividing by C_(i+1)=c_i C_i and summing gives the stated finite prefix
formula. The complete exponent sums, including the modified closing tail,
give C_25=3^K/2^N. The independently verified Lambda interval puts
C_25 strictly between zero and one, so n_0=B/(1/C_25-1)>0 is the
unique cyclic root and satisfies all endpoints exactly. No approximate
iteration or expanded enormous integer is needed for this conclusion.

The inherited normalized bounds and minimum are eligible without H or
seed assumptions. For the actual first 24 edges, row 0 meets
c_0>=3^64/2^92>10^8/2^18>2 and eta_0>2; all remaining rows
through 23 have J_i>=15, H_i>=72 and a_i<=20, so
c_i>=3^117/2^152>2. Positivity of eta_i then proves strict growth
through n_24. It is not applied to the closing edge. The finite bound

\[
B<(23/11)\left(1+\frac{2^{18}}{10^8}
                   \sum_{t=0}^{23}2^{-t}\right)<B_+
\]

and eta_0>2 justify the root bounds in L064. The audit checks their
exact rational operands, obtaining
n_0>39999999995766/2117>18*10^9 and
s_i/C_i<37631162507944991614/1894921875<20*10^9 for all inputs.
Independent logarithms verify log(18*10^9)>23.61 and
log(20*10^9)<24. Thus (1), the domain and the designated minimum
have all the required hypotheses. No original tail-2 margin is imported.

The independent program
`python3 scripts/postspell-word-count/audit_survivor_real_system.py`
neither runs nor imports the original generator. It transcribes the 25-row
table separately, compares it with L055, and sums each prefix directly:
p_i=sum_(t<i)(3J_t+H_t), q_i=sum_(t<i)(4J_t+H_t+a_t).
It verifies every original height and H record using
v_i=2361*S/100+p_i T_--q_i E_+ and
w_i=24*S+p_i T_+-q_i E_-, rather than propagating (2).
All 25 published H numerators agree exactly. In particular, at i=18
the prefix counts are p_18=6078924 and q_18=6862841, and the
full scaled comparison is

\[
2284064134558756480<2284064140847870732,
\]

whose difference is 6289114252. Row 24's lower height numerator is
85945486039524230268, so the extra eighteen halvings are retained.

For independent logarithms use L064's audited unrounded method, with
x=(t-1)/(t+1),

\[
P=2\sum_{m=0}^{127}\frac{x^{2m+1}}{2m+1},\qquad
R=\frac{2x^{257}}{257(1-x^2)}.
\]

For 1<t<=3, 0<x<=1/2 and P<log t<P+R; for t=1 the
exact interval is [0,0]. Larger positive arguments are divided by powers
of two until they lie in [1,3], and the corresponding multiple of the
independent log2 interval is added. Thus log3 is evaluated directly at
x=1/2, independently of the original binary reduction and rounding.
Write the resulting bounds for log2, log3 and log(11/4) as
[ell_-,ell_+], [tau_-,tau_+] and [delta_-,delta_+]. For every row,
the audit checks positivity of both independent lower margins

\[
23.61+(p_i+3J_i)\tau_--(q_i+4J_i+H_i)\ell_+,
\qquad
23.61+p_i\tau_--(q_i+4J_i)\ell_++\delta_-.
\]

They certify all H and J guards, respectively, with the correct own-input
pairing. Each independent H lower bound is also strictly above its
published grid lower bound. All independent logarithm truncation widths
after multiplication by the full H coefficients, and by N,K for Lambda,
are below 10^-60. This does not describe the wider inherited normalized
height uncertainty, which remains explicitly [23.61,24] in these bounds.

The complete independent Lambda interval lies strictly between
10584/10^14 and 10585/10^14. The seed check gives
0<23.61<h_0<24<280<(133/10)log N+8+log25, retaining both
logarithm errors and the log25 term. Every parameter lower bound, tail
congruence, total count and d=1 scaling premise is checked; the length
margin is exactly 30908902223/5170>0. These are all clauses of L051
(1)–(4). Choosing K_0=K satisfies the explicit numerical parameter
requirement and asserts no primitive-orbit realization.

The audit reconstructs all 672 original rounded summands across the
log2 base and six reduced logarithm records. Each floor inequality,
96*2^-192 rounding budget, integrated remainder envelope, reduction and
full interval is checked. All 42 rational comparisons are reconstructed
with both complete operands and their margins; all 63 integer checks,
25 full H records, prefixes, seed record and aggregate summary are
compared with independent constructions. Original certificate data is
preserved unchanged and its SHA-256 recorded in the audit evidence.

The full certificate is
`scripts/postspell-word-count/survivor-real-system-audit-certificate.json`:
929 checks pass, with no failures. It stores complete independent rational
intervals and guard operands, every verification verdict and exact selected
bounds. The full summary, every published H lower numerator and the
complete decisive row-18 interval were also inspected. This certificate
supports the written algebra above; its check count alone is not a proof.

No mathematical dependency changes are required. Attempt 026 and L064's
J-family stop are preserved. Fixed-allocation rigidity and prime tests
remain inapplicable to these changed tails. Integer junctions, parity,
residue, exact valuations and primitive realization are unproved, as are
unrestricted cycle exclusion, divergence control and universal descent.

## Mathlib

Full matching coverage for this changed-tail remaining-guard calculation
is **not checked**. Supporting rational arithmetic and logarithm facts
are used informally; no Mathlib theorem or Lean build is claimed.
Unknown availability is not evidence of absence.
