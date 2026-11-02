# Lemma 608: consistency of the actual Jacobi orbit and kernel reconstruction

## Hypotheses

Let x>0 and define the real-nome theta constants by

\[
Y(x)=\theta_3(x)=\sum_{n\in\mathbb Z}e^{-\pi n^2x},\quad
\theta_2(x)=\sum_{n\in\mathbb Z}e^{-\pi(n+1/2)^2x},\quad
\theta_4(x)=\sum_{n\in\mathbb Z}(-1)^n e^{-\pi n^2x}.
\]

Set L=log x, and on the entire real L axis define

\[
\mathscr Y(L)=Y(e^L),\quad A(L)=\pi e^L\mathscr Y(L)^4,
\quad a=A'/A,
\quad U=2a'+1-a^2,
\quad V=a''+a^3-3aa'-a.
\]

Primes on these state variables mean L derivatives; subscripts x on
Y mean ordinary x derivatives. This A is the source's state variable,
not the boundary function named A in L019. Use L019's K on [0,infinity)
and its even extension k(u)=K(|u|).

Import the following precisely scoped source inputs.

1. Dan Romik, *The Taylor coefficients of the Jacobi theta constant
   theta_3*, [arXiv:1807.06130v2](https://arxiv.org/pdf/1807.06130v2),
   Section 1.1 (1)-(3), printed pp.1-2, and Section 6 (28), p.14:
   theta analyticity on Re x>0, the modular identity
   Y(1/x)=sqrt(x)Y(x), the value
   Y(1)=Gamma(1/4)/(sqrt(2) pi^(3/4)), and the named Jacobi equation
   \[
   (Y^2Y_{xxx}-15YY_xY_{xx}+30Y_x^3)^2
   +32(YY_{xx}-3Y_x^2)^3
   =\pi^2Y^{10}(YY_{xx}-3Y_x^2)^2.                 \tag{1}
   \]
   The source's centered-coordinate Theorem 11 is not used: its
   coefficient is different. The original Jacobi-equation proof is
   not independently audited here.
2. Michel Planat and Patrick Sole, *Second-Level Concavity of the
   Riemann Xi Kernel*,
   [arXiv:2608.19160v1, Section 5.1, Lemma 5.1 (5.7)](https://arxiv.org/html/2608.19160v1#S5.SS1):
   on this actual theta-defined trajectory, for every real L,
   \[
   U(L)=\pi^2e^{2L}\theta_2(e^L)^4\theta_4(e^L)^4>0.       \tag{2}
   \]
   This is an explicitly imported positive-divisor identity. Its
   upstream logarithmic-derivative identities and their proof are
   unaudited in this result; no division by U is used to justify (2).

The audited source claims are Planat–Sole v1, Proposition 5.3
(5.10)-(5.11) and Section 5.2 (5.12). The claims themselves are
replayed below, not assumed. This lemma is conditional on the stated
imports and makes no assertion about arbitrary curves satisfying only
the squared Jacobi relation.

## Conclusion

The function chi=V/U is well-defined and real analytic for every real L.
The actual theta orbit satisfies everywhere

\[
\boxed{
a'=\tfrac12(U+a^2-1),\qquad
U'=2U(a+\chi),\qquad
\chi'=a\chi-U.}                                           \tag{3}
\]

In particular, the third equation remains valid at every V=0; it is
not obtained by division there. At the modular fixed point,

\[
a(0)=\chi(0)=0,\quad
U(0)=R_*:=\frac{\Gamma(1/4)^8}{64\pi^4},\quad
\chi'(0)=-R_*<0.                                         \tag{4}
\]

With the positive real fourth root of A, the source's kernel obeys

\[
\Phi(L/4)=\frac{A(L)^{1/4}}{8\pi^{1/4}}
       \left[U(L)+\frac32(a(L)^2-1)\right].                \tag{5}
\]

Consequently the exact L019 normalization is

\[
\boxed{
k(u)=4\Phi(u/2)=\frac{A(2u)^{1/4}}{2\pi^{1/4}}
       \left[U(2u)+\frac32(a(2u)^2-1)\right]
\quad(u\in\mathbb R).}                                  \tag{6}
\]

All state derivatives in (3)-(5) are in L; substituting L=2u
multiplies a first derivative by 2. There is no division by L in
these formulas. This is a source reproduction and coordinate audit,
not a new Jacobi equation, spatial concavity theorem, integrated
Fourier estimate, first Laguerre sign or RH argument.

## Proof

**Regularity and permitted denominators.** The defining theta series,
with any fixed number of derivatives, converge locally uniformly in
Re x>0: on Re x>=epsilon>0 their terms are bounded by a polynomial
in n times exp(-pi epsilon n^2), with the analogous shifted bound
for theta_2. Thus these series are holomorphic there. In particular
all displayed compositions are real analytic at every finite real L.
For real x>0, Y(x)>=1, so x, Y and A are strictly positive. Input (2)
gives U>0, making chi real analytic everywhere. These facts justify
the divisions by x,Y,A,U used below. No uniform lower bound as
L tends to infinity is needed.

**The squared relation with the correct x coordinate.** Put
b(L)=xY_x(x)/Y(x)=(a-1)/4, and q(x)=Y_x/Y=b(L)/x.
Ordinary differentiation, with d/dx=x^(-1)d/dL on functions of L,
gives

\[
q_x=(b'-b)/x^2,\qquad q_{xx}=(b''-3b'+2b)/x^3.
\]

Therefore

\[
\begin{split}
YY_{xx}-3Y_x^2
 &=Y^2(q_x-2q^2)
  =\frac{Y^2}{x^2}(b'-b-2b^2)
  =\frac{Y^2}{8x^2}U,\\
Y^2Y_{xxx}-15YY_xY_{xx}+30Y_x^3
 &=Y^3(q_{xx}-12q q_x+16q^3)\\
 &=\frac{Y^3}{x^3}
       (b''-3b'+2b-12bb'+12b^2+16b^3)
  =\frac{Y^3}{4x^3}V.
\end{split}                                                \tag{7}
\]

For clarity, the first last equality uses
8(b'-b-2b^2)=2a'+1-a^2. In the second, the b' terms total
-3aa'/4 and 2b+12b^2+16b^3=(a^3-a)/4, while b''=a''/4.
Substitute (7) in the imported (1) and multiply by 64x^6/Y^6.
The result is

\[
4(V^2+U^3)=\pi^2x^2Y^8U^2=A^2U^2,
\qquad A^2=4(U+\chi^2).                                 \tag{8}
\]

The latter equality divides only by the positive U^2. No square
root or branch sign for V has been chosen.

**The unsquared equations and exceptional points.** The first
equation in (3) is the definition of U. The definitions also give

\[
U'=2a''-2aa'=2aU+2V=2U(a+\chi)                          \tag{9}
\]

at every L. Differentiate (8), use A'=aA and (9), and substitute
A^2=4(U+chi^2). Explicitly,

\[
8a(U+\chi^2)=2aA^2=4U'+8\chi\chi'
                  =8U(a+\chi)+8\chi\chi',
\]

so

\[
\chi(\chi'-a\chi+U)=0.                                  \tag{10}
\]

This only directly proves the third equation where chi is nonzero.
We now verify that those points are dense, using the actual theta
orbit rather than an arbitrary solution of (10).

For x>=1, the defining series imply the explicit finite bounds

\[
\begin{split}
0<\theta_2(x)
 &=2e^{-\pi x/4}\sum_{n\ge0}e^{-\pi n(n+1)x}
 \le C_2e^{-\pi x/4},\\
|\theta_4(x)|&\le1+2\sum_{n\ge1}e^{-\pi n^2}=C_4<\infty.
\end{split}
\]

Here C_2=2 sum_(n>=0) exp(-pi n(n+1)) is finite. The convergence
follows, for example, by comparison with geometric
series for n>=1. Since A^2=pi^2 x^2Y^8>=pi^2x^2, input (2) yields

\[
0<\frac{U}{A^2}\le C_2^4C_4^4e^{-\pi x}\longrightarrow0.
\]

Thus (8) gives chi^2=A^2/4-U>0 at all sufficiently large finite x.
In particular chi is not identically zero. A nonzero real analytic
function on the connected real line has only isolated zeros: an
accumulation at a finite point would force every Taylor coefficient
there to vanish and then force the function to vanish identically.
Its nonzero set is therefore dense. The continuous function
chi'-a chi+U vanishes on that set by (10), so it vanishes everywhere.
This proves the third equation including all V=0. The argument
does not presume chi'(0), choose a square-root branch, or exclude
the modular point.

**Modular point.** The imported modular identity gives
mathscr Y(-L)=exp(L/2)mathscr Y(L), hence A(-L)=A(L).
Since A>0, a is odd. Its derivative a' is even, making U even;
a'' and each of a^3, aa', a are odd, making V and chi odd.
It follows that a(0)=chi(0)=0. Equation (8) now gives
U(0)=A(0)^2/4. The imported value of Y(1) implies
A(0)=Gamma(1/4)^4/(4pi^2), proving the value in (4).
The already extended third equation then gives chi'(0)=-U(0).
Also (3) gives U'(0)=0 and a'(0)=(R_*-1)/2, consistent with
the even and odd parities. No endpoint exception remains.

**Kernel reconstruction and L019 coordinates.** The source uses

\[
\Phi(r)=\sum_{n\ge1}\pi n^2(2\pi n^2e^{4r}-3)
                         e^{5r-\pi n^2e^{4r}}.
\]

Local uniform convergence permits ordinary x differentiation of Y.
For x=exp(4r), termwise differentiation gives exactly

\[
\Phi(r)=x^{5/4}(xY_{xx}+\tfrac32Y_x).                    \tag{11}
\]

Indeed Y_x=-2pi sum n^2 exp(-pi n^2x) and
Y_xx=2pi^2 sum n^4 exp(-pi n^2x), giving each displayed
Phi summand. At r=L/4, (11) and q=b/x give

\[
\begin{split}
\Phi(L/4)
 &=x^{1/4}Y\,[b'+b^2+b/2]\\
 &=\frac{A^{1/4}}{\pi^{1/4}}\,
       \frac{4a'+a^2-1}{16}\\
 &=\frac{A^{1/4}}{8\pi^{1/4}}
       \left[U+\frac32(a^2-1)\right],
\end{split}
\]

which proves (5). The positive real fourth root is forced by
x>0,Y>0. Neither the bracket nor 1-a^2 is a denominator.
This formula and the parities just proved also show Phi is even.

For u>=0, four times the Phi summand at r=u/2 is

\[
[8\pi^2n^4e^{9u/2}-12\pi n^2e^{5u/2}]
                       e^{-\pi n^2e^{2u}},
\]

exactly L019's K summand. Equality holds at u=0 as well by
convergence. Evenness extends the equality to k(u) for all real u,
and L=4r=2u in (5) proves (6). This rechecks, as required for this
coordinate audit, the normalization also recorded in L605; no hazard
or spatial shape theorem from L605 is used as a premise.

**Scope of the audit.** Equations (3)-(6) reproduce the indicated
source package conditional on (1)-(2). The missing exceptional-point
detail in the compressed source proof is supplied above; no incorrect
coefficient or identity was found. The full spatial concavity proof,
elliptic inequalities and source certificates are outside this audit.
In particular a spatial nonlinear state does not close the Fourier
transform, bound the nonlocal Stein tail, or control L604's signed
integral. Those are unresolved separate requirements.

## Mathlib

Full-result and supporting-result Mathlib coverage not checked.
No matching formal theorem or absence claim is made. The real-analytic
identity theorem is used in its standard elementary form; the explicit
theta inputs and their unaudited upstream status are recorded above.
