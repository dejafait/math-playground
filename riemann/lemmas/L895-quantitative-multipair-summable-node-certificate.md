# Lemma 895: quantitative multipair summable-node certificate

## Hypotheses

Let (beta_j) be a finite or countable multiset of nonzero complex numbers,
invariant under conjugation including multiplicity, with
sum_j |beta_j| < infinity. Fix m >= 1 distinct unordered nonreal conjugate
pairs, and choose their representatives w_1,...,w_m in the upper half-plane.
Let mu_l >= 1 be the multiplicity of w_l (and hence of conjugate(w_l)).
Multiplicity counts copies of a location, not independent pairs.

Choose 0 < r < min_l |w_l|. The supplied finite head E is the set of
**all distinct** node locations v with |v| >= r; supply their exact locations
and multiplicities. Write h = |E|. Supply a finite real number T >= 0 with

    sum_{j: |beta_j| < r} |beta_j|^2 <= T.

This bound includes every omitted node with its multiplicity. Summability
implies E is finite, every multiplicity is finite, and some such T exists;
effective head data and a rigorous numerical upper bound T are additional
inputs to a numerical certificate. Nodes on |v| = r belong to the head.

Define S_k = sum_j beta_j^k for k >= 1 and the real symmetric matrix
H_D = (S_{a+b+2})_{0 <= a,b <= D}. Put Q(q) = sum_j beta_j^2 q(beta_j)^2
for real polynomials q, with an algebraic square. The convergence argument
of L030 applies verbatim to these generic summable nodes, as in L032.

## Conclusion

All the following constants depend only on the supplied data:

    P_l(t) = product_{v in E, v != w_l} (t + |v|)/|w_l-v|,  t >= 0,
    C_l = 2 P_l(r)/|w_l|,
    U = sum_{l=1}^m C_l^2,
    theta = r / min_l |w_l|,        mu_* = min_l mu_l.

Thus 0 < theta < 1 and U > 0. Use natural logarithms and set

    N = 1,                                                     if T = 0;
    N = max{1, ceil(log(max{1,T U/mu_*})/(2 log(1/theta)))},    if T > 0;
    D = N + h - 1,
    delta = T U theta^(2N),          gamma = 2 mu_* - delta,
    b_l = 2 |w_l|^(-N-1) P_l(1),     B^2 = sum_l b_l^2.

In particular delta <= mu_* and gamma >= mu_* > 0, and B^2 > 0.
There are explicit linearly independent real polynomials q_1,...,q_m of
degree at most D such that, for every x in R^m,

    Q(sum_l x_l q_l) <= -gamma ||x||_2^2.                      (1)

Consequently H_D has at least m strictly negative eigenvalues, counting
multiplicity. More precisely its m-th eigenvalue in increasing order is
at most -gamma/B^2. Repeated copies of a selected node strengthen mu_l
but do not yield extra directions.

For finite coefficient errors let epsilon >= 0 and real numbers S_hat_k satisfy
|S_hat_k-S_k| <= epsilon for 2 <= k <= 2D+2, and form H_hat_D by the same
Hankel rule. Let A be the (D+1)-by-m real matrix of coefficients of the
q_l in ascending powers, so the compressed matrices are F = A^t H_D A
and F_hat = A^t H_hat_D A. Then

    ||F_hat-F||_op <= epsilon B^2.                             (2)

In particular epsilon <= gamma/(2 B^2) ensures
F_hat <= -(gamma/2) I_m. Conversely any independently certified bound
F_hat <= -a I_m with a > epsilon B^2 certifies m negative directions for
H_D. Here matrix inequalities are real quadratic-form inequalities.
The basis A is exact; these statements do not include unbounded errors
in node locations, multiplicities or basis coefficients.

If the data instead approximate the logarithmic coefficients
ell_k = -S_k/k in log f(z) = sum_{k>=1} ell_k z^(2k), a sufficient uniform
error tolerance for 2 <= k <= 2D+2 is

    |ell_hat_k-ell_k| <= gamma / (2 (2D+2) B^2).                (3)

No existence of a nonreal node of actual Xi, actual-Xi sign inequality,
uniform cutoff or RH conclusion is asserted.

## Proof

Audit, 7 November 2026 (step91): the common-degree, whole-subspace and
coefficient-error calculations below were replayed, including zero tail
and increasing eigenvalue order. This verifies the conditional certificate,
not the availability of its data for actual Xi or any actual-Xi sign.

### Standard inputs and why explicit specialization is needed

