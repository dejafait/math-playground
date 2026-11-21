# C019i — A growing family of actual Jensen roots in the omitted edge band

## Hypotheses

Let d tend to infinity through positive integers and use the Riemann
xi-function of L018. With the factorial convention of L021, put
\[
 F(z)=\xi(1/2+\sqrt z)=\sum_{j\geq0}\frac{\gamma(j)}{j!}z^j,
 \qquad \gamma(j)=\frac{j!}{(2j)!}M_{2j},\qquad
 J_d(X)=\sum_{j=0}^d\binom dj\gamma(j)X^j.
\]
The square-root expression means the single-valued entire function
specified by the even Taylor expansion. Fix K=Q throughout.
Use C019c's exact conventions and the entire closed band of C019h:
\[
 d=\frac{T}{2\pi}\left(\log\frac{T}{2\pi}-1\right),\quad
 T>2\pi e,\quad \Lambda=2\left(\log\frac{T}{2\pi}-1\right),
 \quad B=T^2,\quad\kappa=\pi/2,
\]
\[
 \kappa r_e\left(1+\frac{2\log r_e}{\Lambda}\right)=2,
 \qquad q_e=r_e^{-2}+\frac{2\kappa}{\Lambda r_e},\qquad
 q_-=q_e+d^{-1/2},\quad q_+=q_e+2d^{-1/2},\quad
 \mathcal B_d=[q_-,q_+].                                    \tag{1}
\]
Here r_e is the positive edge radius selected by the cited source.
For q in this band take its saddle branch
\[
 u_q=r^2e^{-2i\alpha},\quad 0<\alpha<\pi/2,\quad
 \frac{\Lambda\cos\alpha}{\kappa r}+\alpha\cot\alpha
       =\frac{\Lambda}{2}+1+\log r,\quad
 q=r^{-2}+\frac{2\kappa}{\Lambda}\frac{\alpha}{\sin\alpha}r^{-1}.
\]
The lower-semicircle definitions, including branches, are
\[
 \begin{split}
 h_q(u)&=-qu+2\kappa\sqrt u+
       \frac{2\kappa}{\Lambda}\sqrt u\Log u-\Log u,
                  &&-\pi\leq\arg u\leq0,\\
 w_q(\theta)&=Tr e^{i\theta/2},\quad
 a_q(\theta)=2^{-1/4}\pi^{1/4}w_q(\theta)^{7/4}
       \zeta(1/2+w_q(\theta))g_{\mathbb Q}(w_q(\theta)),
                  &&-\pi\leq\theta\leq0,\\
 \theta_q&=-2\alpha,\quad D_q=u_q^2h_q''(u_q),\quad
 P_d=d!/d^d,\quad S(q)=\Im h_q(u_q),\\
 \ell_q&=\epsilon_0\min(\alpha,\cos\alpha),\quad
 n_q=d|D_q|\ell_q^2,\quad
 Z_d(q)=\frac{P_da_q(\theta_q)e^{dh_q(u_q)}}{\sqrt{2\pi dD_q}}.
 \end{split}                                                \tag{2}
\]
Use the principal powers, the exact nonvanishing gamma remainder g_Q
and the fixed sufficiently small epsilon_0 from C019h and its cited
source. In particular sqrt(D_q) is principal. Upper-circle expressions
use conjugate branches. Define the reciprocal and rescaled polynomials
\[
 R_d(y)=y^dJ_d(1/y),\qquad A_d(y)=(B/d)^dR_d(dy/B),           \tag{3}
\]
where the reciprocal polynomial is extended at y=0.

The analytic inputs are C019h's audited complement estimate and the
precise Ono v1 results specified in the proof. No extended bulk cosine
formula, phase bound, root count, simplicity or RH is assumed.

## Conclusion

