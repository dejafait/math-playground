# L084 equality audit — step 304 working record

Approved target: critically audit L084's rank-27 equality compatibility
and complete 18-parameter solution on the zero plane. Reuse the saved
SPECIALIZE assessment `literature/2026-10-18-zero-plane-equality-critical-audit.md`.

The main gap remains arbitrary-center 67/68-agreement safety. This audit
can secure the equality parametrization for a later joint-feasibility
test. Retain it only if the complete exact rank, compatibility and both
all-solution directions pass; otherwise identify and preserve the failed
claim. Nonnegative moments, 53 remaining modes, other anchors and global
realization are independent unresolved requirements.

Read canonical L084, relevant L076/L082/L083/L085 contracts, the original
constructor/verifier, foundations/10's precise Ye imports and recorded
ATTEMPTS/052–053,066–067. L085's reviewed equivalence does not duplicate
L084's rank/exhaustiveness audit. The existing verifier checks particular
raw moments but does not explicitly store all raw homogeneous residuals
or a linear identity proving the reverse all-solution direction. The
audit will check these, replay every recorded invertible operation and
compare all original pivots and coefficient arrays. These are checks
of the already claimed theorem, not an expanded feasibility target.

The first audit run stopped on a schema KeyError: selected L085 blocks
store `scalar_face_equation`, while `face_equations` is an unselected
block field. Its pre-verdict certificate is preserved in
`../scripts/finite-support/zero-plane-positive-mode-compatibility-critical-audit-initial.json`.
Archiving initially hit Python's integer-string limit; disabling that
limit changed no data. The next complete run passed the mathematical
identities but reported 28 serialization-comparison failures: stored
rational zeros `[0,1]` were compared to integer zeros without decoding.
Its complete evidence is
`../scripts/finite-support/zero-plane-positive-mode-compatibility-critical-audit-encoding-failure.json`.
Decoding those entries as Fractions fixes the test without changing any
coefficient or weakening the requirement that every residual be zero.

Preserve step-298's failed numerical candidate and all earlier point/weight
stops. No solver, scan, new weights or new mathematical target is tested
in this step. Ancestor PSD/uniqueness/whole-kernel qualifications remain
imported rather than recursively reviewed.

Final verdict: RETAINED, with 3673 exact checks and no failures. The full
proof, both all-solution identities, raw-coordinate verification and limits
are recorded canonically in L084; complete evidence is
`../scripts/finite-support/zero-plane-positive-mode-compatibility-critical-audit.json`.
This secures a local mathematical input without a source-level novelty or
feasibility claim. A changed fixed-face reduced proposal is recorded only
as a REVIEW_REQUIRED continuation; no dependent calculation was performed.
