# L051 — Fixed-pair cyclic-product word-count range

## Hypotheses

All logarithms are natural. Let r>=3 be an integer, with indices modulo r.
Let J_i>=2, H_i>=3 and a_i>=0 be integers, a_i congruent to 2 modulo 18.
Define P_i=4J_i+H_i, K=sum_i(3J_i+H_i), L=sum_i(J_i+a_i), N=K+L.
Let d,K_0,L_0 be positive integers, K=dK_0, L=dL_0 and K_0>225640000.
Assume

\[
\Lambda=N\log2-K\log3>0,\qquad
N<\frac85K+\frac{69r}{1034}.                         \tag{1}
\]

Let s_i>=540/11 be real, h_i=log s_i, s_0=min_i s_i, s_r=s_0.
Require the unchanged seed and every occurrence's own guards

\[
0<h_0<\frac{133}{10}\log N+8+\log r,                 \tag{2}
\]
\[
4J_i\log2\le h_i+\log(11/4),\qquad
H_i\log2<h_i+J_i\log(27/16).                         \tag{3}
\]

For G_i=(27/16)^{J_i}(3/2)^{H_i}, require all exact endpoints

\[
s_{i+1}=2^{-a_i}\left(G_i s_i-\frac{12}{11}(3/2)^{H_i}-1\right)
                  +\frac{23}{11}.                   \tag{4}
\]

This is L050's necessary-condition real-height subsystem at general r,
with exactly the count-dependent constants displayed. No integer parity,
valuation or residue realization of the real junctions is assumed.
Independent tails, repeated periods and coincident junctions are retained.

Fix rho=48/25, p=9809721694, q=6189245291, ell=log2 and
epsilon=q log3-p log2. Define

\[
R_r=\sum_{j=0}^{r-1}\rho^j,\quad A_r=\frac{399}{5}R_r,
\quad B_r=(54+6\log r)R_r+\frac{69r}{1034},
\]
\[
F_r(t)=t-A_r\log t-B_r,\quad
D_r=\frac{69rq+23}{11},\quad T_r=\frac{15}{4}R_r(1+\log D_r).
\]

The specified sufficient test selects the least integer M>A_r with
F_r(M)>0, then requires 2M epsilon<ell and T_r<=225640000.
An equality fails either strict ceiling test or the strict half-log guard.
No approximation, transfer, offset or seed optimization is part of this test.

## Conclusion

The sufficient test succeeds for every integer 3<=r<=22 and first fails
at r=23. Every system (1)–(4) with 3<=r<=22 is consequently infeasible.
In particular, actual closed concatenations under L041's hypotheses at
those word counts are excluded, subject to the published qualifications
below. The new restricted exclusions are r=21 and r=22.

At r=22 the least ceiling is M=3386647505 and T_r<198293520<225640000.
At r=23 it is M=6697335032; the half-log guard fails and
T_r>381318038>225640000. No larger integer ceiling at that count can
restore the guard. This is maximality only of the specified initial
sufficient-test range, not of all uses of the fixed pair or endpoints.
No simultaneous feasibility, integer orbit or actual cycle is asserted
at the first failure. The separate critical audit below found no defect
within these hypotheses and inherited qualifications.

This is local REPRODUCTION within prior SPECIALIZE coverage, not a claim
of originality beyond inspected sources. Entry, unrestricted cycles,
divergence and universal eventual descent remain unresolved.

## Proof

### Variable-count substitutions

L046's per-occurrence real-domain argument uses only (3), (4), a_i>=2
and s_i>=540/11, all unchanged here. Its audited numerical conclusions
are h_{i+1}+1<rho(h_i+1) and P_i<(15/4)h_i+3. We import these
per-occurrence estimates, not its eighteen-word infeasibility conclusion.
Along the r-1 edges from 0 through r-2, induction gives
h_j+1<=rho^j(h_0+1) for 0<=j<r, allowing equality at j=0. Thus

\[
K=\sum_i(P_i-J_i)<\frac{15}{4}\sum_i(h_i+1)
 \le\frac{15}{4}R_r(h_0+1).                          \tag{5}
\]

