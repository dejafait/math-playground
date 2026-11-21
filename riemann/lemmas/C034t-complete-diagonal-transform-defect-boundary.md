# C034t: complete diagonal transform and the unpaid defect boundary

## Hypotheses

Retain C034s's exact arithmetic and kernel definitions:
\[
 c_2=\zeta(2)^{-1},\qquad
 d(a,b)=1_{(a,b)=1}\mu(a)\mu(b)\rho(ab),\qquad
 M_K=\sum_{a,b\le K}\frac{d(a,b)}{\sqrt{ab}}k(\log(b/a)).
\]
Here \(q=2\), \(Q=\log2\), \(g(y)=e^{-1/(1-y^2)}1_{|y|<1}\),
\(h=-g''+g/4\), \(f=J(C_\Phi h)\),
\(C_h(r)=\int f(y)f(y+r)dy\), and
\[
 k(r)=C_h(r)1_{|r|<Q}
       \int_{|r|/2}^{Q-|r|/2}e^{-s/2}(s^2-r^2/4)\,ds.
\]
The arithmetic weight is
\(\rho(n)=c_2\prod_{p\mid n}p/(p+1)\).
C034s supplies the real even continuous kernel, its Fourier density
\(\lambda=\widehat k\ge0\) in \(L^1(\mathbb R)\),
\(\int\lambda/(2\pi)=k_0:=k(0)>0\), and
\[
 D(u,v)=\frac{\mathcal H(u,v)}{\zeta(u)\zeta(v)},\qquad
 \mathcal H(u,v)=c_2\prod_p
 \frac{1-\frac p{p+1}(p^{-u}+p^{-v})}
      {(1-p^{-u})(1-p^{-v})}.
\]
The series defining \(D\) is absolute for \(\Re u,\Re v>1\);
\(\mathcal H\) is holomorphic for
\(\Re u,\Re v>0\), \(\Re(u+v)>1\).
Fourier transforms have phase \(e^{-itr}\) and inverse factor \(1/(2\pi)\).

The statements involving a zero are conditional on an actual zero
\(\rho_*=\beta+i\gamma\), \(\beta=1/2+\delta\),
\(0<\delta<1/2\), of exact finite order \(m\ge1\).
Set \(a_*=2\delta\in(0,1)\). No rightmost zero, simplicity,
uniform separation, sign of \(M_K\), or RH is assumed.

## Conclusion

For \(\Re z>1\) the full integral
\[
 \mathcal F(z)=\int_2^\infty M_{\lfloor X\rfloor}X^{-z-1}\,dX
\]
converges absolutely and has the exact representations
\[
 \mathcal F(z)=\frac1z\sum_{a,b\ge1}
 \frac{d(a,b)}{\sqrt{ab}}k(\log(b/a))\max(2,a,b)^{-z},       \tag{1}
\]
\[
 \mathcal F(z)=E(z)+\frac1{2\pi z}\int_{\mathbb R}
 W_z(t)D(s_z+it,s_z-it)\,dt,\qquad
 s_z=\frac{1+z}{2},\quad E(z)=c_2k_0\frac{2^{-z}-1}{z},     \tag{2}
\]
where \(E\) extends to an entire function and
\[
 W_z=\widehat{\,k(r)e^{-z|r|/2}\,},\qquad
 W_z(t)=\frac1{2\pi}\int_{\mathbb R}
 \lambda(\tau)\frac{z}{z^2/4+(t-\tau)^2}\,d\tau
 \quad(\Re z>0).                                         \tag{3}
\]
Both square boundaries and the lower endpoint are included. The domain
\(\Re z>1\) is a proved absolute domain, not a claimed optimal one.
No continuation of (2) to all \(\Re z>0\) is asserted.

For real \(\sigma>0\), \(W_\sigma(t)>0\) for every real \(t\),
and \(\mathcal H(s+it,s-it)>0\) for \(s>1/2\). Thus the
straight real-frequency integrand in (2) is nonnegative wherever
defined on such a real line. This does not establish its integrability
or its identification with \(\mathcal F\) outside the initial domain.

Choose a sufficiently small interval \(I=[\gamma-r,\gamma+r]\)
about the selected ordinate. Its retained-frequency integral
\[
 J_I(\sigma)=\frac1{2\pi\sigma}\int_I
 \frac{W_\sigma(t)\mathcal H(s_\sigma+it,s_\sigma-it)}
      {|\zeta(s_\sigma+it)|^2}\,dt                         \tag{4}
\]
is finite for \(\sigma>a_*\) sufficiently close to \(a_*\), and
\[
 \lim_{\sigma\downarrow a_*}
 (\sigma-a_*)^{2m-1}J_I(\sigma)=L_*>0,                     \tag{5}
\]
where, writing \(b_*=m!/\zeta^{(m)}(\rho_*)\),
\[
 L_*=
 \frac{2^{2m-1}}{2\pi a_*}
 W_{a_*}(\gamma)\mathcal H(\rho_*,\overline{\rho_*})|b_*|^2
 \int_{\mathbb R}(1+y^2)^{-m}\,dy.                         \tag{6}
\]
This is a positive local integral, not a singularity of the full transform.

