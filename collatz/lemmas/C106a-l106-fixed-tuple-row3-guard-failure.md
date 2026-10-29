# C106a — L106's fixed endpoint tuple violates row3's own J guard

## Hypotheses

Use exactly the positive rational chronological tuple of L106 (8),
with L055's literal25-row table modified only at H0=5,H24=32670656.
Fix kappa=23/11,B=9250245, b0=b1=1,b2=12,b24=9250231,
all other b_i=0, and a_i=2+18b_i. In particular J3=52,H3=249.
All25 endpoints, closure and lower domains are those proved in L106.
For indices modulo25 put

\[
c_i=3^{3J_i+H_i}/2^{4J_i+H_i+a_i},\qquad
\eta_i=\kappa-(16/27)^{J_i}\bigl(12/11+(2/3)^{H_i}\bigr),
\quad n_i=s_i-\kappa.
\]

The own-input guards to be tested are
4J_i log2 <= log s_i+log(11/4) and
H_i log2 < log s_i+J_i log(27/16), with natural logarithms.
They are not assumptions on the tuple. No minimum, seed, integer or
residue junction, exact valuation, actual-word realization or primitive
period is assumed. Repetitions remain allowed.

## Conclusion

The fixed tuple strictly violates its original row3 non-strict J guard:

\[
s_3<\frac{2300000000030429}{14553}<10^{12}
 <\frac4{11}2^{208}.
\tag{1}
\]

Thus it is not feasible for the full J/H system. The other49 guards
are untested; the endpoint-only counterexample L106 remains valid.
This is a local RESEARCH/REPRODUCTION calculation of assessed affine
machinery, with no claim of novelty beyond the sources checked.
A separate critical audit on 2026-10-26 retained the verdict without
mathematical repair, as recorded below. It excludes only this fixed tuple,
not other allocations, actual cycles or divergent trajectories.

## Proof

### Same chronological tuple and denominator

L106 proves 0<eta_i<kappa and, for every original cut i, the identity

\[
n_i=\frac{\mathcal B_i}{D},\qquad
\mathcal B_i=\sum_{k=0}^{24}\frac{\eta_{i+k}}{P_{i,k}},\qquad
P_{i,k}=\prod_{j=0}^{k-1}c_{i+j},\quad P_{i,0}=1,
\quad D=\exp(\Lambda)-1.
\tag{2}
\]

These are coordinates of L106's single tuple (8), not independently
chosen roots. Its sums are K=397573379,N=630138897 and
Lambda=N log2-K log3. Thus precisely L104's audited enclosure applies:

\[
0<\lambda_-:=10584/10^{14}<\Lambda
 <\lambda_+:=10585/10^{14}<1/2.
\]

The assessed positive-real exponential bounds give

\[
D>\Lambda>\lambda_-,\qquad
e^{\Lambda}\le(1-\Lambda)^{-1}<(1-\lambda_+)^{-1}<2.
\tag{3}
\]

Only the matching enclosure is imported from L104, not its allocation
or guard exclusion. No new logarithmic approximation is used here.

### All25 terms at cut3, including closure

For rows3 through23, a_i=2,H_i>=6,J_i>0, so

\[
c_i=(27/16)^{J_i}(3/2)^{H_i}/4
 >(3/2)^6/4=729/256>2.
\]

At cut3 the first22 terms, k=0,...,21, have input rows3,...,24.
Their prefixes contain only rows3,...,23, so

\[
\sum_{k=0}^{21}P_{3,k}^{-1}
 \le\sum_{k=0}^{21}2^{-k}
 =4194303/2097152<2.
\tag{4}
\]

The remaining inputs are rows0,1,2. The full product is exactly
P=product_i c_i=exp(-Lambda). Taking the complementary factors yields

\[
P_{3,22}^{-1}=c_0c_1c_2e^{\Lambda},\qquad
P_{3,23}^{-1}=c_1c_2e^{\Lambda},\qquad
P_{3,24}^{-1}=c_2e^{\Lambda}.
\tag{5}
\]

This keeps row24's actual tail166504160 and the original closing
row24-to-row0 junction. No growth estimate is applied to row24.
Direct coefficient matching at rows0,1,2 gives respectively
(p_i,q_i)=(29,57),(117,152),(218,464), where c_i=3^p_i/2^q_i.
The exact comparisons 3^5=243<256=2^8 and 3^r<2^(2r)
for r=3,4 imply

