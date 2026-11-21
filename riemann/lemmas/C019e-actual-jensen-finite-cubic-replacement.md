# C019e — Actual Jensen local integral: an additive finite cubic replacement

## Hypotheses

Use C019c's exact data for the fixed field \(K=\mathbb Q\): positive
integers \(d\to\infty\), \(1\leq x\leq4\),
\(q=q_e+xd^{-2/3}\), its saddle \(u_q=r^2e^{-2i\alpha}\),
\(T,\Lambda,\kappa=\pi/2\), phase \(h_q\), amplitude \(a_q\), and
\(H_q=\Re h_q(u_q)\). In particular
\[
 h_q(u)=-qu+2\kappa\sqrt u+
       \frac{2\kappa}{\Lambda}\sqrt u\Log u-\Log u,
 \qquad P_d=\frac{d!}{d^d},\qquad
 M_d(x)=P_d|a_q(-2\alpha)|e^{dH_q}d^{-1/3}.
\]
Keep its actual radius \(r^2\), prefactor and both counterclockwise
arc orientations. Fix \(0<\theta_0\leq1/10\), and put
\(\epsilon=(\log d)d^{-1/3}\). For \(d\) large enough that
\(\epsilon<\theta_0\), let
\[
 I_{\rm loc}=\frac{P_d}{2\pi i}
  \int_{\substack{u=r^2e^{i\theta}\\|\theta|\leq\epsilon}}
       F(T^2u)e^{-dqu}\frac{du}{u^{d+1}},
 \qquad F(z)=\xi(1/2+\sqrt z).
\]
On this neighborhood of the positive real axis use the common principal
branches and define the exact, degree-dependent quantities
\[
 \Psi(\theta)=h_q(r^2e^{i\theta}),\qquad
 \mathcal T_3(\theta)=\sum_{j=0}^3
           \frac{\Psi^{(j)}(0)}{j!}\theta^j,\qquad
 I_3=\frac{P_da_q(0)}{2\pi}
          \int_{-\epsilon}^{\epsilon}e^{d\mathcal T_3(\theta)}d\theta.
\]
Use the fixed constants \(B_0,B_1\) established in C019d for the
normalized amplitude and its actual angular derivative. No local
integral lower bound, infinite Airy integral or sign is assumed.

## Conclusion

There is a common onset, independent of \(x\in[1,4]\), such that
\(M_d(x)>0\) and
\[
 \boxed{\quad
 \frac{|I_{\rm loc}-I_3|}{M_d(x)}
 \leq d^{-1/3}\left[
       \frac{B_1}{2\pi}(\log d)^2+
       \frac{B_0}{24\pi}e^{\delta_d}(\log d)^5\right],
 \qquad \delta_d=\frac5{24}d^{-1/3}(\log d)^4.
 \quad}                                                     \tag{1}
\]
In particular the supremum over \(1\leq x\leq4\) is
\(O(d^{-1/3}(\log d)^5)=o(1)\). Constants and onset are existential.
This is a finite Taylor specialization of assessed source inputs,
retained after the critical replay1353 below. It gives no sign.

## Proof

