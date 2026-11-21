# Corollary C030i: actual-zero separated nodes and count audit

## Hypotheses

Use the actual nontrivial zeta-zero occurrences and squared exponents
of C030g. Each positive-ordinate zero rho=b+i gamma contributes its
actual multiplicity, with

\[
 a=-(\rho-1/2)^2,\qquad
 N(r)=\#\{\text{occurrences}:0<\gamma\le r\}.
\]

No RH or simplicity assumption is made in the counting conclusions.
The conditional node conclusion assumes an integer N>=1 and that
every nontrivial zero with 0<gamma<=150N is on the critical line.
For the low-spectrum interface, assume instead line verification
through a real T>=max(1000,150N). These hypotheses concern all zeros
in the indicated closed height interval, not a list of selected zeros.

Import the explicit counting theorem stated below. Its proof and
computations are not reproduced.

## Conclusion

For every real r>=100,

\[
 N(r+50)-N(r)>\frac{137307}{125000}>1.                     \tag{1}
\]

For every real r>=1000 the exact envelope in Polson's equation (13)
holds, in fact with strict first inequality:

\[
 N(r)+1<\frac{r^2}{6}+0.58r+3.463<r^2.                  \tag{2}
\]

For every integer j>=1 there is an occurrence with
100j<gamma_j<=100j+50. Under the node hypothesis, choosing one such
occurrence for each 1<=j<=N gives distinct positive real exponents
a_j=gamma_j^2 satisfying

\[
 10000<a_j\le22500N^2,\qquad
 |a_j-a_l|>10000|j-l|\quad(j\ne l).                     \tag{3}
\]

Thus (3) implies the source's weak separation inequality as well.
The choices are valid for N=1 without a separation obligation.
Multiple occurrences at other ordinates are neither removed nor
identified. An occurrence at gamma=T is in the low part, and the
high part is exactly gamma>T.

Under line verification through T, the actual spectrum satisfies
the conjugation, strip, positive-low-part, selected-node and count
hypotheses of C030h. Its additional tau, Delta and rho_N thresholds
remain separate obligations; this result alone gives no positivity
conclusion. No all-degree result or RH candidate is claimed.

## Proof

### Source, scope and reason for specialization

