# L117 — First-42 signed derivative assembly

## Hypotheses

Use all fixed-curve analytic hypotheses of audited L116: E=[0,1,1,-2,0]
over Q has exact conductor 389, its full normalized elliptic newform has
Fricke eigenvalue -1, L(E,1)=L'(E,1)=0, and |a_n|<=n for every n>=1.
The derivative is the unnormalized L''(E,1). No exact order is assumed.
Use L031's separately audited derivative-facing coefficient export and
the audited containment conclusions of L103 through L114, with their
unchanged common parameter c_*=73775804382331484748893662180180200545104154546089041648426948815067512948607/(2*2^256).
L103 supplies c_l<=2*pi/sqrt(389)<=c_u in [3/10,1/2] and delta.
All historical timing and document-transition qualifications remain.

## Conclusion

One exact rational application produces the following certificate,
**finite mathematical checks pass in step 486, but both production and
audit exceed their inclusive reporting caps; contract acceptance is withheld**:

s = 2407549352791235365884773413443560720308875069905943492000328848086153057678675202444744022501/1585339814916885115736385298979544551506837956473230977962055333554756848751197697128739635200

B_42 = 1397665588934849987731909781600195508271982319785544169920083394934519613458279812393339503/68169612041426059976664567856120415714794032128348932052368379342854544496301500976535804313600

The producing calculation reports |L''(E,1)-s|<B_42 under the imported
premises, and certifies by integer comparisons

1518612493225/10^12 < s-B_42 < s+B_42 < 1518653498757/10^12.

Thus the produced enclosure excludes zero and is positive. Its radius
satisfies 20502765/10^12 < B_42 < 20502766/10^12 < 2^-14,
but B_42>2^-40. These rational decimal bounds are outward comparisons,
not rounded values used as premises. This is local REPRODUCTION of a
known method, not a new BSD case or a solution of the general conjecture.

## Proof

