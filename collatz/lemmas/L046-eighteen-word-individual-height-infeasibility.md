# L046 — Eighteen-word individual-height infeasibility

## Hypotheses

All logarithms are natural. Indices are modulo 18. Consider integers
J_i>=2, H_i>=3 and a_i>=0 with a_i congruent to 2 modulo 18. Define

\[
P_i=4J_i+H_i,\quad K=\sum_i(3J_i+H_i),\quad
L=\sum_i(J_i+a_i),\quad N=K+L.
\]

Let d,K_0,L_0 be positive integers with K=dK_0, L=dL_0 and
K_0>225640000. Require

\[
\Lambda=N\log2-K\log3>0,\qquad
N<\frac85K+\frac{1242}{1034}.                         \tag{1}
\]

Let s_i>=540/11 be real, h_i=log s_i, s_0=min_i s_i and s_18=s_0.
Require the seed and each occurrence's own parameter bounds

\[
0<h_0<\frac{133}{10}\log N+8+\log18,                 \tag{2}
\]
\[
4J_i\log2\le h_i+\log(11/4),\qquad
H_i\log2<h_i+J_i\log(27/16).                         \tag{3}
\]

For every i put G_i=(27/16)^{J_i}(3/2)^{H_i} and require

\[
s_{i+1}=2^{-a_i}\left(G_i s_i-\frac{12}{11}(3/2)^{H_i}-1\right)
                  +\frac{23}{11}.                   \tag{4}
\]

These are a subsystem of the approved simultaneous relaxation of L045.
Its additional aggregate K,N inequalities, quantitative upper/lower
linear-form bounds and factor-2 transfer may all be imposed too; they
are not needed for the contradiction. The junctions s_i-23/11 are
allowed to be real: integer parity, exact integer valuations and residue
membership are not additional assumptions of this infeasibility result.

## Conclusion

There is no assignment satisfying (1)–(4) and the stated guards. Thus
the full approved eighteen-word simultaneous system is infeasible.
In particular no actual closed eighteen-word postspell concatenation
under L041's hypotheses exists, subject to the published cycle inputs
and computational qualifications specified below.

This extends the restricted cycle exclusion through eighteen when
combined with L045. It does not determine the best possible word-count
cutoff, prove entry into this language, exclude arbitrary cycles or
divergence, or establish universal eventual descent. This local
specialization passed the separate critical audit below within its stated
hypotheses and published qualifications; no complete Collatz candidate is asserted.

## Proof

### Apply the already retained coefficient to the real system

We use L044's numerical transfer (3)–(6), before its final weakening
to factor 2. Its applicability to the real relaxation must be checked:
integer-cycle estimates are not being asserted for arbitrary real cycles.

Here a_i>=2 and G_i>1. Equation (4), with its negative terms retained,
gives

\[
s_{i+1}<G_i s_i/4+23/11<G_i s_i,
\]

because (3/4)G_i s_i>=(3/4)(540/11)=405/11>23/11.
All logarithms are defined since every s_i>=540/11>1. Thus the
shifted comparison used by L044 holds on this real domain.

For completeness of the applicability substitution, put ell=log2,
delta=log3/ell, alpha=log(27/16)=ell(3delta-4) and c_J=log(11/4).
Both delta-1 and alpha are positive. Using the second inequality
of (3) with the positive multiplier delta-1 gives exactly L044's
calculation

\[
\log G_i=J_i\alpha+H_i(\log3-ell)
 <(\delta-1)h_i+\delta J_i\alpha.
\]

The first inequality of (3) now gives

\[
h_{i+1}<\frac{3\delta^2}{4}h_i
       +\frac{\delta(3\delta-4)}4c_J
       <\frac{48}{25}h_i+\frac{32}{75}.             \tag{5}
\]

The last bounds are the existing L044 constants: 1<delta<8/5
from 3^5<2^8, 3delta-4>0 from 27>16, and 0<c_J<4/3.
The coefficient substitutions have positive signs, and h_i>0.
No integrality, actual valuation identity or new cycle theorem enters
this numerical passage. Repeating these lines is necessary to justify
their use under the relaxed real hypotheses, rather than to reprove
the sourced integer-cycle estimates.

Set q=48/25. Since 32/75+1=107/75<144/75=q, (5) gives
h_(i+1)+1<q(h_i+1). Induction along the first seventeen outgoing
words yields h_j+1<=q^j(h_0+1) for 0<=j<=17, permitting equality
at j=0. All eighteen input occurrences are covered even if heights
coincide. Equation (4) also holds at the closing index, but dropping
that equation already leaves an impossible system. Consequently the
proof does not replace a closing tail with an independent endpoint.

### Prefix counts and the unchanged seed

L041's bound P_i<(15/4)h_i+3 likewise uses just (3) and h_i>0.
Explicitly (3) implies

\[
P_i<\left(\frac{\log27}{4(\log2)^2}+\frac1{\log2}\right)h_i
       +\frac{\log27}{4(\log2)^2}c_J
     <\frac{15}{4}h_i+3.
\]

