# Signed side-gap flux: bounded dual-functional test

TARGET: Test the one-sided gap-flux bound Q_T<=C_R a M_T under L503's unchanged signed rectangle hypotheses using a positivity-supported dual functional with a genuinely bounded real-axis residual.
CHECKED: 2026-10-30
DECISION: EXPLORE
SEARCH_EVIDENCE: Reuse the completed exact-bound searches and local duplicate/failure comparison in drafts/literature/2026-10-30-signed-gap-flux-conditional-bound.md; no matching theorem was identified, and no originality is inferred.
SOURCE_EVIDENCE: Brevig--Chirre--Ortega-Cerda--Seip, https://arxiv.org/pdf/2210.13922v2, (3.3), Theorem 3.6, Corollary 3.9, Theorem 3.10, printed pp. 12--15, including the potentially unbounded p=1 distributional residual and its Schwartz-test proof; ABR, https://axler.net/HFT.pdf#page=124, second edition, 17 July 2020, Theorem 6.13(a)/Corollary 6.15, printed pp. 119--120. Exact statements and essential proof cases are assessed in the parent review.
COMPARISON: Known evaluation duality suggests testing a real-axis functional, but it neither uses continuum rectangle positivity nor supplies a bounded L1 dual residual for Q. The inspected positive Poisson theorem does not cover the signed gap. L503's absolute Fourier closure remains too large and is stopped.
GAP: Establish the proposed one-sided inequality uniformly in T and f, or rigorously obstruct a specific positivity-supported dual certificate; formal distributional Fourier matching alone does not give the required finite norm.
REASON: The conditional source review identifies a concrete uncovered dual-functional mechanism within the unchanged class. This is a bounded test of the strengthened residual estimate, not a new positivity domain, a proof of feasibility or an imported theorem.
SCOPE: One dual-functional attempt for the exact family below; no new detector construction, other geometry, unconditional first-mode repeat or arithmetic application. Newly nominated ready coverage requires separate supervisor approval before mathematical invocation.

## Exact family, input and threshold

Fix R>0 independently of T, with L=log T, a=log L/pi, b=a/4,
B=L/(4pi), lambda=pi/(2a). Let K(x)=1-(sin(pi x)/(pi x))^2,
K(0)=0. Let f_T be even entire, real on R, and represented by the
inverse Fourier transform in the 2pi convention of a C_c^infinity
function supported on [-R,R]. Require Re f_T(x+iy)>=1 for |x|<=a,
b<|y|<B, with no other sign or uniform Fourier-derivative bound. Put

    M_T=integral_R |f_T(x)|K(x)dx,
    Q_T=-integral_0^b exp(-lambda y)
          [Re f_T(a+iy)+Re f_T(-a+iy)]dy.

The target is Q_T<=C_R a M_T beyond a single onset for fixed R, with
finite C_R independent of T and f_T. Preserve the lower normalization
1 in the rectangle; do not normalize M without tracking that change.
L503 is the sole prospective local input and remains unaudited. Its
N<=A_R M conversion can be replayed, so a uniform O_R(a) unweighted
real-axis functional norm would suffice for the proposed estimate.
Its necessity bound is relevant downstream only if valid; a complete
independent audit remains outstanding. L502 is contrast only.

## Bounded attempt and stopping rule

Seek a real-axis dual representation controlling the complete signed
gap functional after using only positive weights or measures supported
where rectangle positivity is known. The sign, representation, support
and residual norm are tasks to prove, not identities or a duality
equivalence asserted here. Check the source's angular Fourier convention
before any specialization. Prove boundedness on the full smooth Fourier
class, not a sampled grid; at the L1 endpoint a formal distributional
residual may have infinite norm.

A uniform O_R(a) certificate is the desired positive test. An admissible
family with Q_T/(a M_T) unbounded would refute the estimate. Failure of
one certificate ansatz does not refute the inequality. If only the old
exponential gap norm, a formal residual or no quantitative improvement
is obtained, preserve that evidence and stop the ansatz after this one
attempt; do not repeat the unconditional closure under another name.

The prospective downstream use is a fixed-R nonvanishing absolute-cost
bound through L503, eliminating this sufficient detector class. It would
not establish actual-Xi signs, control negative actual-zero contributions,
prove arithmetic moving-test/height transfer or RH. No zero-free premise,
simplicity, spacing or cross-notebook input is assumed. Mathlib coverage
is unchecked. No dual certificate or new mathematical result is claimed
by this assessment.
