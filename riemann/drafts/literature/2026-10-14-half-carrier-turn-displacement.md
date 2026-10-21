# Half-carrier-turn displacement source comparison

TARGET: Assess shifted-fourth-moment coverage for the half-carrier-turn displacement test H^(-1) integral_[H,2H] |f(t+delta(t))-f(t)|^4 dt=o((log H)^4), where phi(t+delta(t))-phi(t)=pi.
CHECKED: 2026-10-14
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Bounded shifted-Hardy fourth-moment and displacement searches found primary Bui--Hall and Hughes--Young coverage; inspected their exact shift hypotheses and relevant proof cases, and compared L390/L411, L383's carrier conversion and step-99's recorded sign-symmetry failure. No matching variable-half-turn displacement theorem or completed local duplicate was located in the checked scope; no novelty is inferred.
SOURCE_EVIDENCE: Directly inspected Bui--Hall arXiv:2304.05178v1 Section 4.2 Proposition 3, defining quartic asymptotic/Theorem 3, Section 5 Cauchy passage and Section 7 ordinary-Hardy conversion; Hughes--Young arXiv:0709.2345v2 Theorem 1.1/(16)--(17), printed pp. 4--5, with prior assessed residue-cancellation coverage reused. L389 (2)--(3), L390 phase bounds and L383 carrier-ratio argument identify the actual input and supporting estimates.
COMPARISON: Bui--Hall supplies the complete sharp constant-small-complex-shift quartic formula and fixed-order derivative bounds; it does not state a moving shift or decide this displacement coefficient. These sources permit the scalar test after an explicit variable-shift and Hardy-phase specialization; L411 gives no opposite-sign relation and step-99 remains stopped.
GAP: Prove leading-scale replacement of the exact phase-defined shift by a constant microscopic shift, retain all Hardy carrier ratios and all five quartic binomial terms, and evaluate the complete coefficient with sharp endpoints; neither little-o nor a nonzero coefficient has been established in this literature turn.
REASON: Essential source coverage is accessible and sufficient for this bounded specialization without a new moment theorem; the remaining obligations are mathematical applications of covered inputs, not an essential unread source or approval of a derived result.

LITERATURE_REASON: The new proposed half-turn displacement mechanism changes the target from absolute clipping stability to a height-dependent shifted Hardy fourth moment; this specialization has not been assessed.

Use the actual f=F_0/A and gamma phase phi of L390/L411. On their
eventual increasing phase ray, delta(t) denotes the positive increment
for a phase change pi. The source review must check the exact shift,
not silently replace it by a fixed constant divided by log H. The
proposed target includes deciding that the little-o test fails; it does
not prescribe a favorable answer or assume RH.

The proposed downstream mechanism pairs opposite response phases while
trying to retain the critical jets. The scalar displacement test is a
first necessary check for that particular frozen-jet comparison. If it
has a nonzero quartic leading term, abandon that implementation, without
claiming that the actual clipped means differ or that another pairing
is impossible. If it is little-o, the derivative displacements, complete
response variation, product transfer and endpoint comparison still need
separate coverage and proof. No pairing implication is proved in this
proposal, and no signed clipped statistic is evaluated.

Essential input IDs for the continuation are L390 and L411; L405 is
the full-square benchmark motivating a possible opposite-sign comparison.
The main mixed-positivity gap, actual clipped signed mean, regulator scale,
total L367 margin/remainder and common-zero upper counts stay unresolved.
Preserve L394/L399/L400, step-99 and L410 stops. A scalar obstruction
model is not an actual-function displacement estimate; a formal phase
flip is not sign symmetry of the actual critical jets.

The preceding proposal is retained as motivation. The source comparison
below completes its coverage review; no displacement proof or coefficient
is derived in this literature-only step. Full matching Mathlib coverage is
not checked; this is unknown availability, not a claim of absence.

## Primary source scope and inspected cases

