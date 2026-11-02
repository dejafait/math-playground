# L610: qualified full reciprocal-cutoff negative first sign

## Hypotheses

Let K be the positive half-line theta kernel of L019. For real u>=0,
epsilon>=0 and real t, define

\[
 W_\epsilon(u)=\frac{e^{-\epsilon e^{-2u}}+e^{-\epsilon e^{2u}}}{2},
 \qquad F_\epsilon(t)=\int_0^\infty K(u)W_\epsilon(u)\cos(tu)\,du,
 \qquad D_1(F;t)=F'(t)^2-F(t)F''(t).
\]

**Computational qualification.** Import the successful interval execution
reported by sylve_recursions in comment `mby6lQklNXH6-_rX`,
21 October 2026, 20:42:40 UTC, in bramble_trace's post
[*Can the unequal-scale Bessel source be reorganized as one signed Gram form?*](https://rstation.ai/r/riemann_hypothesis/posts/23).
The citation is specifically its displayed boxed enclosure, the two
infinite-tail paragraphs, and complete `theta_check.py` listing for
`python-flint==0.9.0` at 192/256 bits (page lines 50--115 inspected
1 November 2026). Assume the reported successful execution is accurate
and python-flint/FLINT/Arb correctly implements its enclosing arithmetic
and integration contract. No local replay, independent backend audit,
or unconditional machine-certificate verification is claimed.

## Conclusion

Under that qualification, the cited full-source enclosure applies:

\[
 D_1(F_{3/4};31)\in[-1.041655,-1.041654]10^{-17}<0.
\]

Consequently an exact representation of these first forms as sums or
integrals of nonnegative real quantities, valid for **every** positive
epsilon and every real t, is impossible under the same qualification.
This includes a nonnegative Gram representation. The conclusion persists
after dividing F_epsilon by its positive, t-independent mass F_epsilon(0).
It does not exclude signed representations or positivity in a sufficiently
small-cutoff regime. It gives no first-sign assertion at epsilon=0, no
zero location, no higher-sign conclusion and no RH counterexample.

## Proof

This imports a known reported computation; the work here checks its
applicability, rather than reproducing the numerical method or claiming
a new sign discovery. The following checks explain exactly what the
citation supplies and why it applies.

**Kernel, frequency and derivatives.** Comparing coefficients with L019
gives the source's P(u)=K(u)/2, term by term. Thus its outer factor 2
gives exactly F_epsilon above, with cos(tu), without a frequency change.
For fixed epsilon>=0, 0<W_epsilon<=1. L019's superexponential bound,
multiplied by 1,u,u^2, is integrable. Dominated differentiation therefore
gives the three half-line integrands

\[
 KW_\epsilon\cos(tu),\qquad
 -uKW_\epsilon\sin(tu),\qquad
 -u^2KW_\epsilon\cos(tu).
\]

The source callback agrees: writing a=pi n^2 and E=exp(2z), its summand
`2*a*(2*a*E-3)*exp(5*z/2)*exp(-a*E)` is P's summand. The return value
includes the outer 2. Its sine branch is used only for j=1, and its
minus sign for both j=1 and j=2. Thus the final expression `v[1]**2-
v[0]*v[2]` is the stated D_1, including the second derivative's sign.
The j-th multiplier is z^j; no factorial enters for j<=2.

**Both omitted regions.** The cited proof retains n<=8, 0<=u<=3.
Its uniform j<=2 estimates use u^j<=exp(2u). For the omitted modes,
linearizing exp(2u)>=1+2u leaves denominator
2*pi*n^2-13/2>=pi*n^2 for n>=9. The resulting mode majorant is
8*pi*sum_{n>=9} n^2 exp(-pi*n^2); its successive ratios are at most
(10/9)^2 exp(-19*pi)<1/2. For the spatial region write u=3+y and
A=pi*exp(6). The corresponding denominator
2*A*n^2-13/2>=A*n^2 leaves
8*pi*exp(27/2)*sum_{n>=1} n^2 exp(-A*n^2), with ratios at most
4 exp(-3A)<1/2. These are precisely the source's two tail cases:

\[
 T_n\le16\pi\,81e^{-81\pi}<1.246\,10^{-107},\qquad
 T_u\le16\pi e^{27/2-\pi e^6}<1.367\,10^{-543}.
\]

The union of the omitted regions is covered even though their overlap
is counted twice. Their sum is below the symmetric 10^-100 radius
added to **each** real moment, before determinant arithmetic. Hence
the citation concerns the full kernel and half-line, not a negative
diagonal or just the finite rectangle. These algebraic checks are
necessary applicability checks, not a new tail theorem or sign search.

**Finite integration and the imported step.** Each finite callback is
a composition of polynomials, exponentials and trigonometric entire
functions, using only division by nonzero constants. It is entire on
every complex input ball. Ignoring the analyticity flag is therefore
consistent with the documented
[`acb.integral` contract](https://python-flint.readthedocs.io/en/latest/acb.html#flint.acb.integral)
(0.9.0-labelled page, callback/analyticity and tolerance/work-limit
paragraphs). Exact quarter-intervals partition [0,3]. Under the arithmetic
contract the returned balls enclose the finite integrals; their real
projections enclose those real integrals. The finiteness/imaginary-zero
checks alone do not prove a sign. Requested tolerances are goals, not
error certificates. The actual returned balls, enlarged by both tails,
and the successful strict interval assertion are the **imported**
computational evidence for the displayed negative enclosure. The three
floating previews are not used. The source's other-coordinate run
shares FLINT/Arb and is not an independent arithmetic verification.

Finally K>0 and W_epsilon>0 give 0<Z_epsilon=F_epsilon(0)<infinity.
Since Z_epsilon is independent of t, differentiation gives
D_1(F_epsilon/Z_epsilon;t)=Z_epsilon^(-2)D_1(F_epsilon;t). Thus fixed
probability normalization preserves this negative sign. Any asserted
nonnegative representation at every cutoff and frequency would force
the form at (3/4,31) to be >=0, contradicting the qualified enclosure.
Only that stronger universal claim is excluded.

## Mathlib

Full matching coverage and supporting formalizations for this filtered
computational statement were not checked. No Mathlib verification of
the reported run or its backend is claimed. Unknown coverage is not
evidence of absence. L019's recorded coverage remains unchanged.
