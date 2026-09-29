# Unfiltered rotation-extension test — saved reasoning

The saved target and SPECIALIZE assessment are in [the source review](literature/2026-09-27-three-rotation-sheaf-extensions.md). This research step retains exactly that target. Existing work was read and preserved.

## Relevance and discriminating test

The gap is the missing transverse direction in the four-dimensional cubic RM tangent space. For K=O_(C^(2))^2 and Q=O_C direct sum O_(C^(3)), Chern-character additivity gives generic multiplicities 1,2,1. The rotation actions recorded in L015 give the prospective action U^2-3 id, which is non-scalar. This passes only the relevance test, not the obstruction test.

Try to extract an embedded lift of C from any unfiltered middle-sheaf lift. A transverse sheaf lift would justify further work on higher orders and algebraization. If every such lift recovers C, L008 excludes the transverse direction and stops this representative class. No automatic lifting of the filtration, flatness of a Fitting support, or vanishing inferred from Hodge persistence is allowed.

## Reasoning saved before the full calculation

At a finite C^(i)--C^(2) crossing, put M=R/(z,r), N=R/(z,q). The Koszul calculation gives sheaf Ext^1(M,N)=O_D in the base-coordinate trivialization. Its two-copy extension coordinate is a constant vector on the complete elliptic curve D. Locally a nonzero vector gives R/(z,rq) direct sum N; a zero vector gives M direct sum N^2. At C--C^(3) crossings, K vanishes and the middle module is already the direct sum of its two quotient branches.

For a deformation of a rank-m module on a separated graph, ambient functions reduce to scalar matrices. Their normalized traces multiply to first order, providing a graph centre without an algebra structure on the original module. At a nonsplit mixed crossing, the union self-extension block could have smoothing residue mu. The remaining N self-extension block is regular, so the tentative residue of the rank-two centre is mu/2, versus mu on the rank-one branch. Off-diagonal blocks must be retained and checked to have zero trace after restricting to the separated branches.

If the two complete-fibre graph centres satisfy the necessary j-invariant relation, these residues give d+H mu=0 and d+H mu/2=0 at a critical pair, with H nonzero. This would force mu=d=0. At split crossings the rank-one self-extension block already extends regularly. A recovered C off infinity would extend across its three punctures by L008's normal-sheaf Hartogs property.

The steps above remain to be justified fully. In particular, do not substitute the ordinary-square rank-three algebra from L015 for this rank-two module. At infinity both structure sheaves are singular; L013's smooth-target Ext calculation cannot be reused without change. The provisional local analysis predicts one punctual mixed Ext^1 class per point, in addition to four finite-curve classes for each ordered rotation pair. Check the connecting maps before recording any dimension or a reverse kernel inclusion.

At this intermediate save, no conclusion about a transverse lift or the full global extension space had been adopted.

## Completed calculation

[L017](../lemmas/L017-rotation-sheaf-extensions-retain-obstruction.md) resolves the saved questions. Each mixed pair has four curve classes and three point classes, so the total extension space has dimension 28. The point calculation uses both normalization sequences and verifies its connecting maps; the smooth-target calculation of L013 would miss these classes. All classes lift along V_D by relative Ext computations.

For necessity, first-order scalar-reduction module trace is multiplicative on each separated rank-two sheet. At a nonsplit crossing the self-extension blocks give residues mu and mu/2, while arbitrary mixed blocks have zero trace. The common j-relation forces mu=0. Split cases already give regular rank-one block lifts. These recover C away from infinity, and its normal-sheaf Hartogs property fills the punctures independently of all point parameters. Thus every middle sheaf has kernel exactly V_D, of dimension three against four required, despite the non-scalar U^2-3 id action.

The result is NEGATIVE for this representative class. The prior SPECIALIZE review is unchanged. General deformation tools are imported; the specific mixed Ext and residue calculation was not matched by the checked sources, without a certified novelty claim. The full proof is kept only in L017. Exact supporting checks are in `scripts/cubic-deformation/check_rotation_sheaf_extensions.py`.

## Mathlib

Coverage: **not checked**. The source review identifies the supporting obstruction criterion and local-to-global Ext framework. They do not provide the proposed mixed-module calculation.
