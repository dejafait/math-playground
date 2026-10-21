# L048 — Nineteen-word exclusion using the exact logarithmic transfer

## Hypotheses

Let T(t)=t/2 for even positive integers and T(t)=(3t+1)/2 for odd
positive integers. O and E specify actual input parities. For 0<=i<19
let J_i>=2,H_i>=3,a_i>=0 be integers, with a_i congruent to 2 modulo
18. Put W_i=(OOEO)^{J_i}O^{H_i}E^{a_i}, D_i=4J_i+H_i+a_i and
N=sum_i D_i. Assume W_0...W_18 is actual at a positive odd integer
n_0>1, T^N(n_0)=n_0, and every junction occurrence
n_i=T^(D_0+...+D_(i-1))(n_0) is positive, odd and 20 modulo 27.
Set n_19=n_0. Every final even tail is exact. Independent tails,
repeated periods and coincident junctions are allowed. There is no
least-root, first-return, primitive-representation, global-minimum or
relative-height assumption. These are L041's hypotheses at r=19.
All logarithms are natural. Retain the published qualifications below.

## Conclusion

No such nineteen-word closed concatenation exists, subject to the
published cycle inputs and their computational qualifications.
The exact logarithmic transfer gives the necessary bound

\[
N<16047780\log N+13695003.                         \tag{1}
\]

It is incompatible with every real N>=338460000, whereas the imported
primitive odd-count threshold forces N>338460000. Combined with the
earlier exclusions this extends the restricted language exclusion through
nineteen words. The separate critical audit below found no defect within
the stated qualifications. It supplies no universal entry, unrestricted word-count or cycle
exclusion, divergence control or universal eventual descent. No complete
Collatz candidate or optimal word-count cutoff is asserted.

## Proof

### Applicability and the unchanged inputs

L041 gives K=sum_i(3J_i+H_i), L=sum_i(J_i+a_i), N=K+L and positive
primitive scaling K=dK_0,L=dL_0 with integer d>=1. Here a_i>=2 and
n_i>=47. The closed orbit is therefore nontrivial, outside the invariant
shortcut cycle {1,2}. Counts refer to input times, including repetitions.
Cyclically relabel to choose n_0=min_i n_i, with ties resolved by any
occurrence, without identifying it with the global orbit minimum. Set
s_i=n_i+23/11, h_i=log s_i>0, and P_i=4J_i+H_i. L041 (6), (7), (11)
give precisely

\[
h_0<(133/10)\log N+8+\log19,\quad
P_i<(15/4)h_i+3,\quad N<(8/5)K+1311/1034.           \tag{2}
\]

Write delta=log3/log2, c_J=log(11/4), and

\[
q=3\delta^2/4,\qquad b=\delta(3\delta-4)c_J/4.
\]

L044 (5), before relaxing either term, gives at each occurrence

\[
h_{i+1}<q h_i+b.                                   \tag{3}
\]

Its applicability here is wordwise, not an extension by citation of
L044's thirteen-word conclusion. Indeed L041 supplies each occurrence's
own bounds 4J_i log2<=h_i+c_J and
H_i log2<h_i+J_i log(27/16). Its exact endpoint retains both shifts:
s_(i+1)=2^(-a_i)[G_i s_i-(12/11)(3/2)^{H_i}-1]+23/11,
where G_i=(27/16)^{J_i}(3/2)^{H_i}. Since s_i>=540/11 and a_i>=2,
it gives s_(i+1)<G_i s_i/4+23/11<G_i s_i. L046's transfer passage
checks the same implication even under relaxed real-height guards,
independently of the word count. The positive factors delta-1 and
log(27/16) justify both own-index substitutions in L044 (4)–(5).
Thus (3) uses no other occurrence's parameters, tail cap, mass estimate
or new cycle theorem. Moreover delta>3/2 from 3^2>2^3, so q>1,b>0.

