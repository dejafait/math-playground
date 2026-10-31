# Actual-theta Fourier determinants — completed residual comparison

TARGET: Assess whether Sra's order-four Fourier determinant inequalities give −(F²)''/8 >= −F'²/2 for F=2Xi at every real argument, or a concrete weaker bound with a stated missing remainder.
CHECKED: 2026-10-31
DECISION: EXPLORE
SEARCH_EVIDENCE: Exact Fourier-determinant, pointwise-Laguerre, reverse-regularity and residual searches located the primary v1 and its explicit limitation; local searches found L233, the September associated-kernel assessment and L055/C055a, but no prior assessment of this theorem's residual interface. Queries and comparison below; no novelty inference.
SOURCE_EVIDENCE: Suvrit Sra, Sharp order-four sign regularity of a Jacobi theta kernel, v1, 10 October 2026, https://suvrit.github.io/papers/csordas/csordas-v1.pdf ; (1.1), (1.8)–(1.10), Theorems 1.1 and 1.4, Assumption 1.5 and Limitations, printed pp. 1–4; Lemma 2.2 and Section 3's tail, compact and fifth-order cases, pp. 5–9; complete Section 4.3, pp. 10–11. No verifier replay or independent manuscript audit.
COMPARISON: Theorem 1.4 restates square-root-theta Wronskian signs as integrated Fourier determinants. It supplies neither a pointwise frequency inequality nor a signed remainder bound for L233; the source explicitly withholds the first global Laguerre sign. No admissible residual specialization was found.
GAP: A new localization or transfer estimate must control the residual at each real frequency, including zeros of F'; no compensating remainder or uniform localization estimate is supplied by the inspected theorem. Higher signs remain independent.
REASON: Park direct use as a pointwise D_1 certificate. EXPLORE records completed source comparison, not approval of an unspecified mathematical bridge or a theorem that every possible bridge fails.
SCOPE: Literature only. No lemma import, new derivation, script, verifier run or generic preservation claim. A mathematical continuation requires a specified and assessed mechanism.
LITERATURE_REASON: The supplied REVIEW_REQUIRED target had essential unread trust hypotheses, Fourier proof and residual applicability. Existing associated-kernel coverage was reused unchanged.

## Exact question and local overlap

The main gap remains all-degree actual-Xi mixed positivity. The narrower
source target could support the first sign while leaving higher signs
and all-degree positivity unresolved. The continuation test required an
admissible signed specialization or useful weaker bound with explicit
remainder; none was found.

Read L233 in full, L018 and L019–L020's actual-kernel formulas. L233
already gives, for F=2Xi,

