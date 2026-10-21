# Conditional shell test — working record

Approved target: Test AVZ Proposition 17 on shells (67,68) of L022's
unchanged pair witness using the fixed head-weight partition and integer
shortening upper coefficients. Prior coverage is the unchanged
`drafts/literature/2026-10-06-conditional-shell-fixed-coefficient-test.md`.
Main gap: arbitrary-center safety at 68 or 67 agreements. Continue on a
certified violation; park on a complete pass, without retuning.

Before implementation: independent block complementation is an isometry,
and deletion of a zero-weight block preserves distances injectively.
After normalization S is the total weight. For d=2h, S<h permits just
one word; S=h requires disjoint supports and has maximum
min floor(n_a/u_a). This value is attainable by pairing disjoint subsets
in each positive block; the empty tuple has one word. At S>h, incidences
in any positive block give M*u_a<=n_a*K(child). Shortening deletes a
coordinate equal to one in the entire subcode, so preserves distance.
Normalized u satisfies 2u<=n and hence 2(u-1)<=n-1; the child decreases
S by exactly one. Induction bounds every child and taking all integer
floors and their minimum yields the prescribed upper bound. Use h=4
for d=8 and h=5 for d=10. Reject invalid weights.

For each prescribed T' input, repeated AVZ Theorem 26 with e=0 peels
off head weights 63 down to 1, without changing either block length
or the total weight. Its p=min(current head cap,n2-current tail floor)
is positive at every nonterminal stage. The terminal head cap zero is
Theorem 22's one-block constant-weight bound. Thus the sum over head
weights 0,...,63 uses constant-weight upper bounds with the original
lengths, not a fixed-weight interpretation of T'. All displayed head
and tail weights are admissible. No source theorem is reproved.

Essential inputs: L021, L022, L023 scalar supplement and L025 stop;
C001a and foundations/04–06 fix threshold, normalization and theorem.
Preserve L024 and ATTEMPTS/017. Coefficients, ratio sign and slacks are
uncomputed at this checkpoint. Exact maxima, omitted blocks, full-SDP
feasibility, list realization, exponent m, sharpness, 67-agreement safety
and ABF equivalence remain unresolved.

Completed: L026 records both sums, clipping to individual caps and strict
passes in the exact ratio-2 branch. All 81537 states, 156800 branches and
128 summands were independently audited without failures. Canonical
certificates are `scripts/finite-support/conditional-shell-results.json`
and `scripts/finite-support/conditional-shell-audit-results.json`.
ATTEMPTS/018 preserves the stop. No retuning was performed.
