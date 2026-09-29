# Global degree-three support reduction — completed working record

The unchanged target has the prior SPECIALIZE assessment in
[the saved source review](literature/2026-10-03-universal-sheaf-global-support-reduction.md).
This is one research specialization, not a new source-only target.
The gap is a boundary-inclusive family/action reduction; its use
is a later search for a stable map with non-scalar cubic-RM action.
Continue if the actual hull and base-changing quotient exist;
restrict or abandon the assertion if a boundary fibre fails.

## Reasoning saved before the family check

Let F be H-Gieseker stable on a projective K3 surface, with
rank two, c_1=0, c_2=3, hence chi(F)=1. Stability gives h^0(F)=0,
so Serre duality supplies a nonzero F -> O_S. Slope semistability
removes any effective divisorial zero locus of its image. Write
the resulting sequence as 0 -> I_Z -> F -> I_W -> 0.
The Chern equation gives length(Z)+length(W)=3. Stability of
I_Z gives length(Z)>=2, so length(W)<=1.

The map extends to the actual locally free hull G=F^{**}.
Its image is I_Y with I_W contained in I_Y, so length(Y)<=1.
Its rank-one kernel is a line bundle with trivial determinant.
If Y has length one, Ext^1(I_Y,O_S)=0 by Serre duality and
H^1(I_Y)=0, contradicting local freeness of G. If Y is empty,
H^1(O_S)=0 splits the extension. Thus G=O_S^2 in either
remaining admissible case; no slope-graded hull was substituted.

For a flat family on B x S, the intended construction is
V=(Ext_p^0(F,O_{B x S}))^vee. Fibrewise Hom has dimension two,
Ext^1 has dimension one and Ext^2 vanishes. The remaining check
is that the relative Hom bundle and its evaluation commute
with base change. The evaluation F -> p^*V should then be
injective on every fibre, giving a flat quotient of length three
by the already inspected Huybrechts--Lehn Lemma 2.1.4.

If this works, Fulton gives ch_2(Q)=[Q]_2 and
ch_2(F)=p^*ch_2(V)-[Q]_2. Markman's dual convention makes
the normalized action the positive weighted-support action.
No map, non-scalar action, transverse surface, or complete
candidate for the Hodge conjecture has been constructed.

## Completed specialization and critical check

The full scoped informal proof is recorded in
[L039](../lemmas/L039-global-degree-three-support-action.md).
The family check succeeded. The actual fibre hull is O_X^2
for every stable fibre, and the relative Hom construction gives
a rank-two bundle V, an exact base-changing inclusion into p^*V
and a flat quotient Q of length three. The normalized Mukai
action is the positive associated-cycle action of Q.

The critical points were checked explicitly:

- The map F -> O_X is supplied by chi(F)=1 and stability,
  without assuming slope stability or a trivial graded hull.
- Stability makes |W|<=1. The length-one image of the bundle
  hull is impossible by Ext^1(I_Y,O_X)=0 and local freeness.
- Hom dimension two, Ext^1 dimension one and Ext^2 zero are
  constant on every stable fibre. Perfect pushforward and
  its local normal form construct the relative Hom bundle;
  reducedness of the smooth base removes a possible nilpotent
  differential. This is not a pointwise-to-flatness inference.
- Fibre injection implies actual injection by an associated
  graded and Krull-intersection check before applying the
  short-exact-sequence flatness criterion.
- The quotient's generic-stalk lengths determine its leading
  Chern character. The raw ch_2 action has the negative sign,
  and Markman's dual convention gives the positive support action.
  Base twists add only pure parameter terms.

The constant-dimension perfect-complex argument uses the
supporting statements actually read on 2026-10-03:
[Stacks Tag 0DJT](https://stacks.math.columbia.edu/tag/0DJT),
[Tag 0BCD](https://stacks.math.columbia.edu/tag/0BCD), and the
local normal form in the proof of
[Tag 0BDI](https://stacks.math.columbia.edu/tag/0BDI).
The other cited source framework is reused from the ready
assessment. It was not rewritten or assigned a new decision.

This passes the saved all-fibre family/action test, including
images contained in collision strata. It supplies a relevant
input for a later stable-lift search, not a stable lift of every
support map. L038's collision failure and scalar calculation
remain valid for its specific recipe. The main bounds remain
21 known algebraic dimensions on the Dickson family and three
RM directions against four required; no new non-scalar class
on a transverse surface is supplied.

Classification is REPRODUCTION: known tools are imported and
specialized, with no originality or progress beyond the checked
literature claimed. Mathlib coverage is not checked. There is
no complete informal candidate for the Hodge conjecture.
