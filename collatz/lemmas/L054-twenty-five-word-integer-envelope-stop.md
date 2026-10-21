# L054 — Twenty-five-word endpoint-product/integer-envelope stop

## Hypotheses

Consider exactly L051 (1)–(4) at r=25. Thus integer J_i>=2, H_i>=3
and a_i>=0 with a_i=2 modulo 18 define K=sum(3J_i+H_i),
L=sum(J_i+a_i), N=K+L. Positive integers d,K_0,L_0 satisfy
K=dK_0, L=dL_0, K_0>225640000. Require Lambda=N log2-K log3>0,
N<(8/5)K+1725/1034, real s_i>=540/11, h_i=log s_i,
s_0=min s_i, s_25=s_0, the seed h_0<(133/10)log N+8+log25,
and each own-index guard

\[
4J_i\log2\le h_i+\log(11/4),\qquad
H_i\log2<h_i+J_i\log(27/16).
\]

All 25 endpoints are

\[
s_{i+1}=2^{-a_i}\{G_i s_i-(12/11)(3/2)^{H_i}-1\}+23/11,
\quad G_i=(27/16)^{J_i}(3/2)^{H_i}.
\]

Independent tails, repeated periods and coincident junctions are allowed.
No integer parity, residue or valuation realization of s_i is assumed.
All logarithms are natural. Keep p=9809721694, q=6189245291.

For the branch calculation only, additionally fix

\[
K=397573379,\qquad N=630138897,\qquad L=232565518. \tag{1}
\]

Statements conditional on a full solution in this branch do not assert
its existence. The standalone integer example below satisfies only the
expressly identified aggregate constraints.

## Conclusion

The whole r=25 system implies N<14000000000. The branch (1) has
Nq-Kp=1, satisfies the primitive-scaling and aggregate count conditions,
and has 10584/10^14<Lambda<10585/10^14. Conditional on a full solution
in that branch, the retained product and cyclic split imply

\[
14<h_0<603/25=24.12,\qquad h_i>28\quad(1\le i\le24). \tag{2}
\]

The specified integer upper recurrence below then gives only

\[
K\le534432492>397573379>225640000.                 \tag{3}
\]

Thus this endpoint-product, two-segment split and forward floor-envelope
comparison supplies no count contradiction for (1): its bound exceeds
the fixed K by 136859113. Stop this specified comparison. No simultaneous
solution, actual cycle, optimality among all retained inequalities, or
r=25 exclusion is established. In particular, a failed upper bound does
not prove its attainability. The restricted exclusion remains through
twenty-four words. The universal eventual-descent gap remains open.

This is REPRODUCTION of inspected tools at a changed count, with an
informative negative outcome, not a new general cycle theorem. A separate
critical audit of this calculation has not been performed.

## Proof

### Count-independent estimates and the whole-ray ceiling

Write rho=189/100, R_m=sum_{j=0}^{m-1}rho^j. The own-index arguments
in L052 before its count-specific assembly use precisely the local
guards, endpoints, s_i>=540/11 and a_i>=2 above. Hence for every index

\[
3J_i+H_i<(14/5)(h_i+1),\qquad
h_{i+1}+1<\rho(h_i+1).
\]

Induction over 24 forward edges counts all 25 inputs and gives
K<(14/5)R_25(h_0+1). Exact geometric sums satisfy R_25<9170000
and R_24<4850000. The exponential series gives e>163/60>27/10
and (27/10)^4>25, so log25<4. Also 1725/1034<2. Substitution of
the seed and length inequality, only with positive multipliers, gives

\[
N<A\log N+B,\quad A=546385280,\quad B=534060802.
\]

For M=14000000000, certified log M<117/5 gives
M-(117/5)A-B=680523646>0. On t>=M the derivative of
t-A log t-B is 1-A/t>0. Thus N<M on the entire real domain,
and Lambda>0 together with log3/log2>3/2 gives K<2M/3.

Put epsilon=q log3-p log2. The certificate proves
0<epsilon<958/10^13, but log2-(2M/3)epsilon<0. This last fact
only diagnoses failure of that coarse z>=1 separation bound; it does
not imply Lambda<=0 or rule out a better ceiling. We proceed using
the exact branch counts, without assuming a global separation margin.

### A scalar count branch, with no height realization claim