For the defect test only, suppose a one-sided upper holds with
\(0<\epsilon<a_*\) and \(C\ge0\):
\(M_K\le CK^\epsilon\) for every integer \(K\ge2\).
Let
\[
 N_\epsilon(X)=CX^\epsilon-M_{\lfloor X\rfloor}\ge0,
 \quad \alpha_\epsilon=\inf\left\{\sigma\in\mathbb R:
    \int_2^\infty N_\epsilon(X)X^{-\sigma-1}dX<\infty\right\}.
                                                               \tag{7}
\]
Allow \(\alpha_\epsilon=-\infty\). We prove
\(\alpha_\epsilon\le1\), and the following exhaustive alternatives:

- If \(\alpha_\epsilon>a_*\), the desired point is outside the
  defining convergence range. For
  \(\epsilon<\sigma<\alpha_\epsilon\), the truncated real integral
  defining \(\mathcal F(\sigma)\) tends to \(-\infty\).
- If \(\alpha_\epsilon\le a_*\), define, for real \(\sigma>a_*\)
  sufficiently close to \(a_*\),
  \(R_I(\sigma)=\mathcal F(\sigma)-E(\sigma)-J_I(\sigma)\).
  Then
  \[
   \limsup_{\sigma\downarrow a_*}
   (\sigma-a_*)^{2m-1}R_I(\sigma)\le-L_*<0.                \tag{8}
  \]

On the initial real domain \(\sigma>1\), the same subtraction is
exactly the integral over \(\mathbb R\setminus I\) in (2), and is
nonnegative. That integral representation and sign have not been
transported to the interval in (8). Proving such transport, or a lower
bound excluding (8), is an unpaid premise. The dichotomy is therefore
not a contradiction, not a refutation of the upper, and not an RH result.

## Proof

### Coverage and purpose

