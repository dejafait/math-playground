# Global variation closure: separate conceptual-audit coverage

TARGET: Assess literature coverage for a separate conceptual audit of L521's global translation-quotient closure, including endpoint renewal cutoffs, interior L1 absorption and the full signed model.
CHECKED: 2026-10-30
DECISION: EXPLORE
SEARCH_EVIDENCE: Reused the completed global-BV comparison and approved construction assessment; searched the specific global-variation histories, working notes and automatic-BV import stop. Read all of L521 to delimit its audit, plus the relevant L513/L515/L520 input statements. Reopened the primary BV criterion and renewal statements/proof cases below; no repeated broad search or novelty claim.
SOURCE_EVIDENCE: Galerne (2016), doi:10.1017/apr.2016.60, Section 2 Lemma 1/Theorem 1 and proofs pp.951–953, direct publisher PDF below; Grzywny–Ryznar arXiv:1107.0745v1 Section 3, Proposition 3.2, Proposition 3.5's upper-bound proof, Remark 3.6 and Lemma 4.1's alpha=2 case. Reuse the primary regularity exclusions in the completed comparison and the audited local inputs L513/L515/L516/L520; imported manuscript proofs remain qualified.
COMPARISON: Galerne supplies the criterion, not the model estimate. The renewal source supplies monotonicity and a nonnegative occupation identity, not signed global BV. L521's absolute signed interchange, two truncated collar bounds, small L1 inverse, relative commutator and absorption are local proof obligations, not theorem imports. No matching full-model result was found in the reused comparison.
GAP: Independently verify or locate a precise failure in L521 (2)–(20), including domain/localization and every signed cutoff term, without assuming BV. The source comparison does not certify any of those estimates or their resulting global closure.
REASON: Separate source-scope review is complete; no essential unread theorem is needed for the bounded conceptual audit under the unchanged hypotheses. The next audit is covered below, subject to the supervisor's separate approval of this newly ready continuation. This is process progress only, not a new mathematical result.
SCOPE: Exactly L520's fixed complete signed model with 0<a<A, ell=2a>log(2), real normalized nullvector, nonzero left trace and excluded direct reflected-endpoint collision; both half-line operator splits, all cutoff-equality atoms, nu_rho, c=log(2pi) and signed pole retained. No family-uniform conclusion or Xi realization.
COVERED_TARGET: Critically audit L521 (2)–(20) under its unchanged full signed-model hypotheses, requiring both endpoint collars and interior absorption to yield theta<=1/2 with finite h-independent error without assuming BV.

LITERATURE_REASON: The construction target was ready, but its newly
written conceptual-audit scope was REVIEW_REQUIRED at invocation.
Reuse its adequate literature assessment and check the exact imported
hypotheses; do not reopen the already-covered construction search.

The result to be audited is
[L521](../../lemmas/L521-fixed-model-global-translation-variation.md).
Its construction used the prior
[approved target](2026-10-30-weil-global-translation-variation-test.md)
and [completed primary comparison](2026-10-30-weil-nullvector-bounded-variation-coverage.md).
The [Galerne publisher PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/83627D38EAB49283AE917366027E8BE7/S0001867816000604a.pdf/random_fields_of_bounded_variation_and_computation_of_their_variation_intensity.pdf)
is the already-inspected deterministic criterion, not a theorem
establishing the model's finite quotient norm.

Retain L520's fixed hypotheses: 0<a<A, ell=2a>log(2), real
normalized nullvector, nonzero left trace, and the excluded direct
reflected-endpoint collision. Keep c=log(2pi), nu_rho, every
prime-power atom including cutoff equality, and the signed pole.
L513 supplies normalized renewal inversion; L515 supplies bounded
data and the half-line splits; L516 fixes the complete model; L520
supplies the L1 resolvent kernel and justified local inverse. No
cross-notebook input or expansion of these hypotheses is proposed.

The bounded critical test is the claimed inequality with a finite
h-independent error and absorption coefficient at most 1/2. The
endpoint collars must be fixed before the frequency cutoff; each
unknown quotient must be finite before subtraction, with no global
BV premise. Review also the signed exterior forcing and all cutoff
jumps. An interior-only estimate or assumed trace-error derivative
would fail. The desired audit is proof_audit/conceptual_audit at
deep_research/xhigh after its scope is separately approved.

