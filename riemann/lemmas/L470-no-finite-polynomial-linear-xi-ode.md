# Lemma 470: the classical growth obstruction to polynomial linear Xi closure

## Hypotheses

Let xi and Xi be the entire functions of L018, with
Xi(z)=xi(1/2+iz). Let r>=1 be finite, and let p_0,...,p_r belong
to C[z], with p_r not identically zero. Derivatives are ordinary
complex derivatives, without factorial normalization.

No RH, simplicity, Laguerre–Polya membership or external zero-free
half-plane assumption is made.

## Conclusion

There is no identity

    sum_{j=0}^r p_j(z) Xi^(j)(z) = 0

on C. The same identity cannot hold on any nonempty open real interval.
Consequently an exact finite homogeneous polynomial-coefficient linear
height closure for actual Xi is unavailable. This is a specialization
of classical growth results, not a new growth theorem or a sign result.

## Proof

For a nonconstant entire function f, use the maximum modulus
M_f(R)=max_{|s|=R}|f(s)| and the conventions

    rho(f)=limsup_{R->infinity} log log M_f(R)/log R,
    tau(f)=limsup_{R->infinity} log M_f(R)/R^rho(f)

when 0<rho(f)<infinity. Normal type means 0<tau(f)<infinity;
infinite type means tau(f)=infinity. Replacing the circle by its
closed disk leaves M_f unchanged by the maximum modulus principle.
A nonzero constant factor changes log M_f only by a constant and
does not change positive finite order or its type.

We import these two precise source inputs, using their already reviewed
scope rather than reproving either growth assertion:

* G. Valiron, *Sur les fonctions entières vérifiant une classe
  d'équations différentielles*, Bulletin de la Société Mathématique
  de France **51** (1923), 33–45, [Proposition I, pp. 33–34, with
  the linear-case proof in §2, pp. 35–38](https://www.numdam.org/item/10.24033/bsmf.1030.pdf):
  a transcendental entire solution of a finite linear differential
  equation with rational-function coefficients and nonzero highest
  coefficient has positive finite rational order and normal type.
  Only this consequence is needed here. Polynomial coefficients
  are included. The theorem does not require a constant highest
  coefficient or forbid its isolated zeros. The transcendental
  qualification is essential: the conclusion is not asserted for
  polynomial solutions. F. Bornemann, *Accuracy and Stability of
  Computing High-Order Derivatives of Analytic Functions by Cauchy
  Integrals*, [arXiv:0910.1841v4, §8.1, Theorem 8.1 and its
  polynomial-coefficient footnote, printed p. 28](https://arxiv.org/pdf/0910.1841v4),
  corroborates this qualification and normal-type conclusion;
  Valiron's original linear proof is the primary input.
* J. C. Lagarias and E. Rains, *On a two-variable zeta function for
  number fields*, Annales de l'Institut Fourier **53**(1) (2003),
  1–68, [§4 opening, printed p. 23](https://www.numdam.org/item/10.5802/aif.1939.pdf),
  records that the classical completed function
  xi(s)=s(s-1)pi^(-s/2)Gamma(s/2)zeta(s)/2 has order one and
  infinite type. This is the xi statement in the opening discussion,
  not their Theorem 4.1's upper bound for a two-variable function.
  In the conventions above it gives rho(xi)=1 and
  limsup log M_xi(R)/R=infinity. L018 identifies exactly this
  normalization on Re(s)>1, and hence its entire extension is the
  same function by the identity theorem. In particular xi is
  transcendental entire: a nonconstant polynomial has order zero,
  whereas xi has order one.

Suppose the claimed Xi equation holds identically. For every j>=0,
the affine chain rule gives

    Xi^(j)(z)=i^j xi^(j)(1/2+iz).

Substitute z=-i(s-1/2). This produces the homogeneous equation

    sum_{j=0}^r q_j(s) xi^(j)(s)=0,
    q_j(s)=i^j p_j(-i(s-1/2)).

Every q_j is a complex polynomial. Because s |-> -i(s-1/2) is a
bijection of C and i^r is nonzero, q_r is not identically zero.
Thus this is a finite order-r equation in Valiron's permitted class.
One may divide by q_r away from its finitely many zeros to obtain
rational coefficients; those possible poles are allowed by the
cited theorem, and do not impose an extra zero-avoidance hypothesis
on the entire solution.

Valiron now gives xi normal type at its order. Since the second
source fixes that order to one, this would imply

    0 < limsup_{R->infinity} log M_xi(R)/R < infinity,

contrary to the infinite-type assertion. This proves nonexistence
of the entire identity. We transferred the differential equation
to xi directly, so no unproved invariance of type under a translated
center or change of growth order is needed.

Finally, the residual sum p_j Xi^(j) is entire by L018. If it vanishes
on a nonempty open real interval, its zeros have an accumulation
point in C. The identity theorem makes it identically zero on C,
which is the contradiction just established. This also explains why
isolated zeros of the highest polynomial do not evade the conclusion.

The argument excludes only the stated homogeneous polynomial linear
class. It gives no obstruction to arbitrary analytic coefficients,
inhomogeneous equations with unrestricted forcing, nonlinear equations
or difference systems, and supplies neither D_1 signs nor all-degree
mixed positivity. In particular it is not a disproof of RH. The cited
growth theorems are imported, not independently re-established here;
the source scope and proof-case inspection are recorded in
`drafts/literature/2026-10-26-xi-polynomial-ode-source-notes.md`.

The separate critical application audit on 2026-10-27 found no failed
implication in the source hypotheses, normalization, affine transfer
or interval extension; its complete replay is recorded in
`drafts/audits/2026-10-27-l470-critical-audit.md`. This validates the
stated application, not an independent reproof of the imported growth
theorems or a larger differential-equation class.

## Mathlib

Not checked. Availability of a full matching theorem excluding this
Xi ODE class, the imported normal-type theorem, and completed-xi
infinite type is unknown. Supporting affine chain rules, polynomial
composition and identity-theorem coverage have not been assessed here;
no absence claim is made. [Mathlib documentation](https://leanprover-community.github.io/mathlib4_docs/).