The numerical estimates are log2>2/3, log27<4 and c_J<4/3,
as justified in L041. They follow, respectively, from the positive
derivative of log t-2(t-1)/(t+1) for t>1, and the exponential-series
bound e^(4/3)>293/81>3 (also 11/4<3). In particular all coefficients
and the h_i being bounded are positive.

Write R=sum_(j=0)^17 q^j. Then

\[
K=\sum_i(P_i-J_i)<\sum_iP_i
 <\frac{15}{4}\sum_i(h_i+1)
 \le\frac{15}{4}R(h_0+1).
\]

Using (1) and (2) therefore forces

\[
N<\frac{399}{5}R\log N+(54+6\log18)R+\frac{1242}{1034}.
                                                               \tag{6}
\]

Every tail remains in N through (1); no upper bound on any a_i is
assumed. This is a consequence of the approved individual inequalities,
not an extra hypothesis imposed on the system. It is stronger than
Attempt 021's fixed factor-2 comparison, which remains exhausted.

### Exact contradiction on the entire admissible length ray

Since q>1,

\[
48^6=12230590464<12451171875=51\cdot25^6,
\quad
R=\frac{q^{18}-1}{q-1}
 <\frac{25(51^3-1)}{23}=\frac{3316250}{23}<150000.
\]

The exponential series gives e>163/60>27/10, so
27^3=19683>18000 proves log18<3. Also 1242/1034<2.
As N>1, substituting these upper bounds into (6) gives

\[
N<A\log N+B,\qquad A=11970000,\quad B=10800002.       \tag{7}
\]

On the other hand (1), 3^2>2^3 and primitive count scaling imply

\[
N>K\frac{\log3}{\log2}>\frac32K
  \ge\frac32K_0>C:=338460000.
\]

Define F(t)=t-A log t-B for every real t>=C. Since A<C,
F'(t)=1-A/t>0 on this entire ray. The exact integer comparison

\[
27^{20}=42391158275216203514294433201
 >33846000000000000000000000000=C10^{20}
\]

and e>27/10 imply log C<20. Hence

\[
F(C)>C-20A-B=338460000-250200002=88259998>0.
\]

Thus F(N)>0, contradicting (7). No search over integer parameters
or sample of lengths is used.

### Actual-word applicability, sources and verification limits

For actual eighteen-word closed concatenations, L041 supplies (1)'s
length conversion, (2), (3), (4), positivity, the lower junction height,
occurrence counts and primitive scaling. L044 records the primitive
odd-count input and nontriviality check: a junction n_i>=47 lies outside
the invariant shortcut cycle {1,2}. The relevant exact imports are:

- Christian Hercher, *There are no Collatz m-Cycles with m <= 91*,
  JIS 26 (2023), Article 23.3.5,
  [Theorem 16 and proof, printed pp. 10–11](https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/hercher5.pdf).
