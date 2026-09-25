# 2026-09-25 — Testing the cubic support after adding the diagonal

## Gap, intermediate target, and decision test

The near-term gap is extending the algebraic cubic RM action to the fourth NS-fixed RM tangent direction. The intermediate target is the first-order embedded lifting test for the reduced union Y = C union Delta_S in S x S. Its cycle acts by U+id; a successful algebraic extension would recover U by subtracting the diagonal. First-order vanishing would only justify higher-order and algebraization work, and would not settle arbitrary K3 self-products, arbitrary fourfolds, or higher codimensions.

The required threshold is vanishing in all four RM tangent dimensions, compared with the three-dimensional Dickson-family tangent already available. A nonzero transverse obstruction would stop this representative. A genuine new local smoothing parameter alone is less than the required global lift and must be reported as such.

## Prior evidence and preserved work

Read the shared and local goals, shared prompt, complete overview and DAG, existing changes, the current checkpoint, L006–L008, and Attempts 004–005. The earlier obstruction applies to C alone: its isolated surface crossings force a simultaneous normalization with two double-cover involutions. Adding the diagonal is a changed geometric representative, not a repetition of that test. Its intersections must be determined before reusing any normalization argument. All existing work and stopped branches are retained.

## Reasoning saved before the calculation

On the finite Weierstrass chart, C meets the diagonal when t=s, equivalently v^2=a/zeta. Each root gives an entire elliptic fibre rather than an isolated point. The generic local union should therefore have two smooth surface branches meeting along a curve, with possible node-smoothing directions. At infinity the diagonal passes through the three double points of C, producing three-branch intersections. The outstanding test is whether these curve gluings and their global compatibility can remove the first-order obstruction, or whether a quotient/trace argument still extracts an obstructed lift of C. No outcome is asserted yet.

## Global extraction argument saved before final write-up

The two finite intersections are smooth elliptic fibres F_+ and F_-. Near either, the two components have ideal (z,rs), with Delta given by (z,r) and C by (z,s). A first-order lift has equations z=epsilon a and rs=epsilon b. Away from the double curve its diagonal branch is a graph over the first S_A. Comparing its second projection with the identity defines a vector field v on S minus F_+, F_- and the three fixed points at infinity. In coordinates s=2u on Delta its displacement is b_Delta/(2u) in the base direction and a_Delta in the fibre direction. Thus v extends to T_S(F_++F_-), with any possible pole normal to the elliptic fibre.

Projection to the elliptic base is a section of T_P1(t_++t_-), of degree four. It vanishes at every finite nodal singular value, since the differential of the elliptic map vanishes at the node and v is regular there. There are 21 such values at very general parameters, so this section is zero. Consequently the local smoothing residues vanish and v extends over the two fibres; Hartogs handles the three isolated points. H^0(S,T_S)=0 then forces v=0. Every global embedded lift therefore contains the actual relative diagonal, including over infinity by vanishing on a dense open set.

Off the three isolated points, the residual ideal is flat: after absorbing multiples of z, containment of the diagonal puts the local union ideal in the form (z-epsilon r alpha, r(s-epsilon beta)). Its colon by (z,r) is (z-epsilon r alpha, s-epsilon beta), a lift of the smooth C branch. At the isolated points one need not assume normalization or residual flatness for a three-branch singularity: L008 gives N_C=nu_*N_j with N_j locally free on the smooth normalization. Sections of N_C extend uniquely across these points by Hartogs. In a local trivialization of the ambient deformation, the punctured residual lift is such a normal section; extending it gives a flat C lift. These extensions glue uniquely.

This proves that any lift of the union yields a lift of C. For the reverse kernel inclusion, the Dickson family supplies a flat union: the two curve crossings are relative node models, and finite-order linearization at each fixed point makes the three graphs id, f, f^(-1) a constant three-plane arrangement over the parameters. The intended conclusion is the same three-dimensional kernel inside the four-dimensional RM tangent space. The remaining write-up check is to retain the hypotheses on the two smooth fibres and the distinct nodal values, and to distinguish the Hartogs extension of the already known normal sheaf from a new assertion about simultaneous normalization of the union.

## Completed assessment

[L009](../lemmas/L009-diagonal-union-retains-cubic-obstruction.md) gives the full proof. The kernel for the union is exactly V_D, of dimension three, against the required four RM tangent dimensions. Both inclusions are checked; the construction of a flat union along the known family includes its three-branch points. The Hartogs step extends sections of N_C in a locally trivial ambient deformation, not arbitrary deformations of a normalization or an unproved flat colon at an isolated intersection.

Outcome: NEGATIVE. This is new evidence, not a repeated stop review: the union has new curve-smoothing parameters, and the global calculation proves that none can remove the transverse obstruction. Exploration turns used reset to 0. The representative is recorded in [Attempt 006](../ATTEMPTS/006-adding-diagonal-to-cubic-support.md). No new surface attains the 21-dimensional Hodge span. Higher-order extension of another representative, arbitrary K3 surfaces, arbitrary fourfolds, and higher codimensions remain unresolved.

The reason for changing the added component is specific: F_+ x F_+ has a divisor-product class and acts as zero on T, while its projection to S is not a deformation of the identity. Thus the vector-field extraction that stopped the diagonal does not directly settle that different union. This is a reason for a new discriminating test, not a claim of vanishing or a candidate proof of the target.

The primary rational target was rechecked in [Deligne, section 1](https://www.claymath.org/wp-content/uploads/2022/06/hodge.pdf#page=2); the existing cubic-family source was reopened. [Stacks Project Lemma 15.24.18, tag 0AVB](https://stacks.math.columbia.edu/tag/0AVB) was checked as support for the Hartogs step, not as a citation for the full new theorem. The relevant numerical comparison is 21 nodal values versus degree four for the meromorphic base vector field, followed by kernel dimension three versus four required RM directions; neither count asserts surjectivity on additional varieties.

The command `PYTHONDONTWRITEBYTECODE=1 python3 scripts/cubic-deformation/check_diagonal_union.py` passes the exact conic, intersection, derivative, critical-fibre, and tangent-eigenvalue checks. The global deformation argument is an informal proof, not certified by that computation.

## Mathlib

Coverage of the full lifting statement: **not checked**. No Mathlib match or absence is claimed. The directly linked Stacks result is a supporting extension theorem, not a match for the full statement.
