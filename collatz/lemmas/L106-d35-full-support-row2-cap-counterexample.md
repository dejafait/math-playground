# L106 — Exact endpoint counterexample to the full-support row2 cap

## Hypotheses

Use the chronological25-row J,H table of L055, changing only H0=5
and H24=32670656. Thus J2=28,H2=134 and every J_i>=8,H_i>0.
Set kappa=23/11,B=9250245 and fix the integer allocation

\[
b_0=b_1=1,\quad b_2=12,\quad b_{24}=9250231,
\quad b_i=0\ (3\le i\le23),\qquad a_i=2+18b_i.
\tag{1}
\]

All indices in cyclic expressions below are modulo25. Put

\[
G_i=(27/16)^{J_i}(3/2)^{H_i},\qquad
Q_i=(12/11)(3/2)^{H_i}+1.
\]

The proposed cap concerns real tuples satisfying exactly

\[
s_{i+1}=2^{-a_i}(G_i s_i-Q_i)+\kappa\quad(0\le i<25),
\qquad s_{25}=s_0,\qquad s_i\ge540/11.
\tag{2}
\]

No J/H guards, minimum, seed, integer junctions, residue class,
actual Collatz realization or primitive-period condition are assumed.

## Conclusion

There is an explicitly defined positive rational tuple satisfying every
equation, closure and lower domain in (2), for allocation (1), with

\[
s_i>100+23/11>540/11\quad(0\le i<25),\qquad
s_2>2^{118}>(4/11)2^{112}.
\tag{3}
\]

Consequently the endpoint-only full-support cap
s2<(4/11)2^112 with b0,b1>=1 is false. This refutes that proposed
intermediate cap, not full-guard feasibility or the Collatz conjecture.
This is local REPRODUCTION of assessed finite-affine machinery, with a
new local allocation test; no originality beyond checked sources is claimed.
A separate critical audit on 2026-10-26 retained the construction without
mathematical repair; its evidence and qualifications are recorded below.

## Proof

### Exact coefficients and matching the imported enclosure

Set

\[
p_i=3J_i+H_i,\quad q_i=4J_i+H_i+a_i,\quad
c_i=3^{p_i}/2^{q_i},\qquad
\eta_i=\kappa-(16/27)^{J_i}\bigl(12/11+(2/3)^{H_i}\bigr).
\tag{4}
\]

Since J_i>=8 and H_i>0,

\[
0<(16/27)^{J_i}\le(16/27)^8<1/2,\qquad
0<12/11+(2/3)^{H_i}<\kappa.
\]

Hence kappa/2<eta_i<kappa and in particular eta_i>23/22>1.
The inequality (16/27)^8<1/2 can also be checked as
2*16^8<27^8. No tail or guard is used in this bound.

The budgets in (1) are nonnegative integers, have sum9250245,
and b0,b1>=1. The J sum is66061058 and the H sum remains199390205:
the two changes to L055's table are -35,+35. Thus

\[
\sum a_i=50+18B=166504460,\quad
K:=\sum p_i=397573379,\quad N:=\sum q_i=630138897.
\tag{5}
\]

These are exactly the operands of L104's audited enclosure, so it gives

\[
0<\lambda_-:=10584/10^{14}<\Lambda:=N\log2-K\log3
 <\lambda_+:=10585/10^{14}<1.
\tag{6}
\]

Consequently P:=product_i c_i=3^K/2^N=exp(-Lambda) lies in(0,1).
Define the positive rational denominator

\[
D=P^{-1}-1=2^N/3^K-1=\exp(\Lambda)-1.
\]

For positive Lambda<lambda_+<1 the assessed exponential inequality
exp(Lambda)<=1/(1-Lambda) gives

\[
0<D<\delta:=\frac{\lambda_+}{1-\lambda_+}
 =\frac{2117}{19999999997883}<\frac1{100}<1.
\tag{7}
\]

This uses the same real Lambda as L104, not a floating-point product
or a new enclosure. Its smallness is independent of the allocation
once the totals in (5) have been checked.

### A single exact tuple and all25 endpoints

Let C0=1 and C_i=product_(j<i)c_j. Define finite positive rationals

\[
S_i=\sum_{j=0}^{i-1}\eta_j/C_j\quad(0\le i\le25),
\qquad n_0=S_{25}/D,\qquad
n_i=C_i(n_0+S_i),\qquad s_i=n_i+\kappa.
\tag{8}
\]

These are exact factored rational definitions; no large-power expansion
or approximation is needed to specify a number. At i=0 the two
definitions of n0 agree, since C0=1,S0=0. As
C_(i+1)=C_i*c_i and S_(i+1)=S_i+eta_i/C_i, (8) gives
n_(i+1)=c_i(n_i+eta_i) at every original index0,...,24.
Moreover C25=P and S25=Dn0, so
n25=P*n0*(1+D)=n0 exactly. This retains the actual row24 tail
a24=166504160 and every chronological junction.

