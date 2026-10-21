# L044 — Thirteen-word exclusion using retained height coefficients

## Hypotheses

Let T(t)=t/2 for even positive integers and T(t)=(3t+1)/2 for odd
positive integers. O and E specify actual input parities. For 0<=i<13
let J_i>=2, H_i>=3 and a_i>=0 be integers with a_i congruent to 2
modulo 18. Write

\[
W_i=(OOEO)^{J_i}O^{H_i}E^{a_i},\qquad
D_i=4J_i+H_i+a_i,\qquad N=\sum_{i=0}^{12}D_i.
\]

Assume the concatenation is actual at a positive odd integer n_0>1,
returns to n_0 after N shortcut steps, and every junction occurrence
n_i=T^(D_0+...+D_(i-1))(n_0) is odd and 20 modulo 27. Set n_13=n_0.
All final even tails are exact. Independent tails, repeated periods and
coincident junctions are allowed. No least-root, first-return, primitive
representation, global-minimum or relative-height assumption is imposed.
All logarithms are natural.

## Conclusion

No such closed concatenation of thirteen words exists, subject to the
published cycle estimates and computational qualifications specified below.

The retained wordwise estimates imply the necessary inequality

\[
N<A\log N+B,\qquad
A=\frac{399}{5}\,8191=\frac{3268209}{5},\qquad
B=72\cdot8191+\frac{897}{1034}.                    \tag{1}
\]

It is incompatible with every real N>=338460000, whereas the sourced
primitive odd-count threshold forces N>338460000. This extends the
restricted language exclusion to thirteen; it does not bound arbitrary
word counts or establish entry, arbitrary-cycle exclusion, divergence
control or universal eventual descent. The separate critical audit below
found no defect within the stated hypotheses and imported qualifications.

## Proof

### Inputs, counts and the designated-junction seed

The hypotheses are exactly L041's hypotheses at r=13. In particular
a_i>=2 and n_i>=47. Its occurrence counts and period reduction give

\[
K=\sum_i(3J_i+H_i),\quad L=\sum_i(J_i+a_i),\quad N=K+L,
\quad K=dK_0,\quad L=dL_0\quad(d\ge1).
\]

Here K_0,L_0 are the primitive odd and even counts. The orbit is nontrivial:
it closes through n_0>=47, outside the invariant shortcut cycle {1,2}.
L041 counts input times rather than distinct junction values, so the
counts and all its estimates retain repetitions and coincident states.

