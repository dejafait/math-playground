# Corollary 466f: the two-term Möbius inverse cannot globally dominate the actual density

## Hypotheses

Use C466a's normalization
\[
 c_0=\xi(1/2)>0,\qquad h(s)=\xi(1/2+\sqrt{s})/c_0,
 \qquad p=\theta_1\ge0,\quad \int_0^\infty p(x)\,dx=1,
 \quad \mathcal Lp(s)=h(s)^{-1}\quad(\Re s>0).
\]
The density and its cited external qualifications are exactly those of
C466a; no new density theorem is assumed here. In particular, unit mass
belongs to p, not to p/c_0. Use the principal square root on \(\Re s>0\).
For \(q=\sqrt{s}\), define the explicit finite-head transform
\[
 M_2(s)=1-2^{-1/2-q},\qquad
 G_2(s)=\frac{2c_0\pi^{q/2+1/4}M_2(s)}
                   {(s-1/4)\Gamma(q/2+1/4)}.                 \tag{1}
\]
This retains the entire reciprocal prefactor in C466a's displayed
factorization. It is not assumed positive or of finite mass.

Known analytic inputs are the sectorial log-Gamma expansion with
remainder, [NIST DLMF 5.11.1](https://dlmf.nist.gov/5.11#E1) and
[5.11(ii)](https://dlmf.nist.gov/5.11#ii), and Cauchy's residue theorem.
The expansion is used only in a fixed closed subsector of
\(|\arg w|<\pi\), with \(|w|\to\infty\). Standard Fourier/Bromwich
inversion conventions are [DLMF 1.14.3](https://dlmf.nist.gov/1.14#E3)
and [1.14.20](https://dlmf.nist.gov/1.14#E20); all convergence and
one-sided inversion properties needed here are proved below instead
of presupposing that (1) is a density transform.

The ordinary Möbius formula
[DLMF 27.4.5](https://dlmf.nist.gov/27.4#E5) explains (1) only on
\(\Re(1/2+\sqrt{s})>1\), including the line \(\Re s=1\).
No continuation or termwise inversion of its infinite series is used.
This is a specialization of standard transform tools, not a new general
inversion theorem or an originality claim. Reproduction is needed to
check the complete normalization, composed gamma estimate and pole
before testing a global approximation premise.

## Conclusion

The absolutely convergent Bromwich integral
\[
 g_2(x)=\frac{1}{2\pi i}\int_{1-i\infty}^{1+i\infty}
                       e^{sx}G_2(s)\,ds                       \tag{2}
\]
defines a real \(C^\infty\) function on \(\mathbb R\), vanishing on
\(( -\infty,0]\), whose Laplace transform is G_2 on \(\Re s>1/4\).
For a finite constant K, independent of \(x\ge0\),
\[
 g_2(x)=c_0e^{x/4}+E(x),\qquad |E(x)|\le K e^{x/8}.        \tag{3}
\]
Thus g_2 is eventually strictly positive, and the exact remainder
\(r_2=p-g_2\) cannot satisfy
\[
                  |r_2(x)|=o(|g_2(x)|)\quad(x\to\infty).   \tag{4}
\]
The result stops only global relative domination by this fixed head.
It does not rule out compact-window joint cancellation, derivative
bounds, or a different decomposition. It gives no sign for C466b(7),
no contact exclusion, no global PF property and no RH conclusion.

## Proof

### Uniform sectorial bounds and the only pole

Write \(q=u+iv\) and \(w=q/2+1/4\). For \(\Re s\ge1/8\),
\[
 |\arg q|<\pi/4,\quad u\ge |q|/\sqrt2,\quad
 |\arg w|\le\pi/4,\quad |w|\asymp|q|\quad(|s|\to\infty).
\]
The comparability constants are uniform in this half-plane. The
principal log-Gamma branch is analytic for \(\Re w>0\). DLMF's
sectorial expansion, including its remainder, gives uniformly
\[
 \log\Gamma(w)=(w-1/2)\Log w-w+\tfrac12\log(2\pi)
                      +O(|w|^{-1}),
\]
and hence the lower-modulus estimate
\[
 \log|\Gamma(w)|=(u/2-1/4)\log|w|
       -(v/2)\arg w-u/2-1/4+\tfrac12\log(2\pi)
       +O(|q|^{-1}).                                      \tag{5}
\]
In particular this controls the reciprocal gamma; it does not invert
an upper bound for gamma. Since \(|M_2(s)|\le1+2^{-1/2-u}\le2\),
\(|s-1/4|\asymp|s|\) for large \(|s|\), and
\(\log|w|=\log|q|-\log2+O(|q|^{-1})\), (5) implies
\[
 |G_2(s)|\le
 \exp\{-\tfrac{u}{2}\log|q|+C_1|q|+C_2\log|q|+C_3\}.
\]
All constants can depend on c_0 but not on s in the specified region.
Absorbing the positive lower-order terms into the negative leading
term, there exist \(c,C,R>0\) such that
\[
 |G_2(s)|\le C\exp[-c\sqrt{|s|}\log(2+|s|)]
       \quad(\Re s\ge1/8,\ |s|\ge R).                    \tag{6}
\]
This follows from \(u\ge |q|/\sqrt2\) and
\(\log|q|=\frac12\log|s|\); it is a large-modulus bound,
not a bound through the pole. On \(\Re s\ge1\) it holds for all
s after increasing C, by continuity on the remaining compact set.

The principal square root is analytic in \(\Re s>0\),
\(1/\Gamma(w)\) is analytic there, and the other numerator factors
are analytic. Thus the only possible singularity of G_2 in this
half-plane is s=1/4. At that point q=1/2, w=1/2,
\(\pi^{1/2}/\Gamma(1/2)=1\), and \(M_2=1/2\). It follows that
\[
                    \operatorname{Res}_{s=1/4}G_2(s)=c_0. \tag{7}
\]
This pole is genuine. No branch cut, gamma pole or zeta zero is
crossed in the strip used below; zeta is absent from (1).

### Absolute inversion, reality and support

For each fixed \(\sigma\ge1/8\), \(\sigma\ne1/4\), and integer
\(k\ge0\), (6) and continuity on the finite part of that line give
\[
 \int_{\mathbb R}(1+|t|)^k|G_2(\sigma+it)|\,dt<\infty.    \tag{8}
\]
The tail is bounded by a polynomial times
\(\exp[-c\sqrt{|t|}\log(2+|t|)]\), which is integrable.
Equation (8) at \(\sigma=1\) proves absolute convergence of (2)
and permits every x-derivative under the integral, locally uniformly
in real x. Thus g_2 is smooth. Conjugate symmetry
\(G_2(\overline{s})=\overline{G_2(s)}\) makes it real.

For any fixed \(\sigma>1\), close the strip between 1 and \(\sigma\)
at heights \(\pm T\). There are no poles. For a fixed real x, the
horizontal integrals tend to zero by (6), since their length is
\(\sigma-1\) and \(e^{x\Re s}\) is bounded on this fixed strip.
Consequently (2) equals the integral on \(\Re s=\sigma\).
The global version of (6) on \(\Re s\ge1\) gives a uniform constant
\[
 \int_{\mathbb R}|G_2(\sigma+it)|\,dt\le K_1\quad(\sigma\ge1),
                                                               \tag{9}
\]
because \(|\sigma+it|\ge|t|\) and the positive function
\(y\mapsto\sqrt y\log(2+y)\) is increasing. Hence
\(|g_2(x)|\le K_1e^{\sigma x}/(2\pi)\). Letting
\(\sigma\to\infty\) proves g_2(x)=0 for x<0; continuity gives
g_2(0)=0. This also makes every derivative at zero vanish.

### Contour displacement and full residue

Now close the finite rectangle between \(a=1/8\) and 1.
The horizontal integrals of \(e^{sx}G_2(s)\) are bounded, for fixed
real x, by
\[
 C(1-a)\max(e^{ax},e^x)
              \exp[-c\sqrt T\log(2+T)]\longrightarrow0.
\]
The sole enclosed singularity is (7). The residue theorem and (8)
therefore give the exact equality
\[
 g_2(x)=c_0e^{x/4}
       +\frac{1}{2\pi}\int_{\mathbb R}
                    e^{(a+it)x}G_2(a+it)\,dt.             \tag{10}
\]
Take \(K=(2\pi)^{-1}\int|G_2(a+it)|\,dt<\infty\) to obtain (3).
The contour equality holds for every fixed real x; the bound for
x>=0 uses no unproved decay estimate for p. In particular,
\(g_2(x)/(c_0e^{x/4})=1+O(e^{-x/8})\), and g_2 is eventually
nonzero and positive. This resolves the possible denominator zeros
in (4).

For completeness, (2) is a genuine one-sided inverse. For \(\Re z>1\),
(8) and Fubini give
\[
 \int_0^\infty e^{-zx}g_2(x)\,dx
   =\frac{1}{2\pi i}\int_{1-i\infty}^{1+i\infty}
                              \frac{G_2(s)}{z-s}\,ds.     \tag{11}
\]
Close this last contour to the right at \(\Re s=b>\Re z+1\).
At fixed b the horizontal integrals vanish by (6). The residue of
\(G_2(s)/(z-s)\) at z is \(-G_2(z)\); the clockwise rectangle
therefore gives left upward integral minus right upward integral
equal to \(2\pi iG_2(z)\). By (9), the absolute right integral is
at most \(K_1/(b-\Re z)\), which tends to zero as b tends to infinity.
Thus (11) equals G_2(z). By (3) both the Laplace integral and G_2
are holomorphic on \(\Re z>1/4\), so the identity theorem extends
this equality to that half-plane. This proves the asserted transform
identity without imposing unverified inversion hypotheses.

### Finite-mass contradiction and scope

For all sufficiently large x, (3) implies
\(g_2(x)\ge(c_0/2)e^{x/4}>0\). If (4) held, increasing the
threshold would also give \(|p(x)-g_2(x)|\le g_2(x)/2\). Hence
\[
 p(x)\ge\tfrac12g_2(x)\ge\tfrac{c_0}{4}e^{x/4}
\]
on the whole final half-line, contradicting \(\int p=1\).
The required relative threshold is eventual error at most 1/2 of
the head; the proposed little-o estimate would imply it, and fails.
No pointwise rate for the integrable density has been inferred.

The full reciprocal transform h^{-1} is holomorphic at s=1/4 by
C466a's probability Laplace identity. The usual zeta pole, with
residue one ([DLMF 25.2(i)](https://dlmf.nist.gov/25.2#i)), explains
the cancellation in its completed factorization. For the exact
remainder, \(\mathcal Lr_2=h^{-1}-G_2\) on \(\Re s>1/4\), by
absolute convergence of both integrals there. This difference has
meromorphic continuation near 1/4 with residue -c_0. This is a
statement about the explicit difference, not convergence of the
infinite Möbius tail at that point. The failure of (4) demands global
cancellation and leaves compact estimates logically open. All-degree
contact forcing, simultaneous contacts, propagation and the
L030-L032/C032a assembly remain unresolved.

### Critical audit — 14 November 2026, step906

The proof was checked under unchanged assessment904; no repair to its
conclusion or analytic argument was needed. These are the load-bearing
checks, rather than additional hypotheses or a new theorem.

In (5), Re(w)-1/2=u/2-1/4 and Im(w)=v/2, giving exactly the
displayed real log-Gamma formula. The absolute remainder is uniform
since |arg(w)|<=pi/4. The term (v/2)arg(w) has absolute value at most
pi|q|/8, while u>=|q|/sqrt(2). Thus -(u/2)log|q| dominates all
O(|q|)+O(log|q|) terms uniformly, including when Re(s) tends to
infinity. This verifies (6) on the whole large-modulus half-plane,
not only on the contours. The compact-set extension for (9) stays in
Re(s)>=1 and avoids the pole. Its integrable majorant is
C exp[-c sqrt(|t|)log(2+|t|)], independent of sigma>=1.
The rightward support argument therefore uses a uniform bound.
All polynomial frequency weights are integrable as claimed;
smoothness and conjugate symmetry require no assumption on p's tail.

At s=1/4, q=1/2, w=1/2 and M_2=1/2. The full numerator divided
by Gamma is c_0, so (7) has neither a square-root Jacobian nor an
extra factor of two: the denominator is already s-1/4. In the
leftward displacement, the upward right edge minus the upward left
edge encloses the pole positively, giving the positive term in (10).
Bound (6) controls both complete horizontal edges. Absolute
integrability on Re(s)=1/8 makes K finite and gives the error estimate
uniformly for x>=0 after the fixed-x contour equality is established.

For (11), absolute Fubini follows from the finite bound
integral_R |G_2(1+it)| dt / (Re(z)-1).
The right closure is clockwise and its residue is -G_2(z), so the
two minus signs give the asserted transform. First let the horizontal
heights tend to infinity at fixed b; only then let b tend to infinity,
using K_1/(b-Re(z)). No unproved joint limit is required. Estimate (3)
supplies local domination of the Laplace integral and its z-derivatives
on Re(z)>1/4, paying the holomorphy needed for the identity theorem.
Finally, g_2>=(c_0/2)exp(x/4) and p>=g_2/2 on a final half-line
contradict finite mass. Even an almost-everywhere version of that
relative bound contradicts mass; no pointwise decay inference from
integrability is used.

This audit verifies the obstruction relative to C466a's cited external
density assertion; it does not replay that source or its finite-zero
certificates. C466a remains the sole direct local input. The conclusion
is a checked specialization of known analytic tools, not a new general
transform result or an actual contact-sign estimate.

## Mathlib

Full matching coverage of this composed finite-head inverse and its
relative-error obstruction is unchecked. No absence claim is made.
The proof imports the cited sectorial expansion and standard residue
theorem with the detailed applicability arguments above; no Lean
verification or numerical certificate is claimed. C466a's qualified
external density assertion remains an input rather than a new proof
of that assertion.