By (4), c_i=2^(-a_i)G_i and eta_i=kappa-Q_i/G_i.
Substituting s_i=n_i+kappa in the last recurrence yields precisely
(2). Thus the single original tuple, including its closure, satisfies
all25 endpoint equations. The finite-affine specialization in L055
and the cyclic-cut calculation in L105 use exactly this algebra;
their fixed-tail estimates, guards and witness margins are not imported.

### Every lower domain and the row2 threshold

For any original index i define P_(i,0)=1 and
P_(i,k)=product_(j=0)^(k-1)c_(i+j). The preceding recurrence,
divided by P_(i,k+1) and summed over one closed traversal, gives

\[
n_i=\mathcal B_i/D,\qquad
\mathcal B_i=\sum_{k=0}^{24}\eta_{i+k}/P_{i,k}.
\tag{9}
\]

Indeed its left and right endpoints are both n_i, and its full
product is P, so n_i=P*(n_i+mathcal B_i), which is (9).
This is an identity for the same tuple (8), not separate independently
chosen roots. All summands are positive and the k=0 term is eta_i>1.
Therefore n_i>1/D>100 for every i by (7). This proves all25 lower
domains in (3), rather than merely positivity or selected domains.

At cut2 the k=1 term of mathcal B2 is eta3/c2. Here a2=218 and

\[
p_2=3\cdot28+134=218,\qquad
q_2=4\cdot28+134+218=464,\qquad c_2=3^{218}/2^{464}.
\]

The finite comparisons

\[
3^{41}=36472996377170786403<36893488147419103232=2^{65},
\qquad 3^{13}=1594323<2097152=2^{21}
\]

imply 3^218=(3^41)^5*3^13<2^346. Thus 1/c2>2^118,
and (9),(7) give

\[
s_2=n_2+\kappa>\frac{\eta_3}{c_2D}+\kappa
 >2^{118}/\delta+\kappa>2^{118}>(4/11)2^{112}.
\]

The last comparison is simply 64>4/11 after dividing by2^112.
This proves the counterexample. No omitted guard has been used or
claimed to hold. In particular it supplies no actual closed Collatz word.

### Sources, verification and qualifications

