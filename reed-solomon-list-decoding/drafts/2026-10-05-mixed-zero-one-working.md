# Mixed (0,1) fixed-assignment diagnostic — working record

Approved target: Test L022's unchanged assignment against both full (0,1) Schrijver blocks for A(1024,10,68), with exact PSD or negative-quadratic certificates.

Main gap: arbitrary-center safety at 68 agreements; 67 agreements is
independent. The prior SPECIALIZE assessment covers this exact target.
Inputs are L022's prescribed values, L023's admissible-orbit extension,
L021's pair witness, L001/C001a's support interpretation, and foundations/04's
Schrijver III.A (58), III.B (64), corroborated by Kim–Toan III.B (32)–(35).

Construct precisely indices 1,...,68, with beta_(ij,0)^(t,68) and
beta_(ij,1)^(s,956). Preserve forbidden, repeated-word, then product
branches; do not replace distinct t-s variables by a new identification.
Both full matrices must be on disk before sign testing. Independently
reconstruct all entries and certify either every exact congruence identity
and nonnegative diagonal, or a rational vector with negative quadratic.

A negative excludes only this unchanged extension and warrants a concrete
constraint follow-up. Both PSD parks this diagnostic and requires a route
reassessment before further block tests. No optimization, full scalar
feasibility, actual code, sharpness, or ABF-model equivalence is assumed.

Completed: L024 records both matrices PSD, with 64/4 and 68/0 positive/zero
pivots. The independent audit reconstructs 86207 beta coefficients,
771681 actual orbits, all 9248 ordered matrix entries and every exact
congruence identity. All 7093 old orbit values and 2346 weight-68 beta
arrays agree; there are no failures. Full certificates are
scripts/finite-support/mixed-zero-one-results.json and
scripts/finite-support/mixed-zero-one-audit-results.json.

The unchanged objective exceeds 1.383 times threshold. This is NEGATIVE
evidence for this exclusion diagnostic, not full-SDP feasibility or an
unsafe-list witness. Both signs pass, so further individual-block tests
are parked. A different full scalar diagnostic is proposed for a separate
scope review in drafts/literature/2026-10-05-full-scalar-extension-test.md.
