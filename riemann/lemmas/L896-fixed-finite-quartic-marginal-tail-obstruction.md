# Lemma 896: fixed finite quartic marginals cannot equal the theta law

## Hypotheses

Fix an integer n>=1 and finite real parameters a_i>0, b_i, and
J_ij>=0 for 1<=i<j<=n. On R^n set

    E(phi)=sum_i a_i phi_i^4 + sum_i b_i phi_i^2
           - sum_(i<j) J_ij phi_i phi_j,
    Z=integral_(R^n) exp(-E(phi)) dphi.

There is no field or singular constraint. Let w_i>=0 be finite and
not all zero, and set X=sum_i w_i phi_i under the probability density
Z^(-1) exp(-E). Every parameter and n is fixed as t tends to infinity.

Let K be the full theta kernel of L019, and M_0=integral_0^infinity K(u)du
as in L021. Define the probability measure nu on R by the density
K(|u|)/(2M_0).

## Conclusion

The normalization satisfies 0<Z<infinity. There exist model-dependent
c,C>0 such that for every t>=0,

    P(X in [t,t+1]) >= c exp(-C(1+t)^4).

There is a finite A_theta>0 such that for every t>=0,

    nu([t,t+1]) <= A_theta exp(9t/2 - pi exp(2t)).

In particular nu([t,t+1])/P(X in [t,t+1]) tends to zero as t tends to
infinity, and the law of X cannot equal nu. This includes n=1, zero
couplings, disconnected graphs, and observables with exactly one
nonzero weight. Constants are not uniform across models. No claim is
made about dimension-growing or parameter-varying weak limits.

## Proof

**Normalization.** Put J_ji=J_ij and J_ii=0 for this paragraph, and set

    d_i=|b_i| + (1/2) sum_(j!=i) J_ij,
    D=sum_i d_i^2/(2a_i).

The inequality |phi_i phi_j|<=(phi_i^2+phi_j^2)/2 gives

    E(phi) >= sum_i (a_i phi_i^4-d_i phi_i^2)
           >= (1/2) sum_i a_i phi_i^4 - D.

For the second inequality complete the square in y=phi_i^2:
(a_i/2)y^2-d_i y >= -d_i^2/(2a_i). Consequently

    Z <= exp(D) product_i integral_R exp(-a_i x^4/2) dx < infinity.

Each one-dimensional integral is finite: on |x|>=1 its integrand is
at most exp(-a_i x^2/2), and on [-1,1] it is bounded by 1. Tonelli's
theorem applies to these nonnegative functions. Positivity of Z follows
by integrating the continuous strictly positive integrand over any
compact box of positive volume. This also establishes the existence of
the stated probability measure without relying on a ferromagnetic
construction theorem.

**Fixed box.** Choose k with w_k>0 and put

    W=sum_i w_i >0,  delta=1/(4W),  B=1/w_k+delta.

For t>=0 define a closed box Q_t by

    |phi_k-(t+1/2)/w_k|<=delta,
    |phi_i|<=delta for every i!=k.

Its Lebesgue volume is (2delta)^n. For every phi in Q_t,

    |X-(t+1/2)| <= sum_i w_i delta = 1/4.

Thus Q_t is contained in the inverse image of [t,t+1]. Also, for every
coordinate on this box,

    |phi_i| <= B(1+t).

Indeed the k-th coordinate is at most (t+1/2)/w_k+delta
in absolute value, which is at most B(1+t); all other coordinates
are bounded by delta<=B(1+t). Define the finite positive constant

    C=B^4 sum_i a_i + B^2 (sum_i |b_i| + sum_(i<j) J_ij).

Taking absolute values of each quadratic and coupling contribution,
and using (1+t)^2<=(1+t)^4, gives on Q_t

    E(phi) <= C(1+t)^4.

It follows directly by integration that

    P(X in [t,t+1])
      >= Z^(-1) integral_(Q_t) exp(-E(phi)) dphi
      >= ((2delta)^n/Z) exp(-C(1+t)^4).

This proves the lower bound with c=(2delta)^n/Z>0. Empty sums cause
no problem when n=1, and the construction never divides by a zero
weight or requires positive couplings. In particular it covers the
single-nonzero-weight case without a marginal-density formula.