- John Simons and Benne de Weger, *Theoretical and computational bounds
  for m-cycles of the 3n+1-problem*, Acta Arith. 117 (2005), 51–70,
  [Corollary 2 and proof p. 53; Lemma 12 and proof p. 61; period conventions p. 52](https://www.impan.pl/shop/en/publication/transaction/download/product/82263).

The first gives positive linear form and reciprocal control; Lemma 12
and L041's junction mass yield the seed; Corollary 2 gives K_0>225640000.
Their known applicability is reused, with repeated periods and coincident
junctions counted by time occurrences. The full source minimum count is
never set to eighteen, and the selected junction is not asserted to be
the global minimum. The published height x_min>301*2^50, distributed
[Ro] computations and Roosendaal communication, continued-fraction
denominators 225644606 and 397573379, and Rhin/Crandall originals retain
their recorded import qualifications. Original certificates are not
independently verified. The inspected Hercher correction does not change
Theorem 16; no amended Theorem 21 or new computational threshold is used.

Reproduce the exact arithmetic support with
`python3 scripts/postspell-word-count/certify_eighteen_heights.py`.
The full certificate is
`scripts/postspell-word-count/eighteen-height-certificate.json`:
ten strict rational/integer comparisons pass, with no failures.
The proof above supplies the analytic transfer and all-real monotonicity;
the script is not a substitute for them or a separate critical audit.
L045's aggregate feasible tuple remains valid for its weaker stated system.
No new general theorem or originality beyond the inspected sources is claimed.

### Separate critical audit — 2026-10-10

Pre-invocation coverage was the unchanged SPECIALIZE assessment
`drafts/literature/2026-10-10-eighteen-height-infeasibility-audit.md`.
Verdict: **no defect found within the stated hypotheses and published
qualifications**. This REPRODUCTION audit establishes no stronger bound,
repair, originality or independent certification of the published inputs.
The full proof, L041's proof and audit, L044's transfer/applicability
passages, the approved real system, the complete generator and every
certificate value were inspected. No broader word count was tested.

For subsystem inclusion, the approved system explicitly assumes the same
integer guards, counts, primitive scaling, lower real heights, seed,
own-index inequalities and all eighteen endpoint equations. Its quantitative
positive lower linear-form bound implies Lambda>0; its length conversion
is exactly (1). Dropping its other aggregate and linear-form restrictions
can only enlarge the feasible set. Thus a contradiction from (1)–(4)
excludes the original full system. No real height is assumed to have an
integer valuation or to realize a parity path. Conversely, L041's actual
words give all the retained necessary conditions: a_i>=2, n_i>=47,
s_i>=540/11, the seed at a cyclically chosen smallest junction, the
two own-index bounds and the exact endpoint identity. The choice permits
ties and preserves every outgoing tail. Count scaling K=dK_0,L=dL_0
uses a positive repeat factor and never merges coincident occurrences.
The actual primitive cycle is nontrivial because it contains a junction
at least 47. The precisely cited Corollary 2 applies to that cycle and
gives K_0>225640000, without substituting eighteen for its full minimum
count. The general estimates are imposed as necessary conditions in the
real system, not extended as source theorems about real cycles.

For the transfer, subtracting the positive terms in (4), then using
2^(-a_i)<=1/4 on the positive G_i s_i, gives
s_(i+1)<G_i s_i/4+23/11. The second strict comparison follows from
(3/4)G_i s_i>=405/11>23/11. This argument retains both shifts; all
logarithms have positive arguments greater than one. With
alpha=ell(3delta-4)>0 and delta-1>0, the H_i substitution gives
log G_i<(delta-1)h_i+delta J_i alpha. Adding h_i and substituting
the same index's J_i bound gives coefficient
delta+delta(3delta-4)/4=3delta^2/4. The positive factors satisfy
delta<8/5, 3delta-4<4/5 and c_J<4/3, so (5) follows with
48/25 and 32/75. The shift is valid because 107/75<48/25.
Induction uses exactly the seventeen edges 0 through 16 to cover
indices 0 through 17. The final edge remains an assumption of the
stated system; proving its enlarged subsystem impossible needs no use
of that edge and does not purport to construct an unclosed witness.

The prefix bound uses only (3): P_i ell<h_i+J_i log27, followed
by the first own-index inequality with positive log27. The elementary
logarithm estimate has derivative (t-1)^2/[t(t+1)^2]>0 for t>1
and value zero at t=1, giving log2>2/3. The exponential partial
sum through degree three at 4/3 equals 293/81>3, giving log27<4
and c_J<4/3. Therefore the prefix height coefficient is below
9/4+3/2=15/4 and its constant below (9/4)(4/3)=3. Since h_i>0
and J_i>=2, summing yields strictly
K<sum P_i<(15/4)sum(h_i+1)<=(15/4)R(h_0+1).
Multiplication by 8/5 and insertion of the unchanged seed gives
exactly 399R/5 and (54+6log18)R in (6). The additive tail term
is 69*18/1034=621/517; no tail is discarded from N or capped.

The independent closed-form geometric calculation is
R=(48^18-25^18)/(23*25^17)
=79544651309362595873687268553/582076609134674072265625.
The sixth-power comparison gives
R<3316250/23<150000. The positive exponential tail after degree
five gives e>163/60>27/10. The integer comparisons 27^3>18*10^3
and 27^20>C*10^20 consequently imply log18<3 and log C<20.
All substitutions in (6) have positive multipliers, including log N
because the positive counts force N>1. They give precisely
A=11970000 and B=10800002. Positivity of Lambda and 9>8 give
N>(3/2)K>=(3/2)K_0>C. Finally A<C ensures F'(t)=1-A/t>0 for
every real t>=C, and 20A+B=250200002 yields F(C)>88259998>0.
Hence F(N)>0 contradicts (7) on the entire required ray. Neither
integer sampling nor finite parameter feasibility is used in this step.

Reproduce the audit with
`python3 scripts/postspell-word-count/audit_eighteen_heights.py`.
It regenerates the original certificate byte for byte (SHA-256
`d4fbc8efc0d2bac5025a5b85bba34e6972a6c664c21c196cf57811bf9e51a689`),
checks all ten records including exact operands and saved flags, and
checks their summaries and supporting identities. All 32 exact checks
pass, with full actual/required values and no failures in
`scripts/postspell-word-count/eighteen-height-audit-certificate.json`.
The geometric sum is recomputed using its closed form independently of
the original termwise sum. All certificate records were read completely;
the analytic arguments above, not these finite checks, justify the
real-domain transfer and monotonicity.

The source citations and computational qualifications above remain in
force. Original published computation certificates, Rhin/Crandall
originals, external Lean and matching Mathlib coverage were not verified.
L045's height-free witness and Attempt 021's factor-2 stop remain valid
for their weaker system. L041 and L044 remain the direct local inputs;
no argument or dependency changed, so PROOF.md and DAG.md are unchanged.
This canonical verdict supersedes the overview's pending L046 audit
wording only. Entry, unrestricted counts/cycles, divergence and universal
eventual descent remain unresolved.

## Mathlib

Matching coverage of this full simultaneous system and the imported cycle
estimates was not checked. Elementary logarithm and finite geometric-sum
facts are used in the written proof, but no Lean declaration is asserted
to formalize this result. Unknown coverage is not evidence of absence.