Multiplying (5) by 8/5 and inserting (1), (2) gives

\[
N<A_r\log N+B_r.                                    \tag{6}
\]

Indeed (8/5)(15/4)=6, 6(133/10)=399/5 and 6(8+1)=54.
Every substitution has a positive multiplier, and N>=13r>1. All tails
remain in N through (1); no tail upper bound is imposed.

For fixed r, A_r>1 and B_r>0. On the entire real ray t>A_r,
F_r'(t)=1-A_r/t>0. Also F_r(t) tends to infinity as t tends to
infinity, so integers M>A_r with F_r(M)>0 exist and have a least
member. If such an M is selected, (6) implies N<M: otherwise
F_r(N)>=F_r(M)>0 contradicts (6). In particular 0<K<N<M.

L050 certifies epsilon>0 for this exact pair; the certificate below
also recomputes it. Suppose the selected M satisfies 2M epsilon<ell.
Since Lambda>0, N/K>log3/log2>p/q. Therefore z=Nq-Kp is a positive
integer and z>=1, irrespective of whether the junctions are integers.
Exactly as in L050,

\[
q\Lambda=\ell z-K\epsilon>\ell-M\epsilon
 >\ell/2>1/3,\qquad \Lambda>1/(3q).                  \tag{7}
\]

The final strict inequality uses ell>2/3. This is derived from integer
total counts and the ceiling, not an additional relaxation hypothesis.

Set n_i=s_i-23/11>=47 and

\[
\eta_i=\frac{23}{11}-\frac{12}{11}(16/27)^{J_i}
                         -(16/27)^{J_i}(2/3)^{H_i}.
\]

The two subtracted positive terms have sum strictly below 12/11+1,
so 0<eta_i<23/11. Subtracting 23/11 from (4) gives the exact equation
n_{i+1}=G_i 2^{-a_i}(n_i+eta_i). Multiplying all r equations, including
the closing equation, cancels prod n_i and gives

\[
\Lambda=\sum_{i=0}^{r-1}\log(1+\eta_i/n_i)
 <\frac{23r}{11n_0}.                                \tag{8}
\]

Here log prod(G_i/2^{a_i})=K log3-N log2=-Lambda, and n_i>=n_0.
All factors are positive; ties and repeated time occurrences cause no
change to cancellation or summation. Combining (7), (8) yields
n_0<69rq/11, hence s_0<D_r and h_0<log D_r. Inserting this in (5)
proves K<T_r. If T_r<=225640000, then

\[
K<T_r\le225640000<K_0\le K,
\]

a contradiction. This also explains the intentional non-strict test
on T_r. We do not replace the half-log guard by a bound optimized in K.

### Exact initial range and first failure

For each r=3,...,23 the certificate proves M>A_r, F_r(M)>0 and
M-1>A_r with F_r(M-1)<0. Strict monotonicity on t>A_r therefore
certifies the least integer ceiling. Integers at or below A_r cannot
pass its first condition. The least ceilings are:

| r | M | r | M | r | M |
|---|---:|---|---:|---|---:|
|3|4878|10|855531|17|110231529|
|4|11017|11|1723967|18|219188637|
|5|23657|12|3464527|19|435294295|
|6|49490|13|6946364|20|863456373|
|7|102015|14|13899373|21|1710903708|
|8|208393|15|27762044|22|3386647505|
|9|423153|16|55360636|23|6697335032|

For every r=3,...,22 the exact certificate also verifies
ell-2M epsilon>0 and 225640000-T_r>0. Each count is checked;
no monotonicity in r or floating-point inference fills a missing count.
At r=22 certified outward bounds give

\[
F_{22}(M)>0.542833173111,\quad
F_{22}(M-1)<-0.413407377843,
\]
\[
\ell-2M\epsilon>0.044804922744,\qquad T_{22}<198293520.
\]

At r=23 they give

\[
F_{23}(M)>0.708478495879,\quad
F_{23}(M-1)<-0.249035961741,
\]
\[
\ell-2M\epsilon<-0.588995501718,\qquad T_{23}>381318038.
\]

