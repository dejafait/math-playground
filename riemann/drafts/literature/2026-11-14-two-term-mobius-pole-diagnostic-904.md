# Two-term actual Möbius head: independent diagnostic coverage

TARGET: Test whether the two-term Möbius head of C466a's reciprocal-Xi transform can have a globally negligible inverse-Laplace remainder, accounting for the s=1/4 singularity and the actual density's finite mass.
CHECKED: 2026-11-14
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Review904 searched reciprocal-Xi/Möbius/inverse-Laplace terminology and screened the local direct-Mellin, L625/L722 and contact stops; standard transform/contour tools cover this diagnostic, with no claim of originality or completed calculation.
SOURCE_EVIDENCE: C466a's normalized factorization and finite probability mass; DLMF27.4.5, 25.2(i), 1.14.3/1.14.20 and 5.11.1/5.11(ii), with Cauchy's residue theorem as the standard contour input; exact primary links and read cases are in assessment903's completed904 review.
COMPARISON: The Möbius series and pole/gamma tools are known; only the specified finite-head normalization and inverse relative-error comparison are to be specialized. This tests an unconditional approximation premise, not the unread Polson reciprocal-sign claims or C466b(7)'s sign.
GAP: No two-term inverse, residue, contour displacement, large-x asymptotic or relative-error conclusion has been proved in this nomination; all are tasks for the bounded specialization, including convergence on both contours.
REASON: Independent of blocked signed-forcing source coverage, this diagnostic can decide whether global head domination is a legitimate preparatory premise or whether later work must preserve joint cancellation on a compact contact window.
SCOPE: Actual p=theta_1 and c_0 of C466a; the fixed head is n=1,2 only; principal square root; ordinary Möbius convergence on Re(s)=1, with any contour displacement applied only to the explicitly specified finite head; no continuation of the infinite Möbius series.

This is a newly written ready continuation for separate supervisor approval.
No mathematical attempt or source-result specialization was executed while
preparing it. The full completed review is
`2026-11-14-actual-reciprocal-mobius-contact-decomposition-903.md`,
including exact source statements, access limits and duplicate comparison.
Its SOURCE_BLOCKED decision applies to the broad signed-contact target,
not to the standard normalization diagnostic explicitly isolated here.

Use C466a's displayed h(s) and form the proposed finite-head transform by
replacing its reciprocal-zeta factor by

    M_2(s)=1-2^(-1/2-sqrt(s)).

Keep the complete reciprocal prefactor from that same formula, including
2c_0, the pi power, (s-1/4)^(-1) and reciprocal Gamma. Call this explicit
candidate transform G_2(s). This defines the object to test, not an
assertion that it is a positive or finite-mass transform. Preserve the
principal branch and every normalization factor.

The bounded mathematical task is to justify a real inverse g_2 on a
vertical line Re(s)=1 using sectorial gamma decay, inspect the exact
behavior at s=1/4, and, if justified, move only this finite-head contour
to Re(s)=1/8 with the complete residue and horizontal-edge estimates.
Then test whether the exact remainder r_2=p-g_2 could satisfy

    |r_2(x)| = o(|g_2(x)|) as x tends to infinity.

Zeros of g_2 must be handled in stating that comparison; a proved
eventual nonzero leading term would suffice. C466a gives p>=0 and
integral p=1. Do not silently assume an unproved pointwise decay rate
for p or require a new zeta zero-free region. If an eventual relative
estimate is incompatible with these mass/sign facts, record only that
conditional approximation obstruction. If the required inverse/contour
estimates fail, preserve the first failed hypothesis and stop; do not
claim a residue asymptotic from a pole alone.

The sources inspected in904 cover the required ordinary tools:
[DLMF27.4.5](https://dlmf.nist.gov/27.4#E5),
[25.2(i)](https://dlmf.nist.gov/25.2#i),
[1.14.3](https://dlmf.nist.gov/1.14#E3),
[1.14.20](https://dlmf.nist.gov/1.14#E20),
[5.11.1](https://dlmf.nist.gov/5.11#E1) and
[5.11(ii)](https://dlmf.nist.gov/5.11#ii).
Fourier inversion plus proved weighted integrability is an alternative
to imposing unjustified separated-density hypotheses. Cauchy's residue
theorem requires analyticity off the specified singularities and control
of the whole truncating rectangle. No theorem about the infinite
arithmetic tail is asserted by these references.

This is a routine specialization/obstruction test, not a creative new
RH mechanism. Its possible downstream use is to determine whether an
arithmetic contact certificate must keep head and tail jointly or work
on a bounded x-window. It neither rules out compact derivative bounds
through 2m-1 nor establishes their contact-weighted utility. Even a
successful global diagnostic leaves C466b(7), hypothetical contacts at
all orders, simultaneous contacts, propagation and L030 assembly open.
Do not grow the head, search parameters, infer global PF, or restart the
blocked Polson comparison during this test. A short obstruction record
is sufficient; no new lemma is required merely to label the outcome.
Matching Mathlib coverage is unchecked. No cross-notebook input is used.
