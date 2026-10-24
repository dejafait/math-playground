# Coverage: conditional subendpoint sign assembly

TARGET: Combine audited L454 and L455 to prove uniform eventual positivity of D_{m/2}(Ξ;a) on 31/32≤m/r≤63/64, retaining the pinned external premise and exact normalization.
CHECKED: 2026-10-23
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the completed exact-band arithmetic/sector searches and audit assessments; compared L454/L455 statements, normalizations and concluding audit passages, the October overlap review and external-input register, and the recorded L323/L327 failures. No new external search, exhaustive duplicate screen or novelty claim.
SOURCE_EVIDENCE: Reused inspected Csordas arXiv:1309.0055v2 https://arxiv.org/html/1309.0055v2, Theorem 3.5, Lemma 3.6 and Theorem 3.7 (3.10)–(3.14); DLMF https://dlmf.nist.gov/7.2#iii (7.2.6–7.2.9), https://dlmf.nist.gov/2.3#iv (2.3.21–2.3.23), https://dlmf.nist.gov/1.14.E20, https://dlmf.nist.gov/25.2 and https://dlmf.nist.gov/5.11; Titchmarsh–Heath-Brown (1986), Theorem 14.2 and Section 14.3, pp. 336–339, through audited L452 and the saved Littlewood comparison; pinned September 30 Theorem 1.1 through the register, without new external-proof verification.
COMPARISON: Audited L454 and L455 state the identical real-r/even-m band, height relation and full finite sum. L454 provides the uniform relative error and non-Euler square lower bound; L455 provides the complete additive error and exact positive multiplier. Existing sources cover their mechanisms, not a separately stated matching sign theorem; only their downstream quantitative combination remains to be justified.
GAP: Establish the combined positive margin with one uniform onset and the exact P_{r,m}; this literature turn checks coverage and statement applicability only, not that inequality or a Laguerre sign.
REASON: The separate comparison now covers the saved application using adequate existing source evidence. Approve one REPRODUCTION attempt without redoing Mellin or sector proofs, importing Euler bounds below one, or auditing the external manuscript.
SCOPE: The exact conditional L454/L455 application on the stated coupled band only; no arbitrary-height extension, smaller indices, new zero-free region, external-proof certification or RH conclusion.
LITERATURE_REASON: The newly selected sign application was outside the preceding audit-only scopes; its separate exact-scope approval was explicitly required. No additional source browsing is needed.

## Exact scope and continuation obligations

Retain r positive real tending to infinity, m a positive even integer,
31/32≤m/r≤63/64, h=9/2+m/(2r),
a=sqrt(4π²exp(4r)−h²)>0, and the full product cutoff in
S_{r,m}. L455 supplies an additive error bounded by
C(1+r)²exp(−r/200) and the exact positive P_{r,m}. L454
states S/B=1+O(r^(−1/6)) and B≥exp(−C r^(1/3)),
where B=|ζ((1+m/r)/2+ia)|². These are restatements of
the canonical conclusions; no combined inequality is proved here.

The eventual application must check whether its complete normalized
error is smaller than a positive margin, uniformly for every admissible
r,m with one onset. Do not substitute an absolutely convergent Euler
lower bound on this line below one. Do not drop the factorial, double
the reflection twice, or claim a sign at an arbitrary unpaired height.
Continue if exact hypotheses and full errors support the desired sign;
otherwise preserve the failed comparison before changing the target.

Essential inputs are audited L454 and L455. The former retains
L303/L330/L452 and OpenAI's September 30, 2026 Theorem 1.1 at commit
`1581d4cbdd69a0faf34b2089614fe2a814316a6a`, including the allowed
pole and unaudited external manuscript/import closure. The latter uses
L269, C294b, L324 and L325 and needs no external zero-free premise.
This paragraph identifies continuation inputs in prose, not a second
dependency graph. No external source verification is added by this record.

