# Actual Jensen circle: oscillatory annulus nomination1347

TARGET: Assess whether one integration by parts pays the actual K=Q Jensen angular annulus (log d)*d^(-1/3)<=|theta|<=theta_0 at q=q_e+x*d^(-2/3), 1<=x<=4, for each fixed 0<theta_0<=1/10: does sup_x |I_ann|/M_d(x)=o(1), with source r, both counterclockwise arcs, C019c's Cauchy prefactor and its unchanged M_d scale?
CHECKED: 2026-11-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Review1348 searched exact arXiv identifier with Airy/annulus, unshifted Jensen coalescing-saddle terminology and complex nonstationary phase; inspected the primary source below. Notebook-scoped annulus/nonstationary searches and targeted 1344-1347 assessments/failure/history reads found no completed matching annular estimate. Search absence is not novelty evidence.
SOURCE_EVIDENCE: Ken Ono, An Asymptotic Jensen–Pólya Criterion for GRH, arXiv:2610.38870v1, 28 October 2026, exact (2.5)-(3.12), Lemma9/full proof, Corollary10/full proof, Lemmas12-14/full proofs and Proposition15/proof through (5.6), primary HTML Sections2.2-5.2: https://arxiv.org/html/2610.38870v1 . Relevant near-edge, sector, Euler-product, endpoint and complex-phase cases inspected; no formalization audit.
COMPARISON: Source Lemma14 contains the needed one-step complex integration-by-parts identity with boundary terms, but its Gaussian theorem is not the requested annular theorem. Lemma13's stated C1 estimate concerns its saddle interval only; the Euler-product inequalities in its proof and Lemma12 supply reusable amplitude inputs under explicit half-plane/sector hypotheses. The exact phase and saddle equations permit a separate derivative test. No inspected stronger result pays this actual moving annulus automatically.
GAP: Prove or refute quantitative nonstationarity and sufficient weighted second-derivative control on the nominated annulus; verify amplitude/derivative bounds there from the cited half-plane estimates, then retain both endpoints and normalize by unchanged M_d. These are the mathematical specialization obligations, not missing source statements or established bounds. Uniformity in x is essential.
REASON: Essential source comparison is complete for a bounded attempt using cited estimates and the exact identity. Citation alone leaves the actual-annulus derivative and weighted-remainder calculation unresolved. Ready coverage permits that test only; it does not approve an Airy expansion, signs or full-contour asymptotics. No research calculation was made in this literature turn.
SCOPE: Exact TARGET only, K=Q, integer d tending to infinity, x in [1,4], each fixed theta_0 in (0,1/10], C019c radius/branches/prefactor/M_d and both counterclockwise arcs unchanged. REPRODUCTION, established-route development. A newly changed ready assessment is subject to the supervisor's separate approval before invocation.

## Exact proposed observable

Use all exact definitions and hypotheses of C019c, including its source
saddle radius r=r(d,x), integer d, fixed K=Q and x in [1,4]. Let
epsilon_d=(log d)*d^(-1/3). For sufficiently large d, epsilon_d<theta_0.
Define I_ann by the same Cauchy integral as I_out in C019c, replacing
its angular set by epsilon_d<=|theta|<=theta_0. Both arcs retain their
counterclockwise orientation. Keep M_d unchanged, including the
absolute saddle amplitude, exp(d H_q), d^(-1/3) and d!/d^d. No local
integral lower bound, Airy value or new normalization is assumed.

The proposed mechanism is cancellation by one integration by parts on
each angular interval using the exact complex phase, with all boundary
terms retained. Source review must check the required nonstationarity,
amplitude regularity, uniform bounds and any stronger existing result.
It must compare with Ono's actual near-edge/Gaussian ranges, rather
than importing the Gaussian conclusion outside those ranges. This
nomination does not assert that integration by parts works.

The original nomination required a separate source review; review1348
below completes that review without executing the test. A separately
approved mathematical attempt must exhibit a
uniform upper bound tending to zero after division by M_d, or identify
the exact failed inequality. A failed upper-bound certificate is not a
lower bound on the actual annular integral. A source hypothesis failure
must remain recorded; missing coverage stays REVIEW_REQUIRED or
SOURCE_BLOCKED as appropriate, rather than being silently supplied.

This would at most pay another contour piece. A cubic local integral,
its real reference and orientation, a nonzero signed margin, outer root
losses and every-degree hyperbolicity remain independent. Main target
L030-L032/C032a is unchanged. No cross-notebook input is nominated.

This is established-route development, not a protected creative central
mechanism. C019c's audit was completed in1347. No mathematical work on this
new target was performed in either nomination1347 or review1348, and no
new theorem or novelty is claimed.
Full matching Mathlib coverage for the proposed annular result is unchecked.

## Completed source comparison, 17 November 2026 (1348)

