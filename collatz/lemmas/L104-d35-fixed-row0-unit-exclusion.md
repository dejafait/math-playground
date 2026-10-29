# L104 — Fixed d35 row0-unit allocation exclusion

## Hypotheses

Use all 25 indexed pairs in L055's literal table, changing only H_0=5
and H_24=32670656. Set B=9250245 and fix exactly

\[
b_0=1,\quad b_{24}=9250244,\quad b_1=\cdots=b_{23}=0,
\qquad a_i=2+18b_i,\quad \kappa=23/11.
\]

Thus a_0=20, a_1=...=a_23=2 and a_24=166504394. Let
G_i=(27/16)^{J_i}(3/2)^{H_i} and
Q_i=(12/11)(3/2)^{H_i}+1. Suppose real s_0,...,s_25 obey

\[
s_i\ge540/11\ (0\le i<25),\qquad s_{25}=s_0,
\qquad s_{i+1}=2^{-a_i}(G_i s_i-Q_i)+\kappa\ (0\le i<25).
\tag{1}
\]

Require the non-strict own-input J and strict own-input H guards

\[
4J_i\log2\le\log s_i+\log(11/4),\qquad
H_i\log2<\log s_i+J_i\log(27/16)\quad(0\le i<25).
\tag{2}
\]

All logarithms are natural. No minimum, seed, integer junction,
residue, exact valuation, realization or primitive-period assumption
is made; repeated periods are permitted.

## Conclusion

No such tuple exists. More specifically, the unique real cyclic tuple
satisfying the endpoint equations alone has positive coordinates and

\[
s_1<\frac{82225000004347}{2079}<60000000000,
\tag{3}
\]

whereas its row1 J guard requires
s_1>=(4/11)2^60=4611686018427387904/11. Thus even the
endpoint subsystem plus this one necessary guard is infeasible.
The remaining lower-domain and guard comparisons are unnecessary
for this infeasibility verdict and have not been certified individually.

This is local RESEARCH/REPRODUCTION under the pre-existing SPECIALIZE
assessment `drafts/literature/2026-10-25-d35-row0-unit-allocation-feasibility.md`.
It is a finite specialization of known affine machinery, not a claim
of novelty beyond the sources checked. It excludes only the fixed
allocation above, not arbitrary b0>0, other orders or tables, actual
Collatz cycles, divergence or universal descent. Independent critical
review on 2026-10-25 retained this statement without a mathematical
repair; the audit and its limitations are recorded below.

## Proof

### Changed coordinates and the exact cyclic root

Take n_i=s_i-kappa and, exactly as in L055's finite root construction,
define

\[
c_i=\frac{3^{3J_i+H_i}}{2^{4J_i+H_i+a_i}},\qquad
\eta_i=\kappa-\frac{12}{11}(16/27)^{J_i}
                  -(16/27)^{J_i}(2/3)^{H_i}.
\tag{4}
\]

Every c_i is positive and 0<eta_i<kappa, since J_i>=2,H_i>=3
make the two subtracted terms positive with sum strictly less than
12/11+1=kappa. Inserting s_i=n_i+kappa into (1) gives
n_{i+1}=c_i(n_i+eta_i). Indeed Q_i/G_i equals the sum of those
two terms. Both endpoint subtractions remain inside division by 2^a_i,
and kappa remains outside.

The H changes cancel in the total, as do the +18 and -18 tail changes.
Direct sums from the table give

\[
K=\sum_i(3J_i+H_i)=397573379,\quad
N=\sum_i(4J_i+H_i+a_i)=630138897,\quad
\Lambda=N\log2-K\log3.
\tag{5}
\]

The certified enclosures below establish

\[
\lambda_-:=10584/10^{14}<\Lambda<10585/10^{14}=: \lambda_+<1/2,
\qquad \lambda_->10^{-10}.
\tag{6}
\]

For the cut immediately before row1, let
t_0,...,t_24=(1,2,...,24,0), let P_0=1 and
P_k=product_{j<k} c_{t_j}. Put

\[
\mathcal B_1=\sum_{k=0}^{24}\frac{\eta_{t_k}}{P_k},\qquad
D=2^N/3^K-1=e^\Lambda-1.
\tag{7}
\]

The product P_25=3^K/2^N=e^(-Lambda) is strictly between zero
and one by (6). Applying L055's finite affine composition at this
cyclic cut forces and defines

\[
n_1=\mathcal B_1/D>0.
\tag{8}
\]

For completeness the specialization keeps every endpoint: at the input
of row t_k its exact coordinate is
P_k(n_1+sum_{j<k} eta_{t_j}/P_j). After all 25 rows the value is
P_25(n_1+mathcal B_1)=n_1. All prefixes and summands are positive.
Returning the coordinates to their original indices supplies exactly
(1), including row24's endpoint at row0 and row0's endpoint at row1.
Conversely any cyclic endpoint tuple satisfies this composition, so
(8) is its unique root. No approximate closure, minimum or seed is used.

### Reciprocal-prefix cap at cut1