**Imported mathematics.** Apply L116 without changing its analytic
partition or parameter transfer. Its primary identity is J. E. Cremona,
*Algorithms for Modular Elliptic Curves*, corrected second edition
(1997), Section 2.13, Proposition 2.13.1 and proof, pp.42–43
([primary chapter](https://johncremona.github.io/book/fulltext/chapter2.pdf)).
The Fricke sign and lower vanishing needed at r=2 are hypotheses above;
the factor four gives L'' itself. L031 imports the same book's Section
2.6, equations (2.6.1)–(2.6.2), p.25, and Section 2.8, (2.8.3), p.29
for the normalized Euler coefficients. All selected primes are good.
No analytic identity, coefficient theorem or kernel containment is
reproved. The prior SPECIALIZE assessment is
`drafts/literature/2026-10-25-forty-two-kernel-signed-assembly.md`.

**Complete finite matching.** The sole command was
`python3 scripts/signed-derivative-assembly/assemble-484.py <setup-epoch-seconds>`.
The source parses integer pairs only, using Fraction without floats
for mathematics. Its full selected certificate, parameter, all 128
coefficient export rows, full selected kernel records and 110-entry
input inventory are in
`scripts/signed-derivative-assembly/step-484/selected-inputs.json`.
Every selected coefficient/kernel/parameter file matches its respective
completed audit's initial byte-length and SHA256 binding. The coefficient
export also matches L031's explicit canonical hash, exact model/conductor,
normalization, original source hash, all indexed slots and a_1=1.
Every n=1,...,42 occurs once. Every whole parameter equals the audited
L103 record; its c interval, midpoint, delta and range are checked.
Every kernel's n, denominator 2^256, 1016-panel count, ordered endpoints,
midpoint and nonnegative radius are checked. Each pair of endpoints
matches the complete corresponding canonical conclusion, including
L106's separately accepted step-446 audit. This imports those audited
containment results; hashes and panel counts alone are not proofs of
containment, and no new panel integration runs.

**Exact assembly.** For the matched endpoints define
j_n=(l_n+u_n)/2 and e_n=(u_n-l_n)/2. The program computes
s=4 sum_(n=1)^42 (a_n/n)j_n and
W=4 sum_(n=1)^42 (|a_n|/n)e_n, retaining negative and zero a_n.
Reverse-order Fraction summation agrees exactly. A separate integer
common-denominator sum, with Q=lcm(1,...,42)*2*2^256, equals s.
Direct signed endpoint multiplication and reverse interval addition
produce exactly [s-W,s+W]. Therefore eta=0 in L116.
All actual allowances are retained:

- Original two analytic remainders combined: 2^-43.
- Full-sum parameter transfer: 5395948348266044881859122933554671769574375/28948022309329048855892746252171976963317496166410141009864396001978282409984.
- Discarded n=43,...,128 finite block: 65/3170304.
- Actual retained kernel width W: 3707525217135832664285432304688532268821/1585339814916885115736385298979544551506837956473230977962055333554756848751197697128739635200.

Their exact sum is the displayed B_42. L116 gives the strict enclosure;
its discarded block neither replaces nor duplicates either analytic
remainder. The full exact endpoints, all components, arithmetic
comparisons and zero test are in
`scripts/signed-derivative-assembly/step-484/certificate.json`.
The positive lower endpoint follows by exact cross multiplication with
the stated positive rational lower bound. No original 2^-40 guarantee
is asserted or inferred from the successful zero test.

**Preservation, limits and pending review.** All 110 inputs retain their
hashes and lengths after certificate writing, as recorded in
`scripts/signed-derivative-assembly/step-484/preservation.json`.
No finite-input or arithmetic failure was reported. The inclusive
180-second cap subsequently failed during documentation/reporting. No
retry occurred; the application is stopped and its preliminary arithmetic
is preserved without claiming successful execution under the contract. Final inclusive setup/reporting resource evidence is in
`scripts/signed-derivative-assembly/step-484/finalization.json` against
180 seconds and 134217728 new bytes; the time requirement fails. Earlier historical timing claims
are not repaired or used to establish containment. The historical producer identity is not certified by input preservation;
the separate audit below validates the current finite mathematics independently.
The fixed curve's order is already imported elsewhere in the notebook;
this is no new curve case. General rank equality, full Sha and refined
BSD remain unresolved, and there is no complete target candidate.

### Separate critical audit — 2026-10-25, step 486

**Verdict.** The finite mathematical checks PASS under exactly the
hypotheses above, but this audit is UNACCEPTED under its inclusive
180-second contract: final reporting already measured 234.193 seconds.
The historical production resource contract also remains failed. This is REPRODUCTION, not a result beyond the checked
sources. The prior SPECIALIZE assessment is
`drafts/literature/2026-10-25-first-forty-two-signed-assembly-audit.md`.
The independent checker is `scripts/signed-derivative-assembly/audit-486.py`;
its complete finite certificate is
`scripts/signed-derivative-assembly/step-486/audit.json`.
No producer or integration replay executed.

**Imported premises and bindings.** Read L116's complete conditional
proof and separate audit; its full-sum transfer and both disjoint analytic
remainders are retained. Read the canonical hypotheses, conclusions and
relevant acceptance passages of L031 and L103–L114. L031's step-410
export audit identifies the coefficients of the same normalized newform;
L106's step-446 acceptance supersedes its historical pending text.
L105's failed step-419 report comparison is superseded by the complete
step-422 audit, without erasing the old failure. Later kernels have
separate audits 433, 437, 442, 451, 455, 459, 463 and 470.
These established containment conclusions, rather than an audit substring
or a saved success flag, are the mathematical inputs. All historical
execution and editorial-transition qualifications remain.

The checker loads the complete selected-input object, compares the full
embedded coefficient certificate and all 128 indexed exports with L031's
canonical hash and step-410 inventory, and checks normalization, curve,
conductor, source identity and every coefficient slot. For each n=1,...,42
it independently specifies the production and audit paths, compares the
complete kernel object and complete parameter object, and verifies both
files' hashes and lengths against that audit's original inventory. Every
endpoint matches the corresponding canonical conclusion, not merely a
producer table. The entire common parameter equals L103's record; its
canonical endpoints, midpoint, delta and closed range agree. Every exact
midpoint/radius, grid denominator, index and panel count matches. The
110-entry production inventory and full preservation object also agree
with current bytes. These comparisons import containment; they do not
purport to reconstruct integration from hashes.

**Independent arithmetic.** Let M=lcm(1,...,42), Q=2DM, with D=2^256.
Traverse the matched integer endpoints and accumulate
N=sum 4*a_n*(l_n+u_n)*(M/n). Then s=N/Q. Independently accumulate
min(8*a_n*l_n,8*a_n*u_n)*(M/n) and the corresponding maxima;
dividing these totals by Q gives exactly s-W and s+W. Accumulating
4*abs(a_n)*(u_n-l_n)*(M/n) gives QW. These identities retain all
negative and zero coefficients and prove eta=0 without a producer call.
The full integer totals and exact endpoint fractions are in the audit
certificate. All four allowances equal the displayed L116 specialization:
2^-43, 200*delta, 130/(387*2^14), and W. Their sum, center and both
full endpoints exactly match the preserved certificate and the displayed
fractions above. Exact comparisons prove every stated outward decimal
bound and s-B_42>0. The radius exceeds 2^-40; this is a limitation of
the certified allowance, not a lower bound on the true error.

**Current versus historical provenance.** The complete current producer
was read as inert source and captured by hash. Its emitted status was
ASSEMBLED_REQUIRES_SEPARATE_AUDIT; the current certificate instead has
PRELIMINARY_ARITHMETIC_RESOURCE_CONTRACT_FAILED_AUDIT_PENDING and an
added resource_contract_passed=false. These annotations are explicit,
not silently discarded. No contemporaneous producer/output hash binding
was established, so current preservation does not authenticate historical
generation or the exact time of those changes. Independent recomputation
certifies the current mathematical values without that claim. The
step-484 finalization still reports a 203.597-second lower bound against
180 seconds. It remains failed, with no retry. The audit preserves all
115 captured files, including the current source and four output records.
The audit itself exceeds the same time cap during final reporting;
no retry occurs. Its own inclusive resource failure is recorded separately in
`scripts/signed-derivative-assembly/step-486/finalization.json`.

This verifies one fixed-curve derivative enclosure, whose nonvanishing
was already known. It establishes neither the original 128-output/2^-40
contract nor uniform rank equality, full Sha, refined BSD or a complete
candidate. Direct mathematical dependencies are unchanged.

## Mathlib

Full matching derivative/certificate coverage is not checked. Supporting
rational arithmetic or elementary-function theorems would not constitute
formal verification of this Python certificate or its analytic premises.
