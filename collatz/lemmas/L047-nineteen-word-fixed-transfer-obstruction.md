# L047 — Nineteen-word fixed-transfer bound and scalar obstruction

## Hypotheses

Let T(t)=t/2 for even positive integers and T(t)=(3t+1)/2 for
odd positive integers. O and E denote actual input parities. For
0<=i<19 let J_i>=2, H_i>=3 and a_i>=0 be integers, with a_i
congruent to 2 modulo 18. Set

\[
W_i=(OOEO)^{J_i}O^{H_i}E^{a_i},\quad
D_i=4J_i+H_i+a_i,\quad N=\sum_{i=0}^{18}D_i.
\]

Assume W_0...W_18 is actual at a positive odd integer n_0>1,
T^N(n_0)=n_0, and each junction occurrence
n_i=T^(D_0+...+D_(i-1))(n_0) is positive, odd and 20 modulo 27.
Set n_19=n_0. Every final even tail is exact. Independent tails,
repeated periods and coincident junctions are admitted. No least-root,
first-return, global-minimum or primitive-representation assumption
is imposed. These are L041's hypotheses at r=19. All logarithms are
natural. Retain the published cycle-input qualifications below.

## Conclusion

Put

\[
q=48/25,\quad R=\sum_{j=0}^{18}q^j
 =\frac{48^{19}-25^{19}}{23\,25^{18}}
 =\frac{3818157814764632968788795531169}
        {14551915228366851806640625},
\]
\[
A=(399/5)R,\qquad B=(54+6\log19)R+1311/1034.
\]

Every actual representation in the hypotheses satisfies

\[
N<A\log N+B,\qquad 338460000<N<1000000000.           \tag{1}
\]

However the scalar length N_*=370000000, strictly above even
(8/5)225640000=361024000, satisfies the first inequality in (1):

\[
A\log N_*+B>392550000>N_*.                          \tag{2}
\]

Thus this fixed nineteen-word assembled length comparison does not
contradict the entire admissible represented-length ray. Stop this
comparison. Equation (2) asserts only a scalar obstruction: it is not
a witness to the simultaneous own-index height, integer-count,
linear-form, parity, shifted-endpoint or closure conditions. No actual
cycle or feasibility of their full necessary system is established.
Other retained information may exclude nineteen words. No maximal
word-count cutoff, arbitrary-cycle exclusion or eventual descent follows.
The result awaits a separate critical audit.

## Proof

### Assemble the unchanged inputs at nineteen occurrences

Use L041's counts K=sum_i(3J_i+H_i), L=sum_i(J_i+a_i), N=K+L,
and its positive primitive-period scaling K=dK_0, L=dL_0 for an
integer d>=1. Since a_i>=2 and n_i>=47, the actual orbit is
nontrivial and all shifted heights below are positive. Cyclically
relabel to choose n_0=min_i n_i, resolving ties by any occurrence.
This selects a designated junction, not a global orbit minimum.
Set s_i=n_i+23/11, h_i=log s_i and P_i=4J_i+H_i.
L041 (6), (7) and (11) give, with r=19 throughout,

\[
h_0<(133/10)\log N+8+\log19,\quad
P_i<(15/4)h_i+3,\quad
N<(8/5)K+1311/1034.                                \tag{3}
\]

The own-index valuation bounds and exact shifted endpoint in L041
apply at every occurrence, independently of closure or the number of
words. Hence L044 (3)–(6), before its weakening to factor 2, give

\[
h_{i+1}<(48/25)h_i+32/75,\qquad
h_{i+1}+1<q(h_i+1).                                \tag{4}
\]

L046's transfer proof and separate audit check the same numerical
passage even on the enlarged real-height domain. In particular its use
here imports the transfer, not the eighteen-word infeasibility conclusion.
The exact endpoint is
s_(i+1)=2^(-a_i)[G_i s_i-(12/11)(3/2)^(H_i)-1]+23/11,
where G_i=(27/16)^(J_i)(3/2)^(H_i). The lower bound s_i>=540/11
and a_i>=2 justify s_(i+1)<G_i s_i, retaining both shifts. Each
coefficient substitution uses that same occurrence's J_i,H_i and has
positive multipliers. No sharper coefficient, seed or reciprocal-mass
bound is introduced.

Induct along eighteen edges, i=0 through 17, to obtain
h_j+1<=q^j(h_0+1) for 0<=j<=18, with equality permitted at j=0.
This covers all nineteen input occurrences, including repetitions or
coincident heights. The closing edge is still an actual hypothesis,
but is not needed for this necessary bound. Using (3),

\[
K=\sum_i(P_i-J_i)<\sum_iP_i
 <(15/4)\sum_i(h_i+1)\le(15/4)R(h_0+1).
\]

Insert the unchanged seed and length conversion in (3). Since
(8/5)(15/4)=6, this gives precisely

\[
N<(399/5)R\log N+(54+6\log19)R+1311/1034.           \tag{5}
\]

All tails remain in N through the cycle identity used by L041's
length conversion; no individual tail cap is imposed.

