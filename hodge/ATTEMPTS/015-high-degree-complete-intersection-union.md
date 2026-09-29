# High-degree ample complete-intersection unions

The tested representative is C union B with B=V(f,g) smooth,
f in I_C(nH), g in O_X(mH), and m>n>0. The tested regime has
H^1(C,O_C(nH))=0, which holds for all sufficiently large n. Smooth
added surfaces with smooth ample intersection curves exist there.

## WHY IT FAILS

[L018](../lemmas/L018-high-degree-complete-intersection-unions-retain-obstruction.md)
uses this cohomology vanishing to lift the basic-double-link extension
from any union lift. The strict degree inequality then lifts a line
summand inclusion, recovering a sheaf lift of I_C. Determinant and
Hartogs recover an embedded C, which is obstructed transversely by
L008. With the additional positive ideal-cohomology vanishing, the
union's kernel is exactly the three-dimensional V_D against four RM
directions required. No component or filtration is assumed to persist.
The added divisor-product class leaves the action U unchanged, but
does not enlarge the set of surfaces covered. This stops the stated
degree regime, not the existential target for smaller n with nonzero
H^1(C,O_C(nH)), other representatives, or the universal Hodge target.

## All-positive-degree extension on 2026-09-27

[L019](../lemmas/L019-positive-degree-cubic-support-vanishing.md) proves
H^1(C,O_C(nH))=0 for every n>0 with the original ample L. Its divisor
lattice inequality makes L-F nef and big; adjoint vanishing and the
simultaneous six-point evaluation handle the normalization and all
three gluing conditions. Thus the recovery in L018 now excludes every
admissible smooth union in the ordering m>n>0. There is no remaining
small-degree exception to this exclusion. Equality with V_D retains
the independent H^1(X,I_C(nH)) hypothesis. The prior large-degree
argument is preserved above; the new result does not cover other degree
orderings, arbitrary added components, or the universal Hodge target.

## Removal of the degree ordering on 2026-09-27

[L022](../lemmas/L022-direct-summand-recovery-all-positive-degrees.md)
extends the exclusion to every admissible pair m,n>0. The basic-double-link
extension lifts by the same Ext^2 vanishing, now supplied in all positive
degrees by L019. Naturality of the full obstruction recovers existence
of a lift of the ideal summand; the reviewed perfectness and base-flatness
criteria turn it into a coherent sheaf, and determinant/Hartogs recovers
an embedded C. The chosen summand inclusion in the middle lift need not
extend. Thus L020's nonzero inclusion-lifting group cannot provide an
escape, and the uncomputed L.F>=4 range is unnecessary for this exclusion.

This stops the entire stated class of first-order smooth
complete-intersection additions, including equal degrees and m<n.
The converse still has its independent section-lifting hypothesis;
without it the lifting locus is only known to be contained in V_D.
The mechanism is an application of known obstruction theory, with no
originality claim. Ramified higher-order lifts and other cycle
representatives remain outside the conclusion. The earlier restricted
arguments above are retained as the history of this attempt.

## Ramified order-two exclusion on 2026-09-27

[L023](../lemmas/L023-ramified-complete-intersection-unions-retain-obstruction.md)
also excludes a transverse ambient coefficient at order tau^2 over
C[tau]/(tau^3), allowing arbitrary earlier union motion. Positive
top cohomology on C vanishes, so for every degree pair either the
central inclusion or the central projection of the recovered middle
sheaf lifts through both small extensions. Its flat cokernel or kernel
recovers an ideal sheaf and then an embedded C. Fixed-product rigidity
eliminates the earlier motion of that recovered support, leaving the
same three-versus-four obstruction. This is why ramification at this
order does not rescue the stated unions. The proof does not assume a
preserved splitting or component, and equality still needs the separate
containing-section vanishing. It is a reproduction/application of
standard tools; other representatives and higher orders are outside
the stated conclusion.
