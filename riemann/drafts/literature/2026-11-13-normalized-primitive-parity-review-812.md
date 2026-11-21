# Normalized primitive as a different parity comparison — source review

TARGET: Assess source coverage and recorded obstructions for Q(Pf)/||Pf||_2^2 <= Q(f), where Pf(x)=integral from -1 to x of f(t)dt, on real odd unit vectors with Q(f)<=1/250 in C759a's complete form domain; determine whether a bounded primitive-based parity test is justified.
CHECKED: 2026-11-13
DECISION: EXPLORE
SEARCH_EVIDENCE: Step813 completed bounded primitive/antiderivative/Volterra and parity searches in active-notebook assessments and ATTEMPTS, then exact/stronger-result web searches listed below. No inspected theorem gives the proposed capped complete-form comparison; this is not a novelty finding.
SOURCE_EVIDENCE: Inspected Suzuki2606.09096v2 Theorem1.1, (1.8), Section2.4/(2.7) and the following digamma/polar passage, Lemma3.1/proof and Section3.2 closure setup; v3 Sections8.2/8.4/8.5, (8.2)/(8.6)/(8.7), including the integral normalization argument and final metric warning. Read Andrews-Connes-La Gatta2611.13129v1 Lemma8.16/proof and Theorem7.1/hypotheses; DLMF5.9.12-13 with Re(z)>0. Reuse C759a/d/e and assessment548 as scoped below; direct URLs follow.
COMPARISON: The primitive representation and its nontrivial norm metric are standard inputs, not an energy-order theorem. Conditional finite-block/ground-state results do not prove the proposed map comparison. Modulus and fixed-shift stops remain scoped; a fixed two-sine primitive slice is a different independently testable specialization.
GAP: The complete normalized defect on the full capped odd domain remains unsigned. No uniform norm lower bound, full parity ordering, ground-state sign/simplicity, all-window control or Xi realization is supplied. Finite-slice admissibility, nonzero normalization, signed entries and rigorous remainders must be proved in the subsequent calculation.
REASON: Missing source comparison is now supplied; nominate one finite two-sine sublevel test, not a proof of the uniform assertion. No new identity, inequality, lemma or mathematical script is derived in this literature-only turn.
LITERATURE_REASON: Invocation-start REVIEW_REQUIRED covered a new map outside the ready modulus assessment; this review supplies its essential domain, metric and complete-form source comparison.

The preserved nomination below describes the questions at invocation
start; its unreviewed wording is superseded by the completed comparison
below. This was a future-target nomination, not a second mathematical attempt
in step812. The main goal is actual-Xi all-degree mixed positivity.
A successful parity comparison could supply a variational ordering input;
ground-state sign/simplicity, all-window control and Xi realization would
still be independent gaps. No such implication is assumed to close RH.

For real odd f on(-1,1), consider the displayed primitive on that
interval with zero extension and normalize only if its L2 norm is
nonzero. Source review must check its precise domain, parity, endpoint
behavior and normalization, rather than silently treating it as a
unitary operator or a form contraction. Keep the full unneutralized Q,
both poles and every overlapping prime power. No positivity of Q or
of its mixed terms is available as an assumption.

The exact inequality is a proposal to assess, not a result inferred
from smoothing. Review standard antiderivative/intertwining and
variational comparisons, stronger results and counterexamples under
these hypotheses. Compare only relevant local failures before loading
their proofs. No cross-notebook input is nominated. Missing source
coverage must remain REVIEW_REQUIRED or SOURCE_BLOCKED.

A subsequent bounded test, if justified by that review, should either
produce a sign-controlled complete-form comparison with stated scope or
an eligible counterexample to this precise map. A first-sine pass alone
would not establish the sublevel assertion; a rigorous eligible failure
would abandon it. Do not retest modulus, alter the cap or sweep windows
under this nomination. The review should choose and separately approve
one concrete test, or park this proposal if there is no discriminating
mechanism. A genuinely new central mechanism may merit creative routing;
a fixed-entry specialization remains calculation/reproduction.

Matching Mathlib coverage and external theorem coverage for this new
assertion are unchecked. The current source identities are supporting
inputs, not an approval to derive the proposed comparison in this turn.

## Completed source comparison — 13 November 2026, step813

The main gap is L030-L032/C032a actual-Xi all-degree mixed positivity.
The proposed intermediate comparison could inform a variational parity
ordering. It would leave simplicity, signs, other windows and Xi
realization unpaid even if the full capped assertion were established.
Continue by one bounded slice test; abandon the exact map assertion if
one unit odd eligible input has a rigorously positive normalized defect.
A pass on the slice supplies no conclusion for its infinite complement.

### Primary inputs and their limits