There exist constants c>0 and d_0 such that, for every integer d>=d_0,
J_d has at least c*d^(1/4) distinct negative real roots with q parameters
strictly in (q_-,q_+), under the exact map
\[
                          X_d(q)=-\frac{T^2}{dq}.           \tag{4}
\]
Equivalently, these roots lie in the open interval
(X_d(q_-),X_d(q_+)). Their sign-change intervals are disjoint from
all the intervals counted in Ono v1 Section 6 with
\[
 I_d=[q_e+\tau,Q],\qquad
 \tau=M\sqrt{\log d/d},\qquad Q=c_0T,                       \tag{5}
\]
for the fixed constants chosen in that source's (5.6).

More precisely, there is a continuous real phase vartheta_d on the
closed band for which, uniformly there,
\[
 \frac{A_d(-q)}{2|Z_d(q)|}=\cos\vartheta_d(q)+E_d(q),\qquad
 |E_d(q)|\leq\eta_d\longrightarrow0,                       \tag{6}
\]
and positive constants k,C_omega, independent of d and q, satisfy
\[
 \vartheta_d(q_+)-\vartheta_d(q_-)\geq k d^{1/4}-2C_\omega.
                                                                  \tag{7}
\]
An admissible c is k/(2 pi) after increasing d_0. All onsets and
constants here are existential. Critical replay1367 below retains this
specialization without a mathematical repair. It neither improves the order
of the source's overall exceptional-root bound nor proves every-degree
hyperbolicity or actual-Xi all-degree positivity.

## Proof

