# L013 — The literal terminal container fails while the coarse enclosure is sharp

## Hypotheses

Use L012's unchanged packet: K = Q_3(pi), pi^9 = 3, O = O_K, J = log(O^times), I = J/6, a = pi, beta = 1, and G the Q_3-linear extensions of Aut_(Z_3)(I). Normalize v_3(3) = 1 and |x|_3 = 3^(-v_3(x)). Put X = G(pi O union pi J). For a positive real R, D_K(0,R) is the closed ball {x : |x|_3 <= R}.

Retain the literal terminal expression in [Dupuy–Hilado, arXiv:2004.13108v2, §6.2, (6.8), printed p. 20](https://arxiv.org/pdf/2004.13108v2#page=20):

\[
C_{6.8}=p^nD_K\left(0,\left(\frac{2p}{\mathrm e\ln p}\right)^m\prod_i e_i\right),
\qquad n=\lfloor v_p(a)-v_p(\beta)\rfloor.
\]

Here 2p in the fraction denotes real multiplication, p^n outside denotes field scaling, and \(\mathrm e=\exp(1)\) differs from the ramification indices e_i. As a distinct prescription, retain the unnumbered enclosure immediately following the chain:

\[
C_{\rm coarse}=D_K\left(0,\frac{\prod_i e_i}{|2p|_p}\,
p^{-\lfloor v_p(a)+\|\mathrm{diff}\|_\infty-\|\mathrm{diff}\|_1\rfloor}\right).
\]

The [saved SPECIALIZE assessment](../drafts/literature/2026-10-04-odd-prime-final-container.md) covers these comparisons. Original initial theta data, identification with Ind3, the full IUT image family and normalized A/B are not established hypotheses of this local test.

## Conclusion

The literal terminal radius satisfies

\[
R_{6.8}=\frac{54}{\mathrm e\ln3},\qquad 9<R_{6.8}<\frac{81}{4}<27.
\]

Neither X nor its hull is contained in C_(6.8). L012's I-preserving involution sends pi log(1+pi) to an element of absolute value 27 outside that container. Its exact log-image witness pi q_1 maps to q_1/18, also of absolute value 27.

In contrast,

\[
C_{\rm coarse}=D_K(0,27)=\pi^{-27}O=\operatorname{hull}(X).
\]

Thus the separately printed coarse enclosure contains the entire orbit and is sharp. The achieved/literal-required radius ratio is \(\mathrm e\ln3/2>1\); the achieved/coarse-required ratio is exactly one. The rounded hull(I), of radius 9, is itself contained in C_(6.8).

## Proof

L012 supplies X = I/3, hull(X) = pi^(-27) O of radius 27, and hull(I) = pi^(-18) O of radius 9. Its exact logarithm point q_1 belongs to J and has valuation -1. The displayed involution g satisfies g(pi q_1) = q_1/18, of valuation -3. It also satisfies g(pi log(1+pi)) in q_1/18+I. Since every error in I has valuation at least -2, the actual infinite-log input has image valuation -3 as well. These results are imported from L012 rather than recomputed or inferred from finite approximations.

There is one factor with ramification index nine, and n = floor(1/9-0) = 0. Consequently (6.8) has no outside scaling and its real radius is

\[
\frac{2\cdot3}{\mathrm e\ln3}\cdot9=\frac{54}{\mathrm e\ln3}.
\]

For a rigorous comparison, the exponential series gives \(\mathrm e>1+1+1/2+1/6=8/3\). For integers k >= 2, k! >= 2^(k-1), strictly for k >= 3. Therefore

\[
\mathrm e=2+\sum_{k=2}^{\infty}\frac1{k!}
<2+\sum_{k=2}^{\infty}2^{-(k-1)}=3.
\]

Monotonicity of ln gives ln3 > 1. Also \(\mathrm e^2>(8/3)^2>3\), so ln3 < 2. Hence

\[
\frac83<\mathrm e\ln3<6,
\qquad 9<\frac{54}{\mathrm e\ln3}<\frac{81}{4}<27.
\]

The radius-27 witness is outside the literal closed terminal ball. This proves noncontainment of X and its hull. Conversely every point of hull(I) has absolute value at most 9, so that rounded hull is contained in C_(6.8). The failure is in transporting the actual input to the terminal set, rather than enclosing I alone. No approximate field-radius cutoff is used.

For the separate coarse prescription, a one-entry different vector has equal infinity and 1-norms. Thus its floor exponent is floor(1/9) = 0. Its denominator is the p-adic absolute value |6|_3 = 1/3, giving radius 9/(1/3) = 27. Since |pi|_3 = 3^(-1/9), its closed ball equals pi^(-27) O, exactly L012's orbit hull. This proves containment and sharpness without treating the coarse prescription as a correction to (6.8). The earlier printed formula (6.2) remains separate and is not used here.

### Source comparison and scope

The supporting local setup and source formulas are imported from the prior assessment; L012 supplies the full orbit and exact witness. The difference derived here is the terminal numerical comparison. The suspect chain cannot be cited as an independent proof of the inclusion under audit. Its literal terminal slack does not absorb this packet's threefold orbit loss, while the separate coarse bound does.

The unchanged strict |a|_3 < 1, one-factor conductor and full lattice group fit the assessed toy hypotheses. No claim is made that this packet realizes original initial theta data or the complete IUT image family. This is not a counterexample to native IUT IV Proposition 1.2(ii) or Proposition 1.4(iii), whose inputs and correction terms differ. Essentiality to original IUT and finite B >= A remain unresolved.

Classification is **POTENTIALLY_NEW** only relative to the saved bounded source comparison. The numerical consequence is derived, known inputs are reused, and no certified originality or essential IUT flaw is claimed.

## Mathlib

Full local terminal-failure/coarse-sharpness statement: **not checked**. Supporting real exponential/logarithm inequalities, local-field valuations and closed-ball coverage: **not checked**. The named source and local calculation supply precise inputs, not matching Mathlib theorems or formal verification. No absence from Mathlib is inferred.
