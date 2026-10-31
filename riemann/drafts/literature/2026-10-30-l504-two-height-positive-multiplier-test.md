# L504: proposed two-height positive-multiplier test

TARGET: Test whether nonnegative multipliers on heights b and 2b yield an O_R(a) weighted real-axis certificate for E_a on L504's H_a.
CHECKED: 2026-10-30
DECISION: EXPLORE
SEARCH_EVIDENCE: The completed 2026-10-30-l504-positive-class-residual-upper-bound.md review records exact-class, positive-real-part, constrained-duality and boundary-multiplier queries and local duplicate/failure checks; no matching quantitative theorem or two-height certificate was identified. No originality is certified.
SOURCE_EVIDENCE: Reuse that completed review: Goberna--Volle https://arxiv.org/pdf/2106.14573v1, Example 1.2, Lemma 2.1, Propositions 2.1/3.1/3.2 and Remark 3.1, pp. 3--9; parent Brevig et al. https://arxiv.org/pdf/2210.13922v2, (3.3), Theorems 3.6/3.10 and Corollary 3.9, pp. 12--15; ABR https://axler.net/HFT.pdf#page=124, second edition Theorem 6.13(a)/Corollary 6.15, pp. 119--120. Relevant proof cases and qualifications are recorded in the completed reviews; the separate approval rechecked the primary passages specified below.
COMPARISON: These sources motivate a constrained certificate but provide no uniform estimate or necessary dual representation here. L504 rules out its particular b-level full-space residual, without ruling out a modified residual that uses additional positivity at 2b. An explicit calculation requires no asserted strong-duality theorem.
GAP: For the explicit family below, prove an O_R(a) weighted functional bound uniformly at all large T, or a rigorous obstruction uniform over all nonnegative choices of its two coefficients; neither conclusion is known locally. Failure would stop this certificate family, not the H_a estimate.
REASON: The added higher-level multiplier uses positivity absent from L504's obstruction. This is one independently testable development of the existing dual-certificate route, with adequate elementary source coverage and no essential unread premise. Separate literature approval completed below; no mathematical test was performed.
SCOPE: Only the displayed two-height family and the elementary applicability checks below; no arbitrary-measure optimization, duality equivalence, positive-class counterexample, L503 audit, detector-cost theorem, arithmetic transfer or RH claim.

## Essential input and proposed family

Retain all L504 hypotheses and definitions: fixed R>0, L=log T,
a=log L/pi, b=a/4, B=L/(4pi), lambda=pi/(2a), K with K(0)=0,
V_R, u=Re f, H_a with lower normalization 1, M, Q_a and E_a.
L504 is the sole essential local theorem input. In particular its
full-space tests are not assumed to satisfy H_a. There is no uniform
Fourier-derivative bound, gap sign or sign outside the rectangle.

For a proposed extension of the same classical kernel, define, for
h in {b,2b} and 0<=y<b,

    p_h(t,y)=(1/(2h)) Re sech(pi(t+iy)/(2h)),
    W_{h,b}(x)=integral_0^b exp(-lambda y)
                           [p_h(x-a,y)+p_h(x+a,y)]dy,
    P_h(f)=integral_{-a}^a W_{h,b}(x)u(x,h)dx.

For h=b interpret the endpoint integral as in L504; P_b is its
existing mu_a term. These are definitions of a candidate family,
not a new kernel identity or an asserted estimate. Investigate

    F_{alpha,beta}=E_a+alpha P_b+beta P_{2b},
    alpha>=0, beta>=0,
    ||F||_M=sup_{0!=f in V_R} |F(f)|/M(f).

The coefficients may depend on a and fixed R, with no imposed growth
or mass bound. The proposed certificate threshold is

    inf_{alpha,beta>=0} ||F_{alpha,beta}||_M <= C_R a

at every sufficiently large real T, with C_R and onset independent
of T and f. No attainment of this infimum is assumed. Bounds only
on a sampled frequency set are not a certificate.

## Single bounded attempt and relevance

