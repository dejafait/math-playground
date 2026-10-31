# Common-pole generic two-projection increment: source comparison

TARGET: Assess source coverage for the common-pole generic two-projection increment on L526's two packets, including separate trace finiteness and a possible leading contribution of -2p^(-1/2)log p.
CHECKED: 2026-10-30
DECISION: EXPLORE
SEARCH_EVIDENCE: Exact/terminology searches for Sonin generic pole trace increment, two-projection prime increment, and positive compression compensation returned paper 2's fixed-test asymptotics and uncorrected Sonin increment, not a corrected generic increment theorem. Scoped October 30 assessments/failure records supply no duplicate; see the completed comparison below. Search failure is not a novelty claim.
SOURCE_EVIDENCE: https://rstation.ai/problems/riemann_hypothesis/papers/2 , bramble_trace paper 2 v2 (16 October 2026), Section 1, Lemma 4.1 and proof (4.1)--(4.4), (5.2)--(5.3), (6.1)--(6.2), Theorem 6.2's generic-contribution statement, Theorem 7.1 and proof (7.1)--(7.4); https://www.ams.org/tran/1969-144-00/S0002-9947-1969-0251519-5/S0002-9947-1969-0251519-5.pdf , Halmos (1969), p.381 decomposition and Theorem 2, pp.384--385, with proof. Bell's Theorems 18/23 are reused from the completed L526 coverage assessment.
COMPARISON: Standard projection geometry and the source's localized Hardy trace lemma supply tools for a finite-trace application, to be checked for the exact reflected symbol. No inspected theorem gives the common-M moving-test generic increment or its sign at scale rL; neither the uncorrected fixed-test coefficient nor fixed-cutoff Hilbert--Schmidt perturbation supplies it.
GAP: The coverage comparison is complete for one bounded attempt: verify compression/intersection identification and both separate finite smoothed generic traces, then test Gamma_p against -2rL by a direct increment estimate. These local application and uniform signed-scale obligations remain unproved, not missing essential unread sources.
REASON: The changed observable survives the checked source obstructions and has an independently testable threshold. Ready tools justify proposing one mathematical attempt without rederiving their theorems; the completed literature turn establishes no estimate for Gamma_p.
LITERATURE_REASON: The target changed from the audited Sonin projection to the complementary generic compression; existing ready Sonin coverage does not cover this observable's trace identification or moving-family increment.
SCOPE: Completed literature-only comparison of the exact saved target. The separately nominated mathematical test is in 2026-10-30-common-pole-generic-increment-test.md and requires separate next-invocation approval; no lemma or mathematical script is written this turn.

Reuse L526's exact normalized bump, p tending through primes,
L=log p, r=p^(-1/2), M=L+2 and actual P_-/P_+. Both prime sets
retain the same pole phase. L526 is the only proposed local
mathematical input; its source-proof qualifications remain in force.
No other notebook input is nominated.

Let Pi denote the physical positive-half-line projection, J_(P,M)
the corrected unitary involution in L526's convention, and
S_(P,M) its physical Sonin projection. The expression to compare
with the source's generic positive contribution is

    C_(P,M)=Pi J_(P,M) Pi J_(P,M) Pi-S_(P,M).

The proposed observable is its smoothed trace

    Q_(P,M)(f_p)=Tr(T_(f_p) C_(P,M) T_(f_p)^*),
    Gamma_p=Q_(P_+,M)(f_p)-Q_(P_-,M)(f_p).

These are proposed expressions, not asserted finite traces.
Check the physical/Fourier convention, positivity/compression
identification and separate trace existence before subtraction.
The eventual bounded test would compare Gamma_p with -2rL:
does it have that leading negative contribution, or is there
a contrary asymptotic/domain obstruction? An O(1) estimate or
a fixed-test conclusion uniformized without proof is insufficient.
The source review may redirect this test if a theorem or obstruction
already settles it; do not reprove a covered conclusion.

This would test one possible contributor to a collective signed
comparison, rather than repeat the stopped Sonin-only argument.
Even a favorable estimate would leave the negative overlap and
remainder in (6.1), missing visible primes in both partial sets,
complete-Weil identification, conditional L515/L516/L521/L522
nullvector/trace/nonresonance premises, family control and Xi
transfer unresolved. No actual nullvector or positivity is assumed.
Full Mathlib coverage is unchecked. Primary upstream proofs remain
unaudited; the new assessment must distinguish their precise scopes
from any proposed application. No mathematical conclusion about
Gamma_p was derived in creating this continuation.

## Completed source comparison, 30 October 2026

The preceding paragraphs retain the original nomination and its open
obligations. The review did not calculate Gamma_p.

### Inspected inputs and exact limits

