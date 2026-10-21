# Lemma 372: eventual simple-zero counting for the actual regulator response

**Hypotheses.** Let G be the actual right regulator derivative in L366 (1),
with real frequency t. Use L368's exact reflected carrier, and L005's
Euler logarithm only on Re v>1. No assumption on critical-strip zeros,
F_0/G common zeros, or a positive regulator is made.

**Conclusion.** There is a finite, unevaluated H_0>0 such that every real
zero of G on [H_0,infinity) is simple. For every fixed H≥H_0 and every
real X≥H, the number of real zeros in the closed interval, counted either
distinctly or with multiplicity, satisfies

\[
 N_G([H,X])=\frac{X}{2\pi}\log\frac{X}{2\pi}
                -\frac{X}{2\pi}+O_H(1).                 \tag{1}
\]

The error is bounded independently of X, including when H or X is a
zero and when X=H. No numerical onset or constant-term refinement is
claimed. This is a response-only reference count, not a zero count for
F_0, a comparison between the pair, or a new actual-theta sign.

**Proof.** This is a **REPRODUCTION** of the standard phase-level counting
mechanism, specialized to the response with its variable completion
factor. The source comparison is J. C. Lagarias, *Zero spacing
distributions for differenced L-functions*, Acta Arith. 120(2) (2005),
159–184, DOI 10.4064/aa120-2-4,
[arXiv:math/0601653v2](https://arxiv.org/pdf/math/0601653v2), Theorem 3.1
and its §3 proof, equations (3.2)–(3.5), PDF pp. 9–10; Lemma 4.1(1),
pp. 11–12, treats the bounded logarithmic derivative on a line to the
right of 1. Its stated count is for constant-angle shifted-xi projections
and has O(log X) error. It is not imported as a theorem about G. We prove
the specific variable-factor assembly and bounded error here. The scalar
inputs have already been proved or cited in L005 and L368; their named
sources are [DLMF 25.2.1/11](https://dlmf.nist.gov/25.2),
[5.11.2 and §5.11(ii)](https://dlmf.nist.gov/5.11), with the right-line
and gamma-sector qualifications stated below. No reproof of those scalar
theorems is needed.

For t>0 put

\[
 s=\tfrac14+it/2,\quad v=\tfrac52+it,\quad
 Q=(t^2+\tfrac14)\Gamma(s)\pi^{-s},\quad
 b=-s(s+\tfrac12)/\pi,\quad Z=\zeta(v).
\]

L366 (1) fixes the response convention, and L368 (3)–(4) gives exactly

\[
 G(t)=\operatorname{Re}(Q(t)b(t)Z(t)),\qquad
 B(t)=|Q(t)b(t)|>0.                                  \tag{2}
\]

Choose L368's smooth real phase theta on the positive half-line with
Qb=B exp(i theta). Its derivative obeys, for some t_0≥1 and C_0≥0,

\[
 \theta'(t)=\tfrac12\log(t/(2\pi))+r(t),\qquad
 |r(t)|\le C_0t^{-2}\quad(t\ge t_0).                 \tag{3}
\]

This is the uniform first line of L368 (8), including the polynomial b
correction. The underlying digamma estimate applies at Re s=1/4 inside
the closed sector |arg s|≤3pi/4 at large t, separated from the negative
real axis. In particular (3) is an estimate for the actual carrier,
not a derivative obtained by differentiating an uncontrolled remainder.

Let mathscr L be L005's absolutely locally uniformly convergent Euler
logarithm. On the actual fixed line Re v=5/2 it gives

\[
 Z(t)=\exp\mathscr L(v),\qquad
 |\mathscr L(v)|\le\mathscr L(5/2)=\log\zeta(5/2)=:E. \tag{4}
\]

The bound follows by taking absolute values term by term in the
absolutely convergent double series; its positive real-line sum is E.
Local uniform convergence makes mathscr L holomorphic on Re v>1.
Define eta(t)=Im mathscr L(v), retaining this continuous branch throughout
the ray rather than reducing it to a principal argument. Then |eta|≤E.
Differentiating Z=exp mathscr L along the real t variable gives

\[
 \eta'(t)=\operatorname{Im}\frac{Z'(t)}{Z(t)}.
\]

L368 (5)–(6) supplies
|Z'|≤M_1=sum_(n≥1)(log n)n^(-5/2)<infinity and
|Z|≥m=1/zeta(5/2)>0. Thus

\[
 |\eta'(t)|\le K:=M_1/m\quad(t>0).                  \tag{5}
\]

All these bounds are on the absolutely convergent side of the Euler
product; no continuation of a prime sum into the critical strip occurs.

Set

\[
 D(t)=B(t)\exp(\operatorname{Re}\mathscr L(v))>0,
 \qquad \phi(t)=\theta(t)+\eta(t).
\]

Equations (2) and (4) give the exact full-phase representation

\[
 G(t)=D(t)\cos\phi(t).                               \tag{6}
\]

By (3) and (5),
phi'(t)≥one-half log(t/(2pi))−K−C_0/t^2 for t≥t_0.
Choose one finite H_0≥t_0 so large that
one-half log(H_0/(2pi))>K+C_0+1. Since t≥H_0≥1, this ensures
phi'(t)>1 for every t≥H_0. The existence of this single onset uses only
finite constants independent of t; it does not assert an evaluated
threshold. Therefore the full phase, including its zeta correction, is
strictly increasing on the entire eventual ray.

At any zero t_*≥H_0, (6) gives phi(t_*)=pi/2+k pi for an integer k.
Differentiating (6) at that point yields

\[
 G'(t_*)=-D(t_*)\sin\phi(t_*)\,\phi'(t_*)\ne0.        \tag{7}
\]

The amplitude is positive, |sin phi(t_*)|=1, and phi' is positive.
Thus every such zero is transverse and simple; no division by G is used.
The scalar factors in (2) are holomorphic in a neighborhood of each real
t, so their real projection is real analytic. Consequently the usual
analytic multiplicity is indeed one at the zeros in (7).

To control the phase itself define

\[
 f(t)=\tfrac t2\log\frac{t}{2\pi}-\tfrac t2,
 \qquad f'(t)=\tfrac12\log\frac{t}{2\pi}.
\]

For every fixed H≥H_0 and X≥H, integrate (3) on the finite interval:

\[
 \phi(X)-\phi(H)
   =f(X)-f(H)+\int_H^X r(u)\,du+\eta(X)-\eta(H).
                                                               \tag{8}
\]

The two error terms have the uniform bound

\[
 \left|\int_H^X r(u)\,du+\eta(X)-\eta(H)\right|
       \le C_0/H+2E.                                  \tag{9}
\]

This is an absolutely convergent integral bound for the carrier error
and a bound on the Euler logarithm itself. Integrating only (5) would
give a growing error and would not prove (9).

For exact closed-endpoint counting put
alpha=(phi(H)−pi/2)/pi and beta=(phi(X)−pi/2)/pi.
Continuity and strict increase give precisely one zero for each integer
k in [alpha,beta], and no other zero. Consequently

\[
 N_G([H,X])=\lfloor\beta\rfloor-\lceil\alpha\rceil+1.
                                                               \tag{10}
\]

Since beta≥alpha, the right side is nonnegative: floor beta is at least
ceil alpha−1. Equality at either endpoint is retained by the floor and
ceiling. Subtracting beta−alpha from (10) gives
(floor beta−beta)+(alpha−ceil alpha)+1 in (−1,1], so

\[
 \left|N_G([H,X])-\frac{\phi(X)-\phi(H)}\pi\right|\le1. \tag{11}
\]

This also treats X=H: the count is one exactly when H is a zero, and
zero otherwise. Combining (8)–(11) proves the concrete uniform bound

\[
 \left|N_G([H,X])-\frac{f(X)}\pi\right|
 \le\frac{|f(H)|}\pi+\frac{C_0}{\pi H}+\frac{2E}\pi+1.
                                                               \tag{12}
\]

Its right side is independent of X, and f(X)/pi is exactly the two main
terms in (1). Simplicity makes distinct and multiplicity counts equal.
This proves the approved target. No statement about the count of F_0,
common zeros, the signed discriminant residual, or a margin in L367
has been inferred. In particular L371's generic distinct-count failure
is not repaired by this response-only computation. ∎

### Critical audit, 2026-10-06

The separately approved REPRODUCTION audit checks (2)–(12) against
L005, L366 (1), and L368 (3)–(8). The proof survives without a repaired
claim, new estimate or stronger conclusion. In particular:

- Substitution of v=2s+2 in L366's reflected quotient gives
  \(-p\xi_c(v)/v=-p(s+1/2)\Gamma(s+1)\pi^{-s-1}Z=QbZ\).
  Thus taking real parts preserves both the minus sign and the
  completion's factor 1/2. Gamma has no zero or pole on this line,
  p>0, and neither s nor s+1/2 vanishes; B is strictly positive.
- The exact carrier derivative is
  \(\theta'=\tfrac12(\operatorname{Re}\Psi(s)-\log\pi)
  +\operatorname{Im}(b'/b)\). The real p'/p contributes nothing.
  L368's separately controlled digamma expansion, together with
  \(\log|s|-\log(t/2)=\tfrac12\log(1+1/(4t^2))\),
  gives the uniform integrable error in (3). Its exact rational
  b'/b correction is also O(t^−2); no asymptotic error is differentiated.
  Only the first carrier derivative is needed for this count.
- L005 fixes one holomorphic Euler logarithm on Re v>1. Its absolute
  majorant E bounds its imaginary part itself for every height.
  Differentiating the exponential identity gives Z'/Z along t,
  so (5) bounds the derivative of that same branch. This checks that
  (6) has the full phase, and that (8)–(9) do not replace a bounded
  derivative by an unjustified bounded accumulated error. All E, K,
  C_0 and t_0 are independent of t and X. The choice of H_0 in the
  proof works simultaneously for every t≥H_0, since t^−2≤1 and the
  logarithm increases. The integral bound is C_0(1/H−1/X)≤C_0/H.
- Near a real point, the carrier product P=QbZ is holomorphic; the
  local extension of its real restriction is
  \((P(z)+\overline{P(\bar z)})/2\) on a conjugation-invariant disk.
  Hence its real-analytic multiplicity is defined. Equation (7)
  proves multiplicity one even if that zero is an interval endpoint.
  No assumption about F_0 or common zeros is used.

For an independent endpoint check let e denote the count in (10) minus
beta−alpha, and let {x}=x−floor(x). Direct integer counting gives:

| alpha | beta | e |
| --- | --- | --- |
| integer | integer | 1 |
| integer | noninteger | 1−{beta} |
| noninteger | integer | {alpha} |
| noninteger | noninteger | {alpha}−{beta} |

All cases satisfy |e|≤1. An empty integer interval necessarily has
noninteger endpoints in the same unit interval, so the last row gives
e=−(beta−alpha) and count zero. If X=H, alpha=beta: the first row
counts the singleton zero once, while the last row counts zero. Strict
increase prevents any other endpoint identification or repeated level.
Thus closed endpoints and empty intervals do not require a growing
correction. Combining this check with (9) recovers exactly (12), whose
right side is finite for each fixed H and independent of X.

The direct mathematical inputs remain L005, L366 and L368. The named
phase-count source is a comparison, not an unstated theorem about G.
The audit validates the existing response reference count only; it
does not evaluate H_0, repair L371's distinct-count obstruction, or
establish any actual-pair count inequality or actual-theta positivity.

**Mathlib.** Full matching response count and phase-level counting:
**not checked**. Supporting Euler-product and right-half-plane
nonvanishing coverage is inherited from L005, including
[riemannZeta_eulerProduct_exp_log](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/EulerProduct/DirichletLSeries.html#riemannZeta_eulerProduct_exp_log).
These supporting theorems do not establish the full response count.
Unknown full coverage is not evidence of absence or originality.
