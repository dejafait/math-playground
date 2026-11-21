# Primitive-theta Hankel-square determinant: bounded coefficient test

TARGET: Test det(I-c z^2 A)=Xi(z)/M_0 through z^4 for H_K f(x)=integral_0^infinity K(x+y)f(y)dy on L2(0,infinity), A=H_K^*H_K and c=S_1/Tr(A), by rigorously enclosing c^2 Tr(A^2)-S_2.
CHECKED: 2026-11-06
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step22's completed post-bracket discovery searched exact primitive-theta/Hankel/Fredholm and trace terminology, stronger spectral existence claims and local duplicates. No inspected result evaluates this fixed ansatz; no novelty is inferred. Reuse the complete query/comparison record in 2026-11-06-post-bracket-interface-discovery.md.
SOURCE_EVIDENCE: Direct primary URLs https://arxiv.org/pdf/2205.15007v2#page=5 (Bothner Section2.1 (10)-(13), printed p5) and https://arxiv.org/pdf/0804.2543v2#page=7 plus https://arxiv.org/pdf/0804.2543v2#page=10 (Bornemann Section2 product bound, printed p7; Section3 (3.1)-(3.3), printed p10) reopened and inspected in recovery step23 on 2026-11-06. Reuse step22's remaining source/overlap comparison; Arellano-Pena Theorem7.1 remains a contrast only.
COMPARISON: Standard theory supplies the factor/composition/determinant framework, not equality with Xi. Specialize only to L019's exact K and one scalar normalization; derive and certify the first-two-coefficient compatibility test without assuming the ansatz, RH, real zeros or any higher mixed sign.
GAP: Weighted kernel integrability, adjoint/trace formulas, scalar normalization, all enclosures and the residual sign remain to be justified. No identity or mismatch was established in literature. Higher traces and the full determinant identification remain independent open obligations even after a pass.
REASON: A fixed independently specified positive-operator candidate provides a concrete arithmetic-to-logarithm interface hypothesis and an inexpensive falsifier. Test compatibility before attempting an all-degree representation. A citation cannot evaluate the actual-theta integrals; known determinant facts should be imported without reproof.
SCOPE: Exactly this unshifted primitive-K adjoint square, ordinary determinant, L2 Lebesgue half-line measure and one scalar c. No fitted weights, other operators, shifts, rank corrections, exponential prefactors, regularized determinants or higher-coefficient sweep. New ready continuation subject to separate approval next turn.

The main gap is L030-L032/C032a. The intermediate target is whether
this one positive-operator determinant can even reproduce the first
two logarithmic coefficients of actual Xi. Its plausible downstream
use would be an independently constructed real-node representation if
the full arithmetic identity were eventually proved. The test neither
assumes nor establishes that identity.

Essential local inputs are L016/L019 for the exact kernel and tails,
L021 for M_0,M_2,M_4, and L024/L025 for S_1,S_2 and the normalized
local logarithm. L030-L032/C032a specify the downstream gap only.
L044/L057 and the September20 audit are contrasts to automatic Gram
transfer; L796 is a common-Favard contrast. No cross-notebook input.
No detailed proof of those contrasts is needed for this fixed test.

Use the exact K series and variable u of L019. Do not replace it by a
single summand, a model density, a rescaled logarithmic variable or a
finite truncation without explicit error bounds. The later attempt
must establish H_K is Hilbert-Schmidt, justify its real symmetric
adjoint, and establish positive trace class for A before using the
ordinary determinant. Bothner's half-line conditions and Bornemann's
general Hilbert-space product theory cover the framework. The
finite-interval continuous-kernel trace shortcut alone does not
license an unbounded-domain diagonal integral.

Import Plemelj's formula precisely from Bornemann Section3 (3.3),
and justify its specialization near z=0. Only local logarithms are
needed. Establish Tr(A)>0 and hence a well-defined c, with the
normalization in the TARGET; verify the factorial factors against
L025 before comparing the z^4 terms. These are future proof obligations,
not formulas already verified by this assessment. No global logarithm,
real-zero premise or equality of unknown spectra may be used.

For a numerical approach, justify every trace integral, order exchange,
kernel-series truncation, half-line tail and quadrature bound; ordinary
floating-point agreement is not a certificate. An analytic inequality
that rigorously separates the residual from zero also suffices. Use
only precision needed to decide this fixed comparison. Save a complete
certificate if a script is needed and print just bounds, the exact
required threshold zero, failures and its path. Do not add scripts
merely to manufacture a lemma or a positive sign certificate.

A certified nonzero residual rejects this ansatz and ends its coefficient
extension. An interval meeting zero is inconclusive, not evidence of
an identity; save partial work rather than enlarging the candidate
class. A proven zero residual clears only these two coefficients.
Every higher trace match, a full determinant identity, all-degree
mixed positivity and RH remain open. No disproof of RH follows from
failure of the ansatz.

The canonical source versions, exact citations, checked cases and
source-access qualifications are in the completed
[discovery assessment](2026-11-06-post-bracket-interface-discovery.md).
Its stronger existence-equivalence comparison cannot supply an
independent construction: the source's diagonal realization assumes
RH. The stopped Suzuki compressed operators and signed Toeplitz
determinants have different definitions. Historical failures remain
evidence with their original scopes, not a ban on this specific test.

The actual task is a bounded calculation/specialization, not a creative
all-degree sign theorem or novelty claim. Full matching Mathlib coverage
is unchecked; ordinary supporting operator theory is not a verification
of the arithmetic identity. This assessment authorizes no mathematics
in its own literature authoring turn.

## Step23 separate source approval and URL repair

The direct URLs in SOURCE_EVIDENCE were retrieved successfully. Bothner,
v2 (wrapper 12 September 2023, manuscript 14 September 2023), (10)-(13),
requires the weighted square integrals for both shifted factors and
defines their half-line composition and determinant. Only this framework
is approved; Lemma2.2's resolvent/differentiation conclusions are unused.
The complex-kernel symmetry terminology there does not justify a Hilbert
adjoint identification; the proposed real-K case still needs its own check.

Bornemann v2 (wrapper 24 June 2008; delivered manuscript dated
26 November 2024), Section2 p7, gives the general Hilbert-Schmidt product
bound. Section3 p10 (3.1)-(3.3) gives the trace-class spectral determinant,
trace-norm finite-rank limit, and Plemelj series within its convergence
disk. Only the determinant has the stated entire continuation. The
finite-interval diagonal shortcut remains outside the approved half-line
argument. No numerical error theorem is imported.

This repairs the missing direct-URL field and separately approves the
unchanged SPECIALIZE target. It adds no theorem, coefficient calculation,
new search result or evidence of an identity. Step22's duplicate/failure
search remains adequate at this unchanged scope. All stated local proof
and certification obligations remain unresolved; mathematical work may
now test precisely the saved target. No new continuation is nominated.
