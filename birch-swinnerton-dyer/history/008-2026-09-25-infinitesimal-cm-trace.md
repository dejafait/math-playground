# 2026-09-25 — The normalized CM trace fails its first-order test

Preserved all existing changes and inactive branches. Rechecked the
Clay page and its Wiles statement; the rank target and separate
refinement are unchanged. The [saved test](../drafts/2026-09-25-infinitesimal-cm-trace.md)
records relevance, the exact threshold, and the initial decision test.

The [normalization audit](../foundations/09-cm-diagonal-deformation.md)
pins Castella--Hsieh's equations (2.3)--(2.4), the critical twist,
and the coordinate T = v^(-1)(1+S)-1. The new result is
[L008](../lemmas/L008-infinitesimal-cm-trace-obstruction.md): the
anticyclotomic derivative gives a nonzero trace-lifting obstruction
in the quadratic-character summand. It also excludes corrections
involving V_p E. Unlike L007, this uses the actual normalized CM
deformation and no accumulating classical tame-twist points.

Checked the four inducing characters, both actions of complex
conjugation, arbitrary first-order functional corrections, the
nonzero cohomology class, and the matrix-trace contradiction for
representation-valued corrections. The zero-tangent case lifts to
first order, while the source's universal character supplies a
nonzero tangent. No numerical evidence or Mathlib lookup was needed.

Decision: stop the regular trace contraction, including infinitesimal
lifts, and preserve it in [the failed attempt](../ATTEMPTS/006-infinitesimal-cm-trace-lift.md).
A projector obstruction is different from the obstruction to lifting
a particular cohomology class. This motivates a class-level Bockstein
test with local conditions; no implication from its vanishing to
Kummer membership is assumed.

There is no improved rank bound: L006 still gives r <= 2 (or
1 <= r <= 2 under Theorem B), short of r >= 2. Kummer membership,
analytic nonvanishing, auxiliary existence, and higher ranks remain
missing. The new DAG row is empty because L008 uses its direct
character calculation and the named source normalization, not an
earlier lemma; L006 and L007 supply application and contrast only.
The shared structure checker passed with 8 nodes and 5 edges; the
mathematical input review confirms the empty L008 row.

Step BSD-2026-09-25-008-infinitesimal-cm-trace is NEGATIVE: it provides
new evidence changing the trace-lifting decision. STATUS remains
IN_PROGRESS with no complete candidate. Exploration turns without
an advance or informative negative result remain 0 of 3.
