# Mixed extensions by the diagonal: saved first-order test

## Gap and discriminating target

The near-term gap is an algebraic representative of the cubic RM action that extends outside the three-dimensional Dickson family in the four-dimensional NS-fixed RM period locus. Arbitrary primitive fourfold classes and higher-dimensional cases remain unresolved. The proposed representative is a coherent extension

\[
0\longrightarrow\mathcal O_\Delta\longrightarrow\mathcal F
\longrightarrow\mathcal O_C\longrightarrow0
\]

on X=S x S. Its degree-four Chern character is [C]+[Delta], so a transverse sheaf lift could be useful for extending U+id and eventually subtracting the diagonal. First-order lifting would still leave higher-order extension, algebraization, and coverage of other varieties open.

Compute Ext^1_X(O_C,O_Delta), then test all its extension classes. Continue if an extension actually lifts transversely or a concrete obstruction-cancellation mechanism survives. Stop these extensions if every sheaf lift recovers a lift of C. The required first-order kernel has dimension four; dimension three does not improve the known family.

## Redundancy and initial reasoning saved

The entire overview and DAG, the uncommitted L012 work, and the preceding union failures have been inspected and are preserved. L009 treats embedded lifts of the reduced union; L012 treats sufficiently negative syzygies. Neither already proves that a lift of an arbitrary extension sheaf preserves its support or filtration. That missing passage is the point of this test. The Clay page and Deligne's section 1 were rechecked on 2026-09-25 and retain the rational, smooth projective target in foundations/01-target-and-scope.md.

The two finite intersection curves have local ideals I_C=(z,s), I_Delta=(z,r) in C[[r,s,z,w]]. The Koszul calculation suggests that sheaf Ext^1(O_C,O_Delta) is O_D(D) on each diagonal elliptic fibre D, with no Hom sheaf. The two normal bundles are trivial. At each isolated point at infinity, use 0 -> O_C -> O_A direct sum O_B -> k -> 0 for the two transverse branches. The potentially contributing Ext^2(k,O_Delta) -> Ext^2(O_A direct sum O_B,O_Delta) must be checked for injectivity before claiming there is no punctual Ext^1.

A nonzero local extension on a finite double curve should be cyclic, whereas a zero local extension is split. For a cyclic central module, flatness and Nakayama recover a flat embedded support locally. For a split central module, the diagonal blocks of its Yoneda self-extension determine the two support displacements away from the crossing; the mixed blocks vanish on that complement. This may show that the diagonal branch has at most the same simple normal poles as in L009, after which its nodal-fibre zero count forces it to stay fixed. Extracting C must then be justified separately at cyclic and split points, and across the three isolated points using the known Hartogs property of N_C.

These are proof obligations, not established conclusions at this checkpoint. In particular a Fitting support is not assumed flat, and no lift of the extension filtration is assumed. Exploration turns used before this step: 0.

## 2026-09-26 — Calculation saved before the full write-up

The existing uncommitted notebook work, including this draft and L012, was read and retained. The primary rational target was checked again against Deligne's section 1. The local Koszul calculation gives Ext-sheaf degree one equal to the normal line of each D in Delta, hence trivial on each of the two elliptic fibres. At an isolated triple point, Ext^2(k,O_Delta) -> Ext^2(O_P direct sum O_Q,O_Delta) is injective: use coordinates with Delta=(x_1,x_2), P=(y_1,y_2); the P component is the identity on the top y-Koszul class. Thus no isolated Ext^1 remains, and the global mixed extension space is C^2.

Each extension is cyclic along a fibre whose coordinate is nonzero, and locally split along a fibre whose coordinate is zero. This dichotomy is stronger than the initial draft's uncomputed possibility. For a flat lift of a cyclic module, a lifted generator gives an actual flat quotient support. At a split point, the four blocks of Ext^1(M direct sum N,M direct sum N) show that the two diagonal blocks extend the branch supports regularly; mixed blocks vanish after restriction away from the other branch. This does not split the lifted sheaf or preserve its filtration.

The resulting diagonal displacement therefore has at most the same simple base-direction poles as in L009. Its base projection has degree at most four and 21 nodal zeros, forcing the displacement to vanish. At cyclic points the flat residual gives C; at split points its self-extension block does so. These local supports agree off the intersection and hence glue on the smooth part of C. L008's normal-sheaf Hartogs property fills the three isolated points. The remaining write-up check is the converse for every extension class: in a Dickson-family lift the same relative Ext calculation gives A^2, whose reduction surjects onto C^2. The intended result is a three-dimensional kernel for every tested extension, against four required; no global Hodge candidate is suggested.

## Completed assessment

[L013](../lemmas/L013-mixed-diagonal-extensions-retain-cubic-obstruction.md) completes both directions. Its converse computes the relative Ext group over A explicitly and lifts every e; it does not assume Ext base change. The Atiyah obstruction criterion for perfect complexes applies to A-flat coherent sheaves here, with the passage between the two lifting notions justified. The result is NEGATIVE for this mechanism: the nonzero mixed extension space never supplies a fourth RM direction. This is new information beyond the embedded-union and syzygy tests. The main algebraicity gap and the known 21-dimensional family span are unchanged. Exploration turns used are 0 after this informative negative result.

## Mathlib

Coverage of the full mixed-extension statement: **not checked**. The full proof and the distinction between supporting sources and a match for this statement are in L013. The supporting Atiyah criterion is [Huybrechts--Thomas, Corollary 3.4](https://arxiv.org/pdf/0805.3527#page=14); it does not compute the mixed Ext group or the obstruction kernel in this example.
