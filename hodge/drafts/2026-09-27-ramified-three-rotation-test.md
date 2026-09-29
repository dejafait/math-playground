# Ramified three-rotation lift: working calculation

## Scope and discriminating test

The saved SPECIALIZE assessment in `drafts/literature/2026-09-27-ramified-three-rotation-lift.md` predates this turn and matches its exact target. The central ideal is I_C intersect I_(C^(2))^2 intersect I_(C^(3)), with the full ordinary square at infinity. The ambient product is constant modulo tau^2, and its coefficient at tau^2 is a fixed direction in V_RM outside V_D. Every first-order embedded motion of the union is allowed.

The main local gap is an algebraic representative extending the non-scalar cubic RM action beyond the three-dimensional Dickson family. This test seeks an actual flat lift over C[tau]/(tau^3), or an obstruction excluding every allowed first-order motion. A specific cancellation with a bounded remaining compatibility check would justify continuation. Local algebra alone is below that threshold. Higher orders, algebraization, arbitrary fourfolds and higher dimensions remain separate unresolved steps.

The shared and local instructions, whole overview and DAG, current checkpoint, saved review, existing changes, and the relevant L007, L008, L014 and L015 arguments have been inspected. Existing work is preserved. The first-order obstruction is not assumed to persist automatically under ramification; normalized trace was only proved multiplicative over the dual numbers.

## Reasoning saved before completion

The assessed arbitrary-base cubic-algebra parametrization is the appropriate known input on separated thickened sheets. Its quadratic scalar terms can contribute at order tau^2 even when all structural parameters start at order tau. The first calculation must distinguish its intrinsic trace map from an actual graph section. Any nonzero trace defect must then be compared with the allowed embedding and complete-fibre conditions, not treated by itself as cancellation of the global obstruction.

Further possibilities to resolve within this same target: the global first-order motions may force those scalar terms to vanish in the base direction; alternatively the reduced branches may recover C at second order without a trace section. Neither assertion is established at this checkpoint. The full ideal at infinity and gluing have not been computed at second order.

## Compatibility mechanism saved during the calculation

The first-order trace centres extend across the mixed curves by L015's regularity formulas and across the isolated points by L008's normal-sheaf Hartogs property. The coefficient classification in L008, together with its generic rank-three family map, should also give H^0(N_(C^(j)))=0: in a fixed surface the four normalized coefficients can move only by Weierstrass scaling, and the quotient identifications have no infinitesimal automorphisms. This needs to be written out, including the intrinsic nature of the thickened component's first-order centre.

With these centres fixed, the first-order multiplication on a separated squared sheet is trace-free. It is a section of Sym^3(N) tensor det(N)^(-1). On a general complete elliptic fibre, N is the restriction of T_S. Its extension of O by O is non-split because the derivative of the j-map is nonzero. A Cech calculation for its third symmetric power leaves only the cube of the vertical tangent. Thus, in horizontal and vertical normal coordinates q,z, the only possible first-order products are q^2=qz=0 and z^2=tau*beta*q.

Associativity for an arbitrary second-order continuation of these products forces every second-order scalar coefficient to vanish. Consequently normalized trace becomes multiplicative at this order for these globally allowed motions, although it fails for general cubic algebras. At a mixed crossing the first-order ideal consequently has the form (z^2-tau*r*q*A,zq,rq^2). This admits a flat local reference lift over C[tau]/(tau^3) containing the fixed reduced branch. Differences from that reference are tau^2 times L015's full normal-module formulas, so the two displacement residues remain mu and mu/3. The fibre j-identities then force mu and the critical-value difference to vanish.

Outstanding verification at this checkpoint: spell out the rigidity and centre-gluing arguments, prove the reference ideal is flat, handle the reduced--reduced curves, and extend the recovered C (constant modulo tau^2) across infinity. Only after these checks can this mechanism exclude the requested lift. No general second-order trace theorem is being asserted.

## Completed assessment

The checks above are completed in [L016](../lemmas/L016-ramified-rotation-union-retains-obstruction.md). Its proof establishes rigidity from the full coefficient classification, checks the first-order centre under changes of tangential and normal coordinates, restricts the cubic tensor on complete elliptic fibres, proves the reference union flat by an exact sequence, and recovers C at order tau^2 through all remaining strata. The required lift does not exist for kappa in V_RM outside V_D. The allowed coefficient space remains three-dimensional against four required. This is a negative result for the specified representative and order, with no extension of the known cycle span.

The algebra script `scripts/cubic-deformation/check_ramified_trace.py` passes. It checks all independent order-two associativity constraints with symbolic sparse polynomials over Q, trace multiplicativity in the restricted algebra, the cubic tensor and residue rank, and an unrestricted example with trace defect -tau^2. It does not test the global geometric arguments. The general obstruction theory and cubic-algebra tables are imported from the prior assessment; the combined specialization is potentially beyond the checked sources, without an originality claim. No complete Hodge candidate exists.