All displayed decimals denote exact rationals. As epsilon>0, increasing
M decreases ell-2M epsilon. Every ceiling passing the first two tests
is at least the certified least M, so none can pass the third test at
r=23. Independently, its T_r threshold fails. The search stops there.
This failure establishes only a sufficient-method limitation, not a
solution of (1)–(4), even over reals, nor a cycle counterexample.

### Exact arithmetic certificate and its remainder justification

The generator uses integer/Fraction arithmetic exclusively. For t>=1
write t=2^k v with integer k>=0 and 1<=v<2, and put x=(v-1)/(v+1),
so 0<=x<1/3. For log2 use x=1/3 directly. The finite geometric
identity integrated in 2/(1-x^2) gives

\[
\log v=2\sum_{j=0}^{m-1}\frac{x^{2j+1}}{2j+1}
       +2\int_0^x\frac{u^{2m}}{1-u^2}\,du.
\]

For m=96 the remainder is nonnegative and strictly less than
E=9/[4(2m+1)3^{2m+1}]. This follows from the bound
2x^{2m+1}/[(2m+1)(1-x^2)]<=E; at x>0 the integral inequality
is strict, while x=0 gives zero<E. With S=2^192, round each of the
m rational summands down to a multiple of 1/S. Their rounded sum b
satisfies b<=log v<b+m/S+E. Hence b+k ell_lower and
b+m/S+E+k ell_upper rigorously enclose log t. Lower endpoints may be
non-strict; every tested sign has a strictly positive rational margin.

The full certificate stores reduced arguments, exponents, rounded partial
integers, rounding budgets, remainder bound, complete log enclosures and
every row's exact R,A,B,F,guard,D,T operands. For epsilon its bounds are
q(log3)_lower-p ell_upper and q(log3)_upper-p ell_lower.
For F(M), the lower bound uses upper log M and B, while its upper
bound uses their lower bounds; the same sign choices apply at M-1.
The guard lower/upper bounds use respectively ell_lower/upper and
epsilon_upper/lower. T uses the corresponding log D bounds. Thus all
large cancellation is handled by outward rational bounds.

Binary search finds each ceiling on t>A_r; doubling terminates by
F_r(t) tending to infinity. An interval containing zero raises an error,
never a failed-predicate conclusion. The final proof of minimality uses
the two certified neighboring integers, not the binary search itself.
Every sign margin is rounded down to a multiple of 10^-12 for compact
inspection; all 107 such checks are positive, with no check failures.
The two mathematically false predicates at r=23 are recorded as certified
failure conclusions, not omitted or labeled successful exclusions.

Reproduce with
`python3 scripts/postspell-word-count/certify_fixed_pair_range.py`.
Full evidence is `scripts/postspell-word-count/fixed-pair-range-certificate.json`.
The complete sign-check list, log2/log3 and residual enclosures, and full
r=22/r=23 rows were inspected. The analytic proof above remains essential;
this finite rational certificate is not an independent critical audit.

### Actual-word bridge, source qualifications and comparison

L041's all-r proof supplies (1)–(4) for every actual closed concatenation
under its hypotheses. Its seed selects the smallest designated junction,
not the global cycle minimum. Each own-index guard and shifted endpoint
uses that occurrence's actual word. Exact independent tails give a_i>=2;
positive odd residue-20 junctions are at least 47. Primitive reduction
gives K=dK_0,L=dL_0 with d>=1, retaining all time occurrences and ties.
The primitive cycle is nontrivial because it contains a junction >=47.

