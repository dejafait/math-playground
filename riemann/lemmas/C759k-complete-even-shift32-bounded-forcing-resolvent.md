# C759k: Complete even shift32 resolvent on bounded forcing

## Hypotheses

Let I=(-1,1), E be zero extension, and H_e the real even subspace
of L2(I). Use exactly the complete closed Weil form of C759a(1),(5)-(6),
with self-adjoint form operator A_e on H_e, as in C759h. In particular
all five overlapping prime powers n=2,3,4,5,7 and both original pole
functionals are retained. Bounded means essentially bounded, and
all asserted function equalities are equalities of equivalence classes.
No sign, neutrality, isolation, simplicity or RH hypothesis is imposed.

This is the known-method SPECIALIZE target of
`drafts/literature/2026-11-13-even-bounded-residual-specialization-834.md`,
whose source approval835 predates this step. The precise standard
inputs and their specialization are given below. The result is a local
REPRODUCTION, not a claim of a new general resolvent theorem.

## Conclusion

For every real even g in L-infinity(I), the L2 inverse exists and satisfies

\[
 \|(A_e+32I)^{-1}g\|_\infty\le\frac18\|g\|_\infty.       \tag{1}
\]

The perturbation has norm strictly below24 on both relevant spaces;
the required budget is strictly below32. No complete-operator order
preservation is asserted. This supplies only an unsigned, unweighted
bounded-forcing estimate. It does not supply an L2-to-supremum estimate,
a boundary-relative bound, eigenfunction isolation or sign, parity
ordering, a residual certificate for any particular trial, or Xi transfer.
The separate conceptual audit in Proof5 accepts this specialization.

## Proof

### 1. Exact killed reference and complete bounded perturbation

Write w(t)=half log(1+t²). Let G be the nonnegative killed reference
operator on I whose closed form is

\[
 q_G(f,h)=\int_{\mathbb R}w(t)\widehat{Ef}(t)
                   \overline{\widehat{Eh}(t)}\frac{dt}{2\pi}.
                                                               \tag{2}
\]

Its form domain is the closure of smooth compact functions on I in
the supported weighted Fourier norm of C759a(6). C759a Proof1 proves
that this closure equals the entire supported weighted space, including
its parity restriction. The reference/form identification is precisely
L515's reference, translated from (0,2) to I. It imports Fukushima,
Oshima and Takeda, *Dirichlet Forms and Symmetric Markov Processes*,
second revised edition, Theorems4.4.2-4.4.3, pp173-175: the regular
symmetric whole-line Levy form and its part on the open interval give
the killed process, with this smooth-core closure. Thus the identification
uses equality of forms and their closures, not symbol growth alone.
The Levy density is exp(-|x|)/(2|x|); the exponent is w.

