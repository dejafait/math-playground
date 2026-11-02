# L611: reciprocal-cutoff first variation at a hypothetical double zero

## Hypotheses

Use the full half-line theta kernel K of L019 and the Xi normalization of
L020. For epsilon>=0 and z in C define, exactly as in L610,

\[
 W_\epsilon(u)=\frac{e^{-\epsilon e^{-2u}}+e^{-\epsilon e^{2u}}}{2},
 \qquad F_\epsilon(z)=\int_0^\infty K(u)W_\epsilon(u)\cos(zu)\,du,
 \qquad D_1(F;t)=F'(t)^2-F(t)F''(t).
\]

The L610 numerical assertion and computational qualification are not
inputs. Put

\[
 Q(z)=\frac{\Xi(z+2i)+\Xi(z-2i)}2.
\]

For the double-zero specialization only, assume a is real and
Xi(a)=Xi'(a)=0, A=Xi''(a) is nonzero. No such a is asserted to exist.
All cutoff limits below are from epsilon>=0.

## Conclusion

For every finite R>=0, every epsilon>=0, and j=0,1,2,

\[
 \sup_{|z|\le R}
 |F_\epsilon^{(j)}(z)-\Xi^{(j)}(z)+\epsilon Q^{(j)}(z)|
 \le \epsilon^2 M_{j,R},\qquad
 M_{j,R}=\frac12\int_0^\infty K(u)u^j e^{Ru}\cosh(4u)\,du<\infty.
 \tag{1}
\]

In particular the right parameter derivative of F_epsilon^(j) at zero
is -Q^(j), uniformly on these compact sets. Uniformly for real |t|<=R,

\[
 D_1(F_\epsilon;t)=D_1(\Xi;t)
 +\epsilon\{\Xi(t)Q''(t)+\Xi''(t)Q(t)-2\Xi'(t)Q'(t)\}
 +O_R(\epsilon^2)\quad(\epsilon\downarrow0).
 \tag{2}
\]

At the fixed hypothetical double zero,

\[
 D_1(F_\epsilon;a)
 =\epsilon\,\Xi''(a)\operatorname{Re}\Xi(a+2i)+O_a(\epsilon^2).
 \tag{3}
\]

If c=Xi''(a) Re Xi(a+2i) is strictly positive, this first form is
strictly positive for all sufficiently small positive epsilon; if c is
strictly negative, it is strictly negative for all sufficiently small
positive epsilon. If c=0, this leading-order test only gives O_a(epsilon^2)
and does not decide the sign. Neither strict-sign hypothesis is established
here for actual Xi. There is no height-uniform threshold, moving-frequency
claim, zero-splitting claim, higher-sign assertion or RH conclusion.

## Proof

**Analytic domination and the parameter derivative.** L019 gives
K(u)<=C exp(9u/2-pi exp(2u)) on u>=0. Thus K(u)u^j exp(Bu) is
integrable for every fixed B and nonnegative integer j. In particular
all constants in (1) are finite. For epsilon>=0, 0<W_epsilon<=1, so
the defining integral is entire in z with every fixed frequency
derivative locally uniformly convergent, by the same domination as
L020. For j frequency derivatives, the absolute value of the derivative
of cos(zu) is at most u^j exp(Ru) on |z|<=R.

For epsilon>=0 the first two parameter derivatives of the weight are

\[
 \partial_\epsilon W_\epsilon
 =-\frac{e^{-2u}e^{-\epsilon e^{-2u}}+e^{2u}e^{-\epsilon e^{2u}}}{2},
 \qquad
 \partial_\epsilon^2 W_\epsilon
 =\frac{e^{-4u}e^{-\epsilon e^{-2u}}+e^{4u}e^{-\epsilon e^{2u}}}{2}.
\]

Their absolute values are bounded by cosh(2u) and cosh(4u), respectively,
uniformly in epsilon>=0. After multiplication by K(u)u^j exp(Ru)
these are integrable. Dominated differentiation, including right
derivatives at zero, therefore commutes with the integral and with the
needed frequency derivatives. No extension to negative epsilon is used.

At zero the first derivative of the weight is -cosh(2u). The elementary
complex-cosine identity and L020, applied at both shifted arguments, give

\[
 \int_0^\infty K(u)\cosh(2u)\cos(zu)\,du
 =\frac12\int_0^\infty K(u)
       \{\cos((z+2i)u)+\cos((z-2i)u)\}\,du
 =Q(z).
\]

Both integrals, and their required derivatives, converge absolutely
locally uniformly: replace R by R+2 in the preceding exponential
majorant. This verifies the shift, its factor 1/2 and the derivative's
minus sign. For real t, conjugation of the L020 integral gives
Xi(t-2i)=conj(Xi(t+2i)), hence Q(t)=Re Xi(t+2i). Q and all its
real-frequency derivatives are real on R.

