# Ramified second-order lift of the ordinary-square union: literature assessment

TARGET: Compute whether I_C intersect I_(C^(2))^2 intersect I_(C^(3)) admits a flat embedded lift over C[tau]/(tau^3) with ambient deformation constant modulo tau^2 and a transverse RM term at order tau^2.
CHECKED: 2026-09-27
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched higher-order embedded obstructions, ramified K3/RM correspondences, semiregularity and cubic-algebra trace; followed Miranda's domain restriction to Wood's arbitrary-base theorem and Poonen's explicit parametrization. Queries, versions, inspected statements and reused comparisons are recorded below.
SOURCE_EVIDENCE: Buchweitz--Flenner (2003), Lemmas 7.6--7.7 and Theorem 7.8, pp. 190--191, https://www.cambridge.org/core/services/aop-cambridge-core/content/view/712BFB5F73E0C38B4B32206699B0277F/S0010437X03100413a.pdf/a-semiregularity-map-for-modules-and-applications-to-deformations.pdf#page=56; Poonen (2008, author version corrected 2022), Proposition 5.1, PDF pp. 5--6, https://math.mit.edu/~poonen/papers/moduli.pdf#page=5; Wood (2011), Theorem 2.1 and equation (1), pp. 1073--1074, https://msp.org/ant/2011/5-8/ant-v5-n8-p05-p.pdf#page=6.
COMPARISON: Relative obstruction theory covers nonreduced closed subspaces, and cubic-algebra parametrizations cover nilpotent bases; neither computes the prescribed union's global ramified lift. L015's first-order component recovery does not evaluate the obstruction for arbitrary first-order subscheme motions.
GAP: Evaluate the relative embedded obstruction for an allowed first-order motion in the fixed product against the specified transverse ambient term at order tau^2, retaining the mixed crossings, gluing and full ordinary-square ideal at infinity.
REASON: Import the known obstruction framework and algebra parametrizations; specialize only their compatibility with this embedding. Neither abstract cubic-algebra smoothness nor persistence of the cycle's Hodge type supplies the required global lift. The checked literature leaves this bounded test open without establishing novelty.

## Hypotheses

The central scheme is exactly the one in L015, with the ordinary square of the entire second rotation ideal, including infinity. Both factors have the same NS-fixed RM deformation over C[tau]/(tau^3), trivial modulo tau^2. Its coefficient of tau^2 is a fixed direction in V_RM outside V_D. The subscheme is allowed arbitrary first-order embedded motion in the fixed product modulo tau^2; its reduction, components and nilpotent filtration need not lift.

Write A_1=C[tau]/(tau^2) and A_2=C[tau]/(tau^3). The question concerns a flat closed subscheme over A_2 extending some allowed motion over A_1, not only the constant motion. The ordinary square is not replaced by a symbolic square, squares of separate branches, or a ribbon.

Reuse the rational target formulation and source-scope check of 2026-09-27 in the [first-order assessment](2026-09-26-three-rotation-thickening.md) and the [target audit](../../foundations/01-target-and-scope.md). The universal goal is still rational cycle-class surjectivity for every smooth projective complex variety. No target hypothesis has changed.

## Conclusion

SPECIALIZE: the supporting machinery is known and should be cited; its evaluation on this global embedded union is not supplied by the inspected results. Keep the exact saved target for a later research turn. This review computes no second-order obstruction, trace defect, cancellation or lift.

The gap remains a non-scalar cubic RM representative extending beyond the Dickson family. L015 already checks this cycle's relevance and gives a first-order kernel of dimension three against four RM directions. The new threshold is an actual global A_2 lift with the fixed nonzero transverse coefficient, allowing first-order subscheme motion. It is not a claim that a ramified lift enlarges the first-order kernel. The achieved 21-dimensional cycle span on the known family is unchanged. Even success here would leave higher orders, algebraization, extension to actual transverse surfaces, arbitrary fourfolds and higher dimensions unresolved.

This completed review is LITERATURE / NOVELTY_UNCHECKED / EXPLORATION. Known supporting results are imported by citation; no result for the target is reproduced or established beyond those sources. The search does not certify originality. It uses one exploration turn after the informative negative result in L015.

## Proof

The evidence below consists of inspected source statements and applicability comparisons, not a proof of the proposed lift or its impossibility.

### Relative embedded obstruction theory

