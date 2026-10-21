# L053 — Twenty-four-word simultaneous real-height infeasibility

## Hypotheses

Use exactly L051 (1)–(4) at r=24. Explicitly, indices are modulo 24,
J_i>=2, H_i>=3 and a_i>=0 are integers with a_i congruent to 2 modulo 18.
Set K=sum_i(3J_i+H_i), L=sum_i(J_i+a_i), N=K+L. Positive integers
d,K_0,L_0 satisfy K=dK_0, L=dL_0 and K_0>225640000. Require

\[
\Lambda=N\log2-K\log3>0,\qquad
N<\frac85K+\frac{1656}{1034}.                       \tag{1}
\]

Let s_i>=540/11 be real, h_i=log s_i, s_0=min_i s_i and s_24=s_0.
Require the unchanged seed and every own-index guard

\[
0<h_0<\frac{133}{10}\log N+8+\log24,               \tag{2}
\]
\[
4J_i\log2\le h_i+\log(11/4),\qquad
H_i\log2<h_i+J_i\log(27/16),                       \tag{3}
\]
and, writing G_i=(27/16)^{J_i}(3/2)^{H_i}, all exact endpoints
\[
s_{i+1}=2^{-a_i}\left(G_i s_i-\frac{12}{11}(3/2)^{H_i}-1\right)
                      +\frac{23}{11}.              \tag{4}
\]

All logarithms are natural. Independent tails, repeated occurrences and
coincident junctions remain permitted. Real junctions are not assumed to
realize integer parities, valuations or residues. In particular, none of
L051's failed sufficient-test guards is imposed.

## Conclusion

This simultaneous system has no solution. For actual closed words under
L041's hypotheses, this extends the restricted postspell cycle exclusion
through twenty-four words, with the inherited published qualifications.
The final alternatives force either K=343857546 and K<298760000, or

\[
K\le224363706<225640000<K_0\le K.                    \tag{5}
\]

This is local REPRODUCTION under prior SPECIALIZE coverage, not a claim
of originality beyond the inspected sources. The separate critical audit
below found no defect under the written hypotheses and inherited
qualifications. This is not a complete Collatz candidate: entry, unrestricted
cycles, divergence and universal eventual descent remain unresolved.
The stopped weaker tests in L049 and L051 are unchanged.

## Proof

### Coarse bounds from the existing per-occurrence estimates

Put ell=log2, c=log(11/4), alpha=log(27/16), beta=log(3/2),
rho=189/100 and R_m=sum_{j=0}^{m-1}rho^j. The own-index proof in
L052, before its count-specific assembly, gives

\[
3J_i+H_i<\frac{14}{5}(h_i+1),\qquad
h_{i+1}+1<\rho(h_i+1).                              \tag{6}
\]

Its proof uses exactly (3), (4), s_i>=540/11 and a_i>=2, all unchanged
here; it does not require twenty-three occurrences or integer heights.
Thus its per-occurrence estimates apply to all 24 indices. Induction
along indices 0,...,22 and summation give

\[
K<\frac{14}{5}R_{24}(h_0+1),\qquad
R_{24}<4850000,\quad R_{23}<2570000.                 \tag{7}
\]

The geometric comparisons are exact rational inequalities. The induction
at input zero is equality; strictness of the odd-count estimates supplies
the strict outer sign. All outgoing inputs are counted, even with ties.

The exponential series gives e>163/60>27/10, and (27/10)^4>24, so
log24<4. Since N>=13*24>1, inserting (7) and (2) in (1), using
positive multipliers, proves

\[
N<A\log N+B,\qquad A=288982400,\quad B=282464002.    \tag{8}
\]

Here A=(8/5)(14/5)4850000(133/10),
B=(8/5)(14/5)4850000*13+2, and 1656/1034<2. Let M=6900000000.
The rational logarithm certificate below gives log M<227/10. On the
whole real ray t>=M, F(t)=t-A log t-B has derivative 1-A/t>0, and

\[
F(M)>M-(227/10)A-B=57635518>0.
\]

Equation (8) therefore forces N<M. Also log3/log2>3/2, because
3^2>2^3, so Lambda>0 implies K<2N/3<4600000000. This improves the
K ceiling used in integer separation without imposing any tail cap.

Keep exactly the earlier pair p=9809721694, q=6189245291. Exact
logarithm bounds certify

\[
0<\epsilon=q\log3-p\log2<958/10^{13},\qquad
\ell>6931/10000.                                    \tag{9}
\]

Since N/K>log3/log2>p/q, z=Nq-Kp is a positive integer. Hence

