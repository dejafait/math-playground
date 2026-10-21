# L077 — Variable-table sufficient last-pair cutoff

## Hypotheses

Let r>=3 and B>=0 be integers. Fix integer pairs with
2<=J_0<...<J_(r-1) and H_i>=3, in literal indexed order. Put
p=r-2, q=r-1, kappa=23/11 and

\[
K=\sum_{i=0}^{q}(3J_i+H_i),\qquad
N=\sum_{i=0}^{q}(4J_i+H_i)+2r+18B,\qquad
\Lambda=N\log2-K\log3.
\tag{1}
\]

For every integer 0<=t<=B set b_i=0 for i<p, b_p=t,
b_q=B-t and a_i(t)=2+18b_i. Define the following rational data:

\[
c_i(t)=\frac{3^{3J_i+H_i}}{2^{4J_i+H_i+a_i(t)}},\quad
C_i(t)=\prod_{j<i}c_j(t),\quad C_0(t)=1,
\]
\[
\eta_i=\kappa-\frac{12}{11}(16/27)^{J_i}
                    -(16/27)^{J_i}(2/3)^{H_i}.
\tag{2}
\]

Require certified rational constants lambda_-,lambda_+,e with

\[
0<\lambda_-\le\Lambda\le\lambda_+<1,\qquad
0<e\le\min(\eta_0,\eta_q),\qquad
\frac{e(1-\lambda_+)}{\lambda_+}\ge47.
\tag{3}
\]

Choose a nonnegative integer cutoff tau. If tau<=B, require positive
rationals L_0,...,L_q,Q,U and rationals T,ell,u,v satisfying

\[
0<L_i\le C_i(\tau)\quad(0\le i\le q),\qquad
Q\ge\kappa\sum_{i=0}^{q}\frac1{L_i},
\]
\[
\frac{Q}{\lambda_-}+Q+\frac{\kappa}{L_q}\le U\le\exp(T),
\qquad 0<\ell\le\log2,\quad \log3\le u,\quad\log(11/4)\le v.
\tag{4}
\]

Define the incoming prefix exponents at the boundary by

\[
k_q=\sum_{i<q}(3J_i+H_i),\qquad
d_q(\tau)=\sum_{i<q}(4J_i+H_i+a_i(\tau)).
\]

The final rational test is

\[
F:=T+k_qu-(d_q(\tau)+4J_q)\ell+v<0.
\tag{5}
\]

All tests concern only the finite indexed table, budget, chosen cutoff
and certificate constants. Logarithm/exponential comparisons in (3)–(4)
require certified inequalities rather than approximate decimals. The
prefix tests may use exact products or proved rational lower bounds.
No unknown junction or guard verdict occurs in these tests. If tau>B,
there are no rejection parameters and tests (4)–(5) are omitted; (3)
still suffices for the endpoint/domain conclusion below.

The tested subsystem consists of real s_0,...,s_r with s_r=s_0,
s_i>=540/11 and, for every indexed outgoing row including closure,

\[
s_{i+1}=2^{-a_i(t)}\left((27/16)^{J_i}(3/2)^{H_i}s_i
                     -(12/11)(3/2)^{H_i}-1\right)+23/11,
\]
\[
4J_i\log2\le\log s_i+\log(11/4).
\tag{6}
\]

These are only L051's endpoint/domain/non-strict own-input J conditions.
No H guard, seed, minimum location, integer junction, parity, residue,
exact valuation, actual-word, primitive-count or count-ray premise is used.

## Conclusion

Under (3), each integer 0<=t<=B has exactly one real cyclic endpoint
tuple. It is positive rational and every unshifted input
n_i=s_i-23/11 is strictly greater than 47, so all its domain conditions
hold. As t increases, inputs 0,...,p strictly increase and input q
strictly decreases, whenever two distinct parameters are available.

If tau<=B and (4)–(5) hold, the own-input J guard of row q fails for
every integer tau<=t<=B. Its right-minus-left margin at tau is strictly
less than F<0 and decreases thereafter. Thus any feasible parameter in
(6) lies in 0<=t<tau. No passing parameter is asserted for general tables.
If tau>B the rejection interval is empty. In particular B=0 or B=1,
with tau=2, requires no boundary tests and implies no guard verdict.
The uniform endpoint/domain assertion in these cases still needs (3).

