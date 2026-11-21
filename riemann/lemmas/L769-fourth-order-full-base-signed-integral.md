# Lemma 769: a fourth-order full-base signed integral and uniform lower factor

## Hypotheses

Let u>=0 and let m>=7 be an integer. For v>=0 put

\[
 x(v)=\pi e^{2v},\quad c=3/2,\quad
 H(v)=8\pi e^{5v/2-x(v)},\quad
 B(v)=H(v)(x(v)-c),\quad F_0(v)=H(v)x(v).
\]

Thus B is the complete first summand of L019's K, whereas F_0 is
only its leading exponential term. Define, with the original factorial,

\[
 C_m(F;u)=\frac1{(m-1)!}\int_0^\infty t^{m-1}F(u+t)\,dt,
 \qquad S_{4,m}(F;u)=\det[\partial_u^{i+j}C_m(F;u)]_{i,j=0}^3.
\]

The usual signed factor is (-1)^6=1. For four real variables let e_k
be the elementary symmetric polynomial of degree k, with e_0=1,
and let Delta(z)=prod_(i<j)(z_j-z_i). In an integral below write
v_j=u+t_j, x_j=x(v_j), H_j=H(v_j), and

\[
 P(x_1,x_2,x_3,x_4)
 =e_4-\frac32e_3+\frac{15}4e_2-\frac{105}8e_1+\frac{945}{16}.
\]

## Conclusion

There is an exact, absolutely convergent representation

\[
 S_{4,m}(B;u)=\frac{2^6}{\prod_{i=0}^3(m-1-i)!}
 \int_{0<t_1<t_2<t_3<t_4}
 \left(\prod_{j=1}^4 t_j^{m-4}H_j\right)
 \Delta(t)\Delta(x)P(x)\,dt_1\cdots dt_4.                 \tag{1}
\]

Replacing P by prod_j x_j gives exactly S_(4,m)(F_0;u). In particular,
uniformly over the stated integer m and real u,

\[
 S_{4,m}(B;u)>\frac{19}{72}S_{4,m}(F_0;u)>0.             \tag{2}
\]

This is a signed-base result only. It supplies no effective M4 for
the complete-K relative error<1/2, no general-order theorem, no
exceptional coefficient transfer, and no RH conclusion. The step401
conceptual audit below accepts this signed-base statement; the finite
algebra check alone is not that review.

The unsmoothed polynomial-base determinant structure is known precedent:
John Nuttall, *Basic Wronskians in the Riemann Hypothesis*, author report,
Theorem3.1, Section3/(3.2)–(3.12), printed pp.5–6,
https://publish.uwo.ca/~jnuttall/basicRH.pdf.
The cumulant determinant-integral method is also used in Nuttall,
*Cumulants, the Riemann Hypothesis, and Similar Problems*, author
manuscript, Sections4.2–4.3, pp.9–12,
https://publish.uwo.ca/~jnuttall/cumanal_a.pdf.
These are method comparisons, not assumptions of a conjectured sign.
The prior source assessments did not supply (2) with this full B,
factorial normalization, and explicit uniform factor. The calculation
below specializes the polynomial structure and spells out the exact
integral and constant for the approved comparison. It is not presented
as a new determinant mechanism or an originality claim.

## Proof

### Differentiation and the integral determinant

Every derivative of B or F_0 is an exponential factor times a
polynomial in x(v). Consequently it has faster-than-exponential decay
as v tends to infinity; all polynomially weighted integrals used below
converge. On each compact u-interval these same estimates dominate the
derivatives. L019 gives the corresponding exact kernel normalization.

Differentiate the shifted integral and integrate by parts i times.
For 0<=i,j<=3, the infinity boundary vanishes by that decay, and
the zero boundary vanishes because m-1-i>=3. This proves

\[
 \partial_u^{i+j}C_m(F;u)
 =\frac{(-1)^i}{(m-1-i)!}
   \int_0^\infty t^{m-1-i}F^{(j)}(u+t)\,dt.             \tag{3}
\]

Expanding the determinant and applying Fubini gives the usual
Andreief integration identity: the determinant of the integrals in
(3) equals 1/4! times the integral of the product of their two
four-by-four evaluation determinants. This identity follows directly
by expanding both determinants: permutation of the four integration
variables identifies the 4! equal copies of the determinant expansion.
All such integrals are absolutely convergent by the bounds just given.

