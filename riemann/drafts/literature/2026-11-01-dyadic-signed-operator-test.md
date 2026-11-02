# Dyadic signed operator test: completed source comparison

TARGET: Test whether L622's full six-term signed matrix restricted to n=2^j<=floor(T^(1/100)) has a positive spectral lower bound independent of T, uniformly in X and the common real unit observer, by controlling the summed shift deformation in operator norm.
CHECKED: 2026-11-01
DECISION: EXPLORE
SEARCH_EVIDENCE: Completed bounded exact/stronger-result searches for dyadic twisted-fourth-moment positivity, signed Hardy arithmetic forms, prime-power/GCD spectra and finite Toeplitz bounds; queries and inspected scopes below. Reused collective arithmetic coverage and checked the local row/freezing/congruence stops. No matching full signed dyadic lower bound was identified in the checked sources; no novelty claim.
SOURCE_EVIDENCE: Newly read Robert M. Gray's author-hosted Toeplitz and Circulant Matrices: A review, https://ee.stanford.edu/~gray/toeplitz.pdf, Lemma 2.1/(2.2)–(2.7), pp. 12–13, norm definitions pp. 15–18, Section 4.1/(4.3)–(4.8), pp. 38–40, and Lemma 4.1/(4.11)–(4.16), pp. 41–43, including both proof cases. Reopened Hughes–Young arXiv:0709.2345v2 (13)–(17)/Theorem 1.1 and p. 5 holomorphy remark; reuse the previously inspected Lemma 6.9/(139)–(155) and stronger-source comparison. Rechecked BBLR arXiv:1609.02539v1 Theorem 1.1 hypotheses; details below.
COMPARISON: Finite Hermitian Toeplitz eigenvalue bounds are known, but the exact signed block's suitable symbol/reference and uniform summed deformation are not supplied by those theorems. The moment imports determine the full six-term expression without asserting its signed positivity. L623's reference Gram bound and relative-freezing obstruction, L621's two-frequency case and L622's fixed block do not settle the growing chain.
GAP: Prove a coefficient-uniform dyadic operator comparison retaining the complete six-term collision sum, exact phase and every Q V_c derivative, then obtain a strictly positive uniform spectral margin exceeding L622 (1). Justifying the reference symbol and its lower bound, the summable deformation and uniformity in X,c are mathematical obligations, not established by this review.
REASON: Adequate arithmetic and finite spectral toolkit coverage permits one bounded attempt on the unchanged target. The operator norm may test something the failed relative-entrywise comparison did not; no small norm, symbol positivity or signed conclusion is asserted. No essential unread source blocks the attempt, and no further general browsing is required without a changed hypothesis or specific lead.
LITERATURE_REASON: The invocation-start nomination was REVIEW_REQUIRED for a growing dyadic chain and summed operator control; existing arithmetic coverage did not assess this spectral specialization. This turn fills that scope gap rather than refreshing ready transfer coverage.
SCOPE: The fixed w, T<=X<=2T, N=floor(T^(1/100)), arbitrary unit complex a supported on {2^j: j>=0, 2^j<=N}, single real unit c and exact K_c of L622; no enlarged observer, altered window, numerical onset or all-prime spectral conclusion.

## Completed comparison — 1 November 2026

One LITERATURE / NOVELTY_UNCHECKED source review, outcome EXPLORATION.
This authorizes a bounded mathematical attempt, not a spectral conclusion.
No lemma, mathematical script, DAG edge or proof overview was changed.
The nomination below is preserved as historical planning; this completed
comparison supersedes its pending-review language.

### Newly inspected finite spectral input

