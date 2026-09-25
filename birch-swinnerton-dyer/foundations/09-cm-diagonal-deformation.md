# Normalized CM tensor on the diagonal weight line

Checked 2026-09-25 in Castella--Hsieh, *On the nonvanishing of
generalised Kato classes for elliptic curves of rank 2*,
[published version](https://doi.org/10.1017/fms.2021.85), CC BY 4.0.
Retain Section 2.4's CM-family hypotheses; this is not an existence
claim for auxiliary data for arbitrary E. Use the Q_p coefficient
case of the earlier audit. Write H = G_K and tau for complex conjugation.

- [Section 2.4, equation (2.3), printed page 10](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/72ED842AB428A7ED619B1B84287A6864/S2050509421000852a.pdf/on-the-nonvanishing-of-generalised-kato-classes-for-elliptic-curves-of-rank-2.pdf#page=10)
  defines Psi_T(h) = (1+T)^{l(h)}. The quotient
  xi_T = Psi_T/Psi_T^tau is the universal anticyclotomic character.
- [Proposition 2.5 and Remark 2.6, equation (2.4), printed page 11](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/72ED842AB428A7ED619B1B84287A6864/S2050509421000852a.pdf/on-the-nonvanishing-of-generalised-kato-classes-for-elliptic-curves-of-rank-2.pdf#page=11)
  use T = v^(-1)(1+S)-1 and give, on S_2 = S_3 = S,

  \[
  \mathbb V^\dagger_{f,\mathbf g\mathbf g^*}
   \simeq V_f(1)\otimes
    \bigl(\operatorname{Ind}_{H}^{G_{\mathbf Q}}\xi_T
      \oplus\operatorname{Ind}_{H}^{G_{\mathbf Q}}\chi\bigr),
  \qquad \chi=\psi/\psi^\tau.
  \]

- [Section 5.1, printed page 25](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/72ED842AB428A7ED619B1B84287A6864/S2050509421000852a.pdf/on-the-nonvanishing-of-generalised-kato-classes-for-elliptic-curves-of-rank-2.pdf#page=25)
  identifies S = v-1, hence T = 0, with the diagonal stabilization
  (g_alpha,g*_(alpha^(-1))). Here V_f(1) = V_p E.

Our inference, proved in L008: the derivative of xi_T obstructs
lifting the fiber trace. The unit coordinate change has nonzero
derivative, so it cannot remove that obstruction. The elementary
normalized inducing-character calculation is included there; no
unwritten choice of cyclotomic twist is used in this application.

## Localizations of the actual diagonal class

Rechecked 2026-09-25 in the same published article. The
[publisher's mathematical HTML](https://www.cambridge.org/core/journals/forum-of-mathematics-sigma/article/on-the-nonvanishing-of-generalised-kato-classes-for-elliptic-curves-of-rank-2/72ED842AB428A7ED619B1B84287A6864)
preserves the bars on prime labels that are lost in the PDF text extraction.
Keep all the earlier auxiliary, residual, and coefficient hypotheses.

[Section 3.4, (3.12)--(3.13)](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/72ED842AB428A7ED619B1B84287A6864/S2050509421000852a.pdf/on-the-nonvanishing-of-generalised-kato-classes-for-elliptic-curves-of-rank-2.pdf#page=17)
defines the anticyclotomic Iwasawa component Z by Shapiro.
[Theorem 3.6 and Corollary 3.7, page 18](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/72ED842AB428A7ED619B1B84287A6864/S2050509421000852a.pdf/on-the-nonvanishing-of-generalised-kato-classes-for-elliptic-curves-of-rank-2.pdf#page=18)
give, for Corollary 3.7's test vectors,

\[
\operatorname{Loc}_{\overline{\mathfrak p}}Z=0,\qquad
\operatorname{Col}^{\eta}(\operatorname{Loc}_{\mathfrak p}Z)
 =C(T)\Theta_{f/K}(T),\qquad C(0)\ne0.
\]

Here C is regular and invertible at augmentation after extending
coefficients. Its factors are displayed in Corollary 3.7; Proposition
2.5 supplies the unit w. Theorem 3.6's local filtration contains the
whole V factor at mathfrak p, so it supplies no vanishing of its
ordinary component. Section 5.1 and Lemma 5.1 identify the fiber.

[Theorem 3.4, page 16](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/72ED842AB428A7ED619B1B84287A6864/S2050509421000852a.pdf/on-the-nonvanishing-of-generalised-kato-classes-for-elliptic-curves-of-rank-2.pdf#page=16)
gives the augmentation Coleman functional through the dual exponential.
Equivalently, [Proposition 4.3 and Lemma 4.4, pages 22--23](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/72ED842AB428A7ED619B1B84287A6864/S2050509421000852a.pdf/on-the-nonvanishing-of-generalised-kato-classes-for-elliptic-curves-of-rank-2.pdf#page=22)
express it, up to a factor nonzero at augmentation, as local Tate
pairing with a finite local class. The proof of
[Theorem 4.5, page 24](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/72ED842AB428A7ED619B1B84287A6864/S2050509421000852a.pdf/on-the-nonvanishing-of-generalised-kato-classes-for-elliptic-curves-of-rank-2.pdf#page=24)
computes that class's nonzero logarithm. L010 checks the resulting
kernel and the local specialization before using them.

[Section 5.5, (5.9)--(5.11), page 28](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/72ED842AB428A7ED619B1B84287A6864/S2050509421000852a.pdf/on-the-nonvanishing-of-generalised-kato-classes-for-elliptic-curves-of-rank-2.pdf#page=28)
provides the bounds recorded in the nonvanishing foundation. L010
deduces ord_T Theta >= 2 under kappa != 0. This is not a comparison
with complex analytic order or a calculation of the full localization.

## Mathlib

Full coverage of the CM-family decomposition, diagonal localization,
Coleman interpolation, and local specialization: **not checked**.
The named source statements supply arithmetic inputs, not a Mathlib
match or a theorem about rational Kummer membership. The first-order
local derivative formula in L010 is a notebook deduction.
