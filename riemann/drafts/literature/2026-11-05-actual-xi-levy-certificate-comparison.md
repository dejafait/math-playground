# Actual-Xi Mellin/Levy claims: completed source comparison

TARGET: Compare the actual-Xi Mellin/Levy certificate claimed in rStation paper23 with the precise KPS class hypotheses and paper20's Fabry obstruction, and select one independently testable remaining analytic claim or park the construction.
CHECKED: 2026-11-05
DECISION: EXPLORE
SEARCH_EVIDENCE: Step508 read both primary manuscripts' mathematical bodies, checked KPS class definitions and its sufficient theorem, and inspected Eremenko Theorem A. Exact supplement searches and access failures are recorded below; no certificate replay or novelty inference.
SOURCE_EVIDENCE: bramble_trace, rStation paper23 v1 (18 October 2026), Sections1–10, Theorem1/Lemmas2–4; paper20 v2 (18 October 2026), Theorems1–2 and Sections2–3; KPS AIF74(2024), (4.14)/Theorem4.4 p396 and (5.4) p404/Proposition5.2 p405; Eremenko arXiv:0710.5894v2, Theorem A pp1–3. Direct links and limitations below; supplements unread.
COMPARISON: The specified actual Mellin factor replaces a previously missing candidate, but paper23's membership is conditional on analytic/evaluator enclosures and yields ordinary B_J only. Paper20 claims an obstruction to the complete-Bernstein sufficient route, not ordinary B_J. Neither supplies all-degree signs.
GAP: Supplement derivations, enclosure provenance and finite certificates are uninspected; no unconditional membership or actual-factor obstruction is imported. The bridge from ordinary B_J to actual real zeros/mixed positivity remains absent even if membership holds.
REASON: Informative source-scope NEGATIVE: park automatic sufficient-class transfer, retain the conditional actual construction, and select one independently testable displayed saddle-domain premise for a separate audit gate.
LITERATURE_REASON: Essential new actual-construction and obstruction sources were discovered in step507; ready generic representation coverage does not assess their analytic claims.
SCOPE: Completed literature-only comparison; no new result, lemma, mathematical script, numerical inversion or interpolation derivation. The original nomination below is retained; the new audit assessment is separate.

Main gap: actual-Xi all-degree mixed positivity. Intermediate target:
determine whether the claimed actual Mellin construction supplies a
root-independent analytic premise useful toward a sufficient zero
theorem, and isolate exactly one bounded claim if it does. Distinguish
class membership, a sign claim for a Levy density, and the stronger
hypotheses needed for real zeros. A claimed complete solution stays
UNVERIFIED CANDIDATE/IN_PROGRESS pending later critical review.

Retrieve exact primary statements, definitions and load-bearing proof
cases before larger passages or certificates. Identify the authors,
versions and dates. Do not import an OCR-ambiguous ratio or equate
different normalizations. Check full actual-kernel coverage, contour
inversion/convergence, any global sign assertion, and the exact scope
of the obstruction; general Bernstein, complete Bernstein and separated
Pick assumptions must not be conflated. An obstruction to one sufficient
subclass does not exclude a general Levy representation or RH.

Continuation test: source-covered explicit actual data plus a bounded
independent analytic claim with a stated threshold and plausible sign
use. Nominate a creative central attempt only if there is a real new
mechanism with that test; routine specialization remains reproduction.
If no sufficient bridge or useful independent claim survives, record
the exact mismatch and park this construction. Do not extend common
Favard orthogonality, redo generic root-disk tools, or repeatedly seek
the same inaccessible source. No quota-driven theorem is required.

Essential local inputs: L019/L021's actual theta kernel and moments,
L795's polynomial convention, and the completed step507 assessment.
L795/L796 stops remain context, not premises for a Levy obstruction.
L778/L791 analytic/software contracts remain inherited if certified
coefficient data are eventually used; this review does not require
their numerical replay. Actual normalization, interpolation, global
analytic/sign conditions and mixed-positivity transfer are unresolved.
No cross-notebook input. Mathlib matching coverage is unchecked.

## Completed source comparison — step508, 5 November 2026

Main gap: actual-Xi all-degree mixed positivity. Intermediate target:
identify an actual Mellin construction and distinguish its analytic
premises from a sufficient zero theorem. Downstream use would be a
root-independent analytic representation; a further sign theorem would
still be required. Continue only with an explicit independently testable
claim; park automatic transfer if only ordinary membership survives.
This review meets the latter stop condition but locates an analytic
premise that can be tested independently of inaccessible certificates.

### Exact construction and normalization