Robert M. Gray, *Toeplitz and Circulant Matrices: A review*,
[author-hosted 98-page draft](https://ee.stanford.edu/~gray/toeplitz.pdf),
retrieved 1 November 2026: Lemma 2.1, printed pp. 12–13, gives the
Rayleigh extrema for finite complex Hermitian matrices. Section 4.1,
(4.3)–(4.8), pp. 38–40, uses absolutely summable two-sided coefficients
and their Fourier symbol. Lemma 4.1, (4.11)–(4.16), pp. 41–43, bounds
every eigenvalue of a Hermitian finite section between the symbol's
essential infimum and supremum. Its complete proof was read: Fourier
quadratic form, Parseval normalization, Rayleigh extrema, then the
separate real/imaginary-part argument for a non-Hermitian norm bound.
The published bibliographic counterpart is *Foundations and Trends in
Communications and Information Theory* 2(3) (2006), 155–239,
[DOI 10.1561/0100000006](https://doi.org/10.1561/0100000006);
page numbers above refer only to the inspected draft.

The strong operator norm and dimension-normalized Hilbert–Schmidt norm
are distinguished in (2.13)–(2.22), pp. 15–18. Theorem 2.4, p. 23,
concerns averaged eigenvalue distributions under asymptotic equivalence;
it does not replace the required finite minimum-eigenvalue estimate.

These are cited tools, not results to reprove. Their hypotheses must
be checked in a later application. No symbol, Fourier sum, tail bound,
norm limit or lower margin for the notebook matrix was computed here.
In particular, a symbol for the zero-shift reference would not itself
identify the exact shifted signed block. If a T-dependent symbol is
used, uniformity must be proved rather than inferred from a theorem
about a single fixed symbol.

### Arithmetic coverage reused, with exact scope

Reuse [the completed collective arithmetic comparison](2026-11-01-collective-arithmetic-signed-spectrum.md)
and [the L622 transfer assessment](2026-11-01-l622-uniform-transfer-audit.md).
The audited application is L622 (1), Sections 1–4, under named imports;
its Section 5 and L623's full Gram proof remain outside that audit.

C. P. Hughes and M. P. Young, *The twisted fourth moment of the Riemann
zeta function*, J. reine angew. Math. 641 (2010), 203–236,
[arXiv:0709.2345v2, Theorem 1.1/(13)–(17), printed pp. 4–5](https://arxiv.org/pdf/0709.2345v2#page=4),
was reopened for both prime-power orientations and the exact theorem.
It requires coprime h,k, hk<=T^(2/11-epsilon), complex shifts O(1/log T),
a smooth nonnegative weight supported in [T/2,4T], all-fixed-order
derivative bounds O_j(T0^(-j)), and T^(1/2+epsilon)<<T0<<T.
Its six-term main integral carries (hk)^(-1/2); the error is
O(T^(3/4+epsilon)(hk)^(7/8)(T/T0)^(9/4)). The p. 5 remark imports
complete-sum holomorphy from CFKRS Lemma 2.5.1. Reuse the already
inspected Lemma 6.9/(139)–(155), pp. 22–24, for general prime powers;
no manuscript-proof audit is claimed. L622's audit covers the actual
complex phase weight, shift differentiation and coefficient sum in
the permitted range. Restriction of its coefficient family is the
proposed application, with the exact signed expression retained.

S. Bettin, H. M. Bui, X. Li and M. Radziwill, *A quadratic divisor
problem and moments of the Riemann zeta-function*,
[arXiv:1609.02539v1, Theorems 1.1–1.2 and remarks, pp. 2–4](https://arxiv.org/pdf/1609.02539v1#page=2),
is the stronger-length comparison already assessed. Theorem 1.1's
small shifts, smooth [1,2] weight, length exponent <1/4 and coefficient
growth conditions were rechecked. Neither it nor its six-term variant
asserts this signed spectral margin; the normalization issue for
arbitrary unit coefficients remains as recorded in the reused review.
No stronger transfer is needed here.

The same assessment has inspected paper 36 v4 Theorem 6/Section 7's
untwisted derivative-filter forms and paper 41 v4 Theorems 2–2a's
positive Laguerre-order/log-height regime. Those scopes do not cover
fixed first order with this arbitrary growing arithmetic square.
Likewise the inspected Bui–Hall and Bui–Hall–Subira Jorge amplifier
results specify different coefficient families/fourth powers. These
are reused theorem comparisons, not fresh readings or new exclusions.
A current direct web retrieval of paper 36/v4 returned an internal
error; the completed version-specific assessment is still adequate,
so that access failure creates no essential source blocker.

### Bounded discovery and local duplicate/failure comparison

Queries on 1 November 2026 included `"zeta" "twisted fourth moment"
"Laguerre" positivity`, `"twisted fourth moment" "prime powers"
positivity matrix`, `"twisted fourth moment" "positive definite"`,
`"Hardy" "signed" "dyadic" zeta moment`, `"twisted fourth moment"
"dyadic" positivity`, `"zeta" "GCD matrices" prime powers positivity
derivatives`, and finite Toeplitz/Hermitian symbol searches. No checked
theorem settles the exact target. General GCD-norm papers and recent
singular-symbol eigenvalue papers appeared as leads; their theorems
were not inspected or imported. No claim about their precise coverage,
nor novelty or exhaustive literature absence, follows from the search.
They are not needed to attempt the finite spectral toolkit above.

The relevant local paths were L622's definition and audit, L623's
conclusion/Section 1, L624 Section 4, the collective Gram working note
and history, and the row/freezing/divisor-prefix stop records. L623's
prime-power autocorrelation remains an applicability calculation to
verify if used; this review does not certify its unaudited full lemma.
The first-row dominance failure and relative local-factor freezing
failure are preserved in their ATTEMPTS records. L624 stops an o(1)
shifted-prefix claim in inverse-divisor coordinates, not an estimate
of the present signed dyadic operator. The parked L625 physical
Mobius scalar and boundary-cost tests are not repeated. No completed
matching operator comparison was found in these checked local paths.

### Authorized continuation and decisive test

Keep TARGET exactly as saved above. The mathematical attempt may
check a candidate reference's hypotheses and normalization, apply the
cited finite spectral bounds, and estimate the complete shifted
deformation in the original coefficient norm. It must preserve both
orientations, square-root twist weights, all six collision terms,
the exact phase and all Q V_c derivatives. No separate singular term
may be evaluated at a collision. Any justification for a limit or a
sum must be uniform over the allowed growing chain and X,c.

Success requires an explicit positive asymptotic lower margin d_w>0
for the exact dyadic restriction, exceeding L622 (1)'s vanishing
absolute transfer error. A reference margin without a comparison is
inconclusive. An uncontrollable signed derivative or a concrete norm
defect preventing this comparison stops this mechanism; neither is
evidence of a negative eigenvalue. Floating spectra, relative uniform
freezing and weak-norm spectral distribution do not pass the test.

Essential continuation inputs are those in the preserved nomination:
L622 (1)/(3)–(12), L619(H=T), L465, L471 (7), L018, and L623 Section 1
only after its applicability check. The actual signed spectrum, a
quantitative margin, all-prime interactions, effective onset and
pointwise initial signs remain unproved. Matching Mathlib coverage
was not checked. No cross-notebook input is used.

EXPLORE permits a mathematical attempt, with its result honestly
classified then. The expected work is a specialization/development of
known moment and finite-section tools, not a protected creative claim.
Quantitative control of cross-prime signed interactions remains the
blocker to justifying a new central creative mechanism. Separate
source approval is completed in this turn; unchanged continuation
coverage need not be rewritten or browsed again next turn.

## Historical nomination: proposed discriminating test and its limits

Keep the calculation above as the target while assessing its source
coverage. Reuse the approved arithmetic imports and the completed
L622 application audit. Review primary statements about finite Toeplitz
quadratic forms and symbols only as needed, and search for a matching
stronger signed moment or prime-power comparison. Do not infer coverage
from the name of a theorem or from a numerical matrix. The exact
Toeplitz representation, if useful, must itself be justified later.

The proposed new feature is to estimate the summed absolute deformation
as an operator, taking the square-root twist weights into account.
The relative local-factor counterexample of L623 is retained. It does
not by itself answer whether this different norm is small. No norm
bound, symbol formula, derivative estimate or positivity result is
derived in this nomination, and an entrywise relative o(1) assertion
would simply repeat the stopped mechanism.

For the later mathematical attempt, success would mean a proof of
lambda_min(K_c restricted to the dyadic indices)>=d_w>0 beyond one
onset, uniformly in X,c, with all omitted costs controlled. This would
exceed L622 (1)'s vanishing absolute error and stop this restricted
sign-witness family. A concrete nonvanishing operator defect that
prevents the proposed comparison, or a failure to control the complete
signed derivatives, must be recorded as such; it would not prove a
negative eigenvalue. A floating enlargement or a change to the
zero-shift reference alone does not pass the test.

Essential later inputs are L622 (1)/(3)–(12), L619(H=T)'s complex
germ and absolute estimates, L465's analytic phase and curvature,
L471 (7), and actual Xi as in L018. L623 Section 1's prime-power
autocorrelation is a proposed reference calculation that still needs
its own applicability check; its unaudited full Gram argument is not
silently certified by the L622 audit. The arithmetic and holomorphy
manuscripts remain named imports. No cross-notebook result is used;
full matching Mathlib coverage is unknown.

A positive dyadic answer would give a controlled local spectral test
despite persistent relative deformation, potentially useful when
seeking an all-prime form bound. Interactions between distinct primes,
the full coefficient family, pointwise initial signs, exceptional
heights and all-degree mixed positivity would remain unresolved.
The absence of a quantitative mechanism for those interactions blocks
a justified central creative claim here. The later proof's routing
must reflect the actual source comparison; this restricted diagnostic
is not relabeled creative merely to satisfy a scheduling preference.