Direct integer multiplication gives Nq-Kp=1 for (1). Take d=1,
K_0=K, L_0=L. The strict primitive threshold holds, as does
N<(8/5)K+1725/1034 and N<M. Exact outward logarithm bounds give
10584/10^14<Lambda<10585/10^14, in particular Lambda>0.

The aggregate sums and all parameter congruences alone can be realized
by J_i=2 for every i, H_i=3 and a_i=2 for 0<=i<24,
H_24=397573157 and a_24=232565420. Then
sum J_i=50, sum H_i=397573229, sum a_i=232565468;
a_24=2+18*12920301. These parameters are not asserted to satisfy
any own-index guard, seed, or endpoint. They demonstrate only that the
count case is not eliminated by its aggregate integer conditions.

### All endpoints and a branch-specific two-segment split

Assume conditionally a full solution with (1). As in L051, put
n_i=s_i-23/11>=47 and
eta_i=23/11-(12/11)(16/27)^{J_i}-(16/27)^{J_i}(2/3)^{H_i}.
Then 0<eta_i<23/11 and each exact endpoint is
n_{i+1}=G_i 2^{-a_i}(n_i+eta_i). Multiplication over all 25 indices,
including the closing endpoint, cancels the positive product of n_i.
Since prod G_i2^{-a_i}=3^K/2^N, this proves

\[
\Lambda=\sum_{i=0}^{24}\log(1+\eta_i/n_i)
 <\frac{23}{11}\sum_{i=0}^{24}\frac1{n_i}
 \le\frac{575}{11n_0}.                            \tag{4}
\]

Let lambda_*=10584/10^14 and D_0=23/11+(575/11)/lambda_*.
As Lambda>lambda_*, (4) implies s_0<D_0. Certified log D_0<27
gives h_0<27. Conversely h_0<=14 would imply
K<(14/5)9170000*15=385140000<K, impossible. Thus every h_i>=h_0>14.

If some h_j<=28, 1<=j<=24, split the cyclic sequence into the j
inputs starting at zero and the 25-j inputs starting at j. Both initial
heights are at most 28. The two geometric estimates give

\[
K<(14/5)29(R_j+R_{25-j})
 \le(14/5)29(1+R_{24})
 <393820081.2<397573379.
\]

The middle inequality follows by expanding
(rho^{j-1}-1)(rho^{24-j}-1)>=0, which yields
rho^j+rho^{25-j}<=rho+rho^{24}. All 25 input occurrences are counted
once, including repeats. Hence h_i>28 for every i!=0; this is deduced,
not imposed as a distinctness hypothesis.

Using e>163/60, define the rational numbers

\[
T=\frac{552/11}{(163/60)^{28}-23/11},\qquad
D=\frac{23}{11}+\frac{23/11}{\lambda_*-T}.
\]

The certificate checks lambda_*-T>0. The 24 nonminimum terms in (4)
have sum less than T, so
lambda_*<Lambda<(23/11)/(s_0-23/11)+T implies s_0<D.
Exact logarithm bounds give 24.11<log D<24.12. The lower bound here
is a diagnostic on this computed cap, not a lower bound on h_0.
This proves (2) with the earlier lower height bound.

### The integer envelope and its failed threshold

The lower bound h_i>14 gives s_i>e^14>(27/10)^14>10^6.
The endpoint with a_i>=2 and G_i>1 yields s_{i+1}<G_i s_i/4+23/11.
Thus log(1+x)<x for x>0 gives, with ell=log2,
alpha=log(27/16)>0 and beta=log(3/2)>0,

\[
h_{i+1}<h_i+J_i\alpha+H_i\beta-2\ell+10^{-5},      \tag{5}
\]

because the positive-shift error is at most 92/(11G_i s_i)
<92/(11*10^6)<10^-5. This justifies reusing the earlier recurrence
at the newly proved lower height 14; L053's lower height 15 is not assumed.

Let S=10^12, E=693147180559, U=1098612288669, C=1011600911679.
The certificate verifies E/S<ell, log3<U/S and log(11/4)<C/S.
Put A_*=3U-4E=523248143771 and B_*=U-E=405465108110.
Starting at v_0=24120000000000, define for i=0,...,24

