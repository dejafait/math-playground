# Finite Jensen cubic: completed signed-reference source comparison1354

TARGET: Assess whether C019e's exact finite I_3(d,x)/M_d(x) converges uniformly for 1<=x<=4 to an explicitly normalized real Airy-type reference with a simple zero, opposite endpoint signs and a positive absolute margin on closed subintervals avoiding its zeros, retaining the degree-dependent coefficients, radius, prefactor and both counterclockwise arcs.
CHECKED: 2026-11-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Exact identifier/Airy, unshifted Jensen/Airy and uniform cubic oscillatory-tail queries were checked; relevant local assessments1344/1350, stop1345 and canonical C019c/C019d/C019e were compared. No inspected theorem states this exact normalized signed-reference conclusion; search details and unread leads below. No novelty inference.
SOURCE_EVIDENCE: Ono arXiv2610.38870v1, 28 October2026, (3.2), Lemma7 including (3.11) and its uniform implicit-function proof, Lemma12/(4.2)-(4.3) and exact gamma-remainder proof, Lemma13's half-plane proof, Lemma14's complete comparison/integration-by-parts proof, Proposition15 and Corollary16; https://arxiv.org/html/2610.38870v1 . NIST DLMF1.2.8, released2026-09-15: 9.5.1/9.5.4, 9.2.1/9.2.3/9.2.4, 9.4.1/9.4.2, 9.9(i)/9.9.3/Table9.9.1 and 5.2.1; direct links and precise qualifications below. Prior CFU1957/Olde Daalhuis-Temme1994 assessments reused.
COMPARISON: Known real Airy integral, series and zero facts provide the reference tools; the exact finite cubic and its normalization still require specialization. Neither the Gaussian theorem nor the previously assessed general Airy theorems automatically identify I_3/M_d. No source certifies opposite signs at the saved x=1 and x=4; that condition must be tested and may fail.
GAP: Unproved obligations are degree-uniform coefficient and prefactor limits with adequate error control, finite oscillatory-tail completion, identification of the real reference, and rigorous zero/endpoint/margin tests. Pointwise phase convergence and decimal zero tables do not pay them. No limit or sign is derived in this source turn.
REASON: Essential source comparison is now complete enough for one bounded specialization attempt at the unchanged TARGET, after separate approval. SPECIALIZE authorizes a proof or informative failure of these explicit obligations, not an assumption that the nominated signs hold. Standard Airy identities should be cited; only the actual degree-dependent difference needs proof.
SCOPE: Exact TARGET with C019c/C019d/C019e, K=Q, x in [1,4], source q_e(d), r(d,x), exact finite Taylor coefficients, positive M_d and original orientations. Established-route REPRODUCTION, not creative discovery. Includes checking and, if warranted, rejecting the endpoint-sign condition. No different contour, changed x-window, global hyperbolicity, full manuscript audit or RH conclusion is covered. Newly ready coverage needs separate approval before research.
LITERATURE_REASON: Nomination1353 changes the observable beyond1350's finite additive replacement: identifying its limiting signed reference needs essential real-integral, zero and finite-tail source comparison. This review supplies that comparison once; the unchanged general CFU assessment is reused.

## Exact question and relevance

The question is the one saved in nomination1353, whose text is preserved.
The finite integral, all four coefficients and positive denominator are
defined canonically in C019e. C019c/C019d pay the original angular
complement. None of these inputs identifies a signed limiting reference.
The required threshold is a uniform additive error tending to zero on
the M_d scale, with a separately justified absolute reference margin.
The endpoints mean exactly x=1 and x=4. They may not be moved to obtain
the desired signs within this target.

The main gap remains L030–L032/C032a actual-Xi all-degree positivity.
Such a reference could yield local real-root sign information. The other
edge windows, exceptional-root deficit and every-degree hyperbolicity
remain independent. A successful local comparison is partial progress;
same-sign endpoints would refute only that extra nominated condition.
"A simple zero" does not license assuming exactly one zero in the window.
Every zero of the identified reference must be excluded from a compact
set on which an absolute positive margin is claimed.