**Citations and the specialization.** The primary source is Ken Ono,
*An Asymptotic Jensen–Pólya Criterion for GRH*,
[arXiv:2610.38870v1](https://arxiv.org/html/2610.38870v1),
28 October 2026. Import (2.7)–(2.10); Lemma 7's continuous saddle
branch and uniform geometry; Lemma 9/(3.13)–(3.14); Corollary 10/
(3.17)–(3.20); Lemma 11/(3.22); Lemma 12/(4.1)–(4.3);
Lemma 13/(4.6)–(4.9); Lemma 14/(5.1); and Proposition 15's local
integral calculation with (5.2)–(5.3). Also use the exact conjugation
identity in Corollary 16's proof, the branch ingredients in Lemma 17/
(6.2), and Section 6's ordered phase-level sign-count method.
Equation (5.6), (2.10) and Remark 18 specify the comparison intervals.

Corollary 16 and Lemma 17 are printed on I_d, not on (1); their
extended conclusions are not imported. The work below checks their
ingredients on (1), replaces only the complementary integral by C019h,
and derives a lower phase span and the corresponding localized count.
Proposition 15/(5.5) is not used with a bounded small upper endpoint Q.
The general Gaussian and intermediate-value theorems are cited, not
reproved. The existing assessment1364/review1365 covers this exact
specialization; its search did not establish originality.

**Actual coefficients and one uniform onset.** L018 gives
Xi(z)=xi(1/2+iz). Substitution in L021's locally uniformly convergent
entire series gives
\[
 \Xi(-i\sqrt z)=\sum_{j\geq0}\frac{M_{2j}}{(2j)!}z^j=F(z).
\]
Both factors (-1)^j cancel; the even powers make the expression
single-valued. This verifies the factorial convention and reality of
J_d; moreover gamma(j)>0 by L021, so J_d is a nonzero degree-d
polynomial. There is no replacement of gamma(j) by raw moments.
Import the Cauchy identity (2.9) in the exact form
\[
 A_d(-q)=\frac{P_d}{2\pi i}
       \oint F(Bu)e^{-dqu}\frac{du}{u^{d+1}}.               \tag{8}
\]
Any positive radius is permitted. For fixed d,q use |u|=r(d,q)^2
with counterclockwise orientation, exactly as in C019h.

C019h, equations (5)–(6) and its common-onset argument, supplies
fixed positive constants a_-,a_+,r_-,r_+,c_D,C_D for which
\[
 a_-d^{-1/4}\leq\alpha\leq a_+d^{-1/4},\quad
 r_-\leq r\leq r_+,\quad
 c_D\alpha\leq|D_q|\leq C_D\alpha,\quad\Re D_q>0          \tag{9}
\]
uniformly on the entire closed band. These are consequences of the
cited uniform geometry, not assumptions of a new root theorem.
Choose the same fixed c_0 as in (5), decreasing it if necessary as
specified in the source. Since q_e=pi^2/16+O(1/Lambda), Lambda tends
to infinity, and T is comparable to d/log d, the band lies in
(q_e,c_0T] for every sufficiently large d. Increase a common onset
until alpha<=1/2, alpha<cos(alpha), Tr>=max(W_0,1), and
1/2+Tr cos(alpha)>=4 throughout the band. All these conditions
follow uniformly from (9). In particular ell_q=epsilon_0 alpha and
\[
 n_q\geq c_n d^{1/4},\qquad
 c_n=\epsilon_0^2c_Da_-^3>0.                               \tag{10}
\]
Thus n_q>=1 eventually. No use of the source's large-Q condition is
hidden in (10), and Lambda and q_e retain their degree dependence.

**Local Gaussian and the full signed error.** Let I_loc^- be the
contribution to (8) of theta in [theta_q-ell_q,theta_q+ell_q].
This interval lies strictly in (-pi,0) by Corollary 10. The change
theta=theta_q+ell_q*y uses its unchanged p_q and Lemma 13's f_q.
Their bounds are uniform in d,q: p_q is C^3, f_q is C^1,
p_q(0)=p_q'(0)=0, p_q''(0)=-D_q/|D_q|, Re p_q<=0,
|p_q'(y)|>=|y|/2, f_q(0)=1, and their stated norms are bounded.
Lemma 9 gives |D_q/|D_q||=1 and Re(D_q/|D_q|)>0.
Together with (10) these verify every hypothesis of Lemma 14.

Its error constant is uniform even as Re(D_q/|D_q|) tends to zero;
no lower bound on that real part is imposed. The local calculation
in Proposition 15 therefore gives a constant C_loc with
\[
 I_{\rm loc}^-=Z_d(q)(1+\delta_{\rm loc}(d,q)),\qquad
 |\delta_{\rm loc}|\leq C_{\rm loc}n_q^{-1/10}
       \leq C_{\rm loc}c_n^{-1/10}d^{-1/40}.                \tag{11}
\]
In detail the prefactor is P_d*ell_q*a_q(theta_q)*exp(dh_q(u_q))
divided by 2 pi; multiplying by sqrt(2 pi/(n_q D_q/|D_q|))
gives exactly Z_d, since ell_q>0. This checks the angular measure
and principal square root without an extra radius or factor two.
The saddle amplitude and Z_d are nonzero by C019h (or Lemma 13).

Fix theta_0=1/10 in C019h. Write its complementary bound as
\[
 \rho_d=C_1d^{-1/8}+C_2d^{-3/8}
       +C_3\frac{d^{11/8}}{\log d}e^{-\gamma d},\qquad
 |R_d^-(q)|\leq\rho_d|Z_d(q)|.                            \tag{12}
\]
It covers both remaining angular intervals with every endpoint.
Their union and the local interval cover the lower semicircle, so
its contribution is exactly L_d=I_loc^-+R_d^-.

For clarity about the sign, set
b(theta)=F(Br^2e^{i theta}) exp(-dqr^2e^{i theta})
r^(-2d)exp(-id theta). This is the single-valued angular integrand
in (8). Reality of F and real q give b(-theta)=conj(b(theta)).
The substitution theta -> -theta in the upper integral reverses
both its limits and its differential. Consequently its increasing-angle
contribution is precisely conj(L_d), as in Corollary 16's proof.
No I_d remainder estimate is used for this identity. Thus
\[
 A_d(-q)=2\Re Z_d(q)+2\Re\{Z_d(q)\delta_{\rm loc}+R_d^-(q)\}.
                                                                  \tag{13}
\]
After division by the positive quantity 2|Z_d| the error is real and
has absolute value at most
\[
 \eta_d=C_{\rm loc}c_n^{-1/10}d^{-1/40}+\rho_d=o(1).        \tag{14}
\]
Choose one enlarged onset so that eta_d<1/2 for every later d.
This is a full signed assembly; the complement modulus alone would
not imply a sign.

**The phase on the new band.** Write v_q=r exp(-i alpha). Lemma 7
makes r and alpha continuous in q for fixed d. The same is true of
D_q, whose real part is positive. The saddle has |Tv_q|=Tr>=W_0
and |arg(Tv_q)|=alpha<pi/2. Lemma 12 therefore supplies its one
holomorphic log(g_Q), with |log(g_Q(Tv_q))|<=G/(Tr) for a constant G.
The saddle zeta argument has real part at least 4 by the onset above.
Use the absolutely convergent Euler-product logarithm there; it is
continuous and has absolute value at most log(zeta(4)). The principal
Arg D_q is continuous in the right half-plane and has modulus <pi/2.
All of Lemma 17's branch ingredients thus hold on this band.

Since the field specialization has mu_Q=7/4 and
c_Q=2^(-1/4)pi^(1/4)>0, define exactly
\[
 \begin{split}
 \omega_d(q)&=-\frac74\alpha
   +\Im\Log\zeta(1/2+Tv_q)+\Im\log g_{\mathbb Q}(Tv_q)
   -\frac12\Arg D_q,\\
 \vartheta_d(q)&=dS(q)+\omega_d(q).
 \end{split}                                                \tag{15}
\]
Every term is continuous. From Tr>=1 and alpha<pi/2 a fixed bound is
\[
 |\omega_d(q)|\leq C_\omega,
 \qquad C_\omega=\frac{9\pi}{8}+\log\zeta(4)+G.             \tag{16}
\]
The positive factors P_d,c_Q,(Tr)^(7/4) and sqrt(2 pi d) do not
contribute an argument; the principal powers and square root give
the other terms in (15). Hence Z_d=|Z_d| exp(i vartheta_d) exactly.
Equations (13)–(16) prove (6) on the new band, not merely on I_d.

**A lower span and strict open root intervals.** For each fixed d,
Lambda,T and q_e are constant while q varies. Import Lemma 11/(3.22),
which applies to this saddle branch:
\[
                         S'(q)=r^2\sin(2\alpha).
\]
For 0<=2 alpha<=1, sin(2 alpha)>=alpha. Thus (9) gives on all of
the band
\[
 S'(q)\geq r_-^2a_-d^{-1/4}.
\]
Integrate between the exact endpoints of (1), whose difference is
d^(-1/2). With k=r_-^2a_->0, this yields
\[
 d\{S(q_+)-S(q_-)\}\geq k d^{1/4}.
\]
Together with (16) this proves (7). No subtraction of the source's
two upper bounds (3.23) is involved, and no monotonicity of the
corrected phase vartheta_d is claimed.

Apply Section 6's ordered integer-level method with
\[
 k_{\min}=\left\lceil\vartheta_d(q_-)/\pi\right\rceil,
 \qquad
 k_{\max}=\left\lfloor\vartheta_d(q_+)/\pi\right\rfloor.
                                                                  \tag{17}
\]
When d is large, (7) gives k_max>k_min. Continuity supplies ordered
points t_k with vartheta_d(t_k)=k*pi, q_-<=t_k<t_(k+1)<=q_+:
after a chosen point the right endpoint still has phase at least
(k+1)pi, which is the hypothesis for the source's next hitting step.
At these points (6), eta_d<1/2 and |Z_d|>0 give strict signs
sign(A_d(-t_k))=(-1)^k. The intermediate value theorem therefore
supplies a zero in each (t_k,t_(k+1)). These intervals are open,
pairwise disjoint, and contained strictly in (q_-,q_+), even when
the first or last sign sample is a band endpoint. There is no
endpoint root being counted and no multiplicity or uniqueness claim.

The number of these intervals is exactly k_max-k_min, and rounding
in (17) gives the lower bound
\[
 \begin{split}
 k_{\max}-k_{\min}
 &\geq\frac{\vartheta_d(q_+)-\vartheta_d(q_-)}{\pi}-2\\
 &\geq\frac{k}{\pi}d^{1/4}-\frac{2C_\omega}{\pi}-2.
 \end{split}                                                \tag{18}
\]
Increase the onset until (k/2)*d^(1/4)>=2C_omega+2*pi.
Then (18) is at least c*d^(1/4) for c=k/(2*pi)>0.
The integer interpretation causes no further loss: an integer count
bounded below by this real number is the asserted count.

**Actual roots and bulk separation.** The exact identity (2.10), or
direct substitution in (3), gives
\[
             A_d(-q)=(-q)^d J_d\!\left(-\frac{B}{dq}\right).
                                                                  \tag{19}
\]
Since q_e>0, every q here is positive, (-q)^d is nonzero, and
X_d'(q)=B/(d q^2)>0. Thus (19) transfers the zeros and their
disjoint open intervals to distinct negative zeros of the actual J_d.
Signs of J_d itself differ by the fixed parity (-1)^d, which does
not affect the zero correspondence.

Use the exact source constants M>0 and c_0>0 in (5), not the coarse
containing interval in Remark 18. For every sufficiently large d,
M*sqrt(log d)>2, so
\[
        q_+=q_e+2d^{-1/2}<q_e+M\sqrt{\log d/d}=q_e+\tau.
                                                                  \tag{20}
\]
Also q_e+tau<Q eventually, as in the source. Since the reciprocal
map is strictly increasing, (20) gives
\[
 X_d(q_+)<X_d(q_e+\tau),
\]
and the interval of roots just proved is strictly to the left of the
source's exact counted interval
[X_d(q_e+tau),X_d(Q)]. This proves separation from every open
sign-count interval used in its Section 6. It does not assert that
the source excludes other roots on our band.

There are finitely many onset requirements above, all uniform on the
closed band; their maximum gives a single d_0. This completes the
approved target without a numerical certificate or an effective d_0.

**Qualifications.** This is local progress by a specialization of
established methods and cited inputs, not a certified novelty claim.
The inspected source's printed theorem did not localize these roots,
but its much larger bulk count remains the main count. Recovering this
family alone does not remove its near-edge loss of order
d^(1/4)(log d)^(3/4) or its larger far-end loss of order sqrt(d log d).
Those are losses in a lower-bound argument, not known nonreal zeros.
The C019g fixed-window result and stops1345/1355/559 are unchanged;
no compact Airy limit is evaluated on a growing window. The manuscript
has not been audited source-wide and its formal artifacts have not been
replayed here. The separate conceptual audit below retains this local
application. Full hyperbolicity and the main RH gap remain open.

**Critical replay, 17 November 2026 (1367).** Under the unchanged
SPECIALIZE assessment1364/review1365, this first separate conceptual
audit read the whole proof and checked the source hypotheses used in
the changed band. No error in the conclusion or its proof was found.
The following is verification of the existing application, not a new
root theorem or an independent source-wide certification.

The primary passages checked against the v1 linked above were Lemma 7,
including (3.11)'s uniform near-edge proof; Lemma 9; Corollary 10 and
its local derivative proof; Lemma 11/(3.22); Lemma 12's logarithm;
Lemma 13's stated local amplitude bounds; the complete Lemma 14 proof;
Proposition 15's local calculation; Corollary 16's conjugation identity;
Lemma 17/(6.2); and Section 6 through Remark 18. The general theorems
are imported by those citations; the replay below checks their use.

1. **Common onset and local range.** The whole band is eventually
   contained in (q_e,c_0 T], since q_e tends to pi^2/16 and T tends
   to infinity. C019h's uniform constants in (9) give
   ell_q=epsilon_0 alpha and n_q>=epsilon_0^2 c_D a_-^3 d^(1/4).
   Both band endpoints are strictly above q_e. The same constants
   make Tr large and Re(1/2+Tr exp(-i alpha))>=4. Each required
   inequality persists for every sufficiently large d, so the finite
   maximum of their onsets is legitimate. No bounded-Q use of (5.5)
   or substitution into a fixed-window Airy limit occurs.

2. **The nearly imaginary quadratic coefficient.** The normalized
   functions used in (11) have the stated uniform C3/C1 bounds,
   derivative lower bound and nonpositive real phase; f_q(0)=1.
   These are precisely the hypotheses of Lemma 14, with
   A=D_q/|D_q|, whose real part is positive but need not have a
   uniform positive lower bound. Its proof bounds both finite and
   infinite tails by cancellation, with constants independent of
   Re A. In particular the boundary at infinity is zero for each
   Re A>0, while the resulting bound uses |A|=1; no uniform
   exponential-decay rate is needed. Hence the relative error
   C_loc n_q^(-1/10) is valid here. Multiplication by the local
   angular prefactor gives exactly (11), on the principal square
   root, and its worst band rate is d^(-1/40).

3. **Full signed normalization.** C019h supplies both omitted
   lower intervals, with all endpoints and the same P_d and Z_d.
   The angular integrand in (8) has b(-theta)=conj(b(theta)), so
   the upper contribution equals the conjugate of the lower with
   no orientation sign. Division of (13) by 2|Z_d| gives exactly
   the real error in (14), bounded by the sum, not twice that sum.
   The rates d^(-1/40), d^(-1/8), d^(-3/8) and the exponentially
   small term all vanish. The leading term is nonzero and the
   normalization is positive. A single eventual bound eta_d<1/2
   therefore preserves both signs at every phase barrier.

4. **No hidden winding or phase assumption.** The Euler-product
   logarithm is available on the whole band in Re s>=4; the fixed
   gamma logarithm is available in the closed right sector; and
   D_q stays in the right half-plane. Formula (15) is consequently
   a continuous real lift, including -7 alpha/4 and -Arg D_q/2.
   Their combined absolute bound is 7 pi/8+pi/4=9 pi/8; the two
   remaining terms give exactly the rest of C_omega in (16).
   No zeta logarithm near the critical line or unstated global
   argument principle is used.

5. **Lower span and ordered count.** For fixed d, neither Lambda
   nor q_e varies during the q-integration. The exact derivative
   is positive and obeys S'>=r_-^2 a_- d^(-1/4) because
   sin(2 alpha)>=alpha when 2 alpha<=1. The width d^(-1/2)
   and the outer factor d give k d^(1/4), as asserted. Subtracting
   two bounded correction values costs at most 2C_omega. Starting
   at q_-, continuity reaches k_min*pi; after any chosen hitting
   point it reaches the next larger level at or before q_+, since the
   latter's phase is at least k_max*pi. Successive points are
   strictly ordered because their phase values differ. This needs
   no monotonicity of vartheta_d. Floor and ceiling cost at most
   two in the number of intervening intervals, so (18) and the
   chosen c=k/(2 pi) follow with the stated onset. Band endpoints
   can be samples, but never roots counted by these open intervals.

6. **Actual family, separation and qualifications.** L018/L021
   give gamma(j)=j! M_(2j)/(2j)!, with positive leading coefficient.
   Direct substitution in (3) confirms (19); the map has derivative
   B/(d q^2)>0 and no zero or pole on the band. The inequality
   2<M sqrt(log d) establishes strict separation from the exact
   bulk q interval before applying the same injective map. It
   does not exclude additional roots counted by other methods.
   Distinct sign intervals give distinct roots, with neither
   uniqueness nor simplicity. The larger far-end loss and the
   source's remaining near-edge loss are not paid by this result.

This audit establishes the local applicability and assembly recorded
above without changing the statement, constants, direct inputs or
argument. No numerical certificate, new mathematical script, effective
onset, source-wide validation or formal verification is claimed. The
unresolved all-degree sign problem remains exactly that in the notebook.

## Mathlib

Full matching theorem and supporting Mathlib coverage have not been
checked; availability is unknown, not asserted absent. The cited
primary's Appendix advertises a separate Lean repository, which is
an unread artifact lead rather than formal verification of this
specialization. No new mathematical script is needed: the uniform
estimates and finite root-counting argument are written above.
