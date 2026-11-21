# C019h — Moving-saddle complement on the d^(-1/2) edge band

## Hypotheses

Fix the field K=Q and let d tend to infinity through positive integers.
Use the exact phase, amplitude and saddle conventions of C019c/C019d,
from Ken Ono, *An Asymptotic Jensen–Pólya Criterion for GRH*,
[arXiv:2610.38870v1](https://arxiv.org/html/2610.38870v1),
28 October 2026, equations (2.5)–(3.5) and (4.4)–(4.5).
Explicitly, kappa=pi/2, T>2 pi e is determined by
\[
 d=\frac{T}{2\pi}\left(\log\frac{T}{2\pi}-1\right),\qquad
 \Lambda=2\left(\log\frac{T}{2\pi}-1\right),
\]
and the positive edge parameters satisfy
\[
 \kappa r_e\left(1+\frac{2\log r_e}{\Lambda}\right)=2,
 \qquad q_e=r_e^{-2}+\frac{2\kappa}{\Lambda r_e}.
\]
The parameter range in this result is exactly
\[
                 d^{-1/2}\leq q-q_e(d)\leq2d^{-1/2}.       \tag{1}
\]
Take the source's Lemma 7 saddle u_q=r^2 exp(-2i alpha), with
r>0 and 0<alpha<pi/2 determined by
\[
 \frac{\Lambda\cos\alpha}{\kappa r}+\alpha\cot\alpha
       =\frac{\Lambda}{2}+1+\log r,\qquad
 q=r^{-2}+\frac{2\kappa}{\Lambda}\frac{\alpha}{\sin\alpha}r^{-1}.
\]
For -pi<=theta<=0 use the lower branch -pi<=arg u<=0 and define
\[
 \begin{split}
 h_q(u)&=-qu+2\kappa\sqrt u+
              \frac{2\kappa}{\Lambda}\sqrt u\Log u-\Log u,\\
 w_q(\theta)&=Tr e^{i\theta/2},\\
 a_q(\theta)&=2^{-1/4}\pi^{1/4}w_q(\theta)^{7/4}
          \zeta(1/2+w_q(\theta))g_{\mathbb Q}(w_q(\theta)),
 \end{split}                                               \tag{2}
\]
where g_Q is the exact nonvanishing gamma remainder of source Lemma 12,
with its principal powers. Put
\[
 \theta_q=-2\alpha,\quad D_q=u_q^2h_q''(u_q),\quad
 H_q=\Re h_q(u_q),\quad P_d=d!/d^d.
\]
Fix once and for all the sufficiently small positive epsilon_0 of
source Corollary 10, chosen in (0,1), and use its unchanged interval
\[
 \ell_q=\epsilon_0\min(\alpha,\cos\alpha),\qquad
 E_q=[-\pi,\theta_q-\ell_q]\ \cup\ [\theta_q+\ell_q,0].
\]
Both intervals have increasing angular orientation. Define
\[
 R_d^-(q)=\frac{P_d}{2\pi}\int_{E_q}
            a_q(\theta)e^{dh_q(r^2e^{i\theta})}\,d\theta,
 \qquad
 Z_d(q)=\frac{P_da_q(\theta_q)e^{dh_q(u_q)}}{\sqrt{2\pi dD_q}},       \tag{3}
\]
with the principal square root. No local-integral approximation,
root count, sign margin, or conclusion of RH is assumed.

## Conclusion

For every fixed 0<theta_0<=1/10 there are positive constants
C_1,C_2,C_3,gamma and a common onset d_0, independent of q in (1),
such that Z_d(q) is nonzero and
\[
 \boxed{\quad
 \frac{|R_d^-(q)|}{|Z_d(q)|}
 \leq C_1d^{-1/8}+C_2d^{-3/8}
       +C_3\frac{d^{11/8}}{\log d}e^{-\gamma d}.
 \quad}                                                       \tag{4}
\]
In particular the supremum of this ratio on (1) tends to zero and is
eventually <1/4. The constants and onset are existential, with dependence
on the fixed epsilon_0 and theta_0 allowed. This is a quantitative
specialization of established oscillatory integration by parts, retained
by critical replay1364 below; it is not a sign or hyperbolicity theorem.

## Proof

**Inputs and the difference being proved.** Import Ono v1 Lemma 7,
especially (3.6)–(3.9) and its uniform near-edge proof; Lemma 8/(3.12)
including the closed-arc endpoints; Lemma 9/(3.13)–(3.14); Corollary 10's
definition (3.17); Lemma 12/(4.2)–(4.3); Lemma 13/(4.6) and the
half-plane Euler-product inequalities in its proof; and the finite
integration-by-parts identity in Lemma 14's proof. Proposition 15,
(5.2)–(5.3) and its angular substitution, fix the normalization.
These are precise citations to the primary version linked above.
They are imported, not reproved as general theorems.

C019c supplies the exact angular factorization conventions and C019d
the exact derivative algebra. Their fixed-x conclusions are not used
on (1). All band-dependent inequalities below are justified anew.
The source's absolute complement estimate (5.4) does not tend to zero
on (1), since d(q-q_e)^2 stays bounded. The additional work here is
the oscillatory estimate on both sides of the source saddle interval.

**One uniform onset and an exact partition.** Equation (2.7) of the
source gives Lambda tending to infinity and T comparable to d/log d.
Lemma 7 gives q_e=pi^2/16+O(1/Lambda). Consequently q stays in a fixed
positive compact interval on (1). For all large d, this entire interval
is contained in (q_e,c_0 T] as needed in Lemma 13, where c_0>0 is
fixed as in that lemma. Moreover 2d^(-1/2)<=t_0 eventually, so the
uniform near-edge estimate (3.7) and (3.6) give fixed positive constants
\[
 a_-d^{-1/4}\leq\alpha\leq a_+d^{-1/4},\qquad
             0<r_-\leq r\leq r_+<\infty.                    \tag{5}
\]
In particular W=Tr tends to infinity uniformly. Lemma 9 gives, after
enlarging the same onset,
\[
 0<c_D\alpha\leq|D_q|\leq C_D\alpha,\qquad \Re D_q>0.       \tag{6}
\]

Set b=theta_0/2, s=epsilon_0/2, u=1-s and v=1+s. Thus 0<u<1<v.
Choose the onset so that alpha<=b<=1/20, v alpha<b,
alpha<cos(alpha), and C:=2 kappa r/Lambda<=1. These all follow
uniformly from (5). Then ell_q=epsilon_0 alpha exactly, and E_q
is the union of the following three intervals (shared endpoints do
not affect the integrals):
\[
 I_{\rm far}=[-\pi,-\theta_0],\quad
 I_{\rm out}=[-\theta_0,-2v\alpha],\quad
 I_{\rm in}=[-2u\alpha,0].                                 \tag{7}
\]
There is no omitted interval between the saddle neighborhood and zero.
Lemma 13 makes a_q(theta_q) nonzero; (6) makes division by Z_d legitimate.
The source local parameter also satisfies
n_q=d|D_q|ell_q^2 comparable to d alpha^3 comparable to d^(1/4),
so n_q>=1 at the same enlarged onset. This checks the local range if
the source's local Gaussian estimate is used subsequently; no such
estimate is needed to prove (4).

**Exact derivative, on both sides of the saddle.** Put
\[
 \phi(\theta)=h_q(r^2e^{i\theta})-h_q(u_q),\quad
 \beta=-\theta/2,\quad z=e^{-i\beta},\quad A=qr^2,\quad
 R=\alpha/\sin\alpha.
\]
The exact saddle equations (3.8)–(3.9) imply
\[
 A-1=CR,\qquad
 \kappa r\left(1+\frac{2+2\log r}{\Lambda}\right)
                =(A+1)\cos\alpha.
\]
Thus C019d's algebraic identity, which used only these equations and
differentiation of (2), remains valid here:
\[
 \begin{split}
 \phi'(\theta)
 &=i[-Az^2+((A+1)\cos\alpha-iC\beta)z-1]\\
 &=iz(U(\beta)+iV(\beta)),\\
 U(\beta)&=(A+1)(\cos\alpha-\cos\beta),\qquad
 V(\beta)=C(R\sin\beta-\beta).                         \tag{8}
 \end{split}
\]
In particular the 1/Lambda terms have not been discarded. The functions
U and V are real on these intervals. For 0<=alpha,beta<=1/20,
sin(t)>=t/2 on the interval between them gives
\[
 |\cos\alpha-\cos\beta|\geq\tfrac14|\alpha^2-\beta^2|.
\]
Since A>=1, equation (8) yields
\[
               |\phi'|\geq |U|\geq\tfrac12|\beta^2-\alpha^2|.
                                                                  \tag{9}
\]
Define the fixed positive numbers
\[
                 k_-=(1-u^2)/2,\qquad k_+=(1-v^{-2})/2.
\]
The endpoint and outer intervals then satisfy respectively
\[
 \begin{array}{ll}
 I_{\rm in}:& |\phi'|\geq k_-\alpha^2,\quad 0\leq\beta\leq u\alpha,\\
 I_{\rm out}:& |\phi'|\geq k_+\beta^2,\quad v\alpha\leq\beta\leq b.
 \end{array}                                                    \tag{10}
\]
Both bounds hold at their endpoints. In particular phi' never vanishes
on either closed integration interval; at theta=0 its size is of
order alpha^2. The former restriction beta>=2 alpha in C019d is
neither used nor asserted on the endpoint side.

We also need the actual angular second derivative. The elementary
bounds 1<=R<=2 and 0<=R-1<=alpha^2 follow from
sin(alpha)>=alpha/2 and alpha-sin(alpha)<=alpha^3/6.
Thus 1<=A<=3. Put m=max(alpha,beta)<=1/20. Directly from (8),
\[
 |U|\leq2m^2,\quad |V|\leq\tfrac76m^3,\quad
 |U_\beta|\leq4m,\quad |V_\beta|\leq\tfrac32m^2.             \tag{11}
\]
For the last bound use R cos(beta)-1=(R-1)cos(beta)-(1-cos(beta));
for the second use R sin(beta)-beta=(R-1)sin(beta)+sin(beta)-beta.
Because z'=iz/2 and beta'=-1/2, differentiating (8) gives
\[
 \phi''=-\frac z2(U+iV)-\frac{iz}{2}(U_\beta+iV_\beta),
 \qquad
 |\phi''|\leq2m+\tfrac74m^2+\tfrac7{12}m^3\leq4m.          \tag{12}
\]
Consequently |phi''|<=4 alpha on I_in and <=4 beta on I_out.
Lemma 8 supplies |exp(d phi)|<=1 on the entire lower semicircle,
including theta=0. No division by Re D_q is made.

**Amplitude in the actual angular coordinate.** On [-theta_0,0],
including the saddle angle, |w_q|=W and
\[
 \Re(1/2+w_q)\geq1/2+W/2.
\]
Increase the common onset until W>=max(W_0,1) and this last lower
bound is >=4. The half-plane estimates in Lemma 13's proof and
Lemma 12/(4.3) therefore apply on the whole interval, not just the
rescaled local saddle interval. In this sector every factor in a_q
is nonzero. For f(theta)=a_q(theta)/a_q(theta_q) there are fixed
positive B_0,B_1 such that
\[
                         |f|\leq B_0,\qquad |f'|\leq B_1.  \tag{13}
\]
Here is an explicit choice in terms of the source constants, to check
the derivative scale. If |log g_Q(w)|<=C_g/W,
|g_Q'/g_Q(w)|<=C_g/W^2 and
|zeta'/zeta(s)|<=C_zeta exp(-c_zeta Re s) for Re s>=4, take
\[
 \begin{split}
 B_0&=\zeta(4)^2e^{2C_g},\\
 B_*&=\frac78+\frac{C_\zeta}{2}
          \sup_{t\geq1}t e^{-c_\zeta(1/2+t/2)}+\frac{C_g}{2},
 \qquad B_1=B_0B_*.
 \end{split}
\]
The supremum is finite. Indeed |zeta(s)| lies between zeta(4)^(-1)
and zeta(4), |g_Q| lies between exp(-C_g/W) and exp(C_g/W), and
|w_q^(7/4)|=W^(7/4). Moreover w_q'=iw_q/2 gives exactly
\[
 \frac{a_q'}{a_q}=\frac{7i}{8}+\frac{iw_q}{2}
       \left(\frac{\zeta'}\zeta(1/2+w_q)+\frac{g_Q'}{g_Q}(w_q)\right).
\]
This bounds the theta derivative itself by B_* times the amplitude;
there is no missing factor ell_q from a change to the source y coordinate.

**Two finite integrations by parts, retaining every boundary.** For
either interval I=[a,b'] in (7)'s near part, source Lemma 14's finite
identity applies, because f is C^1, phi is C^2 and phi' is nonzero:
\[
 J_I:=\int_a^{b'}f e^{d\phi}\,d\theta
 =\left[\frac{f e^{d\phi}}{d\phi'}\right]_a^{b'}
 -\frac1d\int_a^{b'}\left(\frac{f'}{\phi'}-
                    \frac{f\phi''}{(\phi')^2}\right)e^{d\phi}\,d\theta.
                                                                  \tag{14}
\]
For I_in, its length is 2u alpha, so (10), (12) and (13) give
\[
 |J_{\rm in}|\leq\frac1d\left[
   \underbrace{\frac{B_0}{k_-\alpha^2}+\frac{B_0}{k_-\alpha^2}}_{
                        \theta=-2u\alpha\ \text{and}\ 0}
   +\frac{2uB_1}{k_-\alpha}
   +\frac{8uB_0}{k_-^2\alpha^2}\right].                       \tag{15}
\]
The two remaining terms bound the f'/phi' and f phi''/(phi')^2
integrals respectively. No cancellation with another interval is assumed.

On I_out, change variables only in the positive upper bounds using
|d theta|=2 d beta and v alpha<=beta<=b. This yields
\[
 \begin{split}
 |J_{\rm out}|\leq\frac1d\Bigg[&
 \underbrace{\frac{B_0}{k_+b^2}+\frac{B_0}{k_+(v\alpha)^2}}_{
                      \theta=-\theta_0\ \text{and}\ -2v\alpha}\\
 &+\frac{2B_1}{k_+}\left((v\alpha)^{-1}-b^{-1}\right)
  +\frac{4B_0}{k_+^2}\left((v\alpha)^{-2}-b^{-2}\right)\Bigg].
 \end{split}                                                    \tag{16}
\]
The last coefficient is 8 B_0/k_+^2 times the integral of beta^(-3),
so it includes the factor 2 from angular measure and the factor 4
in (12). Equations (15)–(16) display all four boundary terms.
Since b>v alpha, they imply
\[
 |J_{\rm in}|+|J_{\rm out}|
             \leq\frac{K_2}{d\alpha^2}+\frac{K_1}{d\alpha},       \tag{17}
\]
where the fixed positive constants can be taken to be
\[
 \begin{split}
 K_2&=B_0\left(\frac2{k_-}+\frac{8u}{k_-^2}
                +v^{-2}\left(\frac2{k_+}+\frac4{k_+^2}\right)\right),\\
 K_1&=2B_1\left(\frac{u}{k_-}+\frac1{k_+v}\right).
 \end{split}                                                    \tag{18}
\]

**Fixed exterior and exact Gaussian normalization.** Set
eta=1-cos(b)>0. By (5), the common onset can also ensure
1-cos(alpha)<=eta/2. Then cos(alpha)-cos(beta)>=eta/2 for
b<=beta<=pi/2. Lemma 8 gives Re phi<=-gamma with
gamma=c eta^2/4>0, where c is its constant in (3.12).
Lemma 13/(4.6), with N=1, gives |f|<=C_ext T on this entire arc,
including its negative-axis endpoint. Therefore
\[
 J_{\rm far}:=\int_{-\pi}^{-\theta_0}f e^{d\phi}\,d\theta,
 \qquad |J_{\rm far}|\leq(\pi-\theta_0)C_{\rm ext}T e^{-\gamma d}.
                                                                  \tag{19}
\]
This is C019c's fixed-separation argument with the uniform band check
just given. It neither differentiates the distant amplitude nor omits
the endpoint at -pi. No integration by parts is used on I_far, so
there is no unrecorded boundary term there.

The exact partition (7) and (3) give
\[
 R_d^-=\frac{P_d}{2\pi}a_q(\theta_q)e^{dh_q(u_q)}
                  (J_{\rm far}+J_{\rm out}+J_{\rm in}),\qquad
 |Z_d|=\frac{P_d|a_q(\theta_q)|e^{dH_q}}{\sqrt{2\pi d|D_q|}}.
\]
Thus (6), (17) and (19) imply the full uniform certificate
\[
 \frac{|R_d^-|}{|Z_d|}\leq\sqrt{\frac{C_D}{2\pi}}\left[
  \frac{K_2}{\sqrt d\,\alpha^{3/2}}
 +\frac{K_1}{\sqrt d\,\alpha^{1/2}}
 +(\pi-\theta_0)C_{\rm ext}T\sqrt{d\alpha}\,e^{-\gamma d}\right].
                                                                  \tag{20}
\]
There is no upper-semicircle factor 2, extra r^(-2d), or arc-length
Jacobian: du/u=i d theta is exactly the substitution of source
Proposition 15. Substituting (5) and T<=C_T d/log d into (20) gives
(4), for example with
\[
 C_1=\sqrt{C_D/(2\pi)}K_2a_-^{-3/2},\quad
 C_2=\sqrt{C_D/(2\pi)}K_1a_-^{-1/2},\quad
 C_3=\sqrt{C_D/(2\pi)}(\pi-\theta_0)C_{\rm ext}C_T\sqrt{a_+}.
\]
Every onset was chosen from uniform bounds on the closed band (1),
so the result includes both q-endpoints. Each term in (4) vanishes;
the exponential dominates its fixed polynomial factor. This proves
the asserted uniform limit and eventual <1/4 consequence.

**Qualifications and relevance.** This proof pays precisely R_d^-.
Its proof method is established; the quantitative moving-band
application was not supplied by the inspected source remainder bound.
The recorded search does not establish originality. The onset is not
effective, no finite computation is used, and critical replay1364 below
retains the estimate without a repair. The source manuscript and its formal artifacts have not been
audited in full here. A local Gaussian assembly, continuous phase
barriers and their count, separation from previously counted roots,
the larger far-end loss, every-degree hyperbolicity and actual-Xi
all-degree positivity remain separate. No RH-equivalent positivity,
unproved zero-free region, global sign or numerical extrapolation is
used. C019g and the stops1345/1355/559 are unchanged.

**Critical replay, 17 November 2026 (1364).** This is the first separate
conceptual audit of this result, under unchanged assessment1362. The
full proof above was checked against the cited primary v1. No mathematical
error or change to the conclusion, constants, band or inputs was found.
The following records the load-bearing checks; it adds no root theorem.

The primary passages inspected are Ono v1 equations (2.5)-(2.9),
(3.1)-(3.5); Lemma 7 including its uniform implicit-function proof and
(3.6)-(3.11); Lemma 8 and its closed-endpoint proof; Lemma 9 and
(3.13)-(3.16); Corollary 10/(3.17)-(3.20) with its local normalization;
Lemma 12/(4.1)-(4.3) including the larger-sector/Cauchy derivative
argument; Lemma 13/(4.4)-(4.9) including both the whole-circle polynomial
bound and the absolute-convergence logarithmic derivative bound; the
finite identity in Lemma 14's proof; and Proposition 15/(5.2)-(5.4)
with its angular normalization and complementary-circle division.
These are the version and link in the hypotheses, not a source-wide audit.

1. **Uniform geometry and applicability.** Source (3.11) has a positive
   quadratic coefficient bounded away from zero and a uniform remainder
   for small 1/Lambda, so (5) is genuinely uniform on the closed band (1).
   Both q-endpoints are strictly above q_e and eventually below c_0 T.
   The field specialization N=1, r_1=1, r_2=0, Delta_Q=1 gives
   mu_Q=7/4 and c_Q=2^(-1/4) pi^(1/4), as used in (2).
   The conditions v alpha<b, alpha<cos(alpha), C<=1, W>=max(W_0,1)
   and 1/2+W/2>=4 all follow uniformly by increasing a single onset.
   They place theta_q in [-theta_0,0] and make (7) precisely the
   complement of the original local interval. No extra connector is
   discarded. Lemma 9 gives (6) with |D_q|, rather than Re D_q;
   the latter has a different order near the edge and is never used
   as a substitute. The recorded n_q asymp d^(1/4) is valid, although
   the local Gaussian approximation is not an input to this result.

2. **Nonstationarity at the endpoint and outside the saddle.** To replay
   (8), divide its first bracket by z and use
   -Az-z^(-1)=-(A+1)cos(beta)+i(A-1)sin(beta), then A-1=CR.
   This recovers U+iV exactly, including every 1/Lambda term. Integration
   of sin(t)>=t/2 between alpha and beta gives (9) on either side;
   no assumption beta>=alpha is needed. In particular
   phi'(0)=i(A+1)(cos(alpha)-1), which is nonzero for alpha>0 and
   has modulus at least alpha^2/2. On the whole inner interval,
   alpha^2-beta^2>=(1-u^2)alpha^2; on the outer interval,
   beta^2-alpha^2>=(1-v^(-2))beta^2. These reproduce both positive
   constants in (10), at all four endpoints as well as in the interiors.

3. **Actual second and amplitude derivatives.** The elementary estimate
   R-1=(alpha-sin(alpha))/sin(alpha)<=alpha^2/3 is more than sufficient
   for the displayed R-1<=alpha^2. It gives precisely the four bounds
   in (11). Differentiating with z'=iz/2 and beta'=-1/2 yields (12),
   whose upper bound is at most 4m for m<=1/20. For the amplitude,
   the fixed small sector has Re(1/2+w)>=1/2+W/2, so the half-plane
   inequalities from Lemma 13's proof apply throughout that sector.
   The saddle denominator obeys the same bounds. Lemma 12 supplies
   |g'/g|<=C_g/W^2 there with the same fixed constant after enlargement.
   Thus B_0 in (13) bounds the modulus ratio, and logarithmic angular
   differentiation gives exactly 7i/8 plus the two iw/2 terms printed
   above (14). The exponential bound on zeta'/zeta absorbs W uniformly.
   No estimate in the rescaled y variable is being transferred to theta.

4. **Every integration-by-parts term.** Source Lemma 8 gives Re phi<=0
   on each closed interval. Consequently the finite identity (14)
   applies without a damping lower bound. The inner f'/phi' integral
   is at most 2u B_1/(k_- alpha), and the inner second-derivative
   integral is at most 8u B_0/(k_-^2 alpha^2), before division by d.
   Both inner boundary terms are bounded by B_0/(k_- alpha^2).
   On the outer interval, the change to positive beta measure gives
   2 B_1/k_+ times the integral of beta^(-2) and 8 B_0/k_+^2 times
   the integral of beta^(-3). Their integrals are exactly the two
   differences in (16). Its two boundary terms retain beta=b and
   beta=v alpha. Using b^(-2)<=(v alpha)^(-2) and discarding only
   subtracted nonnegative terms gives the stated K_1,K_2 in (18).
   There is no boundary cancellation assumption and no unpaid endpoint.

5. **Exterior, branch and normalization checks.** On beta in [b,pi/2],
   cos(alpha)-cos(beta)>=eta/2, so the same constant gamma=c eta^2/4
   applies throughout the far arc. Lemma 12 includes arg(w)=-pi/2;
   Lemma 13 includes theta=-pi and permits zeros of the distant
   amplitude. Only the nonzero saddle amplitude is divided out.
   W tends uniformly to infinity, so the whole-circle zeta bound is
   away from its pole and within its stated |s|>=2 range. The branch
   endpoint is interpreted from below as in source Section 3, not as
   an analytic continuation through the cut. Finally, Re D_q>0 fixes
   the principal square root and implies |sqrt(D_q)|=sqrt(|D_q|).
   Direct division of (3) multiplies each normalized angular bound by
   sqrt(d|D_q|/(2 pi)), with no factor two or radius factor.
   Equation (20) therefore yields respectively d^(-1/8), d^(-3/8)
   and d^(11/8) exp(-gamma d)/log d, exactly as in (4).

There are finitely many onset conditions, each uniform in q on (1),
so their maximum remains independent of q. All three positive majorants
tend to zero; choosing their sum below 1/4 proves the stated eventual
threshold without an effective value of d. This is local validation of
the existing quantitative specialization, not additional progress beyond
that statement or a claim of originality. No new mathematical dependency,
script, numerical certificate, sign count or global assumption is added.

## Mathlib

Full matching theorem and supporting formal coverage have not been
checked. No absence claim is made, and the source's autoformalization
claim is not a verified formal artifact in this notebook. The proof
uses the cited analytic inputs and the explicit finite calculations
above; no mathematical script or numerical certificate is required.
