# L744: Uniform complete-energy penalty for corrected smooth modulations

## Hypotheses

Fix an integer K>=2, ell=log(3)/2, L=K ell, and M<infinity for which
the following family is nonempty:

\[
 \mathcal F_{K,M}=\left\{w(x)=\sum_{j=0}^{K-1}w_j(x-j\ell):
 w_j\in C_c^\infty(0,\ell;\mathbb C),\quad
 \|w\|_2=1,\quad \|w\|_{H^2(\mathbb R)}\le M\right\},
 \qquad
 \|f\|_{H^2}^2=\|f\|_2^2+\|f'\|_2^2+\|f''\|_2^2.       \tag{1}
\]

All extensions are by zero, and all L2 norms are unweighted. In
particular M>=1. Use L740's complete generator A_L and
E_L(f)=-Re<A_L f,f>, with the inner product linear in its first
argument. Use L743's entire bounded Hermitian arithmetic operator

\[
 B_L=\sum_{2\le n<e^L}\frac{\Lambda(n)}{\sqrt n}
                         (T_{\log n}+T_{\log n}^*),
 \quad (T_af)(x)=\mathbf1_{x>a}f(x-a),\quad
 C_{\rm prime}=2\sum_{2\le n<e^L}\frac{\Lambda(n)}{\sqrt n}.
                                                               \tag{2}
\]

All prime powers are included; a delay exactly L is zero. Here B_L
means the Hermitian arithmetic operator, not a continuous perturbation
or the nonsymmetric generator A_L.

Fix L743's real nonnegative chi in C_c^infinity(0,ell), positive on
some open interval. For sigma,tau in {+1,-1}, put

\[
 b_\tau(s)=\chi(s)e^{\tau s/2},\qquad
 G_{\sigma\tau}=\int_0^\ell\chi(s)e^{(\sigma+\tau)s/2}\,ds.
\]

L743 (9) proves that G is invertible. For real t and w in (1), use
exactly its complex-linear correction:

\[
 \begin{split}
 d_{j,\sigma}(t,w)&=e^{itj\ell}\int_0^\ell
                         e^{\sigma s/2}w_j(s)e^{its}\,ds,\\
 h_{t,w}(x)&=\sum_{j=0}^{K-1}\sum_{\tau=\pm1}
                  (G^{-1}d_j(t,w))_\tau b_\tau(x-j\ell),\\
 v_{t,w}(x)&=e^{itx}w(x)-h_{t,w}(x).
 \end{split}                                                   \tag{3}
\]