Its L2 contraction C0-semigroup T_t=exp(-tG) acts consistently on
bounded data by the killed transition kernel. The primary normalization
and killed-kernel domination are Grzywny-Ryznar, *Potential theory of
one-dimensional geometric stable processes*, arXiv:1107.0745v1,
[Section2, (2.1)-(2.4) and the following killed-process formulas](https://arxiv.org/html/1107.0745v1).
Their alpha=2 process has exponent log(1+t²), so we use half speed.
In particular

\[
 \|T_t\|_{2\to2}\le1,\qquad
 \|T_tf\|_\infty\le\|f\|_\infty\quad(f\in L2\cap L^\infty).
                                                               \tag{3}
\]

This reference is killing the Levy process, not subordinating killed
Brownian motion. These standard inputs are reused from the approved
assessment; no source theorem is reproved.

Let b=log(2pi) and use the one-sided real integrable function r in
L741(13),(16). Define on R, with the value at0 immaterial,

\[
 \rho(x)=\tfrac12r(|x|),\qquad
 \|\rho\|_1=\|r\|_{L1(0,\infty)}\le\log2+4.
\]

Even symmetrization and the absolute integrability give
hat rho(t)=Re hat r(it), with L741's Laplace-transform notation.
C759a(5) therefore gives the exact multiplier identity
m(t)=w(t)-b-hat rho(t). Let

\[
 Rf=(\rho*Ef)|_I,\quad
 Jf=\sum_{n\in\{2,3,4,5,7\}}a_n
                  [Ef(\cdot+\log n)+Ef(\cdot-\log n)]|_I,
 \quad a_n=\Lambda(n)/\sqrt n,
\]
\[
 v(x)=\cosh(x/2),\quad Pf=2v\langle v,f\rangle,\qquad
 K=bI+R+J-P \quad\hbox{on }H_e.                              \tag{4}
\]

Before even restriction the two poles are the operator with kernel
exp((x-y)/2)+exp(-(x-y)/2)=2cosh((x-y)/2).
For even f its sinh moment vanishes, leaving exactly Pf. This is
C759h Proof1's complete pole, not a convolution substitution or a
discarded favorable term. The sign of P in A_e is positive.
Each term of K is bounded and symmetric on L2 and preserves parity.
Plancherel and polarization now give, on the common closed form domain,

\[
 q_{A_e}(f,h)=q_G(f,h)-\langle Kf,h\rangle.                  \tag{5}
\]

The full five-shift operator here has the zero-extension masks in (4).
For the same reason that bounded form perturbations preserve the operator
domain, (5) implies

\[
 D(A_e)=D(G)\cap H_e,\qquad A_e=G-K.                        \tag{6}
\]

Explicitly, the form functional for one operator is L2-bounded if and
only if that for the other is, since their difference is the bounded
functional represented by Kf. The representation theorem then gives
both domain equality and (6). No causal generator from L741 is used.

### 2. Compatible perturbations and a strict common budget

Young's inequality gives norm at most ||rho||_1 for R on L2 and
L-infinity. Fubini shows the two constructions agree on their
intersection. Each masked translation in J is a contraction in both
spaces. It respects equivalence classes: translation carries a null
set to a null set; multiplication by the interval mask and restriction
preserve this property. The finite-rank P is defined by the same
Lebesgue integral in both spaces. Thus K is a compatible operator
on even L2 and even L-infinity; no point values are required.

For explicit conservative bounds, 2<e<3 and pi<4 give
b<log8<3, and ||rho||_1<=log2+4<5. The inequality e<3 follows, for
example, from the exponential series using n!>=2^(n-1) for n>=2,
with strict inequality for n>=3. For every x>=1 the maximum of
log(x)/sqrt(x) is2/e<1, by differentiating. Since Lambda(n)<=log n,
all five a_n<1, and hence

\[
 \|J\|_{2\to2}<10,\qquad \|J\|_{\infty\to\infty}<10.      \tag{7}
\]

These are paired-shift triangle bounds, not the sharper L2 chain
estimate of C759a. No L2 chain constant is transferred to L-infinity.
Direct integration and v>=0 yield

\[
 \|P\|_{2\to2}=2\|v\|_2^2=2(1+\sinh1)<5<6,
\]
\[
 \|P\|_{\infty\to\infty}
 =2\|v\|_\infty\int_Iv(x)dx
 =8\cosh(1/2)\sinh(1/2)=4\sinh1<6,                         \tag{8}
\]

where sinh1=(e-e^(-1))/2<3/2. The supremum in the second equality
is an essential supremum; constant forcing attains the norm limit.
Consequently both compatible K norms satisfy

\[
 \|K\|_{2\to2}<3+5+10+6=24<32,
 \qquad \|K\|_{\infty\to\infty}<24<32.                    \tag{9}
\]

The even pole is included by its absolute norm, so no positivity
property of the complete semigroup or resolvent enters this estimate.

### 3. Reference resolvent without an L-infinity C0 assumption

On L2, import the Laplace-resolvent theorem: Jacob-Zwart,
*14th Internet Seminar: Infinite-dimensional Linear Systems Theory*,
2010-11 course version,
[Proposition5.2.4(a), pp59-60](https://www.math.tecnico.ulisboa.pt/~czaja/ISEM/14internetseminar201011.pdf).
The hypotheses are a C0-semigroup on its Hilbert space and a Laplace
parameter strictly above a valid exponential growth bound. Here (3)
gives growth bound at most0; one may take omega=1 and parameter32.
It identifies the L2 strong integral

\[
 R_0=(G+32I)^{-1},\qquad
 R_0g=\int_0^\infty e^{-32t}T_tg\,dt,
 \qquad \|R_0\|_{2\to2}\le1/32.                            \tag{10}
\]

For bounded g on the finite interval, g belongs to L2. For any real
h in L2(I), hence also L1(I), (3) and the L2 integral give

\[
 |\langle h,R_0g\rangle|
 \le\int_0^\infty e^{-32t}\|h\|_1\|g\|_\infty dt
 =\|h\|_1\|g\|_\infty/32.                                 \tag{11}
\]

This implies R_0g is essentially bounded by ||g||_infinity/32:
if its absolute value exceeded that bound by epsilon on a set of
positive measure, test with its sign times that set's indicator, an
L2 function, to contradict (11). Thus (10) defines a compatible
bounded-data action with L-infinity norm at most1/32. This is an
L2 Bochner integral and an L2 duality argument, not an assertion of
strong measurability or strong continuity in L-infinity. Reflection
commutes with the reference form and semigroup, so the same bound
holds on even data.

### 4. Consistent Neumann series and the full inverse

By (9)-(11), R_0K has norm at most3/4 on each even space. For any
even g in L-infinity form the single compatible series

\[
 u=\sum_{j=0}^\infty(R_0K)^jR_0g.                            \tag{12}
\]

Its terms have L-infinity norm at most
(3/4)^j||g||_infinity/32, so it converges in L-infinity with norm
at most ||g||_infinity/8. It also converges in L2 by (9)-(10).
On the length2 interval, L-infinity convergence implies L2 convergence,
so the two limits are the same equivalence class. This explicitly pays
the stronger-norm passage.

The L2 geometric series gives u=R_0(g+Ku). Its right side belongs
to D(G), so (G+32I-K)u=g, that is (A_e+32I)u=g by (6).
The same series works for every even L2 input and is unique there:
a homogeneous solution satisfies u=R_0Ku and therefore vanishes since
||R_0K||_2<1. This proves L2 invertibility and identifies (12) with
the L2 inverse, establishing (1).

No differentiations at an endpoint, spectral extrapolations, numerical
quadratures, tail truncations or interchange of unbounded prime sums
occur. The only infinite integrals are the standard L2 Laplace
integral and the already absolutely integrable remainder; the series
is geometrically summable in both relevant norms.

### 5. Separate conceptual audit, 13 November2026, step838

The prior SPECIALIZE assessment
`drafts/literature/2026-11-13-even-shift32-resolvent-audit-836.md`
covers this exact audit. Its GR, FOT and Jacob-Zwart primary coverage
is reused with the recorded retrieval qualifications; no new source
theorem or mathematical parameter is introduced. The result passes.
This establishes a checked local known-method input, not progress
beyond the cited general theorems or a sign theorem for Q.

**Reference form and its exact domain.** The normalization of the
whole-line Levy density is important: integrating the two half-lines
in its characteristic exponent gives

\[
 \int_{\mathbb R}(1-\cos(tx))\frac{e^{-|x|}}{2|x|}\,dx
 =\int_0^\infty(1-\cos(tx))\frac{e^{-x}}x\,dx
 =\tfrac12\log(1+t^2).
\]

For this normalization check, differentiating the last integral in t
is allowed by domination by e^(-x); its derivative is t/(1+t²),
and its value at0 is0. This checks the local factor, not a reproof
of the cited killed-process theorem. Thus GR's half-speed process
and L515's reference are exactly the same whole-line process.

The FOT import used here concerns a regular symmetric form and an
open part. The whole-line Fourier form is regular as recorded in
L513's FOT applicability argument and used in L515: smooth convolution
approximates in form norm, and spatial cutoffs are justified by the
integrability of min(1,x²)e^(-|x|)/(2|x|). Its open interval part has
the closure of the compact smooth core. Translation from (0,2) to
(-1,1) multiplies the Fourier transform by a phase and leaves the
form unchanged. Cadlag paths starting in this open interval remain
in it for a positive initial time, as required in the recorded
part-process correspondence. Killing is applied to this process;
there is no substitution of a spectral fractional Dirichlet operator.

To check that this core closure is the supported space used by A_e,
put W(t)=1+half log(1+t²). For 1/2<r<1 one has
W(s/r)<=W(s)+log2, while W>=1. Consequently the dilation
F(t) -> r^(1/2)F(rt) is uniformly bounded in L2(W dt).
It converges strongly to the identity on continuous compactly
supported Fourier functions, and then on all of L2(W dt) by density
and that uniform bound. Applied to a function supported in [-1,1],
this is C759a's support contraction into [-r,r]. A nonnegative real
even smooth mollifier of integral1, supported within the remaining margin, has
Fourier multiplier bounded by1 and tending pointwise to1. Dominated
convergence in L2(W dt) completes the compact smooth approximation.
Conversely a limit of such functions has zero extension supported
in [-1,1], by L2 convergence, and belongs to the weighted space by
completeness. Both domain inclusions are therefore paid. Endpoint
values, which are irrelevant for L2 classes, impose no extra trace
condition. Reflection preserves the norm and the core, so this
identification also holds in the even sector.

**Complete signed perturbation.** With rho(x)=r(|x|)/2,
the ordinary Fourier transform is
hat rho(t)=integral_0^infinity r(x)cos(tx)dx=Re hat r(it).
This uses L741(13),(16), including absolute integrability on the
imaginary axis, not a growth-only comparison of multipliers. Hence
the multiplier contribution is G-bI-R, with exactly the sign in(5).
Each paired masked translation is self-adjoint on L2, with quadratic
value 2C_f(log n). Its coefficient in A_e is negative. For general
real f, polarizing the two original poles gives the kernel
2cosh((x-y)/2). Even restriction kills the sinh moment, leaving
the positive operator P=2v<v,.>. Thus A_e=G-bI-R-J+P=G-K.
No pole, mask or overlapping prime power is omitted.

All these bounded L2 operators preserve the real even space. For
f in the common form domain, the functional q_G(f,.) is represented
by an L2 vector exactly when q_A(f,.) is, because their difference
is represented by Kf. This proves both operator-domain inclusions
in(6). On the even space this is the restriction of G, since
reflection commutes with the closed form and hence its operator.
The causal generator of L741 is not used in this identification.

**Budget in both norms.** Young's inequality applies to the full L1
kernel rho before restriction, giving ||R||<=log2+4<5. Translation
and zero extension give norm at most1 per masked shift in each
space; they carry null sets to null sets. The maximum of
log(x)/sqrt(x) on x>=1 is2/e<1. All five coefficients a_n are
therefore strictly below1, giving ||J||<10 without transferring an
L2 chain improvement to L-infinity. Also 0<b<3. For the pole,

\[
 \int_{-1}^1\cosh^2(x/2)dx=1+\sinh1,\qquad
 \int_{-1}^1\cosh(x/2)dx=4\sinh(1/2).
\]

These give exactly ||P||_2=2(1+sinh1)<5 and
||P||_infinity=4sinh1<6, using e<3. The real even constant
test also shows that restricting to the even sector does not
invalidate the claimed L-infinity norm computation. Accordingly
each K norm is strictly below24; the required bound is32. The
conservative use of6 for both pole norms is legitimate. Fubini,
translation invariance of null sets and the same finite-rank
Lebesgue integral establish compatibility, not merely equal norms.

**Reference inverse and the stronger norm.** The reference is
nonnegative self-adjoint, so its L2 semigroup is a contraction and
is strongly continuous. Jacob-Zwart Proposition5.2.4(a) applies to
generator -G with omega=1 and s=32, since its growth bound is at
most0. The proposition identifies the strong L2 integral; the
sharper norm1/32 in(10) is obtained by integrating the actual
contraction bound, not by misreading the proposition's1/31 bound
at omega=1. The killed kernel gives the compatible L-infinity
contraction for every bounded datum.

For such a datum g, finiteness of |I| ensures g is L2. Pairing the
L2 integral with any real L2 test h is justified by its absolute
scalar integral, bounded by ||h||_1||g||_infinity/32. If the
resulting L2 vector exceeded ||g||_infinity/32 in absolute value
on a set of positive measure, some positive epsilon level set
would also have positive measure. Its indicator times the sign
of that vector is an admissible L2 test and contradicts(11).
Thus the reference resolvent bound really holds on bounded data.
Neither strong continuity nor Bochner integration in L-infinity
has been assumed. Evenness follows from reflection commutation.

**The common series and both inverse identities.** Each term of(12)
is the same L2/L-infinity equivalence class because R_0 and K are
compatible. Its L-infinity norm is bounded by
(3/4)^j||g||_infinity/32. Hence the sum converges in that norm,
and its norm is at most (1/32)/(1-3/4)=1/8 times ||g||_infinity.
It converges in L2 as well. The inequality ||f||_2<=sqrt2||f||_infinity
identifies the two limits; convergence in L2 alone would not suffice.

For every even L2 datum, the L2 series defines a bounded operator S
and satisfies Sg=R_0(g+KSg). It follows that Sg belongs to D(G)
and (A_e+32I)Sg=g. Conversely, if f is in D(A_e), put
g=(A_e+32I)f. Both f and Sg solve the same equation. Their difference
equals R_0K times itself and vanishes since ||R_0K||_2<1.
Thus S(A_e+32I)f=f as well. This verifies surjectivity, uniqueness,
the operator domain and identification with the L2 inverse.

The audit needs no mathematical script or numerical quadrature.
All constants are controlled by elementary strict bounds, the
reference integral by contraction, and the series by its geometric
majorant. C759i's order obstruction, C759j's unrestricted L2
conversion stop, and the missing isolation/boundary/sign/Xi inputs
remain intact. In particular, this audit does not establish a
boundary-weighted bound or an eigenfunction enclosure.

## Mathlib

Full matching theorem and supporting Mathlib coverage were not checked.
This is a specialization of the cited killed-reference, part-form and
Hilbert-space Laplace-resolvent theorems, with the explicit compatible
perturbation and norm-limit argument above. No absence or formal
verification claim, new general theory, or RH conclusion is asserted.