H. M. Bui and R. R. Hall, *On the derivatives of Hardy's function Z(t)*,
[arXiv:2304.05178v1](https://arxiv.org/html/2304.05178v1#S4.SS2),
11 April 2023, Section 4.2, Proposition 3, evaluates the sharp integral
J of two factors zeta(1/2+alpha_j+it) and two factors
zeta(1/2+beta_j-it), over [T,2T]. All four shifts are constant complex
numbers with modulus at most C/log T for fixed C. It has error
O(T(log T)^3), uniform in that range, and main term

    T(log T)^4/(2 zeta(2)) integral_[0,1]^4 (u1-u2)^2
      T^(-(alpha1+beta1)u1-(alpha2+beta2)u2)
      T^((alpha1-alpha2)(u1-u2)u3+(beta1-beta2)(u1-u2)u4) du.

This is the source formula, not its evaluation at the proposed shifts.
It includes coincident shifts without singular denominators. Section 4.2
omits its proof. Directly inspected the related Section 4.1 cancellation
of singular shift differences in (17)--(20), using integral identity (19),
and Section 5's Cauchy argument on shift circles. Section 7 uses two
positive-height and two negative-height representations, ordinary phase
derivatives, the uniform error and Proposition 3 to prove Theorem 3.
The preceding defining asymptotic gives the fixed-order fourth-product
scale (log T)^(k+ell+m+n+4), with one lower logarithmic degree in the
error. In particular the pure fixed orders zero and one supply the
scalar and first-derivative quartic envelopes needed for shift comparison.
Its odd-order cancellation is not a joint sign symmetry.

C. P. Hughes and M. P. Young, *The twisted fourth moment of the Riemann
zeta function*, J. reine angew. Math. 641 (2010), 203--236,
[arXiv:0709.2345v2](https://arxiv.org/pdf/0709.2345v2#page=4),
Theorem 1.1/(16)--(17), printed pp. 4--5, provides supporting independent
constant-shift coverage: coprime positive h,k, hk<=T^(2/11-epsilon),
four complex shifts O(1/log T), smooth nonnegative w supported in
[T/2,4T], and w^(j)=O_j(T0^(-j)), T^(1/2+epsilon)<<T0<<T.
Its error is O(T^(3/4+epsilon)(hk)^(7/8)(T/T0)^(9/4)).
Only the full six-term expression is regular at coincident shifts.
Reuse the inspected residue cancellations (46)--(58) and their final
combination recorded in
[the complete-square assessment](2026-10-10-discriminant-second-moment-leading-scale.md).
The scalar target needs h=k=1, no growing response head and no twisted
carrier theorem. Bui--Hall's already sharp formula avoids an unnecessary
new smoothing argument. Neither theorem allows substitution of a
height-dependent shift directly into its stated constant-shift formula.
No reproof of either moment theorem is justified.

## Applicability and bounded mathematical continuation

L389 (3) already identifies f=-sigma Z_Hardy for one constant sign sigma
on the connected positive ray, including critical zeros. Its phase is
the gamma phase of Q, not the response's full Euler phase. L390 gives
phi'=log(2+t)/2+O(1) and phi''=O(1/t), so the proposed implicit shift
is on the eventual increasing ray. L383's proof around (11) gives the
covered gamma-ratio conversion at small offsets; it is a two-factor
input and must not be relabeled a four-factor displacement conclusion.

The next mathematical attempt may compare the exact shift with the
candidate constant 2pi/log H on [H,2H]. It must prove a uniform shift
error at most O((log H)^(-2)), then use the fundamental theorem of
calculus, Holder and the imported ordinary first-derivative fourth
moment to control the resulting difference on an enlarged dyadic
interval. An integrated derivative bound cannot be replaced by a
pointwise assertion of small derivatives or by an unproved moving
supremum bound. This paragraph specifies proof obligations, not their
discharge or a new estimate established today.

For the constant shift, expand the fourth displacement into all five
real monomials. Represent each with two positive-height and two
negative-height zeta factors using the exact Hardy relation; retain the
ratios of gamma phases at the two heights. Prove their leading-phase
replacement in absolute integral error using quartic envelopes before
applying Proposition 3. Every scaled shift lies in a fixed bounded
complex set; no conditional large-shift theorem is needed. Keep the
original sharp [H,2H] endpoints. If any change of variables is used,
account for its Jacobian and both endpoint strips explicitly.

Only after those comparisons may the full source integral be specialized
and the complete real coefficient evaluated. A positive coefficient
stops the scalar frozen-jet implementation; vanishing permits checking
the required little-o remainder but proves no derivative displacement,
clipped pairing, response transfer or signed mean. This is the same
saved target, now source-ready for a separate mathematical invocation.
No new continuation beyond that scalar target is approved here.

## Search, duplicates and recorded failures

Queries included `Hardy Z shifted fourth moment Z(t+a/log T) difference
fourth moment`, `Hughes Young twisted fourth moment 0709.2345 theorem
shifts`, `"Hardy" "shifted fourth moment" difference`, and
`"Z(t" "Z(t+" "fourth moment" shift`. Search snippets were discovery
only. The primary Bui--Hall v1 HTML was fully readable at the relevant
sections; its PDF fetch timed out and a shell HTML fetch had DNS failure.
These are not source blockers because the primary HTML supplies the
complete theorem and relevant argument. The Hughes--Young v2 PDF
theorem was accessible. Broader-shift moment and derivative-zero-gap
papers found in search are uninspected, nonessential leads; no theorem
from them is used and no larger source survey is claimed.

Narrow reads covered L390's definitions, full response differentiation
and quartic norm proof; L411's hypotheses and transfer scope; L389's
known input and zero-safe Hardy identification; L366's exact Q; L368's
carrier definitions; and L383's small-offset carrier-ratio argument.
Checked the recorded step-99 draft/history and canonical clipped
assessment, plus the fixed-response-cell correlation assessment/failure.
That earlier correlation target concerns Wronskians within response
cells, not this scalar quartic displacement. No completed duplicate
in those records was found. L394/L399/L400 and L410 remain independent
failed implementations or scalar-moment obstructions; none establishes
this actual-function displacement or prohibits testing it.

Decision: SPECIALIZE. The source comparison changes readiness, not a
mathematical sign range. Global mixed positivity and the actual clipped
signed mean remain the main gaps. Essential local input IDs for the
mathematical attempt are L389, L390 and L383; L411 and L405 motivate
the downstream comparison but cannot supply shift smallness. Regulator
scale, total L367 margin/remainder and common-zero upper counts remain
unresolved. Full matching Mathlib coverage has not been checked.
