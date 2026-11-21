# Gaussian explicit-formula sign target: source review1555

TARGET: Test whether the Gaussian explicit formula proves K'(u)<0 for every u in [1/10000,1/200], where K(u)=sqrt(u)H(u) from C032j/s, with rigorous archimedean and prime-term bounds.
CHECKED: 2026-11-18
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Review1555 completed exact weighted-heat/monotonicity and explicit-formula searches and the narrow local duplicate/stop comparison; no inspected matching sign theorem was found. Queries, unread leads and version/access distinctions are in drafts/literature/2026-11-18-gaussian-explicit-formula-source-notes-1555.md; no novelty is inferred.
SOURCE_EVIDENCE: Chirre-Goncalves Proposition5 https://link.springer.com/article/10.1007/s00209-021-02820-9 ; Carneiro-Chirre-Milinovich1710.10362v1 Lemma8 pp9-10 https://arxiv.org/pdf/1710.10362 ; Polson1708.02653v24 Section4.3/(3), Lemma5.2, Theorem5.4 and Corollary5.5/full proofs, Lemmas6.1-6.2/full proofs https://arxiv.org/html/1708.02653v24 ; Connes2402.13082v1 (4)-(25), pp4-8 https://alainconnes.org/wp-content/uploads/heat-zeta.pdf ; Haslinger2.39 coverage1537 reused. Exact read ranges and qualifications: source-notes1555.
COMPARISON: Exact Gaussian decomposition and analytic tools are covered; the weighted sign is not an inspected source conclusion. C032s supplies the adjoining ranges and finite mass; its middle-interval counting bound remains unsuccessful. Connes's RH spectral interpretation is excluded; use the unconditional complex-zero explicit formula. Polson's ordinary derivative signs and asymptotic do not supply the weighted sign.
GAP: Prove a uniform strict bound for K' on the stated compact interval, verifying all new dominators, normalizations and effective archimedean/pole/prime bounds. These are specialization obligations, not assumed inequalities; a source formula or asymptotic alone does not close them.
REASON: Separate literature-only review1555 resolves the previously missing essential analytic source coverage without deriving a sign, lemma or script. SPECIALIZE licenses only the stated bounded attempt after the supervisor's separate approval of this changed assessment; source-wide preprint correctness and C032s's independent audit remain qualified.
SCOPE: Retain C032j/s actual-divisor, multiplicity, strip, finite-zero and fixed-v1 qualifications; u ranges over the closed interval [1/10000,1/200]. No RH, sign of the new terms, positivity of p_sigma, full J_eta cancellation or unsmoothed realization is assumed.

## Original nomination1554 retained

The following describes the nomination before review1555; its unread-source
and no-approval statements are historical, superseded by the fields above.

The intended downstream use is limited: a strict negative K' on this
interval, combined with C032s's two adjoining ranges, would settle the
fixed-width Levy-density sign test. Finite mass is already known from
C032s. Law comparison, a genuinely signed positive output, full
cancellation and actual-Xi realization remain separate tasks.

Review the primary theorem hypotheses and the relevant proof cases
before importing any formula. In particular, establish the scaling of
the Gaussian transform and account for the positive-ordinate convention
with multiplicity, possible complex zeros, pole terms and trivial zeros.
A leading heat asymptotic or an unchecked formula is insufficient.
Prefer importing an existing matching monotonicity theorem if found.

The bounded prospective mathematical test is a uniform strict sign on
this one compact u interval, with justified derivative interchanges and
explicit remainder bounds. A positive K' would stop this sufficient
monotonicity mechanism only; refuting the actual ordered density would
still require a rigorously negative integral in C032s's exact identity.
Failure of a chosen termwise bound also would not be an actual sign
counterexample. Retain reverse-order stop1553 and the separate full-
cancellation stop1302.

No new formula, prime-term sign, mathematical lemma or approval is
contained in this nomination. Full matching Mathlib coverage is unknown.

## Completed source review1555 — 18 November 2026

Use [source-notes1555](2026-11-18-gaussian-explicit-formula-source-notes-1555.md)
for the complete source inventory and exact imported identity. The all-zero
formula includes complex ordinates with multiplicity; its half-sum matches
C032j. All pole and gamma terms must be retained, with trivial zeros
already accounted for by the latter. Both Fourier conventions are recorded;
do not mix their factors. No RH spectral assumption is imported.

Primary theorem statements and the relevant Gaussian, contour, convergence,
archimedean subtraction and prime derivative proof cases have been inspected.
Reuse Haslinger2.39 for differentiation, but verify the new dominators in
research. Applying the explicit formula directly to a polynomial-Gaussian
test is also within scope. Do not differentiate asymptotic remainders or
reprove the general explicit formula. No new compact sign estimate has
been derived, and there is no claimed matching monotonicity import.

Continue only with a strict negative uniform bound on [1/10000,1/200].
A rigorous positive K' stops this sufficient mechanism; a failed bound
is inconclusive. Actual ordering fails only on a rigorously negative D.
Keep the full-cancellation, realization and main-Xi gaps independent.
This completes the missing-source review for the unchanged exact TARGET;
the newly changed ready assessment remains subject to separate supervisor
approval before invocation. No further source search is intrinsically needed.
