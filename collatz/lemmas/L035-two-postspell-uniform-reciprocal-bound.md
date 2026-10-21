# L035 — Uniform odd-occurrence reciprocal mass for two postspell words

## Hypotheses

Use the shortcut map T(u)=u/2 for even positive integers and
T(u)=(3u+1)/2 for odd positive integers. O and E denote actual
input parities, not merely formal affine branches. For i=1,2 let
J_i>=2, H_i>=3, a_i>=0 be integers with a_i congruent to 2 modulo 18.
Put W_i=(OOEO)^(J_i) O^(H_i) E^(a_i),
D_i=4J_i+H_i+a_i, and N=D_1+D_2.

Suppose W_1 W_2 is actual at a positive odd integer n>1. Its junction
x=T^(D_1)(n) and endpoint y=T^N(n) are positive and odd, and n,x,y
are congruent to 20 modulo 27. Both final even tails are exact.
No closure, least-root, first-return, distinct-junction or primitive-period
assumption is imposed for the finite-word bound. Define

\[
S=\sum_{\substack{0\le t<N\\ T^t(n)\ \mathrm{odd}}}
       \frac1{T^t(n)}.
\]

This counts input occurrences by time, including repetitions. The
cycle application below additionally assumes y=n.

## Conclusion

Writing q=16/27, the finite-word bound is

\[
S<\frac{69-36q^{J_1}}{11n}
  +\frac{69-36q^{J_2}}{11x}
 <\boxed{\frac{69}{11}\left(\frac1n+\frac1x\right)}.       \tag{1}
\]

Thus C=69/11 is parameter-independent; the final-tail lengths and
terminal odd-run lengths do not enter this constant. No sharpness
claim is made.

Under actual closure put

\[
K=3(J_1+J_2)+H_1+H_2,\quad
L=J_1+J_2+a_1+a_2,\quad N=K+L,\quad
\delta=\frac{\log3}{\log2}.
\]

Hercher's Theorem 16 specializes to

\[
0<\frac{N}{K}-\delta
 <\frac{23}{11K\log2}\left(\frac1n+\frac1x\right),       \tag{2}
\]

or equivalently

\[
0<N\log2-K\log3
 <\frac{23}{11}\left(\frac1n+\frac1x\right).             \tag{3}
\]

These are necessary restrictions, including for repeated representations.
They give neither an integer-closure exclusion nor a bound on all
parameters. Universal entry into this language, other cycles, divergence
and universal eventual descent remain unresolved.

## Proof

### Imported coverage and the finite-word specialization

The pre-invocation SPECIALIZE assessment is
`drafts/literature/2026-10-07-two-postspell-reciprocal-sum.md`.
The following argument combines the inspected affine identities and
finite odd-run estimate; it is REPRODUCTION, without a priority claim.
General parity coding and general cycle product inequalities are not
reproved. The actual-word hypotheses provide every required parity.

Consider either single word at its start b (b=n or b=x), and let
r_j=T^(4j)(b), 0<=j<=J, be the starts and endpoint of its OOEO portion.
L020's actual-prefix identity, applied also to each initial group of
blocks, gives

\[
r_j=\left(\frac{27}{16}\right)^j
          \left(b+\frac{23}{11}\right)-\frac{23}{11}
     \ge\left(\frac{27}{16}\right)^j b>0.                \tag{4}
\]

Here j=0 is the empty group. For j=1 the identity is exactly the
single-block identity 16r_1=27b+23 stated in L020's proof; repeated
application proves (4) for every j. The positive offset is retained:
the difference from the lower bound in (4) is
(23/11)((27/16)^j-1), which is nonnegative.

In block j the states at its four input times, relative to r_j, are

\[
r_j,\qquad \frac{3r_j+1}{2},\qquad
\frac{9r_j+5}{4},\qquad \frac{9r_j+5}{8}.
\]