The row signs in (3) multiply to (-1)^6=1. Reversing the four rows
of [t_l^(m-1-i)] has the same sign, so its determinant is
prod_l t_l^(m-4) Delta(t). Thus

\[
 S_{4,m}(F;u)=\frac1{4!\prod_{i=0}^3(m-1-i)!}
 \int_{(0,\infty)^4}
 \left(\prod_l t_l^{m-4}\right)\Delta(t)
 \det[F^{(j)}(u+t_l)]_{j=0,\ldots,3;\ l=1,\ldots,4}\,dt. \tag{4}
\]

### Exact full-polynomial factor

Let T=x d/dx-x and q_j=T^j(x-c). Differentiation of H(v)p(x(v))
gives H(v)(5/2+2T)p. A triangular change of the derivative rows
therefore replaces (5/2+2T)^j by (2T)^j, with determinant one.
Factoring the row factors 2^j gives

\[
 \det[B^{(j)}(v_l)]_{j,l}=2^6\left(\prod_l H_l\right)
                              \det[q_j(x_l)]_{j,l}.     \tag{5}
\]

The four polynomials, in ascending derivative order, are

\[
\begin{aligned}
 q_0&=x-3/2,\\
 q_1&=-x^2+(5/2)x,\\
 q_2&=x^3-(9/2)x^2+(5/2)x,\\
 q_3&=-x^4+(15/2)x^3-(23/2)x^2+(5/2)x.
\end{aligned}
\]

Expand their coefficient determinant in the five monomial degrees
0,1,2,3,4. Omitting degree k from those five gives the alternant
Delta(x)e_(4-k)(x). One way to verify this elementary identity is
to expand the five-by-five Vandermonde on x_1,...,x_4,z in its last
column and compare powers of z with Delta(x)prod_l(z-x_l).
The corresponding four-by-four coefficient minors are:

| Omitted degree k | 0 | 1 | 2 | 3 | 4 |
|---|---:|---:|---:|---:|---:|
| Coefficient minor | 1 | -3/2 | 15/4 | -105/8 | 945/16 |

Hence det[q_j(x_l)]=Delta(x)P(x), including coincident variables by
polynomial continuity. Substitution in (4) proves (1): the integrand
is symmetric in the t_l, since the two Vandermondes change sign
together, and the 4! ordered regions cancel the prefactor 1/4!.

For F_0 replace q_j by T^j x. Dividing each column by x_l leaves
polynomials of degrees 0,1,2,3 with leading coefficients 1,-1,1,-1.
Their product is 1, so their evaluation determinant is Delta(x).
This proves the assertion about S_(4,m)(F_0;u).

### A lower factor valid at every height and smoothing order

Set y_l=x_l-3>=0, using pi>3. Expansion of P gives

\[
 P(x)=e_4(y)+\frac32e_3(y)+\frac{15}4e_2(y)
                    +\frac{57}8e_1(y)+\frac{369}{16},
\]
\[
 \prod_lx_l=e_4(y)+3e_3(y)+9e_2(y)+27e_1(y)+81.
\]

In particular the exact difference is

\[
 P(x)-\frac{19}{72}\prod_lx_l
 =\frac{53}{72}e_4(y)+\frac{17}{24}e_3(y)
                         +\frac{11}8e_2(y)+\frac{27}{16}>0. \tag{6}
\]

On the ordered integration region all t_l and H_l are positive,
and x_l increases strictly with t_l. Both Vandermondes are therefore
strictly positive there. Equation (6), integrated in (1), proves
(2), including strict positivity of its reference integral. All
constants and identities are independent of m and u; there is no
pointwise-asymptotic inference of uniformity.

### Exact location of the remaining complete-theta problem

For comparison only, define

\[
 f_j(x)=\sum_{n\ge1} n^2 e^{-(n^2-1)x}q_j(n^2x),
 \quad j=0,1,2,3,
 \qquad E(x_1,\ldots,x_4)=\det[f_j(x_l)]-\Delta(x)P(x).
                                                               \tag{7}
\]