The unchanged EXPLORE assessment2087, separately approved2088, covers
this exact complete-transform/nonnegative-defect test. C034s supplies
the arithmetic factors and actual kernel; no different positive kernel
is substituted. The previously inspected
[DLMF Section 2.5(i), equations 2.5.1-2.5.7](https://dlmf.nist.gov/2.5.i)
provides Mellin/Fubini and contour context, not a theorem identifying
this coprime diagonal transform. We apply standard absolute Fubini,
Fourier inversion, dominated holomorphic integration and dominated
convergence, checking their hypotheses below. The specialization is
needed for the maximum cutoff, its exceptional lower endpoint, and
the exact signed arithmetic weight. No general Mellin theorem is reproved.

For the proposed Landau step, the inspected primary statement is
J. Kaczorowski and J. Pintz, *Oscillatory properties of arithmetical
functions. I*, Acta Math. Hung. 48 (1986), 173-185,
[p. 173, named Landau theorem](https://personal.math.ubc.ca/~gerg/teaching/592-Fall2018/papers/1986.Kaczorowski_1.pdf).
Its sign-change conclusion requires a specified holomorphy half-plane,
no larger such half-plane, and regularity at the real boundary point.
Those hypotheses are not established here for the complete transform.
We do not apply it with a boundary inferred from one selected zero,
or import a stronger quantitative or generalized Tauberian theorem.
The inequalities below are direct nonnegative-integral arguments.

### 1. Absolute integration of both square cutoffs

Fourier inversion gives \(|k(r)|\le k_0\). Also \(|d(a,b)|\le c_2\),
so
\[
 |M_{\lfloor X\rfloor}|\le c_2k_0
 \left(\sum_{n\le X}n^{-1/2}\right)^2\le4c_2k_0X.
\]
Replacing each summand by its absolute value gives the same bound.
For \(\sigma=\Re z>1\) the resulting majorant integrates to
\(4c_2k_0\,2^{1-\sigma}/(\sigma-1)\).
The function is measurable and locally bounded, so absolute Fubini
applies. For each pair \((a,b)\), the two inclusive cutoffs hold
exactly when \(X\ge\max(a,b)\). Their contribution begins at
\(\max(2,a,b)\); integration gives (1). Isolated endpoint values
have measure zero, without half-weights or a floor approximation.

Put \(r_{ab}=\log(b/a)\). The identity
\(\max(a,b)=\sqrt{ab}\,e^{|r_{ab}|/2}\) gives
\[
 z\mathcal F(z)=c_2k_0(2^{-z}-1)
 +\sum_{a,b\ge1}d(a,b)(ab)^{-s_z}
                   k(r_{ab})e^{-z|r_{ab}|/2}.              \tag{9}
\]
Only \((a,b)=(1,1)\) has \(\max(a,b)<2\), and \(d(1,1)=c_2\).
This proves the correction and its sign. Its apparent singularity at
zero is removable by the exponential power series.

### 2. The diagonal Fourier representation

For \(\Re z>0\), direct integration on the two half-lines gives
\[
 \widehat{e^{-z|r|/2}}(t)
 =\frac1{z/2+it}+\frac1{z/2-it}
 =:P_z(t)=\frac{z}{z^2/4+t^2}.
\]
This is in \(L^1\): on compact \(z\)-sets in \(\Re z>0\) the
denominators have no real zeros, are uniformly bounded away from
zero on bounded \(t\)-sets, and the last expression is
\(O((1+|t|)^{-2})\) uniformly at infinity. The same statement holds
for any fixed number of \(z\)-derivatives. Convolving with
\(\lambda\in L^1\) therefore gives the \(L^1\) function (3),
locally holomorphic in \(z\) with values in \(L^1\).
Multiplying the two absolutely convergent inverse Fourier integrals
and applying Fubini identifies its inverse as \(k(r)e^{-z|r|/2}\).
This also identifies (3) with the Fourier transform in the conclusion.

For \(\Re z>1\), set \(s_0=(1+\Re z)/2>1\). The sum-integral
interchange in (9) has the finite absolute majorant
\[
 \frac{c_2}{2\pi}\zeta(s_0)^2\|W_z\|_1.
\]
The phase is \(e^{it\log(b/a)}=a^{-it}b^{it}\), giving exactly
\(D(s_z+it,s_z-it)\). This proves (2). On compact subsets of this
domain the same majorant with a smaller real-part margin also bounds
the necessary logarithmic derivatives, proving holomorphy.
No Perron contour, truncation-height limit or zero expansion is used.

For real \(\sigma>0\), \(P_\sigma(t)>0\) everywhere and
\(\lambda\ge0\) has positive mass. Hence (3) is strictly positive
everywhere. It is jointly continuous for real \(\sigma>0,t\in\mathbb R\),
by dominated convolution on compact parameter sets. Moreover
\(\int W_\sigma(t)dt=2\pi k_0\), since
\(\int P_\sigma(t)dt=2\pi\).

For \(u=s+it,v=s-it,s>1/2\), every Euler numerator of \(\mathcal H\)
is at least
\[
 1-\frac{2p^{1-s}}{p+1}
 >1-\frac{2\sqrt p}{p+1}>0,
\]
and its denominator is \(|1-p^{-s-it}|^2>0\). The factor minus
one is bounded, uniformly in \(t\) and \(s\ge s_0>1/2\), by a
constant times \(p^{-1-s_0}+p^{-2s_0}\), a summable sequence.
The product is strictly positive. On each compact real \(s\)-interval
inside \((1/2,\infty)\), it is bounded above and bounded away from
zero uniformly in \(t\): control the tail by the summable deviations,
and the finitely many earlier factors by the displayed strict lower
bound and \(|1-p^{-s-it}|\le1+p^{-s_0}\).
These statements do not assert anything about the size of reciprocal
zeta on such lines.

### 3. The retained-frequency blowup

Let \(a=a_*\) temporarily. Choose \(r_0>0\) so small that
\[
 \zeta(\rho_*+w)=w^m q(w),\qquad
 q(0)=1/b_*,\quad q(w)\ne0\quad(|w|\le r_0).
\]
Take \(0<r<r_0/2\), reducing \(r_0\) if needed to remain in the
domains of \(\mathcal H\) and \(\Re z>0\). For
\(h=\sigma-a>0\) sufficiently small and \(x=t-\gamma\in[-r,r]\),
the argument of \(q\) is \(h/2+ix\), inside that disk.
Consequently (4) is finite, and is exactly
\[
 J_I(a+h)=\frac1{2\pi(a+h)}\int_{-r}^r
 \frac{V(h,x)}{((h/2)^2+x^2)^m}\,dx,
\]
where
\[
 V(h,x)=\frac{W_{a+h}(\gamma+x)
 \mathcal H(\beta+h/2+i(\gamma+x),\beta+h/2-i(\gamma+x))}
 {|q(h/2+ix)|^2}.
\]
This function is continuous and bounded on a sufficiently small closed
rectangle \(h\ge0,|x|\le r\), with
\(V(0,0)=W_a(\gamma)\mathcal H(\rho_*,\overline{\rho_*})|b_*|^2>0\).
Substitute \(x=hy/2\) and multiply by \(h^{2m-1}\).
The resulting integrand, extended by zero outside \(|y|\le2r/h\),
is bounded by a constant times \((1+y^2)^{-m}\), which is
integrable for every integer \(m\ge1\). Dominated convergence
proves (5)-(6). In particular there is \(h_0>0\) such that
\(J_I(a+h)\ge(L_*/2)h^{1-2m}\) for \(0<h<h_0\).

As a normalization check using C034s's actual multiplier,
\[
 W_{a_*}(\gamma)=a_*B(\rho_*,\overline{\rho_*}).
\]
This follows immediately from (3) and \(a_*/2=\delta\).
The positive local term therefore uses the original cutoff multiplier.
We have not declared it an uncanceled contribution to \(\mathcal F\).

### 4. The nonnegative deficit and its two unresolved cases

The hypothetical integer upper implies
\(M_{\lfloor X\rfloor}\le CX^\epsilon\) for all \(X\ge2\).
Also \(N_\epsilon(X)\le CX^\epsilon+4c_2k_0X\), proving
\(\alpha_\epsilon\le1\). Nonnegativity makes its set of real
convergence parameters an upper interval. Its transform
\(G_\epsilon(z)\) is absolutely convergent and holomorphic on
\(\Re z>\alpha_\epsilon\); a smaller real-part margin absorbs
logarithmic derivatives. This includes the case
\(\alpha_\epsilon=-\infty\).

The pointwise bound \(|M_{\lfloor X\rfloor}|
\le N_\epsilon(X)+CX^\epsilon\) proves absolute convergence of
\(\mathcal F\) on \(\Re z>\max(\alpha_\epsilon,\epsilon)\), and
there we have the actual-integral identity
\[
 G_\epsilon(z)=\frac{C2^{\epsilon-z}}{z-\epsilon}-\mathcal F(z).
                                                               \tag{10}
\]
In particular, for real \(\sigma>\max(\alpha_\epsilon,\epsilon)\),
\[
 \mathcal F(\sigma)\le\frac{C2^{\epsilon-\sigma}}{\sigma-\epsilon}.
                                                               \tag{11}
\]
The upper alone gives no absolute bound on \(M\). Indeed, if
\(\epsilon<\sigma<\alpha_\epsilon\), the nonnegative truncated
integrals of \(N_\epsilon\) tend to infinity, whereas those of
\(CX^\epsilon\) have a finite limit. Subtracting shows the truncated
real integrals of \(M\) tend to \(-\infty\), proving the first case.

In the second case \(\alpha_\epsilon\le a_*\), (11) is uniformly
bounded above as \(\sigma\downarrow a_*\), because
\(a_*>\epsilon\). The entire correction \(E\) is bounded there.
Subtracting (5) from (11), then multiplying by
\((\sigma-a_*)^{2m-1}\), proves (8). Only an upper bound is used;
\(\mathcal F\) itself may tend to minus infinity.

For real \(\sigma>1\), (2) identifies the subtraction defining
\(R_I\) with its nonnegative omitted-frequency integral. To use that
sign near \(a_*\), one must prove equality with the straight-line
integral there, including convergence of the unbounded frequency tail
and any corrections from crossing other reciprocal-zeta poles.
Neither local holomorphy of \(\mathcal H\), positivity of \(W_\sigma\),
nor C034s's local principal part supplies this step. No rightmost-zero
or uniform reciprocal-zeta bound is available. Positivity in the
initial domain is not a sign theorem for an analytic continuation.
The primary Landau statement cited above also does not locate
\(\alpha_\epsilon\) or pay this complement.

Thus the bounded test stops with exactly the alternative of an
inaccessible convergence range or the unpaid negative complement (8).
The initial-domain identity and the local integral asymptotic are
preparatory results, not the requested complete-transform obstruction.
The full GC12 upper, GC13/GC18 remainder audit, high primitive control,
full energy bound and actual-Xi mixed transfer remain open. This work
has not had a separate critical audit and is not a complete candidate.

## Mathlib

Full matching coverage of this arithmetic diagonal transform, exact
maximum-cutoff correction and defect dichotomy has not been checked.
Availability is unknown. The supporting mathematics is standard
Fourier inversion, Fubini, dominated convergence, holomorphic parameter
integration and local finite-order factorization of a holomorphic
function. No Mathlib theorem is used to bypass the missing global
continuation or complement estimate. No numerical certificate is used.
