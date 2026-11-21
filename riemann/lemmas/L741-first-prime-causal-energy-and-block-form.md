# L741: First-prime causal energy and the equal-half form estimate

## Hypotheses

Use L740's complete causal generator A_L on the original complex space
X_L=L2(0,L), with inner product linear in its first argument. In this
lemma L=log(3), ell=L/2, d=log(2), and a=log(2)/sqrt(2). Every function
on an interval is extended by zero when a Fourier transform is taken:

\[
 F_f(t)=\int_{\mathbb R}f(x)e^{-itx}\,dx,\qquad
 C_f(u)=\int_{\mathbb R}f(x+u)\overline{f(x)}\,dx.
 \tag{1}
\]

Keep all of L740's q, its scalar c=log(2*pi), and its arithmetic term.
Here P_L=2a T_d; the delay log(3)=L acts as zero. Define

\[
 w(t)=\log|1+it|=\tfrac12\log(1+t^2),
 \quad
 \begin{split}
 V_I&=\{f\in L^2(\mathbb R):\operatorname{supp}f\subset\overline I,
                       \ \int w(t)|F_f(t)|^2dt<\infty\},\\
 W_I&=\{f\in L^2(\mathbb R):\operatorname{supp}f\subset\overline I,
                       \ \int w(t)^2|F_f(t)|^2dt<\infty\}.
 \end{split} \tag{2}
\]

The norms used below are respectively the Fourier norms with weights
1+w and (1+w)^2, and Fourier integrals use measure dt/(2*pi).
These are supported function spaces, not imposed pointwise trace spaces.

