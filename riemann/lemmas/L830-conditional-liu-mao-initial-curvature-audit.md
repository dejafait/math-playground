# Lemma 830: conditional Liu–Mao initial curvature interface

## Hypotheses

Use Yanxin Liu and Jianxi Mao, *Infinite log-concavity of the Taylor
coefficients of the Riemann xi-function*,
[arXiv:2610.04972v1](https://arxiv.org/html/2610.04972v1), 4 October 2026,
Lemma2.3 and equations (2.10)–(2.13) for the moment interpolation

\[
 \omega(t)=\sum_{j\ge1}(2\pi^2j^4t^2-3\pi j^2t)e^{-\pi j^2t},\quad
 H(z)=2^{1-2z}\int_0^\infty u^{2z}e^{u/4}\omega(e^u)\,du,
 \quad \Lambda(z)=\frac{H(z)}{\Gamma(2z+1)}.                 \tag{1}
\]

The integral uses the real logarithm of u>0. The imported moment
representation says that H and Lambda are holomorphic for Re z>-1/2,
are positive on the real part of that domain, and
Lambda(k)=lambda_k=xi^(2k)(1/2)/(2k)! for positive integers k.
These are ordinary coefficients, not k!lambda_k. All integer arguments
used below exceed zero. No new moment representation is claimed.

**Unpaid sector assumptions.** On
S={z: |arg z|<=pi/4, |z|>=4000}, set
w=W_0(2z/pi), a=Re w, T=|z|/a, and

\[
 H_*(z)=4\pi^2e^{7w/4}\sqrt{\frac{2w}{1+w}}
       \exp\left(2z\left(\operatorname{Log}(w/2)-1/w\right)\right).
                                                               \tag{2}
\]

W_0 is the principal Lambert-W branch, satisfying we^w=2z/pi;
the square root and the displayed elementary logarithms are principal.
Assume precisely the sector conclusions of the source's Lemma3.1
(3.2) and Lemma3.2 (3.8):

\[
 a\ge6,\qquad T\ge(\pi/2)e^6>630,\qquad
 \left|H/H_*-1\right|\le30/T,\qquad
 \left|\operatorname{Log}(H/H_*)\right|\le32/T<51/1000.       \tag{3}
\]

Here the last logarithm is Log(1+v), v=H/H_*-1, |v|<1; the
conclusion includes nonvanishing of H on S and holomorphy of this
logarithm in the sector interior. These assumptions reproduce the
complete relative-error/nonvanishing/logarithm interface. They are
not asserted to have been independently proved for (1) in this audit.

Fix any real n>=12000. Write
D={|z-n|<=n/2}, U={|z-n|<2n/3}, and
Delta^2 f(z)=f(z-1)-2f(z)+f(z+1).

## Conclusion

There is a holomorphic logarithm ell of Lambda on U agreeing with
the real logarithm on U intersect R. The function g_0=-Delta^2 ell
is holomorphic on a neighborhood of D, real on [n/2,3n/2], and
g_0(k)=log(lambda_k^2/(lambda_(k-1)lambda_(k+1))) for integer k in D.
For every z in the **entire closed disk** D,

\[
 \left|g_0(z)-\frac{2W_0(2z/\pi)}{z(1+W_0(2z/\pi))}\right|
 <\frac{18}{n^2}<\frac{20}{n^2}.                            \tag{4}
\]

This is a conditional reproduction audit of Liu–Mao v1 Lemma3.3,
printed pp.31–37, specifically (3.55)–(3.68) and their error assembly;
[versioned PDF](https://arxiv.org/pdf/2610.04972v1).
The source already gives the intermediate constant 18. Neither an
improved source result nor unconditional actual-Xi curvature is claimed.
The additional real-part bounds, iteration lemma, finite certificate,
all-iterate theorem and any mixed-minor sign are outside this conclusion.

## Proof

The prior SPECIALIZE assessment is
`drafts/literature/2026-11-05-liu-mao-initial-curvature-conditional-audit.md`.
This reproduction checks complex domains, branches, differentiations and
effective constants. We import the analytic-logarithm theorem for a
nonvanishing holomorphic function on a simply connected domain, the
identity theorem, Cauchy's derivative estimate and Taylor's integral
remainder. We also import Gamma's functional equation and its
holomorphy, nonvanishing and real positivity on the right half-plane.
These standard named theorems are not reproved here. No zero statement
about Xi, or positivity criterion equivalent to RH, is an input.

### Domains and branches

For z in U,

\[
 |z|>n/3\ge4000,\qquad
 \Re z-|\Im z|\ge n-\sqrt2|z-n|
             >n(1-2\sqrt2/3)>0.
\]

Thus U lies in the interior of S, including when n=12000.
Assumption (3) gives nonvanishing of H. Gamma(2z+1) is also
holomorphic and nonzero there. Their logarithms ell_H and ell_Gamma
exist on the disk U and can be fixed to their real values at n.
Positivity on the connected real interval (n/3,5n/3) makes them real
logarithms throughout that interval. Set ell=ell_H-ell_Gamma.

The larger shifted domain V={|z-n|<2n/3-1} contains D strictly,
since its radius exceeds n/2 by n/6-1>=1999. For z in V,
z-1,z,z+1 all belong to U. Hence g_0 is holomorphic on V,
and its asserted real and integer identities follow from (1).

On U, Re w>=6 implies

\[
 |1+w|\ge7,\qquad |w/(1+w)|<1,\qquad
 \Re\frac{w}{1+w}=\frac{|w|^2+\Re w}{|1+w|^2}>0.             \tag{5}
\]

In particular w/2 and 2w/(1+w) stay in the right half-plane.
Their principal logarithms and the square root in (2) are compatible
and holomorphic. Define

\[
 p=2z(\operatorname{Log}(w/2)-1/w),\quad
 h_0=\log(4\pi^2)+7w/4+\tfrac12\operatorname{Log}(2w/(1+w)),
 \quad \varepsilon=\operatorname{Log}(H/H_*).
\]

Then H_*=exp(p+h_0). By (3), epsilon is holomorphic on U with
|epsilon|<51/1000. On its real interval H and H_* are positive and
all three logarithms agree with real ones. The identity theorem gives
ell_H=p+h_0+epsilon on U. No principal-logarithm product identity
is being assumed for arbitrary complex values of H.

Differentiating we^w=2z/pi, with z,w,1+w all nonzero, gives

\[
 w'=\frac{w}{z(1+w)},\qquad
 p'=2\operatorname{Log}(w/2),\qquad
 p''=\frac{2}{z(1+w)},\qquad Q:=2/z-p''=\frac{2w}{z(1+w)}.
\]

Consequently, on D,

\[
 g_0-Q=-(\Delta^2p-p'')-\Delta^2h_0-\Delta^2\varepsilon
              +(\Delta^2\ell_{\Gamma}-2/z).                \tag{6}
\]

Taylor's integral remainder along the real segment from z-1 to z+1
gives, for every function f holomorphic on U,

\[
 \Delta^2f(z)=\int_{-1}^{1}(1-|s|)f''(z+s)\,ds,
 \qquad \int_{-1}^{1}(1-|s|)\,ds=1.                         \tag{7}
\]

### Action error: the first budget

Differentiating the displayed expression for p'' gives

\[
 p'''=-\frac2{z^2}\left(\frac1{1+w}+\frac{w}{(1+w)^3}\right),
 \quad
 p^{(4)}=\frac1{z^3}\left(\frac4{1+w}+\frac{4w}{(1+w)^3}
                       +\frac{2w^2(w+4)}{(1+w)^5}\right).
\]

For example the final term follows by combining
2w/(1+w)^3-2w(1-2w)/(1+w)^5=2w^2(w+4)/(1+w)^5.
Using (5) and |w+4|<=|w|+4 bounds its full bracket by
4/7+4/49+2/49+8/343=246/343<1. Taylor's fourth-derivative
remainder at z+1 and z-1 cancels the first and third derivatives.
Since |z+s|>=n/2-1 for |s|<=1, it yields

\[
 |\Delta^2p-p''|\le\frac1{12(n/2-1)^3}
       \le\frac9{4n^3}<\frac1{n^2}.                         \tag{8}
\]

The factor 1/12 is 2*(1/6)*integral_0^1(1-s)^3 ds.
The middle inequality uses n/2-1>=n/3, valid for n>=6.

### Prefactor error: the second budget

Direct chain-rule differentiation gives

\[
 h_0'=\frac1z\left(\frac{7w}{4(1+w)}+\frac1{2(1+w)^2}\right),
\]
\[
 h_0''=\frac1{z^2}\left(-\frac{7w}{4(1+w)}
  -\frac1{2(1+w)^2}+\frac{7w}{4(1+w)^3}-\frac{w}{(1+w)^4}\right).
\]

By (5), the absolute value of its bracket is at most
7/4+1/98+1/28+1/343=617/343<9/5. Applying (7),

\[
 |\Delta^2h_0|<\frac{9/5}{(n/2-1)^2}<\frac8{n^2}.           \tag{9}
\]

For an exact check of the last strict inequality, n>=12000 implies
n/2-1>49n/100, and (9/5)*(100/49)^2=18000/2401<8.

### Logarithmic remainder: the third budget

For every |z_0-n|<=n/2+1, the complete closed radius-n/7 disk about
z_0 lies strictly inside U. Its margin is

\[
 2n/3-(n/2+1+n/7)=n/42-1\ge1993/7>0.                       \tag{10}
\]

Thus Cauchy's estimate applies with the uniform bound 51/1000
on the full circle, not merely on its real diameter:

\[
 |\varepsilon''(z_0)|\le\frac{2!(51/1000)}{(n/7)^2}
              =\frac{2499}{500n^2}<\frac5{n^2}.             \tag{11}
\]

Every z+s in (7) lies among those centers. Integrating gives
|Delta^2 epsilon|<=2499/(500n^2)<5/n^2. The decimal 4.998
in the source is exactly 2499/500; there is no rounding loss.

### Gamma error: the fourth budget

The Gamma functional equation gives, on V,

\[
 \frac{\Gamma(2z+3)\Gamma(2z-1)}{\Gamma(2z+1)^2}
 =\frac{(1+1/z)(1+1/(2z))}{1-1/(2z)}.
\]

Here Re z>n/3+1>1, so the three right-hand factors lie in
the open disk of radius 1 about 1 and have principal logarithms.
On the real interval in V the Gamma quotient and all factors are
positive. Equality of their real logarithms there, followed by the
identity theorem on V, proves the compatible branch identity

\[
 \Delta^2\ell_{\Gamma}
 =\operatorname{Log}(1+1/z)+\operatorname{Log}(1+1/(2z))
                         -\operatorname{Log}(1-1/(2z)).     \tag{12}
\]

This rules out an unaccounted multiple of 2pi i. On D, |z|>=n/2,
so all logarithmic series converge absolutely. Subtracting 2/z leaves

\[
 \sum_{j\ge2}\frac{(-1)^{j+1}}{jz^j}
       +2\sum_{j\ge1}\frac1{(2j+1)(2z)^{2j+1}}.
\]

The first sum has absolute value at most
2/[n^2(1-2/n)]<3/n^2 (n>6). The second is at most
2/[3n^3(1-1/n^2)]<1/n^2 (already for n>=2).
Thus |Delta^2 ell_Gamma-2/z|<4/n^2. No asymptotic expansion
of Gamma and no interchange with an infinite contour integral is used.

Combining these four bounds in (6) proves (4), uniformly on the
closed disk and for real n, with the required threshold unchanged.
No stronger sector hypothesis was added. This establishes only the
conditional interface. The long saddle proof supplying (3) and the
implication from curvature to exceptional mixed-minor signs remain
independent obligations. L772's generic obstruction is unaffected;
L790's derivative estimate is a comparison, not an input to this proof.

## Mathlib

Full matching coverage is not checked. The availability of supporting
analytic-logarithm, Cauchy, Gamma and Lambert-W results in Mathlib has
not been checked for this audit; no absence claim is made.
[Mathlib documentation](https://leanprover-community.github.io/mathlib4_docs/).
