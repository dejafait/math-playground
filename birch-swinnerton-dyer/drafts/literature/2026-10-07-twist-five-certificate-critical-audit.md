# Twist-five finite certificate — approved critical-review scope

TARGET: Critically audit L031's fixed twist-five certificate, checking base optimality, cusp denominators, total-period factors, every outward interval and exact rational isolation without BSD or L030's normalization scalar.
CHECKED: 2026-10-07
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the unchanged fixed-input production and independent-value assessments; compared L031 and the verifier source boundary with their covered hypotheses; checked ATTEMPTS/022--023 and history/075--076; no broad discovery search repeated.
SOURCE_EVIDENCE: Reused full primary coverage in drafts/literature/2026-10-07-independent-twist-five-value.md and the calibration audit; spot-read Wuthrich v2 Proposition 1/Lemma 4 https://arxiv.org/pdf/1608.06423v2, Cesnavicius Theorem 2.13 https://arxiv.org/pdf/1703.02951, Cremona Theorem 5.2 https://wstein.org/papers/ars-manin/html/node13.html, Chapter 2 Section 2.11 https://johncremona.github.io/book/fulltext/chapter2.pdf, Chapter 3 Section 3.7 https://johncremona.github.io/book/fulltext/chapter3.pdf, Pal v2 Corollary 2.6/Theorem 3.2 https://arxiv.org/pdf/1012.0094v2 and DLMF https://dlmf.nist.gov/19.8.i.
COMPARISON: Existing coverage supports a fixed-input critical audit of a known rational-recovery specialization; no theorem certifies these particular stored intervals or implementation. Source hypotheses and complete finite evidence must be checked separately in the research audit.
GAP: Literature scope is ready; correctness of L031 source application, every outward operation, all-n tail and exact rational isolation remains for the separately invoked audit. No audit verdict, new value or BSD result is supplied here.
REASON: Separate literature-only approval of the saved critical-review target, reusing adequate coverage without extending its curve, twist or period hypotheses; this process approval is STALLED rather than new mathematical evidence.
SCOPE: Only L031 for E=[0,1,1,-2,0], d=5, total minimal Neron periods and B=2; no uniform twist production, coefficient or BSD claim.

## Preserved pending scope from the production step

Reuse the adequate primary theorem/proof coverage of the unchanged fixed
curve in the production assessment. The next literature step should
confirm that it covers the precise critical audit; it must not repeat a
broad search or approve and perform uncovered mathematics in one turn.
Primary direct URLs are retained in that assessment and in L031.

The audit inputs are L031, L030's minimal arithmetic and its complete
arithmetic certificate, and `scripts/twist-five/certify.py`, `verify.py`,
`certificate.json` and `verification.json`. L028 is used only for the
already recorded conventions and possible downstream calibration.
Check optimal label versus exact model, c=1 on the base only, all four
unitary cusps, the total/least-positive period factor, the positive-d
minimalization hypotheses, bad-prime point-count/Fricke sign, the all-n
coefficient bound, signed interval propagation, finite AGM bracketing
and existence as well as uniqueness in exact rational isolation.

The arithmetic verifier validates the complete finite evidence and
records that it does not verify external theorem statements. The new
audit should continue only if source applicability and full error
coverage are correct; a specific error must be repaired or recorded.
No general BSD candidate exists. Later calibration needs good ordinary
p>=5 with p!=5; C, b, other L026 premises, F, divisible Sha, rational
membership and complex-order comparison remain unresolved.

## Separate approval, 2026-10-07

STEP BSD-2026-10-07-077-twist-five-audit-source-approval approves exactly
TARGET above. The previous pending text records the scope at production;
its request for separate approval is now fulfilled. This is approval to
perform a mathematical audit, not acceptance of the certificate.

L031 was read in full. The production assessment and independent-value
comparison were read, including their qualifications and duplicate routes.
L030's arithmetic statement and proof through minimality/conductor were
read only to identify the existing arithmetic input. The first 100 lines
of verify.py were inspected only to distinguish declared source parameters
from finite arithmetic checks; no implementation verdict or certificate
replay is claimed. No lemma or mathematical script was changed.

### Coverage matched to the audit