**Inputs and scope.** C019c supplies the exact factorization, positive
saddle normalization, uniform compact bounds and actual-phase envelope;
C019d supplies the exact saddle identities and the normalized amplitude
bounds on the larger fixed angular interval including zero. Their source
is Ken Ono, *An Asymptotic Jensen–Pólya Criterion for GRH*,
[arXiv:2610.38870v1](https://arxiv.org/html/2610.38870v1),
28 October 2026, (3.2), Lemma7/(3.6)–(3.9), Lemma8/(3.12),
Lemma12/(4.3), (4.4)–(4.5), and the half-plane proof of Lemma13.
We import the exact exponential-difference identity in Lemma14's proof
and apply the standard Taylor theorem with integral remainder to a
complex-valued C4 function of the real angular variable. The necessary
fourth-derivative and interpolation bounds are proved below: the source's
order-three bound and its Gaussian conclusion do not give (1).

**Common branch and fourth derivative.** Use C019d's common onset, so
\(0<\alpha\leq1\), \(\epsilon<\theta_0\), and, with
\[
 A=qr^2,\qquad C=\frac{2\kappa r}{\Lambda},\qquad
 R=\frac{\alpha}{\sin\alpha},\qquad
 E=2\kappa r+2C\log r,
\]
we have \(0<C\leq1\), \(1\leq R\leq2\), and
\[
 A-1=CR,\qquad 1\leq A\leq3,\qquad
 E=2(A+1)\cos\alpha-2C,\qquad |E|\leq10.             \tag{2}
\]
The formula for \(E\) is the exact saddle identity
\(\kappa r+C(1+\log r)=(A+1)\cos\alpha\), with no
\(1/\Lambda\) term discarded.

For \(|\theta|\leq\theta_0<\pi\), the point
\(r^2e^{i\theta}\) avoids the principal logarithm's cut. Thus
\(\Log(r^2e^{i\theta})=2\log r+i\theta\) and
\(\sqrt{r^2e^{i\theta}}=re^{i\theta/2}\) on both sides of zero.
These branches are analytic on a neighborhood of the entire retained
arc, and the phase is exactly
\[
 \Psi(\theta)=-Ae^{i\theta}+(E+iC\theta)e^{i\theta/2}
                      -2\log r-i\theta.                    \tag{3}
\]
In particular it is C4 across zero and
\(\Psi(-\theta)=\overline{\Psi(\theta)}\).
Differentiating (3) four times gives
\[
 \Psi^{(4)}(\theta)=-Ae^{i\theta}
     +\left(\frac E{16}+\frac C2+\frac{iC\theta}{16}\right)
                                                    e^{i\theta/2}.
\]
The product-rule contribution from differentiating \(iC\theta\)
is \(4(iC)(i/2)^3=C/2\). Hence, for real
\(|\theta|\leq\theta_0\leq1/10\), (2) yields
\[
 |\Psi^{(4)}(\theta)|
 \leq3+\frac{10+1/10}{16}+\frac12
 =\frac{661}{160}<5.                                      \tag{4}
\]
All constants in (4) are independent of \(d,x\).

For clarity, all four coefficients retained by the proposed comparison are
\[
 \mathcal T_3(\theta)=-A+E-2\log r
   +i(-A+C+E/2-1)\theta
   +\tfrac12(A-C-E/4)\theta^2
   +\tfrac i6(A-3C/4-E/8)\theta^3.                         \tag{5}
\]
They have not been replaced by limiting coefficients. Taylor's theorem
on the real segment from zero to either sign of \(\theta\) gives
\[
 \Psi(\theta)-\mathcal T_3(\theta)
  =\frac{\theta^4}{6}\int_0^1(1-t)^3\Psi^{(4)}(t\theta)\,dt,
 \qquad
 |\Psi(\theta)-\mathcal T_3(\theta)|
       \leq\frac5{24}|\theta|^4.                          \tag{6}
\]

**Actual and cubic exponentials.** The actual-phase envelope from
C019c, using source Lemma8/(3.12), gives \(\Re\Psi\leq H_q\)
on the lower interval; conjugation gives the same on the upper one.
For \(|\theta|\leq\epsilon\), (6) therefore implies
\[
 \Re(d\mathcal T_3)\leq dH_q+\delta_d,\qquad
 \Re\{t d\Psi+(1-t)d\mathcal T_3\}\leq dH_q+\delta_d
                  \quad(0\leq t\leq1).                   \tag{7}
\]
Apply the exact source Lemma14 identity
\[
 e^{z_1}-e^{z_2}=(z_1-z_2)
                   \int_0^1e^{t z_1+(1-t)z_2}\,dt
\]
with \(z_1=d\Psi\), \(z_2=d\mathcal T_3\). Equations (6)–(7)
prove the complete local bound
\[
 |e^{d\Psi}-e^{d\mathcal T_3}|
 \leq\frac{5d}{24}|\theta|^4 e^{dH_q+\delta_d}.           \tag{8}
\]
We have not assumed \(\Re\mathcal T_3\leq H_q\) or used the
source's contraction inequality without its real-part hypotheses.

**Amplitude across zero and its variation.** C019d gives, on
\([-\theta_0,0]\),
\[
 |a_q(\theta)|\leq B_0|a_q(-2\alpha)|,\qquad
 |a_q'(\theta)|\leq B_1|a_q(-2\alpha)|.                    \tag{9}
\]
There is a common analytic amplitude at zero. Indeed the exact
factorization identifies it on the lower interval with
\[
 b(\theta)e^{-d\Psi(\theta)},\qquad
 b(\theta)=F(T^2r^2e^{i\theta})e^{-dqr^2e^{i\theta}}
                                        (r^2e^{i\theta})^{-d}.
\]
The right side is analytic on a neighborhood of zero and of this local
arc. Real coefficients of \(F\), real \(q,r\), integer \(d\) and
(3) show that its value at \(-\theta\) is the conjugate of its value
at \(\theta\). Thus it agrees with the prescribed conjugate amplitude
on the upper arc, with \(a_q(0)\) real and no jump. Differentiating
that conjugation relation preserves the derivative modulus, so (9)
extends to the upper interval. Integration of the derivative along
the segment from zero to \(\theta\) now gives
\[
 \frac{|a_q(\theta)-a_q(0)|}{|a_q(-2\alpha)|}
       \leq B_1|\theta|,\qquad
 \frac{|a_q(0)|}{|a_q(-2\alpha)|}\leq B_0.                \tag{10}
\]
Only the already nonzero saddle amplitude is divided out.

**Integration and unchanged normalization.** On both counterclockwise
arcs \(du/u=i\,d\theta\), with \(\theta\) increasing. Source
(4.5) includes \(u^{-d}\), so their sum is exactly
\[
 I_{\rm loc}=\frac{P_d}{2\pi}
         \int_{-\epsilon}^{\epsilon}a_q(\theta)e^{d\Psi(\theta)}d\theta.
\]
There is no orientation minus sign, connector or additional radius factor.
Subtract \(I_3\) using the exact decomposition
\[
 a_q(\theta)e^{d\Psi}-a_q(0)e^{d\mathcal T_3}
 =(a_q(\theta)-a_q(0))e^{d\Psi}
       +a_q(0)(e^{d\Psi}-e^{d\mathcal T_3}).
\]
Equations (8)–(10) and \(|e^{d\Psi}|\leq e^{dH_q}\) imply
\[
 \begin{split}
 |I_{\rm loc}-I_3|
 &\leq\frac{P_d|a_q(-2\alpha)|e^{dH_q}}{2\pi}
   \int_{-\epsilon}^{\epsilon}
       \left(B_1|\theta|+\frac{5B_0d}{24}e^{\delta_d}|\theta|^4\right)d\theta\\
 &=\frac{P_d|a_q(-2\alpha)|e^{dH_q}}{2\pi}
           \left(B_1\epsilon^2+\frac{B_0d}{12}e^{\delta_d}\epsilon^5\right).
 \end{split}                                                \tag{11}
\]
Here the two full-interval moments are exactly \(\epsilon^2\) and
\(2\epsilon^5/5\). Divide (11) by the positive \(M_d(x)\):
\(d^{1/3}\epsilon^2=d^{-1/3}(\log d)^2\) and
\(d^{4/3}\epsilon^5=d^{-1/3}(\log d)^5\), giving (1).
Since \(\delta_d\to0\), its right side tends to zero independently
of \(x\). The common onset already established in C019c/C019d
suffices after the displayed fixed requirements; no pointwise-in-\(x\)
limit or exchange of an infinite integral is used.

**Qualifications and downstream use.** Combining this additive bound
with the already paid exterior and annulus permits a later comparison
of the actual circle integral with this finite \(I_3\) on the same
positive scale. This proof neither evaluates \(I_3\) nor establishes
its size, sign, nonvanishing or a lower bound. It does not extend the
finite interval to an infinite Airy contour or divide by a possibly
zero reference. Such a signed reference, exceptional-root control,
every-degree hyperbolicity and actual-Xi all-degree positivity remain
open. The automatic-Airy import stop remains unaffected. The local
specialization is not a claim of a discovery beyond the sources checked
and is not a foundational audit of the source manuscript.

**Critical replay, 17 November 2026 (1353).** This replay checks the
stated finite replacement, not the Gaussian formula or a signed Airy
limit. The primary v1 passages checked against the inputs are (2.5)–(2.9),
(3.2), Lemma7/(3.3)–(3.9), Lemma8/(3.12) including its endpoint case,
Lemma12/(4.1)–(4.3) and its gamma-remainder proof, (4.4)–(4.5), the
half-plane bounds in Lemma13's proof, and the exponential identity
in Lemma14's proof. These are the previously assessed sources, not
an extension of their stated conclusions. In particular the local
rescaled C1 assertion of Lemma13 is not substituted for C019d's
actual angular derivative bound.

Here is a direct coefficient check. Multiplying source (3.8) by r
gives A-1=CR. Multiplying (3.9) by r gives
\((A+1)\cos\alpha=\kappa r+C(1+\log r)\), hence the exact E
in (2). Since \(0<\alpha\leq1\), \(1\leq R\leq2\) and
\(0<C\leq1\), we have A in [1,3] and
\(|E|\leq2(A+1)+2C\leq10\). In the product
\((E+iC\theta)e^{i\theta/2}\), the first three derivatives at zero
are respectively \(i(E/2+C)\), \(-E/4-C\), and
\(-i(E/8+3C/4)\). Adding the derivatives of the other terms of
(3) reproduces every coefficient of (5), including the constant
\(-A+E-2\log r\) and the linear contribution \(-i\theta\).
For the fourth derivative the two product terms are
\((E+iC\theta)/16\) and C/2, which reproduce (4).
The arithmetic is \(3+10/16+1/2+1/160=661/160<5\).
The real-segment integral remainder has weight integral 1/4;
thus its factor is 5/(6*4)=5/24 for either sign of theta.

For an independent modulus check set
\(U=d(\Psi-H_q)\) and \(V=d(\mathcal T_3-H_q)\).
The imported envelope gives \(\Re U\leq0\); (6) gives
\(|U-V|\leq5d|\theta|^4/24\leq\delta_d\) and
\(\Re V\leq\delta_d\). Hence every interpolation exponential
has modulus at most \(e^{\delta_d}\), and multiplying the
exponential-difference identity by \(e^{dH_q}\) recovers (8).
No nonpositive-real-part assertion for V is needed.

The branch check uses an open neighborhood of the positive arc,
not boundary values on the negative axis. There the principal powers
are analytic and the actual integrand b is analytic as a function of
theta. The quotient \(b e^{-d\Psi}\) therefore continues the exact
lower amplitude through zero. Since b and Psi obey conjugation on
this neighborhood, its real restriction obeys
\(a_q(-\theta)=\overline{a_q(\theta)}\) and
\(a_q'(-\theta)=-\overline{a_q'(\theta)}\).
This verifies the upper derivative bound, continuity at zero and
(10) with the same B0 and B1. The saddle denominator is nonzero
by C019c; on the fixed small interval C019d verifies the stronger
half-plane nonvanishing needed for its amplitude estimates.