The external sign input is **Xuefeng Zhu, arXiv:2608.24827v2**
(2 September 2026),
[Corollary 6.3](https://arxiv.org/html/2608.24827v2), using its
normalization (2)--(3), Section 6 and its complex-test conclusion:

\[
 Q(f)\ge c_*\|f\|_2^2,\qquad c_*=8.9\cdot10^{-18},
 \quad \operatorname{supp}f\subset[-0.8,0.8].                 \tag{3}
\]

Only this finite-window computer-assisted theorem is imported. Its
supplementary computation has not been locally replayed. The retracted
larger support claim is not used. The geometric normalization to be
matched is also explicit in **Li Hongmin**, *Cutoff-free positivity of
localized Weil forms through the (log 11)/2 threshold*,
[rStation paper 45 v1](https://rstation.ai/problems/riemann_hypothesis/papers/45)
(23 October 2026), equation (2.1). No stronger sign theorem from that
paper is needed.

The interface input is **Perfekt--Pushnitski**, *On the spectrum of the
multiplicative Hilbert matrix*, Ark. Mat. 56 (2018), 163--183,
[Lemma 2.1, p.166](https://archive.intlpress.com/site/pub/files/_fulltext/journals/arkiv/2018/0056/0001/ARKIV-2018-0056-0001-a010.pdf):
a Hankel kernel bounded in absolute value by A/(u+v) on the positive
half-line has L2 norm at most A*pi. This is the classical Carleman bound;
it is imported, not reproved. Also use Plancherel's theorem and
[DLMF 5.9.13](https://dlmf.nist.gov/5.9.E13) for the digamma function.
L740 already imports the exact fractional-integral generator domain.
Suzuki, [arXiv:2606.09096v3](https://arxiv.org/html/2606.09096v3),
Theorem 1.1 and Sections 2.3--3.2, supplies the localized-form context
and a smooth form core. The particular generator-domain and midpoint
specializations required here are justified below rather than inferred
by identifying two different operators.

## Conclusion

With zero extension understood, D(A_L)=W_(0,L). Its Hermitian energy

\[
 H_L(f,g)=-\tfrac12\bigl(\langle A_Lf,g\rangle+
                              \langle f,A_Lg\rangle\bigr),
 \qquad E_L(f)=H_L(f,f),                                    \tag{4}
\]

has a closed semibounded extension with domain V_(0,L), the closure of
its restriction to D(A_L). On that form domain its quadratic value is
exactly

\[
 \begin{split}
 E_L(f)=Q(f)={}&\frac1{2\pi}\int_{\mathbb R}
  [\Re\psi(1/4+it/2)-\log\pi]|F_f(t)|^2dt\\
 &+2\Re\bigl(F_f(i/2)\overline{F_f(-i/2)}\bigr)
       -2a\Re C_f(d).                                    \tag{5}
 \end{split}
\]

Both half-interval restrictions preserve W_(0,L) and V_(0,L).
There is no new midpoint trace condition. For f_0 supported in [0,ell]
and f_1 supported in [ell,L], belonging to the form domain,

\[
 E_L(f_j)\ge c_*\|f_j\|_2^2,\qquad
 |H_L(f_0,f_1)|\le\sqrt{E_L(f_0)E_L(f_1)}.                 \tag{6}
\]

Thus the requested lossless estimate holds with kappa=1. It retains
the complete cross-block operator, including its singular continuous
kernel and the delay d. In particular, this is not an estimate obtained
by setting that coupling to zero. Each diagonal block is the same
translated prime-free length-ell energy.

This is a specialization/reproduction of known finite-window positivity,
not a new sign theorem beyond the cited sources. The separate conceptual
audit below (4 November 2026, step 278) passes for this bridge, with the
source-computation qualification retained. It gives no larger-window
iteration, fixed-parameter all-window bound, Xi mixed signs or RH proof.

## Proof

### 1. A damped logarithmic generator and the actual operator domain

On L2(R), define the closed Fourier multiplier B with symbol
b(t)=-log(1+it), using the principal logarithm. Its domain is the
space with finite integral of w(t)^2|F(t)|^2: the imaginary part of
log(1+it) is arctan(t), bounded by pi/2. For epsilon>0 put

\[
 B_\epsilon f=\int_\epsilon^\infty
                   \frac{e^{-u}}u\,[f(\cdot-u)-f]du.       \tag{7}
\]

These are bounded operators. Their multipliers converge to b(t):
differentiation in t gives -i/(1+it), and the value at t=0 is zero.
Differentiation is justified by the integrable majorant e^(-u).
Splitting the integral at min(1,1/|t|) gives, uniformly in epsilon,
|b_epsilon(t)|<=C(1+w(t)). Dominated convergence and Plancherel show
B_epsilon f -> Bf in L2 for every f in D(B). For any f in L2 the
same convergence holds distributionally: pair its Fourier transform
with a Schwartz function and apply Cauchy--Schwarz to the majorant.

Let G_L=gamma I+Phi_f' be the unperturbed generator in L740, and put

\[
 d_0(u)=\frac{e^{-u}-1}{u}\quad(u>0),\qquad
 (D_Lf)(x)=\int_0^x d_0(x-y)f(y)dy.                        \tag{8}
\]

The subscript on d_0 distinguishes this kernel from the delay d.
D_L is bounded, since d_0 is bounded on every finite interval.
In distributions on R the kernel of B is

\[
 \gamma\delta_0+\frac{d}{du}\bigl({\bf1}_{u>0}\log u\bigr)
                     +{\bf1}_{u>0}d_0(u).                 \tag{9}
\]

Here is the normalization check, including gamma. Acting on a smooth
compact test phi, the derivative in (9) is the limit of
log(epsilon)phi(epsilon)+integral_epsilon^infinity phi(u)/u du.
The kernel in (7) acts by
integral_epsilon^infinity e^(-u)[phi(u)-phi(0)]/u du.
Their difference tends to zero because

\[
 \int_\epsilon^\infty e^{-u}/u\,du+\log\epsilon
       \longrightarrow-\gamma.
\]

Indeed integration by parts gives
integral_epsilon^infinity e^(-u)log u du
=e^(-epsilon)log epsilon+integral_epsilon^infinity e^(-u)/u du,
and the left side tends to Gamma'(1)=psi(1)=-gamma.
This proves (9) without using a multiplier for xi'/xi.
Consequently, for f supported in [0,L],

\[
 (Bf)|_{(0,L)}=G_Lf+D_Lf                              \tag{10}
\]

as distributions, with either side in L2 whenever the corresponding
domain condition is established.

We verify both domain inclusions, including endpoints. Define on R
Phi_f=(1_(0,infinity) log)*f. It is continuous locally, by convolution
of two locally relevant L2 functions; it vanishes for x<=0. If
f belongs to D(G_L), L740 gives Phi_f in AC[0,L] and Phi_f' in L2(0,L).
For x>L its ordinary derivative is

\[
 \Phi_f'(x)=\int_0^L\frac{f(y)}{x-y}dy.                   \tag{11}
\]

Set u=x-L and v=L-y. The kernel is 1/(u+v), a compression of the
Carleman kernel. The imported bound proves that (11) is in L2(L,infinity)
with norm <=pi||f||_2. Phi_f is continuous at both 0 and L. Its
piecewise weak derivatives are locally L2 and hence locally L1;
integrating them across the two junctions proves global local absolute
continuity. There are therefore no hidden boundary delta terms in (9).
Outside [0,L], (9) gives zero to the left and

\[
 (Bf)(x)=\int_0^L\frac{e^{-(x-y)}}{x-y}f(y)dy,
                      \qquad x>L.                       \tag{12}
\]

This is again Carleman-dominated and has norm <=pi||f||_2.
Inside the interval use (10). Thus Bf is globally L2 and f belongs
to D(B). Conversely, if the zero extension belongs to D(B), (9)--(10)
give Phi_f'=Bf-gamma f-D_Lf in L2(0,L). A function with this weak
derivative has an AC representative on [0,L]; its continuous convolution
representative is the same one. L740's domain criterion now gives
f in D(G_L). Its bounded perturbation A_L has the same domain.
This proves D(A_L)=W_(0,L). Equations (10) and (12) also prove equivalence
of the A_L graph norm and the W_(0,L) norm: the exterior contribution
is <=pi||f||_2 and all differences inside are bounded L2 operators.

For later closure arguments, C_c^infinity(0,L) is dense in both
W_(0,L) and V_(0,L). To see this without assuming a trace theorem,
first contract the support toward m=L/2 by
f_r(x)=r^(-1/2)f(m+(x-m)/r), 0<r<1. Its Fourier transform is
r^(1/2)e^(-im(1-r)t)F_f(rt). Dilation and this phase converge strongly
to the identity in each weighted L2 space as r tends to 1. For a
detailed density justification, the dilation operators are uniformly
bounded for 1/2<r<1 because 1+w(t/r)<=C(1+w(t)); convergence holds
first for compactly supported smooth Fourier functions by dominated
convergence, then for every weighted L2 function by density. Multiplication
by the phase converges strongly by the same dominated-convergence
argument. Next mollify f_r by a compactly supported smooth approximate
identity of radius smaller than its distance to the endpoints. Its
Fourier multiplier is uniformly bounded and converges pointwise to 1,
so it converges in either weighted norm. The resulting functions lie
in C_c^infinity(0,L). This also proves that this smooth space is an
A_L graph core. The same argument applies to either half interval.

### 2. Complete energy and scalar normalization

For u>0 define

\[
 k(u)=\frac{2e^{-u/2}}{1-e^{-2u}},\qquad
 r(u)=k(u)-\frac{e^{-u}}u
   =\frac{e^{-u/2}-e^{-u}}u+2e^{-u/2}h(2u),               \tag{13}
\]

where h is L740's function. Its 0<h<1 bound shows r is integrable
on (0,infinity), with ||r||_1<=log(2)+4. In L740's q the cancellation
is exact:

\[
 q(u)=-1/u+k(u)-4\cosh(u/2),
 \qquad q(u)-d_0(u)=r(u)-4\cosh(u/2).                    \tag{14}
\]

Thus, with R_L convolution by r and V_L convolution by cosh(u/2)
on the causal finite interval,

\[
 A_Lf=(Bf)|_{(0,L)}+c f+R_Lf-4V_Lf+2aT_df,
                 \qquad c=\log(2\pi).                   \tag{15}
\]

Every term in this equation has been retained. In particular, V_L
represents both rational completion terms, not a discarded favorable
pole. Only R_L is represented by an integrable full-line kernel;
V_L is used on the finite interval.

DLMF 5.9.13, with z=(p+1/2)/2, and the convergent Frullani difference
in (13) give

\[
 \widehat r(p)=\log(p+1)-\psi((p+1/2)/2)-\log2.
                                                              \tag{16}
\]

This identity is valid also at p=it: all integrals defining r converge
absolutely, the digamma argument has real part 1/4, and both logarithms
used to evaluate the difference have positive real parts. For clarity,
the two parts of (13) have transforms
log(p+1)-log(p+1/2) and
-psi((p+1/2)/2)+log(p+1/2)-log2, respectively.
No critical-axis evaluation of xi'/xi is made.

Since f vanishes outside [0,L], its pairing with (Bf)|_(0,L) is its
full-line pairing. Plancherel and (16) show that the energy of
B+cI+R_L has symbol

\[
 w(t)-c-\Re\widehat r(it)
                   =\Re\psi(1/4+it/2)-\log\pi.           \tag{17}
\]

The gamma in G_L has already entered (9); it is not added again in c.
For the pole term, F_f(plus or minus i/2) are genuine bounded linear
functionals on L2(0,L). Fubini on the finite square gives

\[
 4\Re\langle V_Lf,f\rangle
 =4\int_0^L\cosh(u/2)\Re C_f(u)du
 =2\Re\bigl(F_f(i/2)\overline{F_f(-i/2)}\bigr).          \tag{18}
\]

For the arithmetic term Re<T_df,f>=Re C_f(d). The only nonzero
delay at this L is n=2, and the n=3 endpoint delay is zero almost
everywhere. Combining (15)--(18) proves (5) on D(A_L). These
calculations involve either L1 convolution, finite-interval bounded
kernels, or Plancherel with Bf in L2; no divergent prime sum or contour
interchange occurs.

Since r is L1, (17) differs from w by a bounded real function. The
pole and delay forms are bounded in L2 on the fixed window. Therefore
(5) is the nonnegative closed Fourier form integral w|F|^2/(2*pi),
of domain V_(0,L), plus a bounded Hermitian form. Adding a sufficiently
large multiple of ||f||_2^2 gives a norm equivalent to the V norm;
completeness of weighted Fourier L2 and closedness of the support
condition prove closedness and semiboundedness. The smooth density
proved above shows this is exactly the closure of (4), not an arbitrary
extension. It also matches the source localized form: the geometric
formulas agree on the smooth core, and their closed-form completions
agree. D(A_L) has not been equated with this larger form domain or with
the operator domain of a self-adjoint Friedrichs realization.

### 3. Restriction at the midpoint, including the singular coupling

On the full line let P be multiplication by 1_(-infinity,ell).
The compensating scalar terms in (7) commute with P. Directly,

\[
 (B_\epsilon P-PB_\epsilon)f(x)
 =\begin{cases}
 0,&x<\ell,\\
 \displaystyle\int_{y<\ell,\ x-y>\epsilon}
       \frac{e^{-(x-y)}}{x-y}f(y)dy,&x>\ell.
 \end{cases}                                               \tag{19}
\]

After u=x-ell, v=ell-y, its absolute kernel is at most 1/(u+v).
Carleman domination gives norm <=pi, uniformly in epsilon. The
operators in (19) converge strongly to the operator C with epsilon=0:
the integrals converge pointwise for almost every x>ell, and their
absolute values are bounded by the Carleman image of |f|, an L2
function. Dominated convergence of the squared difference applies.

For f in D(B), B_epsilon f -> Bf. Hence (19) shows B_epsilon Pf
converges in L2 to PBf+Cf. Its distributional limit is BPf by (7),
so Pf belongs to D(B) and BPf=PBf+Cf. The complementary projection
also preserves D(B). On functions supported in [0,L], this proves
preservation of W_(0,L), with bounded graph norms. It also proves
membership in the translated length-ell generator domains by (2)
and the already proved interval domain characterization. There is
no assumed midpoint value of f.

To extend restriction to the form domain without identifying it with
D(B), write h_B for the Hermitian form of -B and
q_B(f)=integral w|F_f|^2/(2*pi)>=0. For f in W_(0,L), put
f_0=Pf and f_1=(I-P)f. Causality gives <Bf_1,f_0>=0, and (19) gives

\[
 h_B(f_0,f_1)=-\tfrac12\langle Cf_0,f_1\rangle,
 \quad |h_B(f_0,f_1)|\le\tfrac\pi2\|f_0\|_2\|f_1\|_2.
\]

Consequently

\[
 q_B(f_0)+q_B(f_1)
 \le q_B(f)+\pi\|f_0\|_2\|f_1\|_2
 \le q_B(f)+\tfrac\pi2\|f\|_2^2.                         \tag{20}
\]

Each term on the left is nonnegative. Thus both restrictions are
bounded for the V norm on the dense subspace W_(0,L). Their continuous
extensions to V are the same L2 restrictions, proving the full claim.
This argument retains, rather than loses, the interface singularity.

We can now state its actual complete coupling. For x in (ell,L),
define an operator from L2(0,ell) to L2(ell,L) by

\[
 (C_Af_0)(x)=\int_0^\ell
       [k(x-y)-4\cosh((x-y)/2)]f_0(y)dy
       +2a\,{\bf1}_{x>d}f_0(x-d).                         \tag{21}
\]

The kernel in brackets is 1/(x-y)+q(x-y). Its first term is a
finite compression of the Carleman operator, and q has L1 norm on
(0,L) bounded in L740. The delay has norm at most one. Therefore

\[
 \|C_A\|\le\pi+\|q\|_{L^1(0,L)}+2a\le\pi+b_L.          \tag{22}
\]

This is only a boundedness estimate for closure, not the desired
energy-normalized estimate. Initially on the generator domain, the
opposite causal block is zero and (15) gives

\[
 H_L(f_0,f_1)=-\tfrac12\langle C_Af_0,f_1\rangle.         \tag{23}
\]

Smooth approximation within each half interval, using the V density
already proved, extends (23) to the entire split form domain: its
right side is L2-continuous by (22), and its left side is V-continuous.
In particular the delay part of (23) is exactly

\[
 -a\int_d^L f_0(x-d)\overline{f_1(x)}dx,                 \tag{24}
\]

since ell<d<L and L-d<ell. The diagonal blocks have no delay,
because ell=log(sqrt(3))<log(2), and translation makes each equal
to the complete length-ell energy. This identifies every block;
no scalar or boundary logarithm has been removed by splitting.

### 4. Applying the known sign theorem and obtaining kappa=1

Translate the support by -L/2. The norm and C_f are unchanged.
The Fourier transform on the real axis acquires a factor of modulus
one, while the two factors F_f(i/2) and overline(F_f(-i/2)) acquire
opposite real exponential factors. Their product is unchanged. Thus
(5) is translation invariant, including its signed pole term.

The centered support is [-ell,ell], strictly inside [-0.8,0.8]:
exp(1.6)>1+1.6+1.6^2/2>3 implies log(3)<1.6. Apply Zhu's cited
complex-test Corollary 6.3 to the translated smooth compact functions.
The normalization dictionary is explicit. Zhu uses the positive Fourier
exponent, so its transform is F_f(-t). The symbol in (3) of that paper
is even; changing t to -t preserves the integral. The two imaginary
arguments in the complex pole product are interchanged, conjugating
that product and preserving its real part. Its Lemma 6.1 and (14)
retain the negative odd pole and extend the assertion to complex tests;
the even-real formula (2) alone would not suffice. Finally,

\[
 \frac1{2\pi}\int_{\mathbb R}|F_f(t)|^2\cos(tu)\,dt
       =\Re C_f(u).
\]

This is Fourier inversion for the autocorrelation, with |F_f|^2 in L1.
Zhu's half-width 0.8 symbol includes n=2,3,4. For our support of length
L, C_f(u)=0 for |u|>=L: the two supports have intersection of measure
zero at equality and are disjoint beyond it. Thus its n=3 and n=4
terms vanish exactly, including the n=3 endpoint; its n=2 coefficient
is precisely -2a. Li Hongmin's (2.1) is therefore the same complete
form (5), with no positive rescaling of c_* or of the norm required.
The smooth-core density and closed-form continuity proved in sections
1--2 extend its lower bound to every f in V_(0,L). In particular
E_L(f)>=c_*||f||_2^2. This is a use of the cited theorem, not an
independent replay of its certified sign calculation.

The Hermitian form H_L is now positive on V_(0,L). Apply positivity
to f_0+z f_1 for every complex z. With the convention of (4), its
value is E_L(f_0)+2 Re(conj(z)H_L(f_0,f_1))+|z|^2 E_L(f_1).
If f_1 is nonzero, E_L(f_1)>0 by (3); substituting
z=-H_L(f_0,f_1)/E_L(f_1) yields
|H_L(f_0,f_1)|^2<=E_L(f_0)E_L(f_1). If f_1=0 the conclusion
is immediate. This proves (6), and hence kappa=1, with the exact
coupling (21)--(24) and the full block/domain extension paid.

### 5. Separate conceptual audit, 4 November 2026, step 278

The audit covers the written bridge, not a new positivity theorem or
an independent validation of Zhu's supplementary computation. Reuse
L740's audited exact domain and the source hypotheses identified above.
The audit directly rechecked Zhu v2 (2)--(3), Lemma 6.1 and its proof, (14),
Corollary 6.3 and its proof, Li Hongmin v1 (2.1), and DLMF 5.9.13/18
for the normalization checks. The known Carleman bound and the
previously assessed source form-core coverage are unchanged imports.

1. **Distribution and both endpoint inclusions.** For a compact smooth
   test phi the difference between the right side of (9) and the
   truncated kernel in (7) is
   phi(0)[gamma+log(epsilon)+E_1(epsilon)]+o(1), which tends to zero;
   here E_1(epsilon)=integral_epsilon^infinity e^(-u)/u du.
   The replacement of
   log(epsilon)phi(epsilon) by log(epsilon)phi(0) has error
   O(epsilon|log(epsilon)|), and the omitted d_0 integral tends to zero.
   This fixes the sign of gamma. The uniform multiplier bound follows
   from integrating e^(-u)min(2,|t|u)/u, so both the strong limit on
   D(B) and the distributional limit on L2 are valid. The continuous
   convolution Phi_f has no jump at 0 or L. Its derivative in (11)
   is Carleman-bounded on the entire exterior half-line; integration
   to either endpoint is legitimate by local L1 control. Hence the
   interior and exterior AC representatives glue without deltas.
   Equation (12) bounds the exterior Bf, while (10) bounds the interior.
   Conversely the distributional interior derivative in (10) is L2
   if the zero extension is in D(B). These are both inclusions, not
   an inference from a core identity alone.

2. **Graph and form completions.** The bounded imaginary part of b and
   the exterior estimate give equivalence of the full supported W norm
   and the A_L graph norm, in both directions. For exponent alpha=1,2,
   a change of Fourier variable bounds the squared norm of the support
   contraction by
   integral (1+w(s/r))^alpha |F_f(s)|^2 ds/(2*pi). The weights are
   uniformly comparable for r in (1/2,1); density in weighted L2 gives
   strong convergence, and the translation phase preserves the weight.
   Subsequent interior mollification gives the claimed graph and form
   cores. The support constraint is closed under L2 convergence.
   Equation (17) and boundedness of the pole/delay forms then make the
   shifted energy norm equivalent to the V norm. The closure is V,
   while the generator domain is W; no self-adjoint operator-domain
   identification is used. This independent argument is necessary
   because Suzuki's form-core assertion alone does not identify A_L.

3. **Complete scalar and signed terms.** In (14), the -1/u from q
   cancels the undamped logarithmic kernel; after subtracting d_0 the
   remainder is exactly r-4cosh(u/2). The integral of r is finite,
   including the origin. In (16), p=it keeps p+1 and p+1/2 in the
   right half-plane and the digamma argument at real part 1/4, meeting
   DLMF's hypothesis without continuation across a pole. Subtracting
   c=log(2*pi) leaves precisely Re psi-log pi. Finite-square Fubini
   yields the signed product in (18), not a nonnegative modulus square.
   Re<T_df,f>=Re C_f(d), so the arithmetic sign and factor are -2a.
   The n=3 endpoint is the zero delay operator on this interval.
   All terms and the original norm survive the energy identification.

4. **Singular cut and form restriction.** After u=x-ell and v=ell-y,
   (19) is a compression of e^(-(u+v))/(u+v), dominated by the
   Carleman kernel. At each u>0 the cutoff is inactive once epsilon<u;
   the Carleman image of |f| supplies an L2 dominating function. This
   proves strong convergence, not operator-norm convergence. Together
   with the distributional limit it gives BPf=PBf+Cf on D(B).
   Causality makes the reverse block zero. The resulting cross energy
   has coefficient -1/2 and gives (20). Applying (20) to differences
   in the dense W subspace proves that both restrictions extend
   continuously in V and agree with the L2 restrictions. There is no
   hidden boundary or midpoint trace hypothesis. For the actual C_A,
   subtracting its Carleman kernel leaves q, an L1 convolution kernel;
   its delay is bounded. Equation (22) therefore justifies passage
   of the full cross form to V. It supplies no sign by itself.

5. **Imported positivity and complex polarization.** The dictionary
   now written in section 4 checks the Fourier convention, complex
   pole, endpoint shifts and unchanged norm explicitly. Translation
   multiplies the two imaginary evaluations by reciprocal real factors.
   Apply Corollary 6.3 first on the smooth core and then pass in V;
   no assertion that arbitrary L2 functions have finite energy is
   necessary. The lower bound gives positivity for every complex
   combination of the two restrictions. Minimizing in z with the
   first-argument-linear convention gives exactly (6), with kappa=1.
   This is a consequence of the cited full-window positivity, not an
   independent bound that could be iterated to prove that positivity.

No counterexample or coefficient/domain failure was found in this
audit. The conclusion is a checked local specialization, with full
Mathlib coverage still unchecked and the cited computation still
unreplayed. The direct mathematical input remains L740, so the DAG
row is unchanged. Larger-window coupling, treatment of all windows
at a fixed parameter, and actual-Xi mixed signs remain independent gaps.

### Qualifications and relevance

The successful bounded test supplies a known local sign seed in the
original norm and a local analytic bridge to L740. The numerical lower
bound comes solely from Zhu's theorem and remains subject to the stated
source qualification. The crude bound (22) was not used to certify
kappa<=1. No norm estimate is extrapolated to larger intervals, where
additional arithmetic delays enter; no critical-axis full-line multiplier
for xi'/xi, no reflection composition law and no square ordering is
asserted. The earlier L739 obstruction and the realization-only stop
are contrasts, not mathematical inputs to this proof. Independent
larger-window coupling and actual-Xi mixed signs remain unresolved.

## Mathlib

Full coverage of this causal-generator/localized-Weil identification,
its logarithmic form domain and the midpoint restriction has not been
checked; availability is unknown. The source computer-assisted theorem
is not a local Lean verification. L740 records its own supporting
coverage and qualifications. Plancherel, ordinary convolution identities
and the named Carleman theorem are informal mathematical inputs here;
no full matching Mathlib theorem or formal RH consequence is claimed.