\[
c_2=3^{218}/2^{464}<2^{350-464}<1,
\quad c_1c_2=3^{335}/2^{616}<2^{536-616}<1,
\quad c_0c_1c_2=3^{364}/2^{673}<2^{584-673}<1.
\tag{6}
\]

Here 218=5*43+3,335=5*67,364=5*72+4. Combining (3),(5),(6)
bounds each of the final three reciprocal prefixes strictly below2.
All eta_i lie strictly between0 and kappa. Consequently all25
positive terms in (2) are retained and

\[
0<\mathcal B_3<\kappa(2+2+2+2)=8\kappa.
\]

Equations (2),(3) therefore give

\[
s_3=n_3+\kappa
 <8\kappa/\lambda_-+\kappa
 =2300000000030429/14553<10^{12}.
\tag{7}
\]

For a finite integer check of the last inequality,
2300000000030429<14553000000000000.
Since s3>0, exponentiating its own non-strict J3=52 guard is equivalent
to s3>=(4/11)2^208. But

\[
(4/11)2^{208}
 =1645504557321206042154969182557350504982735865633579863348609024/11
 >10^{12}.
\]

This proves the strict failure in (1), which suffices to end the
approved test. No verdict on any remaining J or strict H guard is needed.

### Sources, certificate and limits

