# C057a — Physical strain signs and the selected top/top cubic coefficient

## Hypotheses

Keep L057's SU(2), all-face fixed box, lower-rooted straight forest,
both original Wilson-flow probes i=3,6, tau=1/16 and a=8/N through
admitted even meshes. Take the small-coupling coefficient at fixed
mesh before mesh refinement. Retain every selected upper transverse
edge, including pinned end edges. Use L055's one-color kernel K_i,
E_(i,mu,mu), compressed strain w_mu and torus constant d_*, and
exactly L046's compressed forms, traces A_i,B_i and constant c_*.

Import L047's complete trace and selected quartic enclosures, with
its stated IEEE binary64 arithmetic model, full Fourier uncertainty,
inverse-weight errors and omitted-spectrum bound. The numerical
conclusions below inherit that model; they are not processor or
formal proof verification. L039's unrestricted second index in I_i
is retained; no axial compression of I_i is made.

For the same f=f_(i,0), r=r_0 and upper plaquette set as L049, put

\[
 \mathcal W_{i,a}=-\kappa(f,r,S_{4,\mathrm{nr,top}}),\qquad
 \mathcal C_{i,a}=\tfrac12
       \kappa(f,r,S_{3,\mathrm{top}},S_{3,\mathrm{top}}).
\]

Thus L049's exact selected group is
G_i=mathcal W_(i,a)+mathcal C_(i,a), also the group in L057.
Both terms retain all three colors and all ordered top/top pairs.

## Conclusion

The physical strain integral has the exact trace identification

\[
 \mathcal S_i:=\int_{D_\perp}\sum_{\mu=2}^4
                         E_{i,\mu\mu}(x)w_\mu(x)\,dx=8B_i,
                                                               \tag{1}
\]

and the complete enclosures

\[
 888.29928<\mathcal S_3<888.29944,\qquad
 -257.75984<\mathcal S_6<-257.75968.                    \tag{2}
\]

An elementary bound on the full torus constant is 0<d_*<=1/4.
Consequently, writing k_i=lim_(a downarrow 0) a² G_i,

\[
 k_i=768d_*B_i,\qquad
 0<k_3<21319.18656,\quad -6186.23616<k_6<0.             \tag{3}
\]

The top/top cubic contribution alone has a scaled limit

\[
 \begin{split}
 \ell_i&:=\lim_{a\downarrow0}a^2\mathcal C_{i,a}
       =k_i-(J_i-48I_i)\\
       &=48I_i-16A_i+(768d_*-96c_*)B_i,\qquad
 16688.19&<\ell_3<40698.68656,\\
 157055.03384&<\ell_6<164110.08.                         \tag{4}
 \end{split}
\]

Both cubic coefficients are positive. Compared with L047's negative
quartic coefficient for both probes, the joint group's triplet
coefficient changes sign and its shear coefficient remains negative.
Neither joint coefficient vanishes. These are selected a^-2
coefficients, not coefficients of the complete forest-independent
response or of its logarithm. Other cubic pairs, measure, insertion
and nonlinear flow jets, all subleading powers and logarithms,
finite matching, the interacting reflected error <=c_box/2,
continuum field axioms, infrared control and finite positive mass
remain unresolved. No lower numerical bound on d_* is asserted.

## Proof

### Exact normalization of the physical integral

L055 identifies E_(i,mu,mu) with the diagonal mixed derivative of
precisely the kernel in L046(5), namely

\[
 K_i(x,y)=8\sum_{k,l}
 \frac{e^{-\tau(\lambda_k+\lambda_l)}(Q_i^0)_{kl}}
      {\lambda_k\lambda_l}\psi_k(x)\psi_l(y).
\]

Its fixed positive-time double heat sum converges with every fixed
number of derivatives. Indeed L046 proves the relative form bound
|(Q_i^0)_(kl)|<=C_i sqrt(lambda_k lambda_l), and differentiated
normalized sine modes have only polynomial index growth. The
positive spectral gap and heat factors dominate those polynomials.
The smooth compact coefficients w_mu are bounded. Differentiating
and integrating term by term is therefore justified absolutely.

L046(3)'s triplet bilinear form gives

\[
 \int\sum_\mu w_\mu
       (\partial_\mu\psi_k)(\partial_\mu\psi_l)
          =(Q_3^0)_{lk}.
\]