## Inspected primary inputs and their hypotheses

**Exact phase and geometry.** [Ono v1](https://arxiv.org/html/2610.38870v1)
Lemma7 supplies uniform analytic edge control in delta=1/Lambda and
(3.11). Lemmas12–13 supply the exact principal-branch amplitude and
half-plane estimates. Lemma14's finite integration-by-parts identity
requires nonzero phase derivative; its bounds require exponential
control. Its Gaussian conclusion is not a cubic theorem. Proposition15
retains n_q>=1 and an exterior term; Corollary16 is restricted to I_d.
These conclusions do not identify the saved Airy limit.
Reuse C019c/C019d/C019e's verified specializations; do not audit or reprove
their payments again. No foundational or formal-artifact audit is claimed.

**Reference integral.** [DLMF9.5.1](https://dlmf.nist.gov/9.5.E1)
states, for real z,
\[
 \operatorname{Ai}(z)=\frac1\pi\int_0^\infty
                 \cos(t^3/3+zt)\,dt.
\]
This is the real improper oscillatory representation, with its stated
normalization. [DLMF9.5.4](https://dlmf.nist.gov/9.5.E4) instead uses
the oriented complex contour from infinity at angle -pi/3 to infinity
at angle pi/3 and prefactor 1/(2*pi*i). Both are attributed there to
Olver, *Asymptotics and Special Functions*, A.K.Peters1997 corrected
reprint of1974, p53. Their distinction matters: neither is an identity
for a finite perturbed angular cubic without a justified substitution
and tail argument. Cite the appropriate known identity after verifying
its use; do not reprove a general Airy representation. No Ai/Bi choice
or normalization for I_3 is asserted here.

**Zero and sign tools.** [DLMF9.9(i)](https://dlmf.nist.gov/9.9#i)
gives the negative real zero sequence of Ai, with no other Ai zeros;
[9.9.3](https://dlmf.nist.gov/9.9.E3) gives its derivative at those
zeros in terms of the Airy modulus. References are Olver1997 pp414–415
and p404; the definition in [9.8(i)](https://dlmf.nist.gov/9.8#i) was
also consulted. Table9.9.1 was inspected as a locator only. Its displayed
decimals are not strict enclosures for endpoint certification here.
These facts concern Ai, not an unidentified scaled reference; no zero
count or endpoint sign for the saved x-window is imported.

[DLMF9.2.1](https://dlmf.nist.gov/9.2.E1) gives the Airy equation and
entire solutions; [9.2.3](https://dlmf.nist.gov/9.2.E3) and
[9.2.4](https://dlmf.nist.gov/9.2.E4) give exact Ai initial values in
terms of Gamma(2/3) and Gamma(1/3), respectively, attributed to
Olver1997 p392. These are exact constants, not certified intervals for
their displayed decimals. [DLMF9.4.1](https://dlmf.nist.gov/9.4.E1)
and [9.4.2](https://dlmf.nist.gov/9.4.E2), Olver1997 p54, give the
entire series for Ai and its derivative. They provide a possible
evaluation tool after explicit remainder bounds are supplied, rather
than an endpoint certificate by themselves. If rigorous initial-value
bounds are needed, [DLMF5.2.1](https://dlmf.nist.gov/5.2.E1) states
Euler's Gamma integral for Re(z)>0; a later numerical enclosure still
requires full truncation and integration errors. No such computation
is performed or certified in this literature turn.

**General Airy coverage reused.** Assessment1344 already inspected
Chester–Friedman–Ursell1957, Theorems1–2/Sections2–5, and
Olde Daalhuis–Temme1994, Sections3/5/Appendix, with precise citations
and contour qualifications. No refresh of those unchanged claims is
needed. Their local analytic cubic transformation is not the angular
Taylor polynomial of C019e. The finite cubic can instead be tested
using its explicit coefficients, the cited real Airy identity and
ordinary finite-interval comparison/integration by parts. This is a
specialization obligation, not a claim that a general theorem already
proves the result. The automatic-import stop1345 remains valid.

## Bounded specialization obligations, not derivations

A separately approved mathematical attempt may address the exact TARGET
in the following order, preserving any partial result or obstruction:

1. Use C019e's exact coefficients and source saddle equations to test
   their rescaled limits uniformly in x. Keep q_e and the radius exact
   until error estimates permit replacement. Mere convergence at each
   fixed rescaled angle is insufficient on an expanding interval.
2. Test the prefactor on the unchanged M_d scale: the signed amplitude,
   its saddle modulus, the constant exponential offset relative to H_q,
   and the real Jacobian all matter. A positive denominator gives no
   signed lower bound. Bounds on an amplitude ratio alone do not
   identify its limit or sign.
3. Justify the finite-to-improper oscillatory passage with complete
   endpoint and derivative bounds. A fixed-cutoff comparison followed
   by a uniform tail bound is an allowed standard-method test. A
   degree-dependent real quadratic term must be controlled on the
   finite interval; it cannot be dropped and then integrated over
   infinity by an unproved dominated-convergence argument. Do not
   extend the finite cubic itself to infinity without checking that
   the resulting integral exists.
4. Only after identification, test existence of a simple reference zero
   and certify both fixed endpoint signs. Cite known Airy properties
   with the actual real argument and signed prefactor. Supply rigorous
   enclosures or analytic bounds if signs require evaluation. Uniform
   convergence of values does not alone prove uniqueness or simplicity
   of an actual polynomial zero. Compact zero-free reference sets need
   an absolute positive lower margin, never division by an Ai zero.

Continue with signed root transfer only if every required local error
and reference margin is paid. An incompatible endpoint-sign product
rejects that part of TARGET and calls for a separately assessed narrower
window or different downstream use; it does not invalidate the limit,
C019e, or RH. A failed bound that leaves cancellation undecided must be
reported as such. No coefficient, rate, sign, reference formula or new
lemma is calculated or approved as true during this review.

## Searches, duplicates, access and classification

Queries actually submitted: `"2610.38870" "Airy"`;
`"Jensen" "finite cubic" Airy unshifted`;
`"2610.38870" "Airy" site:arxiv.org`;
`"unshifted Jensen" "Airy" asymptotic`;
`"Airy" "oscillatory integral" "uniform" tail cubic`.
Identifier queries returned nonmatching aggregator results as well as
locators; none is theorem evidence. Primary Ono and NIST pages were
read directly. NIST's footer identifies version1.2.8, release2026-09-15.
The book identity was checked in the NIST bibliography; the cited book
pages are NIST attributions, not a claim of direct book-page inspection.

Mielke–Patz, *Uniform Asymptotic Expansions for the Fundamental Solution
of Infinite Harmonic Chains*, Z.Anal.Anwend.36(2017),437–475,
DOI10.4171/ZAA/1596, appeared as a primary-source search lead. Its
theorem hypotheses were not inspected, so no comparison or import from
it is asserted. Unrelated stationary-phase and numerical quadrature
hits were not used. No unread lead is essential for this finite
specialization with the stated elementary tools.

Named local searches/read ranges checked assessments1344/1350,
stop1345, working notes1352/1353 and history1353, alongside canonical
C019c/C019d/C019e. None contains a finished normalized signed limit.
No broader novelty or absence claim follows. Existing source-level
claims and unfinished work are preserved. The initial notebook-scoped
git status was oversized/truncated and establishes no mathematical
claim; subsequent inspection was narrow.

This completed step is LITERATURE / NOVELTY_UNCHECKED / EXPLORATION:
new essential source comparison, without a mathematical advance or a
proved obstruction to TARGET. No mathematical exploration turn is
spent. The nominated attempt is established-route REPRODUCTION under
SPECIALIZE, subject to separate next-turn approval. It is not a new
central creative mechanism; no such mechanism is justified by this
source comparison. Full matching Mathlib coverage, source foundational
validity and formal artifacts remain unchecked. No lemma, mathematical
script, PROOF, DAG, shared infrastructure or runtime state is changed.