For every i=1,...,23 the actual tail is 2 and H_i>=6, J_i>0.
Consequently

\[
c_i=(27/16)^{J_i}(3/2)^{H_i}/4
   >(3/2)^6/4=729/256>2.
\tag{9}
\]

Thus P_k>=2^k for 0<=k<=23, with equality only at k=0
among these estimates. These are precisely the prefixes before
rows1,...,24; no bound for the huge-tail row24 multiplier is presumed.
For the last prefix, before row0, retain the exact product identity

\[
P_{24}=e^{-\Lambda}/c_0,\qquad
c_0=3^{29}/2^{57}
    =68630377364883/144115188075855872<1/1000.
\tag{10}
\]

The elementary exponential bounds, for 0<Lambda<lambda_+<1/2,
give e^Lambda<=1/(1-Lambda)<1/(1-lambda_+)<2 and
D=e^Lambda-1>Lambda>lambda_-. Therefore
P_24^{-1}=c_0 e^Lambda<1/500. Combining these inequalities with
eta_i<kappa gives the rational estimate

\[
0<\mathcal B_1
 <\kappa\left(\sum_{k=0}^{23}2^{-k}+\frac1{500}\right)
 <\kappa(2+1/500)=2093/500<5.
\tag{11}
\]

In particular, (8) implies

\[
n_1<\frac{2093/500}{10584/10^{14}}=
\frac{7475000000000}{189},\qquad
s_1=n_1+23/11<\frac{82225000004347}{2079},
\]

which proves (3). The exponential inequalities used here are the
standard positive-real power-series/geometric majorants, within the
assessed analytic scope; no Taylor approximation to the cyclic root
is substituted for (8).

### Decisive own-input guard

The table has J_1=15. Since the forced s_1 is positive, monotonicity
of exp makes its non-strict J guard equivalent to

\[
s_1\ge\exp(60\log2-\log(11/4))
       =(4/11)2^{60}=4611686018427387904/11.
\tag{12}
\]

This contradicts (3): the necessary lower bound exceeds the coarse
upper cap 60000000000 by the positive rational
4611685358427387904/11. Strictness is more than sufficient to reject
the non-strict guard. This is the outgoing row1 input, rather than a
post-row1 height or a comparison at a different represented count.

### Certified arithmetic, sources and qualifications

Reproduce the finite certificate with
`python3 scripts/postspell-word-count/certify_d35_row0_unit.py`.
It writes `scripts/postspell-word-count/d35-row0-unit-certificate.json`:
the full changed table and budgets, all 25 rotated prefix exponent
pairs, all rounded logarithm terms and error bounds, exact rational
root caps and required guard bound, and 170 passing finite checks.
There are no failed checks and no parameter samples. The complete
load-bearing root-cap operands, Lambda interval endpoints and summary
were inspected using the scoped JSON inspector. The symbolic proof
above, not a numerical certificate preview, establishes exact endpoints,
closure and uniqueness. This is construction evidence, not an independent
critical audit.

For (6), reuse L055's finite outward enclosure method with 96 terms
rounded down to multiples of 2^-192. For 1<=t<=2 and
x=(t-1)/(t+1), 0<=x<=1/3, the log lower sum consists of the rounded
terms 2*x^(2m+1)/(2m+1), m=0,...,95. The upper sum adds
96*2^-192+9/(4*193*3^193), covering both rounding and the integrated
geometric-series remainder. Use t=2 for log2 and t=3/2 for log(3/2);
log3=log2+log(3/2). If their outward log2 and log3 bounds are
l2,u2 and l3,u3, the exact rational bounds N*l2-K*u3 and
N*u2-K*l3 lie strictly between lambda_- and lambda_+.
All large multiplier amplification and cancellation are retained.

