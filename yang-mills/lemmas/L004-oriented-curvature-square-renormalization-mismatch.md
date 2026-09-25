# L004 — Oriented curvature-square renormalization mismatch

## Hypotheses

Use the SU(2) Wilson normalization of L003. Its quadratic plaquette insertion is the smeared canonical curvature square \(\tfrac12\sum_c(dA)^c_{12}{}^2\). For the present ultraviolet diagnostic use continuum connection variables \(\mathcal A=g_0A\), with component convention

\[
\mathcal F^c_{\mu\nu}
=g_0(\partial_\mu A_\nu^c-\partial_\nu A_\mu^c)+O(g_0^2).
\]

Define the formal bare local operators, without summing over the displayed plane,

\[
h_{\mu\nu,B}=\frac1{2g_0^2}
\left(\sum_c(\mathcal F^c_{\mu\nu})^2\right)^{\rm cen},
\quad \mu<\nu,
\qquad h_{\nu\mu,B}=h_{\mu\nu,B},\quad h_{\mu\mu,B}=0.
\]

Work coefficientwise in continuum dimensional regularization, \(D=4-2\epsilon\), with minimal subtraction (MS), rotation covariance, and the centered scalar and contracted-tensor identities in the [perturbative source record](../foundations/04-perturbative-curvature-renormalization.md). Equalities involving renormalized operators are understood in separated gauge-invariant insertions, with the qualifications recorded there. No convergence of perturbation theory or identification of its remainder with the fixed-box Wilson measure is assumed.

A common multiplicative prescription means \(h_{\mu\nu,B}=\mu^{-2\epsilon}Z_hh_{\mu\nu,R}\) for the whole rotation orbit, with \(Z_h=1+z g^2/\epsilon+O(g^4)\), and no other dimension-four operator counterterms. Finite changes of scheme preserving the tree operator are allowed; they do not change this one-loop residue. Vacuum subtraction is already included.

## Conclusion

The scalar and traceless contracted-tensor projections require different one-loop bare-to-renormalized pole factors:

\[
\frac{Z_S}{Z}=1+\frac{b_0g^2}{\epsilon}+O(g^4),
\qquad
\frac{Z_T}{Z}=1,
\qquad b_0=\frac{11}{24\pi^2}>0.
\]

Consequently the common multiplicative prescription is impossible: the scalar projection forces \(z=b_0\), while the traceless stress-tensor projection forces \(z=0\). Rotation covariance then excludes multiplicative renormalization of a single fixed plane as an isolated operator in this prescription. Operator mixing, or projection onto a specified tensor sector, is necessary.

In four-dimensional bare tensor algebra set

\[
s=\sum_{\mu<\nu}h_{\mu\nu},\qquad
t_\mu=2\sum_{\nu\ne\mu}h_{\mu\nu}-s,\qquad
w_{12}=\frac{h_{12}+h_{34}}2-\frac{s}{6}.
\]

Then the exact identities are

\[
h_{12}=\frac{s}{6}+\frac{t_1+t_2}{4}+w_{12},\qquad
h_{12}-h_{34}=\frac{t_1+t_2-t_3-t_4}{4}.
\]

The complementary-plane difference thus selects a traceless diagonal stress-tensor combination at tree level. Neither its positive reflection coefficient nor its finite lattice matching is asserted here. The full one-loop correction to the oriented-plaquette reflection coefficient is also not determined: the remaining tensor sector and mixed reflected correlations have not been computed.

## Proof

### 1. Keep the bare coupling in the operator normalization

The expansion of \(\mathcal F\) in the hypotheses gives

\[
h_{12,B}=\frac12\sum_c
\left((\partial_1A_2^c-\partial_2A_1^c)^2\right)^{\rm cen}
+O(g_0).
\]

This is the quadratic density matched to the Wilson plaquette by L003. The comparison is only at tree level; it is not a derivation of an interacting continuum operator from that lattice lemma.

In dimensional regularization let

\[
s_B^{(D)}=\frac{(\mathcal F^2)_B^{\rm cen}}{4g_0^2},
\qquad s_R^{(D)}=\frac{[\mathcal F^2]_R}{4g^2},
\quad \mathcal F^2=\sum_{c,\mu,\nu}\mathcal F^c_{\mu\nu}\mathcal F^c_{\mu\nu}.
\]

The coupling and scalar identities give, as formal Laurent series,

\[
s_B^{(D)}=\mu^{-2\epsilon}\frac{Z_S}{Z}s_R^{(D)},
\qquad
\frac{Z_S}{Z}=1-\frac{\beta(g)}{g\epsilon}
=1+\frac{b_0g^2}{\epsilon}+O(g^4).
\]

Although \(Z_S=1+O(g^4)\) in the connection convention, the factor \(1/g_0^2\) changes the answer. Ignoring that factor would incorrectly remove the scalar one-loop pole from this diagnostic. With SU(2), the cited value \(11N_c/(48\pi^2)\) is \(11/(24\pi^2)\).

For a traceless symmetric numerical tensor \(k_{\mu\nu}\), form

\[
\tau_B(k)=\frac{k_{\mu\nu}}{g_0^2}
(\mathcal F^c_{\mu\rho}\mathcal F^c_{\nu\rho})_B^{\rm cen}.
\]

The term proportional to \(Z_M\delta_{\mu\nu}\) vanishes on contraction. Hence

\[
\tau_B(k)=\mu^{-2\epsilon}\frac{Z_T}{Z}
\frac{k_{\mu\nu}}{g^2}
[\mathcal F^c_{\mu\rho}\mathcal F^c_{\nu\rho}]_R,
\qquad \frac{Z_T}{Z}=1.
\]