\[
q\Lambda=\ell z-K\epsilon>
6931/10000-4600000000(958/10^{13})
=12621/50000>1/4.                                   \tag{10}
\]

This uses the unchanged pair, not the failed half-log test of L051.

As in L051's exact product argument, put n_i=s_i-23/11>=47 and
eta_i=23/11-(12/11)(16/27)^{J_i}-(16/27)^{J_i}(2/3)^{H_i}.
Each eta_i is strictly between 0 and 23/11. Equation (4) is exactly
n_{i+1}=G_i 2^{-a_i}(n_i+eta_i). Multiplication of all 24 equations,
including closure, cancels the positive product of the n_i, giving

\[
\Lambda=\sum_{i=0}^{23}\log(1+\eta_i/n_i)
 <\frac{23}{11}\sum_{i=0}^{23}\frac1{n_i}
 \le\frac{552}{11n_0}.                              \tag{11}
\]

The powers in the product are exactly 3^K/2^N; no term or closing
tail is omitted. Equations (10)–(11) imply
s_0<(2208q+23)/11<(163/60)^28<e^28, hence h_0<28. Consequently

\[
225640000<K<393820000<394000000<q.                   \tag{12}
\]

The lower bound is primitive scaling; the upper bound is (7).
Also (7) would give K<217280000 if h_0<=15. Therefore h_i>=h_0>15
for every i. No designated junction is identified with the global
minimum of an actual orbit.

### At most one small junction

Suppose h_j<=30 for some j in {1,...,23}. We already have h_0<28<30.
Apply (6) separately along the segment starting at zero with j inputs
and the segment starting at j with 24-j inputs. They partition all 24
input occurrences. Thus

\[
K<\frac{14}{5}\,31(R_j+R_{24-j}).
\]

For 1<=j<=23, R_j+R_{24-j}<=1+R_{23}. Indeed
(rho^{j-1}-1)(rho^{23-j}-1)>=0 gives
rho^j+rho^{24-j}<=rho+rho^{23}, and division of the corresponding
geometric expressions by rho-1>0 proves the claim. By (7),

\[
K<\frac{14}{5}\,31(2570001)
=223076086.8<225640000,
\]

a contradiction. Hence h_i>30 for all i=1,...,23, even if heights
otherwise coincide. This is a consequence, not an assumption of distinct
junctions. Using e>27/10, the exact comparison

\[
\frac{529/11}{(27/10)^{30}-23/11}<10^{-11}
\]

sharpens (11) to

\[
\Lambda<\frac{23/11}{s_0-23/11}+10^{-11}.           \tag{13}
\]

### The integer count alternatives from the same pair

The integer identity

\[
630138897q-397573379p=1
\]

shows that, for u=397573379, K congruent to uz modulo q: modulo q,
z=-Kp and -up=1. Because 0<K<q, K must be the least nonnegative
residue of uz (and cannot be zero). This is a Bezout identity of the
fixed pair, not another rational approximation or optimized pair.

For 1<=z<=62 the quotient floor(uz/q) has the following values.
Within each range the residue increases by u at every step:

| z range | quotient | first residue | second residue |
|---|---:|---:|---:|
|1–15|0|397573379|795146758|
|16–31|1|171928773|569502152|
|32–46|2|343857546|741430925|
|47–62|3|118212940|515786319|

The range endpoints follow by integer multiplication; all 62 residues
are also stored in the certificate. In the interval (225640000,394000000),
only z=32 with K=343857546 survives. Thus either this explicit case
holds, or z>=63.

For an integer b>0 define the rational numbers

\[
\lambda_b=\frac{b(6931/10000)-394000000(958/10^{13})}{q},
\quad D_b=\frac{23}{11}+\frac{23/11}{\lambda_b-10^{-11}}.
\]

For b=32 and b=63, the denominators are positive. If z>=b, (9),
(12) and qLambda=ell z-Kepsilon imply Lambda>lambda_b. Equation
(13) then implies s_0<D_b. The exact logarithm certificate gives

\[
\log D_{32}<21,\qquad \log D_{63}<98/5.             \tag{14}
\]

In the case z=32, (7) and (14) force
K<(14/5)4850000*22=298760000<343857546, contradicting its fixed K.
It remains to exclude z>=63, for which h_0<98/5.

### Integer own-index propagation for z>=63

The lower height h_i>15 already proved implies
s_i>e^15>(27/10)^15>10^6. Since a_i>=2 and G_i>1, (4) gives

