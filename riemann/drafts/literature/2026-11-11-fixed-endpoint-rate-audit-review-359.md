# Fixed endpoint complete-rate proof — conceptual-audit nomination

TARGET: Assess source coverage for a conceptual audit of C997p(1)-(14), checking the fixed saddle, nonzero coefficient, both endpoint costs, complete-response dominance and C997n compensation transfer.
CHECKED: 2026-11-11
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Separate literature-only step360 read the full C997p proof and relevant audited C997c/e/n/o contracts; reused reviews345/347/357's exact-family searches, Bessel comparisons and failures. Reopened primary DLMF2.4(iii)-(iv),(2.4.10)-(2.4.16) and7.7.3 for the actual audit boundary; no repeated discovery query or source-blocker retry.
SOURCE_EVIDENCE: Reused Vanlessen https://arxiv.org/pdf/math/0504604v2 (29 August2005),Theorem2.4(b),Proposition3.31,Theorem3.32/(3.110),Proposition5.1/(5.5)-(5.6),pp5-7,32-34,39; DLMF https://dlmf.nist.gov/1.9#iii (1.9.29-31),https://dlmf.nist.gov/1.10#i (1.10.1-3); Axler https://measure.axler.net/MIRA.pdf (12 June2026),Theorem3.31 pp92-93,both proof cases,complex extension after6.22 p157; newly reread https://dlmf.nist.gov/2.4#iv and https://dlmf.nist.gov/7.7#E3. Exact local amplitudes/domain/correction remain the audited C997e/o/n inputs.
COMPARISON: Existing analytic contracts suffice to audit the written fixed-parameter specialization. The scalar saddle/Bessel formulas do not automatically cover its n-dependent exact amplitudes or complete-response comparison; the direct dominated-convergence proof is an appropriate specialization to inspect, not a new general theorem to reprove. No source independently verifies C997p's quantitative claims.
GAP: A later independent conceptual audit must verify C997p(1)-(14) and its concluding compensation comparison: normalization, branches/domain, nonzero coefficient, both vertical sides and horizontal outer pieces, varying-amplitude limit and all complete remainders on one scale. Coverage is ready; correctness remains unresolved.
REASON: Step360 completes the separately requested audit-specific source comparison. SPECIALIZE nominates one later REPRODUCTION conceptual audit, without verifying C997p or deriving mathematics. Its new ready wording receives separate next-turn approval.
LITERATURE_REASON: The saved REVIEW_REQUIRED action requested comparison of the newly written C997p proof with ready sources; audit scope, rather than general asymptotic tools, was missing. That comparison is now complete; unchanged assumptions warrant mathematics next.
SCOPE: Integer n>=2, fixed theta=1, gamma=2, delta=1/8, J=[15/8,17/8], nu_n of C997n(1); fixed A>=A_0>=16 and lambda=A/128 only for compensation; C997o's fixed U and exact C997e amplitudes. No changed family, varying parameters or actual-Xi transfer.
COVERED_TARGET: Audit C997p(1)-(14) and its concluding compensation comparison for the complete fixed theta=1,gamma=2 data asymptotic, checking normalization, branches, nonzero coefficient, both endpoint costs, all competing terms and transfer through C997n(3)-(4).

## Historical nomination — step359

Proposed subsequent mathematical target, not yet approved: audit
C997p(1)-(14)'s complete data asymptotic and its transfer through
C997n(3), accepting the scoped stop or locating a precise failure.
The proof and all qualifications are canonical in C997p; the rational
certificate only checks arithmetic. Do not replace conceptual audit
with rerunning that certificate or assume the new conclusion as input.

Essential inputs are C997c(1),(5), C997e(4),(15)-(16), C997o's
audited full rectangle and uniform amplitude limits, C997n(1)-(4),
and the standard analytic contracts named above. L997 is used only
through C997c/e. C997m is a scope comparison and supplies target
retention through C997n, not a small-theta saddle estimate.

The next source comparison should decide whether the existing
coverage suffices for the proposed audit and record exact approved
wording. No external theorem is currently known to be inaccessible.
Unresolved obligations include source applicability, branch choices,
fixed contour deformation, dominated convergence with varying
amplitudes, normalization and complete-response noncancellation.
Matching Mathlib coverage is unchecked and unknown.

The main gap remains L030-L032/C032a actual-Xi positivity, L966/L968
signed forcing and unpaid L984(H). The point bridge, selected/both-sign
transfer, C997a(8), assay/reconstruction, signed recovery, complementary
zeros, regulators and L993 remain open. No cross-notebook input.
An essential audit is the present blocker to nominating a new central
creative mechanism; none is invented to satisfy a scheduling target.

## Separate source comparison — step360, 11 November 2026

This literature-only step completes the TARGET above. Read all of
C997p, C997c(1),(4)-(6), C997e(4),(15)-(16), C997n(1)-(4) and its
step357 audit's final comparison, and C997o's domain conclusion and
audit acceptance statement. These reads identify application obligations; they do
not independently verify the newly written proof. No lemma, script,
DAG row or PROOF.md argument is changed.

The intermediate target is readiness for one conceptual audit of the
complete fixed-family asymptotic. Its downstream use is deciding
whether this subfamily really fails uniform exponential band suppression,
so that later point-bridge selection can rely on the scoped stop.
Continue with that audit if the inspected standard contracts cover
the written proof; park or narrow it if an essential source contract
is missing. The comparison below finds no such source blocker.
The mathematical acceptance test remains independent verification of
all written hypotheses and errors; a failure calls for a precise
repair or withdrawal of the affected claim, not a general family stop.

