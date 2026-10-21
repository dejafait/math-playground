# L037 — Joint logarithmic restriction at one postspell boundary

## Hypotheses

Use the shortcut map T(t)=t/2 for even positive integers and
T(t)=(3t+1)/2 for odd positive integers. O and E denote actual
input parities. For i=1,2 let J_i>=2, H_i>=3 and a_i>=0 be
integers, with a_i congruent to 2 modulo 18. Put

\[
W_i=(OOEO)^{J_i}O^{H_i}E^{a_i},\qquad
D_i=4J_i+H_i+a_i,\qquad N=D_1+D_2.
\]

Assume W_1W_2 is actual at a positive odd integer n>1, with
positive odd junction x=T^{D_1}(n), both n,x congruent to 20
modulo 27, and T^N(n)=n. Both final even tails are exact.
There is no least-root, primitive-period, first-return,
distinct-junction or relative-growth assumption. Repeated periods,
including x=n, are allowed. All logarithms are natural.

## Conclusion

Choose i=1 if n<=x and i=2 otherwise. Then

\[
\boxed{4J_i+H_i<50\log N+33.}                         \tag{1}
\]

Thus A=50,B=33 are explicit absolute constants for the approved
same-index bound. This controls both parameters of the word at
the smaller designated junction, not independently selected minima.
The other word, the independent tails and N remain unbounded.
This is a necessary conditional restriction, not an exclusion of
integer closure or a resolution of universal eventual descent.

## Proof

### Sourced boundary-size estimate

Put b=min(n,x), and retain J=J_i,H=H_i for the index just chosen.
Define the represented occurrence counts

\[
K=3(J_1+J_2)+H_1+H_2,\qquad
L=J_1+J_2+a_1+a_2,\qquad N=K+L.
\]

There are three odd and one even inputs in every OOEO. Since
a_i>=2, we have K>=18,L>=8 and 1<K<N. The positive closed
orbit is nontrivial: it contains the odd residue-20 state n outside
the invariant shortcut cycle {1,2}, which it therefore cannot enter.

