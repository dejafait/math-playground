# Truncated arctangent-model Stieltjes error — completed comparison

TARGET: Prove the pointwise bound integral_(sqrt(n),infinity) K_n(t) d(N(t)-M(t))=O(sqrt(n) log n), where M(t)=t*log(t/(2*pi*e))/(2*pi), with a weak finite cutoff and multiplicities.
CHECKED: 2026-11-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused reviews214/215; screened local Li/tail assessments, attempts and November10 histories for Stieltjes/counting-error duplicates; searched exact Li/Keiper truncated-zero and arctangent terminology plus finite-variation integration by parts. No inspected source supplies the exact truncated pointwise bound.
SOURCE_EVIDENCE: Reused review214's primary Hasanalizade-Shen-Wong2107.06506v1 Cor1.2/(1.5), Section2 and corollary proof, and Arias de Reyna31Jan2011 Thm1/full proof pp.4-5; rechecked counting definition/Cor1.2 in primary PDF pp.1-3. Newly inspected Folland Real Analysis 2nd ed.(1999), NBV definition p.103 and Thm3.36/full proof p.107, with finite-interval FTC Thm3.35 p.106.
COMPARISON: Unconditional multiplicity counting with logarithmic error and signed finite-interval integration by parts are covered; their uniform kernel estimate and improper truncated specialization are not stated by these sources. The full-model normalized l2 conclusion supplies no requested pointwise rate.
GAP: Establish the n-uniform kernel/derivative estimates, finite-interval specialization with the right-continuous endpoint value, vanishing upper boundary and convergent improper tail; handle sqrt(2)<=sqrt(n)<e separately. No bound is derived in this review.
REASON: Essential source scope is now adequate for a standard calculation using elementary kernel estimates; cite the counting and integration theorems instead of reproving them. The full residual, smooth-model constant matching and finite-head signs remain separate gaps.
SCOPE: Actual zeta; integer n>=2; N(t)=#{rho:0<Im(rho)<=t} with orders; K_n(t)=2-2*cos(2*n*arctan(1/(2*t))); fixed-zeta O-constant independent of n; interval (sqrt(n),infinity), excluding atoms at sqrt(n). No RH, simplicity, low-head replacement or sign assumption.
LITERATURE_REASON: The incoming REVIEW_REQUIRED target changed from off-line displacement to a truncated pointwise counting-error integral; exact endpoint/tool coverage was essential. Coverage is now ready; no further literature repetition is recommended.

## Original nomination, step216

The saved gate action was “Assess the pointwise bound” with the same
formula and hypotheses as TARGET above. The wording now names the
mathematical continuation. The following nomination is retained as
pre-review context; its pending-coverage statements are superseded by
the completed comparison below.

## Bounded review and relevance

Reuse [review214](2026-11-10-symmetric-zero-tail-residual-review-214.md)
and the existing primary citations. Retrieve additional source passages
only where essential for the exact Stieltjes hypotheses; this is not a
request to repeat the Li or zero-counting source search in full.
Search the local direct-residual record for an existing proof or failure
before deciding IMPORT, SPECIALIZE or EXPLORE. This file proposes a
target and records no bound or mathematical derivation.

L978 has just bounded the off-line displacement of the actual tail at
O(sqrt(n)*log n). The target here would address the model counting-error
part. A later full residual would still require the smooth model term,
arithmetic normalization/constant matching, and the ordinary Li identity.
Even that residual would leave the growing actual finite-zero sum's sign
unproved; L968's whole-Li lower bound is the main downstream benchmark.

Approve a mathematical continuation only if the source comparison
supplies an exact import or elementary tools with a precise missing
specialization, preserving atoms at the cutoff and the improper tail.
Do not infer the desired pointwise rate from membership in l2. If the
source requires RH or already assumes the whole residual, park that
import and record the obstruction. No contour-majorant repair, low-head
ordinate replacement or new central sign mechanism is authorized here.

Essential local context: L978 and its counting citation; L018 for actual
zero multiplicities/conjugation, L977 for ordinary finite-cutoff
conventions and the contour stop, L968 for the downstream sign threshold.
L975 normalization and L976 envelope stop are context only. No
cross-notebook theorem is used. Mathlib coverage remains unchecked.

Next task recommendation: literature_comparison, standard/high. There is
no justified creative escalation: this continuation isolates another
standard error estimate, and no independently testable mechanism for
the finite-head signs has emerged from this single approved attempt.

## Completed comparison, step217, 10 November 2026

### Exact source scope and applicability

