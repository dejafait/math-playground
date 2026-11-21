# Weighted Fourier-deficit complementary floor — audit source coverage

TARGET: Audit C759c's full weighted Fourier-deficit trace and shifted complementary floor on C759a's W, checking the support cutoff, positive compression, entire sine tail, outward rectangle certificate and closed-form implication.
CHECKED: 2026-11-13
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step803 reused assessment800's exact searches and primary-source comparison, read all of C759c and the relevant C759a/L744 proof ranges, assessment793's separate approval, C759b's statement and histories801/802; no fresh external search or numerical replay.
SOURCE_EVIDENCE: Reuse step801's inspected Hamhalter Definitions5.1/5.5/5.6 and Proposition5.2, Bell Section8/Theorems18/19/26 and proofs, and assessment793's realization/scalar/enclosure coverage; C759a Sections1-3/6 and L744 scalar-input paragraph/Section2 were read for the exact audit mapping below.
COMPARISON: The new canonical proof uses the previously assessed positive diagonal-trace, sine-tail and scalar-enclosure methods at their covered hypotheses; no additional kernel theorem, external numerical positivity claim or new domain theorem is needed for this audit.
GAP: No essential source gap was identified for the exact saved audit; its support/compression construction, all rectangle arithmetic and whole-domain lower implication remain mathematically unaudited, and coupling/Schur/parity/Xi conclusions remain outside scope.
REASON: Separate step803 completes the source-to-obligation comparison for the new audit scope; approve one RESEARCH/REPRODUCTION conceptual audit, without validating C759c or deriving a new result in this literature turn.
SCOPE: Exact C759c, level4, interval(-1,1), sine120 complement, original C and P_120, cutoff350, all349 unit rectangles and every omitted sine mode; no optimization, altered prime cost, finite Schur computation or global sign assertion.

The original step802 nomination is preserved below; the separate
step803 approval at the end supersedes its pending source gate. This
record approves coverage for an audit, not the mathematical conclusion.
Step802's completed work and its pending independent-audit qualification
are retained.

The canonical argument is C759c, with full certificate and reproducible
script at `scripts/spectral-triples/weighted-fourier-deficit-802.json`
and `.py`. The actual rectangle majorant B is about0.52800039427;
the trace itself is only enclosed by0<=T_4<=B. The exact required
threshold is about0.81391352324; the claimed shifted floor exceeds
0.2859. Step802's ambient-precision7 replay is byte-identical, but is
not an independent mathematical audit or a formal interpreter proof.

Pay particular attention to: evenness and Fourier dt/(2*pi)
normalization; h(350)>4 and350<121*pi; boundedness of the compression
before trace-class use; finiteness before norm domination; the infinite
sine sum and its denominator range; upper-rectangle directions near
the positive-part crossing; the complete origin bound; all349 terms
and all five prime powers; outward rounding and branch/domain checks;
and the sign of the projected odd pole. Check the lower inequality
on the whole logarithmic closed domain, not just sine polynomials.

Continuation test: retain the complementary floor if these exact
claims survive independent audit. Otherwise repair or qualify the
first load-bearing failure and preserve the original certificate.
Do not treat a failure as evidence against the actual parity gap.
The historical C759a/C759b/L743 stops remain scoped evidence.

The original source comparison explains why no new general theorem
or external positivity computation suffices for this quantitative
specialization. Mathlib matching coverage remains unchecked. The
independent coupling/Schur, parity, even simplicity/sign and actual-Xi
realization gaps remain. No justified central creative mechanism is
ready: the full-energy-to-Xi bridge still lacks a concrete bounded
test, and this standard trace specialization must not be relabeled
creative to satisfy scheduling preferences.

## Separate source comparison — step803, 13 November 2026

LITERATURE_REASON: The invocation-start audit target was REVIEW_REQUIRED; this separate turn compares its newly written canonical argument with existing inspected coverage, without repeating step801's external search.

The main gap remains actual-Xi all-degree mixed positivity
L030-L032/C032a. The intermediate target is the exact audit in TARGET:
if its conclusion survives, the local shifted complementary floor can
serve as a prerequisite for a later conditional form-dual coupling/Schur
comparison. Neither that comparison nor the parity/Xi bridges is proved
or approved here. Retain the floor only after the audit checks the full
argument and complete certificate; the first load-bearing failure instead
requires repair or qualification. A preview or generator replay alone
is insufficient.

### Reused primary coverage and applicability obligations

