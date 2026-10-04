# Birch and Swinnerton-Dyer conjecture: argument overview

The target is Wiles's official Clay rank assertion for every E/Q.
[The scope](foundations/01-target-and-scope.md) separates the stronger refinement. No candidate exists.
The [standard inputs](foundations/02-standard-inputs.md) include finite generation, analytic continuation, the analytic-rank-zero/one theorem, and Selmer and Kummer theory.

## Unresolved gap

For arbitrary E/Q with analytic order m(E) >= 2, the missing claim is rank E(Q) = m(E).
Finite Selmer sizes have a Tate–Shafarevich defect; cyclotomic characteristic order has an additional augmentation defect.
The certificates remove defects conditionally; their uniform production and comparison with m(E) remain missing.
No checked generalised Kato construction supplies a nonzero rational Kummer class from m(E) = 2 alone; a cycle-valued specialization is missing.

## Partial results

L001 gives the exact torsion-corrected size identity
\[
\log_p|\operatorname{Sel}_{p^n}|-\log_p|E(\mathbf Q)_{\rm tors}[p^n]|
 =n\operatorname{rank}E(\mathbf Q)+\log_p|\Sha[p^n]|.
\]
Finite-depth abstract towers match ranks zero and two, finite paired Sha, and zero pulled-back pairings.
Even parity and r <= 2 do not force r = 2; no elliptic-curve realization or BSD counterexample is asserted.

Using the named theorems in [the cyclotomic foundations](foundations/03-cyclotomic-control.md), L002 proves, at an odd good-ordinary prime,
\[
\operatorname{ord}_T f_X=\operatorname{rank}E(\mathbf Q)
 +\operatorname{corank}_{\mathbf Z_p}\Sha(E/\mathbf Q)[p^\infty]
  +\operatorname{length}_{\Lambda_{(T)}}(T X_{(T)}).
\]
The last term vanishes exactly when T X_(T) = 0. Control gives rank <= Selmer corank <= characteristic order.
Abstract modules with ideal (T^4) have specialized dimensions two and four, both even; no arithmetic realization is asserted.

L003 applies [Schneider--Perrin-Riou](foundations/04-cyclotomic-height-criterion.md):
finite p-primary Sha and a nonzero canonical cyclotomic regulator give ord_T f_X = rank E(Q), hence T X_(T) = 0. Equality with rank is equivalent
to finite p-primary Sha and the natural isomorphism X_(T)[T] -> X_(T)/T X_(T).
The converse retains finite Sha and non-CM E; no uniform hypotheses are supplied.

L004 uses [Kato divisibility](foundations/05-kato-divisibility.md) for non-CM E at good-ordinary p >= 5.
Given n independent rational points and a rigorously nonzero T^n coefficient of the primitive ordinary L_p,
\[
n\le r\le\operatorname{ord}_T f_X\le\operatorname{ord}_T L_p\le n.
\]
Both defects vanish, p-primary Sha is finite, and the cyclotomic height is nondegenerate.
With k < n points, only (r-k)+s+delta <= n-k follows.
Neither n = m(E) nor uniform availability of this certificate is established.

The [2016 audit](foundations/06-generalised-kato-scope.md) separates Selmer theorems from conjectural point membership;
the adjoint rank-(2,0) formulas predict at most one line from four stabilisations.
L005 proves that one nonzero strict rational Kummer class forces r >= 2:
the local logarithm has rank one on E(Q) tensor Q_p when r > 0. A nonzero a_2 then reaches L004's r = 2 threshold.