The precise general inputs used in L041 are Christian Hercher,
*There are no Collatz m-Cycles with m <= 91*, JIS 26 (2023),
Article 23.3.5, [Theorem 16 and proof, printed pp. 10–11](https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/hercher5.pdf),
and John Simons and Benne de Weger, *Theoretical and computational bounds
for m-cycles of the 3n+1-problem*, Acta Arith. 117 (2005), 51–70,
[Lemma 12, printed p. 61; nonminimal-period conventions, p. 52](https://www.impan.pl/shop/en/publication/transaction/download/product/82263).
L041 has already justified their applicability and represented-period
scaling, giving 0<Lambda=N log2-K log3 and its junction reciprocal
upper bound and logarithmic lower bound. Their only use here is through
L041's proved seed and length conversion. No general cycle theorem is
reproved. The inspected June 2026 Hercher corrigendum does not amend
Theorem 16; no amended Theorem 21 input is used.

Cyclically relabel to choose n_0=min_i n_i, resolving ties by any one
occurrence. This is the smallest designated junction, not necessarily
the global orbit minimum. Put

\[
s_i=n_i+23/11,\quad h_i=\log s_i>0,\quad
P_i=4J_i+H_i,\quad G_i=(27/16)^{J_i}(3/2)^{H_i}.
\]

L041 (6), (7) and (11) give respectively

\[
h_0<\frac{133}{10}\log N+8+\log13,\qquad
P_i<\frac{15}{4}h_i+3,\qquad
N<\frac85 K+\frac{897}{1034}.                       \tag{2}
\]

The last inequality retains every final tail in N through the cycle
identity; no upper bound on an individual a_i is assumed.

### Retain the logarithmic coefficients in each transfer

Write ell=log2, delta=log3/ell and c_J=log(11/4); c_J is a fixed
constant, independent of the indexed parameters. L041's two inequalities
immediately before (7), applied to each occurrence's own J_i,H_i, yield

\[
4J_i\,ell\le h_i+c_J,\qquad
H_i\,ell<h_i+J_i(3\log3-4ell).                     \tag{3}
\]

For the second inequality subtract 4J_i ell from the displayed bound
P_i ell<J_i log27+h_i. Both follow from actual-word valuations and
the positive shifted affine identity in L041, not from a selected
minimum's parameters at a different occurrence.

Put alpha=3 log3-4ell=log(27/16)>0. Since delta>1, substitution
of the strict H_i bound from (3) into log G_i gives

\[
\begin{aligned}
\log G_i
 &=J_i\alpha+H_i(\log3-ell)\\
 &<(\delta-1)h_i+\delta J_i\alpha.
\end{aligned}                                                     \tag{4}
\]

L041 (8) gives s_(i+1)<G_i s_i. The shifts are already justified
there by the exact identity
z=G_i s_i-(12/11)(3/2)^{H_i}-1, n_(i+1)=z/2^{a_i}, followed by
s_(i+1)<G_i s_i/4+23/11<G_i s_i. Thus this use of (8) retains
both offsets and needs only a_i>=2; it does not approximate an
unshifted endpoint or impose a junction-height ratio.

Taking logarithms, applying (4), and then using the first bound in
(3) with the positive coefficient delta alpha gives

\[
\begin{aligned}
h_{i+1}
 &<\delta h_i+\delta J_i\alpha\\
 &\le\delta h_i+\frac{\delta(3\delta-4)}4(h_i+c_J)\\
 &=\frac{3\delta^2}{4}h_i
       +\frac{\delta(3\delta-4)}4c_J.               \tag{5}
\end{aligned}
\]

All substitutions preserve their direction: ell>0 and 3delta-4>0
because 27>16. The exact inequality 3^5<2^8 gives delta<8/5.
Also 0<c_J<4/3: 11/4<3 and L041's elementary bound log3<4/3
applies. Consequently (5) and h_i>0 give

\[
h_{i+1}<\frac{48}{25}h_i+\frac{32}{75}<2h_i+1,
\qquad h_{i+1}+1<2(h_i+1).                         \tag{6}
\]

The constant bound is
(8/5)(4/5)(4/3)/4=32/75; the difference in the second comparison
is (2/25)h_i+43/75>0. This is the gain from retaining the
coefficients instead of L041's looser log G_i<P_i/2 relaxation.

### Assemble thirteen occurrences and test all admissible lengths

Induction using (6) gives h_j+1<=2^j(h_0+1) for 0<=j<=12,
with equality allowed at j=0. These are the thirteen successive
indexed occurrences after the cyclic relabeling; no distinctness of
their state values is needed. From (2),

\[
K<\sum_{j=0}^{12}P_j
 <\frac{15}{4}\sum_{j=0}^{12}(h_j+1)
 \le\frac{15}{4}\,8191(h_0+1),                    \tag{7}
\]

where sum_{j=0}^{12}2^j=2^13-1=8191. The strict comparison
P_j<(15/4)(h_j+1) follows from 3<15/4.

The exponential series gives e>163/60>27/10, so
e^3>(27/10)^3=19683/1000>13 and log13<3. The seed in (2)
therefore gives h_0+1<(133/10)log N+12. Inserting (7) into
the final inequality of (2) proves (1), since
(8/5)(15/4)=6 and 6(133/10)=399/5.

Import Simons–de Weger, the paper cited above,
[Corollary 2 and complete proof, printed p. 53; map and period conventions, pp. 51–53](https://www.impan.pl/shop/en/publication/transaction/download/product/82263):
the primitive odd count satisfies K_0>M=225640000. The positive
nontrivial primitive orbit just identified meets its hypotheses.
Its full local-minimum count is used for source applicability; it is
not set equal to thirteen designated junctions. As 3^2>2^3 and
Lambda>0, the represented counts obey

\[
N>K\frac{\log3}{\log2}>\frac32K
  \ge\frac32K_0>C=338460000.                       \tag{8}
\]

Now define F(t)=t-A log t-B for real t>=C. The exact comparisons

\[
27^{20}=42391158275216203514294433201
 >C10^{20}=33846000000000000000000000000,
\qquad A=3268209/5<C
\]

give log C<20 and F'(t)=1-A/t>0. Moreover 897/1034<1 and

\[
20A+B=1668\cdot8191+897/1034<13662589,
\]
\[
F(C)>C-13662589=324797411>0.                         \tag{9}
\]

Thus F(N)>0 by (8) and monotonicity, contradicting (1), which
requires F(N)<0. This excludes every admissible length above the
published threshold, not just L043's scalar witness or a bounded
parameter sample.

### Qualifications and verification

The source Corollary 2 imports the computational height
x_min>301*2^50, attributed to distributed [Ro] computations with a
Roosendaal personal-communication footnote, and continued-fraction
denominators 225644606 and 397573379. These are published inputs;
their original certificates and Crandall's proof are not independently
certified here. L041's Rhin and computational qualifications for
Lemma 12 remain unchanged. No external Lean build is certified.

The pre-invocation assessment is
`drafts/literature/2026-10-08-unrelaxed-thirteen-word-estimates.md`
(SPECIALIZE). This is REPRODUCTION: the local progress is an elementary
assembly of inspected wordwise estimates, with no claim of originality
or progress beyond the checked source mathematics. Full working notes
are in `drafts/2026-10-08-unrelaxed-thirteen-word-calculation.md`.
Exact constant checks are reproducible with
`python3 scripts/postspell-word-count/certify_thirteen.py`; their full
values are in `scripts/postspell-word-count/thirteen-certificate.json`.
The finite arithmetic checks supplement (3)–(9); they do not substitute
for the cyclic argument or the proof for all real t>=C.

L043's maximality statement for its specified relaxed scalar system
remains valid: this proof uses additional wordwise information that
system discarded. Attempt 019's guard-only failure and history 069's
full-minimum-count mismatch are also preserved. This is neither a
guard-only contradiction nor the substitution m=13. No claim about
fourteen or unrestricted word counts is made in this bounded step.
Universal entry, other cycles, divergence and eventual descent remain
unresolved. The main Collatz target has no complete candidate argument.

### Separate critical audit — 2026-10-09

The unchanged pre-invocation SPECIALIZE assessment is
`drafts/literature/2026-10-08-thirteen-word-exclusion-audit.md`.
Verdict: **no defect found within the stated hypotheses and published
qualifications**. This is a REPRODUCTION audit. It supplies no stronger
bound, repaired theorem, source-computation certification or originality
claim. The full proof, L041's load-bearing passages and its separate
audit, the entire exact generator, and all seventeen certificate records
and summary values were inspected.

The actual-word hypotheses match L041 at r=13. Odd residue-20 junctions
are at least 47, while nonnegative tails congruent to 2 modulo 18 are
at least 2. The word intervals partition the N input times; the counts
K=sum(3J_i+H_i) and L=sum(J_i+a_i) therefore include every input once.
Least positive return time p divides N: writing N=dp+s with 0<=s<p
would give T^s(n_0)=n_0, hence s=0. Thus K=dK_0 and L=dL_0,
including repeated representations. A positive orbit returning through
n_0>=47 cannot be the invariant cycle {1,2}. These facts license the
published Corollary 2 cited above on the primitive orbit. No assumption
that the thirteen junctions are distinct, primitive or all local minima
is made; the source's full minimum count is not replaced by thirteen.

For the inherited seed, L041 combines
e^(-6.125581)K^(-133/10)<Lambda<(23/11)sum_i(1/n_i)
with sum_i(1/n_i)<=13/b at b=min_i n_i. This gives the upper bound
on b in the required direction. The shift costs
log(1+23/(11b))<23/517<1/20; the remaining fixed terms are
less than 73/10<8. Replacing log K by log N is valid since 1<K<N.
This verifies the first inequality in (2). The source upper bound scales
linearly from primitive occurrences, while the primitive Lemma 12 lower
bound scales to e^(-6.125581)d^(143/10)K^(-133/10), at least the
represented lower bound just used. L041's length identity
N=K log3/log2+Lambda/log2, with Lambda<299/517 and log2>2/3,
gives the last inequality in (2), including the term 897/1034.
No tail is discarded or separately capped.

For each own index, actual finite-word valuations in L041 give
v_2(y+1)=H_i and v_2(11n_i+23)=4J_i+2. Positivity then gives
4J_i ell<=h_i+log(11/4) and
H_i ell<h_i+J_i log(27/16), precisely (3). The same actual endpoint
has z=G_i s_i-(12/11)(3/2)^H_i-1>0. Since a_i>=2,
s_(i+1)<G_i s_i/4+23/11<G_i s_i, with the second comparison
following from G_i s_i>=540/11. Thus neither affine offset is lost.

In (4), multiplication by log3-ell=(delta-1)ell preserves strictness
since delta>1. The J_i coefficient becomes alpha+(delta-1)alpha
=delta alpha>0. Substitution of the J_i bound in (5) is therefore
valid, giving h_i coefficient
delta+delta(3delta-4)/4=3delta^2/4. Both delta and 3delta-4 are
positive, and 3^5<2^8 gives their upper bounds 8/5 and 4/5.
Together with 0<c_J<4/3 this gives coefficients below 48/25 and
32/75. Since h_i>0, the gap to 2h_i+1 is
(2/25)h_i+43/75>0. This verifies the strict shifted recurrence (6).

Cyclic relabeling preserves all thirteen actual words and chooses a
minimizing occurrence, with any tie allowed. Induction uses j=0,...,12;
its only permitted equality is at j=0, and coincident state values cause
no change. The exact sum is 8191. Also
K=sum(P_i-J_i)<sum P_i and P_i<(15/4)h_i+3<(15/4)(h_i+1).
Hence (7) follows with the indicated strict sign. The exponential-series
partial sum 163/60>27/10 and (27/10)^3>13 give log13<3, so the
seed shift is bounded by (133/10)log N+12. Multiplication by
(8/5)(15/4)=6 gives exactly A=3268209/5 and
B=609804465/1034 in (1).

The imported strict threshold K_0>225640000 and positive Lambda give
N>(log3/log2)K>(3/2)K>= (3/2)K_0>338460000, because 9>8.
The exponential-series bound and the full integer power comparison
in (9) prove log C<20 without decimal approximations. Since A<C,
F'(t)>0 for every real t>=C. Exact rational recomputation gives
20A+B=14127116889/1034<13662589 and
C-20A-B=335840523111/1034>324797411>0. Thus F(C)>0 and
F(N)>0, contradicting (1) throughout the required real ray. A check
only at C would not suffice without this derivative argument.

The generator `scripts/postspell-word-count/certify_thirteen.py` uses
integer and Fraction arithmetic for its seventeen claims. Each claim
matches the constant or comparison used above; all actual/required
values in `scripts/postspell-word-count/thirteen-certificate.json` were
read in full. Regeneration passed 17/17 checks and reproduced that
certificate byte for byte (SHA-256
`8d1877968c0b94b8c6ea41efe702723a05affb04014e2101a394450537b54c86`).
These finite checks verify the constants, while the analytic and
occurrence arguments above supply the infinite-domain justification.

The precise Hercher Theorem 16 and Simons–de Weger Lemma 12 and
Corollary 2 citations and their qualifications above remain in force.
Their original computational certificates, Rhin/Crandall originals,
external Lean and Mathlib matching were not independently verified.
L043 is a scalar comparator, not an input; its maximality and the
recorded guard/minimum-count failures remain intact. L041 remains the
only direct local lemma input. No mathematical assembly or dependency
changed, so PROOF.md and DAG.md are unchanged; this canonical verdict
supersedes the overview's pending-audit wording for L044 only. No
larger word count, uniform count bound, entry or descent result was
derived in this audit.

## Mathlib

Full matching theorem: **not checked**. Supporting real logarithms,
geometric sums, monotonicity, valuations and period/count arithmetic:
**not checked** for exact declarations. No matching theorem, absence
from Mathlib or formal verification is asserted.
