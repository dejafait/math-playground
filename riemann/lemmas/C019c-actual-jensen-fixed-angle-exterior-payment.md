# C019c — Actual Jensen circle: a fixed-angle exterior is exponentially small

## Hypotheses

Fix the field \(K=\mathbb Q\). Let \(d\) tend to infinity through positive
integers, and use the following exact notation from Ken Ono,
*An Asymptotic Jensen–Pólya Criterion for GRH*,
[arXiv:2610.38870v1](https://arxiv.org/html/2610.38870v1),
28 October 2026, equations (2.5)–(3.5) and (4.4).
Here \(F(z)=\xi(1/2+\sqrt z)\) is the single-valued real entire function,
\(\kappa=\pi/2\), and \(T>2\pi e\) is the unique solution of
\[
 d=\frac{T}{2\pi}\left(\log\frac{T}{2\pi}-1\right),\qquad
 \Lambda=2\left(\log\frac{T}{2\pi}-1\right),\qquad B=T^2.
\]
The positive edge parameters are defined by
\[
 \kappa r_e\left(1+\frac{2\log r_e}{\Lambda}\right)=2,
 \qquad q_e=r_e^{-2}+\frac{2\kappa}{\Lambda r_e}.
\]
For \(x\in[1,4]\), set \(q=q_e+xd^{-2/3}\), and take precisely the
source's Lemma 7 saddle \(u_q=r^2e^{-2i\alpha}\), where
\[
 \frac{\Lambda\cos\alpha}{\kappa r}+\alpha\cot\alpha
   =\frac{\Lambda}{2}+1+\log r,
 \qquad
 q=r^{-2}+\frac{2\kappa}{\Lambda}\frac{\alpha}{\sin\alpha}\,r^{-1}.
\]
On the lower semicircle use \(-\pi\leq\arg u\leq0\), and put
\[
 h_q(u)=-qu+2\kappa\sqrt u+
       \frac{2\kappa}{\Lambda}\sqrt u\Log u-\Log u,
 \qquad w_q(\theta)=Tr e^{i\theta/2}.
\]
The exact amplitude is
\[
 a_q(\theta)=2^{-1/4}\pi^{1/4}w_q(\theta)^{7/4}
       \zeta(1/2+w_q(\theta))g_{\mathbb Q}(w_q(\theta)),
 \qquad -\pi\leq\theta\leq0,
\]
where \(g_{\mathbb Q}\) is the holomorphic nonvanishing gamma remainder
of the source's Lemma 12, with its specified principal powers. Use the
conjugate phase and amplitude on the upper semicircle.

Fix \(0<\theta_0\leq1/10\), independently of \(d,x\). Define
\[
 I_{\rm out}(d,x;\theta_0)=\frac{d!}{2\pi i d^d}
   \int_{\substack{u=r^2e^{i\theta}\\\theta_0\leq|\theta|\leq\pi}}
      F(T^2u)e^{-dqu}\frac{du}{u^{d+1}},
\]
with each of the two arcs counterclockwise, and define
\[
 H_q=\Re h_q(u_q),\qquad
 M_d(x)=\frac{d!}{d^d}|a_q(-2\alpha)|e^{dH_q}d^{-1/3}.
\]
No local Airy approximation or lower bound on a local integral is assumed.

## Conclusion

For every such fixed \(\theta_0\), there are constants
\(C,C'>0\), \(\gamma(\theta_0)>0\), and an onset \(d_0(\theta_0)\)
such that \(M_d(x)>0\) and, uniformly in \(x\in[1,4]\),
\[
 \frac{|I_{\rm out}(d,x;\theta_0)|}{M_d(x)}
 \leq C T d^{1/3}e^{-\gamma(\theta_0)d}
 \leq C'\frac{d^{4/3}}{\log d}e^{-\gamma(\theta_0)d}=o(1).
\]
If \(c>0\) is the constant in the source's (3.12), one may take
\[
 \gamma(\theta_0)=\frac c4(1-\cos(\theta_0/2))^2.
\]
The onset may depend on \(\theta_0\); there is no assertion uniform
as \(\theta_0\) tends to zero. This is a specialization of cited
estimates, not a new general contour theorem or a sign assertion.

## Proof

**Imported estimates and their range.** Use Ono v1, (2.7), Lemma 7
and (3.6)–(3.7), Lemma 8/(3.12), Lemma 12 and (4.4)–(4.5), and
Lemma 13/(4.6). In the PDF these are on pp. 5–11; the angular
Cauchy normalization is also used in Proposition 15, p. 13.
These estimates are imported, not reproved. Their specialization to
the fixed-cutoff region, absent from the stated Gaussian comparison,
is what must be checked here.

Equation (2.7) gives \(\Lambda\to\infty\), \(T\asymp d/\log d\to\infty\).
Lemma 7 gives \(q_e=\pi^2/16+O(\Lambda^{-1})\). Thus \(q\) stays in
a fixed compact subinterval of \((0,\infty)\), uniformly in \(x\).
Choose the fixed \(c_0>0\) allowed by Lemma 13. Eventually
\(q_e<q\leq c_0T\leq T\), uniformly in \(x\). This verifies its range;
the more restrictive interval of the later Gaussian formula is not used.

The uniform near-edge estimate (3.7) applies since
\(0<q-q_e\leq4d^{-2/3}\leq t_0\) eventually. It gives
\(\alpha\leq C_\alpha d^{-1/3}\), uniformly in \(x\).
Also \(r\asymp q^{-1/2}\) by (3.6), so \(r\) is bounded above and
below by fixed positive constants. Hence \(Tr\to\infty\) uniformly,
and Lemma 12 applies throughout the closed semicircles, including
their negative-axis boundary values. Lemma 13 gives
\[
 |a_q(-2\alpha)|\asymp(Tr)^{7/4}>0,\qquad
 \sup_{-\pi\leq\theta\leq0}|a_q(\theta)|
       \leq C T|a_q(-2\alpha)|.                 \tag{1}
\]
The power \(T\) is \(T^N\) with \(N=[\mathbb Q:\mathbb Q]=1\).
In particular division by \(M_d(x)\) is legitimate. For clarity, the
source's saddle lower bound uses the Euler product in \(\Re s\geq4\)
and \(g_{\mathbb Q}=1+O((Tr)^{-1})\); it requires no nonvanishing
assertion near the critical line. Zeros of the amplitude elsewhere on
the circle are permitted.

**Fixed angular separation.** Write
\(\eta=1-\cos(\theta_0/2)>0\). Enlarge the onset until
\(1-\cos\alpha\leq\eta/2\), uniformly in \(x\), using the bound on
\(\alpha\). On the retained lower arc, put \(\beta=-\theta/2\).
Then \(\theta_0/2\leq\beta\leq\pi/2\), so
\[
 \cos\alpha-\cos\beta
 \geq1-\eta/2-\cos(\theta_0/2)=\eta/2.
\]
Lemma 8/(3.12), valid on the entire closed lower semicircle, gives
\[
 \Re h_q(r^2e^{i\theta})\leq H_q-c\eta^2/4
                    =H_q-\gamma(\theta_0).       \tag{2}
\]
This uses the fixed cutoff directly, rather than the shrinking-interval
gap in Corollary 10.

**Measure, upper arc and exact prefactor.** Let \(P_d=d!/d^d>0\).
The factorization (4.5) includes \(u^{-d}\). Since \(du/u=i\,d\theta\),
the lower exterior contribution is exactly
\[
 \frac{P_d}{2\pi}\int_{-\pi}^{-\theta_0}
     a_q(\theta)e^{dh_q(r^2e^{i\theta})}\,d\theta.
                                                        \tag{3}
\]
There is no additional \(r^{-2d}\) or arc-length factor.
Because \(F\) has real Taylor coefficients and \(q,r\) are real,
the upper integrand after this angular substitution is the complex
conjugate of the lower integrand at \(-\theta\). The upper
contribution is (3)'s conjugate: changing the variable from
\(\theta\in[\theta_0,\pi]\) to \(-\theta\) reverses the limits as
well as the differential. Both original arcs are counterclockwise.
Thus (1)–(2) bound both arcs, including both values at the negative
axis. The integer power \(u^{-d}\) agrees with \(e^{-d\Log u}\)
on each branch. There is no contour deformation and no connector.

The triangle inequality and the total angular length
\(2(\pi-\theta_0)\) now give
\[
 |I_{\rm out}|
 \leq P_d\left(1-\frac{\theta_0}{\pi}\right)
       C T|a_q(-2\alpha)|e^{dH_q-\gamma(\theta_0)d}.
\]
Divide by the positive scale \(M_d(x)\), and use
\(T\leq C'd/\log d\). The resulting exponential dominates the
displayed polynomial uniformly in \(x\), proving the conclusion.

**Qualifications.** This pays only a fixed-angle exterior relative
to the proposed \(d^{-1/3}\) normalization. It neither shows that
this is the size of the omitted integral nor supplies its sign.
A shrinking cutoff, local cubic coordinate, analytic normalized
amplitude bounds, real reference/orientation, nonzero reference margins,
global root deficit and every-degree hyperbolicity remain separate.
It gives no RH proof, new zero-free region or bound on exceptional roots.

**Critical replay, 17 November 2026 (1347).** The primary v1 HTML
statements and relevant proof cases were checked again: (2.5)–(2.9),
Lemma 7 including its uniform analytic-parameter argument for (3.7),
Lemma 8 including its endpoint-continuity argument, and Lemmas 12–13
including the whole-semicircle and saddle-nonvanishing cases. Only
(4.6), not the local \(C^1\) assertion following (4.7), is used here.
Proposition 15's proof confirms the angular identity (3), without
importing its Gaussian conclusion or its additional range conditions.

There is one common onset for all \(x\in[1,4]\). Indeed, first bound
\(q\) in a fixed positive compact interval using the uniform edge
estimate. Its upper endpoint is eventually below \(c_0T\). After
\(4d^{-2/3}\leq t_0\), choose the uniform constant \(C_\alpha\) in
\(\alpha\leq C_\alpha d^{-1/3}\). The additional explicit requirement
\(C_\alpha^2d^{-2/3}\leq\eta\) ensures
\(1-\cos\alpha\leq\alpha^2/2\leq\eta/2\), exactly the inequality
needed in (2). The same compact interval and (3.6) give a uniform
positive lower bound for \(r\), so \(Tr\geq W_0\) eventually and
the positive lower bound in (1) applies before division.

For an independent orientation check, put
\(b(\theta)=F(T^2r^2e^{i\theta})e^{-dqr^2e^{i\theta}}
(r^2e^{i\theta})^{-d}\). Then
\(b(-\theta)=\overline{b(\theta)}\), and angular substitution gives
\(P_d(2\pi)^{-1}\int b(\theta)\,d\theta\) on each counterclockwise
arc. Thus \(\int_{\theta_0}^{\pi}b(\theta)\,d\theta
=\overline{\int_{-\pi}^{-\theta_0}b(\theta)\,d\theta}\).
At \(\theta=\pm\pi\), the entire function and integer power give
the same real value of \(b\); no branch jump remains in the actual
integrand. Combining the two lengths, the common amplitude ratio
and (2) reproduces the displayed upper bound exactly. The replay
therefore retains the conclusion, with no change to its hypotheses
or argument and no new mathematical input beyond the cited estimates.

## Mathlib

Full matching theorem and supporting formal theorem coverage were not
checked. The source's autoformalization claim is not a verified Lean
artifact in this notebook. This informal specialization relies on the
precisely cited analytic estimates above.