The precise source imports behind (2) are Christian Hercher, *There are
no Collatz m-Cycles with m <= 91*, JIS 26 (2023), Article 23.3.5,
[Theorem 16 and complete proof, printed pp. 10–11](https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/hercher5.pdf),
and John Simons and Benne de Weger, *Theoretical and computational
bounds for m-cycles of the 3n+1-problem*, Acta Arith. 117 (2005), 51–70,
[Lemma 12 and complete proof p. 61; period conventions p. 52](https://www.impan.pl/shop/en/publication/transaction/download/product/82263).
L041 already justifies their positive integer-cycle applicability and
represented-period scaling. No transcendence or general cycle estimate
is reproved here. The inspected June 2026 Hercher correction leaves
Theorem 16 unchanged; amended Theorem 21 is not used.

Import from Simons–de Weger, the same published version,
[Corollary 2 and complete proof, printed p. 53](https://www.impan.pl/shop/en/publication/transaction/download/product/82263),
the primitive odd count K_0>M=225640000. This applies to the nontrivial
primitive positive cycle just identified. L041's positive linear form
Lambda=N log2-K log3 and delta>3/2 imply

\[
N>\delta K>(3/2)K>=(3/2)K_0>C=338460000.             \tag{4}
\]

No full local-minimum count is replaced by nineteen selected junctions.

### Assemble both exact transfer terms

For x>1 define S(x)=sum_(j=0)^18 x^j and
U(x)=sum_(j=0)^18 sum_(k=0)^(j-1) x^k, where the inner sum is zero
at j=0. Finite geometric summation gives U(x)=(S(x)-19)/(x-1).
Induction along the eighteen edges i=0,...,17 gives

\[
h_j\le q^j h_0+b\sum_{k=0}^{j-1}q^k\quad(0\le j\le18).
\]

At j=0 this is equality; for each positive j it follows by multiplying
the preceding bound by q>0 and adding b in (3). All nineteen outgoing
word inputs are covered. Repeated or coincident heights do not merge
these occurrences. The closing edge remains an actual hypothesis,
although it is not needed to obtain this necessary upper bound.
Consequently sum_j h_j<=S(q)h_0+bU(q). From (2),

\[
K=\sum_i(P_i-J_i)<\sum_iP_i
 <(15/4)[S(q)h_0+bU(q)]+57.
\]

Multiply by 8/5 and insert the unchanged seed and length conversion:

\[
N<(399/5)S(q)\log N+6(8+\log19)S(q)
       +6bU(q)+456/5+1311/1034.                    \tag{5}
\]

This retains the exact coefficient and additive transfer term together.
No shift of heights, sharper seed or prefix optimization has been used.
All tails remain in N through the cycle identity behind (2).

### Certified rational enclosures

For t>1 set x=(t-1)/(t+1), so 0<x<1. Integration of the finite
geometric identity for 1/(1-u^2) from 0 to x gives

\[
\log t=2\sum_{k=0}^{m-1}\frac{x^{2k+1}}{2k+1}
       +2\int_0^x\frac{u^{2m}}{1-u^2}\,du.
\]

The integral is positive and is strictly less than
x^(2m+1)/[(2m+1)(1-x^2)], because the denominator bound is strict
for 0<u<x. Thus the finite sum and that rational remainder bound give
rigorous lower and upper enclosures, with no infinite-sum interchange.
At m=12 and t=2,3,11/4 exact rational evaluation yields

\[
\log2>6931/10000,\quad \log3<10987/10000,\quad c_J<41/40.
\]

The complete rational sums and remainders are saved in the certificate
specified below. Cross multiplication gives
delta<10987/6931<793/500. Since delta>3/2, both delta and
3delta-4 are positive and increasing in this range. Therefore

\[
q<\frac{3}{4}(793/500)^2
 =1886547/1000000<\widehat q=189/100,
\]
\[
b<(793/500)(3(793/500)-4)(41/40)/4
 =12322427/40000000<\widehat b=31/100.               \tag{6}
\]

S and U are polynomials with nonnegative coefficients. Hence
S(q)<=S(\widehat q) and bU(q)<\widehat b U(\widehat q).
The complete geometric value is

\[
\widehat S=S(\widehat q)
 =\frac{189^{19}-100^{19}}{89\,100^{18}}
 =\frac{201086004979505972137061961346282731948781}
        {1000000000000000000000000000000000000}<201100.
\]

Also U(\widehat q)=(\widehat S-19)/(89/100), whence

\[
6\widehat b U(\widehat q)
 <\frac{186}{89}\widehat S<\frac{21}{10}\widehat S;
\]

the last comparison is 1860<1869. The positive exponential series gives
e>sum_(j=0)^5 1/j!=163/60>27/10. The integer inequalities
27^3=19683>19000 and
27^20=42391158275216203514294433201
>C*10^20=33846000000000000000000000000 therefore prove
log19<3 and log C<20. Finally
456/5+1311/1034=478059/5170<93.

Since log N>0, all substituted multipliers in (5) are positive.
Equations (5)–(6) consequently give

\[
N<(399/5)201100\log N+(66+21/10)201100+93
  =16047780\log N+13695003,
\]

which is (1). Each enclosure is in the direction required for an upper
bound; in particular the additive geometric contribution is not omitted.

### Contradiction on the entire required real ray

Put A=16047780, B=13695003 and F(t)=t-A log t-B for t>=C.
Then A<C implies F'(t)=1-A/t>0 on this whole ray. Since log C<20,

\[
F(C)>C-20A-B=338460000-334650603=3809397>0.
\]

Thus F(t)>=F(C)>0 for every real t>=C, contradicting (1) and (4).
This is an all-real argument, not a finite length or parameter screen.
It proves the restricted exclusion with the stated published inputs.

### Evidence, qualifications and bounded decision

The pre-invocation SPECIALIZE assessment is
`drafts/literature/2026-10-10-nineteen-exact-logarithmic-transfer.md`.
This is REPRODUCTION: an elementary local assembly of inspected inputs,
without an originality claim or progress beyond the checked source
mathematics. Rational enclosures are proved here because their certified
constants are necessary to decide this precise threshold comparison;
general source theorems are imported rather than reproved.

Reproduce with
`python3 scripts/postspell-word-count/certify_nineteen_exact_transfer.py`.
All nineteen exact comparisons pass, with full sums, logarithm remainder
enclosures, operands, actual/required bounds and no failures in
`scripts/postspell-word-count/nineteen-exact-transfer-certificate.json`.
Every load-bearing logarithm enclosure and comparison was inspected
completely. The finite checks support the arithmetic; the analytic proof
above supplies applicability, induction and all-real monotonicity. The
separate critical audit is recorded below.

The count-ray test succeeds. L047's fixed 48/25 scalar obstruction and
Attempts 021/022 remain valid for their weaker comparisons; neither
asserted a cycle or simultaneous feasibility. This changed transfer does
not refute those recorded failures. No larger word count was tested.
Universal entry, unrestricted counts/cycles, divergence and eventual
descent remain unresolved.

Inherited source qualifications include the published height
x_min>301*2^50, distributed [Ro] computations and Roosendaal communication,
continued-fraction denominators 225644606 and 397573379, and the
Rhin/Crandall original-proof qualifications. Their original certificates
and proofs are not independently certified here. No external Lean build
is asserted to verify this exclusion. This is not a complete Collatz
candidate; the audit below does not independently certify those imports.

### Separate critical audit — 2026-10-10

The pre-invocation SPECIALIZE assessment is
`drafts/literature/2026-10-10-nineteen-exact-transfer-critical-audit.md`.
Verdict: **no defect found within the stated actual-word hypotheses and
published qualifications**. This REPRODUCTION audit verifies the existing
argument; it produces neither a stronger theorem nor a repaired error.
L041's relevant proof and prior audit, L044's exact coefficient passage,
L046's count-independent applicability passage, the complete proof above
and its complete certificate generator were inspected. Primary coverage
is reused at the precise theorem citations above.

For the source bridge, each word has 3J_i+H_i odd inputs and J_i+a_i
even inputs. The half-open word intervals partition the represented
period, including coincident state values at different times. If p is
the least return time, division N=dp+s with 0<=s<p gives
T^s(n_0)=n_0, forcing s=0. Thus K=dK_0,L=dL_0 and the full odd-input
reciprocal mass also scales by d>=1. The cycle is nontrivial because
n_0>=47 and {1,2} is invariant. Hercher's cited Theorem 16 scales to
0<Lambda<S_mass/3. The cited Lemma 12 applied primitively gives
Lambda>e^(-6.125581)d^(143/10)K^(-133/10), which implies the weaker
represented lower bound used here. There is no assumption that the
source's full minimum count equals nineteen.

L041's mass bound is S_mass<(69/11)sum_i 1/n_i. At the smallest
designated junction n_0 it gives n_0<(437/11)e^(6.125581)K^(133/10).
The shift from log n_0 to h_0 costs less than 23/517<1/20;
6.125581+log(23/11)+1/20<25/4+1+1/20<8.
Consequently the first bound in (2) follows with precisely log19.
The seed uses a smallest designated junction, not the global minimum.
The same mass bound gives Lambda<437/517. With log2>2/3 and
delta<8/5 it gives N<(8/5)K+1311/1034; all final tails remain in N.
The published Corollary 2 applies to this nontrivial primitive positive
cycle and gives K_0>225640000. Since delta>3/2, (4) holds strictly
regardless of the repeat factor.

At each word let y=T^(4J_i)(n_i). Actuality and the odd endpoint give
v_2(y+1)=H_i. Since H_i>=3, v_2(11y+23)=2, and the exact B^J identity
then gives v_2(11n_i+23)=4J_i+2. These yield that same occurrence's
two logarithmic bounds in the applicability passage. Substituting them
with log2>2/3, log27<4 and c_J<4/3 gives the unchanged
P_i<(15/4)h_i+3. No selected small junction's parameters are applied
at another index.

The positive exact endpoint is G_i s_i-(12/11)(3/2)^(H_i)-1 before
the final tail. Since a_i>=2, dividing by 2^a_i and adding 23/11 gives
s_(i+1)<G_i s_i/4+23/11<G_i s_i, using G_i s_i>=540/11.
Both negative endpoint terms and the positive shift have therefore
been accounted for. Write alpha=log(27/16)>0. Multiplication of
H_i log2<h_i+J_i alpha by delta-1>0 gives
log G_i<(delta-1)h_i+delta J_i alpha. Substitution of
4J_i log2<=h_i+c_J has positive multiplier delta alpha, giving
h_(i+1)<[delta+delta(3delta-4)/4]h_i+b=q h_i+b.
This verifies (3) without extending a thirteen-word conclusion or
assuming a bound on relative heights or tail lengths.

Iterating (3) along indices 0 through 17 gives the nineteen bounds
used in the proof. Summing the additive terms explicitly counts
q^k exactly 18-k times for 0<=k<=17, so
U(q)=sum_(k=0)^17(18-k)q^k and (q-1)U(q)=S(q)-19.
The positive bU(q) contribution is essential and is retained.
K=sum_i(P_i-J_i)<(15/4)sum_i h_i+57, and multiplying by 8/5
gives the height-sum factor 6 and constant 456/5. Substituting the
seed gives coefficient 6*(133/10)=399/5, verifying every term of
(5). The closing edge is omitted only from a necessary upper estimate;
closure is still used for the cycle inputs. Repeated periods and ties
do not reduce the number of occurrences being summed.

For the logarithm enclosures, the finite identity
1/(1-u^2)=sum_(k=0)^(m-1)u^(2k)+u^(2m)/(1-u^2)
integrates to the displayed formula because
log((1+x)/(1-x))=2 integral_0^x du/(1-u^2). The denominator bound
on 0<u<x is strict, so the full remainder is strictly between zero
and 2x^(2m+1)/((2m+1)(1-x^2)). At m=12 the three full rational
enclosures were independently recomputed and compared with the saved
values. They justify log2>6931/10000, log3<10987/10000 and c_J<41/40.
Thus delta<793/500, q<1886547/1000000<189/100 and
b<12322427/40000000<31/100. Positivity and monotonicity of the
factors in b follow from delta>3/2, so the directions are valid.

The independent arithmetic audit iterates the unit homogeneous and
unit additive responses through eighteen edges and sums the nineteen
input states. It reproduces exactly both saved S and U, independently
of their closed forms. In particular S<201100 and
0<6*(31/100)U<(186/89)S<(21/10)S. The separately recomputed positive
exponential partial sum is 163/60>27/10; cubing and taking its
twentieth power certify log19<3 and log C<20. Finally
456/5+1311/1034=478059/5170<93. These checks give precisely
A=16047780 and B=13695003 in (1), with no missing additive term.
Since A<C, F'(t)=1-A/t>0 for every real t>=C, and
F(C)>C-20A-B=3809397. This excludes the entire necessary ray,
not merely its first integer or a finite parameter screen.

The original nineteen-check certificate regenerated byte for byte.
Run `python3 scripts/postspell-word-count/audit_nineteen_exact_transfer.py`
for the independent audit: all 87 exact checks pass, with no failures,
in `scripts/postspell-word-count/nineteen-exact-transfer-audit-certificate.json`.
The script recomputes all logarithm enclosures, the geometric and
additive sums, coefficient and constant bounds, exponential comparisons,
derivative guard and ray margin; it also cross-multiplies every original
comparison instead of trusting stored pass flags. Full selected rational
values and the complete original comparisons were inspected. Arithmetic
checks support the proof above; they do not certify source computations
or replace the all-real argument.

No mathematical argument or direct dependency changed. L047 and
Attempts 021/022 remain weaker-comparison stops, not feasibility claims.
No larger count or optimality test was performed. Published
computation/Rhin/Crandall qualifications remain unchanged, as do unknown
matching Mathlib coverage and the gaps of universal entry, unrestricted
counts/cycles, divergence and eventual descent.

## Mathlib

Full matching coverage of the nineteen-word exclusion and imported cycle
estimates is **not checked**. Supporting finite geometric sums,
logarithms, integral remainder and monotonicity facts are used in the
written proof; exact Mathlib declarations have not been checked. Unknown
availability is not evidence of absence, and no formal verification is
claimed.
