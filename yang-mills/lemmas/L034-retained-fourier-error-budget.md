# L034 — Retained Fourier error budget and ideal time-window tails

## Hypotheses

Keep L033's two pure-sector functionals, weak expansions, cutoff M=112,
tau=1/16 and all allowed second-index components. Use L008's exact rho
and omega=pi/8. For q=0,1 put

\[
 F_q(n)=\int_{-3}^3 x^q\rho(x)e^{i\omega nx}\,dx,
 \qquad H_0=6,\quad H_1=9.
\]

The bounds |F_q(n)|<=H_q follow by integration of |x|^q. A weak
matrix entry is expanded into exponentials after moving coefficient
derivatives onto the mode product, as in L033. Suppose approximations
satisfy |Fhat_q(n)-F_q(n)|<=eta H_q for every |n|<=224.
These are absolute, normalized errors, not relative errors in Fourier
coefficients that might vanish. Use the complete expansion, with no
approximate deletion of modes. Exact parity exclusions may be retained.

Let gamma=3(pi/8)^2 and U=80/gamma. For every retained eigenvalue define

\[
 A_U(\lambda)=\int_0^U v e^{-\lambda v}\,dv,\qquad
 B_U(\lambda)=\int_0^U e^{-\lambda v}\,dv.
\]

Suppose weight approximations obey
|Ahat-A_U|<=epsilon_s/lambda^2 and
|Bhat-B_U|<=epsilon_r/lambda. All three error parameters are nonnegative.
Define Ihat_i as the exact finite algebraic sum using these approximate
Fourier coefficients and weights, while keeping the exact heat factors
exp(-tau(lambda_k+lambda_ell)), mode phases, derivative multipliers and
normalizations. Suppose the reported real number y_i satisfies
|y_i-Ihat_i|<=E_i. Thus E_i must include any remaining computational
error in the phases, eigenvalues, heat factors, products and summation.
No such eta, epsilon_s, epsilon_r or E_i is established for the existing
binary64 evaluator by this lemma.

## Conclusion

With the rational moment bounds from L033 define

\[
 B_i^*=C_i7^5(5.32283164890\,10^{12})(9.95308720484)^6,
 \quad C_3=11584512,\ C_6=46338048.
\]

These are explicit majorants for the full absolute weak/exponential
expansion, and approximately equal (1.00753e30,4.03012e30). Let
H_160(x)=(sum_(j=0)^160 x^j/j!)^(-1), as in L033, and beta=82 H_160(80).
Then, with L033's same-cutoff spectral tails t_i,

\[
 |I_i-y_i|\le t_i+\beta B_i^*
 +\big[(1+\eta)^8(1+\epsilon_s)(1+\epsilon_r)-1\big]B_i^*+E_i. \tag{1}
\]

For the exact intended window [tau,tau+U], its omitted time integrals
alone obey beta B_3^*<0.0015 and beta B_6^*<0.006. The floating-point
implementation's endpoint is not automatically this exact endpoint;
any discrepancy must enter its validated weight or arithmetic errors.

Equation (1) is a conditional enclosure, not a certification of y_i.
Under the illustrative assumptions eta=epsilon_s=epsilon_r=2^(-52)
and E_i=0, its perturbation allowances exceed 2.23e15 and 8.94e15.
These exceed the cutoff-112 diagnostic sizes by over twelve orders of
magnitude. Thus this particular sufficient test fails at that input
error scale. It does not give a lower bound on the actual error or
prove that binary64 certification by a sharper method is impossible.
No sign, full Ward coefficient, logarithm or interacting estimate follows.

## Proof

For a weak monomial, compact support permits integration by parts in
each coordinate. Each product of two trigonometric mode factors is a
sum of exponentials. Derivatives contribute exact frequency multipliers,
and the integral in each coordinate is one F_q(n). Since both mode
indices are at most 112, |n|<=224. There are four such Fourier factors
in one operator monomial and eight in a product from Q_i and N.
If a parity exclusion is used, preserve conjugation/parity in the
approximate Fourier table or apply the same exact exclusion before
expansion; no unproved approximate cancellation is needed.

For complex numbers |z_j|<=h_j, |d_j|<=eta h_j, expand
prod_j(z_j+d_j)-prod_j z_j over the nonempty subsets of perturbed
factors. Taking absolute values gives

\[
 \left|\prod_{j=1}^8(z_j+d_j)-\prod_{j=1}^8z_j\right|
 \le ((1+\eta)^8-1)\prod_{j=1}^8h_j.
\]

The same subset expansion including the two weight factors gives the
bracket in (1), since 0<=A_U<=lambda^(-2) and 0<=B_U<=lambda^(-1).
No lower bound on any signed coefficient is used.

The absolute exponential/weak-monomial count is precisely the count
underlying L033(6): each positive-frequency normalized mode has sum
of exponential coefficient magnitudes 1/2, the zero cosine is at most
1/2, and coefficient derivatives contribute the factor bounded there
by 2^|d|. The product of the four H_q is 6^2 9^2=2916 for either
potential. Thus the absolute sum of all expanded contributions at a
seven-index frequency vector is bounded by
C_i R^10 exp(-9 R^2/1024), including both potentials and the sum over
components as in L033 section 2. This estimate is before signed
cancellations, so it also controls perturbations of individual Fourier
factors. Extend the finite index set to all nonnegative seven-indices.
The convexity inequality R^10<=(7^4)sum_j n_j^10 gives total bound
C_i7^5 S_10 S_0^6<=B_i^*. Using a full-spectrum bound here only enlarges
the retained error majorant; the spectral truncation error remains
separately t_i. There is no extra component-count factor because L033's
Omega products already sum those coefficients.

Direct integration gives

\[
 \lambda^2 A_U(\lambda)=1-(1+\lambda U)e^{-\lambda U},\qquad
 \lambda B_U(\lambda)=1-e^{-\lambda U}.
\]

Every eigenvalue is at least gamma, hence lambda U>=80. The functions
(1+x)e^(-x) and e^(-x) decrease on [0,infinity). If d_s,d_r are the
two missing normalized weights, then
0<=1-(1-d_s)(1-d_r)<=d_s+d_r<=82e^(-80)<=beta.
Multiply by the absolute expansion bound B_i^*. This covers the union
of both omitted time strips and their overlap, including every retained
mode. Add the weight/coefficient perturbation bound, E_i and L033's
spectral tail by the triangle inequality to obtain (1).

The exact rational reproduction command is

```sh
python3 scripts/combined-ward-response/check_retained_error_budget.py
```

Its complete certificate is
`scripts/combined-ward-response/retained-error-budget-certificate.json`.
It uses only L033's outward rational moment bounds, rational arithmetic
and the positive-series upper bound H_160. It records the failed
binary64-scale budgets, hypothetical finer budgets and their comparison
with the old same-cutoff diagnostic values. Those values are comparators,
not certified lower bounds; no assumption in (1) is discharged merely
by passing a budget comparison. The general flow and matching results
remain imported under the existing SPECIALIZE source assessment; none
evaluates these stencil-specific errors. The elementary subset expansion
and exponential integrations are provided to justify this specialization.

## Mathlib

Coverage of this full error-budget specialization: not checked.
Supporting finite product expansions, triangle inequalities and
exponential integrals: not checked. The rational certificate is not a
formalization and does not validate the existing numerical evaluator.
