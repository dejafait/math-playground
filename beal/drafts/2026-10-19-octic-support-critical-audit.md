# L098 critical audit — working record

Approved target: Critically audit L098's finite cube-class containment, fixed support {3,5,11} and both norm scales for the full L095 domains.

Prior SPECIALIZE coverage: `drafts/literature/2026-10-18-octic-supported-cube-class-audit.md`.
Inputs read: complete L095 domains and proof, audited L097, complete L098,
the original arithmetic producer, complete Sylvester matrix and check list,
and ATTEMPTS/043–044. Existing unfinished work is preserved.

Main gap: integer elimination of both systems, with other factors and
signatures independent. This audit tests whether the necessary finite
ambient group is valid for later class and fifth-power compatibility work.
Continue if every maximal-prime case and exact scale survives; otherwise
correct or narrow L098 and record the escaping case.

Saved reasoning: both substitutions give gcd(m,n)=1. Outside 3,5,11,
theta is integral because the leading coefficient is a unit. Primes
dividing n give unit alpha; otherwise a nonunit alpha forces the
complementary factor to reduce to n^7 h'(theta), a unit by the
nonzero polynomial resultant. Normalized valuations then retain the
ramification index and are multiples of three. The cited Kummer
sequence keeps the S-class three-torsion. No escaping case found so far.
The completed canonical audit is in
`lemmas/L098-octic-supported-cube-class-containment.md`: PASS without
correction. Fourteen independent arithmetic checks and all seven original
assertion replays pass; the complete certificate is
`scripts/rational-factor/octic-cube-support-audit-certificate.json`.
The exact resultant and norm-polynomial evidence was checked, and the
canonical proof records every unbounded prime case. No class
representative, integer exclusion or new source theorem is claimed.
