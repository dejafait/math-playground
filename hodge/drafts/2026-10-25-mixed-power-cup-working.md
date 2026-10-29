# Mixed-power cup working record — step 533

2026-10-25. One bounded proof attempt under the invocation-start SPECIALIZE
assessment `drafts/literature/2026-10-25-mixed-first-second-power-cup-sign.md`.
All pre-existing changes are retained. No external search or mathematical
script is needed for this specialization.

Target: test m_1*m_2=0 with all L161 hypotheses, ordinary W and delta.
Main gap: universal primitive Hodge realization; downstream use would be
restriction of same-sign line coexistence in M, independently of unresolved
F existence, other stable types, lower z control and transport.

For inputs (v,Rv,w,Rw) of weights (-1,-1),(1,1),(-1,-2),(1,2),
the three partitions have targets (0,0)/(0,0), (-2,-3)/(2,3),
and (0,1)/(0,-1). Only the last partition vanishes. The mixed target
has dimension 26*61=1586; it must not be suppressed.

Unfinished sign check: for beta=A(alpha wedge gamma), the two coefficient
quaternionic maps have determinant +conjugation, so the raw opposite
product should equal S beta, where S is line duality times exterior
conjugate-J in degree two. S is anti-unitary and preserves harmonic
forms by the assessed doubled-dual theorem. Therefore harmonic projection
commutes with S without assuming S commutes with bar-partial. Both raw
products are closed. This should justify replacing beta by its harmonic
representative in the dual product.

On the line-valued harmonic target, Kunneth leaves only degree one from
each factor. Crossing the middle degree-one forms introduces a minus
sign; the two negative surface norm pairings then give a negative
normalized degree-two pairing. If verified, this cancels the positive
opposite-trace product rather than excludes coexistence. Check constants,
all exterior orders and exact corrections before promoting this reasoning.
Continue only for an exclusion or a precise failed-sign/cancellation verdict;
park the mixed exclusion if this negative balance is verified.

Completed in this invocation: the specialization and exact correction
are now canonical in `lemmas/L162-mixed-power-cup-negative-balance.md`.
The target has dimension 1586 and the normalized mixed product is
-||beta_h||^2/(4 Vol_1 Vol_2) times xy. The quartic identity therefore
gives a necessary positive norm balance, with no coexistence exclusion.
The negative verdict parks this mechanism, pending a separate critical
audit of the recorded proof. The preliminary reasoning above is retained
as the interruption checkpoint, not as a second canonical proof.