**Uniform remainder.** Taylor's theorem with integral remainder gives,
for every real x>=0,

\[
 e^{-x}=1-x+\int_0^x(x-v)e^{-v}\,dv,
 \qquad 0\le e^{-x}-1+x\le x^2/2.
\]

Apply this separately to x=epsilon exp(-2u) and x=epsilon exp(2u),
then average. The pointwise weight remainder obeys

\[
 0\le W_\epsilon(u)-1+\epsilon\cosh(2u)
 \le\frac{\epsilon^2}{4}(e^{-4u}+e^{4u})
 =\frac{\epsilon^2}{2}\cosh(4u).
\]

Multiplying by each frequency derivative of the cosine and using the
integrable majorant proves (1). The weight remainder is nonnegative,
but its cosine transform has no asserted sign. Boundedness of Xi, Q
and their derivatives on a compact set, followed by multiplication of
the three expansions (1), proves (2): the linear term in F'^2 is
-2 epsilon Xi' Q', and the linear term in -F F'' is
epsilon(Xi Q''+Q Xi''). All remaining products are uniformly
O_R(epsilon^2) for 0<=epsilon<=1.

For an explicit audit of this last uniformity, write
f_j=Xi^(j)(t), q_j=Q^(j)(t) and
F_epsilon^(j)(t)=f_j-epsilon q_j+epsilon^2 r_j(t,epsilon).
By (1), |r_j|<=M_{j,R}. The exact remainder in (2), divided by
epsilon^2 for epsilon>0, is

\[
 (-q_1+\epsilon r_1)^2+2f_1r_1-f_0r_2-f_2r_0
 -(-q_0+\epsilon r_0)(-q_2+\epsilon r_2).
\]

Put B_j=sup_(|t|<=R)|Xi^(j)(t)| and
H_j=sup_(|t|<=R)|Q^(j)(t)|, both finite. For 0<epsilon<=1
the absolute value of this remainder is bounded by

\[
 E_R=(H_1+M_{1,R})^2+2B_1M_{1,R}+B_0M_{2,R}+B_2M_{0,R}
       +(H_0+M_{0,R})(H_2+M_{2,R}).
\]

This verifies the compact-set dependence without requiring a sign for
the transformed weight remainder.

**Double-zero substitution and strict signs.** Fix R>=|a|. For
epsilon>0 write

\[
 F_\epsilon(a)=-\epsilon q_0+\epsilon^2 r_0,\quad
 F_\epsilon'(a)=-\epsilon q_1+\epsilon^2 r_1,\quad
 F_\epsilon''(a)=A-\epsilon q_2+\epsilon^2 r_2,
\]

where q_j=Q^(j)(a), and (1) gives |r_j|<=M_{j,R}.
Substitution yields the exact identity

\[
 D_1(F_\epsilon;a)-\epsilon A q_0
 =\epsilon^2\bigl[
  (-q_1+\epsilon r_1)^2-A r_0
  -(-q_0+\epsilon r_0)(-q_2+\epsilon r_2)\bigr].
\]

Consequently for 0<epsilon<=1 its absolute value is at most C_a epsilon^2,
with the explicit finite choice

\[
 C_a=(|q_1|+M_{1,R})^2+|A|M_{0,R}
       +(|q_0|+M_{0,R})(|q_2|+M_{2,R}).
\]

This proves (3). If c=A q_0 is nonzero, taking
0<epsilon<min{1,|c|/[2(C_a+1)]} bounds the error by
|c|epsilon/2 and proves both strict-sign implications. This threshold
is local to the fixed hypothetical a and its shifted data. If c=0 the
same estimate gives only the claimed order bound. Existence of a,
control of c and any global sign inference have not been used or proved.

This is a routine specialization of dominated differentiation and
Taylor's theorem, classified REPRODUCTION under the saved assessment.
The local proof is needed to compute this exact non-Gaussian weight's
shift and error; it does not reprove or import heat-flow preservation,
Weierstrass preparation or a collision theorem. The inspected literature
does not establish the needed sign of c; that bounded comparison is not
a novelty or theorem-absence claim.

Independent bounded audit, 1 November 2026: the j<=2 parameter
majorants, factor 1/2 in the shift, right-sided Taylor estimate,
exact determinant remainders and both strict-sign thresholds were
checked against L019/L020. No assertion or sign hypothesis was changed;
the explicit E_R above makes the compact uniformity check inspectable.
The audit does not use L610's qualified execution.

## Mathlib

Full matching coverage and supporting dominated-parameter/Taylor theorem
names have not been checked. No absence claim or formal verification is
made. L019/L020 retain their recorded coverage qualifications.
