# L068 — Uniform last-pair lower-domain and J-guard classification

## Hypotheses

Keep exactly L055's literal indexed table of 25 pairs J_i,H_i, with
K=397573379 and N=630138897. For an integer 0<=t<=9250245 set
a_23=2+18t, a_24=166504412-18t, and a_i=2 for 0<=i<23.
Consider real s_0,...,s_25 with s_25=s_0 satisfying all endpoints

\[
s_{i+1}=2^{-a_i}\left((27/16)^{J_i}(3/2)^{H_i}s_i
             -(12/11)(3/2)^{H_i}-1\right)+23/11.
\tag{1}
\]

The tested conditions are s_i>=540/11 and the own-input guards

\[
4J_i\log2\le\log s_i+\log(11/4),\qquad 0\le i\le24.
\tag{2}
\]

Logarithms are natural. No minimum location, H guard, seed, integer,
parity, residue, exact valuation or primitive-orbit realization is
assumed. These hypotheses use only the endpoint/J part of L051;
its full-system hypotheses are not asserted for this family.

## Conclusion

For every permitted t there is exactly one real cyclic endpoint tuple,
and it is positive rational. Every unshifted junction n_i=s_i-23/11
exceeds 18*10^9, so every lower-domain condition holds. Exactly t=0
and t=1 satisfy all 25 guards (2), strictly. Every 2<=t<=9250245
violates the guard at its own outgoing row 24. At t=2 its
right-minus-left margin is strictly less than
-474883782659/125000000000<-3.79, and it strictly decreases thereafter.

This completes the approved necessary-subsystem classification. It
excludes these larger-t literal allocations from that subsystem, but
supplies no all-order or integer-realization theorem. The two survivors
are already known rational tuples, not new cycle witnesses. Other
allocations, unrestricted cycles, entry, divergence and universal
eventual descent remain unresolved. This is local REPRODUCTION under
the prior SPECIALIZE assessment, with no originality claim beyond the
sources inspected. The separate critical audit below found no defect
within this necessary-subsystem scope.

## Proof

### Affine construction and all endpoints

Define, for the actual tails at t,

\[
c_i(t)=3^{3J_i+H_i}/2^{4J_i+H_i+a_i(t)},\qquad
\eta_i=23/11-(12/11)(16/27)^{J_i}
                       -(16/27)^{J_i}(2/3)^{H_i},
\]
\[
C_i(t)=\prod_{j<i}c_j(t),\quad C_0(t)=1,\qquad
B(t)=\sum_{i=0}^{24}\eta_i/C_i(t).
\]

The table and preserved tail budget give sum(3J_i+H_i)=K and
sum(4J_i+H_i+a_i)=N. Every tail is at least 2 and congruent to 2
modulo 18, including both interval endpoints. L055's audited bound

\[
0<\lambda_-=10584/10^{14}<\Lambda=N\log2-K\log3
 <10585/10^{14}=\lambda_+<1
\tag{3}
\]

applies because K,N are unchanged. Thus C_25(t)=exp(-Lambda)<1.
Put D=2^N/3^K-1=exp(Lambda)-1>0. Each eta_i is positive and
less than 23/11, since both subtracted factors lie in (0,1).

