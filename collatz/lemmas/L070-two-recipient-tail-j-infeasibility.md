# L070 — Literal two-recipient tail J infeasibility

## Hypotheses

Use exactly L055's indexed table of pairs J_i,H_i, in literal order,
for 0<=i<=24. For an integer 1<=t<=9250244 put

\[
a_{22}=20,\quad a_{23}=2+18t,\quad
a_{24}=166504394-18t,\quad a_i=2\ (i<22).
\]

Consider real junctions s_0,...,s_25 with s_25=s_0 and all endpoints

\[
s_{i+1}=2^{-a_i}\left((27/16)^{J_i}(3/2)^{H_i}s_i
 -(12/11)(3/2)^{H_i}-1\right)+23/11.                 \tag{1}
\]

The proposed necessary subsystem adds s_i>=540/11 and every own-input
J guard

\[
4J_i\log2\le\log s_i+\log(11/4),\qquad 0\le i\le24. \tag{2}
\]

All logarithms are natural. These are only the endpoint/domain/J
conditions of L051, with the specified pairs and tails. No minimum
location, H guard, seed, integer, residue, parity, exact valuation,
primitive-orbit or count-ray premise is imposed. No other order or
allocation is included.

## Conclusion

For every admitted t the endpoints (1) have exactly one real cyclic
tuple. It is positive rational and satisfies the entire lower domain;
indeed n_i=s_i-23/11>18*10^9 at every input. However its row-24
own-input J margin

\[
M_{24}(t)=\log s_{24}(t)+\log(11/4)-4J_{24}\log2
\]

strictly decreases with t, and

\[
M_{24}(t)\le M_{24}(1)
 <-474883782659/125000000000<-3.79<0.                \tag{3}
\]

Consequently the endpoint/domain/J system is infeasible for all
9250244 admitted integers. This is a local REPRODUCTION under the
prior SPECIALIZE assessment
`drafts/literature/2026-10-15-two-recipient-tail-j-feasibility.md`,
not an originality claim beyond inspected sources. The separate critical
audit below found no defect within this exact scope. It neither assembles an actual-word application
nor changes the unrestricted-cycle, entry, divergence or universal
eventual-descent gaps. The existing rational witnesses remain valid.

## Proof

### Exact changed-support specialization

For the actual tails define

\[
c_i(t)=3^{3J_i+H_i}/2^{4J_i+H_i+a_i(t)},\quad
\eta_i=23/11-(12/11)(16/27)^{J_i}
                    -(16/27)^{J_i}(2/3)^{H_i},
\]
\[
C_i(t)=\prod_{j<i}c_j(t),\quad C_0(t)=1,\qquad
B(t)=\sum_{j=0}^{24}\eta_j/C_j(t).
\]

The fixed table has sum J_i=66061058 and sum H_i=199390205.
The tail sum is
44+20+(2+18t)+(166504394-18t)=166504460.
Thus the unchanged totals are K=397573379 and N=630138897.
Both varying tails are at least 2 and congruent to 2 modulo 18,
including the upper endpoint (a_23,a_24)=(166504394,2).
The positive Lambda enclosure from audited L055 therefore applies:

\[
0<\lambda_-=10584/10^{14}<\Lambda=N\log2-K\log3
 <10585/10^{14}=\lambda_+<1.                        \tag{4}
\]

