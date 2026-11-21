# Proposed simultaneous ordinary and auxiliary compatibility test

TARGET: Test simultaneous ordinary probability compatibility of C874b's full S_2,...,S_8 prefixes at S_1=16 using moments m_0,...,m_8, without claiming actual-theta realization.
CHECKED: 2026-11-21
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step2135 searched even truncated Stieltjes/range criteria, eighth moments with cumulants, prescribed-cumulant Gaussian terminology and Theorem5.3 corrections; compared C874b/C874c/L058/L874 and reused step2131's exact-prefix and recorded-failure assessment. No inspected result decides these two fixed m_8 tuples; no novelty claim.
SOURCE_EVIDENCE: Read Curto-Fialkow1991 Theorem5.3 and its complete proof, printed pp626-627, plus Section5 definitions pp625-626, at https://www.math.uh.edu/~hjm/v017n4/0603CURTO.pdf ; reuse assessed Theorem5.1/Theorem4.1 singular/support cases and the November9 Gallier block-PSD coverage. The even theorem retains its range condition.
COMPARISON: Theorem5.3 gives an exact finite representation criterion for m_0,...,m_8; it does not evaluate the prescribed coefficients. C874c covers only m_7 and C874b separately fixes auxiliary S_8=2, so neither is a duplicate joint witness. Earlier fixed-panel and auxiliary-only stops have different premises.
GAP: Compute and certify both prescribed eighth-moment tuples at S_1=16 using the assessed even criterion; no such arithmetic or compatibility decision is made by this review. Actual theta and parameter consistency remain independent gaps.
REASON: Essential changed-scope source coverage is now sufficient for one later finite specialization. Import the representation and matrix criteria by citation; no representation theorem needs reproof and no target calculation is performed in this literature turn.
SCOPE: One fixed S_1=16 test for each full C874b prefix, ordinary moments through m_8 only; include singular qualifications if necessary, with no degree sweep, all-order completion, actual-theta claim or new general moment theorem.
LITERATURE_REASON: The invocation-start REVIEW_REQUIRED target adds prescribed S_8 beyond the ready odd-degree assessment; Theorem5.3 and its essential proof cases required separate inspection before dependent arithmetic.

## Preserved nomination from step2134

The following records the original unapproved nomination. The separate
step2135 approval below supersedes its pending-review language.

Inputs for the proposed continuation: C874b,C874c,L058,L874.
The full prefixes are (S_2,...,S_8)=(2,2,2,2,2,2,2) and
(3,2,2,2,2,2,2), with m_0=1 and
m_j=(-1)^j(2j)![z^(2j)]exp(-sum_(k=1)^8 S_k z^(2k)/k).
These specify finite formal coefficients only. Step2134 did not
compute m_8, assert its feasibility or exclude any compatible law.

A bounded next review must compare the exact even-data theorem,
including singular/range qualifications, with existing ordinary-moment
and contact stops. If essential coverage suffices, the later test can
decide whether these two restrictions can be met simultaneously at
the fixed S_1. A successful joint witness would stop this joint finite
exclusion; a failed fixed-S_1 trial alone would not exclude other S_1
or actual theta. Do not extrapolate a finite outcome to all orders.
The target is routine finite specialization, not a creative mechanism.

Actual-theta realization, continuous parameter tilts, contact existence,
actual signed flux, initialization, equality and global/all-degree
closure remain unresolved. No independently testable signed
actual-kernel input presently supports a creative nomination. Full
and supporting Mathlib coverage are unchecked. This nomination is
unapproved and needs a separate literature turn before mathematics.

## Separate source approval, step2135

Main gap: L030-L032/C032a actual-Xi all-degree algebraic mixed
positivity. Intermediate target: the unchanged TARGET above, adding
the prescribed eighth coefficient to the previously separate finite
restrictions. Its downstream use is to decide whether this joint finite
restriction can remove either positive-flux formal contact. It cannot
establish an actual-theta sign or realize a heat trajectory.

### Primary theorem and essential proof cases

