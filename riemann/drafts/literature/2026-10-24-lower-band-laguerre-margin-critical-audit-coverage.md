# Coverage nomination: lower-band Laguerre margin critical audit

TARGET: Critically audit C458a's conditional lower-band Laguerre margin, checking the complete L457/L458 error comparison, exact normalization and one uniform onset on the closed band.
CHECKED: 2026-10-24
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the completed exact-band assembly search and L457/L458 audit assessments; read C458a in full and compared the input statements and concluding audit passages, the C455a audit scope and recorded L456 failure. No new external discovery search or originality claim.
SOURCE_EVIDENCE: Reused inspected DLMF 2.4.10–2.4.16; Temme arXiv:1308.1547v1 Sections 2.2–2.3 and 4.1; Csordas arXiv:1309.0055v2 Lemma 3.6 and Theorem 3.7 (3.10)–(3.14); DLMF 2.3.21–2.3.23 and 7.2.6–7.2.9; Titchmarsh–Heath-Brown (1986), Theorem 14.2 and Section 14.3, pp. 336–339, via saved assessments; pinned September 30 Theorem 1.1 via the external-input register. No primary page newly fetched or external manuscript verified.
COMPARISON: The written C458a application uses the identical L457/L458 real-r/even-m closed-band domain and full finite sum; its additional source requirements are only elementary relative-error and uniform-onset comparisons. C455a has a narrower different band and fixed-center normalization, so its audit verdict cannot substitute for this audit.
GAP: A separate correctness verdict must check the complete additive error divided by M*, the claimed relative rate, exact positive factorial/reflection multiplier and one real-r onset. This source comparison supplies no such verdict.
REASON: Existing adequate primary-source coverage and audited input interfaces cover this precise critical-audit scope; approve one REPRODUCTION proof audit without repeating discovery or removing external trust qualifications.

SCOPE: C458a on positive real r, positive even m, 7/8≤m/r≤31/32, with its unchanged coupled h,a,S,P and M*; no domain extension, external-manuscript audit or RH claim.
LITERATURE_REASON: The newly nominated C458a critical audit was REVIEW_REQUIRED and outside the preceding assembly-only approval; this separate comparison now completes its exact-scope coverage using saved evidence.

## Original nomination, preserved

The following paragraphs record the pre-review proposal; their future-tense approval requests are discharged by the completed comparison below.

Essential inputs are C458a, L457 and L458. The exact domain is positive
real r, positive even m, 7/8≤m/r≤31/32, h=9/2+m/(2r), and
a=sqrt(4π²exp(4r)−h²)>0. Preserve the full finite S with zero
cutoff equality, the exact positive P=[2^(m−1)/m!]C₀exp(Φ_*)π/a
and L457's M*>0, |log M*|≤K r^(2/3).

The proposed audit checks that the complete relative error is
δ+ε/M*, with |δ|≤C_A(log r)^3/sqrt(r) and
|ε|≤C_E(1+r)²exp(−r/200), and verifies all limits and one
common real-r onset in C458a. It should inspect C458a in full and
the exact input conclusions/audit passages; repeat deep saddle or
sector proofs only if a specific defect requires it. Check duplicate
scope against C455a without importing its narrower-band conclusion.