Wuthrich v2 (arXiv banner 23 March 2017), Proposition 1, printed pp. 3--4,
retains the strong-Weil Manin constant assumption and the unitary-cusp
restriction. Read its definition and torsion-reduction proof case; the
least-positive-period convention differs from the total real period.
Lemma 4, printed pp. 6--7, uses the all-n coefficient bound and a geometric
tail, not a finite coefficient experiment. These are the denominator and
tail sources already assessed. The audit must check their specialization
as written, including all four cusps, rather than grant B from JSON.
Lemma 6 concerns floating-point errors; L031 instead claims exact rational
outward arithmetic, so its implementation needs direct proof/replay.

Cesnavicius arXiv:1703.02951, Theorem 2.13 and proof, printed p. 9,
were spot-read with the new optimal quotient and prime-square level
restriction retained. Optimality and the exact model/torsion row remain
the separate published Cremona inputs in the production assessment:
Appendix Theorem 5.2 (N<60000, exception 990h), ecdata Table One conventions
https://johncremona.github.io/ecdata/ and the exact allcurves row at
https://raw.githubusercontent.com/JohnCremona/ecdata/master/allcurves/allcurves.00000-09999.
The already inspected table is reused; it was not freshly downloaded.
Its rank column is excluded. No additive-twist Manin constant theorem
is required or approved. Published optimality is imported, not reproved.

Cremona corrected second edition (1997), Chapter 2, printed pp. 37--39,
Proposition 2.11.2 and the following character-cycle calculation were
spot-read. Both sign branches and the oriented Gauss-sum identity are
covered. Chapter 3, Section 3.7, printed pp. 97--98, covers the ordered
real-root positive-square-root AGM period formula; Section 3.9's elliptic
Euler factors and bad-prime point-count convention retain the production
assessment's coverage. The audit must distinguish Fricke eigenvalue from
root number and verify the finite point-count inputs; a sign permits a
nonzero value but does not prove it.

Pal v2 (21 January 2011), Corollary 2.6, printed p. 6, and its odd-prime
and 2-adic proof, plus Theorem 3.2, printed pp. 7--8, were spot-read.
The entire positive-d proof (3.1)--(3.2) integrates the absolute minimal
differential over the full real locus. Coprimality to the minimal
discriminant and d=1 modulo 4 remain essential. The audit must match both
real components and the minimalization factor; negative-twist statements
are outside this scope. No independent value comes from this theorem.

DLMF Section 19.8(i), equations 19.8.1--19.8.5, positive AGM iteration
and common-limit coverage, is reused with the directly accessible page.
It supports the analytic period mechanism, not stored endpoint accuracy.
Elementary Machin/Taylor identities, root bisection, signed outward
arithmetic, finite AGM bracketing and rational enumeration are the written
finite proof being audited. Checking them is the difference from source
import, and justifies SPECIALIZE and a later REPRODUCTION classification.
Full matching Mathlib coverage remains not checked; unknown is not absent.

### Bounded continuation and exclusions

The intermediate target is to validate or identify a specific defect in
L031's independent q certificate. Its plausible use is L028's calibration
and then L027's denominator input. The main rank gap for analytic order
at least two, C, b, other L026 premises, F, divisible Sha, rational Kummer
membership and complex-order comparison remain unresolved. No uniform
production or BSD candidate is in scope.

Essential inputs: L031; L030's minimal arithmetic and complete relative-t2
certificate.json, verification.json and audit.json; twist-five certify.py,
verify.py, certificate.json and verification.json; L028 conventions only.
The research audit must inspect complete relevant evidence, not previews.
Retain q=4 only after checking imported hypotheses, denominator existence,
total-period scale, every finite error and infinite tail, and exact reduced
rational isolation. A concrete failure requires a recorded correction or
specific rejection of that certificate; an unresolved source hypothesis
parks its dependent claim. Do not silently assume BSD or L030's unknown
normalization scalar. Later calibration retains good ordinary p>=5, p!=5.

ATTEMPTS/022--023 stop repeated conditional audits without production.
This audit concerns newly produced finite evidence in L031, so is a
separate bounded correctness check; it does not remove those stops.
The review supplies no new theorem coverage and makes no novelty claim.
No essential source blocker was found; no broad search or new mathematics
was undertaken. The exact saved target is ready for one research audit.