Global BV could support later individual prime Stieltjes formulas.
Those formulas, their signs, eigenvalue-relative saving, nullvector
existence, full-Weil identification, branch rates, collars and Xi
transfer remain outside this continuation. Matching Mathlib coverage
is unchecked. No further lemma is proposed or derived here.

## Separate scope review, 2026-10-30

The original continuation above identified the pending obligations.
This review approves their investigation, not their conclusions.
The audit object was read in full for source attribution and scope;
its estimates were not independently proved or certified this turn.

Reopened Galerne's
[primary publisher PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/83627D38EAB49283AE917366027E8BE7/S0001867816000604a.pdf/random_fields_of_bounded_variation_and_computation_of_their_variation_intensity.pdf),
Section 2, Lemma 1 and Theorem 1, pp.951–953. Hypotheses are an
open U, f in L1(U), and a unit direction. Lemma 1 assumes finite
directional variation; Theorem 1 characterizes it by finite quotient
liminf and identifies the derivative measure and variation limit.
Read the smooth-density case, distributional test identity,
compactness and lower-semicontinuity proof cases. For U=R in dimension
one there is no erosion; bounded compact support from L515 supplies
integrability. The later audit must check the positive/negative
translation convention. This criterion needs citation, not a reproof;
its missing finite-bound premise is precisely L521's asserted work.

Reopened Grzywny–Ryznar,
[*Potential theory of one-dimensional geometric stable processes*,
arXiv:1107.0745v1](https://arxiv.org/html/1107.0745v1), Section 3,
Proposition 3.2, Proposition 3.5's upper-bound proof, Remark 3.6,
and Lemma 4.1's alpha=2 proof case. Proposition 3.2 assumes a
symmetric non-compound-Poisson process with a complete-Bernstein
exponent psi(xi^2); it supplies completely monotone V'. The occupation
identity in Proposition 3.5's proof is for nonnegative measurable
data. Its cited origin is Bertoin, *Levy Processes*, Chapter VI,
Theorem 20, p.176; the book proof is reused through the existing
assessment, not freshly inspected. L513 records the normalization
V=sqrt(2)V_GR for the slowed exponent and retains the nonzero linear
renewal term at alpha=2. Keep that normalization and the killed
half-line realization. Signed inversion and absolute exterior
integrability are the separately qualified local L513/L515 inputs;
the occupation formula alone does not establish them or global BV.

The earlier comparison's Kulczycki–Ryznar harmonic/nonnegative-data
restriction and Jarohs–Kassmann–Weth kernel-BV/solution-continuity
distinction remain adequate and were not rebrowsed. The
[automatic-BV import stop](../../ATTEMPTS/2026-10-30-weil-global-bv-automatic-source-import-stop.md)
is preserved. Specific global-variation histories and the construction
notes contain L521's attempt but no earlier independent audit or
ready theorem replacing its closure. No novelty follows from this
bounded comparison, and no new theorem search is needed to audit
the explicit local argument.

The bounded audit must address all of the following together:

- L521 (2)–(9): finite signed measure and exterior L1 forcing,
  absolute renewal interchange with its almost-everywhere scope,
  and both jumps of each sharp cutoff, including exterior data.
- L521 (10)–(13): both reflected collars, the global partition,
  and a fixed spatial delta giving the stated endpoint coefficient;
  no derivative bound on a trace little-o may be inserted.
- L521 (14)–(18): smallness in L1 operator norm, not multiplier
  decay; the commutator's relative quotient estimate; localized
  operator domains and agreement of the L2 and L1 identities.
- L521 (19)–(20): fix delta before choosing N; verify theta<=1/2
  and a finite h-independent remainder. Each Q_h must be finite
  before subtraction. Retain all atoms and both signed densities.

Continue only if the complete inequality passes independent scrutiny;
otherwise identify and preserve the first load-bearing failure and
park that claimed closure. This is not a test of RH or a disproof
of BV. Passing could enable individual prime Stieltjes correlations,
but those formulas and their signs require a later covered target.
No mathematical script, lemma modification, DAG edit or overview
change was made by this literature-only review. Mathlib matching
remains unchecked. No source-access blocker or cross-notebook input
was introduced.
