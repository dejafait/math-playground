# Lemma 903: degree-uniform loss on own-normalized height cells

## Hypotheses

Use L898's actual full-line theta normalization Phi(u)=K(|u|)/2,
p=u+v, q=u-v and

\[
 W_y=p^2\operatorname{sinhc}(yp)\Phi(u)\Phi(v),\qquad
 A_{2j}(y)=\iint W_yq^{2j},\qquad
 m_{2j}(y)=A_{2j}(y)/A_0(y),\quad 0\le y\le\tfrac12.
\]

All spatial integrals below are over R² with Lebesgue measure; sinhc(0)=1.
Retain exactly L902's hypotheses, including the smooth even kernel and
L309's L037 directed-rounding and exponential arithmetic contracts.
In particular L902's strict decrease of m_(2j) for j>=1 is used
conditionally on those contracts; their curvature certificate is not
independently replayed here. L899's scalar potential comparison and
normalization-stability input are also used. No Fourier sign, zero
information, simplicity assumption or RH assumption is made.

Fix real R>0 and eta>0. For integers m>=0, real x, and a height cell
0<=a<=y<=b<=1/2, define

\[
 \begin{split}
 S_m(y,x)&=\sum_{j=0}^{2m+1}(-1)^jm_{2j}(y)\frac{x^{2j}}{(2j)!},\\
 B_m^{a,b}(x)&=1+
 \sum_{\substack{1\le j\le2m+1\\j\text{ even}}}
 m_{2j}(b)\frac{x^{2j}}{(2j)!}
 -\sum_{\substack{1\le j\le2m+1\\j\text{ odd}}}
 m_{2j}(a)\frac{x^{2j}}{(2j)!}.
 \end{split}
\]

## Conclusion

Here are explicit constants, specified by finite positive theta integrals:

\[
 \begin{split}
 \alpha&=A_0(0),\qquad c_R(u,v)=\cosh(Rq),\\
 D_R(y)&=\iint c_RW_y,\qquad D_R=D_R(1/2),\\
 Q_R&=\iint c_Rp^2W_{1/2},\qquad Q_0=\iint p^2W_{1/2},\\
 \Lambda_R&=\frac{Q_R}{2\alpha}+
                  \frac{D_RQ_0}{6\alpha^2}\in(0,\infty),\\
 \delta(R,\eta)&=\min\left\{\tfrac14,\frac{\eta}{\Lambda_R}\right\}>0.
 \end{split}                                                    \tag{1}
\]

For every such m,a,y,b and |x|<=R,

\[
 0\le S_m(y,x)-B_m^{a,b}(x)
       \le\Lambda_R(b^2-a^2).                                  \tag{2}
\]

Consequently b²-a²<=delta(R,eta) implies the requested error at most eta,
uniformly in degree and throughout the closed cell, including a=0.
No numerical optimization or positive width uniform as R tends to
infinity is claimed. This is an ordinary specialization of known
normalization stability, with an additional coefficient application;
it is not a certified novelty claim or a sign result for B_m or Xi.

## Proof

### Imported stability theorem and existing scalar input

