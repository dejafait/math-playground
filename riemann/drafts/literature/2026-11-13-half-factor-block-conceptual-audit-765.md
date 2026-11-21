# Formal theta half-factor block: proposed conceptual audit

TARGET: Critically audit C795a's eventual 3-by-3 half-factor Hermite positivity, including the undifferentiated source remainder, exact fourth-moment cancellation and all principal minors.
CHECKED: 2026-11-13
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step766 reused the completed step764 exact-statement, stronger-result and obstruction searches; narrowly checked C795a, L795, L019/L021 normalization, L825/L827 contrasts and the step765 detector stop. No matching ready audit was found in those records; no novelty claim.
SOURCE_EVIDENCE: Step766 rechecked O’Sullivan2007.13582v2 (1.2), Theorem1.4 and (7.3)-(7.14); MSS1504.00350v2 Definition1.1/(1)-(2), printed p2; Arizmendi-Perales1611.06598v2 Propositions3.4/3.6 pp7-8 and Lemma4.1 p9; Nathanson1911.01745v2 Theorem1 and its real/nonreal proof cases pp2-3; earlier full Laplace coverage reused.
COMPARISON: Established algebraic inversion, integer coefficient asymptotics and the full Hermite root criterion cover the inputs. They do not certify C795a’s explicit-approximant derivative bounds, fourth-moment cancellation or proper-block signs; these exact application checks justify a conceptual audit, without reproving the imported general theorems.
GAP: Source coverage for this exact audit is now ready; the mathematical audit itself remains unpaid. C795a’s eventual-sign claim remains pending independent verification, with no effective onset, full-factor roots or shifted/mixed/global assembly.
REASON: Approve only the saved bounded conceptual audit after separate source comparison; no audit conclusion or new mathematics is established in this literature turn.
SCOPE: Only C795a for integers d>=4 tending to infinity; fixed offsets 0,...,4 and K=4, real monic algebraic half-factors, source remainder O(log^4(d)/d^4), exact power sums through four. No new mechanism, degree sweep, larger block or increased truncation order.

Essential inputs are L019/L021/L795 and the precise sources cited in
[the previously approved assessment](2026-11-13-theta-half-factor-asymptotic-block-764.md).
Their coverage remains reusable. The new audit target is written only
after completion of step765, so its scope is REVIEW_REQUIRED until a
separate approval turn. No fresh mathematical derivation is authorized
by this nomination.

The central gap is L030-L032/C032a actual-Xi all-degree mixed positivity.
This audit determines whether one proposed necessary-condition detector
can safely be retired. Check actual gamma normalization, the triangular
self-convolution equations, the passage from source rational coefficients
to a smooth explicit approximant, and Taylor expansion at fixed integer
offsets without differentiating an unknown remainder. Check the complete
fourth-moment cancellation before taking the limit and all seven principal
minors. The canonical proof and auxiliary exact certificate specify these
obligations; the script does not certify analytic hypotheses.

Continue only if each analytic/error step is justified and the normalized
minor limits remain strictly positive. A gap must be repaired in place
or reported as unresolved without retaining the eventual-sign claim.
No independent creative central mechanism is proposed here: that missing
mechanism cannot be supplied by relabeling this established-method audit.
Full-factor signs and all shifted/mixed transfer remain unresolved, even
if the audit passes. Full matching Mathlib coverage is unchecked.

## Completed source review — 13 November 2026, step766

The earlier nomination above is preserved as history. Its REVIEW_REQUIRED
status is superseded by SPECIALIZE for the unchanged TARGET and SCOPE.
This approves a later audit, not the correctness of C795a. No lemma or
mathematical script was changed or executed in this source-only step.
LITERATURE_REASON: The newly nominated conceptual audit required its own
source-scope approval; the underlying half-factor assessment is reused.

[O’Sullivan v2](https://arxiv.org/html/2007.13582v2), 9 December 2020,
(1.2) and Theorem1.4, match the gamma convention recorded in C795a.
The fixed-K integer expansion and rational coefficient formulas are
available; (7.3)-(7.8) absorb the higher-theta tail, and (7.9)-(7.14)
combine that result with Stirling. The earlier full Laplace assessment
is reused. The theorem gives no differentiated remainder estimate.
The later audit must check C795a’s distinction between that remainder
and its smooth explicit approximant, including eventual positivity of
B, rational coefficient derivative bounds, fixed offsets and error
amplification. These are obligations, not conclusions of this review.
The normalization check must retain L019/L021 and L795 exactly; a
constant from another convention cannot be silently substituted.

[Arizmendi–Perales v2](https://arxiv.org/pdf/1611.06598v2), 7 March 2017,
Propositions3.4/3.6, printed pp7-8, supply coefficient/cumulant inversion
and additivity for monic degree-d polynomials; the latter proof is
algebraic, without hyperbolicity. Lemma4.1, p9, is the Newton conversion.
Reused the prior complete proof comparison and rechecked the additivity
proof. Its normalized moments must be distinguished from C795a’s
unnormalized root sums. [MSS v2](https://arxiv.org/pdf/1504.00350v2),
Definition1.1/(1)-(2), printed p2, defines the same-degree operation for
complex coefficients. C795a’s triangular equations and low-order Newton
identities need verification as the necessary specialization; no general
cumulant theorem needs reproof. Forward root preservation cannot supply
inverse-factor roots.

[Nathanson v2](https://arxiv.org/pdf/1911.01745v2), 24 November 2019,
Theorem1, pp2-3, assumes a nonconstant real polynomial and tests its full
Hermite matrix, with multiplicities. Rechecked the real-root square
argument and nonreal conjugate-pair interpolation case, using Lemmas1-2.
The later audit concerns a proper block and must not infer full roots
from its positivity or replace algebraic squares by modulus squares.

Duplicate and failure coverage is reused from the completed step764
comparison, with a narrow check of the step765 stop and L825/L827
contrasts. L825 concerns a common symbol; L827 different reciprocal
moments. Neither settles this audit. The recorded fixed-block stop is
conditional on audit validity, not a ban on all future mechanisms.
No external search is repeated merely to renew that coverage.

For continuation, check C795a (7)-(18), all seven minors, and the
analytic-to-integer error passage in one conceptual audit. Consult the
existing exact certificate only as auxiliary algebra evidence, inspecting
all load-bearing values before relying on it. Continue the detector’s
retirement only if all obligations pass; otherwise report or repair the
precise gap without retaining an unsupported sign claim. No larger
block, increased K, degree sweep or new mechanism is approved. Essential
inputs remain C795a and L019/L021/L795 with the named sources; finite
exceptions, full-factor signs and global assembly remain unresolved.
Full matching Mathlib coverage remains unchecked. No independently
justified creative central target emerged; the essential audit comes first.
