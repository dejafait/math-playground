# L052 — Twenty-three-word simultaneous real-height infeasibility

## Hypotheses

Use exactly L051 (1)–(4) at r=23. Explicitly, indices are modulo 23;
J_i>=2, H_i>=3 and a_i>=0 are integers with a_i=2 modulo 18. Set
K=sum_i(3J_i+H_i), L=sum_i(J_i+a_i), N=K+L. Positive integers
d,K_0,L_0 satisfy K=dK_0, L=dL_0 and K_0>225640000. Require

\[
\Lambda=N\log2-K\log3>0,\qquad
N<\frac85K+\frac{1587}{1034}.                       \tag{1}
\]

Let s_i>=540/11 be real, h_i=log s_i, s_0=min_i s_i and s_23=s_0.
Require

\[
0<h_0<\frac{133}{10}\log N+8+\log23,                \tag{2}
\]
\[
4J_i\log2\le h_i+\log(11/4),\qquad
H_i\log2<h_i+J_i\log(27/16),                        \tag{3}
\]
\[
s_{i+1}=2^{-a_i}\left(G_i s_i-\frac{12}{11}(3/2)^{H_i}-1\right)
                    +\frac{23}{11},\qquad
G_i=(27/16)^{J_i}(3/2)^{H_i}.                        \tag{4}
\]

All logarithms are natural. Independent tails, repetitions and ties
remain allowed. No integer parity, residue, valuation realization or
global-minimum assertion about the real junctions is imposed. In
particular, L051's failed sufficient-test guards are not hypotheses.

## Conclusion

There is no simultaneous solution of this system. Under L041's actual
word hypotheses this excludes closed concatenations of twenty-three
postspell words, subject to the inherited published qualifications.
Together with L051 this extends the restricted exclusion through
twenty-three. The key contradiction is

\[
K<211120000<225640000<K_0\le K.                      \tag{5}
\]

This is a local REPRODUCTION under prior SPECIALIZE coverage. It makes
no originality claim beyond the inspected sources. The separate critical
audit below found no defect under the written hypotheses and inherited
qualifications. It is not a complete Collatz candidate: universal
entry, unrestricted cycles, divergence and eventual descent remain open.
L051's fixed-test failure and L049's weaker scalar survivor remain valid.

## Proof

### Own-index odd counts and the retained logarithmic transfer

Put ell=log2, delta=log3/ell, c=log(11/4) and alpha=log(27/16).
The elementary comparisons 3^2>2^3 and 27>16 give delta>3/2 and
alpha>0. Every h_i is positive. The rational logarithm certificate
specified below proves

\[
\ell>6931/10000,\quad \log3<10987/10000,\quad
c<41/40,\quad \delta<10987/6931<793/500.             \tag{6}
\]

From this occurrence's second guard in (3),

\[
3J_i+H_i< h_i/\ell+(3\delta-1)J_i.
\]

Since 3delta-1>0, its first guard can be substituted with the same
index, giving

\[
3J_i+H_i<\frac{3(\delta+1)}{4\ell}h_i
              +\frac{(3\delta-1)c}{4\ell}.
\]

All substituted quantities are positive. By (6), the two coefficients
are respectively less than

\[
\frac{19395}{6931}<\frac{14}{5},\qquad
\frac{77039}{55448}<\frac75.
\]

Thus, directly retaining the odd count rather than bounding it by
4J_i+H_i, we obtain

\[
3J_i+H_i<\frac{14}{5}h_i+\frac75
                  <\frac{14}{5}(h_i+1).            \tag{7}
\]

L046's real-domain transfer proof, before its numerical weakening,
applies occurrence by occurrence to (3)–(4). Indeed a_i>=2 and
s_i>=540/11 give s_(i+1)<G_i s_i/4+23/11<G_i s_i. The positive
multipliers delta-1 and alpha then permit both own-index substitutions,
yielding

\[
h_{i+1}<\frac{3\delta^2}{4}h_i
                   +\frac{\delta(3\delta-4)c}{4}.
\]

This uses L046's per-occurrence calculation, not its eighteen-word
conclusion or an integer theorem about arbitrary real junctions. By (6),

\[
\frac{3\delta^2}{4}<\frac{1886547}{1000000}<\frac{189}{100},
\quad
\frac{\delta(3\delta-4)c}{4}
 <\frac{12322427}{40000000}<\frac{31}{100}.
\]

As 1+31/100<189/100, putting rho=189/100 gives
h_(i+1)+1<rho(h_i+1). Induction along the 22 edges from occurrence
0 to occurrence 22 covers all 23 outgoing word inputs. With

