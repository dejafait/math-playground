# L841 — Nonnegative first solid ray for the dyadic cubic product

## Hypotheses

Let
\[
 P(w)=1+2w+2w^2+w^3,\qquad
 F_M(z)=\prod_{j=0}^{M-1}P(2^{-j}z)\quad(M\ge1).
\]
Write F(z)=lim_(M to infinity) F_M(z), with convergence established
below, and let a_n=[z^n]F(z) be its ordinary Taylor coefficients.
Set a_n=0 for every integer n<0. For each integer r>=1 define
\[
 D_r=\det[a_{1+j-i}]_{0\le i,j<r}.
\]
There is no factorial normalization, additional exponential factor,
assumption of strict signs or Xi realization.

## Conclusion

F is entire, F(0)=1, and for every integer r>=1,
\[
 D_r=[t^r]\frac1{F(-t)}\ \ge0.                         \tag{1}
\]
The reciprocal Taylor series in (1) is taken in |t|<1. This decides
the complete weak first-ray question, not just finitely many ranks
or an eventual range. Zero coefficients in the individual reciprocal
factors are allowed throughout the proof.

This is a specialization of known reciprocal, determinant and compact
product identities. It certifies no higher shift k>=2, inherited PF
order, strict-sign assertion or actual-Xi sign. It is not a proof or
disproof of RH, and no originality claim is made. An independent
critical audit of this specialization has not yet been performed.

## Proof

### Named inputs and the exact finite match

