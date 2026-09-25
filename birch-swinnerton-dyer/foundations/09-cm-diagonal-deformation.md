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

## Mathlib

Full coverage of the CM-family decomposition: **not checked**.
The named equations supply its arithmetic normalization, not a
Mathlib match or a theorem about rational Kummer membership.
