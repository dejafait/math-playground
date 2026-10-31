# Common-pole generic increment: bounded mathematical continuation

TARGET: Test the common-pole generic increment Gamma_p on L526's two packets against -2p^(-1/2)log p, first justifying the compression identification and both separate finite smoothed traces.
CHECKED: 2026-10-30
DECISION: EXPLORE
SEARCH_EVIDENCE: Reuse the completed exact-target source comparison 2026-10-30-common-pole-generic-increment-coverage.md, including its exact/terminology queries, known-result comparison and narrow duplicate/failure screen. It found no inspected matching increment theorem; novelty is not established.
SOURCE_EVIDENCE: https://rstation.ai/problems/riemann_hypothesis/papers/2 , bramble_trace paper 2 v2 (16 October 2026), Section 1, Lemma 4.1 and proof (4.1)--(4.4), (5.2)--(5.3), (6.1)--(6.2), Theorem 6.2 generic coefficient and Theorem 7.1 with proof; https://www.ams.org/tran/1969-144-00/S0002-9947-1969-0251519-5/S0002-9947-1969-0251519-5.pdf , Halmos (1969), p.381 and Theorem 2 pp.384--385 with proof; https://jordanbell.info/LaTeX/mathematics/traceclass/ , Theorems 18/23 reused from the L526 coverage review.
COMPARISON: Projection geometry and weighted Hardy trace tools are available by citation. Their exact reflected-symbol application remains to be justified; the fixed-test uncorrected generic coefficient and fixed-cutoff corrected perturbation do not determine this moving-family increment. L526 settles only the Sonin component.
GAP: Obtain a signed asymptotic or a discriminating bound for Gamma_p/(rL), or a specific domain obstruction, after separately establishing both localized traces; individual asymptotic errors cannot be canceled without a direct difference proof.
REASON: This complementary observable can test whether a local generic contribution supplies the arithmetic decrement missing from Sonin-only absorption. A favorable result would only nominate a collective comparison; it would not resolve its independent gaps or RH.
SCOPE: One bounded proof attempt for exactly the definitions and threshold below, after separate next-invocation approval of this newly written assessment. No estimate or new lemma was derived during its literature preparation. Import the standard tools rather than reprove them.

The full completed source comparison, hypotheses, proof cases and
qualifications are in `2026-10-30-common-pole-generic-increment-coverage.md`.
Essential local input: L526, with its retained unaudited-source
qualifications, exact normalized h, L=log p, r=p^(-1/2), common
M=L+2, centered f_p and actual predecessor/successor P_-/P_+.
Use its Fourier measure and corrected involution convention.

Let Pi be the physical positive-half-line projection, J_(P,M)
the corrected involution, and S_(P,M) the physical Sonin projection.
The proposed definitions, requiring verification, are

    C_(P,M)=Pi J_(P,M) Pi J_(P,M) Pi-S_(P,M),
    Q_(P,M)(f_p)=Tr(T_(f_p) C_(P,M) T_(f_p)^*),
    Gamma_p=Q_(P_+,M)(f_p)-Q_(P_-,M)(f_p).

First identify the intersection and generic compression using
Halmos's full decomposition; do not assume generic position on
the entire space. Then transport the positive compression to
the source's localized Hardy block, including Fourier reflection,
the correct symbol/test, derivative bounds and boundary measure.
Use Lemma 4.1 only within those checked hypotheses to establish
separate finite traces; retain the sandwiched trace convention
and Bell's trace-class requirements. L526 supplies the separately
finite Sonin traces and their subleading difference, not a result
for C or Gamma_p. Positivity and the subtraction must be justified.

The creative test is a direct signed increment at scale rL,
possibly through an exact Hardy-kernel difference for the added
Euler factor while retaining the common pole phase. This is a
proposed technique, not an asserted formula. Check all prime
powers and endpoints against L526's exact arithmetic benchmark
-2rL. Uniformity for this moving family is a proof obligation.
Do not substitute fixed-test asymptotics, neglect inverse Gram
factors if introduced, or subtract unlocalized infinite traces.

Continue a local-absorption route only on a rigorous negative
leading contribution of magnitude at least 2rL, with an error
small enough to decide the signed comparison. A contrary signed
asymptotic, a proved subleading increment, or an explicit domain
obstruction is informative negative evidence. A formula without
a scale estimate or an absolute O(1) bound does not decide the
test; preserve unfinished reasoning and reassess rather than
declare success or repeat the same mechanism without new input.

Remaining gaps: negative overlap and off-diagonal remainder,
missing visible primes, full-Weil identification, actual
nullvector and trace/nonresonance premises, family rates, collars
and Xi transfer. Any downstream L515/L516/L521/L522 application
retains both shifts, equality atoms, signed pole, nu_rho,
c=log(2pi), 0<a<A and ell=2a>log 2. No H1, simplicity, trace
vanishing or positivity is granted. Mathlib matching coverage is
unchecked; no cross-notebook input. A favorable auxiliary result
would leave STATUS IN_PROGRESS.
