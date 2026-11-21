# Fixed Gaussian multiplier — unshifted coefficient-budget test

TARGET: Determine whether one fixed Gaussian multiplier exp(-a z^2), a>0 independent of degree, can satisfy O'Sullivan's Turan coefficient budget for every unshifted degree with the actual gamma_j.
CHECKED: 2026-11-04
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the October31 actual-Hermite signed-cross-term review and step379's Jensen source search; read the new product-criterion interface and full relevant sufficient-budget application. Narrow primitive/Jensen searches found no prior exact fixed-Gaussian all-degree budget test; this is no novelty claim.
SOURCE_EVIDENCE: C. O'Sullivan, arXiv:2007.13582v2(9December2020), https://arxiv.org/html/2007.13582v2 , (1.2)–(1.4), Theorem3.5 with proof/(3.3)–(3.6), Theorem8.1/(8.1)–(8.5); exact source comparison in 2026-10-31-actual-hermite-signed-cross-term-review.md reused. Theorem8.1 is the precise restatement of Turan1959 TheoremIII; original not independently audited.
COMPARISON: A known sufficient criterion covers the proposed test, while its all-degree unshifted applicability for a fixed multiplier has not been established here. Only real scaling and actual coefficient substitution are authorized; failure of the budget would not imply failure of hyperbolicity.
GAP: Verify the parameter/basis normalization and determine whether the strict sufficient budget can hold for all d>=2 at n=0. No signs, primitive margins, or degree-dependent multiplier equivalence are granted.
REASON: This independently testable coefficient-budget mechanism needs no input Jensen root signs and avoids the parked primitive constant selection. It is a known-method specialization, not a creative proof mechanism or a claimed new convergence theorem. New ready continuation awaits the supervisor's separate approval before research.
SCOPE: Actual gamma_j=j!M_(2j)/(2j)! from L021/L028, with L018 fixing xi normalization; n=0, integer d>=2, one real a>0 fixed across degrees. Exact finite algebra and analytic bounds only; no computed-zero premise or raw-moment replacement.
LITERATURE_REASON: Changed from prescribed antiderivative signs to a fixed-multiplier sufficient coefficient test; the required product theorem and coefficient application were inspected in the same source review, with prior budget coverage reused.

## Source interface

O'Sullivan's Theorem3.5 assumes a real entire Phi of genus1* and
an LP multiplier Omega; its all-degree product-Jensen test is an
equivalence. Here Phi=Theta and Omega=exp(-a z^2), with one fixed a>0.
His Theorem8.1 states that G=sum c_k H_k has simple real zeros if

    sum_(k=0)^(d-2) 2^k k! c_k^2 < 2^d (d-1)! c_d^2.

For a=1, the application is precisely (8.2), not an inferred necessary
condition. The source uses physicists' Hermite polynomials. Check the
positive-parameter change of variables before invoking this budget.

The proposed family is defined, without a claimed estimate, by

    Q_d^(a)(X) = g_d^*(Theta(z) exp(-a z^2); X),
    Theta(z) = sum_(j>=0) gamma_j z^j/j!,
    g_d^*(F;X) = sum_(j=0)^d binom(d,j) F^(j)(0) X^(d-j).

This keeps the actual low coefficients and a single entire product.
The research difference is only testing the known sufficient budget,
including all its nonnegative summands, after the exact scaling. Do not
reprove the criterion, infer a primitive theorem, or assume actual input
hyperbolicity. Do not import the source's large-n coefficient estimates
at n=0. Its product proof and application (8.2)–(8.5) were inspected;
original Turan1959 proof coverage is not claimed.

## Relevance and bounded decision

Main gap remains all-degree actual-Xi signs. A uniform successful
sufficient budget could supply a direct all-degree real-rootedness
mechanism without shift descent. The test asks about this method's
feasibility before attempting detailed theta root estimates.

Continue only with an exact, justified bound strictly below the
criterion's threshold in every degree for one fixed a. Stop this
sufficient method if a retained positive summand forces failure for
arbitrarily large degrees for every fixed a; record a symbolic threshold
in terms of a and actual positive coefficients if available. Such a
failure is a method obstruction, not a nonreal Xi zero. If neither
alternative is established in one bounded attempt, preserve the partial
normalization and state the precise undecided inequality. Changing a
with degree would be a different target requiring review of its
all-degree implication.

This nomination contains no calculation, new bound, or source-theorem
reproof. It is proposed for calculation/standard/high after separate
approval. There is no justified creative theta-margin mechanism yet:
the parked source review found a sign criterion, not independent theta
control. L030/C032a are downstream criteria, L738 is a contrast, and
neither is a positivity premise. Mathlib coverage is not checked.
