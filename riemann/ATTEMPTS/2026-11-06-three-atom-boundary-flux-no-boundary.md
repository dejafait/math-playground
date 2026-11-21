# Fixed three-atom boundary-flux discriminator — no boundary

The approved support {0,1,4}, block D_(3,2), and positive probability
weights admit no zero-determinant boundary. See the complete exact
proof in [L843](../lemmas/L843-three-atom-heat-minor-has-no-boundary.md)
and its recorded certificate. This is an informative negative test of
this witness search, not a failure of general heat descent or an RH
result. Source toolkit: Shi Hexagon2610.00521v1 Cor3.2/Prop3.3/Prop9.1;
the fixed-family sign is a finite specialization.

**WHY IT FAILS.** The sought positive flux must occur at B(0)=0, but
L843's exact positive decomposition gives B(0)>=671116 p4^3/14515200>0
everywhere in this family. Initial eliminated boundary points had a
negative mass and cannot count as witnesses. Thus neither a positive
flux at those invalid points nor any proper-minor filter can supply the
approved countermodel. Stop this fixed-family discriminator without an
automatic support/rank extension. Its nonexistence conclusion leaves
general signed cofactors, actual-theta constraints and all-order
propagation unresolved; it does not prove an invariant cone.

6 November 2026 independent audit: the canonical L843 audit reconstructs
all determinant coefficients and individual derivative rows without the
original polynomial engine. Sixteen exact checks pass, no failures.
The strict lower bound and this fixed-family stop survive; no expanded
support/rank test or general sign conclusion follows.
