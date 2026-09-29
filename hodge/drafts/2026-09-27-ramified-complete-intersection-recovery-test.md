# Ramified complete-intersection recovery: saved reasoning

The saved SPECIALIZE assessment matches this turn's target: decide the
length-three lift of an admissible complete-intersection union with
arbitrary first-order motion and ambient coefficient outside V_D at
order tau^2. Reuse that assessment. The intended downstream use is a
representative for the non-scalar cubic RM action beyond the Dickson
family; an exclusion must cover every earlier union motion.

The first-order obstruction in L022 alone cannot decide this question.
Let I=I_C, F=I(-mH), G=O_X(-nH), E=F direct sum G, and d=n-m. A more
concrete recovery may handle the nonreduced lower base:

- If d<=0, Ext^1(G,E)=H^1(I(dH)) direct sum H^1(O_X)=0.
  For d<0 use antiampleness on C and negative product cohomology;
  for d=0 use H^0(O_C)=C. Thus the central inclusion G -> E should
  lift through both small extensions, without splitting E.
- If d>0, Ext^1(E,G)=H^3(I(dH))^* direct sum H^1(O_X)=0 provided
  H^2(C,O_C(dH))=0. The finite normalization sequence reduces this
  to H^2(W,M^d). Serre duality, K_W=2F_W, and
  (K_W-dM).F_W=-2d(L.F)<0 should give the vanishing because F_W is
  nef. This would lift the central projection E -> G instead.

The central extension obstruction Ext^2(I_Y,O_X(-m-n)) already
vanishes by L022. Derived adjunction and the tau-adic filtration
should recover its extension through both stages for any actual
flat I_Y lift. The map selected above must then be lifted on that
actual middle sheaf, not substituted for a different central-summand
lift. Its flat kernel or cokernel would recover an abstract I lift.

Remaining checks before claiming a result: extension reduction over
X_(A_2) -> X_(A_1), the two differently oriented Hom sequences,
flatness of the recovered kernel/cokernel, determinant and Hartogs
over all three layers, and the exact use of L016's fixed-product
rigidity to make the recovered C constant modulo tau^2. That would
reduce the remaining equation to L008's central obstruction.

Continue if this recovers C for every admissible m,n>0 and every
earlier motion; otherwise retain the failed map or flatness condition
as the unresolved test. Only three of four RM directions are currently
allowed, and the attained span is still 21 on the same family. An
order-two exclusion would be a new notebook consequence of standard
tools, not a new general obstruction theory or a Hodge resolution.

No final lifting assertion is claimed by these saved notes yet.

## Completion on 2026-09-27

[L023](../lemmas/L023-ramified-complete-intersection-unions-retain-obstruction.md)
completes the listed checks. The positive top-cohomology vanishing
follows from Serre duality on W and negative intersection with its
nef fibre. For d<=0 the actual middle lift admits the central inclusion;
for d>0 it admits the central projection. The linkage extension and
the chosen map both lift through A_1 and A_2 by their central Ext
vanishings. Flat kernel/cokernel recovery, determinant and three-layer
Hartogs give an embedded C_2. L016's rigidity makes C_1 constant, so
L008 forces the order-tau^2 coefficient into V_D.

The outcome is NEGATIVE for the entire saved representative class and
degree range, with every earlier motion allowed. Equality of coefficient
loci keeps the independent section-lifting hypothesis. This is a
reproduction/application of known tools with a new scoped notebook
exclusion, without an originality claim. The full informal proof and
Mathlib coverage qualifications are in L023; no new computation script
is needed. The earlier provisional notes are retained above.