Import Björn Sprungk, *On the Local Lipschitz Stability of Bayesian
Inverse Problems*, Inverse Problems 36 (2020), 055015,
[arXiv:1906.07120v3, Theorem 8, printed p.10](https://arxiv.org/pdf/1906.07120v3#page=10),
22 January 2020 version. The probability setup is on p.3, the
half-L1 total-variation convention on p.7, and the normalization
proof cases on pp.7–9 and Appendix A before (13), p.24.
On a Polish space with Borel probability mu, for real f,g in L1(mu),
essinf_mu f=0 and 0<Z_f,Z_g<infinity, where Z_h=int exp(-h)dmu,
the theorem states

\[
 d_{\rm TV}(\mu_f,\mu_g)
 \le\frac{e^{-[\operatorname{essinf}_\mu g]_-}}{Z_f}
                 \|f-g\|_{L^1(\mu)},\qquad
 d\mu_h=e^{-h}d\mu/Z_h,\quad [r]_-:=\min(0,r).                  \tag{3}
\]

The general theorem is imported, not reproved. L899 already specializes
its unweighted version and proves, for every real p and 0<=y,v<=1/2,

\[
 \Psi_y=\log\frac{\operatorname{sinhc}(p/2)}
                         {\operatorname{sinhc}(yp)},\qquad
 0\le\Psi_y\le p^2/24,\qquad
 |\Psi_y-\Psi_v|\le p^2|y^2-v^2|/6.                            \tag{4}
\]

These scalar statements include p=0 and y=0. Their cited inputs are
DLMF 4.36.1, 4.33.1 and 25.6.1, with the applicability and convergent
product argument already in L899; no reproof is needed. L899's
unweighted law bound alone cannot control the unbounded observer
cosh(Rq). The changed reference and the return to the original
normalization below are the needed specialization beyond that result.

### Finiteness and the changed probability reference

L898 supplies 0<alpha<=A_0(y)<=A_0(1/2)<infinity and integrability
of its theta kernel against every fixed polynomial times an exponential.
For a fully explicit check of the additional weight, put

\[
 J_k=\int_{\mathbb R}|u|^ke^{(R+1/2)|u|}\Phi(u)\,du
                \quad(0\le k\le4).
\]

Every J_k is finite by that same theta decay, with bounded kernel on
compact intervals. Since |p|,|q|<=|u|+|v|, sinhc(p/2)<=exp(|p|/2)
and c_R<=exp(R|q|), nonnegative Fubini and the binomial theorem give

\[
 D_R\le\sum_{k=0}^2\binom2kJ_kJ_{2-k}<\infty,\qquad
 Q_R\le\sum_{k=0}^4\binom4kJ_kJ_{4-k}<\infty.                   \tag{5}
\]

The same argument permits any additional fixed polynomial in p,q.
Both displayed integrals are positive on any open rectangle avoiding
p=0, because Phi is positive. In particular 0<Q_0<=Q_R and
0<alpha<=D_R(y)<=D_R<infinity, the upper bound following from
W_y<=W_(1/2). Thus all constants in (1) are finite and positive.

Take E=R² with its Euclidean metric and the Borel reference probability

\[
                       d\mu_R=\frac{c_RW_{1/2}}{D_R}\,du\,dv.
\]

It is on a Polish space. The potentials in (4) are real, continuous
and measurable. Moreover

\[
 \int p^2d\mu_R=Q_R/D_R<\infty,
 \qquad \|\Psi_y-\Psi_v\|_{L^1(\mu_R)}
       \le\frac{Q_R}{6D_R}|y^2-v^2|,                            \tag{6}
\]

so each Psi_y belongs to L1(mu_R). To check its essential infimum,
let epsilon>0 and choose d>0 with d²/24<epsilon. On the open rectangle
d/4<u<d/2, d/4<v<d/2 one has 0<p<d, Psi_y<epsilon, and strictly
positive reference density. This rectangle has positive mu_R measure;
no mass on the null line p=0 is needed. Since Psi_y>=0 everywhere,
essinf_mu_R Psi_y=0, including y=0 and y=1/2.

The exact identity exp(-Psi_y)W_(1/2)=W_y holds even on p=0.
Consequently the likelihood normalizers and posterior probabilities are

\[
 Z_y=\frac{D_R(y)}{D_R}\in[\alpha/D_R,1],\qquad
                   d\rho_y=\frac{c_RW_y}{D_R(y)}\,du\,dv.
\]

Every hypothesis of (3) is now verified for f=Psi_y, g=Psi_v.
Write h=|y²-v²|. With the half-L1 convention, (3) and (6) yield

\[
                    \|\rho_y-\rho_v\|_1
                \le\frac{Q_R}{3D_R(y)}h.                       \tag{7}
\]

Here and below the norm of a difference of Lebesgue densities is its
full L1 norm, not its half-L1 total variation.

### Recovering the original A_0 normalization

Weighted posterior stability (7) alone would not prove the target.
The scalar function exp(-t) is 1-Lipschitz for t>=0. By (4) and the
likelihood identity, integration gives the raw mass differences

\[
 |D_R(y)-D_R(v)|\le Q_Rh/6,\qquad
 |A_0(y)-A_0(v)|\le Q_0h/6.                                   \tag{8}
\]

These are only the mass estimates required for this application,
not a reproof of general normalization stability.
Set r_y=D_R(y)/A_0(y). Since A_0>=alpha and D_R(v)<=D_R,

\[
 \begin{split}
 |r_y-r_v|
 &\le\frac{|D_R(y)-D_R(v)|}{A_0(y)}
    +\frac{D_R(v)|A_0(y)-A_0(v)|}{A_0(y)A_0(v)}\\
 &\le\left(\frac{Q_R}{6\alpha}
               +\frac{D_RQ_0}{6\alpha^2}\right)h.              \tag{9}
 \end{split}
\]

Let n_y=W_y/A_0(y) be the original probability density. Its weighted
density is c_Rn_y=r_y rho_y, where rho_y also denotes its density.
Splitting r_y rho_y-r_v rho_v as r_y(rho_y-rho_v)+(r_y-r_v)rho_v,
and using that rho_v has mass one, (7)–(9) give

\[
 \begin{split}
 \iint c_R|n_y-n_v|
 &\le r_y\|\rho_y-\rho_v\|_1+|r_y-r_v|\\
 &\le\left(\frac{Q_R}{3\alpha}+
            \frac{Q_R}{6\alpha}+
            \frac{D_RQ_0}{6\alpha^2}\right)h
   =\Lambda_Rh.                                               \tag{10}
 \end{split}
\]

The cancellation D_R(y)/D_R(y) in the first term is essential; no
weighted mass was silently treated as the original A_0 mass. All
statements used closed-square scalar estimates, so (10) includes
zero heights, both upper endpoints and equal heights.

### Parity observers and every finite degree

For real x define the nonnegative polynomials in q

\[
 T_E(q,x)=\sum_{\substack{1\le j\le2m+1\\j\text{ even}}}
                 \frac{(xq)^{2j}}{(2j)!},\qquad
 T_O(q,x)=\sum_{\substack{1\le j\le2m+1\\j\text{ odd}}}
                 \frac{(xq)^{2j}}{(2j)!}.
\]

For |x|<=R each lies between zero and c_R. Indeed each term is
nonnegative, (xq)^(2j)<=R^(2j)q^(2j), and the sum over every j>=0
is exactly the convergent cosh(Rq) series. Integrating this infinite
nonnegative series is justified by Tonelli; its integral against
n_y is D_R(y)/A_0(y)<=D_R/alpha<infinity. Thus the majorant controls
all finite degrees by one integrable function. There is no signed
infinite-series interchange or degree-dependent integrability claim.

By L902, each coefficient m_(2j)(y)-m_(2j)(b) and
m_(2j)(a)-m_(2j)(y), j>=1, is nonnegative, also with equal heights.
The real powers x^(2j) are nonnegative. It follows term by term that

\[
 \begin{split}
 0\le S_m(y,x)-B_m^{a,b}(x)
   &=\iint T_E(q,x)(n_y-n_b)
      +\iint T_O(q,x)(n_a-n_y)\\
   &\le\iint c_R|n_y-n_b|+\iint c_R|n_a-n_y|\\
   &\le\Lambda_R[(b^2-y^2)+(y^2-a^2)]
     =\Lambda_R(b^2-a^2),
 \end{split}
\]

by (10). This proves (2), including m=0, x=0 and a=b. Substitution
of (1) proves the eta claim. ∎

Only the nonnegative lower inequality in (2) uses L902's retained
curvature/arithmetic contract; (10) is independent of it. The potential
downstream use is an explicit absolute refinement price for each fixed
frequency window. Independent positive margins, control as R grows,
all-height defect signs and L030–L032/C032a's higher mixed forms are
still unresolved. L898's fixed cross-endpoint obstruction and L312's
oscillatory-order failure are comparisons, not premises. This lemma
neither contradicts those stops nor turns a negative minorant into a
negative actual defect. The separately approved audit below checks this
specialization; there is no RH candidate.

### Audit of normalization, uniform degree and endpoints (2026-11-08, step132)

The pre-existing unfinished audit text in this section was independently
checked and completed in step132; it was preserved rather than treated
as evidence of its own correctness. The stated bound passes without
changing its constant or hypotheses. This verifies the local application of the
cited stability theorem; it establishes no stronger general stability
result and no Fourier sign. The source hypotheses and convention are
the primary extraction already recorded above and in the step129
assessment, reused through the approved audit assessment.

First, (5) uses powers two for D_R and four for Q_R, not powers of q
alone: W_(1/2) already contains p², and Q_R adds another p².
The coefficients in the two finite binomial sums are respectively
1,2,1 and 1,4,6,4,1. Each J_k is locally integrable since Phi is bounded
on compact intervals, and is integrable at infinity by L898's
polynomial-exponential domination. The positive rectangle argument
also works for alpha and Q_0. Thus every denominator used is strictly
positive and every displayed weighted moment is finite for fixed R.
No uniformity as R grows is supplied by this check.

Second, the changed reference is a probability on a Polish space, and
(4) bounds each potential in L1(mu_R) by Q_R/(24D_R). The rectangle
used for its essential infimum lies in d/2<p<d, has positive mu_R
measure, and satisfies Psi_y<epsilon for every allowed y. Hence the
essential infimum is zero even though the line p=0 itself has no mass.
At y=1/2 the potential is identically zero. Its likelihood identity
gives exactly Z_y=D_R(y)/D_R and rho_y=c_R W_y/D_R(y); it does not
give A_0(y)/D_R. Sprungk's factor is consequently one, and its
half-L1 convention gives

\[
 2\frac{D_R}{D_R(y)}\frac{Q_R}{6D_R}h
       =\frac{Q_R}{3D_R(y)}h
\]

for the full-L1 posterior difference. This checks (7), including the
factor two and the first-potential normalizer.

Third, the raw differences in (8) integrate the pointwise inequality
W_(1/2)|exp(-Psi_y)-exp(-Psi_v)|<=W_(1/2)p²h/6,
once with weight c_R and once without it. Both dominating moments
are already finite. Formula (9) uses the exact identity

\[
 r_y-r_v=\frac{D_R(y)-D_R(v)}{A_0(y)}
       +D_R(v)\frac{A_0(v)-A_0(y)}{A_0(y)A_0(v)}.
\]

Multiplication of (7) by r_y cancels D_R(y), leaving
Q_R/(3A_0(y))<=Q_R/(3alpha). Adding (9) therefore gives precisely
Q_R/(2alpha)+D_R Q_0/(6alpha²)=Lambda_R, as in (1).
In particular the recovery of the original normalizer retains both
raw mass corrections, and the splitting in (10) has mass-one rho_v.

Finally each finite parity observer is nonnegative and bounded by
cosh(Rq), whose integral against every n_y is at most D_R/alpha.
This majorant is independent of m; no signed infinite Taylor series
is integrated to prove (2). The equality expressing S_m-B_m as two
finite integrals follows by cancellation of m_0=1 and the definitions
of A_(2j). L902 supplies the sign of each coefficient difference;
pointwise signs of n_y-n_b and n_a-n_y are neither asserted nor needed.
Their absolute estimates use (10) on two pairs, so their increments
are b²-y² and y²-a², summing to b²-a² with no doubling.

For m=0 the even observer is empty and the odd observer is just
(xq)²/2; the same proof applies. At x=0 both are zero. For a=b the
condition a<=y<=b forces y=a=b, and both losses vanish. The bounds
on Psi, the positive normalizers and the common integrable majorant
already hold at a=0 and b=1/2, so no limiting argument or division by
a height is needed. Since 0<Lambda_R<infinity, delta in (1) is
strictly positive and Lambda_R delta<=eta; equality of the width is
allowed. This checks the entire stated closed-cell range.

Only the lower inequality retains L902's L309/L037 curvature and
arithmetic contracts, which this audit does not replay. The weighted
absolute bound (10) is independent of those contracts. Direct
mathematical inputs remain L898, L899 and L902; L312 and the fixed-cell
failure remain comparisons. Positive section margins, growing-R
coverage and higher mixed positivity are unresolved.

## Mathlib

Full matching coverage is not checked; availability is unknown.
No supporting Mathlib theorem names were verified. Sprungk's theorem,
the scalar DLMF application in L899 and L902's conditional coefficient
order are informal mathematical inputs, not formal proof certificates.
The new work is the weighted-reference application, recovery of the
original normalization and the uniform parity bound, not a reproof or
claimed discovery of the general stability theorem.
