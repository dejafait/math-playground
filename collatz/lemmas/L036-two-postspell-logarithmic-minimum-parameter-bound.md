# L036 — Logarithmic restriction on the smaller postspell parameter

## Hypotheses

Use the shortcut map T(t)=t/2 for even positive integers and
T(t)=(3t+1)/2 for odd positive integers; O and E specify actual
input parities. For i=1,2 let J_i>=2, H_i>=3 and a_i>=0 be
integers, with a_i congruent to 2 modulo 18. Put

\[
W_i=(OOEO)^{J_i}O^{H_i}E^{a_i},\qquad
D_i=4J_i+H_i+a_i,\qquad N=D_1+D_2.
\]

Assume W_1W_2 is actual at a positive odd integer n>1,
with positive odd junction x=T^{D_1}(n), with n and x congruent
to 20 modulo 27, and with T^N(n)=n. Both final even tails
are exact. No least-root, first-return, distinct-junction,
primitive-period or relative parameter-growth assumption is made.
All logarithms below are natural.

## Conclusion

Write j=min(J_1,J_2) and K=3(J_1+J_2)+H_1+H_2. Then

\[
\boxed{
j<\frac{13.3}{4\log2}\log K+
  \frac{13.3\cdot0.46057+\log(46/3)}{4\log2}
 <5\log N+4.}                                           \tag{1}
\]

In particular A=5,B=4 are explicit absolute constants for
the approved necessary bound j<=A log N+B. This permits
independent unbounded H_i,a_i, unequal or equal J_i, and repetitions.
It does not bound the larger J_i or total N from above, exclude
integer closure, or settle any other cycle or divergent orbit.
Universal entry into this language and eventual descent remain open.

## Proof

### Actual boundary heights

L031's exact boundary valuation identities, valid for independent
exact final tails, give

\[
v_2(11n+23)=4J_1+2,\qquad
v_2(11x+23)=4J_2+2.
\]

For either boundary b (n or x) and its corresponding J, positivity
therefore gives 11b+23=2^{4J+2}u for a positive odd integer u.
Thus

\[
11b\ge4\cdot2^{4J}-23>3\cdot2^{4J},
\qquad
\frac1b<\frac{11}{3}2^{-4J}.                           \tag{2}
\]

The strict inequality uses 2^{4J}>=256>23, since J>=2.
It retains the additive 23 rather than ignoring it. No comparison
between the two boundary heights or their other parameters is used.

### Sourced lower bound and reciprocal upper bound

Every OOEO has three odd and one even inputs. Hence the represented
odd/even occurrence counts are

\[
K=3(J_1+J_2)+H_1+H_2,\qquad
L=J_1+J_2+a_1+a_2,\qquad N=K+L.
\]

In particular K>=18 and L>0, so 1<K<N. The cycle is positive
and nontrivial: n>1 is odd and 20 modulo 27, so it is outside
the invariant trivial shortcut cycle {1,2}. Occurrence counts
are used even if states repeat or x=n.

