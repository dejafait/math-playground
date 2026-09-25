# Birch and Swinnerton-Dyer conjecture: argument overview

The target is Wiles's official Clay rank assertion for every E/Q.
[The scope](foundations/01-target-and-scope.md) separates the stronger refinement. No candidate exists.
The [standard inputs](foundations/02-standard-inputs.md) include finite generation, analytic continuation, the analytic-rank-zero/one theorem, and Selmer and Kummer theory.

## Unresolved gap

For arbitrary E/Q with analytic order m(E) >= 2, the missing claim is
rank E(Q) = m(E). Finite Selmer sizes have a Tate–Shafarevich defect;
cyclotomic characteristic order has an additional augmentation defect.
The certificates remove defects conditionally; their uniform production and comparison with m(E) remain missing.
No checked generalised Kato construction supplies a nonzero rational
Kummer class from m(E) = 2 alone; a cycle-valued specialization is missing.

## Partial results

L001 gives the exact torsion-corrected size identity
\[
\log_p|\operatorname{Sel}_{p^n}|-\log_p|E(\mathbf Q)_{\rm tors}[p^n]|
 =n\operatorname{rank}E(\mathbf Q)+\log_p|\Sha[p^n]|.
\]
Finite-depth abstract towers match ranks zero and two, finite paired Sha,
and zero pulled-back pairings. Even parity and r <= 2 do not force r = 2.
No elliptic-curve realization or BSD counterexample is asserted.

Using the named theorems in [the cyclotomic foundations](foundations/03-cyclotomic-control.md),
L002 proves, at an odd good-ordinary prime,
\[
\operatorname{ord}_T f_X=\operatorname{rank}E(\mathbf Q)
 +\operatorname{corank}_{\mathbf Z_p}\Sha(E/\mathbf Q)[p^\infty]
  +\operatorname{length}_{\Lambda_{(T)}}(T X_{(T)}).
\]
The last term vanishes exactly when T X_(T) = 0. Control gives rank <=
Selmer corank <= characteristic order. Abstract modules with ideal (T^4)
have specialized dimensions two and four, both even; no arithmetic realization is asserted.

L003 applies [Schneider--Perrin-Riou](foundations/04-cyclotomic-height-criterion.md):
finite p-primary Sha and a nonzero canonical cyclotomic regulator give
ord_T f_X = rank E(Q), hence T X_(T) = 0. Equality with rank is equivalent
to finite p-primary Sha and the natural isomorphism X_(T)[T] -> X_(T)/T X_(T).
The converse retains finite Sha and non-CM E; no uniform hypotheses are supplied.

L004 uses [Kato divisibility](foundations/05-kato-divisibility.md) for non-CM E at good-ordinary p >= 5.
Given n independent rational points and a rigorously nonzero T^n coefficient of the primitive ordinary L_p,
\[
n\le r\le\operatorname{ord}_T f_X\le\operatorname{ord}_T L_p\le n.
\]
Both defects vanish, p-primary Sha is finite, and the cyclotomic height
is nondegenerate. With k < n points, only (r-k)+s+delta <= n-k follows.
Neither n = m(E) nor uniform availability of this certificate is established.

The [2016 audit](foundations/06-generalised-kato-scope.md) separates Selmer theorems from conjectural point membership;
the adjoint rank-(2,0) formulas predict at most one line from four stabilisations.
L005 proves that one nonzero strict rational Kummer class forces r >= 2:
the local logarithm has rank one on E(Q) tensor Q_p when r > 0.
A nonzero a_2 then reaches L004's r = 2 threshold.

[Castella--Hsieh's Theorem A](foundations/07-castella-hsieh-nonvanishing.md), under its auxiliary and residual
hypotheses, gives Selmer dimension two from nonzero kappa. L006 combines
this with L005: Kummer membership gives r = 2 and finite p-primary Sha
without a cyclotomic coefficient. That membership is not established.
Theorem B assumes positive rational rank and anticyclotomic theta order two; its bounds still allow (r, dim V_p Sha) = (1,1).
Neither theta order nor nonzero Kummer membership follows here from m(E) = 2.

The [construction audit](foundations/08-diagonal-cycle-specialization.md) leaves a motivic comparison missing.
L007, under its explicit classical accumulation hypotheses, shows that continuing
the ordinary tame-dual pairing forces crossed stabilizations; L006 uses a diagonal pair.
For the [normalized CM diagonal family](foundations/09-cm-diagonal-deformation.md), L008 obstructs
extending the fiber trace already modulo T^2, even with corrections involving V_p E.
Maps confined to the fiber or to an individual class remain outside that obstruction.

L009 uses [Selmer-complex duality](foundations/10-selmer-bockstein-duality.md) and the vanishing
of the auxiliary twist's Selmer space: the ordinary anticyclotomic Bockstein
vanishes on all of S, so d cup res_K(kappa) = 0 gives no Kummer criterion.
A strict class has a unique conjugation-invariant ordinary first-order lift;
it stays strict exactly when its local derivative in the one-dimensional D^- is zero.
That derivative's value and its relation to rational points remain unproved.

## Known traps checked

- The rank assertion differs from central vanishing and the refined formula.
- The zero/one theorem retains its analytic hypothesis; Selmer rank need not equal rational rank.
- A nondegenerate pairing on finite Sha does not make its p^n-torsion
  restrictions nondegenerate or give a stopping depth. The models vary
  with depth and respect eventual descent and independent-point certificates.
- Abstract models do not prove arithmetic realizability or BSD.
- Control's finite errors disappear over Q_p; characteristic length can still exceed dimension.
- Semisimplicity at (T), zero divisible Sha defect, and the complex/p-adic
  comparison are separate inputs, not consequences of control or cotorsion.
- Heights keep finite Sha and nonzero regulator explicit; the checked
  converse retains its non-CM restriction and gives no complex-order comparison.
- Kato gives an upper bound after inverting p; no reverse divisibility or
  p-adic BSD formula is assumed. Approximate zero is not certified nonvanishing.
- Strict Selmer need not mean Kummer. The 2016 Conjectures 3.2/3.12
  remain conjectures; the 2022 Section 5.7 assumes finite p-primary Sha.
  Triple-product values, theta orders, cyclotomic coefficients, and
  complex vanishing orders are distinguished throughout.
- A fiber trace need not lift; its obstruction is not non-Kummer membership of an individual class.
- Ordinary lifting need not preserve strictness; neither lifting condition is identified with Kummer membership.