### Primary contracts and application boundaries

Reuse review347's primary Vanlessen inspection and review357's
comparison: alpha=2>-1, Q=x has positive leading coefficient,
N=n+1, beta_N=4N. Proposition3.31 cancels the real bulk jump;
Theorem3.32 controls the exact residual matrix off the reduced
contour; Proposition5.1 reconstructs the polynomial with both
oscillatory branches. C997e(15)-(16) retain this matrix and the
scalar normalization exactly. C997o's separately audited fixed
domain, not an arbitrary continuation of a real O term, supplies
the neighborhood of the full rectangle used in C997p. The general
Riemann-Hilbert results are imported by citation, without reproof.
No widened lens or parameter-uniform estimate is needed for this audit.

Reuse review347's inspected Cauchy and Taylor contracts at
[DLMF1.9.29-31](https://dlmf.nist.gov/1.9#iii) and
[1.10.1-3](https://dlmf.nist.gov/1.10#i). Deformation needs the
exact integrand holomorphic on a neighborhood of the closed rectangle;
local logarithm expansions need their own valid disk. C997p uses
the polynomial on outer pieces and a logarithm only centrally.
The later audit must check those domains and retain both vertical
segments. Neither endpoint zeros nor an undeclared branch permits
omitting a contour contribution. Finite complex-measure Fubini is
already covered in review332 and C997c; no infinite zero sum is used.

Newly reread [DLMF2.4(iii)-(iv)](https://dlmf.nist.gov/2.4#iv),
(2.4.10)-(2.4.16), including the assumptions preceding(2.4.12).
The scalar theorem requires analytic phase/amplitude, appropriate
local expansions, absolute uniform endpoint convergence and strict
real-phase separation. Its simple-saddle case specifies a square-root
branch and does not require an exact steepest path. It treats a fixed
amplitude. Thus it is a comparison, not a ready uniform theorem for
C997p's degree-dependent amplitudes; it supplies neither the contour
inequalities nor complete-response noncancellation. Reuse review357's
scalar Bessel comparison without another search or asymptotic import.

Reuse S. Axler, *Measure, Integration & Real Analysis*, author version
12 June2026, [Theorem3.31 pp92-93](https://measure.axler.net/MIRA.pdf),
including both the finite-measure proof and infinite-measure reduction,
and the complex-valued extension after6.22 p157, already fully inspected
in review347. Its required measurable convergence and single integrable
majorant are exactly the contracts to check for the zero-extended,
rescaled integrands. Compactness of each original interval is insufficient
by itself. A direct leading-term limit is justified as a method because
the amplitudes vary with n; the later audit must independently check
their uniform limit, domination and escaping rescaled endpoints.
No stronger general saddle theorem or higher-order expansion is needed.

Newly reread [DLMF7.7.3](https://dlmf.nist.gov/7.7#E3): the
half-line complex Gaussian formula assumes Re(a)>0 and allows complex
linear parameter. Its zero-linear-parameter case is the cited Gaussian
input. C997p must still verify its quadratic sign and branch convention;
this source supplies no nonvanishing assertion for the packet amplitude.
The live DLMF pages were retrieved on 11 November2026; their release
identifier was not independently rechecked in this step.

Olver/Boyd references linked from DLMF and the formerly blocked
Pritsker-Varga lead were not read here and are not essential inputs.
No source access retry or claim of exhaustive discovery is made.
Matching Mathlib coverage remains unchecked and unknown; no absence
or formal verification claim is inferred.

### Duplicates, scope and exact later audit

Reuse reviews345/347/357's exact-family searches and C997f/g/i/l
comparisons. Read the strong-taper failure347 and its step349 audit
annotation. C997m's accepted leakage requires theta>=Theta_0 and
lambda>=A; it does not import the proposed theta=1,lambda=A/128
conclusion. C997i retains its degree<=n and large-A hypotheses.
C997o supplies a domain; C997n supplies a correction conditional on
a separate data lower bound. None independently verifies C997p.
The fixed subfamily in C997p is not a reopening of those stopped
regimes, and historical stops are not bans on other mechanisms.

The exact COVERED_TARGET is ready as SPECIALIZE / REPRODUCTION,
task proof_audit/conceptual_audit. The later audit must check:

1. C997p(1)-(5): real normalization and original TV, the exact
   complete-response identity, every exponential sign and factor,
   uniform holomorphic amplitude limits and the entire Rem_n.
2. (6)-(9): the actual stationary point and branch choices, claimed
   fixed-domain phase sign, rate margin, and nonzero amplitude at
   the prescribed fixed point. These remain claims to audit.
3. (10)-(14): both vertical sides, both horizontal outer pieces,
   central curvature, varying-domain dominated convergence, Gaussian
   normalization and suppression of the other Laguerre branch on
   the same leading scale. Arithmetic replay cannot establish these
   analytic hypotheses or complete-response noncancellation.
4. The concluding comparison with audited C997n(3)-(4), including
   the compensation normalization, strict rate separation and
   quantifiers through sufficiently large integers. Accept only the
   fixed subfamily, or identify the exact failed hypothesis/estimate.

No mathematical audit was performed in this source step. Outcome is
EXPLORATION / LITERATURE / NOVELTY_UNCHECKED: audit-specific coverage
is now prepared, without mathematical progress beyond the cited tools.
The main actual-Xi/signed-forcing/H gaps remain as in the nomination;
the new ready continuation needs its separate approval next turn.
No justified central creative mechanism was prepared: the essential
conceptual audit is the present blocker. No extra literature turn is
warranted on unchanged assumptions. No cross-notebook input is used.