Import affine composition and the nonzero-denominator fixed-point
formula from Halbeisen–Hungerbuehler, *Optimal bounds for the length
of rational Collatz cycles*, Acta Arithmetica 78 (1997), 227–239,
DOI 10.4064/aa-78-3-227-239,
[section 2, equations (2)–(4), Lemma 2, pp. 228–229](https://math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
The word is nonempty with N letters and K odd letters, and
2^N-3^K is nonzero by (3). Only its formal affine identity is used;
no integer-realization theorem is imported. The local specialization
needs checking because the two tails now vary.

Substitute n_i=s_i-23/11 into (1). It gives exactly
n_(i+1)=c_i(t)(n_i+eta_i), using
(27/16)^{J_i}(3/2)^{H_i}(16/27)^{J_i}=(3/2)^{H_i}.
Dividing by C_(i+1)(t) and summing gives

\[
n_{25}=C_{25}(t)(n_0+B(t)),\qquad
n_0(t)=B(t)/D,
\]
\[
n_i(t)=C_i(t)\left(n_0(t)+\sum_{j<i}\eta_j/C_j(t)\right).
\tag{4}
\]

Closure has precisely this one root since C_25(t)!=1. Equations (4)
then establish all endpoints, including the closing one, algebraically.
They define positive rational junctions, with no approximate closure.

### Uniform parameter dependence and domain

Set x=2^(-18t), C=C_24(0)>0 and
A=sum_(j<24)eta_j/C_j(0)>eta_0. Prefixes C_i(t) for 0<=i<=23
do not depend on t. The changed row 23 gives C_24(t)=Cx, whereas
the changed final row restores the unchanged C_25. Consequently

\[
B(t)=A+\eta_{24}/(Cx),\qquad
n_0(t)=\frac{A+\eta_{24}/(Cx)}{D},
\]
\[
n_{24}(t)=Cx(n_0(t)+A)
 =\frac{\eta_{24}}{D}+\frac{CA(1+D)}{D}x.
\tag{5}
\]

All coefficients are positive. As t increases, x strictly decreases.
Thus n_0 strictly increases, and by (4) so do n_1,...,n_23:
their prefixes and partial sums are independent of t. Meanwhile
n_24 strictly decreases. This conclusion uses full exact closure,
not a growth estimate for the parameterized row.

Every literal pair has J_i>=8,H_i>=40. Increasing either exponent
decreases the subtracted positive terms in eta_i, so

\[
\eta_i\ge\eta_0
 =\frac{7122556955297586891012225981605}
         {3433683820292512484657849089281}>2.
\]

The first 23 unchanged multipliers exceed 2: even J=2,H=3,a=2
gives 19683/8192>2. Thus C_i(t)>1 for 1<=i<=23.
Equations (4)–(5) give n_0>A/D>2/D, n_i>n_0 for 1<=i<=23,
and n_24>eta_24/D>2/D. For 0<u<1, the exponential series gives
exp(u)-1<u/(1-u), comparing 1/k!<=1 termwise with a strict
comparison at k=2. By (3),

\[
D<\lambda_+/(1-\lambda_+),\qquad
2/D>2(1-\lambda_+)/\lambda_+
 =39999999995766/2117>18\cdot10^9.
\tag{6}
\]

This proves the domain uniformly for all t, even when row 23
contracts or the designated minimum moves. The repeated closing input
is s_25=s_0 and satisfies the same domain.

### One boundary test covers all rejected integers

L055 supplies t=0 with every J guard strict. Audited L064's literal
j=23 case is exactly t=1 and supplies all 25 strict J guards there.
For rows 0 through 23 their input increases with t, so their margins
increase as well. For row 24 its input decreases, and its right-minus-left
J margin strictly decreases. It suffices to bound that margin at t=2.

Only for this boundary test use a_23=38, a_24=166504376. Row 0
has c_0=3^64/2^74>10^8. For 1<=i<=23 the table has J_i>=15,
H_i>=72 and a_i<=38, giving
c_i>=(27/16)^15(3/2)^72/2^38=3^117/2^170>2
by integer comparison. Hence C_i>10^8*2^(i-1) for 1<=i<=24,
and the finite geometric sum gives

\[
B(2)<B_+=(23/11)(1+2/10^8)=1150000023/550000000.
\]

Also D>Lambda>lambda_- by the exponential series. From (4),
C_i>=1 and each partial sum is less than B(2), so

\[
\frac{s_i(2)}{C_i(2)}
 =n_0(2)+\sum_{j<i}\eta_j/C_j(2)+\frac{23}{11C_i(2)}
 <B_+/\lambda_-+B_++23/11
 =435606069410390910013/22050000000<20\cdot10^9
\tag{7}
\]

for every 0<=i<=24. A direct positive finite sum
sum_(k=0)^40 24^k/k!>20*10^9 shows log(20*10^9)<24.
Thus log s_24(2)<24+log C_24(2).

The complete first-24 totals at t=2 are

\[
\sum_{i<24}(3J_i+H_i)=271907921,\qquad
\sum_{i<24}(4J_i+H_i+a_i)=306970784.
\]

Use audited L064's strict outward logarithm bounds, with S=10^12:
log3<1098612288669/S,
log2>693147180559/S, and log(11/4)<1011600911679/S.
These were certified using the integrated geometric remainder and
independently audited; no floating-point logarithms enter this comparison.
Since J_24=30998279, (7) gives the row-24 margin M_24(2) bounded by

\[
M_{24}(2)
 <24+271907921\log3-430963900\log2+\log(11/4)
\]
\[
 <\frac{24S+271907921(1098612288669)
            -430963900(693147180559)+1011600911679}{S}
 =-\frac{3799070261272}{10^{12}}
 =-\frac{474883782659}{125000000000}<-3.79<0.
\tag{8}
\]

By (5) this same necessary guard fails for every integer t>=2
in the permitted interval. Together with t=0,1 and (6), this is the
complete classification of all 9250246 parameters. No other guard or
allocation was tested or inferred. The boundary growth bound was used
only at t=2; (5)–(6) provide the uniform comparisons.

### Certificate, failed probe and scope

Reproduce the finite arithmetic with
`python3 scripts/postspell-word-count/certify_uniform_last_pair.py`.
The full certificate is
`scripts/postspell-word-count/uniform-last-pair-certificate.json`.
It retains the complete t=2 table, every chronological prefix,
closing exponents, all rational/table checks, finite exponential terms,
the exact margin operands and symbolic full-interval coverage formula.
All 11 required rational checks and 13 table checks pass. The complete
load-bearing t=2, checks, table_checks and exp24_terms fields were inspected.
An initial nonessential request for margin<-4 failed; its actual value,
requested bound and failed verdict remain in diagnostic_probes. The
required negative sign and the final <-3.79 claim pass.

No minimum location is needed, and no fixed-tail prefix bound is
transferred to large t. Both parameterized tails remain at their own
outgoing rows. Real domain feasibility does not imply parity or integer
realization; the J-only survivors are imported known tuples. In particular
this result alone does not assemble their integer exclusions, arbitrary
orders, H/seed conditions or an actual-cycle bridge. All earlier method
stops and rational witnesses retain their stated scopes.

### Independent critical audit — 2026-10-14

The approved audit reused
`drafts/literature/2026-10-14-uniform-last-pair-critical-audit.md`
and the primary affine and logarithm coverage recorded there. It found
no defect. This verifies the existing local reproduction, without a
stronger classification or a new result beyond the inspected sources.

**Closure and parameter dependence.** Substitution of s_i=n_i+23/11
in (1) gives c_i n_i+c_i eta_i exactly, using
G_i(16/27)^J_i=(3/2)^H_i and
G_i(16/27)^J_i(2/3)^H_i=1, with the coefficient 12/11 retained.
Thus n_(i+1)/C_(i+1)=n_i/C_i+eta_i/C_i, including the final row.
The full exponent sums are K,N because the increase 18t in a_23
cancels the decrease 18t in a_24. Both tails stay at least 2 throughout
the closed integer interval, and remain 2 modulo 18. Consequently
C_25=1/(1+D) with D>0. The composition has exactly one real fixed
point, n_0=B/D, and all its junctions are positive rational numbers.
No input parity or denominator-parity conclusion is needed.

For incoming prefixes i<=23, neither changed row has occurred, so C_i
and sum_(j<i)eta_j/C_j are independent of t. Incoming C_24=Cx contains
the changed row 23 but not row 24; all eta_i are independent of tails.
This proves B=A+eta_24/(Cx). Substituting it into
n_24=Cx(n_0+A) gives

\[
n_{24}=\eta_{24}/D+CA(1+D)x/D.
\]

All coefficients are strictly positive and x=2^(-18t) strictly decreases.
Hence n_0,...,n_23 strictly increase, n_24 strictly decreases, and the
same directions hold for s_i and their own-input J margins. The final
recurrence is already included in closure; row 24's larger multiplier
is not omitted from the fixed-point computation. Imported t=0 and t=1
have exactly the current tails and the same unique cyclic roots.

**Domain and boundary.** Every pair has J>=8,H>=40, proving
eta_i>=eta_0>2 without constructing huge powers. Only unchanged rows
0–22 need the c_i>2 bound to give C_i>1 for i=1,...,23. Formula (5)
separately supplies n_24>eta_24/D; thus no growth of row 23 and no
fixed minimum are used for the uniform domain. The exponential-series
comparison and the strict Lambda upper bound give (6) for every input.

At t=2 only, the first row satisfies c_0>10^8 and rows 1–23 satisfy
c_i>=3^117/2^170>2. Therefore the complete sum of 24 inverse incoming
prefix bounds is (1/10^8) sum_(k=0)^23 2^-k<2/10^8. This proves B<B_+.
Since D>lambda_-, each partial sum is below B, and every C_i>=1,
the full expression s_i/C_i is below (7). All 41 positive terms of
sum_(k=0)^40 24^k/k! verify exp(24)>20*10^9. The incoming exponents
271907921 and 306970784 include a_23=38, while full closure includes
a_24=166504376. Adding 4J_24 gives the negative log2 coefficient
430963900. Its negative sign requires the lower log2 bound; the two
positive logarithm coefficients require upper bounds. Their exact
substitution gives (8). Monotonicity then covers every integer from
2 through 9250245, with no sampling or minimum-location assumption.

**Independent finite evidence.** Run
`python3 scripts/postspell-word-count/audit_uniform_last_pair.py`.
It does not import or run the construction program. A separately
transcribed table is compared with all 25 rows of L055. It reconstructs
every original boundary row, all 25 prefix records by direct summation,
both closing exponents, all 11 rational checks with full operands and
differences, all 13 table checks, all 41 exponential terms, and the
failed optional <-4 probe. The preserved probe remains false; the
required upper margin is exactly -474883782659/125000000000<-3.79.

Independent logarithms use 160 unrounded rational terms. For the
positive arguments z=2,3,11/4 and (18*10^9)/2^34, put x=(z-1)/(z+1).
Here 0<x<=1/2. The exact finite geometric identity integrated from
0 to x bounds log z strictly between

\[
P=2\sum_{k=0}^{159}\frac{x^{2k+1}}{2k+1},\qquad
P+\frac{2x^{321}}{321(1-x^2)}.
\]

Indeed the remainder is 2 integral_0^x u^320/(1-u^2) du; its positive
integrand is bounded above using 1/(1-u^2)<=1/(1-x^2), strictly
inside the interval. There is no rounding budget in this second method.
These intervals verify every grid logarithm used in (8) and both sides
of the full cancellation N log2-K log3, using opposite endpoints.
The fourth argument plus 34 log2 verifies log(18*10^9)>23.61.
Direct incoming-prefix sums recompute all 50 imported t=0,1 J lower
margins with their actual tails; their minimum is 402427610954/10^12
in each case. Independent unrounded lower bounds are strictly larger.

The complete evidence is
`scripts/postspell-word-count/uniform-last-pair-audit-certificate.json`:
177 checks pass, with no failures. It retains all exact operands, series
terms and errors, independent Lambda and boundary intervals, both
survivor tables, and the original certificate's SHA-256. Its complete
selected summary and original rational-check/probe records were inspected.
The finite checks supplement the full-interval symbolic argument above.
The original certificate is unchanged.

No mathematical input or assembled argument changed. H/seed conditions,
integer/parity/residue/exact-valuation or primitive realization, arbitrary
orders and other allocations are outside this audit. No actual-cycle
bridge or survivor integer-exclusion assembly is inferred here. Universal
eventual descent remains unresolved.

## Mathlib

Full matching coverage for this parameterized endpoint/J classification
has **not been checked**. Supporting rational arithmetic, finite sums,
exponential and logarithm order facts would not by themselves constitute
a matching theorem. The affine theorem is imported by the precise primary
citation above; logarithm coverage is reused from audited L064, without
claiming a Mathlib formalization or absence from Mathlib.