\[
s_{i+1}<G_i s_i/4+23/11.
\]

Taking logarithms and using log(1+x)<x for x>0,

\[
h_{i+1}<h_i+J_i\alpha+H_i\beta-2\ell
            +\frac{92}{11G_i s_i}
 <h_i+J_i\alpha+H_i\beta-2\ell+10^{-5},             \tag{15}
\]

because 92/(11*10^6)<10^-5. Both negative endpoint terms have only
been dropped in a valid upper bound. The -2ell contribution is kept;
no final-tail cap, assumed monotonicity or actual parity is used.

Here is a fully rational upper recurrence. Set S=10^12 and

\[
E=693147180559,\quad T=1098612288669,\quad C=1011600911679.
\]

The certificate establishes E/S<ell, log3<T/S and c<C/S. Put
a=3T-4E=523248143771, b=T-E=405465108110. These give positive
upper bounds alpha<a/S and beta<b/S. Start v_0=19600000000000
and, for i=0,...,23, define entirely by integer arithmetic

\[
\widehat J_i=\left\lfloor\frac{v_i+C}{4E}\right\rfloor,
\quad
\widehat H_i=\left\lfloor\frac{v_i+\widehat J_i a}{E}\right\rfloor,
\quad
v_{i+1}=v_i+\widehat J_i a+\widehat H_i b-2E+10^7.    \tag{16}
\]

We prove h_i<v_i/S, J_i<=Jhat_i and H_i<=Hhat_i by induction.
The height statement at zero is (14). If h_i<v_i/S, the first guard
in (3), E/S<ell and c<C/S imply J_i<(v_i+C)/(4E); since J_i is
integer, it is at most that floor. Positivity of alpha and the second
guard then give H_i<(v_i+Jhat_i a)/E, hence its floor bound. Every
replacement has the correct sign, and (15) with -2ell<-2E/S gives
h_{i+1}<v_{i+1}/S. All numerators used are positive (as also follows
from the positive actual quantities they bound). A possibly integral
floor argument merely weakens the valid upper bound.

The exact recurrence yields these 24 pairs:

|i|Jhat_i|Hhat_i|i|Jhat_i|Hhat_i|
|---:|---:|---:|---:|---:|---:|
|0|7|33|12|12785|60791|
|1|13|60|13|24087|114532|
|2|23|111|14|45382|215785|
|3|43|206|15|85502|406554|
|4|81|386|16|161093|765978|
|5|152|724|17|303511|1443161|
|6|286|1362|18|571838|2719027|
|7|539|2563|19|1077389|5122862|
|8|1015|4827|20|2029885|9651877|
|9|1912|9092|21|3824465|18184902|
|10|3602|17127|22|7205596|34261800|
|11|6786|32267|23|13575916|64551955|

Therefore K=sum_i(3J_i+H_i)<=sum_i(3Jhat_i+Hhat_i)=224363706,
contradicting K>225640000 with margin 1276294. Only 23 forward
transitions are needed to bound the 24 inputs; the generated 24th upper
transition is harmless and is not used as an independent closing
condition. All 24 exact endpoints were essential earlier in (11).

### Exact certificate, known inputs and qualifications

Reproduce with `python3 scripts/postspell-word-count/certify_twenty_four_heights.py`.
Full evidence is `scripts/postspell-word-count/twenty-four-height-certificate.json`.
All 29 strict rational checks pass; the modular identity, all 62 residues,
all 24 floor inequalities and the final sum are also checked exactly.
Every recurrence numerator and exact floor argument is saved. The complete
compact sign/floor tables and residue list were inspected, including the
full small epsilon margin where decimal rounding alone was inconclusive.
This certificate is not an independent critical audit.

For the logarithms, binary-reduce t>=1 to t=2^k v with 1<=v<2,
k>=0, and x=(v-1)/(v+1). For log2 use x=1/3. The integrated
finite geometric identity gives

\[
\log v=2\sum_{j=0}^{95}\frac{x^{2j+1}}{2j+1}
       +2\int_0^x\frac{u^{192}}{1-u^2}\,du.
\]

The nonnegative remainder is strictly below 9/(4*193*3^193), by
bounding 1/(1-u^2) by its endpoint value and x<=1/3. Strictness at
x>0 comes from the integral; at zero the remainder is zero. Round each
summand down to a multiple of 2^-192. The total rounding loss is less
than 96*2^-192. The rounded sum and that sum plus both error budgets
therefore enclose log v; adding k outward log2 intervals encloses log t.
This is the already justified L051 procedure. All binary reductions,
rounded summands and complete enclosures are retained. Epsilon uses
opposite endpoints for the subtracted term, so the large cancellation
is rigorous. No floating-point value enters the certificate or proof.
The earlier decimal trial files are exploratory, unused evidence.