Raul E. Curto and Lawrence A. Fialkow, *Recursiveness, Positivity,
and Truncated Moment Problems*, Houston Journal of Mathematics
**17**(4) (1991), 603-635, [Theorem 5.3, pp626-627](https://www.math.uh.edu/~hjm/v017n4/0603CURTO.pdf).
For real gamma_0,...,gamma_(2k), gamma_0>0, a positive Borel measure
on [0,infinity) represents the data exactly when

    A(k)=(gamma_(i+j))_(i,j=0)^k >= 0,
    B(k-1)=(gamma_(i+j+1))_(i,j=0)^(k-1) >= 0,
    (gamma_(k+1),...,gamma_(2k))^T in Ran B(k-1).

A finite atomic representation is included in the theorem. Neither
matrix must be nonsingular. Its necessity proof handles the mass at
zero separately and uses t dmu and a positive Hankel extension for
the range condition. Sufficiency recursively adjoins gamma_(2k+1)
and invokes the odd theorem. Both proof directions were read through
their conclusions on pp626-627; the positive-invertible remark on p626
agrees with the criterion. Reuse the assessed odd-theorem support and
singular cases from the step2131 assessment; no reproof is needed.

For this target gamma_j=m_j, k=4, gamma_0=1. Thus the required objects
are A_4=(m_(i+j))_(i,j=0)^4, B_3=(m_(i+j+1))_(i,j=0)^3 and the
range column (m_5,m_6,m_7,m_8)^T. C874c's audited B_3 is invertible
for each unchanged lower prefix, so its range is the full R^4.
This identifies the applicable theorem branch; it does not certify A_4
or compute m_8. Singular A_4 remains allowed. Failure of a strict-PD
test alone must not be reported as nonexistence of a representing law.

For exact matrix certification, reuse the November9 assessment
`drafts/literature/2026-11-09-d2-flux-weighted-cubic-norm-review.md`:
Jean Gallier, [*The Schur Complement and Symmetric Positive Semidefinite
(and Definite) Matrices*](https://www.cis.upenn.edu/~jean/schur-comp.pdf),
author version 24 August 2019, Proposition4.2/Theorem4.3, pp9-12,
including its singular range qualification. Standard named Sylvester's
criterion already assessed for C874c suffices for strict PD. No new
matrix criterion or general moment theorem is being proposed.

### Local overlap and interpretation

Read C874b's hypotheses, conclusion and two explicit examples;
C874c's statement, coefficient definition, representation and scope;
L874's normalization and finite-contact statement; and L058's moment
and analyticity hypotheses. The fixed data are exactly S_1=16 and
(S_2,...,S_8)=(2,2,2,2,2,2,2) or (3,2,2,2,2,2,2), m_0=1.
The coefficient formula at the top remains the specification, used only
through z^16. A successful representing law must match all eight
logarithmic coefficients, not just the seven certified in C874c.
Auxiliary atoms encode S_(j+2); ordinary atoms encode m_j. They must
not be identified. The finite cosine-log interpretation already
assessed for C874c applies at the specified finite order; no claim
that the truncated exponential is a global characteristic function is
permitted, and no vanishing higher cumulants are assumed.

Reuse step2131's inspected September20 ordinary/logarithmic distinction
and November9 L936 fixed-panel comparison. Read the step2132 stop and
step2134 audit history: neither tests m_8. The auxiliary-only stop in
`ATTEMPTS/2026-11-21-single-extension-contact-sign-stop-2128.md` and
C874b fixes S_8 but leaves ordinary realization open. The November9
scope/test assessments concern a different tuple, panel boxes and
singular raw matrices. These recorded failures are preserved and do
not answer this independently specified joint test.

### Search record and limits

Queries issued: `Curto Fialkow 1991 theorem 5.3 truncated Stieltjes even
moments positive definite range`; `"Stieltjes" "m_8" "S_8" contact
moments`; `"Stieltjes" "eighth" "cumulants" moment`; `"prescribed
cumulants" "Gaussian" moment positive`; and `"Curto" "Fialkow"
"5.3" "1991" Stieltjes correction`. Reused the broader prescribed-
cumulant searches documented in the step2131 assessment. No matching
fixed-prefix answer or correction was inspected. Search snippets,
including later moment papers and the CausalSmith cumulant lead,
are unread leads, not imported results or evidence of novelty.

The journal PDF text supplied the complete essential theorem and
proof. Screenshot requests returned references without viewable image
payloads; a separate shell download failed DNS resolution. These are
recorded retrieval limitations, not a theorem access blocker: the
displayed theorem, range column and full proof were accessible as text.
Use the primary statement's nonnegative inequalities and range
condition, not an OCR strict-sign rendering inside its proof.

### Approved bounded continuation

Perform the unchanged TARGET once on a later RESEARCH turn. Compute
both full moment tuples exactly, verify the prescribed coefficients,
and certify the complete even criterion, allowing singular A_4.
Save full evidence under scripts/heat and later canonical mathematics
in its own lemma file; print actual values/bounds, required threshold
zero, failures and certificate paths. Inspect complete load-bearing
records. Existing C874c values may be reused with their audit citation;
any inconsistent lower entry requires retained discrepancy evidence.

Joint witnesses for both prefixes stop this joint finite exclusion.
Exact incompatibility at S_1=16 decides only that fixed tuple, leaving
other S_1 and actual theta open. An unsuccessful strict-PD search is
inconclusive unless the full even criterion is decided. No degree or
parameter sweep is approved. Actual theta, parameter tilts, contact
existence, signed flux, initialization, equality and global/all-degree
closure remain unresolved. Full/supporting Mathlib coverage is not
checked; absence is not asserted. No signed actual-kernel input yet
justifies a creative central-gap nomination. This is routine finite
specialization; this review produces no m_8 value, witness or new lemma.
