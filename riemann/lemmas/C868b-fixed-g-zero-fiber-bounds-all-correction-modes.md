# Corollary 868b: one actual G-zero fiber bounds every nonzero correction mode

## Hypotheses

Retain exactly L868's actual coefficient and full admissible class:

\[
 F(z_1,z_2)=-C G(z_1)G(z_2)(z_1-z_2)^2/(z_1^2z_2^2),
 \qquad z_j=R e^{x_j+i y_j},\quad C,R>0,
\]

where G is L847's actual entire function. The functions q,r,h are
real C1 on R2 times T2, periodic with period 2pi in each angle, and

\[
 h\geq0,\qquad q^2+r^2\leq |F|^2,\qquad
 r_{x_j}=q_{y_j},\qquad (q+h)_{x_j}=-r_{y_j}\quad(j=1,2).
 \tag{1}
\]

Use C868a's normalized Fourier coefficients
\(\widehat f_n(x)=(2\pi)^{-2}\int_{[0,2\pi]^2}f(x,y)e^{-i n\cdot y}\,dy\).
In particular S=q+h has constant mean K; M is the angular mean
of F; and C868a gives constants

\[
 \widehat q_0(s,s)=A,\qquad \widehat h_0(s,s)=H=K-A\geq0.
 \tag{2}
\]

There is no growth, bandwidth, absolute Fourier summability,
holomorphic coefficient, graph-existence or RH assumption. All F
zeros and all graph-Jacobian zeros, and L868's fixed orientation,
remain in force. No multiplicity assumption is made on G's zeros.

## Conclusion

Choose one nonzero zero a of actual G by the Hardy input below,
and set ell=log(|a|/R), phi=arg(a) modulo 2pi. Then

\[
 \widehat q_0(\ell,s)=A,\qquad
 \widehat h_0(\ell,s)=H\quad(s\in\mathbb R).
 \tag{3}
\]

Consequently every nonzero angular correction mode satisfies

\[
             |\widehat h_n(x)|\leq H
       \quad(n\in\mathbb Z^2\setminus\{0\},\ x\in\mathbb R^2).
 \tag{4}
\]

In particular (4) includes the previously exceptional modes
n=(k,-k) at every radial difference, not only at equal radii.
Their finite Toeplitz tests have the following stronger necessary
positivity. For fixed x put

\[
 a_0(x)=H,\qquad a_k(x)=\widehat h_{(k,-k)}(x)\ (k\ne0).
\]

For every N>=0 and c_0,...,c_N in C,

\[
       \sum_{j,l=0}^{N}c_j\overline{c_l}\,a_{j-l}(x)\geq0.
 \tag{5}
\]

If H=0, h is independent of both angles everywhere:

\[
                   h(x,y)=\widehat h_0(x).                \tag{6}
\]

Its radial dependence is not removed. Nor does (4) bound the zero
mode of h away from x1=ell or equal radii. The desired period bound
K=A+H>=-|M| is still unresolved. These are additional necessary
conditions on certificates, not a full-class no-gain theorem, a
strict-gain certificate or an RH conclusion. The independent
conceptual audit of 6 November 2026 below accepts this exact
restriction. The prior bounded EXPLORE comparison does not certify
originality.

## Proof

### Reused sources and actual-zero applicability

The prior assessment is
`drafts/literature/2026-11-06-one-sided-g-zero-fiber-period-scope.md`,
whose covered target is the fixed-fiber period test in the unchanged
class (1). Reuse audited L868 and C868a; no new PDE uniqueness,
global smoothing or relative-cohomology theorem is invoked.