Use ordinary finite Lagrange interpolation and the standard named
Courant-Fischer min-max theorem for finite real symmetric matrices.
A precise source for the latter statement is N. J. Higham,
[Eigenvalue Inequalities for Hermitian Matrices](https://nhigham.com/2021/03/09/eigenvalue-inequalities-for-hermitian-matrices/),
9 March 2021, the displayed Courant-Fischer formulas. Its perturbation
inequalities (1) also record the usual operator-norm stability principle.
The finite weighted Hermite context is
[Certified Hermite Matrices from Approximate Roots, arXiv:2110.10313v1](https://arxiv.org/pdf/2110.10313v1),
Section 2, Definitions 2.1/2.3, Example 2.2 and Theorems 2.4/2.7,
printed pp. 4-5. Theorem 2.7 is the classical weighted Hermite signature
theorem stated there by citation; it supplies no infinite-tail constant.
No rational reconstruction algorithm or unknown-Xi root input is imported.

We do not reprove that signature theorem. We calculate the selected head
block explicitly to retain the weight beta^2 and arbitrary multiplicities,
and extend L032's one-pair interpolation to a simultaneous bound and finite
precision budget. Neither the qualitative one-pair statement nor a finite
signature alone specifies these constants for the complete summable tail.

### Common real interpolation basis and exact head

For completeness, write M = sum_j |beta_j| and R = max{1,M}. Then
|beta_j| <= R and sum_j |beta_j|^2 <= R M. For each fixed polynomial q,
|q(beta_j)| <= sum_a |q_a| R^a, so Q(q) is absolutely convergent.
Also sum_j |beta_j|^k <= R^(k-1) M for every k >= 1. Thus the generic
version of L030's finite expansion is justified. For deg q <= D it gives
Q(q) = c^t H_D c for a coefficient vector c padded through degree D.
Conjugation with multiplicity makes each S_k and Q(q) real. There are
at most M/r node copies of modulus at least r, hence the head is finite;
each fixed nonzero location has finite multiplicity for the same reason.
All products and denominators defining the constants are therefore finite,
and P_l(r), P_l(1), C_l, U and B^2 are strictly positive. In particular
h >= 2m because the selected unordered pairs are distinct.

For v in E put

    L_v(X) = product_{a in E, a != v} (X-a)/(v-a).

All denominators are nonzero because E lists distinct locations.
Conjugation invariance of E implies that coefficientwise conjugation
of L_v gives L_conjugate(v). Define

    q_l(X) = (i/w_l)(X/w_l)^N L_{w_l}(X)
             - (i/conjugate(w_l))(X/conjugate(w_l))^N
                 L_conjugate(w_l)(X).                         (4)

The second summand is the coefficientwise conjugate of the first;
therefore q_l has real coefficients and degree at most N+h-1 = D.
Its values on E are i/w_l at w_l, -i/conjugate(w_l) at its conjugate,
and zero at every other location. In particular, for real x,
q_x = sum_l x_l q_l satisfies q_x(w_l) = x_l i/w_l. This proves
linear independence over R and injectivity of x -> A x.

At the two selected locations the summands beta^2 q_x(beta)^2 both
equal -x_l^2. Every unselected head location contributes zero. Thus,
including every multiplicity, the exact head contribution is

    Q_head(q_x) = -2 sum_l mu_l x_l^2.                         (5)

This directly checks the power shift two and does not substitute a
modulus square. Cross terms vanish on the entire head, not merely on
the chosen pairs.

### Complete tail and explicit degree

For |z| <= r the product triangle inequality gives
|L_{w_l}(z)| <= P_l(r). Conjugation invariance gives the same bound
for L_conjugate(w_l). Hence

    |q_l(z)| <= C_l (r/|w_l|)^N <= C_l theta^N.

For any real x, Cauchy-Schwarz now controls every linear combination:

    |q_x(z)|^2 <= ||x||_2^2 sum_l |q_l(z)|^2
                <= ||x||_2^2 U theta^(2N).

Absolute convergence, the supplied full tail mass, and the identity
|beta^2 q_x(beta)^2| = |beta|^2 |q_x(beta)|^2 imply

    |Q_tail(q_x)| <= delta ||x||_2^2.                          (6)

Conjugation with equal multiplicities makes this tail real. This
justifies its use as an upper error in (5), and bounds the operator
norm of the whole real compressed tail by delta. No partial-tail
preview or separate-vector estimate replaces (6).

If T = 0, the sum of the nonnegative tail masses is zero; since all nodes
are nonzero, the tail is empty. The definition N = 1 is legitimate,
delta = 0 and gamma = 2 mu_*. If T > 0 and TU/mu_* <= 1, the numerator
in the ceiling is zero, so N = 1 and theta^(2N) <= 1 already gives
delta <= mu_*. If TU/mu_* > 1, the definition of N gives
2N log(1/theta) >= log(TU/mu_*), again yielding delta <= mu_*.
Combining (5) and (6) proves (1) with the stated strictly positive gamma.
It also establishes absolute convergence of the displayed head/tail
calculation; alternatively L030 supplies it for every fixed q_x.

### Coefficient norm, negative index and finite precision

For a polynomial p write ||p||_{coeff,1} for the sum of the absolute
values of its coefficients. This norm is submultiplicative: expanding
a product and applying the triangle inequality proves
||p s||_{coeff,1} <= ||p||_{coeff,1} ||s||_{coeff,1}.
Consequently ||L_{w_l}||_{coeff,1} <= P_l(1). Multiplication by X^N
only shifts coefficients, and (4) therefore gives

    ||q_l||_{coeff,1} <= b_l,
    ||A x||_2 <= ||A x||_1 <= sum_l |x_l| b_l <= B ||x||_2.     (7)

For c = A x in the m-dimensional space V = image A, L030's identity
and (1)/(7) yield

    c^t H_D c <= -gamma ||x||_2^2
               <= -(gamma/B^2) ||c||_2^2.

Courant-Fischer, applied to this specific m-dimensional V, gives
lambda_m(H_D) <= -gamma/B^2 < 0. The matrix is real symmetric because
each absolutely convergent S_k is real by conjugation, and m <= D+1
because A is injective. These check the min-max hypotheses.
Explicitly, for n = D+1 and increasing eigenvalues lambda_1 <= ... <=
lambda_n, the formula used is

    lambda_m(H_D) = min_{dim W=m} max_{0 != c in W}
                       (c^t H_D c)/(c^t c).

Higham orders eigenvalues decreasingly: lambda_m here is his eigenvalue
with index n-m+1. The minimum-over-subspaces formula at that index has
subspace dimension n-(n-m+1)+1 = m and is exactly the displayed formula.
The bound on ||A x|| is an upper bound only; its use with a negative
factor reverses the inequality as displayed. No lower singular-value
bound or orthonormality of A is assumed or needed.

Every entry of H_hat_D-H_D has absolute value at most epsilon. For any
x, the triangle inequality for its quadratic form and (7) give

    |x^t(F_hat-F)x| <= epsilon ||A x||_1^2
                     <= epsilon B^2 ||x||_2^2.

For a finite real symmetric matrix the largest absolute Rayleigh quotient
is its operator norm, proving (2). Combining this with F <= -gamma I_m
proves the forward tolerance statement. Subtracting the same error from
F_hat <= -a I_m gives F <= -(a-epsilon B^2)I_m, proving the converse
certificate by the same injectivity and min-max argument.

Finally S_hat_k = -k ell_hat_k gives
|S_hat_k-S_k| = k |ell_hat_k-ell_k|. Since k <= 2D+2, (3) implies
the required uniform epsilon <= gamma/(2B^2). This only multiplies
coefficient errors by finite known integers; it makes no new analytic
continuation or infinite interchange. All tolerances and degree bounds
are finite explicit expressions in the supplied head and tail data. QED.

### Qualifications for use toward Xi

L024 supplies summability of the paired reciprocal-square nodes of Xi;
L025 identifies their S_k with its local logarithmic coefficients.
Those interpretation inputs do not supply a specified nonreal pair,
certified head enclosures, a usable tail mass or all-degree signs.
The constants can deteriorate with small node separation, large head,
small |w_l|, or a weak tail bound. Their data dependence is essential:
L057 permits arbitrarily many fixed Hankel tests in generic nonreal-zero
examples. L034 separately blocks inference from scalar power-sum signs.
These two obstructions are comparisons, not assumptions in this proof.
This is local quantitative specialization of known interpolation and
finite-form principles, with no claim of a new theorem beyond the sources
checked or of progress on the actual-Xi sign input.

## Mathlib

Coverage of this complete quantitative, summable-tail statement is not
checked. Availability is unknown, not claimed absent. No Mathlib result
is imported here. General interpolation or min-max support would not by
itself verify the explicit common-degree and full-tail/error calculation.
