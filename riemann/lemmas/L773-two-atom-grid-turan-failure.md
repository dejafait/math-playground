# Lemma 773: the approved two-atom grid has no joint countermodel

## Hypotheses

For integers 1<=p<=15 and -8<=j<=8, put r=p/16, w=2^j and

\[
 b_n=\frac{1+w r^n}{(2n)!}\quad(n\ge0),\qquad b_n=0\quad(n<0).
\]

Use the original half-line boundary at every iterate:
\(\mathcal L(x)_n=x_n^2-x_{n-1}x_{n+1}\) for n>=0, with negative
indices zero. Write \(b^{[d]}=\mathcal L^d(b)\) and
\(D_{5,4}=\det[b_{4+v-u}]_{u,v=0}^4\).

## Conclusion

Every grid sequence is positive, has the positive-measure representation
\((2n)!b_n=\int x^n\,d(\delta_1+w\delta_r)(x)\), and has an entire
ordinary generating function. None has both D_(5,4)<0 and strictly
positive Turan iterates at every index and order.

Exactly two grid points have a negative determinant:

\[
\begin{array}{c|c|c}
(p,j)&D_{5,4}&\text{negative iterate}\\ \hline
(6,4)&-171143377859458144499/
76851920262358181705097983725316918476800000000&b^{[4]}_4<0\\
(7,4)&-532464112879658032522559819/
80585079141022492739604823382757913108729036800000000&b^{[5]}_4<0.
\end{array}
\]

All other 253 determinants are strictly positive; none is zero.
The second point passes the prescribed depth1–4, index0–8 screen,
but fails the next local closure inequality. This is a finite-grid
exclusion, not a theorem for other two-atom parameters or arbitrary
positive measures. It supplies no actual-Xi sign or RH consequence.

## Proof

### Moment representation and convergence

Here 0<r<1 and w>0. The displayed measure is finite, positive and
nonzero, with precisely the stated moments. In the even-variable
convention of L021, its square-root pushforward is
\(\delta_1+w\delta_{\sqrt r}\); its 2n-th moment is 1+w r^n.
No identity with the actual theta measure is asserted or needed.

For |z|<=R, \(|b_nz^n|\le(1+w)R^n/(2n)!\). For R>0 the successive
ratios of this majorant are R/((2n+2)(2n+1)), tending to zero.
Thus the majorant is summable on every disk. The power series
converges locally uniformly and defines an entire function. These
elementary checks verify membership in the tested class; they do
not import an all-order positivity claim.

### Exhaustive exact determinant calculation

The generator
`python3 scripts/coefficient-countermodel/two-atom-grid-413.py`
enumerates p=1,...,15 and, for each p, j=-8,...,8. For every point
it stores b_0,...,b_12 as reduced rationals and evaluates the full
5-by-5 determinant in two ways: rational Gaussian elimination with
row swaps and the signed sum over all 120 permutations. The results
agree for all 255 points. Its complete certificate, including all
initial entries, pivots, both determinant values, and the entire
shrinking dependency layers for negative cases, is
`scripts/coefficient-countermodel/two-atom-grid-413.json`.

The separate arithmetic replay
`python3 scripts/coefficient-countermodel/two-atom-closure-413.py`
checks the ordered parameter list against the full Cartesian product,
regenerates every initial entry from the hypotheses, and uses integer
arithmetic after scaling. Specifically, let Q be the least common
multiple of the denominators of b_0,...,b_12, and A_n=Q b_n. It sums