Import Hardy's theorem from E. C. Titchmarsh, *The Theory of the
Riemann Zeta-function*, second edition revised by D. R. Heath-Brown,
Oxford (1986), [Section 10.2, pp256-258](https://sites.math.rutgers.edu/~zeilberg/EM18/TitchmarshZeta.pdf#page=133):
there are infinitely many zeta zeros on Re(s)=1/2. Choose one with
nonzero ordinate gamma. Such a choice is possible without a specified
ordinate or simplicity assumption. L018's zero correspondence gives
xi(1/2+i gamma)=0. L847's formula
G(z)=xi(1/2+sqrt(z)/2)/8 therefore gives

\[
                         a=-4\gamma^2\ne0,\qquad G(a)=0.
 \tag{7}
\]

The two square roots give 1/2+/-i gamma; L018's reflection identity
makes both xi values zero. Thus no branch or RH assumption is hidden
in (7). Hardy's theorem is imported, not reproved. This is its
necessary coordinate specialization, not a new zero certificate.

For compact angular reconstruction reuse Loukas Grafakos,
*Classical Fourier Analysis*, third edition (2014),
[Definition 3.1.8, Remark 3.1.9, Proposition 3.1.10 and Corollary
3.2.2, pp180-183](https://www.math.stonybrook.edu/~bishop/classes/math638.F20/Grafakos_Classical_Fourier_Analysis.pdf),
with [corrected Theorem 1.2.19(2) and proof, pp27-29](https://grafakos.missouri.edu/Books_Correction_Pages/CFA-Page27-29.pdf).
These already inspected inputs give uniform product Fejer convergence
on each continuous angular slice, after the normalization y/(2pi).
C1 in (1) supplies that continuity. C868a already establishes the
coefficient profiles by compact differentiation and periodic
integration by parts; those arguments are not reproved here.

Specifically, for n!=0 C868a gives a C3 function B_n with

\[
 \widehat q_n(x)=B_n''(n\cdot x),\qquad
 \widehat h_n(x)=B_n(n\cdot x)-B_n''(n\cdot x).
 \tag{8}
\]

No unweighted Fourier series or feasible finite approximation is
needed below. Each reconstruction is at fixed finite radial values.

### The fiber fixes a radial line of angular means

At x1=ell and y1=phi, z1=a. For every real s=x2 and every y2,
F=0 by (7), and (1) forces q=r=0. This is one fixed angular value
y1=phi, not an entire angular torus.

Let q_N(x,y) be the product Fejer polynomial of q(x,.) and put
w_N(k)=max(1-|k|/(N+1),0). Uniform convergence on T2, followed by
restriction to y1=phi and normalized integration in y2, gives

\[
 D_N(s):=\frac1{2\pi}\int_0^{2\pi}
                 q_N((\ell,s),(\phi,v))\,dv\longrightarrow0
       \quad\text{for each fixed }s.                       \tag{9}
\]

Indeed the absolute value in (9) is at most the uniform error of
q_N from q on this angular slice. Integration of the finite sum
selects n2=0, so exactly

\[
 D_N(s)=\widehat q_0(\ell,s)+
   \sum_{0<|k|\leq N}w_N(k)e^{ik\phi}B_{(k,0)}''(k\ell).
 \tag{10}
\]

There is one Fejer weight, since w_N(0)=1. By (8) the whole
nonzero finite sum is independent of s. Subtract (10) at s=ell
before taking the limit. Equation (9) at the two fixed radial
points yields

\[
 \widehat q_0(\ell,s)=\widehat q_0(\ell,\ell)=A.
\]

Since the mean of S is K, its difference from this mean is
\(\widehat h_0(\ell,s)=K-A=H\). This proves (3), including
every finite s. It takes neither a noncompact limit nor a trace
of a merely formal infinite series.

### Every nonzero profile can be sampled where the mean is H

For any n and any s, nonnegativity of h and (3) imply

\[
          |\widehat h_n(\ell,s)|\leq\widehat h_0(\ell,s)=H.
 \tag{11}
\]

Fix arbitrary x and n with n2!=0. The finite real number
s=(n dot x-n1 ell)/n2 satisfies n dot (ell,s)=n dot x.
Thus (8) equates hhat_n at these two radial points. Apply (11)
to obtain (4) for n2!=0. For n2=0 and n!=0, n1+n2=n1!=0;
C868a's already proved nonresonant bound gives (4). This covers
all nonzero n without division by F, J or a vanishing frequency.

For (5), set d=x1-x2 and x*=(ell,ell-d). For every k!=0,
(k,-k) dot x* = k d = (k,-k) dot x. Equation (8) equates the
corresponding coefficients at x and x*, while (3) gives the
zero coefficient at x* equal to H. Therefore for every integer k,

\[
 a_k(x)=(2\pi)^{-2}\int h(x^*,y)e^{-ik(y_1-y_2)}\,dy.
\]

Only a finite sum is used in the identity

\[
 \sum_{j,l=0}^{N}c_j\overline{c_l}\,a_{j-l}(x)
  =(2\pi)^{-2}\int h(x^*,y)
       \left|\sum_{j=0}^{N}c_j e^{-ij(y_1-y_2)}\right|^2dy
  \geq0.
\]

This proves (5). In particular, the diagonal in this Toeplitz test
is H, not the potentially different mean hhat_0(x).

When H=0, (4) makes every nonzero Fourier coefficient of h(x,.)
zero at each fixed x. Every product Fejer polynomial of that slice
is then the constant hhat_0(x). Uniform convergence proves (6).
No infinite Fourier differentiation is used.

### Exact downstream restriction and unresolved threshold

For each k!=0, an opposite-index correction profile
\(t\mapsto B_{(k,-k)}(t)-B_{(k,-k)}''(t)\)
must now be bounded by the same finite H on all R; (5) adds
simultaneous finite positivity constraints on these profiles.
A proposed profile unbounded at either end, or violating one of
these finite tests, cannot occur in an admissible certificate.
An H=0 certificate cannot use any angularly varying h at all.
These are explicit new restrictions on the modes left exceptional
by C868a, useful before attempting L868's strict-period construction.

They do not control the remaining zero mode globally or the
constant A at the threshold -|M|-H. L868's existing global bump
has H=K=0, is angularly independent, and has nonconstant radial h;
it therefore also shows why (6) does not permit the
radial-independent-h theorem to be invoked. No part of that example
is a strict-gain construction, and it is not reproved here.

The period remains exactly -(2pi)^2 K, with strict gain precisely
when K<-|M| by L868. Neither inequality at that threshold is
proved here. All original domination and closure equations away
from the chosen fiber remain necessary; Fourier tests are not
claimed sufficient. In particular, no graph realization, actual-Xi
higher sign or all-degree mixed positivity follows.

### Independent conceptual audit, 6 November 2026

The invocation-start EXPLORE assessment was
`drafts/literature/2026-11-06-fixed-g-zero-fiber-bound-audit.md`,
separately approved before this audit. Reuse the inspected Hardy
and Grafakos inputs cited above, L018's zero correspondence and
reflection, L847's actual G formula, and audited L868/C868a. This
checks the submitted restriction; it imports no further period,
PDE or approximation theorem and makes no originality claim.

Hardy's infinitely many critical-line zeros include one with a
nonzero real ordinate gamma. L018 therefore gives a zero of xi
at 1/2+i gamma. For a=-4 gamma^2, the two possible square roots
are +/-2i gamma, and reflection sends one resulting xi argument
to the other. Thus G(a)=0 independently of that choice. Since
a!=0 and R>0, ell is finite and z1=a is exactly the simultaneous
condition x1=ell, y1=phi modulo 2pi. It imposes no restriction
on x2 or y2. At this fiber the denominator in F is nonzero,
and exact domination forces q=r=0 even if G has a multiple zero.
No entire angular torus is asserted to vanish.

For each fixed finite s define

\[
 \epsilon_N(s)=\sup_{y\in\mathbb T^2}
 |q_N((\ell,s),y)-q((\ell,s),y)|.
\]

The angular slice is continuous and compact, so the cited product
Fejer theorem gives epsilon_N(s)->0. The normalized fiber average
satisfies |D_N(s)|<=epsilon_N(s). Integration of its finite
polynomial kills precisely n2!=0. The zero term has weight one;
the term n=(k,0) has weight w_N(k)w_N(0)=w_N(k), phase
exp(i k phi), and coefficient B_(k,0)''(k ell). C868a's
profile identity makes that coefficient independent of s.
Consequently the exact finite subtraction yields

\[
 |\widehat q_0(\ell,s)-\widehat q_0(\ell,\ell)|
   =|D_N(s)-D_N(\ell)|
   \leq\epsilon_N(s)+\epsilon_N(\ell)\longrightarrow0.
\]

This verifies (3) for every real s. Only two fixed compact slices
are used at a time. There is no absolute summability assumption,
trace of a formal series, radial uniform-convergence claim or
exchange with a noncompact limit. C868a identifies the second
mean as A; L868 identifies the mean of S as K. Hence the mean of
h on the line is exactly H=K-A, a finite nonnegative number.

For any integer frequency the modulus of h's coefficient on that
line is at most its normalized integral, namely H, because h>=0.
If n2!=0, the point x*=(ell,(n dot x-n1 ell)/n2) is a finite
radial point with n dot x*=n dot x. Formula (8) equates the two
h coefficients, proving the bound at arbitrary x. Negative n2
causes no change. If n2=0 and n!=0, then n1!=0 and the point
(x1,x1) has the same profile argument n1 x1; C868a's diagonal
mean and positivity give the same bound there. These cases exhaust
all nonzero frequencies. Neither case controls hhat_0(x).

For the opposite-index tests, d=x1-x2 and x*=(ell,ell-d)
work simultaneously for every k, because (k,-k) dot x*=k d.
The zero coefficient of the nonnegative function h(x*,.) is H.
For k!=0 its coefficient at (k,-k) equals the asserted a_k(x).
Since h is real, a_-k=conjugate(a_k), so the finite quadratic
form is real. With theta=y1-y2, its exact expansion is

\[
 \sum_{j,l=0}^{N}c_j\overline{c_l}\,a_{j-l}(x)
 =\left\langle h(x^*,y)
       \sum_{j,l=0}^{N}c_j\overline{c_l}
           e^{-i(j-l)\theta}\right\rangle_y
 =\left\langle h(x^*,y)
       \left|\sum_{j=0}^{N}c_j e^{-ij\theta}\right|^2
   \right\rangle_y\geq0.
\]

Here brackets denote the normalized angular integral. This checks
both the index sign and the replacement of the diagonal by H;
the replacement is justified at x*, not by claiming that the
actual mean at x is H. The argument includes N=0 and zero
coefficients, uses only finite sums, and needs no infinite
Toeplitz representation theorem.

If H=0, (4) kills every nonzero coefficient at each fixed radial
point. All product Fejer polynomials of h at that point are the
constant hhat_0(x). Their uniform convergence proves exactly (6).
This is angular uniqueness, not radial constancy. For the existing
L868(12)-(13) bump, the annuli are disjoint, so it vanishes at
equal radii. Moreover both annuli lie in a disk where G has no
zero; thus |a| is outside them and the bump also vanishes on
x1=ell. Its S is zero and its h varies radially, consistently
giving A=H=K=0 and no nonzero angular modes. This is a check of
the existing example, not a new certificate or an application
of the radial-independent-h subclass theorem.

Finally L868's fixed orientation gives the period -(2pi)^2 K,
so strict gain still means K<-|M|. None of the audited steps
estimates A at -|M|-H, bounds the zero mode globally, or proves
that these necessary Fourier tests are sufficient for the original
domination and closure system. All other F zeros and all J zeros
remain in force; no Fejer polynomial replaces a feasible triple.
Graph realization and actual-Xi all-degree positivity remain open.

No mathematical defect was found. The fixed-fiber means, global
nonzero-mode bound, finite opposite-index positivity and H=0 angular
independence are accepted as a checked local input. This audit
reproduces the submitted result, with no stronger conclusion.

## Mathlib

Full matching coverage and supporting formal Fourier results were
not checked; unknown availability is not evidence of absence.
Hardy's theorem and product Fejer convergence are the cited known
inputs. The coordinate specialization and fixed-fiber argument have
passed the independent informal conceptual audit above. No
mathematical script, numerical evidence or formal verification is used.