Their parities are respectively O,O,E,O by actuality. Its odd-input
reciprocal contribution is therefore exactly

\[
\frac1{r_j}+\frac2{3r_j+1}+\frac8{9r_j+5}
 \le\frac{1+2/3+8/9}{r_j}
 =\frac{23}{9r_j}.                                    \tag{5}
\]

This bounds all three odd inputs, including the input after the isolated
E. It does not replace the word by its block endpoints. Summing (5)
for 0<=j<J and using (4) gives

\[
S_B\le\frac{23}{9b}\sum_{j=0}^{J-1}q^j
      =\frac{69}{11b}(1-q^J).                          \tag{6}
\]

For the terminal O^H portion starting at r_J, import the finite-run
part of Christian Hercher, *There are no Collatz m-Cycles with m <= 91*,
JIS 26 (2023), Article 23.3.5,
[Definition 6 and Remark 7 with its proof, printed pp. 4–5](https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/hercher5.pdf):
the odd-input reciprocal mass of a finite actual consecutive odd run
at a positive start s is less than 3/s. The proof uses growth by more
than 3/2 at each positive odd step, hence the finite geometric sum.
This part applies to the terminal subrun even though the preceding
last letter of OOEO is O: the geometric estimate uses only the
specified positive consecutive odd inputs, not maximality or a local
minimum. The additional source comparison with a verification height
X_0 is not imported for arbitrary finite words.

Consequently, using (4), the terminal contribution satisfies

\[
S_H<\frac3{r_J}\le\frac{3q^J}{b}.                     \tag{7}
\]

The final E^a contributes no odd input. The time intervals of the
J blocks and the H terminal O inputs are disjoint: the last block's
last odd input is at 4J-1, whereas the terminal portion starts at 4J.
Although the odd run continues through that boundary, no occurrence
has been omitted or counted twice. Its final endpoint at D is excluded
from the single-word input interval 0<=t<D. Combining (6) and (7)
gives

\[
S_W<\frac{69(1-q^J)+33q^J}{11b}
    =\frac{69-36q^J}{11b}.                            \tag{8}
\]

For W_1 and W_2 the input intervals are respectively [0,D_1) and
[D_1,N). The junction x is counted exactly once, as the first input
of W_2; y is excluded. Sum (8) at b=n and b=x to obtain (1).
The finite-word estimate has nowhere assumed y=n or a cycle minimum.

### Imported cycle inequality and repeated representations

Under y=n the actual represented orbit is positive and closed. It is
nontrivial: n>1 is odd and 20 modulo 27, so n is in neither {1,2},
and the trivial shortcut cycle stays in that set. Every OOEO supplies
three odd and one even input; each terminal portion supplies H_i odd
and a_i even inputs. This proves the displayed K,L and N=K+L.

Import Hercher, the same article,
[Theorem 16 and full proof, printed pp. 10–11](https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/hercher5.pdf).
For a positive nontrivial cycle its step counts obey

\[
0<\frac{K+L}{K}-\delta<\frac{S}{3K\log2},             \tag{9}
\]

where the source partitions S into maximal-odd-run sums. Those sums
cover precisely all odd input occurrences; our partition gives the
same S and need not itself be a maximal-run partition.

To avoid assuming primitiveness, use L034's return-time argument:
if p is the least positive return time, N=rp for an integer r>=1.
All states and parities repeat every p steps. If K_0,L_0,S_0 are
the primitive-period counts and mass, then K=rK_0, L=rL_0 and
S=rS_0. Write u_t=T^t(n). The primitive states are distinct: if u_i=u_j with
0<=i<j<p, applying T^(p-j) gives u_(p-j+i)=n at a positive time
less than p, a contradiction. Thus the source's sums over cycle
states agree with time-occurrence sums on this primitive period.
The primitive cycle is positive and nontrivial. Apply (9)
to it. Both (K+L)/K and S/K are unchanged by the repeat factor,
so (9) holds for the represented word without assuming distinct
junctions or distinct state values. Substituting (1) proves (2);
multiplication by the positive K log2 proves (3). This is solely an
applicability specialization of the published theorem.