Reuse the sourced lower estimate and its applicability check in L036:
John Simons and Benne de Weger, *Theoretical and computational bounds
for m-cycles of the 3n+1-problem*, Acta Arithmetica 117 (2005),
51–70, [Lemma 12, printed p. 61](https://www.impan.pl/shop/en/publication/transaction/download/product/82263),
with the nonminimal-period conventions of section 1.2, printed p. 52.
For our represented counts, putting c=13.3*0.46057=6.125581,

\[
\Lambda=N\log2-K\log3>e^{-c}K^{-13.3}.
\]

The source's Rhin input and computational inputs remain imported
by this precise citation, not independently certified. L036 already
checks this actual nontrivial cycle scope and repetition; no reproof
of the general lower theorem is needed here. L035's cycle application
has exactly our actual-word and closure hypotheses and gives

\[
0<\Lambda<\frac{23}{11}\left(\frac1n+\frac1x\right)
\le\frac{46}{11b}.
\]

Consequently

\[
b<\frac{46}{11}e^cK^{13.3},\qquad
\log b<13.3\log K+c+\log(46/11).                    \tag{2}
\]

This selects a designated junction by size without identifying it
with the global cycle minimum or replacing the full minimum count
by two. No distinctness of the two junctions is used.

### Both parameters at that same boundary

Let y be the actual state after B^J from b, where B=OOEO.
For i=2 this is the corresponding suffix of the represented orbit.
L031's exact boundary and terminal valuations and its equation (4)
give

\[
11b+23=2^{4J+2}u\quad(u\text{ positive odd}),\qquad
v_2(y+1)=H,\qquad
y=(27/16)^J(b+23/11)-23/11.
\]

These statements retain the independent exact tail of this word.
In particular the terminal identity
2^H(2^{a_i}m+1)=3^H(y+1), with m its odd final endpoint,
gives the valuation because 2^{a_i}m+1 is odd. The state y
is a terminal-subrun start, not assumed to be a local minimum.
We use the actual finite-prefix identities, not source estimates
requiring such a minimum.

Put s=b+23/11. Positivity of u gives

\[
4J\log2\le\log s+\log(11/4).                       \tag{3}
\]

Also y+1 is a positive integer divisible by 2^H, so

\[
2^H\le y+1=(27/16)^Js-12/11<(27/16)^Js.
\]

Taking logarithms and adding 4J log2 yields
(4J+H)log2<J log27+log s. Substitute (3), with all
divisors and coefficients positive, to obtain

\[
4J+H<\left(\frac{\log27}{4(\log2)^2}
                  +\frac1{\log2}\right)\log s
       +\frac{\log27}{4(\log2)^2}\log(11/4).          \tag{4}
\]

Every parameter and height here belongs to the chosen word.
There is no comparison with the other word's J,H or intermediate
height, and neither a_i nor a relative-growth hypothesis enters.

### Explicit constants without rounded logarithms

Since b is positive, odd and 20 modulo 27, b>=47. The elementary
inequality log(1+t)<t for t>0 follows by differentiating
t-log(1+t), whose derivative is t/(1+t)>0. Thus (2) gives

\[
\log s=\log b+\log(1+23/(11b))
 <13.3\log K+c+\log(46/11)+1/20,
\]

where 23/(11b)<=23/517<1/20. The positive exponential
series terms through degree four give

\[
e^{3/2}>1+\frac32+\frac98+\frac9{16}+\frac{27}{128}
 =\frac{563}{128}>\frac{46}{11}.
\]

Hence log(46/11)<3/2. Since c<25/4, the constant in the
last logarithmic estimate is less than
25/4+3/2+1/20=39/5<8. Therefore

\[
0<\log s<13.3\log K+8.                              \tag{5}
\]

Reuse L036's elementary log2>2/3 estimate. The positive series
terms through degree three also give

\[
e^{4/3}>1+\frac43+\frac89+\frac{32}{81}
 =\frac{293}{81}>3,
\]

so log3<4/3 and log27=3log3<4. It follows that

\[
\frac{\log27}{4(\log2)^2}<\frac94,\qquad
\frac1{\log2}<\frac32,\qquad
0<\log(11/4)<\log3<\frac43.
\]

Apply these strict bounds to (4), using log s>0 and (5):

\[
4J+H<\frac{15}{4}(13.3\log K+8)+3
 =\frac{399}{8}\log K+33<50\log N+33.
\]

The last strict inequality uses 1<K<N and 399/8<50.
This proves (1) with exact rational comparisons; no numerical
screen or approximate logarithm establishes the bound.

### Qualifications and relevance

The pre-invocation SPECIALIZE assessment is
`drafts/literature/2026-10-07-two-postspell-joint-odd-parameter-bound.md`.
This is REPRODUCTION: a local specialization of known effective
cycle estimates and canonical finite-word identities. The new local
combination, rather than transcendence theory or parity coding,
is the work needed for the exact same-index target. No progress
beyond the mathematics of the sources checked or originality is
claimed. The separate critical audit below found no defect.

Attempt 019's guard-only stop remains valid. The present bound
combines boundary heights with an independent sourced lower estimate;
it does not assert that guards alone obstruct closure. History 069's
minimum-count mismatch is avoided by using the two-boundary reciprocal
upper bound, not a theorem with the full minimum count set to two.
The estimate may help organize asymmetric closure cases but does not
bound the other word or N above. Positive integer closure exclusion,
entry, other cycles, divergent orbits and eventual descent remain open.

### Separate critical audit

The 2026-10-07 audit used the pre-invocation SPECIALIZE assessment
`drafts/literature/2026-10-07-two-postspell-joint-parameter-audit.md`.
It read the complete L037 and L036 proofs, L031's actual-word identities
and general-tail valuation proof, and L035's finite mass proof and cycle
application. The statement, constants and direct mathematical inputs
are unchanged. The working record is
`drafts/2026-10-07-two-postspell-joint-parameter-audit.md`.

For i=1, the selected word starts at n; for i=2 it starts at x and
ends at n within the given actual representation. In either case its
positive odd endpoint m and a_i>=2 make 2^{a_i}m+1 odd. L031's
identity 2^H(2^{a_i}m+1)=3^H(y+1) therefore gives exactly
v_2(y+1)=H, independently of the value of this tail or the other
tail. Writing y+1=2^H v with v positive odd gives
11y+23=4(11*2^{H-2}v+3), of valuation exactly 2 because H>=3.
The affine identity 16^J(11y+23)=27^J(11b+23) then gives
v_2(11b+23)=4J+2. Its positive odd multiplier u is at least 1.
This necessity argument does not require L031's converse from
divisibility, E^2-only transport, or a least-root assumption.

Both designated junctions are positive odd integers 20 modulo 27.
Writing either as 20+27t, positivity forces t>=0 and oddness forces
t odd, so it is at least 47. Taking b=min(n,x) once selects the
J,H used in every subsequent height inequality. If x=n, the prescribed
choice i=1 is valid and the reciprocal comparison is an equality;
its preceding strict bound remains strict. The terminal y is an
actual subrun start. No source local-minimum chaining is applied to y.

Actual closure matches L035's additional endpoint hypothesis. The
represented counts satisfy K>=18,L>=8 and N=K+L, hence 1<K<N.
The closed orbit containing n outside {1,2} cannot enter that invariant
trivial cycle and return to n. If a source labeling begins at a local
minimum, the final incoming E starts at 2n>n and the outgoing O sends
n to (3n+1)/2>n, so n is such a minimum. No global-minimum assumption
is used. The precisely cited Simons–de Weger Lemma 12 and section 1.2
convention apply to these represented counts. Reusing inspected source
coverage checks applicability, not Rhin's original proof or the source
computations, which remain imported.

Repetition also checks directly: if N=rN_0 and K=rK_0 for a primitive
period, Lambda=r Lambda_0. The published primitive lower estimate yields
r Lambda_0>r e^{-c}K_0^{-13.3}>=e^{-c}(rK_0)^{-13.3}
for r>=1. L035's occurrence-mass argument supplies the upper estimate
with the same represented counts. Thus both bounds used in (2) hold
when periods repeat, including x=n. From
e^{-c}K^{-13.3}<Lambda<46/(11b), multiplication by the positive
b e^c K^{13.3} gives exactly the strict upper bound for b in (2).
No estimate for the global minimum or full minimum count is substituted.

To check the joint algebra, 11s=11b+23>=4*16^J gives (3).
The terminal height identity is y+1=(27/16)^J s-12/11, so
H log2<J(log27-4log2)+log s. Adding 4J log2 gives
(4J+H)log2<J log27+log s. Substitute the upper bound for J
from (3), then divide by log2>0: this is precisely (4), including
the coefficient of log(11/4). The negative offset makes the terminal
height bound strict; the positive offset is retained inside s.
All multipliers used in the substitution are positive.

Every constant comparison can be checked rationally. The exact value
of c is 6125581/1000000<25/4, and
1/20-23/517=57/10340>0. The exponential-series sums are
563/128 and 293/81; their differences from 46/11 and 3 are
305/1408 and 50/81 respectively. Positive omitted terms give the
strict logarithmic bounds used in the proof. Also
25/4+3/2+1/20=39/5<8. L036's derivative proof gives log2>2/3.
Since s>=47+23/11>1 and 11/4>1, both logarithms multiplying
the coefficient bounds in (4) are positive. Therefore replacing
those coefficients by 9/4 and 3/2 preserves the upper direction,
and (9/4)log(11/4)<3. Finally
(15/4)(133/10)=399/8<50 and (15/4)*8+3=33.
The passage from (399/8)log K+33 to 50 log N+33 is strict
because 1<K<N. Thus all signs and both advertised constants survive.

The audit found no mathematical defect, repair or stronger conclusion.
It verifies this local REPRODUCTION, without an originality claim or
progress beyond the checked source mathematics. Attempt 019's guard-only
stop and the full-minimum-count mismatch remain applicable. The bound
does not control the other word, the independent tails or N above,
and is not a complete candidate for Collatz.

## Mathlib

Full matching same-index restriction, Simons–de Weger's Lemma 12,
its transcendence/computational inputs and the imported cycle-mass
theorem: **not checked**. Supporting valuation, logarithm and
exponential-series declarations: **not checked**. No matching theorem
or Mathlib absence is asserted. The cited inputs and elementary
specialization above are the informal evidence.
