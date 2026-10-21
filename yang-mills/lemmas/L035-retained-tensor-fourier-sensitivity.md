# L035 — Conditional retained tensor Fourier sensitivity

## Hypotheses

Keep L033's exact two pure-sector sums at cutoff M=112, L008's
relative modes and tau=1/16. The second index retains all four one-form
components and every allowed frequency. The axial odd-frequency exclusion
from L032 may be imposed exactly. Keep L034's definitions
F_h(n)=integral_(-3)^3 x^h rho(x) exp(i omega n x) dx,
omega=pi/8, H_0=6, H_1=9, and assume, conditionally,

\[
 |\widehat F_h(n)-F_h(n)|\le\eta H_h
 \quad(h=0,1,\ |n|\le224),\qquad\eta\ge0.                 \tag{1}
\]

Mode phases, derivative multipliers, heat and inverse weights in the
following definitions are exact. Actual floating-point errors in these
quantities are not included in (1).

For coordinate j of a potential, h is 1 in its two named directions
and 0 otherwise. Let A_j(d,a,b;k,ell) be the integral of
the d-th derivative of x^h rho(x), times the a-th derivative of the
left mode and the b-th derivative of the right mode. Define its
approximation by replacing F_h by Fhat_h in its Fourier expansion and
taking the real part. Set both the exact and approximate integral to
zero when their integrand is odd by exact parity. The modes, including
the zero cosine, have precisely L008's normalizations.

Expand a product of Q_i^alpha and N^alpha weak monomials as
v prod_(j=1)^4 A_j B_j. Collect terms with identical unordered pairs
of one-dimensional features in every coordinate, using exact rational
coefficients v. This collection is valid for the exact and approximate
integrals alike. No numerical threshold deletes terms.

## Conclusion

Suppose the differentiated left and right modes in one coordinate have
finite exponential expansions sum_p c_p exp(i omega p x) and
sum_q c'_q exp(i omega q x). Set

\[
 d_A=\eta H_h\sum_{p,q}|c_p c'_q|
                  |\omega(p+q)|^d,\qquad b_A=|\widehat A|,          \tag{2}
\]

with 0^0=1; take d_A=0 for the imposed exact parity zero. For a pair
of weak integrals define the nonnegative mode tables

\[
 B_j=b_{A_j}b_{B_j},\qquad
 D_j=d_{A_j}b_{B_j}+b_{A_j}d_{B_j}+d_{A_j}d_{B_j}.                 \tag{3}
\]

The following is an exact finite real number, not a floating-point
estimate:

\[
 S_i(\eta)=8\sum_{\alpha,c,k,\ell}\sum_v
 |v|\frac{e^{-\tau(\lambda_k+\lambda_\ell)}}{
                 \lambda_k^2\lambda_\ell}
 \left\{\prod_{j=1}^4(B_j+D_j)-\prod_{j=1}^4 B_j\right\}.       \tag{4}
\]

Here each v indexes a collected monomial product for that potential,
probe and second-index component; the sums use L033's same mode domains.
If Ihat_(i,112) is the exact finite sum obtained from the approximate
one-dimensional integrals with the exact weights, then

\[
 |I_{i,112}-\widehat I_{i,112}|\le S_i(\eta).                    \tag{5}
\]

S_i has a nonnegative separable double-Laplace contraction. For each
coordinate, collected feature pair and component define

\[
 \mathcal B_j(s,r)=\sum_{k_j,\ell_j}e^{-s\omega^2 k_j^2-r\omega^2\ell_j^2}B_j,
 \quad
 \mathcal D_j(s,r)=\sum_{k_j,\ell_j}e^{-s\omega^2 k_j^2-r\omega^2\ell_j^2}D_j.
\]

For each monomial product, start P=1,E=0 and process the four
coordinates using old values on each right-hand side:

\[
 E_{new}=E(\mathcal B_j+\mathcal D_j)+P\mathcal D_j,
 \qquad P_{new}=P\mathcal B_j.                                  \tag{6}
\]

Then S_i=8 sum_(alpha,c,v) |v| integral_tau^infinity (s-tau) ds
integral_tau^infinity E(s,r) dr. This representation requires only
one-dimensional mode-pair tables, with no seven-index array and no
subtraction of nearby products.

If a reported y_i also has a separately proved error
|y_i-Ihat_(i,112)|<=E_i, L033 yields
|I_i-y_i|<=t_i+S_i(eta)+E_i. This is a conditional enclosure only.

The binary64 implementation below diagnoses a windowed contraction
of (4) at eta=1e-12 as approximately
(5.0420797280e-7,1.8312544019e-6), below the chosen coefficient-error
budgets (100,1000). Neither these numbers nor their comparison are
certified inequalities for the exact S_i. Assumption (1), quadrature,
weight and arithmetic enclosures remain unproved. No sign of I_i,
compensated power coefficient, full logarithm or interacting bound follows.

## Proof

Compact support permits moving the coefficient derivatives onto the
mode product. The finite exponential expansions then give exactly

\[
 A=\sum_{p,q}c_p c'_q[-i\omega(p+q)]^d F_h(p+q).                 \tag{7}
\]