For L055's table and B=9250245 these tests hold with tau=2. They recover
every L068 rejection through t=B, including final tail 2, with the same
strict margin bound -474883782659/125000000000<-3.79. The t=0 and t=1
J-feasible rational tuples are imported from audited L055/L064 (also
assembled in audited L068), rather than asserted for arbitrary tables.

This is a sufficient criterion only. Failed tests imply neither
feasibility nor failure of a cutoff. This local REPRODUCTION specializes
known affine machinery and L068's mechanism under the prior SPECIALIZE
assessment `drafts/literature/2026-10-17-variable-table-last-pair-cutoff.md`;
no originality beyond inspected sources is claimed. The separate critical
audit below found no defect. No new table, survivor integer exclusion, order/support
assembly, actual-word application or universal eventual descent is proved.

## Proof

### Imported machinery and coordinate applicability

Import formal finite-word affine composition and its nonzero-denominator
fixed-point formula from Halbeisen–Hungerbuehler, *Optimal bounds for the
length of rational Collatz cycles*, Acta Arithmetica 78 (1997), 227–239,
DOI 10.4064/aa-78-3-227-239,
[section 2, equations (2)–(4), Lemma 2, pp. 228–229](https://www.math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
The finite nonempty prescribed word has N letters and K odd letters;
the exponents in (1) count each actual tail. Condition (3) guarantees
2^N-3^K>0. Only formal affine algebra is used, with no integer-realization
converse. The following coordinate and parameter computations are needed
because the table and budget now vary; general coding is not reproved.

Reuse the positive-real log/exp facts and series coverage assessed before
this turn: [DLMF 4.5.1](https://dlmf.nist.gov/4.5.E1),
[4.6.4](https://dlmf.nist.gov/4.6.E4) and
[4.2.19](https://dlmf.nist.gov/4.2.E19). In particular L068's proved
series comparison gives w<exp(w)-1<w/(1-w) for 0<w<1. Its strict
signs, and monotonicity of log/exp on positive arguments, apply to (3).
Benchmark analytic enclosures are imported from audited L055/L064/L068;
no new analytic theorem or fixed-table bound is assumed for other tables.

For all these pairs, 0<eta_i<kappa: both powers in the subtracted terms
lie in (0,1), so their sum is positive and strictly below 12/11+1=kappa.
L051's pointwise shift, or direct substitution in (6), gives exactly

\[
n_{i+1}=c_i(t)(n_i+\eta_i),\qquad n_i=s_i-\kappa.
\tag{7}
\]

Indeed with G_i=(27/16)^{J_i}(3/2)^{H_i},
G_i eta_i=kappa G_i-(12/11)(3/2)^{H_i}-1. This identity uses no
minimum or guard. Every tail is at least 2 throughout 0<=t<=B, including
a_q(B)=2, and their sum is 2r+18B. Hence
C_r(t)=3^K/2^N=exp(-Lambda), independently of t. Put

\[
D=2^N/3^K-1=\exp(\Lambda)-1,
\qquad 0<\lambda_-<D<\frac{\lambda_+}{1-\lambda_+}.
\tag{8}
\]

The inequalities follow from (3) and the strict series comparison.
Composition, with the last edge included, gives the unique cyclic root

\[
S(t)=\sum_{j=0}^{q}\frac{\eta_j}{C_j(t)},\qquad
n_0(t)=\frac{S(t)}D,\qquad
n_i(t)=C_i(t)\left(n_0(t)+\sum_{j<i}\frac{\eta_j}{C_j(t)}\right).
\tag{9}
\]

The denominator is nonzero, so this is the unique real endpoint tuple,
not merely the unique positive tuple. Formula (9) satisfies every edge
and closure algebraically, and all its inputs are positive rationals.

### Parameter signs and the full uniform domain

Set x=2^(-18t), C=C_q(0)>0 and
A=sum_(j<q)eta_j/C_j(0)>0. Incoming C_i and their partial sums for
i<=p do not depend on t. Only incoming prefix q includes the changed
row p, giving C_q(t)=Cx; the changed last row restores C_r(t).
Consequently (9) specializes to

\[
n_0(t)=\frac{A+\eta_q/(Cx)}D,\qquad
n_q(t)=Cx(n_0(t)+A)
       =\frac{\eta_q}D+\frac{CA(1+D)}D x.
\tag{10}
\]

All displayed coefficients are strictly positive. Thus decreasing x
increases n_0 and, through the unchanged positive prefixes in (9),
every n_i for i<=p. It strictly decreases n_q. The same directions
hold for s_i and their own-input J margins. This uses both varying tails
in exact closure and assumes no growth of their individual maps.

For the unchanged rows i<p, their actual tail is 2 and

\[
c_i\ge(27/16)^2(3/2)^3/4=19683/8192>2.
\]

Thus C_i>=1 for i<=p, including the empty prefix. Since A>=eta_0,
(8)–(10) and (3) give n_0>eta_0/D>e(1-lambda_+)/lambda_+>=47.
Formula (9) gives n_i>=n_0>47 for i<=p, while (10) separately gives
n_q>eta_q/D>e(1-lambda_+)/lambda_+>=47. This proves every lower-domain
condition uniformly, without using a varying-row growth estimate or
locating the smallest input. Closure repeats n_0 and retains its domain.

### One certified boundary rejects the entire remaining interval

Suppose tau<=B and (4)–(5) hold. At t=tau, 0<eta_i<kappa and
C_i>=L_i imply S(tau)<kappa sum_i(1/L_i)<=Q. Also
sum_(j<q)eta_j/C_j<S(tau)<Q. Divide the q-th expression in (9) by
C_q, add the shift kappa/C_q, and use (8) and (4):

\[
\frac{s_q(\tau)}{C_q(\tau)}
 =\frac{S(\tau)}D+\sum_{j<q}\frac{\eta_j}{C_j(\tau)}
                         +\frac{\kappa}{C_q(\tau)}
 <\frac{Q}{\lambda_-}+Q+\frac{\kappa}{L_q}\le U\le e^T.
\tag{11}
\]

All denominators and arguments are positive. Therefore
log s_q(tau)<T+log C_q(tau)=T+k_q log3-d_q(tau) log2.
The right-minus-left margin of its own outgoing J guard satisfies

\[
\log s_q(\tau)+\log(11/4)-4J_q\log2
 <T+k_q\log3-(d_q(\tau)+4J_q)\log2+\log(11/4)
 \le F<0.
\tag{12}
\]

Here k_q>0 and d_q(tau)+4J_q>0, so the upper log3/log(11/4) and
lower log2 enclosures have exactly the required directions. By (10)
the same margin strictly decreases at every larger parameter. This
rejects every integer tau<=t<=B against the non-strict guard, not just
sampled endpoints. If tau=0 or tau=1 the argument is unchanged; no
known-survivor premise is imposed. If tau>B the rejected set is empty
and (11)–(12) are not invoked. The root/domain proof applies also to
B=0. For r=3, p=1 and q=2, the unchanged prefix consists of row 0;
all sums and the positive A in (10) remain valid.

### Full L068 benchmark and finite evidence

Use L055's complete table with B=9250245, tau=2, e=2 and
lambda_-=10584/10^14, lambda_+=10585/10^14. Audited L055 supplies
this Lambda enclosure. All its pairs have J>=8,H>=40, so
eta_0<=eta_i and its exact eta_0 is greater than 2. This verifies both
eta tests, including the last row. The domain lower bound is

\[
\frac{2(1-\lambda_+)}{\lambda_+}
 =\frac{39999999995766}{2117}>18\cdot10^9>47.
\]

At tau=2, audited L068 proves c_0>10^8 and c_i>2 for 1<=i<=23
from the exact comparison 3^117/2^170>2. These bounds are used only
at this boundary, where a_23=38 and a_24=166504376. Choose

\[
L_0=1,\quad L_i=10^8 2^{i-1}\ (1\le i\le24),\qquad
Q=\frac{23}{11}(1+2/10^8)=\frac{1150000023}{550000000},
\]
\[
U=Q/\lambda_-+Q+23/11
 =\frac{435606069410390910013}{22050000000}<20\cdot10^9,\quad T=24.
\]

The finite geometric sum gives kappa sum_i(1/L_i)<Q; L_q>=1
ensures Q/lambda_-+Q+kappa/L_q<=U. L068's certified positive
41-term sum for exp(24) exceeds 20*10^9, so U<exp(T).
Import its audited logarithm bounds with S=10^12:

\[
\ell=693147180559/S,\quad
u=1098612288669/S,\quad v=1011600911679/S.
\]

The incoming exponents are k_q=271907921 and d_q(2)=306970784;
J_q=30998279. Thus (5) is exactly

\[
F=\frac{24S+271907921(1098612288669)
             -430963900(693147180559)+1011600911679}{S}
 =-\frac{474883782659}{125000000000}<-3.79<0.
\]

This recovers every rejection 2<=t<=9250245, including the boundary
where a_24=2. Passing t=0,1 and all their J guards are separate imported
facts from audited L055/L064/L068; their two rational witnesses remain
valid. No survivor arithmetic or H/seed verification is repeated here.
The old unnecessary margin<-4 probe remains false and preserved in
L068's certificate; it is not required by (5).

Reproduce only this criterion's finite benchmark checks with
`python3 scripts/postspell-word-count/certify_variable_table_last_pair.py`.
Its complete certificate is
`scripts/postspell-word-count/variable-table-last-pair-certificate.json`.
It records every incoming prefix bound, exact test operands, exponential
terms, boundary/full exponents, imported analytic qualifications, the
old failed probe and the entire rejected parameter interval. These
checks supplement the quantified proof (7)–(12); finite computation
alone proves no general table criterion or integer orbit realization.
All 17 required rational checks and 11 integer checks pass. The complete
check operands, all 25 prefix bounds, boundary table and all 41 positive
exponential terms were inspected. Imported Lambda/logarithm enclosures
are explicitly identified as imported, rather than freshly recertified.

### Independent critical audit — 2026-10-17

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-17-variable-table-last-pair-critical-audit.md`.
The independent review found no defect in the stated sufficient criterion
or its complete L068 benchmark. This verifies an existing local
REPRODUCTION; it supplies no stronger conclusion or claim of originality.
The precise affine and positive-real analytic citations above are reused.
L051 is used only for its pointwise endpoint/J/shift facts, not its
additional seed, minimum, H or primitive-count assumptions.

**All parameters, closure and signs.** For each indexed row, substitution
of s=n+kappa gives the coefficient c_i on n and constant c_i eta_i:
G_i(16/27)^J_i=(3/2)^H_i and the additional factor (2/3)^H_i
makes the latter product 1. Both subtracted terms in eta_i are positive
and have sum strictly below kappa for J_i>=2,H_i>=3. Thus
0<eta_i<kappa for every row; monotonicity of H across rows is unnecessary.
The total of both changing tails is constant, so the full cyclic
multiplier is C_r=exp(-Lambda)=1/(1+D), including the final edge.
The standard fixed-point formula applies since (3) gives D>0.
Successively dividing each recurrence by its incoming/outgoing prefix
gives (9); at the final edge closure is n_0=C_r(n_0+S), precisely
D n_0=S. These rational formulas prove existence and uniqueness over
all real endpoint tuples, as well as positivity, without realizing any
integer parity sequence.

For i<=p the incoming prefix and its partial offset sum contain neither
changing row. Incoming prefix q contains row p but not row q, giving
C_q=Cx, S=A+eta_q/(Cx). Substitution yields exactly
n_q=eta_q/D+CA(1+D)x/D. Here A includes q positive summands, C>0,
D>0 and eta_q>0. Every coefficient needed for strict monotonicity is
therefore positive. The opposite change in the closing row is retained
through constant D. Decreasing x as t increases strictly raises all
inputs through p and strictly lowers input q; no comparison of either
varying map with the identity is used.

**Uniform domain.** The elementary positive-real series inequalities
give lambda_-<D<lambda_+/(1-lambda_+), even when either endpoint in
the Lambda enclosure is attained. Only rows i<p need growth: their
tail is exactly 2 and their multiplier is at least 19683/8192>2.
Thus C_i>=1 for i<=p, and the positive partial offsets give
n_i>=n_0>eta_0/D>e(1-lambda_+)/lambda_+>=47. The separate formula
for q gives n_q>eta_q/D>e(1-lambda_+)/lambda_+>=47. The strict
signs survive equality in the certified eta or domain tests. Closing
input n_r=n_0 also has the required domain. No designated minimum
or growth at either changing row is assumed.

**Boundary sufficiency and edge cases.** At tau, all L_i,C_i,D and
lambda_- are positive. Since each eta_i<kappa, the complete S is
strictly below kappa sum 1/L_i<=Q; its proper partial sum is below S.
The identity s_q/C_q=S/D+sum_(j<q)eta_j/C_j+kappa/C_q
then gives (11), strictly, including the shift. Taking logarithms is
valid and preserves this strict upper bound. The coefficient k_q of
log3 is positive, while -(d_q+4J_q) is negative; therefore precisely
the upper log3/guard and lower log2 bounds in (4) give (12).
A strictly negative right-minus-left margin contradicts the non-strict
own-input guard. Formula (10) propagates that rejection to every larger
integer in the closed parameter range, not merely its sampled endpoints.

When r=3, p=1 and q=2: C_p contains just unchanged row 0, A has
the two terms eta_0 and eta_1/C_1, and the same positive-coefficient
argument applies. For tau=0 or 1 no survivor is assumed; if the tests
pass they reject the asserted range. For tau=B, the same boundary
calculation includes a_q=2 and rejects that single parameter. For tau>B,
(4)–(5) are unused and the rejection range is empty; (3) still proves
the entire endpoint/domain claim. This includes B=0 or 1 with tau=2.
For B=0 there are no distinct parameters to compare, so strict
monotonicity asserts nothing beyond its stated qualification. These are
logical boundary checks, not claims that any arbitrary table passes (3).

**Independent complete benchmark.** Run
`python3 scripts/postspell-word-count/audit_variable_table_last_pair.py`.
This program neither imports nor runs the construction program. It
compares a separately transcribed table with all 25 canonical L055 rows,
reconstructs the 25 boundary rows and all incoming/closing exponent sums,
all 25 rational prefix bounds, all 17 original rational comparison
records with full operands and differences, all 11 integer comparisons,
and all 41 positive terms of the exp(24) lower sum. The incoming
counts are 271907921 and 306970784, the full counts remain
397573379 and 630138897, and the negative log2 coefficient is
430963900. In particular the complete finite reciprocal sum satisfies
Q-kappa sum_i(1/L_i)=23/9227468800000000>0.

The rational comparisons give eta_0>2,
e(1-lambda_+)/lambda_+=39999999995766/2117>18*10^9>47,
and U=435606069410390910013/22050000000<20*10^9.
The positive 41-term exponential sum exceeds 20*10^9, so U<exp(24).
Every intermediate prefix bound is justified by c_0>10^8 and, only
at this boundary, c_i>=3^117/2^170>2 for 1<=i<=23. No such bound
is transferred to larger t. Exact substitution gives the unchanged
F=-474883782659/125000000000<-3.79. The optional F<-4 probe
remains false and is preserved verbatim with the original artifacts.

For an additional independent check of the imported analytic operands,
the program uses the already proved integrated geometric remainder with
128 unrounded rational terms. For z=2,3,11/4 and
z=(18*10^9)/2^34, set x=(z-1)/(z+1), so 0<x<=1/2. Then
P=2 sum_(j=0)^127 x^(2j+1)/(2j+1) and
R=2x^257/(257(1-x^2)) satisfy P<log z<P+R. Indeed the remainder
is 2 integral_0^x u^256/(1-u^2) du; its positive integrand has a
strict integral upper bound obtained by replacing 1-u^2 by 1-x^2.
These intervals check both grid endpoints for all three logarithms,
both sides of N log2-K log3 with opposite interval endpoints, and
log(18*10^9)>23.61 after adding 34 log2 to the fourth interval.

The t=0 tails are exactly L055's, and the t=1 tails are exactly L064's
j=23 case. Uniqueness identifies their cyclic roots. For each of these
two tuples, direct incoming exponent sums reconstruct all 25 imported
J-margin lower bounds and compare them with independent unrounded
log bounds. All 50 are positive, with minimum
201213805477/500000000 in each tuple. They certify only the already
known benchmark survivors; no arbitrary-table passing parameter follows.

The full certificate is
`scripts/postspell-word-count/variable-table-last-pair-audit-certificate.json`:
243 checks pass with no failures. Complete original comparison operands,
prefix records, boundary rows and exponential terms, and the full selected
audit summary were inspected. Exact analytic terms and errors, survivor
operands, exponent sums and original hashes are saved in the certificate.
The finite evidence supplements the quantified proof, not conversely.
Original certificates, both rational witnesses and Attempts 026–031
remain unchanged. No mathematical dependency or assembled argument has
changed, so PROOF.md and DAG.md are unchanged. Order/support assembly,
new-table survivor integer exclusion and universal eventual descent
remain unresolved. Full matching Mathlib coverage remains unchecked.

## Mathlib

Full matching Mathlib coverage for this variable-table sufficient cutoff
has **not been checked**. Supporting affine, rational, exponential and
logarithm facts would not constitute a matching theorem. The formal
affine identity has the precise primary citation above; benchmark bounds
and analytic coverage are reused with their positive-real hypotheses.
No absence from Mathlib or formal verification is claimed.
