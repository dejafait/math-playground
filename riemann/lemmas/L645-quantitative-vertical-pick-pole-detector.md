# Lemma 645: a quantitative detector on every vertical Pick grid

## Hypotheses

Use the entire completion of L018,

\[
 \xi(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s),
 \qquad F(s)=\xi'(s)/\xi(s),
\]

with the removable values in the completion formula understood;
\(F\) is meromorphic and is evaluated only where \(\xi\ne0\).
Suppose conditionally that
\(\rho=\beta+i\gamma\) is a **simple** zero of \(\xi\), with
\(\gamma\ge e^5\) and \(1/2<\beta<1\). Define

\[
 \delta=\beta-\tfrac12\in(0,\tfrac12),\quad
 s_*=2+i\gamma,\quad a=\tfrac32,\quad d=a-\delta,\quad
 R=R_\delta=a-\tfrac\delta2,
\]
\[
 M_\rho=\max_{|s-s_*|=R} (|\xi(s)|+|\xi'(s)|),\qquad
 H_\rho=\frac{(1+|F(s_*)|)M_\rho}{|\xi'(\rho)|},\qquad
 h=\log^+H_\rho=\log\max\{1,H_\rho\}.
\]

For each integer \(n\ge1\), retain exactly the nodes and matrix

\[
 s_j=2+i(\gamma+j/n),\qquad
 K_n(\gamma)_{jk}
 =\frac{F(s_j)+\overline{F(s_k)}}{3+i(j-k)/n},
 \qquad 0\le j,k<n.
\]

L018 makes every datum finite, since \(\xi\) has no zeros on
\(\Re s=2\). No hypothesis on other zero multiplicities, a derivative
lower bound, a height-only growth bound, or actual matrix positivity
is imposed. All logarithms are natural.

## Conclusion

The following constants depend only on \(\delta\):

\[
 A_\delta=\frac{a+R}{a-R}=\frac6\delta-1>1,\qquad
 q_\delta=\left(\frac{R^2(d^2+1)}{R^4+d^2}\right)^{1/2}\in(0,1),
 \qquad \lambda_\delta=\log(1/q_\delta)>0,
\]
\[
 C_\delta=1+\frac{1+\log A_\delta}{\lambda_\delta}.
\]

Set the positive integer

\[
 n_0=1+\left\lfloor
        \frac{\log A_\delta+h}{\lambda_\delta}
       \right\rfloor.
\]

Then

\[
 n_0\le\left\lceil C_\delta(1+\log^+H_\rho)\right\rceil,
 \qquad
 K_n(\gamma)\text{ has a strictly negative eigenvalue for every }n\ge n_0.
\]

More precisely, for every integer \(n\ge1\), a temporary assumption
\(K_n(\gamma)\succeq0\) entails

\[
                   1\le A_\delta H_\rho q_\delta^n.                 \tag{1}
\]

This is a conditional detector for a specified simple off-line zero,
not a claim that such a zero exists. It specializes standard finite
interpolation and analytic zero bounds; no novelty is asserted.
The proof passed a separate critical audit on 1 November 2026 under
exactly these hypotheses; the audit record appears below.

## Proof

### Standard inputs and the scope of specialization

Import the following results with their stated hypotheses.

1. **Finite Nevanlinna–Pick interpolation, including singular data.**
   For distinct nodes \(\alpha_j\) in the open unit disk and specified
   values \(\eta_j\), a holomorphic \(g\) on that disk with \(|g|\le1\)
   and \(g(\alpha_j)=\eta_j\) exists if and only if
   \([(1-\eta_j\overline{\eta_k})/(1-\alpha_j\overline{\alpha_k})]\)
   is positive semidefinite. The conclusion includes singular PSD
   matrices and modulus-one data. This is the simple-value case of
   V. Bolotnikov, *A multi-point degenerate interpolation problem for
   generalized Schur functions*, Operators and Matrices **4** (2010),
   151–191, definitions (1.1)–(1.7) and Theorem 1.1, pp.151–153
   ([publisher PDF](https://files.ele-math.com/articles/oam-04-08.pdf)).
2. **Borel–Caratheodory, real-part version.** If \(f\) is holomorphic
   on \(|z|<b\), \(b>0\), and \(\Re f\le M\) there for a constant
   \(M>0\), then for \(|z|<b\),
   \[
    |f(z)|\le \frac{2M|z|}{b-|z|}
               +|f(0)|\frac{b+|z|}{b-|z|}.
   \]
   Use the named theorem in the precise form `Complex.borelCaratheodory`,
   [Mathlib frozen source](https://raw.githubusercontent.com/leanprover-community/mathlib4/0d3fb85496130669f472d62be6f25999ca085c59/Mathlib/Analysis/Complex/BorelCaratheodory.lean),
   commit `0d3fb85496130669f472d62be6f25999ca085c59`, lines 37–110.
3. **Finite Blaschke zero bound.** A holomorphic function bounded by
   \(B>0\) on \(|z|<R\), vanishing at distinct \(z_j\) there, satisfies
   \[
    |E(z)|\le B\prod_j
       \left|\frac{R(z-z_j)}{R^2-\overline{z_j}z}\right|.
   \]
   This is the finite-Blaschke division bound, after scaling the disk,
   in S. Zakeri, *A Course in Complex Analysis*, author
   [Notes and Comments, Section 8.3](https://zakerimath.com/CAbook/COM.html),
   paragraph following Example 8.33, accessed 1 November 2026.
   The complete argument permits extra zeros and does not require
   boundary continuity. Only the finite version is used here.

The saved source assessment inspected these statements and their needed
cases before this attempt. They are imported, not reproved. What follows
checks the exact scalar convention, disk bounds, array geometry and
strict integer quantifiers. It does not assume positive-real continuation
of the actual meromorphic function \(F\).

### 1. Temporary PSD gives a finite-data positive-real interpolant

Fix an arbitrary integer \(n\ge1\) and suppose \(K_n\succeq0\).
Write \(w_j=F(s_j)\) and \(x_j=s_j-1/2\). The matrix is Hermitian;
its diagonal is \(2\Re w_j/3\). Thus \(\Re w_j\ge0\), and
\(w_j+1\ne0\). Also \(\Re x_j=3/2>0\).

Put

\[
 \alpha_j=\frac{x_j-1}{x_j+1},\qquad
 \eta_j=\frac{w_j-1}{w_j+1}.
\]

The \(\alpha_j\) are distinct points of the open unit disk,
\(|\eta_j|\le1\), and \(\eta_j\ne1\). The exact identity

\[
 \frac{1-\eta_j\overline{\eta_k}}
      {1-\alpha_j\overline{\alpha_k}}
 =\frac{x_j+1}{w_j+1}
   \frac{w_j+\overline{w_k}}{x_j+\overline{x_k}}
   \frac{\overline{x_k}+1}{\overline{w_k}+1}                 \tag{2}
\]

is an invertible diagonal congruence of \(K_n\), since
\(x_j+\overline{x_k}=3+i(j-k)/n\). Therefore the disk Pick matrix
in (2) is PSD. Input 1 supplies a Schur interpolant \(g\), without
requiring positive definiteness.

The function \(g\) cannot take the value 1 anywhere in the open disk:
the maximum modulus principle would make it identically 1, contrary
to \(g(\alpha_0)=\eta_0\ne1\). Consequently

\[
 P(s)=\frac{1+g(\phi(s))}{1-g(\phi(s))},\qquad
 \phi(s)=\frac{(s-1/2)-1}{(s-1/2)+1},
 \qquad \Re s>1/2,
\]

is holomorphic and satisfies

\[
 \Re P(s)=\frac{1-|g(\phi(s))|^2}{|1-g(\phi(s))|^2}\ge0,
 \qquad P(s_j)=w_j.
\]

A unimodular constant \(g\ne1\) is allowed and gives a purely imaginary
constant \(P\); the argument retains that boundary case. In particular
\(P(s_*)=w_0=F(s_*)\), because the anchor is a node for every \(n\).
Only these finite data are interpolated. No equality \(P=F\) away
from them is claimed.

### 2. Bound the analytic residual on the prescribed disk

The open disk \(|s-s_*|<a=3/2\) lies in \(\Re s>1/2\). Apply
input 2 to \(f(z)=-P(s_*+z)\) on this disk with the strictly positive
real-part upper bound \(M=1\); indeed \(\Re f\le0\le1\).
For \(|s-s_*|\le R<a\), that theorem gives

\[
 |P(s)|\le\frac{2R+|F(s_*)|(a+R)}{a-R}
        \le A_\delta(1+|F(s_*)|),                         \tag{3}
\]

where the second inequality uses \(2R\le a+R\). This application
requires neither \(\Re F(s_*)>0\) nor a lower bound for its modulus.

Define

\[
                       E(s)=\xi'(s)-P(s)\xi(s).
\]

It is holomorphic on \(\Re s>1/2\), even at zeros of \(\xi\).
On the circle \(|s-s_*|=R\), (3) and \(A_\delta>1\) imply

\[
 |E(s)|\le A_\delta(1+|F(s_*)|)
               (|\xi'(s)|+|\xi(s)|)
          \le B,
 \qquad B=A_\delta(1+|F(s_*)|)M_\rho.                    \tag{4}
\]

The closed radius-R disk is strictly inside the half-plane, so \(E\)
is holomorphic on a neighborhood of it. The maximum modulus principle
extends (4) throughout the disk. All samples lie inside it because
\(|s_j-s_*|=j/n<1<R\). Moreover \(\rho-s_*=-d\) and
\(0<d<R\), so \(\rho\) also lies inside. The simple-zero assumption
and the interpolation give exactly

\[
 E(s_j)=0\quad(0\le j<n),\qquad E(\rho)=\xi'(\rho)\ne0. \tag{5}
\]

The same maximum principle applied to the entire function \(\xi'\)
shows \(M_\rho\ge|\xi'(\rho)|>0\), hence \(H_\rho\ge1\) and \(B>0\).
No quantitative lower bound on that nonzero derivative is being used.

### 3. A contraction uniform in all the moving grids

Apply input 3 to \(E(s_*+z)\), with zeros \(z_j=it_j\),
\(t_j=j/n\), and evaluate at \(z=-d\). Equations (4)–(5) yield

\[
 |\xi'(\rho)|\le B\prod_{j=0}^{n-1} b_\delta(t_j),\qquad
 b_\delta(t)^2=\frac{R^2(d^2+t^2)}{R^4+d^2t^2}.           \tag{6}
\]

The denominator is nonzero. For \(u\ge0\), differentiation gives

\[
 \frac{d}{du}\frac{R^2(d^2+u)}{R^4+d^2u}
 =\frac{R^2(R^4-d^4)}{(R^4+d^2u)^2}>0,
\]

because \(R>d>0\). Thus \(0\le t_j<1\) entails
\(b_\delta(t_j)\le b_\delta(1)=q_\delta\). Finally

\[
 1-q_\delta^2
 =\frac{(R^2-d^2)(R^2-1)}{R^4+d^2}>0,
\]

since \(R>d\) and \(R>5/4>1\). This proves \(0<q_\delta<1\).
Divide (6) by \(|\xi'(\rho)|\) to obtain (1). The bound is uniform
over \(j/n\) and all \(n\ge1\); no nesting of the grids is needed.

### 4. Strict integer threshold and the stated order bound

Let \(X=(\log A_\delta+h)/\lambda_\delta\). Since
\(A_\delta>1\) and \(h\ge0\), \(X>0\) and \(n_0=\lfloor X\rfloor+1\)
is a positive integer. For every integer \(n\ge n_0\), one has
\(n>X\), including when \(X\) is itself an integer. Therefore

\[
 A_\delta H_\rho q_\delta^n
 \le\exp(\log A_\delta+h-n\lambda_\delta)<1,
\]

contradicting (1). Hence \(K_n\) is not PSD. As it is a finite
Hermitian matrix, the spectral theorem gives a strictly negative
eigenvalue. The argument applies separately to every \(n\ge n_0\).

For the requested explicit form, use

\[
 n_0\le1+\frac{\log A_\delta+h}{\lambda_\delta}
      \le\left(1+\frac{1+\log A_\delta}{\lambda_\delta}\right)(1+h).
\]

The second difference is
\(h+(1+h\log A_\delta)/\lambda_\delta\ge0\). Taking the ceiling
proves the asserted bound with the displayed finite \(C_\delta\).

### Qualifications and comparison with the logarithmic grid size

For \(N=\lfloor\log\gamma\rfloor\ge5\), this proof reaches that
particular matrix if

\[
        \lambda_\delta N>\log A_\delta+\log^+H_\rho.       \tag{7}
\]

Indeed (7) is equivalent to \(N\ge n_0\) for the stated \(n_0\).
Since \(H_\rho\ge1\), it can also be written
\(H_\rho<A_\delta^{-1}e^{\lambda_\delta N}\). This strict comparison
is not supplied by finiteness of \(H_\rho\). No height-only estimate
for \(H_\rho\), no uniform control as \(\delta\downarrow0\), and no
positivity of \(K_N\) or any other actual matrix is proved here.

The lower-height hypothesis is retained from the approved target; the
analytic detector itself does not use its numerical size. At a multiple
zero, (5) would instead give \(E(\rho)=0\); the present proof and
normalization do not cover that case. Other zero multiplicities do not
affect the proof, which uses the entire completion without truncation.

L258 already supplies a different normalized-growth finite Laguerre
witness. This result is its analogue for the exact nonnested vertical
Pick arrays, using the cited interpolation machinery, not a new general
positivity principle. C644a's fixed-reserve obstruction is not an input
and remains intact. Actual-Xi signs and full RH remain open.

### Independent critical audit — 1 November 2026

**Verdict: accepted as stated.** The audit used the previously approved
SPECIALIZE source assessment, with L018 as the local mathematical
input. The three standard theorems above remain imports; this audit
checks their applicability and the quantitative specialization. No
constant, threshold or mathematical hypothesis needed repair. The
hypothesis wording now explicitly distinguishes the removable values
of the completion formula from the genuine poles of \(F\).

The following are the load-bearing checks, including the degenerate
and endpoint cases.

1. **Finite PSD, not global positivity.** For each fixed \(n\), the
   diagonal gives \(\Re w_j\ge0\). Thus \(\Re(w_j+1)\ge1\) and
   \(\Re(x_j+1)=5/2\), so every diagonal congruence factor in (2)
   is finite and nonzero. Expanding each Cayley numerator gives the
   factors \(2(w_j+\overline{w_k})\) and
   \(2(x_j+\overline{x_k})\); their 2's cancel. This verifies the
   exact matrix convention, including conjugations. The cited finite
   Pick theorem includes singular PSD. If its interpolant takes any
   unimodular value internally it is constant. The constant 1 is
   excluded by \(\eta_0\ne1\); every other unimodular constant has
   a legitimate purely imaginary inverse Cayley transform. The
   anchor value is fixed for all grids, although the interpolants may
   differ. No passage to an infinite interpolant or identification
   with \(F\) is used.
2. **Analytic residual and uniform prefactor.** The geometric margins
   are \(a-R=R-d=\delta/2>0\), and \(R>5/4>1\). Hence the closed
   residual disk is inside the interpolant's domain, the specified
   \(\xi\)-zero \(\rho\) is internal, and every sample is internal.
   Borel–Caratheodory is
   applied on the larger *open* radius-\(a\) disk with \(M=1>0\),
   so it applies at every point of the smaller closed disk; there is
   no boundary-regularity assumption on \(g\). Since
   \(A_\delta(1+|F(s_*)|)\ge1\), the same factor bounds both terms
   of \(\xi'-P\xi\) in (4). The maximum principles used for \(E\)
   and \(\xi'\) are legitimate on neighborhoods of the closed
   radius-\(R\) disk. In particular \(B>0\) and \(H_\rho\ge1\).
   Zeros on its boundary and other multiple zeros cause no pole in
   \(E\); simplicity is used only for \(E(\rho)\ne0\).
3. **Uniform finite-zero contraction.** At \(z=-d\) and \(z_j=it\),
   the scaled Blaschke denominator is \(R^2-idt\), whose squared
   modulus is \(R^4+d^2t^2>0\). The derivative with respect to
   \(t^2\) in (6) has numerator \(R^2(R^4-d^4)>0\).
   The displayed identity for \(1-q_\delta^2\) therefore supplies
   a positive contraction margin for every allowed fixed \(\delta\).
   Replacing the \(n\) factors by \(q_\delta\) is valid even for
   \(n=1\). The bound is independent of the chosen finite
   interpolant and of the lack of nesting between grids.
4. **Strict threshold and remaining gap.** With \(H_\rho\ge1\),
   (1) permits equality when \(n=X\). The chosen
   \(\lfloor X\rfloor+1\), including integral \(X\), is strictly
   larger than \(X\), and so excludes PSD for every such integer
   \(n\). The difference in the bound for \(C_\delta(1+h)\)
   is exactly \(h+(1+h\log A_\delta)/\lambda_\delta\ge0\).
   Hermitian non-PSD means a strictly negative eigenvalue, not merely
   singularity. Finally, integer \(N\ge n_0\) is equivalent to
   \(N>X\), so (7) is the exact sufficient threshold of this proof.
   Its failure would not imply that \(K_N\) is PSD or that a smaller
   detector is impossible. Its truth, height-only growth control,
   actual matrix signs and extension to a multiple specified zero
   remain unproved.

This is an independent validation of a standard-tool specialization,
not an additional theorem beyond the sources checked or an RH candidate.
The comparison with L258 and the C644a stop introduces no mathematical
input; the existing DAG row remains correct.

## Mathlib

Supporting Borel–Caratheodory is present as
[`Complex.borelCaratheodory`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Complex/BorelCaratheodory.html#Complex.borelCaratheodory),
with the frozen source and explicit positive-bound hypothesis cited
above; its statement and supporting proof were inspected in the prior
source assessment. No local Lean replay was performed. Matching Mathlib
coverage for finite Pick interpolation, the finite-Blaschke division
bound, or this complete detector was not checked; no absence is claimed.
