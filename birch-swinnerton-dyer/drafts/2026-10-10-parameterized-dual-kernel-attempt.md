# Parameterized dual-kernel implementation — working record

2026-10-10, approved SPECIALIZE target: implement the finite full-relative
certificate and independent checker, with mandatory L030 conductor-389 replay.
Main gap remains arbitrary rank/complex order equality. L029's line can feed
L028/L036 only with independent q and normalization inputs. Reuse L029,
L030, L037, L038 and the supplied source review; no new theorem mechanism.

Plan: preserve fixed/general programs and certificates. Add an explicit
adapter for their different schemas. Independently replay the full structural
input; bind externally supplied model, conductor, traces and provenance.
Persist all reversible rational operations, complete kernel basis and all
integral-generator values. Independently reconstruct the transpose blocks,
replay exact elimination and verify a nonzero (d-1)-minor and nullvector at
nullity one. Empty/larger kernels are diagnostics, not line certificates.

Continue only if full rank, bindings, all generator/relation values and
bounded corruption checks pass. Otherwise record the precise missing witness.
No normalized period, q, coefficient, universal software theorem or BSD
candidate is sought. Existing ATTEMPTS/023--024 stop repeated conditional
calibration audits, not this finite production step. Separate critical review
of newly produced executable evidence remains future work.

Completed: the independent fixed structural replay checks all 1,950 paths
and 8,142 segments. The new full B is 130-by-65, rank 64/nullity one;
the exact selected minor determinant is -58000. All 3,525 reversible
operations, 390 generator values, 780 source and 325 saturated relation
values pass. All 22 corruption cases reject and four synthetic core fixtures
pass. Complete evidence and source hashes are in
`scripts/dual-kernel/manifest.json`; full canonical qualifications are in
L030's parameterized executable supplement. Generic arithmetic remains
supplied conditional input; no additional elliptic instance or universal
software soundness is claimed. The final documentation check passes.

This is a local implementation advance reproducing known algorithms.
No new lemma or DAG edge is required, and PROOF.md's mathematical argument
is unchanged. The future critical-audit assessment is REVIEW_REQUIRED
for separate next-turn approval, preserving this completed attempt.