The Fourier convention is F_f(xi)=integral f(x)e^(-i xi x)dx;
Fourier quadratic integrals use dxi/(2*pi). The analytic inputs are
Plancherel's theorem and its Fourier derivative identity on smooth
compactly supported functions, plus the principal-logarithm expansion
and complex remainder in [NIST DLMF 5.11.2](https://dlmf.nist.gov/5.11.E2)
and [5.11(ii)](https://dlmf.nist.gov/5.11#ii), inspected 4 November 2026.
For psi(z)=log(z)-1/(2z)+R(z), that remainder gives
|R(z)|<=sec^3(arg(z)/2)/(12|z|^2) in the right half-plane.
L741 Section 2 supplies the scalar/kernel and finite-square pole
normalizations; its closed-domain and positivity conclusions at
L=log(3) are not extended or used. No RH hypothesis, conditional
conclusion of L742, or unreplayed source positivity computation is used.

## Conclusion

There are t0<infinity and a nonnegative epsilon_(K,M,chi)(t), tending
to zero as |t| tends to infinity independently of w, such that
v_(t,w) is nonzero and, for every w in (1) and |t|>=t0,

\[
 \boxed{\quad
 \frac{E_L(v_{t,w})}{\|v_{t,w}\|_2^2}
 \ge \log\frac{|t|}{2\pi}-C_{\rm prime}
                         -\epsilon_{K,M,\chi}(t).
 \quad}                                                       \tag{4}
\]

One admissible error and threshold are given in (17)-(18) below;
epsilon=O_(K,M,chi)(1/|t|). No phase-return condition is required.
This proves the prior assessment's (P) only for fixed K, M and chi.
The proof is a standard-mechanism specialization/REPRODUCTION, not a
claim of discovery beyond the sources checked. The separate conceptual
audit below (4 November 2026, step 289) accepts (4), with the
all-T denominator qualification in (15) repaired. It supplies no bounded-frequency sign, unrestricted
envelope bound, growing-window estimate, energy-Rayleigh equality,
moment-complement positivity or RH resolution.

## Proof

### 1. Complete smooth energy on this fixed window

Every f in C_c^infinity(0,L) belongs to D(A_L). Indeed L740's Phi_f
has derivative integral_0^x log(x-y)f'(y)dy, with f(0)=0; the local
integrability of log and boundedness of f' give an L2 derivative and
an absolutely continuous Phi_f. This verifies L740's actual domain
criterion without imposing or extending a closed-form domain theorem.

Here is the arbitrary-fixed-L specialization of L741's normalization.
Let D be the full-line Fourier multiplier -log(1+i xi), put
d_0(u)=(e^(-u)-1)/u, and set

\[
 k(u)=\frac{2e^{-u/2}}{1-e^{-2u}},\qquad
 r(u)=k(u)-\frac{e^{-u}}u,\qquad u>0.
\]

L741 (9), (13)-(16) are full-line kernel identities independent of
L. In particular r is L1(0,infinity),
q-d_0=r-4 cosh(u/2), and

\[
 \widehat r(i\xi)=\log(1+i\xi)
                  -\psi(1/4+i\xi/2)-\log2.
\]

On smooth tests their restriction, together with L740 (4)/(5), gives

\[
 A_Lf=(Df)|_{(0,L)}+\log(2\pi)f+R_Lf-4V_Lf+P_Lf,
                                                               \tag{5}
\]

where R_L and V_L are causal convolutions with r and cosh(u/2), and
P_L=2 sum_(2<=n<exp L) Lambda(n)n^(-1/2) T_(log n). The gamma
normalization already belongs to the distributional kernel of D in
L741 (9), so no further gamma scalar is added. Smooth zero extensions
have Schwartz Fourier transforms, making Df an L2 function. Pairing
its restriction against f equals the full-line pairing. Plancherel
and the displayed transform of r therefore give the real symbol

\[
 m(\xi)=\Re\psi(1/4+i\xi/2)-\log\pi.
\]

Finite-square Fubini, as in L741 (18), gives
4 Re<V_L f,f>=2 Re(F_f(i/2) overline(F_f(-i/2))). The arithmetic
energy is -Re<P_L f,f>=-<B_L f,f>. Consequently the exact identity is

\[
 E_L(f)=\int_{\mathbb R}m(\xi)|F_f(\xi)|^2\frac{d\xi}{2\pi}
       +2\Re\bigl(F_f(i/2)\overline{F_f(-i/2)}\bigr)
       -\langle B_Lf,f\rangle.                              \tag{6}
\]

These steps use only an L1 convolution, a bounded kernel on a finite
square, a finite delay sum and a smooth Fourier integral. They extend
the smooth calculation, not L741's closed-domain or positivity theorem.
Both rational completion terms and the continuous kernel are retained.

For (3), the defining matrix gives each local moment of h_(t,w)
exactly d_(j,sigma). Thus

\[
 F_{v_{t,w}}(\sigma i/2)
 =\sum_j e^{\sigma j\ell/2}
     \int_0^\ell e^{\sigma s/2}v_{t,w}(s+j\ell)\,ds=0
 \quad(\sigma=\pm1).                                      \tag{7}
\]

In particular the pole product in (6) is exactly zero, including for
complex tests. No pole is discarded merely because it is small.

### 2. Imported symbol estimate and a uniform shifted integral

Set

\[
 A=2+\frac{8\sqrt2}{3}+\log(4\pi),\qquad
 W(\xi)=A+\log(2+|\xi|),\qquad c_T=\log(T/(2\pi)).
\]

Apply the cited DLMF remainder at z=1/4+i xi/2. The line has
|arg z|<pi/2, so the sector multiplier is at most 2 sqrt(2), and
|R(z)|<=sqrt(2)/(6|z|^2). For |xi|>=1,

\[
 \left|\log|z|-\log(|\xi|/2)\right|\le\frac1{8\xi^2},
 \qquad \left|\Re\frac1{2z}\right|\le\frac1{2\xi^2},
 \qquad |R(z)|\le\frac{2\sqrt2}{3\xi^2}.
\]

Their sum is less than 2/xi^2. For |xi|<=1, |z| is between 1/4
and 1, so |log|z||<=log4, |1/(2z)|<=2 and
|R(z)|<=8 sqrt(2)/3. Thus the following estimates hold:

\[
 |m(\xi)-\log(|\xi|/(2\pi))|\le 2/\xi^2\quad(|\xi|\ge1),
 \qquad |m(\xi)|\le W(\xi)\quad(\xi\in\mathbb R).        \tag{8}
\]

This is only the required specialization of the imported scalar
remainder, not a reproof of the digamma expansion. In particular no
logarithmic singular approximation is used near xi=0.

For w in (1), dmu_w(eta)=|F_w(eta)|^2 deta/(2*pi) is a probability
measure. Plancherel and differentiation give

\[
 \int(1+\eta^2+\eta^4)\,d\mu_w\le M^2,\qquad
 \int|\eta|\,d\mu_w\le M.                               \tag{9}
\]

Write T=|t|>=2 and f=e^(itx)w, so F_f(xi)=F_w(xi-t).
On |eta|<=T/2, |t+eta|>=T/2>=1. Equation (8) and
|log|1+eta/t||<=2|eta|/T give

\[
 |m(t+\eta)-c_T|\le 2|\eta|/T+8/T^2.
\]

On the complementary set, T<2|eta| and |t+eta|<3|eta|.
Since log(2+r)<=3+r^2 for r>=0, (8) gives

\[
 |m(t+\eta)-c_T|
 \le A+\log3+3+\log(2\pi)+\log T+\eta^2.
\]

The fourth moment in (9) gives
mu_w(|eta|>T/2)<=16 M^2/T^4 and
integral_(|eta|>T/2) eta^2 dmu_w<=4 M^2/T^2. Hence, uniformly in w,

\[
 \begin{split}
 |Q_m(f)-c_T|&\le a(T),\qquad
 Q_m(g):=\int m(\xi)|F_g(\xi)|^2\frac{d\xi}{2\pi},\\
 a(T)&=\frac{2M}{T}+\frac{8+4M^2}{T^2}
 +\frac{16M^2}{T^4}
       [A+\log3+3+\log(2\pi)+\log T].
 \end{split}                                                   \tag{10}
\]

This bounds the complete shifted integral, including eta near -t,
where its frequency t+eta is small. It does not exchange an unbounded
multiplier with a profile-dependent limiting statement.

For the correction estimate also use the positive norm
||g||_W^2=integral W(xi)|F_g(xi)|^2 dxi/(2*pi).
The inequalities 2+T+|eta|<=(2+T)(2+|eta|) and (9) imply

\[
 \|f\|_W^2\le U(T):=A+\log(2+T)+3+M^2.                  \tag{11}
\]

### 3. Uniform size and logarithmic cost of the exact correction

Twice integrating each cell moment in (3) by parts gives

\[
 |d_{j,\sigma}(t,w)|
 \le T^{-2}\|(e^{\sigma s/2}w_j)''\|_{L^1(0,\ell)}
 \le T^{-2}\sqrt{\ell}\,e^{\ell/2}\frac{\sqrt{33}}4
                                      \|w_j\|_{H^2}.     \tag{12}
\]

There are no boundary terms: each w_j is compactly supported in its
open cell. The last inequality uses
(e^(sigma s/2)w_j)''=e^(sigma s/2)(w_j''+sigma w_j'+w_j/4),
L1<=sqrt(ell)L2 and Cauchy--Schwarz on coefficients (1,1,1/4).
Cell derivative supports are disjoint, so summing both signs and cells
gives sum_j |d_j|^2 <= (33 ell e^ell/8) M^2 T^(-4).

Define the finite constants

\[
 R_\chi=\|G^{-1}\|
          (\|b_+\|_{H^2}^2+\|b_-\|_{H^2}^2)^{1/2},
 \quad H=R_\chi\sqrt{33\ell e^\ell/8}\,M,
 \quad \delta(T)=H/T^2.
\]

The Hilbert-space Cauchy--Schwarz estimate for each two-term correction,
then disjointness of the cells for all derivatives through order two,
proves

\[
 \|h_{t,w}\|_{H^2}\le\delta(T),\qquad
 \|h_{t,w}\|_2\le\delta(T),\qquad
 \|h_{t,w}\|_W\le\sqrt{A+3}\,\delta(T).                  \tag{13}
\]

For the last inequality, W(xi)<=A+3+xi^2<=(A+3)(1+xi^2)
and Plancherel suffice. No modulation is applied to the fixed b_tau
in the correction: all t dependence in h lies in its coefficients.

Because |m|<=W, weighted Cauchy--Schwarz gives

\[
 \left|\int m F_f\overline{F_h}\frac{d\xi}{2\pi}\right|
 \le\|f\|_W\|h\|_W.
\]

It is valid even though m itself need not be positive. Expanding the
quadratic form with v=f-h and using (11)-(13) therefore yields

\[
 |Q_m(v)-Q_m(f)|\le b(T):=
 2\sqrt{U(T)(A+3)}\,\delta(T)+(A+3)\delta(T)^2.           \tag{14}
\]

All constants in (10)-(14) are independent of w. This verifies the
correction in the unbounded logarithmic form, not just in L2.

### 4. Denominator and full arithmetic payment

Let N=||v||_2^2. Since ||f||_2=1, (13) gives

\[
 N\ge\max\{0,1-\delta(T)\}^2,\qquad
 |N-1|\le2\delta(T)+\delta(T)^2.                         \tag{15}
\]

The maximum is needed here when delta(T)>1: the lower bound
||v||_2>=1-delta(T) cannot then be squared. For delta(T)<=1/2,
the displayed bound is N>=(1-delta(T))^2>=1/4, and v is nonzero. The identity
Q_m(v)/N-c_T=[Q_m(v)-c_T+c_T(1-N)]/N and (10), (14), (15) imply

\[
 \left|\frac{Q_m(v)}N-c_T\right|
 \le\frac{a(T)+b(T)+|c_T|[2\delta(T)+\delta(T)^2]}
               {(1-\delta(T))^2}.                         \tag{16}
\]

In particular choose

\[
 t_0=\max\{2,\sqrt{2H}\},\qquad
 \epsilon_{K,M,\chi}(t)=
 \frac{a(|t|)+b(|t|)+|c_{|t|}|[2\delta(|t|)+\delta(|t|)^2]}
      {(1-\delta(|t|))^2}\quad(|t|\ge t_0).               \tag{17}
\]

Define epsilon=0 for |t|<t0; no claim is made there. The function is
nonnegative and independent of w. Directly from its displayed terms,

\[
 a(T)=O_M(T^{-1}),\quad
 b(T)=O_{K,M,\chi}(T^{-2}\sqrt{\log(2+T)}),\quad
 |c_T|(2\delta+\delta^2)=O_{K,M,\chi}(T^{-2}\log(2+T)),
 \quad \epsilon_{K,M,\chi}(t)=O_{K,M,\chi}(|t|^{-1}).     \tag{18}
\]

Finally L743 (4), or the finite sum of contractions in (2), gives
<B_L v,v><=C_prime N. Use the exact pole cancellation (7) in (6),
and then (16), to obtain (4). The scalar is log(|t|/(2*pi)) with
coefficient one, the arithmetic payment has its full factor two, and
no pole product or prime power is omitted. The estimates used |t|
throughout and thus apply to either sign of t.

For this fixed family eventual positivity follows only once
log(|t|/(2*pi))>C_prime+epsilon(t). No numerical onset or bound uniform
in K, M or the conditioning of G is asserted. The lower bound prices
high-carrier recurrence in complete energy; it neither transfers the
prime-only equality to energy normalization nor supplies the remaining
bounded-frequency and unrestricted-test signs.

### Separate conceptual audit (4 November 2026, step 289)

The fixed-K, fixed-M, fixed-chi assertion (4) passes this audit after
the qualification in (15). This is verification and a local repair of
the standard-mechanism specialization, not a new sign theorem. The
unchanged SPECIALIZE assessment is
`drafts/literature/2026-11-04-uniform-neutral-modulation-energy-audit.md`.
The scalar DLMF remainder and the previously audited local inputs are
reused; no source positivity computation is an input.

1. **Smooth domain and arbitrary fixed window.** For a zero-extended
   f in C_c^infinity(0,L), write f(y)=integral_0^y f'(z)dz.
   Absolute Fubini expresses Phi_f(x) as the integral of
   [(x-z)log(x-z)-(x-z)]f'(z) over 0<z<x. Its derivative is
   integral_0^x log(x-z)f'(z)dz, bounded by
   ||f'||_infinity integral_0^L |log u|du. Thus Phi_f is absolutely
   continuous with L2 derivative, so f belongs to L740's stated domain.
   L741 (9) is a full-line distribution identity. Substituting it
   into L740 (5) and using q-d_0=r-4cosh yields (5) for every fixed
   L; no closed-form-domain or small-window positivity theorem is
   extended. The L1 kernel r has the transform stated above (5), so
   -Re[-log(1+i xi)+log(2pi)+r-hat(i xi)] equals m(xi).
   This checks both the scalar log(pi) and the absence of an extra gamma.

2. **Complex poles and every prime power.** The real part of
   F_f(i/2) overline(F_f(-i/2)) is the integral over the full square
   of cosh((x-y)/2) Re(f(x)overline(f(y))). By symmetry it is twice
   the corresponding integral over x>y. Hence its twice-real-part
   term is exactly 4 Re<V_L f,f>, with the sign in (6).
   With the first-slot-linear inner product,
   <B_L f,f>=2 sum a_n Re<T_(log n)f,f>=Re<P_L f,f>.
   Each delay is a contraction, and the delay L vanishes almost
   everywhere. Formula (7) uses the complex-linear inverse G^-1
   without conjugating d; multiplying each vanishing local moment
   by e^(sigma j ell/2) kills both global pole moments exactly.

3. **Scalar bounds and uniform Fourier tails.** The DLMF remainder
   is used only in |arg z|<pi/2. For |xi|>=1 the three error
   constants sum to 1/8+1/2+2sqrt(2)/3<2. For |xi|<=1 the bound
   is A. For |xi|>=1, also
   |log(|xi|/(2pi))|<=log|xi|+log(2pi) and
   A>=2+log(2pi), establishing the global majorant W in (8).
   Smooth zero extensions give exactly the second and fourth
   Fourier moments in (9), even when supports approach cell
   endpoints as w varies. On |eta|<=T/2 the logarithm is bounded
   using |eta/t|<=1/2, for either sign of t. On the complement,
   log(2+|t+eta|)<=log3+log(2+|eta|), and fourth-moment Markov
   bounds give respectively 16M^2/T^4 and 4M^2/T^2 for its mass
   and second moment. These yield every term of a(T), including
   the small-frequency region near eta=-t, without a limiting
   interchange or a profile-dependent tail estimate.

4. **Correction in the unbounded form.** Both the value and first
   derivative of e^(sigma s/2)w_j vanish at each cell endpoint,
   justifying both integrations by parts. The coefficient-vector
   squared norm is 1+1+1/16=33/16; summing the two signs gives
   33 ell e^ell/8 in (12). The derivative supports in distinct
   cells are disjoint. The fixed right inverse therefore bounds
   the full H2 correction by H/T^2 uniformly over the family.
   Although the original profile is modulated, the correction
   basis b_tau is not. W<=(A+3)(1+xi^2) gives its weighted norm,
   and |m|<=W justifies the mixed-form Cauchy--Schwarz bound even
   where m is negative. Equations (11)-(14) therefore control
   the complete logarithmic correction, not just its L2 size.

5. **Denominator qualification and final bound.** The former first
   inequality of (15) omitted the restriction delta<=1. It has
   been replaced by max{0,1-delta}^2 for all T>=2; the norm-defect
   estimate remains valid without that restriction. At the stated
   t0=max{2,sqrt(2H)}, delta<=1/2, so N>=1/4. In (16) the term
   |c_T|(2delta+delta^2) is necessary and is retained. Its size
   is O(T^-2 log T); the weighted correction is
   O(T^-2 sqrt(log T)) and a(T)=O(T^-1), all with constants
   independent of w. Thus epsilon=O(T^-1) and is nonnegative.
   Apply <B_L v,v><=C_prime N after normalization and exact
   cancellation of both poles. This gives precisely (4) for
   both signs of t, with coefficient one and the full prime payment.

The repair changes no hypothesis or conclusion of (4), since its
admitted range already has delta<=1/2. The three direct local
mathematical inputs remain L740, L741 and L743. No RH-conditional
conclusion of L742 is used. The audit supplies neither a bound uniform
in K/M/chi nor control of arbitrary linear combinations of these
profiles; normalization and signed cross terms would require their
own argument. Bounded frequencies, general envelopes, moment
complements and support-uniform positivity remain open.

## Mathlib

Full matching Mathlib coverage of (4), with this complete operator and
exact correction, has not been checked. No formal verification or
absence claim is made. Plancherel, Fourier differentiation and the
digamma asymptotic are named analytic inputs; the finite-window
normalization and uniform integration/correction steps are written out
above. L741's finite-window sign certificate is not an input here.