[Suzuki v2](https://arxiv.org/html/2606.09096v2#S2.SS4), Theorem1.1,
(1.8), Section2.4/(2.7) and its digamma/polar continuation identify the
Friedrichs realization for a>0 and the complete formula on H_0^1.
Lemma3.1/proof and Section3.2 give inclusion and form-core closure.
[Suzuki v3](https://arxiv.org/html/2606.09096v3#S8.SS2),
Sections8.2/8.4/8.5, (8.2)/(8.6)/(8.7), give the mean-zero inverse
derivative, its inverse-Neumann norm metric, and a generalized quotient;
they warn that the two compact operators' interaction still needs control.
Section8.2 writes D=i d/dx but its integral display omits the phase:
retain the norm identity, and check the real-primitive convention locally.
Neither version supplies the proposed inequality. These are supporting
inputs, not a primitive contraction theorem.

The specialization must set a=1, use C759a's complete real Q and its
Fourier convention, and check support, mean zero, both endpoint traces,
parity and nonzero normalization for the chosen inputs. An inverse
derivative is not asserted to be unitary or uniformly bounded below on
the full capped domain. For the finite test, direct application to the
specified functions suffices; no new general realization theorem is
needed. No operator or spectral conclusion from Section8 is imported
without its metric.

[Andrews, Connes and La Gatta v1](https://arxiv.org/html/2611.13129v1#S8.SS6),
Lemma8.16 and its complete square-completion proof require a positive
complementary floor and form-dual coupling. Theorem7.1 requires a simple
even finite ground state. Neither asserts this primitive comparison;
their hypotheses cannot be supplied by numerical parity observations.
Searching the primary HTML for primitive and antiderivative found no
occurrences. This is a bounded overlap check, not a survey of all papers.

[NIST DLMF5.9.12-13](https://dlmf.nist.gov/5.9#ii) require Re(z)>0;
z=1/4+it/2 stays in that half-plane. Reuse their role in L741 and
C759d/e for complete gamma-kernel evaluation. Existing tail estimates
are function-specific: a changed primitive correlation needs its own
proved convergent expansion or integral remainder, not copied numbers.

### Local overlap and recorded failures

Read C759a's hypotheses and Section1, C759d's hypotheses/conclusion and
complete cross-map setup, C759e's hypotheses/Sections1-2 and the relevant
domain/convention/tail audit passage in Section5. Reuse the supplied
step812 acceptance of the full modulus certificate; this was not another
certificate audit. C759e rules out modulus on the cap; C759d rules out
the fixed shift, and C998z remains supplied unrestricted-modulus evidence.
None is a primitive counterexample. No detailed C998z proof was needed.

The active-notebook primitive/parity search found no matching earlier
test. It did find [assessment557/comparison558](2026-11-12-two-moment-green-covariance-557.md)
and [assessment548/comparison549](2026-11-12-full-response-mechanism-discovery-548.md).
Their second-order exponential-moment and three-cell targets differ.
Reuse their warning about the induced metric; do not repeat their
absolute-density or truncated-response mechanisms. Other hits concerned
theta primitives, polynomial antiderivatives or unrelated Volterra
operators and were not mathematical inputs. No cross-notebook read occurred.

### Search record and decision

Web queries included `"Weil quadratic form" primitive odd even integration
parity`, `"Weil" "quadratic form" "Volterra"`, `antiderivative parity
eigenvalues Fourier multiplier Rayleigh quotient monotonic symbol`,
`"Weil quadratic" "antiderivative"`, `"Weil quadratic" "primitive" "odd"`,
`"Weil" "primitive" "Rayleigh"`, `"Weil" "parity" "integration" ground state
quadratic`, `"Weil" "primitive" "parity" inequality`, `"Weil" "antiderivative"
"Rayleigh"`, `"Weil" "primitive" "sin" quadratic form`, and `Sobolev interval
primitive mean zero H1 zero trace theorem derivative inverse`.

Bombieri's 2000 memoir was an additional historical lead: searched its
exact title and author; the primary bdim item
[RLIN_2000_9_11_3_183_0](https://www.bdim.eu/item?id=RLIN_2000_9_11_3_183_0)
timed out. A third-party text/search result was not treated as an inspected
theorem. Suzuki's directly available primitive and complete-form passages
are sufficient for the proposed finite test, so this optional access
failure is not an essential source blocker. Search hits claiming other
window bounds or generic nodelessness were not imported. No stronger
applicable theorem was established by the inspected material; no novelty
or nonexistence conclusion follows from the search.

Use [the two-sine test assessment813](2026-11-13-two-sine-primitive-test-813.md)
for the exact continuation. Its new ready scope needs the supervisor's
separate next-turn approval. This is ordinary source specialization:
the outstanding general signed comparison has no justified creative
certificate mechanism yet. The bounded test is useful because a single
eligible failure decides the proposed map assertion, while an entire
slice pass constrains what any later proof must explain. No sweep of
window sizes, cap changes or higher-mode enlargement is nominated.
Matching Mathlib coverage is not checked; elementary integration and
Fourier results would be support, not a matching theorem for the target.