These contractions select stress-tensor components. In particular, diagonal \(k\) with entries summing to zero produces linear combinations of the plane squares and has no one-loop pole. The scalar and such a tensor are nonzero independent tree polynomials: taking only \(\mathcal F_{12}\) nonzero makes the scalar and the choice \(k=\operatorname{diag}(1,1,-1,-1)\) nonzero; replacing it by \(\mathcal F_{34}\) preserves the scalar and reverses this tensor. Centering changes only an identity term and cannot identify these quadratic polynomials.

### 2. The multiplicative contradiction concerns pole residues

If the common prescription in the hypotheses existed, contraction of its tree operators into the scalar and into any nonzero traceless diagonal tensor would give the same simple-pole residue \(z\). The preceding two calculations require \(z=b_0\) and \(z=0\), respectively. This contradicts \(b_0>0\). Finite order-\(g^2\) redefinitions cannot remove a nonzero \(g^2/\epsilon\) residue.

The statement for a single plane uses the covariance hypothesis: rotating a multiplicatively renormalized 12 insertion gives the same scalar counterterm on each rotated plane, which would be the impossible common prescription. This does not prohibit defining a renormalized 12 insertion by a matrix of counterterms.

The pole test is performed on the dimensionally continued scalar and tensor before taking their finite four-dimensional limits. No identity equating the finite trace of a renormalized tensor with the separately renormalized scalar is used. An order-\(\epsilon\) change of a tree tensor projection can alter finite terms by multiplication with a one-loop simple pole, but cannot alter its residue. There are no higher poles at this order. Thus the noncommutation of trace and MS, explicitly recorded in Suzuki's equation (2.19), does not invalidate this residue contradiction.

### 3. Locate the tensor components of the chosen insertion

All identities in this paragraph are four-dimensional algebra on the six bare symbols \(h_{12},h_{13},h_{14},h_{23},h_{24},h_{34}\). Each symbol is counted twice in \(\sum_\mu\sum_{\nu\ne\mu}h_{\mu\nu}\), so \(\sum_\mu t_\mu=0\). Direct expansion gives

\[
t_1+t_2=2(h_{12}-h_{34}),\qquad
t_3+t_4=-2(h_{12}-h_{34}).
\]

Substituting these and the definition of \(w_{12}\) proves both displayed decomposition identities. Defining \(w_{13}=(h_{13}+h_{24})/2-s/6\) and \(w_{14}=(h_{14}+h_{23})/2-s/6\) gives \(w_{12}+w_{13}+w_{14}=0\). Thus the two further diagonal tensor directions are retained rather than silently discarded.

The bare classical energy–momentum tensor in the source convention has diagonal entries

\[
T_{\mu\mu}=\frac1{g_0^2}
\left(\sum_{c,\rho}(\mathcal F^c_{\mu\rho})^2
-\frac14\mathcal F^2\right)^{\rm cen}=t_\mu.
\]

Consequently \(h_{12}-h_{34}=(T_{11}+T_{22}-T_{33}-T_{44})/4\). The latter is a traceless contraction, so its formal continuation belongs to the protected tensor sector. This four-dimensional tree identity does not bypass evanescent finite terms, lattice translation-symmetry breaking, or boundary matching in an interacting regulator.

### 4. What this ultraviolet test does and does not decide

The pole mismatch rejects a single multiplicative renormalization for the full oriented operator. The elementary radial identity

\[
\int_m^\infty r^{-1}(\mu/r)^{2\epsilon}\,dr
=\frac{(\mu/m)^{2\epsilon}}{2\epsilon},
\qquad
\int_m^\Lambda\frac{dr}{r}=\log(\Lambda/m)
\]

explains the usual one-loop correspondence of a residue multiplying \(1/\epsilon\) with a logarithm \(2\log(\Lambda/\mu)\) for the same primitively logarithmic integral, after finite infrared terms are matched. This is a normalization diagnostic, not a computation of the fixed-boundary Wilson diagrams. In particular, neither a coefficient nor a sign for the complete logarithmic term of \(Q_{a,g}\) follows by assigning the scalar residue to \(h_{12}\).

Even formally, if an operator has matching matrix \(I+g^2\ell M+\cdots\), its reflected two-insertion form receives the insertion terms

\[
g^2\ell\bigl(q(Mh,h)+q(h,Mh)\bigr).
\]

The scalar and stress-tensor projections alone do not specify \(Mh_{12}\); the \(w\) sector remains. No cancellation or divergence of the full reflection coefficient is proved here. A fixed-order expansion also needs control of higher orders along the chosen coupling trajectory.

The actual threshold from L003 is still an interacting error at most \(c_{\rm box}/2\), uniformly in fine meshes. This lemma supplies no estimate toward that inequality. It identifies why a scalar-only or single-factor normalization is insufficient at the operator level and supplies a concrete tensor projection to test instead. Its free reflection lower bound must be established separately; L003's bound cannot be transferred by subtracting two positive plaquette forms.

## Mathlib

Coverage of the full formal renormalization-mismatch statement: **not checked**. Coverage of supporting finite-dimensional tensor algebra, formal Laurent series, and the elementary logarithmic integral: **not checked**. No theorem names or direct Mathlib links have been inspected. The cited Suzuki identities are perturbative supporting inputs, not a match for the full statement or a nonperturbative construction; the normalization conversion, pole contradiction, and plane decomposition are proved above.