The assessed primary input is Halbeisen–Hungerbuehler,
*Optimal bounds for the length of rational Collatz cycles*,
Acta Arithmetica78(1997),227–239, DOI10.4064/aa-78-3-227-239,
[Lemma2, pp.228–229](https://www.math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
Only finite composition and the nonzero-denominator fixed point are
used. Equations(4)–(9) verify the changed shifted-block specialization;
no general parity-coding reproof or integer realization is asserted.
The analytic source is [NIST DLMF4.6.4](https://dlmf.nist.gov/4.6.E4)
for L104's audited log enclosure and
[4.5.8–4.5.11](https://dlmf.nist.gov/4.5) for the exponential bound,
recorded version1.2.8 in the reused assessment. The positive arguments,
identical K,N and 0<Lambda<1 hypotheses are checked above.

Reproduce the finite operands with
`python3 scripts/postspell-word-count/certify_d35_full_support_row2_counterexample.py`.
It writes
`scripts/postspell-word-count/d35-full-support-row2-counterexample-certificate.json`
containing all25 changed rows, every cyclic-cut prefix as factored
exponents, the exact tuple definitions, imported enclosure, full rational
bound operands and249 passing checks with no failures. The complete rows,
bound operands and load-bearing cut2 prefix were inspected. The proof
above establishes the affine identities and all-cut inequalities;
neither a certificate preview nor the number of passing checks proves them.
No approximate root, sampling or huge rounded orbit is used. This is a
construction check, not an independent audit or formal verification.

L105 remains valid on b2=...=b23=0; the allocation(1) leaves that
triangle. L103's guard-conditioned cap was not used. Attempt032's
failed sufficient package, both original-H witnesses and unfinished
work are preserved. This result abandons only the endpoint-only cap;
support/order exhaustion, other guards, actual-word transfer, entry,
unrestricted cycles, divergence and universal descent remain open.

### Independent critical audit — 2026-10-26

This separate RESEARCH/REPRODUCTION audit used the invocation-start
SPECIALIZE assessment
`drafts/literature/2026-10-26-l106-endpoint-counterexample-critical-audit.md`.
No mathematical defect was found in the stated endpoint-only conclusion.
This establishes a dependable local obstruction to the proposed cap,
not a new general result beyond the sources checked. The construction
certificate and earlier unfinished notes remain preserved.

The independent transcription of L055's literal25 pairs, followed by
exactly H0-=35 and H24+=35, agrees with every changed row in the
construction certificate. Allocation (1) sums to9250245. Its tails are
20,20,218 at rows0,1,2, tail2 at rows3 through23, and166504160 at
row24. Direct summation gives sum J=66061058, sum H=199390205,
sum a=166504460 and precisely K=397573379,N=630138897. Thus L104's
audited enclosure concerns the identical real Lambda; neither its
fixed allocation nor its guard exclusion is imported. The complete
L104 enclosure argument and its separate audit were inspected. The
log enclosure was reused, not recertified in this step.

Directly in (2), the substitution s_i=n_i+kappa gives
n_(i+1)=c_i*n_i+c_i*kappa-2^(-a_i)*Q_i. Dividing Q_i by G_i
gives both subtractions in (4), with the signs shown there. Every
J_i>=8 and H_i>0, and the exact comparison 2*16^8<27^8 holds.
Consequently Q_i/G_i is strictly between0 and kappa/2, giving
eta_i>kappa/2=23/22>1 at every row without any guard premise.
The matching Lambda interval implies 0<P<1 and
0<D<2117/19999999997883<1/100. The exponential upper bound applies
only at the positive argument Lambda<lambda_+<1, as required;
strictness follows already from Lambda<lambda_+ and monotonicity of
x/(1-x). No subtraction of approximate large powers is involved.

For an independent check that all cyclic roots are the same tuple,
write B_i for the numerator in (9). In the original tuple (8),
multiplying n_i by D and using D+1=P^-1 gives

\[
D n_i=C_i\left(P^{-1}\sum_{j<i}\frac{\eta_j}{C_j}
                    +\sum_{j\ge i}\frac{\eta_j}{C_j}\right).
\tag{10}
\]

If j>=i, the cyclic prefix from i to j is C_j/C_i. If j<i, it
is P*C_j/C_i, because the traversal crosses the closing row24
exactly once. Their reciprocals are exactly the coefficients in (10).
This proves D n_i=B_i simultaneously for all25 original coordinates,
including the empty prefix at j=i. Each rational is finite and the
common denominator is nonzero. There is no independently selected
root at another cut, cyclic reordering beyond rotation, or implicit
minimum assumption.

The audit independently sums all625 cyclic-prefix exponent pairs
from their indicated row subsets and compares them with both the
original certificate and the coefficients in (10). As a further exact
identity check it represents coefficients by Laurent monomials
3^p/2^q and treats the eta_j as independent symbols. For every i,
including24, all coefficients of the following residual cancel:

\[
B_{i+1}-c_i B_i-c_i\eta_i(P^{-1}-1)=0,
\qquad B_{25}=B_0.
\tag{11}
\]

Dividing by D proves the recurrence for the same tuple (10);
adding kappa returns all original endpoint equations, with row24's
output at row0. This symbolic check is stronger than a numerical
replay of the enormous coordinates. It does not impose parity,
integrality, residues or primitive period; repetitions remain allowed.

All B_i terms are strictly positive and their k=0 terms equal eta_i>1.
Thus every n_i>1/D>19999999997883/2117>100 and every
s_i>220000000025404/23287>540/11. This is an all-coordinate bound,
not a check of a distinguished minimum. At cut2 the k=1 summand is
eta3/c2, and its independent prefix exponents are exactly(218,464).
The complete integer comparisons 3^41<2^65 and3^13<2^21 hold;
41*5+13=218 and65*5+21=346. A direct finite comparison also confirms
3^218<2^346. Therefore the strict lower bound for s2 is

\[
s_2>\frac{73107539760431939925248554332341212926812904013363}{23287}
 >2^{118}.
\]

The proposed threshold is20769187434139310514121985316880384/11,
and the difference between2^118 and that threshold is the positive
rational3634607800974379339971347430454067200/11. These strict bounds
validate precisely (3); they assert no J/H guard satisfaction.

Reproduce the independent finite audit with
`python3 scripts/postspell-word-count/audit_d35_full_support_row2_counterexample.py`.
It neither imports nor executes the construction program. Its full
certificate is
`scripts/postspell-word-count/d35-full-support-row2-counterexample-audit-certificate.json`.
All1923 checks pass with no failures. The audit consumes and compares
all25 complete rows, all625 stored cyclic prefixes and exact bounds;
it also replays every one of the249 original finite comparisons and
its saved difference without trusting pass flags. Complete endpoint
residuals, threshold and lower-domain operands were separately inspected
with the scoped inspector. The check count is not the proof: (10)–(11),
the shift, positivity and exact inequalities above establish it.

The cited finite-affine and positive-real methods remain the same.
L055 supplies the literal table and affine construction, L104 the
matching audited enclosure, and L105 the shifted/cyclic-cut identities
only; its fixed-tail cap is not used here. No DAG dependency changes.
Mathlib coverage remains unchecked. The audit does not revisit the
failed sufficient package of Attempt032, extend the L105 triangle,
or establish guard feasibility, actual-word realization, support/order
exhaustion, entry, divergence or universal descent. Attempt033's
endpoint-only cap rejection is now independently audited.

## Mathlib

Full matching theorem and supporting Mathlib coverage were not checked
for this exact endpoint system. Unknown coverage is not evidence of
absence. The rational certificate is not a Lean proof.