This audits the actual-zero input in Nicholas G. Polson,
*On Hilbert's 8th Problem*,
[arXiv:1708.02653v24, 11 September 2026](https://arxiv.org/pdf/1708.02653v24),
Lemma 7.8 and (27), printed p20, and (10)/(13), printed p13.
The relevant proof cases were covered by assessment1196 before this
audit. The node construction and count envelope are source results,
not new discoveries. The replay is needed to check the fixed cutoffs,
multiplicity and endpoint interface used by C030h within C030b.

For the actual counting proof import Elchin Hasanalizade, Quanli
Shen and Peng-Jie Wong, *Counting zeros of the Riemann zeta function*,
J. Number Theory235 (2022),219-241,
[arXiv:2107.06506v1, 14 July 2021](https://arxiv.org/pdf/2107.06506v1#page=2),
Corollary1.2/(1.5), p2: for every x>=e,

\[
 |N(x)-F(x)|\le B(x),\quad
 F(x)=\frac{x}{2\pi}\log\frac{x}{2\pi e},\quad
 B(x)=0.1038\log x+0.2573\log\log x+9.3675.                \tag{4}
\]

The introduction defines the positive count with closed upper
endpoint. Section2/(2.1)-(2.3), p3, identifies twice that count
with the argument-principle count of the entire completion, so
zeros are counted with multiplicity. Its completion differs from
the local one by a nonzero constant; counts are identical.
We import (4), including its effective constants, rather than
reprove a zero-counting theorem. Its constants differ from Polson's
Rosser input, so all its consequences below are checked afresh.

If the argument-principle calculation is initially stated only at
heights avoiding zeros, (4) still has the required inclusive meaning.
For a fixed r>=100, the locally finite zero set gives a sequence of
nonzero contour heights r_n decreasing to r with N(r_n)=N(r).
Indeed C030g's completion is entire, not identically zero, and all
zeros lie in the strip, so only finitely many ordinates occur in
[r,r+1]. Choose r_n below the first ordinate strictly above r, if
there is one. Continuity of F and B permits the limit in (4).
This includes every multiplicity at r; no assertion that r is not
an ordinate is needed. The same argument applies at r+50 and at T.

### Exact elementary constants

Use Archimedes' standard bounds 3<pi<22/7. The following finite
rational checks suffice for the logarithms used below:

\[
 2\sum_{k=0}^{19}\frac{(9/11)^{2k+1}}{2k+1}>\frac{23}{10},
 \qquad
 \sum_{k=0}^{8}\frac{(46/25)^k}{k!}>\frac{44}{7}.          \tag{5}
\]

For the first inequality's use, integrate the finite geometric
identity for 1/(1-u^2) from 0 to 9/11. The integral remainder is
strictly positive, while
2 integral_0^(9/11) du/(1-u^2)=log(10). Thus the left member
in (5) is a strict lower bound for log(10). For the second, the
positive exponential series gives a strict lower bound for
exp(46/25). Consequently

\[
 \log100>4.6,\qquad \log(2\pi)<1.84,\qquad
 \frac{25}{\pi}>\frac{175}{22}>7.95.                      \tag{6}
\]

The second conclusion uses 2pi<44/7 and (5), with monotonicity of
log. Also e>1+1+1/2+1/6=8/3>5/2. Concavity of log, or its tangent
line at e, gives for every u>0

\[
 \log u\le u/e<(2/5)u.
\]

In particular log log x<(2/5)log x for x>1. With the exact rational
number alpha=0.1038+(2/5)0.2573=0.20672, it follows that

\[
 B(x)<\alpha\log x+9.3675\quad(x>1).                     \tag{7}
\]

All inequalities in (5) and the rational arithmetic below are
verified with Python Fraction in
`scripts/far-time/actual-input-audit-1197.py`; reproduction from
this notebook is `python3 scripts/far-time/actual-input-audit-1197.py`.
The full numerators, denominators, finite terms and margins are in
`scripts/far-time/actual-input-audit-1197.json`.
These are exact finite checks, not rounded evaluations of logs or
zeros. The uniform analytic arguments are supplied here.

### Uniform interval existence using the independent count

Since F'(u)=(1/(2pi))log(u/(2pi)) is increasing, for r>=100,

\[
 F(r+50)-F(r)
 \ge\frac{25}{\pi}\log\frac{r}{2\pi}
 >7.95(\log r-1.84).                                    \tag{8}
\]

The last factor is positive by (6), so multiplying the two strict
lower bounds has the stated direction. Since r+50<=(3/2)r and
log(3/2)<1/2 (integrate 1/(1+u)<1 over 0<u<1/2), (7) gives

\[
 B(r)+B(r+50)
 <2\alpha\log r+\alpha+18.735.                          \tag{9}
\]

Subtract the upper error at r and the lower error at r+50 in (4).
Equations (8)-(9) imply

\[
 \begin{split}
 N(r+50)-N(r)
 &>(7.95-2\alpha)\log r-7.95(1.84)-\alpha-18.735\\
 &>(7.95-2\alpha)(4.6)-7.95(1.84)-\alpha-18.735\\
 &=\frac{137307}{125000}>1.
 \end{split}                                             \tag{10}
\]

Here 7.95-2alpha=7.53656>0, justifying the substitution at every
real r>=100. This proves (1) uniformly, not by testing a finite
set of heights. The integer difference counts exactly the
occurrences r<gamma<=r+50, including repetitions. It is at least
two, though only one occurrence is required. No claim that the
two have distinct ordinates is needed.

### The exact quadratic envelope for every real r>=1000

For positive r, log r<=r; for r>1, log log r<=log r. Since
2pi e>1 and log r>0 in the range at issue, pi>3 implies

\[
 F(r)<\frac r{2\pi}\log r\le\frac{r^2}{2\pi}<\frac{r^2}{6}.
\]

Using (4) with the coarser logarithmic bounds gives

\[
 N(r)+1<\frac{r^2}{6}+0.3611r+10.3675.
\]

The difference between the claimed envelope and this upper bound
is 0.2189r-6.9045, increasing in r and at r=1000 equal to
423991/2000>0. Finally let

\[
 g(r)=\frac56r^2-0.58r-3.463.
\]

For r>=1000, g'(r)=(5/3)r-0.58>0 and
g(1000)=2498249611/3000>0. Hence g(r)>0 on this full real interval.
This proves both strict inequalities in (2). It retains the source's
extra +1 margin; using only N(r)<=r^2 would suffice for C030h.

### Check of the printed Rosser scalar chain

For comparison with the source's own arithmetic, import Rosser's
named estimate in the exact form quoted by Habiba Kadiri,
*Une region explicite sans zeros pour la fonction zeta de Riemann*,
Acta Arithmetica117.4(2005),303-339,
[p329, Lemma4.3 proof before (38)](https://www.cs.uleth.ca/~kadiri/articles/zero-free-region-riemann-zeta-acta-2005.pdf#page=27):
for u>=2, |N(u)-M(u)|<=E(u), where

\[
 M(u)=F(u)+7/8,\qquad
 E(u)=0.137\log u+0.443\log\log u+1.588.
\]

The original is Barkley Rosser, *Explicit bounds for some functions
of prime numbers*, Amer. J. Math.63(1941),211-232,
[Theorem19, p223, doi:10.2307/2371291](https://doi.org/10.2307/2371291).
The original theorem page was not accessed; this attribution and
exact version use the inspected published quotation. The actual
count proof (4)-(10) and (2) above is independently based on HSW,
so no reconciliation of an unread Rosser count definition is hidden
in the main proof.

Since the added 7/8 cancels in the difference, (6) and (8) give
M(r+50)-M(r)>7(log r-2) for r>=100. The error is increasing on
u>1. Using log log x<=log x and log(r+50)<log r+1/2,

\[
 E(r)+E(r+50)\le2E(r+50)
 \le1.16\log(r+50)+3.176
 <1.16\log r+3.756
 <(6/5)\log r+19/5.
\]

Thus the source's difference estimate is
N(r+50)-N(r)>(29/5)log r-89/5>27/5>1, since log r>4.
Its quadratic estimate follows from
7/8+1.588+1=3.463 and 0.137+0.443=0.58 using the same coarse
F and logarithm bounds as above. These checks find no failed scalar
inequality in the printed chain. They do not reprove Rosser's
theorem, certify its original proof, or substitute HSW's constants
into a formula whose constants came from Rosser.

### Selection, separation, multiplicity and the C030h interface

Apply (1) at r=100j for each integer j>=1 and choose one occurrence
in I_j=(100j,100j+50]. For any finite N this requires only finitely
many nonempty sets. These intervals are disjoint and ordered, so
the selected ordinates, hence the selected occurrences, are distinct.
When j<=N, gamma_j<=100N+50<=150N. The conditional line hypothesis
therefore gives a_j=gamma_j^2>10000 and
a_j<=22500N^2.

For l>j put k=l-j>=1. The precise endpoint choices give

\[
 \gamma_l-\gamma_j>100k-50\ge50k,\qquad
 \gamma_l+\gamma_j>200.
\]

Consequently a_l-a_j=(gamma_l-gamma_j)(gamma_l+gamma_j)
>10000k. This proves (3), hence the required weak bound, for
every pair. When N=1 the interval I_1 lies in (100,150] and
the same lower/upper bounds hold; there is no missing base case.

One occurrence is selected from each I_j even if the chosen zero
has higher multiplicity. Other copies stay in the full spectrum.
There is no assertion of simplicity. At a lower endpoint 100j the
occurrence is excluded from I_j; at its upper endpoint 100j+50
it is included. The count difference used above has exactly that
convention.

C030g gives a=gamma^2-d^2-2id gamma with real |d|<1/2, so
Re(a)>=gamma^2-1/4 and |a|<=gamma^2+1/4. It also gives
conjugation invariance of the positive-occurrence spectrum.
An off-line quartet contributes two conjugate nodes; no factor
two converts N(r) into a count of all signed ordinates.
If verification is assumed through T>=max(1000,150N), every
occurrence with gamma<=T has a=gamma^2>0. The selected nodes are
among them. Equation (2) supplies N_*(r)=N(r)<=r^2 for every
real r>=T, including T itself. Subtracting N(T) then counts
exactly T<gamma<=r, as required by C030h's strict-tail argument.
All multiplicities at T stay in its positive low part.

These are exactly the delimited actual-input obligations. The
remaining tau*T^2>=4N, T^2>22500N^2+1/4 and rho_N(T,tau)<1
are not inferred here. C030b's joining estimates and its other
analytic source inputs remain separate; auditing these inputs
does not establish all-degree mixed positivity, actual-theta
signing, common-graph realization or RH. This is local reliability
progress for a reproduction, with no conclusion beyond the sources
being specialized.

## Mathlib

Full matching coverage for this node/count statement, HSW's explicit
constants and Rosser's exact estimate is unchecked. Supporting
finite sums, derivatives, exp/log inequalities and zero-counting
interfaces do not amount to a matching formal theorem.
[Mathlib documentation](https://leanprover-community.github.io/mathlib4_docs/)
is a reference only; no availability or absence claim and no Lean
certification is made. Fraction arithmetic verifies only the
selected rational checks; it does not verify the imported counting
theorem or the analytic proof.