The main gap remains global mixed positivity and the initial low-index
segment. The proposed sign band would be an intermediate partial result;
smaller indices, bounded exterior heights and the selected-law/regulator
gaps remain independent. Preserve L323's larger-strip and L327's PSD
stops. Full matching Mathlib coverage is not checked. This assessment
now approves source coverage for the stated application, not its correctness.

## Completed separate source comparison

This invocation reused the exact-band
[arithmetic assessment](2026-10-23-subendpoint-relative-mellin-coverage.md)
and [sector assessment](2026-10-23-subendpoint-theta-sector-reduction-coverage.md),
and their separate critical-audit coverage records. The existing queries,
source versions, theorem hypotheses, relevant proof cases and distinctions
between inspected and unread leads remain those recorded there. No primary
page was freshly fetched. Olver/Lyness and the general parameter-dependent
stationary-phase lead remain unread and are not essential inputs.

The directly compared canonical ranges are L454 Hypotheses, Conclusion,
Section 1 and its final audit/onset discussion, and L455 Hypotheses,
Conclusion, Section 1 and its final audit/normalization discussion.
These supply matching definitions of h,a and S, including the positive-part
cutoff. L454's statement includes fixed constants independent of r,m for
both its relative error and its lower bound for B. L455's statement includes
fixed constants for the entire additive error, real remainder and positive
P. Thus no parameter extension or additional source theorem is needed for
the proposed assembly. This is a statement-level applicability finding;
the independent correctness audits are reused, not repeated here.

The necessary specialization is to take both existing results at exactly
the same admissible pair, keep their potentially different constants and
onsets, and compare the full additive error with the same non-Euler B.
The future proof must explicitly choose one eventual onset for the relative
error and the additive-error/B comparison, then retain P without changing
the factorial or reflection factor. The continuation test is a strictly
positive uniform signed margin after both errors; abandon or repair this
implementation if that complete comparison fails. No such comparison is
proved in this review. A new lemma, if the attempt succeeds, must contain
the full elementary assembly, external hypothesis and Mathlib qualification;
there is no reason to reprove either source mechanism.

Csordas's admissible-kernel statements do not assert positive definiteness
of every associated kernel for actual theta; Theorem 3.7 retains that
premise. DLMF stationary-phase hypotheses and Fresnel limits do not alone
give the moving-domain uniform estimates; L455 is the already audited local
input providing them. Likewise Titchmarsh's printed RH-conditional theorem
is not imported with RH deleted: the input is L452's separately justified
fixed-half-plane specialization under the precise pinned external premise.
The register's allowed pole, strict boundary and unaudited manuscript/import
closure stay load-bearing. No reciprocal Euler expansion is used below one.

The scoped duplicate comparison distinguishes C452a's m=r sequence,
L453's bounded-offset rounded index and L326's m/r=3/4 sequence from the
present fixed proportional band. L454 is arithmetic-only and L455 is an
unsigned reduction, so neither already states the requested combined sign.
The earlier searches did not identify an external theorem giving precisely
this application; this is not evidence of originality. Classification for
the approved research is REPRODUCTION, a local known-method application.

L323's r/4 summed-modulus obstruction and L327's phase-uniform PSD
replacement obstruction were checked through their recorded failures and
the existing assessments. This target changes neither cutoff nor phase
vector: it uses L455's already established smaller-strip reduction and
L454's actual coupled-height comparison. Those stops are preserved.
L304/L330 older freezing failures and L335 fixed-r/unit-phase negatives
also retain the scopes documented in the arithmetic assessment.

The outcome is EXPLORATION: a new exact-scope approval using existing
evidence, with no new mathematical input or progress beyond the checked
sources. No lemma, mathematical script, DAG edge or assembled argument is
changed. Mathematical exploration usage remains 0 of 3; this literature
step does not spend or reset it. The next turn defaults to the approved
mathematical assembly after supervisor approval of this changed assessment.