\[
R=\sum_{j=0}^{22}\rho^j
 =\frac{189^{23}-100^{23}}{89\,100^{22}}<2600000,
\]

equation (7) implies

\[
K<\frac{14}{5}\sum_{i=0}^{22}(h_i+1)
 \le\frac{14}{5}R(h_0+1).                           \tag{8}
\]

At i=0 the induction bound is an equality; all other steps are strict.
Coincident values and repeated periods are still distinct occurrences.
The twenty-third endpoint will be used in the product below.

### A finite ceiling that retains every tail in N

The integer guards give N>=13*23>1. Combining (1), (2) and (8),
with positive multipliers throughout, gives

\[
N<\frac{112}{25}R\left(\frac{133}{10}\log N+9+\log23\right)
      +\frac{1587}{1034}.
\]

The exponential series gives e>163/60>27/10, and (27/10)^4>23,
so log23<4. Using R<2600000 and 1587/1034<2 therefore yields

\[
N<A\log N+B,\qquad A=154918400,\quad B=151424002.    \tag{9}
\]

Let M=3600000000. The certificate proves log M<111/5. For every
real t>=M the function F(t)=t-A log t-B has positive derivative,
since A<M. Moreover

\[
F(M)>M-\frac{111}{5}A-B=9387518>0.
\]

Consequently (9) is impossible anywhere on that ray, and 0<K<N<M.
This is an all-real argument; no bounded enumeration replaces it.
All independent tails remain in N through (1); none is individually capped.

### Integer counts and all cyclic endpoints

Keep exactly L050's pair p=9809721694, q=6189245291. The certificate
proves

\[
0<\epsilon=q\log3-p\log2<958/10^{13},\qquad
2M(958/10^{13})=4311/6250<6931/10000<\ell.
\]

Since Lambda>0, N/K>delta>p/q. Thus z=Nq-Kp is a positive integer,
even though the junctions may be real. In particular z>=1 and K<M
give the same separation argument as L050:

\[
q\Lambda=\ell z-K\epsilon>\ell-M\epsilon
  >\ell/2>1/3,\qquad \Lambda>1/(3q).               \tag{10}
\]

The last inequality follows from (6), which implies ell>2/3. No pair
optimization or new lower-bound hypothesis is used.

Use L050's exact product calculation, whose word count is arbitrary:
set n_i=s_i-23/11>=47 and

\[
\eta_i=\frac{23}{11}-\frac{12}{11}(16/27)^{J_i}
                         -(16/27)^{J_i}(2/3)^{H_i}.
\]

Both subtracted terms are positive and their sum is strictly smaller
than 12/11+1=23/11, so 0<eta_i<23/11. Equation (4) is exactly
n_(i+1)=G_i 2^(-a_i)(n_i+eta_i). Multiplying all 23 equations,
including the closing equation, and taking logarithms cancels the
positive product of the n_i and gives

\[
\Lambda=\sum_{i=0}^{22}\log(1+\eta_i/n_i)
 <\frac{529}{11n_0}.                               \tag{11}
\]

Here log prod_i(G_i/2^{a_i})=K log3-N log2=-Lambda, and
n_i>=n_0. This restates the necessary substitution in the cited
product argument without asserting a general rational-cycle theorem.
It permits ties, repetitions and independent tails.

Combining (10)–(11) gives

\[
s_0< D:=\frac{1587q+23}{11}=\frac{9822332276840}{11}.
\]

The exact integer-power comparison D<(27/10)^28, with e>27/10,
proves h_0<28. Inserting this into (8) now gives

\[
K<\frac{14}{5}\,2600000\,29=211120000.
\]

But d>=1 and K_0>225640000 imply K=dK_0>225640000. This is (5),
the required contradiction for the entire simultaneous system.

### Exact certificate and its scope

Run `python3 scripts/postspell-word-count/certify_twenty_three_heights.py`.
Its full rational evidence is
`scripts/postspell-word-count/twenty-three-height-certificate.json`.
The 22 checks pass with no failures; the complete sign comparisons and
load-bearing operands were inspected. The generator is a calculation
aid, not an independent critical audit or a replacement for the proof.

For completeness, its logarithm bounds use L051's already justified
integrated geometric remainder. Write t=2^k v, k>=0, 1<=v<2,
x=(v-1)/(v+1); for log2 use x=1/3. With m=96,

\[
\log v=2\sum_{j=0}^{m-1}\frac{x^{2j+1}}{2j+1}
 +2\int_0^x\frac{u^{2m}}{1-u^2}\,du.
\]