Indeed L019's nth summand is
H(v)n^2 e^{-(n^2-1)x(v)}(n^2x(v)-c). The same triangular row
calculation as (5), now with T acting on each exponential factor,
gives det[K^(j)(v_l)]=2^6 prod_l H_l det[f_j(x_l)].
Termwise differentiation and integration are valid: for any fixed
derivative order each summand is bounded by a fixed polynomial in
n and x times exp(5v/2-n^2x); for x>=pi the n-series and its
derivatives converge locally uniformly, and summing their polynomial
majorants leaves an integrable, faster-than-exponential v-tail.
This also justifies (3)–(4) for K, up to the six derivatives required.

With W_m(t;u)=prod_l(t_l^(m-4)H_l) Delta(t)>0, the exact relative
error is thus

\[
 \frac{|S_{4,m}(K;u)-S_{4,m}(B;u)|}{S_{4,m}(B;u)}
 =\frac{\left|\int_{t_1<\cdots<t_4}W_m E(x)\,dt\right|}
        {\int_{t_1<\cdots<t_4}W_m\Delta(x)P(x)\,dt}.       \tag{8}
\]

For example, a sufficient condition for the desired <1/2 would be
an absolute numerator bound strictly below
(19/144) integral W_m Delta(x) prod_l x_l. No such bound is proved
here. Although the scalar theta summands are positive, the q_j have
mixed signs; that scalar positivity does not sign E or control (8).
In particular the regions with some small x_l and others large, and
their m-dependent weights, are not estimated by this signed-base
argument alone.

### Finite algebra evidence and its limits

Run `python3 scripts/cumulant-comparison/fourth-order-polynomial-399.py`.
It computes the five coefficient minors and every coefficient in
(6) using exact rational arithmetic, recording them in
`scripts/cumulant-comparison/fourth-order-polynomial-399.json`.
The general determinant identity and integral justification are the
proof above, not the script's extra sample evaluation.

The separate `scripts/cumulant-comparison/fourth-order-local-diagnostic-399.json`
contains noncertified finite-sum evaluations at four coalescing-point
locations. Its rounding and omitted theta terms are not enclosed.
It is not evidence for (2), a proof of (8)<1/2, or a certificate of
any smoothing onset; no conclusion of this lemma depends on it.

### Critical review — 2026-11-04, step401

Accepted for every integer m>=7 and u>=0 after a separate conceptual
audit of the stated comparison. The normalization was checked directly:
L019's first term is H(x-3/2), and the leading term is Hx. In (3)
every zero-boundary exponent encountered during the i integrations
by parts is positive; the final exponent m-1-i is at least three.
The shifted-integral derivatives at u=0 are understood as right
derivatives, justified by the same compact domination. Thus no
origin boundary or endpoint hypothesis is missing. The determinant
transpose in the integral identity changes no sign, and both the
row signs and the reversed monomial rows have sign (-1)^6=1.
Absolute integrability justifies the finite determinant expansion
and Fubini before restriction to the ordered chamber.

The recurrence Tq_j=q_(j+1), all five coefficient minors, the shifted
polynomial and the coefficientwise 19/72 comparison were checked.
Replaying `scripts/cumulant-comparison/fourth-order-polynomial-399.py`
reproduced the exact coefficients. In (6) the strictly positive
constant 27/16 supplies strictness even where the linear coefficient
vanishes. Both Vandermondes and all remaining factors are positive
on the open ordered chamber, which has positive measure; hence the
reference integral is strictly positive as well as finite.

For the complete-theta identity (7), putting a=n^2-1 gives exactly
T_x[e^(-ax)q_j(n^2x)]=e^(-ax)q_(j+1)(n^2x). The factor n^2 is
unchanged. For each required derivative, the remaining n-polynomials
are summable against e^(-pi n^2), uniformly on compact v-intervals,
and the v-tail has an integrable exponential majorant. This checks
the infinite series and integration operations in (7)–(8), without
assigning a sign to the error determinant.

No repair to the statement, proof identities or mathematical inputs
was needed. The old certificate's unresolved complete-theta flag
describes the limited scope of that polynomial check; it is preserved
as historical evidence, not treated as a failed algebra check. This
audit establishes a local input, not a result beyond the sources
checked or a claim about arbitrary order.

## Mathlib

Full-statement coverage and supporting determinant-integration,
symmetric-polynomial and special-function coverage were not checked.
Availability is unknown, not established absent. The proof is an
informal finite-algebra and dominated-integration argument; no Lean
verification or Mathlib theorem import is claimed.
