# L039 — A positive signed upper-face functional and a selected power term

## Hypotheses

Keep L008's box, relative modes, exact displacement and tau=1/16;
L030's residual stencil and selected upper-face one-internal-action-pair
class; and L032–L033's full two-potential decomposition and mode domains.
Use cutoff M=112, all four second-index components, and the exact axial
even-frequency restriction. No transition coefficient is removed.

The approximate Fourier table is exactly L037's saved hexadecimal table.
Define Ihat_(i,112) by L035, retaining exact phases, pi, normalizations,
heat factors and inverse weights. L037–L038 supply its coefficient-error
allowance against the exact I_(i,112). The certificate uses standard
IEEE binary64 rounded multiplication/addition or fused multiply-add,
with arbitrary summation order, and the explicit forward-error model
below. This is an informal computer-assisted enclosure, not a formal
verification of the processor or BLAS implementation. Reproduction
requires arithmetic satisfying that model; machine exponentials are
not numerical premises.

## Conclusion

The complete selected continuum functionals have strict enclosures

\[
 452.8<I_3<453.35,\qquad 3351.60<I_6<3353.59.                 \tag{1}
\]

For the reported dyadic centers y_i, the separately certified retained
errors, including inverse-weight approximation and tensor arithmetic, are

\[
 |\widehat I_{3,112}-y_3|<0.196837<100,\qquad
 |\widehat I_{6,112}-y_6|<0.711941<1000.                     \tag{2}
\]

After L038's coefficient allowance and L033's spectral tail, the total
errors against I_i are below 0.271616 and 0.992365, respectively.
Both signs are resolved. In particular L030 now gives

\[
\begin{split}
 -21760.8&<\lim_{a\downarrow0}a^2G_{\rm top}(3,a)<-21734.4,\\
 -160972.32&<\lim_{a\downarrow0}a^2G_{\rm top}(6,a)<-160876.8.
\end{split}                                                   \tag{3}
\]

These limits concern only the specified upper-face one-internal-pair
action class, in the straight forest, after the fixed-mesh small-coupling
coefficient. Other plaquettes, the no-internal-pair class, action/measure
and observable/flow jets, and L019's compensations are not evaluated.
A nonzero selected power term supplies no power coefficient or logarithm
for the complete response. It neither disproves the normalization route
nor improves the interacting reflected-error requirement <= c_box/2.
There is no candidate Yang–Mills solution.

## Proof

### A uniform exact inverse-weight rule

For every retained eigenvalue lambda, L008 gives
27/64<lambda<50176/4=12544. Write shifted times v=s-tau and w=r-tau.
The required inverse weights are integrals of v exp(-lambda v) and
exp(-lambda w) on [0,infinity). Use the exact positive 12-point
Gauss–Legendre rule on [0,2^-14] and each of the 22 panels [b,2b],
b=2^j, j=-14,...,7. The last endpoint is 256; there are 276 nodes.
The same rule is used independently in both time directions, with
weights d_s=weight*v and d_r=weight.

Import the standard Gauss–Legendre quadrature error theorem: on an
interval of length h, for f in C^(2m), the absolute rule error is at most

\[
 C_m h^{2m+1}\sup|f^{(2m)}|,\qquad
 C_m=\frac{(m!)^4}{(2m+1)((2m)!)^3}.                         \tag{4}
\]

Its hypotheses hold for both entire exponential integrands here. This
is the named standard Gaussian quadrature remainder theorem, with its
affine interval scaling; it is not a claim about stored numerical nodes.
The error specialization is necessary because the prior diagnostic
log-time rule had no uniform certified inverse-weight error.

On [b,2b], let x=lambda*b. For f=exp(-lambda v), multiplication of
(4) by lambda bounds the normalized error by
C_m x^(2m+1) exp(-x). For f=v exp(-lambda v),

\[
 |f^{(2m)}(v)|
 \le e^{-\lambda b}(2b\lambda^{2m}+2m\lambda^{2m-1}),
\]

so multiplication of (4) by lambda^2 gives
C_m exp(-x)[2x^(2m+2)+2m x^(2m+1)]. The positive exponential
series implies x^q exp(-x)<=q! for every nonnegative integer q.
On the initial panel lambda*2^-14<1, the corresponding normalized
bounds are C_m and C_m(1+2m); these follow from the same derivative
estimates with exp(-lambda v)<=1 and v<=2^-14.

Let H=(sum_(j=0)^160 108^j/j!)^-1. Since lambda*256>108,
the normalized missing tails obey
exp(-256 lambda)<=H and (1+256 lambda)exp(-256 lambda)<=109H.
The latter function is decreasing on nonnegative arguments. Thus, for
m=12 and the exact finite-rule weights Ahat(lambda), Bhat(lambda),

