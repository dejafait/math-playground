# Lemma 837: PF2 and an eventual shift-three ray do not force the adjacent ray

## Hypotheses

Let
\[
 P(z)=(1+4z)(1+3z)(1+2z)(1+z+z^2)=\sum_{n=0}^5a_nz^n,
 \qquad a_n=0\quad(n<0\text{ or }n>5).
\]
For positive integers r and nonnegative integers k define the ordinary
coefficient minor
\[
 D_{(r,k)}(P)=\det[a_{k+j-i}]_{0\le i,j<r}.
\]
PF2 means nonnegativity of **every** ordered minor of size one or two
of the infinite Toeplitz matrix (a_(j-i))_(i,j>=0), not merely its
contiguous minors. No Xi coefficient identification is assumed.

## Conclusion

The six coefficients are (1,10,36,59,50,24), all positive integers,
and their zero-extended sequence is PF2. Its five polynomial roots
are distinct. For every integer r>=16,
\[
 D_{(r,3)}(P)>0.
\]
For every integer r>=16 with r congruent to5 modulo6,
\[
 D_{(r,4)}(P)<0.
\]
Thus PF2 plus eventual strict positivity at shift3 does not imply
eventual nonnegativity at shift4, even for a positive rational
degree-five polynomial. This does not test an implication requiring
PF_m for an arbitrary prescribed m, the much larger finite band
available for Xi, strict overlap, all minor shapes, or Xi realization.
It gives neither a proof nor a disproof of RH. The construction is a
specialization of known formulas; originality is not asserted.

## Proof

### Imported results and applicability

