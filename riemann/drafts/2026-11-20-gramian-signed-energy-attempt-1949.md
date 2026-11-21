# Signed Krylov-energy attempt1949 — working record

Approved scope is the unchanged exact r_d test in assessment1947,
with C028b, C028h and C029b as inputs and T=d^2. No horizon change,
spectral premise or numerical coefficient enclosure is introduced.
The target is r_d=o(1), or a positive liminf; full k_d remains separate.

Unfinished reasoning saved before further work: use u(t)=exp(itC)e_(d-2)
and its exact chain [u,-iu',-u''] to integrate the signed endpoint
derivatives by parts. In particular, test whether the mismatch between
integrated H_13 and H_22 controls the third axial component without
losing the small Gram determinant. Endpoint values at t=0 must be
retained. The potential gain is an estimate relative to integrated
energy, rather than the exhausted semigroup norm bound. No vanishing
ratio, positive floor or uniform conditioning is currently established.

Source coverage is reused from assessment1947 and source-notes1947;
the calculation is within its signed terminal-three specialization.
No new literature claim or source reproof is planned. Any identity
alone is only a reduction, not the requested asymptotic estimate.

Completion: EXPLORATION. The full signed calculation is now canonical
in C029b, section “Integrated signed energies and the remaining Schur
residual.” It supplies an exact two-term split but proves neither
asymptotic alternative. The initial concern about a small determinant
means small relative to the numerator: the canonical proof establishes
an absolute lower coercivity bound and does not claim absolute collapse.
See ATTEMPTS/2026-11-20-gramian-signed-energy-unpaid-1949.md for the
scoped stop and PROGRESS.md for the sole current continuation.
