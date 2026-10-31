# Explicit tail on a fixed positive-time band — source comparison

TARGET: Assess whether Polymath v2's explicit estimates give a numerical real/simple tail cutoff for F uniformly on 1/100<=lambda<=11/200.
CHECKED: 2026-10-30
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Exact arXiv/title and explicit real/simple-cutoff searches, plus narrow positive-time/Polymath local comparisons; queries and inspected evidence are recorded in drafts/heat/2026-10-30-explicit-positive-time-tail-source-review.md. No additional matching numerical-cutoff theorem was imported, and no novelty or global absence is inferred.
SOURCE_EVIDENCE: D. H. J. Polymath, arXiv:1904.12438v2 (4 August 2019), https://arxiv.org/html/1904.12438v2 , (5)–(24), Theorem 1.3, Corollary 1.4, Theorem 1.5(i)–(ii), Proposition 6.6(i)–(vi), Proposition 9.1 and Lemma 9.2 with proofs, and (102)–(104) with the following exhaustion argument were inspected. Explicit input formulas and qualifications are retained in drafts/heat/2026-10-30-explicit-positive-time-tail-source-review.md.
COMPARISON: Theorem 1.3 supplies numerical approximation errors on the needed strip, but Theorem 1.5's real/simple count, Proposition 9.1 and Lemma 9.2 retain unspecified thresholds/errors. L488's existential cutoff therefore cannot receive a numerical value by direct citation; additional quantitative specialization is needed.
GAP: No numerical R_0 or strict count at its edge is established. Missing local work includes a uniform numerical two-term remainder, quantitative phase variation/separation, strict contours, whole-strip exhaustion and threshold padding; the inspected explicit formulas cover a preparatory residual calculation without a new source theorem.
REASON: Stop direct cutoff extraction, then test a bounded residual specialization before attempting numerical zero counts. An effective tail would bound the collision-search domain in this fixed band but leave interior exclusion, lambda<1/100 and zero-time control unresolved.
SCOPE: Completed literature-only comparison. SPECIALIZE records partial coverage by explicit known estimates, not approval or proof of a full numerical tail. The separately stated residual target in drafts/literature/2026-10-30-explicit-two-term-tail-remainder.md has the narrower scope; no new lemma, script or source-proof audit was performed here.
LITERATURE_REASON: This turn inspected the previously unread explicit primary estimates and real/simple counting cases because numerical effectivity was outside the ready existential-tail and C489a application coverage. That missing coverage is now resolved for the nominated residual specialization.

## Reviewed question and decision

Seek a stated numerical R_0 such that, for every real lambda in the
closed interval [1/100,11/200], every zero of F(lambda,.) with
|Re z|>=R_0 is real and simple. The existing identity
F(lambda,z)=8 H_(4lambda)(2z) sets the source time band
[1/25,11/50]. This change of variables is an existing input, not a new
effective estimate. Start with the primary theorem statements and
necessary zero-localization/counting cases before loading larger proofs.

Direct numerical-cutoff extraction does not pass: the zero-count and
phase statements retain unnamed constants. The approximation errors
are explicit, so no inaccessible source blocks a narrower residual
calculation. Its proposed bound and height are not yet verified. The
source comparison and precise remaining counting obligations are in
the source note named above. A numerical approximation to a zero or
an unspecified O-constant cannot replace a strict counting certificate.
No blocked scan retrieval or endpoint-integrability attempt is resumed.

The potential use is a finite spatial rectangle for threshold collisions
whose time lies in this fixed band. It does not make that rectangle
zero-free or collision-free, and does not treat arbitrarily small
positive transition times. C489a's conditional failure-of-RH premise and
the source-proof/certificate qualifications remain in force. Full
matching Mathlib coverage for the effective target is unchecked.

The endpoint inverse-gap route is still parked for its documented
Hamiltonian/source gap. Generic shape and bounded negative-energy
comparisons remain obstructed by their existing countermodels. No
theta-specific sign or arithmetic input has been identified here that
would justify a creative collision-exclusion attempt. This narrower
effective-source question is independently testable; it is not a renamed
attempt at either stopped mechanism or a claimed new route to RH.