The invocation-start SPECIALIZE assessment is
`drafts/literature/2026-10-26-l106-own-input-guard-test.md`.
The finite-affine primary source is Halbeisen–Hungerbuehler,
*Optimal bounds for the length of rational Collatz cycles*,
Acta Arithmetica78(1997),227–239, DOI10.4064/aa-78-3-227-239,
[Lemma2, pp.228–229](https://www.math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
L106 already verifies the changed shifted-block coefficients and
the same-tuple formula (2); only the additional guard comparison is
specialized here. No general coding reproof or rational-cycle
interpretation is imported. The matching audited enclosure uses
[NIST DLMF4.6.4](https://dlmf.nist.gov/4.6.E4), recorded version1.2.8;
the positive-real exponential series is
[DLMF4.2.19](https://dlmf.nist.gov/4.2.E19). Its geometric majorant
is used only at 0<Lambda<1/2, as checked in (3).

Reproduce the exact finite operands with
`python3 scripts/postspell-word-count/certify_l106_row3_guard_failure.py`.
It writes
`scripts/postspell-word-count/l106-row3-guard-failure-certificate.json`,
with all25 changed rows, all25 cut3 prefixes, complementary products,
imported enclosure operands, exact rational bounds and92 passing checks
with no failures. Complete relevant prefix, product and bound values
were inspected. The proof above establishes the analytic inequalities
and ties every term to the same original tuple; passing flags or a
preview alone are not a proof. This is a construction check, not an
independent audit or formal verification.

This parks only the proposal to use this fixed endpoint tuple as a
full-guard witness. L106's endpoint-only cap refutation, L105's
fixed-tail triangle, Attempt032/033, original-H witnesses and unfinished
work remain intact. Other supports, order exhaustion, entry, realization,
unrestricted cycles, divergence and universal descent remain unresolved.

### Independent critical audit — 2026-10-26

This separate RESEARCH/REPRODUCTION audit used the invocation-start
SPECIALIZE assessment
`drafts/literature/2026-10-26-c106a-row3-guard-critical-audit.md`.
No defect was found within the fixed-tuple conclusion (1). This verifies
a local specialization of the assessed machinery; it makes no claim
of mathematical novelty beyond the sources checked. The construction
certificate and unfinished work are preserved.

The audit independently transcribed all25 literal J,H pairs from L055,
applied only H0-=35,H24+=35, and independently assigned the four nonzero
budgets in the hypotheses. Every changed row and every construction
coefficient agrees. Direct sums give sum J=66061058,
sum H=199390205,sum a=166504460,sum b=9250245, hence exactly
K=397573379,N=630138897. Row24's tail is166504160. The full
L104 enclosure argument and its separate audit were inspected; this
audit reuses that enclosure at the identical operands, without importing
L104's different allocation or guard verdict and without recomputing
logarithms. L106's complete audited proof supplies the one rational
tuple, all endpoints, closure, lower domains and identity (9).

For a direct check of the cut and denominator, let
z_k=n_((3+k) mod25) and P_k=P_(3,k). The original recurrence gives
z_(k+1)/P_(k+1)=z_k/P_k+eta_((3+k) mod25)/P_k.
Summing k=0,...,24 and using z25=z0 and P25=P yields
z0/P=z0+B3, hence z0=B3/(P^-1-1). Thus the denominator is
precisely exp(Lambda)-1 and this is the original n3, not a new
independently selected root. Shifting back gives the original s3.
L106's positive eta bound uses only J>=8,H>0 and
2*16^8<27^8; all these hypotheses were checked row by row.
In particular no guard is assumed to bound the eta or establish closure.

The audit independently sums each of the25 prefix exponent pairs
from its complete indicated row subset. The order is exactly
3,...,24,0,1,2. For k=0,...,21 the inputs are3,...,24 and the
prefix factors are subsets of3,...,23 only. Each of those21 factors
has tail2,H>=6,J>0, so its strict lower bound729/256>2 applies.
The empty prefix is retained and the complete geometric sum is
4194303/2097152<2. At k=22,23,24 the prefix exponent pairs are
respectively

\[
(397573015,630138224),\quad
(397573044,630138281),\quad
(397573161,630138433).
\]

Their differences from (K,N) are exactly (364,673),(335,616),
(218,464). They are the complements {0,1,2},{1,2},{2}, proving
every identity in (5), including the positive sign on Lambda.
All three prefixes include row24 with its actual tail and cross the
closing junction once. No tail2 growth bound is applied to that row.

The integer decompositions364=5*72+4,335=5*67,
218=5*43+3 give precisely the upper numerator exponents584,536,350.
The audit checks both these small-power bounds and the direct finite
comparisons3^364<2^673,3^335<2^616,3^218<2^464.
Thus all three complementary products are strictly below1.
The imported interval satisfies0<lambda_-<Lambda<lambda_+<1/2;
the positive-real exponential series gives D>Lambda, and its geometric
majorant gives exp(Lambda)<=1/(1-Lambda)<1/(1-lambda_+)<2.
All25 positive numerator terms, with eta<23/11, are therefore covered
by the strict bound8*23/11. No summand or closure term is dropped.

The independent exact cap is2300000000030429/14553, strictly below
10^12. The own-input table value is J3=52, so monotonicity of exp on
the positive coordinate s3 converts its non-strict guard into
s3>=(4/11)2^208. The full threshold in (1) and its strict separation
from both bounds were recomputed exactly. There is no reliance on
logarithmic rounding, an adjacent input's guard, or a strict J convention.
The H guards are not needed for this failure and none is tested here.

Reproduce the independent finite audit with
`python3 scripts/postspell-word-count/audit_l106_row3_guard_failure.py`.
It neither imports nor executes the construction program. Its complete
certificate is
`scripts/postspell-word-count/l106-row3-guard-failure-audit-certificate.json`.
All729 checks pass with no failures. It compares all25 changed rows,
all25 complete cut3 prefixes, all three complementary products and all
bound operands; it also replays all92 construction comparisons and
their exact saved differences without trusting pass flags. The complete
rows, prefixes, complements, enclosure operands and bounds were inspected
with the scoped inspector. These finite checks support the identities
and analytic proof above; their count is not itself a proof.

No direct mathematical dependency changes. L055 supplies only the table
and guard conventions, L104 the matching audited enclosure, and L106
the original tuple and cut identity. The cited primary finite-affine
and positive-real methods remain as stated above. Repetitions are allowed;
no minimum, seed, integer/residue junction, exact valuation, primitive
period or actual-word premise was introduced. The other49 guards remain
untested. This confirms Attempt034's stop for this fixed witness only;
L106's endpoint-only counterexample and L105's triangle survive.
Other supports, support/order exhaustion, entry, realization, unrestricted
cycles, divergence and universal descent remain unresolved.

## Mathlib

The full matching theorem and supporting Mathlib coverage for this exact
fixed-tuple guard test were not checked. Unknown availability is not
evidence of absence. The rational certificate is not a Lean proof.