Finally each counterclockwise arc contributes \(P_d/(2\pi)\)
times its angular integral. Combining increasing theta intervals
[-epsilon,0] and [0,epsilon] gives exactly the finite integral used
in (11). The amplitude error integrates to B1*epsilon^2; the phase
error integrates to
\((5B_0d/24)e^{\delta_d}(2\epsilon^5/5)
= (B_0d/12)e^{\delta_d}\epsilon^5\).
After division by M_d these are the two terms in (1), without any
division by I3 or by a limiting reference. All constants are fixed:
C019c/C019d give common onsets and uniform r, alpha, amplitude and
phase bounds, while epsilon and delta_d depend only on d and tend
to zero. Their finitely many onset conditions are compatible.

The replay finds no failed inequality, branch jump, missing arc,
normalization factor or hidden pointwise-in-x limit. It retains (1)
with the same hypotheses and the same direct inputs C019c/C019d.
This verifies a local specialization; it neither strengthens the rate
nor supplies a sign theorem, global root count, foundational audit
of the full source manuscript or verification of its formal artifacts.

## Mathlib

Full matching theorem and supporting formal theorem coverage were not
checked. No claimed source autoformalization has been verified here.
The cited Taylor and exponential-difference tools are applied informally;
the degree-uniform derivative, interpolation and integrated bounds needed
for this exact specialization are written out above.