The remainder is nonnegative and strictly less than
E=9/[4(2m+1)3^{2m+1}]. Round each summand down to a multiple of
2^(-192). If b is their sum, b<=log v<b+m*2^(-192)+E. Add k
times the outward bounds for log2. All operations use integers and
Fractions, including the four arguments 2,3,11/4,M. The certificate
retains each rounded summand, binary reduction, remainder, enclosure,
operand and sign margin. Epsilon uses q times the lower/upper log3
bound minus p times the upper/lower log2 bound, respectively. Thus
the large cancellation is rigorously outward enclosed. All power and
geometric-sum comparisons are exact integer/rational arithmetic.

### Actual-word specialization and inherited qualifications

L041 supplies exactly (1)–(4) for actual closed concatenations at r=23.
Its own-index identities, seed and length conversion hold for every
r>=3. The lower junction bound, primitive scaling and cyclic relabeling
retain repeated representations and ties. A junction at least 47 makes
the primitive integer cycle nontrivial. Hence this infeasibility theorem
excludes actual words without identifying a junction with the global
cycle minimum or setting the full local-minimum count equal to 23.

The precise inherited imports are Christian Hercher, *There are no
Collatz m-Cycles with m <= 91*, JIS 26 (2023), Article 23.3.5,
[Theorem 16 and proof, pp. 10–11](https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/hercher5.pdf),
and John Simons and Benne de Weger, *Theoretical and computational
bounds for m-cycles of the 3n+1-problem*, Acta Arith. 117 (2005), 51–70,
[Corollary 2 and proof p. 53, Lemma 12 and proof p. 61, period conventions p. 52](https://www.impan.pl/shop/en/publication/transaction/download/product/82263).
Hercher and Lemma 12 support the imposed seed/length conditions via
L041; Corollary 2 gives the primitive integer odd-count threshold.
Their general theorems are not reproved or asserted for arbitrary reals.
No rational coding theorem is needed for this contradiction.

The published height 301*2^50, distributed [Ro] computation, Roosendaal
communication, continued-fraction denominators 225644606/397573379,
and Rhin/Crandall originals retain their existing imported qualifications;
original computational certificates and external Lean builds are not
independently verified here. The inspected June 2026 Hercher correction
does not change Theorem 16; amended Theorem 21 is not used. The prior
SPECIALIZE assessment covers the simultaneous target; the specialization
above improves retained coefficient arithmetic, not a general Collatz
theorem or the fixed predicate stopped in L051.

### Separate critical audit — 2026-10-10

The approved RESEARCH/REPRODUCTION audit found no defect in this proof
or its certificate. It reused the ready SPECIALIZE source assessment;
it neither strengthens the theorem nor recertifies the published inputs.
The full generator and every load-bearing certificate field were checked.
All **601 audit checks pass**, including all 480 rounded summands, all
four logarithm arguments, every saved operand and all 22 saved sign rows
with their margins. Saved flags were compared with recomputed truth values,
not assumed. The original certificate regenerates byte for byte with SHA-256
`bc1bc06f1be4dd43c287e2ac7cc1611f6a6e48a6616696cca304d95e96c23060`.

Here are the analytic and applicability checks underlying that verdict.
The congruence and nonnegativity of each integer a_i give a_i>=2;
each word contributes at least 9 odd and 4 even inputs, so N>=299.
All h_i>0. Writing alpha=ell(3delta-4), the own-index H guard gives
3J_i+H_i<h_i/ell+(3delta-1)J_i. The multiplier 3delta-1 is
positive, so the same occurrence's J guard gives exactly the two
coefficients in (7). Their stated rational majorants are respectively
19395/6931 and 77039/55448, independently recomputed and strictly
below 14/5 and 7/5. No other occurrence's parameter is substituted.

Dropping the negative endpoint terms gives
s_(i+1)<G_i s_i/4+23/11<G_i s_i: the second comparison follows
from (3/4)G_i s_i>=405/11>23/11. This reasoning uses positive real
junctions and a_i>=2, with no integer-orbit premise. Next
log G_i<(delta-1)h_i+delta J_i alpha. Substitution of the same
J guard makes the h_i coefficient
delta+delta(3delta-4)/4=3delta^2/4 and the constant
delta(3delta-4)c/4. Every factor being enlarged is positive.
The exact majorants 1886547/1000000 and 12322427/40000000
are strictly below 189/100 and 31/100; adding 1 is valid because
131/100<189/100. Twenty-two forward edges cover all twenty-three
outgoing inputs. The bound at input zero is equality, while the remaining
inductive comparisons are strict; (8) has the correct strict outer sign.
Repeated values remain separate time occurrences.

The exact geometric sum is less than 2600000. In (1), replace K
using (8), then use h_0+1<(133/10)log N+9+log23. All multipliers
are positive, and log N>0 licenses enlargement of R. The positive
exponential tail gives e>sum_(j=0)^5 1/j!=163/60>27/10;
(27/10)^4>23 proves log23<4. Thus A=154918400 and
B=151424002 are correct in (9). The independently enclosed log M
is below 111/5; A<M and M-(111/5)A-B=9387518>0 establish the
contradiction on the entire real ray t>=M, not only at its endpoint.
Every tail remains in N. This proves 0<K<N<M before integer
separation is used.

Independent unrounded rational sums certify epsilon>0 and
epsilon<958/10^13 for the unchanged p,q. The compact comparison is
2M(958/10^13)=4311/6250<6931/10000<ell. Since K,N,p,q are
integers and N/K>delta>p/q, z=Nq-Kp is an integer at least one.
Consequently q Lambda=ell z-K epsilon>ell-M epsilon>ell/2>1/3.
Real junctions do not affect integrality of these total counts. Neither
the failed old half-log guard nor L051's sufficient predicate is used
as a premise.

All n_i=s_i-23/11>=47 are positive. The powers in eta_i lie in
(0,1), proving 0<eta_i<23/11, with both affine offsets retained.
Expanding G_i(n_i+eta_i) recovers exactly
G_i s_i-(12/11)(3/2)^H_i-1. Also
log(G_i/2^a_i)=(3J_i+H_i)log3-(4J_i+H_i+a_i)log2.
Multiplication of all twenty-three endpoint equations, including the
closing one, therefore gives (11). The choice n_0=min_i n_i allows
ties; no global cycle minimum is selected. Combining (10) and (11)
gives s_0<(1587q+23)/11=9822332276840/11. The exact power comparison
with (27/10)^28 and the exponential lower bound prove h_0<28.
Equation (8) then gives K<211120000, leaving the strict margin
225640000-211120000=14520000 against K>=K_0>225640000.

The arithmetic audit is independent of the generator's rounding code.
For each saved reduction it checks t=2^k v, 1<=v<2, and every
integer floor against its exact rational summand, including the base
log2 calculation. It verifies the 96-term rounding budget, integral
remainder and both outward endpoints, then reconstructs every operand
and sign row. As a second computation, for x=(v-1)/(v+1) it sums
144 **unrounded** terms 2x^(2j+1)/(2j+1). The integral identity above
puts log v between that sum and the sum plus
2x^289/[289(1-x^2)]. For x>0 the upper inequality is strict; at
x=0 both bounds are exactly zero. Applying the same independent
construction to log2 and adding k times its bounds encloses every
logarithm inside the saved interval. All 22 inequalities also pass
using these independent enclosures; epsilon is enclosed with opposite
log endpoints on the subtracted term. Complete exact evidence is saved
in `scripts/postspell-word-count/twenty-three-height-audit-certificate.json`.
Reproduce with
`python3 scripts/postspell-word-count/audit_twenty_three_heights.py`.
The verifier reads the original certificate fully, regenerates it in
a temporary directory and preserves the original file.

For the actual-word bridge, L041's hypotheses retain actual input
parities, positive odd residue-20 junctions, exact independent tails
and closure. The junction bound is n_i>=47. Its disjoint occurrence
partition and primitive scaling preserve K=dK_0,L=dL_0, including
repeated representations. The primitive cycle is nontrivial because
it contains a junction at least 47. Simons–de Weger's cited Corollary 2
therefore supplies K_0>225640000 with the original qualifications.
L041 derives the positive linear form and length conversion from the
cited Hercher Theorem 16, and the log r seed from that mass bound
and the cited Lemma 12, before putting r=23. Its own-word identities
give each guard and the exact shifted endpoint. Relabeling chooses only
the smallest designated junction. No full minimum count is set to 23,
and the cited integer-cycle theorems are never applied to arbitrary real
junctions. The published computations, Rhin/Crandall imports and external
formal-verification limitations remain exactly as stated above.

No argument or direct dependency changed, so PROOF.md and DAG.md are
unchanged. This canonical verdict supersedes their pending L052 audit
wording only. L051's fixed-test stop and the recorded weaker-system
failures remain valid. No new count, optimized pair, simultaneous witness,
unrestricted cycle exclusion or universal descent theorem was obtained.

## Mathlib

Full matching coverage has not been checked. Integer counts, finite
products and sums, real logarithms, geometric sums and monotonicity are
the supporting mathematics used here; no particular Mathlib declaration
is asserted to establish the whole result. Unknown coverage is not an
absence claim, and no local formal verification is claimed.
