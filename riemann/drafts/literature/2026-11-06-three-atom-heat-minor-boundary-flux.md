# Fixed three-atom heat-minor boundary flux — proposed specialization

TARGET: Test whether the factorial-normalized three-atom heat law on {0,1,4} admits a rank-two D_(3,2)=0 boundary with all proper matrix minors positive and strictly positive time derivative.
CHECKED: 2026-11-06
DECISION: SPECIALIZE
SEARCH_EVIDENCE: The completed actual-Xi signed-integral discovery searched exact heat/minor/cofactor/backward/moment terms in primary-source discovery and the active notebook; found the primary Hexagon paper and its earlier identifier mismatch, but no inspected theorem deciding this exact fixed-family flux question. No novelty inference.
SOURCE_EVIDENCE: Pulin Shi, Coefficient Dynamics and Consecutive Toeplitz Minors for the de Bruijn–Newman Family, https://hexagonmath.org/pdf/2610.00521v1, PDF24 October2026, Corollary3.2/(3.4)–(3.5), Proposition3.3/(3.6), Theorem3.4, Proposition9.1/(9.1) and Remark9.2, pp5–6/12–13; complete relevant proofs and compact-parameter domination cases inspected in the parent review.
COMPARISON: The source supplies normalized moment coefficients, heat evolution and an exact alternating row-derivative identity, with no minor-sign theorem. The proposed finite law makes convergence automatic but retains all factorials and signed cofactors. Its boundary-flux conclusion still requires a separate exact algebraic attempt; it is not an actual-Xi assertion or a larger L827 moment test.
GAP: Decide existence of the stated strict positive flux with exact zero determinant and every proper minor positive, in this single fixed three-atom family. Actual-theta constraints, higher orders, full cone invariance and RH signs remain outside scope.
REASON: Specialize known determinant differentiation to a bounded signed-premise discriminator, rather than redo a known actual positive minor or a stopped angular core. The completed literature step derives no new identity, boundary point or sign; the new ready assessment receives separate supervisor approval before research.
SCOPE: Only positive probability weights on {0,1,4}, the single 3-by-3 block [q_(2+i-j)] and its first time derivative at0. Exact algebra/elimination or a rigorously certified witness is permitted after approval; no additional support family, higher-rank sweep, actual-theta quadrature or new general sign theorem is covered.
COVERED_TARGET: Test whether the factorial-normalized three-atom heat law on {0,1,4} admits a rank-two D_(3,2)=0 boundary with all proper matrix minors positive and strictly positive time derivative.

## Defined test and threshold

Let p_0,p_1,p_4>0, p_0+p_1+p_4=1, and define

    q_n(t) = sum_(y in {0,1,4}) p_y exp(t y) y^n/(2n)!, n>=0,
    0^0=1,   M(t)=[q_(2+i-j)(t)]_(i,j=0)^2,   B(t)=det M(t).

Seek weights for which rank M(0)=2, B(0)=0, every one-by-one and
two-by-two minor of M(0) is strictly positive, and B'(0)>0.
Every proper minor means all of them, not just consecutive or principal
ones. Retain q_0 through q_5 and all normalizations. No witness or
expansion has been calculated. Algebraic weights require exact
isolating intervals/equality proofs, not a floating near-zero determinant.

## Source use and reason for specialization

The source's q_n(t) is an integral of u^(2n) exp(t u^2) Phi(u)/(2n)!.
Our explicitly defined model is a positive finite measure in y=u^2;
it is not the source's theta density. The source proof of the heat shift
uses differentiation of that moment integrand. For a finite sum this
applicability check has no interchange or tail obligation. The future
attempt must verify its own finite coefficient shifts and every term
of the row-replacement formula rather than assume that general
coefficient monotonicity signs a determinant. Cite the source identity;
no reproof of its analytic semigroup or any PF theorem is needed.

No theorem here equates raw-moment Hankel positivity with factorial
coefficient Toeplitz positivity. No use is made of the source's full
strict-minor criterion, product alphabet, zero threshold, numerical
bounds or asserted total-positivity references. Its normalization at
actual t=0 was compared using L019/L021 and L786, but the actual-Xi
conclusions of L786 are not premises about this arbitrary atomic law.
L825, L827, L775 and L842 are stopping/context evidence, not sign inputs.
L030–L032/C032a identify the main downstream gap only. No cross-notebook
input or original numerical certificate is needed for this finite model.

## Decision and limits

A rigorous B'(0)>0 witness at the specified boundary stops using these
finite moment/proper-minor premises alone to guarantee positivity under
decreasing time. This is a signed-flow obstruction, distinct from L825's
common-symbol mismatch, L827's reciprocal moment consistency and L775's
absolute angular mass comparison. It would require a stronger
actual-theta condition before attempting that descent mechanism.

A rigorous nonexistence result covers only this two-parameter weight
simplex. It neither proves a larger cone invariant nor licenses another
support/rank search. Failure of a bounded search to decide the question
is EXPLORATION, with partial reasoning preserved and no automatic
extension. Any proposed wider scope or actual signed inequality needs
its own review. No amount of passing this model test signs the actual
all-degree family. Full matching Mathlib coverage is unchecked.

The intended work is conventional specialization of known moment and
determinant differentiation, classified REPRODUCTION, not creative
research or a new theorem claim. The main creative blocker remains a
sufficient signed actual-theta estimate. This assessment is newly saved;
the supervisor supplies the separate approval turn before invocation.