The precise inherited primary inputs are Christian Hercher,
*There are no Collatz m-Cycles with m <= 91*, JIS 26 (2023), Article
23.3.5, [Theorem 16 and full proof, pp. 10–11](https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/hercher5.pdf),
and John Simons and Benne de Weger, *Theoretical and computational bounds
for m-cycles of the 3n+1-problem*, Acta Arithmetica 117 (2005), 51–70,
[Corollary 2 and proof p. 53, Lemma 12 and proof p. 61, period conventions p. 52](https://www.impan.pl/shop/en/publication/transaction/download/product/82263).
Corollary 2 gives K_0>225640000 for the primitive integer cycle;
Hercher and Lemma 12 supply L041's seed and length conversion. These
are imposed necessary conditions in the real relaxation, not source
theorems about arbitrary real cycles. The full local-minimum count is
never set to r. The published height 301*2^50, distributed [Ro]
computations, Roosendaal communication, continued-fraction denominators
225644606 and 397573379, and Rhin/Crandall originals retain their
imported qualifications; original certificates and external Lean builds
are not independently verified. The inspected Hercher correction leaves
Theorem 16 unchanged, and amended Theorem 21 is unused.

The unchanged prior assessment is
`drafts/literature/2026-10-10-fixed-pair-cyclic-product-range.md`.
Known rational parity coding and global-minimum theorems there do not
supply this designated-junction fixed-test range. No such theorem is
reproved or imported as a stronger bound here. Repeating L050's product
algebra is necessary to justify its changed count and exact constants.
L049 and Attempts 019/021–023 remain valid for their weaker systems;
their scalar survivors do not meet an asserted full closing system.
This test is now stopped at its first failure, with no conclusion about
larger counts, optimal rational pairs or universal eventual descent.

### Separate critical audit — 2026-10-10

The prior SPECIALIZE assessment was
`drafts/literature/2026-10-10-fixed-pair-range-critical-audit.md`.
Verdict: **no defect found within the written hypotheses and imported
qualifications**. This is a REPRODUCTION audit, not a new exclusion,
mathematical repair or originality claim. The full L051 proof and generator,
L041's relevant actual-word argument and L046's real-domain estimates were
checked against L050's separate audit. The ready primary-source assessments
were reused; the cited computations and transcendence inputs were not
independently recertified.

The own-index substitutions apply on the real domain: a_i>=2 and the
negative endpoint terms give s_(i+1)<G_i s_i/4+23/11<G_i s_i, using
s_i>=540/11. With delta=log3/log2, the positive multipliers delta-1,
delta and 3delta-4 permit substitution of that same occurrence's J,H
bounds, giving h_(i+1)<(3delta^2/4)h_i+
[delta(3delta-4)/4]log(11/4)<(48/25)h_i+32/75.
Thus the shift by 1 is valid since 107/75<48/25. The prefix estimate
P_i<(15/4)h_i+3 uses those same guards. It assumes no integer valuation
of a real height. The r-1 outgoing edges with indices 0,...,r-2 cover
exactly the r input heights. Their sum gives (5), since J_i>=2 and
3<15/4. Multiplication by 8/5 and the seed give precisely A_r and B_r,
including 6log r and 69r/1034. No closing tail is dropped from N.

For fixed r, A_r>1, B_r>0 and F_r is strictly increasing on t>A_r,
with limit infinity. The certificate checks M-1>A_r, F_r(M-1)<0 and
F_r(M)>0 for every r=3,...,23. This proves each displayed M is the
least eligible integer; it also proves N<M on the whole real ray,
not merely at sampled integers. Values at or below A_r are ineligible.
The analytic argument allows any eligible ceiling, but the first-failure
comparison correctly uses the least one.

The residual is positive. Since Lambda>0 and K>0, N/K>log3/log2>p/q,
so z=Nq-Kp is an integer at least one. No coprimality or integrality
of the junctions is required. The minus sign in qLambda=(log2)z-K epsilon
is correct. With K<N<M and 2M epsilon<log2 it gives qLambda>log2/2>1/3.

Subtracting 23/11 from every exact endpoint gives the stated eta_i:
the two positive subtractions sum to less than 12/11+1=23/11, so
0<eta_i<23/11. All n_i=s_i-23/11>=47 are positive and n_i>=n_0.
The product uses all r equations, including the closing one. Its powers
are 3^K/2^N; cancellation of the r positive junction factors therefore
gives exactly Lambda=sum log(1+eta_i/n_i), with no lost offset.
The strict log(1+x)<x estimate yields (8). Combined with integer
separation it gives n_0<69rq/11 and s_0<D_r, hence K<T_r via (5).
The test T_r<=225640000 is intentionally non-strict: its equality would
still contradict K<T_r and K>=K_0>225640000. Neither equality in
F_r(M)>0 nor in the half-log guard suffices for the stated strict tests.
All evaluated thresholds have strict margins, so the generator need not
decide an interval straddling equality; it raises an error in that case.

For the stored log bounds, the integrated geometric remainder is
nonnegative and strictly below E=9/[4*193*3^193]. At x>0 the strictness
comes from replacing 1/(1-u^2) by its endpoint value over an interval of
positive length; at x=0 the remainder is zero<E. Flooring each of the
96 summands loses less than 1/2^192, so the stated 96/2^192 budget
and all binary-reduction enclosures are valid. The audit recomputes each
rounded summand sum, exponent, reduced argument, remainder, budget and
complete enclosure for log2 and all 84 stored arguments.

Independently, the audit evaluates 112 unrounded Horner terms at
x=(v-1)/(v+1), with remainder bounded by
2x^225/[225(1-x^2)]. At x=0 the interval is exact. Binary reduction
is performed by repeated halving, independently of the generator's
bit-length normalization. Every resulting interval is contained in its
stored enclosure. For the delicate residual it additionally uses
(q-p)log2+qlog(3/2); q-p<0 reverses the log2 endpoint choices.
This independently certifies 9/10^11<epsilon<1/10^10. Thus residual
cancellation is checked by exact rational arithmetic, not decimal logs.

For every r=3,...,23 the audit recomputes R_r by the closed form
(48^r-25^r)/(23*25^(r-1)), all complete B,F,D,T and guard operands,
the previous-ceiling data, predicates and saved sign margins. Independent
log enclosures also recheck both neighboring F signs, the guard and T
comparison in every row. All 107 saved rational sign checks match
exactly, including both failure conclusions at r=23. At r=22,
19829351901/100<T_22<19829351902/100<225640000 and the guard is positive.
At r=23, 38131803830/100<T_23<38131803831/100 and the guard is negative.
Every displayed rational bound in the conclusion is separately checked.
Since epsilon>0, every larger eligible ceiling worsens that guard.
This verifies the stated first-failure conclusion, not feasibility at 23.

Reproduce with
`python3 scripts/postspell-word-count/audit_fixed_pair_range.py`.
All **370 audit checks pass**, with no failures. The full exact operands,
independent enclosures and checks are saved in
`scripts/postspell-word-count/fixed-pair-range-audit-certificate.json`.
The original certificate regenerates byte for byte, SHA-256
`d52e14d2d0774b1e425706da292bc41fcf3a4ba989608c94ec734cb59631d59b`.
The original script's finite range is not used as a substitute for the
all-parameter proof or the whole-real-ray monotonicity argument.

For actual words, L041 supplies the unchanged log r seed, length
conversion, each own-index guard and every endpoint. Cyclic relabeling
selects only the smallest designated junction. Positive odd residue-20
junctions are at least 47; their presence makes the primitive orbit
nontrivial. Primitive reduction gives K=dK_0,L=dL_0 with d>=1, and the
precisely cited Simons–de Weger Corollary 2 supplies K_0>225640000.
Repetitions and coincident junctions remain time occurrences. The full
local-minimum count is never set to r. Source qualifications and unknown
matching Mathlib coverage remain as above.

No argument or direct dependency changed; PROOF.md and DAG.md remain
unchanged. This canonical verdict supersedes their pending L051 audit
wording only. L049 and Attempts 019/021–024 retain their stops; neither
scalar survival nor failed sufficient tests imply simultaneous feasibility.
Entry, unrestricted cycles, divergence and universal descent remain open.

## Mathlib

Matching coverage of the full variable-count subsystem or cutoff is not
checked. Elementary logarithm, product, integral-remainder and rational
arithmetic facts support the written proof; no matching Lean declaration
or formal verification is asserted. Unknown availability is not absence.