\[
 \widehat A(2x)=\frac{F'(x)^2-F(x)F''(x)}4
 =\frac{F'(x)^2}2-\frac{(F(x)^2)''}8.
\]

This is reused, not derived here. The required residual threshold is the
TARGET above, including where the positive summand vanishes.

Reused [the associated-theta assessment](2026-09-27-first-associated-theta-lattice.md)
and [the signed-Xi comparison](2026-10-31-family003-signed-xi-bridge-scope.md).
Read L055 and C055a's statement/source application. Their comparison
kernels have nonreal Fourier zeros despite square-root and second-level
concavity. They do not assert RR4, a negative D_1 value, or an obstruction
for actual theta. L057's finite reciprocal-node Hankel tests concern a
different matrix. No new audit of those results is claimed. The
[positive-kernel failure](../../ATTEMPTS/2026-09-09-positive-theta-kernel-inference.md)
and [theta relevance audit](../../ATTEMPTS/2026-09-20-theta-logarithm-relevance-audit.md)
retain their scopes; neither globally bans theta-sensitive mechanisms.

## Primary theorem and proof interface

Source: Suvrit Sra, *Sharp order-four sign regularity of a Jacobi theta
kernel*, v1, 10 October 2026,
[primary PDF](https://suvrit.github.io/papers/csordas/csordas-v1.pdf).

Assumption 1.5 assumes correctness of Python integers, SymPy exact
polynomial operations and mpmath.iv outward intervals. Checks use 90
decimal digits, exact factorials and rational endpoints; overlap is
checked exactly. Theorem 1.1 combines analytic tails and compact checks.
These computations were not replayed.

The source defines s(t)=Phi(sqrt(t)), Xi_Phi(lambda)=Xi(lambda/2)/4,
epsilon_m=(-1)^(m(m-1)/2), and
Theta_j(r,lambda)=((2r)^(-1) partial_r)^j cos(r lambda).
Under Assumption 1.5, Theorem 1.4 asserts, for r>0 and m=1,2,3,4,

\[
 \epsilon_m\int_{(0,\infty)^m}\prod_{\ell=1}^m\Xi_\Phi(\lambda_\ell)
 \det[\Theta_{i+j-2}(r,\lambda_j)]_{i,j=1}^m\,d\lambda>0.
\]

Section 4.3 identifies the integral as pi^m times W_m of s at r^2. Schwartz
decay and polynomial kernel growth justify differentiation and Fubini
at fixed r>0; Theorem 1.1 supplies the signs. The fifth-order exception
uses its t=10^(-2) witness. The Limitations paragraph explicitly
withholds the global first Laguerre sign.

Reading limits: inspected the complete Fourier proof and displayed
quadratic kernel, and the tail, near-zero Taylor, away-from-zero
interval, overlap and fifth-order proof cases. This identifies source
hypotheses; it is not an independent computational audit. Upstream
Csordas–Varga/Karlin proofs and verifier code were not audited.

## Applicability and exact mismatch

L019's k(u)=4Phi(u/2), already recorded in the September assessment,
and L233's F=2Xi keep the normalizations distinct. No normalization
change repairs the following mismatch.

**Inference from the inspected statements:** r is a spatial evaluation
parameter, whereas the lambda_j are integrated frequencies. The theorem
permits choosing r and m. It does not permit inserting an arbitrary
frequency test function or diagonal localization while retaining its
sign. Its quartic constraint integrates four Xi values; L233 requires
a quadratic jet at one specified frequency. Even m=2 is an integrated,
oscillatory constraint. A new operation would need a signed justification;
fixed-r absolute convergence supplies no uniform localization estimate.

This is a statement comparison, not a no-go theorem. No useful weaker
bound with a compensating signed remainder was found. The achieved
threshold is unchanged: this source supplies no bound reaching −F'^2/2.
No negative actual-Xi sign is established. The fifth-order witness is
not a failure of the mixed forms, and the paper cautions against
transferring it even to its coefficient transform. A different transform
could still help. Rerunning the certificate or importing a coefficient
corollary would not resolve this interface.

## Search, decision and different lead

Queries included `site:suvrit.github.io/papers/csordas "Theorem 1.4"`,
`"Sharp order-four sign regularity" theta`,
`"Fourier determinant" "theta" "Sra"`,
`"Sra" "Fourier-side determinant inequalities"`,
`"Sharp order-four" "pointwise Laguerre"`,
`"reverse regular" "Laguerre" theta Fourier inequalities`,
`"theta kernel" "quartic" "residual"`, and
`"Riemann Xi" "first Laguerre" "2026"`.
Local searches covered exact title/order-four/Fourier-determinant terms
in drafts/literature, ATTEMPTS, foundations and relevant history. The
PDF became accessible through its author-page link after an initial
browser error; shell DNS and GitHub access failures did not block the
essential source. Snippets and expositions were not theorem evidence.
No exhaustive search or novelty claim is made.

Outcome: NEGATIVE source evidence changes routing, with no mathematical
advance beyond the inspected source. Park direct transfer, not every
possible theta mechanism. Mathematical exploration usage is unchanged.

The search located an **unread lead** in Min–Kang's square-variable work:
*A Lorentz–Laguerre Transport Equation for the Square-Variable Riemann Xi
Function* (27 September 2026), linked from their
[complex-Laguerre abstract](https://www.alphaxiv.org/abs/2609.complex-laguerre-positivity-riemann-xi).
Only that abstract page was read for nomination. Its advertised
half-plane is not an all-height real-frequency D_1 theorem. The transport
statement, forcing, domain, boundary data and coordinate correction
remain unread. No transport identity or applicability is asserted.
A narrow local title/author/square-variable search found only an older
explicitly unread half-plane lead in the October 5 Gaussian-response
assessment. This does not establish absence of all overlap; the separate
REVIEW_REQUIRED nomination requires exact failure checks.

Transport with full forcing is a different source mechanism from finite
reverse regularity. No creative calculation is justified until its
interface is specified and assessed. No lemma, script, canonical argument
change, Mathlib coverage claim, cross-notebook input or RH candidate
was produced.