Reread Buchweitz--Flenner, *A Semiregularity Map for Modules and Applications to Deformations*, Compositio Mathematica 137 (2003), 135--210, [section 7.2, Lemmas 7.6--7.7 and Theorem 7.8, pp. 190--191](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/712BFB5F73E0C38B4B32206699B0277F/S0010437X03100413a.pdf/a-semiregularity-map-for-modules-and-applications-to-deformations.pdf#page=56). For flat closed subspaces in a flat ambient family, tangent data are Hom(I_Z,O_Z tensor N), and extension obstructions belong to T^2_{Z/X}(O_Z tensor N). This framework allows a nonreduced subspace over an Artinian base; it is not restricted to lifting the central fibre once. Thus it supplies the criterion for extending a chosen Y_(A_1) from A_1 to A_2. It does not evaluate that criterion for Y. Theorem 7.8 additionally requires injectivity of semiregularity and gives smoothness over a closed subspace of the ambient base, not automatically the whole base. These are supporting results. Applying the criterion only to the constant Y_(A_1) would omit motions permitted by the target. No replacement of the full obstruction group by H^1 of a normal bundle is justified here.

### Cubic algebras: known tools, including nilpotent bases

Read Miranda, *Triple Covers in Algebraic Geometry*, American Journal of Mathematics 107 (1985), 1123--1158, [section 2, Lemmas 2.2, 2.4 and 2.6, Theorem 2.7, pp. 1124--1127](https://www.math.colostate.edu/~miranda/preprints/TripleCoversInAG.pdf#page=3). The trace decomposition and multiplication tables exhibit scalar coefficients quadratic in the structural parameters. However, the setup and necessity argument use integral domains, including fraction-field reasoning. The saved nilpotent base does not meet that hypothesis. This is a useful comparison, not an unrestricted theorem to apply to A_2. No parameter substitution or trace calculation for Y is made here.

Read Wood, *Parametrizing quartic algebras over an arbitrary base*, Algebra & Number Theory 5 (2011), 1069--1094, [section 2, Theorem 2.1 and equation (1), pp. 1073--1074](https://msp.org/ant/2011/5-8/ant-v5-n8-p05-p.pdf#page=6). Despite the title, this section treats cubic algebras: it gives the equivalence with binary cubic forms over arbitrary schemes, compatible with base change, and an explicit multiplication table in a normalized basis. No reducedness or domain hypothesis is imposed on the base. This resolves the scope issue for nilpotent bases. The table is available as a cited input on separated rank-three sheets; it does not specify their embedding, supply a multiplicative trace retraction, or glue them through the union's crossings.

Followed Wood's reference and read Poonen, *The moduli space of commutative algebras of finite rank*, J. Eur. Math. Soc. 10 (2008), 817--836, [author version dated 4 June 2008, corrected 29 July 2021 and 5 August 2022; Definitions 1.4--1.5 and Proposition 5.1 with proof, PDF pp. 2--3 and 5--6](https://math.mit.edu/~poonen/papers/moduli.pdf#page=5). The moduli scheme of based rank-three algebras with first basis vector 1 is A^6 over Z. Its proof gives four multiplication parameters in a normalized basis plus two basis translations. This covers the abstract algebra problem over arbitrary rings, including the square-zero algebra identified in Definition 1.4. Re-deriving that parametrization would reproduce known mathematics. It is not a theorem about the entire rotation union or the two projections to the deforming K3 surface.

Also checked the two relevant entries in Poonen's [*Remarks and errata*, dated 14 August 2025, pp. 2 and 5](https://math.mit.edu/~poonen/papers/errata.pdf#page=2). They concern the proofs of large-rank bounds in section 11 and the group in Remark 6.9, not Proposition 5.1. The inspected author version records its corrections.

The applicability judgment is consequently limited: import the algebra classification, and compute only the extra embedding and compatibility conditions. The smooth parameter space of a based algebra is not evidence that this prescribed global embedded subscheme lifts. In particular, a module projection obtained from trace must not be treated as a scheme section without establishing multiplicativity to the required order.

### Stronger lifting comparisons and reuse

Reuse the theorem-level comparison in the [two-rotation assessment](2026-09-26-current-target.md) of Pridham, *Semiregularity as a consequence of Goodwillie's theorem*, [arXiv:1208.3111v4, 4 November 2024, Corollaries 2.22 and 2.25 and Remark 2.27, pp. 18--20](https://arxiv.org/pdf/1208.3111v4#page=18). Its square-zero-extension statements concern perfect complexes and the image of their obstruction under semiregularity, including the horizontal Chern-character obstruction. They do not supply injectivity here or recover a flat embedded quotient from a perfect-complex lift. The arbitrary-extension scope was already inspected; a first-order-only reading is not the reason it fails to settle this target. No new reading of that paper is claimed today.

Also reuse the [first-order assessment](2026-09-26-three-rotation-thickening.md) for the inspected rope and multiple-structure smoothing statements and their direct primary citations. Their smooth-support, conormal, cover and ambient hypotheses have not become true merely by changing the Artinian base. A smoothing in projective space does not give containment in the specified product. These comparisons do not need a new search for the same hypotheses.

The family comparison is reused from the [cubic-family audit](../../foundations/05-cubic-rm-family.md) and the previous assessments: van Geemen--Schutt, *On families of K3 surfaces with real multiplication*, Forum of Mathematics, Sigma 13 (2025), e2, [sections 4.8--4.9 and 5.3--5.4, pp. 13--15](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/26D90B781A518CB95969B4473C8852C8/S2050509424001464a.pdf/on-families-of-k3-surfaces-with-real-multiplication.pdf#page=13). These provide the correspondence and family dimensions, not this thickened union's ramified deformation. The already reviewed broader algebraicity statements retain their recorded hypotheses; no universal cubic-RM deformation theorem is imported.

For redundancy, read the overview, L015's statement and relevant first-order trace setup, the [saved first-order calculation](../2026-09-27-three-rotation-thickening-test.md), [attempt 012](../../ATTEMPTS/012-ordinary-square-three-rotation-union.md), and [history 017](../../history/017-2026-09-27-three-rotation-thickening-test.md). The earlier reduced unions, fibre additions and sheaves failed for their specified representatives. This target changes the order at which the ambient deformation appears and allows a subscheme motion at the preceding order. Its distinguishing test is that interaction, not a repeat of the computed first-order kernel. The earlier stops remain valid in their stated scopes.

### Search record and access boundary

Queries on 2026-09-27 included:

- `embedded deformations second order obstruction quadratic Hilbert scheme differential graded Lie algebra Iacono Manetti`
- `finite flat algebra rank three trace deformation square zero second order Miranda triple covers`
- `semiregularity ramified deformation algebraic cycles higher order obstruction Buchweitz Flenner`
- `"K3" "real multiplication" "ramified" correspondence deformation`
- `"cubic algebras" "arbitrary base" "Wood"`
- `"embedded deformations" "quadratic" "obstruction" "nonreduced"`
- `"K3" "real multiplication" "higher order" deformations correspondence`
- `Poonen "moduli space of commutative algebras" "5.1"`
- `"K3" "Dickson" "second order"`
- `"ramified" "deformation" "algebraic cycles" Hodge`
- `"trace" "cubic algebra" "nilpotent" deformation`
- `"real multiplication" "correspondence" "thickening" K3`
- `"ramified" "Hilbert scheme" "Hodge" deformation`

The exact-geometry searches did not locate an inspected theorem deciding this lift. The algebra search yielded the primary statements read above; following references resolved the nilpotent-base scope issue. Search leads for Manetti's higher-obstruction papers, Iacono--Manetti on complete intersections, and recent local-equation papers on punctual Hilbert schemes were not read at theorem level and are not inputs. Deligne's letter and the original Delone--Faddeev reference behind the cubic parametrization were not independently read; the explicit arbitrary-base statement and Poonen's proof were inspected. The previously recorded unread Friedman original is not an input. No essential inaccessible source remains for the selected supporting framework. This is a bounded comparison, not an exhaustive classification of the literature.

### Bounded specialization and stopping test

The saved computation should import the general theory and retain these obligations:

1. Allow every relevant first-order embedded motion in the fixed product. Use the known rank-three algebra tables on separated sheets without assuming that trace is multiplicative or that a central reduction or nilpotent filtration persists over A_2.
2. Impose the actual embedding, crossing and overlap conditions for the specified ideal and ambient deformation. Establish any component recovery, flatness or fibre identity used; do not extend identities from the reduction without justification. Keep the full ordinary-square ideal at infinity.
3. Test whether the resulting global obstruction can vanish for the prescribed transverse term. A local algebra or a count of parameters alone is below the required threshold.

Continue this mechanism only on an actual flat A_2 lift, or on a specific surviving cancellation with a bounded, explicitly named remaining compatibility check. Stop it if the global conditions force recovery of C in the prohibited direction or exclude every allowed first-order motion. Failure for one arbitrarily chosen motion is insufficient. Even a successful second-order lift would not settle higher-order extension or algebraization. Complete the continuation/stop assessment within the shared exploration budget; this review does not reset that budget.

The initial REVIEW_REQUIRED record proposed the possible interaction of first-order nilpotent motions with a later ambient obstruction, and asserted no cancellation. That motivation and exact target are preserved. Source notes were saved while the review was in progress; the pending Poonen reference has now been read. The completed decision is recorded in [history 018](../../history/018-2026-09-27-ramified-three-rotation-literature.md).

## Mathlib

Coverage: **not checked** for the full ramified embedded-lifting target or the supporting obstruction and cubic-algebra results. No matching theorem or absence from Mathlib is asserted. The named primary citations above are supporting mathematical references, distinguished from a match for the full target.