The precise affine input is Halbeisen–Hungerbuehler, *Optimal bounds
for the length of rational Collatz cycles*, Acta Arithmetica78 (1997),
227–239, DOI10.4064/aa-78-3-227-239,
[Lemma2, pp.228–229](https://www.math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
Only finite affine composition and its nonzero-denominator fixed point
are used, as specialized in L055 and (4)–(8); no general coding theorem
is reproved and no integer realization is imported. The reused analytic
source coverage includes [NIST DLMF4.6.4](https://dlmf.nist.gov/4.6.E4)
and [4.5.8–4.5.11](https://dlmf.nist.gov/4.5), recorded version1.2.8, on
positive real arguments. All arguments and the denominator sign have
been checked here. Old d0 numerical margins and L055's minimum/seed
claims are not reused.

Attempt032's failed row0 tail20 sufficient offset package is preserved;
failure of that package was not a feasibility result. Here the exact
cyclic root and its own row1 J guard supply a different discriminating
test. C103a assumes b0=0 and is not an input; neither its exclusions
nor L098's different d34 table transfer a sign to this test. Both d0
witnesses and unfinished work remain intact.

### Independent critical audit — 2026-10-25

The separate pre-existing SPECIALIZE assessment is
`drafts/literature/2026-10-25-l104-row0-unit-critical-audit.md`.
This is RESEARCH/REPRODUCTION: independent verification of this fixed
specialization, not a new theorem beyond the sources checked. No
mathematical defect was found, and the statement and argument above
are retained. The original construction evidence is preserved.

The substitution was checked directly: with n_i=s_i-kappa, (1) gives
n_(i+1)=c_i n_i+c_i*kappa-2^(-a_i)Q_i. Since
Q_i/G_i=(12/11)(16/27)^J_i+(16/27)^J_i(2/3)^H_i,
this is c_i(n_i+eta_i). Each factor in the two subtractions defining
eta_i is strictly between zero and one, so 0<eta_i<kappa at every
row. Thus no offset or positivity premise has been lost.

At cut1 write z_k=n_(t_k), with z_25=z_0 and t_k=1,...,24,0
for k=0,...,24. The recurrence divided by P_(k+1)=P_k*c_(t_k)
gives z_(k+1)/P_(k+1)=z_k/P_k+eta_(t_k)/P_k.
Summing all25 equations yields z_25=P_25(z_0+B1).
The independent positive Lambda enclosure below implies 0<P_25<1;
therefore this closure equation has exactly the root (8). Conversely
the displayed prefix formula satisfies each divided recurrence and
the final closure equation. The order's outgoing indices are
2,...,24,0,1, so both row24-to-row0 and row0-to-row1 are present.
Every coordinate is positive because the root, prefixes and summands
are positive. This establishes exact endpoints, uniqueness and
positivity symbolically, without expanding enormous integer powers.

The audit independently transcribes L055's25 pairs, compares them with
the canonical table, applies precisely H0-=35,H24+=35 and the stated
budget, and directly sums each rotated prefix. The full sums are
K=397573379,N=630138897. For k=0,...,23 the prefix uses exactly
rows1,...,k, all with tail2 and H>=6. Hence the strict ordinary
growth bound (9) applies to those23 factors only. For k=24 the
exponent pair is (K-29,N-57), proving P24=P25/c0 including the
huge row24 tail. No growth assertion is made for row24.

For an independent log enclosure, reuse the unrounded method recorded
in L065: for t=2 and t=3 separately set x=(t-1)/(t+1) and

\[
T(t)=2\sum_{m=0}^{127}\frac{x^{2m+1}}{2m+1},\qquad
R(t)=\frac{2x^{257}}{257(1-x^2)}.
\]

The cited positive-real log series gives T(t)<log(t)<T(t)+R(t):
in the positive tail, each denominator is at least257, with strict
inequality after its first term, and summing the geometric majorant
gives R(t). Here x is1/3 or1/2, so the domain and convergence
hypotheses hold. This evaluates log3 directly, independently of the
construction's binary reduction and term rounding. With opposite
endpoints and full N,K multipliers, rational arithmetic gives

\[
\frac{105843488431681308627}{10^{30}}<\Lambda
 <\frac{105843488431681308628}{10^{30}}.
\]

The entire independent interval width is N*R(2)+K*R(3)<10^-68;
the displayed interval is a coarser outward enclosure. Both its ends
lie strictly between lambda_- and lambda_+. Separately, all192
original rounded summands satisfy floor/2^192<=term<(floor+1)/2^192.
Both original remainder bounds and interval endpoints are recomputed.
Writing E=96/2^192+9/(4*193*3^193), their full Lambda interval
width is (N+2K)E<10^-46. Thus large-coefficient error amplification
and cancellation are included for both methods. The independent
interval is strictly inside the original enclosure.

The audited rational comparisons retain
sum_(k=0)^23 2^-k=16777215/8388608<2 and
c0/(1-lambda_+)<1/500. The cited exponential inequalities apply
because 0<Lambda<lambda_+<1/2, and give D>lambda_->0 and
P24^-1<c0/(1-lambda_+). Consequently the root cap and the own-input
row1 threshold in (3),(12) are unchanged. The threshold exceeds
60000000000 by exactly 4611685358427387904/11>0. This is sufficient
to violate the non-strict J guard; no claim about the remaining
guards, domain lower bounds, minimum or seed is necessary.

Reproduce with `python3 scripts/postspell-word-count/audit_d35_row0_unit.py`.
It writes `scripts/postspell-word-count/d35-row0-unit-audit-certificate.json`
with all independent log terms, full rational intervals and amplified
errors,25 prefix records, root/guard operands and887 passing checks,
with no failures. It also recomputes all170 original comparisons and
their differences rather than accepting saved success flags. Full
cancellation and root-bound evidence was inspected with the scoped
JSON inspector. Symbolic identities are verified in the paragraphs
above, not inferred from the finite-check count. L055 remains the
mathematical input; L065 supplies an enclosure-method reference only, and its
different witness or conclusions are not used. No family extension,
actual-word transfer or universal-descent conclusion was audited.

## Mathlib

Full matching coverage for this fixed 25-row feasibility verdict is
not checked. L055 records supporting affine and logarithmic coverage;
that does not certify the changed table or its bounds. No absence
claim is made. The Python certificate verifies finite rational data;
the informal symbolic argument has not been formally verified.