Reuse [review214](2026-11-10-symmetric-zero-tail-residual-review-214.md)
for the inspected counting proof and full-model theorem. The
[Hasanalizade-Shen-Wong v1 PDF](https://arxiv.org/pdf/2107.06506v1#page=2),
Corollary1.2/(1.5), gives for every t>=e the unconditional estimate

    |N(t)-M(t)|<=0.1038*log t+0.2573*log log t+9.3675.

The definition on p.1 uses 0<gamma<=t, not half-weight endpoints.
Section2/(2.3) obtains the symmetric count by the argument principle,
with orders; the proof first avoids boundary zeros. The corollary's
stated count and all-t range are what will be imported. No assumption
that the cutoff avoids ordinates is licensed or required. Its
bounded-height numerical input remains an external theorem input,
not a locally replayed certificate. For n with sqrt(n)<e, a compact
interval treatment is still a proof obligation, not an obstruction.

G. B. Folland, *Real Analysis: Modern Techniques and Their Applications*,
2nd ed., Wiley, 1999, §3.5, [Theorem3.36, p.107](https://djvu.online/file/NPF4BEtSuqdFA),
states for F,G in NBV, one continuous, and finite a<b:

    integral_(a,b] F dG + integral_(a,b] G dF
        =F(b)G(b)-F(a)G(a).

NBV (p.103) means globally bounded variation, right continuity and
zero limit at minus infinity. The complete proof reduces to increasing
functions and evaluates a product measure on a triangle by Fubini;
continuity removes the diagonal ambiguity. Theorem3.35, p.106, supplies
the absolutely continuous finite-interval FTC. These are finite-interval
tools: local integrators require suitable NBV extensions, and the
infinite upper limit requires a separate convergence argument. Both
are explicit obligations for the specialization, not hypotheses to
silently impose on the globally unbounded counting function.

The theorem's right-side value at a is F(a)G(a), not a left limit.
This convention agrees with an excluded lower atom. The target keeps
all zeros at the weak finite cutoff in the finite head. Establish the
specialized boundary identity and the uniform bound next turn; neither
has been derived here.

### Why a specialization, and its bounded test

The known error theorem concerns N-M, not its total variation. Do not
bound a signed counting-error integral by a fictitious O(log t) bound
on its variation. The finite-interval theorem handles signed
integrators, so positivity of d(N-M) is unnecessary. Required work is
ordinary differentiation and integrable bounds for the specified
oscillatory kernel, followed by a justified upper-limit passage.
The fixed constant must work for all integers n>=2. Do not replace a
pointwise task by an averaged estimate or drop the lower boundary.

[Arias de Reyna, author version31Jan2011, Thm1, pp.4-5](https://personal.us.es/arias/56-2RHB.pdf#page=4)
already supplies a real-ordinate model and normalized l2 error, with
its proof's smooth/counting split. Review214 has inspected that proof;
no reread was needed. The varying lower cutoff and requested pointwise
rate are the precise difference. No new Li identity, zero-counting
proof or Fourier theorem is called for. This is standard specialization
work, classified REPRODUCTION if successful, with no novelty claim.

Continue if the sourced finite-interval identity yields the stated
O(sqrt(n)*log n) uniformly, including cutoff atoms and convergence.
If the proposed kernel estimates or boundary control miss that rate,
record the actual bound and reassess this specialization. An RH premise,
finite-head sign or full-model l2 inference cannot repair a failed test.
A success pays only the counting-error tail part after L978; smooth-term
and arithmetic-constant matching, the ordinary Li identity and the
actual growing finite-head signs remain unresolved before L968's
whole-Li threshold can be used.

### Duplicate/failure screen, access and limits

The targeted local search found nominations in reviews214/215/216 and
step215/216 histories, but no earlier proof of this exact truncated
bound. L977's contour inference failure and L976's coefficient-envelope
stop are preserved. Review214's exact ordinate-replacement warning and
parked Coffey2007 source route remain applicable; this tail error is
not an all-degree ordinate-only equality. No sibling notebook was read.

Queries included `Li coefficients Stieltjes sqrt`, `Keiper counting
Stieltjes`, `Li coefficients truncated zero counting`, `Li coefficients
arctan error truncation` and finite-variation/right-continuity theorem
queries. The bounded search returned the known Arias de Reyna paper and
standard integration tools, not a matching inspected theorem. Other
AI notebooks and unreviewed purported RH proofs were not used as
mathematical evidence. This is no claim of global absence or novelty.

The Utah integration notes and Saks chapter could not be opened; the
large Folland PDF exceeded the web tool's size limit. A mirror's book
text was accessible: the full Thm3.36 statement/proof and NBV definition
were read there, and the indexed primary PDF text clarified the
half-open interval notation lost in mirror OCR. Thus essential source
coverage is available; failed access attempts are not pending blockers.
No visual scan verification is claimed. Full matching Mathlib coverage
was not checked and remains unknown; no Mathlib theorem is imported.

Outcome: EXPLORATION, LITERATURE, NOVELTY_UNCHECKED. New endpoint/tool
coverage approves a bounded standard attempt; the requested bound is
still unproved. Newly completed continuation coverage is left for the
supervisor's separate next-turn approval. No justified creative sign
mechanism is ready: the actual growing finite head remains unsigned.