### Comparison and remaining obstruction

For a closed word let w be its actual least state. Since n,x>=w,
(1) supplies S<138/(11w). L034 counts M=J_1+J_2+2 minimum
occurrences. Applying the generic finite-run estimate separately
at all these minima would supply the count-only envelope S<3M/w.
Our constant 138/11 is smaller than 3M already when M>=6, which
holds from J_i>=2. More importantly it remains fixed as M grows.
This comparison is with the count-only envelope: we do not claim
that (1) always improves the finer 3 times the sum of actual minimum
reciprocals, which retains their individual heights.

At the verification height X_0 used in Hercher's source (including
its qualification X_0>765 for the supporting estimates), the same
nontrivial-cycle lower-height input n,x>X_0 would give
S<138/(11X_0). The loose envelope S<3M/X_0 follows from
Remark 7. In contrast, Corollary 17 and its proof, printed p. 11,
give the sharper non-strict mass bound S<=97M/(54X_0).
Theorem 27 and its proof, printed pp. 19–20, give
S<=3K/(4X_0). The source's corresponding ratio inequalities
are strict; this does not make these mass conclusions strict.
For repeated representations these two mass bounds follow first
on the primitive cycle, then by multiplying by r: L034 gives
M=r m_0, and K=rK_0 and S=rS_0 as above.

The ratio of our constant envelope to the Corollary 17 envelope
is 7452/(1067M), since (138/11)/(97M/54)=7452/(1067M).
It is less than one exactly when M>7452/1067, or M>=7 for
integer M. Thus the formal minimum M=6 improves the loose
Remark 7 envelope but not this sharper published comparator.
The ratio to the Theorem 27 envelope is 184/(11K); it is less
than one exactly when K>184/11, and the parameter hypotheses
give K>=18. L034's imported necessary cutoff strengthens the
conditional comparison to M>=92 and K>=276. The two ratios
are then at most 7452/(1067*92) and 184/(11*276), respectively.
The earlier ratio 46/(11*92) applies only to the loose 3M/X_0
envelope, not to Corollary 17.
These compare sourced upper bounds, not realized cycles. No reproof
or new independent verification of Theorem 27 or X_0 is asserted,
and neither numerical input is needed for (1)–(3).

This meets the approved discriminating test: an explicit uniform
constant improves the generic count-dependent estimates. Nevertheless
the positive linear form in (3) can be very small; no sufficient
Diophantine lower bound is supplied. L031's positive integer closure
condition remains unresolved. Neither (1) nor (3) excludes the full
unbounded language, proves eventual descent, or establishes a complete
candidate solution.

### Separate critical audit

The separate 2026-10-07 audit reused the preapproved SPECIALIZE
assessment `drafts/literature/2026-10-07-two-postspell-reciprocal-bound-audit.md`.
It checked all input times, the prefix identity at j=0 and j=1,
positive offsets, the terminal subrun, strict signs and primitive
period scaling. No defect was found in (1)–(3). The set-versus-time
identification is made explicit above. The comparison section was
repaired to distinguish Corollary 17 from Remark 7, preserve the
non-strict mass signs and recompute the improvement threshold and
ratio. The review record is
`drafts/2026-10-07-two-postspell-reciprocal-bound-audit.md`.
This is a local audit and repair of a REPRODUCTION, not a new
general cycle theorem or independent certification of the source's
verification height and computations.

## Mathlib

Full matching finite-word bound, the represented-period specialization,
Hercher's Theorem 16, and supporting finite geometric sums and periodic
orbit results: **not checked**. No matching declaration or absence from
Mathlib is asserted. The elementary specialization and precise source
citations above are the informal mathematical evidence.