[Castella--Hsieh's Theorem A](foundations/07-castella-hsieh-nonvanishing.md), under its auxiliary and residual hypotheses, gives Selmer dimension two from nonzero kappa.
L006 combines this with L005: Kummer membership gives r = 2 and finite p-primary Sha without a cyclotomic coefficient. That membership is not established.
Theorem B assumes positive rational rank and anticyclotomic theta order two; its bounds still allow (r, dim V_p Sha) = (1,1).
Neither theta order nor nonzero Kummer membership follows here from m(E) = 2.

The [construction audit](foundations/08-diagonal-cycle-specialization.md) leaves a motivic comparison missing.
L007, under its explicit classical accumulation hypotheses, shows that continuing the ordinary tame-dual pairing forces crossed stabilizations; L006 uses a diagonal pair.
For the [normalized CM diagonal family](foundations/09-cm-diagonal-deformation.md), L008 obstructs extending the fiber trace already modulo T^2, even with corrections involving V_p E.
Maps confined to the fiber or to an individual class remain outside that obstruction.
L009 uses [Selmer-complex duality](foundations/10-selmer-bockstein-duality.md) and the auxiliary twist's
zero Selmer space: the ordinary anticyclotomic Bockstein vanishes on all of S, giving no Kummer criterion.
A strict class's unique invariant ordinary lift stays strict exactly when its derivative Delta_d in D^- is zero.
L010 applies the actual diagonal family's local conditions: for U = Loc_mathfrak_p Z and u = (U/T)(0),
the scalar law makes u ordinary and Delta_d(res_K(kappa)) = (u,-tau u)/2.
Strict lifting requires U in T^2 M_mathfrak_p; even the full Coleman series leaves u undetermined locally.
Neither u = 0 for the actual global class nor a connection to rational Kummer membership is proved.
L011 pairs Delta_d with the one-dimensional minus **relaxed** Selmer space, which survives ordinary minus vanishing.
On the strict vector from rational P,Q its coefficient is log_p(Q)t_d(P)-log_p(P)t_d(Q), independent of the local lift choice.
Dual complexes and an injective rational logarithm permit a nonzero determinant in a formal full-Kummer model.
Automatic vanishing is not a consequence of those data; its truth for actual rational points remains unresolved.
L012 specializes [rank-zero Kato reciprocity](foundations/11-rank-zero-kato-reciprocity.md): w = res_K(z_tw) generates the relaxed minus line, and its mixed pairing is 2 lambda t_d with lambda != 0.
The lift asks whether -tilde_d cup z_tw vanishes in H^2(Q,V), for an explicit extension of V tensor chi_K by V. This remains uncomputed and supplies no new rank bound.
L013 reproduces Sano's degree-one cyclotomic determinant descent in a formal model with compatible local-condition triangles and inverse-parameter duality.
Its Selmer dimension and characteristic/scalar order are two, but its marked rational/Sha dimensions are (1,1). The leading vector is rational; its determinant preimage uses a Sha direction. No arithmetic realization or rank improvement is asserted.
L014 applies Kim's classical-system vanishing and torsion reciprocity: a full rational Kummer correction preserving the original auxiliary relations is zero.
Under the stated local-torsion and nonzero mod-p Kurihara premises, even an isolated rational correction leaves a nonzero p-singular component. This extraction mechanism stops; rational determinant membership and the r >= 2 lower bound remain open.
Under the additional p not dividing #E(F_p) hypothesis, Sakamoto's [Theorem 3.17 and Corollary 4.10](https://ems.press/content/serial-article-files/29299?nt=1#page=30) supply a Kato-derived rank-zero family and a prime-deletion classical mod-p Selmer basis at a minimal Kurihara index.
L015 specializes this [assessed construction](drafts/literature/2026-10-03-rank-zero-extra-relaxed-prime.md) at fixed P_(2,0) primes: both prescribed p^2 components are classical exactly when Sel_(p^2) -> Sel_p is onto, equivalently Sha[p] = p Sha[p^2], or both residual errors vanish.
L016 reduces the errors to one alternating scalar tau; the one-prime scalars always vanish. If tau = 0 the components give an R_2 Selmer basis; otherwise classical reduction is zero, r = 0 and p-primary Sha is F_p^2.
L017 specializes Section 2.5's Stark transfer: the actual p-local extension at N splits, and its rank-three to rank-two determinant contraction is an isomorphism. Divisor transitions retain order-p error vectors with zero scalar regulators.
A maximal-isotropic model extends the tested package through this p-local contraction and all divisor transitions at N with tau != 0; the final scalar contains p^2BC = 0 in R_2. It supplies no full Stark/Kato family or arithmetic realization.
The [depth-three source assessment](drafts/literature/2026-10-04-prime-deletion-p3-initial-fitting.md) imports Sakamoto's initial Fitting/all-depth primitivity statements and [Kim's Corollary 1.11](https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf#page=8). C016a applies the converse: adding L(E,1) = 0 excludes L016's finite-Selmer nonzero-tau branch, so tau = 0 and both prescribed p^2 classes form a classical Selmer basis. The p-primary Selmer group is infinite, but rational Kummer membership, the required r >= 2 and higher-depth compatible lifting remain missing. No P_(3,0) eligibility or depth-three calculation is used.

## Known traps checked

- The rank assertion differs from central vanishing and the refined formula.
- The zero/one theorem retains its analytic hypothesis; Selmer rank need not equal rational rank.
- A nondegenerate pairing on finite Sha does not make its p^n-torsion restrictions nondegenerate or give a stopping depth. The models vary with depth and respect eventual descent and independent-point certificates.
- Abstract models do not prove arithmetic realizability or BSD.
- Control's finite errors disappear over Q_p; characteristic length can still exceed dimension.
- Semisimplicity at (T), zero divisible Sha defect, and the complex/p-adic comparison are separate inputs, not consequences of control or cotorsion.
- Heights keep finite Sha and nonzero regulator explicit; the checked converse retains its non-CM restriction and gives no complex-order comparison.
- Kato gives an upper bound after inverting p; no reverse divisibility or p-adic BSD formula is assumed. Approximate zero is not certified nonvanishing.
- Strict Selmer need not mean Kummer; the 2016 Conjectures 3.2/3.12 remain conjectures. The 2022 Section 5.7 assumes finite p-primary Sha. Triple-product values, theta orders, cyclotomic coefficients, and complex vanishing orders are distinguished throughout.
- A fiber trace need not lift; its obstruction is not non-Kummer membership of an individual class.
- Ordinary lifting need not preserve strictness; neither lifting condition is identified with Kummer membership. The dual of zero local conditions is relaxed, so ordinary height vanishing does not settle the mixed pairing.
- Scalar Coleman data alone do not force full-localization divisibility; local freedom is not a global realization. A nonzero Kato reciprocity value normalizes the relaxed class without deciding its anticyclotomic obstruction.
- Cohomological determinant descent, including its H^2-dual factor, does not identify the preimage with wedge^2 of rational points. Rationality of the contracted leading vector is a weaker condition.
- A minimal nonzero two-prime Kurihara index is an additional premise, not analytic rank two or Kim's first integral index. Ordinary classical-system vanishing does not cover an isolated finite class or a differently indexed rank-zero system; p-finiteness alone is not rational Kummer membership. Fixed primes require P_(2,0) eligibility and the non-anomalous restriction. Reciprocity and L017's determinant contraction permit L016's alternating error in their formal subsystem. C016a excludes the actual nonzero branch only after adding central vanishing and applying the checked finite-Selmer converse; an infinite Selmer group still does not identify rational directions. The formal model supplies no full arithmetic family.