\[
 \sum_{\sigma\in S_5}(-1)^{\#\{u<v:\sigma(u)>\sigma(v)\}}
       \prod_{u=0}^4 A_{4+\sigma(u)-u}.
\]

Division by Q^5 gives D_(5,4), since every term has five factors.
Every regenerated result equals both recorded rational determinants.
The complete integer sums, scales, and signs for all 255 points are
in `scripts/coefficient-countermodel/two-atom-closure-413.json`, under
`determinant_replay`. They are positive except for the two values in
the conclusion; no sign is inferred from a decimal approximation.
This is a fully enumerated rational-arithmetic proof of a bounded
claim, with its algorithm and complete evidence retained for replay.

### Exact failure of the selected survivor

Only the two negative-determinant cases need iterate tests. Starting
from indices0–12, compute each layer only through index12-d at
depth d. At index0 repeatedly square; at other retained indices use
both neighbors from the preceding layer. Thus every stored entry
equals the original infinite sequence's iterate by induction on d.
No right boundary is set to zero. In particular, depth4 at indices
3,4,5 and depth5 at index4 have complete initial dependency ranges.

The integer replay uses A^[0]=A and the same recurrence. Its scaling
identity, proved immediately by induction using the quadratic
recurrence, is

\[
 A^{[d]}_n=Q^{2^d}b^{[d]}_n.
\]

For both negative cases it recomputes and compares every recorded
layer, including the halos, and every recorded nonpositive target
entry. For the sole survivor (7,4) it computes one further layer.
Define, where the three entries are positive,

\[
 c_d(4)=\frac{b^{[d]}_3b^{[d]}_5}{(b^{[d]}_4)^2}.
\]

The common scale cancels. At (6,4), the three depth3 entries are
positive and the exact ratio is

\[
 c_3(4)=
 \frac{323224354536434806056476224667180512210485126652231419}
 {88107268828173440774535437104579102305852724380022264},
 \qquad 3<c_3(4)<4.
\]

At (7,4), all screened entries at depths1–4 and indices0–8 are
positive. The exact ratio at the closure obstruction is

\[
 c_4(4)=
 \frac{2270981111989552992469560450385379363132973093737266709366320081268731754713212398618050050338348766501705433103554877443203246672711742446821248}
 {214867114785396360253445680623919950404020035386428719925510174543646117146043491302130012680703498680108837125651309804462858785595532693363375},
 \qquad 10<c_4(4)<11.
\]

The replay checks these intervals by integer cross-multiplication
and stores both strict margins, all integer layers and the exact
negative iterates under `negative_cases`. Consequently

\[
 b^{[d+1]}_4=(b^{[d]}_4)^2(1-c_d(4))<0
\]

at the respective depths. This proves the two failures and, combined
with the exhaustive determinant signs, the asserted grid exclusion.
All final replay checks pass. A first-pass diagnostic incorrectly
tested the interval (2,3) for c_3(4) of the rejected case; its failure
is preserved in `two-atom-closure-first-pass-413.json` in the same
script directory. The corrected interval is (3,4). The determinant,
ratio, negative-iterate values and survivor selection did not change.

### Certificate method and normalization qualifications

The approved method was Matthew H. Y. Xie, Candice X. T. Zhang and
Philip B. Zhang, *A unified approach to infinite log-concavity of
combinatorial sequences*,
[arXiv:2610.12237v1](https://arxiv.org/pdf/2610.12237v1), Lemma2.1
(printed p.5) and Corollary2.6 (printed p.8). The former is a
position-dependent stopping criterion with positivity through each
stopping depth; the latter supplies sufficient holomorphic curvature
bounds. Neither theorem asserts them for this family. They are not
reproved or used to infer the negative result. The exact negative
iterate already contradicts the desired all-order property, so no
tail cutoff, logarithm branch or finite-boundary completion is claimed
or needed for this exclusion. This is a failure of the candidate's
required positivity, not merely failure of a sufficient analytic bound.

For completeness, positive constant/geometric renormalization cannot
remove either obstruction. If \(\widetilde b_n=C A^n b_n\), C,A>0,
direct induction in the recurrence gives
\(\mathcal L^d(\widetilde b)_n=C^{2^d}A^{n2^d}\mathcal L^d(b)_n\).
Each determinant term has total index 20, so
\(D_{5,4}(\widetilde b)=C^5 A^{20}D_{5,4}(b)\).
In particular the alternative 1/(8*4^n) convention preserves every
sign discussed here. This does not identify any grid point with Xi.
L772 is historical motivation only; L766 and Liu–Mao are unused.

## Mathlib

Full coverage of this finite-grid exclusion, the moment-class
specialization, and the cited stopping/holomorphic theorems has not
been checked. Availability is unknown. The exact integer and rational
certificates are informal reproducible arithmetic, not Lean proofs.
The bounded negative result is not claimed to be original or to extend
the known sources by an all-order theorem.
