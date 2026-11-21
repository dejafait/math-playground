# Corollary C032h: obstruction to the fixed polynomial common commutant

## Hypotheses

Use C032e's full theta density Psi and the unchanged scalar kernels
of C032f(1)-(3), on the original half-line (0,infinity). Thus

\[
 a_\sigma(t)=e^{\sigma t/8}F(t),\qquad F(t)=(1+t)\Psi(t),
 \qquad \sigma\in\{-1,+1\},
\]
\[
 b_\sigma(t)=((1-c)-(1+c)t)e^{\sigma t/8}\Psi(t).
\]

The input core is D=C_c^infinity((0,infinity);C). Let p,q be
one common pair of real polynomials of degree at most two with
p(0)=0 and p(x)>0 for every x>0. Write

\[
 p(x)=A x^2+B x,\qquad q(x)=C x^2+D_1x+E,
 \qquad T f=-(p f')'+qf.
 \tag{1}
\]

For a smooth scalar kernel k, the necessary compact-core identity
being tested is

\[
 (p(y)-p(x))k''(x+y)+(p'(y)-p'(x))k'(x+y)
 -(q(y)-q(x))k(x+y)=0\quad(x,y>0).
 \tag{2}
\]

In particular formal commutation T Gamma_k f=Gamma_k T f on D,
as an identity of smooth functions on the open half-line, requires
(2). No closed self-adjoint realization is assumed.

## Conclusion

There is no pair p,q satisfying these hypotheses for which (2)
holds for both a_- and a_+. Consequently there is no such pair
satisfying the necessary identity for all four a_sigma,b_sigma.
This includes linear p, constant q, and the original possibly complex
scalar c without imposing any reality assumption on it.

This excludes only the fixed degree-at-most-two common compact-core
commutant class. It does not exclude higher-degree or nonpolynomial
expressions, different domains without this core commutation property,
or other spectral interfaces. Neither delta=0 nor delta>0 in C032f,
actual adjoint-range inclusion, a source metric, or actual-Xi positivity
is determined. The bounded correctness audit1287 below accepts this
fixed-class obstruction without enlarging its conclusion.

## Proof

### Imported identity and applicability

The invocation-start SPECIALIZE assessment is
`drafts/literature/2026-11-17-fixed-polynomial-common-commutator-test-review-1284.md`.
Reuse its completed primary comparison1284 and earlier675/677 coverage.
Import Gordon Blower, *Hankel operators that commute with second-order
differential operators*, J. Math. Anal. Appl. **342** (2008), 601-614,
[DOI 10.1016/j.jmaa.2007.12.028](https://doi.org/10.1016/j.jmaa.2007.12.028),
[arXiv:0712.1013v1](https://arxiv.org/pdf/0712.1013v1), Theorem 2.1,
proof (2.3)-(2.5), printed pp.3-4, and Lemma 3.1/Proposition 3.2,
including (3.3), printed pp.5-6. Use source a=p,b=q; these are
not the notebook's kernel labels a_sigma,b_sigma. The proof's
commutator kernel is exactly the left side of (2). Its compact-core
iff statement gives the necessary identity, independently of the
sufficient quotient ansatz in the theorem statement. The polynomial
specialization includes the linear case; no translation or rescaling
of the fixed kernels is made. The general identity is imported,
not reproved here.

C032e proves that Psi is holomorphic in a neighborhood of each
positive real point, strictly positive on the positive real axis,
and obeys, for some finite M,

\[
 0<\Psi(t)\leq M\exp(9t/4-\pi e^t)\quad(t\geq0).
 \tag{3}
\]

Hence each of the four kernels is smooth, and C032f gives the
bounded Hankel realizations on the specified unweighted spaces.
For f in D, its support is a compact subinterval of (0,infinity).
For x in any compact positive interval, k(x+y) and its first two
x-derivatives are bounded on the relevant compact (x,y) rectangle.
This justifies differentiation under the compact integral and the
integrations by parts used by the imported identity. The input and
its derivatives vanish near both endpoints, so its boundary bracket
vanishes; no condition at infinity for an arbitrary input or joint
self-adjoint domain is used. The resulting commutator is smooth
locally in x. Thus even an equality initially asserted almost
everywhere for every compact input gives the same pointwise core
identity. The polynomial coefficients introduce no local singularity.

Only the two real a_sigma kernels will be used. Their incompatibility
already suffices for the four-kernel question; nothing about
self-adjointness or the value of c for b_sigma is needed.

### Undivided polynomial reduction

For x,y>0 with x!=y, put u=x+y. In (2), the three differences are

\[
 p(y)-p(x)=(y-x)(Au+B),\qquad p'(y)-p'(x)=2A(y-x),
 \qquad q(y)-q(x)=(y-x)(Cu+D_1).
\]

Every u>0 has a representation by distinct positive x,y
(for example x=u/3,y=2u/3). Dividing only by the nonzero y-x
shows that each of a_- and a_+ must satisfy, for every u>0,

\[
 W(u)k''(u)+2Ak'(u)-V(u)k(u)=0,
 \qquad W(u)=Au+B,\quad V(u)=Cu+D_1.
 \tag{4}
\]

We never divide by W or V. In particular zeros or identically zero
values of either coefficient, and constant q, have not been excluded.
The constant E cancels from the commutator, as required.

Set h=1/8. Substitute k(u)=e^{\sigma hu}F(u) into (4) and
divide by the strictly positive e^{\sigma hu}. This gives

\[
 W F''+(2A+2\sigma hW)F'
 +(h^2W+2\sigma hA-V)F=0\quad(\sigma=-1,+1).
 \tag{5}
\]

Subtracting the minus equation from the plus equation yields
4h(WF'+AF)=0. Since h!=0 and W'=A,

\[
 (W F)'=0\quad\hbox{on }(0,\infty).
 \tag{6}
\]

Thus WF is one constant on this connected interval. By (3),

\[
 |W(u)F(u)|\leq
 M(|A|u+|B|)(1+u)\exp(9u/4-\pi e^u)\longrightarrow0.
 \tag{7}
\]

Indeed e^u/u tends to infinity, so the negative term -pi e^u
dominates the linear exponent and the logarithm of this polynomial
factor. Therefore that constant is zero. Since F(u)>0 for every
u>0, WF=0 forces Au+B=0 at every positive u. Evaluating at two
distinct positive u gives A=B=0. Then p is identically zero,
contrary to p>0. This is the required contradiction.

For linear p this same proof uses A=0 and B!=0; (6) would force
F to be constant, and (7) forces it to vanish. Thus the linear
case is included explicitly, rather than obtained by a limit from
a monic quadratic. The argument uses neither a truncation nor a
derivative-tail asymptotic for Psi, only its proved full-density
positivity and value bound. It is an exact source specialization,
not a claim of a new general commutator theorem or progress beyond
the inspected literature on RH.

### Correctness audit — 17 November 2026, step1287

The invocation-start SPECIALIZE assessment was
`drafts/literature/2026-11-17-fixed-polynomial-commutant-obstruction-audit-review-1285.md`,
separately approved1286. This is a REPRODUCTION audit of the complete
statement above. The existing primary comparison1284 supplies Blower's
undivided identity, including its necessity on compact inputs; no
additional theorem or domain statement is imported.

**Identity and core.** Match source a=p,b=q. In the imported
L Gamma-Gamma L identity, the second-derivative coefficient is
p(y)-p(x), the first-derivative coefficient is p'(y)-p'(x), and
the zeroth-order coefficient is q(x)-q(y). Thus its signs agree
with (2), rather than its negative in only one term. For a fixed
compact input support and a compact positive x interval, all required
kernel derivatives are bounded by local smoothness. Both integrations
by parts have zero boundary bracket because f and f' vanish near
zero and infinity. This applies even when T Gamma f has only been
defined as a local differential expression, without asserting that
Gamma f lies in a closed operator domain or that T Gamma f is L2.
For each f, a commutator that vanishes almost everywhere in x and
is smooth in x vanishes everywhere. Fixing x then, the fundamental
lemma for all complex compact smooth f forces its continuous kernel
to vanish for every y. There is no need to intersect uncountably many
sets of full measure. Consequently the claimed necessary identity
has exactly the core scope used in the proof.

**Polynomial and tilt checks.** The three differences displayed
before (4) have a common factor y-x with the indicated coefficients.
Taking x=u/3,y=2u/3 covers every u>0 and avoids the diagonal.
No division by W or V occurs. For either sign,
k'=e^(sigma h u)(F'+sigma h F) and
k''=e^(sigma h u)(F''+2 sigma h F'+h^2 F).
These give (5), including the term 2 sigma h A F. Subtracting
the minus equation from the plus equation gives exactly
4h W F'+4h A F=0. Since W'=A and h=1/8 is nonzero, this is
(6). A common q, even a constant q, cancels completely. Separate
q choices would not be covered by this subtraction; they are not
among the stated hypotheses.

**Tail and degeneracies.** C032e (8) gives the full-density bound
(3) on all positive u, together with positivity and local
holomorphy; C032f (1)-(3) matches the original kernels and spaces.
For a finite constant C depending only on M,A,B, (7) is bounded
by C(1+u)^2 exp(9u/4-pi e^u). This tends to zero since
pi e^u-9u/4-2 log(1+u) tends to infinity. No assertion about
F' or F'' at infinity is used. A differentiable function with zero
derivative on the connected interval (0,infinity) is one constant,
so WF is identically zero. Positivity of F then implies W=0
pointwise, hence A=B=0. For A=0,B nonzero the same equation
reads B F'=0 and the same tail excludes a nonzero constant F.
For B=0,A nonzero it reads (Au F)'=0 and the same tail still
forces Au F=0. The case A=B=0 itself violates p>0. Constant
q and all possible zeros of W are therefore included without
any limiting normalization or omitted division case.

**Verdict and limits.** Accept the fixed-class rejection; no repair
was needed. Two real a_sigma already contradict the required common
identity, so the possibly complex c in the unused b_sigma introduces
no extra premise. C032e and C032f are the direct local inputs; the
DAG row is accurate and unchanged. This audit closes the correctness
question for this obstruction, not the source-metric, actual-range,
relative-output, signing, initialization or all-degree Xi gaps.
It supplies local verification of an existing source specialization,
not a new exclusion beyond the stated class or an RH candidate.

## Mathlib

Coverage of Blower's full compact-core commutator theorem and this
fixed-theta specialization was not checked; availability is unknown.
No absence claim, Lean verification, or numerical certificate is
asserted. The correctness audit1287 is an informal proof check, not
Mathlib verification. The supporting theta inputs
remain those qualified in C032e and C032f.
