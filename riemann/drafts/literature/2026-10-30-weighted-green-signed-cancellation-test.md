# Proposed bounded signed-curvature test

TARGET: Test signed-curvature cancellation for the weighted Green product test at delta=log log T/log T after exact completion-factor subtraction, retaining both curvature terms and bounding or isolating the remaining mixed log-modulus error.
CHECKED: 2026-10-30
DECISION: EXPLORE
SEARCH_EVIDENCE: Reuse the completed bounded identity, exact-amplitude, mixed-log-moment and obstruction comparison in drafts/literature/2026-10-30-weighted-green-curvature-source-review.md; no adequate quantitative theorem was identified. This newly written continuation requires separate approval before invocation, without rejecting the completed review.
SOURCE_EVIDENCE: Krishnapur arXiv:math/0607504v1, Section 2.2 (2.2.1)--(2.2.2), printed p. 14, https://arxiv.org/pdf/math/0607504v1#page=23; Fazzari arXiv:1912.08127v2 Proposition 1.1 and its conditional-zero-moment qualification, https://arxiv.org/html/1912.08127v2; Bettin--Fazzari arXiv:2208.08421v1 Theorem 1.2, https://arxiv.org/pdf/2208.08421v1. Primary statements and further comparisons are in the completed review.
COMPARISON: The deterministic compact-test identity is known; the signed estimate below is not supplied by inspected sources. Combine both curvatures before estimating errors. No RH-based prime-log approximation, analytic-test positivity, general weighted-count theorem or W_delta estimate is an input. No originality claim follows from this search.
GAP: Prove the specified signed bound with fixed C,c>0, or isolate an explicit weighted remainder and compare its actually justified bound with the threshold. Completion cancellation, smoothness, integrability, domination and all changing-parameter constants require proof during the later attempt.
REASON: A real two-variable test preserves amplitude before counting zeros and permits a concrete signed test distinct from positive detector squaring. Identity coverage permits an attempt, not approval of its mathematics. A renamed weighted count is a stop outcome, not an advance.
SCOPE: Actual xi/zeta at every sufficiently large real T, delta=log log T/log T, full zero multiplicities, strict beta>1/2+delta/2 and closed ordinate windows in W_delta; no RH, simplicity, spacing, independence, external half-plane premise or selected-zero moment. Exactly one bounded test, without full-range or kernel-transfer conclusions.

## Prospective test, not an established estimate

Let L=log T and delta=log L/L. Preserve W_delta from
[the exact-weight assessment](2026-10-30-zeta-squared-weighted-local-density.md).
Fix smooth real profiles chi,kappa,psi with 0<=chi,kappa<=1,
chi(x)=0 for x<=1/4 and chi(x)=1 for x>=1/2,
kappa(sigma)=1 for sigma<=1 and kappa(sigma)=0 for sigma>=5/4,
and psi>=0 supported in [-3,3], psi>=1 on [-2,2]. Propose

    Phi_delta(sigma)=chi((sigma-1/2)/delta) kappa(sigma),
    Psi_delta(u)=psi(u/delta),
    w(v)=integral_T^(2T) |zeta(1/2+it)|^2 Psi_delta(v-t) dt.

These are proposed fixed-profile choices within the reviewed scope, not
a proved specialization. For the source identity justify the product's
smoothness by convolution, not by differentiating the sharp [T,2T]
indicator. Treat full multiplicities, equality zeros and clipped windows;
do not claim equality with the strict zero count.

The quantitative test is the following signed sum. Both integrals are
over the plane, with only compact support contributing:

    H_xi=integral log|xi(sigma+iv)| Phi_delta''(sigma) w(v) d sigma dv,
    V_xi=integral log|xi(sigma+iv)| Phi_delta(sigma) w''(v) d sigma dv,
    H_xi+V_xi <= C T delta L^2 exp(-c delta L),

for some fixed C,c>0 independent of T. No such inequality, domination or
specialized identity is derived here. Check the factor 2pi in the later
application; constants may absorb fixed profiles but not powers of L
or delta. Absolute integrability at zeros must be justified before
interchanging integrals or differentiating any pairing.

Use q(s)=s(s-1) pi^(-s/2) Gamma(s/2)/2 from L018. The first bounded
operation is to justify subtracting log|q| from the combined curvature
pairing on a zero/pole-free neighborhood of the support. Test its exact
contribution before taking absolute values; do not separately delete
either curvature. Then try to exploit cancellation in the weighted
log|zeta(sigma+iv)| pairing. A bound for this pairing is not an input.
Any approximation must have its weighted changing-cutoff error proved
unconditionally; Fazzari's conditional Proposition 1.1 is unavailable.

Continue with a proved bound or a materially new explicit remainder
whose available bound and required saving are both stated. Stop if all
progress is a restatement of W_delta, an invocation of a missing weighted
estimate, or the previously losing absolute/count separation. A failed
sufficient estimate does not refute W_delta or RH. Save partial reasoning
before lengthy work. A changed target or essential unread source requires
a separate source gate, not approval during the same mathematical turn.

## Relevance, essential inputs and routing

L018 gives the entire function and multiplicities; foundations give Gamma
nonvanishing on the right half-plane. L471/L483/L485/L486 fix downstream
normalization and count-only limits; L500 is only an unaudited diagnostic
contrast. No source arithmetic proof is independently audited here.
Success might replace L486's amplitude/count separation after a separate
kernel-transfer check. Other scales, complementary mass, individual signs
and all-degree mixed positivity remain independent gaps. Mathlib unchecked.

After separate source approval recommend proof_attempt/creative,
deep_research/max. The obstruction is amplitude/off-line selection. The
bounded test is the displayed signed estimate after exact completion
subtraction; a proved cancellation or an explicit unclosed remainder
is decisive evidence. No mathematical attempt, new lemma or source
specialization proof was performed while writing this continuation.