\[
\widehat J_i=\left\lfloor\frac{v_i+C}{4E}\right\rfloor,\quad
\widehat H_i=\left\lfloor\frac{v_i+\widehat J_i A_*}{E}\right\rfloor,
\quad v_{i+1}=v_i+\widehat J_i A_*+\widehat H_i B_*-2E+10^7.
\]

If h_i<v_i/S, the first own-index guard gives
J_i<(v_i+C)/(4E), hence J_i<=Jhat_i. The second guard and alpha>0
then give H_i<(v_i+Jhat_i A_*)/E, hence H_i<=Hhat_i. Equation (5),
the positive upper coefficients and -2ell<-2E/S give h_{i+1}<v_{i+1}/S.
Induction from (2) proves all these bounds. The generated final upper
transition is unused; only 24 transitions bound the 25 outgoing inputs.
No upper bound on an actual a_i or parity realization is assumed.

The exact 25 values of 3Jhat_i+Hhat_i, in order, are

```text
68, 123, 226, 425, 793, 1491, 2807, 5283, 9951,
18745, 35315, 66530, 125344, 236158, 444936, 838289,
1579400, 2975712, 5606474, 10563040, 19901602,
37496200, 70645822, 133102346, 250775412.
```

Their sum is 534432492, proving (3). The full integer divisions,
numerators, denominators and two floor inequalities at every index are
stored in the certificate. This is an upper-envelope failure: neither
these extremal parameters nor a smaller allocation has been shown to
satisfy all counts and cyclic endpoints together. The product retains
closure, but the subsequent forward envelope loses the distribution of
the actual tails by replacing each a_i by its minimum 2.

### Exact evidence, scope and sources

Reproduce with
`python3 scripts/postspell-word-count/certify_twenty_five_envelope_stop.py`.
Full evidence is
`scripts/postspell-word-count/twenty-five-envelope-stop-certificate.json`.
All 30 rational checks pass; every floor inequality and the exact total
are checked. The coarse negative separation expression and the final
missed threshold are recorded as method failures, not failed certificate
checks. The complete floor records and sign table were inspected; full
exact small logarithmic-cancellation margins were inspected where compact
decimal intervals overlap. No floating-point evidence is used.

For completeness, the logarithm enclosure is L051's integrated geometric
identity. Binary-reduce t>=1 to 2^k v, 1<=v<2, and x=(v-1)/(v+1).
The first 96 terms of 2 sum x^{2j+1}/(2j+1), each rounded down to a
multiple of 2^-192, give a lower bound for log v. The rounding error is
less than 96*2^-192 and the positive integral remainder is less than
9/(4*193*3^193), by x<=1/3 and the endpoint bound for 1/(1-x^2).
For x=0 the remainder is zero and still below that positive bound.
Adding these errors gives an upper bound. Apply the same construction
to log2 and add k outward intervals. Opposite interval endpoints bound
N log2-K log3 and q log3-p log2. All term integers and remainders are
stored. This is finite rational certification, not an independent audit.

The prior assessment is
`drafts/literature/2026-10-11-twenty-five-simultaneous-feasibility.md`.
Only L051's real system/product and L052's count-independent estimates
are mathematical inputs to this diagnostic. The changed assembly and
floor comparison are needed because no inspected theorem decides r=25.
L053 is a comparison with the earlier count, not an imported r=25 verdict.

The application motivating L051 remains qualified by L041 and the
published integer-cycle inputs: Hercher, *There are no Collatz m-Cycles
with m <= 91*, JIS 26 (2023), Article 23.3.5,
[Theorem 16, pp. 10–11](https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/hercher5.pdf);
Simons–de Weger, *Theoretical and computational bounds for m-cycles of
the 3n+1-problem*, Acta Arith. 117 (2005), 51–70,
[period conventions p. 52, Corollary 2 p. 53, Lemma 12 p. 61](https://www.impan.pl/shop/en/publication/transaction/download/product/82263).
Their computational height, continued-fraction, Rhin/Crandall and other
published qualifications are unchanged. They are not applied anew to
arbitrary real junctions here; K_0>225640000 is an explicit system
hypothesis. No stronger source result or rational pair is introduced.

## Mathlib

Full matching coverage was not checked. The earlier external Lean builds
and source computations remain unverified locally; unknown availability
is not evidence of absence. The exact arithmetic certificate is Python,
not a formal proof of the simultaneous system's feasibility or infeasibility.
