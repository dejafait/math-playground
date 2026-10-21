# Lemma 412: positive fourth displacement at a half gamma-carrier turn

## Hypotheses

Use the fixed actual functions and gamma phase of L389/L390:

\[
 f=F_0/A,\qquad Q/A=R=e^{i\phi},\qquad A>0.
\]

Choose any smooth real lift phi on the eventual positive ray. For each
sufficiently large real t, define delta(t)>0 by

\[
 \phi(t+\delta(t))-\phi(t)=\pi.
\]

This is the phase of Q, with no response polynomial or Euler phase
added. All derivatives are ordinary real derivatives. No RH, sign
symmetry, nonvanishing zeta value or independent-phase hypothesis is
imposed. All constants and thresholds below are fixed and existential.

## Conclusion

As real H tends to infinity,

\[
 \frac1H\int_H^{2H}|f(t+\delta(t))-f(t)|^4\,dt
 =\frac{\pi^2-3}{\pi^4}(\log H)^4+O((\log H)^3).       \tag{1}
\]

In particular the coefficient is strictly positive, so this statistic
is not o((log H)^4). This stops the proposed scalar frozen-jet
implementation at an opposite gamma-carrier phase. It does not decide
the actual negative-Bcal clipped signed mean, establish derivative or
response-product displacement estimates, or rule out other pairings.
No actual-theta sign, zero-exclusion range or RH conclusion follows.
The separate step-132 critical audit below validates this local specialization.

## Proof

This is a **REPRODUCTION** under the prior SPECIALIZE assessment
`drafts/literature/2026-10-14-half-carrier-turn-displacement.md`.
The shifted moment theorem is imported, not reproved. The moving shift,
Hardy phases and complete coefficient must be checked because the cited
theorem states a constant-shift zeta product, not (1). No originality
beyond the sources checked is claimed.