Olga M. Katkova, *Multiple positivity and the Riemann zeta-function*,
[arXiv:math/0505174v1](https://arxiv.org/pdf/math/0505174v1),
Definition2 and (8), printed p.4, and **Theorem B**, printed p.5,
states the Schoenberg sufficient criterion: a polynomial f with
f(0)>0 and no roots in the open sector |arg z|<pi*m/(m+1) is PF_m.
It concerns all ordered minors. Here P(0)=1; the roots are
-1/4,-1/3,-1/2,exp(2pi i/3),exp(-2pi i/3).
Their arguments have absolute value pi or2pi/3, so none is in the
open sector for m=2. The boundary pair is permitted. The criterion
proves PF2, and direct multiplication gives the stated coefficients.

Per Alexandersson, *Schur polynomials, banded Toeplitz matrices and
Widom's formula*, Electronic Journal of Combinatorics19(4) (2012), P22,
[arXiv:1208.5607v1](https://arxiv.org/html/1208.5607v1),
**Theorem6 (Modified Widom's formula)**, printed p.5, gives, for
distinct variables x_1,...,x_n and their elementary coefficients s_i,
\[
 \det D_c^r=\sum_{|S|=c} B_S^r C_S,\qquad
 B_S=\prod_{i\in S}x_i,\qquad
 C_S=\frac{B_S^{n-c}}{\prod_{i\in S,j\notin S}(x_i-x_j)}.       \tag{1}
\]
Here its s_0=1; deleting the first c columns and taking a leading
r-square gives exactly our entries a_(c+j-i). There is no transpose,
factorial, reciprocal-root or determinant-sign change. Take n=5,
c=k in{3,4}, and use
\[
 (x_1,x_2,x_3,x_4,x_5)=(4,3,2,w,v),\quad
 w=(1+i\sqrt3)/2,\quad v=\bar w=1-w.
\]
Then w^2=w-1, wv=1, w^6=1, and |w|=|v|=1.
The factorization P(z)=prod_i(1+x_i z) supplies the elementary
coefficients required in(1). The variables are distinct: the real
ones are distinct, |w-v|^2=3, and
|R-w|^2=|R-v|^2=R^2-R+1 in{13,7,3} for R in{4,3,2}.
Every cross difference in(1) is consequently nonzero. Complex
variables and all positive ranks r are allowed by Theorem6.
We import the formula and sector criterion, rather than reprove them;
the explicit sign specialization is the obligation not supplied by
those theorem statements.

### Complete exact terms

The following are all ten triples for k=3. Write d_S for the cross
denominator in(1). Entries use w^2=w-1, so every displayed value is
exact in Q(w). In particular C_S=B_S^2/d_S.

| S | B_S | d_S | C_S |
|---|---|---|---|
| 4,3,2 | 24 | 273 | 192/91 |
| 4,3,w | 12w | 36-66w | (-144-120w)/91 |
| 4,3,v | 12v | -30+66w | (-264+120w)/91 |
| 4,2,w | 8w | -27+30w | (576+64w)/273 |
| 4,2,v | 8v | 3-30w | (640-64w)/273 |
| 4,w,v | 4 | 42 | 8/21 |
| 3,2,w | 6w | 60-54w | (-60+6w)/91 |
| 3,2,v | 6v | 6+54w | (-54-6w)/91 |
| 3,w,v | 3 | -39 | -3/13 |
| 2,w,v | 2 | 182 | 2/91 |

The five quadruples for k=4 give C_S=B_S/d_S:

| S | B_S | d_S | C_S |
|---|---|---|---|
| 4,3,2,w | 24w | -33+15w | (40-88w)/91 |
| 4,3,2,v | 24v | -18-15w | (-48+88w)/91 |
| 4,3,w,v | 12 | 6 | 2 |
| 4,2,w,v | 8 | -7 | -8/7 |
| 3,2,w,v | 6 | 26 | 3/13 |

These finite tables follow by multiplying the cross differences;
they exhaust binomial(5,3)=10 and binomial(5,4)=5 terms. Conjugation
sends a+bw to (a+b)-bw, pairing the rows containing w alone and v
alone. The remaining rows are real, so each complete sum is real.
No tied dominant term has been removed.

### Uniform positive shift-three ray

The first triple has base24 and coefficient192/91>0. Every other
base has modulus at most12. For rational a,b, |a+bw|<=|a|+|b|.
The bounds for the nine other coefficients, in table order, sum to
\[
 \frac{264}{91}+\frac{384}{91}+\frac{640}{273}
 +\frac{704}{273}+\frac8{21}+\frac{66}{91}+\frac{60}{91}
 +\frac3{13}+\frac2{91}=\frac{3839}{273}.
\]
Hence for **every** positive integer r,
\[
 \left|24^{-r}D_{(r,3)}-\frac{192}{91}\right|
 \le\frac{3839}{273}2^{-r}.                                \tag{2}
\]
At r=16 the lower margin is
\[
 \frac{192}{91}-\frac{3839}{273\cdot65536}
 =\frac{37744897}{17891328}>0.
\]
The error decreases for all larger ranks. This proves the entire
claimed positive ray, without extrapolating from samples.

### Infinite strictly negative shift-four subsequence

Put C=(40-88w)/91. The two leading rows are conjugate, with bases
24w and24v. The remaining three rows give the exact expression
\[
 24^{-r}D_{(r,4)}=2\operatorname{Re}(Cw^r)
      +2(1/2)^r-\frac87(1/3)^r+\frac3{13}(1/4)^r.          \tag{3}
\]
For r congruent to0,1,2,3,4,5 modulo6, respectively, the leading
real term is
\[
 \frac1{91}(-8,128,136,8,-128,-136).                        \tag{4}
\]
This follows directly from w^2=w-1 and w^6=1, not a numerical
phase approximation. The absolute remainder in(3) is at most
\[
 \left(2+\frac87+\frac3{13}\right)2^{-r}
 =\frac{307}{91}2^{-r}.                                    \tag{5}
\]
On the residue class5 the negative leading magnitude is136/91.
At the common onset16 it exceeds the error by
\[
 \frac{136}{91}-\frac{307}{91\cdot65536}
 =\frac{1273227}{851968}>0.
\]
Thus every r=6m+5>=16 has D_(r,4)<0. These ranks include17,23,...
and are unbounded, proving infinitude. Equations(2)-(5) certify the
sign claims for all stated ranks with full remainder control.

### Reproduction and qualifications

Run `python3 scripts/fixed-shift-overlap/adjacent-degree-five-exact.py`.
The standard-library rational-arithmetic script saves every variable,
pairwise difference, subset base, cross denominator, coefficient,
periodic value, actual/required margin and failure to
`scripts/fixed-shift-overlap/adjacent-degree-five-exact.json`.
All relevant complete fields were inspected. Independent rational
determinants at ranks1 through6 agree with(1) at both shifts;
these are orientation checks, not the proof of unbounded signs.
The printed output includes both positive margins, onset16 and
an empty failure list. The displayed algebraic proof is sufficient
without a trusted floating-point calculation or a source reproof.

The main all-degree mixed-positivity gap L030–L032/C032a remains.
C832a and L834 motivate this abstract comparison but supply no
premises in this proof. L772's different Turan obstruction and the
recorded hybrid-cofactor/growing-order failures are not replaced.
The example cannot negate a bridge using additional actual-Xi
structure or a stronger finite-PF hypothesis. No negative minor of
Xi, no off-line zeta zero and no RH-equivalent positivity are assumed
or obtained.

### Independent audit, 6 November 2026

The audit retained the statement and proof without a mathematical repair.
Theorem B's open sector includes neither boundary root, and its PF2
conclusion concerns every ordered minor through order two. Theorem 6's
complex-variable, distinct-root and positive-rank hypotheses, its
normalization and the shift convention all match (1). These source
statements were checked directly at the citations above; their already
assessed proofs are imported, not reproved. The sources do not supply the
two particular sign conclusions, which follow from the displayed tables
and bounds.

For a separate exact arithmetic check run
`python3 scripts/fixed-shift-overlap/adjacent-degree-five-audit.py`.
It saves its complete evidence to
`scripts/fixed-shift-overlap/adjacent-degree-five-audit.json`.
This program uses coordinates a+b*u with u^2=-3 and w=(1+u)/2,
independently multiplies the rational factors, and computes the cross
denominators from the characteristic derivative rather than the original
cross-product loop. Specifically, with chi(t)=prod_i(t-x_i),
\[
 d_S=(-1)^{c(c-1)/2}
 \frac{\prod_{i\in S}\chi'(x_i)}
 {\prod_{i<j,\ i,j\in S}(x_i-x_j)^2},\qquad c=|S|.
\]
Indeed, the product of derivatives includes each cross factor once;
each internal unordered pair contributes
(x_i-x_j)(x_j-x_i)=-(x_i-x_j)^2. All divisors are nonzero by the
distinctness already proved. This verifies every base, denominator and
coefficient in both tables by a second finite arithmetic calculation.
It also verifies all conjugate pairings, all ten pairwise differences,
the six exact phases and both geometric remainder constants. Integer
Bareiss determinants at both shifts and ranks 1 through 17 match the
formula, including the first claimed negative subsequence rank 17.
The 239 exact checks pass with no failures. These finite replays still
serve only as orientation checks: the infinite-rank conclusions use
(2)–(5), whose error factors decrease for all r>=16. In particular, the
independently recomputed strict margins are exactly
37744897/17891328 and 1273227/851968, both greater than zero.

Thus the PF2-only adjacency obstruction is audited. This does not enlarge
its scope to arbitrary prescribed finite PF order, actual Xi, or a
uniform onset in a varying polynomial family. No new result beyond this
known-method local specialization is claimed.

## Mathlib

Full matching coverage for this explicit PF2 countermodel, the sector
criterion and the complex fixed-band formula has not been checked.
No absence claim is made. The rational certificate is not a Lean proof.