**Full-theta comparison.** L021 gives 0<M_0<infinity, so nu is a
probability measure. Use the full estimate in the proof of L019:
there is a finite H>0 with

    0<K(u)<=H exp(9u/2-pi exp(2u))  for u>=0.

For u in [t,t+1] with t>=0 this is at most
H exp(9(t+1)/2-pi exp(2t)). Integrating over an interval of length one
and dividing by 2M_0 gives the asserted upper bound with
A_theta=H exp(9/2)/(2M_0). This uses the quantitative full-kernel
envelope, not merely decay faster than every fixed exponential;
the latter property alone would not establish this comparison.

Combining the two bounds yields

    0 <= nu([t,t+1])/P(X in [t,t+1])
       <= (A_theta/c)
          exp(C(1+t)^4+9t/2-pi exp(2t)).

The exponent tends to minus infinity. Explicitly, for t>=1 its
positive part is at most (16C+9/2)t^4, while the power series of the
exponential gives exp(2t)>=(2t)^6/6!. The negative sixth-degree term
therefore dominates this fourth-degree upper bound. The ratio tends
to zero, so equality of the two laws (which would make this ratio
one for every t) is impossible.

This is a fixed-model obstruction only. The constants c,C and the
comparison onset may deteriorate with n, weights, or model parameters.
No uniform estimate has been established that could pass to a sequence
of models. Thus it supplies neither a restriction on arbitrary
Griffiths-Simon weak limits nor a zero-location or mixed-sign result
for Xi. The known Lee-Yang and quartic approximation theorems are not
mathematical premises of this proof.

### Independent audit — 7 November 2026, step100

The approved audit was replayed from the stated hypotheses and full
L019/L021 proofs, with L016 inspected for the quantitative envelope.
No correction to the statement or proof is required.

Each coupling contributes at worst -J_ij(phi_i^2+phi_j^2)/2, and
b_i phi_i^2>=-|b_i|phi_i^2. Thus d_i has exactly the required coefficient.
Minimizing (a_i/2)y^2-d_i y gives -d_i^2/(2a_i), confirming D even
when b_i<0. The quartic product majorant is integrable; positivity on
a compact box proves Z>0 independently of that upper bound.

The box center has observable t+1/2, and the maximal observable error
is W delta=1/4, including zero weights. Its volume is (2delta)^n;
for n=1 this is an interval of positive length. A single nonzero weight
still permits the same box in all coordinates. B(1+t) controls every
coordinate. Taking absolute values gives an upper bound for E, hence
a lower bound for exp(-E). No coupling is divided by or required to be
positive. Empty sums and disconnected graphs satisfy the same argument.

L016 supplies finite C_1,C_2 with |psi'(x)|<=C_1 exp(-pi x) and
|psi''(x)|<=C_2 exp(-pi x), x>=1. The full formula in L019 permits
H=12C_1+8C_2 in its envelope, since exp(5u/2)<=exp(9u/2) for u>=0.
L019 gives positivity and L021 gives 0<M_0<infinity. Reflection doubles
the half-line integral, so the stated density has mass one. Both
interval estimates hold for all t>=0, with strictly positive denominator.
For t>=1 the ratio exponent is at most

    (16C+9/2)t^4 - (64pi/720)t^6,

which tends to minus infinity for each fixed C. Equality of laws would
instead make the ratio one. This checks the full kernel, not a truncated
series. Constants and onset remain model dependent; no passage through
a varying-model limit follows. The exact fixed-class stop is retained.
This verifies the local REPRODUCTION; it supplies neither a new theorem
beyond the sources checked nor a resolution of Xi signs.

## Mathlib

Full matching coverage has not been checked. The proof uses elementary
polynomial inequalities, integration of nonnegative functions, and
the previously established full theta bound; no matching formal theorem
is asserted present or absent. Reference for a future coverage check:
https://leanprover-community.github.io/mathlib4_docs/ .

The prior literature assessment is
`drafts/literature/2026-11-07-finite-quartic-marginal-tail-test.md`.
It found no adequate matching theorem and does not certify originality.
This elementary calculation is recorded as REPRODUCTION, without a
claim of progress beyond the checked literature. Independent audit is
completed above under `drafts/literature/2026-11-07-finite-quartic-tail-audit.md`.