\[
\begin{split}
 |\lambda^2\widehat A-1|&\le\epsilon_A
 =C_m\{1+2m+22[2(2m+2)!+2m(2m+1)!]\}+109H,\\
 |\lambda\widehat B-1|&\le\epsilon_B
 =C_m\{1+22(2m+1)!\}+H.                                  \tag{5}
\end{split}
\]

These are exact rational uniform bounds, not tests at sampled
eigenvalues. Positivity of the Gauss weights is retained.

### A table-specific absolute envelope

L038's baseline feature records enclose, for each collected feature,
the complete coordinate sum of exp[-tau omega^2(k^2+ell^2)] times
|Ahat Bhat|. Use those baseline endpoints, not its sensitivity entries.
Multiply four coordinate bounds, apply the absolute collected rational
coefficient, and sum over both potentials and all components. This is
an outward upper bound P_i on the absolute initial-time tensor.

Each contributing pair of relative modes has both eigenvalues >27/64.
Exactly as in L038's positive envelope, integrating the shifted time
weights gives the full-time absolute expansion bound

\[
 B_i^{\rm abs}=8(64/27)^3P_i.                              \tag{6}
\]

This bounds the absolute expansion of the fixed-table sum, even when
individual monomials cancel. Exact collection is an algebraic identity
for this table; no approximate zero or numerical threshold is used.
The certificate recomputes (6) using every one of L038's 1,293 baseline
features and all 3,405 products. Its rational bounds are less than
849681123 and 3073220836.

For two inverse weights the relative product error is at most
epsilon_A+epsilon_B+epsilon_A epsilon_B. Equations (5)–(6) consequently
bound the fixed-table sum's entire time-rule error by

\[
 T_i=B_i^{\rm abs}(\epsilon_A+\epsilon_B+\epsilon_A\epsilon_B).
                                                                  \tag{7}
\]

The outward decimal bounds are 0.196836616622801627 and
0.711940486354459617, respectively. This sharper table-specific
absolute envelope is why the coarse scalar failure in ATTEMPTS/016
does not prevent the present enclosure. Neither coefficients nor
their sensitivities are recertified by (7); those inputs remain L037–L038.

### Enclose the exact finite rule's inputs

