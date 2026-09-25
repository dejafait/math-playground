# 2026-09-25 — First-order deformation of the cubic correspondence

## Gap, target, and discriminating test

The unresolved local gap is extending the cubic RM action from the three-dimensional Dickson-cover family to its four-dimensional RM period locus, with the Néron–Severi lattice fixed. The universal primitive fourfold gap and all higher-dimensional cases remain. The intermediate target is the first-order lifting condition for the support of C_1 from L006 in a diagonal deformation of S x S. Its plausible use is to decide whether deforming this particular algebraic correspondence can supply the missing RM direction.

The required test is a geometric obstruction calculation, not just preservation of Hodge type. Vanishing of the actual obstruction in a transverse RM tangent direction would justify studying higher-order lifting and algebraization. A nonzero obstruction would stop this representative; a precise failure of a proposed obstruction calculation would narrow the deformation problem without settling it. Full cycle-class surjectivity still requires the three-dimensional transcendental field (21 total Hodge dimensions when rho = 4), not merely a tangent-space statement.

## Existing work and sources

Read the shared/local rules, whole overview, DAG, existing local changes, the full L006 construction, its family input and saved assessment, and Attempts 001–003. Preserve the existing results and inactive branches. The divisor and isometry failures do not test deformations of a nonisometric cover correspondence. This is the first deformation-obstruction step, with no outstanding exploration streak. Rechecked the Clay page and Deligne's rational target on 2026-09-25.

## Unfinished reasoning saved before detailed work

On the dense chart, C_1 is parameterized by (x,y,v) with t = v+a/v and s = zeta v+zeta^(-1)a/v. The pair (t,s) determines v, so the pushforward has generic multiplicity one. Its base image is the conic t^2+s^2-(zeta+zeta^(-1))ts+a((zeta+zeta^(-1))^2-4) = 0. The projective closure and its behavior over the elliptic fibre at infinity must be checked before using a normal bundle for a smooth embedded surface. The smooth resolution W used to define a cycle is not automatically its embedded support.

A vanishing infinitesimal Hodge variation is necessary along an RM-preserving direction. It does not by itself compute the embedded obstruction; a semiregularity argument needs both the correct geometric hypotheses and an injectivity statement. The next calculation in this step will inspect the support at infinity and specify what first-order deformation theory actually applies. No vanishing or nonvanishing obstruction is claimed at this save point.

## Intermediate calculation saved

At the zero section over t = infinity use u = 1/t and the fibre parameter z = -X/Y, with X = u^4 x and Y = u^6 y. In the second factor use w = 1/s and z'. On the correspondence z' = (u/w)^2 z. The two preimages of t = infinity are v = infinity and v = 0, both unramified for the degree-two base map. The two branches have tangent matrices diag(zeta^(-1), zeta^2) and diag(zeta, zeta^(-2)) as graphs over the first S. Their difference is invertible. Hence the reduced support has a transverse two-branch surface singularity at the pair of zero-section points.

The proposed local model is R/I with R = C[[r_1,r_2,s_1,s_2]] and I = (r_i s_j : 1 <= i,j <= 2). The four independent quadratic generators rule out a codimension-two local complete intersection. For the first-order normal module, a homomorphism I -> R/I appears to have the unique form r_i s_j -> r_i A_j(r) + s_j B_i(s). This would identify it with C[[r_1,r_2]]^2 direct sum C[[s_1,s_2]]^2, and every such deformation would come from an ambient derivation. These assertions and the global Cech lifting criterion are being checked; the global obstruction in a transverse RM direction has not been evaluated.

## Completed assessment

[L007](../lemmas/L007-cubic-correspondence-deformation-model.md) proves the two-branch local model, the normal-module formula, and the exact global first-order ideal-gluing criterion. The two graph branches exhaust the support near the chosen point because the first projection comes from an unramified two-sheeted base change there. The nonzero determinant is exact. Four generators are required, whereas a codimension-two regular embedding would require two. The normal sheaf has fibre dimension four there, not two. All its local first-order parameters are induced by ambient coordinate changes; this prevents misreporting the singularity as a nonzero deformation obstruction.

The smooth-subvariety version of semiregularity cannot be used for this support, and replacing it by the smooth source of the pushforward does not remedy the embedding hypothesis. Ran, [Theorem 0, pp. 809–810](https://www.numdam.org/article/ASNSP_1999_4_28_4_809_0.pdf#page=2), retains that hypothesis. Singular versions are available in Buchweitz–Flenner, [Theorem 7.8 and Remark 7.11(1)](https://arxiv.org/pdf/math/9912245#page=50); their obstruction-space and injectivity conditions are not established for C here. This is a restricted failure of the normal-bundle shortcut, not a ban on semiregularity or cycle deformations.

The actual first-order class is ob_C(kappa) in H^1(C, Hom(I_C/I_C^2,O_C)), obtained by restricting the ambient Kodaira–Spencer cocycle and applying derivations to the ideal. Its vanishing is equivalent to a first-order flat embedded lift; the lemma proves this by explicit local ideal gluing without any lci assumption. Its value on the fourth RM direction is still unknown. Hodge preservation along that direction only settles the cohomological condition. No cycle has been transported to an additional surface, so the achieved cycle span remains 21 only on the already treated family. Higher-order lifting and algebraization remain independent later requirements.

Outcome: NEGATIVE, because a precise geometric failure changes the proposed deformation method. Exploration turns used: 0 after this informative result. The continuation decision is to use the actual normal sheaf and its global gluing, rather than repeat a smooth-support test. The mathematical input from L006 is its correspondence and cohomological action; L007 adds no dependence on the earlier isometry or divisor-product failures. Mathlib coverage is not checked. The supporting exact local checks passed with `python3 scripts/cubic-deformation/check_local_model.py`; they do not evaluate the global obstruction.