The assessment saved before invocation is
`drafts/literature/2026-10-10-twenty-four-simultaneous-feasibility.md`.
Its primary-source coverage is reused. L041's all-r actual-word bridge
supplies (1)–(4): its own-word identities give (3)–(4), its reciprocal
mass and lower linear-form comparison give (1)–(2), and primitive
reduction preserves K=dK_0,L=dL_0. Positive odd residue-20 junctions
are at least 47 and make the primitive cycle nontrivial. These conditions
hold occurrence by occurrence with independent exact tails and repeats.

The precise inherited sources are Christian Hercher, *There are no
Collatz m-Cycles with m <= 91*, JIS 26 (2023), Article 23.3.5,
[Theorem 16 and proof, pp. 10–11](https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/hercher5.pdf),
and John Simons and Benne de Weger, *Theoretical and computational bounds
for m-cycles of the 3n+1-problem*, Acta Arith. 117 (2005), 51–70,
[Corollary 2 p. 53, Lemma 12 p. 61, period conventions p. 52](https://www.impan.pl/shop/en/publication/transaction/download/product/82263).
Corollary 2 supplies K_0>225640000 for the primitive integer cycle;
the other inputs support L041's seed and length conversion. They are not
asserted as theorems about arbitrary real junctions. No full local-minimum
count is set equal to 24. Their general proofs are not repeated here;
the changed finite count, cyclic splitting and integer guards require
the explicit specialization above. No general parity-coding theorem is
needed, since no real-system witness is claimed.

The published height 301*2^50, distributed computation, Roosendaal
communication, continued-fraction and Rhin/Crandall inputs remain qualified
imports; original certificates and external Lean builds are not independently
verified. The inspected Hercher correction leaves Theorem 16 unchanged;
Theorem 21 is unused. The arithmetic pair is unchanged and its integer
inverse is verified directly, with no stronger published threshold.

### Separate critical audit — 2026-10-11

Prior SPECIALIZE coverage:
`drafts/literature/2026-10-10-twenty-four-infeasibility-audit.md`.
Verdict: **no defect found within the written hypotheses and inherited
published qualifications**. This is REPRODUCTION verification of the
existing exclusion, not a new exclusion, proof repair or originality claim.
The proof, generator and complete relevant certificate operands were
checked independently. Ready primary-source coverage was reused.

The local estimates in L052 apply without its count-specific assembly.
With delta=log3/ell, substituting only this occurrence's first guard in
its second gives
3J_i+H_i<[3(delta+1)/(4ell)]h_i+[(3delta-1)c/(4ell)].
The positive coefficients are below 14/5 and 7/5. Dropping negative
endpoint terms gives s_(i+1)<G_i s_i/4+23/11<G_i s_i, since
(3/4)G_i s_i>=405/11>23/11. Substituting the same own-index guards
in h_(i+1)<h_i+J_i alpha+H_i beta gives coefficient 3delta^2/4
and additive term delta(3delta-4)c/4, respectively below 189/100
and 31/100. Both are checked with exact logarithm enclosures. Adding
1 therefore proves (6) on this real domain. The 23 forward edges
bound all 24 inputs, with equality allowed at the initial induction
step. All count and seed multipliers are positive. Exact A,B and
F(M)>57635518, together with F'>0 on the whole real ray t>=M,
prove N<M; testing M alone would not suffice. Lambda>0 and 3^2>2^3
give the needed K<2N/3 before integer separation.

The audit checks the unchanged positive residual and the sign in
qLambda=ell z-K epsilon. Integer K,N and epsilon>0 give z>=1.
The quarter-log lower margin is exactly 12621/50000>1/4. For every
endpoint, subtracting 23/11 yields precisely the eta_i in (11);
0<eta_i<23/11 follows from J_i>=2,H_i>=3. The product contains
all 24 equations, with powers 3^K/2^N. Cancelling positive junction
factors and applying log(1+x)<x therefore proves (11). The resulting
h_0<28 gives K<393820000. If h_0<=15, (7) would instead give
K<217280000, contradicting primitive scaling. Thus the lower real
height used in the later endpoint-error estimate is justified.

For a second height h_j<=30, the two cyclic segments have j and
24-j inputs and cover each occurrence once. Each starts with height
plus 1 at most 31; the strict odd-count bound makes their sum strict.
The nonnegative product (rho^(j-1)-1)(rho^(23-j)-1) proves the stated
geometric extremum, including equality at j=1 or 23. All 23 split
values are also checked exactly. The resulting upper count is below
225640000, so no second low height, tie or repeated minimum survives.
The positive denominator in the remaining reciprocal bound is checked;
it gives precisely the 23-term error below 10^-11 in (13).

The Bezout identity and all 62 complete residues are independently
verified by integer division, including every quotient range endpoint.
The range 0<K<394000000<q identifies K with the least nonnegative
residue; its positivity rules out residue zero. The only permitted
case below z=63 is exactly (z,K)=(32,343857546). No residue case or
real-system realization is assumed away. Each lambda_b-10^-11 is
positive before inversion, so (13) gives s_0<D_b with the correct
inequality direction. Independent exact logs verify both (14) caps.
The z=32 bound K<298760000 then contradicts its exact residue.

For z>=63, h_0<98/5 supplies the induction base. Every height is
greater than 15, so e^15>(27/10)^15>10^6. Dropping the two negative
endpoint terms yields (15); log(1+x)<x and G_i>1 bound its positive
shift error by 92/(11*10^6)<10^-5. The negative term -2ell is retained
and replaced by -2E/S in the correct upper-bound direction. Each floor
argument strictly exceeds the respective actual integer parameter;
using its floor is valid even when that argument happens to be integral.
All replacements use positive alpha,beta and positive numerators.
Independent division checks every complete row and both floor remainders.
At index 18 the J remainder is 2772275919726 out of 2772588722236,
only 312802510 below the next integer boundary. Its H remainder is
623544922820 out of 693147180559. The complete printed 24-pair table
agrees with the arithmetic recurrence. Their count sum is 224363706,
with strict-threshold margin 1276294. The final generated transition
is checked for consistency but is unused as a closing condition.

The audit checks all 672 stored rounded summands (the base log2 and
six reduced arguments), their binary reductions, rounding budgets,
remainder bounds and complete enclosures. Independently, 144 unrounded
terms are evaluated by Horner's rule, with argument-specific remainder
2x^289/[289(1-x^2)]. This is nonnegative and follows from the same
integrated geometric identity; at x=0 it is exactly zero. Normalization
uses increasing integer powers rather than the generator's repeated
halving. Every independent interval lies inside its stored enclosure.
The delicate residual is also checked as (q-p)log2+qlog(3/2), reversing
log2 endpoints because q-p<0. All 29 saved comparisons, their full
operands and margins, and all corresponding independent signs pass.
All stored inspection intervals are verified but are not proof inputs.

Reproduce with
`python3 scripts/postspell-word-count/audit_twenty_four_heights.py`.
All **1165 audit checks pass**, with no failures. Full operands, exact
rounding evidence, independent intervals, residues, splits and floor
remainders are in
`scripts/postspell-word-count/twenty-four-height-audit-certificate.json`.
The original certificate regenerates byte for byte in a temporary
directory, SHA-256
`618cd46f5cc2491109897ec041877b01c636d47017ff5729268fa3339ad5d5ee`.
Regeneration is an additional consistency check, not the independent
arithmetic argument.

For actual words, the relevant L041 proof verifies each exact endpoint
and own-index guard from that word's actual valuations, occurrence
partition and represented K,N. The length remainder follows from its
represented reciprocal-mass bound and log2>2/3; its log r seed follows
from that bound and the precisely cited lower linear form. Relabeling
selects only the least designated junction. Positive odd residue-20
junctions are at least 47 and make the primitive cycle nontrivial.
Primitive-period reduction preserves K=dK_0,L=dL_0 even with repeats;
the cited Corollary 2 supplies K_0>225640000. Ties and independent
tails remain admitted. Neither source is applied directly to arbitrary
real junctions; the full local-minimum count is never replaced by 24.
Original computation/transcendence certificates, external Lean builds
and matching Mathlib remain unchecked as already qualified above.

No argument or direct dependency changed. PROOF.md and DAG.md remain
unchanged; this canonical audit supersedes their pending L053 wording.
The earlier stopped scalar and sufficient tests remain valid. Universal
entry, unrestricted cycles, divergence and eventual descent remain open.

## Mathlib

Full matching coverage is not checked. Supporting mathematics consists
of real logarithms, finite products, geometric sums, monotonicity, modular
arithmetic, integer floors and rational interval arithmetic. No matching
Lean declaration or formal verification of the whole result is asserted.
Unknown availability is not evidence of absence.