All root, weight, phase and weak-integral enclosures use integer
fixed-point interval arithmetic at scale S=10^80, with floor/ceiling
endpoint operations as in L036–L038. Twelve disjoint brackets inside
(-1,1) have opposite certified signs of P_12 at their endpoints,
and widths at most 10^-50. The intermediate value theorem and degree
12 identify all twelve exact roots, each simple. Proposals from NumPy
are used only to find initial brackets. Legendre recurrence and
P'_12=12(P_11-zP_12)/(1-z^2) enclose the exact positive weights
2/[(1-z^2)(P'_12)^2]. Affine maps enclose each panel's v, weight,
and weight*v, with strictly positive lower endpoints.

Machin's identity and rational alternating arctangent bounds enclose pi;
an integer square-root check encloses 1/sqrt(8). These are the same
standard constructions as L038. Every heat entry at an enclosed exact
node is evaluated by the alternating exponential Taylor bounds of
orders 61 and 60 after reduction to argument at most 1/8, followed by
outward squaring. Intersecting with [0,1] preserves inclusion. This
covers all 276*113 entries, including allowed zero cosines. Neither a
machine exponential nor a binary64 pi supplies an accuracy hypothesis.

For a weak integral, use L038's real-part formula: each signed wave
pair (p,q) has integer coefficient p^a q^b(p+q)^d and phase
i^(p+q+a+b-d), modified by -i sign(p) or -i sign(q) for each sine.
Quarter-turn phases are exact. Sum the selected fixed-table real or
imaginary dyadics with their integer multipliers before multiplying
by omega^(a+b+d)4^(-P)(1/sqrt(8))^Z. Exact parity zeros and derivatives
of zero modes are imposed before evaluation. This encloses the exact
fixed-table weak integral. A zero cosine is a single wave, not a
duplicated unit-amplitude contribution.

### Outward tensor propagation and its arithmetic model

Convert each integer interval to a binary64 midpoint c and radius r.
The code checks with exact rational arithmetic that [c-r,c+r] contains
both integer endpoints. Then carry midpoint-radius matrices throughout
the finite separated contraction. For a dot product of inner dimension
n<=276, apply the rounding-factor bound in N. J. Higham,
*Accuracy and Stability of Numerical Algorithms*, second edition,
SIAM (2002), Lemma 3.1, to the product/addition expression for each
dot entry. With unit roundoff u=2^-53 this gives

\[
 |\operatorname{fl}(AB)-AB|\le\gamma_n|A||B|+\delta,
 \qquad\gamma_n\le\frac{(2n+2)u}{1-(2n+2)u}.                \tag{8}
\]

The conservative count permits separate multiply/add operations,
arbitrary summation order, and fused multiply-add. Take the stored
binary64 G=nextafter(10^-12,+infinity), larger than every (8) bound.
For a nonnegative dot product, its computed value divided by the
stored denominator 1-G, rounded upward, plus 10^-290 is an upper bound
for the exact dot product. The exact audit checks that this denominator,
including its rounding, is below 1-gamma_276. Thus denominator rounding
cannot invalidate the bound.

For midpoint-radius inputs (A,a),(B,b), the exact uncertain-product
radius is bounded by
|A|b+a|B|+ab. Compute each of these nonnegative dots with that upper
operation and add G times the upper |A||B| dot. Scalar/elementwise
products use the analogous radius formula, with 10^-15 times the
absolute computed center as rounding allowance. Additions add the
input radii and that allowance. Positive bound operations use
nextafter toward infinity. The factor 10^-15 exceeds u/(1-u).
An additive 10^-290 at each propagation stage covers all local
underflow errors, even flushing tiny products to zero: it exceeds
1000 times 2^-1022, while at most 554 elementary operations enter
one dot estimate. The saved complete tables and final values are
finite, so overflow is excluded. These inequalities prove inclusion
by induction under the stated ordinary binary64 arithmetic model.

For a coordinate feature pair, first form its weak-integral product
matrix, then contract with the left and right enclosed heat matrices.
This gives every signed coordinate tensor. Multiply four coordinate
tensors, multiply the collected rational coefficient enclosed as
midpoint-radius, and sum all products and components. Finally contract
with the enclosed d_s and d_r vectors and multiply by 8. The mode
domains are the exact product domains of L033–L035; no seven-index
array, mode deletion, or approximate symmetry cancellation is needed.

### Complete evidence, final budgets and specialization

Reproduction commands:

```sh
OPENBLAS_NUM_THREADS=1 python3 scripts/combined-ward-response/check_signed_retained_enclosure.py
OPENBLAS_NUM_THREADS=1 python3 scripts/combined-ward-response/audit_signed_retained_enclosure.py
```

The full certificate is
`scripts/combined-ward-response/signed-retained-enclosure-certificate.json`;
the audit is `scripts/combined-ward-response/signed-retained-enclosure-audit.json`.
Eight `signed-retained-tables-<potential>-<component>.npz` archives save
all signed coordinate centers and radii; hashes are in the certificate.
All 1,293 features and 3,405 rational products are covered. The audit
checks every saved table's shape, finiteness and nonnegative radii,
covering 98,495,568 coordinate entries, and recomputes the exact
absolute-envelope, weight-error, final-budget and sign inequalities.
Root/heat/weak enclosures and tensor propagation rely on the generator's
induction above; the audit does not independently reevaluate every
dot product or establish processor conformance. There are no failures.

The reported centers are the exact dyadics specified by
`0x1.c512db3024550p+8` and `0x1.a312fb203c36ap+11`, approximately
453.07365704428685 and 3352.5931550193827. The outward arithmetic radii
are below 4.127492e-8 and 1.974653e-7. Adding (7) gives exact outward
retained-error bounds
0.196836657897716750 and 0.711940683819756296. This proves (2).

Use L035's triangle inequality, L038's actual full-time coefficient
allowances and L033's same-cutoff spectral tails. The total outward
error bounds are 0.271615561939352206 and 0.992364023307806023.
The certificate saves the complete rational endpoint values, and the
audit checks them exactly. They imply (1); multiplication of L030's
limit identity by these strict bounds proves (3). This use of L030
does not assign its selected coefficient to any other class.

The existing combined-response SPECIALIZE assessment and its primary
flow/matching citations are reused within their recorded scopes. No
bulk matching constant or protected-tensor finiteness claim is used to
infer (1). This finite enclosure reproduces standard quadrature and
interval/rounding methods for the specified representatives; it is local
progress, not certified originality beyond the sources checked.

## Mathlib

Full matching coverage for this signed stencil enclosure: not checked.
Supporting Gaussian quadrature error/positivity, Legendre identities,
spectral-gap exponential integrals and floating-point error estimates:
not checked. No matching theorem or direct Mathlib link is asserted.
Unknown coverage is not evidence of absence. The certificate and audit
are not a proof-assistant formalization.