Import John Simons and Benne de Weger, *Theoretical and computational
bounds for m-cycles of the 3n+1 problem*, Acta Arithmetica 117
(2005), 51–70,
[Lemma 12, printed p. 61](https://www.impan.pl/shop/en/publication/transaction/download/product/82263):
for the odd/even counts of a positive nontrivial shortcut cycle,

\[
\Lambda=(K+L)\log2-K\log3
 >\exp[-13.3(0.46057+\log K)].                        \tag{3}
\]

Section 1.2, printed p. 52, explicitly permits a nonminimal period.
The inspected Lemma 12 proof uses Rhin's Proposition and the paper's
Lemma 8, including its computational cycle-height input. Those are
imported as published inputs to Lemma 12; neither the computations
nor Rhin's original proof are independently certified here. The
decimal constants in (3) are the stated theorem constants.
Our actual positive nontrivial closed orbit has precisely this
shortcut convention and these represented counts. We apply (3)
to K,N as represented, without replacing them by primitive counts.

L035's cycle application, already retaining repeated representations,
supplies

\[
0<\Lambda<\frac{23}{11}\left(\frac1n+\frac1x\right).
\]

Use (2), then J_1,J_2>=j, to obtain

\[
0<\Lambda<\frac{23}{3}
 (2^{-4J_1}+2^{-4J_2})
 \le\frac{46}{3}2^{-4j}.                              \tag{4}
\]

Both sides of (3)–(4) are positive, so taking logarithms preserves
order. Combining their strict signs gives

\[
-13.3(0.46057+\log K)<\log(46/3)-4j\log2,
\]

which, after rearranging and dividing by 4 log2>0, proves the
first inequality in (1). This is the necessary quantitative
specialization; it is not a contradiction to positive closure.

### Explicit simple constants

For t>1, log t>2(t-1)/(t+1). Indeed their difference is zero
at t=1 and has derivative (t-1)^2/[t(t+1)^2]>0 for t>1.
In particular log2>2/3. Also the exponential series gives

\[
e^3>1+3+\frac92+\frac{27}{6}+\frac{81}{24}
 =\frac{131}{8}>\frac{46}{3},
\]

so log(46/3)<3. Finally 13.3*0.46057=6.125581<7.
Consequently the coefficient and constant in the first bound obey

\[
\frac{13.3}{4\log2}<\frac{39.9}{8}<5,
\qquad
\frac{13.3\cdot0.46057+\log(46/3)}{4\log2}
 <\frac{10}{8/3}=\frac{15}{4}<4.
\]

Since 1<K<N and log N>0, these inequalities give the second
inequality in (1). They require no rounded numerical logarithms.

### Qualifications and relevance

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-07-two-postspell-logarithmic-parameter-balance.md`.
This is REPRODUCTION: the known effective lower bound is imported
by precise citation, and the proof derives only its guarded
combination with canonical boundary and reciprocal estimates.
No reproof of transcendence theory or general parity coding is needed,
and no priority or progress beyond the inspected source mathematics
is claimed. No inspected source states this exact local specialization.

Attempt 019 remains stopped: its boundary guards alone cannot
contradict integer closure. Here the height consequence of those
guards is combined with an independent sourced linear-form lower
bound. The resulting logarithmic necessary restriction narrows the
case where both J_i are large relative to log N; it still permits
unbounded asymmetry and gives no all-parameter exclusion. The separate
critical audit below found no defect in this specialization.

### Separate critical audit

The 2026-10-07 audit used the pre-invocation SPECIALIZE assessment
`drafts/literature/2026-10-07-two-postspell-logarithmic-balance-audit.md`
and read the complete proofs of L031 and L035. No change to (1),
its hypotheses or its direct mathematical inputs was needed.

For the boundary input, L031's necessity argument applies to the
already actual closed word; its converse from divisibility is not
needed here. For either word, its actual B^J endpoint y satisfies
2^H(2^a m+1)=3^H(y+1), with m odd and a>=2. Thus
v_2(y+1)=H. Since H>=3, the displayed factorization of 11y+23
in L031 has exactly two factors of 2. Its affine B^J identity
then gives v_2(11b+23)=4J+2 for that word's own starting
boundary b. This checks independent tails directly; it does not
use E^2-only transport. Positivity of b makes the odd multiplier
positive, so 11b>=4*2^(4J)-23. The gap to 3*2^(4J)
is at least 256-23=233>0. Inverting this strictly positive
height inequality proves exactly the strict reciprocal bound (2).

L036's endpoint is n, so all finite-word and closure hypotheses
of L035 match with y=n. The represented counts have K>=18
and L>=8, because each a_i>=2; in particular 1<K<N.
Both n and x are legitimate word starts even if equal. A closed
orbit containing n outside {1,2} cannot enter that invariant
trivial cycle and return to n. Also the last E before n starts
at 2n>n, while its next O goes above n, so n is a local minimum
if the source's cycle labeling is started at such a boundary.
No global-minimum or least-nonconvergent-root assumption is used.

The precise published Lemma 12 and section 1.2 convention cited
above match this positive nontrivial shortcut cycle and permit
the represented nonminimal period. L035 independently checks
the repeated-period upper bound. As a further check on the lower
bound's scaling, if N=rN_0, K=rK_0 and Lambda=r Lambda_0
for a primitive period, its lower estimate gives
r Lambda_0>r exp[-13.3(0.46057+log K_0)]
>=exp[-13.3(0.46057+log(rK_0))] for r>=1.
Thus repetition cannot invalidate (3), including when x=n.
This checks applicability, not the source's computational inputs
or Rhin's original proof, which remain imported by citation.

In (4) each reciprocal inequality is strict; replacing the two
exponentials by twice the larger one is non-strict and retains
the preceding strict sign, including J_1=J_2. Combining (3)
and (4) and taking natural logarithms is legitimate because
their endpoints are positive. Rearranging gives
4j log2<13.3(0.46057+log K)+log(46/3); division by
the positive 4 log2 gives the direction in (1).
The derivative proving log2>2/3 is positive for every t>1.
The exact exponential-series sum is 131/8, exceeding 46/3
by 25/24, and 13.3*0.46057=6.125581. Therefore the
coefficient is less than 39.9/8<5 and the constant less than
15/4<4. Since log K>0 and K<N, their use in (1) preserves
strictness. No numerical approximation or finite screen is needed.

The audit found no mathematical defect or stronger conclusion.
Attempt 019's guard-only obstruction and the count mismatch in
history 069 remain intact. This validates a local REPRODUCTION;
it is neither an originality claim nor a complete candidate.
The working record is
`drafts/2026-10-07-two-postspell-logarithmic-balance-audit.md`.

## Mathlib

Full matching parameter restriction, Simons–de Weger's Lemma 12,
and its transcendence/computational inputs: **not checked**.
Supporting valuation, logarithm monotonicity and exponential-series
declarations: **not checked**. No matching theorem or absence from
Mathlib is asserted; the elementary estimates and cited theorem
above are the informal evidence.
