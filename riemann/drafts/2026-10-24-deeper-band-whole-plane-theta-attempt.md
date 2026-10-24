# Deeper-band whole-plane theta attempt — working record

The gate-approved target is the exact TARGET in
[the saved assessment](literature/2026-10-24-deeper-band-whole-plane-theta-coverage.md),
whose SPECIALIZE decision predates this invocation. The main gap is
initial low-index signs and global mixed positivity. The intermediate
target is a matching additive theta reduction on 13/16≤m/r≤7/8;
its downstream use is a separately assessed assembly with L459's
conditional arithmetic margin. No arithmetic assembly is performed here.

Existing active-notebook changes have been inspected and preserved.
Read L458's full proof and separate audit, L455's explicit estimates,
L269's parameterwise contour passage, C294b, and the L323/L327 failure
records. No duplicate exact-band reduction is recorded. The r/4 strip
failure is avoided by retaining r/20 and its full signed sum; no PSD
replacement is attempted.

Unfinished reasoning: alpha∈[13/16,7/8] gives
beta∈[1/8,3/16], h∈[157/32,79/16]⊂[39/8,5], and
nu=(1+alpha)/2∈[29/32,15/16]. The high-strip containing
envelope in L458 uses beta≤1/4 and beta/2≥1/128;
the new beta interval satisfies these. The translated complement
uses only nu≥7/8, not the old band's sharper value. The mass,
clipping and low-strip bounds use alpha≥3/4; patch derivatives
use m≤r and bounded h. These preliminary domain comparisons are
not yet a complete changed-band theorem or correctness review.

Continue only if every mass, boundary, infinite translated tail,
clipped/full patch and sector error has one uniform onset and fits
C(1+r)^2 exp(-r/200), with the exact positive multiplier including
m! and one reflection. Otherwise preserve the specific failed term.
Only exact rational domain/rate checks supplement the analytic proof.

Completed construction: [L460](../lemmas/L460-deeper-band-whole-plane-theta-reduction.md)
writes the matching reduction with the exact full S, positive P, all
sector and boundary budgets, and one common onset. Its changed-band
proof reproduces the assessed explicit methods; it makes no originality
claim and awaits separate critical audit. No arithmetic assembly or
Laguerre sign is proved. The complete rational comparisons are saved in
[the ancillary certificate](../scripts/deeper-band/L460-theta-domain-certificate.json);
all 11 pass. This certificate checks only endpoint/domain and rate
arithmetic, not the analytic proof. The canonical proof contains the
complete relevant reasoning and qualifications.

The complete normalized patch-mass and translated-complement rates are
19/120 and 61/80, the mixed-sector rate exceeds 1/54, and the
clipping/low-strip bound retains 1/200. The high-strip term is faster
than exponential. Thus the construction meets its continuation test.
The DAG adds only L460's actual direct proof inputs; L459 remains a
downstream input. The new audit target is REVIEW_REQUIRED and must
receive separate scope/source approval before execution. The main RH
gap and independent realization gaps are unchanged.