The source imports are Christian Hercher, *There are no Collatz
m-Cycles with m <= 91*, JIS 26 (2023), Article 23.3.5,
[Theorem 16 and complete proof, printed pp. 10–11](https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/hercher5.pdf),
and John Simons and Benne de Weger, *Theoretical and computational
bounds for m-cycles of the 3n+1-problem*, Acta Arith. 117 (2005),
51–70, [Corollary 2 and proof p. 53; Lemma 12 and proof p. 61; period conventions p. 52](https://www.impan.pl/shop/en/publication/transaction/download/product/82263).
The first two general estimates supply L041's seed and length
conversion. Corollary 2 gives the primitive odd count
K_0>M=225640000. Their applicability and positive represented-period
scaling have already been justified in L041 and L044; no source result
is reproved. Positivity of Lambda=N log2-K log3 and 3^2>2^3 yield
N>(3/2)K>=(3/2)K_0>C=338460000. The source's full local-minimum
count is never set to nineteen designated junctions. This proves
(5) and the lower bound in (1).

### Certify the missed comparison, without claiming feasibility

Exact rational evaluation of R gives

\[
250000<R<300000,\qquad A<23940000<C.                \tag{6}
\]

These strict inequalities can be checked by multiplying the displayed
positive denominator of R; the full exact comparisons are saved in
the certificate below. To bound log N_* rigorously from below, use
the exponential series. For k>=0, (4+k)!>=24*5^k, with strict
inequality for k>=2. Consequently

\[
e=\sum_{n=0}^3\frac1{n!}+\sum_{k\ge0}\frac1{(4+k)!}
 <8/3+(1/24)\sum_{k\ge0}5^{-k}=87/32<11/4.
\]

The exact integer inequality 11^19<N_*4^19 implies
e^19<(11/4)^19<N_*, so log N_*>19. Since log19>0 and
1311/1034>0, equation (6) now gives

\[
A\log N_*+B>
 [(399/5)19+54]\,250000=392550000.
\]

The excess over N_*=370000000 is strictly greater than 22550000.
Also N_*>(8/5)M>C. Since log3/log2<8/5 is an existing input,
this scalar witness lies even above (log3/log2)M; the failure is
not caused by choosing a length below that stronger primitive-count
ray start. No K,J_i,H_i,a_i,s_i or primitive counts are assigned
to N_*. It is a witness solely to the retained scalar inequality.

### What upper ceiling still follows

For F(t)=t-A log t-B on t>=C, (6) gives F'(t)=1-A/t>0.
Equation (2) shows F(N_*)<0. Thus monotonicity cannot give a
contradiction starting at C (indeed F(C)<F(N_*)<0).

The positive exponential series through degree five gives
e>163/60>27/10. The exact comparisons
27^3>19*10^3 and 27^21>10^9*10^21 imply log19<3 and
log(10^9)<21. Also 1311/1034<2. Therefore, at T=10^9,

\[
A\log T+B<21(399/5)300000+72\,300000+2
 =524340002<T.
\]

In particular F(T)>475659998>0. For all real t>=T,
F(t)>=F(T)>0, contradicting (5) if an actual represented length
were at least T. This proves the upper bound in (1). It is a
conditional length ceiling, not the required exclusion: the fixed
scalar test allows N_* between the sourced lower bound and this ceiling.

### Evidence, qualifications and route decision

The pre-invocation SPECIALIZE assessment is
`drafts/literature/2026-10-10-nineteen-word-retained-transfer.md`.
This is REPRODUCTION. The local assembly and informative negative
result make no claim of progress beyond the inspected source mathematics
or of originality. Reproduce the exact arithmetic with
`python3 scripts/postspell-word-count/certify_nineteen_transfer.py`.
All fifteen comparisons pass, with full operands and no failures in
`scripts/postspell-word-count/nineteen-transfer-certificate.json`.
The analytic induction, logarithm bounds and all-real monotonicity above
are essential; finite arithmetic alone is not a proof audit.

Preserve Attempt 021's weaker factor-2 stop and L045's height-free
witness. The fixed q=48/25 nineteen-word comparison now stops too;
it neither refutes the actual language nor limits other wordwise methods.
No simultaneous necessary-system witness or optimal cutoff is claimed.
Universal entry, unrestricted word counts/cycles, divergence and
eventual descent remain unresolved.

Inherited published inputs include x_min>301*2^50, distributed [Ro]
computations and Roosendaal communication, continued-fraction denominators
225644606 and 397573379, and the Rhin/Crandall original-proof
qualifications. Their original certificates/proofs are not independently
verified here. The inspected June 2026 Hercher correction leaves
Theorem 16 unchanged; amended Theorem 21 is not used. No external
Lean verification is asserted.

## Mathlib

Matching coverage of this nineteen-word assembly, the imported cycle
estimates and the scalar obstruction was not checked. Elementary
logarithm and finite geometric-series facts support the written proof,
but no matching Lean declaration is asserted. Unknown availability
is not evidence of absence.