Substitution yields (1), with factor 8 from the physical kernel,
no extra color multiplicity, and exactly L046(1)'s B_i. This
calculation retains all transition coefficients and both complete
transverse mode indices. It acts on the already compressed physical
kernel only; it never changes either index domain of I_i.
Multiplication of L047(1)'s exact rational endpoints for B_i by 8
proves (2). In particular d_*>0 alone would not have supplied the
two different signs.

### A sufficient uniform bound for the universal constant

In L055(1), 0<=lambda_mu<=4 and lambda=sum_mu lambda_mu. For
lambda>0 rationalizing its expression gives

\[
 b_\infty(\lambda)=
 \frac{2\lambda}{\sqrt{\lambda(\lambda+4)}+\lambda}<1.
\]

Also lambda_4<=lambda, |lambda_2-lambda_3|<=lambda and
4+lambda_4<=8. The nonnegative integrand in the definition of
32d_* is thus at most 8. The normalized torus has measure one;
the value at theta=0 is immaterial. Hence d_*<=1/4. L055's
positive-open-set argument gives d_*>0. No quadrature of this
constant or small-frequency replacement is required.

L057's full selected limit is 96d_* mathcal S_i. Equation (1)
therefore proves k_i=768d_*B_i. For B_3>0, its upper bound is
192 times 111.03743 = 21319.18656. For B_6<0, its lower bound
is 192 times (-32.21998) = -6186.23616. Both inequalities are
strict because the imported B endpoints are strict; the zero
endpoints are excluded by d_*>0. This proves (3).

### Compare the same quartic once

L049's S_(4,nr,top) is L029's ordered upper-face quartic summed
over exactly the same plaquettes. L047's two classes are the
complete one-internal-pair class and its complete no-internal-pair
companion for this polynomial, with their negative cumulant sign.
Thus L047 identifies
lim a² mathcal W_(i,a)=J_i-48I_i; L049(9) identifies
G_i=mathcal W_(i,a)+mathcal C_(i,a) at every admitted mesh.
The existence of the first and joint limits implies the existence
of their difference. Subtracting, rather than adding, the quartic
coefficient proves the identity in (4). L046 supplies
J_i=16A_i+96c_*B_i for its second expression.

For the enclosures import L047(3):

\[
 -19379.50<J_3-48I_3<-16688.19,\qquad
 -164110.08<J_6-48I_6<-163241.27.
\]

Subtract these intervals from (3). The resulting cubic endpoints
are respectively 16688.19 and 21319.18656+19379.50,
and -6186.23616+163241.27 and 164110.08. These give exactly
(4). No covariance sign is inferred from pointwise positivity of
the conditional defect; the signs follow from the complete signed
trace enclosure and the already proved scaled limits.

### Verification and source scope

The complete aggregate audit of L047's saved coordinate tensors was
rerun successfully: 38 feature tables, 2894688 tensor entries,
31301 heat entries, 928258 weak-entry occurrences, all four trace
error budgets and both prior separations. It inherits L047's
primitive interval induction and IEEE model; it is not independent
processor verification. The exact rational endpoint propagation for
(2)–(4), including containment of both exact saved B intervals in
the imported decimal intervals, is recorded in
`scripts/combined-ward-response/physical-strain-comparison-certificate.json`.
Reproduce it from this notebook with

```sh
OPENBLAS_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python3 scripts/combined-ward-response/audit_companion_enclosure.py
PYTHONDONTWRITEBYTECODE=1 python3 scripts/combined-ward-response/check_physical_strain_comparison.py
```

Reuse the unchanged SPECIALIZE assessment
`drafts/literature/2026-09-26-current-target.md`. This corollary
applies established local trace identities and enclosures; its
new local consequence is the selected strain sign and compensation
comparison, not mathematical originality or a result beyond the
general methods of the sources checked. Luescher–Weisz,
*Perturbative analysis of the gradient flow in non-abelian gauge
theories*, [arXiv:1101.0963v2](https://arxiv.org/pdf/1101.0963v2),
sections 7.1–7.4, (7.1)–(7.8), and 8.2, concerns perturbative
flow finiteness after ordinary four-dimensional renormalization on
R^4. It is not used to assign this bare-normalized fixed-box
coefficient. Reproving that general theorem would not give (1).
All terms previously removed only at a² scale must be restored for
the logarithmic target; no uniform positive-coupling conclusion is
drawn from these fixed-mesh coefficients.

## Mathlib

Coverage of this full specialized strain and cubic comparison:
**not checked**. Supporting differentiated heat expansions,
spectral traces, interval propagation and elementary integral
inequalities: **not checked**. No matching Mathlib theorem or
machine verification is asserted; unknown availability is not
evidence of absence.