Assessment800 records primary hypotheses and essential proof cases
actually read in step801, not search snippets: Jan Hamhalter,
*Classes of Operators on Hilbert Spaces*, 10 April 2008, printed pp18-19,
Definitions5.1/5.5/5.6 and Proposition5.2
([author PDF](https://math.fel.cvut.cz/en/people/hamhalte/malta07.pdf));
Jordan Bell, *Trace class operators and Hilbert-Schmidt operators*,
18 April 2016, Section8, Theorems18/19/26 and their proofs
([author notes](https://jordanbell.info/LaTeX/mathematics/traceclass/)).
Relevant hypotheses are a bounded positive operator on a complex Hilbert
space and a complete orthonormal basis; finite positive diagonal sum is
needed before positive trace-class norm domination. C759c Section1
constructs a complex compression and Section2 claims a finite diagonal
bound. The audit must check these hypotheses in that order, including
the Fourier measure, isometry and actual basis. Cite the general theorem
rather than reprove it; those concrete checks are the necessary local
specialization. No rectangular kernel extension of Hamhalter
Proposition5.10 is needed. The unread Reed--Simon scan remains
nonessential; Bell's cited Conway book was not independently read.

C759c's scalar inputs are exactly C759a(5) and L744(8), not a new
digamma estimate. L744 records the right-half-plane, principal-logarithm
specialization of [DLMF5.11.2](https://dlmf.nist.gov/5.11.E2) and the
[complex remainder in 5.11(ii)](https://dlmf.nist.gov/5.11#ii).
Its |t|>=1 bound and C759a's global lower bound cover the claimed two
frequency regimes. Cutoff350 and its comparison with121*pi still need
local checking; no source supplies their numerical verification.
C759a Section2 and its separate audit provide the integer-sine transform
and complete inverse-square tail for |t|<121*pi. Check that every use
stays in that range, including the support endpoint, and that Tonelli
and evenness give the stated normalization. The source asymptotic is
not licensed at the origin or an unhandled removable denominator.

C759a Sections1/3/6, read narrowly this turn, fix the supported logarithmic
domain and complete bounded prime/pole costs. Its assessed realization
input is Suzuki, *Weil's quadratic form via the screw function*,
[arXiv:2606.09096v2](https://arxiv.org/html/2606.09096v2),
Theorem1.1, Corollary1.2 and Sections3.2,4.1-4.2,4.5; the local
domain/core specialization was independently audited in step795.
Reuse that coverage and canonical result, without importing Suzuki's
small-window positivity at another parameter. Still check the passage
from the bounded deficit inequality to the whole closed logarithmic
domain, retaining all five prime-power weights and the negative odd
pole. A smooth-only calculation or finite sine matrix is insufficient.
The conditional Schur criterion is downstream context, not a required
premise of C759c.

Assessment793 and C759a Section6 cover the enclosure convention using
the [Python Decimal reference](https://docs.python.org/3/library/decimal.html),
exact integer/decimal inputs, directed basic arithmetic, correctly rounded
ln/exp/sqrt expanded to adjacent endpoints, and rational alternating
Machin sums. C759c introduces a different finite sum, not a new arithmetic
model. Its script and every relevant certificate entry still require
inspection: origin, all349 rectangles, positive-part branches, denominator
positivity, prime/pole entries, constants and final comparisons. Old
certificate success does not verify new code or its output. Python/Decimal
correctness remains a software trust assumption. No mathematical script
was read, run or modified this turn.

### Duplicate/failure comparison and decision

Assessment800's inspected Li paper45/v2 Theorem1.1 and Sections2-5 give
unshifted localized positivity with different retained modes and costs,
not the exact shifted coercive estimate or this audit. Its supplement
was not replayed; no new source result is imported now. C759a's failed
two-region estimate and C759b's independently audited arithmetic3/2
obstruction address different bounds. C759b's statement explicitly
leaves full Weil energy open. Neither historical stop forbids this
full-symbol audit; neither is evidence for its success. The direct-payment
and generic joint-energy failures remain as compared in assessment800;
their proofs were not reread. No exact duplicate beyond the saved
comparison is claimed, and failed searches establish no novelty.

SPECIALIZE is ready for the unchanged TARGET, with classification
REPRODUCTION for the ensuing conceptual audit. Next work defaults to
mathematics without another unchanged literature turn. This comparison
supplies no new lemma, certified number or result beyond the inspected
sources and performs no mathematical audit. Full matching Mathlib
coverage remains unchecked. Essential local inputs are C759c, C759a and
L744; C759b/L743 are scoped stop evidence, not positive premises.
Independent form-dual coupling, finite Schur sign, actual parity gap,
even simplicity/sign and Xi realization with multiplicities remain open.
No justified creative central test is ready while the full-energy-to-Xi
bridge lacks a concrete mechanism; the essential conceptual audit must
not be relabeled creative to meet scheduling.