All frequencies satisfy |p+q|<=224. The true integral is real, so
taking the real part after substitution cannot enlarge its error.
Equation (1) and the triangle inequality give |A-Ahat|<=d_A. When
the integrand is odd, its exact integral vanishes; imposing this exact
zero also on Ahat gives error zero without assuming that arbitrary
approximate Fourier data preserve parity. For completeness, reflection
in x sends a cosine of frequency k to (-1)^k times itself and a sine
to (-1)^(k+1) times itself. Each derivative reverses parity. Thus the
integrand's parity is determined exactly by
h+d+a+b+lp+rp modulo 2, where lp=k for a cosine and k+1 for a sine,
and similarly for rp. A zero-frequency sine is absent from the domains.

For two one-dimensional integrals, write A=Ahat+delta_A,
B=Bhat+delta_B and expand the product. Its error is bounded by
d_A b_B+b_A d_B+d_A d_B, which is (3), and its approximate product
has absolute value B_j. Expand the product over four coordinates
using all nonempty subsets of perturbed factors. Each subset's
absolute contribution is bounded by its product of D_j on the
perturbed coordinates and B_j on the other coordinates. Their sum
is the bracket in (4). Multiplication by the nonnegative exact weight
and |v|, followed by the finite sums, proves (5). Collection of
identical product terms is legitimate because identical features use
the identical approximation; this is an algebraic identity before
the error estimate, not a cancellation of independently rounded terms.

L033's elementary Laplace identities represent each inverse weight.
All sums here are finite and their terms nonnegative, so distributing
products and interchanging sums and integrals needs no limiting
argument. Their mode domains are coordinate product sets for each
component; k_1=0 and the second-index axial frequency may be split
into zero and positive even parts. Hence each subset contribution
factors into its four coordinate sums. Recurrence (6) enumerates
these subsets without cancellation: inductively P is the product of
the processed baselines and E is the sum of all their nonempty
perturbation subsets. A new coordinate either is unperturbed, is
perturbed after a previous perturbation, or is the first perturbed
coordinate, giving exactly (6). This proves the separated formula.
The final conditional enclosure follows from (5), L033's spectral
tail and the triangle inequality. It makes no numerical claim about E_i.

The relevant general flow and matching results remain imported by the
precise primary citations and qualifications in
`drafts/literature/2026-09-26-current-target.md`. They do not evaluate
this coefficient-uncertainty contraction. The elementary finite-product
argument above justifies the estimator specific to the present weak
operators; it does not reprove those general theorems or assert originality.

### Numerical reproduction and qualifications

Run

```sh
OPENBLAS_NUM_THREADS=1 python3 scripts/combined-ward-response/check_retained_tensor_sensitivity.py --cutoff 112 --time-degrees 8 12
```

The complete certificate is
`scripts/combined-ward-response/retained-tensor-sensitivity-certificate.json`.
The coefficient table uses the inherited degree-144 quadrature. Zero
cosines have amplitude 1/sqrt(8); the allowance implementation may
equivalently duplicate their zero exponential with half amplitudes.
Positive modes have two exponential amplitudes of magnitude 1/4 before
derivatives. All allowed second-index components are retained; exact
parity tests are imposed before propagation. The two pure sectors are
already mathematically separated in L032.

At M=2 the separated heat contraction is compared at s,r in
{1/16,1/8} with an explicit dense mode sum and explicit nonempty-subset
enumeration. The largest relative discrepancy is 1.793e-14, below
1e-11; complete arrays are saved and were inspected. This checks
factorization and recurrence, while sharing the operator expansion and
Fourier/allowance tables. It is not independent validation of those inputs.

At M=112 the positive time rule uses panel width 0.5, eight lower-endpoint
subdivision levels and exponent window 80. Degrees 8 and 12 produce
192 and 288 nodes. The window is [tau,tau+80/(3 omega^2)]. The
nonnegative baseline diagnostics are (8495.6048119,30374.1386774).
The allowance totals change by approximately (1.06e-22,6.35e-22)
on time refinement. The maximum relative change across baseline and
allowance totals is 4.283e-16 versus tolerance 1e-9. Every integer
squared-frequency sum from 3 through 50176 is tested for both inverse
weights; the refined relative discrepancies are approximately
(4.45e-15,1.07e-14), against tolerance 1e-11. No check failed.

These are diagnostics, not upper bounds. In particular, the integral
in the theorem extends to infinity while the implementation uses a
finite time window. Rounding of the center tables, derivative factors,
heat factors, weight evaluations and summation also needs validation.
L034 separately bounds ideal window tails for the signed value using
a much coarser majorant; it does not turn these sensitivity diagnostics
into an enclosure. The observed small sensitivity licenses testing a
rigorous Fourier error input next, not declaring a retained sign.

## Mathlib

Full matching coverage for this estimator: not checked. Supporting
finite-product expansions, triangle inequalities and Laplace integrals:
not checked. The Python output is not a formal proof or an interval
certificate. Unknown Mathlib coverage is not evidence of absence.
