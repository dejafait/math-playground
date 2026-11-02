# Bounded second-derivative replay: proposed mathematical continuation

TARGET: Audit the second-y-derivative identity for C_A(iy) from its defining integral and test its sign for every y>0 using Csordas's associated-kernel admissibility, explicitly checking Norvidas's sign conventions.
CHECKED: 2026-10-31
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the completed exact-target and shape comparison in 2026-10-31-associated-theta-cauchy-second-derivative-review.md, including its listed searches and local duplicate screen; no exact finite-sign theorem was identified, and no novelty is claimed.
SOURCE_EVIDENCE: Csordas https://arxiv.org/html/1309.0055v2 (PDF https://arxiv.org/pdf/1309.0055v2), Definition 1.2, Theorem 3.5 with both proof cases, (4.2), Theorem 4.5; Norvidas https://arxiv.org/html/2009.04449v1 (PDF https://arxiv.org/pdf/2009.04449v1), Theorem 2 with both proof directions, Corollary 3, (1.3), (2.2)-(2.16); Norvidas https://arxiv.org/html/2009.04492v1, (1.6)-(1.7), (2.1). All primary passages were inspected in the completed parent review; direct links and exact scope are retained there.
COMPARISON: Known associated-kernel admissibility supplies shape and decay, not the requested differentiated Cauchy sign. Norvidas supplies derivative representations with sign conventions requiring replay, and an all-order criterion; neither is an automatic finite-sign application.
GAP: Verify the transform normalization, exact second-y-derivative identity, integration by parts and all endpoint terms; decide its all-y>0 sign without a Fourier-positivity premise. No outcome or corrected source formula is presumed.
REASON: A bounded routine verification of a suspect formula/specialization is justified before either importing or abandoning the finite test; theta logarithmic concavity and the full Cauchy criterion should be cited, not reproved.
SCOPE: Only the second derivative for this exact real-axis A, with a generic admissible-kernel argument permitted if it settles the same sign. No third or higher derivatives, all-order criterion application, boundary transfer, or new central mechanism is approved by this scope. Newly written continuation requires separate next-turn approval.

## Inputs, hypotheses and replay obligations

Use L019's actual k, the even identification in L239, L233's complete
absolute-moment/Fourier argument, and L596's definition of A. Use

    A(t)=integral_R s^2 k(s+t)k(s-t) ds,
    C_A(z)=(2pi i)^(-1) integral_R A(t)/(t-z) dt, Im z>0.

The source's normalization is k(u)=4 Phi(u/2), already recorded in the
parent review. Check the exact factor in A before invoking Csordas's
Theorem 4.5. Import that theorem's smoothness, evenness, strict decrease
on the positive axis and decay with its qualifications. L233 alone
already supplies integrability. This C_A is not L596's A(iy).

Work on compact y intervals with positive lower endpoint when justifying
differentiation, then cover every y>0. Check reality from evenness and
normalization; distinguish y derivatives from complex derivatives.
If moving derivatives to A by integration by parts, show boundary terms
at zero and infinity and the needed integrability. Inspect the second-
derivative case of Norvidas's (2.15) against the defining Poisson integral
(1.3), not by assuming the displayed sign is correct. The extracted PDF
and HTML agree on the sign-sensitive formulas; no correction has yet
been proved locally. If a source error is demonstrated, document its
exact scope and the independent verification in a canonical lemma.

## Relevance and stop test

Main gap: all-degree actual-Xi signs at unbounded heights. A finite
second-derivative sign can check one necessary part of the first
associated-kernel hierarchy; it leaves the rest of that hierarchy and
all higher mixed forms unresolved. For real-even normalized data the
known Norvidas criterion already handles half-plane reconstruction once
the full Poisson hierarchy holds; do not list it as an independent gap
in this special case. The required full hierarchy itself remains open.

Continue for this one replay if the sign is isolated by the cited shape
input and justified calculus. Stop if it needs Ahat>=0, an unsupported
higher derivative, or a nonvanishing unbounded endpoint term. A generic
shape-only success should end this finite test without being sold as a
theta-specific mechanism. Compare L232/L247's different transforms and
L233/L253/L257's retained limitations as recorded in the parent review.
No numerical experiment or mathematical script is needed. Matching
Mathlib coverage is not checked; uncertainty is not absence.

## Direct-source recovery check (2026-10-31)

LITERATURE_REASON: The supervisor reported missing direct source URLs in this ready assessment; repair that source-location field without expanding the mathematical target.

Reopened the three versioned primary HTML URLs now written directly in
SOURCE_EVIDENCE. Csordas's Theorem 3.5 states admissibility under strict
logarithmic concavity, and Theorem 4.5 applies it to the associated theta
kernels of (4.6). Norvidas 2009.04449v1 Theorem 2 retains bounded continuous
real-even data, normalization at zero, and the full complete-monotonicity
condition; its (2.15) retains the sign-sensitive display flagged in the
parent review. Norvidas 2009.04492v1 Theorem 3 retains both half-plane
conditions, and (2.1) is the differentiated Cauchy representation. These
locations were accessible. The existing parent review supplies the fuller
proof-case reading and duplicate/failure comparison; it is reused rather
than replaced. No formula was derived or corrected in this recovery step.

The SPECIALIZE decision and exact TARGET are unchanged. This is a source
location repair, not new mathematical evidence or a repeated attempt at the
sign. All normalization, endpoint and sign obligations above remain for
the next mathematical turn. Mathlib coverage remains unchecked.
