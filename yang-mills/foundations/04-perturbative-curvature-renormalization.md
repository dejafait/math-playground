# Perturbative curvature-operator normalization

Checked 2026-09-25: Hiroshi Suzuki, *Energy–momentum tensor from the Yang–Mills gradient flow*, PTEP 2013, 083B03, [arXiv:1304.0533v6](https://arxiv.org/abs/1304.0533v6), section 2, [equations (2.1)–(2.22)](https://arxiv.org/html/1304.0533v6#S2). The versioned [PDF](https://arxiv.org/pdf/1304.0533v6), pp. 3–5, was checked against the HTML equations.

The convention is connection curvature \(\mathcal F=d\mathcal A+\mathcal A\wedge\mathcal A\), action \(\int\mathcal F^c_{\mu\nu}\mathcal F^c_{\mu\nu}/(4g_0^2)\), and \(D=4-2\epsilon\). All operator identities below are centered and used in separated gauge-invariant correlations. Gauge-fixing, ghost, equation-of-motion, and contact terms are not imported as identities on an arbitrary off-shell algebra.

Equations (2.7)–(2.11), (2.13), (2.18), and (2.21) give

\[
g_0^2=\mu^{2\epsilon}g^2Z,\qquad
Z=1-\frac{b_0g^2}{\epsilon}+O(g^4),\qquad
b_0=\frac{11N_c}{48\pi^2},\qquad \beta(g)=-b_0g^3+O(g^5),
\]
\[
(\mathcal F^2)_B^{\rm cen}=Z_S[\mathcal F^2]_R,\qquad
(\mathcal F_{\mu\rho}^c\mathcal F_{\nu\rho}^c)_B^{\rm cen}
=Z_T[\mathcal F_{\mu\rho}^c\mathcal F_{\nu\rho}^c]_R
+Z_M\delta_{\mu\nu}[\mathcal F^2]_R,
\]
\[
Z_T=Z,\qquad Z_S=(1-\beta(g)/(g\epsilon))Z.
\]

These are formal perturbative renormalization identities. The trace-anomaly identity is (2.15); (2.19) explicitly warns that tracing a renormalized tensor and renormalizing its trace need not commute. Only one-loop pole residues and traceless projections are used in L004.

The paper supplies the contracted scalar/tensor identities, not the uncontracted rank-four mixing matrix or the fixed-boundary Wilson reflection coefficient. It supplies no nonperturbative cutoff-uniform bound here.

## Mathlib

Full statement and supporting formal-power-series or tensor-algebra coverage: **not checked**. The named source is a perturbative reference, not a Mathlib match or a continuum existence theorem.