**Imported inputs, with their restrictions.** Ono v1 Lemma7/(3.6)-(3.11)
gives uniform near-edge geometry for positive q-q_e at most a fixed t_0.
Lemma8/(3.12) controls the real phase on the closed lower semicircle.
Lemma9 bounds its first three angular derivatives. Corollary10 uses only
|theta+2alpha|<=ell_q, with ell_q=epsilon_0 min(alpha,cos alpha).
Lemma12/(4.3) bounds log g and its derivative for |arg w|<=pi/2,
|w|>=W_0. Lemma13 assumes q_e<q<=c_0 T; its proof gives Euler-product
upper/lower bounds for sigma>1 and a logarithmic derivative bound for
sigma>=4. Its stated normalized C1 bound is on that local interval.

Lemma14 assumes p in C3 and f in C1 on [-1,1], p(0)=p'(0)=0,
p''(0)=-A, |A|=1, Re A>0, Re p<=0, |p'|>=c|y| and fixed norm bounds;
its parameter n is at least1. Its proof integrates once by parts on each
tail, retains endpoints, and estimates both f'/p' and fp''/(p')^2.
Proposition15/(5.4) also requires n_q>=1. Its subsequent uniform o(1)
formula uses the distinct range (5.6). None is an annular assertion.

**Applicability and what a later proof must supply.** C019c already
checks the eventual q range, sector, saddle denominator and exact
angular measure for this degree/parameter window. Reuse those checks;
they do not check annular derivatives. The nominated annulus is outside
the range on which the source asserts its local C1 bound and its local
linear nonstationarity estimate. Neither conclusion may be moved there
by changing the variable name. In particular, Lemma7's uniqueness of a
saddle is not a quantitative lower bound for the derivative away from it.

For the amplitude, the appropriate source ingredients are the half-plane
Euler-product estimates inside Lemma13's proof and (4.3), rather than
its whole-circle polynomial allowance or its local C1 conclusion. The
later attempt must verify Re(1/2+w)>=4 on every retained angle with a
common onset, bound the angular derivative of each factor, and divide
by the actual nonzero saddle amplitude. It must keep the theta
coordinate: a derivative bound in the source's rescaled y coordinate
cannot be inserted as a theta derivative. No annular extension has been
proved here.

For the phase, use the exact (3.2) and the saddle identities (3.8)-(3.9),
not a fixed limiting phase with an uncontrolled 1/Lambda error. The
moving endpoint makes that distinction essential. A concrete candidate
test is |phi'(theta)|>=c|theta|^2 together with
|phi''(theta)|<=C|theta| on the lower annulus, where
phi(theta)=h_q(r^2 exp(i theta))-h_q(u_q). These inequalities are
**unproved targets**, not imported estimates. Other sufficient bounds
are allowed only for this same annular observable. A uniform O(1)
second-derivative bound alone must not be silently sharpened to the
displayed target.

The integration-by-parts identity in Lemma14's proof is algebraic for a
C2 complex phase with nonzero derivative and a C1 amplitude on a finite
interval. Only this identity, with its actual endpoint terms, is needed;
its local Gaussian theorem and relative error are not being imported.
Use Lemma8 for the modulus of the shifted exponential. Then estimate
both weighted remainder terms actually produced by that identity. The
upper arc uses conjugation with both original arcs counterclockwise;
there is no contour deformation, smoothing of endpoints or connector.
The normalization and factorial prefactor remain those of C019c.

**Bounded discriminator.** Continue only if the later attempt obtains a
uniform upper certificate tending to zero after division by M_d. Stop
that certificate if quantitative nonstationarity, amplitude control or
the full weighted endpoint/remainder bound fails, recording the precise
failed inequality. Such failure is not a lower bound on I_ann and is
not an impossibility theorem for cancellation. No target rate, target
inequality or signed local integral has been established by this review.

## Search and overlap record

Queries used: `"2610.38870" Jensen annulus saddle point`;
`Jensen polynomials Riemann xi coalescing saddle Airy asymptotics unshifted Ono 2026`;
`"2610.38870" "Airy"`; `"2610.38870" "annulus"`;
`"non-stationary" "complex phase" integration by parts derivative bound`.
Exact-identifier search results included unrelated aggregator text;
that text supplied no mathematical evidence. The primary v1 abstract
page confirmed the version; theorem evidence came from the HTML above.

Reuse assessment1344 for CFU1957 Sections2-5 and Olde Daalhuis-Temme1994
Sections3/5/Appendix: neither supplies this annular certificate, and their
analytic contour hypotheses are unnecessary for one finite-interval
integration by parts. The automatic-Airy stop remains recorded in
ATTEMPTS/2026-11-17-unshifted-edge-automatic-airy-import-stop-1345.md.
C019c's fixed-cutoff result is retained with its original scope.

A search lead on general complex nonstationary phase was the primary
APDE2024 article *Upper bound on the number of resonances for even
asymptotically hyperbolic manifolds with real-analytic ends*,
https://msp.org/apde/2024/17-10/apde-v17-n10-p06-s.pdf . Opening returned
no readable text. This is an **unread, nonessential lead**, not a cited
theorem, source blocker or stronger-result claim. The already inspected
finite-interval identity supplies the method needed for the nominated
test. No additional generic browsing is required before that attempt.

Assessment result: SPECIALIZE, with no annular proof and no claim of
originality. The main positivity gap and all independent local sign,
root-deficit and all-degree obligations stated above remain open.
