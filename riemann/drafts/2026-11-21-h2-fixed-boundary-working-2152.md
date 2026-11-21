# Fixed boundary implementation, step2152 (in progress)

Approved target: step2150 SPECIALIZE assessment, unchanged fixed 32-by-64
source boxes, 100 Decimal digits, N=3 guard first. No sweep or ABC fallback.
Main gap: L030-L032/C032a actual-Xi all-degree mixed positivity.
Intermediate use: one vertical boundary prerequisite for later independent
census/continuation/head-margin work; none of these follows from this test.

Read the omitted step2150 detailed comparison, L019, L058, L037 and the
L919 normalization proof. Rechecked the primary theorem formulas (6)-(19),
(23)-(25), and Proposition 6.6(iv)-(vi). Existing step206 Rayleigh and
moment-box stops remain; the normalized boundary observable is distinct.
Runtime is Python 3.15.2. No certified complex package is assumed.

Implementation plan: directed Decimal real intervals; exact 96-term Machin
pi; rectangular complex arithmetic; principal log by rotation onto a
positive imaginary-axis scale and the 128-term log(1+w) series, with a
geometric absolute remainder and branch guard. Complex exponential uses
real exp and 128-term sine/cosine after verified 2pi reduction. All square
root bounds must pass exact rational squared checks. Evaluate the actual
gamma, kappa and s_* and the two published complete error bounds. Save
every box and guard, including failures. A nonpositive lower margin parks
the fixed test as inconclusive; it supplies neither a zero nor RH evidence.

If a uniform positive margin m is obtained for t>0, continuity of H/B at
t=0 (L058, L919 normalization and nonzero branch-safe explicit B) carries
|H/B|>=m to t=0. If the test fails, this is only a conditional endpoint
justification, not an established boundary claim. Conjugation covers the
negative local height. Canonical result/proof to be saved after evaluation;
no mathematical outcome was asserted at that checkpoint.

## Completion

All 2048 boxes passed, with no failures; minimum margin
0.18367020352895683864520364570840596328... > 18367/100000.
The complete statement, inclusion argument, source qualifications and
zero-time/conjugation specialization now live in canonical C919b.
The full evidence is `scripts/heat/fixed-boundary-2152.json`;
`scripts/heat/fixed-boundary-integrity-2152.json` contains 6150 exact
saved-evidence checks with no failures, including all 116736 guard
thresholds. This is an unaudited local certificate, not an independent
audit or a complete RH candidate. No sweep or fallback was used.