The standard input is Halbeisen–Hungerbuehler, *Optimal bounds for
the length of rational Collatz cycles*, Acta Arithmetica 78 (1997),
227–239, DOI 10.4064/aa-78-3-227-239,
[section 2, equations (2)–(4), Lemma 2, pp. 228–229](https://math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
Reuse its inspected formal affine composition and nonzero-denominator
fixed-point formula. The nonempty formal word has N letters and K
odd letters; (4) gives 2^N-3^K>0. No integer/parity realization is
imported. The following calculation justifies the changed-support
coordinate specialization, rather than reproving general coding.

Substitution n_i=s_i-23/11 in (1) gives exactly
n_(i+1)=c_i(t)(n_i+eta_i). Indeed the two subtracted terms in
c_i eta_i are 2^(-a_i)(12/11)(3/2)^H_i and 2^(-a_i).
Dividing by C_(i+1)=c_i C_i and summing gives, with
D=2^N/3^K-1=exp(Lambda)-1>0,

\[
n_0(t)=B(t)/D,\qquad
n_i(t)=C_i(t)\left(n_0(t)+\sum_{j<i}\eta_j/C_j(t)\right).
                                                               \tag{5}
\]

In particular n_25=C_25(n_0+B)=n_0 because C_25=1/(1+D).
This verifies all endpoints and the closing edge exactly. Conversely
composition forces (5) for every real cyclic tuple, proving uniqueness.
Every eta_i is in (0,23/11): both subtracted terms are positive,
and their sum is less than 12/11+1 because J_i,H_i>0.
Thus the tuple is positive rational.
The large final tail is retained in C_25, never treated as growing.

### Parameter dependence and lower domain

For defining reference coefficients only, extend the formulas to t=0;
no J feasibility at that boundary is asserted or used. Set

\[
x=2^{-18t},\quad C=C_{24}(0)>0,\quad
A=\sum_{j<24}\eta_j/C_j(0)>\eta_0>2.
\]

The fixed row-22 tail is 20 in these reference prefixes. All C_i(t)
for i<=23 are independent of t. Row 23 gives C_24(t)=Cx, while
row 24 restores the unchanged C_25. Therefore (5) yields

\[
B(t)=A+\eta_{24}/(Cx),\qquad
n_{24}(t)=\eta_{24}/D+CA(1+D)x/D.                   \tag{6}
\]

Both coefficients in the last expression are positive. Since x
strictly decreases as t increases, n_24 and s_24 strictly decrease.
They are positive, so M_24 strictly decreases as well. This argument
uses full closure and applies even when row 23 contracts.

For completeness, the domain does hold uniformly. The literal table
has J_i>=8,H_i>=40, so eta_i>=eta_0>2, where

\[
\eta_0=7122556955297586891012225981605/
3433683820292512484657849089281.
\]

For all t, c_0=3^64/2^74>10^8. For rows 1 through 22 the
fixed tails are at most 20, J_i>=15 and H_i>=72. Monotonicity of
(27/16)^J(3/2)^H gives c_i>=3^117/2^152>2. Hence C_i>1
for 1<=i<=23. From (5)–(6), n_0>A/D>2/D, all n_i>n_0
for 1<=i<=23, and n_24>eta_24/D>2/D. For 0<u<1,
the exponential series gives exp(u)-1<u/(1-u), with strictness
already at its quadratic term. Thus (4) implies

\[
n_i>2/D>2(1-\lambda_+)/\lambda_+
 =39999999995766/2117>18\cdot10^9.                 \tag{7}
\]

In particular every s_i=n_i+23/11 exceeds 540/11, including the
repeated closing input. No minimum location is needed.

### Certified boundary rejection

At t=1, tails 22 and 23 are both 20 and the final tail is
166504376. Row 0 still has c_0>10^8. Every row 1 through 23
now has a_i<=20,J_i>=15,H_i>=72, so c_i>=3^117/2^152>2.
Only at this boundary do we use growth through row 23. For 1<=i<=24,
C_i>10^8*2^(i-1). Consequently

\[
B(1)<B_+=(23/11)(1+2/10^8)=1150000023/550000000.
\]

Since D>Lambda>lambda_- and every partial sum in (5) is less
than B_+, at every 0<=i<=24 the boundary tuple satisfies

\[
\frac{s_i(1)}{C_i(1)}
 <B_+/\lambda_-+B_++23/11
 =435606069410390910013/22050000000<20\cdot10^9.     \tag{8}
\]

Here C_i>=1 at this boundary; that condition is not transferred to
the parameterized C_24 for large t. The positive finite sum
sum_(k=0)^40 24^k/k!>20*10^9 proves log(20*10^9)<24.
Thus log s_24(1)<24+log C_24(1).

The complete first-24 sums at t=1 are

\[
p=\sum_{i<24}(3J_i+H_i)=271907921,\qquad
q=\sum_{i<24}(4J_i+H_i+a_i)=306970784.
\]

With J_24=30998279, this gives

\[
M_{24}(1)<24+p\log3-(q+4J_{24})\log2+\log(11/4).
\]

Reuse audited L064's strict outward enclosures, with S=10^12:
log3<1098612288669/S, log2>693147180559/S, and
log(11/4)<1011600911679/S. The signs above require precisely
these endpoints. Since q+4J_24=430963900, exact integer arithmetic gives

\[
M_{24}(1)
 <\frac{24S+271907921(1098612288669)
      -430963900(693147180559)+1011600911679}{S}
 =-3799070261272/10^{12}<-3.79.                     \tag{9}
\]

Those logarithm bounds have the complete geometric-series remainder
proof and independent rational audit in L064; no logarithms are
recomputed with floating point here. The matching numerical margin
in L068 is only a comparison: here the changed prefix multipliers,
B upper bound, all exponents and monotonicity were justified for the
actual two-recipient support. By (6), (9) rejects every admitted t.
A strict failure of this one necessary non-strict guard suffices;
no verdict on the other guards is needed.

### Finite evidence and qualifications

Reproduce with
`python3 scripts/postspell-word-count/certify_two_recipient_tail.py`.
The complete certificate is
`scripts/postspell-word-count/two-recipient-tail-certificate.json`.
It stores the actual 25-row boundary table, every chronological prefix,
closing exponents, 11 rational checks with full operands and margins,
16 table checks, all 41 positive exponential terms and the exact row-24
guard operands. All checks pass. These complete fields were inspected.
The finite arithmetic supports (7)–(9); the written exact formulas and
positivity argument, not sampling, prove coverage of the whole interval.

This is a changed-support specialization of the inspected affine method.
L064's rejected t=0 boundary alone would not answer this target, and
L068's different row-22 tail precludes importing its classification.
No earlier source obstruction or method stop is discarded. This result
uses no integer-cycle lower bound or its computational qualifications.
It proves only the stated necessary-subsystem rejection. A later actual
word bridge must separately verify every own-input condition; it is not
assumed here. Other tail supports/orders and all universal gaps remain.

### Independent critical audit — 2026-10-15

The separate audit under the prior SPECIALIZE assessment
`drafts/literature/2026-10-15-two-recipient-tail-critical-audit.md`
found no defect. It checks exactly the stated endpoint/domain/J family,
without enlarging the allocation or adding any realization premise.
The formal affine source and logarithm coverage cited above suffice;
this is verification of their local specialization, not a new general
coding theorem or an originality claim.

Substitution into L051 (4) gives the unshifted offset
c_i(23/11)-2^(-a_i)(12/11)(3/2)^H_i-2^(-a_i)=c_i eta_i.
Thus dividing by C_(i+1) gives an increment eta_i/C_i at every
edge. Summing all 25 increments includes the changed closing tail.
Its exponent sums are exactly K=397573379 and N=630138897,
independent of t, so C_25=exp(-Lambda)<1. The linear closing
equation has the unique solution (5); all its terms are positive
rationals. No integer, parity or valuation conclusion is imported
from the formal fixed-point formula.

The independently reconstructed prefix exponents have t-coefficient
zero through C_23, coefficient 18 in the denominator of C_24,
and zero again in C_25. The fixed tail 20 at row 22 is included
even in the t=0 reference. Consequently the partial offset sum
before row 24 is exactly A, independent of t; substituting B into
n_24=Cx(n_0+A) gives exactly (6), with both coefficients positive.
The integer interval's upper endpoint has tails (20,166504394,2)
at rows 22–24. This proves strict decrease for its entire range,
even when c_23 is less than one. No extension of boundary growth
to that range is used.

For the uniform domain, each pair dominates (8,40), so
eta_i>=eta_0>2. The fixed rows 1–22 dominate (15,72) and have
tails at most 20; their multipliers exceed two. Together with
c_0>10^8 this proves C_i>1 for 1<=i<=23. Hence (5) gives
n_0>2/D and n_i>n_0 for those inputs; (6) gives n_24>2/D
separately. The exact inequality D<lambda_+/(1-lambda_+)
then yields (7). The closing input equals input zero. No minimum
location or J guard is needed to obtain the domain.

At t=1, the same growth comparison also applies to row 23.
The finite geometric reciprocal-prefix sum is strictly less than
2/10^8, yielding the B_+ bound. Since D>lambda_- and C_i>=1
at this boundary, adding both the partial offset sum and 23/(11C_i)
gives exactly (8). This verifies the shifted coordinate used in the
J guard; an unshifted height is not substituted for it. The complete
41-term positive exponential sum certifies log(20*10^9)<24.

The independent program
`python3 scripts/postspell-word-count/audit_two_recipient_tail.py`
does not import or execute the original certifier. It separately
transcribes all 25 pairs and compares them with L055, reconstructs
all chronological prefix and closing exponents, and checks every
original rational comparison operand, difference and all 41 exponential
terms. Its full certificate is
`scripts/postspell-word-count/two-recipient-tail-audit-certificate.json`.
The original certificate is preserved and its SHA256 is recorded.

For independent logarithms, the program uses, for u in {2,3,11/4}
and x=(u-1)/(u+1), the exact rational enclosure

\[
P=2\sum_{k=0}^{127}\frac{x^{2k+1}}{2k+1}
 <\log u<P+\frac{2x^{257}}{257(1-x^2)}.
\]

Here 0<x<=1/2. Integrating the positive geometric remainder
2 z^256/(1-z^2) on [0,x] proves both strict signs; its denominator
is strictly larger than 1-x^2 off the endpoint. This is L064's
already audited method with unrounded terms. It independently verifies
the outward grid values and both ends of the cancellation-sensitive
Lambda interval, then the boundary margin using the correct signed
endpoints. The full series operands and rational intervals are saved.

The independent first-24 exponents are (271907921,306970784),
and adding 4J_24 gives 430963900. The complete scaled operands are
24000000000000, 298721383397039647149,
-298721412207710820100 and 1011600911679. Their sum is
-3799070261272, giving exactly (9); the independent finer interval
lies strictly below this upper bound as well. All 217 checks pass,
with no failed comparison. The full summary and all symbolic prefix
records were inspected; the proof of interval coverage is the algebra
above, rather than sampling or certificate success flags.

The audit changes no mathematical input or dependency: L051 supplies
the retained equations/guard, L055 the table and positive Lambda,
and L064 the logarithm method/bounds. L068 is comparison only.
This verifies the existing restricted exclusion; it supplies no new
allocation result, actual-word application, H/seed or integer/parity/
valuation realization, primitive/count-ray claim or universal descent.

## Mathlib

Full matching coverage for this classification is **not checked**.
The argument uses supporting finite rational arithmetic, affine
composition and logarithm monotonicity informally. No Lean theorem or
build is claimed; unknown coverage is not evidence of absence.