L457 retains L452/L456 and September 30, 2026 Theorem 1.1 at
commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a`: strict
Re(s)>7/8, allowed pole at one, external manuscript/import closure
unaudited locally. L458 has no external zero-free premise. The audit
must not remove these qualifications or replace M* by a fixed-center
zeta square. L323/L327/L456 stops remain scoped evidence.

Continue the audit if the saved source coverage covers this precise
application and all bounds and normalizations agree; otherwise record
the missing hypothesis/source or exact defect. Every-height transfer,
initial low-index signs, bounded heights, global mixed positivity and
selected-law/regulator gaps remain outside scope. Full matching
Mathlib coverage is unchecked. This nomination neither approves new
mathematics nor rejects the completed assembly.

## Completed separate scope comparison — 2026-10-24

The main gap remains initial low-index signs and global mixed positivity.
The intermediate target is a correctness verdict on the conditional
C458a assembly. A reliable coupled lower-band sign margin could support
later every-height transfer; it does not supply that transfer, bounded
heights, the remaining indices or any global positivity implication.

Read C458a's complete statement and proof to identify the required
sources, without performing its correctness audit. Compare L457's
Hypotheses, Conclusion, Section 6 and concluding separate audit, and
L458's Hypotheses, Conclusion and final normalization/onset audit.
Both inputs explicitly use positive real r, positive even m, the closed
band 7/8≤m/r≤31/32, identical h,a and the finite sum with zero cutoff
equality. L457 already states a positive M*, its logarithmic bound and
complete relative arithmetic error. L458 already states the full real
additive error and exact positive P. No extended uniformity theorem or
unread theorem is essential to audit this downstream application.

Reuse the [assembly assessment](2026-10-24-lower-band-laguerre-assembly-coverage.md)
and the [moving-saddle](2026-10-23-lower-band-moving-saddle-critical-audit-coverage.md)
and [theta](2026-10-24-lower-band-theta-critical-audit-coverage.md)
audit assessments. Their primary source records cover
[DLMF 2.4.10–2.4.16](https://dlmf.nist.gov/2.4#iii) and
[Temme, arXiv:1308.1547v1](https://arxiv.org/html/1308.1547v1),
Sections 2.2–2.3, (2.9)–(2.13), and 4.1, (4.1)–(4.5): analytic
neighborhoods, endpoint convergence, the two saddle half-paths,
direction-selected Gaussian root and separate pole handling. These do
not state the parameter-uniform paired-zeta margin; that is the local
L457 input, with its already completed audit.

For L458 reuse [Csordas, arXiv:1309.0055v2](https://arxiv.org/html/1309.0055v2),
Lemma 3.6 and Theorem 3.7, (3.10)–(3.14), for the associated-kernel
coefficient identity, not automatic positivity. The saved inspection of
[DLMF 2.3.21–2.3.23](https://dlmf.nist.gov/2.3#iv) includes smoothness,
nonstationarity away from the endpoint, differentiable expansions and
controlled endpoint limits; both finite endpoints contribute.
[DLMF 7.2.6–7.2.9](https://dlmf.nist.gov/7.2#iii) supplies scalar
Fresnel definitions and limits. Neither source gives L458's complete
moving-domain uniform error; use that locally audited input directly.

Titchmarsh–Heath-Brown, second edition (1986), Theorem 14.2 and
Section 14.3, pp. 336–339, are reused through the assembly's saved
Littlewood comparison. Its printed RH assumption cannot simply be
replaced in the theorem statement; L452/L456/L457 contain the local
analytic-logarithm specialization. The exact pinned external theorem
and its qualifications remain those in the
[register](../../foundations/2026-10-quasi-riemann-input.md): September 30,
2026, Theorem 1.1 at commit 1581d4cbdd69a0faf34b2089614fe2a814316a6a,
strict Re(s)>7/8, allowed pole at one, unaudited external manuscript
and formal import closure. This review does not verify that theorem.
Full matching Mathlib coverage is unchecked; absence is not asserted.
No primary source was freshly retrieved, and no new reproof is needed.

The [C455a audit comparison](2026-10-23-subendpoint-laguerre-margin-critical-audit-coverage.md)
is a process and method precedent, not approval of the current domain:
it uses 31/32≤m/r≤63/64 and a fixed-center square. C458a must retain
M*, not assume relative freezing to that square. The assembly assessment
already screened L323's larger-strip and L327's PSD failures. The read
[L456 failure record](../../ATTEMPTS/2026-10-23-lower-band-fixed-circle-freezing.md)
explicitly leaves moving-saddle comparison open. These scoped stops
remain evidence, not global prohibitions. No inspected external theorem
already gives this exact assembly, and no novelty follows from that fact.

Continue with one separate critical audit if all canonical hypotheses,
complete error bounds and exact normalizations agree. Check the claimed
comparison of q=C_E(1+r)^2 exp(−r/200+K r^(2/3)) with
(log r)^3/sqrt(r), and the single onset independent of m, rather than
accepting formal error labels. If any check fails, record the exact
inequality or missing hypothesis and repair or withdraw only that claim.
Deep saddle/sector proofs need reopening only on a specific defect.
This turn does not decide any of those mathematical checks. The visible
literal '+covers' in C458a's assessment-link sentence is an editorial
artifact, not an additional mathematical premise; leave lemma editing
to the authorized research audit.

Outcome: EXPLORATION / LITERATURE / NOVELTY_UNCHECKED. This is a new
exact-scope approval using ready source evidence, not a mathematical
advance or progress beyond those sources. No lemma, script, DAG or
PROOF change is made. Mathematical exploration usage remains 0 of 3,
neither spent nor reset by this review. The unchanged exact target is
ready for the subsequent REPRODUCTION proof audit.