**Imported input and normalization.** H. M. Bui and R. R. Hall,
*On the derivatives of Hardy's function Z(t)*,
[arXiv:2304.05178v1, Section 4.2, Proposition 3](https://arxiv.org/html/2304.05178v1#S4.SS2),
11 April 2023, give the following sharp constant-shift formula. Set
ell=log H. For four constant complex shifts of modulus at most C/ell,
where C is fixed,

\[
 \int_H^{2H}\prod_{j=1}^2
 \zeta(1/2+\alpha_j+it)\zeta(1/2+\beta_j-it)\,dt
 =\frac{H\ell^4}{2\zeta(2)}\mathcal I(\alpha,\beta)
       +O_C(H\ell^3),                                    \tag{2}
\]
\[
 \mathcal I=\int_{[0,1]^4}(u-v)^2
 \exp\bigl(-\ell(\alpha_1+\beta_1)u
           -\ell(\alpha_2+\beta_2)v
           +\ell(\alpha_1-\alpha_2)(u-v)r
           +\ell(\beta_1-\beta_2)(u-v)s\bigr)
       \,du\,dv\,dr\,ds.
\]

The uniform formula includes coincident shifts; no singular individual
residue terms are used. All shifts below have modulus at most 2pi/ell.
The same paper's Theorem 3 and its preceding defining asymptotic give
ordinary fixed-order Hardy fourth moments. L389 specializes the orders
zero and one and proves, without division by zeta, f=-sigma Z_Hardy
for one constant sigma in {1,-1}, including at critical zeros. Thus

\[
 \int_{H/2}^{3H}|f^{(j)}(t)|^4\,dt
       \ll H\ell^{4j+4}\quad(j=0,1).                     \tag{3}
\]

For (3), restrict the nonnegative integrals up to 3H in L389's imported
bound; log(3H) is comparable to ell. No source sign-density conclusion
or joint sign symmetry is imported. The completion's exact reflection,
also used in L389, gives at every real height on this ray

\[
 f(t)=-R(t)\zeta(1/2+it)
     =-R(t)^{-1}\zeta(1/2-it).                            \tag{4}
\]

This identity is valid when either side vanishes.

**Exact moving-shift replacement.** L390 gives
phi'(x)=log(2+x)/2+O(1) and phi''(x)=O(1/x). In particular phi is
strictly increasing on some eventual ray and tends to infinity. The
intermediate value theorem and strict monotonicity give the unique
delta(t)>0 in the hypotheses. For t in [H,2H], the derivative on
[H,3H] is ell/2+O(1), uniformly. It is at least ell/3 for H large,
so the phase increases by at least pi before an increment 3pi/ell.
Consequently delta(t)<=3pi/ell, and integration of the same derivative
estimate gives

\[
 \pi=\tfrac12\ell\delta(t)+O(\delta(t)),\qquad
 h:=2\pi/\ell,\qquad |\delta(t)-h|\le w:=C_0\ell^{-2}. \tag{5}
\]

The inverse function theorem also gives continuity of delta, so the
following integrands are measurable. Here and below H is sufficiently
large that every shifted height used lies in [H/2,3H]. Write

\[
 e(t)=f(t+\delta(t))-f(t+h),\qquad
 D_h(t)=f(t+h)-f(t).
\]

The fundamental theorem of calculus and Holder on the interval between
h and delta(t) imply the pointwise bound

\[
 |e(t)|^4\le w^3\int_{-w}^{w}|f'(t+h+v)|^4\,dv.
\]

Fubini for this nonnegative continuous integrand, followed by (3), yields

\[
 \int_H^{2H}|e(t)|^4dt
 \le 2w^4\int_{H/2}^{3H}|f'(x)|^4dx=O(H).              \tag{6}
\]

This uses a fixed enclosing strip, not a moving-supremum bound or a
change of variables by t+delta(t). Define the normalized L4 norm on
[H,2H] by ||g||_4=(H^(-1) integral |g|^4)^(1/4). By (3), constant
translation and the triangle inequality,

\[
 \|D_h\|_4=O(\ell),\qquad \|e\|_4=O(1),\qquad
 \|D_h+e\|_4=O(\ell).
\]

For real a,b, |a^4-b^4|<=4|a-b|(|a|+|b|)^3. Holder therefore gives

\[
 \left|\frac1H\int_H^{2H}
       \bigl(|D_h+e|^4-|D_h|^4\bigr)dt\right|
       =O(\ell^3).                                     \tag{7}
\]

The original sharp integration interval has been retained. The larger
interval in (3) and (6) is used only for absolute upper bounds; there
is no signed endpoint-strip subtraction or unaccounted Jacobian.

**All five constant-shift monomials.** Put

\[
 M_k=\int_H^{2H} f(t+h)^k f(t)^{4-k}\,dt
                   \quad(0\le k\le4).
\]

In (4), choose two positive-height zeta representations and two
negative-height representations among the four factors. Let a of the
two positive representations and b of the two negative ones occur at
t+h. Use the following choices:

| k | a | b | alpha_1 | alpha_2 | beta_1 | beta_2 |
|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 1 | 1 | 0 | ih | 0 | 0 | 0 |
| 2 | 1 | 1 | ih | 0 | -ih | 0 |
| 3 | 2 | 1 | ih | ih | -ih | 0 |
| 4 | 2 | 2 | ih | ih | -ih | -ih |

Each row has a+b=k. The four minus signs in (4) cancel, and the
remaining exact carrier factor multiplying the zeta product is

\[
 (R(t+h)/R(t))^{a-b}.
\]

Integrating phi'=ell/2+O(1) over the constant increment h shows
phi(t+h)-phi(t)=pi+O(ell^(-1)). Thus, uniformly in t and all five rows,

\[
 (R(t+h)/R(t))^{a-b}=(-1)^k+O(\ell^{-1}).             \tag{8}
\]

The parity follows from a+b=k; it is not an assumed sign relation
between actual f values. The absolute integral of each zeta product
is O(H ell^4), by four-factor Holder and (3), since |R|=1 on the real
ray. Therefore replacing its carrier by (-1)^k costs O(H ell^3),
even though the original monomial can have either sign. Applying (2)
then gives

\[
 M_k=\frac{H\ell^4}{2\zeta(2)}(-1)^k J_k
                   +O(H\ell^3),                        \tag{9}
\]

where J_k is the source integral for its row. There is no height shift
of the sharp interval in this application: all offsets are constant
parameters inside (2).

**Exact source-integral evaluation.** Set q=ell h=2pi and d=u-v.
For rows 0 and 4 all exponential factors in the source integral cancel,
so

\[
 J_0=J_4=\int_0^1\int_0^1(u-v)^2du\,dv=1/6.          \tag{10}
\]

For row 1 the only nontrivial exponential factors are
exp(-iqu)exp(iqdr). After integrating r, and trivially s, their product
with d^2 is

\[
 \frac{d}{iq}(e^{-iqv}-e^{-iqu}).
\]

This expression has its continuous value at d=0. Since

\[
 \int_0^1e^{-iqu}du=0,\qquad
 \int_0^1u e^{-iqu}du=-\frac1{iq},
\]

its double integral is (1/(iq))(2/(iq))=-2/q^2. For row 3 the
nontrivial factors are exp(-iqv)exp(-iqds). Integrating s gives
exactly the same expression d(e^(-iqv)-e^(-iqu))/(iq). Hence

\[
 J_1=J_3=-2/q^2.                                        \tag{11}
\]

For row 2 the factors are exp(iqdr)exp(-iqds), with the two other
exponents zero. Integrating r and s gives

\[
 d^2\left|\int_0^1e^{iqdr}dr\right|^2
       =\frac{2-2\cos(q(u-v))}{q^2}.
\]

The double integral of cos(q(u-v)) is
|integral_0^1 exp(iqu)du|^2=0. Consequently

\[
 J_2=2/q^2.                                             \tag{12}
\]

All these are finite continuous integrals; no infinite-sum interchange
or limiting evaluation at a singular shift is involved. Equations
(9)--(12) give the five complete real leading coefficients:

\[
 \frac{M_k}{H\ell^4}
       =\frac1{12\zeta(2)}+O(\ell^{-1})\quad(k=0,4),
 \qquad
 \frac{M_k}{H\ell^4}
       =\frac1{q^2\zeta(2)}+O(\ell^{-1})\quad(k=1,2,3).
                                                               \tag{13}
\]

In particular the negative J_1,J_3 are accompanied by negative Hardy
carrier factors; dropping these phases would change the answer.

Since f is real, |D_h|^4=D_h^4. Expand every binomial term:

\[
 \int_H^{2H}|D_h|^4dt=M_4-4M_3+6M_2-4M_1+M_0.
\]

Its coefficient is therefore

\[
 \frac1{6\zeta(2)}-\frac2{q^2\zeta(2)}
 =\frac1{\pi^2}-\frac3{\pi^4}
 =\frac{\pi^2-3}{\pi^4}>0,                             \tag{14}
\]

using q=2pi and Euler's zeta(2)=pi^2/6. Combining the O(H ell^3)
error in this calculation with (7) proves (1), for every sufficiently
large real H. Positivity in (14) is exact, not a decimal certificate.

The required threshold was little-o(ell^4); the established value has
a fixed positive coefficient at ell^4. This invalidates the specific
scalar-small-displacement premise. L411's absolute clipping transfer
and L405's unclipped benchmark are downstream motivation only and are
not mathematical premises of this proof. The failure supplies neither
a clipped-sign conclusion nor a global obstruction to other routes. ∎

### Separate critical audit — 2026-10-14, step 132

This is a REPRODUCTION proof audit under the unchanged prior SPECIALIZE
assessment `drafts/literature/2026-10-14-half-carrier-turn-displacement-audit.md`.
The conclusion, hypotheses and direct inputs L389/L390 are unchanged.
The following checks independently validate the specialization; they do
not reprove the imported analytic number theory theorem.

**Source and actual function.** Direct comparison with Bui--Hall v1
Section 4.2, Proposition 3, confirms exactly (2): the two positive and
two negative height factors, prefactor 1/(2 zeta(2)), sharp [H,2H]
interval, uniform complex shifts O(1/log H), and O(H log^3 H) error.
The continuous four-dimensional formula includes repeated shifts. Its
proof is omitted there by reference to the preceding derivation; this
audit imports the stated theorem, without claiming an independent proof
of it. Theorem 3's defining cumulative asymptotic and Section 7 cover
ordinary derivative orders zero and one. Restricting their nonnegative
pure fourth powers from [0,3H] proves (3) for all large real H.

In L389, Q=(t^2+1/4)Gamma(1/4+it/2)pi^(-1/4-it/2).
Its positive polynomial multiplier has no phase. Thus R squared equals
the Hardy phase squared; continuity makes the quotient one constant
sign on the ray. The exact completion identity gives f=-R zeta(1/2+it),
and conjugating this real identity gives the second orientation in (4).
Neither step divides by a zeta value. Zeros cause no exceptional case.
L390's exact phase formula is
phi'=Re Psi(1/4+it/2)/2-(log pi)/2; its stated Stirling bound gives
phi'=ell/2+O(1) uniformly on [H,3H]. No response Euler phase is present.

**Moving shift and endpoints.** On a fixed eventual ray phi'>0 and
phi tends to infinity. Its inverse defines
delta(t)=phi^(-1)(phi(t)+pi)-t, continuously and uniquely. For large H,
3pi/ell stays inside [H,3H] from every t in [H,2H], and phi'>=ell/3
there. Integration bounds delta by 3pi/ell and then gives
|delta-h|<=C_0 ell^(-2), with C_0 independent of t,H.
For w=C_0 ell^(-2), the interval in the fundamental theorem of calculus
has length at most w, so its fourth-power Holder factor is w^3.
Tonelli followed by translation gives, explicitly,

    integral_H^(2H) integral_(-w)^w |f'(t+h+v)|^4 dv dt
      <=2w integral_(H/2)^(3H) |f'(x)|^4 dx.

Hence the normalized fourth power of the error is O(w^4 ell^8)=O(1).
The normalized fourth norms of both displacements are O(ell).
Holder with exponents 4 and 4/3 then bounds their fourth-moment
difference by O(ell^3). All constants have one common eventual onset.
Only absolute upper bounds use the enclosing interval; neither a
moving-variable Jacobian nor a signed endpoint subtraction is needed.

**Every phase and coefficient.** For a shifted positive and b shifted
negative factors, the exponents of R(t+h) and R(t) are a-b and b-a.
For the five displayed rows, a-b is respectively 0,1,0,1,0. Their
leading carriers are therefore 1,-1,1,-1,1, with uniform error O(1/ell).
Four-factor Holder and (3) bound every absolute zeta product by
O(H ell^4), including the odd monomials. Thus phase replacement has
absolute error O(H ell^3), without assuming a sign relation between
values of f at the two heights.

To check the finite integrations independently, write
A_q=integral_0^1 exp(-iqu)du=0 and
B_q=integral_0^1 u exp(-iqu)du=-1/(iq), for q=2pi.
In each odd row integration in the nontrivial auxiliary variable
leaves d(exp(-iqv)-exp(-iqu))/(iq). Its remaining integral is
(-2B_q)/(iq)=-2/q^2. For the middle row the two auxiliary integrals
are conjugates; multiplication by d^2 leaves
(2-2cos(qd))/q^2. The cosine integral is |A_q|^2=0, giving 2/q^2.
The endpoint rows give 1/6. These formulas extend continuously across
d=0, and there is no singular residue limit. After the carrier signs,
the five coefficients are exactly those in (13). Their binomial sum is

    2/(12 zeta(2)) + (-4+6-4)/(q^2 zeta(2))
      =(pi^2-3)/pi^4>0.

Each of the five source errors and phase errors is O(H ell^3); their
finite sum and the moving-shift error therefore have the claimed order.
This validates (1) for every sufficiently large real H, with fixed
existential constants. No missing endpoint, phase or uniformity defect
was found. The target little-o(ell^4) premise fails, but the audit says
nothing about derivative displacements, a pairing retaining changed
jets, or the signed clipped mean. It establishes no new source theorem
or progress beyond the checked literature.

## Mathlib

Full matching coverage of the shifted Hardy fourth moment and (1) is
**not checked**. The proof imports Bui--Hall Proposition 3 and the
ordinary fourth-moment bounds cited above. Unknown Mathlib coverage
is not evidence of absence. The finite integrations, Holder, Fubini
and elementary polynomial identities are supporting steps, not a
replacement for the imported analytic number theory theorem.
