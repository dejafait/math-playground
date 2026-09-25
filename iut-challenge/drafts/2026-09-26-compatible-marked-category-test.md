# Compatible marked category test — 2026-09-26

Initial reasoning was saved before completion. This one review and mathematical test of the local-global compatibility obligation is now complete. Existing unfinished changes and the exhausted historical exploration sequence are preserved; no runner state is changed.

## Gap, intermediate target, and test

The exact gap is finite B ≥ A in IUT III, Corollary 3.12(xi-f). The intermediate target is to distinguish a category whose morphisms respect localization from an object equipped with a global marking to the output determinant. The proposed use is to type the additional datum that could make a transported q-pilot yield a degree comparison, without imposing an ordinary global scalar as necessary for IUT.

The test fixes an output arithmetic line D and forms the category of globally defined arithmetic lines with local marking orbits into D, allowing only global morphisms whose localizations preserve those orbits. Does this compatibility axiom force all objects to have degree at most d(D), or does it merely separate objects according to the total marking defect? A forced bound would support checking this axiom during transport. Unbounded degrees would reject compatibility of morphisms, by itself, as an adequate replacement for marked transport; an invariant separating the component of D would give a more precise subsequent test.

The original q-pilot, realified Frobenioids, formal quotient, log-Kummer transport, and all permitted hull images remain to be related to any model. Failure of that relation in this notebook is not an IUT contradiction.

## Redundancy and source check

L004 already proves the local defect inequality and a counterexample to local-marking sufficiency. Repeating the absence of a global scalar would add nothing. The new question is categorical: does imposing the localization compatibility axiom on *all morphisms* remove bad-degree objects or connect their markings to the determinant's identity marking? L001–L003 and ATTEMPTS/001–004 do not test this question.

The [official announcement](https://zen.ac.jp/news/0ul6zqed9-0) and [current prize page](https://zen.ac.jp/en/lp/icp) were rechecked today with unchanged scope. The author-hosted IUT III remains the 199-page May 2020 PDF.

The [source record](../foundations/02-comparison-claim-and-sources.md) now distinguishes the (cQ3) morphism condition from existence of a global marking to the determinant. The prior notebook's localization equation is a sufficient extra lifting test in its ordinary realization. It is not a restatement of the listed object data. This distinction does not rule out a degree comparison supplied by the full formal construction.

## Completed calculation

The full proof is [L005](../lemmas/L005-compatible-marked-categories-and-defect-components.md). For fixed D, the model category has objects (Λ,[c_v]) with c_vΛ_v ⊆ D_v and allows only genuine global morphisms preserving those local marking orbits. The product formula makes Δ invariant under every such morphism and every finite zigzag.

More precisely, its connected components are exactly the fibers Δ = δ. The degree range of the component δ is (−∞, d(D) − δ], with its upper endpoint attained. Every object of that component has an arrow to an explicit object with that endpoint degree. The component of the identity-marked D is δ = 0; membership in it is equivalent to admitting an arrow to D. The entire category, with the compatibility axiom imposed on every morphism, nevertheless has object degrees ranging over all ℝ.

This corrects a possible reading of the previous review. The L004 example does not violate a morphism axiom merely because no comparison arrow to D exists. It is a legitimate object of this ordinary compatible category, in a different component from D. The earlier conclusion that local markings do not suffice remains valid; the stronger claim that the category's compatibility axiom itself excludes the example does not follow. No assertion is made that L004 instantiates the full IUT data.

## Assessment against the required bound

The model gives A + δ ≤ B, sharply in every component. The required inequality A ≤ B follows uniformly for a component only when δ ≥ 0. For δ < 0 the top object has A = B − δ > B. Merely insisting on compatible global arrows *whenever arrows exist* does not select the component or improve this bound. A particular object with δ < 0 could still satisfy A ≤ B; neither zero defect nor a global arrow is asserted necessary for that object's inequality.

Outcome: NEGATIVE for treating the compatibility axiom as a sufficient numerical test. This is new evidence about a stronger proposed replacement than the local-marking existence test: the model enforces the global arrow axiom throughout and identifies its exact remaining component parameter. It also qualifies an overstatement in the preceding notebook assessment. It is not a negative verdict on IUT.

The actual finite B ≥ A remains unestablished and unrefuted. Connecting the model to the source still requires control of realification, the noncanonical localization isomorphisms, the admitted morphisms, and the formal quotient on the distinguished q-pilot. A finite zigzag in this ordinary category is not being substituted for that quotient. The reason for the subsequent direction is to determine what becomes of the defect under the source's realified localization formalism, before trying to use it to test q-pilot transport. The sole current action is in PROGRESS.md.

The historical exploration sequence remains 3/3, assessed. This informative negative review is not a fourth unassessed exploration turn, and no runner-state change or renewed exploration allowance is claimed. No complete candidate exists.

## Checks and limits

The mathematical checks were the identity/composition laws, orbit invariance, the product formula, the explicit rational lift including its real absolute value, and attainment of every degree in the stated intervals. These exact computations required no numerical experiment. L005 uses L004 for the defect inequality and product formula; its single new DAG edge records that mathematical input. Mathlib coverage is **not checked**. Documentation validation is recorded in the dated history after execution.