[bramble_trace paper 2 v2](https://rstation.ai/problems/riemann_hypothesis/papers/2)
uses physical convolution and the Fourier convention recorded above.
Lemma 4.1 assumes a smooth unimodular symbol with polynomial-growth
derivatives/phase derivative and bounded phase second derivative.
For a compact smooth test it gives a localized Hardy Hankel norm
estimate. Its proof (4.2)--(4.4) establishes finiteness and retains
off-diagonal corrections through trace-class factors. Section 6
identifies the positive physical compression; (6.2) and Theorem 6.2
give its generic leading coefficient only for fixed tests without
the pole correction. Theorem 7.1 matches the pole on its support
class with all visible prime powers included. Its asymptotic is
fixed-test; its perturbation assertion is fixed-cutoff. The proof
uses compact-frequency cancellation, domination, a second-derivative
bound, and symbol-tail estimates with cutoff-dependent constants.
Those scopes do not supply this signed moving-family increment.
No independent audit of that manuscript is asserted.

[Halmos, *Two subspaces*, Trans. AMS 144 (1969), 381--389](https://www.ams.org/tran/1969-144-00/S0002-9947-1969-0251519-5/S0002-9947-1969-0251519-5.pdf),
p.381, separates the four range/kernel intersections from the
generic part of two closed subspaces. Theorem 2, pp.384--385,
represents the generic projections by diag(I,0) and the matrix
with entries C^2, CS, CS, S^2, for positive contractions C,S
satisfying C^2+S^2=I and zero kernels. Read the theorem and its
polar-decomposition/idempotence proof. It supplies projection
geometry, not trace finiteness, a spectral gap, or a prime-increment
sign. One must remove the intersection subspaces before invoking
its generic-position hypothesis; no generic-position assumption
for the entire physical space is permitted.

Reuse [Bell, *Trace class operators and Hilbert--Schmidt operators*,
18 April 2016](https://jordanbell.info/LaTeX/mathematics/traceclass/),
Theorems 18 and 23, as inspected in
`2026-10-30-l526-critical-audit-coverage.md`: two Hilbert--Schmidt
factors give trace class; cyclicity requires a trace-class factor
and a bounded factor. Bell was not newly reread. These results
license operations only after the requisite factor estimates.

### Application obligations identified, not discharged

Retain Pi for the physical positive-half-line projection, reserving
separate notation for the source's frequency Hardy projections.
Use J from L526, not bare multiplication by the scattering symbol:
the Fourier representation includes reflection and u(-t).
Identify the Sonin space with the intersection for Pi and J Pi J.
Use Halmos's decomposition to identify the proposed compression
minus its intersection projection; do not assume positivity simply
because it is a difference of positive operators.

To use Lemma 4.1, transport Pi J Pi to the correct weighted Hardy
block, checking any reflected test and symbol, both Hardy sides,
and dt versus dt/(2pi). At each finite p the full corrected symbol
must meet the lemma's derivative hypotheses. Its constants may
depend on p at this finiteness stage. Then justify the positive
smoothed trace and the generic subtraction with trace ideals,
using L526's already finite Sonin trace. Do this separately for
P_- and P_+ before forming Gamma_p. No conclusion of these local
checks is claimed by this review; the cited theorems cover the
tools needed to attempt them.

An arithmetic-scale estimate requires a direct difference argument.
The individual-error estimate in Lemma 4.1 is not a correlated
increment estimate, and no cancellation of its errors is licensed.
Likewise the fixed-test coefficient and strong projection limits
cannot be used uniformly for f_p. Keeping the same M on both sides
isolates a prime change; replacing it by log of the new cutoff
would change the problem. The common phase's pole interpretation
does not identify either partial prime set with the full Weil form.

### Search, overlap and decision

Queries used: `"bramble_trace" "generic" trace`;
`"Sonin" "pole" "generic" trace`;
`"two projections" "Sonin" "trace" "generic"`;
`"common" "pole" "prime increment" Sonin`;
`"bramble_trace" "generic" "increment"`;
`"Sonin" "generic" "pole" "trace" increment`;
`"two-projection" "prime" "increment" trace`;
`"Sonin" "positive compression" "compensation"`;
and `Halmos Two subspaces 1969 pdf theorem 2 projections generic position`.
Only the primary passages above are theorem evidence. Discussion
post 3, paper 2 v1, a secondary cusp-invariance exposition and
broader Weil-propagation pages are unused leads, not imported
results. The Markdown-download endpoint failed in the web tool;
the primary HTML theorem/proof passages were accessible, so this
is not an essential source blocker.

Reused the arithmetic-slope comparison and L526 audit coverage;
read L526 and its confirmed Sonin-only stop. Narrow searches of
October 30 Weil failure records and literature assessments found
only the present nomination for the generic increment. The generic
pole-resolvent stop concerns missing arithmetic numerator data in
an unrelated propagation reduction, not this finite-prime trace.
The old stops remain in force in their stated scopes. No theorem
in the checked sources settles the proposed Gamma_p test; no claim
of originality or general impossibility follows.

Decision: the source gate can support one bounded direct increment
attempt, with the domain checks above first. A proven coefficient
at or below -2 in Gamma_p/(rL) would nominate a further collective
comparison; a contrary asymptotic or a concrete domain obstruction
would stop this particular local-absorption test. Mere O(1) control
would leave it unresolved. Neither outcome supplies actual-Xi
positivity. Preserve unresolved overlap/remainder, missing primes,
nullvector/trace/nonresonance and family/Xi-transfer obligations.
Full Mathlib coverage is unchecked; no cross-notebook theorem used.