First verify integrability, Fourier normalization and the relation of
this proposed family to the one-sided H_a bound, using positivity
only where H_a provides it. Check 2b<B at the retained onset and the
continuity endpoint at b. Then analyze the complete residual, including
both coefficients, rather than one isolated large term. The desired
upper result must control the actual M norm and its zero weight. An
unweighted upper estimate requires a separately justified conversion;
no unaudited L503 conclusion may be silently used. A lower obstruction
may use M<=N from L504. Smooth Fourier witnesses must genuinely lie
in V_R; formal cosines alone are insufficient.

Continue this family only with the stated uniform upper threshold or
a rigorously quantified obstruction uniform over every nonnegative
coefficient choice. A candidate obstruction must account for choices
that vary with a, rather than fix alpha or beta first. Otherwise save
the partial residual and stop after this one attempt. No automatic
second coefficient search or general-measure optimization is approved.

A successful certificate could address the positive-class E bound and,
through L504, the conditional Q bound. A failed family is narrower
information and cannot settle either bound. Refuting the H_a inequality
itself would require genuine H_a functions with E_a/(a M) unbounded;
that construction is outside this nomination. Actual-Xi signs,
negative zero contributions, moving-test errors and height transfer
remain independent. No known result is being reproved for novelty;
the classical kernel calculation is only an applicability step.
Full matching Mathlib coverage is unchecked.

## Source access and approval

The completed parent assessment records the accessible primary sources
and all unread-lead qualifications. No unread source is essential to
this explicit computation. It does not authorize inferring a measure
certificate from abstract duality. This assessment was written in an earlier literature-only turn. The separate
approval below completes its source gate for the unchanged exact target.


## Separate source approval and URL repair, 2026-10-30

LITERATURE_REASON: Supervisor recovery reported missing direct source URLs in this ready assessment; repair those links and confirm the existing source comparison for the unchanged target, without another broad search or mathematical attempt.

Direct primary PDFs above were accessible. Reused the parent exact-class
search and duplicate/failure comparison, including the clipped-measure
failure record; no fresh novelty claim or additional search is needed.
The following source checks confirm scope, rather than prove the target:

- Goberna--Volle v1, printed pp. 7--9: rechecked Proposition 3.1,
  Proposition 3.2 and its proof, the revisited Example 1.2 and Remark 3.1.
  Strong Slater requires one objective-domain point with a common strictly
  negative margin for every constraint. The attained scalar sup-dual is
  distinct from finite-support conic multipliers; the finite-index remark
  cannot be imported for our continuum constraints. No such qualification
  or quantitative bound is asserted for H_a.
- Brevig--Chirre--Ortega-Cerda--Seip v2, printed pp. 14--15:
  rechecked the angular Fourier convention, Corollary 3.9, the p=1
  distributional warning and Theorem 3.10 with its full proof using
  Schwartz tests, Holder and density. Origin evaluation on PW^p is the
  source setting; at p=1 the residual functional can be unbounded.
  This supplies neither the moving two-height estimate nor conversion
  to M. Earlier (3.3)/Theorem 3.6 coverage is reused.
- Axler--Bourdon--Ramey, second edition, PDF dated 17 July 2020,
  printed pp. 119--120: rechecked Theorem 6.13(a)'s bounded-measure
  representation proof and Corollary 6.15's complete proof. The latter
  requires positivity throughout the ball; its proof uses constant
  spherical L1 mass and a positive weak-star limit. Rectangle positivity
  with a signed gap does not meet that hypothesis on a domain crossing
  the gap. No new specialization is claimed.

Decision EXPLORE is approved for the exact displayed family and scope.
This is a source-access/metadata repair, honestly STALLED mathematically:
no new theorem, obstruction, counterexample or changed route evidence.
It preserves L504's stop and does not validate the candidate kernel or
its applicability. The next turn may perform the single bounded test,
including those checks; there is no essential unread source for it.
No lemma, mathematical script, PROOF or DAG was changed. Full matching
Mathlib coverage remains unchecked. A creative central-gap target is
not justified by this repair; the missing positivity-sensitive foothold
remains the blocker, rather than a reason to relabel this development.