We use I. G. Macdonald, *Symmetric Functions and Hall Polynomials*,
second edition, Oxford (1995),
[primary book PDF](https://math.berkeley.edu/~corteel/MATH249/macdonald.pdf),
I.2 (2.4)–(2.6), pp.20–21, and I.3 (3.4), (3.5), (3.9),
pp.41–42. If E(t)=sum e_n t^n, e_0=1, then
H(t)E(-t)=1, where H(t)=sum h_n t^n; negative subscripts vanish.
The dual Jacobi–Trudi formula for the partition (r), together with
s_(r)=h_r, is
\[
 \det[e_{1-i+j}]_{1\le i,j\le r}=h_r.                  \tag{2}
\]
These are polynomial identities in the elementary coefficients;
numerical specialization to complex variables is permitted. In
particular, they impose no positivity or distinctness condition on
those variables. Macdonald I.2 (2.9)/(2.9'), pp.22–23, proves the
complementary-minor correspondence using triangular inverses with
diagonal 1. There is no division by a possibly zero solid minor.
We import these identities rather than reprove them.

At m=1 the audited L840 has theta=pi/3 and exactly the polynomial P:
\[
 P(w)=(1+w)(1+e^{i\pi/3}w)(1+e^{-i\pi/3}w).
\]
Both its constant and leading coefficients are 1. Let
b_n=[t^n]1/P(-t), so b_0=1. Applying (2) to these three elementary
variables identifies b_n, for n>=1, with the first-ray determinant
in L840. Its sine formula and rank residues give, exactly,
\[
 b_n=\begin{cases}
 1,&n\equiv0,3\pmod6,\\
 2,&n\equiv1,2\pmod6,\\
 0,&n\equiv4,5\pmod6.
 \end{cases}                                         \tag{3}
\]
Indeed L840's period is 2(m+2)=6, and substitution of theta=pi/3
in its formula at ranks 1,...,6 gives 2,2,1,0,0,1. The value b_0=1
agrees with the same residue pattern. Thus (3) includes every rank
and both exact zero classes, without any floating-point calculation.
P has all its roots on |w|=1, so this reciprocal series converges
for |t|<1.

### Finite products and their coefficient signs

Scaling t by 2^(-j) gives
\[
 \frac1{P(-2^{-j}t)}=\sum_{n\ge0}b_n2^{-jn}t^n.
\]
For fixed M this is an ordinary finite Cauchy product of series
convergent on |t|<1. Consequently, for every integer r>=0,
\[
 c_r^{(M)}:=[t^r]\frac1{F_M(-t)}
 =\sum_{\substack{n_0,\ldots,n_{M-1}\ge0\\
                  n_0+\cdots+n_{M-1}=r}}
       \prod_{j=0}^{M-1} b_{n_j}2^{-j n_j}\ \ge0.        \tag{4}
\]
The sum has finitely many terms at each fixed M,r. All terms are
real and nonnegative by (3), including terms with a zero factor.
This is positivity of scalar reciprocal coefficients; no closure
theorem for solid-minor signs is asserted.

Put a_n^(M)=[z^n]F_M(z), with zero extension for n<0. The 3M
elementary variables are 2^(-j), 2^(-j)e^(i*pi/3),
2^(-j)e^(-i*pi/3), 0<=j<M. Their elementary generating function is
precisely F_M and a_0^(M)=1. Thus (2) gives, for every r>=1,
\[
 \det[a_{1+j-i}^{(M)}]_{0\le i,j<r}=c_r^{(M)}.          \tag{5}
\]
This also checks the orientation of the indices and the ordinary
coefficient normalization in the desired determinant.

### Compact convergence and a zero-free reciprocal disk

For the analytic passage we use C. McMullen, *Advanced Complex
Analysis*, Harvard Math213a notes dated 2 December 2025,
[primary notes PDF](https://people.math.harvard.edu/~ctm/home/text/class/harvard/213a/25/html/home/course/course.pdf),
the compact-product criterion preceding Theorem3.1 and Theorem3.1,
p.80. Summable compact suprema of the deviations from 1 give
holomorphic product convergence; a product of linear factors with
summable absolute reciprocal zero parameters has exactly its stated
zeros, counted with multiplicity. Taylor coefficient passage uses
the Cauchy formula (1.2) and its bound, pp.12–13.

For every R>0,
\[
 \begin{split}
 \sum_{j\ge0}\sup_{|z|\le R}|P(2^{-j}z)-1|
 &\le \sum_{j\ge0}
     (2R2^{-j}+2R^2 2^{-2j}+R^3 2^{-3j})\\
 &=4R+\frac83R^2+\frac87R^3<\infty.
 \end{split}                                         \tag{6}
\]
Hence F_M converges uniformly on every compact subset of C to an
entire F, and F(0)=1. To verify nonvanishing in the disk needed for
the reciprocal, factor each P as above. The sum of the absolute
values of all its scaled elementary parameters is
\[
 \sum_{j\ge0}3\,2^{-j}=6<\infty.
\]
The linear product is therefore covered by Theorem3.1. Grouping its
successive triples gives exactly F_M and the same compact limit F.
Every zero of a linear factor has modulus 2^j>=1, and the theorem
introduces no other zeros. In particular, F(-t) is nonzero on |t|<1.
This use of zero location only verifies the reciprocal domain; no
assumption about real zeros is made.

Fix 0<rho<1. Continuity and nonvanishing give
\[
 m_\rho=\min_{|t|\le\rho}|F(-t)|>0.
\]
For all sufficiently large M, uniform convergence gives
|F_M(-t)|>=m_rho/2 throughout the disk, and therefore
\[
 \sup_{|t|\le\rho}\left|\frac1{F_M(-t)}-\frac1{F(-t)}\right|
 \le\frac{2}{m_\rho^2}
       \sup_{|t|\le\rho}|F_M(-t)-F(-t)|\longrightarrow0. \tag{7}
\]
Each reciprocal is holomorphic there. For every fixed r>=0 the
Cauchy coefficient bound on |t|=rho now gives
\[
 \left|c_r^{(M)}-[t^r]\frac1{F(-t)}\right|
 \le\rho^{-r}\sup_{|t|=\rho}
       \left|\frac1{F_M(-t)}-\frac1{F(-t)}\right|
 \longrightarrow0.                                   \tag{8}
\]
Similarly, compact convergence of F_M and the same coefficient
formula give a_n^(M) to a_n for every fixed n>=0. Negative-index
coefficients are identically zero for all M and in the limit.

### Passage to every fixed rank

Fix any integer r>=1. The determinant in (5) uses only the finitely
many coefficients with indices 2-r,...,r and is a polynomial in
those entries. Thus coefficient convergence, (5), and (8) imply
\[
 D_r=\lim_{M\to\infty}\det[a_{1+j-i}^{(M)}]
    =\lim_{M\to\infty}c_r^{(M)}
    =[t^r]\frac1{F(-t)}\ge0,
\]
where the final inequality follows from (4) and the closedness of
the nonnegative real half-line. Since r was arbitrary, this proves
(1) at every required rank. No uniform-in-r limit or exchange of
rank and product limits is needed. Finite-factor zero cases were
retained in (3)–(4); no step divided by them or required a positive
lower bound for a determinant. A zero limiting coefficient would
also satisfy the stated weak conclusion.

The substantive extension over the finite input is the verified
infinite-product and fixed-coefficient passage. It leaves all higher
solid shifts and the actual-Xi mixed-positivity gap unresolved.

## Mathlib

Full matching Mathlib coverage of this dyadic product, (2), and the
combined all-rank first-ray statement has not been checked. No
absence claim is made. The cited classical algebraic identities and
compact-product/Cauchy theorems are the standard inputs; L840 supplies
the previously audited finite sign sequence. This is a known-method
specialization, classified REPRODUCTION, not a certified new theorem
beyond the checked literature.