bramble_trace, *A continuum certificate for the decreasing Lévy factor
associated with Riemann xi*, [paper23 v1](https://rstation.ai/problems/riemann_hypothesis/papers/23),
18 October 2026, Sections1–10, Theorem1 and Lemmas2–4. The accessible
primary manuscript, rather than its abstract or automatic reviewer
report, supplies the mathematical statements used here. The author
licenses original prose/data CC BY4.0. No human identity is inferred
from the handle.

Its P is K/2 in L019, by the displayed kernel formulas, with the same
real variable and cosine argument. Its M(s) is the integral of
x^(2s)P(x); thus M(n)=M_(2n)/2 in L021 notation. This is only a
normalization comparison of existing definitions. The normalized
transform is the same Xi(t)/Xi(0); the factor of two cancels in the
source's ratio

    phi(s)=(4s-2)M(s-1)/M(s),  Psi(s)=s phi(s).

For nonintegral s this is initially a specified Mellin quotient,
not an arbitrary interpolation of integer samples. Section2 (9)
states its coefficient telescoping identity; Section4 discusses the
affine ambiguity after inversion. No recurrence-uniqueness theorem
or assumed exclusion of periodic interpolation factors is used here.

Theorem1 assumes Lemmas2–4's uniform analytic enclosures and validity
of Section5's moment evaluator enclosures. It then claims k(r)>0 and
k'(r)<0 for every r>0 and ordinary B_J membership, with positive
constant and zero linear term. This is explicitly a conditional source
result, not a proved input to the notebook. No complete solution or
UNVERIFIED CANDIDATE for RH is asserted by this review.

Read the source's load-bearing cases: Section3's saddle-image and
translated-disc arguments; Section4's inverse construction, endpoint
integrability and affine-term removal; Section5's canceled Mellin
poles and winding/evaluator provisions; Sections7–8's contour ordering,
finite joins, infinite tails and large-parameter bounds. The cited
numbered supplement derivations were NOT read. In particular, the
displayed proof outlines do not verify the uniform estimates.

The claimed global cover consists of the analytic small interval,
the middle finite cover, and the analytic large interval. A finite
arithmetic reconstruction would still leave the analytic/evaluator
provenance obligations. The source itself distinguishes these tasks.
We did not retrieve input balls, inspect complete certificate evidence,
run verify.py, or install dependencies. Its reviewer report is a report
by that source, not our verification.

### Published sufficient hypotheses and the obstruction's scope

T. Konstantopoulos, P. Patie and R. Sarkar, *A new class of solutions
to the van Dantzig problem, the Lee–Yang property, and the Riemann
hypothesis*, AIF74 (2024),377–421,
[(4.14), Theorem4.4, p396; (5.4), p404; Proposition5.2, p405](https://www.numdam.org/item/10.5802/aif.3600.pdf).
Reused step507's inspected Theorems4.1/4.4 and proof scope; checked
the precise density definition and root-zero correspondence directly.
B_J requires a nonnegative nonincreasing density with integral
min(1,r)k(r) finite, allowing killing and drift. B_P1 additionally
requires a Bernstein-Pick function with ordered zeros z_k and poles
rho_k=z_k-1>z_(k+1). Theorem4.4 gives real zeros for that subclass
and explicitly denies inclusion of all D_P in D_L. Ordinary B_J is
not that sufficient hypothesis. Paper23 does not claim otherwise.

bramble_trace, *A Fabry obstruction to complete Bernstein constructions
of the Riemann xi function*, [paper20 v2](https://rstation.ai/problems/riemann_hypothesis/papers/20),
18 October 2026, Theorems1–2, Sections2–3: claims no root-zero
complete-Bernstein representation. Its general theorem assumes an
even analytic positive probability density, every exponential moment,
finite positive Taylor radius R, continuation near +R, and a forced
factor regularly varying with index one, unbounded but sublinear.
Read the entire-quotient identification, integer zero-string induction,
coefficient-sign deficit including zero coefficients, theta cusp and
inverse-square moment-tail cases. These supply the claimed exclusion
of the stronger sufficient route; they do not exclude ordinary B_J,
locate a zeta zero, or transfer to a different logarithmic exponent.
This scope assessment is not a full independent audit or theorem import.

The essential Fabry input was inspected independently: A. Eremenko,
*A version of Fabry's theorem for power series with regularly varying
coefficients*, Proc. AMS136 (2008),4389–4394,
[arXiv:0710.5894v2, Theorem A and density discussion, pp1–3](https://arxiv.org/pdf/0710.5894).
For a real series of radius one, the allowed sign-change set's maximum
density controls the required singular arc; density zero gives the
positive endpoint. The additional coefficient-magnitude regularity
belongs to Theorem1, not Theorem A. PDF metadata has a later internal
date; this citation binds to the accessed v2 text. No new Fabry
specialization is derived. Other full-proof inputs of paper20 remain
unaudited, so its theorem is not added to canonical lemmas.

### Access, duplicate check, and decision

Source extraction read both HTML mathematical bodies through their
references. Their Markdown download links returned unsupported
text/markdown errors in the web reader. A direct unauthenticated
Python URL retrieval failed DNS resolution. The rendered paper23
mentions its supplement but exposes no supplement URL among its
numbered links. Exact searches were `"rstation" "riemann_hypothesis_23"
supplement`, `"A continuum certificate" "verify.py"`, and
`"bramble_trace" "derivation87"`. They did not retrieve the packet.
No guessed private endpoint, credential or infrastructure change was
used. This is limited access evidence, not proof that no public packet
exists. Further dependent certificate work is parked until actual
source access changes; repeating access attempts is not the next task.

The narrow November5 assessment/attempt search found step507's generic
KPS comparison, not a prior audit of this actual saddle claim. L019,
L021 and L795 definitions and the step507 stop were read; L796 remains
stop context only. No other notebook was read. These checks do not
establish novelty. Full matching Mathlib coverage remains unchecked.

New local evidence: the actual candidate is specified, but its claims
are conditional and its ordinary class supplies no real-zero bridge.
The apparent conflict with the stronger-class obstruction is resolved
at the level of stated hypotheses. This is an informative source-scope
NEGATIVE, with no theorem, new bound or progress beyond the sources.
Preserve L795/L796 and all earlier stops. Park automatic membership-to-
sign transfer and dependent certificate replay. Do not globally ban
the Mellin construction.

Select one independent source-claim audit: the saddle image and strip
clearance in paper23 Lemma2, on its stated high-frequency domain,
using its explicitly displayed defining equation. The claim can be
tested without accepting the missing input balls or inverse estimates.
The new assessment is `2026-11-05-actual-mellin-saddle-domain-audit.md`;
it requires separate next-turn approval. This is reproduction/audit of
an existing claim, not a creative mechanism. No justified creative
target yet has both actual data and a sufficient sign bridge; that
blocker is retained rather than filled with an artificial nomination.
